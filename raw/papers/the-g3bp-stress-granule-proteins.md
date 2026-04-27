---
source_path: /mnt/c/Users/Administrator/Zotero/storage/VMBW3EHN/Smith和Bartel - 2026 - The G3BP stress-granule proteins reinforce the integrated stress response translation programme.pdf
ingested: 2026-04-23
sha256: ed95295f31c25d45
---

nature cell biology
Article https://doi.org/10.1038/s41556-025-01834-3
The G3BP stress-granule proteins
reinforce the integrated stress response
translation programme
Received: 31 July 2025 Jarrett Smith 1,2,3 & David P. Bartel 1,2,3
Accepted: 31 October 2025
When mammalian cells are exposed to stress, they co-ordinate the
Published online: 19 December 2025
condensation of stress granules (SGs) through the action of proteins G3BP1
Check for updates
and G3BP2 (G3BPs) and, simultaneously, undergo a massive reduction in
translation. Although SGs and G3BPs have been linked to this translation
response, their overall impact has been unclear. Here we investigate the
question of how, and indeed whether, G3BPs and SGs shape the stress
translation response. We find that SGs are enriched for mRNAs that are
resistant to the stress-induced translation shutdown. Although the accurate
recruitment of these stress-resistant mRNAs does require the context of
stress, a combination of optogenetic tools and spike-normalized ribosome
profiling demonstrates that G3BPs and SGs are necessary and sufficient
to both help prioritize the translation of their enriched mRNAs and help
suppress cytosolic translation. Together, these results support a model
in which G3BPs and SGs reinforce the stress translation programme by
prioritizing the translation of their resident mRNAs.
When exposed to stresses, such as oxidative stress, high temperature during the ISR20,24,25. However, G3BP-knockout (KO) cell lines, which
and harmful chemicals, cells initiate the integrated stress response lack microscopically visible SGs, still undergo the eif2α-dependent
(ISR)1–4. The ISR integrates signals from different stress sensors to translation reduction associated with the ISR16,26.
converge on the phosphorylation of translation initiation factor As the formation of SGs is enhanced by polysome collapse, and
eif2α1–5, which causes reduced global translation while allowing selec- SGs are enriched in small ribosomal subunits but not large riboso-
tive translation of stress-responsive mRNAs that help cope with the mal subunits, SGs are also proposed to simply be sites devoid of
stress2,4,6–9. During this dramatic alteration of the translation state, translation1,2,10,20,27,28. However, single-molecule analyses show that
cytoplasmic puncta known as stress granules (SGs) form through the translating mRNAs are not forbidden inside of SGs29, and some report
process of liquid–liquid phase separation1,6,10–15. These granules are that translation inside of SGs might not be a rare event compared with
non-membrane-bound collections of RNA-binding proteins, mRNAs translation in the cytosol30.
and translation machinery1,11,16–19. Although SGs contain a diverse pro- Despite their many connections to translation and the stress
teome, their formation requires the RNA-binding proteins G3BP1 and response, the overall impact that G3BPs and SGs have on transla-
G3BP2 (G3BPs)12,16. Both SGs and G3BPs have been hypothesized to tion during stress, or indeed whether they have any impact, is not
play roles in translation16,20–23, but their precise impacts are not well fully understood10,31–33. Previous attempts to determine the effects
understood. of G3BPs or SGs on translation have relied either on bulk meas-
As they are highly enriched for translation machinery and form urements of translation with limited sensitivity and specificity,
concurrently with translation shutdown, SGs were originally hypoth- such as 35S-labelling of nascent peptides, or have been restricted
esized to be required for the dramatic translation shutdown observed to observations of single mRNAs and reporters16,21,30. Here, we use
1Howard Hughes Medical Institute, Cambridge, MA, USA. 2Whitehead Institute for Biomedical Research, Cambridge, MA, USA. 3Department of Biology,
Massachusetts Institute of Technology, Cambridge, MA, USA. e-mail: dbartel@wi.mit.edu
Nature Cell Biology | Volume 28 | January 2026 | 135–148 135
Article https://doi.org/10.1038/s41556-025-01834-3
a
AAAAAA
5
AAAAAA
AAAAAA
0
AAAAAA
–5
0 5 10 15
spike-normalized ribosome profiling and optogenetic methods to mRNA, which could then be spiked into each sample (Fig. 1a and
measure the impact of G3BPs and SGs on translation with or without Extended Data Fig. 1a).
stress. These results support a model in which G3BPs and SGs rein- Using our ribo-spike, we then compared translation between
force the ISR translation programme by prioritizing the translation unstressed cells and cells treated with 500 µM sodium arsenite for
of their most enriched transcripts. 1 h. This dose of sodium arsenite activates the ISR, leading to eif2α
phosphorylation and a substantial reduction in global translation16,20.
Results By normalizing to the spike-in TE across samples, we were able to meas-
Ribo-spike enables observation of absolute translation ure absolute changes in TE for mRNAs of >10,000 individual genes.
changes during the ISR Aggregating these measurements revealed a drastic (20 fold) reduc-
Global changes to translation, such as those observed during the ISR, tion in global TE, consistent with previous bulk measurements16,36,37
have been challenging to observe by ribosome profiling, which typi- (Fig. 1b and Extended Data Fig. 1b,c). Interestingly, TEs of mitochondrial
cally lacks information on the absolute differences between samples34. mRNAs increased in the presence of sodium arsenite (Fig. 1b), validating
RNA spike ins typically used to quantify absolute differences in other our concern that they might not remain constant under stress.
high-throughput approaches are not appropriate for ribosome pro- Although translation was globally reduced during stress, some
filing, as the RNAse treatment used to create ribosome-protected mRNAs retained or even enhanced their translation in response to
fragments (RPFs) would destroy the unprotected spike molecules. stress. Among them were mRNAs of several stress-responsive genes
Normalizing to endogenous mitochondrial RPFs can bypass this previously reported to maintain their translation during the ISR,
problem34,35. However, this approach assumes that mitochondrial including ATF4, ATF5, CEBPα and DDIT3/CHOP (Fig. 1b). Many of these
translation is unaffected by the experimental condition—an assump- mRNAs contain upstream open reading frames (uORFs), which can
tion that does not always hold, especially if cells are subjected to stress. help regulate their translation during stress38. Indeed, regulation by
To use ribosome profiling to measure absolute changes to translation uORFs is proposed to help shape the general translation response to
efficiency (TE) occurring as a consequence of stress, we developed a stress2,4,7,8,39–41. Supporting this proposal, mRNAs reported to contain
ribosome profiling spike in (ribo-spike) consisting of a defined amount one or more functional uORFs were significantly better translated dur-
of rabbit reticulocyte lysate translating orthogonal firefly luciferase ing the stress response42 (Extended Data Fig. 1d). Moreover, while our
Nature Cell Biology | Volume 28 | January 2026 | 135–148 136
)dessertsnu/desserts(gol
egnahc
ET
2
b
Stress enhanced (71)
ATF4/5
CEBPα Stress resistant (263)
Endogenous Mitochondrially translated EN1 DDIT3/CHOP
mRNAs (13) FOXF1 HSPA5
HSPE1
IER3
Ribo-spike LSM7
Stress hypersensitive (62)
CSDE1
RNAse PCBP2
digestion COPS3/6
CLTC
Arsenite stress SCFD1
Ribosomes n = 10,677
protecting mRNA
fragments
mRNA expression (mean normalized counts)
c
Stress enhanced (158)
Ribosome
ATF4/5
removal Stress resistant (175)
Mitochondrially translated HSPE1 HSPA5
mRNAs (13) CEBPα IER3
RPFs 5 EN1/2 LSM3
DDIT3/CHOP
LSM7
MYEOV
0
Stress hypersensitive (52)
CSDE1
PCBP2
–5 CLTC
VSP4A
Heat shock
n = 11,104
0 5 10 15
mRNA expression (mean normalized counts)
)dessertsnu/desserts(gol
egnahc
ET
2
Fig. 1 | Ribo-spike enables observation of absolute translation changes cells responding to 500 µM sodium arsenite (for 1 h) as a function of the mRNA
during ISR. a, A schematic representation of the ribo-spike. The ribo-spike expression. The dashed red line indicates unchanged TE, as determined by the
consists of polysomes formed on an orthogonal mRNA sequence, in this case, ribo-spike. Points for stress-enhanced, stress-resistant and stress-hypersensitive
firefly luciferase mRNA (fLuc) translated in a rabbit reticulocyte lysate. A mRNAs are indicated by colours, with exemplar mRNAs listed for each category.
defined amount of the ribo-spike sample is added to each experimental sample, Stress response categories were determined by DESeq2 (log FC >1, adjusted
2
ultimately generating orthogonal RPFs that enable normalization between P value <0.05). Mitochondrially translated mRNAs are indicated in orange.
samples. b, The ISR translation programme induced upon arsenite stress. n indicates the number of unique mRNAs. c, The ISR translation programme
Plotted for each mRNA is the log fold change (FC) in TE observed in HCT116 induced upon heat shock (45 °C for 25 min), otherwise as in a.
2
Article https://doi.org/10.1038/s41556-025-01834-3
manuscript was in review, another study published the development measurements separately. Interestingly, changes to RPFs and mRNA
of a similar ribo-spike and also applied it to show that uORF-containing levels both contributed to the overall TE effects, with the presence
mRNAs are better translated during stress41. of G3BPs leading to more RPFs of ISR-enhanced transcripts despite a
In yeast, newly transcribed mRNAs tend to be preferentially reduction in the levels of these transcripts (Extended Data Fig. 2c,d).
translated during stress43,44. To assess this possibility in mammalian Although these G3BP-dependent decreases in mRNA might represent
cells, we compared the translation change in response to stress to an independent function of G3BPs, they are perhaps more parsimoni-
mRNA half-lives, reasoning that mRNAs with short half-lives would ously explained as the translation-dependent destabilization of mRNA,
be predominantly composed of newly synthesized transcripts. Con- which has been previously reported49–54. Indeed, we also observed
sistent with the observations made in yeast, we observed a moderate evidence of such mRNA stabilization occurring transcriptome-wide in
negative correlation between the translation change of an mRNA response to arsenite stress (Extended Data Fig. 2e). However, the previ-
upon stress and its estimated half-life45 (Spearman R (R) of −0.22; ously observed correlation between translation change upon stress
S
Extended Data Fig. 1e). and unstressed mRNA half-lives might complicate this interpretation
At the other extreme, some mRNAs were especially sensitive to (Extended Data Fig. 1e).
translation shutdown, including CSDE1 and PCBP2, as reported previ- Given that the ISR translation programmes differed between
ously40. Interestingly, other hypersensitive mRNAs encoded proteins arsenite and heat shock, we examined whether G3BPs also reinforced
involved in energetically expensive processes, such as vesicle traffick- the heat shock ISR translation programme and found similar results
ing (COPS3, COPS6, CLTC and SCFD1), which are strongly downregulated (Fig. 2j and Extended Data Fig. 2f–j). Furthermore, analyses of published
during stress46 (Fig. 1b). measurements of G3BP-dependent translation in U2OS cells treated
To measure absolute TE changes in another stress context, we with the endoplasmic reticulum stressor thapsigargin, also yielded
performed analogous experiments under 45 °C heat shock (Fig. 1c similar results55 (Extended Data Fig. 3a–e). Taken together, these results
and Extended Data Fig. 1b,c). The results resembled those observed indicated that G3BPs, and perhaps SGs, reinforce the ISR translation
for arsenite stress (Fig. 1c and Extended Data Fig. 1f,g). However, the programme across multiple stresses and cell types.
translation changes were not identical (R of 0.63) and many mRNAs We next asked whether the factors correlating with ISR trans-
S
were called as differentially regulated in one stress but not the other lation—uORF presence and estimated mRNA half-lives—also corre-
(Extended Data Fig. 1h–j), consistent with previous reports that the lated with G3BP-dependent translation during both arsenite stress
type and dosage of stress shape the ISR3. and heat shock. However, we found no strong relationship between
We consider the combination of widespread translation shutdown, either of these factors and G3BP-dependent translation (Extended
the retained or increased translation of select transcripts and the hyper- Data Fig. 4a–d).
sensitive downregulated translation of others to be the ISR translation To determine whether the G3BP-dependent translation was
programme. These results illustrate how using ribo-spike enables accu- constitutive or stress specific—potentially through the formation of
rate and precise monitoring of absolute translation changes between SGs—we performed analogous ribosome profiling experiments, com-
samples and emphasize the utility of a truly orthogonal spike-in for paring translation in cells with and without G3BPs, but this time in the
studies monitoring global changes to translation. absence of stress. Interestingly, in unstressed cells, G3BP-dependent
translation changes showed no positive correlation to the translation
G3BPs reinforce the ISR translation programme changes of arsenite or the heat-shock ISRs (R values of –0.033 and
S
Having developed a method to globally monitor absolute TE changes, –0.12, respectively; Fig. 2i,k). Similar results were observed when
we wanted to use it to determine the effects of G3BPs and SGs on the ISR. analysing published data from G3BP-KO U2OS cells55 (Extended Data
To do so, we needed to be able deplete cells of G3BPs and SGs. There- Fig. 3b). Together, these results argued that G3BPs reinforce the ISR
fore, we engineered HCT116 cells in which both endogenous G3BP1 translation programme in a stress-dependent manner, consistent
and endogenous G3BP2 were homozygously tagged with RFP and an with a model in which this is a function of G3BP through its nuclea-
auxin-inducible degron (AID) allowing their rapid and efficient deple- tion of SGs.
tion (>90% within 3 h) upon addition of indole-3-acetic acid (IAA)47,48. As G3BPs are required for SG formation, we could not say whether
By assessing another SG marker protein, PABPC1 labelled with GFP, we the effects we observed upon depleting G3BPs were a consequence of
confirmed that our depletion of G3BPs before stress imparted minimal losing SGs or whether they were a consequence of losing some other
effects on PABPC1 stability and largely prevented the formation of SGs stress-specific G3BP function. We sought to disambiguate G3BP and SG
in response to both sodium arsenite and heat shock (Fig. 2a–f). function by targeting CAPRIN1 or UBAP2L, two other proteins reported
Having generated these degron lines, we used ribosome profiling to be required for SG formation16,19,56,57. However, no reduction in SG
with the ribo-spike to compare translation in cells with and without formation was detected upon AID depletion of either of these proteins
the ability to form SGs (Fig. 2g). Compared with G3BP-depleted cells, (Extended Data Fig. 4e–m). These results concurred with findings that,
normal cells underwent a somewhat stronger inhibition of global trans- in many cell types, G3BPs are uniquely required for SG formation, and
lation during arsenite stress (1.4 fold; Extended Data Fig. 2a), consistent illustrated the difficulties in disentangling the functions of SGs from
with reports that G3BPs are largely dispensable for the global reduction those of their required G3BP components12.
in translation caused by the ISR16.
We were intrigued to find that G3BPs, and perhaps SGs, did seem SGs are enriched for mRNAs that are favoured by the ISR
to contribute, if only modestly, to the massive reduction in transla- translation programme
tion that occurs during the ISR. To further examine this contribution, After difficulty using this genetic approach to define the role of SGs,
we compared the translation changes caused by presence of G3BPs we turned to other approaches. One attractive hypothesis was that
with those caused by activation of the ISR. Here, we observed a clear mRNAs that are differentially regulated by the ISR translation pro-
positive correlation (R of 0.33; Fig. 2h and Extended Data Fig. 2b). This gramme are also differentially localized to SGs and that this localiza-
S
implied that G3BPs, and perhaps SGs, tend to translationally upregulate tion to SGs determines the effect that G3BPs have on the translation
the same mRNAs that the ISR upregulates and tend to translationally of those mRNAs during stress.
downregulate the same mRNAs that the ISR downregulates, thereby To assess the relationships between regulation by the ISR, regula-
reinforcing the ISR translation programme. tion by G3BPs and SG localization, we purified SG cores from HCT116
To determine whether these G3BP-dependent changes to cells treated with 500 µM sodium arsenite for 1 h18,58. Sequencing
TE were driven by effects on RPFs or RNA, we examined these two identified 488 transcripts enriched in SG cores and 453 that were
Nature Cell Biology | Volume 28 | January 2026 | 135–148 137
Article https://doi.org/10.1038/s41556-025-01834-3
Arsenite stress
depleted compared with total cytoplasm (>2-fold change, adjusted P We next examined the relationship between ISR regulation and
value <0.05; Fig. 3a). Overall, our SG enrichments observed in HCT116 SG enrichment and found that mRNAs that retained or enhanced their
cells resembled those previously reported from U2OS cells18, including translation during stress tended to be more enriched in SGs, whereas
an enrichment for longer mRNAs and mRNAs that were poorly trans- hypersensitive mRNAs tended to be depleted (Fig. 3b). Furthermore,
lated before stress. This indicated that we had successfully purified SG analyses of SG enrichment in U2OS cells treated with sodium arsenite18,
cores (Extended Data Fig. 5a–d). stress-dependent RNA-granule enrichment in NIH 3T3 cells treated
Nature Cell Biology | Volume 28 | January 2026 | 135–148 138
sPB3G::PFR::DIA
Untreated
PFG::1CPBAP
Depleted
Heat shock
sPB3G::PFR::DIA
Untreated
PFG::1CPBAP
c
Depleted
)%(
sGS
htiw
slleC
***
100
80
60
40
20
0
)%(
sGS
htiw
slleC
a d e f
***
100
AID::RFP::G3BP1 80
AID::RFP::G3BP2
PABPC1::GFP 60
GAPDH
40
b 20
0
h i
Arsenite stress Arsenite stress
4 4
n = 10,385 n = 10,625
R = 0.33 R = –0.033 s s
2 2
0 0
g
–2 –2
Stress enhanced (70) Stress enhanced (69)
Stress resistant (262) Stress resistant (263)
–4 Stress hypersensitive (62) –4 Stress hypersensitive (62)
–5 0 5 –5 0 5
j k
4 Heat shock 4 Heat shock
n = 10,813 n = 10,704
R = 0.43 R = –0.12 s s
2 2
0 0
–2 –2
Stress enhanced (155) Stress enhanced (140)
Stress resistant (175) Stress resistant (175)
–4 Stress hypersensitive (52) –4 Stress hypersensitive (52)
–5 0 5 –5 0 5
)%( noitelped
nietorP
100
80 60
40
20
0
fo
tceffE
sserts
AID depletion
+G3BPs –G3BPs
Effect of
G3BPs
Unstressed
Effect of
SGs
Stressed
+SGs –SGs
ssertS
Effect of stress Effect of stress
sGS
fo
tceffE
sPB3G
fo
tceffE
egnahc
ET dessertS
egnahc
ET
dessertS
)sPB3G–/sPB3G+(gol
)sPB3G–/sPB3G+(gol
2
2
egnahc
ET
dessertsnU
egnahc
ET
dessertsnU
)sPB3G–/sPB3G+(gol
)sPB3G–/sPB3G+(gol
2
2
150 kDa
150 kDa
100 kDa
37 kDa
Untrea D te e d pleted Untrea D te e d pleted
G3BP
G
1 3BP
P
2 ABP C1
TE change log(stressed/unstressed) TE change log(stressed/unstressed)
2 2
detaertnU detelpeD
Fig. 2 | G3BPs reinforce the ISR translation programme. a, The depletion of G3BP-depleted unstressed HCT116 cells were used to determine the effect of
endogenous G3BPs fused to AID. Immunoblots probed for the indicated proteins G3BPs on translation and G3BP-depleted stressed HCT116 cells were used to
show specific depletion of AID fusion proteins after treatment with 500 µM determine the effects of G3BPs/SGs on translation. The effects of stress were then
IAA for 3 h. b, Quantification of protein depletion in a, normalizing to levels of compared with the effects of G3BPs and SGs. h, The relationship between G3BP-
GAPDH. The points show values for two biological replicates. c, The prevention dependent translation during arsenite stress and the ISR translation programme.
of SG formation during arsenite stress. HCT116 cells were either treated with The plots indicate the log FC in TE owing to the presence of G3BPs in cells treated
2
500 µM IAA to deplete G3BPs (right) or not treated (left) before arsenite with arsenite as a function of the log FC in TE owing to arsenite. Points for stress-
2
stress (500 µM sodium arsenite for 1 h). The images show either G3BPs (red) enhanced, stress-resistant and stress-hypersensitive mRNAs are indicated by
or SG marker protein PABPC1 (green) (scale bar, 10 µm). d, The quantification colours. n indicates the number of unique mRNAs. i, The relationship between
of SG formation in c. The points show values for three biological replicates G3BP-dependent translation in the absence of stress and the ISR translation
(***P = 6.5 × 10−5; Welch’s two-sample, two-tailed t-test). e,f, Images (e) and programme, otherwise as in h. j, The relationship between G3BP-dependent
quantification (f) of the prevention of SG formation during heat shock (45 °C for translation during heat shock and the heat shock ISR translation programme,
25 min; ***P = 0.001), otherwise as in c and d. g, A schematic representation otherwise as in h. k, The relationship between G3BP-dependent translation in the
of the G3BP-depletion experiment. Ribosome profiling was performed on absence of stress and the ISR translation programme, otherwise as in h.
stressed HCT116 cells to determine the effects of stress on translation,
Article https://doi.org/10.1038/s41556-025-01834-3
10
5
0 5 10
with thapsigargin59 and stress-dependent G3BP proximity labelling in a majority of cells. UBAP2L-induced puncta lacked the canonical SG
in HEK293T cells treated with sodium arsenite60 yielded similar, albeit marker eIF4G, and, while puncta induced by G3BP1 overexpression did
sometimes weaker, trends (Extended Data Fig. 5f–j). Together, these resemble authentic SGs, they formed in only ~20% of cells (Extended
results supported a model in which mRNAs that are favoured by the ISR Data Fig. 6a–d).
translation response preferentially localize to SGs and suggest that this To more robustly form ectopic SGs, we adapted a published CRY2
model might be generalizable across multiple stresses and cell types. optogenetic system63. We replaced the N-terminal NTF2L dimerization
domain of G3BP1 with the blue light-dependent cryptochrome 2 pho-
SG-enriched mRNAs are favoured by G3BPs during stress tolyase homology region oligomerization domain (CRY2), tagged with
We next examined the relationship between G3BP regulation and SG GFP (GFP::CRY2::G3BP ) (Fig. 4a). Even in the absence of blue light,
ΔN
enrichment in our HCT116 cells. Surprisingly, the presence of G3BPs doxycycline-induced expression of this construct caused formation of
tended to enhance the TE of SG-enriched mRNAs during arsenite stress, ectopic puncta in ~20% of cells, similar to overexpressing GFP::G3BP1.
whereas the presence of G3BPs tended to repress the TE of mRNAs However, exposing these cells to 488-nm blue light enhanced puncta
depleted from SGs during arsenite stress (Fig. 3c). Moreover, repeating formation, such that they were observed in ~80% of cells within 3 h.
this analysis with SG enrichment data from arsenite-treated U2OS cells18, Consistent with previous findings63, our light-induced granules were
RNA-granule enrichment data from heat-shocked NIH 3T3 cells59 and also reversible (disassembling to basal levels within 2 h of blue light
G3BP proximity labelling data from arsenite-stressed HEK293T cells60 removal), positive for canonical SG markers eIF4G and CAPRIN1 and
all yielded analogous results (Extended Data Fig. 4k–m). Thus, in a vari- exhibited photobleaching dynamics resembling those of canonical
ety of stresses and cell types, the G3BPs appeared to favour the transla- SGs (Fig. 4a,b and Extended Data Fig. 6e–g). Together, these results
tion of SG-enriched mRNAs or disfavour the translation of SG-depleted showed that our OptoGranules (OGs) were dynamic, reversible, SG-like
mRNAs, suggesting a model in which those transcripts that are most condensates formed in the absence of exogenous stress.
strongly upregulated by the ISR translation programme localize to If SG-like condensation alone was sufficient to drive an ISR-like
SGs, leading to further upregulation by G3BPs. response, then we would predict that induction of OGs would yield the
following results: first, cells with OGs would undergo a global reduc-
SG-like OGs drive global reduction in translation without a tion in translation. Second, these OG-induced translation changes
full ISR would positively correlate with ISR-induced translation changes.
Our global analyses showed that G3BPs, while not required to establish Third, OG-induced translation changes would also positively correlate
the ISR translation programme, do reinforce it. To determine whether with G3BP-dependent translation during stress. Fourth, transcripts
SG formation was indeed sufficient to drive these translation changes enriched in SGs would be resistant to any translation shutdown caused
in the absence of exogenous stress, we set out to form ectopic SGs in the by the formation of these SG-like condensates.
absence of exogenous stress. Overexpressing reported SG-nucleating To test these predictions, we induced OGs in HCT116 cells and
proteins UBAP2L and G3BP1 (refs. 61,62) failed to induce authentic SGs used ribosome profiling with our ribo-spike to compare them with cells
Nature Cell Biology | Volume 28 | January 2026 | 135–148 139
)MPR(
ANRm
GS
a
Arsenite stress
n = 10,383
R = 0.92 s
2.5
0
0
SG enriched (488)
SG depleted (453)
Cytoplasmic mRNA (RPM)
–2.5
)MPR
cimsalpotyc/MPR
GS(
tnemhcirne
GS
b
***
*** ***
2
0
–2
)sPB3G–/sPB3G+(gol
egnahc
ET
etinesrA
2
c
***
*** ***
-repyh
RSI
evitisnes klub
RSI
dna
tnatsiser
RSI
decnahne detelped
GS
rehtieN dehcirne
GS
Fig. 3 | Translation of SG-enriched mRNAs is favoured by G3BPs. a, mRNAs and stress-hypersensitive (lines represent the median, notches represent the
enriched and depleted in SGs. Plotted for each mRNA is its abundance in the SG 95% confidence interval, boxes represent quartiles and whiskers represent
fraction as a function of its abundance in the cytoplasmic fraction. Abundance 1.5× interquartile ranges (IQRs); ***P = 7 × 10−26, 9 × 10−56 and 6 × 10−26 (from left
is reported in reads per million (RPM). Points for SG-enriched and SG-depleted to right) Welch’s two-sample, two-tailed t-test; n = 10,383 unique mRNAs). c, The
mRNAs, as determined by DESeq2 (log FC >1, adjusted P value <0.05), are relationship between G3BP-dependent translation and SG enrichment. The plots
2
indicated in red and blue, respectively, with their numbers in parentheses. indicate the log FC in TE owing to presence of G3BPs in stressed cells for mRNAs
2
n indicates the total number of unique mRNAs. b, The relationship between SG in each of three SG-enrichment categories: SG enriched, SG depleted and neither
enrichment and ISR translation. Plotted are the SG enrichments of mRNAs in each (***P = 2.6 × 10−5, 1.2 × 10−15 and 5.6 × 10−15 (from left to right); otherwise as in b).
of three ISR translation categories: stress-enhanced/resistant, bulk behaviour All stresses were 500 µM sodium arsenite for 1 h.
Article https://doi.org/10.1038/s41556-025-01834-3
10
5
0
exposed to blue light but lacking GFP::CRY2::G3BP , and therefore results failed to confirm any of the remaining three predictions. OG
ΔN
lacking OGs. We observed a modest global TE reduction in OG-induced translation changes did not correlate with either the ISR translation
cells when compared to blue-light controls (Fig. 4c). This modest programme or G3BP-dependent translation changes in stressed cells
reduction (1.6 fold) agreed with our earlier result that G3BPs were (R values of 0.019 and –0.054, respectively; Fig. 4d,e), and mRNAs that
S
responsible for a small fraction of the ISR translation shutdown (1.4 were enriched in SGs did not perform any better than those that were
fold for arsenite stress) (Extended Data Fig. 2a) and was consistent neither enriched nor depleted (Fig. 4f). Considered together, these
with the first of our four predictions. However, analyses of the TE results argued that condensation of the SG-like OGs, while sufficient
Nature Cell Biology | Volume 28 | January 2026 | 135–148 140
)gol(
ekips-obir
ot
evitaler
ET
2
*
e
5.0 5.0
2.5
0 0
–2.5
−5.0 −5.0
–5 0 –4 –2 0 2 4
Stressed TE change log(+G3BPs/–G3BPs)
2
gol
egnahc
ET
2
)lortnoc
thgil-eulb/sGO(
d
Arsenite stress Arsenite stress
n = 10,129 n = 10,129
R = 0.019 R = –0.054
2.5 s s
0
–2.5
−5.0
de
plete
d Neither
G
S
)lortnoc
thgil-eulb/sGO(gol
egnahc
ET
2
a
NTF2L G3BP Endogenous G3BP
GFP CRY2 G3BP ∆N Dox-inducible GFP::CRY2::G3BP ∆N c
Blue
Dox light
G3BP eIF4G G3BP CAPRIN1
f
***
*** n.s.
2.5
–2.5
d
TE change log
2
(stressed/unstressed)
G
enriche
S
sGS
sGO
)sserts
etinesra(
)sserts
on(
b
thgil-eulB lortnoc decudni
GO
Fig. 4 | SG-like OGs can drive a global reduction in translation. a, A schematic (lines represent medians, notches represent 95% confidence intervals, boxes
representation of the OG system. HCT116 cells expressing endogenous represent quartiles and whiskers represent 1.5x IQRs; n = 10,129 unique mRNAs).
G3BP containing an NTF2L dimerization domain were edited to also express Significance was determined using ribo-spike values as in Extended Data Fig. 1b
doxycycline (dox)-inducible ectopic G3BP in which the NTF2L domain had been (*P = 0.026 with Welch’s two-sample, two-tailed t-test). d, The comparison of OG
replaced with a fusion of GFP and the light-inducible CRY2 dimerization domain and ISR translation programmes. Plotted is TE change caused by induction of
(GFP::CRY2::G3BP ). After doxycycline induction, a minority of cells formed OGs as a function of TE change caused by arsenite. n indicates the total number
ΔN
ectopic granules. After exposure to blue light (488 nm), most cells formed of unique mRNAs. e, A comparison of OG and G3BP-dependent translation
ectopic granules. b, SG marker localization to OGs. HCT116 cells expressing wild- programmes. Plotted is TE change caused by OGs as a function of TE change
type GFP::G3BP1 were either stressed with 500 µM sodium arsenite for 1 h (top) caused by the presence of G3BPs in arsenite-treated cells, otherwise as in c.
or treated with 1 µM doxycycline to induce expression of GFP::CRY2::G3BP and f, A comparison of OG translation programme and SG enrichment. The plots
ΔN
exposed to blue light for 3 h (bottom). Fluorescent or immunostained proteins indicate the log FC in TE caused by the induction of OGs for mRNAs in each
2
are as indicated (scale bars, 10 µm). White boxes highlight insets that are of three SG enrichment categories: SG enriched, SG depleted and neither
expanded on the right. n = 3 replicates with similar results. c, The comparison (lines represent medians, notches represent 95% confidence intervals, boxes
of TE in OG-induced cells to that in blue-light control cells. Plotted are the represent quartiles and whiskers represent 1.5× IQRs; n = 10,129 unique mRNAs.
TE distributions in HCT116 cells in which GFP::CRY2::G3BP was expressed ns, not significant; ***P = 6.9 × 10−9, 2.3 × 10−5 and 0.067 (left to right) Welch’s two-
ΔN
and exposed to blue light to form OGs (right) and in control cells expressing sample, two-tailed t-tests).
only wild-type G3BP exposed to blue light, in which no OGs were formed (left)
Article https://doi.org/10.1038/s41556-025-01834-3
to drive a modest reduction in global translation, was not sufficient to and Extended Data Fig. 7b). Taken together, our results indicated that
specify the ISR translation programme. establishing the SG transcriptome requires not only the interaction
network established by G3BPs but also the RNA-binding landscape
OGs require cellular stress to recruit an SG transcriptome established during cellular stress.
One caveat of our previous analysis was the assumption that sponta- These OG enrichment data also allowed us to confirm that the
neously formed OGs contained the same transcriptome as SGs and transcripts enriched in OGs did indeed better retain their translation
could therefore regulate those transcripts in the same manner. This (Fig. 5g). Taken together, our OG ribosome profiling and purification
assumption aligned with evidence that G3BP was the central scaffold of results support a model in which SGs are sufficient to drive a modest
the SGs complex protein–RNA interaction network and was further sup- decrease in global translation while prioritizing the translation of their
ported by the observation that OGs were positive for many canonical enriched mRNAs. However, SGs required stress to induce an ISR-like
SG markers12–14,63 (Extended Data Fig. 6e). Interestingly, this assumption translation programme, presumably because the sorting of SG mRNAs
was also consistent with the observation that the established determi- is dictated by the cellular RNA-binding landscape, which is drastically
nants of the SG transcriptome (transcript length and TE before stress) remodelled upon activation of the ISR.
are parameters that are independent of stress18. However, the SG tran-
scriptome is also thought to be largely determined by the transcriptome Tethering to SGs imparts resistance to ISR translation shutdown
RNA-binding landscape (the landscape created by proteins bound Our findings suggested that localization to an SG grants an mRNA pri-
to the transcriptome)10,12,64,65. Stress can dramatically remodel this oritized translation during the ISR. To test this model, we examined
RNA-binding landscape, shifting the RNA content of other biological whether tethering a reporter to SGs influenced its translation. The
condensates, such as P bodies and P granules66,67. Thus, SGs formed in reporter-encoded nanoluciferase (nLuc) fused to the Escherichia coli
the presence of stress and OGs formed in the absence of stress might dihydrofolate reductase (ecDHFR) destabilizing domain, which causes
recruit different sets of mRNAs, despite their general compositional, rapid turnover of its protein fusions, ensuring reporting on recently
morphological and biophysical similarities. translated nLuc68. The 3′-UTR of the reporter mRNA included an array
To test this hypothesis, we purified OGs formed in the pres- of 24 bacteriophage MS2 hairpins, which bind MS2 coat protein (MCP),
ence of stress. To do this, we integrated the doxycycline-inducible thereby providing a means to tether the reporter to the SG30,69 (Fig. 6a).
GFP::CRY2::G3BP construct into cells expressing endogenously G3BPs strongly partition into SGs16,62,70; almost half of our endog-
ΔN
edited AID::RFP::G3BPs and doxycycline-inducible OsTIR1, the E3 enous G3BP1 fusion protein (45.9%) localized to SGs after 90 min of
ligase responsible for the turnover of the AID. Upon treatment with arsenite stress (Extended Data Fig. 8a,b). Considering this high par-
doxycycline and IAA, these cells degraded their endogenous G3BPs and titioning coefficient, we chose an MCP fusion to endogenous G3BP1
replaced them with GFP::CRY2::G3BP , rendering them incapable of as our SG-tethering protein. Our reporter was stably integrated into
ΔN
forming SGs in the absence of blue light, even when stressed. However, HCT116 cells in which all endogenous G3BP1 alleles were tagged with
when these cells were stressed and exposed to blue light, they readily either GFP (GFP::G3BP1) or MCP and GFP (MCP::GFP::G3BP1) (Fig. 6a).
formed granules (Fig. 5a,b). We refer to these OGs formed in the pres- We also explored the λN–BoxB aptamer system71,72, but found that it
ence of stress as StressOptoGranules (SOGs). perturbed G3BP localization and SGs (Extended Data Fig. 8c).
We then purified and sequenced the transcripts associated with To assess the effects of SG tethering on an mRNA not normally
both OGs and SOGs. We compared transcripts across OGs, SOGs and recruited to SGs, we created a reporter using the 5′ and 3′ UTR of
control SGs from each cell line, including our original SG enrichment CNOT10, an mRNA that was not enriched in SGs in either our data or
data acquired from the parental line (Fig. 5c,d). Control SGs corre- published datasets18, and was translationally repressed both by the ISR
lated strongly with each other (R values of 0.72–0.75). OGs formed and by G3BPs during stress (Supplementary Table 1). Single-molecule
S
in the absence of stress, correlated substantially less with control SGs fluorescence in situ hybridization (smFISH) with probes targeting the
(R values of 0.35–0.45), indicating a distinct transcriptome (Fig. 5e nLuc sequence indicated that the reporter was recruited to SGs at a
S
and Extended Data Fig. 7a). Interestingly, we found that transcripts basal level of 38% in cells expressing only GFP::G3BP (Fig. 6b,c). In cells
enriched in SOGs strongly resembled those enriched in SG controls (R expressing MCP::GFP::G3BP, the reporter was more robustly recruited
S
values of 0.69–0.70), indicating that the difference between SG and OG to SGs (92%) (Fig. 6b,c), a higher fraction than that observed for 99%
transcriptomes was because of a lack of cellular stress, as opposed to of endogenous mRNAs18.
some intrinsic bias of OG formation (Fig. 5e and Extended Data Fig. 7a). Next, we measured how the translation of this reporter responded
These differences in granule composition did not appear to be driven to arsenite stress. Cells were treated with 500 µM sodium arsenite for
by differences in gene expression, as the cytoplasmic mRNA levels cor- timepoints ranging from 0 to 90 min, and protein production was
related quite well between these groups (R values of 0.84–0.96) (Fig. 5f monitored by measuring the luciferase signal. Reporter mRNA levels
S
Fig. 5 | OGs require stress to recruit the SG transcriptome. a, The replacement AID and RFP (RFP::AID::G3BP), doxycycline-inducible OsTIR1 and doxycycline-
of G3BP with GFP::CRY2::G3BP to induce SOGs. HCT116 cells expressing inducible GFP::CRY2::G3BP . Control SGs were purified from each cell line by
ΔN ΔN
endogenously tagged AID::RFP::G3BPs were either untreated or treated with 1 µM treating them with 500 µM sodium arsenite for 1 h. In addition, OGs were purified
doxycycline (dox) and 500 µM IAA for 18 h, leading to turnover of endogenous from the OG line treated with doxycycline for 18 h, followed by 3 h of blue light,
G3BP (red) and expression of GFP::CRY2::G3BP (green) (left). Cells were treated and SOGs were purified from the SOG line treated with both doxycycline and
ΔN
as on the left, but were subsequently stressed with 500 µM sodium arsenite for IAA for 18 h, followed by exposure to arsenite stress for 30 min in the absence of
1 h in the absence of blue light (middle). Cells were treated as in the middle, but blue light and then an additional 30 min of stress in the presence of blue light.
were also exposed to blue light, beginning 30 min after the start of the arsenite d, mRNAs enriched and depleted in the indicated types of granules, otherwise
treatment (right) (scale bars, 10 µm). White boxes highlight insets that are as in Fig. 3a. e, Comparisons of granule enrichments. The heat map depicts the
expanded on the right. b, The quantification of granule formation in a. Error bars pairwise correlations (R values) observed between the enrichments of granules
S
represent the s.d. for three biological replicates (n.s., P = 0.48; ***P = 5.9 x 10−9; from Figs. 3a and 5d. f, Comparisons of cytoplasmic transcriptomes of cells
and n.s., P = 0.071 (left to right) Welch’s two-sample, two-tailed t-test). c, A used to determine granule enrichments in e. g, A comparison of OG-dependent
schematic representation of the granule purification experiment. Three cell translation and OG enrichment. Plotted are distributions of TE changes caused
lines were used: the parental HCT116 line expressing endogenous G3BPs; an by the induction of OGs for mRNAs in each of three OG enrichment categories,
OG HCT116 line expressing endogenous G3BPs and doxycycline-inducible ***P = 9.5 × 10−9, 1.5 × 10−17 and 9.5 x 10−11 (left to right), otherwise as in Fig. 4f.
GFP::CRY2::G3BP ; and an SOG line expressing endogenous G3BP fused to
ΔN
Nature Cell Biology | Volume 28 | January 2026 | 135–148 141
Article https://doi.org/10.1038/s41556-025-01834-3
0
–5
Nature Cell Biology | Volume 28 | January 2026 | 135–148 142
)lortnoc
thgil-eulb/sGO(gol
egnahc
ET
2
10
5
0 5 10
***
*** ***
2.5
–2.5
)MPR(gol
ANRm
elunarG
2
OGs
n = 10,827
R = 0.92 s
Enriched (199)
0
Depleted (225)
10
5
0 5 10
)MPR(gol
ANRm
elunarG
2
SOGs
n = 10,827
10 R = 0.89 s
5
Enriched (167)
0
Depleted (192)
0 5 10
OG control SOG control
n = 10,827 n = 10,827
R = 0.90 10 R = 0.88 s s
5
Enriched (230) Enriched (391)
0 0
Depleted (343) Depleted (398)
0 5 10
Cytoplasmic mRNA log(RPM) Cytoplasmic mRNA log(RPM)
2 2
Parental
SOG control
OG control
SOG induced
OG induced
latneraP lortnoc
GOS
lortnoc
GO
decudni
GOS
decudni
GO
latneraP lortnoc
GOS
lortnoc
GO
decudni
GOS
decudni
GO
g
e f
1 SG 1 Cytoplasmic
0.75 1 mRNAs 0.96 1 mRNAs
0.75 0.72 1 0.92 0.91 1
0.69 0.70 0.69 1 0.90 0.91 0.92 1
0.35 0.38 0.45 0.46 1 0.86 0.84 0.93 0.87 1
)%(
selunarg
htiw
slleC
a
Unstressed
Untreated Replaced
Untreated
Replaced
*** n.s.
100
80
60
40
20 n.s.
0
AID::RFP::G3BPsGFP::CRY2::G3BP∆N
Stressed Stressed + blue light
Untreated Replaced Untreated Replaced
b c
Stress
Parental line
Stress Dox Blue
OG line +CRY2::G3BP∆N OGs
Stress Dox Stress Stress
IAA Blue
Control SGs SOG line –AID::G3BP +CRY2::G3BP∆N SOGs
Unstressed Stressed
+
S t
b
re lu s e s e li d ght
d
G
depleted
Nei
G
th e
e
r nriched
O O
Article https://doi.org/10.1038/s41556-025-01834-3
were then monitored by reverse transcription–quantitative PCR (RT– stress-dependent translation shutdown stabilizes it and recruitment to
qPCR) to calculate a TE for each timepoint. For the untethered reporter, SGs, in rescuing translation, destabilizes the reporter yet again49,50,53,54.
we observed a 95% reduction in reporter TE over the 90 min period of To test this model, we treated cells expressing our untethered
stress (Fig. 6d). This aligned with the 20-fold average decrease in TE CNOT10 reporter with two different translation inhibitors—cyclohex-
observed by ribosome profiling, indicating that our assay accurately imide and puromycin (puro)—and monitored protein and mRNA levels.
reported on stress-induced translation changes. As expected, both drugs inhibited translation by 98% over a 4 h time
We then examined what happens to the translation of this reporter course (Extended Data Fig. 8l,m). Both drugs also caused dramatic
when tethered to MCP::GFP::G3BP1. Strikingly, even when tethered to stabilization of reporter mRNA (cycloheximide by tenfold and puro
G3BP1 in unstressed cells, our reporter was more efficiently translated, by 22 fold; Extended Data Fig. 8n). These results indicated that our
with an average threefold higher TE. This observation was consistent reporters are subject to translation-dependent destabilization, and
with previous reports that G3BPs can act as translational regulators, are consistent with a model in which the translation shutdown during
even outside the context of stress16,21–23,73,74 (Fig. 6d). When stressed, we stress contributes to the stabilization of our reporters.
saw that our G3BP1 tethering continued to enhance the translation of To further distinguish between SG and G3BP function, we examined
our reporter. Interestingly, this translation enhancement peaked early whether the effect of tethering was specific to G3BPs. To do this, we
in stress, as translation both in tethered and untethered cells dimin- tethered our CNOT10 reporter to SGs using another SG protein, CAPRIN1.
ished at later timepoints. However, even at our latest timepoints, our CAPRIN1-mediated recruitment to SGs was robust, resembling that
tethered reporter was translated significantly better than its unteth- observed with G3BP1 tethering (Extended Data Fig. 9a,b). To measure the
ered counterpart (Fig. 6d). translation effects of this alternative tethering strategy, we integrated
To test whether these effects on translation were specific to this both the reporter and doxycycline-inducible, MCP-tagged CAPRIN1 into
reporter, we created two additional reporters using 5′ and 3′ UTRs from our AID::G3BP cell line. With this combination, we could assess the effects
the genes DDIT4L and RB1, which represented a range of endogenous of tethering the reporter to SGs via CAPRIN1 and also deplete G3BPs to
translational responses to stress and to G3BPs (Supplementary Table 1). control for any effects that did not require formation of SGs (Fig. 6e).
The results for both of these reporters resembled those observed for We first expressed the reporter in untreated cells without the
CNOT10, with the tethered reporter showing enhanced SG recruitment induction of any MCP-tagged protein (Fig. 6f and Extended Data
and translation across all stressed timepoints, peaking early in stress Fig. 9c). In this condition, our reporter underwent a ~75% reduction
and then decreasing at later timepoints (Extended Data Fig. 8e–g). in TE, similar to our previous experiments (Fig. 6g). We then induced
We next wanted to determine whether, as in our ribosome profiling MCP-tagged CAPRIN1 (MCP::GFP::CAPRIN1) without depleting the
experiment, changes to mRNA levels contributed to these changes in AID-tagged G3BPs by treating cells with both 1 µg ml−1 doxycycline
TE. Examining protein and RNA separately, we saw that, although the and 200 µM auxinole, a small-molecule inhibitor of OsTIR1 activ-
rate of luciferase production was modestly higher for some tethered ity (Fig. 6f and Extended Data Fig. 9c). Under these conditions, the
reporters, as evidenced by the slower rate of luciferase disappearance CAPRIN1-tethered reporter was more efficiently translated following
upon stress (Extended Data Fig. 8h,i), the untethered reporter mRNA arsenite treatment, indicating that tethering effects do not require
levels consistently increased across all reporter constructs during the tethering via G3BP (Fig. 6g). However, these benefits to translation were
stress treatment, by an average of 5.2 fold, whereas G3BP1-tethered abolished when cells expressing MCP::GFP::CAPRIN1 were depleted
mRNA levels remained steady or slightly decreased, with an average of G3BPs by treating cells with both 1 µg ml−1 doxycycline and 500 µM
change of 0.9 fold (Extended Data Fig. 8j,k). This pattern was consistent IAA (Fig. 6f,g and Extended Data Fig. 9c), indicating that this effect of
with a model in which translation destabilizes the reporter mRNA, the tethering required the presence of G3BPs and perhaps SGs.
Fig. 6 | Tethering to SGs imparts resistance to ISR translation shutdown. depicted in h. The x axis shows 12 equal-volume fractions that were taken with
a, A schematic representation of G3BP1 tethering. b, Tethering a luciferase boundary points between fractions marked as ticks. j, Reporter distributions
reporter to SGs via G3BP1. HCT116 cells expressing a NanoLuc reporter bearing across G3BP1-tethered polysome profile fractions. Plotted are the proportions
5′ and 3′ UTRs from CNOT10 and endogenous G3BP1, tagged with either GFP or of total reporter mRNA in each polysome fraction as measured in h and i by RT–
MCP::GFP, were stressed with 500 µM sodium arsenite for 90 min. The images qPCR, otherwise as in i. k, The relative ribosome loading of the G3BP1-tethered
show G3BP1 (green) and smFISH of NanoLuc reporter molecules (magenta) reporter. Plotted is the total ribosome load as determine by polysome profiling
(scale bars, 1 µm). White boxes highlight insets on the right. n = 3 replicates with of the G3BP1-tethered reporter relative to its untethered counterpart. l, The
similar results. c, The G3BP1 tethering efficiency. The percentage of SG-localized polysome profile analysis of MCP::GFP::CAPRIN1-expressing cells. Plotted are
reporter molecules in either untethered cells (green) or tethered cells (pink) are the polysome traces for untethered cells expressing endogenous G3BPs (green),
shown. The points show values for biological replicates (***P = 3.6 × 10−6 Welch’s tethered cells expressing MCP::GFP::CAPRIN1 along with endogenous G3BPs
two-sample, two-tailed t-test; n = 3 biological replicates). d, G3BP1-tethered (pink) and tethered cells expressing MCP::GFP::CAPRIN1 with endogenous G3BPs
ISR translation. Plotted is the TE of the reporter in untethered cells (green) or depleted (red), otherwise as in i. m, Reporter distributions across CAPRIN1-
tethered cells (pink) during a time course of arsenite stress (500 µM sodium tethered polysome profile fractions. Plotted are the proportions of total reporter
arsenite). The bold line shows average values from at least three biological mRNA in each polysome fraction of conditions shown in l. Plots are shown for
replicates (shown as thin lines). Light-coloured ribbons report the s.e.m. TE stress timepoints of 0 and 15 min, otherwise as in j. n, The relative ribosome
is reported relative to that of untethered, unstressed cells from the matched loading of the CAPRIN1-tethered reporter. Plotted is the total ribosome load
biological replicate. e, A schematic representation of CAPRIN1 tethering. as determine by polysome profiling of the CAPRIN1-tethered reporter in the
f, The quantification of SG formation in cells treated as depicted in e. Error presence of G3BPs (pink) and in their absence (red) relative to their untethered
bars represent the s.d. for three biological replicates (n.s., P = 1; ***P = 5.9 × 10−8 counterpart (green), before and during arsenite stress, otherwise as in k.
Welch’s two-sample, two-tailed t-test). g, CAPRIN1-tethered ISR translation. o, A plausible model of SG translation control: (1) ISR-enhanced transcripts are
Plotted is the relative TE of the reporter in untethered cells (green), tethered preferentially recruited to SGs between cycles of translation, when they lack
cells with SGs (+SGs; pink), and tethered cells without SGs (–SGs; red), otherwise ribosomes; (2) as a consequence of being recruited to SGs, these transcripts
as in d. h, A schematic representation of the polysome profiling experiment. are licensed for translation, possibly through the recruitment of G3BPs;
We performed polysome fractionation on cells treated with 500 µM sodium and (3) after this licensing, this model is agnostic to whether the transcript
arsenite, added an in vitro transcribed RNA standard to each fraction, isolated diffuses out to the cytosol or remains inside the SG to be translated. Once these
the total RNA and performed RT–qPCR to measure the abundance of the reporter transcripts complete their translation, they would be available to, once again, be
relative to the standard. i, The polysome profile analysis of MCP::GFP::G3BP1- preferentially recruited to (or retained in) the granule.
expressing cells. Plotted are the polysome traces produced by the workflow
Nature Cell Biology | Volume 28 | January 2026 | 135–148 143
Article https://doi.org/10.1038/s41556-025-01834-3
a
5′ UTRecDHFR nLuc 3′ UTR
Nature Cell Biology | Volume 28 | January 2026 | 135–148 144
)%(
sGS
ot
dezilacol
retropeR
derehtetnu
1PB3G::PFG
derehtet
1PB3G::PFG::PCM
)retroper
cuLn
RTU
01TONC(
)retroper
cuLn
RTU
01TONC(
b
MERGE
24× MS2
smFISH
GFP
c
MERGE
***
100
80 smFISH
60
GFP 40
20
0
ET
evitaleR
5
4
3
2
1
0
0 25 50 75
ET evitaleR
3
2
1
0
0 25 50 75
)%(
sGS
htiw
slleC
e
24× MS2
f
*** n.s.
100
80
60
40
20
0
)mn
062(
ecnabrosbA
0.5
0.4
0.3 0.2
ta ecnabrosbA ).u.a(
mn
062
1.00
Polysome profiling 0.75
0.50
Fractionation 0.25
Addition of RNA standard
RNA isolation
RT–qPCR
retroper
latot fo noitroporP
0.3
0
1 5 10 0.3
0 1 5 10 0.3
0 1 5 10
0.3
0 1 5 10
retroper
latot
fo noitroporP
0.3
0
1 5 10 0.3
0 1 5 10 daol
emosobir
latoT
derehtetnu
ot
evitaler
1.5 Fraction 4
3
1.0
2
1 0.5
0 20 40 60 0 15
Time stressed (min) Time stressed (min)
Fraction
daol
emosobir
latoT
derehtetnu
ot
evitaler
5′ UTRecDHFR nLuc 3′ UTR
Untethered Tethered
Untethered (+SGs) (–SGs)
Tethered Tethered
(+SGs)
GFP::G3BP1 MCP::GFP::G3BP1 AID::RFP::G3BPs MCP::GFP::CAPRIN1 MCP::GFP::CAPRIN1
AID::RFP::G3BPs depleted G3BPs
d
g
Time stressed (min) Time stressed (min)
h i j l m
Untethered Untethered (+SGs)
Tethered Tethered (+SGs) 0 min Tethered (–SGs) 0 min
2 4 6 8 10 12 15 min 2 4 6 8 10 12 15 min
Fraction Fraction n k
30 min
60 min
o
ISR enhanced
1. SG recruitment
AAA AAA
G3BPs ISR bulk behaviour AAA
Translating ribosome ISR hypersensit A i A v A e AAA AAA Non-translating mRN A A AA
AAA
AAA 2. G3BP
AAA
recruitment
AAA
AAA
AAA
AA
AAA
3. Translation
AAA
AAA
AAA
AAA
AAA
derehtetnU derehteT )sGS+(
derehtetnU
)sGS+(
derehteT
)sGS–(
derehteT
AA
Article https://doi.org/10.1038/s41556-025-01834-3
As with our G3BP1-tethering experiments, we then replicated these regulate mRNA levels. Whether this additional example of SGs impart-
CAPRIN1-tethering experiments using both the DDIT4L and RB1 report- ing subtle, global tuning effects on gene expression was indirectly
ers. We observed results similar to those obtained with CNOT10 at the caused by translation-dependent destabilization of mRNAs or illus-
TE, protein and RNA levels, consistent with the idea that the reporter trates an independent function of SGs will be an interesting question
was better translated only when recruited to SGs, and thus under- for further investigation.
went translation-dependent destabilization (Extended Data Fig. 9d–i). Consistent with the idea that SGs impart global tuning effects,
Interestingly, the average effect size observed with CAPRIN1 tethering a recent study investigating the impact of SGs during viral infection
was smaller than that observed with G3BP1 tethering and, unlike our reports that SGs play a role in tuning the innate immune response to
G3BP1-tethered reporters, CAPRIN1-tethered reporters showed only viral infection57. However, instead of amplifying the ISR translation
modestly improved translation in unstressed cells (Extended Data response, here SGs are reported to dampen the ISR transcriptional
Fig. 9d,e). This difference may suggest that, while heavily G3BP-bound response57. This difference in results might be explained by differences
mRNAs are subject to enhanced translation, even in unstressed condi- in the nature of the stressors or composition of the SGs19,37. Compared
tions, other mRNAs only benefit once they are recruited to the SG and with SGs formed by arsenite, heat shock or endoplasmic reticulum
brought into proximity with G3BPs. stress, the granules formed in response to viral infection tend to be
To further measure the effect of SG association on translation by smaller, only weakly recruit PABPC1 and polyadenylated mRNAs, do
an orthogonal method less likely to be affected by mRNA stability or the not require the phosphorylation of eIF2α for their formation and can
kinetics of luciferase production and degradation, we monitored the include RNAse L bodies, which share many of the same markers with
ribosome association of our CNOT10 reporter using polysome profiling SGs and also form in response to viral infection57,75,76. Moreover, the
RT–qPCR (Fig. 6h). As expected, untethered reporter mRNA shifted response to viral infection might differ between cells or viruses, as
gradually from heavy polysomes to lighter polysomes, and finally to this negative tuning role has been absent in some other reports on
monosomes and free RNA fractions over a 60 min arsenite treatment viral stress77. Thus, although our results seem likely to be generalizable
time course. However, G3BP-tethered reporter mRNA was associated across canonical SGs that require eIF2α phosphorylation, granules
with heavier polysome fractions compared with its untethered counter- formed under viral infection appear to have distinct effects.
part, even in unstressed cells, where SGs were not formed. In addition, In presenting a model in which SGs reinforce the ISR translation
this preferential association peaked early in stress and diminished by programme, we propose that SGs help to promote the translation
the 60-min timepoint, when SGs were still fully formed but translation of a subset of RNAs. Several observations have led to the hypothesis
had largely shut down (Fig. 6j,k). Both the preferential polysome asso- that SGs play strictly repressive roles in translation. However, none of
ciation of our G3BP-tethered reporter in the absence of SGs, and the these observations actually preclude SGs from promoting translation.
collapse in this preference at later timepoints suggested that this shift Although SGs are nucleated by translationally silent mRNAs, implying
was not due to the inclusion of the reporter in heavy-sedimenting gran- that the mRNAs localized to them are non-translating, those mRNAs
ules, but due to more efficient loading into actual ribosomes. These also dynamically exchange with the cytosol and could therefore
results indicated that tethering to G3BP enhanced reporter translation transit out of the SG after their translation was initiated, maintaining
in both unstressed and stressed conditions, and were consistent with enrichment for translationally silent mRNAs inside the SGs25,29,30,36,78.
the results of our luciferase assays. Indeed, translation initiation itself might even expel the mRNA from
To further evaluate the results of our luciferase assays, we per- the SG, as the presence of even a single ribosome has been reported
formed polysome profiling of the CNOT10 reporter in CAPRIN1-tethered to prevent SG localization79. Similarly, although SGs are enriched
cells under unstressed and early stress (15 min) conditions. Consistent for 40S but not 60S ribosomal subunits, implying that 60S subunits
with results of our luciferase assay, CAPRIN1 tethering enhanced ribo- are not stoichiometrically available to assemble translating 80S
some association only during stress and in a G3BP-dependent man- ribosomes, 60S subunits are not depleted from SGs and appear to be
ner (Fig. 6l–n). The G3BP dependence of this polysome shift further equally available to form translating ribosomes as in the cytosol20,28.
supported the idea that it was not caused simply by CAPRIN1 protein Indeed, a recent single-molecule study reports that translation of an
sedimenting farther into the gradient. Collectively, the results of these ATF4 reporter inside the SG is neither impossible nor rare30. Thus,
tethering experiments indicated that tethering the 3′ UTR of an mRNA the prior observations, although originally interpreted as evidence
to either G3BP1 or CAPRIN1 increased recruitment to SGs and imparted of SGs being incompatible with translation, are also consistent with
preferential translation during the ISR—consistent with a model in the possibility that they could be sites of privileged translation for a
which localization to SGs grants an mRNA prioritized translation dur- subset of mRNAs.
ing stress. Although a model of mRNAs being preferentially translated while
inside the SG is perhaps the simplest interpretation of our results, it is
Discussion not the only interpretation. Alternatively, mRNAs could be licensed
SGs were once thought to be required for the global repression of trans- for translation while transiting through an SG. In this scenario,
lation observed during the ISR1,11,20,24,25. Later studies hypothesized that pre-initiation complexes or translational activators such as UBAP2L,
SGs might have no function at all and are incidental by-products of which are known to be enriched in SGs1,10,20,28,56,80, could preferentially
increased RNA availability owing to translation repression32,33. Here, interact with mRNAs transiting through the SG. Then, having acquired
we propose a model in which SGs are neither required for the ISR nor this license, the mRNAs could go on to be translated independently of
functionless condensates, but instead measurably enhance and rein- their localization inside or outside of the SG (Fig. 6o). Such a model, in
force the ISR translation programme, thereby leading to a widespread which licensed mRNAs are translated inside or outside the SG, could
and statistically significant, albeit relatively modest, impact on global reconcile the previous observation that mRNAs devoid of ribosomes
translation. are preferentially recruited to SGs with our observation that mRNAs
This widespread yet subtle reinforcement of the ISR is consistent that are translationally enhanced during the ISR are enriched in SGs,
with several observations of SG biology. SGs recruit a wide array of further enhancing their translation. Such a model could also explain
mRNAs and proteins and yet contain only ~10% of cytoplasmic mRNAs why a single-molecule reporter based on ATF4 mRNA is no more effi-
and protein molecules10,17,18,59. This implies that they would be more ciently translated in the SG than in the cytosol30. This being said, we
likely to subtly tune widespread gene expression than to have dramatic found that ATF4 mRNA was neither enriched in SGs nor influenced
impacts. Indeed, both our ribosome profiling and reporter experiments by the presence of SGs, indicating that other transcripts might better
demonstrate that, in addition to translational effects, SGs modestly represent mRNAs influenced by SGs.
Nature Cell Biology | Volume 28 | January 2026 | 135–148 145
Article https://doi.org/10.1038/s41556-025-01834-3
The difficulty of distinguishing the function of SGs from the 7. Starck, S. R. et al. Translation from the 5′ untranslated region shapes
function of the SG-nucleating G3BPs must be acknowledged. One the integrated stress response. Science 351, aad3867 (2016).
approach to inferring SG function is to consider shared phenotypes of 8. Sidrauski, C., McGeachy, A. M., Ingolia, N. T. & Walter, P. The small
depleting proteins reported to be required for SG formation. However, molecule ISRIB reverses the effects of eIF2alpha phosphorylation
many of these proteins are thought to also form complexes with each on translation and stress granule assembly. eLife 4, e05033
other, independent of SGs, obscuring the interpretation of shared (2015).
phenotypes19,32,33. Moreover, we and others found that the requirement 9. Vattem, K. M. & Wek, R. C. Reinitiation involving upstream ORFs
for reported non-G3BP nucleators appears to be stress or cell-type regulates ATF4 mRNA translation in mammalian cells. Proc. Natl
specific, which limits the utility of depleting these factors. Acad. Sci. USA 101, 11269–11274 (2004).
Although we have not conclusively distinguished between these 10. Protter, D. S. W. & Parker, R. Principles and properties of stress
models, five lines of reasoning support the proposal that the ISR trans- granules. Trends Cell Biol. 26, 668–679 (2016).
lation programme is reinforced by the formation of SGs rather than 11. Kedersha, N. L., Gupta, M., Li, W., Miller, I. & Anderson, P.
only by G3BPs. First, both our ribosome profiling experiments and our RNA-binding proteins TIA-1 and TIAR link the phosphorylation of
tethering experiments demonstrated stress-specific effects. Although eIF-2 to the assembly of mammalian stress granules. J. Cell Biol.
G3BP1 tethering enhanced translation in unstressed cells, this might 147, 1431–1441 (1999).
reflect the effect of our 24× MS2/MCP system artificially recruiting 12. Yang, P. et al. G3BP1 is a tunable switch that triggers phase
many copies of G3BP simultaneously, and thereby simulating the SG separation to assemble stress granules. Cell 181, 325–345 (2020).
environment. Second, although our SG purifications relied on immu- 13. Guillen-Boixet, J. et al. RNA-induced conformational switching
noprecipitation (IP) of G3BP, these were IPs on SG-enriched fractions and clustering of G3BP drive stress granule assembly by
depleted of cytosolic G3BP17,18,58,81. Thus, our data should reflect the condensation. Cell 181, 346–361 (2020).
SG transcriptome and not simply the G3BP–RNA interactome. Fur- 14. Sanders, D. W. et al. Competing protein–RNA interaction networks
thermore, we identified similar trends in SG-enrichment data that do control multiphase intracellular organization. Cell 181, 306–324
not require IP of G3BPs59. Third, the process of forming OGs, which (2020).
simply manipulates G3BPs condensation, was sufficient to trigger 15. Molliex, A. et al. Phase separation by low complexity domains
a translation response. Fourth, tethering reporter mRNAs to SGs, promotes stress granule assembly and drives pathological
whether by G3BP1 or CAPRIN1, was sufficient to impart resistance to fibrillization. Cell 163, 123–133 (2015).
stress-induced translation shut down. Although G3BPs and CAPRIN1 16. Kedersha, N. et al. G3BP–Caprin1–USP10 complexes mediate
are binding partners16, this result indicates that this effect does not stress granule condensation and associate with 40S subunits.
require direct recruitment via G3BPs. J. Cell Biol. 212, 845–860 (2016).
Last, in distinguishing between SG- and G3BP-centric models, we 17. Jain, S. et al. ATPase-modulated stress granules contain a diverse
should not dismiss the possibility that both G3BPs and SGs contrib- proteome and substructure. Cell 164, 487–498 (2016).
ute to this translation reinforcement. G3BPs have been observed to 18. Khong, A. et al. The stress granule transcriptome reveals
regulate translation and exhibit exceptionally high partitioning into principles of mRNA accumulation in stress granules. Mol. Cell 68,
SGs16,21–23,71,73,74. Indeed, we observed almost half of G3BP1 localizing 808–820 (2017).
to SGs and that tethering to the protein enhanced translation, even 19. Markmiller, S. et al. Context-dependent and disease-specific
in unstressed cells. If G3BPs license translation, perhaps recruitment diversity in protein interactions within stress granules. Cell 172,
of mRNAs to SGs is a molecular strategy to increase their interaction 590–604 (2018).
with G3BPs, reinforcing their translation during stress (Fig. 6o). 20. Kedersha, N. et al. Evidence that ternary complex (eIF2–GTP–
Although these considerations do not conclusively distinguish tRNAiMet)-deficient preinitiation complexes are core constituents
between SG and G3BP function, they do support the proposal that of mammalian stress granules. Mol. Biol. Cell 13, 195–210 (2002).
SGs are a functional condensate responsible for reinforcing the ISR 21. Laver, J. D. et al. The RNA-binding protein Rasputin/G3BP
translation programme. enhances the stability and translation of its target mRNAs.
Cell Rep. 30, 3353–3367 (2020).
Online content 22. Alam, U. & Kennedy, D. Rasputin a decade on and more
Any methods, additional references, Nature Portfolio reporting sum- promiscuous than ever? A review of G3BPs. Biochim. Biophys.
maries, source data, extended data, supplementary information, Acta Mol. Cell Res. 1866, 360–370 (2019).
acknowledgements, peer review information; details of author contri- 23. Meyer, C., Garzia, A., Morozov, P., Molina, H. & Tuschl, T.
butions and competing interests; and statements of data and code avail- The G3BP1-family-USP10 deubiquitinase complex rescues
ability are available at https://doi.org/10.1038/s41556-025-01834-3. ubiquitinated 40S subunits of ribosomes stalled in translation
from lysosomal degradation. Mol. Cell 77, 1193–1205 (2020).
References 24. Anderson, P. & Kedersha, N. RNA granules: post-transcriptional
1. Buchan, J. R. & Parker, R. Eukaryotic stress granules: the ins and and epigenetic modulators of gene expression. Nat. Rev. Mol. Cell
outs of translation. Mol. Cell 36, 932–941 (2009). Biol. 10, 430–436 (2009).
2. Advani, V. M. & Ivanov, P. Translational control under stress: 25. Kedersha, N. et al. Dynamic shuttling of TIA-1 accompanies the
reshaping the translatome. Bioessays 41, e1900009 (2019). recruitment of mRNA to mammalian stress granules. J. Cell Biol.
3. Pakos-Zebrucka, K. et al. The integrated stress response. 151, 1257–1268 (2000).
EMBO Rep. 17, 1374–1395 (2016). 26. Kwon, S., Zhang, Y. & Matthias, P. The deacetylase HDAC6 is a
4. Harding, H. P. et al. Regulated translation initiation controls novel critical component of stress granules involved in the stress
stress-induced gene expression in mammalian cells. Mol. Cell 6, response. Genes Dev. 21, 3381–3394 (2007).
1099–1108 (2000). 27. Youn, J. Y. et al. Properties of stress granule and P-body
5. Harding, H. P., Zhang, Y. & Ron, D. Protein translation and folding proteomes. Mol. Cell 76, 286–294 (2019).
are coupled by an endoplasmic-reticulum-resident kinase. Nature 28. Kimball, S. R., Horetsky, R. L., Ron, D., Jefferson, L. S. &
397, 271–274 (1999). Harding, H. P. Mammalian stress granules represent sites of
6. Yamasaki, S. & Anderson, P. Reprogramming mRNA translation accumulation of stalled translation initiation complexes. Am. J.
during stress. Curr. Opin. Cell Biol. 20, 222–226 (2008). Physiol. Cell Physiol. 284, C273–C284 (2003).
Nature Cell Biology | Volume 28 | January 2026 | 135–148 146
Article https://doi.org/10.1038/s41556-025-01834-3
29. Moon, S. L. et al. Multicolour single-molecule tracking of 52. Bicknell, A. A. et al. Attenuating ribosome load improves protein
mRNA interactions with RNP granules. Nat. Cell Biol. 21, 162–168 output from mRNA by limiting translation-dependent mRNA
(2019). decay. Cell Rep. 43, 114098 (2024).
30. Mateju, D. et al. Single-molecule imaging reveals translation of 53. Horvathova, I. et al. The dynamics of mRNA turnover revealed by
mRNAs localized to stress granules. Cell 183, 1801–1812 (2020). single-molecule imaging in single cells. Mol. Cell 68, 615–625
31. Baymiller, M. & Moon, S. L. Stress granules as causes and (2017).
consequences of translation suppression. Antioxid. Redox Signal. 54. Rosa-Mercado, N. A., Buskirk, A. R. & Green, R. Translation
39, 390–409 (2023). elongation inhibitors stabilize select short-lived transcripts.
32. Putnam, A., Thomas, L. & Seydoux, G. RNA granules: functional RNA 30, 1572–1585 (2024).
compartments or incidental condensates?. Genes Dev. 37, 55. Liboy-Lugo, J. M. et al. G3BP isoforms differentially affect stress
354–376 (2023). granule assembly and gene expression during cellular stress.
33. Mateju, D. & Chao, J. A. Stress granules: regulators or Mol. Biol. Cell 35, ar140 (2024).
by-products? FEBS J. 289, 363–373 (2022). 56. Cirillo, L. et al. UBAP2L forms distinct cores that act in nucleating
34. Ingolia, N. T. Ribosome footprint profiling of translation stress granules upstream of G3BP1. Curr. Biol. 30, 698–707 (2020).
throughout the genome. Cell 165, 22–33 (2016). 57. Paget, M. et al. Stress granules are shock absorbers that prevent
35. Iwasaki, S., Floor, S. N. & Ingolia, N. T. Rocaglates convert excessive innate immune responses to dsRNA. Mol. Cell 83,
DEAD-box protein eIF4A into a sequence-selective translational 1180–1196 (2023).
repressor. Nature 534, 558–561 (2016). 58. Khong, A., Jain, S., Matheny, T., Wheeler, J. R. & Parker, R. Isolation
36. Wilbertz, J. H. et al. Single-molecule imaging of mRNA of mammalian stress granule cores for RNA-seq analysis. Methods
localization and regulation during the integrated stress response. 137, 49–54 (2018).
Mol. Cell 73, 946–958 (2019). 59. Namkoong, S., Ho, A., Woo, Y. M., Kwak, H. & Lee, J. H. Systematic
37. Aulas, A. et al. Stress-specific differences in assembly and characterization of stress-induced RNA granulation. Mol. Cell 70,
composition of stress granules and related foci. J. Cell Sci. 130, 175–187 (2018).
927–937 (2017). 60. Ren, Z., Tang, W., Peng, L. & Zou, P. Profiling stress-triggered
38. Sonenberg, N. & Hinnebusch, A. G. Regulation of translation RNA condensation with photocatalytic proximity labeling.
initiation in eukaryotes: mechanisms and biological targets. Nat. Commun. 14, 7390 (2023).
Cell 136, 731–745 (2009). 61. Huang, C. et al. UBAP2L arginine methylation by PRMT1
39. Holcik, M. & Sonenberg, N. Translational control in stress and modulates stress granule assembly. Cell Death Differ. 27, 227–241
apoptosis. Nat. Rev. Mol. Cell Biol. 6, 318–327 (2005). (2020).
40. Andreev, D. E. et al. Translation of 5′ leaders is pervasive in genes 62. Tourriere, H. et al. The RasGAP-associated endoribonuclease
resistant to eIF2 repression. eLife 4, e03971 (2015). G3BP assembles stress granules. J. Cell Biol. 160, 823–831 (2003).
41. Tomuro, K. et al. Calibrated ribosome profiling assesses the 63. Zhang, P. et al. Chronic optogenetic induction of stress granules
dynamics of ribosomal flux on transcripts. Nat. Commun. 15, 7061 is cytotoxic and reveals the evolution of ALS-FTD pathology. eLife
(2024). 8, e39578 (2019).
42. Chen, J., Brunner, A.-D., Nunez, J. K. & Weissman, J. Pervasive 64. Panas, M. D., Ivanov, P. & Anderson, P. Mechanistic insights into
functional translation of noncanonical human open reading mammalian stress granule dynamics. J. Cell Biol. 215, 313–323
frames. Science 367, 1135–1140 (2020). (2016).
43. Glauninger, H. et al. Transcriptome-wide mRNA condensation 65. Ivanov, P., Kedersha, N. & Anderson, P. Stress granules and
precedes stress granule formation and excludes new mRNAs. processing bodies in translational control. Cold Spring Harb.
Mol. Cell 85, 4393–4409.e11 (2025). Perspect. Biol. https://doi.org/10.1101/cshperspect.a032813
44. Zedan, M. et al. Timing of transcription controls the selective (2019).
translation of newly synthesized mRNAs during acute 66. Matheny, T., Rao, B. S. & Parker, R. Transcriptome-wide
environmental stress. Mol. Cell 85, 4379–4392.e5 (2025). comparison of stress granules and p-bodies reveals that
45. Agarwal, V. & Kelley, D. R. The genetic and biochemical translation plays a major role in RNA partitioning. Mol. Cell Biol.
determinants of mRNA degradation rates in mammals. Genome https://doi.org/10.1128/MCB.00313-19 (2019).
Biol. 23, 245 (2022). 67. Lee, C. S. et al. Recruitment of mRNAs to P granules by
46. Pizzinga, M. et al. The cell stress response: extreme times call condensation with intrinsically-disordered proteins. eLife 9,
for post-transcriptional measures. Wiley Interdiscip. Rev. RNA 11, e52896 (2020).
e1578 (2020). 68. Ramadurgum, P. & Hulleman, J. D. Protocol for designing
47. Natsume, T., Kiyomitsu, T., Saga, Y. & Kanemaki, M. T. Rapid protein small-molecule-regulated destabilizing domains for in vitro use.
depletion in human cells by auxin-inducible degron tagging with STAR Protoc. 1, 100069 (2020).
short homology donors. Cell Rep. 15, 210–218 (2016). 69. Bertrand, E. et al. Localization of ASH1 mRNA particles in living
48. Nishimura, K., Fukagawa, T., Takisawa, H., Kakimoto, T. & yeast. Mol. Cell 2, 437–445 (1998).
Kanemaki, M. An auxin-based degron system for the rapid 70. Wheeler, J. R., Jain, S., Khong, A. & Parker, R. Isolation of yeast and
depletion of proteins in nonplant cells. Nat. Methods 6, 917–922 mammalian stress granule cores. Methods 126, 12–17 (2017).
(2009). 71. Matheny, T., Van Treeck, B., Huynh, T. N. & Parker, R. RNA
49. Dave, P. et al. Single-molecule imaging reveals partitioning into stress granules is based on the summation of
translation-dependent destabilization of mRNAs. Mol. Cell 83, multiple interactions. RNA 27, 174–189 (2021).
589–606 (2023). 72. Khong, A., Matheny, T., Huynh, T. N., Babl, V. & Parker, R. Limited
50. Tuck, A. C. et al. Mammalian RNA decay pathways are highly effects of m6A modification on mRNA partitioning into stress
specialized and widely linked to translation. Mol. Cell 77, granules. Nat. Commun. 13, 3735 (2022).
1222–1236 (2020). 73. Bidet, K., Dadlani, D. & Garcia-Blanco, M. A. G3BP1, G3BP2 and
51. Laird-Offringa, I. A., de Wit, C. L., Elfferich, P. & van der Eb, A. J. CAPRIN1 are required for translation of interferon stimulated
Poly(A) tail shortening is the translation-dependent step in c-myc mRNAs and are targeted by a dengue virus non-coding RNA.
mRNA degradation. Mol. Cell. Biol. 10, 6132–6140 (1990). PLoS Pathog. 10, e1004242 (2014).
Nature Cell Biology | Volume 28 | January 2026 | 135–148 147
Article https://doi.org/10.1038/s41556-025-01834-3
74. Ortega, A. D., Willers, I. M., Sala, S. & Cuezva, J. M. Human G3BP1 81. Wheeler, J. R., Matheny, T., Jain, S., Abrisch, R. & Parker, R. Distinct
interacts with β-F1-ATPase mRNA and inhibits its translation. J. Cell stages in stress granule assembly and disassembly. eLife 5, e18413
Sci. 123, 2685–2696 (2010). (2016).
75. Burke, J. M., Moon, S. L., Matheny, T. & Parker, R. RNase L
reprograms translation by widespread mRNA turnover escaped Publisher’s note Springer Nature remains neutral with regard to
by antiviral mRNAs. Mol. Cell 75, 1203–1217 (2019). jurisdictional claims in published maps and institutional affiliations.
76. Burke, J. M., Lester, E. T., Tauber, D. & Parker, R. RNase L promotes
the formation of unique ribonucleoprotein granules distinct from Open Access This article is licensed under a Creative Commons
stress granules. J. Biol. Chem. 295, 1426–1438 (2020). Attribution 4.0 International License, which permits use, sharing,
77. Burke, J. M., Ratnayake, O. C., Watkins, J. M., Perera, R. & adaptation, distribution and reproduction in any medium or format,
Parker, R. G3BP1-dependent condensation of translationally as long as you give appropriate credit to the original author(s) and the
inactive viral RNAs antagonizes infection. Sci. Adv. 10, eadk8152 source, provide a link to the Creative Commons licence, and indicate
(2024). if changes were made. The images or other third party material in this
78. Buchan, J. R., Muhlrad, D. & Parker, R. P bodies promote stress article are included in the article’s Creative Commons licence, unless
granule assembly in Saccharomyces cerevisiae. J. Cell Biol. 183, indicated otherwise in a credit line to the material. If material is not
441–455 (2008). included in the article’s Creative Commons licence and your intended
79. Fedorovskiy, A. G. et al. A solitary stalled 80S ribosome prevents use is not permitted by statutory regulation or exceeds the permitted
mRNA recruitment to stress granules. Biochem. (Mosc.) 88, use, you will need to obtain permission directly from the copyright
1786–1799 (2023). holder. To view a copy of this licence, visit http://creativecommons.
80. Luo, E. C. et al. Large-scale tethered function assays identify org/licenses/by/4.0/.
factors that regulate mRNA stability and translation. Nat. Struct.
Mol. Biol. 27, 989–1000 (2020). © The Author(s) 2025
Nature Cell Biology | Volume 28 | January 2026 | 135–148 148
Article https://doi.org/10.1038/s41556-025-01834-3
Methods incubation time to maximize ribosome occupancy. The reaction was
Cell culture assembled by combining 0.06 µM fLuc mRNA with reticulocyte lysate,
All cells were cultured at 37 °C with 5% CO using McCoy’s 5 A medium 0.02 mM complete amino acid mixture, 0.8 units µl−1 RNAsin ribonu-
2
supplemented with 10% foetal bovine serum and 2 mM l-glutamine. clease inhibitor, 0.01 M creatine phosphate, 0.05 mg ml−1 creatine
HCT116 (CCL-247, ATCC) were obtained from the Young laboratory. phosphokinase, 2 mM dithiothreitol (DTT), 0.05 mg ml−1 tRNA, 80 mM
potassium acetate and 0.5 mM magnesium acetate in 23 117 µl reac-
Cell line construction tions. The reactions were incubated at 30 °C for 15 min, cooled on ice
Cas9-mediated editing. Fusion proteins were introduced into the and treated with 0.1 mg ml−1 cycloheximide to block ribosome translo-
endogenous locus of genes using the Cas9 genome editing system. cation. Reactions were then combined, mixed, aliquoted, snap frozen
The 5′ and 3′ homology arms (each 200–700 bp) flanking an insertion in liquid nitrogen and stored at –80 °C.
site were either amplified from genomic DNA of the parental cell line
or from gblock gene fragments (IDT) cloned into a rescue template IAA-induced protein depletion
plasmid, flanking the fusion protein sequence. This plasmid, along with HCT116 cells were engineered using the PiggyBac system to express
pX330 plasmid expressing a Cas9 guide RNA, was reverse transfected multiple copies of doxycycline-inducible OsTIR1. These cells were then
into the parental cell line using Lipofectamine 3000 transfection rea- also engineered using Cas9 to expressed AID-tagged fusion proteins
gent in a 6-well dish at 100% confluency. After 48 h, the cells of each edited at their endogenous loci. Cells expressing fusion proteins were
well were expanded to a 10-cm dish and cultured for an additional 24 h. first doxycycline-induced for 4 h and were then treated with 500 µM IAA
Cells with a strong signal from the fusion protein fluorescence were (Gold Bio, I-110-25) to induce rapid (<3 h) depletion of the AID fusion
single-cell sorted into 96-well plates using flow cytometry. Colonies protein. Depletion was confirmed by microscopy, western blot or both.
derived from single cells were grown, expanded and screened by PCR When confirming by western blot, as was the case with G3BP1, G3BP2
genotyping and western blotting. Unless otherwise stated, all endog- and CAPRIN1 proteins, antibodies raised directly against the target
enously edited cell lines were edited homozygously. proteins were used to enable detection of untagged alleles, if present.
Where indicated, non-depleted controls were treated with 200 µM
PiggyBac editing. Exogenous genes were introduced into cells using auxinole (Aobious, AOB8812) to minimize background protein degra-
the PiggyBac transposon system. The exogenous gene was either ampli- dation83. Unless otherwise stated, all other non-depleted control cells
fied from genomic DNA of the parental cell line or from gblock gene were treated only with ethanol, the solvent used for IAA. Previous work
fragments (IDT) and cloned into a plasmid expressing the PiggyBac has shown that the addition of IAA alone does not affect translation84.
inverted-repeat sequences along with a selection marker for either
hygromycin, puro or blasticidin. This plasmid, along with the super Pig- Stress conditions
gyBac transposase expression vector (System Biosciences, PB210PA-1), For oxidative stress, unless otherwise stated, cells were treated with
was reverse transfected into the parental cell line using Lipofectamine media containing 500 µM sodium arsenite (Sigma, 93289) for 1 h. For
3000 transfection reagent (Thermo, L3000015) in a 6-well dish at 100% heat shock, media was separately heated to 45 °C. Media were removed
confluency. After 48 h, cells of each well were expanded to a 10-cm from cells previously grown in a 37 °C, rapidly replaced with 45 °C media
dish, and successfully edited cells were selected using the appropriate and then cells were quickly placed in a 45 °C incubator for 25 min.
antibiotic. For cases in which a fluorescent protein had been transposed
into the genome, cells expressing the protein at the appropriate level Doxycycline induction
were single-cell sorted into 96-well plates by flow cytometry. Colonies For all doxycycline inductions, cells were treated with 1 µg ml−1 doxycy-
derived from single cells were grown, expanded and screened by either cline (Clonetech Takara Bio, 631311) for the indicated amount of time.
microscopy, western blotting or both.
Tethered reporter TE experiments
Ribo-spike production To measure changes in TE for the nanoluciferase reporters (NanoLuc),
In vitro transcription. Ribo-spike mRNA was generated using the cells expressing a reporter containing selected 5′ and 3′ UTRs, NanoLuc
mMessage mMachine kit (Thermo, AM1344) following the standard T7 fused to an ecDHFR domain and 24× MS2 stem loops, were washed with
protocol. The DNA transcription template was generated by PCR of a cold PBS, lysed directly in their dish in buffer containing 10 mM Tris HCl
plasmid template encoding the firefly luciferase coding region (fLuc) pH 7.5, 5 mM MgCl, 100 mM KCl, 1% Triton, 1× cOmplete mini tablet
2
preceded by the T7 promotor and followed by an encoded poly(A) tail (EDTA free) and 0.02 U µl−1 SUPERase-In RNase inhibitor, and depleted
of 30 nt length. The resulting PCR product was purified using phenol– of nuclei by centrifuging at 1,300g for 10 min at 4 °C. Nuclear-depleted
chloroform extraction followed by ethanol precipitation, and was size supernatant was then transferred to a new tube and flash frozen using
selected and purified from an agarose gel using the ‘freeze and squeeze’ liquid nitrogen and stored at –80 °C. Cells were then assayed for total
method, in which the gel slice was frozen at –80 °C for 30 min, followed protein using bicinchoninic acid, luciferase production and reporter
by centrifugation at 21,000g for 5 min (ref. 82). The eluted DNA was mRNA using RT–qPCR by comparison to GAPDH
then concentrated by an additional ethanol precipitation and added mRNA, which did not change in abundance during the treatment
to the mMessage mMachine in vitro transcription reaction, incubated with sodium arsenite (Extended Data Fig. 8c). TE was then calculated
for at 37 °C for 2 h and then treated with TURBO DNAse for 15 min at according to the following equation:
37 °C. RNA from the in vitro transcription reaction was recovered by
passing the reaction over a Tris-buffered micro bio-spin p30 gel column NanoLucsignal/totalprotein
TE=
(Bio-Rad, 7326223) and centrifuging at 1,000g for 4 min. The resulting NanoLucmRNA/GAPDHmRNA
flow through was then purified by phenol–chloroform extraction and
ethanol precipitation, and then resuspended in water. RNA was exam- In G3BP-tethering experiments, the reporter was integrated into in
ined by running an aliquot on a 4% urea–polyacrylamide denaturing two different HCT116-derived cell lines: a line expressing endogenous
gel and staining with Sybr Gold (Thermo, S11494). G3BP1 tagged with GFP (GFP::G3BP1) and a line expressing endogenous
G3BP1 tagged with MCP fused to GFP (MCP::GFP::G3BP1) (Fig. 6a). In
In vitro translation. The fLuc mRNA was in vitro translated using a rab- CAPRIN1-tethering experiments, the reporter was expressed in an
bit reticulocyte lysate system (Promega, L4151) following the standard HCT116-derived cell line under three different conditions: unteth-
non-nuclease treated protocol, with the exception of using a shorter ered, in which the cell line was untreated and expressed endogenous
Nature Cell Biology
