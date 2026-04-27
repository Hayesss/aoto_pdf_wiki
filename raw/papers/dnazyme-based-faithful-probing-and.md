---
source_path: /mnt/c/Users/Administrator/Zotero/storage/7SSE3S2R/Hu 等 - 2024 - DNAzyme-based faithful probing and pulldown to identify candidate biomarkers of low abundance.pdf
ingested: 2026-04-23
sha256: 6c1d57f84a4125d0
---

nature chemistry
Article https://doi.org/10.1038/s41557-023-01328-5
DNAzyme-based faithful probing and
pulldown to identify candidate biomarkers
of low abundance
Received: 22 December 2022 Qinqin Hu 1,2,7, Zongxuan Tong1,7, Ayimukedisi Yalikong 1,7, Li-Ping Ge 1,7,
Qiang Shi1, Xinyu Du1, Pu Wang 1, Xi-Yu Liu1, Wuqiang Zhan1, Xia Gao 1,
Accepted: 17 August 2023
Di Sun1, Tong Fu1, Dan Ye1, Chunhai Fan 2,3,4,5, Jie Liu6, Yun-Shi Zhong 1 ,
Published online: 14 September 2023 Yi-Zhou Jiang 1 & Hongzhou Gu 1,2
Check for updates
Biomarker discovery is essential for the understanding, diagnosis,
targeted therapy and prognosis assessment of malignant diseases.
However, it remains a huge challenge due to the lack of sensitive methods
to identify disease-specific rare molecules. Here we present MORAC,
molecular recognition based on affinity and catalysis, which enables the
effective identification of candidate biomarkers with low abundance.
MORAC relies on a class of DNAzymes, each cleaving a sole RNA linkage
embedded in their DNA chain upon specifically sensing a complex system
with no prior knowledge of the system’s molecular content. We show that
signal amplification from catalysis ensures the DNAzymes high sensitivity
(for target probing); meanwhile, a simple RNA-to-DNA mutation can shut
down their RNA cleavage ability and turn them into a pure affinity tool
(for target pulldown). Using MORAC, we identify previously unknown,
low-abundance candidate biomarkers with clear clinical value, including
apolipoprotein L6 in breast cancer and seryl-tRNA synthetase 1 in polyps
preceding colon cancer.
Biomarkers are informative molecules, particles and even cells that dif- differentially expressed in disease2–4. However, the subsequent pri-
fer quantitatively or qualitatively between healthy and at-risk individu- oritization and validation of candidate biomarkers require lots of
als1. Identification of biomarkers is thus particularly critical to disease bioinformatics-based data analysis and time-consuming antibody
diagnosis and treatment, yet the rarity of biomarkers, especially in the development; the rigorous sample preparation process of MS also
early stages of disease, makes their discovery extremely challenging. disfavours low-abundance proteins (those present in biological fluids
Traditional mass spectrometry (MS)-based techniques repre- with levels lower than 1–5 μg ml–1)5,6, which are believed to contain
sented by proteomics can generate lists of protein targets that are lots of potential biomarkers. Conventional affinity-based molecular
1Key Laboratory of Breast Cancer in Shanghai, Department of Breast Surgery, Institutes of Biomedical Sciences, Fudan University Shanghai Cancer
Center, Shanghai Stomatological Hospital, and Endoscopy Center, Zhongshan Hospital, Fudan University, Shanghai, China. 2Department of Chemical
Biology, School of Chemistry and Chemical Engineering, and School of Global Health, Shanghai Jiao Tong University, Shanghai, China. 3Institute of
Molecular Medicine, Shanghai Key Laboratory for Nucleic Acids Chemistry and Nanomedicine, Renji Hospital, School of Medicine, Shanghai Jiao Tong
University, Shanghai, China. 4New Cornerstone Science Laboratory, Frontiers Science Center for Transformative Molecules and National Center for
Translational Medicine, Shanghai Jiao Tong University, Shanghai, China. 5Zhangjiang Laboratory, Shanghai, China. 6Department of Digestive Disease,
Huashan Hospital, Fudan University, Shanghai, China. 7These authors contributed equally: Qinqin Hu, Zongxuan Tong, Ayimukedisi Yalikong, Li-Ping Ge.
e-mail: zhong.yunshi@zs-hospital.sh.cn; yizhoujiang@fudan.edu.cn; hongzhou.gu@fudan.edu.cn
Nature Chemistry | Volume 16 | January 2024 | 122–131 122
Article https://doi.org/10.1038/s41557-023-01328-5
a
DNAzyme library Normal sample Triggered RNA cleavage
5‘ rA 5‘ rA in series
No Signal
reaction amplification
5‘ rA 5‘ rA
SELEX 5‘ rA
5‘ 5‘
5‘ rA 5‘ rA
rA rA
5‘ rA 5‘ rA
5‘ rA 5‘ rA Undefined
Disease sample molecule
b
F1 F2 F3 F4 F5 F6 F7 F8 F9 F10
Biochemical purification:
IEX, SEC and so on
Disease
sample
rA
Collect fractions 5‘ rA
F1 F2 F3 F4 F5 F6 F7 F8 F9 F10
Profiling
dPAGEgel
c
Inactivation: rA to A F5
5‘ Beads Identification
5‘ rA Affinity tool A A A (MS) and
experimental
conversion Conjugation Precipitation Elution validation
Fig. 1 | The DNAzyme-based MORAC technique for discovery of potential are incubated with the DNAzyme, and the induced cleavage signals are
biomarkers from disease samples. a, Overview of a selected DNAzyme to analysed by dPAGE to guide the collection of fractions that contain relatively
specifically sense a disease sample. Through subtractive/positive SELEX, a high levels of target molecule (high induction of DNAzyme cleavage). The step
DNAzyme is identified to self-cleave upon binding a target molecule (purple star) is pivotal to reduce the molecular complexity of the disease sample. c, Overview
present only in the disease sample, releasing the target molecule, which repeats of the DNAzyme-based pulldown of the target molecule from the prepurified
the process by binding another copy of the DNAzyme and yielding an amplified sample for identification. Through single-nucleotide RNA-to-DNA mutation
signal. rA, ribonucleotide adenosine embedded in the single-stranded DNAzyme at the cleavage site, the DNAzyme is converted to a pure affinity tool for
chain. b, Overview of the DNAzyme-based probing to facilitate biochemical antibody-like antigen precipitation and enrichment from the collected fractions
prepurification of the disease sample. The fractions purified by chromatography in b. A, deoxyribonucleotide adenosine.
recognition approaches use antibody7,8 or oligonucleotide9–11 librar- the system’s molecular contents (Fig. 1a). Through subtractive/posi-
ies to target complex biological systems for disease-specific antigen tive SELEX16–20, wherein a control system (for example, lysate from
identification. From in vivo targeting by a murine immune system (anti- normal cells) and a target system (for example, lysate from cancer
body–antigen)7 to in vitro targeting by cell-based systematic evolution cells) are used for subtractive selection and positive selection in each
of ligands by exponential enrichment (SELEX; aptamer–antigen)9–11, round, respectively (Supplementary Fig. 1a), a group of DNAzymes are
the operational complexity and cost of the latter are greatly reduced evolved to gain their enzymatic activity, that is, to cleave a lone RNA
compared to that of the former, but in most cases antigen identifica- linkage buried in their DNA chain only upon the recognition of certain
tion is still restricted to either membrane-bound or high-abundance identity-undefined molecules rising quantitatively or qualitatively in
proteins11,12, likely because of the inherent limitations of the solely the target system (as compared to the control). Molecular recognition
affinity-based recognition strategies. Recent advances in the develop- induces such a DNAzyme to cleave the RNA and thus disassemble itself,
ment of molecular probes made of catalytic DNAs (deoxyribozymes or releasing the target molecule to be recognized by the next copy of the
DNAzymes)13–15 provide an intriguing alternative way to target complex DNAzyme (Fig. 1a). Within a reasonable time frame, the same one target
systems (DNAzyme–antigen)16–20, yet this approach remains incom- molecule can trigger multiple copies of the DNAzyme to cleave the
plete due to the lack of effective means to identify the antigens that RNA, yielding an amplified signal that can be readily monitored. Such
are targeted by the DNAzyme probes. To overcome these problems, a catalytic mode thus ensures high sensitivity (a decent lower detec-
here we develop MORAC, a molecular recognition strategy based on tion limit, down to ~100 pM, according to the experimental results in
affinity and catalysis that enables the efficient identification of can- Figs. 2g and 4g) of the DNAzymes.
didate biomarkers in low abundance, regardless of whether they are MORAC then employs the DNAzymes as an efficient feedback
membrane bound or not. reporter to analyse samples separated by common biochemical frac-
tionation strategies, for example, ion-exchange chromatography
Results and discussion (IEX), size-exclusion chromatography (SEC) and so on, to prepurify
Overview of the DNAzyme-based MORAC for biomarker the sensed molecule from the target system (Fig. 1b). Depending on
discovery the system’s complexity, single or combinatorial biochemical puri-
MORAC starts with the in vitro selection of DNAzyme probes to selec- fication strategies can be used. The resulting fractions that contain
tively detect a complex biological system with no prior knowledge of the target molecule are identified via denaturing polyacrylamide gel
Nature Chemistry | Volume 16 | January 2024 | 122–131 123
Article https://doi.org/10.1038/s41557-023-01328-5
a b c
Time (h)
0 1
Dz04 + MDA-MB-231 CEM
Dz04 + MCF-10A CEM
e f g
Pulldown
M B A kDa
70
55
40 APOL6
35 MW, 38,104
25
electrophoresis (dPAGE) analysis of the induced DNAzyme cleavage by mammary epithelial cell lines, HMEC and MCF-10A, as the controls,
each fraction. High induction means high levels of the target molecule, and the well-established breast cancer cell line MDA-MB-231 as the
and the corresponding fractions are collected. Such prepurification target. These cells were cultured to collect the corresponding crude
is pivotal to reduce the noise signals from non-specific interactions extracellular mixture (CEM) but not cell lysate, because we think that
(for example, DNA-binding proteins) in the subsequent pulldown. the less-complex CEM would be more suitable as a target system to
MORAC ends up with the DNAzyme-based pulldown of the target initiate the proof-of-principle demonstration of MORAC. To reduce the
molecule for identification (Fig. 1c). Since the unique RNA linkage is impact from cell line differences (in terms of normal molecules), we
essential for cleavage, a simple single-nucleotide RNA-to-DNA muta- combined the CEMs of HMEC and MCF-10A for subtractive selection,
tion can completely silence the DNAzymes’ enzymatic activity but and used the CEM of MDA-MB-231 for positive selection (Supplemen-
still retain their molecular recognition ability. With biotinylation to tary Figs. 1a and 2). The starting sequence library was composed of
immobilize oligonucleotides on streptavidin magnetic beads, MORAC 109-mer oligos containing 50 random DNA nucleotides and a single
uses the inactivated DNAzymes as a pure affinity tool for antibody-like RNA adenosine (Supplementary Fig. 3a). As the selection went on,
antigen precipitation from the prepurified sample collections. The we tracked for each generation (G) the induced cleavage signal of the
enriched target molecule is then eluted (Supplementary Fig. 1b), con- sequence library by the target and the control CEMs, and took the G11
centrated, analysed and identified by MS, as well as validated experi- pool for sequence analysis since the signal difference (fraction cleaved
mentally. In short, MORAC flexibly exploits the affinity and catalysis of in positive selection over that in subtractive selection) seemed to reach
a subgroup of DNAzymes to enable the efficient discovery of candidate a plateau (Supplementary Fig. 2). Colony sequencing revealed 30 can-
biomarkers in low abundance. didate DNAzyme sequences (Dz01–Dz30; Supplementary Fig. 3b). All
of them were later confirmed to be DNAzymes capable of sensing the
Applying MORAC to breast cancer target but not the control CEM (Supplementary Fig. 3c). Based on the
We first piloted the ability of MORAC to identify potential biomarkers in occurrence of the repeated sequence and the enzyme activity, we chose
cancer cell lines. We chose two readily available non-cancerous human Dz04 and Dz06 as the representatives for further characterization.
Nature Chemistry | Volume 16 | January 2024 | 122–131 124
devaelc noitcarF
Dz04 in Dz04 + CEM (30 min)
1.0 MDA-MB-231 CEM 6
3
R RH M GE M B O PT X GE M 0.5 M D A- M M B- C 2 F 3 - 1 1 0 H A ME C M D A- M M B- D 2 A 3 - 1 M - M B- D 2 A 3 - 1 M - M B- D 4 A 3 - 6 M M B- D 2 A 3 - 1 M - M B- D 2 A 3 - 1 M - B B T -2 5 3 4 1 9 - Hs 57 8T M CF-1 0 M C C A F 1 h -1 0 C A1a M D A- M B-2 31-
k = 0.073 ± 0.008 min–1
obs
0
0 2
T
0
ime (min
4
)
0 60
51.
3
1
6.
4
1.
4 0.7 2.7
4
5.2
4
0.
4
5
6.2C
(%
lv
)
.
h
Dz ( 0 30 4 m + C in E ) M
OL
6–
OL
6+ 0.042 [His 6 -rAPOL6] (nM) 85
EC 50 :
MS: HE
K2
9 3T
HE
K2
9
p
3
C
T
A
/ G- A P
HE
K2
9
p
3
C
T
A
/ G- A P
Dz04 (30 min)
4.1 ± 0.5 nM
1 2 1 2 1 2
[GST-rAPOL6 ] (nM)
1–76 42 680 5,400
2
4. 8
2
6.2C
(%
lv
)
.
Anti-APOL6 antibody (12 h)
)%(
noitcudnI
3 5 417 417
M2- M2- 31 L 31 L B-2 B-2 M M A- A- D D M M
d
Combine, concentrate
CEM Heparin affinity chromatography Elute Flow
pH 7.0 A through Washing fluid Elution
F1 F2 F3 F4 F5 F6 F7 F8 1 2 3 1 2 3 4 5 6 1 2 3
Probing Probing
with Dz04 with Dz06
rA rA
Pulldown with iDz04
A
B, before 100 Dz04
A, after
50
0
–11 –10 –9 –8 –7
log[c (M)]
Fig. 2 | Identification of APOL6 as a candidate biomarker using MORAC (purple star) with iDz04. The pulldown process was monitored by Dz06, another
on breast cancer cell lines. a, Selectively sensing MDA-MB-231 CEM by Dz04. DNAzyme specifically sensing MDA-MB-231 CEM. e, Confirmation of a protein
Filled and hollow arrowheads denote the full length (119 nt) and the 3′ cleavage target (APOL6) pulled down by iDz04 from MDA-MB-231 CEM. M refers to a
product (105 nt) of Dz04, respectively. b, Fraction cleaved versus time for protein ladder, with five reference bands being highlighted (25, 35, 40, 55 and
the induced Dz04 cleavage by MDA-MB-231 CEM. Data are presented as mean 70 kDa). The SDS–PAGE gel was silver stained. f, The overexpression of APOL6
values ± s.d.; n = 3 independent replicates. The k value was calculated to be in HEK293T cells generated CEMs that can trigger Dz04 to cleave. g, Comparing
obs
0.073 ± 0.008 min−1. c, Specificity of Dz04 on breast cancer cell lines. Only the Dz04 with an antibody in terms of sensitivity on rAPOL6. [Dz04] = 100 nM.
CEMs of MDA-MB-231 and its derivatives triggered the cleavage (Clv.) of Dz04. h, Induced Dz04 cleavage signal versus logarithm of the effector (His-rAPOL6)
6
‘–’ refers to no cleavage. Cell names are defined in the Methods. d, Probing the concentration c. Data are presented as mean values ± s.d.; n = 3 independent
prepurified CEM fractions with Dz04 and pulling down the sensed molecule replicates. The apparent EC value for Dz04 is 4.1 ± 0.5 nM.
50
Article https://doi.org/10.1038/s41557-023-01328-5
1
0 1 2 3 4
Days
Both DNAzymes selectively sensed MDA-MB-231 CEM and cleaved from the iDz04 magnetic beads. We repeated the pulldown and elution
the RNA linkage in a time-dependent manner (Fig. 2a and Supplemen- three times to ensure sufficient proteins were obtained. Using Dz06
tary Fig. 4a–d), with the observed rate constant (k ) values estimated at (a second DNAzyme) to assay the samples, we were able to readily moni-
obs
0.073 min−1 for Dz04 (Fig. 2b) and 0.042 min−1 for Dz06 (Supplementary tor the entire process and confirm the presence of the target protein in
Fig. 4e). We examined Dz04’s recognition specificity by checking its the elution (Fig. 2d), which not only shows the convenience of DNAzyme
reactivity to the CEM of 14 breast cancer cell lines (Fig. 2c). Eight of them probing but also implies that Dz04 and Dz06 recognize the same target
were able to activate Dz04, but all eight CEMs were from MDA-MB-231 molecule. On the sodium dodecyl sulfate–PAGE (SDS–PAGE) gel, an
and its derived cell lines, suggesting good specificity of Dz04 on the cell apparent new band emerged for the elution sample (Fig. 2e), hinting at
line level. Heating or proteinase K treatment prevented the MDA-MB-231 the success in target-specific pulldown and enrichment by iDz04 mag-
CEM from triggering Dz04 (Supplementary Fig. 5a,b), implying that the netic beads. That band corresponds to a protein with an MW of ~40 kDa,
target is a protein, whose size was estimated by molecular weight (MW) consistent with the previous estimation of a >30 kDa MW for the target
cut-off filtration to be over 30 kDa (Supplementary Fig. 5c). (Supplementary Fig. 5c). We excised the band, digested it with trypsin
Considering the absence of intracellular DNA-binding proteins and and analysed the digestion mixture by nanoscale liquid chromatogra-
the relatively low level (~0.1 mg ml–1) of total proteins in the CEM, we chose phy coupled to tandem MS (LC-MS/MS; Supplementary Fig. 5d). All the
heparin affinity chromatography to facilitate the prepurification and data together identify the target protein of Dz04/Dz06 to be apolipo-
enrichment of the target protein. We extracted 400 ml of MDA-MB-231 protein L6 (APOL6) with an MW of 38,104 Da. The conclusion was also
CEM and ran it through a 10 ml HiTrap Heparin Sepharose 6 FF column. supported by clear detection of APOL6 in the concentrated F6 elution
Of the eight elution fractions (F1–F8), by Dz04-based analysis, we quickly with an anti-APOL6 antibody (ab92273) and a peroxidase-conjugated
found that F6 was DNase-free and contained the relatively highest levels of secondary antibody (Supplementary Fig. 5e).
target protein (Fig. 2d). Therefore, we performed target-specific pulldown
on this fraction by inactivated Dz04 (iDz04, 100 pmol) bound to magnetic Excellent sensitivity of Dz04 DNAzyme on the APOL6 target
beads (100 μl). Through toehold-mediated DNA strand displacement The human APOL6 is a member of the apolipoprotein L family that has
(Supplementary Fig. 1b), the bound proteins were competitively eluted evolved rapidly under positive selection in primates21. While APOL1 is
Nature Chemistry | Volume 16 | January 2024 | 122–131 125
)mn
054
DO(
noitarefilorp
lleC
1.2 MDA-MB-231
0.6
0
1.2 LM2-4175
0.6
0
***
***
***
***
a b c
1.00
0.50
0.25
0 80 120 160
Months
d e f
siRNA 3
ytilibaborp
lavivruS
Overall survival in breast cancer
**
APOL6 high (n = 469) P = 0.0054
APOL6 low (n = 474)
Migration
confluence
(%)
MDA-MB-231 100
50
0
** 100
50
LM2-4175
0
0 1 2 3 4 5 Control Over-
expression
Days
)mn
054
DO(
noitarefilorp
lleC
Overexpression
2
MDA-MB-231
1
0
2 LM2-4175
1
0
132-BM-ADM
Control Overexpression
Migration
571,4-2ML
** Migration
confluence
(%)
MDA-MB-231 100
**
50
*** 0
*** 100
50
LM2-4175
0
Control siRNA1 siRNA3
132-BM-ADM
Control siRNA1
Migration
5714-2ML
siRNA3
Control
level
ANRm
6LOPA
evitaleR
0.75
40
Knockdown
***
NS
1.5 ***
1.0
0.5
0
1 2 3
siRNA
**
**
Fig. 3 | The tumour suppressor role of APOL6 in breast cancer. a, Kaplan– significant. e, Measured cell proliferation ability with APOL6 knockdown; n = 6
Meier overall survival analysis of APOL6 expression in breast cancer patients biologically independent samples. On MDA-MB-231, P = 5.0 × 10–8 for siRNA1
using the Kaplan–Meier plotter database (compared with a log-rank test). and 7.8 × 10–10 for siRNA3. On LM2-4175, P = 5.1 × 10–5 for siRNA1 and 5.5 × 10–6 for
b, Measured cell proliferation ability with APOL6 overexpression; n = 6 biologically siRNA3. f, Transwell migration assay with APOL6 knockdown; n = 3 biologically
independent samples. OD refers to optical density. P = 0.0020 for MDA- independent experiments. Representative micrographs and the derived data are
MB-231. P = 0.0030 for LM2-4175. c, Transwell migration assay with APOL6 shown on the left and right, respectively. On MDA-MB-231, P = 0.0023 for siRNA1
overexpression; n = 3 biologically independent experiments. Representative and 0.0031 for siRNA3. On LM2-4175, P = 0.00010 for siRNA1 and 0.00020 for
micrographs and the derived data are shown on the left and right, respectively. siRNA3. Assays in b–f were conducted on MDA-MB-231 and its derived LM2-4175
P = 0.0034 for MDA-MB-231. P = 0.0020 for LM2-4175. d, Relative APOL6 mRNA cells, using a two-tailed unpaired Student’s t-test. Data in b–f are presented as
level by siRNA-guided knockdown; n = 4 biologically independent experiments. mean values ± s.d. **P < 0.01, ***P < 0.001. Scale bars, 100 μm.
P = 0.00098, 0.36 and 0.00098 for siRNA1, 2 and 3, respectively. NS, not
Article https://doi.org/10.1038/s41557-023-01328-5
a secreted protein22,23, the remaining five family members are intra- non-detectable serum expression of APOL6 in both healthy individuals
cellular and lack a secretion signal. As a cytoplasmic protein, APOL6 and breast cancer patients (Supplementary Fig. 11), suggesting that this
is of low abundance (http://pax-db.org/; bottom 25–50%)24 and has protein is unlikely to be a serum biomarker for breast cancer.
an unknown function. A couple of studies25,26 have pointed out that We then explored the prognostic implication of APOL6 in cancer
APOL6 can induce a dichotomous cell death phenotype involving both patients. Kaplan–Meier analyses (using the Kaplan–Meier plotter
apoptosis and necroptosis in various cell types. database) indicated that high APOL6 expression correlated well with
To further characterize the Dz04–APOL6 interaction, we generated disease-free survival in not only breast cancer patients (943 total cases,
recombinant APOL6 (His tagged, His-rAPOL6) using HEK293T cells. P = 0.0054; Fig. 3a) but also patients with pancreatic cancer (404 total
6
Overexpression of rAPOL6 in HEK293T led to viewable cell death and cases, P = 0.001), ovarian cancer (1,656 total cases, P = 0.00021), lung
presumably rAPOL6-containing CEM that can activate Dz04 (Fig. 2f). cancer (1,144 total cases, P < 0.0001), liver cancer (364 total cases,
With the purified His-rAPOL6, we measured (in a 30 min reaction) the P = 0.0045) and gastric cancer (875 total cases, P = 0.0019; Supplemen-
6
half maximal effective concentration (EC ) for Dz04 to be 4.1 ± 0.5 nM, tary Fig. 12), implying that APOL6 might serve as a universal prognostic
50
and the lower detection limit of Dz04 to be down to ~100 pM (Fig. 2g,h). marker for cancer patients. In addition, we explored anti-cancer drug
Contrarily, the anti-APOL6 antibodies showed a non-detectable signal sensitivity and APOL6 expression associations in breast cancer, and
even with the presence of 85 nM His-rAPOL6, which can induce >90% of found lists of negatively (–) and positively (+) correlated drugs (Sup-
6
Dz04 to cleave in 30 min. Owing to the difficulty in collecting a high con- plementary Fig. 13), including cisplatin (–), cyclin-dependent kinase
centration (>500 nM) of His-rAPOL6, we switched to a commercially inhibitors (–), phosphoinositide 3-kinase inhibitors (–), epidermal
6
available N-terminal fragment of APOL6 (GST-rAPOL6 , ab164299) growth factor receptor inhibitors (–), histone deacetylase inhibitors
1-76
and estimated a lower detection limit of only ~1 μM for the tested most (+) and mammalian target of rapamycin inhibitors (+), which are all
effective anti-APOL6 antibody (Fig. 2g and Supplementary Fig. 6), currently in clinical use for breast cancer treatment.
which is four orders of magnitude poorer than that of Dz04. We reason To investigate the potential biological function of APOL6 in
that the great sensitivity of Dz04 comes from its affinity-based catalytic tumour cells, we established cells with overexpression or knockdown
mode, in which one target triggers multiple enzymes, that can lead to of this protein in MDA-MB-231 and LM2-4175, a breast adenocarcinoma
rapid signal generation (k of 0.073 min−1; Fig. 2b) and amplification. cell line. We noticed that APOL6 was mainly involved in lipid transpor-
obs
Indeed, at the EC (4.1 nM) concentration of rAPOL6, in 30 min, half of tation through vesicles, as evidenced by the observed co-localization
50
the total Dz04s (100 nM) would have been activated (Fig. 2g,h), which of APOL6–mCherry with the Golgi apparatus (pmEmerald–Golgi;
means an average triggering of ~12 Dz04s per rAPOL6. By projecting Supplementary Fig. 14) and the vesicle-like movement of APOL6–
the induced cleavage signal of Dz04 (~57% in 30 min; Fig. 2b) to the Emerald (Supplementary Video 1) in MDA-MB-231 cells. In addition,
dose–response curve (Fig. 2h), we found the APOL6 concentration to we also found that ectopic expression of APOL6 significantly inhibited
be 6.8 nM in the one-to-one (volume-to-volume) reaction mixture of cell proliferation and migration (Fig. 3b,c) and enhanced cell apopto-
the DNAzyme and the MDA-MB-231 CEM. This corresponds to an APOL6 sis (Supplementary Fig. 15), and that knockdown of APOL6 by small
level of 13.6 nM or 518 ng ml–1 in the original CEM, which supports the interfering RNAs (siRNAs) showed the opposite effect (Fig. 3d–f and
classification of APOL6 as a low-abundance protein (<1–5 μg ml–1 in Supplementary Fig. 16).
biological fluids)5,6. Interestingly, no APOL6 signal was detected in the Previous work26 has reported that the overexpression of APOL6
CEM samples by MS (Supplementary Fig. 7), suggesting the limitation can promote the extracellular release of the proinflammatory cytokine
of this traditional technique. In addition, besides Dz04 and Dz06, the IL-1β, but whether (overexpressed) APOL6 itself can enter the extracel-
other 28 DNAzymes identified by colony sequencing of the G11 pool lular space remains unknown. With the highly sensitive Dz04/Dz06
were all found to be inducible to cleavage by His-rAPOL6 (Supplemen- probes developed in this study, we identified APOL6 in the CEM of
6
tary Fig. 8), implying that at the later stage of the selection, APOL6 likely MDA-MB-231 and its derived cell lines (Fig. 2c). Certainly more work is
outcompetes all other potential targets in the system. needed to decipher the biological function of APOL6 and especially its
extracellular release during tumour development. Interestingly, in a
Role of APOL6 as a tumour suppressor recent study30 another APOL family member—APOL3—was identified as
Next, we examined APOL6 expression in human breast cancers. Based having detergent-like activity that kills intracellular pathogens to pro-
on a single‐cell RNA sequencing (scRNA-seq) dataset27 of 130,246 cells tect host human cells. Based on all of these findings, we urge biologists
across 26 primary breast tumours, we found low messenger RNA to pay more attention to APOL6, which appears to be closely involved
(mRNA) expression of APOL6 in all human breast cancers, including in tumour suppression.
the triple-negative breast cancer (TNBC) that represents the clinical
subtype of MDA-MB-231 cells (Supplementary Fig. 9a). Analysis on Applying MORAC to polyps preceding colon cancer
breast cancer proteomic data from the Clinical Proteomic Tumor Analy- To demonstrate MORAC’s generality and to showcase its ability to iden-
sis Consortium28,29 revealed low protein expression of APOL6 in normal tify potential biomarkers at early stages of cancer as well, we chose
and primary-tumour tissue, but in early stages and the TNBC subtype, polyps preceding colon cancer as the next target disease, since this
APOL6 expression seemed to be relatively higher (Supplementary disease follows a clear path from precursor condition to malignancy.
Fig. 9b). To look into that, we collected and lysed breast cancer tissue We applied MORAC particularly on colon low-grade intraepithelial
samples from 12 patients, including 6 non-TNBC and 6 TNBC females neoplasia (LGIN, a premalignant condition), the clinical specimens of
with different degrees of lymph node metastasis (ages ranging from which (from 24 patients, including 14 males and 10 females, with ages
37 to 78 years). Using Dz04 as a probe, we confirmed the overall low ranging from 20 to 81 years) were collected by endoscopic mucosal
APOL6 expression in these samples, and found the stage-independent, resection (Fig. 4a). Considering the differences in expression levels of
higher APOL6 levels in half of the TNBC tumours (Supplementary biomarkers among individuals, we randomly combined the LGIN tissue
Fig. 10). The findings uncover the potential of APOL6 as a tissue bio- samples from ten patients (nearly half of the specimens that we could
marker for TNBC diagnosis. However, considering its overall low access) to produce a mixed LGIN tissue lysate as the target system.
expression in breast cancer, APOL6’s diagnostic value should be further Meanwhile, normal tissue samples nearby LGIN from these patients
interrogated by probes with high sensitivity in the tissue environment were pooled together to generate a mixed normal tissue lysate as the
on larger clinical cohorts (our Dz04 probe arose from the selection control system. Similarly, through subtractive/positive SELEX (Supple-
against a CEM system, and thus could be less adaptive to the more mentary Figs. 1a and 17), we identified two representative DNAzymes,
complex system of tissue lysate). In addition, with Dz04, we observed Dz41 and Dz45 (Supplementary Fig. 18a,b), to selectively sense the LGIN
Nature Chemistry | Volume 16 | January 2024 | 122–131 126
Article https://doi.org/10.1038/s41557-023-01328-5
b c d
0 Time (h) 1
Dz41 + LT lysate
Dz41 + NT lysate
e
Probing Probing Probing
with Dz41 with Dz41 with Dz41
f
tissue lysate (Fig. 4b), with k values of 0.10 min−1 versus 0.00036 min−1 and pulldown assays. To overcome this issue, we screened a series of
obs
for Dz41 in LGIN versus normal tissue lysate (Fig. 4c). Crude truncation colon cancer cell lines with Dz41 probing and determined that the tar-
tests on Dz41 revealed certain redundant and conserved nucleotides in get protein was expressed at relatively high levels in the HCT116 and
its catalytic loop domain (Supplementary Fig. 18c,d), suggesting that SW480 cell lines (Supplementary Fig. 19c). Hence, we cultured HCT116,
room for improvement still exists for this DNAzyme. Identifying its collected the cells (~5 ml cell pellet) and extracted the cell lysate (~6 ml,
core sequence would be interesting but was omitted from this work, with a total protein level of ~15 mg ml–1) as the biological source for
as our major focus was to discover the potential biomarker that was prepurification and pulldown.
recognized by the DNAzyme rather than to study the DNAzyme itself. Despite cell lysate being extremely complex in molecular con-
To further examine the recognition generality of Dz41, we collected tent, current chromatography techniques can purify almost any
another 14 pairs of LGIN–normal tissue samples from LGIN patients. identity-defined, native protein from it with >80% purity31. The key is
Tests revealed that LGIN tissue lysate in each of the 14 pairs induced to combine chromatography techniques that separate on the basis of
more cleavage of Dz41 than normal tissue lysate (Fig. 4d), suggesting different physicochemical characteristics of the protein (orthogonal
that Dz41 recognizes a common target rising quantitatively in LGIN, chromatography). In our work, although the unknown identity of the
which is shared by all of the LGIN tissue samples. Among the tested target protein resulted in its unknown physicochemical characteris-
pairs, the difference in induction of Dz41 by LGIN versus normal tissue tics, we found that the convenient Dz41 probing can always provide
lysate fluctuated, which may be attributed to the differential progres- in-time feedback on the performance of chromatography to guide it
sion of LGIN in the sampled patients. Heating or proteinase K treatment for sufficient purification. Through a combined purification protocol
pointed to a protein target for Dz41, the size of which was estimated of anion-IEX/cation-IEX/SEC and Dz41 probing, we identified the frac-
to be <100 kDa by MW cut-off filtration (Supplementary Fig. 19a,b). tion (F29) that was deeply prepurified and contained the relatively
The attainable tissue samples from the clinical specimens were small highest level of the target protein (Fig. 4e and Supplementary Fig. 20;
in size and weight, which would make them unlikely to be able to gen- details are in the Methods under ‘DNAzyme-assisted purification of
erate a sufficient biological source for the following prepurification cell lysate by ÄKTA purifier’).
Nature Chemistry | Volume 16 | January 2024 | 122–131 127
devaelc
noitcarF
Dz41 + tissue lysate (30 min) 1.0
0.5
k = 0.10 ± 0.007 min–1 obs
k = (3.6 ± 0.6) × 10–4 min–1
obs
0
0 2
T
0
ime (mi
4
n
0
)
60 C
(%
lv
)
. 8.1 12.9 61.1 28.4 2.6 64.9
2.2 ± 0.4 nM
)%(
noitcudnI
a
LGIN tissue (LT or L) Dz41
LT Patient 1 2 3 4 5 6 7
NT N L N L N L N L N L N L N L
C (% lv ) . 0.5 16.1 2.4 4.1 18.2 2.3 8.6 3.4 11.1 1.8 55. 0 0.8 5.2
Patient 8 9 10 1 1 12 13 14
N L N L N L N L N L N L N L
Normal tissue (NT or N)
74.8 67.2 0.5 5.4 34.5 8.9 73.6 6.1
Cell lysate Anion IEX Cation IEX SEC
pH 7.4 pH 5.0 pH 7.4
F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13F14F15F16F17F18F19 F20F21F22 F23F24 F25F26F27F28F29F30F31F32F33F34F35F36
For pulldown
g h
Pulldown with iDz41 0.0098 [rSARS1] (nM) 80
100
Dz41
B M A 30 min
2 h
kDa
380 ± 84 pM
100 MS: Dz41 (30 min)
50
60 SARS1
k = 2.8 ± 0.5 µM
MW, 58,777 D 45
35 Dz41 (2 h)
0
15 B, before –11 –10 –9 –8 –7
A, after Anti-SARS1 antibody (12 h) log[c (M)]
ecnecseroulF )UFR(
ytisnetni
rA rA rA
i
iDz41
A 1,000
EC : 750 50
500
EC :
50 R2 = 0.99
250
0
0 5 10 15
c of iDz41 (µM)
Fig. 4 | Identification of SARS1 as a candidate biomarker using MORAC on target (SARS1) pulled down by iDz41 from the prepurified cell lysate. M refers to a
the tissue of polyps preceding colon cancer. a, Imaging of colon LGIN by protein ladder, with five reference bands being highlighted (15, 35, 45, 60 and 100
endoscopy. b, Selectively sensing LGIN tissue lysate by Dz41. Filled and hollow kDa). The SDS–PAGE gel was silver stained. g, Comparing Dz41 with an antibody
arrowheads denote the full length (109 nt) and the 3′ cleavage product (95 nt) of for the sensitivity on rSARS1. [Dz41] = 100 nM. h, Induced Dz41 cleavage signal
Dz41, respectively. c, Fraction cleaved versus time for the induced Dz41 cleavage versus logarithm of the effector (rSARS1) concentration. Data are presented as
by LGIN and normal tissue lysate. Data are presented as mean values ± s.d.; n = 3 mean values ± s.d.; n = 3 biologically independent experiments. The apparent
biologically independent experiments. The k values of Dz41 are 0.10 ± 0.007 EC values of Dz41 for 30 min and 2 h incubation are 2.2 ± 0.4 and 380 ± 84 pM,
obs 50
and (3.6 ± 0.6) × 10−4 min−1 for LGIN and normal tissue lysate, respectively. d, LGIN respectively. i, Flow cytometry measurement of the binding affinity of iDz41 to
tissue lysate consistently induced more cleavage of Dz41 than normal tissue lysate rSARS1. RFU, relative fluorescence unit. Data are presented as mean values ± s.d.;
on all tested paired samples from 14 patients. e, Probing with Dz41 for rigorous n = 3 biologically independent experiments. The estimated k is 2.8 ± 0.5 μM,
D
biochemical purification of colon cancer cell lysate. f, Confirmation of a protein with a coefficient of determination (R2) of 0.99.
Article https://doi.org/10.1038/s41557-023-01328-5
The DNAzyme-based pulldown protocol was similar to that Role of SARS1 as a potential precancerous biomarker
of the CEM, except for the addition of a subtractive step with a Based on histological characteristics, in 2019 the World Health Organi-
sequence-scrambled, inactivated Dz41 (iDz41, details are in the zation defined a two-tiered system—low grade versus high grade—to
Methods under ‘DNAzyme-based affinity pulldown and enrich- classify neoplastic precursor lesions in the digestive system36. Accord-
ment of target protein’), which was expected to further alleviate ing to the classification, in addition to LGIN, we further collected tis-
the potential interference from intracellular DNA-binding proteins sue specimens of colon high-grade intraepithelial neoplasia (HGIN, a
possibly existing in F29. Using SDS–PAGE (silver stained), we com- premalignant condition) and colon carcinoma (a malignant condition)
pared the protein contents of the samples before and after pulldown as well as the matching normal biopsies from patients (Fig. 5a), and
(Fig. 4f). The before-pulldown sample (F29) contained less than a checked the Dz41’s reactivity to lysates from these samples. Similar to
dozen visible protein bands, in which the band matching in position LGIN lysate (Fig. 4d), we found that each HGIN lysate (n = 10) induced
with the band of the after-pulldown sample occupied nearly 35% (in more Dz41 cleavage than the corresponding normal lysate (Supplemen-
weight) of the total proteins, suggesting that the DNAzyme-assisted tary Fig. 23a). By contrast, no clear trend in Dz41 induction was observed
three-step chromatography purification had greatly eased the between carcinoma and normal lysates (n = 10; Supplementary
protein complexity and enriched the target protein (~35% purity). Fig. 23b). Statistical analysis revealed that the measured Dz41 induction
The single apparent band exhibited in the after-pulldown (elu- and SARS1 concentration were significantly (P ≤ 0.0004) increased
tion) sample implied a pulldown success, whose ~60 kDa MW also in LGIN or HGIN compared to the corresponding normal samples
coincided with the <100 kDa estimation by MW cut-off filtration (Fig. 5b–d). According to Dz41 probing, the average SARS1 levels per mil-
(Supplementary Fig. 19b). MS analysis (Supplementary Fig. 21a) ligram tissue were estimated to be 0.4 versus 5.6 ng for normal versus
further identified the pulldown protein to be seryl-tRNA synthetase 1 LGIN; 1.0 versus 10.6 ng for normal versus HGIN; and 2.2 versus 4.2 ng
(SARS1) with a MW of 58,777 Da, which was supported by the Western for normal versus carcinoma (Fig. 5d). The >tenfold increase of SARS1
blotting detection of SARS1 in HCT116 cell lysate and F29 with an in LGIN or HGIN but not in carcinoma suggests this protein can be a
anti-SARS1 rabbit polyclonal antibody (Sangon Biotech, D225925; potential precancerous biomarker in polyps preceding colon cancer.
Supplementary Fig. 21b). For further verification, we performed SARS1 immunohistochemis-
try (IHC) on the 14 paired LGIN–normal tissue specimens (Fig. 5e),
Excellent sensitivity of Dz41 DNAzyme on the SARS1 target and confirmed an abnormal upregulation of SARS1 in LGIN (Fig. 5f,g).
SARS1, a member of the aminoacyl transfer RNA (tRNA) synthetase Compared to Dz41 probing, the statistical difference displayed by IHC
family, is well-known for its essential function in the aminoacylation was less significant, which could be due to the poor sensitivity of the
of tRNASer for protein synthesis. Among all tRNA synthetases, SARS1 anti-SARS1 antibody (Fig. 4g) used in the IHC assay. In addition, the
possesses a unique, C-terminus UNE-S domain that can divert a fraction Dz41-detected 5.6 ng SARS1 per milligram LGIN tissue corresponds
of itself from the cytoplasm to the nucleus, thereby controlling the to a SARS1 concentration of 560 ng ml–1 in the tissue lysate (0.01 ml
expression of vascular endothelial growth factor A32–34, an angiogenic lysis buffer was used per milligram tissue), supporting the claim of
factor involved in blood vessel growth that is important to cancer devel- low abundance (<1–5 μg ml–1)5,6 for SARS1. Moreover, in normal and
opment. In addition, SARS1 is known to be of relatively low abundance LGIN tissue lysates, SARS1 was also detectable by MS but with close
in the colon (http://pax-db.org/)24. detection levels (Supplementary Fig. 24), which implies the inadequate
To further characterize the Dz41–SARS1 interaction, we purified sensitivity of this traditional technique on low-abundance proteins.
recombinant SARS1 (rSARS1) and then measured Dz41’s EC to be Although the discovery of SARS1 was in precancer rather than
50
2.2 ± 0.4 nM and 380 ± 84 pM for a 30 min and 2 h reaction, respec- cancer tissue, we were still curious about its prognostic implications
tively. Meanwhile, we confirmed Dz41’s lower detection limit down in cancer patients. We found a correlation of high SARS1 expression
to ~40 pM (Fig. 4g,h). Contrarily, the anti-SARS1 antibody exhibited a with poor disease-free survival in patients with pancreatic cancer (404
lower detection limit of ~2.5 nM (Fig. 4g), nearly two orders of magni- total cases, P = 0.0054), lung cancer (1,925 total cases, P = 0.00036)
tude poorer than that of Dz41. Compared to Dz04–APOL6, the catalytic and liver cancer (364 total cases, P = 0.025) using the Kaplan–Meier
mode in which one target triggers multiple enzymes was manifested plotter database (Supplementary Fig. 25), implying that SARS1 may
even better by Dz41–SARS1, which can generate an average triggering promote cancer development in these above-mentioned types of
of ~23 Dz41s per rSARS1 in 30 min at the EC concentration (2.2 nM) cancer. In patients with gastric cancer (875 total cases, P = 0.056) and
50
of rSARS1 (Fig. 4g,h). breast cancer (1,879 total cases, P = 0.13), survival results of SARS1
In addition, we also evaluated the binding affinity and specificity expression did not reach statistical significance. The data suggest that
of iDz41 to rSARS1. Flow cytometry measurement yielded a dissociate for SARS1 expression, the prognostic predictive value is likely cancer
constant (k ) value of 2.8 ± 0.5 μM for iDz41 (Fig. 4i and Supplemen- specific, which could be further examined within larger clinical cohorts.
D
tary Fig. 22a), consistent with the result (~1.3 μM k ) measured by In this study, we revealed that SARS1 expression was upregulated in
D
surface plasmon resonance (Supplementary Fig. 22b). Compared the precancerous stage of colon cancer, indicating that this protein
to known nucleic acids with affinity, such as aptamers that bind to can be a potential biomarker for early cancer development. Whether
thrombin (~1 nM k ) or transforming growth factor β1 (~10 nM k )35, SARS1 increasing is a driving factor for malignant transformation or a
D D
iDz41 falls behind in affinity by two to three orders of magnitude, consequence of dysregulation in precancer development still needs
which could be attributed to its origination from a DNAzyme (Dz41) further investigation.
that was selected for affinity-based robust catalysis. We suspect
that the mediocre rather than strong affinity would favour the rapid Conclusions
release of a bound SARS1 from Dz41, allowing that SARS1 to bind with Built on the ligand-dependent RNA-cleaving DNAzymes, MORAC
the next Dz41 copy to iteratively trigger Dz41 cleavage for efficient offers an unprecedented capability to discover potential biomarkers
signal amplification. In other words, the possible sacrifice in affinity in low abundance. On biological systems of extracellular mixture and
likely contributed to the gaining of high sensitivity for Dz41, which cell/tissue lysate, we demonstrated that MORAC can simultaneously
set the cornerstone for the DNAzyme-based discovery of poten- generate DNAzymes to selectively sense a target system and identify
tial biomarkers in low abundance. Besides the mediocre affinity, a target molecule in the system that is sensed by the DNAzymes.
iDz41 possessed good SARS1-binding specificity (Supplementary The key is to take advantage of the features of selective and easily
Fig. 22c), which should also be inherited from the Dz41 precursor monitored sensing, signal amplification and easily converted pure
that selectively sensed SARS1. affinity of the DNAzymes, to achieve the probing and pulldown of
Nature Chemistry | Volume 16 | January 2024 | 122–131 128
Article https://doi.org/10.1038/s41557-023-01328-5
the target molecule with high specificity, sensitivity and conveni- be an interesting topic for future work. Post-discovery compari-
ence. With MORAC, we identified two cytoplasmic proteins—APOL6, son with the antibodies reveals an advantage of two to four orders
which entered the extracellular space in certain breast cancer cell of magnitude in sensitivity for MORAC DNAzymes, which explains
lines, and SARS1, whose expression rose abnormally in the tissue of why MORAC can discover further low-abundance proteins. Besides
polyps preceding colon cancer—as candidate cancer biomarkers. cytoplasmic proteins, membrane proteins or even non-protein mol-
We showed the prognostic value of APOL6 in patients with multiple ecules could also be identified by MORAC in principle, as the DNA-
types of cancer, and confirmed the abnormal upregulation of SARS1 zymes are able to sense almost any type of target in any system14,15,37.
in the pathological tissue of colon precancer patients. The biological Moreover, although not being tested in this study, the RNA cleavage
function of the two proteins currently remains unclear but should event in MORAC should be combinable with the existing isothermal
Nature Chemistry | Volume 16 | January 2024 | 122–131 129
)%(
egavaelc
14zD
decudnI
b
P = 0.00027 P = 0.00019
100
*** *** NS
80
60
40
20
0
NT lysate LT lysate NT lysate HT lysate NT lysate CT lysate
])M(
c[gol
P = 5.5 × 10–6 P = 4.0 × 10–5
–7
**** **** NS
–8
–9
–10
NT lysate LT lysate NT lysate HT lysate NT lysate CT lysate
25
20
15
10
5
0
)eussit
gm
rep
gn(
1SRAS
fo
c
P = 0.0042 P = 0.0038
** ** NS
Normal LGIN Normal HGIN Normal Carcinoma
3
.on
tneitaP
SARS1 Nuclei SARS1 Nuclei
1
.on
tneitaP
6
.on
tneitaP
a LGIN HGIN Carcinoma e Normal LGIN
c
d f g
100
80
60
40
20
0
erocs-H
P = 0.028 0.25
*
0.20
0.15
0.10
0.05
0
Normal LGIN
aera
eussit
rep
slexip
1SRAS
evitisoP
P = 0.74
P = 0.92
P = 0.17
P = 0.0014
**
Normal LGIN
Fig. 5 | Increase of SARS1 in colon LGIN and HGIN but not colon carcinoma. logarithm of the effector (SARS1) concentration in the lysate for comparison.
a, Representative haematoxylin and eosin (H&E) images of colon LGIN, HGIN d, Converting the induction in b to the effector (SARS1) concentration in the
and carcinoma tissue. Green brackets denote crypt portions occupied by tissue for comparison. In c and d, the n numbers are the same as in b, and the
neoplastic cells. Scale bars, 50 μm. b, Comparison of the induced Dz41 cleavage data are also presented as mean values ± s.d. The SARS1 concentration (ng per
by paired LT–NT lysate (n = 14 biologically independent samples), paired mg tissue wet weight) was estimated to be 0.4 ± 0.3 versus 5.6 ± 5.8 for normal
HT–NT lysate (n = 10 biologically independent samples) and paired CT–NT versus LGIN tissue; 1.0 ± 1.3 versus 10.6 ± 8.5 for normal versus HGIN tissue; and
lysate (n = 10 biologically independent samples). Data were extracted from 2.2 ± 0.9 versus 4.2 ± 4.3 for normal versus carcinoma tissue. e, Representative
Fig. 4d and Supplementary Fig. 11 and presented as mean values ± s.d. Pairing is SARS1 IHC images of paired normal and LGIN tissue. Scale bars, 50 μm. f, Image
reflected by the same colour and shape of the data dots. The averaged induction quantification of n = 14 paired normal and LGIN tissue samples. g, Histochemistry
was estimated to be (4.0 ± 3.8)% versus (37.3 ± 27.5)% for NT versus LT lysate; score (H-score) of the SARS1 detection in n = 14 paired normal and LGIN tissue
(10.2 ± 13.1)% versus (56.8 ± 28.7)% for NT versus HT lysate; and (21.7 ± 8.2)% samples. The P values were calculated with a two-tailed paired Student’s t-test.
versus (33.8 ± 27.6)% for NT versus CT lysate. HT, high-grade intraepithelial *P < 0.1, **P < 0.01, ***P < 0.001, ****P < 0.0001.
neoplasia tissue; CT, carcinoma tissue. c, Converting the induction in b to the
Article https://doi.org/10.1038/s41557-023-01328-5
amplification techniques38–40 to create a fast detection kit for poten- 15. Silverman, S. K. DNA as a versatile chemical component for
tial disease diagnosis. catalysis, encoding, and stereocontrol. Angew. Chem. Int. Ed. 49,
On cell/tissue lysate, we showed how techniques that are com- 7180–7201 (2010).
mon in the field of molecular biology (chromatography purification 16. Aguirre, S. D., Ali, M. M., Salena, B. J. & Li, Y. A sensitive DNA
and antibody-like affinity pulldown) can be harnessed to match the enzyme-based fluorescent assay for bacterial detection.
(inactivated) DNAzymes with their target, and vice versa, providing Biomolecules 3, 563–577 (2013).
simple but effective solutions for the broad application of MORAC to 17. Ali, M. M., Aguirre, S. D., Lazim, H. & Li, Y. Fluorogenic DNAzyme
systems with a high complexity of molecular contents. In this study, probes as bacterial indicators. Angew. Chem. Int. Ed. 50,
the process from DNAzyme selection to target identification by two 3751–3754 (2011).
students took a couple of months. By introducing automated worksta- 18. Shen, Z. et al. A catalytic DNA activated by a specific strain
tions, MORAC could be further improved to shorten the turnaround of bacterial pathogen. Angew. Chem. Int. Ed. 55, 2431–2434
time and to enable multiplexing of dozens to hundreds of biological (2016).
samples, leading to highly efficient biomarker discovery that may help 19. Geng, X. et al. Selective and sensitive detection of chronic
us better understand and battle malignant diseases such as cancers. myeloid leukemia using fluorogenic DNAzyme probes. Anal.
Chim. Acta 1123, 28–35 (2020).
Online content 20. He, S. et al. Highly specific recognition of breast tumors by an
Any methods, additional references, Nature Portfolio reporting sum- RNA-cleaving fluorogenic DNAzyme probe. Anal. Chem. 87,
maries, source data, extended data, supplementary information, 569–577 (2015).
acknowledgements, peer review information; details of author con- 21. Smith, E. E. & Malik, H. S. The apolipoprotein L family of
tributions and competing interests; and statements of data and code programmed cell death and immunity genes rapidly evolved in
availability are available at https://doi.org/10.1038/s41557-023-01328-5. primates at discrete sites of host-pathogen interactions. Genome
Res. 19, 850–858 (2009).
References 22. Vanhamme, L. et al. Apolipoprotein L-I is the trypanosome lytic
1. Crosby, D. et al. Early detection of cancer. Science 375, factor of human serum. Nature 422, 83–87 (2003).
eaay9040 (2022). 23. Pérez-Morga, D. et al. Apolipoprotein L-I promotes trypanosome
2. Cilento, E. M. et al. Mass spectrometry: a platform for biomarker lysis by forming pores in lysosomal membranes. Science 309,
discovery and validation for Alzheimer’s and Parkinson’s diseases. 469–472 (2005).
J. Neurochem. 151, 397–416 (2019). 24. Wang, M. et al. PaxDb, a database of protein abundance averages
3. Kim, D. et al. Proteomics analysis reveals differential pattern of across all three domains of life. Mol. Cell. Proteomics 11, 492–500
widespread protein expression and novel role of histidine-rich (2012).
glycoprotein and lipopolysaccharide-binding protein in 25. Andy Hu, C.-A., Zhaorigetu, S., Davidson, W. S. & Laskey, W.
rheumatoid arthritis. Int. J. Biol. Macromol. 109, 704–710 (2018). ApoL6: a novel biomarker of apoptotic activity in evolving
4. Thomas, S., Hao, L., Ricke, W. A. & Li, L. Biomarker discovery in ST-segment myocardial infarction in man. J. Integr. Cardiol. Open
mass spectrometry-based urinary proteomics. Proteomics Clin. Access https://doi.org/10.31487/j.JICOA.2020.04.10 (2020).
Appl. 10, 358–370 (2016). 26. Murphy, I. et al. ApoL6 induces dichotomous cell death
5. Keshishian, H., Addona, T., Burgess, M., Kuhn, E. & Carr, S. A. phenotype involving both apoptosis and necroptosis in cancer
Quantitative, multiplexed assays for low abundance proteins cells. Clin. Oncol. Res. https://doi.org/10.31487/j.COR.2020.07.12
in plasma by targeted mass spectrometry and stable isotope (2020).
dilution. Mol. Cell. Proteomics 6, 2212–2229 (2007). 27. Wu, S. Z. et al. A single-cell and spatially resolved atlas of human
6. Drabovich, A. P. & Diamandis, E. P. Combinatorial peptide libraries breast cancers. Nat. Genet. 53, 1334–1347 (2021).
facilitate development of multiple reaction monitoring assays for 28. Mertins, P. G. et al. Proteogenomics connects somatic mutations
low-abundance proteins. J. Proteome Res. 9, 1236–1245 (2010). to signalling in breast cancer. Nature 534, 55–62 (2016).
7. Wikstrand, C. J. & Bigner, D. D. Expression of human fetal brain 29. Krug, K. et al. Proteogenomic landscape of breast cancer
antigens by human tumors of neuroectodermal origin as defined tumorigenesis and targeted therapy. Cell 183, 1436–1456 (2020).
by monoclonal antibodies. Cancer Res. 42, 267–275 (1982). 30. Gaudet, R. G. et al. A human apolipoprotein L with detergent-like
8. Kobayashi, M., Katayama, H., Fahrmann, J. F. & Hanash, S. M. activity kills intracellular pathogens. Science 373, eabf8113 (2021).
Development of autoantibody signatures for common cancers. 31. How to combine chromatography techniques to purify an
Semin. Immunol. 47, 101388 (2020). untagged or native protein. Cytiva https://www.cytivalifesciences.
9. Daniels, D. A., Chen, H., Hicke, B. J., Swiderek, K. M. & Gold, L. A com/en/us/Solutions/Protein-Research/Knowledge-center/
tenascin-C aptamer identified by tumor cell SELEX: systematic Protein-purification-methods/How-to-combine-chromatography-
evolution of ligands by exponential enrichment. Proc. Natl Acad. techniques/Untagged-protein-purification-protocols (2021).
Sci. USA 100, 15416–15421 (2003). 32. Fukui, H., Hanaoka, R. & Kawahara, A. Noncanonical activity of
10. Sefah, K., Shangguan, D., Xiong, X., O’Donoghue, M. B. & Tan, W. seryl-tRNA synthetase is involved in vascular development. Circ.
Development of DNA aptamers using cell-SELEX. Nat. Protoc. 5, Res. 104, 1253–1259 (2009).
1169–1185 (2010). 33. Herzog, W., Müller, K., Huisken, J. & Stainier, D. Y. R. Genetic
11. Xiong, H. et al. Cancer protein biomarker discovery based on evidence for a noncanonical function of seryl-tRNA synthetase in
nucleic acid aptamers. Int. J. Biol. Macromol. 132, 190–202 (2019). vascular development. Circ. Res. 104, 1260–1266 (2009).
12. Ray, P., Rialon-Guevara, K. L., Veras, E., Sullenger, B. A. & White, R. R. 34. Xu, X. et al. Unique domain appended to vertebrate tRNA
Comparing human pancreatic cell secretomes by in vitro aptamer synthetase is essential for vascular development. Nat. Commun.
selection identifies cyclophilin B as a candidate pancreatic cancer 3, 681 (2012).
biomarker. J. Clin. Invest. 122, 1734–1741 (2012). 35. Imashimizu, M., Takahashi, M., Amano, R. & Nakamura, Y.
13. Breaker, R. R. & Joyce, G. F. A DNA enzyme that cleaves RNA. Single-round isolation of diverse RNA aptamers from a random
Chem. Biol. 1, 223–229 (1994). sequence pool. Biol. Methods Protoc. 3, bpy004 (2018).
14. Schlosser, K. & Li, Y. Biologically inspired synthetic enzymes made 36. Nagtegaal, I. D. et al. The 2019 WHO classification of tumours of
from DNA. Chem. Biol. 16, 311–322 (2009). the digestive system. Histopathology 76, 182–188 (2020).
Nature Chemistry | Volume 16 | January 2024 | 122–131 130
Article https://doi.org/10.1038/s41557-023-01328-5
37. Zhou, W., Zhang, Y., Ding, J. & Liu, J. In vitro selection in serum: Publisher’s note Springer Nature remains neutral with regard to
RNA-cleaving DNAzymes for measuring Ca2+ and Mg2+. ACS Sens. jurisdictional claims in published maps and institutional affiliations.
1, 600–606 (2016).
38. Gootenberg, J. S. et al. Nucleic acid detection with Springer Nature or its licensor (e.g. a society or other partner) holds
CRISPR-Cas13a/C2c2. Science 356, 438–442 (2017). exclusive rights to this article under a publishing agreement with
39. Chen, J. S. et al. CRISPR-Cas12a target binding unleashes the author(s) or other rightsholder(s); author self-archiving of the
indiscriminate single-stranded DNase activity. Science 360, accepted manuscript version of this article is solely governed by the
436–439 (2018). terms of such publishing agreement and applicable law.
40. Gootenberg, J. S. et al. Multiplexed and portable nucleic acid
detection platform with Cas13, Cas12a, and Csm6. Science 360, © The Author(s), under exclusive licence to Springer Nature Limited
439–444 (2018). 2023
Nature Chemistry | Volume 16 | January 2024 | 122–131 131
Article https://doi.org/10.1038/s41557-023-01328-5
Methods a pause for 45 s. The liquefied tissue was subsequently transferred into
Oligos a 1.5 ml tube and centrifuged at 4 °C and 20,000g for 10 min to remove
All DNA oligonucleotides were synthesized by Generay Biotechnol- any insoluble materials. Finally, the supernatant (a total protein con-
ogy or Integrated DNA Technologies, and purified by standard 10% centration of ~1 mg ml–1) was collected and transferred to a clean tube
dPAGE (8 M urea). All siRNAs were designed and synthesized by on ice for subsequent use.
RiboBio. Sequence information of all oligos is listed in Supplemen-
tary Tables 1–3. Test of DNAzyme activity and specificity
To characterize each potential DNAzyme probe, ~1 pmol DNA was sus-
Cell line information and culturing conditions pended in 10 μl of the ×1 reaction buffer (50 mM HEPES buffer, pH 7.5,
MDA-MB-231 (HTB-26), MDA-MB-436 (HTB-130), BT-549 (HTB-122), 100 mM NaCl and 10 mM MgCl) and then mixed with 10 μl of a certain
2
Hs578T (HTB-126), MCF-10A (CRL-10317), HMEC (PCS-600-010) and CEM or certain tissue lysate for incubation at 22 °C for 30 min. The reac-
colon carcinoma HCT116 (CCL-247) cells were purchased from the tion was stopped by the addition of 20 μl of ×2 loading buffer (8 M urea,
American Type Culture Collection. MDA-MB-231-derived LM2-4173 and 20% (w/v) sucrose, 0.1% SDS, 0.05% bromophenol blue, 0.05% xylene
LM2-4175 cells were kindly provided by G. Hu (University of Chinese cyanol FF, 0.09 M Tris(hydroxymethyl)aminomethane, 0.09 M borate
Academy of Sciences, Shanghai, China). Both cell lines have increased and 1 mM ethylenediaminetetraacetic acid (EDTA)). The products were
metastatic activity to the lungs compared with parental MDA-MB-231 analysed by 8% dPAGE with QuantitiyOne software.
cells. Other MDA-MB-231-derived cells including MDA-MB-231-HM To test DNAzyme specificity, CEMs from different cell lines were
(high lung metastasis), MDA-MB-231-BO (high bone metastasis), individually incubated with a DNAzyme probe for induced cleavage,
MDA-MB-231-GEM (gemcitabine-resistant subline), MDA-MB-231-PTX which was also analysed by dPAGE. For estimating the rate constant
(paclitaxel-resistant subline) and MDA-MB-231-RR (radiation-resistant (k ) of the selected DNAzymes, the induced cleavage signal was
obs
subline) have been established by us based on previously reported recorded at different time points (0 s, 20 s, 40 s, 1 min, 2 min, 5 min,
strategies41. MCF-10CA1h and MCF-10CA1a, both transformed from 20 min and 60 min). After calculating the percentage of cleavage at
normal breast cell MCF-10A by our lab, have displayed phenotypes of each time point, values for k were established by using the following
obs
primary carcinoma and low lung metastasis, respectively. HEK293T equation: fraction cleaved = FC (1 − e−kt), where t = time, k = k and
max obs
and HEK293F cells were kindly provided by L. Sun (Fudan University, FC = maximum of fraction cleaved.
max
Shanghai, China). All cell lines have been authenticated using short
tandem repeat profiling. DNAzyme-assisted purification of CEM by ÄKTA purifier
HMEC, MCF-10A and its transformed cell lines were cultured in MDA-MB-231 cells were cultured in T175 flasks with complete medium
DMEM/F12 medium with 5% horse serum, 0.5 μg ml–1 hydrocortisone, at 37 °C. Once the cells reached ~80% confluence, the medium was
5 μg ml–1 insulin, 20 ng ml–1 epidermal growth factor and 100 ng ml–1 replaced with serum-free medium as described previously. After 24 h,
cholera toxin. MDA-MB-231 and its derived cell lines, MDA-MB-436 and the CEM was collected. Generally, each T175 flask produced 50 ml CEM,
MDA-MB-468 were maintained in Leibovitz’s L-15 medium, wherein and with eight flasks we obtained ~400 ml CEM in total. The CEM was
10 μg ml–1 insulin was supplemented in MDA-MB-436 culture medium. first concentrated to ~30 ml using Millipore 10 kDa cut-off filters (4 °C,
BT-549 and Hs578T were maintained in DMEM medium containing 1,500g for 20 min) and then diluted to 100 ml by buffer A1 (25 mM
10 μg ml–1 insulin. HCT116 cells were cultured in McCoy’s 5A medium HEPES, pH 7.0 and 0.002% β-mercaptoethanol). The sample was then
with 2.2 mg ml–1 NaHCO. Each medium was supplemented with 10% filtered with a 0.22 μm filter and loaded into a 10 ml HiTrap Heparin
3
fetal bovine serum and 1% penicillin–streptomycin. Cells maintained Sepharose 6 FF column equilibrated with buffer A1. To protect the
in L-15 medium were cultured at 37 °C with 100% air. Other cells were column, the pre-column pressure and flow rate were set at 0.5 MPa and
all cultured at 37 °C with 5% CO. 5 ml min–1, respectively. The column was then washed with ~40 ml of
2
buffer A1 until the UV 280 value was down to 0, and the flow through
Preparation of crude extracellular mixtures was collected. Proteins retained in the column were eluted with a linear
As cells were grown to ~80% confluence in 10 cm culturing dishes, we gradient with 0–100% buffer B1 (25 mM HEPES, pH 7.0, 1 M NaCl and
collected them, washed them with cold ×1 phosphate-buffered saline 0.002% β-mercaptoethanol) in 20 min. When the conductance began
(PBS) buffer five times to remove serum proteins and then incubated to increase, fractions were auto-collected in 2 ml tubes until the col-
them in 10 ml of serum-free medium for 24 h. The medium containing umn was filled with 100% buffer B1 (~75 mS cm−1). The fractions were
extracellular secretions was collected and centrifuged at 300g for then combined and pooled into eight groups (F1–F8). F1–F8 and the
10 min at 4 °C to remove cell debris. The supernatant was then filtered flow through were concentrated ~10 times using 10 kDa cut-off filters
by 0.22 μm MW cut-off columns, followed by the supplementation (4 °C, 15,000g for 20 min) before DNAzyme-based profiling. Some
of protease inhibitors. These CEMs (a total protein concentration of 5 μl of each sample was then mixed with 1 pmol Dz04 in a 20 μl reac-
~0.1 mg ml–1) were then aliquoted into 100 μl samples and stored at tion system (50 mM HEPES, pH 7.5, 100 mM NaCl and 10 mM MgCl) to
2
−80 °C before use. evaluate whether the sample contained the target protein and which
sample contained the highest level of the target protein. The reaction
Collection and processing of clinical specimens products of Dz04 were analysed using 8% dPAGE. According to the
In this study, 6 non-TNBC specimens, 6 TNBC specimens, 24 LGIN induced cleavage signal of Dz04, F6 (Fig. 2d) was chosen for the fol-
specimens, 10 HGIN specimens and 10 colon carcinoma specimens lowing pulldown experiment.
were obtained from patients; 9 blood samples were obtained from
healthy individuals. The basic patient and specimen information is DNAzyme-assisted purification of cell lysate by ÄKTA purifier
listed in Supplementary Table 4. HCT116 cells were cultured in T175 flasks with complete medium at
To prepare tissue lysate, fresh tissue samples were immediately 37 °C. As the cells reached ~90% confluence, they were collected and
placed in precooled ×1 PBS buffer and rinsed three times to remove the washed three times with ×1 PBS buffer. Then cells were harvested by
surface blood. The solid tissues were cut into tiny pieces and immersed 0.25% trypsin, followed by 300g centrifugation for 5 minutes at 22 °C.
in NP-40 lysis buffer containing 1 mM phenylmethanesulfonyl fluo- Approximately 5 ml of cell precipitation in total was collected. Equal
ride (200 μl buffer per 20 mg of tissue). The tissue samples were then volume of lysis buffer (20 mM HEPES, 20 mM NaCl, 1 mM PMSF and 1%
homogenized with a refrigerated high-throughput tissue grinder. Five NP-40 buffer, pH 7.4) was mixed with the cell precipitation and vortexed
lytic cycles were conducted on ice with vibration at 60 Hz for 30 s and thoroughly at 4 °C for 30 minutes to fully lyse the cells. The resulting
Nature Chemistry
Article https://doi.org/10.1038/s41557-023-01328-5
cell lysate was centrifuged at 20,000g for 15 min at 4 °C. The superna- together for a tenfold concentration (a final volume of ~150 μl) using
tant was collected and filtered with a 0.22 μm filter to further remove 10 kDa cut-off filters (4 °C, 15,000g for 20 min). The entire pulldown
cell debris. At pH 7.4, we ran 2 ml of the collected sample separately process was monitored by another DNAzyme probe (Dz06). Basically,
through a 10 ml Source 15Q (anion IEX) and Source 15S (cation IEX) 5 μl of each solution including the flow through, the washing liquid,
column, which was pre-equilibrated with buffer A2 (20 mM HEPES, the elution and the concentrated elution was incubated with 1 pmol
20 mM NaCl and 1 mM PMSF, pH 7.4). ÄKTA purifier flow through was Dz06 in a 20 μl reaction system (50 mM HEPES, pH 7.5, 100 mM NaCl
set at a rate of 3 ml min–1 under a pre-column pressure of 1.5 MPa. After and 10 mM MgCl) for 30 min to track the target protein. The protein
2
washing with ×3 bed volumes of buffer A2, the bound proteins were samples before and after pulldown were subsequently characterized
eluted with a linear gradient with 0–100% buffer B2 (20 mM HEPES, by 12% SDS–PAGE.
1 M NaCl and 1 mM PMSF, pH 7.4) at a flow rate of 1 ml min–1 in 40 min. For pulldown on cell lysate, the protocol was similar to that of CEM
Some 1.5 ml sterile tubes were used to collect the eluted fractions with except that we added a subtractive pulldown step prior to the final
1 ml elution per tube. pulldown. The step was to further remove the intracellular DNA-binding
The flow through and each fraction were profiled with Dz41 to proteins potentially existing in the prepurified sample (F29), so that
evaluate their molecular contents. Dz41 probing clearly showed suf- the iDz41-based affinity pulldown would be less interfered with. Briefly,
ficient versus insufficient capturing of the target protein by anion we conjugated the sequence-scrambled iDz41 with magnetic beads,
versus cation IEX at this pH value, as the flow through of the latter but and incubated them with F29. After magnetic separation, we collected
not the former still contained high levels of the target protein (Fig. 4e the supernatant. This step was repeated three times. Following that,
and Supplementary Fig. 20). Of the 12 elution fractions from anion IEX, we used the iDz41 magnetic beads to pull down the target protein and
we collected F5–F8 that possessed relatively high levels of the target Dz41 (or Dz45) to monitor the pulldown process. All DNA oligos used
(Fig. 4e), pooled them together (4 ml in total) and divided the mixture for the pulldown are listed in Supplementary Table 2.
into four aliquots (1 ml each), which were used for Dz41-assisted titra-
tion of pH for effective cation IEX (Supplementary Fig. 20). We adjusted Nanoscale LC-MS/MS analysis
the pH of buffers A2 and B2 to 6.0 and 5.0, and repeated the purification LC-MS/MS analysis was performed on a trapped ion mobility spectrom-
of cell lysate by the 10 ml cation exchange column. We again used Dz41 etry time-of-flight mass spectrometer with parallel accumulation and
to profile the flow through and fractions at the new pH values, and serial fragmentation (Bruker Daltonics). The parameter settings were as
found that at pH 5.0, the target protein can effectively adsorb to the follows: mass-to-charge ratio, 100 to 1,700; inverse reduced ion mobility,
column and be eluted off the column later. Based on the Dz41-based 0.7 V s cm–2 to 1.3 V s cm–2; capillary voltage, 1,500 V; flow rate of dry gas,
profiling data, the fraction (F17) with the highest level of target protein 3 l min–1; column temperature, 180 °C; charge range, 0–5; active exclu-
was concentrated to 0.5 ml with 50 kDa cut-off filters (4 °C, 1,500g). The sion, 0.4 min; scheduling target intensity, 20,000; intensity threshold,
sample was then loaded to a 24 ml Superose 6 10/300 GL column for 2,500; and collision energy for collision-induced dissociation, 27 eV to
size-exclusion purification, which was conducted in buffer C (20 mM 45 eV. The mass spectrometer was coupled to a NanoElute liquid chroma-
HEPES, 150 mM NaCl and 1 mM PMSF, pH 7.4) with a rate of 0.5 ml min–1 tograph (Bruker Daltonics) with a 75-μm-inner-diameter × 25-cm-long
under a pre-column pressure of 1.5 MPa. Some 1.5 ml sterile tubes were column. Peptide separation was performed at a flow rate of 300 nl min–1
used to collect the flow through with 0.3 ml per tube. Similarly, the with mobile phases A (0.1% formic acid in water) and B (0.1% formic acid
flow through and each fraction were profiled with Dz41. According to in acetonitrile) along with a 60 min gradient as follows: 0–45 min, 2–22%
the induced cleavage signal of Dz41, F29 was chosen (Fig. 4e) for the B; 45–50 min, 22–37% B; 50–55 min, 37–80% B; and 55–60 min, 80% B.
following pulldown experiment.
Database search
DNAzyme-based affinity pulldown and enrichment of target All raw data were analysed by PEAKS Online (X build 1.5.2021-03-
protein 16_105304, Bioinformatics Solutions). The parameter settings were as
We used streptavidin-coupled magnetic beads (1 μm, 10 mg ml–1) to follows: MS1 tolerance, 10 ppm; MS2 tolerance, 0.05 Da; and Searched
carry the biotin-modified DNAzymes (inactivated, iDz04 and iDz41) Database, UniProt-human database (20,184 entries). Peptides with a
for the affinity pulldown of the target protein from the prepurified false discovery rate of less than 1% were used as cut-off values for pro-
samples. Prior to DNAzyme-based pulldown, the total protein con- tein identification based on target decoy strategies. Carbamidometh-
centration of the prepurified samples was estimated to be around the ylation of cysteine was deemed to be a fixed modification. Oxidation
microgram per millilitre level (by BCA kits). Using a permanent magnet, of methionine, deamidation and protein N-terminal acetylation were
we separated the magnetic beads from the storage buffer. considered to be variable modifications.
For pulldown on CEM, 100 μl of magnetic beads were washed three
times by binding-and-washing buffer (B&W buffer; 5 mM Tris-HCl, pH Small interfering RNA and vector transfection
7.5, 1 M NaCl and 0.5 mM EDTA) and resuspended in 500 μl B&W buffer. Trizol reagent (R0016, Beyotime Biotechnology) was used to extract
A 100 pmol aliquot of iDz04 was incubated with these magnetic beads total RNA fractions from MDA-MB-231 cells. Then, 500 ng of total RNA
for 30 min at 22 °C for biotin–streptavidin conjugation. The magnetic was reverse transcribed to generate complementary DNA (cDNA) using
beads were then washed twice with 500 μl B&W buffer and three times HiScript III Reverse Transcriptase (R302, Vazyme). An APOL6 gene frag-
with 500 μl reaction buffer (50 mM HEPES, pH 7.4, 100 mM NaCl and ment was amplified from these cDNAs and constructed into pCAG plas-
10 mM MgCl) to remove unbound iDz04. The obtained iDz04 magnetic mid as an APOL6-overexpression vector. All APOL6-targeting siRNAs
2
beads were then mixed with 30 μl of F6 in a total of 500 μl reaction were designed and synthesized by RiboBio, as shown in Supplementary
buffer and incubated on a rotator (20 r.p.m.) for 30 min at 22 °C. After Table 3. TNBC cells were transfected with the overexpression vector or
magnetic separation, the supernatant (or flow through) and magnetic siRNA using Lipofectamine 3000 (Thermo Fisher Scientific) according
beads were both collected. The latter was washed twice with reaction to the manufacturer’s instruction. Real-time polymerase chain reaction
buffer and resuspended in 500 μl reaction buffer. The washing fluid was carried out to evaluate the overexpression or knockdown level of
was also collected. To elute the target proteins from the magnetic the target APOL6 protein.
beads, 120 pmol of the competitive DNA strand was added to the mag-
netic beads for 30 min incubation at 22 °C. Through magnetic separa- Proliferation assay
tion, the elution was collected. To pull down adequate target protein, Cell proliferation was assessed using Cell Counting Kit-8 (CCK8) assays
we repeated the above steps three times, and combined the elution (Dojindo Laboratories) according to the manufacturer’s protocol.
Nature Chemistry
Article https://doi.org/10.1038/s41557-023-01328-5
Cells were pre-seeded in 96-well plates at a density of 2,000 cells per publish were received from all patients and healthy individuals prior
well in triplicate, and later incubated with 10% CCK8 solution at 37 °C to participation. All steps were conducted in accordance with the
for 1 h. The absorbance was then measured at 450 nm using a micro- protocols approved by the Ethics Committee of FUSCC (no. 050432-
plate reader. 4-2108) and Zhongshan Hospital, Fudan University (no. B2021-777R).
Immunohistochemistry assay Data availability
The clinical specimens were soaked in 10% neutral formalin for 72 h. All data are available in the main text or the supplementary materials.
Subsequently, paraffin embedding and sectioning were performed Requests for resources and reagents should be directed to the corre-
for further staining assay after dehydration by routine procedures. sponding authors. Source data are provided with this paper.
For the IHC assay, 4-μm-thick paraffin sections were deparaffinized
in xylene, rehydrated through decreasing concentrations of ethanol, References
washed in PBS and boiled in 0.01 M sodium citrate buffer (pH 6.0) for 41. Zhu, X. et al. Efficacy and mechanism of the combination of PARP
5–8 min in a pressure cooker to unmask antigens. Then, the slides were and CDK4/6 inhibitors in the treatment of triple-negative breast
immersed in 3% HO for 30 minutes to inhibit endogenous peroxidase cancer. J. Exp. Clin. Cancer Res. 40, 122–140 (2021).
2 2
activity, and incubated with the anti-SARS1 antibody (1:100 dilution)
at 4 °C overnight and with HRP-goat anti-rabbit IgG (1:50 dilution) for Acknowledgements
1 h. The expression level of SARS1 in each sample was quantified using We acknowledge funding by the National Key Research and
the H-score (H-score = % of weak staining × 1 + % of moderate stain- Development Program of China (2020YFA0908901 to H.G.), the
ing × 2 + % of strong staining × 3), ranging from 0 to 300. National Natural Science Foundation of China (82121002 and
91859104 to H.G.; 21991134 and T2188102 to C.F.), the Program of
Searching for DNAzymes that sense non-SARS1 targets Shanghai Academic Research Leader (22XD1421500 to H.G.) and
In theory, targeting a complex biological system with an evolved the New Cornerstone Science Foundation (to C.F.). The funders had
SELEX DNAzyme library should generate lists of DNAzyme probes no role in the study design, data collection and analysis, decision to
that can specifically sense targets with different identities. To look publish or preparation of the manuscript.
into that, we analysed sequences from high-throughput sequenc-
ing (~100,000 reads) of the G5 and G9 populations from the tissue Author contributions
sample selection, sorted them into putative families by the align- Q.H., Z.T., A.Y. and L.-P.G. conducted the selection, target identification
ment of consensus sequence and secondary structure and examined and experimental validation of the target. Q.S., X.D., P.W., W.Z., X.G.,
their ligand-dependent DNAzyme activities (Supplementary Fig. 26). D.S. and T.F. conducted the experimental validation of the target.
Because the overall sequence occurrences were low in G5, we chose X.-Y.L. and A.Y. collected clinical specimens. D.Y., J.L. and C.F. analysed
to test the sequences with clearly high occurrences in G9. Among all the data. Y.-S.Z. and Y.-Z.J. supervised the project. H.G. developed
44 tested sequences, 39 of them showed reactivity to SARS1, and the the initial concept, supervised the project, interpreted the data and
other 5 sequences could not be activated by either SARS1 or the LGIN wrote the manuscript. All authors participated in the discussions and
tissue lysate. The results suggest that none of these sequences targets a reviewed and approved the manuscript.
non-SARS1 molecule. Perhaps the G9 population had gone through too
much SELEX evolution, such that the high-occurrence sequences in G9 Competing interests
had a preference to interact with SARS1 under the given selection pres- Three Chinese patents have been filed, with a status of initiative for
sure. To search for DNAzymes that sense non-SARS1 targets in the LGIN examination as to substance. Q.H., Z.T., L.-P.G., X.-Y.L., T.F., Y.-Z.J.
tissue lysate, future work could focus on examining the low-occurrence and H.G. declare the following competing interests: patent no.
sequences in G9; increasing the sequencing throughput and analysing CN202110364792.0 was applied for by Fudan University Shanghai
the sequences from an earlier population; or adjusting the selection Cancer Center, covering the identified DNAzyme probes that
pressure to bias the evolution of non-SARS1-dependent DNAzymes (for selectively sense MDA-MB-231 cells in this study; and patent no.
example, by doping in rSARS1 into the subtractive selection). CN202110361337.5 was also applied for by Fudan University Shanghai
Cancer Center, covering the method to identify the potential
Statistics and reproducibility biomarker (APOL6) of breast cancer based on the DNAzyme probes
Statistical analyses were performed using GraphPad Prism v.8.0 and in this study. Z.T., A.Y., Q.S., D.S., Y.-S.Z. and H.G. declare the following
R software (v.4.2.1). Results are represented as mean ± s.d. Statistical competing interests: patent no. CN202111198079.X was applied for
significance was determined using unpaired or paired two-tailed Stu- by Zhongshan Hospital, Fudan University, covering the findings of the
dent’s t-tests when appropriate. All gel, blot and micrograph images DNAzyme probes that selectively sense LGIN/HGIN specimens and
were independently repeated three times with similar results. All the probes’ utility in biomarker discovery in this study. X.D., P.W., W.Z.,
cell-based in vitro experiments were independently repeated three X.G., D.Y., C.F. and J.L. declare no competing interests.
times in triplicate. All the survival curves were constructed accord-
ing to the Kaplan–Meier method and compared with a log-rank test. Additional information
All findings were considered significant at a P value of less than 0.05. Supplementary information The online version contains supplementary
material available at https://doi.org/10.1038/s41557-023-01328-5.
Reporting summary
Further information on research design is available in the Nature Port- Correspondence and requests for materials should be addressed to
folio Reporting Summary linked to this article. Yun-Shi Zhong, Yi-Zhou Jiang or Hongzhou Gu.
Declaration of ethics oversight Peer review information Nature Chemistry thanks Feng Li, Chao Liang
The non-TNBC and TNBC specimens were all provided by Fudan Univer- and the other, anonymous, reviewer(s) for their contribution to the
sity Shanghai Cancer Center (FUSCC). The normal colon tissue, colon peer review of this work.
LGIN, colon HGIN and colon carcinoma specimens as well as the blood
samples from healthy individuals were all provided by Zhongshan Reprints and permissions information is available at
Hospital, Fudan University. Written informed consent and consent to www.nature.com/reprints.
Nature Chemistry
1
nature
portfolio
|
reporting
summary
March
2021
Corresponding author(s): Hongzhou Gu; Yi-Zhou Jiang; Yun-Shi Zhong
Last updated by author(s): Aug 17, 2023
Reporting Summary
Nature Portfolio wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency
in reporting. For further information on Nature Portfolio policies, see our Editorial Policies and the Editorial Policy Checklist.
Statistics
For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section.
n/a Confirmed
The exact sample size (n) for each experimental group/condition, given as a discrete number and unit of measurement
A statement on whether measurements were taken from distinct samples or whether the same sample was measured repeatedly
The statistical test(s) used AND whether they are one- or two-sided
Only common tests should be described solely by name; describe more complex techniques in the Methods section.
A description of all covariates tested
A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons
A full description of the statistical parameters including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient)
AND variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals)
For null hypothesis testing, the test statistic (e.g. F, t, r) with confidence intervals, effect sizes, degrees of freedom and P value noted
Give P values as exact values whenever suitable.
For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings
For hierarchical and complex designs, identification of the appropriate level for tests and full reporting of outcomes
Estimates of effect sizes (e.g. Cohen's d, Pearson's r), indicating how they were calculated
Our web collection on statistics for biologists contains articles on many of the points above.
Software and code
Policy information about availability of computer code
Data collection No software was used.
Data analysis Statistical analysis was analyzed by GraphPad Prism8.0 and R software (version4.2.1). LC-MS/MS analysis was performed on a timsTOF mass
spectrometer with PASEF (Bruker Daltonics, Bremen, Germany) and the raw data was analyzed by Peaks online (X build
1.5.2021-03-16_105304, Bioinformatics Solutions Inc). Confocal microscopy imaging of APOL6-Emerald in MDA-MB-231 cells was performed
on a TCS SP8 STED 3X microscope (Leica) and raw data was analyzed by Leica Application Suite 4.0. All gel scans were performed on Gel Doc
XR+ with image Lab Software,and raw date was analyzed by Quantity One v4.6.6. For the cell-apoptosis measurement, data was analyzed with
CytExpert software (Beckman Coulter). For the binding affinity measurement, we used BD CellQuest Pro software to collect and analyze the
flow cytometry data.
For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors and
reviewers. We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Portfolio guidelines for submitting code & software for further information.
2
nature
portfolio
|
reporting
summary
March
2021
Data
Policy information about availability of data
All manuscripts must include a data availability statement. This statement should provide the following information, where applicable:
- Accession codes, unique identifiers, or web links for publicly available datasets
- A description of any restrictions on data availability
- For clinical datasets or third party data, please ensure that the statement adheres to our policy
All data are available in the main text or the supplementary materials.
Human research participants
Policy information about studies involving human research participants and Sex and Gender in Research.
Reporting on sex and gender For breast cancer research, we focused on female patients (12 in total). For the research on polyps preceding colon cancer,
our findings apply to both Male and Female. We have considered sex in study design and determined sex based on self-
reporting. We collected specimens from 26 Male patients and 18 Female patients, and have obtained the consent for sharing
of individual-level data. Because the overall numbers for both sex were relatively small, we did not do a sex-based analysis.
Population characteristics The age ranges for non-TNBC and TNBC patients are 53-78 and 37-71 years, respectively. The age ranges for LGIN, HGIN, and
colon carcinoma patients are 20-81, 37-81, and 32-84 years, respectively.
Recruitment Pathological specimens of patients with colon low-grade intraepithelial neoplasia, high-grade intraepithelial neoplasia,
colorectal cancer, as well as Non-TNBC and TNBC specimens were selected for this study. Normal tissue samples of the same
patients were obtained as controls. The patients were recruited randomly from those who had been diagnosed with their
surgical specimens to carry one of the pre-cancers or cancers listed above.
Ethics oversight Fudan University Shanghai Cancer Center and Zhongshan Hospital, Fudan University
Note that full information on the approval of the study protocol must also be provided in the manuscript.
Field-specific reporting
Please select the one below that is the best fit for your research. If you are not sure, read the appropriate sections before making your selection.
Life sciences Behavioural & social sciences Ecological, evolutionary & environmental sciences
For a reference copy of the document with all sections, see nature.com/documents/nr-reporting-summary-flat.pdf
Life sciences study design
All studies must disclose on these points even when the disclosure is negative.
Sample size We assumed that the probability of the occurrence of a differential molecule A in the diseased and normal tissue of the same patient is 0.5,
and the probability of the event occurring simultaneously in five patients is 0.03125. According to the principle of small probability events,
events with a probability of less than 0.05 would not occur. But if it occurred, that means the assumed event is true. Therefore, a sample size
more than 5 is sufficient to our study. To demonstrate that the DNAzymes can be used to identify potential biomarkers directly from clinical
samples, we thought that collecting specimens from 56 (12 + 44) patients should be enough.
Data exclusions No data was excluded from the analyses.
Replication All tests were repeated at least three times with consistent results. Data were presented as mean values +/- standard deviation, which was
generated from at least three replicate assays.
Randomization The specimens used in our experiments were pathological and normal tissues from the same patients, with normal tissues serving as the
control. This is an observational cohort study rather than a traditional randomized controlled study. Selecting different patients for validation
is to improve universality and comply with the principle of biological repetition.
Blinding Only patients whose pathology met inclusion criteria were enrolled, so it was an open-label study.
Reporting for specific materials, systems and methods
