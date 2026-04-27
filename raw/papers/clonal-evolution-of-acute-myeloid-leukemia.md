---
source_path: /mnt/c/Users/Administrator/Zotero/storage/BQHUWED5/Morita 等 - 2020 - Clonal evolution of acute myeloid leukemia revealed by high-throughput single-cell genomics.pdf
ingested: 2026-04-23
sha256: 0924ab1be0e1b046
---

ARTICLE
OPEN
https://doi.org/10.1038/s41467-020-19119-8
Clonal evolution of acute myeloid leukemia
revealed by high-throughput single-cell genomics
Kiyomi Morita 1,2,12, Feng Wang3,12, Katharina Jahn4,5,12, Tianyuan Hu6, Tomoyuki Tanaka1, Yuya Sasaki1,
Jack Kuipers4,5, Sanam Loghavi 7, Sa A. Wang7, Yuanqing Yan8, Ken Furudate1,9, Jairo Matthews1,
Latasha Little3, Curtis Gumbs3, Jianhua Zhang 3, Xingzhi Song3, Erika Thompson10, Keyur P. Patel7,
Carlos E. Bueso-Ramos7, Courtney D. DiNardo 1, Farhad Ravandi1, Elias Jabbour1, Michael Andreeff1,
Jorge Cortes 1, Kapil Bhalla1, Guillermo Garcia-Manero 1, Hagop Kantarjian1, Marina Konopleva 1,
✉ ✉
Daisuke Nakada 7, Nicholas Navin10,11, Niko Beerenwinkel 4,5 , P. Andrew Futreal 3 &
✉
Koichi Takahashi 1,3
Clonal diversity is a consequence of cancer cell evolution driven by Darwinian selection.
Precise characterization of clonal architecture is essential to understand the evolutionary
history of tumor development and its association with treatment resistance. Here, using a
single-cellDNAsequencing,wereporttheclonalarchitectureandmutationalhistoriesof123
acute myeloid leukemia (AML) patients. The single-cell data reveals cell-level mutation co-
occurrence and enables reconstruction of mutational histories characterized by linear and
branching patterns of clonal evolution, with the latter including convergent evolution.
Through xenotransplantion, we show leukemia initiating capabilities of individual subclones
evolving in parallel. Also, by simultaneous single-cell DNA and cell surface protein analysis,
we illustrate both genetic and phenotypic evolution in AML. Lastly, single-cell analysis of
longitudinal samples reveals underlying evolutionary process of therapeutic resistance.
Together, these data unravel clonal diversity and evolution patterns of AML, and highlight
their clinical relevance in the era of precision medicine.
1DepartmentofLeukemia,TheUniversityofTexasMDAndersonCancerCenter,Houston,TX,USA.2DepartmentofHematologyandOncology,Graduate
SchoolofMedicine,TheUniversityofTokyo,Tokyo,Japan.3DepartmentofGenomicMedicine,TheUniversityofTexasMDAndersonCancerCenter,
Houston,TX,USA.4DepartmentofBiosystemsScienceandEngineering,ETHZurich,Basel,Switzerland.5SIBSwissInstituteofBioinformatics,
Basel,Switzerland.6DepartmentofMolecularandHumanGenetics,BaylorCollegeofMedicine,Houston,TX,USA.7DepartmentofHematopathology,The
UniversityofTexasMDAndersonCancerCenter,Houston,TX,USA.8DepartmentofNeurosurgery,TheUniversityofTexasHealthScienceCenterat
Houston,Houston,TX,USA.9DepartmentofOralandMaxillofacialSurgery,HirosakiUniversityGraduateSchoolofMedicine,Aomori,Japan.10Department
ofGenetics,TheUniversityofTexasMDAndersonCancerCenter,Houston,TX,USA.11DepartmentofBioinformaticsandComputationalBiology,The
UniversityofTexasMDAndersonCancerCenter,Houston,TX,USA.12Theseauthorscontributedequally:KiyomiMorita,FengWang,KatharinaJahn.
✉
email:niko.beerenwinkel@bsse.ethz.ch;afutreal@mdanderson.org;ktakahashi@mdanderson.org
NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications 1
;,:)(0987654321
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
A
growing body of evidence supports the role of clonal
Table1Clinicalanddemographiccharacteristicsofthestudy
diversity in therapeutic resistance, recurrence, and poor cohort (N=123).
outcomes in cancer1. Clonal diversity also reflects the
historyoftheaccumulationofsomaticmutationswithinatumor.
Characteristics Median IQR
Thus, a precise characterization of clonal diversity reveals not
only the extent of a tumor’s clonal complexity but also the evo- WBC(×103/L) 8 3.5–30.0
lutionary history of the tumor’s development. Much of the work HGB(g/dL) 9.1 8.5–10.0
PLT(×103/μL) 55 29–86
characterizing the clonal architecture of tumors has been done
BMblasts(%) 46 30–67
by computational inference using variant allele fraction (VAF)
PBblasts(%) 27 5–57
d sa a m ta pl f e r s o 2 m –4. m H a o s w si e v v e e l r y ,t p h a e ra a l b le il l ity D t N o A inf s e e r q c u l e o n n c a i l n h g et o e f ro b g u e l n k eit t y um an o d r L A D g H e( ( y U ) /L) 6 6 8 1 9 4 52 7 – 8 7 – 3 1154
tumorphylogenyfrombulksequencingdataisinherentlylimited, No. %
because bulk sequencing techniques cannot reliably infer muta- Ontogeny
tion co-occurrences and hence often fail in accurately recon- Denovo 93 76
structing clonal substructure. Secondary/therapyrelated 30 24
Single-cellDNAsequencing(scDNA-seq)canaddresssomeof Priortreatment
these challenges5–9. However, until recently, the available meth- Untreated 88 72
odsrequiredlaborioussingle-cellisolationprotocolsandsuffered Treated 35 28
from low cell throughput, limited gene coverage, and technical Karyotype
artifacts from whole-genome amplification that hindered their Normalkaryotype 91 74
ability to characterize clonal architecture precisely10. Recent Complexkaryotype 12 10
technologicaladvancesinmicrofluidicsandmolecularbarcoding Others 20 16
Treatment
nowallowrapid single-cellgenotypingof targetedcancer-related
IA-basedchemotherapy 49 40
genes in thousands of cells. We previously described the perfor- AraC-basedchemotherapy 12 10
mance and feasibility of a scDNA-seq platform (Tapestri®, Mis- decitabineandvenetoclax 27 22
sion Bio, Inc.) in primary samples from two patients with acute HMAwithoutvenetoclax 24 20
myeloid leukemia (AML)11. Here, using this method, we con- Others 11 9
ductedscDNA-seqin154AMLsamplesfrom123patients.In26 Sex
of these patients, we have simultaneously profiled DNA and cell Female 48 39
surface proteins. Our study uncovered the landscape of AML
Abbreviations:IQRinterquartilerange,WBCwhitebloodcells,HGBhemoglobin,PLTplatelets,
clonal architecture at single-cell resolution and revealed clonal BMbonemarrow,PBperipheralblood,LDHlactatedehydrogenase,AMLacutemyeloid
relationships of AML driver mutations. Using the data, we leukemia,IAidarubicinandcytarabine,AraCcytarabine,HMAhypomethylatingagents.
reconstructed the mutational history of driver genes and
demonstrated linear as well as branching clonal evolution pat-
terns in AML. Simultaneous DNA and protein profiling enabled 4.8–7.0%) (Supplementary Fig. 3). The estimated lower limit of
genotype-to-phenotype correlation at single-cell resolution. In detection of the platform was 0.1% of the cellular population
addition, scDNA-seq of longitudinal samples in 15 patients based on the serial dilution assay of a cell line and also from
allowedillustrationofclonalevolutioninresponsetotherapeutic mutation validation by droplet digital polymerase chain reaction
selective pressures. (PCR) (Supplementary Table 2 and Supplementary Fig. 4).
Intotal,wesequenced735,483BMMCsfrom123AMLpatient
samples(Fig.1b).ThescDNA-seqapproachdetected543somatic
Results mutations in 31 cancer-associated genes, which included 388
The cellular-level landscape of driver mutations in AML. We (71%) single-nucleotide variants and 155 (29%) small
analyzed 154 samples of bone marrow mononuclear cells insertion–deletions (indels). Among these, 530 mutations (98%)
(BMMCs) from 123 AML patients, of which 88 (72%) were were orthogonally validated: 489 (92%) by conventional bulk-
previously untreated, and 35 (28%) had relapsed or refractory seq12 (median 397×), 29 (5%) by droplet digital PCR (ddPCR),
disease (clinical characteristics are summarized in Table 1). The and 12 (2%) by a quantitative PCR assay (all FLT3-internal
median bone marrow blasts percentage was 46% (interquartile tandem duplication [ITD]). Of the 13 unvalidated mutations, 3
range[IQR]:30–67%).Allsampleswereconcurrentlyanalyzedby were negative by ddPCR, and the remaining 10 were not tested
conventional bulk next-generation sequencing (bulk-seq) and duetothelackofremainingspecimens.Thesubsequentanalyses
scDNA-seq. Based on the mutation profiles of the samples used a final set of 530 validated mutations (Supplementary
determined by the conventional bulk-seq, scDNA-seq was con- Data 1). Of note, among the shared genomic regions covered by
ducted by one of the two targeted panels (Mission Bio’s prede- the scDNA-seq and the bulk-seq platforms, all mutations called
signed19genespanel[90samples,SupplementaryTable1]orby bythebulk-seqwerealsodetectedbyscDNA-seq.TheVAFfrom
a custom-designed panel interrogating 37 genes with recurrent bulk-seq(bulk VAF)andtheVAF inferredfromthescDNA-seq
mutations in cancer [64 samples, Supplementary Data 2], Sup- data(scDNA-seqVAF)wereingoodconcordance(r =0.84,p<
s
plementary Methods). A median of 6102 BMMCs (IQR: 0.001)suggestingthatthesequencedcellsarerepresentativeofthe
4066–7790) per sample were sequenced by the scDNA-seq plat- total bulk samples (Fig. 1c and Supplementary Fig. 5).
form (Fig. 1a). scDNA-seq resulted in a median of 48× coverage The most frequently detected mutations by scDNA-seq in the
perampliconpercell(IQR:23×–87×,SupplementaryFig.1).The 123 patients were in NPM1 (N=49, 40%), followed by FLT3
amplicons covering guanine–cytosine (GC)-rich sequences, such (N=47, 38%; 36 [29%] with ITD and 22 [18%] with non-ITD
as GATA2, SRSF2, and parts of RUNX1 and TP53, had lower
mutations),DNMT3A(N=45,37%),NRAS(N=45,37%),IDH2
coverage compared with other regions, such that relatively large (N=33, 27%), RUNX1 (N=25, 20%), SRSF2 (N=25, 20%),
numbers of cells had inconclusive genotype information for the TET2 (N=20, 16%), and KRAS (N=19, 15%). scDNA-seq
mutations covered by these amplicons (Supplementary Fig. 2). detectedsubstantiallymoreFLT3mutations(12[80%]ITDand3
Theestimatedmedianalleledropout(ADO)ratewas5.8%(IQR: [20%] non-ITD) than bulk-seq (Supplementary Fig. 6a). This is
2 NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications
rs = 0.84
(p < 0.001)
Ploidy: 2.02,aberrant cell fraction: 83%, goodness of fit: 99.6%
5 1 2 3 4 5 6 7 8 9 10 11 12 13 141516171819202122XY
4
3
2
likely due to the capability of the scDNA-seq platform in analysisisnecessaryfortheaccurateinterpretationofthezygosity
detectingcrypticFLT3mutationsinsmallcellularsubpopulations data from scDNA-seq.
(SupplementaryFig.6b),whichhasbeenreportedpreviouslyfora
different single-cell technology13.
scDNA-seq calls mutations in individual cells with zygosity Clonal relationships of AML driver mutations. Single-cell
state, which allows to observe additional layer of diversity. mutation data unambiguously revealed the cellular-level co-
However, the lack of the validation method in previous studies occurrence and mutual exclusivity among driver mutations.
has made the interpretation of zygosity difficult5. In the current Multiple different mutations (often subclonal) involving
cohort, we sought to validate the zygosity state by concurrently receptortyrosinekinase(RTK)/RasGTPase(RAS)/MAPKinase
performing single-nucleotide polymorphism (SNP) arrays in (MAPK) signaling pathway genes (FLT3, NRAS, KRAS,
selectedsamples.Wedetectedcopy-neutrallossofheterozygosity PTPN11, KIT, and MYC) were detected in the same patients,
(CN-LOH)insamples withcellshavinghomozygousFLT3-ITD, andtheywereoftenpresentinmutuallyexclusiveclonesatthe
RUNX1,andTET2mutations(Fig.1dandSupplementaryFig.7a, cellular level (Fig. 2a and Supplementary Fig. 8a). A similar
b), confirming that the observation of homozygously mutated mutually exclusive relationship was observed among other
cells in these samples was likely true and was as a result of CN- functionally redundant mutations (e.g., IDH1 and IDH2; TET2
LOH.Incontrast,noneofthesampleswithcellshomozygousfor and IDH, Fig. 2b, c and Supplementary Fig. 8b). TP53 and
SRSF2 or NPM1 (Supplementary Fig. 7b–d) mutations had copy PPM1Dmutations werealsofoundtobemutuallyexclusiveby
number alterations involving the mutated loci. These results do scDNA-seq (Fig. 2d). This is in contrast to the findings from
not rule out the possibility that SNP arrays failed to detect the previousbulk-seqstudiesthatshowedsignificantco-occurrence
subclonal allelic imbalance. However, the cells that were of the two mutations at the population level14,15. However,
genotyped as homozygous had significantly lower sequencing because of their functional redundancy in DNA damage
depth than did the cells that were genotyped as heterozygous responsepathway,thetrueco-occurrence(i.e.,cellular-levelco-
(Supplementary Fig. 7), suggesting that the homozygous calls in occurrence) between the two mutations has been debated. The
these mutations may have resulted from low sequencing depth resultfromthescDNA-seqisbiologicallymoreconsistentwith
and ADO. These results indicate that concurrent copy number the functional redundancy of the two mutations. DNMT3A,
fo rebmun
ypoc
elella
hcae
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
a b
12,000
c
d
1
0
Fig.1TheGeneticlandscapeofAMLbasedonsingle-cellDNAsequencing.aDistributionofthenumberoftotalsequencedcells.Eachpointrepresentsa
samplefromuniquepatients.bSomaticmutationsin735,483cellsfrom123AMLpatientsdetectedbysingle-cellDNAsequencing(scDNA-seq).Each
columnrepresentsacellattheindicatedscale,andcellsfromthesamecaseareclusteredtogetherwithintheareassurroundedbythegraylines.Cellsthat
weregenotypedasbeingmutatedorwildtypefortheindicatedgenearecoloredinblueandwhite,respectively.Cellswithmissinggenotypesarecolored
ingray.Whenonesamplehasmultipledifferentmutationsinthesamegene,theywereannotateddifferently(e.g.,DNMT3A_aandDNMT3A_b).Mutated
genesarecoloredbasedontheaffectedmolecularpathway(nucleophosmincoloredingreen,DNAmethylationinorange,RTK/RAS/MAPkinasepathway
inblue,JAK-STATpathwayinbrown,transcriptionfactorinred,chromatin/cohesininlightgreen,splicinginpink,andapoptosisinpurple).Atotalof
76,549cellsthatweregenotypedaswildtypeforallthevariantsscreenedarenotshown.cCorrelationofthevariantallelefraction(VAF)frombulk-
sequencingandscDNA-seq.Thex-axisshowstheVAFfromscDNA-seq(scDNA-seqVAF).They-axisshowstheVAFfromthebulksequencing(bulk
VAF).Eachdotrepresentsadetectedvariant.Thelinerepresentsalinearregressionline.Theshadedarearepresentsthe95%confidenceintervals.dA
representativecasewithhighlyhomozygousvariantinvolvingcopy-neutrallossofheterozygosity(CN-LOH).Heatmap(left)showsthegenotypeofeach
sequencedcellforeachvariant,withclusteringbasedonthegenotypesofdrivermutations.Eachcolumnrepresentsacellattheindicatedscale.Cellswith
homozygousmutation,heterozygousmutation,andwild-typecellsareindicatedinred,blue,andwhite,respectively.Cellswithmissinggenotypesare
indicatedingray.Theallelecountsdistributionisshowntotheright.Theallelecountisshownontheverticalaxis,andthechromosomesareshownonthe
horizontalaxis.Chromosome13involvinghighlyhomozygousFLT3-ITDishighlightedwithabluerectangle.Mut-Homohomozygouslymutated,Mut-
Heteroheterozygouslymutated,WTwildtype,Missingmissinggenotype.
NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications 3
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
a
log OR
FDR < 0.1
FDR < 0.05
FDR < 0.001
b
log OR
FDR < 0.1
FDR < 0.05
FDR < 0.001
c
log OR
FDR < 0.1
FDR < 0.05
FDR < 0.001
d
log OR
FDR < 0.1
FDR < 0.05
FDR < 0.001
e
Single-cell DNA sequencing Bulk sequencing
Fig.2Thecellular-levelmutualexclusivityofAMLdrivermutations.a–dCell-levelmutualexclusivitypatternsofdrivermutationsinindividualsamples
forfourrepresentativecases.aKRAS,NRAS,FLT3-non-ITD,andFLT3-ITD,bIDH1andIDH2,cIDH1p.R132C,IDH1p.R132H,andTET2,dTP53andPPM1D
variantsdidnotco-occurinthesamecellularpopulations.Mutmutated,WTwildtype,Missingmissinggenotype.Heatmaps(left)showthegenotypeof
eachsequencedcellforeachvariant,withclusteringbasedonthegenotypesofdrivermutations.Eachcolumnrepresentsacellattheindicatedscale.Cells
withmutationsandwild-typecellsareindicatedinblueandwhite,respectively.Cellswithmissinggenotypesareindicatedingray.Thesubcloneslocated
totherightoftheredlinecomprised<1%ofthetotalsequencedcells,andsuchsmallsubclonescanrepresentfalsepositiveornegativegenotypesasa
resultofalleledropoutormultiplets.Thefiguresontherightshowthepairwiseassociationofmutations.Thecolorandsizeofeachpanelrepresentthe
degreeofthelogarithmicoddsratio(logOR).ThebarontherightsideisakeyindicatingtheassociationofthecolorswiththelogOR.Co-occurrenceand
mutualexclusivityareindicatedbyredandblue,respectively.Thestatisticalsignificanceoftheassociationsbasedonthefalsediscoveryrate(FDR)is
indicatedbytheasterisks(*FDR<0.1,**FDR<0.05,***FDR<0.001).ePairwiseassociationofdrivermutationsinAMLbasedonsingle-cellDNA
sequencing(left)andbulksequencingdata(right).Foreachpairofmutations,theirdependencywassummarizedaslogOR,withpositivevalues(red)
indicatingadegreeofco-occurrenceandnegativevalues(blue)indicatingadegreeofmutualexclusivity.Thestatisticalsignificanceoftheassociations
basedontheqvalueisindicatedbythedotsandasterisks(**q<0.1,*q<0.01).
WT1, and TET2 were often found to carry two different provide cell-level evidence of mutation co-occurrence, which
mutations co-occurring in the same cells, which is consistent notonlyvalidatespreviousfindingsbybulk-sequencingstudies
with the previously reported biallelic involvement of these butalsocorrectspreviouslymischaracterizedrelationships(e.g.,
tumorsuppressorgenes(SupplementaryFig.8c)16–18.Pair-wise
TP53 and PPM1D).
analysis of mutation co-occurrence using pooled single-cell
data identified more significant co-occurrence and mutually
exclusive relationships among AML driver genes compared to Reconstructing evolutionary histories and mutation order. To
the same analysis using bulk-seq data from the same samples reconstruct evolutionary histories in individual AML, we used
(Fig. 2e). Taken together, these single-cell genotype data single cell inference of tumor evolution (SCITE), a probabilistic
4 NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
model to infer phylogenetic trees from single-cell mutation data of DNMT3A-ASXL1-STAG2-BCOR-U2AF1 p.Q84R-U2AF1 p.
that involves a flexible Markov-chain Monte Carlo (MCMC) S34F with NRAS p.G12S or KRAS p.Q61H, that were similar in
learningalgorithm19.SCITE-basedphylogeniesdemonstratedthe clonal size. Two PDX models were generated from this sample
sequence of mutation acquisition and distinct patterns of clonal (AML-67-001-PDX1 and AML-67-001-PDX2), and in both
evolution in AML including linear and branching models of models,we detectedclonalexpansion of theNRASp.G12Sclone
evolution (Fig. 3a–i). Among the 123 AML patients analyzed, andregressionoftheKRASp.Q61Hclone(Fig.4d).Intriguingly,
68 (55%) showed linear clonal evolution, whereas 55 (45%) similar clonaldynamics were observedin theactualpatient after
exhibitedbranchingclonalevolution(Fig.3aandSupplementary therapy, suggesting that clonal expansion in PDX models may
Fig. 9a). As expected, samples with branching evolution showed reflect the functional fitness of the subclones (Supplementary
significantlyhigherclonaldiversitycomparedtothosewithlinear Fig. 12).These data suggestthatscDNA-seq of PDXmodels can
evolution (median Shannon index 1.83 [IQR: 1.45–2.22] vs. 1.35 reconstruct the heterogeneity of LIC populations and their
[IQR: 1.00–1.57], p<0.001), whereas there were no significant functional fitness.
differences in other clinical characteristics between the two
models (Supplementary Fig. 9b). When we correlated the clonal
Single-cell mapping of genetic-phenotypic evolution in AML.
diversity index with clinical characteristics, we found a modest
p 0. o 2 s 1 it , iv p e = co 0 rr .0 e 2 la , tio S n up b p e l t e w m e e e n n t p ar a y tie F n i t g a . ge 9c a ) n . d I c n lon th al re d e ive c r a s s i e ty s (r w s i = th s T p u e o r r f f a o fu c r e r m th p e r e d o r t s e d i i m i n s s s u e ( l c t s a t c n D t e h N o e u A s i + n p t p r r r a o o - fi t t u e li i m n n g - o s r e o q f h ) e s i t i n e n r g 2 o l 6 e g - e A c n e M e l i l t L y D p N i a n t A ie A n a M t n s d L u , s c i w n el g e l
branching patterns, we found an evolutionary history that is
consistent with convergent evolution (Fig. 3g–i)20. For example, s th cD e N T A ap + e p st r r o i te p in la - t s f e o q rm was (F o ig rt . ho 5 g ). on I a m ll m y u v n al o id p a h t e e n d o b ty y pi c n o g nc d u a rr ta ent b ly y
in AML-38-001, a putative founding mutation, NPM1 p.L287fs, performed multi-color flow cytometry of the same samples
divergedintotwoindependentbrancheswithmutationsIDH1p.
(Supplementary Fig. 13, Methods). We assessed genotype-
R132H and IDH2 p.R140Q, respectively. Each of these branches
phenotype correlation across all sequenced cells (Fig. 5a). As
thenseparatedintoFLT3p.D835H,KRASp.G12A,orPTPN11p. expected,wild-typecellsweresignificantlyassociatedwithhigher
D61H mutated clones and FLT3-ITD, KRAS p.G12D, NRAS p. expressionofCD3(r =0.18,p<0.001)andCD19(r =0.04,p<
G12A, NRAS p.G13R, or PTPN11 p.A72G mutated clones, s s
0.001),suggestingthatmostofthesecellsrepresentnormalTand
respectively. As a result, the sample harbored 12 individual
Blymphocytes,respectively.WealsoobservedthatNPM1orIDH
clones, each with a combination of functionally similar, but mutations were significantly associated with lower expression of
separately evolved, molecular alterations (NPM1-IDH-RAS/RTK/ CD34(r =−0.29forNPM1,r =−0.16forIDH1,r =−0.07for
MAPKsignalingpathwayalteration,Fig.3i).Bycontrast,bulk-seq IDH2)an s dHLA-DR(r =−0.1 s 8forNPM1,r =−0. s 05forIDH1,
( d d S a e u fi t W a p n p h i f t r l i i e o l v e m m e e s m n t i h n t o a e g d r le y s e a - l c F m e o ig l e f l . c 1 c d o l 0 a o h a t n o a – a r d t l ) p o . e r f o vo v p i l a u d t t e i i e s o n n t m s w o w r i a t e h s d n t e o h fi t e n a i s b t a i l m v e e t e o m r p e o r s d o o e v lu l i s d ti e o o n a f r d w s a i = t t h a − a h r 0 i e . g 1 h c 4 e o r n fo s C r is D t I e D 3 n 4 H t 2 w e ) x i , t p h s w re h t s h e s e r io e p a n s re ( T v r i s P o = 5 u 3 s 0 m . fi 3 n 0 u d ) t i a n ( t a i g o s l s l n o s p f w < th e 0 r e . e 0 a 0 a s 1 s s ) o s . o c c T ia i h a ti t e o e s n d e
between these mutations and immunophenotypes22,23.
phylogeny and clonal architecture compared to bulk-seq data,
Using the data obtained from mutational history analysis, we
variability in sequencing coverage among cells and amplicons
then analyzed interplay between genetic and phenotypic evolu-
generates uncertainties. For example, poor sequencing coverage
tion in AML. In AML-103-001, TET2, U2AF1, DNMT3A, and
inSRSF2andotherGC-richampliconsresultedinrelativelylarge
NRASmutationswerelinearlyacquired(Fig.5b).Theanalysisof
numbers of cells with inconclusive genotype (Supplementary cellsurfaceproteinexpressionineachgenotype-definedsubclone
Fig.2),whichcanleadtoinaccurateinferenceofmutationorder
revealedthatTET2single-mutatedcellswereassociatedwithboth
and phylogeny. In such cases, we integrated bulk-seq data and
myeloidandlymphoidmarkers(CD3,CD19,CD22,andCD11b),
scDNA-seq data into consensus phylogenies using the B-SCITE
supporting the preleukemic origin of this mutation24. Double
algorithm21, suggesting complementarity between the two plat-
mutant (TET2-U2AF1) cells were still associated with these
forms (Supplementary Fig. 10e). We also incorporated the
markershoweverwithlowerextent,andalsoweremorestrongly
zygosity state into phylogeny modeling, which revealed the
associatedwithearlymyeloidmarkerssuchasCD123andCD13.
relativetimingofLOHeventsduringclonalevolution(Fig.3j,k).
Then, triple mutant (TET2-U2AF1-DNMT3A) cells were asso-
ciatedwithhematopoieticstemcellmarkers(CD34andCD117).
Finally, quadruple mutant (TET2-U2AF1-DNMT3A-NRAS) cells
Clonal diversity in AML leukemia initiating cells (LICs). We + + +
showed myeloblastic phenotype (CD33 , CD34 , and CD38 ,
then studied clonal diversity and architecture of AML leukemia
initiating cells (LICs), as defined by their ability to initiate (or b F y ig. fl 4 o c w ),w c h yt ic o h m w et a r s y co (F n i s g i . ste 5 n d t ). w S it i h m t i h la e rl o y b , se A r M ve L d - b 1 l 0 a 1 s - t 0 p 0 h 1 en h o a t d yp a e
regenerate) AML in immunocompromised mice, at single-cell
linear clonal structure with two different TP53 mutations and a
resolution. We xenotransplanted aliquots of three AML samples KRAS mutation (Fig. 5e). scDNA+protein-seq identified two
with highly branching clonal structure (AML38-001, AML-41- + +
001,and AML67-001)into immunodeficient mice (PDX: patient phenotypically aberrant populations: one with CD34 CD117
+ myeloblasts and another small population with monocytic
derived xenograft) and analyzed engrafted human CD45 cells differentiation (CD11b + CD64 + ) (Fig. 5f). Genotype–phenotype
using scDNA-seq (Fig. 4a and Supplementary Fig. 11a). While
correlation revealed that the cells with single TP53 mutation
regenerated AML had contracted diversity compared to the ori- + +
(TP53 p. V143M-mutant) manifested a CD34 CD117 pheno-
ginal bulk AML samples (Fig. 4b), it consisted of substantially
type, whereas double TP53 mutant cells (TP53 p. V143M and p.
diverse genetic populations (Fig. 4c, d and Supplementary
Y220C double mutant) were associated with a monocytic
Fig. 11b). For example, in AML-38-001, which exhibited con-
immunophenotype (Fig. 5g). These data illustrate a stepwise
vergentevolutionofmultipleAMLsubclones,11of12subclones
acquisition of driver mutations in the context of malignant
weredetectedintheengraftedsample(Fig.4c).Inaddition,AML
hematopoiesis hierarchy.
subclonesshowedvariableleukemiaregeneratingcapacity,which
mightreflectthefitnesslandscapeofAMLsubclones(Fig.4dand
Supplementary Fig. 11b). For instance, the original AML sample Illustratingclone-by-cloneresponsetoAMLtherapies.Wethen
from AML-67-001 showed two subclones carrying combinations analyzed 46 longitudinal samples from 15 patients (13 with
NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications 5
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
a b c d e
AML-80-001 AML-02-001 AML-28-001 AML-51-001
All patients
N = 123
Linear Branching
N = 68 N = 55
Divergent Convergent
N = 52 N = 3
f g h
AML-67-001 AML-61-001 AML-42-001
i
AML-38-001
j k
AML-25-001 AML-99-001
6 NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
Fig.3InferenceofmutationalhistoryinAML.aSummaryoftheclonalevolutionpatterns.Threeofthe55casesshowingbranchingevolutionpatterns
presentedconvergentevolutionpatterns.b–iInferenceofmutationphylogenybasedonthesingle-cellDNAseqeuncing(scDNA-seq)datausingtheSCITE
algorithm.Representativecasesillustratingdistinctpatternsofclonalevolutionareshown.Eachnoderepresentsamutationalevent,andeachcircle
representsasubclonewithcumulativemutationalevents,whichcanbetracedwithadottedlineandsolidlinestowardstheroot.Thesizeofthecircleis
proportionaltotheclonalpopulation,andthenumberswithineachcirclearethenumberofcellsandthepercentageofeachcloneamongthetotaltumor
cells.The95%credibleintervalsfromtheposteriorsamplingareshowntoillustratetheuncertaintyinthesubclonesizes.Thewild-typecellswhichdidnot
carryanydrivermutationsarenotshown.b,cLinearclonalevolutionpattern,inwhichasubsetofcellsfromthefoundercloneacquiredadditional
mutationsinastepwisemanner.Thetrunkcloneexhibitsaforkedevolutionpatternbasedonthestatusofadditionalmutations.d–iBranchingclonal
evolutionpatternincludingconvergentevolutionpatternswithmolecularalterationsingNPM1-RAS/MAPK-IDH,hchromatin-RUNX1-RAS,andiNPM1-IDH-
FLT3/RAS/MAPKpathways.Theclonalevolutionpatternsarecharacterizedbytheparallelacquisitionofmultiplefunctionallyredundantmutationsin
differentcellpopulations.j,kInferenceoftherelativetimingoflossofheterozygosity(LOH).ZygositystatebasedonthescDNA-seqdatawas
incorporatedintophylogenyreconstruction.TworepresentativecaseswithhomozygousRUNX1mutationsinvolvingLOHareshown.Inbothcases,each
RUNX1mutationwasinitiallyheterozygousandsequentiallydevelopedintohomozygousstate,withoutacquiringanyadditionalmutationsduringLOH
events.ADOalleledropout,FPRfalse-positiverate.
baseline and relapse pairs and 2 with multiple refractory time- leukemia initiating capabilities of multiple parallel subclones,
points) by scDNA-seq to study the evolution of clonal archi- albeit with variable capabilities, consistent with the previous
tecture in response to different therapies (Figs. 6–9 and observationsthatAMLLICpopulationsalsoconsistofgenetically
SupplementaryFig. 14).Forinstance, inAML-09,weobserved a diverse cells7,32. These clonally diverse LIC populations likely
selection of a small subclone with FLT3 p.D835Y during azaci- form the basis of emergence and selection of resistant subclones
tidine and sorafenib (a FLT3 inhibitor) treatment, which was under therapies, a process we have further illustrated meticu-
associatedwithrelapse(Fig.6).Thisclonalselectionisconsistent lously through single-cell analyses of longitudinal specimens
with the known in vitro differential sensitivity of various FLT3 (Figs.6–9andSupplementaryFig.14).Usingemergingsingle-cell
mutations to sorafenib25; indeed, the FLT3 p.D835Y mutation is multi-omics technology, we have simultaneously profiled single-
more resistant to sorafenib than the D835E and ITD mutations cell mutations and cell surface proteins in AML samples. This
(subclones with the two mutations were effectively cleared by analysis allowed correlation of genetic and phenotypic hetero-
sorafenibinthispatient). Similarly, inAML-99,weobserved the geneity in AML, and also advanced our understanding of how
selection of subclones with NRAS mutation along with the mutation history corroborates with the phenotypic changes
acquisition of PTPN11, FLT3-ITD, and IDH1 mutations during during the clonal evolution.
treatment with azacitidine and enasidenib (an IDH2 inhibitor). This work represents the largest cohort of AML patients yet
The selection of subclones with RTK/RAS/MAPK signaling examined at single-cell resolution and contributes to a growing
pathway mutations as well as IDH1 mutation is consistent with body of data5,7,33 enabling a deeper understanding of the fun-
the previously reported resistance mechanism to IDH2 inhibitor damentalclonalarchitecturesofAML.Thedepthofbothpatient
(Fig.7)26,27.Theanalysisoftwotreatment-refractoryAMLcases numbers and cells sequenced allowed a robust analysis of the
showedcomplicatedclonaldynamicsduringtherapy.BothAML- clonal relationship and phylogeny in this study despite the
38(Fig.8,thesamecaseinFigs.3iand4c)andAML-04(Fig.9) technical challenges associated with single-cell sequencing, such
had AML with multiple branching subclones. In both cases, as ADO, multiplets, coverage inconsistency, false positives, and
treatment with a FLT3 inhibitor-containing therapy reduced others. Here, we interrogated up to 37 known leukemia driver
clones with FLT3 mutations, however, with a concurrent expan- genes that have given rise to a remarkable level of clonal com-
sionorselectionofotherclonesfrequentlyinvolvingRAS/MAPK plexity in AML. It is noteworthy that this is still an under-
signalingpathwaymutations,whichisinlinewitharecentstudy estimation of the true extent of clonal diversity. Future studies
utilizing the same scDNA-seq platform in gilteritinib-treated with even more cells, broader coverage of the genome, and
AMLpatients28.Takentogether,scDNA-seqoflongitudinalAML integrationwithsingle-celltranscriptomicandepigenomicstates,
samples allowed meticulous illustration of clonal response to which is becoming a reality with recent technological advance-
therapies that revealed underlying evolutionary dynamics asso-
ments33–35,
will further elucidate the clonal diversity and evolu-
ciated with therapeutic resistance. tionary trajectories of AML. Such studies should be performed
ideally in samples collected from a large clinical trials, which
wouldallowsystematicinvestigationofpredictiveandprognostic
Discussion
impact of clonal diversity in AML.
Usingahigh-throughputscDNA-seqplatform,wehavedescribed
the landscape of AML clonal architecture with breadth and high
resolution. Cell-level mutation co-occurrence and mutual exclu-
Methods
sivity data obtained from this study provide a validation for the
Patientsandsamples.Weincludedintheanalysis154samples(140BMMCsand
clonal relationship among AML driver mutations previously 14peripheralbloodmononuclearcells)from123patientswithAMLwhohadatleast
inferred by bulk-sequencing studies, but also revealed novel clo- onesomaticmutationcoveredbythetargetedpanelforsingle-cellDNAsequencing
nal relationships, such as between TP53 and PPM1D that was (scDNA-seq).Ofthe123patients,108patientswereanalyzedforthesingle-timepoint
samplecollectedatpre-treatment(N=98)orrelapsed/refractorytimepoint(N=10).
previously mischaracterized by the population-based
Fortheremaining15patients,weanalyzedthelongitudinalsamplesobtainedatpre-
analysis14,15. Reconstruction of mutational history based on the treatmentandrelapse(N=8),pre-treatment,duringtreatmentincludingremission,
single-cell data provided evidence for both linear and branching andrelapse(N=5),and3randomrefractorytimepoints(N=2).Among123patients,
evolutionpatternsinAMLwithsomecasesexhibitingconvergent 97wereanalyzedbyscDNA-seq,23wereanalyzedbythesimultaneoussingle-cell
DNAandcellsurfaceproteinsequencing(scDNA+protein-seq),and3wereanalyzed
evolution, which is similar to the observations in other studies
bybothscDNA-seqandscDNA+protein-seq.Allthepatientsprovidedwritten
utilizing multi-region sequencing or single-cell analysis for dif-
informedconsentforsamplebankingandanalysis.Wehadpermissiontopublishthe
ferent
tumors7,20,29–31.
Xenotransplantation of several AML detailsoftheindividualpatients.ThestudywasapprovedbytheMDAnderson
samples including the one with convergent evolution showed institutionalreviewboardandwasinaccordancewiththeDeclarationofHelsinki.
NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications 7
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
a b
p < 0.001
Human Human
AML-38-001 NSG-SGM3 AML-67-001 NSG-SGM3
PDX-1 PDX-1
Transplant Transplant
scDNA-seq for BM PDX-2
scDNA-seq for BM scDNA-seq for BM scDNA-seq for BM
AM H L u - m 41 a - n 001 NSG-SGM3 S fr e o r m ia l P t D ra X n -1 splant N P S D G X -S -1 G _ M se 3 rial1
PDX-1
Transplant Serial transplant PDX-1_serial2
PDX-2 from PDX-2
scDNA-seq for BM PDX-3 PDX-2_serial1
PDX-2_serial2
PDX-4
scDNA-seq for BM/PB
scDNA-seq for BM/PB
c Human PDX-1
Human
AML-38
d
AML-67
Human PDX-1 PDX-2
Variantdetectionbysingle-cellDNAsequencing.Weusedamicrofluidic cells/mL.Next,35–100μLofcellsuspensionwasloadedontoamicrofluidics
approachwithmolecularbarcodetechnologytoamplifytheDNAfromindividual cartridgeandcellswereencapsulatedontheTapestriinstrumentfollowedbythe
cells.Briefly,cryopreservedBMMCswerethawed,andcellswerequantifiedusinga celllysisandproteasedigestiononathermalcyclerwithintheindividualdroplet.
CountessAutomatedCellCounter(ThermoFisherScientific).Thecellswere Thecelllysatewasthenbarcodedsuchthateachcellhadauniquelabel11.The
resuspendedincellbufferanddilutedtoaconcentrationof2,000,000–4,000,000 barcodedsampleswerethenthermocycledusingeither50primerpairsspecifictoa
8 NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
Fig.4Clonalarchitectureinxenotransplantedmodels.NSG-SGM3miceengraftedwithaliquotesofAML-38-001,AML-67-001,andAML-41-001were
analyzedbysingle-cellDNAsequencing(scDNA-seq).aSchematicfiguresofxenotransplantassay.PDXpatientderivedxenograft,BMbonemarrow,PB
peripheralblood.bChangeinclonaldiversitybetweenhumanandxenotransplantedmodels.Thetypesofsamplesareshownonthex-axis.They-axis
showsShannonindex.Thethicklinewithineachboxrepresentsthemedian,andthetopandbottomedgesoftheboxrepresentthe25thand75th
percentiles,respectively.Theupperandlowerwhiskersrepresentthe75thpercentileplus1.5timestheinterquartilerangeandthe25thpercentileminus
1.5timestheinterquartilerange,respectively.Two-sidedStudent’sttestwasusedwithoutadjustmentformultiplecomparisons(p=0.000557).N=
19samplesfrom3cases.Alldatapointsareshowncoloredbythedonors.PDXpatientderivedxenograft.c,dClonalstructurebasedonscDNA-seqdatain
humanandxenotransplantedsamplesincAML-38anddAML-67.Thephylogenetictreesvisualizetheestimatedorderofmutationacquisitionandthe
proportionofsubcloneswithadifferentcombinationofmutationsateachtimepoint.Thewild-typecellswhichdidnotcarryanydrivermutationsarenot
shown.ADOalleledropout,FPRfalse-positiverate.
panelof19mutatedgenescoveringknownAML-relatedhotspotlociand10 locususingthepatient-specificestimateaspriormean(SD=0.002).Treemodels
commonlyheterozygousSNPlociforADOdetermination(19-genepanel,Sup- usingthelocus-specificADOweresimilartotheonesusinglocus-independent
plementaryTable1),or279primerpairsspecifictoapanelof37mutatedcancer ADO(SupplementaryFig.15).Therefore,wereporthereonlytreesbasedona
genes(custom-designedpanel,SupplementaryData2). singlelocus-independentADOrate.
ThepooledlibrarywassequencedbyoneoftheIllumina’ssequencingplatforms Toincorporatezygositystatesintothephylogenyinference,werepresentedloci
(MiSeq,HiSeq4000,orNovaSeq6000)with150-or250-basepair(bp)paired-end withheterozygousandhomozygousmutationstatesastwoseparaterowsinthe
multiplexedruns.DetailedmethodsareprovidedintheSupplementaryMethods. tableofmutationcalls.Thefirstrowrepresentingtheheterozygousstateencodes
Briefly,fastqfilesgeneratedbythesequencerswereprocessedusingtheTapestri wild-typeandhomozygousstateattherespectivelocusas0,andheterozygousstate
AnalysisPipelineforadaptertrimming,sequencealignment,barcodecorrection, as1.Thesecondrowrepresentingthehomozygousstateencodes0forwildtype
cellfinding,andvariantcalling.Loomfilesthatweregeneratedbythepipelinevia and1forheterozygousandhomozygousstate.Thisencodingisbasedonthe
GATK-basedhaplotypecallingwerethenprocessedusingin-housefiltering assumptionthatahomozygousmutationismorelikelytoemergefromapre-
criteria.Weincludedcellsfordownstreamanalysisthatmetthefollowingcriteria existingheterozygousmutation,thandirectlyfromthewildtype.Wethenran
forgenotyping:totalreadcount(depth,DP)≥10×andalternativeallelecount≥3 SCITEonthismodifiedmutationtablerestrictingtheMCMCsearchto
(scVAF≥15%if20×≤DP≤99×;scVAF≥10%ifDP≥100×)36.Cellsthatdidnot phylogenieswheretheheterozygousstateofanymutationprecedesits
satisfythesecriteriawereconsideredtohavemissinggenotypes. homozygousstate.
TheADOrateforeachsamplewascalculatedonthebasisofcommonSNP TheinferenceprocedureunderlyingSCITEisfullyBayesian,whichallowedus
information.TheVAFfromsingle-cellgenotypedata(scDNA-seqVAF)was toquantifyuncertaintyintheinferredclonalarchitecturesbysamplingtreesfrom
calculatedasfollowsbasedonthesequencingreadsfromthepooledsinglecells: themodel’sposteriordistribution.Wesummarizedthesampledtreesbyreporting
(numberofthesingle-cellsequencingreadswithalternateallele)/(numberoftotal 95%credibleintervalsforeachinferredsubclone.
single-cellsequencingreads). Forlongitudinalsamples,wecombinedthescDNA-seqdatafromalltime
pointsfromthesamepatientandranSCITEforthepooleddata,andreconstructed
thetumorphylogeny.Whenanalyzingxenotransplantedsamples,wefirstsetthe
Mutationdetectionbybulksequencing.Asanorthogonalvalidation,allsamples
treestructureusinghumanAMLsamplesandassignedregeneratedsubclonesto
wereconcurrentlysequencedbyconventionalbulknext-generationsequencing thetreestructure.Toobtaintimepoint-specificestimatesofsubclonesizes,we
(bulk-seq)usingtarget-capturedeepsequencing(N=111,mediancoverage:421×,
performedcell-to-subcloneassignmentintheposteriorsamplingseparatelyfor
IQR:319×–610×)orwhole-exomesequencing(N=12,mediancoverage:150×,
eachtimepoint.Asinsomecasesnotallmutationswereobservedatalltime
IQR:86×–160×).Target-capturenext-generationsequencingwasperformedusing
points,weadjustedtheassignmentprobabilitiessuchthatacellcannotbeplaced
aSureSelect(AgilentTechnologies)custompanelof297genesthatarerecurrently belowanymutationunobservedatthecell’ssamplingtime.Thisleadstosubclones
mutatedinhematologicalmalignancies(SupplementaryTable3).Briefly,genomic
withatemporaryprevalenceof0%.Thisdoesnotnecessarilymeanthatthe
DNAwasextractedusinganAutopureextractor(QIAGEN/Gentra)andwas subclonewasextinctatthattime,butsimplyreflectsthelackofevidenceforits
fragmentedandbait-capturedinsolutionaccordingtothemanufacturer’sproto-
existencebasedonthecellssampledattherespectivetimepoint.Thenumberof
cols.CapturedDNAlibrarieswerethensequencedusingaHiSeq2000sequencer subcloneswasdefinedasthenumberofdistinctcellularpopulationscarryingat
(Illumina)with76-bppaired-endreads.Whole-exomesequencingwasperformed
leastonemutationbasedonmodel2.
usingSureSelectV4exomeprobes(AgilentTechnologies)andaHiSeq
B-SCITEwasusedtoinferthephylogenytreesbasedonthecombineddata
2000sequencer(Illumina)with76-bppaired-endreads.ModifiedMutectand
fromscDNA-seqandbulk-seq.Briefly,thesingle-celldataweregivenasamutation
Pindelalgorithmswereusedformutationcalling12.
matrix,andbulkdataconsistedofthevariantandtotalreadcountofthemutant
loci.B-SCITEreportedasinglemaximumlikelihoodmutationtreebyclustering
Inferenceofmutationalphylogenies.WeusedtheSCITEsoftwaretoinfer lineartreesegmentsbasedonVAFsimilarity21.TheTrAp(atreeapproachfor
phylogenetictreesofthedrivermutationsfromscDNA-seqdata.SCITEimple-
fingerprintingsubclonaltumorcomposition)algorithmwasusedtoinfer
mentsastatisticalmodelandanMCMC-basedBayesianinferenceschemethatcan
phylogenetictreesfrombulk-seqdata4.Fiftypatientswhosemutationsdetectedby
beusedtofindamutationtree(apartialtemporalorderofmutations)thatbestfits scDNA-seqwereallvalidatedbybulk-seqwithavailableread-countdatawere
theobservedsingle-cellgenotypes.Encodingtheevolutionaryhistorybyamuta- included.
tiontree(asopposedtoacelllineagetree)makestheuseofSCITEparticularly
efficientforusewithourdatawhichischaracterizedbyfewmutationaleventsand
manycells19. SNParray.GenomicDNAfrom40samplesinwhichscDNA-seqdatashowedat
SCITEoperateswithtwoparameters,oneforthefalse-positiverate(FPR)and least5%ofhomozygouslymutatedcloneswereanalyzedbyIlluminaOmni2.5-8
oneforthefalse-negativerate(FNR),whichcanbeeithersettopredefinedvalues SNParray.TherawdataretrievedfromanIlluminaOmni2.5-8SNParraywas
orinferredduringMCMCalongwiththetreestructure.Weusedaglobalestimate processedusingGenomeStudio2.0.TherawlogRratioandBallelefrequencywere
ofthesequencingerrorrateastheFPR(1%)anddataset-specificestimatesofthe usedforallele-specificcopynumberanalysisoftumorsalgorithm37toidentify
dropoutrate(ADOprovidedbytheplatform)astheFNR.WeranSCITE allele-specificcopy-numberalterations.
separatelyforeachpatient,providingthetableofmutationcallsastheinput
(encodingzeroforwildtype,oneformutation,andthreeformissingdata).To
obtainarobustmodel,weranSCITEwithfourdifferentcombinationsof DropletdigitalPCR.WeperformeddropletdigitalPCR(ddPCR)usingQX200TM
parameters:(1)usingallcellsincludingmissinggenotypeinformationwith1%FPR DropletDigitalTMSystem(Bio-RadLaboratories)toconfirmthevariantsthatwere
andSCITE-inferredFNR,(2)usingallcellsincludingmissinggenotype detectedbyscDNA-seqbutwerenotdetectedbybulk-seq.ddPCRTMSupermixfor
informationwith1%FPRandplatform-providedFNR,(3)usingonlycellswithfull Probes(NodUTP)wasusedwith50ngofgenomicDNAasatemplateforddPCR
genotypeinformationwith1%FPRandSCITE-inferredFNR,and(4)usingonly assayina96-wellplateaccordingtothemanufacture’sprotocol.Sevennanogram
cellswithfullgenotypeinformationwith1%FPRandplatform-providedFNR. ofsynthesizedmutantDNA(designedthroughBio-RadLaboratoriesandordered
Whenprovidedwithanincompletegenotypeforacell,SCITEisstillabletousethe throughIntegratedDNATechnologies)inabackgroundof130ngofnormal
partialgenotypinginformationinthetreeinferenceandassignscellsintosubclones humangenomicDNA(Promega)wasusedasapositivecontrol.Fiftynanogramof
basedontheavailableinformation.Thetreestructurewasmostlyconsistentamong normalhumangenomicDNA(Promega)wasusedasanegativecontrol.Water
the4models(74of123[60%]casesshowingconsistenttreestructure).Phylogeny wasusedinsteadofDNAsforno-templatecontrolreactions.Eachreactionwas
figuresthatareshowninFig.2arebasedonmodel2(allcells,1%FPR,and testedinduplicate.Variant-specificprimers/probes(ddPCRTMMutationDetection
platform-providedFNR).Inaddition,wehavealsoimplementedtheuseoflocus- Assays,FAM/HEXformutant/wildtype)weredesignedandorderedthroughBio-
specificADOinSCITE.Intheabsenceoflocus-specificdropoutestimates,we RadLaboratoriesandaresummarizedinSupplementaryTable4.Datawereana-
adaptedtheMCMCschemetolearnADOratesindependentlyforeachmutated lyzedusingQuanta-SoftAnalysisProsoftwarev1.0.596(Bio-RadLaboratories).
NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications 9
a
0.3
0.24
0.18
0.12
0.05
−0.01
−0.07
−0.13
−0.2
−0.26
−0.32
31DC 33DC
3DC
91DC 22DC
b11DC
41DC 46DC 43DC
RD−ALH
711DC 321DC
83DC 09DC 54DC
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
ASXL1
DNMT3A
ETV6
EZH2
FLT3
GATA2
IDH1
IDH2
KIT
KRAS
NPM1
NRAS
PTPN11
RUNX1
SETBP1
SF3B1
SRSF2
STAG2
TET2
TP53
U2AF1
WT1
wild type
Fig.5Continued
10 NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications
262144
C=8D44.45%dim gate 94.7% 3.5%
196506
130872
1.8% 0.0%
19.9% 77.2%
0.2% 2.7%
A-CSS
A-EP
33DC
105
104
103
65236 102
–102 –400 –102102 103 104 105
SC45 V500-A CD13 APC-A
A-7yC-EP
43DC
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
b d
0 –1020 103 104 105
105
104
103
102
–102
–1020
CD38
1
B
0
V
3
421 V4
10
5
4
0-A
105
c
e f
CD34 CD117
Legend Legend
3 3
2 2
1 1
0
–1 0
–1
CD11b CD64
Legend Legend
3 2
2 1
1 0
0 –1
–1 –2
–2
g
Fig.5Thesingle-cellgenotype–phenotypecorrelation.aAheatmapshowingthecellular-levelcorrelationbetweenimmunophenotypeandgenotype
basedontheentiresequencedcells.Eachcircleiscoloredbythervalueofcoefficient(redifpositivelycorrelatedandblueifnegativelycorrelated),with
thesizereflectingtheabsolutervalue(*r<0.05,**r<0.01,***r<0.001).b–dArepresentativecase(AML-103-001)showingastepwisemutation
acquisitionalongwithhematopoieticdifferentiation.bSCITE-inferredmodel2phylogenytreeshowingalinearevolutionpatternofdrivermutations.cA
heatmapshowingtheimmunophenotypeofeachgenotype-definedsubcloneshowninFig.5b.dFlowcytometrydatafromthesamepatient.Acellular
populationdelineatedwitharedlineindicatesCD45-dimcells.TheblastswereCD34+CD33+CD13-myeloblasts.AsubsetofCD34+blastsshowedCD38
expression.DetailedflowcytometrydataisavailableinSupplementaryFig.13c,d.e–gArepresentativecase(AML-101-001)showingtwodistinctblasts
populationsdeterminedbythesimultaneoussingle-cellDNAandproteinprofiling.eSCITE-inferredmodel2phylogenytreeshowingalinearevolution
pattern.fThesingle-cellimmunophenotypingdataforselectedcellsurfacemarkers.Eachdotrepresentsasequencedcell.Relativeexpressionofeachcell
surfacemarkerisnormalizedbythedegreeofthelogarithmicoddsratio(logOR,brownifhighexpression,yellowiflowexpression).gAheatmapshowing
theimmunophenotypeofeachgenotype-definedsubclonedeterminedbytheSCITEmodelfromFig.5e.ADOalleledropout,FPRfalse-positiverate.
NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications 11
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
Fig.6ClonalselectioninresponsetoFLT3inhibitor-containingtherapy.A74-year-oldmanwithnewlydiagnosedtherapy-relatedacutemyelomonocytic
leukemiashowingaselectionofFLT3p.D835YcloneduringaFLT3inhibitor-containingtherapy.Thefishplotshowstheinferredclonalevolutionpattern
basedonthesingle-cellgenotypedata.Thephylogenetictreesvisualizetheestimatedorderofmutationacquisitionandtheproportionofsubcloneswitha
differentcombinationofmutationsateachtimepoint.Thewild-typecellswhichdidnotcarryanydrivermutationsarenotshown.BLbaseline,CRcomplete
remission,Ccycle,Dday,RELrelapse,ADOalleledropout,FPRfalse-positiverate.FullcasedescriptionisavailableinSupplementaryMethods.
12 NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
Fig.7EmergenceofIDH1/FLT3/NRASclonesduringIDH2inhibitor-containingtherapy.A76-yearoldwomanwithAMLshowingtheparallelevolution
ofIDH1p.R132C,FLT3-ITD,NRASp.G60E,andPTPN11p.I282VclonesduringanIDH2inhibitor-containingtherapy.Cladcladribine,LDAClowdose
cytarabine,Enaenasidenib,VENvenetoclax,DACdecitabine.Thefishplotshowstheinferredclonalevolutionpatternbasedonthesingle-cellgenotype
data.Thephylogenetictreesvisualizetheestimatedorderofmutationacquisitionandtheproportionofsubcloneswithadifferentcombinationof
mutationsateachtimepoint.Thewild-typecellswhichdidnotcarryanydrivermutationsarenotshown.BLbaseline,CRcompleteremission,Ccycle,D
day,RELrelapse,ADOalleledropout,FPRfalse-positiverate.FullcasedescriptionisavailableinSupplementaryMethods.
NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications 13
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
Fig.8ParallelevolutionofRAS/PTPN11clonesduringFLT3inhibitor-containingtherapy.A58-year-old-manwithrefractoryAMLshowingtheclearance
ofFLT3-ITDclonewithanexpansionofPTPN11/RASclonesduringaFLT3inhibitor-containingtherapy.Thefishplotshowstheinferredclonalevolution
patternbasedonthesingle-cellgenotypedata.Thephylogenetictreesvisualizetheestimatedorderofmutationacquisitionandtheproportionof
subcloneswithadifferentcombinationofmutationsateachtimepoint.Thewild-typecellswhichdidnotcarryanydrivermutationsarenotshown.Ccycle,
Dday,ADOalleledropout,FPRfalse-positiverate.FullcasedescriptionisavailableinSupplementaryMethods.
14 NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-020-19119-8
Fig.9SelectionofIDH1/RASclonesduringFLT3inhibitor-containingtherapy.A76-year-oldmanwithrefractorysecondaryAMLshowingtheclearance
ofFLT3-ITDclonewithanexpansionofIDH/RASclonesduringaFLT3inhibitor-containingtherapy.Thefishplotshowstheinferredclonalevolutionpattern
basedonthesingle-cellgenotypedata.Thephylogenetictreesvisualizetheestimatedorderofmutationacquisitionandtheproportionofsubcloneswitha
differentcombinationofmutationsateachtimepoint.Thewild-typecellswhichdidnotcarryanydrivermutationsarenotshown.Ccycle,Dday,ADO
alleledropout,FPRfalse-positiverate.FullcasedescriptionisavailableinSupplementaryMethods.
NATURECOMMUNICATIONS|(2020)11:5327|https://doi.org/10.1038/s41467-020-19119-8|www.nature.com/naturecommunications 15
