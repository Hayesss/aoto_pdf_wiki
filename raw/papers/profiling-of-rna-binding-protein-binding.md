---
source_path: /mnt/c/Users/Administrator/Zotero/storage/TIPCFPLW/Xiao 等 - 2024 - Profiling of RNA-binding protein binding sites by in situ reverse transcription-based sequencing.pdf
ingested: 2026-04-23
sha256: c0d7f84100f3f24d
---

nature methods
Article https://doi.org/10.1038/s41592-023-02146-w
Profiling of RNA-binding protein binding
sites by in situ reverse transcription-based
sequencing
Received: 5 March 2023 Yu Xiao 1,2,3,4,5, Yan-Ming Chen 1,2,3,4,5, Zhongyu Zou 1,2,3,4, Chang Ye 1,2,3,4,
Xiaoyang Dou1,2,3,4, Jinjun Wu 2,3, Chang Liu 1,2,3,4, Shun Liu1,2,3,4, Hao Yan1,3,
Accepted: 7 December 2023
Pingluan Wang1,2,3,4, Tie-Bo Zeng 1,2,3,4, Qinzhe Liu 1,2,3,4, Jingyi Fei 2,3,
Published online: 10 January 2024 Weixin Tang 1,3 & Chuan He 1,2,3,4
Check for updates
RNA-binding proteins (RBPs) regulate diverse cellular processes by
dynamically interacting with RNA targets. However, effective methods
to capture both stable and transient interactions between RBPs and
their RNA targets are still lacking, especially when the interaction is
dynamic or samples are limited. Here we present an assay of reverse
transcription-based RBP binding site sequencing (ARTR-seq), which relies
on in situ reverse transcription of RBP-bound RNAs guided by antibodies
to identify RBP binding sites. ARTR-seq avoids ultraviolet crosslinking and
immunoprecipitation, allowing for efficient and specific identification of
RBP binding sites from as few as 20 cells or a tissue section. Taking advantage
of rapid formaldehyde fixation, ARTR-seq enables capturing the dynamic
RNA binding by RBPs over a short period of time, as demonstrated by the
profiling of dynamic RNA binding of G3BP1 during stress granule assembly
on a timescale as short as 10 minutes.
RBPs dynamically interact with their RNA targets to regulate RNA fate in treatment digests RBP-free regions of RNAs, increasing the resolution
all aspects, including transcription, splicing, modification, localization, of binding site detection7–10,14,15. CLIP-seq variants such as PAR-CLIP or
translation and degradation1. The dysfunction of RBPs or their binding eCLIP improve the crosslinking efficiency, specificity or binding site
to RNA substrates can lead to various defects or even diseases. Effec- resolution7,9. While effective and widely used, these methods also have
tive methods to capture RBP–RNA interactions, particularly dynamic limitations. They often require a large amount of starting materials due
or even transient interactions, are critical for a better understanding to the low IP efficiency; the ultraviolet (UV) crosslinking in CLIP-based
of RBP and its functional effect on target RNAs2. methods is a low-efficiency chemical reaction. Recently reported
The widely used approaches to identify RBP targets are based tRIP-seq and LACE-seq can be applied in low-input samples but at the
on immunoprecipitation (IP) of the specific RBP along with its bound cost of reducing the library complexity12,13.
RNAs, either through direct RNA IP (RIP) or crosslinking IP (CLIP) TRIBE and STAMP type approaches fuse RBPs with an RNA base
assisted by covalent capture3–15. Substrate RNAs bound by a specific editor to introduce mutations nearby RBP binding sites, bypassing
RBP can be enriched through either RIP or CLIP using the antibody IP to identify RBP binding sites16–21. These methods could be readily
against the RBP, followed by high-throughput sequencing (seq) to applied to study RBP binding in live cells and with limited materials
profile RBP targets across the whole transcriptome. CLIP-seq captures down to single-cell level. Their deployments into research have offered
RBP binding sites on substrate RNAs via covalent crosslinking. RNase new opportunities; however, these editing-based methods still have
1Department of Chemistry, The University of Chicago, Chicago, IL, USA. 2Department of Biochemistry and Molecular Biology, The University of Chicago,
Chicago, IL, USA. 3Institute for Biophysical Dynamics, The University of Chicago, Chicago, IL, USA. 4Howard Hughes Medical Institute, Chicago, IL, USA.
5These authors contributed equally: Yu Xiao, Yan-Ming Chen. e-mail: chuanhe@uchicago.edu
Nature Methods | Volume 21 | February 2024 | 247–258 247
Article https://doi.org/10.1038/s41592-023-02146-w
limitations. They require genome manipulation by inserting base edit- profile (Fig. 1a(iv)). Note that after in situ RT, immunofluorescence
ing proteins in germlines or cell lines, hindering their application in imaging could be performed to reveal RBP subcellular localization
primary cells and tissues. Inducing editing protein expression typically without disturbing the subsequent library construction if the second-
takes roughly 24 hours or longer, which cannot be applied to monitor ary antibody and pAG-RTase are fluorophore-modified.
dynamic RNA binding by RBPs. These base editors have their own
sequence preferences, potentially changing the native binding profile Validation of ARTR-seq using PTBP1
of the target RBP. While we were working on our method, RT&Tag, a To evaluate ARTR-seq, we applied ARTR-seq to PTBP1, a well-studied
method derived from the CUT&Tag strategy, was published22,23. This splicing factor with a variety of published CLIP-seq datasets for com-
method profiles RBP–RNA interaction by oligo(dT) primer-initiated parison. To verify the production of biotinylated cDNAs from in situ
reverse transcription (RT) and Tn5 tagmentation of the resulting RT, we monitored the biotin group in the cDNA products by dot plot,
full-length RNA–complementary DNA (cDNA) heteroduplex in isolated confirming the incorporation of biotin and requirements of pAG-RTase
nuclei. RT&Tag can identify RBP binding in polyadenylated RNAs but is and primary antibody for successful cDNA synthesis (Fig. 1c). With
ineffective in nonpolyadenylated RNAs and cytoplasmic RBP binding. immunofluorescence staining, we further validated the colocalization
Due to the low efficiency of the Tn5 enzyme on heteroduplex, it requires of pAG-RTase, the secondary antibody and newly synthesized cDNA,
25,000–100,000 nuclei to obtain sufficient transcriptome-wide bind- and their signals largely disappeared on exclusion of the primary anti-
ing signals. body, supporting the localized RT reaction performed by pAG-RTase
To overcome the limitations of existing methods, we introduce tethered to the targeted RBP (Fig. 1d and Extended Data Fig. 1f). Note
an assay of RT-based RBP binding site sequencing (ARTR-seq) to cap- that the use of the secondary antibody increased the biotinylated cDNA
ture RBP–RNA interactions through in situ RT. We demonstrate that yield (Fig. 1d and Extended Data Fig. 1f,g). Altogether, ARTR-seq specifi-
ARTR-seq sensitively profiles RBP targets with good sequencing quality, cally and effectively reverse transcribes RNAs near the targeted protein
using as few as 20 cells or a single tissue section. Additionally, an imag- into biotinylated cDNA products.
ing step can be readily built into the ARTR-seq procedure, providing We next tested ARTR-seq on PTBP1 using 40,000 HepG2 or HeLa
direct spatial information of RBPs. With ARTR-seq, we show distinct cells, and compared the results with the published data from several
binding patterns of splicing factors and the YTH family reader proteins known methods, namely CLIP, iCLIP, irCLIP, eCLIP, sCLIP, tRIP, LACE-seq
of RNA N6-methyladenosine (m6A) modification. ARTR-seq unbiasedly and RT&Tag9–13,22,26,27. We observed that ARTR-seq displayed a compara-
detects RNA binding by RBPs in both cytoplasm and nucleus and meas- ble or higher percentage of usable reads compared to published meth-
ures RBP binding strength on RNA substrates. Furthermore, ARTR-seq ods, indicating a high complexity of the ARTR-seq libraries (Extended
could monitor dynamic RNA binding by G3BP1 during stress granule Data Fig. 2a,b). Then, we calculated the correlation between biological
(SG) assembly on a small timescale of 10 minutes. replicates (R = 0.98 for both HepG2 and HeLa samples), and confirmed
good reproducibility of ARTR-seq (Fig. 2a).
Results Further, we introduced input samples prepared by ARTR-seq with
Strategy and development of ARTR-seq the omission of the primary antibody as controls to help filter out
In ARTR-seq, we started with rapid formaldehyde fixation to preserve potential background signals from the nonspecific binding of the
the cellular structure, followed by permeabilization of cell membranes secondary antibody and RTase (Extended Data Fig. 2c). For PTBP1,
(Fig. 1a(i)). We then targeted the reverse transcriptase (RTase) to the RBP we found that over 70% of usable reads and over 80% of ARTR-seq
of interest using corresponding antibodies (Fig. 1a(ii)). This involved peaks were annotated to introns, with most exon peaks located within
delivering the primary antibody for RBP recognition (Fig. 1a(ii)1), fol- the 3′ untranslated region (3′ UTR), consistent with results reported
lowed by a secondary antibody to enhance the local antibody concen- by other methods10,12,13,26–29 (Fig. 2b and Extended Data Fig. 2d,e).
tration, capitalizing on the potential for multiple secondary antibodies The consensus motif of PTBP1 ARTR-seq peaks was identified as the
to bind a single primary antibody (Fig. 1a(ii)2). Subsequently, a fusion canonical CU-enriched sequence, as known previously30 (Fig. 2b). At
protein of protein A/G and RTase (pAG-RTase) was delivered to bind the whole-transcriptome scale, ARTR-seq reads for PTBP1 piled up at
both primary and secondary antibodies, enabling site-specific attach- the eCLIP peaks, while the input sample did not show such accumula-
ment of RTase to the target RBP (Fig. 1a(ii)3). Each step was followed by tion31 (Extended Data Fig. 3a,b). Additionally, we observed that more
thorough washing to remove any unbound antibodies or pAG-RTase. than 50% of genes identified by ARTR-seq were also detected by other
After localizing RTase to the RBP, we initiated in situ RT at RBP methods (52% for eCLIP, 51% for LACE-seq and 82% for iCLIP). At the
binding sites by adding necessary RT components (Fig. 1a(iii)). To peak level, ARTR-seq successfully identified 41% of eCLIP-targeted
achieve efficient RT, we screened three commonly used RTases, includ- peaks (Extended Data Fig. 3c). Examination of individual PTBP1 binding
ing engineered Moloney murine leukemia virus (MMLV) RTase24,25, sites revealed similar read distribution and density between ARTR-seq
human immunodeficiency virus RTase and a truncated version of and eCLIP or iCLIP results (Fig. 2c and Extended Data Fig. 3d). To further
engineered MMLV RTase (25–497) in the pAG-RTase fusion constructs validate PTBP1 bindings captured by ARTR-seq, we knocked down
with a 30-amino-acid linker (Extended Data Fig. 1a,b). By employing RT PTBP1 in HepG2 cells using two distinct small-interfering RNAs (siRNAs)
with quantitative polymerase chain reaction (RT–qPCR), we confirmed and performed ARTR-seq (Extended Data Fig. 3e). The reads located
pAG-MMLV RTase (25–497) as the most active and selected it for sub- around the ARTR-seq peaks reduced accordingly on PTBP1 knockdown,
sequent studies (Fig. 1b and Extended Data Fig. 1c). indicating the high specificity of ARTR-seq (Fig. 2d).
To identify all RBP binding sites without sequence bias, we applied
random RT primers with an adapter tag for library construction, and Direct versus indirect binding sites detected by ARTR-seq
extended the primer length from commonly used 6 nucleotides (nts) ARTR-seq identifies RBP binding by in situ RT, enabling the capture of
to 10 nts to enhance RT efficiency (Extended Data Fig. 1d). For effective RNAs directly bound by the RBP (direct targets) or potentially those
cDNA enrichment, biotinylated dNTPs were introduced into cDNA prod- spatially close to the RBP (indirect targets) (Extended Data Fig. 4a).
ucts. After screening, we found that biotin-16-dUTP and biotin-16-dCTP To evaluate direct versus indirect targets, we used the splicing factor
exhibited the least hindrance on RT efficiency (Extended Data Fig. 1e). RBFOX2 as an example; RBFOX2 possesses a well-defined canonical
These were included in a 1:1 ratio with regular dTTP and dCTP, respec- binding motif ‘UGCAUG’9,31. Peaks near the UGCAUG motifs likely rep-
tively, in the current ARTR-seq protocol. Following cDNA enrichment resent direct targets, while those farther away may indicate indirect
with streptavidin beads, we performed adapter ligation, library ampli- targets. We found more than 70% of ARTR-seq peaks were within 500 nts
fication and high-throughput sequencing to acquire the RBP binding from UGCAUG. This percentage is slightly higher than that of eCLIP9.
Nature Methods | Volume 21 | February 2024 | 247–258 248
Article https://doi.org/10.1038/s41592-023-02146-w
(i) Formaldehyde fixation
to preserve cellular structure,
and permeabilization
(ii) Targeting reverse transcriptase to RBP
(ii)1. Primary antibody
RNA
RBP
(ii)2. Secondary antibody
(ii)3. Protein A/G RTase RT
T R
RT RT
(iii) In situ RT
T
R
3′
RT RT
NNNN
5′ NNNN
(iv)1. Biotin enrichment
(iv)2. On beads cDNA 3′ adapter ligation
and PCR amplification
(iv)3. Next generation sequencing
RBP binding sites
Nature Methods | Volume 21 | February 2024 | 247–258 249
sdaeR
a b
c
Biotin dNTPs + + – +
pAG MMLV RTase (25–497) + – + +
PTBP1 Antibody + + + –
Biotin
Methylene blue
Fluorophore
d
(covalently conjugated to proteins)
Primer with NNNN Optional, Imaging adapter
+
Biotin dNTP
+
dNTP
(iv) Library preparation and sequencing
)1PBTP(
bA
yramirP
– + +
bA
yradnoceS
+ – +
esaTR
GAp
Biotin
Second Ab pAG RTase Nucleus (cDNA)
+ + +
40,000
20,000
0
Second Ab pAG RTase Biotin
ytisnetni
evitaleR
2.0
1.6
1.2
0.8
0.008
0.004
0
HepG2
0 5 10 15 20 25
ycneiciffe
TR
evitaleR
HDPAG
yb
pAG MMLV RTase (full length) + – – – –
pAG MMLV RTase (25–497) – + – – –
pAG HIV RTase – – + – –
SuperScript II – – – + –
SuperScript III – – – – +
Fig. 1 | ARTR-seq strategy and validation. a, Scheme of ARTR-seq. b, RT–qPCR was the loading control. d, Immunofluorescence imaging of the secondary
analysis showing the RT activity of tested purified pAG-RTase fusion proteins. antibody (secondary Ab; yellow), pAG-RTase (red), biotinylated cDNA (green)
Two commercial RTases, SuperScript II and SuperScript III, were loaded as and nucleus (blue) for PTBP1 ARTR-seq. The line graph analysis shows relative
positive controls. n = 3 biological replicates. c, Biotin dot blot assay showing fluorescence intensity along the line. Scale bar, 10 μm.
biotinylated cDNA products produced from ARTR-seq. Methylene blue staining
Article https://doi.org/10.1038/s41592-023-02146-w
The two methods were comparable when the distance from peaks to This suggests that the application of RNase may reduce reads from
UGCAUG was within 200 nts (Extended Data Fig. 4b). It is worth not- direct targets, thereby potentially elevating the ratio of nonspecific or
ing that RBFOX2 may have other noncanonical binding sites beyond indirect binding signals (Extended Data Fig. 6f). Overall, our studies
the UGCAUG motif, as suggested by the similar percentage of distant revealed that RNase treatment could improve ARTR-seq resolution.
RBFOX2 eCLIP peaks from this motif. Stringent cutoffs of signal values The strength of RNase treatment in ARTR-seq needs to be optimized
and q values for peaks increased confidence in identifying the direct tar- to achieve the desired balance between resolution and sensitivity,
gets, albeit at the expense of target numbers (Extended Data Fig. 4c,d). especially for samples with limited starting materials.
Furthermore, we also examined YTHDF2, an m6A binding protein32.
Approximately 80% of YTHDF2 ARTR-seq peaks were within 300 nts ARTR-seq detects PTBP1 binding sites with as few as 20 cells
from m6A sites identified by m6A-SAC-seq33, comparable to that from The in situ RT-based ARTR-seq bypasses the IP step to minimize sample
the PAR-CLIP method32 (Extended Data Fig. 4e). These results indicate loss, potentially making it feasible for low cell number samples. To
that the indirect interactions captured in ARTR-seq are likely limited. test this, we generated libraries for PTBP1 using different numbers
The percentage of direct targets identified by ARTR-seq is comparable of HepG2 cells and compared the results with published data from
to those observed in CLIP-based methods. LACE-seq and RT&Tag of low cell number samples13,22. The correlations
To further interrogate potential indirect targets identified in remained strong for ARTR-seq libraries prepared from as few as 20 cells
ARTR-seq, we limited the movement range of RTase by shortening the (Extended Data Fig. 7a). Additionally, ARTR-seq libraries exhibited a
linker in pAG-RTase or omitting the secondary antibody (Extended much higher percentage of usable reads compared to other methods
Data Fig. 5a–c). We found shorter linkers reduced RT activity of when using comparable numbers of cells (Fig. 2e and Extended Data
pAT-RTase, indicating that shorter linkers might lead to a slowdown Fig. 7b,c). Furthermore, PTBP1 ARTR-seq presented a consistently high
in the RTase kinetics (Extended Data Fig. 5d). In RBFOX2 ARTR-seq, the percentage of intronic reads, suggesting its effectiveness in capturing
use of shorter linkers or omitting the secondary antibody resulted in informative reads even with the limited starting materials (Extended
decreased biotinylated cDNA yields but slightly increased read accu- Data Fig. 7d). We further subsampled libraries to an equal sequencing
mulation at RBFOX2 ARTR-seq peaks, indicating reduced RT efficiency depth and examined their reads distribution at peaks identified in the
but concentrated signals (Extended Data Fig. 5e–g). Moreover, we corresponding bulk samples. Compared to LACE-seq, ARTR-seq exhib-
observed a little higher percentage (1.9–3.4%) of peaks within 500 nts ited a clearer accumulation at the peak center with a higher proportion
of UGCAUG with a shorter linker or omitting the secondary antibody of effective reads (Fig. 2f and Extended Data Fig. 7e). Visible ARTR-seq
(Extended Data Fig. 5h). These findings indicate that restricting the signal remained stable for libraries with different numbers of cells as
RTase movement range tested here moderately reduced potential exemplified in the Integrative Genomics Viewer (IGV) plot (Fig. 2g).
indirect RNAs captured by ARTR-seq. Optimal RT efficiency is another Because PTBP1 binds to a canonical CU-enriched sequence, we
factor that needs to be considered when designing linkers. compared the CT percentages in usable reads of PTBP1 libraries con-
structed by different methods. We found that all the ARTR-seq libraries
Resolution of ARTR-seq showed comparable or higher CT percentages compared to that of
To assess the resolution of ARTR-seq, we examined the distribution other methods10,13,26–28 (Fig. 2h). We further assessed the read distri-
of RBFOX2 peak centers around UGCAUG sites, and observed a clear bution around CU-enriched regions and observed the stable read
enrichment with most peaks positioned within 200 nts flanking the accumulation in ARTR-seq libraries of all cell numbers, peaking at the
UGCAUG motif (Extended Data Fig. 6a). Furthermore, we conducted region center (Fig. 2i). Taken together, ARTR-seq can effectively and
a parallel analysis on YTHDF2. Compared to RBFOX2, we observed a specifically capture the RBP binding sites, even with limited starting
similar but more enriched distribution for YTHDF2 around the cor- materials.
responding m6A sites, further supporting the capability of ARTR-seq
in capturing RBP binding sites (Extended Data Fig. 6b). Application of ARTR-seq in mouse embryo sections
In an attempt to improve the resolution of binding site identifi- RBPs can have strong tissue-specific expression, or are only expressed
cation by ARTR-seq, we evaluated the impact of RNase treatment on in certain tissues rather than cultured cells. Identifying RBP binding
RBFOX2 ARTR-seq. As expected, the stronger RNase treatment reduced sites in tissues remains technically challenging34. IP-based methods
the library fragment lengths (Extended Data Fig. 6c). We observed that require dissociating tissues into single cells for UV crosslinking, limiting
the stronger RNase treatment led to a sharper enrichment of RBFOX2 their application to whole tissues, particularly embedded frozen tis-
ARTR-seq peaks around UGCAUG sites, indicating an improved reso- sues or formalin-fixed tissues. Editing-based methods require genetic
lution upon RNase treatment (Extended Data Fig. 6d). Through quan- modification and cannot be applied to patient tissues.
tification of biotinylated cDNA, we found that samples with stronger ARTR-seq offers an opportunity for identifying RBP binding sites
RNase treatment exhibited lower RT efficiency (Extended Data Fig. 6e). in tissues. We studied RBFOX2 with a section of OCT-embedded E11
Moreover, stronger RNase treatment markedly reduced the propor- mouse embryo to validate the feasibility of ARTR-seq in tissue sam-
tion of peaks located within 500 nts of the canonical UGCAUG motif. ples (Fig. 3a). We first confirmed the nuclear localization of RBFOX2
Fig. 2 | ARTR-seq captures binding sites of RBPs using as few as 20 cells. cells revealed by ATAR-seq. e, Percentages of usable reads in subsampled uniquely
a, ARTR-seq replicate correlations for usable reads per gene normalized to coverage mapped reads from PTBP1 ARTR-seq with different numbers of cells. The plot
(reads per million reads mapped, RPM) for PTBP1 in HepG2 (top) and HeLa (bottom) shows replicate 1 for simplicity. f, Signal profiles and heatmaps of read density
cells, respectively. Usable reads were the remaining genomic uniquely mapped in ARTR-seq libraries constructed from 20 to 40,000 HepG2 cells at ARTR-seq-
reads after deduplication. The color scale shows the point density. The coefficient identified PTBP1 peaks. g, A snapshot from IGV showing the stable ARTR-seq signal
R and P values were given by the two-tailed Pearson’s correlation. b, Peaks in sequencing libraries constructed from different numbers of HepG2 cells. h, A box
distribution in 3′ UTR, CDS, 5′ UTR, noncoding exon, intergenic region and intron, plot comparing the CT percentages of usable reads from libraries constructed by
and the corresponding motifs of PTBP1 binding peaks identified by ARTR-seq in the using ARTR-seq, CLIP26, iCLIP27, eCLIP28, irCLIP10 and LACE-seq13, respectively. The
HepG2 (top) and HeLa (bottom) cells, respectively. P values were calculated by the green dashed line represents the median percentage in the ARTR-seq input library.
two-tailed binomial test in the HOMER suite52. c, Snapshots from the IGV showing The sample sizes are summarized in Supplementary Table 3. i, Signal profiles of
the signal overlaps between ARTR-seq and eCLIP28 (top) or iCLIP27 (bottom). The ARTR-seq read density at CU-enriched regions. CU-enriched regions are defined as
ARTR-seq input was pooled by three biological replicates. d, ARTR-seq read density 80 nt-wide regions with a percentage of CT content greater than 70% located in the
at PTBP1 binding peaks of control (siCtrl) and PTBP1 knockdown (siPTBP1) HepG2 protein-coding genes.
Nature Methods | Volume 21 | February 2024 | 247–258 250
Article https://doi.org/10.1038/s41592-023-02146-w
with the ARTR-seq built-in imaging (Fig. 3b). The ARTR-seq reads for known binding preference of RBFOX2 (ref. 31) (Supplementary Fig. 1c).
mouse embryo tissue showed a high percentage of usable reads and RBFOX2 binding peaks were mostly located in introns and contained
good reproducibility between biological replicates (Supplementary the canonical UGCAUG motif9 (Fig. 3c). Additionally, we observed that
Fig. 1a,b). Compared to the input, a higher percentage of usable reads mouse tissue samples displayed a similar percentage of usable reads
from RBFOX2 ARTR-seq were mapped to introns, consistent with the containing UGCAUG motifs to that of HepG2 cell samples, indicating
a b c d
P = 1 × 10–736
e
f g
h
40,000 cells ≥ 500 cells ≥ 20 cells
0.6 PTBP1 5,000 200
Input 2,000 100
1,000 50
0.5 500 20
0.4
0.3
0.2
0.1
–0.3 0 0 0 0.3 kb
Nature Methods | Volume 21 | February 2024 | 247–258 251
ytisned
daeR
4.0
3.0
2.0
1.0
0
–0.3 PTBP1 peak center 0.3 kb
CU-enriched region
ytisned
daeR
10 n = 21,810
R = 0.98
P = 0
5
0
−5
−5 0 5 10
log 2 RPM(rep1) Input
PTBP1
−5 0 5 10
log 2 RPM(rep1) HeLa (15,915 peaks)
0.04 0.02 0
Cell no. 40,000 5,000 2,000 1,000 500 200 100 50 20 5
3
1
10
8
s
k
a e 6
P
4
2
0
–0.3 0 0 0 0 0 0 0 0 0 0.3 kb
PTBP1 peaks identified by ARTR-seq
)2per(MPRgol
)2per(MPRgol
2
2
HepG2
HepG2 (23,080 peaks)
HeLa
10 n = 22,410
R = 0.98
P = 0
5
0
−5
P = 1 × 10–474
100
80
60
40
20
0
daer
ni
TC
fo
egatnecreP
i
Input
PTBP1
ARTR
ARTR (low cell number) CLIPiCLIP eCLIP irCLIP LACE
5,000 2,000 1,000 500 200 1005020
ytisneD
42,176,000 bp 42,177,000 bp
ARTR input[61] chr2
HepG2
ARTR rep1 [61]
HepG2
ARTR rep2 [61]
HepG2
eCLIP rep1 [61]
HepG2
eCLIP rep2 [61]
HepG2
Gene
EML4
139,283,000 bp 139,283,800 bp
ARTR input[53] chr5
HeLa
ARTR rep1[53]
HeLa
ARTR rep2[53]
HeLa
iCLIP rep1[53]
HeLa S3
iCLIP rep2[53] HeLa S3
Gene
MATR3
50,568,800 bp 50,569,800 bp
Input [116] chr16
[116] 40,000
[116]
5,000
[116]
2,000
[116]
1,000
[116]
500
[116]
200
[116]
100
[116]
50
[116] 20
Gene
.on
lleC
100
75
50
25
0
0.1 M 0.3 M 1.0 M
No. of subsampled uniquely
mapped reads
NKD1
Type
Cell line HepG2
Cell line HeLa
Cell no. 40,000 M10 M 20 M 1.8 M 100,000 HeLa S3
20 K562
sdaer
elbasu
fo
egatnecreP
Noncoding exon (0.5%)
5′ UTR (0.1%)
CDS (0.3%)
3′ UTR (3.2%)
Intergenic (10.4%)
Intron (85.6%)
siCtrl
siPTBP1-1 siPTBP1-2
Noncoding exon (0.4%)
5′ UTR (0.1%) CDS (0.4%)
3′ UTR (4.6%)
Intergenic (8.3%) Cell no.
40,000
5,000
2,000
1,000
Intron (86.1%) 500
200
100
50 20
Article https://doi.org/10.1038/s41592-023-02146-w
In tubes
(i) Fixation and permeabilization
(ii) Targeting RTase to RBP (iv) Library preparation
(iii) In situ RT
c
Noncoding exon (1.9%)
5′ UTR (0.1%)
CDS (2%) 2.5
3′ UTR (16.5%) 2.0
Intergenic (7.8%) 1.5
Intron (71.7%) 1.0
0.5
RBFOX2 (3,171 peaks)
0
Input rep1 rep2
P = 1 × 10–436 Mouse embryo HepG2
comparable signal detection efficiency of ARTR-seq for tissues and but not around native cassette exons and constitutive exons. We quan-
cultured cells (Fig. 3d). Examination of individual binding sites further tified relative RBP binding strength by ARTR-seq enrichment at the
supported the recognition of UGCAUG by RBFOX2 (Fig. 3e). Overall, gene level, and observed that genes with higher ARTR-seq enrichment
ARTR-seq can identify RBP binding sites in embedded tissue samples tend to present a higher splicing difference upon RBP-KD (Fig. 4e and
with high specificity. Extended Data Fig. 8c). In addition to exon skipping, the number of
included retained introns upon PTBP1-KD (491 events) outnumbered
ARTR-seq profiles regulatory features of splicing factors other splicing modes. With further inspection, we found that higher
PTBP1 and RBFOX2 are well-known splicing factors, with PTBP1 belong- enrichment corresponded to higher splicing inclusion differences
ing to the heterogeneous ribonucleoprotein (hnRNP) family35. To show of retained introns, similar to the trend observed for exon skipping
broader applicability of ARTR-seq, we also studied HNRNPC, another instances (Extended Data Fig. 8d). Altogether, ARTR-seq robustly
splicing factor belonging to the hnRNP family (Extended Data Fig. 8a). captures distinctive binding patterns for different splicing factors,
Consistent with the binding preference of the splicing factors, both and the ARTR-seq enrichment could indicate differences in splicing.
reads (over 70%) and peaks (over 80%) from the ARTR-seq libraries of
all three splicing factors (PTBP1, HNRNPC and RBFOX2) were mainly ARTR-seq identifies binding features of m6A reader proteins
located in introns in HepG2 cells (Fig. 4a,b and Extended Data Fig. 8b). In addition to sequence recognition, RBPs can also target RNAs in a
The RNA-binding motifs of RBFOX2 and HNRNPC were the canonical chemical modification-dependent manner. m6A modification is the
UGCAUG and U-rich sequences, respectively, consistent with the previ- most prevalent chemical modification in mammalian messenger RNA
ous report31 (Fig. 4a,b). (mRNA), and m6A reader proteins can preferentially bind m6A-modified
To explore the association between splicing factor binding and RNAs to regulate its processing and metabolism in both the nucleus and
splicing regulation, we identified the alternative splicing events by cytoplasm32,38–41. We performed ARTR-seq for two cytosolic m6A read-
comparing the ENCODE (Encyclopedia of DNA Elements) RNA sequenc- ers YTHDF1 and YTHDF2, and a nuclear reader YTHDC1 in HeLa cells.
ing (RNA-seq) data from RBP-knockdown (KD) cells with those from We first verified the subcellular localization of the three readers
control cells36. We found most alternative splicing events were cat- with ARTR-seq built-in imaging (Extended Data Fig. 9a). Sequencing
egorized as exon skipping (Fig. 4c). We then generated ‘splicing maps’ data from ARTR-seq remained highly reproducible between replicates
for exon skipping events37 (Fig. 4d). The corresponding ARTR-seq (Extended Data Fig. 9b). Over 80% of the peaks of the two cytoplasmic
peaks were predominantly enriched at upstream proximal introns of m6A readers (YTHDF1 and YTHDF2) were located in exons, whereas
the included exons upon RBP-KD, at downstream proximal introns roughly 81% of the peaks of nuclear reader YTHDC1 were located
of the excluded exons upon RBFOX2-KD and at both upstream and in introns or intergenic regions, consistent with their distinct sub-
downstream proximal introns of the included exons upon HNRNPC-KD, cellular localization (Fig. 5a and Extended Data Fig. 9a,c). The high
Nature Methods | Volume 21 | February 2024 | 247–258 252
elbasu
fo
egatnecreP
GUACGU
htiw
sdaer
a b
On slides
pAG-RTase Secondary Ab Nucleus Merge
RBFOX2
Optional, Imaging Mouse embryo (E11)
d e
Grip1 Prpf4b
119,543,200 bp 119,544,200 bp 35,080,800 bp 35,081,600 bp
[11] chr10 [8.58] chr13
Input
[11] [8.58]
RBFOX2
rep1
[11] [8.58]
RBFOX2
rep2
rep1 rep2
Fig. 3 | ARTR-seq maps RBP binding sites in tissues. a, ARTR-seq scheme for motifs (bottom) of RBFOX2 binding peaks identified by ARTR-seq in the mouse
tissue samples. A section of tissue is fixed on the slide for ARTR-seq. The RTase is embryonic tissue. P value was calculated by the two-tailed binomial test in the
attached to the RBP of interest by specific antibodies and a protein A/G fusion, HOMER suite52. d, A bar plot showing the percentage of usable reads containing
followed by in situ RT, with a built-in optional imaging step. The cDNA product the RBFOX2 canonical UGCAUG motif for mouse embryos and HepG2 cells.
is then collected for library preparation. b, Immunofluorescence imaging e, Snapshots from IGV showing overlap of RBFOX2 ARTR-seq signal in mouse
showing the localization of pAG-RTase (red), secondary Ab (yellow) and nucleus embryos with UGCAUG-containing sequences. The positions of the UGCAUG
(blue) in the mouse embryo section (E11). Scale bar, 20 μm. c, Peaks distribution motifs are indicated with arrows.
(top) in 3′ UTR, CDS, 5′ UTR, noncoding exon, intergenic region and intron, and
Article https://doi.org/10.1038/s41592-023-02146-w
1.0
0.8
0.6
0.4
P = 1 × 10–1,203
0.2
0
P = 1 × 10–170
unique peak ratios observed for the three reader proteins (84.2% for most likely affect their binding to different partner proteins and
YTHDC1, 34.3% for YTHDF1 and 47.5% for YTHDF2) are attributed to therefore different RNA targets42 (Extended Data Fig. 9d). We further
their unique subcellular localization; YTHDF1 and YTHDF2 display investigated the much more abundant non-exonic peaks of YTHDC1,
different sequences of the N-terminal low-complexity domains, which and found more than half of them located in repeat elements, with
Nature Methods | Volume 21 | February 2024 | 247–258 253
ecnereffid
noisulcnI
1,2657051,499 155 152 217 134 91 68 169 106 105 491 169 240
Include
AS mode SE MXE A5SS A3SS RI
0 Exclude
−0.2
−0.4
−0.6
−0.8
−1.0
859 7011,670 130 134 207 79 97 142 94 101 152 99 106 239
ecnereffid
noisulcxE
Splicing factor
/ PTBP1
/ RBFOX2
/ HNRNPC
Number
400
800
1,200
1,600
0.02
0.01
0
0.04
0.02
0
Exons excluded on RBP knockdown Native cassette exons all (1,805 events)
Exons included on RBP knockdown Constitutive exons (7,351 events)
05– 0 003
0.010
0.005
0
003– 0 05 05– 0 003 003– 0 05
PTBP1
RBFOX2
HNRNPC
seulav
dezilamroN
a c
b
d e
1.00
0.75
Exon excluded 0.50
Exon included 0.25
0
0 1 2 3 4
|Inclusion difference|
ytilibaborp
evitalumuC
Exons included
PTBP1
1.0
0.5
0
524 265 185
|ecnereffid
noisulcnI|
1.00
0.75
0.50
0.25
0
0 0.5 1.0 1.5 2.0
|Exclusion difference|
ytilibaborp
evitalumuC
1.0
0.5
Enrichment
No
Low 0
High 387 202 142
|ecnereffid
noisulcxE|
Noncoding exon (1.4%)
5′ UTR (0.1%)
CDS (0.1%)
3′ UTR (1.4%)
Intergenic (9.6%)
Intron (87.4%)
RBFOX2 (5,462 peaks)
Noncoding exon (0.3%)
5′ UTR (0.04%) 3′ UTR (0.5%)
Intergenic (8.6%)
Intron (90.5%)
HNRNPC (9,858 peaks)
Exons excluded
PTBP1
P = 5.2 × 10–3
P = 4.0 × 10–2
P = 2.0 × 10–3
P = 2.7 × 10–4
Enrichment
No
Low
High
Fig. 4 | RNA binding by splicing factors identified in ARTR-seq. a,b, Peaks peak density for skipped exons that were excluded (red) or included (blue) upon
distribution (right) in 3′ UTR, CDS, 5′ UTR, noncoding exon, intergenic region and corresponding splicing factor knockdown. Lines depict average ARTR-seq peak
intron, and the corresponding motifs (left) of RBFOX2 (a) and HNRNPC (b) peaks density. The confidence bounds show the standard errors of the alternatively
detected by ARTR-seq in HepG2 cells. P values were calculated by the two-tailed included or excluded events. e, Cumulative curves and boxplots (inset) showing
binomial test in the HOMER suite52. c, Boxplots showing the splicing differences the absolute value of exon splicing differences upon PTBP1 knockdown. PTBP1-
of five alternative splicing (AS) modes upon the knockdown of PTBP1 (green), regulated genes were divided into three groups according to their enrichment
RBFOX2 (orange) and HNRNPC (purple). The splicing modes include skipped exon in ARTR-seq, including no enrichment (No, 0 ≤ enrichment ≤ 1), low enrichment
(SE), mutually exclusive exon (MXE), alternative 5′ splice site (A5SS), alternative 3′ (Low, 1 < enrichment ≤ 2) and high enrichment (High, 2 < enrichment). The sample
splice site (A3SS) and retained intron (RI). The size of circles on the top or bottom size was labeled below the respective box. P values were determined by the two-
of each bar indicates event numbers. d, Normalized splicing maps37 showing the tailed Student’s t-test of the indicated group versus the ‘no enrichment’ group.
Article https://doi.org/10.1038/s41592-023-02146-w
4
3
2
1
0
1 kb 5′ UTR CDS 3′ UTR 1 kb
YTHDF1 YTHDF2 YTHDC1
long interspersed nuclear elements (roughly 45%) being the most Dynamic RNA binding of G3BP1 during SG assembly
prevalent, consistent with a previous report41 (Fig. 5b). Analysis of SGs are membraneless organelles composed of proteins and RNAs
exonic peak distribution along mRNA showed enrichment around and formed in response to stress. The RBP G3BP1 is the central node
stop codons for all these m6A readers, resembling the meta profile in the network of protein–RNA interaction during SG assembly43,44.
of m6A modifications, especially for YTHDF1 and YTHDF2 (ref. 33) Under sodium arsenite (NaAsO) treatment, SGs could be observed after
2
(Fig. 5c and Extended Data Fig. 9e). 13 min with a progressive increase in size over time, with most of the
Further, we calculated the percentage of exonic peaks overlap- SG assembly completed by 40 min, providing a rapid stress response45.
ping with m6A sites in polyadenylated RNAs identified by m6A-SAC-seq However, whether RNA targets of G3BP1 vary during SG assembly has
(ref. 33). The ARTR-seq peaks for all three readers showed higher per- yet to be investigated.
centages than random peaks, comparable to the YTHDF2 peaks from Taking advantage of the potential high temporal resolution
PAR-CLIP32, supporting the m6A-dependent binding features of these offered by fast formaldehyde fixation and low material requirements
three readers (Fig. 5d). We then analyzed the association between the of ARTR-seq, we performed ARTR-seq for G3BP1 in HeLa cells with
m6A fraction and RBP binding strength, and observed that the group 0.5 mM NaAsO treatment and monitored the SG assembly process
2
with higher m6A fractions showed higher RBP enrichment signals for at time intervals of 0, 10, 20 and 60 min poststress. We first visualized
YTHDF1 and YTHDF2, further suggesting ARTR-seq can measure the G3BP1 localization using immunofluorescence imaging, and con-
relative binding strength of RBPs (Fig. 5e). However, the association for firmed the gradual condensation of G3BP1 into granules over time
YTHDC1 was weaker, potentially due to the limited number of exonic (Fig. 6a). The colocalization of G3BP1 and biotinylated cDNA prod-
YTHDC1 peaks (Extended Data Fig. 9f). Overall, ARTR-seq captures dif- ucts was further verified (Fig. 6b). Subsequently, the verified sam-
ferent features of three m6A binding proteins in cytoplasm and nucleus. ples were used for ARTR-seq library construction and sequencing. We
Nature Methods | Volume 21 | February 2024 | 247–258 254
ytisneD
YTHDC1 intronic and intergenic peaks
(15,650 peaks)
Promoter (2%)
TTS (2%)
SINE (3%)
DNA (4%)
Others (6%)
LTR (7%)
LINE (45%)
Intergenic (8%)
Intron (23%)
1.00
0.75 m6A level
No
Low
0.50 Medium
High
0.25
0
0 2 4 6 0 2 4 6
log(peak enrichment) log(peak enrichment)
2 2
ytilibaborp
evitalumuC
YTHDF1
4
2
0
)tnemhcirne
kaep(gol
2
4
2
0
)tnemhcirne
kaep(gol
2
1.00
0.75
0.50
0.25
0
ytilibaborp
evitalumuC
a b c
d e
YTHDF2
m6A level
No
Low
Medium
High
405,22 953,2 853,2 853,2 457,62 631,3 531,3 531,3
Percentage of exonic peaks containing m6A
ARTR-seq
PAR-CLIP
10.7% 8.7% 5%
7% 3.2%
31.6% 3.7% 33.2% 1.9%
1.9%
45.2% 48%
YTHDF1 (29,740 peaks) YTHDF2 (36,436 peaks)
7.1%
0.6% 6.1% 3' UTR
4% CDS
5' UTR
53.3%
28.9% Noncoding exon
Intergenic
Intron
YTHDC1 (19,370 peaks)
Random
P = 1 × 10–138 P = 6 × 10–145
YTHDF1 P = 2 P × = 1 4 0 × –3 1 5 0–57 P = 2 P × = 1 0 3 – 2 × 0 10–57
YTHDF2
YTHDC1
YTHDF2.rep1
YTHDF2.rep2
YTHDF2.rep3
0 5 10 15 20 25
Fig. 5 | ARTR-seq maps binding features of the selected m6A binding proteins. YTHDF2 PAR-CLIP data were used as the positive controls32. e, Cumulative curves
a, Peaks distribution in 3′ UTR, CDS, 5′ UTR, noncoding exon, intergenic region and boxplots (inset) exhibit the log peak enrichment of ARTR-seq targets for
2
and intron of YTHDF1, YTHDF2 and YTHDC1 identified by ARTR-seq for HeLa YTHDF1 (left) and YTHDF2 (right). Peaks of m6A reader proteins were divided
cells. b, A pie chart showing the detailed genomic feature distribution of into four groups according to the modification fraction of the containing m6A
YTHDC1 intronic and intergenic binding peaks. LINE, long interspersed nuclear (sum value) quantified by m6A-SAC-seq. The peaks without m6A were categorized
elements. c, Aggregation profiles showing the meta distributions of binding in one group (No), and other peaks were divided into three groups with an
peaks for YTHDF1 (green), YTHDF2 (purple) and YTHDC1 (orange) along mRNA equal number of peaks, including low m6A fraction (Low), medium m6A fraction
transcripts. d, A bar plot showing the percentage of exonic peaks containing (Medium) and high m6A fraction (High). The sample size was indicated below
m6A sites detected by m6A-SAC-seq (ref. 33) for the m6A reader proteins. The the respective box. P values were determined by the two-tailed Student’s t-test of
random peaks are random exonic regions with the same lengths as pooled indicated group versus the ‘no m6A’ group.
ARTR-seq peaks from the three reader proteins. Three replicates of published
Article https://doi.org/10.1038/s41592-023-02146-w
NaAsO G3BP1 Biotin Nucleus Merge
2
G3BP1
60,000
40,000
20,000
0
0 1 2 3 4 5 6 7
G3BP1
Biotin
determined G3BP1 binding strength by calculating the ARTR-seq log SG enrichment of RNA was previously assessed by sequencing RNAs
2
fold change (logFC) between G3BP1 and input samples at the gene isolated from NaAsO-induced SGs to quantify their relative localiza-
2 2
level. Roughly 78% of G3BP1–RNA targets (logFC ≥ 1, P < 0.05) were tion within SGs46. Through integrative analysis, we observed that G3BP1
2
no longer enriched at 60 min (T60) post-NaAsO treatment (Fig. 6c). targets at T60 showed notably higher SG enrichment compared to
2
Nature Methods | Volume 21 | February 2024 | 247–258 255
ytisnetni
evitaleR
G3BP1 enriched genes
(ARTR-seq)
Nucleus
T0_only T60_only
1,012 (78%) 285 518 (65%)
Merge
SG-enriched
RNAs
2
0
−2
T0 T10 T20 T60 T0 T10 T20 T60
qes-RTRA
ni
htgnerts
gnidnib
1PB3G
SG-depleted
4 RNAs
2
0
−2
−4
qes-RTRA
ni
htgnerts
gnidnib
1PB3G
5 P = 1.94 × 10–22
P = 0.23
P = 8.43 × 10–21
4
3
2
1
0
T0_only
tnemhcirne
elunarg
ssertS
)7102(
.la
te
gnoK
Nucleocytoplasmic transport
Carbon metabolism GeneRatio
0.04
Spliceosome
0.06
Proteasome 0.08
Amyotrophic lateral sclerosis 0.10
Cell cycle
P Ribosome biogenesis in
0.0020 eukaryotes
0.0015 Aminoacyl−tRNA biosynthesis
0.0010 Platinum drug resistance
0.0005
Human papillomavirus infection
Protein processing in
endoplasmic reticulum
T0_only OL T60_only
OL T60_only (504) (147) (215)
T0 T10 T20 T60
Cluster 1 32,226,200 bp 32,226,500 bp t bp 128,190,400 bp
(1,509) [101] chr1 [74] chr2
T0
[101] [74]
Cluster 2 [101] [74]
(1,359)
T10 [101] [74]
[101] [74]
Cluster 3 T20 [101] [74]
(1,430)
[101] [74]
T60 [101] [74]
Cluster 4
(1,246)
G3BP1
binding
Cluster 5
strength
(1,223) T0 T10 T20 T60 T0 T10 T20 T60
)erocs
z(
htgnerts
gnidnib
1PB3G
a b
T0 T10 T20 T60
c
OL
d e f g
h i
EIF3I UGGT1
1
0
−1
1
0
−1
1
0
−1
1
0
−1
1
0
−1
T0 T10 T20 T60
G3BP1 binding strength
G3BP1 binding strength (z score) Membership values
−2 –1 0 1 2
−1.5 −1.0 −0.5 0 0.5 1.0 1.5 0 0.5 1.0
Article https://doi.org/10.1038/s41592-023-02146-w
Fig. 6 | Dynamic RNA binding of G3BP1 during the assembly of SGs. the clusterProfiler package53 using the one-tailed hypergeometric test.
a, Immunofluorescence imaging showing the localization of G3BP1 in HeLa f,g, Boxplots of G3BP1 binding strength for SG-enriched RNAs (n = 1,512, f) and
cells without treatment (T0) and with 0.5 mM NaAsO treatment for 10 min SG-depleted RNAs (n = 1,671, g). G3BP1 binding strength was defined as ARTR-seq
2
(T10), 20 min (T20) and 60 min (T60), respectively. Scale bars, 5 μm. reads logFC(G3BP1/input). SG-enriched RNAs and SG-depleted RNAs were
2
b, Immunofluorescence imaging (top) showing that G3BP1 (yellow) was colocalized obtained from a previous SG RNA-seq report46. h, A heatmap (left) depicting
with biotinylated cDNA (green) generated from ARTR-seq. The line graph analysis changing patterns of G3BP1 binding strength for RNA clusters across time.
(bottom) shows the relative fluorescence intensity along the line. Scale bar, RNAs were ranked from large to small according to the s.d. of G3BP1 binding
5 μm. c, A Venn diagram showing the overlap between the G3BP1–RNA targets intensity over different time intervals, and the top 50% of RNAs were selected and
at T0 and T60. d, A box plot exhibiting SG enrichment of RNA targets from three clustered by fuzzy c-means. Line plots (right) exhibit the corresponding change
groups defined in c, including T0 only (T0_only, n = 965) fraction, T0 and T60 of G3BP1 binding strength in each cluster. Each line represents one gene, with
overlapped (OL, n = 274) fraction and T60 only (T60_only, n = 482) fraction. SG the black line being the centroid of the cluster. i, IGV snapshots showing two
enrichment values were reported in SG RNA-seq46. P values were determined by G3BP1–RNA targets with decreased (left) and increased (right) binding strength,
the two-tailed Wilcoxon test. e, KEGG enrichment analysis showing RNA targets and each panel was normalized by counts per million. Heatmaps (bottom) show
from three groups are enriched in distinct pathways. P values were calculated by G3BP1 binding strength with the size of circles representing its absolute value.
the starting point without stress (Fig. 6d). These results support the potentially losing signals from nonpolyadenylated RNAs. Additionally,
accuracy of ARTR-seq and revealed distinct RNA binding of G3BP1 in the RT&Tag may experience reduced local resolution due to uniform RT
presence and absence of stress. The functions of stress-induced G3BP1 initiation from the poly-A tail and long matured mRNA length (roughly
targets (T60_only) were enriched to Kyoto Encyclopedia of Genes and 2,065 bp)50, leading to coverage bias toward the RNA 3′ end. Second,
Genomes (KEGG) pathways of protein processing in the endoplas- Tn5 tagmentation on the RNA–cDNA heteroduplex is less efficient,
mic reticulum and human papillomavirus infection, consistent with hindering its applications when using limited starting materials. Third,
previous observations47,48 (Fig. 6e). ARTR-seq can be applied in various cellular compartments, whereas
To further explore the dynamic RNA targeting of G3BP1 over RT&Tag is limited to the isolated nucleus.
time, we calculated pairwise correlations of the G3BP1 binding Investigations of dynamic RBP binding have been hindered by low
strength among time points. The generally low correlation coeffi- UV-crosslinking efficiency, long incubation time and high material
cients (R = 0.38–0.57) suggested distinct G3BP1 bindings at different demands using the existing methods. Benefiting from highly efficient
time intervals (Extended Data Fig. 10a). RNAs were previously classi- formaldehyde crosslinking and low starting material requirements,
fied into SG-enriched RNAs and SG-depleted RNAs according to their ARTR-seq excels at capturing transient RBP binding across various
SG enrichment46. We found that during SG assembly, G3BP1 binding time intervals. In this work, we have demonstrated its application in
strength from ARTR-seq gradually increased for SG-enriched RNAs capturing dynamic RNA binding of G3BP1 during SG assembly on a
and decreased for SG-depleted RNAs, suggesting a shift of G3BP1 timescale of 10 minutes. We envision that the high temporal resolution
targets toward SG-enriched RNAs (Fig. 6f,g). Some RNAs displayed of ARTR-seq will enable the investigation of dynamic or even transient
stable G3BP1 binding, while others showed dynamic G3BP1 binding RBP–RNA interaction in many other events.
across time intervals (Fig. 6h and Extended Data Fig. 10b,c). We then
grouped these RNAs based on G3BP1 binding strength using the Limitations
fuzzy c-means clustering algorithm. We found that G3BP1 binding The good quality of the primary antibody is a prerequisite for ARTR-seq.
strength for these RNAs displayed not only unidirectional trajecto- For those RBPs without good quality antibodies, ARTR-seq may not
ries of increasing or decreasing, but also transient changes during accurately capture RBP–RNA interactions. However, the availability of
60 minutes of NaAsO treatment, suggesting rapid and dynamic a suitable antibody is a common challenge faced by all antibody-based
2
cellular responses to stress (Fig. 6h,i and Extended Data Fig. 10d). methods. To overcome this limitation, strategies such as knocking in
Taken together, ARTR-seq unveiled the highly dynamic nature of a tag protein in frame with the targeted RBP or expressing the tagged
G3BP1–RNA interactions during SG assembly, demonstrating its RBP could be used.
capability in tracking temporal changes of protein–RNA interactions Formaldehyde fixation preserves biological samples at a high tem-
with limited starting materials. poral resolution, but limitations exist, such as perturbing biomolecular
condensates due to the faster protein–protein interaction dynamic
Discussion than the fixation rate51. Strategies to increase the fixation rate, such as
In this work, we present ARTR-seq, a method that captures RBP binding increasing the formaldehyde concentration or moderately raising the
sites using in situ RT by antibody-located RTase. ARTR-seq demon- fixation temperature, can mitigate such artifacts. Like most other meth-
strated high sensitivity and specificity, even when using as few as 20 ods, ARTR-seq may face challenges when applied to low-abundance
cells or limited tissues. The procedure is compatible with immunofluo- RBPs. Approaches such as increasing starting materials or RBP overex-
rescence imaging, providing direct spatial information of the targeted pression could be used. Additionally, unlike the editing-based methods,
proteins without affecting downstream sequencing. With ARTR-seq, which are compatible with long-read sequencing, ARTR-seq typically
we observed the unique binding characteristics of PTBP1, RBFOX2 shows short fragment lengths (averaging around 60 bp), hindering the
and HNRNPC related to their splicing regulatory roles. ARTR-seq also identification of isoform-specific binding patterns (Extended Data Fig.
detected the preferences of m6A reader proteins, YTHDF1, YTHDF2 6c). Last, the linker length needs to be optimized when detecting direct
and YTHDC1. Furthermore, we showed dynamic RNA binding of G3BP1 versus indirect targets using ARTR-seq, and RNase treatment could be
during SG assembly. considered to obtain higher resolution binding sites.
One advantage of ARTR-seq is the use of in situ RT to bypass the
antibody-based IP step, thereby reducing material loss. ARTR-seq is Online content
also highly versatile and applicable for cell lines, tissues, and even Any methods, additional references, Nature Portfolio reporting sum-
clinical formaldehyde-fixed samples. Both inspired by CUT&Tag49, maries, source data, extended data, supplementary information,
ARTR-seq displays distinct advantages compared to the recently acknowledgements, peer review information; details of author contri-
reported RT&Tag22. First, ARTR-seq uses random primers to unbias- butions and competing interests; and statements of data and code avail-
edly capture local signals, while RT&Tag uses oligo(dT) primer for RT, ability are available at https://doi.org/10.1038/s41592-023-02146-w.
Nature Methods | Volume 21 | February 2024 | 247–258 256
Article https://doi.org/10.1038/s41592-023-02146-w
References 23. Kaya-Okur, H. S. et al. CUT&Tag for efficient epigenomic profiling
1. Gerstberger, S., Hafner, M. & Tuschl, T. A census of human of small samples and single cells. Nat. Commun. 10, 1930 (2019).
RNA-binding proteins. Nat. Rev. Genet. 15, 829–845 (2014). 24. Anzalone, A. V. et al. Search-and-replace genome editing without
2. Gebauer, F., Schwarzl, T., Valcarcel, J. & Hentze, M. W. double-strand breaks or donor DNA. Nature 576, 149–157 (2019).
RNA-binding proteins in human genetic disease. Nat. Rev. Genet. 25. Potter, R. J. & Rosenthal, K. High fidelity reverse transcriptases and
22, 185–198 (2021). uses thereof. US patent US7056716B2 (2006).
3. Lerner, M. R. & Steitz, J. A. Antibodies to small nuclear RNAs 26. Coelho, M. B. et al. Nuclear matrix protein Matrin3 regulates
complexed with proteins are produced by patients with systemic alternative splicing and forms overlapping regulatory networks
lupus erythematosus. Proc. Natl Acad. Sci. USA 76, 5495–5499 (1979). with PTB. EMBO J. 34, 653–668 (2015).
4. Tenenbaum, S. A., Carson, C. C., Lager, P. J. & Keene, J. D. 27. Xue, Y. et al. Direct conversion of fibroblasts to neurons by
Identifying mRNA subsets in messenger ribonucleoprotein reprogramming PTB-regulated microRNA circuits. Cell 152,
complexes by using cDNA arrays. Proc. Natl Acad. Sci. USA 97, 82–96 (2013).
14085–14090 (2000). 28. The ENCODE Project Consortium. An integrated encyclopedia of
5. Ule, J. et al. CLIP identifies Nova-regulated RNA networks in the DNA elements in the human genome. Nature 489, 57–74 (2012).
brain. Science 302, 1212–1215 (2003). 29. Fred, R. G., Tillmar, L. & Welsh, N. The role of PTB in insulin mRNA
6. Licatalosi, D. D. et al. HITS-CLIP yields genome-wide insights into stability control. Curr. Diabetes Rev. 2, 363–366 (2006).
brain alternative RNA processing. Nature 456, 464–469 (2008). 30. Xue, Y. et al. Genome-wide analysis of PTB-RNA interactions
7. Hafner, M. et al. Transcriptome-wide identification of RNA-binding reveals a strategy used by the general splicing repressor to
protein and microRNA target sites by PAR-CLIP. Cell 141, modulate exon inclusion or skipping. Mol. Cell 36, 996–1006
129–141 (2010). (2009).
8. Konig, J. et al. iCLIP reveals the function of hnRNP particles in 31. Van Nostrand, E. L. et al. A large-scale binding and functional
splicing at individual nucleotide resolution. Nat. Struct. Mol. Biol. map of human RNA-binding proteins. Nature 583, 711–719
17, 909–915 (2010). (2020).
9. Van Nostrand, E. L. et al. Robust transcriptome-wide discovery of 32. Wang, X. et al. N6-methyladenosine-dependent regulation of
RNA-binding protein binding sites with enhanced CLIP (eCLIP). messenger RNA stability. Nature 505, 117–120 (2014).
Nat. Methods 13, 508–514 (2016). 33. Ge, R. et al. m6A-SAC-seq for quantitative whole transcriptome
10. Zarnegar, B. J. et al. irCLIP platform for efficient characterization m6A profiling. Nat. Protoc. 18, 626–657 (2023).
of protein-RNA interactions. Nat. Methods 13, 489–492 (2016). 34. Hafner, M. et al. CLIP and complementary methods. Nat. Rev.
11. Kargapolova, Y., Levin, M., Lackner, K. & Danckwardt, S. sCLIP-an Methods Prim. 1, 20 (2021).
integrated platform to study RNA-protein interactomes in 35. Dvinge, H. Regulation of alternative mRNA splicing: old players
biomedical research: identification of CSTF2tau in alternative and new perspectives. FEBS Lett. 592, 2987–3006 (2018).
processing of small nuclear RNAs. Nucleic Acids Res. 45, 36. Luo, Y. et al. New developments on the Encyclopedia of DNA
6074–6086 (2017). Elements (ENCODE) data portal. Nucleic Acids Res. 48, D882–
12. Masuda, A. et al. tRIP-seq reveals repression of premature D889 (2020).
polyadenylation by co-transcriptional FUS-U1 snRNP assembly. 37. Yee, B. A., Pratt, G. A., Graveley, B. R., Van Nostrand, E. L. & Yeo,
EMBO Rep. 21, e49890 (2020). G. W. RBP-Maps enables robust generation of splicing regulatory
13. Su, R. et al. Global profiling of RNA-binding protein target sites by maps. RNA 25, 193–204 (2019).
LACE-seq. Nat. Cell Biol. 23, 664–675 (2021). 38. Shi, H., Wei, J. & He, C. Where, when, and how: context-dependent
14. Blue, S. M. et al. Transcriptome-wide identification of functions of RNA methylation writers, readers, and erasers. Mol.
RNA-binding protein binding sites using seCLIP-seq. Nat. Protoc. Cell 74, 640–650 (2019).
17, 1223–1265 (2022). 39. Wang, X. et al. N6-methyladenosine modulates messenger RNA
15. Lorenz, D. A. et al. Multiplexed transcriptome discovery of translation efficiency. Cell 161, 1388–1399 (2015).
RNA-binding protein binding sites by antibody-barcode eCLIP. 40. Roundtree, I. A. et al. YTHDC1 mediates nuclear export of
Nat. Methods 20, 65–69 (2023). N6-methyladenosine methylated mRNAs. eLlife 6, e31311 (2017).
16. McMahon, A. C. et al. TRIBE: hijacking an RNA-editing enzyme to 41. Liu, J. et al. N6-methyladenosine of chromosome-associated
identify cell-specific targets of RNA-binding proteins. Cell 165, regulatory RNA regulates chromatin state and transcription.
742–753 (2016). Science 367, 580–586 (2020).
17. Brannan, K. W. et al. Robust single-cell discovery of RNA targets 42. Zou, Z., Sepich-Poore, C., Zhou, X., Wei, J. & He, C. The
of RNA-binding proteins and ribosomes. Nat. Methods 18, 507–519 mechanism underlying redundant functions of the YTHDF
(2021). proteins. Genome Biol. 24, 17 (2023).
18. Nguyen, D. T. T. et al. HyperTRIBE uncovers increased MUSASHI-2 43. Yang, P. et al. G3BP1 is a tunable switch that triggers phase
RNA binding activity and differential regulation in leukemic stem separation to assemble stress granules. Cell 181, 325–345 e328
cells. Nat. Commun. 11, 2026 (2020). (2020).
19. Xu, W., Rahman, R. & Rosbash, M. Mechanistic implications of 44. Protter, D. S. W. & Parker, R. Principles and properties of stress
enhanced editing by a HyperTRIBE RNA-binding protein. RNA 24, granules. Trends Cell Biol. 26, 668–679 (2016).
173–182 (2018). 45. Wheeler, J. R., Matheny, T., Jain, S., Abrisch, R. & Parker, R. Distinct
20. Flamand, M. N., Ke, K., Tamming, R. & Meyer, K. D. stages in stress granule assembly and disassembly. eLlife 5,
Single-molecule identification of the target RNAs of different e18413 (2016).
RNA binding proteins simultaneously in cells. Genes Dev. 36, 46. Khong, A. et al. The stress granule transcriptome reveals
1002–1015 (2022). principles of mRNA accumulation in stress granules. Mol. Cell 68,
21. Meyer, K. D. DART-seq: an antibody-free method for global m6A 808–820 e805 (2017).
detection. Nat. Methods 16, 1275–1280 (2019). 47. Chou, R. H. & Huang, H. Sodium arsenite suppresses human
22. Khyzha, N., Henikoff, S. & Ahmad, K. Profiling RNA at chromatin papillomavirus-16 E6 gene and enhances apoptosis in
targets in situ by antibody-targeted tagmentation. Nat. Methods E6-transfected human lymphoblastoid cells. J. Cell. Biochem. 84,
19, 1383–1392 (2022). 615–624 (2002).
Nature Methods | Volume 21 | February 2024 | 247–258 257
Article https://doi.org/10.1038/s41592-023-02146-w
48. Sun, H. et al. Sodium arsenite-induced learning and memory Publisher’s note Springer Nature remains neutral with regard to
impairment is associated with endoplasmic reticulum jurisdictional claims in published maps and institutional affiliations.
stress-mediated apoptosis in rat hippocampus. Front. Mol.
Neurosci. 10, 286 (2017). Open Access This article is licensed under a Creative Commons
49. Henikoff, S. & Ahmad, K. In situ tools for chromatin structural Attribution 4.0 International License, which permits use, sharing,
epigenomics. Protein Sci. 31, e4458 (2022). adaptation, distribution and reproduction in any medium or format,
50. Lopes, I., Altab, G., Raina, P. & de Magalhaes, J. P. Gene size as long as you give appropriate credit to the original author(s) and the
matters: an analysis of gene length in the human genome. Front. source, provide a link to the Creative Commons license, and indicate
Genet. 12, 559998 (2021). if changes were made. The images or other third party material in this
51. Irgen-Gioro, S., Yoshida, S., Walling, V. & Chong, S. Fixation can article are included in the article’s Creative Commons license, unless
change the appearance of phase separation in living cells. eLife indicated otherwise in a credit line to the material. If material is not
11, e79903 (2022). included in the article’s Creative Commons license and your intended
52. Heinz, S. et al. Simple combinations of lineage-determining use is not permitted by statutory regulation or exceeds the permitted
transcription factors prime cis-regulatory elements required use, you will need to obtain permission directly from the copyright
for macrophage and B cell identities. Mol. Cell 38, 576–589 holder. To view a copy of this license, visit http://creativecommons.
(2010). org/licenses/by/4.0/.
53. Wu, T. et al. clusterProfiler 4.0: a universal enrichment tool for
interpreting omics data. Innov. 2, 100141 (2021). © The Author(s) 2024
Nature Methods | Volume 21 | February 2024 | 247–258 258
Article https://doi.org/10.1038/s41592-023-02146-w
Methods Transfection
Cell culture and stress treatment PTBP1 siRNA was purchased from Horizon Discovery/Dharmacon.
HeLa cells (American Type Culture Collection (ATCC) catalog no. CCL-2) Cells were seeded in 30% confluency. After incubation for 12 h, siRNA
and HepG2 cells (ATCC, catalog no. HB-8065) were purchased from was transfected with RNAimax (Thermo Fisher Scientific) following
ATCC and cultured in DMEM medium (Gibco) supplemented with 10% the manufacturer’s manual. The fresh medium was changed at 6 h
fetal bovine serum (Gibco) and penicillin-streptomycin (Gibco). K562 posttransfection. Cells were cultured for another 48 h, and the protein
cells (ATCC, catalog no. CCL-243) were obtained from ATCC and cul- knockdown efficiency was quantified by western blot.
tured in RPMI 1640 Medium (Gibco) supplemented with 10% (v/v) fetal
bovine serum. Penicillin-streptomycin (Gibco) and 2 mM l-glutamine ARTR-seq
(Gibco). Cells were grown at 37 °C with 5% CO. For NaAsO treatment, Cells were fixed to an imaging-compatible chamber with 1.5% para-
2 2
HeLa cells were grown to 90% confluence and replaced in the pre- formaldehyde (PFA) at room temperature for 10 min. To mitigate cell
warmed DMEM medium containing 0.5 mM NaAsO, which was further loss, 1.5% PFA crosslinking was applied instead of the commonly used
2
maintained at 37 °C with 5% CO for indicated times. 1% PFA crosslinking. The samples were then quenched with 125 mM
2
glycine at room temperature for 5 min, washed twice with Dulbecco’s
Expression and purification of recombinant protein PBS (DPBS) and permeabilized with 0.5% Triton X-100 in DPBS on
A/G-RTase ice for 10 min. Each DPBS washing step involved 3 min of incubation
The recombinant plasmids were constructed by assembly of pet28A at room temperature. Next, samples were washed twice with DPBS,
vector, protein A/G (pAG), linkers of different lengths and RTase or the blocked with the blocking buffer (1 mg ml−1 UltraPure BSA, 0.2 U μl−1
modified RTase with NEBuilder HiFi DNA Assembly Master Mix (NEB) RNaseOUT in DPBS) at room temperature for 30 min and stained with
or USER enzyme (NEB) following the manufacturer’s protocols. The the diluted primary antibody at room temperature for 1 h. The primary
Protein A/G DNA segment was amplified from the pAG/MNase plas- antibody was diluted with blocking buffer according to the manufac-
mid (Addgene, catalog no. 123461). The engineered MMLV RTase was turer’s instructions for immunofluorescence or at a 1:200 dilution if
modified from the pCMV-PE2 plasmid (Addgene, catalog no. 132775). no specific guidance was provided. For input samples, the primary
The recombinant proteins were expressed in BL21(DE3) Competent antibody diluent was replaced by the blocking buffer. Subsequently,
Escherichia coli (NEB) with isopropyl-β-d-thiogalactoside induction samples were stained with fluorophore-labeled secondary antibody
at 16 °C for 18 h. Cells were collected by centrifuge at 5,500g for 10 min (1:500 diluted in the blocking buffer) at room temperature for 30 min,
and lysed in the buffer of 50 mM Tris-HCl pH 7.5, 300 mM NaCl and followed by incubation with pAG-RTase (10 nM in the blocking buffer)
1 mM PMSF with sonication at 10 s on and 10 s off setting for 10 min at for an additional 30 min. Cells were washed three times with DPBS after
4 °C. The recombinant proteins were purified from the supernatant each staining step by shaking at room temperature for 3 min.
using HisTrap HP column (GE Healthcare), followed by an ion exchange An RT reaction mixture was prepared by mixing 2 μM adapter-RT
chromatography column (GE Healthcare) on an AKTA Purifier 10 system primer (5′-AGACGTGTGCTCTTCCGATCTNNNNNNNNNN-3′), 0.05 mM
(GE Healthcare) according to the manufacturer’s protocol, and then biotin-16-dUTP (Jena Bioscience), 0.05 mM biotin-16-dCTP (Jena Bio-
concentrated to about 20 mg ml−1. The purified enzyme was supple- science), 0.05 mM dTTP (Thermo Fisher Scientific), 0.05 mM dCTP
mented with 40% glycerol and stored at −80 °C for future use. (Thermo Fisher Scientific), 0.1 mM dATP (Thermo Fisher Scientific),
0.1 mM dGTP (Thermo Fisher Scientific), 1 U μl−1 RNaseOUT (Thermo
RT–qPCR Fisher Scientific) in 50 μl buffer of DPBS supplemented with 3 mM
RNA was reverse transcribed with the purified pAG-RTases or commer- MgCl. In situ RT was performed by immersing cells with the RT reaction
2
cial RTases in reaction buffer (50 mM Tris-HCl, 150 mM NaCl, pH 7.5) at mixture and incubating at 37 °C for 30 min, then stopped by adding
37 °C for 15 min, and denatured at 85 °C for 5 min. qPCR was performed 20 mM EDTA and 10 mM EGTA and incubating at room temperature
with FastStart Essential DNA Green Master (Roche) on LightCycler 96 for 3 min.
System (Roche). The efficiency of RT was quantified using the delta Next, cells were stained with 1:200 diluted biotin monoclonal
quantitation cycle method. antibody (BK-1/39), alexa fluor 488 (Thermo Fisher Scientific) in DPBS
by incubation at room temperature for 1 h, followed by staining with
Protein detection by Coomassie brilliant blue stain and 1 μg ml−1 Hoechst 33342 dye (Thermo Fisher Scientific) at room tem-
western blot perature for 15 min. The samples were then imaged by Leica SP8 laser
The mammalian cell samples were lysed with cold RIPA buffer (Thermo confocal microscope. The fluorescence intensity distribution on a line
Fisher Scientific) containing 1× protease inhibitor cocktail (Roche). The was quantified by ImageJ software.
cell lysate was cleared with centrifugation at 15,000g for 10 min at 4 °C. After imaging, cells were digested with 1 mg ml−1 proteinase K
The supernatant or purified protein was then mixed with LDS loading (Thermo Fisher Scientific) at 37 °C for 2 h. The nucleic acids were recov-
buffer (Bio-Rad) and boiled at 95 °C for 10 min. Denatured protein ered by phenol-chloroform extraction (pH 8.0) and concentrated by
was loaded into 4–12% NuPAGE Bis-Tris gel (Thermo Fisher Scientific). ethanol precipitation. RNA was digested with 0.2 U μl RNase H (NEB)
For Coomassie brilliant blue stain, the gel was stained with Imperial and 1:20 diluted RNase A/T1 (Thermo Fisher Scientific) in 50 μl of the
Protein Stain (Thermo Fisher Scientific) and imaged by FluroChem RNase reaction buffer (50 mM Tris-HCl pH 7.5, 75 mM KCl, 10 mM MgCl,
2
R (Proteinsimple). For the western blot, the protein was transferred 10 mM DTT) at 37 °C for 1 h, followed by biotinylated cDNA enrichment
to the polyvinyl difluoride membrane from the gel. The membranes using 10 μl preblocked Dynabeads MyOne Streptavidin C1 (Thermo
were blocked in 3% BSA (diluted in PBST (PBS with 0.1% Tween-20)) Fisher Scientific) at room temperature for 20 min. The beads were
for 1 h at room temperature, incubated in a 1:1,000 diluted primary preblocked with 1 μg μl−1 UltraPure BSA (Thermo Fisher Scientific),
antibody solution at 4 °C overnight, washed four times with PBST (PBS 1 μg μl−1 UltraPure Salmon Sperm DNA Solution (Thermo Fisher Scien-
with 0.1% Tween-20), and incubated in a 1:5,000 dilution of horserad- tific) and 1 μg μl−1 Yeast transfer RNA (tRNA) (Thermo Fisher Scientific)
ish peroxidase (HRP)-conjugated secondary antibody for 1 h at room with incubation at room temperature for 30 min before performing
temperature if the primary antibody was not conjugated with HRP. biotinylated cDNA enrichment.
The membranes were supplied with SuperSignal West Dura Extended Subsequently, the cDNA adapter ligation mixture was prepared
Duration Substrate kit (Thermo Fisher Scientific) and imaged on the by combining 50 mM Tris-HCl pH 7.5, 10 mM MgCl, 25% PEG 8000,
2
FluroChem R machine (Proteinsimple). Quantification was performed 1 mM ATP, 1 U μl−1 T4 RNA ligase 1 (NEB), and 5 μM of 3′ cDNA adapter
using ImageJ software (v.2.3.0). (5′Phos-NNNNNNNNAGATCGGAAGAGCGTCGTGT-3′SpC3). The 3′ cDNA
Nature Methods
Article https://doi.org/10.1038/s41592-023-02146-w
adapter ligation was performed by suspending the beads in the cDNA M29) and Drosophila melanogaster (BDGP6.32, Ensembl Release 107)
adapter ligation mixture and incubating at 25 °C for 16 h. The biotinylated were used for mapping the sequencing reads in this study. Riboso-
cDNA was recovered using an elution buffer composed of 95% (v/v) for- mal RNA (rRNA) reference sequences were downloaded from the
mamide and 10 mM EDTA (pH 8.0) by boiling at 95 °C for 10 min, followed National Center for Biotechnology Information (NCBI) for H. sapiens
by ethanol precipitation. The cDNA was then dissolved in 10 μl of water. (NR_003285.3, NR_003286.4, NR_003287.4, NR_023363.1), M. musculus
For library amplification, 40 μl of mixture was prepared by mix- (NR_003278.3, NR_003279.1, NR_003280.2, NR_046156.1) and from
ing 1× NEBNext Ultra II Q5 Master Mix (NEB), 10 μl of cDNA solution FlyBase for D. melanogaster (5SrRNA-CR33353, 18SrRNA-CR45841,
and 0.5 μM Illumina sequencing primers, such as NEBNext Multiplex 5.8SrRNA-CR45842 and 28SrRNA-CR4584)
Oligos for Illumina (NEB catalog no. E7335S). The library PCR amplifi-
cation followed this program: 98 °C for 30 s (98 °C for 10 s, 60 °C for ARTR-seq primary data processing
30 s, 65 °C for 45 s) for 13 cycles and 65 °C for 5 min; hold at 4 °C. The Reads from the small cell number libraries containing cell barcodes were
final libraries were purified using 6% Novex TBE Gel (Thermo Fisher first demultiplexed with an in-house script using read 2. The adapter
Scientific) with size selection between 180 and 400 bp. Next-generation sequences were trimmed with Cutadapt54 (v.4.2) using the parameter
sequencing was carried out either at the University of Chicago Single cutadapt–nextseq-trim=20 -a AGATCGGAAGAGCACACGTCTGAACTC-
Cell Immunophenotyping Core on an Illumina NextSeq 550 machine CAG; the 8 nt unique molecular identifier sequences were moved and
or Illumina NextSeq 2000 machine, or at the University of Chicago add to the read name for the further deduplication. An extra 4 nts at
Genomics Facility on an Illumina NovaSeq 6000 platform. the reads’ 3′ end were removed from the adapter-free sequence to
minimize mapping mismatch caused by the imperfect paired sequence
RNase treatment in ARTR-seq in the random primer.
RNase treatment was incorporated into the ARTR-seq procedure with The reads were first mapped to the corresponding rRNA
the following modifications: After permeabilization, Cells were incu- sequences using Bowtie2 (ref. 55) (v.2.4.4) with parameters: –seed-
bated with 1 U μl−1 RNase I (Thermo Fisher Scientific) at 37 °C for 5 min, len=15, and the mapped reads were discarded to avoid rRNA con-
followed by two washes with DPBS. For samples with strong RNase tamination. The remaining unmapped reads were mapped to the
treatment, an additional RNase I treatment was conducted as previ- corresponding genome using STAR56 (v.2.7.9a) with parameters: –
ously described before initiating RT. readFilesCommand zcat–alignEndsType EndToEnd–genomeLoad
NoSharedMemory–quantMode TranscriptomeSAM–alignMates-
Dot blot GapMax 15000–outFilterMultimapNmax 1–outFilterMultimap-
After the proteinase K digestion step in ARTR-seq, the total nucleic ScoreRange 1–outSAMprimaryFlag AllBestScore–outSAMattributes
acids were recovered with Oligo Clean & Concentrator Kits (Zymo) to All–outSAMtype BAM SortedByCoordinate–outFilterType BySJout–
get rid of free biotinylated dNTP. The concentration of nucleic acids outReadsUnmapped Fastx–outFilterScoreMin 10–outFilterMatchN-
was measured by Nanodrop 8000 Spectrophotometer and adjusted min 24. Uniquely mapped reads were deduplicated to get the usable
to 50 ng μl−1. Next, 1 μl of nucleic acids were loaded onto the Amersham reads using UMI-tools57 (v.1.1.2) with the parameter, –method unique.
Hybond- N+ membrane (GE Healthcare). Membranes were air-dried The usable reads were assigned to genomic regions with RNASeQC58
and crosslinked by UV strata linker 2400 at 150 mJ cm−2 twice. The (v.2.4.2) using default parameters. Deduplicated reads were assigned
membranes were then blocked in 5% fatty-acid-free BSA in PBST at to genes with featureCounts59 (v.2.0.3) for the calculation of Pearson’s
room temperature for 1 h, followed by incubation in streptavidin-HRP correlation coefficient between biological replicates. For visualiza-
(Thermo Fisher Scientific) in PBST supplemented with 5% fatty-acid free tion in IGV60 (v.2.13.1), .bam files of the usable reads were converted
BSA at room temperature for another 1 h. The membrane was washed to bigWig with bamCoverage in the deepTools suite61 (v.3.5.1) with
with PBST four times before being supplied with SuperSignal West normalization by its respective sequencing depth using the param-
Dura Extended Duration Substrate kit (Thermo Fisher Scientific) and eters –normalizeUsing BPM–binSize 1. All the sample tracks were set
imaged by the FluroChem R machine (Proteinsimple). to the same scale for display, except for the additional instruction
noted in the legend.
ARTR-seq in the mouse embryo
C57 mouse embryo (E11) frozen tissue sections were purchased from Peaking calling
Zyagen. The slide with frozen tissue sections was brought to room For peak calling, we first split the usable reads in one library into
temperature for 10 min of incubation. The PAP pen was used to draw a two .bam files containing reads aligned to the positive and negative
circle around the mouse tissue on the slide, providing a thin film-like strands, respectively. We used macs3 (ref. 62) to identify peaks with
hydrophobic barrier for reagent incubation. Then the tissue was sub- default parameters, except for adding ‘–keep-dup all–nomodel –ext-
jected to typical ARTR-seq procedures with the following change. The size 30’. macs3 gives the fold enrichment (signal value) and P value
2 μM adapter-barcoded RT primer (5′-AGACGTGTGCTCTTCCGATCT- based on Poisson distribution, and corrects the P values for multiple
(8 nt-barcode)-NNNNNNNNNN-3′) was applied for in situ RT. comparison using the Benjamini–Hochberg correction. The peaks
located in two strands were called separately using the corresponding
ARTR-seq with low input strand read in the input libraries as background. The two peak files for
ARTR-seq was applied to 20 to 5,000 HepG2 cells with the following one library were later combined. To generate the consensus motif for
changes. 4% PFA was used to minimize cell loss for low-input samples. peaks, we first extended 20 nts to both upstream and downstream,
The 2 μM adapter-barcoded RT primer (5′-AGACGTGTGCTCTTCCGATCT and the overrepresented sequences were generated using findMo-
-(8 nt-barcode)-NNNNNNNNNN-3′) was applied for in situ RT. After tifsGenome.pl in the HOMER suite52 (v.4.11) with parameters: -rna -S
digestion of proteinase K, two biological replicates were pooled 10 -len 5,6,7,8,9. Specifically, for motif generation for peaks in mouse
together for biotinylated cDNA enrichment, adapter ligation, library tissue, the peak genomic coordinates were converted from mm39 to
amplification and library sequencing. Sequence data were isolated mm10 using liftOver from the UCSC Genome Browser63. Peaks were
based on the 8 nt barcode in adapter-barcoded RT primers. assigned to specific genomic regions with in-house scripts, and the
peaks overlapping two genomic regions were assigned to the region of
Genome reference longer overlapping base pairs. The peaks from the reader YTHDC1 were
Genome and the corresponding reference of Homo sapiens (GRCh38. further assigned to repeats and other regions with annotatePeaks.pl
p13, GENCODE Release 39), Mus musculus (GRCm39, GENCODE Release in the HOMER suite.
Nature Methods
Article https://doi.org/10.1038/s41592-023-02146-w
Subsampling package. Clustering was calculated by the ‘mfuzz’ function in the Mfuzz
To calculate the percentage of usable reads at different sequencing package with 10,000 iterations with Euclidean distance as the cluster-
depths, we subsample the uniquely mapped reads with the samtools ing method. The membership values indicate the degree of association
view in the Samtools suite64 (v.1.16.1). For the comparison between of genes with their respective clusters.
small cell number input libraries for different methods, the sizes of
all libraries were reduced to that of the smallest library. Specifically, Functional enrichment analysis
instead of directly subsampling the fastq files, we subsampled the KEGG enrichment analysis was carried out to compare G3BP1–RNA
uniquely mapped reads to calculate the usable read percentage of targets at different time points using the ‘compareCluster’ function in
each library. the clusterProfiler package53 (v.4.4.4). The KEGG terms with adjusted
P values less than 0.05 were visualized.
Alternative splicing identification
The differential alternative splicing events of each gene were identified Statistics and reproducibility
using rMATS (v.4.1.2). The RBP-knockdown RNA-seq libraries bam files Unless otherwise stated, a two-tailed Student’s t-test or Wilcoxon
and the corresponding control libraries’ .bam files with the annotation test were performed to assess the statistical significance between
of ENCODE4 v.1.2.1 GRCh38 V29 were downloaded from the ENCODE groups. The resulting P values are indicated in the figure or legends.
and were analyzed by rMATS for the identification of five alternative For boxplots, the box represents the 25th to 75th percentiles with a
splicing modes, including skipped exon, mutually exclusive exons, line at the median, whiskers to 1.5 times the interquartile range, a dot
alternative 3′ splice site, alternative 5′ splice site and retained introns. at the mean (if applicable) and outliers omitted. Immunofluorescence
Events of FDR ≥ 0.05 were discarded for the subsequent analysis. imaging experiments were repeated in at least two biological samples
with consistent results.
ARTR-seq enrichment level at the gene level
To calculate the ARTR-seq enrichment at the gene level, we divided Reporting summary
the reads in one library into two groups by whether they were in one Further information on research design is available in the Nature Port-
specific gene, and had a pair of in–out read numbers for each of the folio Reporting Summary linked to this article.
IP and Input libraries. For each gene, we generated two-by-two tables
for all the combinations of in–out read numbers between IP and Input Data availability
libraries. The ARTR-seq enrichment for a gene is defined as the common All the sequencing data generated in this study have been deposited
odds ratio of the tables with significance determined by the Cochran– in the NCBI’s Gene Expression Omnibus (GEO) under the accession
Mantel–Haenszel chi-squared test. number GSE226161. Previously published data are available under
accession numbers GSE42701 (CLIP-seq26), ENCSR384KAN and ENC-
Data visualization and statistical analysis SR981WKN (eCLIP28), E-MTAB-3108 (iCLIP27), GSE78832 (irCLIP10),
Read heatmaps and profiles were generated with plotHeatmap and GSE137925 (LACE-seq13), GSE92995 (sCLIP11), DRA005743 (tRIP-seq12)
plotProfile in the deepTools suite61 (v.3.5.1), using genomic coordinates and GSE195654 (RT&Tag22). The data were downloaded and processed
unless otherwise indicated. The splicing maps of splicing factors are as described in the articles. The processed .bam files of RNA-seq data for
generated by RBP-Maps37 with default parameters in the ‘Plotting knockdown HNRNPC, PTBP1 and RBFOX2, along with their correspond-
peaks’ mode (–peak), and the hg19 coordinates of native cassette exons ing control data, were downloaded from ENCODE portal28 under the
and constitutive exons were downloaded from the software GitHub accession numbers of ENCSR052IYH, ENCSR305XWT, ENCSR767LLP,
deposit. The peak genomic coordinates of the peaks for the splicing ENCSR104ABF, ENCSR064DXG and ENCSR603TCV. The published
factors were first converted from GRCh38 to hg19 using liftOver from PAR-CLIP data and the corresponding peaks for YTHDF2 are available
the UCSC Genome Browser63. The random regions are random exonic under the GEO accession number GSE49339. The m6A modification
regions with the same length as pooled ARTR-seq peaks from the three sites identified by m6A-SAC-seq are available under the GEO accession
m6A reader proteins, generated by bedtools shuffle in the BEDTools number GSE198246. Source data are provided with this paper.
suite65 (v.2.30.0).
The meta distributions of binding peaks were generated by the Code availability
R package Guitar66 (v.2.16.0). All statistical analyses were performed Codes for processing ARTR-seq data are available in the following
with R67, and all the plots were generated by the R package ggplot2 GitHub repository: https://github.com/mingming-cgz/ARTR-seq.
(ref. 68) (v.3.4.1).
References
Quantification of ARTR-seq signal at the gene level 54. Martin, M. Cutadapt removes adapter sequences from
To analyze G3BP1 binding strength at the gene level, ARTR-seq reads high-throughput sequencing reads. EMBnet. J. 17, 10–12 (2011).
were counted for genes in both G3BP1 and paired input samples, and 55. Langmead, B. & Salzberg, S. L. Fast gapped-read alignment with
FCs and significance between G3BP1 and input were determined by Bowtie 2. Nat. Methods 9, 357–359 (2012).
DESeq2 (ref. 69). Only genes with the read sum equal to or greater than 56. Dobin, A. et al. STAR: ultrafast universal RNA-seq aligner.
ten for G3BP1 and input samples were considered. RNA targets of G3BP1 Bioinformatics 29, 15–21 (2013).
were defined as those with a FC ≥ 2 and P < 0.05. Both FC and P value 57. Smith, T., Heger, A. & Sudbery, I. UMI-tools: modeling sequencing
were calculated by DESeq2 with the default setting. errors in unique molecular identifiers to improve quantification
accuracy. Genome Res. 27, 491–499 (2017).
Clustering analysis of G3BP1 ARTR-seq signal 58. Graubert, A., Aguet, F., Ravi, A., Ardlie, K. G. & Getz, G. RNA-SeQC
To track the changing pattern of G3BP1 binding single during the SG 2: efficient RNA-seq quality control and quantification for large
assembly, we used logFC (G3BP1/input) of genes to represent the cohorts. Bioinformatics 37, 3048–3050 (2021).
2
G3BP1 binding signal, and performed fuzzy c-means clustering analysis 59. Liao, Y., Smyth, G. K. & Shi, W. featureCounts: an efficient general
on logFC by the Mfuzz package70 (v.2.54.0). Only genes with the top purpose program for assigning sequence reads to genomic
2
50% of the greatest standard deviation (s.d.) of logFC were considered, features. Bioinformatics 30, 923–930 (2014).
2
and the logFC values were scaled by z score before clustering. The 60. Robinson, J. T. et al. Integrative Genomics Viewer. Nat. Biotechnol.
2
cluster number was determined by the ‘Dmin’ function in the Mfuzz 29, 24–26 (2011).
Nature Methods
