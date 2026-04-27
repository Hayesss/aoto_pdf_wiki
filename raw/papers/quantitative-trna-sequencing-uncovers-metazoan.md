---
source_path: /mnt/c/Users/Administrator/Zotero/storage/KR5DK374/Pinkard 等 - 2020 - Quantitative tRNA-sequencing uncovers metazoan tissue-specific tRNA regulation.pdf
ingested: 2026-04-23
sha256: 28ed95bd8f48490b
---

ARTICLE
OPEN
https://doi.org/10.1038/s41467-020-17879-x
Quantitative tRNA-sequencing uncovers metazoan
fi
tissue-speci c tRNA regulation
✉ ✉
Otis Pinkard1,4, Sean McFarland2, Thomas Sweet3 & Jeff Coller 4
Transfer RNAs (tRNA) are quintessential in deciphering the genetic code; disseminating
nucleicacidtripletsintocorrectaminoacididentity.Whilethisdecodingfunctionisclear,an
emerging theme is that tRNA abundance and functionality can powerfully impact protein
production rate, folding, activity, and messenger RNA stability. Importantly, however, the
expressionpatternoftRNAsisobliquelyknown.HerewepresentQuantitativeMaturetRNA
sequencing (QuantM-tRNA seq), a technique to monitor tRNA abundance and sequence
variants secondary to RNA modifications. With QuantM-tRNA seq, we assess the tRNA
transcriptome in mammalian tissues. We observe dramatic distinctions in isodecoder
expression and known tRNA modifications between tissues. Remarkably, despite dramatic
changesintRNAisodecodergeneexpression,theoverallanticodonpoolofeachtRNAfamily
is similar across tissues. These findings suggest that while anticodon pools appear to be
buffered via an unknown mechanism, underlying transcriptomic and epitranscriptomic dif-
ferences suggest a more complex tRNA regulatory landscape.
1DepartmentofGeneticsandGenomeSciences,CaseWesternReserveUniversity,Cleveland,OH44106,USA.2TevardBiosciences,LabCentral,
Cambridge,MA02139,USA.3DepartmentofNutrition,CaseWesternReserveUniversity,Cleveland,OH44106,USA.4DepartmentofMolecularBiology&
✉
GeneticsandDepartmentofBiology,JohnsHopkinsSchoolofMedicine,Baltimore,MD21205,USA. email:tjs7@case.edu;jmcoller@jhmi.edu
NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications 1
;,:)(0987654321
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
T
ranslation of the genetic code is clearly critical to all life. comparedtodifferentiationstates14.Dittmaretal.clearlyshowed
Whiletheribosomeisthecellularinstrumentthatexecutes thattRNAexpressiondifferedacrosshumantissues15.Moreover,
translation,itreliesupontransferRNA(tRNA)toproperly dysregulation of tRNA expression has been identified in a wide
decipher the genetic information contained within messenger arrayofhumandiseases16.Consistently,tRNAlevelsvarygreatly
RNA (mRNA)1. tRNAs parlay codon identity into amino acid acrossdifferentcancertypes,andGoodarzietal.carefullyshowed
identity.EachtRNAischargedwithhighprecisionandfidelityto thiscanfavortranslationofapro-metastaticstate17–19.Together,
oneof20aminoacids;theaminoacidmatchesthetRNAstriplet these data suggest upregulation of certain tRNA genes is asso-
codeasdeterminedbyitsanticodonloop.Readingofthegenetic ciatedwiththepathogenesisofhumanmalignancies.Inaddition,
codetakesplaceintheribosomeoneaminoacidatatimeviabase mutations in aminoacyl tRNA synthetases, enzymes-mediating
pairing between the mRNA codon and the tRNA anticodon; in tRNA processing events, and tRNA base modification enzymes
this way, each amino acid is brought to the ribosome and poly- are associated with clinical neurodegenerative, neurocognitive,
merizedintothegrowingpolypeptidechaininpreciselytheorder and intellectual disabilities3,20. Since it is becoming clear that
specified within the DNA-encoded gene. tRNA levels can influence gene expression, a detailed under-
This singular nature of tRNA in deciphering the genetic code standing of the tRNA transcriptome is essential.
necessitates that they are subject to a high degree of processing Most previous work has relied on monitoring tRNA levels by
andqualitycontrol.tRNAtranscriptsaresmall;typically~70–80 tedious hybridization-based approaches including array and
nucleotides in size. They are transcribed by RNA polymerase III northernblottingtechniques.Hybridization-basedtechniquescan
(Pol III) in the nucleus and undergo an extensive maturation provide bulk quantitation for some tRNAs with the same antic-
process before utilization2,3. Pol III promoter elements are odon; however, they are unable to distinguish certain anticodon
internal to the tRNA body, constraining sequence variation. In groups and isodecoders differing by only one or a few
addition, all tRNAs undergo exo/endonucleolytic trimming bases15,21,22.Moreover,arraysandnorthernblotsdonotprovide
events and post-transcriptional nucleotide modifications. Some information about potential tRNA modifications, which are
tRNAs are spliced, and all are post-transcriptionally 3′ end considered vital for their function.
modifiedwiththetrinucleotide C-C-A.Inthe cytoplasm, tRNAs This need for improved resolution provided the impetus to
are charged with their appropriate amino acid by specific ami- standardize high-throughput sequencing methodologies capable
noacyl tRNA synthetases4. Mature tRNAs exhibit extensive sec- ofdiscerningtRNAgenesattheisodecoderlevel.Next-generation
ondary cloverleaf and tertiary L-shaped structure and a loop RNA sequencing has revolutionized modern molecular biology
structure containing the codon-specific reverse-complement tri- for most types of transcripts, except tRNAs. Historically, tRNAs
nucleotide (anticodon). Together, processing, modification, and are recalcitrant to high-throughput sequencing due to the afore-
genomically encoded structure cooperate to stabilize tRNA and mentioned base modifications and extensive structures. Many
serveasrecognitionfeaturesforaminoacyltRNAsynthetasesand base modifications disrupt Watson/Crick base pairing and the
translation factors5,6. inherent stem-loop structures impede first-strand synthesis by
tRNAs are present in all known forms of life. In mammals, reverse transcriptase (RT). To circumvent these issues, the few
tRNA anticodons directly complement only 47 (mouse) or 48 publishedmethodsemploycleveranddiverselibrarypreparation
(human)ofthe61sensecodons7.Theothercodonsinthegenetic strategies. DM-tRNA-seq was the first protocol published by
code are recognized by non-cognate tRNA interactions in Zheng et al. specifically for the purposes of sequencing tRNA23.
accordance with Crick’s wobble rules8,9. For example, eight This protocol utilizes a more processive RT and a purified pro-
codons that end in cytosine (C) such as alanine 5′-GCC-3′ have karyotic demethylase, AlkB, to remove a series of methyl groups
no tRNA with a guanosine (G) in the wobble position of the fromtRNAthatcauseRTstalling,thusincreasingthefractionof
anticodon that would decode the 3′ C. Instead, the 5′ adenosine, longer cDNA products. Gogakos et al. developed Hydro-tRNA-
the wobble site of alanine tRNA 5′-AGC-3′, is converted to seq to increase the uniformity of coverage across a given tRNA
inosine (5′-IGC-3′) expanding its capacity to decode C, A, or transcript through a limited fragmentation of tRNA during
uracil(U)-endingcodonsthroughnon-traditionalWatson–Crick librarypreparationtoavoidmodifiedbases24.Thisfragmentation
basepairing.ThusRNAmodificationswithintheanticodonloop allows for priming of shorter tRNA fragments and cDNA
expand the decoding potential of some tRNA families8,10. synthesis. Shigematsu et al. put forth YAMAT-seq, the most
Despite only 20 amino acids and 61 codons, mammals are recent protocol, which utilizes a double-stranded adapter ligated
hypothesized to have well over 400 discrete tRNA genes7. tRNA tothe5′and3′terminiofmaturetRNAthatdiffersfromthenon-
transcripts that share the same trinucleotide anticodon sequence specific adapter ligation and template switching steps of Hydro-
but are encoded by many distinct genes are termed isodecoders. tRNA-seq and DM-tRNA-seq, respectively25. Despite these
In less complex eukaryotes, such as yeast, these genes generate innovative strategies, significant limitations to the current state-
full-length, mature tRNAs of identical sequence. In mammals, of-the-art still exist. For example, DM-tRNA-seq relies on tem-
however, isodecoders generally have sequence distinctions plate switching using TGIRT and gel purification of tRNA, two
beyond the conserved anticodon6. Many of these differences steps with potential to introduce bias26. Hydro-tRNA-seq by
occur in tRNA regions that are important for RNA Pol III design generates shorter reads which are difficult to map, and
transcription, raising the possibility isodecoders are transcribed thusmaybemissingsomeinformation.YAMAT-seqisunableto
differently11. In addition, subtle variations between isodecoders quantifyalargenumberoftRNAsduetotherequirementforfull-
may alter their function in translation12. An important question lengthcDNA,thushighlystructuredandmodifiedtRNAthatRT
intRNAbiologyiswhethermammalianisodecodershavedistinct cannot fully traverse are selected against. A major limitation of
functions, are differentially expressed, or simply reflect genetic each of these protocols is the lack of bias assessment and exten-
redundancy.Theimportanceofthisunderstandingiscleargiven sive cross-validation to evaluate the accuracy of each technique.
the recent finding that tRNA levels dramatically impact mRNA Nonetheless, these technologies have greatly improved our
translation and may influence mRNA decay rates13. understandingoftRNAbiologyandledtoimportantandseminal
Importantly, beautiful work from many groups has suggested discoveries. We posit, however, that a more robust and facile
that tRNA levels are not static, but rather dynamic in nature in meanstosequencetRNAswouldacceleratethisareaofresearch.
bothnormalanddiseasestates.Gingoldetal.showedthatdistinct Herein we present Quantitative Mature tRNA sequencing
tRNA pools associate with proliferative mammalian cell states (QuantM-seq), a simple high-throughput tRNA sequencing
2 NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
protocol utilizing commercially available reagents. In HEK293 of mapping quality (MAPQ) scores per read (Supplementary
cells,wefirstshowedthatQuantM-seqishighlyreproducibleand Fig.1a,b).ReadswereeitherMAPQ=0,orrangedfromMAPQ
representative of tRNA levels across a broad range of expression >10 to MAPQ<50, with increasing MAPQ indicating higher
levels,thusprovidingarobustsurveyofthetRNAtranscriptome. mapping confidence. In contrast with other RNA-seq protocols,
UsingQuantM-seq,wesurveyedtRNAtranscriptomesfrommice tRNAs are short, relatively repetitive, and highly modified and
and reveal the expression landscape is dramatically different thus prone to modification induced base misincorporation or
between tissue types. Fascinatingly, we see a strong CNS-specific truncation by RT23,29,30. Given these limitations inherent to
expression pattern for unique isodecoders. Moreover, the nature tRNAswhichwouldmanifestaslowermappingqualityrelativeto
of library production allows us to use sequence variant infor- other types of RNA-seq, we selected a MAPQ of greater than
mation as a means to approximate select tRNA modifications, 10 to calculate reads per million (RPM) per tRNA. Under the
and we observe tissue-specific nucleotide variants, highly sug- definition of MAPQ used by Bowtie2, this represents reads with
gestiveofmodifications,inparticularwithintheCNS,thatcould >90% probability of the correct mapping. Reproducibility
possibly affect isodecoder function/stability. Intriguingly, when betweenbiologicalreplicatesampleswasexcellentwithPearson’s
isodecoder levels are pooled bioinformatically, the anticodon R2=0.9999. Read length analysis revealed that while shorter
pools between distinct tissues is similar in sharp contrast to the readsarelesslikelytohaveaMAPQ>10(SupplementaryFig.1c,
vast differences observed in isodecoder expression. These results d), there is considerable mappability of all read lengths. These
suggest that strong anticodon buffering occurs, reducing the data show that recovery of truncated tRNA cDNAs via
expression of some isodecoders as others increase in expression. circularization coupled with optimized mapping parameters
The mechanism and consequence of this buffering is unclear. In allows us to include more tRNA reads. To complete these
total, we strongly feel that QuantM-tRNA-seq provides the analyses, we counted reads corresponding to individual tRNA
community with a quick and relatively easy means to robustly sequences and converted to RPM using established R packages
monitor tRNA levels and begin to explore potential tRNA (details in “Methods” and Supplementary Software)31.
modifications. Technologies such as these should greatly accel- Having shown that QuantM-seq is highly specific for tRNAs
erate our understanding of how tRNA influences normal and andreproducible,wenextsoughttoextensivelycross-validatethe
disease states. technique. Using total RNA isolated from HEK293 cells, we
assessed abundance covering ~46% of known tRNA isodecoders
(119 out of 256 unique tRNA sequences) by applying an
Results orthogonal hybridization-based approach (tRNA arrays)15.
High-throughput sequencing of mature tRNA by QuantM- Importantly, we utilized longer array probes antisense to full-
tRNA-seq. We developed QuantM-tRNA-seq (Fig. 1a) to assay lengthtRNAs(~70–80nt;SupplementaryData2).Longerprobes
the relative abundance of mature tRNA. To test the assay, we allow limitations inherent to short probe hybridization
utilized 1µg of total RNA from HEK293 cells. Taking advantage approaches to be
overcome32–34,
and the original study describ-
ofthe3′terminalC-C-AaddedtofunctionaltRNA,weoptimized ing tRNA arrays showed that these longer probes have
a splint ligation strategy to attach a complementary double- comparable hybridization efficiencies33. To further ensure that
stranded adapter to the 5′ and 3′ termini (Fig. 1a)27. Double- probe efficiencieswould besimilar, weselectedprobes ofsimilar
stranded adapter ligation is highly efficient (96% ligation effi- length,GCcontent,meltingtemperature,andstructurepotential
ciency), specific for tRNA in the predicted range of 65–95 and showed that none of these potentially confounding
nucleotides,anddependentonbothligaseandadapters(Fig.1b). characteristics correlated with probe signal from arrays (Supple-
WethenusedSuperScriptIVRTtogeneratecDNAduetoahigh mentary Data 2).
levelofprocessivityandthermostability.cDNAsynthesizedfrom We fixed 30 probes spanning the full-length of their cognate
ligatedtotalRNArevealedarangeofcDNAproducts;consistent tRNA species to a nylon membrane in order from highest
with extensive tRNA base modification and structure that can expressed by QuantM-seq to lowest expressed. As ligation of
inhibitRT.Notably,cDNAbandsshorterthanexpected forfull- double-stranded adapters was specific for tRNA and highly
length tRNA coincide with sites of highly modified bases known efficient (96%; Fig. 1b), we ligated radiolabeled adapter to total
toinhibitRT,T-loopm1A,andtheanticodonloop(Fig.1c)23.In RNA and hybridized to the tRNA probe array (Fig. 1d). tRNA
addition,asignificantamountoffull-lengthcDNAwasobtained. abundance as assessed byQuantM-seqcorrelated stronglyto the
This banding pattern was similar to DM-tRNA-seq with the array signal (mean Pearson correlation coefficient across
shortest truncated cDNA bands coinciding with m1A56–5923. replicates R2=0.75; Fig. 1e). As a control, we further validated
FollowingPAGEpurificationofallcDNAandsubsequentssDNA the array approach (ligation-dependent) by northern blot
circularization, libraries were minimally amplified with seven (ligation-independent) using 10 of the array probes spanning
cycles of PCR to add Illumina adapters and then subjected to therangeofarraysignalintensities.Thenorthernsignalforfull-
high-throughput sequencing on an Illumina platform. length tRNA and array intensities correlate strongly with a
For data analysis, reads were first subjected to adapter and PearsoncorrelationcoefficientofR2=0.92(Fig.1f),showingthat
CCAtrimmingfollowedbyalignmenttothehigh-confidenceset array signal derives largely from full-length tRNA. Together,
of human tRNA sequences annotated in gtRNAdb (Release 18; these results reveal that QuantM-seq provides comparable
hg38) with Bowtie2. Under default conditions in Bowtie2 local performance to hybridization approaches in assessing tRNA
mode, only reads that are 23 nucleotides or greater will map28. abundance.
However, Fig. 1c shows that we have a significant proportion of
~15 nucleotide reads likely generated by stalling of reverse
transcripase at m1A56–59 that would fail to map under default ComparisonofQuantM-seqwithestablishedtRNAsequencing
conditions23.Toensureallreadswereabletobemapped,weset protocols. Several other groups have previously developed high-
theminimumscorethresholdtoallowformappingofshortreads throughput tRNA-sequencing
methodologies23–25.
Each metho-
that are ten nucleotides or greater. dology utilizes different library preparation strategies with
Approximately 90% of reads mapped to gtRNAdb tRNAs, inherent biases and percentage of uniquely mapped reads. To
showing that the assay is very specific for tRNA. To select high- compareQuantM-seqtopreviouslypublishedprotocols,ourdata
confidence reads, for further analysis we first plotted histograms obtained from HEK293 cells were compared to publically
NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications 3
a
3’ AD
Annealed
5′ AD
R T
pri
mer
R T
pri
mer
adapters
G T 3′ 3′ 3′
A 3′ rG A TA TA
C rN C GC GC
5′ N C 5′ N C 5′G NN C 5′G NN C
Deacylation Ligation
*
Reverse QuantM-Seq
5′ Transcription
5′
R
*
R
d
3′ Circularization Truncated Amplification 1 2 3 4 5 6
F
A
F Sequencing
B
cDNA
C
Full length cDNA
D
3′
* E
b c
+
Rnl2 Ligase – – + + Rnl2 Ligase
+
Adapters – + + – total RNA
Total RNA + + + +
300nt full length
Ligated
cDNA product 100nt
tRNA product truncated
100nt 15nt product
RT adapter
Unligated
Adapters
Annealed
Adapters
e f
]tinU[
ytisnetni
yarrA
1 2 3 4 5 6
A
B
C
D
150nt E
1 2 3 4 5 6
75nt A
50nt B
35nt C
D
E
% Ligated 0 0 96 0
3e+06
4e+05
3e+05
2e+06
2e+05
1e+06
1e+05 R2=0.92
0
0
0 20,000 40,000 0 1e+05 2e+053e+054e+05
Northern intensity [Unit]
]tinU[
ytisnetni
yarrA
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
200nt
150nt
75nt
50nt
R2=0.75
Gene expression [RPM]
Fig.1QuantitativematuretRNAsequencing(QuantM-seq).aOutlineofQuantM-seq.tRNAdepictionsareinblack,adapterdepictionsareingreen,and
sequencescorrespondingtheRTprimeraredepictedinblue.TherGandrNattheendofthe5′ADindicateribonucleotides.bPolyacrylamidegelshowing
productsandefficiencyofadapterligationontotRNA.Rnl2:T4RNALigase2.Asterisk(*)indicates5Sand5.8SribosomalRNAbands.cPolyacrylamide
gelshowingproductsofreversetranscription(cDNA).Rnl2:T4RNALigase2.dImagesoftRNAarrays;eacharrayrepresentsanindependentreplicate.
FortheprobesspottedateachpositionseeSourceData.eScatterplotofreadspermillionderivedfromQuantM-seqversusarrayintensitiesderivedfrom
densitometrywithafittedlineartrendline.Shadedarearepresentsthe95%confidenceintervalofthelineartrendline.fScatterplotofnorthernblotversus
arrayintensitiesderivedfromdensitometrywithafittedlineartrendline.Shadedarearepresentsthe95%confidenceintervalofthelineartrendline.Source
dataareprovidedasaSourceDatafilefor(b–f).
4 NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
available datasets from two previously published protocols, toward longer reads or toward shorter reads respectively relative
Hydro-seq and DM-tRNA-seq. In addition, we performed to cDNA (Supplementary Fig. 2e, f). Since read length is an
YAMAT-seq in parallel with QuantM-seq on the same HEK293 important determinant of mappability, both kinds of skew are
cellRNA.Tocontrolforpotentialdifferencesinreadprocessing, likely to contribute to inaccurate tRNA expression values. These
all datasets were subject to the same read quality control and skewsarealsolikelyunderrepresentedastheGEOrecordforthis
alignment pipeline as QuantM-seq. technique lacks raw reads <16nt that would be generated by
As a foundation for assay comparison, we first plotted the anRTstallintheT-loop.Shortreadsdohavesomemappability
number of reads (depth of sequencing) from each dataset (Supplementary Fig. 1c, d),soloss ofthem alsorepresents aloss
(Supplementary Fig. 1e). The percentage of reads assigned to a ofinformation.Itisalsoimportanttonotethatgelpurificationof
particular tRNA with a mapping quality score > 10 is an tRNA alone significantly alleviated m1A58 stalling of RT (Sup-
important metric detailing the efficiency of each protocol. This plementary Fig. 2e, f). This raises the important question as to
percentagevariedgreatlyacrossprotocols(SupplementaryFig.1f). whether the poor recovery of highly structured, modified tRNA
The YAMAT-seq protocol produced the highest percent of from PAGE gels is introducing bias. Together, these analyses
assigned reads at 87.4% of total reads. Hydro-seq had the lowest reveal minimal length bias from cDNA to sequencing reads in
percentageofassignedmappedreadswithameanof15.7%across QuantM-seq compared to DM-tRNA-seq.
three replicates of low coverage libraries. Gogakos et al. (Hydro- WhileitwasclearfromDM-tRNA-seqthatAlkBdemethylase
seq)24conductedasecondexperimentdramaticallyincreasingthe treatmentcouldalleviatesomestallingofRTattheT-loop23,the
number of reads (>100M reads) for a single replicate, and this impact on quantitative power was less clear. To test if
resulted in an increased percentage of assigned reads (Supple- demethylase treatment could improve QuantM-seq, we treated
mentary Fig. 1f; Hydro_HC). Interestingly, the percentage of HEK293 total RNA with a commercial demethylase preparation
assignedreadsforlibrariespreparedbyDM-tRNA-seqincreased prior to performing QuantM-seq. Spike-in of 5 Escherichia coli
as the authors included more steps during library preparation. tRNA to these libraries revealed QuantM-seq linearity over ~3.5
Thepercentageofassignedreadsforlibrariespreparedfromtotal orders of magnitude from ~20 to 100,000 RPM (Supplementary
RNAincreasedwithdemethylasetreatmentfrom52.4%to61.3%. Fig. 3a). Demethylase treatment resulted in a reduction in reads
Gel purification of tRNA prior to demethylase treatment and ending in the T-loop and an increase of reads that ended in the
librarypreparationincreasedthispercentageto80.3%.However, anticodon and D-loops, suggesting alleviation of stalling at
it is important to note that DM-tRNA-seq assigned read methylgroupsintheT-loopasseenbyothers23.However,similar
percentages are likely inflated due to the fact that short reads to DM-tRNA-seq (Supplementary Fig. 2d), QuantM-seq expres-
lessthan16nucleotideswereexcludedfromtheGeneExpression sion values with or without demethylase treatment were highly
Omnibus (GEO) record. Comparatively, 44.0% of QuantM-seq correlated (Supplementary Fig. 3c). Further, demethylase treat-
total reads were assigned to mature tRNA sequences. ment did not dramatically change correlation between QuantM-
While QuantM-seq performs modestly with regards to read seq expression values and tRNA arrays (Supplementary Fig. 3d;
assignment to annotated tRNAs, the real question is how it R2=0.71), showing that demethylase treatment has minimal
performs relative to other techniques. Since YAMAT-seq was effects on our ability to quantitate tRNAs.
performed by us on the same RNA from HEK293 cells and Lastly, we were able to predict an expected nucleotide
Hydro-seq was performed on RNA from the same cells grown frequency across the CircLigase ligation junction as we engi-
under the same conditions24, we compared these techniques neeredtwodegenerate(N)baseswith25%representationofeach
directly to QuantM-seq. YAMAT-seq and Hydro-seq exhibited base at the extreme 5′ end of the reverse transcription primer
weaker correlations to tRNA arrays (R2=0.43 and 0.38, (Fig.2e;leftpanel).Wealsoknewexpectednucleotidefrequency
respectively; Fig. 2a, b) compared to QuantM-seq (R2=0.75; for the majority of cDNA 3′ ends, as the shortest cDNA
Fig. 1e). This is also reflected in weak correlation between these correspondstoRTstallatm1A23andfull-lengthcDNAendinT,
three techniques (Fig. 2c). Comparison of the distribution of andweknowtheirrelativeproportionfromcDNAgels(Fig.2d).
mean RPM of 256 individual tRNA sequences revealed potential Comparingthepredictedligationjunctionsequence fromcDNA
explanations for the disparity in expression values. Thirty of the todsDNAlibrarydeterminedbyBioanalyzerlengthdistributions
256 cytosolic tRNA genes detected reproducibly by QuantM-seq to actual reads reveals minimal sequence bias introduced by
were not detected by YAMAT-seq (Supplementary Fig. 2a). In cDNA purification, CircLigase ligation, PCR, and sequencing
addition, YAMAT-seq showed higher variability between repli- (Fig.2e,compareallpanels).Weattemptedtoperformthesame
catesandageneralunderrepresentationofmosttRNAsequences analysis for DM-tRNA-seq for the sake of comparison, however,
relative to both QuantM-seq (Supplementary Fig. 2a) and tRNA the lack of short reads (<16 nt) in the GEO record prevented us
arrays (Fig. 2a). Compared to QuantM-seq, Hydro-seq also from performing these calculations.
showed higher variability between replicates (Supplementary
Fig. 2c) and both over and underrepresented tRNAs relative to
QuantM-seq (Supplementary Fig. 2b, c) and tRNA arrays tRNA anticodon pools are moderately regulated between tis-
(Fig. 2b). sues in mice. Having developed and extensively validated a
sensitivehigh-throughputsequencingassayfortRNAexpression,
we set out to explore differences in mammalian tRNA expres-
QuantM-seqexhibitsminimallengthandsequencebias.tRNA sion. Previous studies outlined in Dittmar et al. and Gingold
expression inferred from QuantM-seq cannot be directly com- et al. using tRNA arrays suggested the presence of discrete
pared to DM-tRNA-seq as this assay was performed on RNA expression profiles of tRNA across different tissues14,15. We
isolated from HEK293T cells. However, we were able to assess obtained seven tissues from C57BL/6J wild-type mice in tripli-
length bias in both techniques going from cDNA to sequencing cate including four tissues derived from the central nervous
reads. For QuantM-seq, length of cDNA inferred from cDNA system (cortex, cerebellum, medulla oblongata, and spinal cord)
gels,dsDNAlibrariesbyBioanalyzer,andsequencingreadstrack and three non-CNS tissues (heart, liver, and tibialis skeletal
closely, indicating that CircLigase and PCR are not introducing muscle). Total RNA was isolated from each tissue and tRNA
appreciablelengthbias(Fig.2d).Incontrast,DM-tRNA-seqreads libraries were generated using QuantM-seq (Fig. 1a). Following
from total RNA or purified tRNA exhibited significant skew the same read processing pipeline as the HEK293 libraries, we
NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications 5
e
1
0.8
0.6
0.4
0.2
0
N 5′ N 3′
Position
aligned reads to high-confidence mouse tRNA genes annotated to cytosolic tRNA genes are relatively consistent across tissues
in gtRNAdb Release 18. The reproducibility of biological repli- with minor differences found only in heart (Fig. 3a). Interest-
catesampleswasveryhighatanaverageofr=0.97orhigherfor ingly, the contribution of mitochondrial tRNA genes to total
each tissue (Supplementary Fig. 4b). A cursory analysis of the gene expression is dramatically higher in the heart compared to
high-confidencereadsrevealedthecontributionofcytosolicand all other tissues assayed (Fig. 3a, b).
mitochondrial tRNA genes to total reads differed significantly As previous studies had assessed tRNA expression largely at
between heart and all other tissues. Surprisingly, reads mapped theanticodonlevel,the210cytosolictRNAisodecodersmeasured
ycneuqerf
eidtoelcuN
a b
6e+05
4e+05
2e+05
0e+00
0 50,000 100,000 150,000 200,000
YAMAT-seq expression [RPM]
d
cDNA Library
1 1 1
0.8 0.8 0.8
0.6 0.6 0.6
0.4 0.4 0.4
0.2 0.2 0.2
0 0 0
N 5′ N 3′ N 5′ N 3′ N 5′ N 3′
CircLigase
ligation
]tinU[
ytisnetni
yarrA
4e+05
3e+05
2e+05
1e+05
0e+00
0 20,000 40,000 60,000
QuantM QuantM
Rep1 Rep 2
]tinU[
ytisnetni
yarrA
YAMAT-seq Hydro-tRNAseq
R2=0.43 R2=0.38
Hydro-seq expression [RPM]
0.4
0.3
0.2
0.1
0.0
egatnecreP
pool
T
pool
CA
pool
D
LF
1 1 0.51 0.25 0.23 0.33 0.5 0.5 QuantM-seq
YAMAT-seq cDNA
1 1 0.51 0.25 0.23 0.33 0.5 0.5 dsDNA
Reads
0.51 0.51 1 0.53 0.52 0.62 0.55 0.55 Hydro-seq HC
0.25 0.25 0.53 1 0.99 0.98 0.4 0.4
0.23 0.23 0.52 0.99 1 0.98 0.4 0.4 Hydro-seq
0.33 0.33 0.62 0.98 0.98 1 0.45 0.45
0.5 0.5 0.55 0.4 0.4 0.45 1 1
QuantM-seq
0.5 0.5 0.55 0.4 0.4 0.45 1 1
qes-TAMAY CH
qes-ordyH
qes-ordyH qes-MtnauQ
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
c
Correlation of tRNA-seq methodologies (Pearson)
6 NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
Fig.2ComparisonofQuantM-seqwithothertRNA-seqprotocols.aScatterplotofreadspermillionderivedfromYAMAT-seqversusarrayintensities
derivedfromdensitometrywithafittedlineartrendline.Shadedarearepresentsthe95%confidenceintervalofthelineartrendline.bScatterplotofreads
permillionderivedfromHydro-tRNA-seqversusarrayintensitiesderivedfromdensitometrywithafittedlineartrendline.Shadedarearepresentsthe95%
confidenceintervalofthelineartrendline.cPearsoncorrelationcoefficientsbetweentRNAgene-levelexpressionforeachdataset.Hydro-seqHCdenotes
thehighcoveragelibraryfromref.24.dBarchartdepictingtheaveragepercentageofcDNA,dsDNA,orreadsrepresentingreversetranscriptasestallingor
fall-offintheT-loop,anticodon(AC)loop,D-loop,orattheendoftRNA(fulllength;FL).ValueswerecalculatedfromcDNAgel,Bioanalyzertrace,orreads
respectivelyforN=2biologicalreplicatesinHEK293cells.eSequencelogosshowingthefractionofDNAbasesnearCircLigaseligatedbasesasinferred
fromcDNAgels(cDNA)orBioanalyzertrace(Library),orcalculatedfromreads(QuantMRep1andQuantMRep2).See“Methods”fordetailed
calculations.SourcedataareprovidedasaSourceDatafile.
by QuantM-seq were summed by their respective anticodon between CNS (blue) and non-CNS (green and red) tissues with
sequence into the 47 genomically encoded anticodon classes. each tissue co-localizing with other members of their respective
Differential anticodon class expression across tissues was CNS or non-CNS groups. Furthermore, correlation of all
analyzed using the established R package DEseq2 (details in cytosolicgenesrevealedstronginterclusterandweakintracluster
“Methods” and Supplementary Software)35. Intriguingly, minor correlation of CNS and non-CNS group members (Fig. 4e).
differences occurred between tissues at the level of anticodon
expressionwithasignificantdecreaseinThr-TGTtRNAsinliver
Isodecoders underlying anticodon pools differ across tissues.
compared to all other tissues (11-fold-change and padj=6.7E
Precedinganalysesindicatethatwhileanticodonpoolsarelargely
−22; Fig. 3c). Consistent with this, multidimensional scaling of
unchanged across tissues, the isodecoder pools that comprise
the tRNA expression matrix showed high similarity between anticodon pools differ significantly between CNS and non-CNS
tissues (Fig. 3d). These findings suggest that tRNA anticodon
tissues. Next, we wanted to determine how individual tRNA
pools are relatively stable across these seven tissues.
isodecoderscontributetotheconsiderablymorestableanticodon
expressionlevelsacrosstissues.Asmentionedpreviously,wefirst
tRNA isodecoders differ dramatically between tissues. Given summed the RPM for each tRNA gene decoding a particular
the similarity of tRNA expression profiles at the anticodon level, codon, and calculated an RPM per anticodon for each of the
wenextwantedtoelucidatethepotentialregulationofindividual seven tissues (n=3). From this, we calculated the percentage
tRNA isodecoders across tissues. We performed differential contribution of each tRNA gene for the 47 genomically encoded
expression analysis of tRNA isodecoders across all tissues using anticodon groups. Examples from anticodon classes with differ-
DESeq2(detailsin“Methods”andSupplementarySoftware)35.Of entially expressed isodecoders revealed remarkable differences in
the 210 detected tRNAs, 41% (86 genes) of genes differed sig- percent contribution of constituent tRNA genes across tissues.
nificantly in expression level between the seven tissues (padj< TheRPMofArginineTCTtRNAsvariedlessthantwofoldacross
0.01). Interestingly, a heatmap of differentially expressed iso- tissues (Fig. 5a). However, the previously defined CNS-specific
decodersrevealedCNSandnon-CNS-associatedtissuesclustered isodecoder, Arg-TCT-4-1, contributed to 6% of total Arginine
with strikingly similar expression profiles across the four CNS- TCTRPMintheCNS,and~0.03%innon-CNStissues(Fig.5b).
associated tissues (Fig. 4a). Differential expression analysis was Despite the relatively small contribution of Arg-TCT-4-1 to the
performed following grouping of the four CNS tissues (cortex, Arginine TCT pool, mutation of this tRNA had dramatic effects
cerebellum, medulla oblongata, and spinal cord) and three non- on CNS-related phenotypes36, suggesting functional differences
CNS tissues (heart, liver, tibialis). The expression levels of 57 between isodecoders.
genes differed significantly between CNS-associated tissues and To determine the contribution of the newly identified CNS-
non-CNS-associated tissues (27% of all isodecoders) (Fig. 4b). specific isodecoders to the Alanine TGC anticodon class, we
The most significant of these differentially expressed genes is a calculatedthemeanRPMbytissue(Fig.5c)andfoundamarginal
knownCNS-specificisodecoderforArginine,Arg-TCT-4-1,with decrease(<2-fold)inheartrelativetoothertissues.Weidentified
142-fold enrichment across CNS tissues compared to the three asimilarpatternforthepercentageofcontributiontotheAlanine
non-CNS tissues (p<1E−200) (Fig. 4b, c). This isodecoder was TGC anticodon class for our newly identified set of three CNS-
identified previously as CNS-specific and having a CNS-specific specific isodecoders. Ala-TGC-5-1, Ala-TGC-6-1, and Ala-TGC-
function in translation36. In addition to identification of this 7-1 contribute ~20% of mean RPM for the Alanine TGC
previously reported CNS-specific tRNA isodecoder, we report a anticodon across all CNS tissue classes (Fig. 5d). Interestingly,
novel set of highly CNS-enriched Alanine TGC isodecoders these three isodecoders contribute <2% of mean RPM in non-
includingAla-TGC-5-x,Ala-TGC-6-1,andAla-TGC-7-x(Fig.4b, CNS associated tissues.
c). Similar to Arg-TCT-4-1, all three genes were found to be SimilartotherelativelystableexpressionofArg-TCTandAla-
greatlyenrichedat8,15,and40-foldintheCNS-associatedtissue TGCanticodonsacrosstissues,thenon-CNStissueenrichedGly-
group,respectively(p=1.3E−27,1.7E−115,2.8E−87).Themost GCC-2-x isodecoder did not result in dramatic tissue-specific
significantisodecoderthatisenrichedfourfoldinnon-CNStissue changes in Glycine GCC anticodon expression (Fig. 5e). Inter-
is Glycine GCC-2-x (p=3.4E−48; Fig. 4b). In total, 28 iso- estingly,theaveragepercentagecontributionoftheGly-GCC-2-x
decoders (13% of all isodecoders) exhibited a statistically sig- isodecoderenrichedinnon-CNSassociatedtissuesis14%innon-
nificant (p<0.01) greater than threefold enrichment in the CNS CNSversus4%inCNStissues(Fig.5f).Furtheranalysisofheart
relative to non-CNS tissues (Fig. 4c). versus other tissues revealed a heart-specific increase in Gly-
Multidimensional scaling of isodecoder expression reveals the GCC-1-xisodecoderscontributingtoahigherpercentageoftotal
seventissuesinthisstudyaredissimilarfromoneanother.Most RPM for the Glycine-GCC isoacceptor class (66% average in
CNStissuesclustertogetherwithpotentialoutliersrepresentedby heart vs. 35% in all other tissues).
samples isolated from one cortex and several CNS tissues from These findings indicate that while anticodon pools do not
animal 3 (Fig. 4d). These could represent real individual drastically change across tissues, the isodecoders that comprise
differences or technical variability in tissue harvesting. Never- thesepoolsoftendochange.Theseresultsarehighlysuggestiveof
theless, the distance matrix clearly illustrates the differences an unknown mechanism that buffers the overall amount of
NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications 7
CCXB33
MO3
T3
H1
L2LL31 CS ST M CC C1XC ST O B22 B C 1 2 2 12 3 H H 3 2 MO1
CX1
77.0
32.0
38.0
71.0
38.0
71.0
18.0
91.0
38.0
71.0
18.0
91.0
87.0
22.0
38.0
71.0
97.0
12.0
38.0
71.0
68.0
41.0
58.0
51.0
78.0
31.0
78.0
31.0
88.0
21.0
26.0
83.0
36.0
73.0
16.0
93.0
18.0
91.0
38.0
71.0
78.0
31.0
a
100
75
50
25
Mean total mitochondrial counts by tissue (n=3)
0
c d
Anticodon expression
tnecreP
b
Distribution of tRNA counts cyto
mito
xetroC mullebereC atagnolbO
.M
droC
lanipS
reviL traeH silaibiT
xetroC mullebereC atagnolbo
.M
droc
lanipS
reviL traeH silaibiT
Log10 counts
Trp CCA
Ile TAT
Gly CCC
Gly GCC
Ile AAT
Ala TGC
Val TAC
Arg CCT
Ser CGA Ser GCT
Arg CCG iMetCAT
Gly TCC Arg TCT
Val CAC Lys CTT
Leu CAG
Leu CAA Thr AGT Met CAT Pro TGG Arg TCG Thr CGT Glu CTC Ala AGC
Asp GTC
Asn GTT
Ser TGA
Arg ACG
Pro CGG Glu TTC
Val AAC Leu TAA
SeC TCA Lys TTT
Thr TGT Gln CTG
Leu AAG
C H y i s s G GC TG A S P e ro r A A G G A G Ser GGA
Gly ACC
sMPR
naeM
xetroC mullebereC atagnolbo
.M
droc
lanipS
reviL traeH silaibiT
Mean total cytosolic counts by tissue (n=3)
sMPR
naeM
xetroC mullebereC atagnolbo
.M
droc
lanipS
reviL traeH silaibiT
10
0
10
10 0 10 MDS1 27.7%
%6.22
2SDM
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
7.5e+05
5.0e+05
2.5e+05
0
4e+05
3e+05
2e+05
1e+05
0
2 0 2 4 Anticodon level MDS plot
Ala CGC
Leu TAG
Phe GAA
Tyr GTA
Gln TTG
Sup TCA
Sup TTA
Fig.3tRNAanticodonpoolsaresimilaracrossmousetissues.aBarchartwithcentershowingthemeancytosolictRNAreadspermillion(top)and
mitochondrialtRNAreadspermillion(bottom)acrosssevenmousetissues.ErrorbarsrepresentthestandarddeviationofN=3biologicalreplicates.
bStackedbarchartsshowingthepercentageofreadsfromeachlibrarythatcorrespondtoeithercytoplasmictRNAormitochondrialtRNA.ctRNAreads
werecollapsedbyknownanticodongroups,log transformed,andthenplottedasaheatmap.dTableusedtogenerate(c)wasusedtocreatea
10
multidimensionalscalingplottoexaminethedistancebetweentissueswithregardstotRNAexpressionattheanticodonlevel(EuclideanDistance).CNS
tissuesarelabeledinshadesofblue,non-CNSmuscletissuesareinred,andthenon-CNSliverisingreen.
8 NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications
a b
DE tRNA genes (n=50)
d e
anticodons to offset tissue-specific changes in isodecoder to210tRNAgenes,wereliablydetected3026basesthatexhibited
expression. greater than 1% variation across all tissue samples, which indi-
cates that 18.8% of the total bases detected by QuantM-seq
represent sites of potential modification (Fig. 6a). This subset of
tRNA sequence variants differ across tissues. tRNAs contain a variants generally exhibited intratissue reproducibility (Pearson’s
high density of posttranscriptional base modification when r) greater than 0.85 (Supplementary Fig. 5a).
compared to all other RNA classes with an average of 13 mod- Next, we asked whether variant bases changed across tissues
ifications per transcript6. Many of these modifications are abso- using DEXseq (details in “Methods”). We defined differential
lutely essential for normal tRNA stability and function37. Of the variantsasbaseswhoseadjustedpvaluewaslessthan0.01andan
over 100 identified base modifications found in tRNA, some are absolute fold-change in variant frequency greater than 1.5. This
known to induce stalling and base misincorporation by RT, revealed 244 (8%) potential modified bases which vary signifi-
causing reproducible variation in cDNA products such as trun- cantlyinouranalysis.Giventheextensivesecondaryandtertiary
cations and mutations10,23,38. Taking advantage of this relation- structure required for normal function of mature tRNA, we set
ship,weperformedanalysestoaskwhetherwecandetectvariants out to determine if these significant variant bases were enriched
that indicate tRNA post-transcriptional base modification. We in particular structural regions. We found a great proportion of
defined variants as the number of 5′ truncations (putative RT the significant variants to center around the TψC-loop, the
stalls) or mutations at a given base divided by the total read anticodon loop, the entire D-arm, and the 5′ region of the
coverageatthatbase.Outof16,093distinctbasescorresponding acceptor stem (Fig. 6b). Consistent with these findings,
xetroC mullebereC atagnolbo
.M
droc
lanipS
reviL traeH silaibiT
Log10 counts
log10(padj)
egnahc
dlof
2gol
c
CNS/non-CNS fold-change
Differential expression in CNS vs. non-CNS 00 22 44 66 88 11001122
Ala-AGC-1-1
Ala-AGC-10-1
Ala-AGC-3-1
Ala-AGC-5-1;5-2;5-3
Ala-CGC-3-1;3-2;3-3
Ala-TGC-5-1;5-2;5-3
Ala-TGC-6-1 15
Ala-TGC-7-1;7-2 40
Ala-TGC-8-1
Arg-TCT-4-1
Gly-CCC-2-1;2-2
Gly-CCC-3-1
Lys-TTT-2-1;2-2
Lys-TTT-3-1
Met-CAT-4-1
Thr-AGT-6-1
Thr-CGT-3-1
Thr-CGT-4-1
Thr-TGT-1-1
Val-AAC-2-1;2-2
Val-AAC-3-1
Val-AAC-4-1
Val-CAC-1-1
Val-CAC-3-1
10
fe
o
0
c
ro
C
10
10 0 10
MDS1 25.9%
%6.91
2SDM
7.5
0 1 2 3 4 5 ArgTCT41
5.0 AlaTGC71;72
AlaTGC61 142
Glu-TTC-3-1;3-2
ThrAGT61
2.5
His-GTG-1-1
Leu-TAA-3-1
0.0 Ser-GCT-5-1
GlyGCC21;22;23;24;25;26;27;28
–2.5
0 25 50 75 100
Gene level MDS plot
H2
H1H3
T3T2 T1
L1 L2
L3
CB3
CX3 CB1 CX1 MO3 SMC C M C O3S XB OC 222 S12 C1
3_silaibiT 1_silaibiT 2_silaibiT 3_reviL 2_reviL 1_reviL 3_traeH 1_traeH 2_traeH 3_atagnolbo_alludeM 1_droc_lanipS 2_droc_lanipS 3_droc_lanipS 1_xetroC 2_mullebereC 1_mullebereC 3_mullebereC 2_xetroC 3_xetroC 2_atagnolbo_alludeM 1_atagnolbo_alludeM
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
Medulla_oblongata_1
Medulla_oblongata_2
Cortex_3
Cortex_2
1 Cerebellum_3
Cerebellum_1
Cerebellum_2
0.95 Cortex_1
Spinal_cord_3
Spinal_cord_2
0.90 Spinal_cord_1
Medulla_oblongata_3
Heart_2 0.85 Heart_1 Heart_3 Liver_1
Liver_2
Liver_3
Tibialis_2
Tibialis_1
Tibialis_3
Fig.4tRNAisodecoderschangeacrossmousetissues.aHeatmapoflog -transformedtRNAisodecoderexpressionforisodecodersthatsignificantly
10
changeacrosstissues(p<0.01).Hierarchicalclusteringwasusedtogroupisodecoderexpressionalongthey-axis.bThevolcanoplotofallisodecoders
fromthecomparisonofallsampleslumpedintotwobins:CNS(cortex,cerebellum,medullaoblongata,spinalcord)versusnon-CNS(liver,heart,tibialis).
Isodecoderswithapvalueof0.01orlessarecoloredred.Highlysignificant,tissue-specificisodecodersarelabeledwiththeirnames.cIsodecodersthat
exhibitpadj<0.01andCNS/non-CNSfold-change>3aredepicted.dTheexpressionmatrix(RPM)usedtogenerate(a)wasusedtogenerateadistance
matrixandmultidimensionalscalingplottoexaminethedistancebetweentissueswithregardstotRNAexpressionattheisodecoderlevel.CNStissuesare
labeledinshadesofblue,non-CNSmuscletissuesareinred,andthenon-CNSliverisingreen.ePearsoncorrelationcoefficientsbetweentRNA
isodecoderexpressionprofilesofalltissueswereplottedasaheatmap.Hierarchicalclusteringwasusedtogrouptissuesalongthexandyaxes.
NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications 9
a b
Percentage Arg−TCT by gene
Corte
C
x erebell
M
u m
.
oblonga
S
ta
pinal
cord Liver Heart Tibialis
c d
0
Corte
C
x erebel
M
lu m
.
oblongata
Spinal
cord Liver Heart Tibialis
e f
100
75
50
25
0
tnecreP
Corte
C
x erebel
M
lu m
.
oblongata
Spinal
cord Liver Heart Tibialis
Cort
C
ex erebel
M
lu m
.
oblongat
S
a
pinal
cord Liver Heart Tibialis
Corte
C
x erebel
M
lu m
.
oblongata Spinal cord Liver Heart Tibialis Cort
C
ex erebel
M
lu
.
m oblongat
S
a pinal cord Liver Heart Tibialis
naeM
Mean total counts Arg−TCT by tissue (n=3)
100
75
50
25
0
tnecreP
Gene
naeM
Mean total counts Ala−TGC by tissue (n=3)
100
75
50
25
tnecreP
Percentage Ala−TGC by gene
Gene
naeM
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
20,000
15,000
Arg−TCT−1−1
Arg−TCT−2−1
Arg−TCT−3−1
10,000 Arg−TCT−4−1
Arg−TCT−5−1
5000
0
15,000
Ala−TGC−1−1
Ala−TGC−2−1;3−1 10,000
Ala−TGC−4−1
Ala−TGC−5−1;5−2;5−3
Ala−TGC−6−1
Ala−TGC−7−1;7−2
Ala−TGC−8−1
5000
0
Mean total counts Gly−GCC by tissue (n=3) Percentage Gly−GCC by gene
9000
Gene
Gly−GCC−1−1;1−2;1−3
Gly−GCC−2−1;2−2;2−3;
2−4;2−5;2−6;2−7;2−8
6000 Gly−GCC−3−1
Gly−GCC−4−1
3000
0
Fig.5Isodecoderpoolscomprisinganticodonpoolsdifferacrosstissues.BarchartswithcentershowingmeantotalArg-TCT(a),Ala-TGC(c),orGly-
GCC(e)readspermillionacrossmousetissues.ErrorbarsrepresentthestandarddeviationofN=3biologicalreplicates.Stackedbarchartsfor
percentageofeachisodecodercontributingtothepoolofArg-TCT(b),Ala-TGC(d),orGly-GCC(f)acrossmousetissues.Barchartswithblueshading
representsexamplesofanticodonpoolswithCNS-enrichedisodecoders.Redshadingrepresentsanexampleofananticodonpoolwithnon-CNS-enriched
isodecoders.
10 NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications
# of Bases % Total
Total 16,093 100
Coverage > 1% 3,026 18.8
padj < 0.01 CX1
244 1.5
FC > 1.5
CCBB12
T2
SC1 TT31
MO1CX2
SC2 L3 H2
SC3 H3
L2
MMOO32 L1 H1
CCBX33
Ala-TGC-4-1
Ala-TGC-5-1,5-2,5-3
Ala-TGC-6-1
tnuoc
tnairaV
metS
rotpeccA
′5
eglub
rotpeccA
mra-D
′5
pool-D mra-D
′3
egniH mra-CA
′5
pool-CA
′5
)CA(
nodocitnA
pool-CA
′3
mra-CA
′3
egnih mra-CψT
′5
pool-CψT mra-CψT
′3
mets
rotpeccA
′3
pool
elbairaV
a c
20
10
b
0
−10
−20
−20 −10 0 10 20
MDS1 − 43.8%
d e
Cortex
Cerebellum Ala-TGC variant frequency (n=57)
M. oblongata
3′
Spinal cord A
Liver C
C
Heart 5′
Tibialis
1 10 20 30 40 50 60 70
Cortex
Cerebellum
TψC A57
A56
M. oblongata
D
Spinal cord
Liver Freq
Heart 6
5
Tibialis
4
1 10 20 30 40 50 60 70 3
Anticodon 2
34 35 36 1
0
Cortex
Cerebellum
M. oblongata
Spinal cord
Liver
Heart
Tibialis
1 10 20 30 40 50 60 70
%7.61
−
2SDM
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
Anticodon variant counts padj < 0.01
& fold change >1.5 (n=244)
60
40
20
0
Fig.6VariantsinsequencingchangeacrosstissuesintRNAregionsknowntobemodified.aTabulationofQuantM-seqvariantanalyses.Total
representsthetotalnumberofbasesingtRNAdbmousetRNAs.Coverage>1%representsthenumberofbasesthathaveavariantfraction(variantcount
/readcoverage)ofatleast1%acrossalltissuesamples.Thelastrowrepresentsbasesthatareatleast1%variantfraction,changewithpadj<0.01(Two-
tailed,Benjamini–Hochberg),andexhibitanabsolutefold-changeof>1.5acrossmousetissues.bHistogramofsignificantlychangedtRNAbasesacross
seventissuesinmouse.AllvariantbasesarebinnedbytRNAfeatures.cMultidimensionalscalingplotindicatingdistancebetweentissuesampleswith
regardstodifferentialvariantfractionsacrosstissues(Euclideandistance).CNStissuesarelabeledinshadesofblue,non-CNSmuscletissuesareinred,
andthenon-CNSliverisingreen.dHeatmapsforthreeisodecodersrepresentingvariantfractionsateachtRNAposition(x-axis)acrosseachtissue
sample(y-axis).Thenumbersbelowtheplotindicatenucleotideposition.eTwo-dimensionalrepresentationoftheAla-TGCisoacceptorclassshowing
countsofdifferentialvariantsbyposition(n=11isodecoders).
NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications 11
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
modificationsitesarewelldocumentedinthesefourregionsthat extensively validated, this method exhibits minimal bias and
mediate tRNA interactions with elongation factors, aminoacyl improvesuponpreviouslypublishedmethodologies(Fig.2).This
tRNAsynthetases,ribosomalA,P,andEsites,aswellasdecoding was achieved with an efficient splint ligation strategy specific for
ofmRNA.Multidimensionalscalingofthe244significantvariant mature tRNA transcripts containing a 3′ C-C-A, and a cDNA
frequencies revealed that tissues cluster into CNS and non-CNS circularization strategy negating the need for transcript frag-
tissues. This suggests differential regulation of variants between mentationorfull-lengthcDNAsynthesisbyRT.Lastly,QuantM-
tissues (Fig. 6c). seqwasshowntohaveawidedynamicrangeandnottorequire
Given this intriguing finding, we set out to better understand demethylase treatment of RNA for tRNA expression analysis
therelationshipbetweendifferentialtRNAisodecoderexpression (SupplementaryFig.3).Insummary,QuantM-Seqoffersthebest
anddifferentialvariantfrequenciesbetweentissuesbyexamining balance between coverage of the tRNA transcriptome, sequence
some examples. Within the Alanine TGC isoacceptor class, we depth, limited bias, cross-validation by tRNA arrays, ease of use,
identified multiple isodecoders that exhibit differential variant and reducing the need for RNA gel purification. Compared to
frequencies. Two of these isodecoders which are differentially other published methodologies, QuantM-tRNA-seq also greatly
expressed between tissues, Ala-TGC-5-x and Ala-TGC-6-1, also reduces the number of PCR amplification cycles necessary for
show multiple sites of differential variant frequencies between reproducible library preparation with a comparable amount of
tissues (Fig. 6d), including at position 56, a likely site of m1A. input material. In the future, this may allow for reduced input
Interestingly, an isodecoder which only modestly changes tRNA-seq where sample material may be limiting.
expression between tissues less than twofold, Ala-TGC-4-1, also To highlight the utility of QuantM-tRNA-seq, we assessed
exhibits differential variant frequencies comparable to the two tRNA expression across seven mouse tissues at multiple levels:
isodecoders previously mentioned. This presents an unexpected overall anticodon pools, tRNA isodecoder pools, and potential
findingsuggestingsignificantvariantsarenotexclusivelyfoundin differencesinnucleotidemodificationindirectlyassessedbyread
differentially expressed tRNA genes. variant analysis. Broadly speaking, anticodon pools changed
To illustrate how this might impact the entire Ala-TGC modestly across tissues (Fig. 3) while isodecoders that comprise
anticodonpool,wepresentthedistributionofsignificantvariants anticodon pools (Figs. 4 and 5) and nucleotide modifications
forthe 11isodecoders in theAlanine TGCisoacceptorclass as a (Fig.6)exhibitedtissuespecificity.Consistentwithourworkhere,
consensus two-dimensional structure (Fig. 6e). Of note is the Dittmar et al. detected differences in tRNA levels across human
enrichment of significant adenosine variants at positions 56 and tissues15. However, a major limitation of these first generation
57. Adenosine residues at positions 55–59 in the TψC-loop are tRNAarraysistheinabilitytodistinguishisodecodersthatdiffer
methylated ubiquitously across all mature tRNA genes in all byonlyafewbasesandsomeanticodonpools.Forexample,these
isoacceptorclasses.Themethylationatcarbon-1formsmethyl-1- arrays could not distinguish Arg-CCG and Arg-TCG anticodons
adenosine (m1A), which represents one of the most well but instead sum them together as one signal. In addition, many
characterized tRNA modifications with known regulatory func- isodecoders including the CNS-specific Arg-TCT and Ala-TGC
tions37. Importantly, variants over A56 are shown to be m1A, as we detected are unable to be distinguished by these probes.
demethylase treatment of RNA from spinal cord causes a loss of Interestingly, the differences we detect reveal discrete sig-
CNS-specific variant signal (Supplementary Fig. 5b). Together, natures of isodecoder expression and nucleotide modification
theseanalysesrevealthatQuantM-seqcanalsobeusedtoexplore sitesthatareheavilyCNS-enriched.Ofparticularnote,QuantM-
tRNA modifications across biological systems. tRNA-seqrevealedCNSenrichmentofatRNAgene,Arg-TCT-4-
1, which was previously identified as CNS-specific, offering
independent external validation of the protocol in two different
Discussion isogenicmouselines36.MutatedArg-TCT-4-1inC57/Blackmice
Historically, tRNAs have been difficult to sequence due to base predispose these mice to neurodegenerative phenotypes, indi-
modificationsand extensivestructures whichimpedefirst-strand catingfunctionalimportancedespitethisCNS-specificisodecoder
synthesis by RT. To circumvent these issues, the few published comprisingonly6%oftotalArg-TCTtRNAsintheCNS(Fig.5).
methodsemploycleveranddiverselibrarypreparationstrategies. Our analyses also revealed a novel set of 27 tRNA isodecoders
However, each protocol has limitations. YAMAT-seq exhibits enriched in CNS tissue representing several anticodon classes
variability between technical replicates for some tRNAs and (Fig. 4). Further analysis of sequencing variants revealed that
underrepresents many tRNAs. Hydro-seq exhibits improved CNS-enriched Ala-TGC tRNAs also exhibit tissue-specific mod-
coverage of the tRNA transcriptome compared to YAMAT-seq, ification patterns. Specifically, each isodecoder exhibits sig-
butlowcorrelationtotRNAarrayssuggeststhateachofthesetwo nificantly increased variation at A56 in the CNS (Fig. 6) that is
methodsofferlimitedquantitativepower(Fig.2).DM-tRNA-seq alleviatedbydemethylasetreatment(SupplementaryFig.5).This
utilizes TGIRT-mediated template switching, a step known to baseresidesintheTψC-loop,iscommonlymodifiedwithmethyl
introducebias26,exhibitslengthbiasofsequencingreadsrelative groups(m1A),andisthoughttoinfluencetRNAstabilityandthe
to cDNA, and exhibits poor correlation between different abilitytoparticipateintranslation37.Ithasbeendetectedinother
implementations (Supplementary Fig. 2). Two iterations of DM- tRNA-seq as it causes significant RT stalling/mutation23. It is
tRNA-seq implement tRNA purification from PAGE gels, a step tempting to speculate that the increased expression of these iso-
thatmayaddbiasaswell.Importantly,thesetechniqueswerenot decodersislinkedtohigherm1A56methylation,possiblythrough
rigorouslyassessedforbiasnorwerethetRNAexpressionvalues increasedtRNAstability,butmoreworkneedstobedone.Toour
derived from them cross-validated. knowledge this is the first known documentation of both novel
Here we present a high-throughput sequencing method, CNS-specific isodecoders beyond Arg-TCT-4-1 as well as
QuantM-tRNA-seq, for assessing the expression level of mature potential regulation of m1A56 modification across tissues.
tRNA transcripts with isodecoder-level resolution. QuantM- Perhapsoneofthemoststrikingfindingsweobservehereinis
tRNA-seq was subject to rigorous validation with orthogonal that while isodecoder expression can be quite distinct between
hybridization-based approaches accounting for 119 of the 256 tissue types, the overall decoding potential (based on summed
measured tRNA genes in HEK293 cells offering high-confidence anticodons) is relatively uniform. The observation of stable
the data generated using this method accurately represents rela- anticodonpoolsrelativetodifferentialisodecoderexpressionand
tive tRNA abundance in samples (Fig. 1). In addition to being modifications suggests two very interesting, non-mutually
12 NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
exclusive hypotheses. First, isodecoder sequence differences solutionindHO)at60°Covernight.Membraneswerewashedfor5minin2×
2
commonly occur in regions that RNA Pol III contacts for SSC,0.1×SDSthreetimes,then0.5×SSC,0.1×SDSfor60min.Allwasheswere
initiation. It is possible, therefore, that isodecoder genes are dif- performedat60°C.Membraneswereexposedtoastoragephosphorscreenfor15
minandanalyzedonanAmershamTyphoon.
ferentially transcribed in different tissues. In this scenario, the
largenumberofisodecodergenesservestobufferanticodonpools
in a given tissue through reciprocal upregulation and down-
InvitrotranscribedtRNAspike-inpreparation.FivematuretRNAsequences
derivedfromE.colitRNA(gtRNAdbv8)werepurchasedasgBlocks(Integrated
regulation of tRNA gene families at the transcriptional level.
DNATechnologies;SupplementaryData1)withaHepatitisdeltavirus(HDV)
Second,ithasbeensuggestedthatisodecodersmayhavedifferent ribozymesequenceatthe3′endofthesequencetogenerateapreciseCCA3′end.
activitiesandthatuniquemodificationsinfluencestabilityand/or gBlockswereamplifiedusingtheQ52×mastermix(NEB)andtheT7FandHDV
function12,37.Thus,whilethelevelofanticodonsbetweentissues RprimersinSupplementaryData1accordingtothemanufacturer’ssuggested
conditions.Designofthetranscriptswasinaccordancewithpreviouslypublished
appears uniform, the a priori assumption that the decoding protocols39.Amplificationproductsoftheappropriatelengthwerepurifiedfrom
potential is identical could be incorrect. The contribution of nativeagarosegelsstainedwith0.05%EtBrusingtheQiaQuickgelextractionkit
unique isodecoders to decoding potential may be distinct based (Qiagen).Upto1µgofdouble-strandedtemplateDNAwasaddedtotheHiScribe
on tissue-specific differences. These hypotheses warrant further T7HighYieldRNAsynthesiskit(NEB)andtranscribedaccordingtothemanu-
facturer’ssuggestedconditions.TheHDVcleavagereactionoccursspontaneously
investigation. With the ability to easily quantify tRNA at the
inthereactionconditionsrequiredforinvitrotranscription.ThecleavedtRNA
anticodon,isodecoder,andvariantlevels,QuantM-tRNA-seqwill productwasthenpurifiedfromadenaturingpolyacrylamidegelusingthecrush
be an essential tool for future studies aimed at testing these andsoakmethod.Removalofthe2′,3′-cyclo-phosphategrouponthe3′endofthe
importantideasandprobingtRNAbiologyinmuchmoredetail.
purifiedtRNAproductwasperformedbyT4polynucleotidekinase(NEB).The
repairedtRNAproductwasquantifiedusingaQubitfluorometerandindividual
tRNAspeciesweremixedtocoverapproximately3.5ordersofmagnitude.
Methods Appropriatemixingofthespike-inmixwasassessedwithaQubitFluorometer
CellcultureandRNAisolation.HEK293T-RexFlp-INcells(ThermoFisher.cat# (ThermoFisher)andBioanalyzer(Agilent).Seventeennanogramsofcontrol
R78007)wereculturedat37°Cwith5%CO incompleteDulbecco’smodified tRNAswerespikedinto1µgoftotalRNAfromHEK293totalRNAtreatedwith
2
essentialmedia(ThermoFisher)supplementedwith10%fetalbovineserum demethylase.
(ThermoFisher)and1%penicillinandstreptomycin(ThermoFisher).Allpas-
s
fa
a
c
g
t
i
u
n
r
g
er
w
’s
as
su
p
g
e
g
r
e
f
s
o
t
r
e
m
d
e
c
d
on
w
d
it
it
h
io
t
n
ry
s.
p
F
si
o
n
ll
(
o
T
w
h
in
er
g
m
p
o
as
F
s
i
a
s
g
h
i
e
n
r
g
)
,
a
c
c
e
c
ll
o
s
rd
w
i
e
n
r
g
e
t
p
o
la
t
t
h
e
e
d
m
at
an
25
u
%
- QuantM-tRNA-seqlibrarypreparation.TotalRNAsampleswerequantified
confluencyin10cmtissueculturetreateddishesandculturedfor48–72huntil usingananodropspectrophotometer(ThermoFisher)priortolibrarypreparation
~90%confluent.At90%confluency,mediawasaspiratedand1mLoficecold a
re
n
m
d
o
R
v
N
e
A
3′
in
co
te
n
g
j
r
u
i
g
ty
at
w
ed
as
a
c
m
he
in
c
o
ke
a
d
c
o
id
n
s,
a
t
1
o
.
t
2
a
%
lR
d
N
en
A
at
w
ur
a
i
s
n
d
g
e
f
a
o
c
r
y
m
la
a
t
l
e
d
d
eh
a
y
t
d
3
e
7
a
°
g
C
aro
fo
s
r
egel.To
p T a r r h o iz o c o e m l ss o ( i T g n e h g n e . e r R m o N u o s A F s i o w s l h a u e s t r io i ) s n w o . l a a S s t a e a m d d p d ac l e e c d s o t r w o d e i t r n h e g e s c t t o u o l r t m e u d a re n in u an fa T d c r t m i u zo r i e x l r e a ’ d s t o p − n r 8 o i 0 t c o e ° c C f o o l u r w n 3 i t 0 t i h l s f t t u o w rt o a h s 7 e su r 5 r % e a 4 t 5 a m fi in n u al te c s o i n n ce d n e t a r c a y ti l o at n io o n f b 1 u µ ff g e / r µL (fi . n W al h c e o re nc in en d t i r c a a t t i e o d n ,d 20 ea m cy M lat T ed ris to -H ta C l L RN pH A = wa 9 s .0)
treatedwithdemethylase(rtStarTMtRNA-optimizedFirst-StrandcDNASynthesis
e
d
t
i
h
st
a
i
n
lle
o
d
lw
H
as
O
he
a
s
n
f
d
oll
s
o
to
w
r
i
e
n
d
g
a
i
t
so
−
pr
8
o
0
p
°
a
C
no
u
l
n
p
ti
r
l
e
l
c
i
i
b
p
r
i
a
t
r
a
y
tio
p
n
re
.
p
S
a
a
r
m
at
p
io
le
n
s
.
wereresuspendedin Kit,ArrayStar)andcleanedupperthemanufacturer’sinstructions.Onemicro-
2 gramofdeacylatedtotalRNAfromeachsamplewassubjecttolibrarypreparation.
Tenpicomoleofthe3′and10pmolofthe5′single-strandedadaptermix(2.5pmol
TissuesamplepreparationandRNAisolation.Allmousetissuesampleswere ofeachadapter5′-TGrGrA-3′,5′-TGrGrT-3′,5′-TGrGrG-3′,5′-TGrGrC-3′;Sup-
isolatedfrom31to37-day-oldfemaleC57B/6Jmiceusingproceduresapprovedby plementaryData1)wereaddedtoa200µLthin-walledamplificationtubeand
thePsychoGenicsInstitutionalAnimalCareandUseCommittee(IACUC).Sam- denaturedat95°Cfor2min.Thenannealingbufferwasaddedtoafinalcon-
pleswerereceivedondryice,andstoredaswholetissueat−80°C.Sampleswere centrationof5mMTris-HCl(pH8.0),0.5mMethylenediaminetetraaceticacid
thawedoniceand1mLofTrizolwasaddedper100mgofdissectedwholetissue. (EDTA),and10mMMgCl andincubatedat37°Cfor15mintohybridizethe
2
Onice,samplesweremasticatedandpassedthroughsuccessivelyhighergaugesof annealeddouble-strandedadaptertotRNA.Theligationreactionwascatalyzedby
needlestoensureahomogeneousmixture.Sampleswerestoredat−80°Cuntil 5U/µLofRNAligase2(NEB)withthemanufacturer’ssuggestedconditionsat37°
furtherprocessing.RNAwasisolatedaccordingtothemanufacturer’ssuggested Cfor60minthen4°Cat60min.Allreactionswereethanolprecipitatedwith
conditionswithtwo75%ethanolwashesfollowingisopropanolprecipitation. glycoblue(ThermoFisher)followedbytwo75%ethanolwashes,thensuspendedin
SampleswereresuspendedindistilledH 2 Oandstoredat−80°Cuntillibrary 10µLofdH 2 O.Followingligation,synthesisofcDNAbeganwithhybridizationof
preparation. theRTprimertotheligatedtotalRNAwithafinalconcentrationof0.5pmol/µL
(10pmoltotal).Thesampleswereincubatedat70°Cfor2minandtemperature
wasreducedto37°Cby0.1°C/s.SynthesisofcDNAwasachievedusingSuper-
Northernblotting.TotalRNA(500ng)wasseparatedona7Murea6%dena-
t m u e ri m ng br p a o n l e ya (G cr E yl L am ife id S e ci g e e n l c a es n ) d th tr e a n n fi sf x e e r d re b d y o c n r t o o ss a -li H nk yb in o g n i d n -N aU + V ny S l t o r n ata tr li a n n k s e f r er 2400 s s c y r n i t p h t e I s V is, a R t N 5 A 5° w C a f s o h r y 6 d 0 ro m ly in ze . d T w o i r th em a o fi v n e a D lc N on A c - e R n N tr A ati d o i n m o e f rs 0. f 1 ol N low N i a n O g H cD in N d A H 2 O
at98°Cfor20min.Allreactionswereethanolprecipitatedwithglycoblue(Thermo
usingtheauto-crosslinkbuttontwice.Theblotswerehybridizedat60°Cfor12h
Fisher)followedbytwo75%ethanolwashes,thensuspendedin12µLofdHO.
in2×SSC(1×SSCis0.15MNaCland0.015Msodiumcitrate),0.1%sodium 2
dodecylsulfate(SDS),and10×Denhardt’ssolutionwith32P-endlabeledprobes cDNAlibrarieswereseparatedusing7Murea6%denaturingpolyacrylamidegels.
specificforthefull-lengthtRNAtranscript(72–76nucleotides;Supplementary Gelswerestainedwith1×SYBRgold(ThermoFisher)in1×TBEfor15minand
regionsrepresentingtRNAderivedcDNAswereexcisedonaUVlightbox.Gel
Data1and2).Aftertwowashes(each)in2×SSC,0.1%SDSfor20minatroom
sliceswereshearedthroughthebottomofa0.5mLtubenestedina1.7mLtubeby
temperatureand0.5×SSC,0.1%SDSfor60minat60°C,themembranewas
centrifugationthensuspendedin400µLofDNAelutionbuffer(300mMNaCl,10
exposedtoastoragephosphorscreenfor15minandanalyzedonanAmersham mMTris-HCl(pH=8.0),1mMEDTA),incubatedondryicefor30min,and
Typhoon.
allowedtoincubateatroomtemperatureovernightonastandingrotator.cDNA
wasisopropanolprecipitatedwithglycobluefollowedbytwo75%ethanolwashes
tRNAarray.100nanogramsofeachprobe(SupplementaryData1and2)sus- thenwasresuspendedin12µLofdHO.CircularizationofcDNAlibrarieswas
2
pendedin0.5×TBEwasaspiratedontoaHybond-N+nylontransfermembrane performedwithCircLigase(Epicentre)at0.5U/µLusingthemanufacturer’ssug-
(GELifeSciences)witha96-wellmanifoldundervacuum.TheprobeswereUV gestedconditionsat60°Cfor1h.Thereactionwasterminatedwithincubationat
cross-linkedtothemembraneasabove.Arrayswerestoredat4°Cin0.5×TBEfor 80°Cfor20min.Allreactionswereethanolprecipitatedwithglycobluefollowedby
futureuse.Radiolabelingofthedouble-strandedadapterswasachievedby two75%ethanolwashes,thensuspendedin12.5µLofdHO.cDNAlibrarieswere
2
annealing10pmolofthe3′adapterand10pmolofthe5′adaptermix(2.5pmol/µl amplifiedusingtheNEBnextUltraIIQ5next-generationmastermix(NEB)with
eachofthe5′-TGrGrA-3′,5′-TGrGrT-3′,5′-TGrGrG-3′,5′-TGrGrC-3′adapters)at themanufacturer’ssuggestedconditions.HEK293librarieswereamplifiedfor
72°Candreducingtemperatureto37°Cby0.1°C/s.Annealeddouble-stranded sevencyclesandmousetissuelibrariesamplifiedfor7–9cycles.Amplifiedlibraries
adapterswere32P-endlabeledby5U/µLofT4polynucleotidekinase(NEB)under weregelpurifiedfrom2%agarosegelsstainedwith0.05mg/mLethidiumbromide.
themanufacturer’ssuggestedconditions.Thereactionwasethanolprecipitated, Regionsofinterest(100–250bp)wereexcisedonaUVlightboxandpurifiedusing
ethanolwashed,andresuspendedindHO.Theentireradiolabeleddouble- theQiaquickgelextractionkit(Qiagen)takingcaretodissolvegelslicesatroom
2
strandedadapterreactionwasaddedto300ngofdeacylatedtotalRNAforligation. temperatureandusingalloptionalsteps.Alllibrarieswereethanolprecipitated
Theligationreactionwascarriedoutwith0.5U/µLofT4RNAligase2(NEB) withglycoblue(ThermoFisher)withtwo75%ethanolwashes,thensuspendedin
undermanufacturer’ssuggestedconditionsat37°Cfor60minthen4°Cfor60 10µLofdHObeforesubmittingforsequencing.Libraryconcentrationwas
2
min.Thereactionwasethanolprecipitatedwithglycoblue.500,000cpmofradi- assessedusingaQubit(ThermoFisher),qualitywasassessedonaDNAHS
olabeledadapter-ligatedtotaltRNAwashybridizedtothecross-linkedarray bioanalyzerchip(Agilent),andlibrarymultiplexingdirectedbyqPCR.Sequencing
membranein5mLofhybridizationbuffer(2×SSC,0.1%SDS,10×Denhardt’s wasperformedassingle-endreadsfor110cyclesonaNextSeq550(v2.5).All
NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications 13
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
libraryQC,multiplexing,andsequencingwascarriedoutbytheGenomicsCore theanalysespresentedinFig.6waswritteninPython.Allcodeisprovidedasa
FacilityoftheCWRUSchoolofMedicine’sGeneticsandGenomeSciences SupplementarySoftwarefile.
Department.
Received: 18 June2020; Accepted: 23July2020;
Readqualitycontrolandalignment.Readswerefirstprocessedtoremove5′
adaptersequencesusingcutadapt--cut2thencutadapt-gTCCAACTGGA-
TACTGGN-e0.2followedbycutadapt–aCCAGTATCCAGTTGGAATT-e0.2to
remove3′CCAandadaptersequences.CustomhumanormousetRNAreferences
weregeneratedbycollapsingidenticaltRNAsequencesfromgtRNAdbRelease18 References
hg38ormm10high-confidencematuretRNAfastafiles.Mappingofhumanor
1. Nirenberg,M.W.&Matthaei,J.H.Thedependenceofcell-freeprotein
mousereadswiththecorrespondingreferencewasdonewithbowtie2usingthe synthesisinE.coliuponnaturallyoccurringorsyntheticpolyribonucleotides.
parameters:--quiet--min-scoreG,1,8--local-D20-R3-N1-L10-iS,1,0.5. Proc.NatlAcad.Sci.USA47,1588–1602(1961).
Isodecoder-levelreadcounttablesforfurtheranalyseswereproducedbycounting
2. Phizicky,E.M.&Hopper,A.K.tRNAbiologychargestothefront.GenesDev.
readswithMAPQ>10overreferencetRNAsusingtheRsubreadpackage’sfea-
24,1832–1860(2010).
tureCountsfunctioninR.Anticodon-levelreadcounttableswerethencreatedby
3. Schaffer,A.E.,Pinkard,O.&Coller,J.M.tRNAmetabolismand
summingreadsfromallisodecoderswiththesameanticodon.Inadditiontoraw neurodevelopmentaldisorders.Annu.Rev.Genom.Hum.Genet.20,359–387(2019).
readcounttables,tablesofbothisodecoderandanticodon-levelRPMmappedread
valuesweregeneratedbydividingrawreadcounts*1,000,000bythenumberof 4.
a
P
m
an
in
g,
oa
Y
c
.
y
L
la
.,
ti
P
o
o
n
ru
an
ri
d
,K
b
.
ey
&
on
M
d.
ar
W
tin
il
i
e
s
y
,S
In
.
t
A
er
.
d
t
i
R
sc
N
ip
A
.R
sy
ev
n
.
th
R
e
N
ta
A
se
5
:
,
tR
4
N
61
A
–480(2014).
readsmapped. 5. Krutyholowa,R.,Zakrzewski,K.&Glatt,S.Chargingthecode—tRNA
modificationcomplexes.Curr.Opin.Struct.Biol.55,138–146(2019).
Differentialexpressionanalysis.Therawreadcounttablesatboththe 6. Pan,T.ModificationsandfunctionalgenomicsofhumantransferRNA.Cell
anticodon-levelandisodecoder-levelacrossallsevenmousetissuesdescribedinthe Res.28,395–404(2018).
previoussectionwerenextusedtoperformdifferentialtRNAexpressionanalysis. 7. Chan,P.P.&Lowe,T.M.GtRNAdb2.0:anexpandeddatabaseoftransfer
ThelikelihoodratiotestwasappliedtothesetablesusingDESeq2inRasdetailed RNAgenesidentifiedincompleteanddraftgenomes.NucleicAcidsRes.44,
inhttps://hbctraining.github.io/DGE_workshop/lessons/08_DGE_LRT.html D184–D189(2016).
(Command:DESeq(raw_count_table,test=“LRT”,reduced=~1))usingdefault
8. Agris,P.F.etal.Celebratingwobbledecoding:Halfacenturyandstillmuchis
settingsandpvalueadjustment(Benjamin–Hochbergcorrection).Downstream
new.RNABiol.15,537–553(2018).
datavisualizationandplottingwereperformedusingggplot2,gplots(heatmap.2), 9. Crick,F.H.Codon–anticodonpairing:thewobblehypothesis.J.Mol.Biol.19,
ggrepel,andggforceincustomRscripts. 548–555(1966).
10. Bornelov,S.,Selmi,T.,Flad,S.,Dietmann,S.&Frye,M.Codonusage
Variantanalysis.InordertoanalyzevariantsintRNAsequencingreads,acustom optimizationinpluripotentembryonicstemcells.GenomeBiol.20,119
PythonscriptwasusedtogeneratevariantcountsateachpositionineverytRNA (2019).
acrossallsevenmousetissues.Inbrief,bamfileswerereadintothescriptandthe 11. Graczyk,D.,Ciesla,M.&Boguta,M.RegulationoftRNAsynthesisbythe
CIGARstringandMDtagsforeachreadwereusedtotabulateeachmutation, generaltranscriptionfactorsofRNApolymeraseIII-TFIIIBandTFIIIC,and
insertion,ordeletionacrosseveryribonucleotidebaseofalltRNAinthemouse bytheMAF1protein.Biochim.Biophys.ActaGeneRegul.Mech.1861,
reference.Inaddition,5′endsofreadsinternaltotRNAwereusedtoinfersitesof 320–329(2018).
RTstallingorfall-off.Thesefourtypesofvariantsweresummedateachpositionof 12. Geslain,R.&Pan,T.FunctionalanalysisofhumantRNAisodecoders.J.Mol.
eachtRNAforatotalvariantcount,andthenareadcoverageateachpositionwas Biol.396,821–831(2010).
alsocalculated. 13. Hanson,G.&Coller,J.Codonoptimality,biasandusageintranslationand
Toidentifysignificantlychangedsequencingvariantsacrosstissues,we mRNAdecay.Nat.Rev.Mol.CellBiol.19,20–30(2018).
performedDEXseqanalysisontherawvariantcountstableinR.DEXseqwas 14. Gingold,H.etal.Adualprogramfortranslationregulationincellular
originallydevisedtoidentifyalternativeprocessingeventsinmRNA,butwe proliferationanddifferentiation.Cell158,1281–1292(2014).
reasonedthatco-transcriptionalsplicingissimilarinprincipletoRT-mediated 15. Dittmar,K.A.,Goodenbour,J.M.&Pan,T.Tissue-specificdifferencesin
misincorporation/stallingatRNAmodifications.Toensurerobustdetectionof
variantsthatchangeacrosstissues,weaddedtwoadditionalfilteringsteps.First,for
humantransferRNAexpression.PLoSGenet2,e221(2006).
16. Abbott,J.A.,Francklyn,C.S.&Robey-Bond,S.M.TransferRNAandhuman
agiventRNAbase,werequiredthatvariantpercentagebe>1%onaverageinevery
disease.Front.Genet5,158(2014).
tissue.Next,weonlyacceptedbase-levelvariantsthatchangedvariantpercentage 17. Goodarzi,H.etal.ModulatedexpressionofspecifictRNAsdrivesgene
atleast1.5-foldacrosstissues.Downstreamdatavisualizationandplottingwere expressionandcancerprogression.Cell165,1416–1427(2016).
performedusingggplot2,gplots,ggrepel,andggforceincustomRscriptsaswellas
18. Santos,M.,Fidalgo,A.,Varanda,A.S.,Oliveira,C.&Santos,M.A.S.tRNA
matplotlibincustompythonscripts.
deregulationanditsconsequencesincancer.TrendsMol.Med.25,853–865
(2019).
CalculationofnucleotidefrequenciesacrossCircLigasejunction.Foreachband 19. Zhang,Z.etal.GlobalanalysisoftRNAandtranslationfactorexpression
fromthecDNAgeldepictedinFig.2d,wecanreasonablyassumethatthemajority revealsadynamiclandscapeoftranslationalregulationinhumancancers.
ofthestallingresultingintheshortestcDNAendsinA(m1A)23.Wealsoknow
Commun.Biol.1,234(2018).
thatlongestfull-lengthcDNAwillendinT,asthe5′adapterendsinT.The
20. Kapur,M.,Monaghan,C.E.&Ackerman,S.L.RegulationofmRNA
shortestfull-lengthcDNA(without5′adapter)isalsolikelytoendinT,asthisis translationinneurons-Amatteroflifeanddeath.Neuron96,616–637(2017).
complementarytothediscriminatorbase,whichishighlyskewedtowardA40–42.
21. Fujishima,K.&Kanai,A.tRNAgenediversityinthethreedomainsoflife.
Forallotherminorbands,wedonotknowwhatbaseRTisstallingover,soour
Front.Genet.5,142(2014).
priorestimatewas25%foreachbase.Giventhesepriorparametersandthe
22. Goodenbour,J.M.&Pan,T.DiversityoftRNAgenesineukaryotes.Nucleic
a tr m ac o e u ( n S t o s u o r f c e e ac D h at c a D ), N w A e s c p a e n ci c e a s l f c r u o l m ate F a ig. p 2 re d d a ic n t d ed lib n r u a c r l y eo d t s i D de N f A req in ue o n u c r y B f i o o r an th al e yz 3 e ′ r 23. A Zh ci e d n s g R ,G es . . e 3 t 4 a , l 6 . 1 E 3 ffi 7– ci 6 e 1 n 4 t 6 an (2 d 00 q 6 u ) a . ntitativehigh-throughputtRNAsequencing.
p
of
os
t
i
h
ti
e
on
fir
d
st
ep
th
ic
r
t
e
e
e
d
b
in
as
F
es
ig
a
.
c
2
r
e
o
.
s
F
s
o
a
r
ll
re
re
a
a
d
d
s,
s.
wesimplycalculatednucleotidefrequencies Nat.Methods12,835–837(2015).
24. Gogakos,T.etal.Characterizingexpressionandprocessingofprecursorand
maturehumantRNAsbyHydro-tRNAseqandPAR-CLIP.CellRep.20,
Reportingsummary.FurtherinformationonresearchdesignisavailableintheNature 1463–1475(2017).
ResearchReportingSummarylinkedtothisarticle. 25. Shigematsu,M.etal.YAMAT-seq:anefficientmethodforhigh-throughput
sequencingofmaturetransferRNAs.NucleicAcidsRes.45,e70(2017).
Data availability 26. Xu,H.,Yao,J.,Wu,D.C.&Lambowitz,A.M.ImprovedTGIRT-seqmethods
forcomprehensivetranscriptomeprofilingwithdecreasedadapterdimer
Thedatathatsupportthisstudyareavailablefromthecorrespondingauthorupon
formationandbiascorrection.Sci.Rep.9,7953(2019).
reasonablerequest.Thedatasetsgeneratedduringand/oranalyzedduringthecurrent
27. Kurschat,W.C.,Muller,J.,Wombacher,R.&Helm,M.Optimizingsplinted
studyareallavailableintheNCBIGeneExpressionOmnibusrepositorywithaccession ligationofhighlystructuredsmallRNAs.RNA11,1909–1914(2005).
numberGSE141436.Sourcedataareprovidedwiththispaper.
28. Langmead,B.&Salzberg,S.L.Fastgapped-readalignmentwithBowtie2.Nat.
Methods9,357–359(2012).
Code availability 29. Kietrys,A.M.,Velema,W.A.&Kool,E.T.FingerprintsofmodifiedRNA
CodeusedtoperformtheanalysespresentedinFigs.1–5andallSupplementaryfigures basesfromdeepsequencingprofiles.J.Am.Chem.Soc.139,17074–17081
utilizedonlypublishedpackagesforRthataredetailedin“Methods”.Customcodefor (2017).
14 NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-17879-x
30. Potapov,V.etal.BasemodificationsaffectingRNApolymeraseandreverse Author contributions
transcriptasefidelity.NucleicAcidsRes.46,5753–5763(2018). O.P.,T.S.,andJ.C.conceivedandoptimizedQuantM-seq.O.P.performedallthe
31. Liao,Y.,Smyth,G.K.&Shi,W.TheRpackageRsubreadiseasier,faster, experiments.O.P.,S.M.,andT.S.conceivedandimplementedtheQuantM-seqanalysis
cheaperandbetterforalignmentandquantificationofRNAsequencingreads. pipelineandperformedthecomputationalanalyses.O.P.,T.S.,andJ.C.wrotebothdraft
NucleicAcidsRes.47,e47(2019). andfinalmanuscripts.T.S.andJ.C.supervisedthewholeproject.
32. Chou,C.C.,Chen,C.H.,Lee,T.T.&Peck,K.Optimizationofprobelength
andthenumberofprobespergeneforoptimalmicroarrayanalysisofgene Competing interests
expression.NucleicAcidsRes.32,e99(2004).
Theauthorsdeclarenocompetinginterests.
33. Dittmar,K.A.,Mobley,E.M.,Radek,A.J.&Pan,T.Exploringtheregulation
oftRNAdistributiononthegenomicscale.J.Mol.Biol.337,31–47(2004).
34. Liu,H.,Bebu,I.&Li,X.Microarrayprobesandprobesets.Front.Biosci.(Elite Additional information
Ed.)2,325–338(2010).
Supplementaryinformationisavailableforthispaperathttps://doi.org/10.1038/s41467-
35. Love,M.I.,Huber,W.&Anders,S.Moderatedestimationoffoldchangeand 020-17879-x.
dispersionforRNA-seqdatawithDESeq2.GenomeBiol.15,550(2014).
36. Ishimura,R.etal.RNAfunction.Ribosomestallinginducedbymutationofa CorrespondenceandrequestsformaterialsshouldbeaddressedtoT.S.orJ.C.
CNS-specifictRNAcausesneurodegeneration.Science345,455–459(2014).
37. Liu,F.etal.ALKBH1-mediatedtRNAdemethylationregulatestranslation. PeerreviewinformationNatureCommunicationsthankstheanonymousreviewersfor
Cell167,1897(2016). theircontributiontothepeerreviewofthiswork.
38. Clark,W.C.,Evans,M.E.,Dominissini,D.,Zheng,G.&Pan,T.tRNAbase
methylationidentificationandquantificationviahigh-throughputsequencing.
Reprintsandpermissioninformationisavailableathttp://www.nature.com/reprints
RNA22,1771–1784(2016).
39. Schurer,H.,Lang,K.,Schuster,J.&Morl,M.Auniversalmethodtoproduce Publisher’snoteSpringerNatureremainsneutralwithregardtojurisdictionalclaimsin
invitrotranscriptswithhomogeneous3’ends.NucleicAcidsRes.30,e56 publishedmapsandinstitutionalaffiliations.
(2002).
40. Lee,C.P.,Mandal,N.,Dyson,M.R.&RajBhandary,U.L.Thediscriminator
baseinfluencestRNAstructureattheendoftheacceptorstemandpossiblyits
interactionwithproteins.Proc.NatlAcad.Sci.USA90,7149–7152(1993). Open Access This article is licensed under a Creative Commons
41. Limmer,S.,Hofmann,H.P.,Ott,G.&Sprinzl,M.The3’-terminalend Attribution 4.0 International License, which permits use, sharing,
adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
(NCCA)oftRNAdeterminesthestructureandstabilityoftheaminoacyl
acceptorstem.Proc.NatlAcad.Sci.USA90,6199–6202(1993). appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreative
42. Wende,S.,Bonin,S.,Gotze,O.,Betat,H.&Morl,M.Theidentityofthe Commonslicense,andindicateifchangesweremade.Theimagesorotherthirdparty
discriminatorbasehasanimpactonCCAaddition.NucleicAcidsRes.43,
materialinthisarticleareincludedinthearticle’sCreativeCommonslicense,unless
5617–5629(2015). indicatedotherwiseinacreditlinetothematerial.Ifmaterialisnotincludedinthe
article’sCreativeCommonslicenseandyourintendeduseisnotpermittedbystatutory
regulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfrom
Acknowledgements thecopyrightholder.Toviewacopyofthislicense,visithttp://creativecommons.org/
WethankmembersoftheCollerlab,DanielFischer,andDrs.HarveyLodish,Peter licenses/by/4.0/.
Eimon,andHsinChenforimportantscientificdiscussionsrelatedtothiswork.Wealso
thankDr.AshleighSchafferforhelpfuldiscussion.Thisresearchwassupportedbythe
GenomicsCoreFacilityoftheCWRUSchoolofMedicine’sGeneticsandGenomeSci- ©TheAuthor(s)2020
encesDepartment.
NATURECOMMUNICATIONS| (2020) 11:4104 |https://doi.org/10.1038/s41467-020-17879-x|www.nature.com/naturecommunications 15
