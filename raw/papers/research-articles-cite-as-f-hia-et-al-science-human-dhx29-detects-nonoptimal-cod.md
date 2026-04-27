---
source_path: /mnt/c/Users/Administrator/Zotero/storage/7MSGYWPW/Hia 等 - 2026 - Human DHX29 detects nonoptimal codon usage to regulate mRNA stability.pdf
ingested: 2026-04-23
sha256: 9f228f5e5eea5bfc
---

RESEARCH ARTICLES
Cite as: F. Hia et al., Science
10.1126/science.adw0288 (2026).
Human DHX29 detects nonoptimal codon usage to regulate
mRNA stability
Fabian Hia1†‡, Yitong Wu1†, Masanori Yoshinaga1*†, Sakurako Goto-Ito2†, Wakana Iwasaki2, Koshi Imami3,4,5,
Hirotaka Toh6, Peixun Han6, Ting Cai1, Takayuki Ohira7, Akira Fukao8, Daron M Standley9, Yuichi Shichino6,10,
Masaki Takegawa7, Toshinobu Fujiwara8, Tsutomu Suzuki7, Shintaro Iwasaki6,11, Michael C. Bassik12, Takuhiro
Ito2,13*, Osamu Takeuchi1*
1Department of Medical Chemistry, Graduate School of Medicine, Kyoto University, Kyoto, Japan. 2Laboratory for Translation Structural Biology, RIKEN Center for
Integrative Medical Sciences, Yokohama, Japan. 3Proteome Homeostasis Research Unit, RIKEN Center for Integrative Medical Sciences, Yokohama, Japan. 4Laboratory for
Metabolomics, RIKEN Center for Integrative Medical Sciences, Yokohama, Japan. 5Laboratory for Integrative Genomics, RIKEN Center for Integrative Medical Sciences,
Yokohama, Japan. 6RNA Systems Biochemistry Laboratory, Pioneering Research Institute, RIKEN, Wako, Saitama, Japan. 7Department of Chemistry and Biotechnology,
Graduate School of Engineering, The University of Tokyo, Tokyo, Japan. 8Laboratory of Biochemistry, Department of Pharmacy, Faculty of Pharmacy, Kindai University,
Osaka, Japan. 9Department of Genome Informatics, Research Institute for Microbial Diseases, The University of Osaka, Osaka, Japan. 10Department of RNA Biochemistry,
Institute of Medicine, University of Tsukuba, Tsukuba, Ibaraki, Japan. 11Department of Computational Biology and Medical Sciences, Graduate School of Frontier Sciences,
The University of Tokyo, Tokyo, Japan. 12Department of Genetics, Stanford University School of Medicine, Stanford, California 94305, USA. 13Structural Life Science and Cell
Biology Collaboration Team, RIKEN Center for Biosystems Dynamics Research, Yokohama, Japan.
*Corresponding author. E-mail: otake@mfour.med.kyoto-u.ac.jp (O.T.); takuhiro.ito@riken.jp (T.I.); m_yoshi@mfour.med.kyoto-u.ac.jp (M.Y.)
†These authors contributed equally to this work.
‡Present address: ArrowBiome Pte. Ltd., Singapore.
Synonymous codon usage controls global gene expression in both prokaryotic and eukaryotic species. Nonoptimal codons are
known to induce mRNA decay; however, the underlying molecular mechanism remains poorly understood in human cells.
Through genome-wide CRISPR screening, we identified the RNA-binding protein DHX29 as a critical regulator of codon-
dependent gene expression. Cryogenic electron microscopy and selective ribosome profiling demonstrated that DHX29
directly interacts with the A-site entrance of the translating 80S ribosome, the binding site for the eEF1A•GTP•aminoacyl-
tRNA ternary complex, suggesting a role in monitoring aminoacyl-tRNA sampling. Proteomic analysis further revealed that
DHX29 recruits the GIGYF2•4EHP complex to mediate global suppression of nonoptimal mRNAs. These findings establish a
mechanistic link between synonymous codon usage and the regulation of gene expression.
Protein translation is closely coupled to mRNA decay. found that codons can be predominantly categorized into GC-
Ribosomes engaged in aberrant translation serve as ending optimal codons (GC3) and AU-ending nonoptimal co-
molecular hubs, activating quality control mechanisms such dons (AU3) (16, 18). The GC3/AU3-based synonymous codon
as nonstop mRNA decay and nonsense-mediated mRNA usage influences various cellular processes such as subcellu-
decay. These pathways initiate processes to rescue ribosomes lar mRNA localization, pseudogenization, and antiviral de-
or degrade aberrant mRNAs (1–5). Dysregulation of these fense mechanisms (24–26).
mechanisms has been implicated in various pathological The molecular mechanisms by which synonymous codon
conditions, including inflammation, neuronal dysfunction, usage influences mRNA decay in eukaryotic cells remain un-
and cancer (4, 6, 7). Understanding the process of translation- der debate. Studies in S. cerevisiae have shown that ribosome
coupled mRNA turnover is crucial for uncovering disease slowdown due to nonoptimal codons is sensed by Dhh1p and
mechanisms and potential therapeutic targets. the CCR4-NOT mRNA deadenylation complex (27, 28). Mech-
Recent studies have highlighted synonymous codon usage anistically, the empty A site resulting from slow decoding
as a key determinant not only in protein folding and proteo- leads to vacant E-site recognition by Not5, a component of
stasis but also in the regulation of translation-coupled mRNA the CCR4-NOT complex (29). In human cells, it has similarly
decay (8–13). Optimal codons, which facilitate rapid transla- been proposed that CNOT3 interacts with the E-site cavity
tion elongation, are associated with increased protein pro- upon ribosome stalling, likely induced by slow decoding (30).
duction and prolonged mRNA stability. Conversely, mRNAs However, a more recent study suggests that this interaction
rich in nonoptimal codons (nonoptimal mRNAs) are rapidly preferentially occurs when specific arginine codons occupy
degraded and exhibit reduced translation efficiency (14–18). the P-site owing to favorable structural configurations (31).
These codon usage-mediated effects are widely conserved Notably, CNOT3 enrichment did not correlate with nonopti-
across species, but the classifications of optimal and nonop- mal codons (31). Thus, although CCR4-NOT complex recruit-
timal codons vary (16, 17, 19–23). In humans, we and others ment is generally linked to ribosome deceleration, in human
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 1
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
cells the complex more preferentially targets mRNAs en- (Fig. 1C and table S1). Notably, poly(A)+ RNA-binding pro-
riched in arginine codons, unlike yeast. This selective codon teins were prevalent among the hits (fig. S1D), indicating that
sensitivity of CNOT3 raises the possibility that additional, our screen successfully identified regulators operating at the
more universally acting factors are involved in the surveil- post-transcriptional levels.
lance and decay of nonoptimal mRNAs in human cells.
In this study, we aimed to investigate the synonymous co- DHX29 suppresses nonoptimal mRNA expression
don usage-dependent mechanism(s) that regulate gene ex- across the transcriptome
pression in human cells. By employing a genome-wide Among the candidate hits of the CRISPR screen, we observed
CRISPR screen, we identified the RNA-binding protein that the RNA-binding protein DHX29 had one of the highest
DHX29 as a key regulator of codon-dependent mRNA expres- casTLE scores and a positive casTLE effect size (Fig. 1C).
sion in human cells. Proteomic and structural analyses re- These indices indicated the substantial enrichment of
vealed that DHX29 directly interacts with the A-site entrance DHX29-deficient cells in the sorted fraction. DHX29 is a
of the translating 80S ribosome, where the DExH protein that is known to bind to the 43S preinitiation
eEF1A•GTP•aminoacyl-tRNA ternary complex also binds in a complex and to be required for translation initiation (34–37).
mutually exclusive manner. Moreover, selective ribosome While DHX29 was implicated in translation initiation and
profiling revealed that DHX29 preferentially interacts with also in antiviral immunity (34, 35, 38–40), its functional
the 80S ribosomes engaged in decoding AU3 codons. Further- role(s) in translation elongation or synonymous codon usage
more, we found that DHX29 recruits the GIGYF2•4EHP com- have not been elucidated. The CRISPR screen results were
plex to globally suppress mRNA expression. Taken together, validated by flow cytometric analysis, using K562 cells ex-
we propose that DHX29 represses the expression of mRNAs pressing the DHX29-targeting gRNA (DHX29-KO; Fig. 1D
with nonoptimal codon usage in human cells. and fig. S2, A and B). Consequently, DHX29-KO cells showed
an increase in the CD45.2-WT/CD45.1-OPT ratio (Fig. 1E). To
CRISPR screening to identify regulators of synonymous rule out the possibility that DHX29 is only required for un-
codon usage–dependent gene expression winding GC-rich mRNAs, we measured the mRNA levels of
To explore potential regulators of the codon usage effect on the synonymous CD45 reporters in control and DHX29-KO
gene expression, we conducted a genome-wide CRISPR K562 cells. The mRNA levels of CD45.2-WT and CD45.1-OPT
screen experiment using synonymous reporters with differ- were higher and lower in DHX29-KO cells, respectively,
ent codon usage patterns. We took advantage of a pair of mu- showing that DHX29 participates in regulating the amount
rine congenic markers, CD45.1 and CD45.2, which have of mRNA (fig. S2C). These findings confirm DHX29 as a po-
mostly identical amino acid sequences except for five amino tential regulator of gene expression in a synonymous codon
acids that make them distinguishable using specific antibod- usage-dependent manner.
ies (32). We designed a codon-optimized CD45.1 construct We next investigated the transcriptome-wide effect of
(CD45.1-OPT) through synonymous substitutions to increase DHX29 on codon-dependent gene expression by depleting
its GC3 content (16) (Fig. 1A). The resulting CD45.1-OPT has DHX29 in K562 cells in two independent approaches:
a substantially higher GC3 content (95.0%) compared to wild- CRISPR-mediated knockout (DHX29-KO) and a CRISPR in-
type CD45.2 (CD45.2-WT, 43.8%). Notably, the GC3 content terference (CRISPRi)-mediated knockdown (DHX29-KD, fig.
of CD45.2-WT is relatively low among all theoretical tran- S2D). RNA-seq analysis revealed that AU3-rich mRNAs were
scripts, including isoforms, indicating its nonoptimal codon up-regulated in both DHX29-KO and DHX29-KD K562 cells
usage (fig. S1A). Consistent with previous findings (16), RT- compared with controls (Fig. 1F, fig. S2E, and tables S2 and
qPCR analysis revealed that the mRNA encoding CD45.1-OPT S3), consistent with the results obtained using synonymous
showed higher stability compared to CD45.2-WT (fig. S1B). CD45 reporters. Notably, although the up-regulation of AU3-
We then conducted a genome-wide CRISPR screen by sim- rich mRNAs in DHX29-KO cells was significant (p < 0.0001),
ultaneously comparing the change in surface expression of DHX29-KD cells exhibited an even stronger increase (Fig. 1F
CD45.1-OPT and CD45.2-WT upon genetic perturbations. We and fig. S2E). This difference is likely attributable to the ex-
stably expressed both reporter constructs in K562 cells ex- perimental methods: DHX29-KO cells, maintained long-term
pressing Cas9, and then transduced a genome-wide gRNA li- as single-cell clones, may have acquired compensatory adap-
brary (Fig. 1B). Subsequently, we isolated cells showing a high tations, whereas DHX29-KD cells, analyzed shortly after
CD45.2-WT/CD45.1-OPT ratio, assuming that the expression gRNA transduction, more directly represent the acute conse-
of nonoptimal mRNAs was derepressed by the genetic abla- quence of DHX29 depletion.
tion of codon usage mediators (fig. S1C). Analysis of enriched Furthermore, gene expression changes in DHX29-KD cells
gRNAs in this sorted fraction over unsorted samples using were also inversely correlated with the codon stabilization co-
the casTLE pipeline (33) revealed 260 high-confidence hits efficient (CSC), another metric used to evaluate the
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 2
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
relationship between codon and mRNA stability (22) (fig. B, and table S7). Co-immunoprecipitation experiments con-
S2F). Notably, the GC3 content exhibited a correlation coeffi- firmed the interactions of DHX29 with uL10 and uS12, com-
cient comparable to the CSC-based scores (fig. S2G), suggest- ponents of the 60S and 40S subunits, respectively (Fig. 2C). A
ing that GC3 content and CSC are similarly effective in reciprocal co-immunoprecipitation analysis using an anti-
capturing DHX29-mediated regulation of gene expression in body recognizing the 60S components uL10/P1/P2 also con-
human cells. firmed the interaction of the 60S subunit with DHX29 (Fig.
The transcriptome-wide up-regulation of AU3-rich 2D). Additionally, this anti-uL10/P1/P2 antibody also pulled
mRNAs under DHX29 deficiency was similarly observed in down the endogenous DHX29 (fig. S5A), suggesting that the
other cell types, such as the monocytic cell line U937 and the interaction occurs under physiological conditions.
epithelial-like cell line HEK293T, although with cell-type-spe- To further examine whether translating ribosomes associ-
cific enrichment of gene ontology (GO) terms among the up- ate with endogenous DHX29, we performed polysome frac-
regulated and down-regulated genes under DHX29-deficient tionation on HEK293T cells with or without in-cell cross-
conditions (Fig. 1G; fig. S3, A to F; and tables S4 and S5). This linking. Notably, cross-linking did not alter the polysome pro-
variation is presumably attributed to the different sets of ex- files or the distribution of the 40S and 60S subunits (Fig. 2, E
pressed genes across cell types, while indicating the universal and F, and fig. S5, B and C). After the cross-linking, DHX29
role of DHX29 in the regulation of codon-dependent gene ex- interaction with the 80S and polysome, as well as with the
pression. Furthermore, a SLAM-seq [thiol (SH)–linked alkyl- 40S, was detected (Fig. 2, E and F). Without cross-linking,
ation for the metabolic sequencing of RNA] analysis to DHX29 predominantly localized to the ribosome-unbound
determine the mRNA decay rates revealed extended mRNA light fractions (fig. S5, B and C), likely reflecting the dynamic
half-lives for nonoptimal transcripts under DHX29-deficient nature of DHX29’s binding to the ribosome. These results
conditions in HEK293T cells (Fig. 1, H and I, and table S6). suggest that DHX29 interacts with the 80S ribosome and po-
Consistently, mRNA decay assays using 5-ethynyluridine la- tentially plays a role during translation elongation beyond
beling demonstrated that the degradation of nonoptimal the initiation phase.
mRNAs is slowed in the absence of DHX29 (fig. S3G), sug- To investigate the mRNA regions bound by DHX29, we
gesting that DHX29 is involved in the regulation of mRNA performed cross-linking and immunoprecipitation (CLIP)-
turnover. Collectively, these findings highlight the universal seq analysis using a doxycycline-inducible FLAG-DHX29-
role of DHX29 in repressing nonoptimal mRNA expression in expressing HEK293T cell line (fig. S6, A and B). This analysis
human cells. revealed that DHX29 binding is enriched around the start co-
To investigate the biological role of DHX29, we next ex- don (fig. S6C), consistent with its previously established role
plored the impact of DHX29 loss on cell fitness. DHX29-KD in translation initiation (34, 37, 38). In addition, substantial
K562 cells exhibited a growth disadvantage compared to con- DHX29 binding was also detected within the coding se-
trols (fig. S4, A and B), in agreement with a previous report quence (CDS) (fig. S6C), supporting the notion that DHX29
in HeLa cells (38). These observations suggest that codon-de- functions during translation elongation.
pendent mRNA regulation by DHX29 contributes to the To assess whether DHX29-mediated regulation of gene
maintenance of cell fitness across human cell lines. expression is associated with translation initiation and/or
elongation, we performed a global analysis comparing the
DHX29 directly interacts with the translating 80S ribo- changes in gene expression upon DHX29 depletion with fea-
some tures related to the CDS and 5 untranslated region (UTR).
′
To investigate the mechanisms by which DHX29 mediates We found that the local minimal free energy (MFE) of the 5
′
the synonymous codon usage effect, we identified proteins UTR, which represents the degree of structure in the 5 UTR
′
that interact with DHX29. FLAG-DHX29 was expressed in sequences, did not correlate with DHX29-dependent gene ex-
HEK293T cells, followed by the in-cell cross-linking using pression changes under our standard exponential growth
3,3 -dithiodipropionate (DSP) to retain weak and/or transi- conditions (fig. S7, A and B). Given that translation initiation
′
ent interactions (see Materials and Methods) (41). Then, cell efficiency is highly influenced by cellular growth status, our
lysates were harvested and treated with the previously tested experimental condition might not be optimal for detecting
concentration of RNase I (42) to investigate RNA- the potential initiation-related effect of DHX29. In contrast,
independent interactions, and subjected to immunoprecipi- CDS-associated features, including GC3 content and CDS
tation with an anti-FLAG antibody. Mass spectrometry anal- length, showed a stronger correlation with DHX29-
ysis of FLAG-DHX29 coprecipitates revealed that DHX29 dependent changes in gene expression (fig. S7A). Together,
interacts with various proteins of the 60S subunit, as well as these results suggest that, under our experimental condi-
the 40S subunit, which was unexpected because DHX29 was tions, DHX29 primarily affects mRNA expression through
thought to be involved in the scanning process (Fig. 2, A and mechanisms linked to translation elongation.
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 3
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
These findings motivated us to investigate the interaction of 2H). DHX29 does not collide with the accommodated A-site
DHX29 with the translating ribosome by capturing a single-par- tRNA, as shown by superimposition of our structure with the
ticle cryogenic electron microscopy (cryo-EM) snapshot of the previously reported human 80S structure containing A- and
complex. To isolate the translating ribosome, we employed our P-site tRNAs (48) (fig. S9E). Notably, the dsRBD of DHX29
in vitro reconstituted cap-dependent translation system (43, 44). sterically blocks recruitment of aminoacyl-tRNA to the A site
To focus on the ribosome structures during translation elonga- by eEF1A, as revealed by superimposing the current structure
tion, we isolated the 80S ribosome translating human cytomeg- with the previously reported human eEF1A•GTP S•amino-
γ
alovirus upstream open reading frame 2, a sequence that halts acyl-tRNA•80S structure, which represents the codon recog-
ribosome movement before translation termination with the nition or sampling state before the A-site tRNA
peptidyl-tRNA stuck in the P site, where the A-site codon is UAA, accommodation (49) (Fig. 2I). This suggests that the 80S ri-
a stop codon ending with A (45). We incubated the resultant bosome’s interaction with DHX29 and the
stalled ribosomes with recombinant human DHX29, and deter- eEF1A•GTP•aminoacyl-tRNA ternary complex is mutually ex-
mined the structure of the 80S•DHX29 ribosome complex by clusive during the aminoacyl-tRNA sampling.
cryo-EM (fig. S8, A to D). We then investigated whether interaction of DHX29 with
In accordance with the mass spectrometry data, the cryo-EM the A-site entrance of the translating ribosome is crucial for
structure clarified that DHX29 directly interacts with the 80S repressing nonoptimal mRNA expression. We first generated
ribosome. The double-stranded RNA binding domain (dsRBD) a deletion mutant lacking the dsRBD and the coil domain
of DHX29 occupies the A-site entrance position of the 80S ribo- ( dsRBD+Coil; Fig. 3, A and B). Subsequently, we reconsti-
Δ
some, which is connected via the coil domain to the helicase tuted wild-type and mutant DHX29 into DHX29-deficient
module comprising the N-terminal (N-term), RecA1, RecA2, cells (DHX29-KO) expressing synonymous CD45 reporters.
winged-helix (WH), Rachet, and OB-fold domains (Fig. 2, G and Reconstitution of wild-type DHX29, but not the
H). No RNA interaction with the dsRBD was observed in the dsRBD+Coil mutant, restored the CD45.2-WT/CD45.1-OPT
Δ
current structure, despite its structural similarity to the typical ratio (Fig. 3C). Furthermore, the dsRBD mutant containing
Δ
dsRBD. The helicase module resides between the head and body the C-terminal portion of the coil domain, which contacts the
of the 40S subunit, and the resolution of the RecA1/A2 domains helicase module, also failed to restore the ratio (Fig. 3, B and
is relatively low, indicating their structural flexibility (Fig. 2H C). Notably, the 5 UTRs of these reporters are identical and
′
and fig. S8D). The helicase module also interacts with the ribo- do not contain the structured sequences requiring DHX29’s
somal 18S rRNA via its N-terminal domain, WH domain, OB- activity, effectively ruling out initiation effects. Together,
fold domain, and inserted region in the RecA2 domain (fig. S9A). these results indicate the critical role of the dsRBD of DHX29
The cryo-EM densities of the C terminus of the coil domain and in repressing nonoptimal mRNA expression.
ribosomal uS4 are adjacent to each other, and a loop in the OB- Closer examination of the interfaces between the dsRBD
fold domain contacts ribosomal eS10, suggesting that these pro- of DHX29 and the A-site entrance revealed that DHX29 asso-
teins may also contribute to the interaction (fig. S9, A and B). ciates with eS30 and uS12 of the 40S ribosome (Fig. 3D). S373
We detected the cryo-EM density corresponding to the nas- and T375 of DHX29 are located at the interface with uS12 (In-
cent polypeptide in our cryo-EM structure (fig. S10), indicating terface 1, Fig. 3E). Moreover, Q452, S453, Q456, and L457 of
that the majority of 80S ribosomes in our structure were in- DHX29 are involved in interactions with eS30 (Interface 2,
volved in elongation. The obtained structure clearly explained Fig. 3F). Key residues involved in these ribosomal contacts
the cryo-EM density designated as DHX29 in the 43S scanning are conserved across species, although the yeast homolog
complex (46, 47), indicating that DHX29 functions in translation contains additional amino acids within the dsRBD and lacks
elongation at a similar position as in translation initiation (fig. conservation of residues contacting eS30 (fig. S11A). Struc-
S9C). tural predictions further suggest that the dsRBDs of human,
In our structure, the mRNA cryo-EM density was observed mouse, and zebrafish DHX29 adopt highly similar confor-
with its 5 end at the mRNA exit site and its 3 end at the in- mations (fig. S11B), supporting functional conservation.
′ ′
terface between RecA1/2 and the other domains of the DHX29 To evaluate the contributions of the amino acid residues
helicase module (fig. S9D). This indicates that the mRNA may of DHX29 at each interface with the A-site entrance of the
anchor DHX29 to the 80S ribosome, in addition to the interac- 80S ribosome, we generated a series of mutants that could
tion of DHX29 with the 40S subunit. disrupt this interaction. Reconstitution of the T375Y and
S373A/T375A mutants of DHX29, which perturb Interface 1,
The interaction of DHX29 with the A-site entrance is es- failed to restore the CD45.2-WT/CD45.1-OPT ratio (Fig. 3G).
sential for repressing nonoptimal mRNA expression Conversely, single point mutations such as S453Y and Q456A
As mentioned above, the dsRBD and the coil domain of at Interface 2 were able to restore the ratio (Fig. 3H), suggest-
DHX29 reside at the A-site entrance of the 80S ribosome (Fig. ing the modest effects of these alterations on the interaction.
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 4
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
However, the L457Y single point mutation or the abolishment revealed three-nucleotide periodicity surrounding the start
of all residues forming Interface 2 and stop codons in the input and DHX29-bound ribosome
(Q452A/S453A/Q456A/L457A) failed to restore the ratio (Fig. samples (Fig. 4, B and C). Notably, the DHX29-bound ribo-
3H), indicating the essential role of these residues in the in- some footprints were located not only around the start codon
teraction. Therefore, the perturbation of either interface be- but also throughout the rest of the CDS (Fig. 4C), providing
tween the dsRBD of DHX29 and the A-site entrance of the additional evidence of a substantial interaction between
80S ribosome is sufficient to abolish the synonymous codon DHX29 and the translating ribosome in cells.
usage-dependent effect of DHX29. We next examined whether any codon-wise enrichment
exists in DHX29-bound ribosome footprints at the A site. This
The helicase module of DHX29 is crucial for repressing analysis revealed a higher preference of DHX29 for ribo-
nonoptimal mRNA expression somes decoding AU3 codons, especially codons only contain-
We next examined whether mRNA engagement through the ing AU nucleotides (Fig. 4D and table S8). For most amino
helicase module of DHX29 is required for repression of non- acids, DHX29-bound ribosomes exhibit a preference for AU3
optimal mRNAs. To address this, we generated a DHX29 mu- codons over other synonymous codons (Fig. 4E). Using this
tant in which nine basic residues within the helicase domain fold enrichment of each codon upon DHX29 immunoprecip-
(R632A/R664A/R685A/H904A/K952A/H1257A/R1281A/R126 itation (defined as the DHX29 codon enrichment score, or
3A/R1285A), predicted to participate in RNA binding, were CES here), we calculated the DHX29 occupancy of each CDS
substituted with alanine (hereafter referred to as the 9A mu- and found an inverse correlation with the GC3 content (see
tant). Electrophoretic mobility shift assays (EMSA) revealed Materials and Methods, Fig. 4F). Moreover, the levels of
that wild-type DHX29 binds RNA with a dissociation con- mRNAs with high DHX29 occupancy greatly increased upon
stant (K ) of 0.266 ± 0.083 M, whereas the 9A mutant DHX29 depletion, indicating that the DHX29-bound mRNAs
d μ
showed markedly reduced affinity (K of 1.66 ± 0.80 M) (fig. are prone to degradation (Fig. 4G). Based on these observa-
d μ
S12, A to D), confirming severely impaired RNA binding. Co- tions, we propose that the DHX29 CES is a reliable predictor
immunoprecipitation analysis further revealed diminished of the codon-dependent effect of DHX29 on gene expression.
interaction of the 9A mutant with the ribosomal protein uL10 Taken together, these findings indicate that DHX29 directly
compared with wild-type DHX29 (fig. S12E), indicating that interacts with translating ribosomes decoding AU3 codons,
mRNA binding stabilizes the association of DHX29 with the thereby repressing nonoptimal mRNA expression.
80S ribosome. Functionally, reconstitution with the 9A mu-
tant failed to reduce the CD45.2-WT/CD45.1-OPT reporter ra- Comparative analysis of DHX29 CES with other metrics
tio, in contrast to the wild-type DHX29 (fig. S12F). of codon optimality
We then investigated the role of the DHX29 NTPase activ- To investigate the potential link between the codon-wise pref-
ity. A DHX29 mutant carrying a D702A substitution in the erence of the DHX29-ribosome interaction and the codon op-
RecA1 domain exhibited markedly impaired ability to cata- timality, we compared the DHX29 CES with previously
lyze ATP compared with wild-type DHX29 (fig. S12G). Recon- reported metrics of codon optimality. One such metric is the
stitution with the D702A mutant failed to reduce the CD45.2- tRNA adaptation index (tAI), which considers codon usage,
WT/CD45.1-OPT ratio (fig. S12H). Together, these results in- tRNA copy number, and wobble base interactions (51). Since
dicate that both mRNA binding and NTPase activity of the tRNA abundance can vary substantially between cell types,
DHX29 helicase module are required for the suppression of we utilized the HEK293-specific tAI values reported previ-
nonoptimal mRNA expression. ously (52). We did not find a strong correlation between the
CES and the HEK293-specific tAI values (fig. S13A). It is also
DHX29 engages with 80S ribosomes involved in decod- known that tRNA abundance is affected by different experi-
ing AU3 codons mental settings and cell states between laboratories (18).
Since DHX29 binds to the A-site entrance, where the amino- Therefore, we generated a tRNA sequencing dataset using
acyl-tRNA selection occurs, we assessed the codon-wise pref- our HEK293T cells. However, we failed to observe a signifi-
erences of the interaction between DHX29 and the cant correlation between the DHX29 CES and the tRNA
translating 80S ribosome. To this end, we performed selective abundance (fig. S13B). These results suggest that tRNA avail-
ribosome profiling by enriching the FLAG-DHX29-bound ri- ability alone does not fully explain the codon-wise preference
bosomes (Fig. 4A). Due to the limited amount of isolated ri- in the DHX29-ribosome interaction.
bosome footprints from the DHX29-bound ribosome In contrast, when we compared the DHX29 CES with the
samples, we incorporated our recently developed Ribo-seq CSC values from two independent datasets (17, 18), we ob-
technique, which is compatible with low sample input (50) served inverse correlations in both cases (fig. S13, C and D).
(Thor-Ribo-seq, see Materials and Methods). The analysis These findings suggest that the codon-wise preference of
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 5
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
DHX29 is inversely correlated with the codon optimality met- factors involved in mRNA decay (60, 61). Consistently, we
rics, at least to some extent. confirmed the interaction of DHX29 with both GIGYF2 and
4EHP under overexpression conditions in an RNA-
Codon content, rather than nucleotide composition, is independent manner (fig. S15A). Moreover, FLAG-DHX29 ex-
critical for DHX29’s regulatory effect pressed at the physiological levels co-precipitated endoge-
To determine whether the observed effect of DHX29 on gene nous GIGYF2 (fig. S15B). Additionally, proximity ligation
expression arises from overall nucleotide composition bias or assay orthogonally validated the co-localization of FLAG-
from synonymous codon usage bias, we performed luciferase DHX29 and GIGYF2 (fig. S15C).
reporter assays using a 1-nucleotide (nt) frameshift construct Based on these findings, we hypothesized that the
designed to alter AU3 composition while minimally affecting GIGYF2•4EHP complex also participates in the repression of
total AU content and overall sequence. Whereas AU3-rich nonoptimal mRNA expression on the pathway involving
nonoptimal mRNAs tend to be enriched in AU-rich nucleo- DHX29. To explore this hypothesis, we generated K562 cells
tides (fig. S14, A and B), introduction of the 1-nt frameshift lacking GIGYF2 or 4EHP using the CRISPRi-mediated knock-
into the SP4 ORF substantially increased GC3 content from down system and performed an RNA-seq analysis. Similar to
33.8% to 56.4% (fig. S14C). Reporter assays showed that the our observations in DHX29-depleted cells, the nonoptimal
wild-type AU3-rich SP4 constructs, but not the frameshifted mRNA expression was up-regulated across the transcriptome
version, exhibited significantly increased luciferase activity in GIGYF2- or 4EHP-depleted cells (Fig. 5, A and B; fig. S15,
under DHX29-deficient conditions (fig. S14D). D and E; and tables S9 and S10). Furthermore, the genes up-
We also examined the influence of AU content in the un- regulated in DHX29-depleted, GIGYF2-depleted, and 4EHP-
translated 3 UTR regions on DHX29-mediated regulation of depleted cells showed a substantial overlap (Fig. 5C and fig.
′
mRNA expression. We reanalyzed RNA-seq data from S15, F and G), suggesting that these three factors are involved
DHX29-depleted K562 cells (shown in Fig. 1F), focusing on in the same mRNA regulatory process. To further investigate
transcripts with similar GC3 content (>70%) to exclude the the functional relationship between DHX29 and the
effect of DHX29 on the CDS, and then categorizing them by GIGYF2•4EHP complex, we conducted an RNA-seq analysis
the GC content of the 3 UTRs (fig. S14E). We found that of DHX29/4EHP-double-depleted cells. In a DHX29-depleted
′
mRNAs with AU-rich 3 UTRs (GC content < 45%) were not background, further up-regulation of nonoptimal mRNA lev-
′
significantly up-regulated compared to those with GC-rich 3 els by 4EHP depletion was not observed (Fig. 5D, fig. S15H,
′
UTRs (GC content > 65%) in DHX29-depleted cells (fig. S14F). and table S11), revealing a robust genetic interaction between
We further performed reporter assays using constructs con- these proteins. Taken together, our findings suggest that
taining identical luciferase CDS but AU-rich 3 UTRs (fig. DHX29 represses AU3-rich mRNAs through its interaction
′
S14G). This analysis showed that the luciferase reporter ac- with the GIGYF2•4EHP complex.
tivity in DHX29-deficient conditions was comparable to the
control (fig. S14H). These findings suggest that GC3 codon DHX29 and CNOT3 regulate mRNAs in distinct path-
composition, rather than overall nucleotide composition, is ways
critical for DHX29-mediated regulation of nonoptimal As the mass-spectrometry analysis of DHX29 coprecipitates
mRNAs. identified CNOT3 and other components of the CCR4-NOT
complex, we explored the functional relationship between
DHX29 suppresses nonoptimal mRNA expression via DHX29 and CNOT3. Reanalysis of SLAM-seq datasets from
the GIGYF2•4EHP complex CNOT3-deficient human cells (31) confirmed that mRNAs en-
We then tried to identify the downstream molecule(s) riched in CNOT3 target codons (i.e., CGG, CGA, and AGG for
through which DHX29 represses nonoptimal mRNA expres- arginine) were stabilized in the absence of CNOT3 (fig. S16A).
sion. We explored the DHX29-interacting proteins using the Similarly, reanalysis of RNA-seq datasets revealed up-regula-
mass spectrometry analysis mentioned earlier (Fig. 2A). tion of arginine codon-rich transcripts under CNOT3 defi-
DHX29 co-precipitated numerous RNA binding proteins, ri- ciency consistent with previous reports (31, 62) (fig. S16B).
bosomal proteins, and components of the CCR4-NOT com- Moreover, we generated CNOT3-deficient HEK293T cells that
plex, suggesting its integration into a broad protein network exhibited a consistent increase in transcripts enriched in ar-
involved in post-transcriptional regulation (Fig. 2A). Notably, ginine codons (fig. S16, C and D). In contrast, transcripts rich
we identified the GIGYF2•4EHP complex, which is linked to in AU3 codons or those with low CSC-based scores were not
the repression of mRNAs with stalled ribosomes (53–57). stabilized or up-regulated upon CNOT3 depletion (fig. S16, E
4EHP binds the 5 cap structure of mRNA, thus competing to H). These findings suggest that CNOT3 is primarily respon-
′
with the canonical translation initiation factor eIF4E (58, 59). sible for the decay of mRNAs enriched in specific arginine
4EHP simultaneously binds GIGYF2, which recruits the codons.
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 6
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
Reciprocally, we examined whether DHX29 and the pathways (1, 4, 5). Our findings indicate that DHX29 plays a
GIGYF2•4EHP complex contribute to the decay of mRNAs key role in sensing the A-site vacancy, a step proposed to pre-
enriched in CNOT3 target codons (31). We found that the cede CCR4-NOT recruitment to the E-site (29–31). Whereas
mRNAs enriched in CNOT3 target codons were not up-regu- CNOT3 primarily regulates a subset of mRNAs enriched in
lated upon DHX29, GIGYF2, and 4EHP depletion (fig. S17, A specific arginine codons, DHX29 preferentially targets AU3-
to C). Taken together, these results indicate that DHX29 and rich transcripts, which are relatively depleted of CNOT3-
CNOT3 regulate mRNAs in distinct mechanisms. target codons (figs. S16 to S18). These findings suggest that
CNOT3 deficiency resulted in the stabilization of GC3-rich DHX29 and the CCR4-NOT complex constitute two distinct
mRNAs, in contrast to the effect observed under DHX29 de- regulatory mechanisms—both linked to the translational sta-
ficiency (fig. S16E). To explore the basis of this contrasting tus of the ribosome, yet exhibiting different codon prefer-
codon preference, we analyzed the relationship between GC3 ences. Elucidating how these pathways are differentially
content and the frequency of CNOT3 target codons. The anal- deployed depending on cellular contexts will be an important
ysis revealed a positive correlation between GC3 content and goal for future studies.
the frequency of arginine codons across transcripts (fig. Our findings uncover a functional link between DHX29
S18A). Moreover, the top CNOT3-target mRNAs were en- and the GIGYF2•4EHP complex in suppressing nonoptimal
riched in GC3 codons (fig. S18B). A similar positive correla- mRNA expression. The GIGYF2•4EHP complex has been pri-
tion was also observed between CSC-based scores and the marily characterized as a repressor of translation initiation,
frequency of specific arginine codons (fig. S18, C and D). with 4EHP competing with eIF4E for cap binding and
These results suggest that the seemingly opposing codon thereby preventing the recruitment of translation initiation
preferences of DHX29 and the CCR4-NOT complex may, at machinery (55, 58, 63, 64). However, subsequent studies have
least in part, arise from underlying codon composition biases. also shown that this complex is involved in promoting mRNA
decay (53, 60, 61, 65). Repression of translation initiation is
Discussion often associated with enhanced mRNA destabilization (66),
In the current study, we discovered that the RNA-binding at least in part due to competition between translation initi-
protein DHX29 plays a pivotal role in transcriptome-wide re- ation factors and mRNA decay machinery (67). Therefore,
pression of nonoptimal mRNA expression in human cells. translation repression by the GIGYF2•4EHP complex may
Our findings demonstrated that DHX29 directly interacts secondarily promote mRNA decay. Furthermore, members of
with the A-site entrance of the 80S ribosome, where its bind- the GIGYF family might directly induce mRNA degradation,
ing is mutually exclusive with that of the as they act as scaffolds for recruiting mRNA decay factors
eEF1A•GTP•aminoacyl-tRNA complex. Moreover, we re- such as DDX6 and TTP (53, 65). Together with prior studies,
vealed that DHX29 more preferentially interacts with ribo- our findings support a model in which mRNA decay occurs
somes decoding nonoptimal AU3 codons. Upon DHX29 concurrently with translational repression through the en-
binding to the A-site entrance, the GIGYF2•4EHP complex is gagement of the GIGYF2•4EHP complex.
recruited, likely initiating the decay of nonoptimal mRNAs Previous studies have established DHX29 as a crucial fac-
and thereby influencing synonymous codon usage-dependent tor in translation initiation (34–38). Our findings, however,
gene expression patterns (Fig. 5E). reveal a previously unrecognized role for DHX29 during
Our selective Thor-Ribo-seq analysis revealed that DHX29 translation elongation, highlighting its potential bifunction-
preferentially targets AU3 and AU-rich codons (Fig. 4), rais- ality. Notably, this dual role is not without precedent; yeast
ing important questions about the basis of this specificity. Not4, a key player in codon-dependent mRNA decay, exhibits
Considering that DHX29 does not directly interact with similar kinetics by associating with the ribosome during both
mRNA codon sequences in the A site but instead sterically the initiation and elongation steps (29). Also, the ASC-1 com-
interferes with the eEF1A•GTP•aminoacyl-tRNA ternary plex, involved in ribosome-associated quality control (RQC),
complex (Fig. 2I), we speculate that A-site vacancy is the prin- operates in both translation initiation and elongation (68).
cipal determinant of DHX29’s codon preference (Fig. 5E). These examples suggest that the bifunctionality of ribosome-
Clarifying this model will require precise measurement of the associated factors may represent a common mechanism, po-
specific translation sub-step(s) at which DHX29 engages ri- tentially facilitating communication between the initiation
bosomes in a codon-specific manner. However, no in cellulo and elongation phases of translation (55). Further research is
approaches currently allow such resolution, and future stud- needed to elucidate the co-regulation of translation initiation
ies will be required to define the mechanistic basis of and elongation by DHX29.
DHX29’s codon-specific activity. The dysregulation of translation-coupled mRNA decay
Multiple proteins engage with the ribosome to monitor mechanisms has been linked to a range of human diseases,
translation status and to induce a variety of quality control such as autoimmune conditions, neurological disorders, and
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 7
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
cancer (4, 6). Notably, mutations in the DHX29 gene have anti-FLAG (Sigma Aldrich, #F3165, 1:5,000), Rabbit monoclo-
been implicated in tumorigenesis (38, 69), suggesting that the nal anti-DHX29 (Cell Signaling Technology, #5926, 1:1,000),
aberrant regulation of codon-mediated gene expression con- Mouse monoclonal anti-RPS19 (Santa Cruz Biotechnology,
tributes to disease pathogenesis. Future studies investigating #sc-100836, 1:1,000), Mouse monoclonal anti-RPS23 (Santa
the mechanisms of DHX29-mediated decay of nonoptimal Cruz Biotechnology, #sc-100837, 1:1,000), Mouse monoclonal
mRNAs will be crucial for advancing our understanding of anti-Ribosomal P0/P1/P2 (MBL, #RN004M, 1:1,000), Mouse
these processes and may uncover novel therapeutic strategies monoclonal anti- actin (Santa Cruz Biotechnology, #sc-
β
targeting abnormal codon-dependent gene expression. 47778, 1:5,000), Mouse monoclonal anti-transferrin receptor
(Santa Cruz Biotechnology, #sc-32272, 1:1,000), Rabbit poly-
Materials and methods clonal anti-GIGYF2 (Bethyl, #A303-731A) and Rabbit polyclo-
Plasmids nal anti-CNOT3 (Proteintech, #11135-1-AP). HRP-conjugated
Lentiviral packaging components were described previously antibodies were as follows: Anti-Mouse IgG, HRP-Linked
(70). The wild-type CD45.2 sequence (CD45.2-WT) was amplified F(ab')2 Fragment Sheep (Cytiva, #NA9310, 1:5,000), Anti-Rab-
from mouse tail genomic DNA (C57BL/6J). The optimized bit IgG, HRP-Linked F(ab')2 Fragment Donkey (Cytiva,
CD45.1 sequence was designed according to the previous study #NA9340, 1:5,000), Monoclonal ANTI-FLAG M2-Peroxidase
(16) and synthesized using the gBlock Gene Fragment synthesis (HRP) antibody produced in mouse (Sigma Aldrich, #A8592,
service (Integrated DNA Technologies). pEF5_Hy- 1:5,000), and Anti-HA-tag mAb-HRP-DirecT (MBL, #M180-7,
gro_CD45.1OPT and pEF5_Neo_CD45.2WT reporter vectors 1:2,000). Isotype controls for immunoprecipitation experi-
were generated by inserting the optimized CD45.1 and wild-type ments are as follows: Rabbit polyclonal IgG (MBL, #PM035),
CD45.2 sequences into pEF5_BSD-T2A-GFP_Hyg and Mouse monoclonal IgG2a (MBL, #M076-3), and Mouse mon-
pEF5_BSD-T2A-GFP_Neo, respectively. pFLAG-CMV2 was ob- oclonal IgG1 (MBL, #M075-3).
tained from Sigma Aldrich. pHA-CMV2 was a kind gift from Ko- Antibodies for flow cytometry analysis were as follows:
taro Akaki (Kyoto University). pmirGLO-P2A was generated by FITC Mouse anti-mouse CD45.2 (Biolegend, #109806), APC
inserting the P2A sequence at the 3 end of the firefly luciferase Mouse anti-mouse CD45.2 (Biolegend, #109814), and PE/Cy7
′
into the pmirGLO vector (Promega). The coding sequences of Mouse anti-mouse CD45.1 (Biolegend, #110730).
wild-type DHX29, GIGYF2, 4EHP (58), and SP4 were amplified
from human cDNAs or the plasmid pcDNA4/TO/GFP-GIGYF2 Cell lines
(Addgene #141189 deposited by Simon Bekker-Jensen) (71) and The HEK293T cell line was described previously (70). K562
inserted into pFLAG-CMV2 (Sigma Aldrich), pFLAG-CMV2-HA, and U937 parental cell lines were obtained from ATCC. K562
pHA-CMV2, pInducer20-BSD (70), or pmirGLO-P2A. For the re- (#CCL-243) cell lines that stably express wild-type Cas9 or nu-
constitution experiments, the DHX29 mutants were generated clease-dead Cas9 fused with a KRAB domain (K562-CRISPRi)
by the PCR amplification of two fragments flanking the muta- were generated as described previously (73, 74). U937 cell
tion site and the simultaneous insertion. The wild-type and mu- lines that stably express wild-type Cas9 were generated as de-
tant DHX29 also harbor the synonymous mutations that confer scribed previously (75). All cell lines were confirmed to be my-
resistance to the gRNA targeting DHX29. For the luciferase re- coplasma-negative using a PCR Mycoplasma Detection Kit
porter assay, AU-rich 3 UTR sequences were inserted into (Applied Biological Materials). HEK293T cell lines were cul-
′
pGL3-promoter (Promega) as described previously (72). The tured and maintained in Dulbecco’s modified Eagle’s me-
frameshifted SP4 ORF was designed by removing premature ter- dium (DMEM) complete medium (Nacalai Tesque),
mination codons without altering GC composition and synthe- containing 10% (vol/vol) FBS, 50 M 2-mercaptoethanol (2-
μ
sized using GeneArt Gene Synthesis service (Thermo Fisher ME), penicillin, and streptomycin (100 g/mL). K562 and
μ
Scientific). Cloning was performed using In-Fusion Snap Assem- U937 cell lines were cultured in RPMI-1640 complete me-
bly Master Mix (Takara Bio) unless otherwise specified. dium (Nacalai Tesque), containing 10% (vol/vol) FBS, 50 M
μ
For the gRNA-expressing vector construction, gRNA se- 2-ME, penicillin, and streptomycin (100 g/mL).
μ
quences were inserted into the pMCB320 or pMCB306 vectors The Cas9-expressing HEK293T cells were generated by
using the DNA Ligation Kit Ver.2.1 (Takara Bio). Dual gRNA- transducing the lentiCas9-Blast vector (a kind gift from Feng
expressing vectors for the double knockdown experiments were Zhang) (76). The Cas9/reporter-expressing K562 cells were
constructed as described previously (70). The sequences of indi- generated by transfecting the pEF5_Hygro_CD45.1OPT and
vidual gRNAs are listed in table S12. pEF5_Neo_CD45.2WT reporter vectors, using the Neon
Transfection System (Thermo Fisher Scientific). The doxycy-
Antibodies cline (Dox)-inducible FLAG-DHX29-expressing HEK293T
Antibodies for immunoblots and immunoprecipitation anal- cells were generated by transducing the pInducer20-BSD-
yses used in this study were as follows: Mouse monoclonal FLAG-DHX29-WT vector. Cells were transfected using
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 8
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
Polyethylenimine (PEI) “Max” (Polysciences) according to the ReverTra Ace with gDNA Remover (Toyobo) was used for
manufacturer’s protocol. DHX29 mutant-expressing cells cDNA synthesis, according to the manufacturers’ instruc-
were selected for 7 days by adding blasticidin (Invivogen) to tions. The synthesized cDNAs were amplified using PowerUp
the transfected cells to a final concentration of 10 ng/mL. Ex- SYBR Green Master Mix (Applied Biosystems), according to
periments were performed under standard exponentially the manufacturer’s instructions. Fluorescence was detected
growing conditions. using a StepOnePlus real-time PCR system (Applied Biosys-
tems). Primers used for qPCR analysis are listed in table S12.
Lentiviral preparation and transduction
Lentiviral preparation and transduction were performed as RNA sequencing
previously described (70). Briefly, HEK293T cells were trans- For K562 and U937 cells, RNA-seq libraries were prepared
fected with lentiviral packaging components together with a using a NEBNext Poly(A) mRNA Magnetic Isolation Module
transfer vector and incubated for three days. The Cas9-ex- and a NEBNext Ultra II Directional RNA Library Prep Kit for
pressing K562 cell line was then harvested, resuspended in Illumina (New England BioLabs), according to the manufac-
viral supernatant supplemented with polybrene (8.0 g/mL, turer’s protocols. Sequencing was performed using a NextSeq
μ
Sigma Aldrich), and spin-infected for 3h. After two days of 500 Sequencer and a NextSeq 500/550 High-Output v2 Kit (75
transduction, the cells were harvested and analyzed by flow cycles, Illumina). For HEK293T cells, RNA-seq libraries were
cytometry to check the transduction ef ficiency. Puromycin prepared using a TruSeq Stranded Total RNA Kit (Illumina),
was added to the medium, and the cultures were incubated according to the manufacturer’s protocol. Sequencing was
for 3-5 days for the selection of gRNA-expressing cells. performed using a NextSeq 500 Sequencer and a NextSeq
500/550 High-Output v2 Kit (150 cycles, Illumina).
Genome-wide CRISPR/Cas9 screen For the analysis of published RNA-seq datasets, raw se-
The genome-wide CRISPR/Cas9 screen was performed as quencing reads were obtained from the NCBI’s Gene Expres-
previously described with slight modifications (70). Briefly, sion Omnibus under accession numbers GSE64455 (Cnot3-
the gRNA library was divided into three sublibraries for the KO) (62).
ease of experiments. The Cas9/reporter-expressing K562 cells The sequenced reads were analyzed by the standard pipe-
were transduced with each sublibrary and maintained inde- line on the Galaxy web server (https://usegalaxy.org/) or the
pendently throughout the experiments. Cells were then se- local workstation, as described previously (70).
lected with puromycin and expanded until cell sorting. The
cells were stained with FITC anti-CD45.2 and PE/Cy7 anti- SLAM-seq [thiol (SH)–linked alkylation for the meta-
CD45.1 antibodies, and cell sorting was performed using an bolic sequencing of RNA]
SH800Z cell sorter (Sony). Unsorted total cells and sorted Control and DHX29-deficient HEK293T cells were plated and
cells were subjected to DNA isolation. maintained in culture media supplemented with 25 M 4-
μ
DNA isolation and library preparation for the genome- thiouridine (s4U, Sigma Aldrich) for 24 hours. The cells were
wide CRISPR screen were performed as described previously then washed with DPBS and the culture media were replaced
(70). Sequencing was performed using a NextSeq 500 Se- with fresh media containing 2.5 mM uridine (Sigma Aldrich).
quencer and a NextSeq 500/550 High-Output v2 Kit (75 cy- After 0, 3, and 6 hours of incubation, cells were lysed in TRI-
cles, Illumina). Data were analyzed using the casTLE package zol, and total RNA was isolated according to the manufac-
(v0.7) (33). Gene ontology analysis was performed using Im- turer’s protocol under reducing conditions (supplemented
muno-Navigator (77). with 0.1 mM dithiothreitol (DTT)). Samples were protected
from light whenever possible. 10 g of total RNA was incu-
μ
Flow cytometric analysis bated in the reaction mix containing 10 mM iodoacetamide
Cells were stained with fluorescently labeled antibodies at (Sigma Aldrich), 50% DMSO, and 50 mM NaPO (pH 8). Sam-
4
4°C for 45 min. The cells were then washed and resus- ples were incubated at 50°C for 15 min, followed by the addi-
pended in MACS buffer (0.5% bovine serum albumin tion of DTT (20 mM). The alkylated RNA samples were
(Sigma Aldrich), 2 mM EDTA, and 1× DPBS). Flow cytomet- purified using RNA Clean & Concentrator-5 (Zymo Research).
ric data were collected using FACSVerse (BD Biosciences). The RNA quality was examined using a Bioanalyzer (Agilent)
Collected data were analyzed with FlowJo (v7.6.5, BD Bio- with an RNA 6000 Pico Kit (Agilent) to confirm that the RNA
sciences). integrity number (RIN) > 7.
SLAM-seq libraries were generated using a QuantSeq 3
′
Quantitative PCR (qPCR) analysis mRNA-Seq V2 Library Prep Kit (FWD) with Unique Dual In-
TRIzol (Invitrogen) or RNA Clean & Concentrator-5 (Zymo dices (12nt, Lexogen), according to the manufacturer’s in-
Research) was used for the isolation of total RNA, and structions. Sequencing was performed using a NextSeq 500
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 9
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
Sequencer and a NextSeq 500/550 High-Output v2 Kit (75 cy- cells were then incubated in Quenching Buffer (300 mM gly-
cles, Illumina). cine, 10 mM MgCl , 100 g/mL chloramphenicol, 100 g/mL
2 μ μ
The sequenced reads were trimmed and filtered using cu- cycloheximide, and 1× DPBS) for 10 min. Afterwards, the cells
tadapt, according to the manufacturer’s instructions (Lex- were lysed in ice-cold Lysis Buffer (20 mM Tris-HCl (pH 7.5),
ogen). The reads were mapped and the mutation rates were 150 mM NaCl, 5 mM MgCl , 1% Triton X-100, 100 g/mL chlo-
2 μ
calculated using the SlamDunk pipeline (v0.4.3) (78). The ramphenicol, 100 g/mL cycloheximide, and cOmplete Mini
μ
half-lives of mRNAs were calculated using the curve_fit func- Protease Inhibitor Cocktail). The lysates were treated with
tion in the scipy module (v1.5.2). The mRNAs undergoing de- TURBO DNase (25 U/mL, Thermo Fisher Scientific) on ice for
cay at least to a certain extent at the end of the chase 10 min and cleared by centrifugation. The lysates were snap-
experiments (half-lives < 6 hours) were used for the analysis. frozen and stored at -80°C until use or immediately used for
The transcripts with zero mutation rates in any of the sam- downstream analysis.
ples were excluded from the analysis.
For the analysis of the published SLAM-seq dataset from Coimmunoprecipitation
CNOT3-deficient HEK293T cells, raw sequencing reads were Lysates from DSP–cross-linked HEK293T cells were treated
obtained from NCBI’s Gene Expression Omnibus under ac- with RNase I (50 U/mL, Lucigen) at 25°C for 45 min, and then
cession numbers GSE268325 (31). The calculation of mRNA treated with SUPERase•In RNase inhibitor (0.5 U/ L,
μ
half-lives was performed as described above. Thermo Fisher Scientific) on ice. Portions of the lysates were
then removed and used for input. The remaining lysates were
mRNA decay assay pre-cleared with Dynabeads Protein G (Thermo Fisher Scien-
mRNA decay was assessed using the Click-iT Nascent RNA tific) at 4°C for at least 1 hour with gentle rotation. The ly-
Capture Kit (Thermo Fisher Scientific) following the manu- sates were then mixed with Dynabeads Protein G
facturer’s instructions. Briefly, control and DHX29-deficient preincubated with the anti-FLAG antibody (M2, Sigma Al-
HEK293T cells were cultured in the medium supplemented drich), anti-Ribosomal P0/P1/P2 antibody (MBL) or isotype
with 200 M 5-ethynyluridine (EU) for 6 hours. Cells were controls (MBL), and incubated at 4°C for 3 hours or overnight
μ
washed with DPBS, and the culture media were replaced with with gentle rotation. For the mass spectrometry analysis, the
fresh media without EU. After 0, 3, and 6 hours of incubation, lysates were incubated with Anti-FLAG M2 Magnetic Beads
cells were lysed in TRIzol, and total RNA was isolated. Then (Sigma Aldrich). Next, the beads were immobilized and
EU-labeled RNAs were biotinylated and further purified us- washed three times with Lysis Buffer (20 mM Tris-HCl (pH
ing Dynabeads MyOne Streptavidin T1 (Thermo Fisher Scien- 7.5), 150 mM NaCl, 5 mM MgCl , 1% Triton X-100, 100 g/mL
2 μ
tific). Purified RNAs were reverse-transcribed and transcript chloramphenicol, and 100 g/mL cycloheximide). The bead-
μ
levels were analyzed by RT-qPCR. bound proteins were then eluted. For immunoblot experi-
ments, the beads were mixed with SDS sample buffer con-
Competitive growth assay taining 2-ME and heated at 95°C for 5 min. For mass
Competitive growth assay was performed as previously de- spectrometry analysis, the beads were mixed with PTS Buffer
scribed with slight modifications (74). Briefly, K562-CRISPRi (12 mM sodium deoxycholate (FUJIFILM Wako Pure Chemi-
cells were transduced with either the mCherry-expressing cal), 12 mM sodium N-lauroyl sarcosinate (FUJIFILM Wako
pMCB320 vector encoding the control or DHX29-targeting Pure Chemical) in 0.1 M Tris-HCl (pH 8.0)) and incubated at
gRNA, or the GFP-expressing pMCB306 vector. GFP- 37°C for 10 min with gentle shaking. The eluates were then
expressing control cells were then mixed at a 1:1 ratio with stored at -80°C until use.
either control or DHX29-depleted mCherry-expressing cells
and maintained in co-culture for 12 days. The relative propor- Polysome profiling and fractionation
tions of GFP- and mCherry-positive cells were monitored by For the experiments without cross-linking, HEK293T cells
flow cytometry every two days. were treated with a 2.5 g/L trypsin solution (Nacalai Tesque).
Then, the cells were incubated with 1 mg/mL cycloheximide
In-cell di(N-succinimidyl) 3,3′-dithiodipropionate in ice-cold DPBS supplemented with 10 mM MgCl
2
. The cells
(DSP) cross-linking were then harvested, centrifuged, and the supernatant was
HEK293T cells were washed with ice-cold Wash Buffer (10 discarded. This cycloheximide treatment step was repeated,
mM MgCl , 100 g/mL chloramphenicol, 100 g/mL cyclo- and after centrifugation, the supernatant was completely re-
2 μ μ
heximide, and 1× DPBS), and then incubated in Crosslink moved. The resulting cell pellets were snap-frozen and stored
Buffer (0.5 mM DSP (Tokyo Chemical Industry), 10 mM at -80°C until further use.
MgCl , 100 g/mL chloramphenicol, 100 g/mL cyclo- For the experiments with cross-linking, HEK293T cells
2 μ μ
heximide and 1× DPBS) at room temperature for 15 min. The were treated with in-cell cross-linking as described above.
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 10
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
Then, the cells were lysed in the ice-cold Lysis Buffer, fol- the UniProt reviewed Homo sapiens fasta file (2023.6.19). The
lowed by DNase treatment as described above. The lysates protein group data matrix output from DIA-NN was sub-
were snap-frozen and stored until sucrose gradient centrifu- jected to further analysis using Perseus software (81). Data
gation. were log2 transformed, filtered based on valid values (only
The sucrose gradient centrifugation was performed as proteins that were quantified in at least 2 out of the 3 repli-
previously described with slight modifications (79). Briefly, cates were used), and missing values were imputed from a
the cell pellets for the experiments without cross-linking were normal distribution of log intensity of each sample. A volcano
lysed in the same Lysis Buffer as above. Lysates with or with- plot was generated based on log2 fold-change and p-values,
out cross-linking were loaded on top of a linear sucrose gra- with significant proteins defined using permutation-based
dient (10-30% or 15-60%). The fractionated samples were FDR (0.05).
subjected to trichloroacetic acid (TCA) precipitation, fol-
lowed by washing in ice-cold acetone twice. Samples were Cross-linking and immunoprecipitation (CLIP)-seq
then resolved in the sample buffer diluted with TE buffer con- Dox-inducible FLAG-DHX29-expressing HEK293T cells were
taining 2-ME, heated at 95°C for 5 min, and used for im- maintained in complete DMEM supplemented with 15 g/mL
μ
munoblot analysis. blasticidin. Cells were seeded at 5×106 per 15 cm dish and in-
cubated with 40 ng/mL Dox for 24 hours. Following induc-
Mass spectrometry analysis tion, cells were washed with PBS, UV–cross-linked at 254 nm
The immunoprecipitation eluates were reduced and alkylated (300 mJ/cm2), and harvested in lysis buffer (20 mM Tris-HCl
by 10 mM tris(2-carboxyethyl)phosphine hydrochloride and pH 7.5, 150 mM NaCl, 10 mM DTT, 5 mM MgCl , and 1% Tri-
2
40 mM chloroacetamide. Trypsin digestion was carried out ton X-100). Lysates were treated with TURBO DNase at 4°C
by adding 500 ng trypsin (Sequencing Grade Modified; for 10 min, clarified by centrifugation at 4°C at 20,000 × g for
Promega) in 800 L ammonium bicarbonate at 37°C over- 10 min, and digested with 0.01 units/mL RNase I (Ambion)
μ
night. The digestion was quenched the next day by adding at 37°C for 5 min. After SDS addition (0.1%), FLAG-DHX29
1,200 L ethyl acetate and 0.5% trifluoroacetic acid (TFA) to was immunoprecipitated with FLAG M2-Protein G Dyna-
μ
a final concentration. Finally, peptides were desalted using beads at 4°C for 2 hours. A 2% aliquot was reserved for input.
SDB-RPS Stage tips (GL Sciences) before LC/MS/MS analysis. Beads were washed three times with lysis buffer, three times
LC/MS/MS analysis was conducted on samples dissolved with High Salt buffer (50 mM Tris-HCl pH 7.5, 1 M NaCl, 1
in 0.5% TFA and 4% acetonitrile using a Q Exactive Plus Hy- mM EDTA, 1% NP-40, 0.1% SDS, and 0.5% sodium deoxycho-
brid Quadrupole-Orbitrap Mass Spectrometer (Thermo late), and twice with Wash buffer (20 mM Tris-HCl pH 7.4, 10
Fisher Scientific) in data-independent acquisition (DIA) mM MgCl , 5 mM NaCl, and 0.2% Tween-20).
2
mode. Liquid chromatography was performed on an EASY- RNA-protein complexes on beads were dephosphorylated
nLC 1200 system (Thermo Fisher Scientific) with a gradient with T4 polynucleotide kinase (New England BioLabs) at
of solvent A (0.1% formic acid in water) and solvent B (0.1% 37°C for 1 hour and ligated overnight at 22°C to IR800-
formic acid, 20% water, 80% acetonitrile). The following gra- conjugated 3 adapters (pre-adenylated oligos with sample
′
dient was used over 136 min for data acquisition at a flow index barcodes) using T4 RNA Ligase 1 (New England Bi-
rate of 150 nL/min: 0% B to 5% B, from 0 to 1 min; 5% B to oLabs). Complexes were eluted in LDS buffer containing 2.5%
40% B, from 1 to 110 min; 40% B to 95% B, from 110 to 112 2-ME at 70°C for 10 min, resolved on a SuperSep Ace 5-20%
min; 95% B from 112 to 120 min; 95% B to 5% B, from 120 to gel (FUJIFILM Wako Pure Chemical), and fragments >130
121 min; and 5% B from 121 to 136 min. An analytical column kDa were excised. RNA was extracted from gel slices by over-
packed with 1.9- m C18 particles (ReproSil-Pur 120 C18-Aq, night Proteinase K digestion (Ambion) at 25°C in a thermo-
μ
Dr. Maisch GmbH, Germany), with 75- m I.D., and 20-cm fill- mixer, precipitated by isopropanol, purified again using Oligo
μ
ing length was used. A spray voltage of 2.0 kV was applied Clean and Concentrator (Zymo Research), and reverse tran-
during sample measurement. A full-MS MS1 scan was per- scribed with SuperScript IV (Thermo Fisher Scientific) at
formed from 385-1,015 m/z at 35,000 resolution with an AGC 50°C for 60 min using the RT primer (5 -
′
target of 1e6 and a maximum IT of 55 ms and centroid-type GTGACTGGAGTTCAGACGTGTGCTC-3 ). cDNA fragments
′
data were acquired. DIA MS2 data were then collected using (10-200 nt) were size-selected, ligated to the 5 adapter (5 -
′ ′
a 16 m/z staggered windowing scheme at 17,500 resolution /5Phos/NNAGATCGAAGGCAGCGCTGTGGAGAAAG/3ddC/-
with a default charge state of 3, an AGC target of 1e6 and a 3 ), and amplified for 18 cycles with Phusion polymerase
′
maximum IT of 55 ms, with centroid-type data acquired. An (New England BioLabs). Libraries were purified, assessed us-
NCE of 27 was applied. ing a MultiNA system (Shimadzu), and sequenced on an Illu-
Raw data files were analyzed using DIA-NN software (80) mina Novaseq X Plus (pair-end 150 bp).
with default settings and a spectral library generated from Reads were demultiplexed, trimmed, and first mapped to
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 11
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
non-coding RNAs. Remaining reads were aligned to the hu- and fractionated into 48 frames with a pixel size of 1.06 Å.
man genome (hg38). PCR duplicates were removed using Cryo-EM data were processed with RELION-4 and
unique molecular identifiers (UMIs) to generate dedupli- RELION-5 (85, 86). The movie frames were aligned with Mo-
cated BAM files. The metagene plot was generated with the tionCor2 (RELION’s own implementation) and the contrast
Guitar R package (82). transfer function (CTF) estimation was performed with
CTFFIND-4.1 (87).
Prediction of mRNA secondary structures The template-free Laplacian-of-Gaussian filters automati-
The minimal free energy of local secondary structures in the cally picked 1,774,378 particles, which were extracted with
5 UTR was calculated by RNALfold (83). Then, the most neg- two-fold binning. After 2 rounds of 2D classification, 760,631
′
ative values for each transcript were selected as the most sta- particles were subjected to the initial 3D classification. A
ble structures. class representing 80S was selected (167,353 particles) and
further classified by the local 3D classification with a mask
Sample preparation for electron microscopy around the DHX29 density. The classes harboring DHX29
The human DHX29 coding sequence was cloned into the density (144,532 particles) were selected and re-extracted
pEBMulti-Neo vector (Wako) with an N-terminal His-tag and without rescaling, followed by 3D refinement and further 3D
transiently expressed in Expi293F cells (Thermo Fisher Sci- classification to select a class containing P-site tRNA and
entific). The cells were collected after 72 hours of cultivation DHX29. The selected class (111,574 particles) was subjected to
at 37°C and lysed in lysis buffer [20mM HEPES-KOH buffer 3D refinement, Bayesian polishing, CTF refinement, and an-
(pH 7.5), containing 100mM KCl, 2 mM Mg(OAc) , 10 mM other 3D refinement. The refined particles were subjected to
2
imidazole, 2 mM 2-ME, 0.5 mM ED TA, and 0.1% Triton X- local 3D classification with a mask on the tRNA-binding re-
100]. NaCl was added to the sample to a final concentration gion. We chose classes with clear P-site tRNA density (70,441
of 1 M, and the supernatant after centrifugation was passed particles) to select 80S with a peptidyl-tRNA stuck at the P
through a HiTrap SP HP column (Cytiva). The flow-through site. The selected particles were refined with 3D refinement
fractions were further purified by Ni-NTA resin (QIAGEN) followed by additional local 3D classification with a mask on
and passage through a HiTrap SP HP column (Cytiva), fol- the region around DHX29. The resulting class with strong
lowed by buffer exchange to 20 mM HEPES-KOH (pH 7.5), DHX29 density (35,668 particles) was subjected to 3D refine-
containing 100 mM KCl, 10% glycerol, 1 mM DTT, and 0.1 mM ment, Bayesian polishing, CTF refinement, and another 3D
EDTA, using a HiPrep 26/10 Desalting column (Cytiva). refinement. We also performed the local refinement with the
The factors required for cap-dependent in vitro transla- final class for the model building, using a mask containing
tion were basically prepared as described (44, 84), even DHX29.
though the capped PA-HA-uORF2-polyA lacking 2A was used For model building, the human 80S structure (PDB ID:
as the mRNA for in vitro translation. The uORF2-dependently 6Y2L) and the AlphaFold2 model of DHX29 were used as the
stalled human ribosome was purified using the PA-tag as de- initial models (48, 88). After the initial fitting of the models
scribed (43), and dissolved in 20 mM HEPES-KOH (pH 7.5) to the map using UCSF Chimera (89), the model refinement
containing 100 mM KCl, 5 mM Mg(OAc) , 1 mM DTT, 2 mM was performed with Phenix 1.19.2 (90) and Coot 0.9.8.92 (91).
2
spermidine, 0.06% digitonin, 10% glycerol, and 200 g/mL UCSF Chimera 1.15 (89) and UCSF ChimeraX 1.7.1 (92) were
μ
PA peptide. The purified DHX29 protein (1.06 M) was added used for molecular visualization.
μ
to the stalled 80S ribosome (45.5 nM) and incubated for 20 The statistics for image processing and refinement are
min at 37°C. summarized in table S13.
Cryo-EM data collection and image processing Electrophoretic mobility shift assay (EMSA)
The samples (3 L) were loaded onto Quantifoil R1.2/1.3 300 Purified DHX29 protein and synthetic RNA were used for
mesh copper grids (Quantifoil) with an additional in-house EMSA experiments. Wild-type or 9A mutant DHX29 were pu-
prepared contin μuous carbon layer, and plunged into liquid rified basically using the same protocol as for the cryo-EM
ethane using a Vitrobot Mark IV (Thermo Fisher Scientific) sample, except that the final buffer contained 2 mM magne-
with a 30 s. wait time and a 3 s. blot time. sium acetate. The RNA sequence was selected from mRNAs
Data acquisition was performed with a Krios G4 transmis- that are up-regulated under DHX29 deficiency, specifically
sion electron microscope (Thermo Fisher Scientific) operated choosing the TASOR mRNA. A 20-nucleotide RNA fragment
at 300kV and equipped with a K3 direct electron detector (5 -CCCUUUGGAGCUGGGAGUUG-3 ) was designed based
′ ′
(Gatan) at the RIKEN Yokohama cryo-EM facility, Japan. In on a peak observed in selective ribosome profiling and syn-
total, 1 2,501 micrographs were collected using the EPU soft- thesized with a Cy3 label at the 3 end (FASMAC). The reac-
′
ware (Thermo Fisher Scientific) with a total dose of 58e−/Å2 tion mixture contained 100 nM RNA, DHX29 protein at the
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 12
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
concentrations indicated in the figure, 13 mM HEPES-KOH trimmed and quality filtered using fastp (v0.21.0 4), and the
(pH 7.5), 67 mM KCl, 15% glycerol, 0.67 mM DTT, 0.23 mM UMI and barcode sequences were extracted using fastx-split
EDTA, 1.3 mM magnesium acetate, 0.1 g/L BSA, and 1 U/ L (https://github.com/ingolia-lab/RiboSeq). The reads were
μ
RNase inhibitor. Samples were incubated for 30 min. on ice then mapped to the list of noncoding RNAs and the un-
and subjected to electrophoresis on 12% polyacrylamide gels mapped reads were mapped to the human genome using
in 1×TBE buffer at 4°C. Detection was performed using an STAR (v2.7.0a), followed by duplicate removal using UMI-
ImageQuant LAS4000 system (Cytiva). Binding affinity was tools (v1.1.2). The A-site offset was predicted based on the
calculated based on the reduction of the free RNA band in- metagene analysis of the 5 ends of ribosome footprints. The
′
tensity using ImageJ (NIH). The dissociation constant (K ) A-site codon sequences from each sample were then extracted
d
was calculated by quadratic equation fitting. from the reads corresponding to 27-31 nt lengths. The
counted reads were normalized with the total reads, and the
ATPase assay relative reads of each codon for the DHX29-bound samples
ATPase assay was performed using BIOMOL Green (Enzo were divided by those for the input samples to calculate the
Life Sciences). Briefly, recombinant wild-type or D702A mu- fold enrichment of each codon upon the DHX29 immunopre-
tant DHX29 (12.5 nM), which were purified by the same pro- cipitation. These values were defined as the DHX29 codon
tocol as for EMSA samples, was incubated at 37°C in reaction enrichment score (CES) and used for the downstream anal-
buffer (25mM HEPES-KOH (pH7.5), 50mM potassium ace- yses. DHX29 occupancy was calculated by multiplying the
tate, 5mM DTT, 5mM magnesium acetate, 0.2 mM ATP, 250 CES of each codon by its frequency in the transcript and sum-
nM cappe d mRNA used for cryo-EM a nalysis, and 1 U/ L ming the values across all codons.
μ
RNase inhibitor). Then the absorbance at 620 nm of the re-
action was detected using Nivo (PerkinElmer). Phosphate tRNA sequencing
concentrations were determined from absorbance values us- tRNA sequencing was performed as described previously
ing a calibration curve generated with phosphate standards. (94). Briefly, 40 g of total RNA was deacylated in 100 mM
μ
CHES-NaOH (pH 9.0) at 37°C for 30 min and purified by eth-
Selective Thor-Ribo-Seq anol precipitation. The deacylated RNAs were then incubated
HEK293T cells were transfected with the pFLAG-DHX29-WT with the recombinant AlkB WT (1.5 M) and L118V D135S (0.1
μ
vector. The lysates from the transfected cells were then pre- M) in the presence of 1 mM -ketoglutarate, 2 mM L-ascor-
μ α
pared as described in the in-cell DSP Crosslinking section. bic acid, and 50 M (NH )Fe(SO ) in 50 mM HEPES-KOH
μ 4 2 4 2
Next, the lysates were treated with RNase I (50 U/mL, Luci- (pH 8.1) at 37°C for 1 hour, followed by phenol/chloroform
gen) at 25°C for 45 min, followed by SUPERase•In RNase in- extraction and ethanol precipitation. RNAs were further in-
hibitor (0.5 U/ L) on ice. Aliquots of the lysates were then cubated with 10 U of T4 polynucleotide kinase (New England
μ
removed and used for input. The lysates were overlayed onto BioLabs) at 37°C for 1 hour, and purified using RNA Clean &
a sucrose cushion (1 M sucrose, 20 mM Tris-HCl (pH 7.5), 150 Concentrator-5. The samples were separated on 10% 7 M urea
mM NaCl, 5 mM MgCl , 1 mM DTT, 20 U/mL SUPERase•In gels and the bands corresponding to tRNAs were excised and
2
RNase inhibitor, 100 g/mL chloramphenicol, and 100 subjected to gel-extraction. tRNA samples were ligated with
μ
g/mL cycloheximide) and ultracentrifuged with a Type 70Ti adenylated adaptors using T4 RNA Ligase 2, truncated KQ
μ
rotor and Optima XE-100 (Beckman Coulter) at 45,000 rpm (New England BioLabs), followed by gel-purification. The
and 4°C for 3 hours 50 min. The supernatants were dis- samples were reverse-transcribed using TGIRT-III (InGex)
carded, and the pellets were resuspended in Lysis buffer. The and subjected to alkaline hydrolysis. The samples were circu-
samples were pre-cleared with Dynabeads Protein G at 4°C larized using CircLigase II (Lucigen) and purified, and sub-
for 1 hour with gentle rotation. The lysates were then mixed jected to PCR amplification using Phusion Polymerase
with Dynabeads Protein G preincubated with the anti-FLAG (Thermo Fisher Scientific). Sequencing was performed using
antibody and incubated at 4°C for 3 hours with gentle rota- a NextSeq 500 Sequencer and a NextSeq 500/550 Mid-Output
tion. Afterwards, the beads were washed and mixed with TRI- v2 Kit (150 cycles, Illumina).
zol (Thermo Fisher Scientific). The sequenced reads were trimmed using cutadapt (v2.3).
Thor-Ribo-Seq was performed as described previously The UMI sequences (17 nt, N14D3) attached to the 5 end of
′
(50). The oligonucleotides used in the library preparation tRNA sequences were then removed and recorded as UMI
have been described previously (50). The bands correspond- tags by fastp (v0.20.1). The reads were quality-filtered using
ing to 17-34 nt were excised and used for the library prepara- trimmomatic (v0.39), and then aligned to the human tRNA
tion. sequences obtained from GtRNAdb
The sequenced reads were analyzed by the standard Ribo- (https://gtrnadb.ucsc.edu/) using bowtie (v2.3.4.3) with the
seq pipeline, as described previously (93). Briefly, reads were very sensitive local mode and -L 10. PCR duplicates were
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 13
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
removed using the UMI tag by UMICollapse (v1.0.0). The 5. K. N. D’Orazio, R. Green, Ribosome states signal RNA quality control. Mol. Cell 81,
mapped read numbers on each tRNA gene were counted by 1372–1383 (2021). doi:10.1016/j.molcel.2021.02.022 Medline
6. F. Supek, B. Lehner, R. G. H. Lindeboom, To NMD or Not To NMD: Nonsense-
samtools (v1.5).
Mediated mRNA Decay in Cancer and Other Genetic Diseases. Trends Genet. 37,
657–668 (2021). doi:10.1016/j.tig.2020.11.002 Medline
Luciferase reporter assay 7. M. Yoshinaga, O. Takeuchi, Regulation of inflammatory diseases via the control of
Luciferase reporter assays were performed as described pre- mRNA decay. Inflamm. Regen. 44, 14 (2024). doi:10.1186/s41232-024-00326-5
Medline
viously (72). For the frameshift reporter assay, control and
8. H. Bae, J. Coller, Codon optimality-mediated mRNA degradation: Linking
DHX29-deficient HEK293T cells were transfected with pmir- translational elongation to mRNA stability. Mol. Cell 82, 1467–1476 (2022).
GLO vectors. For the analysis of the effect of AU-rich 3 UTR doi:10.1016/j.molcel.2022.03.032 Medline
′
sequences, HEK293T cells were transfected with firefly lucif- 9. F. Hia, O. Takeuchi, The effects of codon bias and optimality on mRNA and protein
regulation. Cell. Mol. Life Sci. 78, 1909–1928 (2021). doi:10.1007/s00018-020-
erase reporter plasmids (pGL3 vectors) harboring AU-rich 3
′ 03685-7 Medline
UTR sequences, together with the plasmid expressing Renilla 10. Q. Wu, A. A. Bazzini, Translation and mRNA Stability Control. Annu. Rev. Biochem.
luciferase as an internal control. Then, the cells were lysed, 92, 227–245 (2023). doi:10.1146/annurev-biochem-052621-091808 Medline
and luciferase activities were measured using the Dual-Lucif- 11. T. Tuller, A. Carmi, K. Vestsigian, S. Navon, Y. Dorfan, J. Zaborske, T. Pan, O. Dahan,
I. Furman, Y. Pilpel, An evolutionarily conserved mechanism for controlling the
erase Reporter Assay System and a GloMax Discover or Multi
efficiency of protein translation. Cell 141, 344–354 (2010).
Microplate Reader (Promega). doi:10.1016/j.cell.2010.03.031 Medline
12. E. M. Novoa, L. Ribas de Pouplana, Speeding with control: Codon usage, tRNAs,
Proximity ligation assay (PLA) and ribosomes. Trends Genet. 28, 574–581 (2012). doi:10.1016/j.tig.2012.07.006
Medline PLA was performed using the Duolink In Situ PLA Kit (Sigma
13. Y. Liu, Q. Yang, F. Zhao, Synonymous but Not Silent: The Codon Usage Code for
Aldrich) according to the manufacturer’s instructions. Gene Expression and Protein Folding. Annu. Rev. Biochem. 90, 375–401 (2021).
Briefly, FLAG-DHX29-expressing HEK293T cells were doi:10.1146/annurev-biochem-071320-112701 Medline
treated with Dox (1 g/mL) or mock control for 24 hours, 14. D. Chu, E. Kazana, N. Bellanger, T. Singh, M. F. Tuite, T. von der Haar, Translation
μ elongation can control translation initiation on eukaryotic mRNAs. EMBO J. 33,
then fixed with 4% paraformaldehyde phosphate buffer solu-
21–34 (2014). doi:10.1002/embj.201385651 Medline
tion at room temperature for 15 min. Cells were permea- 15. C. L. Barrington, G. Galindo, A. L. Koch, E. R. Horton, E. J. Morrison, S. Tisa, T. J.
bilized with 0.5% Triton X-100 in DPBS at room temperature Stasevich, O. S. Rissland, Synonymous codon usage regulates translation
for 10 min and blocked with Duolink Blocking Solution at initiation. Cell Rep. 42, 113413 (2023). doi:10.1016/j.celrep.2023.113413 Medline
16. F. Hia, S. F. Yang, Y. Shichino, M. Yoshinaga, Y. Murakawa, A. Vandenbon, A. Fukao,
37°C for 1 hour in a humidified chamber. Samples were incu-
T. Fujiwara, M. Landthaler, T. Natsume, S. Adachi, S. Iwasaki, O. Takeuchi, Codon
bated with mouse anti-FLAG (M2, Sigma Aldrich) and rabbit bias confers stability to human mRNAs. EMBO Rep. 20, e48220 (2019).
anti-GIGYF2 (Proteintech, #24790-1-AP) antibodies at 4°C doi:10.15252/embr.201948220 Medline
overnight, followed by incubation with anti-rabbit PLUS and 17. Q. Wu, S. G. Medina, G. Kushawah, M. L. DeVore, L. A. Castellano, J. M. Hand, M.
Wright, A. A. Bazzini, Translation affects mRNA stability in a codon-dependent
anti-mouse MINUS PLA probes at 37°C for 1 hour. The liga-
manner in human cells. eLife 8, e45396 (2019). doi:10.7554/eLife.45396 Medline
tion and amplification reactions were performed at 37°C for 18. A. Narula, J. Ellis, J. M. Taliaferro, O. S. Rissland, Coding regions affect mRNA
30 min and 100 min, respectively. After washing, samples stability in human cells. RNA 25, 1751–1764 (2019). doi:10.1261/rna.073239.119
were mounted with Duolink PLA Mounting Medium with Medline
19. Y. Mishima, Y. Tomari, Codon Usage and 3′ UTR Length Determine Maternal mRNA
DAPI. Images were acquired using a Leica TCS SPE confocal
Stability in Zebrafish. Mol. Cell 61, 874–885 (2016).
microscope and analyzed with ImageJ (v1.51r). doi:10.1016/j.molcel.2016.02.027 Medline
20. Y. Harigaya, R. Parker, Analysis of the association between codon optimality and
mRNA stability in Schizosaccharomyces pombe. BMC Genomics 17, 895 (2016).
Statistical analysis
doi:10.1186/s12864-016-3237-6 Medline
Statistical analyses were performed using Prism v.8.2.1 or
21. G. Boël, R. Letso, H. Neely, W. N. Price, K.-H. Wong, M. Su, J. Luff, M. Valecha, J. K.
v10.4.1 (GraphPad), unless otherwise specified. Statistical sig- Everett, T. B. Acton, R. Xiao, G. T. Montelione, D. P. Aalberts, J. F. Hunt, Codon
nificance was calculated with the two-tailed Student’s t test. influence on protein expression in E. coli correlates with mRNA levels. Nature 529,
P values less than 0.05 were considered significant. 358–363 (2016). doi:10.1038/nature16509 Medline
22. V. Presnyak, N. Alhusaini, Y.-H. Chen, S. Martin, N. Morris, N. Kline, S. Olson, D.
REFERENCES AND NOTES Weinberg, K. E. Baker, B. R. Graveley, J. Coller, Codon optimality is a major
1. L. Monaghan, D. Longman, J. F. Cáceres, Translation-coupled mRNA quality control determinant of mRNA stability. Cell 160, 1111–1124 (2015).
mechanisms. EMBO J. 42, e114378 (2023). doi:10.15252/embj.2023114378 doi:10.1016/j.cell.2015.02.029 Medline
Medline 23. N. T. Ingolia, L. F. Lareau, J. S. Weissman, Ribosome profiling of mouse embryonic
2. A. M. Heck, J. Wilusz, The Interplay between the RNA Decay and Translation stem cells reveals the complexity and dynamics of mammalian proteomes. Cell
Machinery in Eukaryotes. Cold Spring Harb. Perspect. Biol. 10, a032839 (2018). 147, 789–802 (2011). doi:10.1016/j.cell.2011.10.002 Medline
doi:10.1101/cshperspect.a032839 Medline 24. C. Mordstein, R. Savisaar, R. S. Young, J. Bazile, L. Talmane, J. Luft, M. Liss, M. S.
3. T. Kurosaki, M. W. Popp, L. E. Maquat, Quality and quantity control of gene Taylor, L. D. Hurst, G. Kudla, Codon Usage and Splicing Jointly Influence mRNA
expression by nonsense-mediated mRNA decay. Nat. Rev. Mol. Cell Biol. 20, 406– Localization. Cell Syst. 10, 351–362.e8 (2020). doi:10.1016/j.cels.2020.03.001
420 (2019). doi:10.1038/s41580-019-0126-2 Medline Medline
4. T. Inada, Quality controls induced by aberrant translation. Nucleic Acids Res. 48, 25. M. A. Takata, D. Gonçalves-Carneiro, T. M. Zang, S. J. Soll, A. York, D. Blanco-Melo,
1084–1096 (2020). doi:10.1093/nar/gkz1201 Medline P. D. Bieniasz, CG dinucleotide suppression enables antiviral defence targeting
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 14
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
non-self RNA. Nature 550, 124–127 (2017). doi:10.1038/nature24039 Medline doi:10.1016/j.celrep.2020.107610 Medline
26. M. Courel, Y. Clément, C. Bossevain, D. Foretek, O. Vidal Cruchez, Z. Yi, M. Bénard, 43. T. Yokoyama, K. Machida, W. Iwasaki, T. Shigeta, M. Nishimoto, M. Takahashi, A.
M.-N. Benassy, M. Kress, C. Vindry, M. Ernoult-Lange, C. Antoniewski, A. Morillon, Sakamoto, M. Yonemochi, Y. Harada, H. Shigematsu, M. Shirouzu, H. Tadakuma,
P. Brest, A. Hubstenberger, H. Roest Crollius, N. Standart, D. Weil, GC content H. Imataka, T. Ito, HCV IRES Captures an Actively Translating 80S Ribosome. Mol.
shapes mRNA storage and decay in human cells. eLife 8, e49708 (2019). Cell 74, 1205–1214.e8 (2019). doi:10.1016/j.molcel.2019.04.022 Medline
doi:10.7554/eLife.49708 Medline 44. K. Machida, T. Shigeta, Y. Yamamoto, T. Ito, Y. Svitkin, N. Sonenberg, H. Imataka,
27. A. Radhakrishnan, Y.-H. Chen, S. Martin, N. Alhusaini, R. Green, J. Coller, The Dynamic interaction of poly(A)-binding protein with the ribosome. Sci. Rep. 8,
DEAD-Box Protein Dhh1p Couples mRNA Decay and Translation by Monitoring 17435 (2018). doi:10.1038/s41598-018-35753-1 Medline
Codon Optimality. Cell 167, 122–132.e9 (2016). doi:10.1016/j.cell.2016.08.053 45. J. P. Alderete, S. Jarrahian, A. P. Geballe, Translational effects of mutations and
Medline polymorphisms in a repressive upstream open reading frame of the human
28. M. W. Webster, Y.-H. Chen, J. A. W. Stowell, N. Alhusaini, T. Sweet, B. R. Graveley, cytomegalovirus UL4 gene. J. Virol. 73, 8330–8337 (1999).
J. Coller, L. A. Passmore, mRNA Deadenylation Is Coupled to Translation Rates by doi:10.1128/JVI.73.10.8330-8337.1999 Medline
the Differential Activities of Ccr4-Not Nucleases. Mol. Cell 70, 1089–1100.e8 46. A. des Georges, V. Dhote, L. Kuhn, C. U. T. Hellen, T. V. Pestova, J. Frank, Y.
(2018). doi:10.1016/j.molcel.2018.05.033 Medline Hashem, Structure of mammalian eIF3 in the context of the 43S preinitiation
29. R. Buschauer, Y. Matsuo, T. Sugiyama, Y.-H. Chen, N. Alhusaini, T. Sweet, K. complex. Nature 525, 491–495 (2015). doi:10.1038/nature14891 Medline
Ikeuchi, J. Cheng, Y. Matsuki, R. Nobuta, A. Gilmozzi, O. Berninghausen, P. Tesina, 47. D. Cui, T. Pestova, C. Hellen, A. des Georges, The translation initiation factor
T. Becker, J. Coller, T. Inada, R. Beckmann, The Ccr4-Not complex monitors the DHX29 appears to pull on mRNA in a direction opposite to scanning. bioRxiv,
translating ribosome for codon optimality. Science 368, eaay6912 (2020). 2025.2007.2013.664561 (2025).
doi:10.1126/science.aay6912 Medline 48. V. Bhaskar, A. Graff-Meyer, A. D. Schenk, S. Cavadini, O. von Loeffelholz, S. K.
30. E. Absmeier, V. Chandrasekaran, F. J. O’Reilly, J. A. W. Stowell, J. Rappsilber, L. A. Natchiar, C. G. Artus-Revel, H.-R. Hotz, G. Bretones, B. P. Klaholz, J. A. Chao,
Passmore, Specific recognition and ubiquitination of translating ribosomes by Dynamics of uS19 C-Terminal Tail during the Translation Elongation Cycle in
mammalian CCR4-NOT. Nat. Struct. Mol. Biol. 30, 1314–1322 (2023). Human Ribosomes. Cell Rep. 31, 107473 (2020).
doi:10.1038/s41594-023-01075-8 Medline doi:10.1016/j.celrep.2020.03.037 Medline
31. X. Zhu, V. E. Cruz, H. Zhang, J. P. Erzberger, J. T. Mendell, Specific tRNAs promote 49. M. Holm, S. K. Natchiar, E. J. Rundlet, A. G. Myasnikov, Z. L. Watson, R. B. Altman,
mRNA decay by recruiting the CCR4-NOT complex to translating ribosomes. H.-Y. Wang, J. Taunton, S. C. Blanchard, mRNA decoding in human is kinetically
Science 386, eadq8587 (2024). doi:10.1126/science.adq8587 Medline and structurally distinct from bacteria. Nature 617, 200–207 (2023).
32. S. L. Zebedee, D. S. Barritt, W. C. Raschke, Comparison of mouse Ly5a and Ly5b doi:10.1038/s41586-023-05908-w Medline
leucocyte common antigen alleles. Dev. Immunol. 1, 243–254 (1991). Medline 50. M. Mito, Y. Shichino, S. Iwasaki, Thor-Ribo-Seq: ribosome profiling tailored for low
33. D. W. Morgens, R. M. Deans, A. Li, M. C. Bassik, Systematic comparison of input with RNA-dependent RNA amplification. bioRxiv, 2023.2001.2015.524129
CRISPR/Cas9 and RNAi screens for essential genes. Nat. Biotechnol. 34, 634– (2023).
636 (2016). doi:10.1038/nbt.3567 Medline 51. M. dos Reis, R. Savva, L. Wernisch, Solving the riddle of codon usage preferences:
34. V. P. Pisareva, A. V. Pisarev, A. A. Komar, C. U. Hellen, T. V. Pestova, Translation A test for translational selection. Nucleic Acids Res. 32, 5036–5044 (2004).
initiation on mammalian mRNAs with structured 5'UTRs requires DExH-box doi:10.1093/nar/gkh834 Medline
protein DHX29. Cell 135, 1237–1250 (2008). doi:10.1016/j.cell.2008.10.037 52. M. E. Forrest, O. Pinkard, S. Martin, T. J. Sweet, G. Hanson, J. Coller, Codon and
Medline amino acid content are associated with mRNA stability in mammalian cells. PLOS
35. T. R. Sweeney, V. Dhote, E. Guca, C. U. T. Hellen, Y. Hashem, T. V. Pestova, ONE 15, e0228730 (2020). doi:10.1371/journal.pone.0228730 Medline
Functional role and ribosomal position of the unique N-terminal region of DHX29, 53. R. Weber, M.-Y. Chung, C. Keskeny, U. Zinnall, M. Landthaler, E. Valkov, E.
a factor required for initiation on structured mammalian mRNAs. Nucleic Acids Izaurralde, C. Igreja, 4EHP and GIGYF1/2 Mediate Translation-Coupled Messenger
Res. 49, 12955–12969 (2021). doi:10.1093/nar/gkab1192 Medline RNA Decay. Cell Rep. 33, 108262 (2020). doi:10.1016/j.celrep.2020.108262
36. V. Dhote, T. R. Sweeney, N. Kim, C. U. Hellen, T. V. Pestova, Roles of individual Medline
domains in the function of DHX29, an essential factor required for translation of 54. D. Peter, R. Weber, F. Sandmeir, L. Wohlbold, S. Helms, P. Bawankar, E. Valkov, C.
structured mammalian mRNAs. Proc. Natl. Acad. Sci. U.S.A. 109, E3150–E3159 Igreja, E. Izaurralde, GIGYF1/2 proteins use auxiliary sequences to selectively bind
(2012). doi:10.1073/pnas.1208014109 Medline to 4EHP and repress target mRNA expression. Genes Dev. 31, 1147–1161 (2017).
37. Y. Hashem, A. des Georges, V. Dhote, R. Langlois, H. Y. Liao, R. A. Grassucci, C. U. doi:10.1101/gad.299420.117 Medline
T. Hellen, T. V. Pestova, J. Frank, Structure of the mammalian ribosomal 43S 55. K. L. Hickey, K. Dickson, J. Z. Cogan, J. M. Replogle, M. Schoof, K. N. D’Orazio, N.
preinitiation complex bound to the scanning factor DHX29. Cell 153, 1108–1119 K. Sinha, J. A. Hussmann, M. Jost, A. Frost, R. Green, J. S. Weissman, K. K.
(2013). doi:10.1016/j.cell.2013.04.036 Medline Kostova, GIGYF2 and 4EHP Inhibit Translation Initiation of Defective Messenger
38. A. Parsyan, D. Shahbazian, Y. Martineau, E. Petroulakis, T. Alain, O. Larsson, G. RNAs to Assist Ribosome-Associated Quality Control. Mol. Cell 79, 950–962.e6
Mathonnet, G. Tettweiler, C. U. Hellen, T. V. Pestova, Y. V. Svitkin, N. Sonenberg, (2020). doi:10.1016/j.molcel.2020.07.007 Medline
The helicase protein DHX29 promotes translation initiation, cell proliferation, and 56. N. K. Sinha, A. Ordureau, K. Best, J. A. Saba, B. Zinshteyn, E. Sundaramoorthy, A.
tumorigenesis. Proc. Natl. Acad. Sci. U.S.A. 106, 22217–22222 (2009). Fulzele, D. M. Garshott, T. Denk, M. Thoms, J. A. Paulo, J. W. Harper, E. J. Bennett,
doi:10.1073/pnas.0909773106 Medline R. Beckmann, R. Green, EDF1 coordinates cellular responses to ribosome
39. N. Sugimoto, H. Mitoma, T. Kim, S. Hanabuchi, Y. J. Liu, Helicase proteins DHX29 collisions. eLife 9, e58828 (2020). doi:10.7554/eLife.58828 Medline
and RIG-I cosense cytosolic nucleic acids in the human airway system. Proc. Natl. 57. S. Juszkiewicz, G. Slodkowicz, Z. Lin, P. Freire-Pritchett, S.-Y. Peak-Chew, R. S.
Acad. Sci. U.S.A. 111, 7747–7752 (2014). doi:10.1073/pnas.1400139111 Medline Hegde, Ribosome collisions trigger cis-acting feedback inhibition of translation
40. Q. Zhu, P. Tan, Y. Li, M. Lin, C. Li, J. Mao, J. Cui, W. Zhao, H. Y. Wang, R.-F. Wang, initiation. eLife 9, e60038 (2020). doi:10.7554/eLife.60038 Medline
DHX29 functions as an RNA co-sensor for MDA5-mediated EMCV-specific 58. E. Rom, H. C. Kim, A.-C. Gingras, J. Marcotrigiano, D. Favre, H. Olsen, S. K. Burley,
antiviral immunity. PLOS Pathog. 14, e1006886 (2018). N. Sonenberg, Cloning and characterization of 4EHP, a novel mammalian eIF4E-
doi:10.1371/journal.ppat.1006886 Medline related cap-binding protein. J. Biol. Chem. 273, 13104–13109 (1998).
41. K. Akaki, T. Mino, O. Takeuchi, DSP-crosslinking and Immunoprecipitation to doi:10.1074/jbc.273.21.13104 Medline
Isolate Weak Protein Complex. Bio Protoc. 12, e4478 (2022). 59. I. Topisirovic, Y. V. Svitkin, N. Sonenberg, A. J. Shatkin, Cap and cap-binding
doi:10.21769/BioProtoc.4478 Medline proteins in the control of gene expression. Wiley Interdiscip. Rev. RNA 2, 277–298
42. P. Han, Y. Shichino, T. Schneider-Poetsch, M. Mito, S. Hashimoto, T. Udagawa, K. (2011). doi:10.1002/wrna.52 Medline
Kohno, M. Yoshida, Y. Mishima, T. Inada, S. Iwasaki, Genome-wide Survey of 60. V. Ruscica, P. Bawankar, D. Peter, S. Helms, C. Igreja, E. Izaurralde, Direct role for
Ribosome Collision. Cell Rep. 31, 107610 (2020). the Drosophila GIGYF protein in 4EHP-mediated mRNA repression. Nucleic Acids
First release: 19 March 2026 science.org (Page numbers not final at time of first release) 15
Downloaded
from
https://www.science.org
at
Tsinghua
University
on
March
24,
2026
