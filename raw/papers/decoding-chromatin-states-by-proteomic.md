---
source_path: /mnt/c/Users/Administrator/Zotero/storage/5W5W5QRT/Lukauskas 等 - 2024 - Decoding chromatin states by proteomic profiling o.pdf
ingested: 2026-04-23
sha256: ca740c8927bdd8f5
---

Article
Decoding chromatin states by proteomic
profiling of nucleosome readers
https://doi.org/10.1038/s41586-024-07141-5 Saulius Lukauskas1,2,3,17, Andrey Tvardovskiy1,17, Nhuong V. Nguyen2,4,17, Mara Stadler1,5,6,
Peter Faull2,7,15, Tina Ravnsborg8, Bihter Özdemir Aygenli1, Scarlett Dornauer1, Helen Flynn7,
Received: 10 May 2021
Rik G. H. Lindeboom9,10, Teresa K. Barth11,16, Kevin Brockers1, Stefanie M. Hauck11,
Accepted: 31 January 2024 Michiel Vermeulen9,10, Ambrosius P. Snijders7, Christian L. Müller5,6,12, Peter A. DiMaggio3,
Ole N. Jensen8, Robert Schneider1,13,14 & Till Bartke1,2,4 ✉
Published online: xx xx xxxx
Open access
DNA and histone modifications combine into characteristic patterns that demarcate
Check for updates
functional regions of the genome1,2. While many ‘readers’ of individual modifications
have been described3–5, how chromatin states comprising composite modification
signatures, histone variants and internucleosomal linker DNA are interpreted is a major
open question. Here we use a multidimensional proteomics strategy to systematically
examine the interaction of around 2,000 nuclear proteins with over 80 modified
dinucleosomes representing promoter, enhancer and heterochromatin states.
By deconvoluting complex nucleosome-binding profiles into networks of co-regulated
proteins and distinct nucleosomal features driving protein recruitment or exclusion,
we show comprehensively how chromatin states are decoded by chromatin readers.
We find highly distinctive binding responses to different features, many factors that
recognize multiple features, and that nucleosomal modifications and linker DNA
operate largely independently in regulating protein binding to chromatin. Our online
resource, the Modification Atlas of Regulation by Chromatin States (MARCS), provides
in-depth analysis tools to engage with our results and advance the discovery of
fundamental principles of genome regulation by chromatin states.
Almost all genetic material of eukaryotic cells is stored in the nucleus combinatorial modification patterns underlying chromatin states are
in the form of chromatin, a nucleoprotein complex comprising DNA, interpreted is largely unclear.
histones and other structural and regulatory factors. DNA and histones To obtain a comprehensive understanding of how chromatin readers
carry chemical modifications that have central roles in chromatin regu- decode different chromatin states, we have implemented a multidimen-
lation by either directly affecting chromatin structure or by recruiting sional mass spectrometry (MS)-based chromatin profiling strategy
reader proteins that mediate downstream events through specialized combining large-scale nucleosome affinity purification25 and chromatin
binding domains4,6. Chromatin modifications rarely occur in isolation immunoprecipitation (ChIP)–MS approaches with computational
but exist in specific combinations on histones or nucleosomes, often methods for the integrative analysis of high volumes of proteomics and
also involving histone variants7–12. As these combinations are highly next-generation sequencing (NGS) data. We performed over 80 affinity
correlated and predictable13,14, they form the basis for the definitions purification experiments with semisynthetic dinucleosomes contain-
of ‘chromatin states’ that are used to annotate functional regions in ing modification signatures and DNA linkers representing promoter,
the genome such as enhancers, promoters, gene bodies and hetero- enhancer or heterochromatin states1,10,26, and identified close to 2,000
chromatin1,2. nucleosome-interacting proteins, including transcription, replication,
Most chromatin regulators contain several modification-binding remodelling and DNA repair factors. Systematically quantifying their
domains, indicating that recognizing multiple modifications is an inte- binding to the different modification states enabled the discovery of
gral function of many nuclear proteins15. However, although readers of co-regulated proteins and complex chromatin modification read-outs
individual modifications are often well understood3–5, only few factors driven by particular nucleosomal features, thereby revealing basic
recognizing multiple modifications are known16–24. Thus, how complex principles of how chromatin readers decode the chromatin landscape.
1Institute of Functional Epigenetics, Helmholtz Zentrum München, Neuherberg, Germany. 2MRC Laboratory of Medical Sciences (LMS), London, UK. 3Department of Chemical Engineering,
Imperial College London, London, UK. 4Institute of Clinical Sciences (ICS), Faculty of Medicine, Imperial College London, London, UK. 5Institute of Computational Biology, Helmholtz Zentrum
München, Neuherberg, Germany. 6Department of Statistics, Ludwig Maximilian University Munich, Munich, Germany. 7Proteomic Sciences Technology Platform, The Francis Crick Institute,
London, UK. 8VILLUM Center for Bioanalytical Sciences and Department of Biochemistry and Molecular Biology, University of Southern Denmark, Odense, Denmark. 9Department of Molecular
Biology, Faculty of Science, Radboud Institute for Molecular Life Sciences, Oncode Institute, Radboud University Nijmegen, Nijmegen, The Netherlands. 10The Netherlands Cancer Institute,
Amsterdam, The Netherlands. 11Metabolomics and Proteomics Core, Helmholtz Zentrum München, Munich, Germany. 12Center for Computational Mathematics, Flatiron Institute, New York, NY,
USA. 13Faculty of Biology, Ludwig Maximilian University Munich, Martinsried, Germany. 14German Center for Diabetes Research (DZD), Neuherberg, Germany. 15Present address: Northwestern
Proteomics Core Facility, Northwestern University, Chicago, IL, USA. 16Present address: Clinical Protein Analysis Unit (ClinZfP), Biomedical Center (BMC), Faculty of Medicine, Ludwig Maximilian
University Munich, Martinsried, Germany. 17These authors contributed equally: Saulius Lukauskas, Andrey Tvardovskiy, Nhuong V. Nguyen. ✉e-mail: till.bartke@helmholtz-munich.de
Nature | www.nature.com | 1
Article
SNAP from HeLa S3 cell nuclear extract
me3 ac ac
H3.1ARTKQTARKSTGGKAPRKQLATKAARK
ac ac ac ac me2
H4 SGRGKGGKGLGKGGAKRHRK
Quantification of nucleosome–protein
interactions by MS
8 EExxcclluuddeedd bbyy
mmooddiifificcaattiioonnss
4
SLF1
SUZ12 KDM2B
0 CB E X Z 5 H2 IN M O E 8 C 0 P B 2
UHRF1 PBRM1
SRCAP TAF3
–4 Recruited by
modifications ORC2 PH B F R 8 D3
–8 SMAR B C R C D 1 4
–8 –4 0 4 8
To make our data easily accessible, we have developed computational Fig. 1a). The label swap enables unbiased identification of proteins that
tools to analyse and visualize the nucleosome-binding data and we are reproducibly either recruited or excluded by the modification(s).
have implemented them in the interactive online resource MARCS Moreover, the SILAC heavy/light (H/L) ratios also indicate a relative
(https://marcs.helmholtz-munich.de/). Our results bridge the gap strength of recruitment or exclusion of a protein by the modifications
between chromatin states and chromatin readers, and we anticipate (Fig. 1c). After optimizing our SNAP methodology (Supplementary
that MARCS will become a valuable resource to drive future chromatin Information) for a large-scale comparison of interactomes of different
research forward as numerous other observations emerge. chromatin states, we used single-end biotinylated dinucleosomes in
all SNAP experiments.
To understand how distinct chromatin states marked by combi-
Proteomic profiling of chromatin readers
nations of modifications are read by binding proteins, we created a
To systematically profile the interactomes of chromatin modifications library of nucleosomes incorporating biologically relevant modifica-
in the nucleosomal context, we performed SILAC nucleosome affinity tion signatures, including mono- and tri-methylation of lysine 4 of
purification (SNAP)25. We assembled nucleosomes from biotinylated histone H3 (H3K4me1/3), di- and tri-methylation of lysines 9 and 27
DNA and histone octamers containing site-specifically modified of histone H3 (H3K9me2/3 and H3K27me2/3), di- and tri-methylation
histones H3.1 and H4 prepared by native chemical ligation27 (Fig. 1a) of lysine 20 of histone H4 (H4K20me2/3), varying degrees of acetyla-
and used them in forward and reverse SILAC nucleosome pull-down tion of lysines (Kac), the histone variant H2A.Z or CpG-methylated
experiments in HeLa S3 cell nuclear extracts (Fig. 1b and Extended Data DNA. This design of the nucleosome library enabled us to capture the
2 | Nature | www.nature.com
oitar
L/H
demrofsnart-2gol
,tnemirepxe
esreveR
]2em02Kca4H3em4K3H/defiidomnu[2gol
a Native chemical ligation and d Repressive modification signatures
assembly of modified dinucleosomes Activating modification signatures
H3K9me H3K4me1
+ + H3K27me H3K4me3
H3ac
meDNA H4ac
H4 1–28 H4 Δ1–28 H3.1 1–31 H3 Δ1–31 H2A.Z
H4K20me
H4 H3.1
H2A.Z Nucleosome composition
H2B H2A/H2A.Z H3K4 Lysine PTMs
H3K9 Monometh. Dimeth.
601 601 Biotin o + r m5C H H 3 3 K K 1 1 4 8 T A r c im et e y t l h at . ion
Di-601 DNA (unmodified/methylated) H3K23 Histone variants
H3K27
H2A.Z
H4K5
b H4K8 DNA modifications
H4K12 meCpG
H4K16
H4K20
meDNA
e * * *
KDM2B
Protein response
MECP2 log2[H/L ratio]
†ORC2 Forward experiment
Reverse experiment
SLF1 (inverse ratio)
UHRF1 –4–2 –1 0 1 2 4
CBX5 Exclusion Binding
c
CBX4 log10[MS1 intensity]
CBX8 ≤4 ≥10
RNF2
†EZH2
SMARCC1
PBRM1
†PHF8
TAF3
†BRD4
BRD3
INO80B
SRCAP
Forward experiment, log2-transformed H/L ratio
log2[H3K4me3H4acK20me2/unmodified]
Fig. 1 | Large-scale identification of chromatin readers by SILAC dinucleosomes. A header specifies the modification status of each
dinucleosome affinity purifications. a, Generation of modified nucleosome. Nucleosomes are arranged in columns, with the respective
dinucleosomes. Modified histones H3.1 and H4 were prepared by native modifications displayed in rows. Modifications of specific lysine residues in
chemical ligations of N-terminal tail peptides (H3, amino acids 1–31; H4, amino histone H3 and H4 and the presence of DNA methylation (meCpG) or H2A.Z
acids 1–28) to truncated histone cores (H3.1Δ1–31T32C or H4Δ1–28I29C, are colour coded as indicated. Nucleosomes are ordered to imitate clustering
respectively). Note that this introduces H3T32C and H4I29C mutations that by increasingly active chromatin states. Monometh., monomethylation;
might affect protein binding to nearby modifications. Ligated histones were PTMs, post-translational modifications. e, Visualization of protein binding
refolded into octamers and assembled into dinucleosomes using a biotinylated responses to the 55 modified dinucleosomes profiled by SNAP. The log[H/L]
2
DNA containing two nucleosome-positioning sequences (di-601)47. For some ratios for each protein in each SNAP experiment are shown as circles, with the
experiments, CpG-methylated DNA (m5C) or H2A.Z were used. b, SNAP right half representing the forward and the left half the reverse log[H/L ratio].
2
purifications. Modified nucleosomes were immobilized on streptavidin beads Recruitment (red) and exclusion (blue) are indicated. The reverse H/L ratio was
and incubated with nuclear extracts from HeLa S3 cells grown in isotopically inverted to display both ratios on the same scale. Circle sizes denote the total
light (RK) or heavy (R K) SILAC medium. c, Protein responses to modified MS1 peak intensities on a log scale. The asterisks indicate experiments that
0 0 10 8 10
nucleosomes. For each SNAP experiment, bound proteins were identified and are shown in Extended Data Fig. 1b–d. The dagger symbols (†) indicate proteins
quantified using MS, and the forward (x axis) and reverse (y axis) SILAC ratios that are highlighted in Extended Data Fig. 1b–e.
(H/L ratio) were plotted on a logarithmic (log) graph. d, A library of modified
2
interactomes of major repressive and activating chromatin states change in the log[H/L ratio] for a particular protein (Fig. 2b). This way,
2
(Fig. 1d), including enhancer, promoter and different heterochromatin we were able to resolve the responses of chromatin readers to 15 dif-
states. A detailed list of modified histones, octamers and nucleosomes ferent modification features resulting from 82 pairs of nucleosomes
and corresponding quality controls is provided in the Supplementary (Fig. 2b, Extended Data Figs. 3b–d and 5a and Supplementary Table 3).
Information. The feature effect estimates enable us to quantitatively describe the
In total we performed SILAC-linked affinity purifications with 55 chromatin-binding behaviours of several hundred proteins and pro-
dinucleosomes. The forward and reverse experiments were generally vide a breakdown of complex binding profiles into a set of key features
very reproducible, and we achieved high detection coverage for most that either positively or negatively regulate their association with the
of the identified proteins. After correction for batch effects and impu- modified nucleosomes (Extended Data Fig. 2c,d). We have implemented
tation of missing values (Supplementary Information), we catalogued this decomposition of binding profiles into ‘chromatin feature motifs’
the responses of 1,915 proteins to the various modification states (Sup- in the MARCS online resource. Importantly, an integrative analysis of
plementary Table 1), covering a large part of the known chromatin public ENCODE30 ChIP followed by sequencing (ChIP–seq) datasets
proteome. Collectively, the SNAP experiments not only characterize covering a subset of identified nucleosome-interacting proteins and
protein binding to the nucleosomal modifications but also offer system- relevant chromatin features demonstrates that the binding behaviours
atic insights into the behaviour of chromatin readers through analysis observed in our in vitro dinucleosome system recapitulate the binding
of the changes in the H/L ratios across the entire dataset. behaviours found in cellular chromatin (Extended Data Fig. 4a–j and
Supplementary Table 4).
Notably, the number of proteins responding to each of the 15 fea-
MARCS maps chromatin-binding responses
tures is highly variable, with euchromatic features such as H3ac or
Comparing the log-transformed H/L ratios of individual proteins H4ac recruiting or excluding many more proteins than heterochro-
2
across SNAP experiments revealed characteristic nucleosome-binding matic ones such as H3K9me2/3 or H3K27me2/3 (Fig. 2c). However,
behaviours (Extended Data Fig. 1b–d). To facilitate the analysis and this might be biased by the extract preparation method, which pref-
exploration of many SNAP experiments (Extended Data Fig. 1e), we erentially releases euchromatic proteins. Furthermore, many proteins
implemented the interactive online visualization resource MARCS are regulated by more than one feature (Fig. 2d,e) indicating that they
(https://marcs.helmholtz-munich.de). either respond to multiple modifications independently or recognize
Figure 1d,e shows an exemplary set of heat maps generated using composite modification signatures. Clustering of individual protein
MARCS. The clustered heat map of all proteins is provided in Sup- binding behaviours revealed that they can be grouped into 40 major
plementary Table 2. Our data capture a broad range of responses by binding responses, largely defined by multisubunit protein com-
chromatin readers to repressive and activating modification states and plexes (Fig. 2e and Supplementary Table 5). For example, multiple
thereby reveal two principle modes of interaction: simple responses factors such as the INO80, MLL3/4, NuA4 or TFIID complexes show
to single modifications as exemplified by the recruitment of MECP2 highly specific responses to the different ‘promoter state’ features
or exclusion of KDM2B by DNA methylation (Fig. 1e); and complex H3K4me3, H3ac, H4ac and H2A.Z. Whereas binding of, for example,
binding patterns indicating binding to multiple modifications or syn- the INO80 remodeller28 is stimulated by H2A.Z in addition to H3 and
ergistic responses as illustrated by the origin recognition complex H4 acetylation (Extended Data Fig. 5a–c), the NuA4 histone acetyl-
(ORC) that shows recruitment to H3K9, H3K27 or H4K20 methyla- transferase complex responds similarly to H3 and H4 acetylation,
tions, with further stimulation by DNA methylation (ORC2 in Fig. 1e). but not H2A.Z (Fig. 2e). This complex regulation of INO80 by a H3ac/
Importantly, while these examples constitute internal controls by H4ac–H2A.Z axis was not directly apparent from the original SNAP data
consistently showing known and expected binding behaviours, our (Extended Data Fig. 5d), illustrating how the feature effect estimates
broad and unbiased profiling of chromatin states also enables the can be used to decode nucleosome-binding determinants across entire
identification of interactions with modified nucleosomes in new con- chromatin states.
texts. For example, we find that the INO80 chromatin remodelling
complex28 and polycomb repressive complex 1 (PRC1)29 are enriched
Absence of distinctive H3K4me1 readers
on nucleosomes displaying active modification signatures, includ-
ing acetylations of the histone H3 and H4 N-terminal tails (INO80B Another notable result from the feature effect analysis was the dif-
for INO80 in Fig. 1e; CBX4 and CBX8 for PRC1 in Fig. 1e and Extended ferential binding of proteins to H3K4 methylations (Fig. 3a). For the
Data Fig. 2a,b). promoter mark H3K4me3, we identified 45 strongly recruited pro-
teins (positive effect to log[H/L ratio] ≥ 1 at a false-discovery rate
2
(FDR) of 1%), including known H3K4me3 readers such as TFIID31 and
Unbiased prediction of binding features PHF832, and 31 strongly excluded proteins (Fig. 2b and Supplementary
Inspection of the heat maps further revealed that many proteins exhibit Table 3), such as polycomb repressive complex 2 (PRC2)33. By con-
broad nucleosome binding responses that cannot be explained by one trast, the enhancer mark H3K4me1 enriched only one protein, BRPF3
single feature, that is, a particular histone modification, DNA meth- (Extended Data Fig. 3c). Consistent with these findings, our integrative
ylation or the H2A.Z variant alone. To describe such complex binding ChIP–seq data analysis revealed no proteins showing strong associa-
behaviours, we deconvoluted the SNAP binding profiles into individual tion with H3K4me1, while many proteins preferentially localized to
nucleosomal features driving these associations. We achieved this by H3K4me3-marked genomic loci (Extended Data Fig. 4c,d). This was
comparing log[H/L ratio] values between related nucleosomes that further supported by a label-free quantitative ChIP–MS analysis of
2
differ by only one single feature. For example, four pairs of dinucle- H3K4me1- and H3K4me3-enriched mononucleosomes (Extended
osomes are informative of the effect of H3K4me3 on protein binding Data Fig. 6a–c). Although many proteins were significantly enriched
(Fig. 2a). A consistent increase or decrease in the log[H/L ratio] across in both H3K4me1 and H3K4me3 ChIPs compared with bulk nucleosome
2
these nucleosome pairs can be attributed only to H3K4me3, irrespec- purifications, the vast majority of these proteins preferentially associ-
tive of other modifications that the chromatin reader may recognize. ated with H3K4me3- but not H3K4me1-modified chromatin (Extended
Repeatedly sampling this effect across multiple nucleosome pairs, in Data Fig. 6d–h and Supplementary Table 6). This suggests the absence
addition to the H3K4me3 dinucleosome-purification experiment itself of a distinctive H3K4me1 interactome, supporting the notion that
(Extended Data Fig. 3a), enables statistical evaluation and calculation H3K4me1 is not a main driver of protein recruitment to enhancer
of a ‘feature effect estimate’ expressed as the H3K4me3-dependent chromatin states.
Nature | www.nature.com | 3
Article
d
400
300
200
100
0
Data Fig. 5d), underscoring that their native compositions remained
MARCS recovers protein interaction networks
intact during the affinity purifications. This prompted us to recon-
Closer analysis of binding profiles of protein complexes indicated that struct a network of proteins co-regulated by similar chromatin states
their subunits showed highly similar binding behaviours (for example, and use this to predict protein–protein interactions. To this end, we
the H2A.Z-responsive INO80, SRCAP and NSL complexes; Extended trained and tested several network inference algorithms (Extended
4 | Nature | www.nature.com
snietorp
fo
rebmuN
293
012
382
08
871
79
41
a b e
H3K4me3
H2A.Z
H3K4
H3K9 H3K14 H3K18 H3K23
H3K27
H4K5
H4K8
H4K12
H4K16
H4K20
meDNA
BRPF3
TAF4
ING5
EZH2
c Number of proteins
H2A.Z 11 (+36) 17 (+54)
DNA methylation 49 (+110) 42 (+67)
H3K4me1 3 (+30) 1 (+4)
H3K4me3 32 (+31) 45 (+31)
H3ac 1 (+178) 120 (+362) >>
H3K9acK14ac 0 (+134) 45 (+236) >>
H3K27ac 0 (+1) 9 (+3)
H3K9me2 0 (+1) 11 (+11)
H3K9me3 0 (+4) 22 (+37)
H3K27me2 0 (+0) 6 (+3)
H3K27me3 1 (+5) 22 (+18)
H4ac 2 (+33) 91 (+166) >>
H4K16ac 2 (+4) 1 (+12)
H4K20me2 10 (+119) 24 (+273) >>
H4K20me3 9 (+7) 1 (+0)
200 150 100 5 0 0 50 100 150 200
Excluded Strongly Weakly
FDR ≤ 0.01
FDR ≤ 0.01, abs(effect) ≥ 1.0
1 2 3 4 5 6 7 8 9 10
Number of chromatin features regulating protein response
54
16
2
52
1
91
4 3 2
EZH2 Effect estimate
PHF8 (1) (change in log2[H/L ratio]) C10orf12 SUZ12 BRPF1 7.5 PHF21A EED ING5 CHD6 SPIN1 MTF2 (1)
TAF4 UHRF1 AAARRRIIIDDD444AAA
BAZ2A TAF6
EPOP MEAF6 PHF13
5.0 BBBRRRPPPFFF333 CHD1
PHF8 (2)
KKKAAATTT777 (((111))) TAF9 TAF5
TTTAAAFFF111000 TAF12
TAF3
2.5
0
–4 –2 0 2 4
Estimated effect
(change in log[H/L ratio])
2
]
P[
gol–
jda
01
Excluded H3K4me3 Recruited
TAF8
TFIID
MOZ/MORF/HBO1 PRC2.1
Z.A2H
noitalyhtem
AND 1em4K3H 3em4K3H ca3H
ca41Kca9K3H
ca72K3H 2em9K3H 3em9K3H 2em72K3H 3em72K3H ca4H ca61K4H 2em02K4H 3em02K4H 5.1– 0.1– 5.0– 0 5.0 0.1 5.1
CHD4 cluster
(including NuRD complex)
IGHMBP2 cluster
(including RMI/BLM,
Fanconi anaemia complexes)
ORC1 cluster
(including ORC complex)
INO80B cluster
(including INO80 complex)
Experiment log 2 [H/L ratio] CDK9 cluster
NSD2 cluster
Reverse Forward –4–2 0 2 4 ( m in e c d lu ia d t i o n r g c i o nt m eg p r le a x to e r s ) and
Dimethylation Acetylation
Trimethylation
ASH2L cluster (including MLL1/2,
ncPRC1.1, MYC–MAX
complexes)
EPOP cluster (including PRC2.1 complex)
ZNF219 cluster
(including MLL3/4,
PR-DUB complexes)
ADNP cluster
(including ncPRC1.6 complex)
KANSL1 cluster
(including NSL complex)
PBRM1 cluster
(including BAF complexes)
Recruited Strongly Weakly
KAT5 cluster
(including NuA4 complex)
YEATS4 cluster (including SRCAP complex)
BARD1 cluster
(including BRCA1/A,
BRCC, SLF1/2 complexes)
SINHCAF cluster
(including EMSY complex)
ING1 cluster
(including SET1A/B,
SIN3A/B complexes)
TAF9 cluster (including TFIID complex)
SGF29 cluster
(including ATAC complex)
Fig. 2 | Feature effect estimates reveal binding responses of chromatin frequent co-occurrence, blocks of acetylation, such as H3K9acK14ac,
readers to different nucleosomal features. a, Nucleosomes informative of H3K9acK14acK18acK23acK27ac (H3ac) and H4K5acK8acK12acK16ac (H4ac)
protein responses to H3K4me3. The four pairs of dinucleosomes that differ were treated as single features. Proteins with statistically significant (limma,
only by H3K4me3, alongside the self-informative H3K4me3 dinucleosome FDR ≤ 0.01) effect estimates ≥ 1 classify as strongly recruited, or strongly
(top), and the binding responses of four representative proteins in the excluded if their estimate is ≤−1. Changes in log[H/L ratio] < 1 are considered
2
corresponding SNAP experiments (bottom) are shown. b, Feature effect to be weakly recruited or excluded. d, The number of chromatin features
estimates of proteins showing H3K4me3-dependent nucleosome binding. regulating protein binding responses. The grey bars tally the number of
The change in the log[H/L ratio] attributable to H3K4me3 (x axis) is plotted proteins with statistically significant feature effects (limma, FDR ≤ 0.01).
2
against the P value (limma, two-sided, Benjamini–Hochberg adjusted) on a − The black bars additionally tally proteins with strong feature effects (absolute
log scale (y axis). The vertical lines highlight an effect to fold change of 1, and effect ≥ 1). e, Clustered heat map of feature effect estimates of proteins
10
the horizontal line signifies the FDR threshold of 0.01. Selected protein strongly responding to at least one feature as shown in c. Individual estimates
complexes are highlighted. Duplicate protein identifiers, for example, PHF8 are colour coded. Entries without an estimate due to insufficient data are
(1), mark distinct UniProt IDs with the same gene name (Trembl versus marked in grey. Prototype proteins representing the binding response of each
SwissProt versions); for annotations, see Supplementary Table 1. c, The number cluster are shown on the right. Notable protein complexes are highlighted.
of interactors responsive to different chromatin features. Owing to their
3
2
1 0 –1 –2
–3
–3 0 3
Data Fig. 7a) against BioGRID34. In this analysis, the context-likelihood Within the resulting network (Supplementary Table 7), key chro-
of relatedness (CLR) algorithm35,36 performed best based on the high- matin regulatory complexes formed clusters (Extended Data Fig. 7e)
est area under the precision-recall curve (Extended Data Fig. 7b). that, at increased stringencies, resolved into separate complexes and
CLR also scored interactions reported by multiple publications high-confidence binary interactions (Extended Data Fig. 8). Impor-
and validated by co-crystal structures and co-purifications highest tantly, the normalized mutual information (MI) estimates between pairs
(Extended Data Fig. 7c,d), confirming the reliability of the predicted of proteins in our integrative ChIP–seq analysis increased in line with
network. increasing confidence of the predicted interactions (Extended Data
Nature | www.nature.com | 5
1em4K3H
fo tceffe detamitsE
Estimated effect of H3K4me3
H3K4me1 H3K4me3 H3K9acK14ac H3K27ac H2A.Z
b
NNNSSSLLL
NNNSSSLLL
SSSIIINNN333AAA///BBB NNNuuuRRRDDD EEEMMM SSS SSS IIINNN YYY 333AAA///BBB NNNuuuRRRDDD MMMeeedddiiiaaatttooorrrEEEMMMSSSYYY
MMMOOOZZZ///MMMOOORRRFFF IIInnnttteeegggrrraaatttooorrrTTTFFFIIIIIIDDD AAATTTAAACCC AAAPPPCCC///CCC MMMLLLLLL333///444 TTTFFFTTTCCC MMMLLLLLL333///444 SSSRRRCCCAAAPPP MMMLLLLLL111///222 MMMRRRNNN PPPRRRCCC222 MMMOOOZZZ///MMM HHH OOO BBB RRR OOO FFF 111 CCCHHHRRR PPP AAA RRR CCC CCC222 nnncccPPPRRRCCC111 IIINNN ...666 OOO888000 NNNuuuAAA444 PPPRRRCCC222 IIINNNOOO888000 XXXPPP nnn CCC cccPPPRRRCCC111...111
H4K20me2 H3ac H4ac H4K16ac DNA methylation
SSShhheeelllttteeerrriiinnn SSSLLLFFF111///222
SSSLLLFFF111///222 BBBRRRCCCAAA111---AAA
RRRNNNAAA PPPooolll IIIIII OOORRRCCC BBBRRRCCCAAA111---AAA RRNNAA PPooll IIII OOORRRCCC
MMMeeedddiiiaaatttooorrr TTTFFF NNN EEE TTT MMM uuu CCC AAA SSS 444 YYY AAATTTAAACCC MMMLLL RRR LLL MMM 111 III /// /// 222 BBBLLLMMM I m I m I m MMM nnnttt eee LLL eee ddd LLL ggg iii 333 aaa rrr /// aaa ttt III 444 ooo ttt NNN ooo rrr OOO rrr/// TTT 888 EEE FFF 000 MMM IIIIII NNN SSS DDD SSS III uuu YYY NNN AAA 333 444 AAA AAA /// TTT BBB AAACCC SSSRRR PPP NNN CCC RRR SSS MMM uuu AAA CCC EEE RRR PPP LLL 111 TTT DDD LLL 111 111 AAA ///222 ///BBB III I m I m I m NNN nnn OOO ttt eee eee ddd 888 ggg iii 000 aaa rrraaa tttooo tttooo rrr rrr NNN /// uuu TTT AAA FFF 444 IIIIIIDDD CCCHHH SSS RRR RRR AAA NNN PPP CCC CCC RRR uuu AAA RRR CCC PPP DDD 111 AAA MMM PPP RRR CCC NNN ///CCC NNNuuuAAA444 HHHBBB MMM OOO OOO 111 ZZZ///MMMOOORRRFFF MMMLLLLLL333///444 HHH AAA BBB SSS TTT NNN OOO RRR AAA uuu CCC CCC 111 RRR AAA DDD PPP RRRMMM nnnccc XXX III/// PPP F a F a F a BBB PPP MMM nnn aaa RRR CCC LLL aaa nnn LLL MMM CCC eee ccc LLL 111 mmm ooo 111 ... nnn 111 /// iiiaaa 222 iii
nnncccPPPRRRCCC111...666 nnncccPPPRRRCCC111...666 (((EEE///GGG///PPP)))BBBAAAFFF GGGBBBAAAFFF PPPRRRCCC222...111
H4K20me3 H3K9me2 H3K9me3 H3K27me2 H3K27me3
SSSLLLFFF111///222 OOORRRCCC OOORRRCCC
OOORRRCCC BBBRRRCCCAAA111---AAA OOORRRCCC OOORRRCCC
SSSIIINNN333AAA///BBB HHHUUUSSSHHH NNNuuuRRRDDD HHHUUUSSSHHH SSSIIINNN333AAA///BBB
RRRMMMIII///BBBLLLMMM AAAPPPCCC///CCC SIN3A/B
HHHBBBOOO111 HHHBBBOOO111
CCCHHHRRRAAACCC PPPRRRCCC222 IIINNNOOO888000 PPPRRRCCC111 PPPRRRCCC111
nnncccPPPRRRCCC111...666 PPPRRRCCC222 PPPRRRCCC222
≤–1.5 ≥+1.5
FABP FAB B/AFABE FABG *CATA *4/3LLM CATA 4/3LLM FRuN *DRuN AGAS DRuN FACP CTFT 4AuN *4AuN DIIFT PACRS FROM/ZOM *1CRP 1CRP rotargetnI *rotargetnI 08ONI rotaideM *08ONI CARHC
5
4
3 2
1
0
erutaef
nitamorhc fo tceffe naidem
detamitsE
6 Effect estimate Preference H3ac (±95% CI)
H4ac (±95% CI) H3ac H4ac
4 2 0
–2
−2 0 2 4 6
Estimated effect of H3ac
Estimated effect of modification feature
(change in log2[H/L ratio])
ca4H fo tceffe detamitsE
a c d
Recruited to BRD4 Preference H3K4me1 BRD2 BRD3
H3ac H4ac TFIID BRPFF3333 MOZ/MORF/HBO1
PRC2.1 CCCCH TA D F 6 3 P -5 HF8 PW P B C W B O A C R P Z L N 2 D E 1 T B A 3 9 1 N N S S D K D U D 2 3 C M H (1 1 B L ) B A 5 Z2 S A M S A M R A C B R A R C 2 D A 7 4 (1) BAZ2 M E A T Z A H 2 2 MMMMMMMMBBBBBBBBBDDDDD22222 TAF C 8 17o U rf B 4 C T 9 F HD1 BAZ1B B C IC H R R A AC1 T S F M P B A T C R L C 7 C C 1 A D R P I F D 2 1A C10 BB o AAAAAA r ZZZZZZ f1 111111 2 BBBPPPHHHHHHHHHFFFFFFFFF22211111 MMMMM AAA TTAA11 CHD H 2 MGXB4 S S M M A A R R C C D B 1 1 PHF1 A 0 RI P D B 2 RM1
SMARCE1
Recruited to [E/P]BAF SMARCC2 (1) H3K4me3 GBAF
CHRAC
SSSIIINNN333AAA///BBB NNNuuuRRRDDD
AAATTTAAACCC SSSRRRCCCAAAPPP SSSRRRCCCAAAPPP PPPRRRCCC222
(((EEE///GGG///PPP)))BBBAAAFFF
Fig. 3 | Differential binding of proteins to H3K4 methylation and H3/H4 c, Comparison of proteins responding to H3 versus H4 acetylation. Changes in
acetylation states. a, Comparison of H3K4me3- versus H3K4me1-responsive the log[H/L ratio] attributable to H3ac or H4ac are plotted on the x and y axes,
2
proteins. H3K4me3- or H3K4me1-dependent changes in the log[H/L ratio] are respectively. Data representation as in a. Proteins are coloured by the difference
2
plotted on the x and y axes, respectively. Proteins with statistically significant between their H3ac and H4ac responses. BAF and CHRAC complex subunits
estimates (limma, two-sided, Benjamini–Hochberg-adjusted FDR ≤ 0.01) are are highlighted with coloured borders and labels. d, The preference of protein
circled with a grey border. The grey area marks ±0.2 radians away from the x = y complexes for H3 or H4 acetylation. Markers indicate the median effect of the
line. Selected protein complexes are highlighted. While H3K4me1 recruits only H3ac versus the H4ac feature across all complex subunits with protein
BRPF3 but no other interactors, it still excludes, for example, the PRC2 complex, response measurements (the number of measurements per complex/feature
albeit not as strongly as H3K4me3. b, CLR-predicted network overlayed with is shown in Supplementary Fig. 1). The error bars represent the empirical 95%
chromatin feature effects. The heat maps reveal the degree and specificity of confidence interval (CI) of this median effect estimated from 100,000 random
protein recruitment or exclusion by the different features. Protein complexes samples of subunit effects, accounting for their variance. The coloured bars
with statistically significant regulation (CAMERA, FDR ≤ 0.01, median highlight the difference between these median estimates for H3ac and H4ac.
effect ≥ 0.3; Supplementary Table 8) were annotated for each feature after Complexes are ordered from H3ac to H4ac preference. The asterisks denote
manual curation. A zoomable version is provided in the MARCS resource. estimates for exclusive complex subunits.
Article
a b
SV40 enhancer Unmodified H3 and H4 H3acK4me3/H4acK20me2/H2A.Z
or Scrambled (referred to as promoter PTMs)
promoter DNA
35 bp 35 bp 200 bp 200 bp
40 bp 40 bp 200 bp SV40 promoter
Variable SV40 Scrambled 200 bp scrambled DNA
45 bp linker length 45 bp enhancer DNA 50 bp
50 bp 200 bp 200 bp
50 bp 50 bp 1
SV40 Scrambled 1.1
promoter DNA 2
55 bp 55 bp 50 bp 200 bp 200 bp
H3K9me3 or H3K27me3 H3acK4me3/H4acK20me2/H2A.Z 3 1.2
1.3
c d
Cluster description 1: Recruited by the 200 bp linker 1.1: No sequence preference
1.2: Prefer 200 bp scrambled DNA
4 1.3: Prefer 200 bp SV40 promoter
2: Repelled by the promoter PTMs
3: Recruited by the promoter PTMs
4: Repelled by the 200 bp linker
(no sequence preference)
−10 0 10
e f g
BRD4 BRD3 BRD2 BRD7
INO80E Modification responsive UCHL5 Linker responsive NFRKB Modification and linker CTCF responsive PRDM10 Z T B F T A B P 4 4 4 Normalization controls SP3 Other
NR2F2 NEIL2 n = 163 Size: estimate imputed
GPATCH1 n = 75 Shape: out of bounds RAD18 n = 13 Recruited to
SV40 promoter linker
Fig. 7f), indicating that the CLR-predicted network correctly enriches modification responses (Fig. 3b). Among other regulations, these
in vivo chromatin interactions. We leverage the identified local protein data reveal differential binding of many factors to H3 and H4 acety-
interactions to implement similarity predictions in the MARCS resource lations, as different subnetworks show distinct binding responses
and augment these with a curated list of protein complexes (Supple- to H3K27ac, H4K16ac, and the combined H3K9acK14ac, H3ac and
mentary Table 8), incorporating information from other resources H4ac features, suggesting a finely orchestrated regulation of active
such as EpiFactors37 and the Complex Portal38. chromatin states by differential acetylation. Whereas, for example,
The CLR algorithm, being based on MI, treats mutually exclusive the CHRAC chromatin remodelling complex shows preferential bind-
interactions similarly to correlated ones. Overlaying the chromatin ing to H4ac, BAF (SWI/SNF) remodellers show a strong preference
feature effect estimates for each protein onto the network reveals how for H3ac (Fig. 3c,d), mainly driven by H3K9acK14ac (Fig. 3b). Fur-
their arrangement into tight subnetworks is driven by the chromatin thermore, while many proteins respond to multiple acetylations in
6 | Nature | www.nature.com
ot detiurceR sMTP
retomorp
11 7 11 9 5 WWTR1 TFAP4 C Z T B C T F B44 SP3 9
7 EME1 HMGB1 7 5 3 SUB1 S N P F 1 KB1 5 3 0 1 TE N A F D A 1 T5 3 –1 0 1 –1 GATA2 –1 0 1
–3 PRDM10
–3 ZBTB17 –3 –5 –5 n n = = 1 7 6 5 3 –5
–7 –7 n = 13 –7
]4H dna
3H defiidomnu/sMTP
retomorp[2gol
reknil retomorp 04VS
pb 002
]delbmarcs
pb 002/retomorp
04VS
pb 002[2gol
.lcun-id MTP retomorp
]4H dna
3H defiidomnu/sMTP
retomorp[2gol
reknil retomorp 04VS
pb 002
6 6
5 5 4 4 3 3
2 2
1 1
0 0
–1 –1
–2 –2
–3 –3
–4 –4
BRD4 BRD3 BRD2 INO80ETAF10 ARID2
UCHL5 BRD7 MCRS1 SMARCA4 PHF10
SUZ12
RAD18 n = 163 n = 75
n = 13
–7 –5 –3 –101 3 5 7 9 11 –7 –5 –3 –10 1 3 5 7 –7 –5 –3 –101 3 5 7 9 11
log2[promoter PTMs/unmodified H3 and H4] log2[200 bp SV40 promoter/200 bp scrambled] log2[p200 bp SV40 promoter/200 bp scrambled]
200 bp scrambled linker unmodified H3 and H4 di-nucl. promoter PTM di-nucl.
reknil
pb 53 ,]3H
defiidomnu/3em9K3H[2gol
–4 –3 –2 –1 0 1 2 3 4 5 6
log2[H3K9me3/unmodified H3], 50 bp linker log2[H3K27me3/unmodified H3], 50 bp linker
reknil
pb 53 ,]3H
defiidomnu/3em72K3H[2gol
50 bp
Linker Linker
H3K4me1K27ac
C17orf96 CBX1 CBX5 C17orf96 PHF1 RLF BMI1 CBX3 PHC3 PHC2
CHD4 CBX8
CDYL CBX2 ORC2
TOP3A
Core histones HIF1A
n = 15 JADE1 n = 28
n = 23 RMI2 n = 25
n = 1 MMS22L n = 10
–4 –3 –2 –1 0 1 2 3 4 5
log2[FC] versus unmodified H3 and H4, 50 bp linker
Fig. 4 | Nucleosomal modifications and linker DNA constitute orthogonal depicted: (1) log[FC] > 1 or log[FC] < −1 compared with unmodified
2 2
routes of protein engagement with chromatin. a, Schematic of dinucleosomes with 50 bp linker; (2) Benjamini–Hochberg-adjusted P ≤ 0.05.
dinucleosomes used in label-free MS-based pull-downs for evaluating the The x = y line indicates where binding responses to H3K9me3 dinucleosomes
effect of linker DNA length and sequence on protein binding to active (right) incorporating 35 bp and 50 bp linkers are identical. The grey area marks ±0.2
and repressive (left) chromatin states. b, Clustered heat map depicting protein radians away from the x = y line. Core histones (normalization controls) are
binding responses to dinucleosomes incorporating different combinations indicated in dark grey. The smaller datapoints indicate response estimates
of 200 bp scrambled DNA or SV40 promoter sequence-based linkers and based on single data points. The triangles indicate points outside the data axes.
promoter PTMs (H3K4me3K9acK14acK18acK23acK27ac in combination d, Comparison of H3K27me3-binding responses on dinucleosomes with 35 bp
with H4K5acK8acK12acK16acK20me2 and H2A.Z). Data are shown as the and 50 bp linkers. Data representation in d–g is as described in c. e, Comparison
log-transformed fold change (log[FC]) in the normalized protein abundances of protein binding responses to promoter PTMs on dinucleosomes with 200 bp
2 2
compared with unmodified dinucleosomes with a 50 bp linker. c, Comparison scrambled DNA and SV40-promoter-sequence-based linkers. f, Comparison of
of H3K9me3-binding responses on dinucleosomes with 35 bp and 50 bp sequence-specific protein binding responses to the SV40 promoter linker in
linkers. Proteins responding to H3K9me3, linker length or both were unmodified dinucleosomes (di-nucl.) and dinucleosomes decorated with
determined using limma statistics and are highlighted in red, blue or purple, promoter PTMs. g, Comparison of protein binding responses to SV40
respectively. Only binding responses fulfilling the following two criteria are promoter linker and promoter PTMs.
Similarly, incorporating a 200 bp long SV40 enhancer linker had no
prominent effect on H3K4me1 and H3K4me1K27ac enhancer state
readout (Extended Data Fig. 10a–c and Supplementary Table 9), and
transcription factor recognition of the SV40 enhancer sequence was
not affected by the H3 modifications (Extended Data Fig. 10d,e). Nucleo-
somal modifications and DNA linkers therefore appear to act largely
independently in recruiting proteins to chromatin. Notably, many
proteins, including multiple spliceosome subunits, showed dimin-
ished binding when increasing the linker length from 50 to 200 bp,
the H3 and H4 tails, only few factors respond to H3K27ac or H4K16ac regardless of the linker sequence or modification status of the adjacent
alone (Fig. 3b). This breakdown of the SNAP data into local interaction nucleosomes (Fig. 4b and Extended Data Figs. 9l,m,o and 10a,f–h),
networks of co-regulated proteins and their responses to specific underscoring the regulatory potential of nucleosome spacing on
chromatin features provides important insights into how chromatin chromatin engagement irrespective of the underlying modification
states are decoded by chromatin readers. landscape.
Modifications and linkers act independently Multivalent chromatin engagement by INO80
Apart from covalent modifications, characteristic features of chromatin Our combined analyses can be used to identify chromatin binding
states also include linker DNA length, typically ranging from 35–55 bp behaviours and nuclear regulators with unknown functions. As a proof
in most chromatin domains39 to over 200 bp in nucleosome-depleted of principle, we selected INO80, an ATP-dependent nucleosome remod-
regions (NDRs). To investigate the effects of linker DNA on chromatin eller and exchange factor for the histone variant H2A.Z that is involved
recognition by nuclear proteins, we performed an additional set of in transcription, replication and DNA repair28, for which several inter-
affinity purifications using dinucleosomes incorporating different esting observations emerged from our data (Extended Data Fig. 5d).
DNA linkers (Fig. 4a and Supplementary Information). Notably, the First, our high-confidence CLR network predicted an interaction with
binding of heterochromatin as well as active promoter modification transforming growth factor beta regulator 1 (TBRG1), a putative tumour
readers was generally not affected by variations in linker length nor suppressor and p53 activator40 (Fig. 5a and Extended Data Fig. 8). Con-
linker sequence (Fig. 4b–e, Extended Data Fig. 9a–g and Supplementary sequently, we were able to co-purify TBRG1 together with INO80 in
Table 9), highlighting the robustness of the protein binding responses co-immunoprecipitation (co-IP) experiments from INO80B-V5 knock-in
captured in MARCS. Likewise, the binding of sequence-specific tran- cell lines (Fig. 5b and Extended Data Fig. 5e–h). Label-free MS-based
scription factors recognizing DNA motifs in the 200 bp long SV40 estimation of the TBRG1:INO80B ratio indicated that TBRG1 is present
promoter linker was insensitive to the active promoter modifications in the complex at substoichiometric levels comparable to the regula-
on the adjacent nucleosomes (Fig. 4f,g and Extended Data Fig. 9d,g). tory subunits MCRS1, INO80D and YY1 (Fig. 5c).
Nature | www.nature.com | 7
]jdaP[01gol–
High-confidence predictions: NFRKB
Prediction INO80 in BioGRID INO80C complex
Prediction not # ACTR5
in BioGRID ## INO80D YY1
Missed prediction ###UCLH5
PCCCP ThDN IIII IA R2DEFNNN 6 NNNN e N RC o OOOO BBB 1 KO B C B P0 l DOOO EEEEP OOOO O olCG , XXX RRRR oC S L L N P T EPZZR XPPP m 8888 2 8 1248 e F CCCC 4 R 11 DHHO A2 C 225 r MBBIM 0000 7 0 ne 2 Z , N i 0 123 1 5 N 1 N 6 b 12 BCD A P2 RR zr (( 6 M EOG S T a 12B PPRR o y N H . , I OO , PPA 1 P B s S )) Z U I P m U M N L s Y Y HH 5 T P IN 2 O N 7 P S FF N RR eY F 7 Z o / U R F H 8 P N YCF 2 CC , F e T 2 M13 O P S 6 A G CC m N P , G R Z T 1 7 F2 D H F 23 5 R R 8 O 2 45 F 1 T 1 1 A 1 a K 2 1 8 L 8 0 P 9 6 6 29 l R , B 5 E ( , 8(1 s H 1 8 1 F 3u 7 ) , ) 4b U 1,u0 2 U L X 3 X n N A A R 5 R i R 2 A t, F A W AC T C 1 1 1 F a 1 C C D S -n 2 0 5 1 6 1 d M R 4 HBII NN C S 3, A UR EW R K BGG 6 E M R PS H KMT ADK P N PO AAAFF I B 45 T A C Z 1P BCCDEP S A AA M R F O TTTOO B 1 M A PB X TT 3 F A R p R 3 CD FFF DD 1 ( T P T ICSS 1 Z 21 6A 6 P T l S4 237 P C AX2C F i 2 BKLLLL M M 1T ) L A4 c U F SA R R A M FB2 IIII S D ( A 5 H - 2 e NNNN E Y K 2 JJJJ ( D A M F 1 B M 3 B B T P2L 1 o 3 A R ) A UUUD B3559 ( 9 BF 2 7 C 1 B B ) 2s Y F A 724F L PNNN B 2 ) o L P P F (B6 P 2 1 2 m BD PPPPSS A 7 4 - 3 ) RRRRFA M F e H A R 3 1 RPPPP R C u I R A P TFFFF F P ( v E2 1 N S 13446 1 B S B) B A1 T 6 P 1 N K SSSSSS B D Z D S FFFNNN CE B S 3 D M 33 C RRW RL PW PB NG RR T N AB 3 G A E NN 1 H E H1 B 2 PP 3 C u D 1 A A B F B AF ( L PP P F T 1 R1 SS R ET R 1 O P P A 245 ) 7AD 45 B MM P 11 00 B B S ( A 2 X 1 8 P M C 0 CC L N C ) A H Z B 1 ZG CC 1 RSRPES B A R U C N E X BRTR IR CC NB A N pC X ( F I S 3 2 1 3F F MLM l RM 5 12 NP4I ( i H F ) H N 2 c 2 1 M AMS II 6 8e 8) 1 1/ 13 F B 1 F Ao 0 2 4 D D T O ( O L s D 1 A SSSSS D ( D o M 1 X X / S F RRRRR B 2m ) BK K A O )SSSSR 2 12 e 1 A ERRE FFFFT RM H H P IxNB 1356 F P o P A 2 A MP4 P n CC 4 H D D A RPS S AA RRR H 8 DD j O H H 3 NNA 1 SC uA PPP L CC RB A S n P AAA ANPI N N c R21 S F P 1 12 PSH 1 t 1 36S X 8 L R F 8 S /1 i N o P (A F RX F ( R 1 1 n R S 2 P5P C BAB ) B P R / N A2 1 B 3 RAA 9 F P) 4 P RBR C C R H M A M C Z AADAI F N0 L ES W XM CE 11F R DC A- D2 31 F N A 1 S A 6 1 7 P 1 N 9 DH L E 3 R UBB R PU L 2 0 N L MM F RRI A F RN M A ( C R1 C CC EE D D V C ) C N 4 DD 5 ACAL M5 1 P 1 C 22 1R3 0T (BBAAB 1 L 91 E A K H R2 RRRCC/ U C D T A GIIDLLDD H TO M 2 /777 L P12 R A P BC 6 8 A) F A B D T 1 D M APPSSS I O D N S F L HMMMB X O M PL RF 4 AAA 3I 1 1 T N MRRR / A 0 1Y 4D CCC1 N T( O AAC 1 P H K ) C 42K A 1 D R S P X ( F D 1 PI P N SS P [ ) 1 H 1IRR A 1 N 2 - SSSS F RS 2 31 MMMM 8 ]FM H 1 AAAA R (H2N 11 RRRR C R )NR CCCCT O R RN R CDDE E RNP N1 B 122 1 AP C 1P B ( (U 1 1B 1 H / ) 8 H 2 P F ) T T 8 N F F R ( A 1 N EEG (N2 P F )O MM A A P) 2 T P UD D SSA 1 YY T D J 6 FA T 1 A F ZP A B F2 P 1 R A 2 RHD C ( PI1 8G H F ) (D22 DT1) ABA CL31XR M 1 C N H is C R s A O e C R d 1 1 PpPHBA rrri e gee Z1 dddhA i -iiccccSS tttoNN iiiooo Rn R nnn PP fiD B din 3neo SnBt N ciiR noeP G B EpRiroeI M DGdA RE MMMMT RE MMMMT AAA CC iR Tc RR PPDD PP FFF MM 11 R BOOBOORR HH XX tI 4 R 4 RB 222 B HH 77 88 RR CC BB 3 TTGG D SS RRRR i PP NN 00 MM o AA o o RR AA FF DD (( CC PP (( LL FFFF C BB C 00 11 RRR 11 rr PP 11 DDDDD DDD SSS n 11 11 fffTTT NN 44 N 4444 )) PPP ))) NNN 444 ((( 444 333 LL FF 22 LLLL 11 TTTT s TTTTTTTTTTTTTTTT TT 99 PP 33 AA 33 1212 )) AAAAAAAA 11 : (( HH 11 AA FFFFFFFFFF )) 99 11 66459459BB TB T R F G P 1 T ### IN # O80E ## INO IN 8 O 0 80B
4 RUVBL2
RUVBL1
NFRKB INO80C
3 UCHL5 ACTR8
INO80E
2 INO80B
TBRG1
1 ACTR5
0
–9 –6 –3 0 3 69
log2[FC of INO80B IP versus control)
Dinucleosome pull-down
Unmod. H3 + +
+ +
+ ++ + +
+ + + +
INO80B - 55
ACTR5 - 70 - 55
- 15
%8–1
,tupnI sdaeB
kDa
ACTR5–GFP (INO80) ChIP–MS
Effect (change in log2[H/L ratio]) log2[ChIP versus input], replicate 1
2
etacilper
,]tupni
susrev
PIhC[2gol
a
b c
d Driver chromatin features for INO80 e
Unmod. H4
H3ac H4ac
H2A.Z
TBRG1
Histones,
streptavidin
f
4 H4K5K8K12K16-4ac
H3K9acK14ac
H3K4me3
2 H3K27acK36me2
H3K18acK23ac
H4K5K8K12K16-3ac
H3K4me2
0 H2AZ FC > 1.5
H2B
–1.0–0.5 0 0.5 1.0 1.5 2.0 0 2 4
1LBVUR 2LBVUR E08ONI 5LHCU C08ONI BKRFN 5RTCA B08ONI A6LTCA TPFT 8RTCA 08ONI 1YY D08ONI 1SRCM 1GRBT
4
3
2
1
0
)B08ONI
ot
evitaler(
yrtemoihciotS
Fig. 5 | The INO80 complex recognizes a multivalent nucleosome-
modification signature. a, CLR-predicted TBRG1–INO80 interaction.
TBRG1–INO80 interactions were reported in several screens48–50 and deposited
at BioGRID but never validated. b, TBRG1 interacts with INO80. Volcano plot
of proteins that are significantly enriched (t-test, two-sided, Benjamini– Hochberg-adjusted FDR ≤ 0.05) in n = 3 biologically independent INO80B-V5 immunoprecipitations (Extended Data Fig. 5h) followed by label-free MS. c, Composition of the INO80 complex. The relative stoichiometries between TBRG1 and INO80 were calculated using quantitative MS data from the INO80B-V5 immunoprecipitation experiments shown in b. n = 3. Data are the
mean ± s.d. of the stoichiometry values. d, Features driving the INO80
nucleosome-binding response. Individual effect estimates (change in log[H/L 2 Core INO80 subunits ratio]) for INO80-exclusive subunits are shown as dots (estimate significantly
Regulatory INO80 subunits
non-zero, limma, two-sided, Benjamini–Hochberg-adjusted FDR ≤ 0.01) or
crosses (estimate not statistically significant). The bars highlight the median
effect across all complex subunits with protein response measurements (n = 11, Bait
except for DNA methylation, H3K27ac, H3K9me2 and H3K27me2, for which
n = 1 and no estimate was derived). The error bars represent the empirical 95%
CI of this median effect estimated from 100,000 random samples of subunit
effects, accounting for their variance. The bold font indicates features with
enrichments greater than expected by chance (CAMERA, Benjamini–Hochberg-
adjusted FDR ≤ 0.01; Supplementary Table 8). e, Targeted dinucleosome pull-
downs confirm INO80 binding to nucleosomes containing hyperacetylated H3
(H3ac), H4 (H4ac) and/or H2A.Z. Binding was detected by immunoblotting
against INO80B and ACTR5. TBRG1 follows the INO80-binding pattern.
H2A.Z
The HeLa S3 cell nuclear extract used was a mixture of three independent meDNA
preparations. Different amounts of the mixed extract were loaded as inputs for
H3K4me1 the different immunoblots. Experiments were independently repeated three
H3K4me3 times with similar results. Unmod., unmodified. f, Quantitative label-free
H3ac LC–MS-based analysis of histone modifications and H2A.Z in mononucleosomes
H3K9acK14ac co-purified with ACTR5 from MNase-digested HeLa cell chromatin. The relative
H3K27ac PTM or H2A.Z abundance over input chromatin is plotted as the log[FC] for
2
n = 2 independent biological experiments.
H3K9me2
H3K9me3
H3K27me2
H3K27me3
H4ac
H4K16ac
H4K20me2 H2A
H4K20me3
Article
Second, while the INO80 complex was unresponsive to variations presence of ATP, nucleosomal modifications can potentially modulate
in the linker DNA (Fig. 4e–g and Extended Data Fig. 9c,d,f,g), our fea- chromatin remodelling activities that could in turn expose nucleoso-
ture effect estimates predicted binding to a multivalent nucleosomal mal DNA sequences, therefore facilitating, for example, the binding of
modification signature consisting of acetylations in the H3 and H4 pioneer transcription factors42 thereby enabling the establishment or
N-terminal tails and the histone variant H2A.Z (Fig. 5d and Extended maintenance of NDRs.
Data Fig. 5b,c). Confirming our prediction, we found in targeted Notably, modifications that are characteristic of distinct chromatin
pull-downs (Fig. 5e) that H3ac had a small positive effect on INO80 states vary greatly in their regulatory potential, as promoter-associated
recruitment, which was more pronounced in the case of H4ac. Notably, H3K4me3 and hyperacetylated H3 and H4 tails affect the binding
while no effect of H2A.Z alone was detectable by western blotting, the of many nuclear factors, while enhancer-associated H3K4me1 and
presence of H2A.Z greatly enhanced INO80 binding when combined H3K27ac appear largely inert in targeting proteins to chromatin. Con-
with H4ac, and to a lesser extent with H3ac (Fig. 5e). Consistent with sistent with previous findings43,44, this suggests that modifications
the in vitro results, mononucleosomes co-purified with INO80 from found at enhancers may act, for example, by preventing the binding
micrococcal nuclease (MNase)-digested HeLa chromatin through of repressive factors to the underlying regulatory loci45, rather than by
the subunit ACTR5 were enriched in H4ac and H3ac as well as H2A.Z directly recruiting proteins.
(Fig. 5f and Extended Data Fig. 5i–k). These results confirm that the Our study unifies two complementary views of chromatin—the
INO80 remodelling complex indeed binds to nucleosomes decorated modification-centric view that defines chromatin states based on chro-
by the predicted multivalent chromatin modification signature in matin marks1,2, and the protein-centric view that defines the chromatin
human cells and suggest a role of histone acetylation and H2A.Z in states by their protein constituents46. By combining both aspects, our
stimulating INO80 recruitment to specific genomic loci (Extended experiments reveal major principles of how complex modification
Data Fig. 5l). patterns define and regulate functional chromatin states. Our data
These independent experimental validations highlight the reliability are easily accessible through the interactive online resource MARCS
of our analyses and predictions, and underscore the value of our data (https://marcs.helmholtz-munich.de) with the aim to serve as a plat-
to identify previously undescribed protein interactions and complex form for both hypothesis generation and validation, and thereby act
binding events involving the concerted interplay between multiple as a catalyst for future chromatin research. We encourage research-
chromatin modification features. ers to thoroughly explore the data as there are many discoveries to
be made.
Discussion
Online content
Here we have combined large-scale quantitative nucleosome affin-
ity purification approaches and computational analysis methods to Any methods, additional references, Nature Portfolio reporting summa-
understand how chromatin states are read and interpreted by nuclear ries, source data, extended data, supplementary information, acknowl-
machineries. Our approach has enabled us to delineate direct effects edgements, peer review information; details of author contributions
of composite modification signatures of promoter, enhancer and and competing interests; and statements of data and code availability
heterochromatin states on chromatin engagement by several hun- are available at https://doi.org/10.1038/s41586-024-07141-5.
dred chromatin readers and to uncover interconnected networks of
nuclear proteins targeting similar chromatin states. Deconvoluting 1. Kundaje, A. et al. Integrative analysis of 111 reference human epigenomes. Nature 518,
the responses of chromatin factors to 15 different modification fea- 317–330 (2015).
2. Ernst, J. & Kellis, M. Discovery and characterization of chromatin states for systematic
tures unravels how complex modification signatures are sensed by
annotation of the human genome. Nat. Biotechnol. 28, 817–825 (2010).
chromatin-binding proteins. Combining these responses to individual 3. Musselman, C. A., Lalonde, M.-E., Côté, J. & Kutateladze, T. G. Perceiving the epigenetic
modification features into modification response profiles, akin to landscape through histone readers. Nat. Struct. Mol. Biol. 19, 1218–1227 (2012).
4. Bannister, A. J. & Kouzarides, T. Regulation of chromatin by histone modifications. Cell
DNA-binding-motif logos of transcription factors41, enables the com- Res. 21, 381–395 (2011).
prehensive prediction of chromatin regulators that recognize complex 5. Greenberg, M. V. C. & Bourc’his, D. The diverse roles of DNA methylation in mammalian
modification patterns. Similarly, it enables the systematic identification development and disease. Nat. Rev. Mol. Cell Biol. 20, 590–607 (2019).
6. Millán-Zambrano, G., Burton, A., Bannister, A. J. & Schneider, R. Histone post-translational
of nucleosomal features modulating the binding of various nuclear modifications—cause and consequence of genome function. Nat. Rev. Genet. 23, 563–580
proteins to their genomic target loci. Predicted responses to multiple (2022).
features point towards a synergistic interplay between the components, 7. Garcia, B. A., Pesavento, J. J., Mizzen, C. A. & Kelleher, N. L. Pervasive combinatorial
modification of histone H3 in human cells. Nat. Methods 4, 487–489 (2007).
as we show for the INO80 remodeller (Fig. 5e,f). 8. Pesavento, J. J., Bullock, C. R., LeDuc, R. D., Mizzen, C. A. & Kelleher, N. L. Combinatorial
While an interplay between distinct nucleosomal modifications is modification of human histone H4 quantitated by two-dimensional liquid chromatography
clearly visible for many proteins, it generally seems not to involve linker coupled with top down mass spectrometry. J. Biol. Chem. 283, 14927–14937 (2008).
9. Voigt, P. et al. Asymmetrically modified nucleosomes. Cell 151, 181–193 (2012).
DNA as we observe no apparent synergy even between active modifi- 10. Young, N. L. et al. High throughput characterization of combinatorial histone codes. Mol.
cations and NDRs often coupled in vivo. However, this might reflect Cell Proteom. 8, 2266–2284 (2009).
11. Tvardovskiy, A., Schwämmle, V., Kempf, S. J., Rogowska-Wrzesinska, A. & Jensen, O. N.
the static nature of the interactions in our pull-downs, in which the
Accumulation of histone variant H3.3 with age is associated with profound changes in the
absence of ATP and the presence of HDAC inhibitors prevent enzymatic histone methylation landscape. Nucleic Acids Res. 45, 9272–9289 (2017).
activities that are known to be involved in highly dynamic regulatory 12. Shema, E. et al. Single-molecule decoding of combinatorially modified nucleosomes.
Science 352, 717–721 (2016).
circuits, such as nucleosome remodelling and rapid histone acetyla-
13. Liu, C. L. et al. Single-nucleosome mapping of histone modifications in S. cerevisiae.
tion turnover. In the case of multistep enzymatic processes, such as PLoS Biol. 3, e328 (2005).
chromatin remodelling by INO80, the reported interactions might 14. Rando, O. J. Combinatorial complexity in chromatin structure and function: revisiting the
histone code. Curr. Opin. Genet. Dev. 22, 148–155 (2012).
therefore reflect particular intermediate states of a dynamic reaction
15. Ruthenburg, A. J., Li, H., Patel, D. J. & Allis, C. D. Multivalent engagement of chromatin
cycle, probably representing one of the first engagement steps of the modifications by linked binding modules. Nat. Rev. Mol. Cell Biol. 8, 983–994 (2007).
complex with chromatin. Likewise, although we saw no prominent 16. Li, B. et al. Combined action of PHD and chromo domains directs the Rpd3S HDAC to
transcribed chromatin. Science 316, 1050–1054 (2007).
effects of different linkers on protein binding to modifications and vice
17. Tsai, W.-W. et al. TRIM24 links a non-canonical histone signature to breast cancer. Nature
versa, a dynamic interplay between the two cannot be excluded. The 468, 927–932 (2010).
testable transcription-factor-binding sites in the linkers were located 18. Eustermann, S. et al. Combinatorial readout of histone H3 modifications specifies
localization of ATRX to heterochromatin. Nat. Struct. Mol. Biol. 18, 777–782 (2011).
distant from the nucleosome-bound DNA regions, and histone modi-
19. Ruthenburg, A. J. et al. Recognition of a mononucleosomal histone modification pattern
fications were unlikely to directly modulate their accessibility. In the by BPTF via multivalent interactions. Cell 145, 692–706 (2011).
8 | Nature | www.nature.com
20. Su, W.-P. et al. Combined interactions of plant homeodomain and chromodomain 39. Voong, L. N. et al. Insights into nucleosome organization in mouse embryonic stem cells
regulate NuA4 activity at DNA double-strand breaks. Genetics 202, 77–92 (2016). through chemical mapping. Cell 167, 1555–1570 (2016).
21. Borgel, J. et al. KDM2A integrates DNA and histone modification signals through a CXXC/ 40. Tompkins, V. S. et al. A novel nuclear interactor of ARF and MDM2 (NIAM) that maintains
PHD module and direct interaction with HP1. Nucleic Acids Res. 45, gkw979 (2016). chromosomal stability. J. Biol. Chem. 282, 1322–1333 (2006).
22. Jurkowska, R. Z. et al. H3K14ac is linked to methylation of H3K9 by the triple Tudor 41. Schneider, T. D. & Stephens, R. M. Sequence logos: a new way to display consensus
domain of SETDB1. Nat. Commun. 8, 2057 (2017). sequences. Nucleic Acids Res. 18, 6097–6100 (1990).
23. Bartke, T. & Groth, A. A chromatin-based signalling mechanism directs the switch from 42. Sinha, K. K., Bilokapic, S., Du, Y., Malik, D. & Halic, M. Histone modifications regulate pioneer
mutagenic to error-free repair of DNA double strand breaks. Mol. Cell. Oncol. 6, 1605820 transcription factor cooperativity. Nature https://doi.org/10.1038/s41586-023-06112-6
(2019). (2023).
24. Xie, S. & Qian, C. The growing complexity of UHRF1-mediated maintenance DNA 43. Sankar, A. et al. Histone editing elucidates the functional roles of H3K27 methylation and
methylation. Genes 9, 600 (2018). acetylation in mammals. Nat. Genet. 54, 754–760 (2022).
25. Bartke, T. et al. Nucleosome-interacting proteins regulated by DNA and histone 44. Zhang, T., Zhang, Z., Dong, Q., Xiong, J. & Zhu, B. Histone H3K27 acetylation is dispensable
methylation. Cell 143, 470–484 (2010). for enhancer activity in mouse embryonic stem cells. Genome Biol. 21, 45 (2020).
26. Sidoli, S. et al. Middle-down hybrid chromatography/tandem mass spectrometry 45. Bleckwehl, T. et al. Enhancer-associated H3K4 methylation safeguards in vitro germline
workflow for characterization of combinatorial post-translational modifications in competence. Nat. Commun. 12, 5771 (2021).
histones. Proteomics 14, 2200–2211 (2014). 46. Filion, G. J. et al. Systematic protein location mapping reveals five principal chromatin
27. Muir, T. W. Semisynthesis of proteins by expressed protein ligation. Annu. Rev. Biochem. types in Drosophila cells. Cell 143, 212–224 (2010).
72, 249–289 (2003). 47. Lowary, P. T. & Widom, J. New DNA sequence rules for high affinity binding to histone
28. Poli, J., Gasser, S. M. & Papamichos-Chronakis, M. The INO80 remodeller in transcription, octamer and sequence-directed nucleosome positioning. J. Mol. Biol. 276, 19–42 (1998).
replication and repair. Philos. Trans. R. Soc. B 372, 20160290 (2017). 48. Hein, M. Y. et al. A human interactome in three quantitative dimensions organized by
29. Geng, Z. & Gao, Z. Mammalian PRC1 complexes: compositional complexity and diverse stoichiometries and abundances. Cell 163, 712–723 (2015).
molecular mechanisms. Int. J. Mol. Sci. 21, 8594 (2020). 49. Pardo, M. et al. Myst2/Kat7 histone acetyltransferase interaction proteomics reveals
30. Dunham, I. et al. An integrated encyclopedia of DNA elements in the human genome. tumour-suppressor Niam as a novel binding partner in embryonic stem cells. Sci. Rep. 7,
Nature 489, 57–74 (2012). 8157 (2017).
31. Vermeulen, M. et al. Selective anchoring of TFIID to nucleosomes by trimethylation of 50. Rolland, T. et al. A proteome-scale map of the human interactome network. Cell 159,
histone H3 lysine 4. Cell 131, 58–69 (2007). 1212–1226 (2014).
32. Kleine-Kohlbrecher, D. et al. A functional link between the histone demethylase PHF8
and the transcription factor ZNF711 in X-linked mental retardation. Mol. Cell 38, 165–178 Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
(2010). published maps and institutional affiliations.
33. Schmitges, F. W. et al. Histone methylation by PRC2 is inhibited by active chromatin marks.
Mol. Cell 42, 330–341 (2011). Open Access This article is licensed under a Creative Commons Attribution
34. Oughtred, R. et al. The BioGRID interaction database: 2019 update. Nucleic Acids Res. 47, 4.0 International License, which permits use, sharing, adaptation, distribution
D529–D541 (2018). and reproduction in any medium or format, as long as you give appropriate
35. Faith, J. J. et al. Large-scale mapping and validation of Escherichia coli transcriptional credit to the original author(s) and the source, provide a link to the Creative Commons licence,
regulation from a compendium of expression profiles. PLoS Biol. 5, e8 (2007). and indicate if changes were made. The images or other third party material in this article are
36. Meyer, P. E., Lafitte, F. & Bontempi, G. minet: a R/Bioconductor package for inferring included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
large transcriptional networks using mutual information. BMC Bioinformatics 9, 461 to the material. If material is not included in the article’s Creative Commons licence and your
(2008). intended use is not permitted by statutory regulation or exceeds the permitted use, you will
37. Medvedeva, Y. A. et al. EpiFactors: a comprehensive database of human epigenetic need to obtain permission directly from the copyright holder. To view a copy of this licence,
factors and complexes. Database 2015, bav067 (2015). visit http://creativecommons.org/licenses/by/4.0/.
38. Meldal, B. H. M. et al. The complex portal—an encyclopaedia of macromolecular
complexes. Nucleic Acids Res. 43, D479–D484 (2014). © The Author(s) 2024
Nature | www.nature.com | 9
Article
Methods Nucleosome assembly. Histone octamers were refolded from the puri-
fied histones and assembled into nucleosomes with biotinylated DNA
Experimental procedures through salt deposition dialysis as previously described25,51. Biotinylated
Preparation of recombinant canonical histones. Recombinant nucleosomal DNAs containing either one (mononucleosomes) or two
human canonical histone proteins were expressed in Escherichia coli 601 nucleosome-positioning sequences47 separated by a 50-base-pair
BL21(DE3)-CodonPlus-RIL cells (Agilent Technologies) from pET21b(+) (bp) linker (dinucleosomes), or four 601 nucleosome-positioning seq-
(Novagen) vectors and purified by denaturing gel filtration and uences (tetranucleosomes), were prepared as described previously25.
ion-exchange chromatography as previously described25,51. CpG-methylated DNA was prepared using the M.SssI methyltrans-
ferase and complete methylation was confirmed by restriction digest
Preparation of recombinant histone H2A.Z. A codon-optimized (Supplementary Information). Dinucleosomes and tetranucleosomes
sequence encoding human H2A.Z (H2AFZ, UniProtKB: P0C0S5) was were assembled in the presence of mouse mammary tumour virus A
purchased from GenScript and cloned into the NdeI/XhoI sites of (MMTVA) competitor DNA (prepared in the same way as 601 DNA)
the pET24a(+) vector (Novagen). H2A.Z was then expressed in E. coli and a slight excess of octamers as described for longer chromatin
BL21(DE3)-CodonPlus-RIL cells (Agilent Technologies) and purified as arrays to ensure saturation of the 601 repeats53. The reconstituted
previously described for canonical H2A25. nucleosomes were then immobilized on streptavidin Sepharose High
Performance beads (Cytiva) through the biotinylated DNA, washed to
Preparation of truncated histones for native chemical ligations. remove MMTVA competitor DNA and MMTVA nucleosomes (in the case
Truncated human H3Δ1–31T32C protein for ligations of modified of dinucleosomes and tetranucleosomes), and directly used for SILAC
histone H3 was expressed in E. coli BL21(DE3)-CodonPlus-RIL cells or label-free nucleosome affinity purifications. Correct assembly and
(Agilent Technologies) and purified as previously described52. Trun- immobilization of nucleosomes was verified by native polyacrylamide
cated human H4Δ1–28I29C protein for ligations of modified his- gel electrophoresis (Supplementary Information). Nucleosomes for
tone H4 was expressed from pET24b(+) vectors (Novagen) in E. coli pull-downs in which only modifications on histone H3 were tested
BL21(DE3)-CodonPlus-RIL cells (Agilent Technologies). The insoluble were assembled with octamers containing recombinant histone H4
protein was extracted from inclusion bodies with unfolding buffer purified from E. coli instead of ligated H4. Likewise, nucleosomes for
(20 mM Tris (pH 7.5), 7 M guanidine hydrochloride, and 100 mM pull-downs in which only modifications on histone H4 were tested con-
dithiothreitol (DTT)) for 1 h at room temperature, and the cleared tained recombinant H3 and not ligated histone H3. Matched unmodi-
supernatant was loaded onto a Sephacryl S-200 gel filtration column fied control nucleosomes were assembled with unmodified ligated H3
(Cytiva) in SAU-1000 buffer (20 mM sodium acetate (pH 5.2), 7 M urea, and recombinant H4, or recombinant H3 and unmodified ligated H4
1 M NaCl, and 1 mM ethylenediaminetetraacetic acid (EDTA)) without accordingly. Nucleosomes containing only CpG methylation (H27M)
any reducing agents. Positive fractions were combined and further were assembled with ligated unmodified H3 and recombinant H4, and
purified by reversed-phase chromatography. Truncated H3Δ1–31T32C nucleosomes containing only H2A.Z (H36) and no other modifications
was purified over a Resource RPC column (Cytiva) using a gradient of were assembled with recombinant (and therefore unmodified) H3 and
0–65% B (buffer A: 0.1% trifluoroacetic acid in water; B: 90% acetoni- H4 produced in E. coli.
trile, 0.1% trifluoroacetic acid) over 20 column volumes. Truncated
H4Δ1–28I29C was purified over a PerkinElmer Aquapore RP-300 (C8) Generation of 601 dinucleosomes incorporating different linker
column (250 mm × 4.6 mm inner diameter) using a gradient of 0–65% DNAs. Plasmid constructs for the preparation of biotinylated 601 dinu-
B (buffer A: 0.1% trifluoroacetic acid in water; B: 90% acetonitrile, 0.1% cleosome DNAs containing different linker lengths (35 bp, 40 bp, 45 bp,
trifluoroacetic acid) over 20 column volumes. The fractions contain- 50 bp and 55 bp linkers) between the two 601 nucleosome-positioning
ing pure H3Δ1–31T32C or H4Δ1–28I29C were pooled and lyophilized. sequences were generated by annealing forward and reverse primers
of corresponding length and ligating them into pUC19-di601_NcoI/
Preparation of modified histone H3 and histone H4 by native chemi- NheI_5xGal4 (pTB891, gene synthesis by Genscript) digested with
cal ligation. For the preparation of modified histone H3, N-terminal NcoI and NheI restriction enzymes (Thermo Fisher Scientific), thereby
H3 peptides (amino acids 1–31) were ligated to truncated H3Δ1–31T32C exchanging the ‘5×Gal4 linker’ against the different linker fragments.
and, for the preparation of modified histone H4, N-terminal H4 pep- Plasmid constructs for the preparation of biotinylated 601 dinucleo-
tides (amino acids 1–28) were ligated to truncated H4Δ1–28I29C using some DNAs containing 200 bp linkers consisting of either the SV40
native chemical ligation. All peptides contained a C-terminal benzyl enhancer or the SV40 promoter were generated by PCR amplification
thioester. All histone H4 peptides were N-terminally acetylated. Liga- of the SV40 enhancer and promoter sequences from pGL3-control
tions were performed in 550 μl of degassed ligation buffer (200 mM (Promega) and cloning the resulting fragments into the vector back-
KPO, 2 mM EDTA, 6 M guanidine hydrochloride) containing 1 mg of bone of pUC19-di601_NcoI/NheI_5xGal4 through NcoI and NheI, thereby
4
modified/unmodified histone tail thioester peptide (purchased from exchanging the ‘5×Gal4 linker’ against the 200 bp SV40 enhancer
Cambridge Peptides or Almac Sciences), 4 mg of truncated histone, or promoter sequences. For all of the constructs, the dinucleosome
20 mg 4-mercaptophenylacetic acid and 25 mg Tris(2-carboxyethyl) sequences were then amplified from one copy to eight copies per
phosphine as reducing agent at a pH of 7.5. The reactions were incu- plasmid as described previously25,51.
bated overnight at 40 °C and quenched by addition of 60 μl 1 M DTT The biotinylated 601 dinucleosome DNAs containing 200 bp link-
and 700 μl 0.5% acetic acid. After precipitation clearance by centrifu- ers with randomized DNA sequences were generated from a library
gation, the ligation reactions were directly loaded and purified onto of single-stranded 200 bp scrambled linker oligonucleotides (cus-
a reversed-phase chromatography column (PerkinElmer Aquapore tom synthesis by Biolegio) containing 192 bp of randomized DNA
RP-300 (C8) 250 mm × 4.6 mm inner diameter). Modified histone H3 sequence flanked by 5′ NcoI and 3′ NheI restriction sites and 5′ bGHR
was purified using a gradient of 45–55% B (buffer A: 0.1% trifluoroacetic and 3′ pCIfor primer-binding sites. The single-stranded oligo was
acid in water; B: 90% acetonitrile, 0.1% trifluoroacetic acid) over 10 converted to double-stranded DNA by annealing it to the pCIfor
column volumes. Modified histone H4 was purified using a gradi- primer (Sigma-Aldrich) and performing a primer extension of pCIfor.
ent of 35–45% B (buffer A: 0.1% trifluoroacetic acid in water; B: 90% The primer extensions were performed using Taq DNA polymerase
acetonitrile, 0.1% trifluoroacetic acid) over 10 column volumes. Positive in a 96-well plate format with 96 × 50 μl reactions. Each 50 μl reac-
fractions containing ligated full-length histone H3 or histone H4 were tion contained 1 μg of the 200 bp scrambled linker oligonucleotide
then combined and lyophilized. (250 nM), 340 ng pCIfor primer (1 μM, fourfold molar excess over
the 200 bp scrambled linker oligonucleotide), 200 μM dNTPs and extraction Maxi kit (Macherey-Nagel). Biotinylation and the purity of
2.5 U Taq polymerase (New England Biolabs) in 1× ThermoPol buffer the dinucleosome DNAs were verified by depletion with streptavidin
(New England Biolabs). Using a thermocycler, the oligonucleotides Sepharose High Performance beads (Cytiva) and agarose gel electro-
were denatured for 5 min at 95 °C, annealed for 1 min at 58 °C and the phoresis of the inputs and supernatants (Supplementary Information).
primer extension reaction was then allowed to proceed for 5 min at Dinucleosomes were then assembled in the presence of MMTVA com-
68 °C. The reactions were pooled and the remaining single-stranded petitor DNA as described above.
DNA was removed by direct addition of 2,000 U of exonuclease I
(New England Biolabs) per ml reaction volume and incubation for Eukaryotic tissue culture. HeLa S3 cells (ATCC, CCL-2.2) cells were
30 min at 37 °C. The resulting double-stranded DNA was purified obtained from the Cancer Research UK Clare Hall Laboratories Cell
using the QIAquick PCR purification kit (Qiagen) according to the Services Facility and maintained in suspension culture at 37 °C under
manufacturer’s instructions (20× columns, total yield of 75 μg in 1 ml 5% CO in RPMI 1640 medium. HeLa S3 cells were authenticated by mor-
2
buffer EB). The double-stranded 200 bp scrambled linker DNAs were phology on the basis of their ability to grow both in suspension culture
digested with NcoI and NheI (Thermo Fisher Scientific) using 5 μl of and as round spherical cells in adhesion culture. A HeLa Kyoto BAC cell
FastDigest enzyme per μg DNA, concentrated using the QIAquick PCR line expressing the C-terminal localization and affinity purification
purification kit (10× columns, total elution volume of 500 μl buffer (LAP)-tagged INO80 subunit ACTR548 was a gift from M. Mann (Max
EB) and separated by 2.5% agarose gel electrophoresis. The 200 bp Planck Institute of Biochemistry). Cells were cultured at 37 °C under
band containing the scrambled linker fragments was excised from 5% CO in Dulbecco’s modified Eagle’s medium (DMEM) containing
2
the gel and purified using the QIAquick gel extraction kit (Qiagen) 4.5 mg ml−1 glucose, 10% fetal calf serum, 1% penicillin–streptomycin
according to the manufacturer’s instructions (eight columns, total and 1% l-glutamine and validated by immunoprecipitation and im-
yield of 11.64 μg in 300 μl buffer EB). The purified NcoI/NheI-digested munoblotting against the tagged ACTR5. MCF-7 cells (ATCC, HTB-22)
200 bp scrambled linker fragments were subsequently ligated into the were obtained from the Cell Services Facility of the IGBMC. Cells were
NcoI/NheI-digested, dephosphorylated (Quick CIP, New England Bio- cultured at 37 °C under 5% CO in DMEM containing 4.5 mg ml−1 glucose,
2
labs) and agarose-gel-purified vector backbone of pUC19-di601_NcoI/ 10% fetal calf serum, 1 mM sodium pyruvate, 1% penicillin–streptomycin
NheI_5×Gal4, thereby exchanging the ‘5×Gal4 linker’ against the library and 1% l-glutamine and authenticated by morphology and by regu-
of 200 bp scrambled linker fragments. Ligations were assembled using larly testing the induction of oestrogen-responsive genes by quantita-
50 μg of NcoI/NheI-linearized pUC19-di601 vector backbone, 11.64 μg tive PCR with gene-specific primers or global RNA-sequencing after
of NcoI/NheI-digested 200 bp scrambled linker inserts (approximately 17β-estradiol treatment. IMR90 human fibroblasts were purchased
3.5-fold molar excess of inserts over the 3 kb vector backbone) and directly from ATCC (CCL-186) and cultured at 37 °C under 5% CO in
2
200 μl (400,000 cohesive end units) of T4 DNA Ligase (New England DMEM containing 4.5 mg ml−1 glucose, 10% fetal calf serum, 1 mM
Biolabs) in a total volume of 4 ml of 1× T4 DNA ligase reaction buffer, sodium pyruvate, 1% penicillin–streptomycin and 1% l-glutamine.
and incubated overnight at 16 °C. After the ligation, ATP was added to Cells were authenticated by morphology and only maintained for a
the reaction to a final concentration of 1 mM and unligated linear DNA limited number of passages. All of the cell lines were tested and were
was digested by addition of 1,000 U of exonuclease V (New England mycoplasma free.
Biolabs) and incubation for 50 min at 37 °C. Circular plasmid DNA that
was protected from the exonuclease V digestion was then purified and SNAP. SILAC-labelled nuclear extracts were prepared from HeLa S3 cells
concentrated using the QIAquick PCR purification kit (10 columns, as previously described25. The isotopically light (R K ) or heavy (R K)
0 0 10 8
elution in 30 μl buffer EB per column). The total yield of ligated circular nuclear extracts were mixes of three independently prepared nuclear
plasmid DNA was 6.5 μg in 280 μl. The ligated plasmids represent a extracts. For each pull-down, nucleosomes corresponding to 12.5 μg
library of pUC19 vectors in which each vector contains one copy of a of octamer were immobilized on 10 μl streptavidin Sepharose High
601 dinucleosome DNA each incorporating a different 200 bp linker Performance beads (Cytiva) in the final reconstitution buffer (10 mM
of random sequence between the two 601 nucleosome-positioning Tris (pH 7.5), 250 mM KCl, 1 mM EDTA and 1 mM DTT; supplemented
sequences. The plasmid library was amplified by electroporation into with 0.1% NP-40) and then rotated with 0.5 mg HeLa S3 SILAC-labelled
10-beta electrocompetent E. coli cells (New England Biolabs) according nuclear extract in 1 ml of SNAP buffer (20 mM HEPES (pH 7.9), 150 mM
to the manufacturer’s instructions using 2 μl (47 ng) of library DNA NaCl, 0.2 mM EDTA, 10% glycerol) supplemented with 0.1% NP-40, 1 mM
and 25 μl of competent cells per electroporation. Cells were recov- DTT and protease inhibitor cocktail (Roche) for 4 h at 4 °C. Nucleosome
ered in 1 ml of outgrowth medium and selected on 24.5 cm2 BioAssay pull-downs with acetylated histones and the corresponding unmodified
LB -agar plates (Corning). Serial dilutions were plated to determine control pull-downs were supplemented with HDAC inhibitors (5 mM
Amp
the transformation efficiency and complexity of the library. In total, sodium butyrate (Sigma-Aldrich, B5887) and 250 nM TSA (Sigma-
>108 independent clones were obtained from 24 electroporations. The Aldrich, T1952)) to prevent removal of the acetyl modifications. After
colonies were gently scraped off the plates in liquid LB medium and two washes with 1 ml SNAP buffer + 0.1% NP-40 and then two washes with
plasmid DNA was isolated using the NucleoBond PC 10000 Giga-prep 1 ml SNAP buffer without NP-40, the beads from both SILAC pull-downs
kit (Macherey-Nagel). The total yield of plasmid DNA from 24 plates (modified and unmodified control nucleosome) were pooled. The
was 16 mg. In total, 20 clones were picked from a high-dilution plate supernatant was completely removed, and bound proteins were eluted
and sequenced to verify the correct length and random composition by on-bead digestion (see below).
of the 200 bp linker sequences.
For preparing the different biotinylated dinucleosome DNAs the Label-free nucleosome affinity purifications. Nuclear extracts were
pUC19 601 dinucleosome plasmid constructs were first digested with prepared from HeLa S3 cells as previously described25 except that cells
EcoRV, ethanol-precipitated and then further digested with EcoRI (New were cultured with 10% regular fetal calf serum and no isotopically
England Biolabs) to liberate the dinucleosome DNAs. After another labelled amino acids were used. Unlabelled nuclear extracts were a
ethanol precipitation, the EcoRI overhangs were filled in with dATP mix of three independently prepared nuclear extracts. Nucleosome
and biotin-11-dUTP (Yorkshire Bioscience) using Klenow (3′→5′ exo−) pull-downs were performed in the same manner as described above
polymerase (New England Biolabs). The biotinylated dinucleosome for SNAP, except for the bead washing and protein elution steps, which
DNAs were again concentrated by ethanol precipitation, separated were performed as follows: after incubation with nuclear extracts,
from the pUC19 vector DNA by preparative agarose gel electrophoresis beads with immobilized nucleosomes were washed three times with
and then purified from the excised gel slices using the NucleoSpin gel 1 ml SNAP buffer + 0.1% NP-40, the supernatant was completely removed
Article
and bound proteins were eluted by boiling the beads in 50 μl Laemmli supplemented with NaCl to a final concentration of 500 mM. Antibod-
sample buffer containing 1% SDS at 95 °C for 5 min. A 20 μl protein ies and co-bound chromatin were eluted by boiling the beads in 30 μl
aliquot was then digested with trypsin using a filter-aided sample prepa- of Laemmli sample buffer containing 1% SDS and supplemented with
ration (FASP) protocol and analysed using liquid chromatography– 300 mM NaCl for 10 min at 95 °C. The eluate was transferred to a fresh
mass spectrometry (LC–MS) as described below. tube and incubated in a thermomixer at 65 °C and 500 rpm for 12 h.
For the histone PTM proteomic analysis, eluted proteins as well as the
Cross-linking ChIP for MS analysis. IMR90 human fibroblasts input samples (see above) were resolved on a 4–20% polyacrylamide
were cultured as described above. Cells were washed three times gel (Novex WedgeWell Tris-Glycin-Minigel, Invitrogen), histone bands
with PBS and cross-linked on the plate with 1.25 μM ethylene glycol were excised, in-gel derivatized, digested with trypsin and processed for
bis(succinimidyl succinate) (EGS) and 0.75 μM disuccinimidyl glutar- LC–MS analysis as described below. For the identification and quanti-
ate in PBS for 30 min at room temperature. After the first cross-linking fication of co-purified chromatin proteins, a 10 μl aliquot of the eluted
reaction, cells were washed twice with PBS and cross-linked with 1% proteins in Laemmli sample buffer was processed for trypsin digestion
formaldehyde in PBS at room temperature for 10 min. Cross-linking using a FASP protocol and analysed using LC–MS as described below.
reactions were quenched by the addition of glycine solution in PBS to a
final concentration of 125 mM and incubation at room temperature for Native chromatin immunoprecipitations for MS analysis. The HeLa
5 min. Cells were then washed three times with ice-cold PBS, collected Kyoto BAC cell line expressing the C-terminal LAP-tagged INO80 subu-
by scraping and pelleted by centrifugation (1,000g, 5 min, 4 °C). Cells nit ACTR548 was cultured as described above. Cells were collected by
were lysed in a hypotonic buffer (10 mM Tris (pH 7.6), 5 mM NaCl, 1.5 mM trypsinization and were washed three times with ice-cold PBS. Nuclei
MgCl) supplemented with 0.1% NP-40, protease inhibitor cocktail were isolated using a Dounce homogenizer under hypotonic conditions
2
(Roche), 10 mM sodium butyrate and 1 mM DTT using a Dounce homog- in the presence of 0.1% NP-40 as described previously25. Nuclei were
enizer as described previously25. Nuclei were pelleted by centrifugation resuspended in ice-cold MNase digestion buffer (10 mM Tris (pH 7.6),
(3,000g, 5 min, 4 °C), washed in hypotonic buffer supplemented with 15 mM NaCl, 60 mM KCl, 0.1% NP-40) supplemented with protease
300 mM NaCl and pelleted again (3,000g, 5 min, 4 °C). Nuclei were inhibitor cocktail (Roche) and 10 mM sodium butyrate, and MNase was
resuspended in nuclear lysis buffer (15 mM Tris (pH 7.6), 10% glycerol, added at a proportion of 150 U per approximately 20 × 106 nuclei. The
1% SDS) and incubated for 5 min on ice. Chromatin was pelleted by nucleus suspension was transferred to a thermomixer and, after 2 min
centrifugation (5,000g, 5 min, 4 °C), washed in chromatin wash buffer incubation at 37 °C and 400 rpm, CaCl was added to a final concentra-
2
(15 mM Tris (pH 7.6), 300 mM NaCl, 1.5 mM MgCl, 0.5% NP-40, 0.5% tion of 1.5 mM and the mixture was incubated at 37 °C for another 6 min.
2
Triton X-100), pelleted again (5,000g, 5 min, 4 °C) and resuspended The MNase digestion was stopped by the addition of EDTA to a final
in ChIP buffer (20 mM Tris (pH 7.6), 150 mM NaCl, 2 mM EDTA, 1% Tri- concentration of 10 mM. The mixture was then diluted 1:1 with ice-cold
ton X-100, 0.01% SDS) supplemented with protease inhibitor cocktail 2× SNAP buffer (30 mM HEPES (pH 7.8), 300 mM NaCl, 0.1% NP-40, 20%
(Roche) and 10 mM sodium butyrate. DNA was fragmented to an aver- glycerol, 0.4 mM EDTA) supplemented with protease inhibitor cocktail
age size of 150–300 bp by sonication (Qsonica, Q800R2, 70% amp, (Roche) and 10 mM sodium butyrate. The samples were rotated on a ro-
10 s off, 10 s on, 40 min active sonication time, 4 °C). Chromatin debris tation wheel for 45 min at 4 °C and further incubated in a thermomixer
was pelleted by centrifugation (16,000g, 10 min, 4 °C). Then, 25 μl of at 4 °C and 1,000 rpm for another 15 min. Nuclear debris was pelleted
supernatant was used for DNA purification to check the average DNA by centrifugation (16,000g, 10 min, 4 °C). The resulting supernatants
fragment size and another 25 μl supernatant aliquot was transferred were transferred to fresh 1.5 ml low-protein-binding Eppendorf tubes
to a fresh tube, de-cross-linked as described below, and stored at 4 °C and used for the purification of nucleosomes bound to the INO80 com-
until it was later used as the input sample for histone PTM analysis to plex as described below. To determine the efficiency of the MNase
define the average levels of core histone PTMs in bulk chromatin. For digestion, the pellets containing the insoluble chromatin fraction were
DNA purification, the sample was mixed 1:1 with 2× de-cross-linking resuspended in 1× supernatant volume of SNAP buffer, supplemented
buffer (20 mM Tris (pH 7.6), 600 mM NaCl, 2% SDS) and incubated at with proteinase K, and incubated at 37 °C overnight. In parallel, 25 μl
65 °C overnight. The next day, proteinase K was added and the mixture aliquots of the supernatants were transferred to fresh tubes, supple-
was incubated at 37 °C for 2 h. DNA was purified using the QIAquick PCR mented with proteinase K and incubated at 37 °C overnight. After pro-
purification kit (Qiagen) and eluted in RNase/DNase-free water. RNase teins were digested with proteinase K, DNA was extracted using the
A was added and the mixture was incubated at 37 °C for 1 h. DNA was QIAquick PCR purification kit (Qiagen) and eluted in RNase/DNase-free
resolved on an agarose gel and visualized with ethidium bromide. App- water. RNase A was added, and the mixtures were incubated at 37 °C
roximately 0.2 mg chromatin (as measured by DNA content) was used for 1 h. The DNA was then resolved on an agarose gel and visualized
for each ChIP reaction with the following antibodies: anti-H3K4me1 with ethidium bromide. For each sample, another 25 μl aliquot of the
(Abcam, ab8895), anti-H3K4me3 (Millipore, 17-614), anti-H3 (Active supernatant was transferred to a fresh tube and subsequently used as
motif, 39163), anti-H4 (Abcam, ab31830). For H3K4me3 ChIP reac- the input sample to define average histone modification levels on bulk
tions, 0.6 mg chromatin was used. To boost the identification of H3K4 chromatin. For the purification of nucleosomes bound to the INO80
methylation-state-specific protein interactors, H3 and H4 ChIPs were complex, 25 μl of GFP-Trap Agarose beads (ChromoTek) were added
performed using chromatin inputs partially depleted in H3K4me1- and to MNase-digested supernatants and the mixture was incubated on
H3K4me3-modified nucleosomes and co-bound protein factors. Speci- a rotation wheel (25 rpm) overnight at 4 °C. The beads were pelleted
fically, H3K4me1 and H3K4me3 ChIPs were performed first, then the by centrifugation (250g, 3 min, 4 °C), followed by two washes with
chromatin inputs used for the H3K4me1 and H3K4me3 ChIPs were com- ice-cold SNAP buffer and one wash with SNAP buffer supplemented
bined and subsequently used for H3 and H4 ChIPs. This aimed to shift with NaCl to the final concentration of 200 mM. The supernatant was
the composition of the bulk chromatin-associated proteome measured completely discarded and the beads were resuspended in 40 μl of SNAP
in H3 and H4 control ChIPs towards regions devoid of H3K4me1 and buffer supplemented with 1 μg of 3C protease (Sigma-Aldrich). The
H3K4me3. The antibody–chromatin mixture was incubated overnight mixture was then incubated for 8 h at 4 °C. The beads were pelleted
on a rotation wheel (25 rpm) at 4 °C. Antibodies were captured using by centrifugation, and the supernatant was transferred to a fresh tube,
a 1:1 mixture of protein A and protein G Dynabeads (Thermo Fisher mixed with Laemmli sample buffer and boiled at 95 °C for 5 min. To iden-
Scientific) for 2 h at 4 °C while rotating on a rotation wheel (25 rpm); tify histone PTMs of INO80-bound nucleosomes the immunopurified
40 μl of bead mixture was used per ChIP sample. Beads were washed proteins and input samples were resolved on a 4–20% polyacrylamide
three times with ice-cold ChIP buffer and twice with ice-cold ChIP buffer gel (Novex WedgeWell Tris-Glycin-Minigel, Invitrogen), histone bands
were excised, in-gel derivatized, digested with trypsin and analysed anti-ACTR5 (GeneTex, GTX80453, 1:1,000), anti-TBRG1 (Santa Cruz
using LC–MS as described below. (D-9), sc-515620, 1:1,000), anti-H3K4me3 (Millipore, 17-614, 1:2,000),
anti-H4 (Abcam, ab31830, 1 μg ml−1), anti-H4ac (pan-acetyl) (Active
CRISPR–Cas9-mediated endogenous protein tagging. The core Motif, 39967, 1:1,000), anti-CBX4 (Cell Signaling Technology, E6L7X
INO80 complex subunit INO80B was endogenously tagged at its 30559, 1:1,000), anti-CBX8 (Santa Cruz (C-3), sc-374332, 1:1,000),
C-terminus with a V5 epitope in the MCF-7 cell line using the tagging anti-H2B (Abcam, ab1790, 1:1,000), anti-H2A.Z (Abcam, ab4174,
strategy described previously54. Specifically, 1 day before transfection, 1:1,000). Immunoblot images were acquired by CCD camera using the
MCF-7 cells were seeded onto 24-well plates at approximately 1.0 × 105 Bio-Rad ChemiDoc Touch Imaging System running Image Lab Touch
cells per well in 500 μl of low-glucose DMEM medium supplemented Software (v.2.3.0.07).
with 10% FBS, 1 mM glutamine and 100 μg ml−1 penicillin–streptomycin.
On the day of transfection, 25 μl of Opti-MEM medium was added to a MS methods
1.5 ml sterile Eppendorf tube, followed by the addition of 1,250 ng of Sample preparation for MS. On-bead digestion and peptide puri-
TrueCut Cas9 Protein v2 nuclease (Invitrogen) and 240 ng of two-piece fication for SNAP samples. The beads were resuspended in 50 μl of
gRNA (crRNA:tracrRNA duplex) generated by annealing crRNA (IDT) elution buffer (2 M urea, 100 mM Tris (pH 7.5), 10 mM DTT) and incu-
and tracrRNA (IDT) according to the manufacturer’s instructions. After bated on a shaker (1,000 rpm) at 25 °C for 20 min. Iodoacetamide
mixing briefly by vortexing, 1 μl Cas9 Plus reagent was added to the (Sigma-Aldrich, I1149) was added to a final concentration of 50 mM
solution containing Cas9 protein and gRNA. The mixture was incubated and the sample was incubated on a shaker (1,000 rpm) at 25 °C in the
at 25 °C for 5 min to allow the formation of Cas9 ribonucleoprotein dark for 10 min. After digestion with 0.3 μg trypsin (Promega V5113)
particles (RNPs). For co-delivery of homology donor DNA, 800 ng for 2 h on a thermo shaker (1,000 rpm) at 25 °C, the supernatant was
of single-stranded DNA oligonucleotide (IDT) was added to the Cas9 transferred to a new tube and was further digested with 0.1 μg trypsin
RNPs at this point. Meanwhile, 25 μl Opti-MEM medium was added to overnight at 25 °C. The digestion was stopped by adding 5.5 μl of 10%
a separate sterile Eppendorf tube, followed by the addition of 1.5 μl of trifluoroacetic acid. Eluted peptides were purified on C18 stage-tips
Lipofectamine CRISPRMAX. After briefly vortexing, the Lipofectamine (Glygen 10-200 μl TopTips) according to the manufacturer’s instruc-
CRISPRMAX solution was incubated at 25 °C for approximately 5 min. tions and dried using a SpeedVac.
After incubation, the Cas9 RNPs were then added to the Lipofectamine FASP of label-free proteomics samples. Filter-aided sample prep-
CRISPRMAX solution. The mixture was incubated at 25 °C for 10–15 min aration was performed as described previously52. In brief, 10–20 μl
to form Cas9 RNPs and Lipofectamine CRISPRMAX complexes and then aliquots of protein mixtures in 1% SDS Laemmli sample buffer were
added to the cells. At 48 h after transfection, the cells were collected diluted with 200 μl of 100 mM triethylammonium bicarbonate buffer
by trypsination and seeded in 96-well plates at 1 cell per well. After (TEAB; pH 8.5). For protein reduction, 1 μl of 1 M DTT was added to each
reaching 60–80% confluency, the cells were trypsinized and split 1:1 sample and the samples were incubated at 60 °C for 30 min. After cool-
into two 96-well plates where the first plate was used for immunofluo- ing the samples to room temperature, 300 μl of freshly prepared UA
rescence screening with monoclonal mouse anti-V5 primary antibodies buffer (8 M urea in 100 mM TEAB (pH 8.5)) was added to each sample.
(eBioscience, TCM5 14-6796-82, 1:250) and Alexa-Fluor-488-coupled Proteins were alkylated by the addition of 10 μl of 300 mM iodaceta-
anti-mouse IgGs as secondary antibodies (Jackson ImmunoResearch mide solution and subsequent incubation for 30 min at room tem-
Laboratories, 715-545-150, 1:333), and the second plate was used for the perature in the dark. The samples were then concentrated to dryness
subsequent expansion and further testing of V5-positive clones. The in a 30 kDa cut-off centrifugal spin filter unit (Millipore), and washed
immunofluorescence screen for V5-positive clones was performed as three times with 200 μl UA buffer and twice with 200 μl of 50 mM
previously described54. TEAB (pH 8.5). Then, 40 μl of a 50 ng μl−1 trypsin solution in 50 mM
TEAB (pH 8.5) was added to each sample and protein digestion was
Co-IP. Approximately 1.0 × 107 MCF-7 WT or INO80B-V5 cells were used performed overnight at 37 °C. Peptides were centrifuged through the
for nuclear extract preparations as described previously25. The nuclear filter, and the collected flow through was acidified by the addition of
extract was diluted with IP buffer (20 mM HEPES (pH 7.9), 50 mM NaCl, trifluoroacetic acid to a final concentration of 0.5% (v/v). About 300 ng
0.2 mM EDTA, 5% glycerol, 0.1% NP-40, 1 mM DTT and protease inhibitor of the tryptic peptide mixtures was then used for LC–MS analysis as
cocktail (Roche)) to a final protein concentration of around 1 μg μl−1 described below.
and a NaCl concentration of 160 mM and subsequently cleared by cen- Histone sample preparation for proteomics analysis. Histone
trifugation at 20,000g for 10 min at 4 °C. Then, 1 ml of cleared nuclear proteins were prepared for LC–MS analysis using a hybrid chemical
extract was mixed with 5 μl of anti-V5 antibodies (Abcam, ab15828) and derivatization protocol adopted for in-gel sample preparation. In
incubated on a rotating wheel over night at 4 °C. The next day, 20 μl of brief, proteins were resolved on 4–20% polyacrylamide gels (Novex
a 1:1 mixture of protein A and protein G Dynabeads (Invitrogen) were WedgeWell Tris-Glycin-Minigel, Invitrogen) followed by Coomassie
added to the sample followed by 1 h incubation on a rotation wheel at staining. Histone protein bands were excised from the gel and destained
4 °C. Magnetic beads were washed three times with the IP buffer con- in a destaining buffer (100 mM triethylammonium bicarbonate in 50%
taining 150 mM NaCl. Co-immunoprecipitated proteins were eluted acetonitrile). After destaining, the gel pieces were dehydrated with
from the beads by boiling in 20 μl of Laemmli sample buffer for 5 min 200 μl of 100% acetonitrile for 10 min at room temperature after which
at 95 °C. Eluted proteins were subsequently used for immunoblotting acetonitrile was discarded. Propionylation solution was prepared by
and LC–MS experiments (IP–MS). For LC–MS analysis, proteins were mixing 50 mM TEAB (pH 8.5) and freshly prepared 1% (v/v) propionic
digested with trypsin using a FASP protocol as described below. anhydride solution in water at a 100:1 ratio. Immediately after prepara-
tion, 100 μl of propionylation solution was added to the dehydrated
Protein detection by immunoblotting. Proteins were separated by gel pieces followed by 10 min incubation at room temperature. The
SDS–PAGE and blotted onto nitrocellulose membranes (0.45 μm, Ther- propionylation reaction was quenched by the addition of 10 μl of 80 mM
mo Fisher Scientific) using a Bio-Rad PROTEAN mini-gel and blotting hydroxylamine and subsequent incubation for 20 min at room tem-
system. Antibodies were diluted in TBST + 5% milk (25 mM Tris (pH 7.5), perature. The propionylation solution was discarded and gel pieces
137 mM NaCl, 2.7 mM KCl, 0.2% Tween-20, 5% non-fat dry milk). The were dehydrated with 200 μl of 100% acetonitrile for 10 min at room
following primary antibodies were used for immunoblots: anti-V5 temperature. After this, the acetonitrile solution was discarded and
tag (eBioscience, TCM5 14-6796-82, 1:1,000), anti-INO80 (Abcam, 20 μl of 50 ng μl−1 trypsin solution in 100 mM TEAB (pH 8.5) was added.
ab118787, 1:2,000), anti-INO80B (Santa Cruz (E-3), sc-390009, 1:1,000), Trypsin digestion was performed overnight at 37 °C. The next day,
Article
50 μl of 100 mM TEAB (pH 8.5) solution was added to each sample fol- for higher-energy collisional dissociation fragmentation depending
lowed by 30 min incubation in a thermo shaker (37 °C, 1,500 rpm). A 1% on signal intensity. Dynamic exclusion was set for 30 s.
(v/v) solution of phenyl isocyanate in acetonitrile was freshly prepared MS analysis of histone samples. For LC–MS analysis of modified his-
and 15 μl added to each sample and incubated for 60 min at 37 °C. The tone proteins, the acidified histone peptide digests were analysed
samples were acidified by the addition of 24 μl 1% trifluoroacetic acid. on the Q-Exactive HF mass spectrometer (Thermo Fisher Scientific)
Peptides were desalted with C18 spin columns (Thermo Fisher Scien- coupled in-line to a nanoEasy LC (Thermo Fisher Scientific). In brief,
tific) according to the manufacturer’s instructions, dried in a speed-vac, the samples were automatically loaded onto an in-house packed 2 cm
resuspended in 50 μl 0.1% trifluoroacetic acid and subsequently used 100 μm inner diameter C18 pre-column with buffer A (0.1% formic acid)
for LC–MS analysis. and then eluted and separated on an in-house packed Reprosil-Pur
120 C18-AQ (3 μm; Dr. Maisch) analytical column (20 cm × 75 μm inner
LC–MS-based proteomics measurements. MS analysis of SNAP diameter) using a 35 min linear gradient from 0% to 40% buffer B (90%
samples. SNAP samples were processed and analysed by LC–MS acetonitrile, 0.1% formic acid). Full scan MS spectra (m/z 300–1,000)
on a Q-Exactive mass spectrometer (Thermo Fisher Scientific) as and MS/MS fragment spectra were acquired in the Orbitrap with a reso-
described previously55. In brief, the samples were loaded at 8 μl min−1 lution of 120,000 or 15,000, respectively, with maximum injection
onto a trap column (Thermo Fisher Scientific, Acclaim PepMap 100; times of 50 ms each. Up to the 20 most intense ions were selected for
100 μm internal diameter, 2 cm length, C18 reversed-phase material, higher-energy collisional dissociation fragmentation depending on
5 μm diameter beads and 100 Å pore size) in 2% acetonitrile and 0.1% signal intensity. Dynamic exclusion was disabled.
trifluoroacetic acid. Each of the samples was loaded twice, providing
two technical replicates. Peptides were eluted on line to an analyti- MS RAW data search and quantification. Analysis of SNAP MS data.
cal column (Thermo Fisher Scientific, Acclaim PepMap RSLC; 75 μm Protein abundances were quantified from the Q-Exactive raw data
internal diameter, 25 cm length, C18 reversed-phase material, 2 μm files using MaxQuant (v.1.5.2.8)56 against the UniProt UP000005640
diameter beads and 100 Å pore size) and separated using a flow rate of canonical proteome (downloaded in September 2016) using 2-plex
250 nl min−1 and the following gradient conditions: initial 5 min with 4% labelling (Arg0/Lys0 and Arg10/Lys8). The search was performed
buffer B; a 90 min gradient of 4–25% B; a 30 min gradient of 25–45% B; a allowing for fixed carbamidomethyl modification of cysteine resi-
1 min gradient 45–90% B; and finally 15 min isocratic at 100% B before dues and variable oxidation of methionine residues and acetylation of
returning to the starting conditions for a 15 min equilibration (buffer amino termini. The minimum peptide length was set to 7. All raw files
A: 2% acetonitrile and 0.1% formic acid in water; B: 80% acetonitrile resulting from the forward and reverse pull-downs, including techni-
and 0.1% formic acid). The Q-Exactive instrument acquired full-scan cal replicates for each nucleosome tested, were processed together
survey spectra (m/z 300–1,650) at 70,000 resolution. An automatic using the ‘match between runs’ feature. H/L ratios were computed in
gain control target value of 3 × 106 and a maximum injection time of advanced ratio computation mode, with the minimal ratio and peptide
20 ms were used. The top 10 most abundant multiply charged ions were count set to 1. The corresponding mqpar.xml file is deposited along
selected in a data-dependent manner, fragmented by higher-energy with the proteomics data. Initial trial experiments with mono-, di- and
collision-induced dissociation, and data were collected over the range tetra-nucleosomes (Supplementary Information) were quantified
200–2,000 m/z at 17,500 resolution. An automatic gain control target separately by MaxQuant v.1.5.1.0 against the December 2015 version
value of 1 × 105 with a maximum injection time of 120 ms was used. A of UniProt proteome with more stringent settings requiring at least
dynamic exclusion time of 30 s was enabled. two peptides for ratio estimation.
MS analysis of label-free proteomics samples. LC–MS/MS analysis Analysis of label-free MS data. Protein identification and quantifica-
of label-free nucleosome pull-downs and ChIP–MS proteomics sam- tion was performed using Proteome Discoverer v.2.5 (Thermo Fisher
ples was performed on the Q-Exactive HF mass spectrometer (Thermo Scientific). Data were searched against the human Swiss-Prot database
Fisher Scientific) coupled in-line to a nanoEasy LC (Thermo Fisher Sci- using Mascot57 as the search engine, with a precursor mass tolerance of
entific). The samples were loaded in solvent A (0.1% formic acid) on 5 ppm and a fragment mass tolerance of 0.05 Da. Two missed cleavages
a two-column set-up consisting of a 3.5 cm, 100 μm inner diameter were allowed for trypsin and carbamidomethylation of cysteine was
pre-column packed with Reprosil-Pur 120 C18-AQ (5 μm; Dr. Maisch) set as a static modification, while oxidation of methionine was set as
and an 18 cm, 75 μm inner diameter analytical column packed with dynamic. Label-free quantification was achieved as match between
Reprosil-Pur 120 C18-AQ (3 μm; Dr. Maisch). A gradient of solvent B (95% runs by using the Minora Feature Detector, the Feature Mapper and
acetonitrile, 0.1% formic acid) was applied at a flow rate of 250 nl min−1 as the Precursor Ions Quantifier. The maximum retention time shift for
follows: 3% to 25% B in 90 min; 25% to 45% B in 30 min; 45% to 100% B in chromatographic alignment was set to 2 min and the retention time
3 min; and 100% B in 8 min. MS was obtained at a resolution of 120,000 tolerance for mapping features was set to 1 min. Peptide quantification
and MS/MS as top 15 at a resolution of 15,000 and with a dynamic exclu- was performed as the peak area normalized to the total peptide amount
sion of 30 s. The maximum injection time was set to 100 ms for both MS and protein quantification as the average of the top three unique
and MS/MS and only peptides of charge state 2, 3 and 4 were selected peptides.
for MS/MS. Analysis of histone MS data. For the identification and quantification
LC–MS/MS analysis of INO80-V5 IP–MS samples was performed on of histone PTMs in ChIP–MS samples and the quality control of recom-
the Q-Exactive HF mass spectrometer (Thermo Fisher Scientific) cou- binantly produced modified histone proteins, MS raw data files were
pled to a nano-RSLC (Ultimate 3000, Dionex). In brief, the samples were manually analysed using Skyline (v.20.1.0.31)58. In brief, a list of unmodi-
automatically loaded onto a nano trap column (300 μm inner diameter fied as well as differentially modified histone H3 and H4 peptides was
× 5 mm, packed with Acclaim PepMap100 C18, 5 μm, 100 Å; LC Packings) manually compiled and used to evaluate the modification status of
before separation by reversed-phase chromatography (HSS-T3 M-class histones in each sample. All lysine residues not bearing acetylation
column, 25 cm, Waters) in a 95 min nonlinear gradient from 3 to 40% ace- or methylation were considered to be propionylated and all peptide
tonitrile in 0.1% formic acid at a flow rate of 250 nl min−1. Eluted peptides N termini were considered to be modified with phenyl isocyanate.
were analysed using the Q-Exactive HF mass spectrometer equipped MS1 filtering was set to include 3 isotope peaks and the MS1 resolving
with a nano-flex ionization source. Full scan MS spectra (m/z 300– power was set at 120,000. MS2 resolving power was set at 15,000. For
1,500) and MS/MS fragment spectra were acquired in the Orbitrap with each modified histone peptide, the relative abundance was estimated
a resolution of 60,000 or 15,000, respectively, with maximum injec- by dividing its peak area by the sum of the areas corresponding to all
tion times of 50 ms each. Up to ten most intense ions were selected of the observed forms of that peptide (that is, all peptides sharing the
same amino acid sequence). The relative abundance of histone vari- zero across experiments. The normalized data were then further filtered
ant H2A.Z was estimated by dividing the sum of peak areas of unique to include only proteins that were detected in at least two replicates
H2A.Z peptides (that is, only present in H2A.Z but not in any other H2A of at least one experiment.
variants) by the sum of peak areas of all unique peptides corresponding We used limma60 to estimate the log[FC] values between H3K4me3
2
to histones H2A, H2B and H2A.Z. and controls (H3 and H4), H3K4me1 and controls, and H3K4me3 and
H3K4me1. Specifically, we used a zero-intercept means model encod-
Data postprocessing and bioinformatic analyses ing one parameter for each experiment (H3, H4, H3K4me1, H3K4me3),
Data postprocessing. Postprocessing of SNAP MS data. MaxQuant and analysed the contrasts between protein abundance in H3K4me1/3
proteinGroups entries marked as ‘potential contaminant’, ‘reverse’ or experiments and the average abundance of H3 and H4 (for example,
‘only identified by site’ were removed from the datasets analysed. The (H3 + H4)/2), as well as a contrast between H3K4me3 and H3K4me1. The
SILAC H/L ratios for each of the remaining entries were converted to analysis was run using the default parameters of limma (v.3.50.1), with
a log scale. In initial trial experiments (Supplementary Information), the addition of ‘robust=True’ in the ‘eBayes’ step, hypothesis testing was
2
the median and first and third quartiles log[H/L ratio] values were performed using the default settings, assuming zero log[FC] under the
2 2
estimated in all experiments individually, treating forward and reverse null hypothesis. P values were corrected using the Benjamini–Hochberg
experiments separately. Proteins were assumed to be significantly procedure, and significance was assumed at an FDR of 0.05.
enriched if they fell 1.5× the interquartile range away from first and In some cases, the contrasts could not be estimated due to missing
third quartiles for both forward and reverse experiments, matching data. This frequently happened when proteins were detected in one of
the box plots. The data for the main set of experiments were addition- the experiments, but not in controls (or vice versa). In these cases, we
ally annotated with up to date (as of 30 July 2019) metadata that were imputed such log[FC] estimates with infinities (positive and negative).
2
downloaded from the mygene.info API service59 based on the IDs in the Moreover, whenever it was possible to estimate the H3 or H4 controls,
‘Majority Protein ID’ column. Protein identifiers were assigned read- but not both, we imputed the log[FC] estimates using one of such
2
able counterparts on the basis of the associated gene names. Duplicate controls only. The imputed estimates are clearly flagged in the data and
entries were enumerated in parentheses (for example, SMARCA (1) and figures. Estimates based only on single data points (that is, an observed
SMARCA (2)), assigning lower numbers to entries with a higher Max- abundance in one of the three replicates only) are flagged as well.
Quant score. Common prefixes of the gene names were collapsed (for To be able to link the ChIP–MS data with MARCS feature effect esti-
example, SMAD[2,3,9]) for brevity. The principal direction of the data mates, we mapped the ChIP–MS proteins to their MARCS counterparts
spread (that is, the direction of enrichment) in each of the pull-downs through their accession numbers and gene names. The cases in which
was estimated by determining the first principal component of the data one ChIP–MS protein mapped to multiple proteins in the MARCS data-
in the top-left and bottom-right quadrants of the forward and reverse set were resolved by assigning the feature effect estimate with the
log[H/L ratio] plot. The estimate was adjusted by re-evaluating the lowest P-value estimate across all of the matched identifiers.
2
principal direction after removing outlier points ±2 s.d. away from the To obtain association statistics, we performed a Mann–Whitney
median in the second principal direction. Protein-specific variation U-test, comparing the imputed ChIP–MS log[FC] estimates of proteins
2
in the second principal direction across pull-down experiments was strongly recruited to or excluded by a MARCS feature to the imputed
adjusted to zero to correct systemic heavy and light cell population log[FC] estimates of other proteins detected in both MARCS and ChIP–
2
batch effects resulting from different abundances of proteins in the MS data. Only the groups with at least five proteins were tested. For
nuclear extracts from the H/L cell populations or different labelling visualization purposes, we computed the mean log[FC] estimates in
2
efficiencies of proteins with the heavy-labelled amino acids. In cases each of the groups, and their respective differences. For this purpose,
in which either the forward or the reverse H/L ratio was measured for we assumed the infinities to be equal to the maximum finite log[FC]
2
the protein (9.13% of ratio pairs), but not both, the missing ratio was plus a small number.
imputed by projecting the measured ratio to the estimated princi- Postprocessing of variable-linker nucleosome pull-down data.
pal enrichment line. In six cases (0.01%) in which the estimated H/L Label-free MS quantification datasets for the short linker nucleosome,
ratio was infinite as protein intensity could have been measured in the long linker SV40 promoter nucleosome and long linker SV40 enhancer
modified nucleosome, but not in the unmodified nucleosome, the ratio nucleosome affinity-purification experiments were analysed indepen-
was imputed to the maximum ratio identified in the particular SNAP dently. The protein abundances were converted to a log scale, treating
2
experiment. All other missing H/L ratios were imputed to zero (24.27%). zero intensities as missing values. The data were normalized using the
Five proteins of which the forward and reverse H/L ratios were equal abundances of HIST1H4A and HIST2H2BF histones (short linkers) or
to zero in all of the experiments were removed. The resulting data for H4C1 and H2BC12 histones (long linkers) as described in the H3K4me1/3
each of the pull-down experiments were then further rotated so the cross-linking-ChIP–MS methods.
estimated principal direction of variation lays exactly on the ideal 45° For each set of experiments, we used a zero-intercept means model
diagonal, so the reverse ratio on average equals the negative of the in limma and hand-crafted contrasts to measure two types of effects
forward one. For visualizations and computational analyses, the sign on protein binding to dinucleosomes: (1) modification-specific effects,
of the reverse experiment was flipped to be on the same scale as the that is, the log-transformed FC in protein abundance between modi-
2
forward one. fied nucleosome and unmodified nucleosome, given a specific linker
Postprocessing of cross-linked H3K4me1 and H3K4me3 ChIP–MS of certain length, for example, log[H3K27me3 with 50 bp linker] ver-
2
data. Protein abundances obtained from H3K4me1 and H3K4me3 sus log[unmodified with 50 bp linker], as well as (2) linker-specific
2
cross-linking-ChIP–MS experiments were converted to log scale, treat- effects, that is, the log-transformed FC in protein abundance between
2 2
ing zero abundances as missing data. The data were normalized to ten two different linkers, given a certain nucleosome modification, for
histone proteins observed in the data: H2AC20, H2AC21, H2AW, H2AZ2, example, log[H3K27me3 with 55 bp linker] versus log[H3K27me3
2 2
H2BC4, H2BU1, H3-2, H4C1, MACROH2A1 and MACROH2A2. Specifically, with 50 bp linker]. Owing to the large number of missing values, the
we calculated the average log-transformed abundance for the histone second replicate of the H3K27me3 experiment with 35 bp linker was
2
proteins in each of the experiments, and calculated the residuals (that excluded from the analysis. Only proteins that had at least two values
is, log-transformed abundances minus the average (M value)) for the in at least one condition were analysed.
2
histone proteins. The data were normalized by subtracting the median The analysis was run using the default parameters of limma (v.3.50.1),
of these residuals for each of the samples, so that the median M value using the ‘robust=True’ parameter in the ‘eBayes’ step. P values were
of the normalized data for the histone proteins remains approximately corrected using the Benjamini–Hochberg procedure, assuming
