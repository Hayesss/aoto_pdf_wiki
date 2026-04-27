---
source_path: /mnt/c/Users/Administrator/Zotero/storage/JKT9G6GT/Das Mandal和Mukherjee - 2025 - Pan-cancer analysis of cancer-specific transcript isoforms reveals the regulatory impact of isoform.pdf
ingested: 2026-04-23
sha256: 3996f780ac0fc89f
---

JBiosci (2025) 50:31 (cid:2)Indian Academy of Sciences
DOI: 10.1007/s12038-025-00509-3
(0123456789().,-volV()0123456789().,-volV)
Pan-cancer analysis of cancer-specific transcript isoforms reveals
the regulatory impact of isoform switching on the alteration
of the interplay between RBPs and miRNAs in cancers
S D M 1,3* and S M 2,3*
UKHEN AS ANDAL UMIT UKHERJEE
1Machine Learning and Systems Biology Research Lab, Department of Computer Science and
Engineering, Ghani Khan Choudhury Institute of Engineering and Technology, Ministry of
Education, Government of India, Narayanpur, West Bengal 732141, India
2Present Address: National Cancer Institute, National Institutes of Health (NIH), Bethesda, MD
20892, USA
3Department of Computer Science, Ben-Gurion University, Beer-Sheva, Israel
*Corresponding authors (Emails, sukhen@gkciet.ac.in; sumit.mukherjee@nih.gov)
MS received 20 August 2023; accepted 16 October 2024
The switch in the predominantly expressed transcript isoform of the same gene has been identified as a
significant factor in the progression of various types of cancer. These switches can impact the gain or loss of
different 30UTRs, which are hotspots for the binding of microRNAs (miRNAs) and RNA-binding proteins
(RBPs).Inthisstudy,wefoundthatincancer-specificdominantexpressingtranscripts,thebindingofmiRNA
andRBPisdisrupted,suggestingthattranscriptswitchingcouldplayapartinmodulatingpost-transcriptional
gene expression during the progression and development of cancer. Our spatial correlation analysis demon-
strated that changes in miRNA and RBP binding, triggered by transcript switching, could interrupt their
interplay.Additionally,statisticalanalysisrevealedthatlocalfoldingenergy(LFE)isakeyfactorinchanging
miRNA and RBP interactions due to isoform switching. Overall, this study revealed that changes in cancer-
specifictranscriptscouldinfluencemiRNA–RBPinteractionsduetoalternationsinthelocalRNAstructureof
thetranscriptcausedbyisoformswitching,therebyleadingtothedysregulationofcrucialgenesinvolvedinthe
evolution and progression of cancer.
Keywords. Isoform switching; local folding energy; miRNA; post-transcriptional gene expression regula-
tion; RBP; RNA structure
1. Introduction stern 2022). These unique, cancer-specific transcripts
can produce varied phenotypes that influence regular
Under normal circumstances, cells from nearly all protein interaction networks, alter pathways, and
types of tissues express the same predominant tran- modify the regulatory landscape within cancer cells
script isoform (Gonza`lez-Porta et al. 2013; Ezkurdia (Porta-Pardo et al. 2015; Calabrese et al. 2020;
et al. 2015). However, in cancer, transcriptional Gulfidan et al. 2020; Broyde et al. 2021; Paull et al.
robustnessisobservedduetothealternationofsplicing 2021). These changes could enable cancer cells to
regulation, which causes the switching of various overcomevariousconstraintsatbothcellularandtissue
transcript isoforms and the generation of different levels, enhancing their survival in the face of diverse
fusiontranscripts(Zhaoetal.2016;Vitting-Seerupand cancer-related stresses (Kahraman et al. 2020;
Sandelin2017;Kahramanetal.2020;Mukherjeeetal. Mukherjee et al. 2021). Therefore, these cancer-speci-
2021, 2022, 2023; Mukherjee and Frenkel-Morgen- fic transcripts could contribute to the generation of
Supplementary Information: The online version contains supplementary material available at https://doi.org/10.1007/
s12038-025-00509-3.
http://www.ias.ac.in/jbiosci
31 Page2 of 14 SukhenDasMandal andSumitMukherjee
phenotypic plasticity for cancer cells. Recent pan-can- 2. Methods
cer analysis of whole-genome (PCAWG) projects
(Campbell et al. 2020) provide the expression land- 2.1 Identification of cMDTs
scape of alternatively spliced transcripts for 1209
cancer samplesfrom 27different cancertypes. Further, We accessed the dataset created by Kahraman et al.
a recent study identified the cancer-specific most (2020) used for the identification of cMDTs. This
dominant transcripts (cMDTs) from these PCAWG dataset, initially produced by the authors, contains
samples and constructed isoform-specific protein–pro- isoform-specific expression levels for 1,393 PCAWG
tein interaction (PPI) networks which reveal the samples, encompassing 27 distinct cancers, along with
involvement of cMDTs in PPI network disruptions in 3,249 genotype-tissue expression (GTEx) samples
cancers (Kahraman et al. 2020). drawn from a variety of normal human tissues. We
Isoform switching can lead to modifications in optedforthosecancer-specificisoformsintheirdataset
untranslated regions (UTRs) within transcripts, which that were discovered to be the highest expressed in a
can have significant impacts on transcriptional and minimum of 50% of the respective cancer samples,
translational regulations. The 30 UTR within a tran- designating these transcripts as cMDTs. Consequently,
script is the binding site for miRNAs and RNA- we pinpointed a total of 471 unique cMDTs, sourced
binding proteins (RBPs), both of which play critical from 465 genes across 23 different types of cancer.
roles in post-transcriptional regulation (Jiang and Similarly, a transcript isoform was considered as the
Coller 2012). The intricate interaction between miR- most dominating transcript isoform specific to normal
NAs and RBPs can govern transcript decay, a vital tissue if that transcript isoform was the highest
mechanism for managing protein abundance (Liu expressed transcript among other transcript variants of
et al. 2020). As such, isoform switching has the the same gene in a minimum of 50% of the respective
potential to change the miRNA and RBP binding site tissue samples.
in the 30 UTR, resulting in dysregulation in post-
transcriptional regulation that may contribute to the
development of cancer. The possible mechanism for 2.2 Number of targeting miRNAs and RBPs
this type of interplay could impact the local structural and their target sites for transcript isoform
change of the RNA (Kim et al. 2021). Yet, no
research has sought to explore whether transcript Transcript isoform-specific miRNA targets and posi-
isoform switching could influence miRNA and RBP- tions of miRNA target sites were obtained from Tar-
based regulation in cancers. Guided by this objective, Base v8 (Karagkouni et al. 2018). We considered a
we undertook this study to explore the connection transcript isoform as a target of an miRNA when
between transcript isoform switching and the alter- experimental interaction evidence was available in the
ation of miRNA and RBP binding across different database. RBPs and their binding sites were down-
types of cancer. To achieve this, we identified loaded from StarBase database (Li et al. 2014). To
cMDTs in 27 different cancers from PCAWG sam- reduce false-positive RBP–RNA interactions, we only
ples. Our investigation revealed that genes with a considered the interaction if there was evidence of at
larger number of exons displayed an alternation in least 3 cross-linking and immunoprecipitation (CliP)
the dominating expressed isoform of the transcript. experiments.
This alternation changes the targets of miRNA and
RBP, potentially influencing the interaction between
2.3 Distance calculation between miRNA
miRNA and RBP in the regulation of target gene
and RBP targeting sites
expression. The change in this interaction may be
influenced by the local RNA structure of the isoform.
We mapped the miRNA target sites and RBP binding
The evidence gathered from these observations sup-
sites to the 30UTRof targetmRNAs. We calculated the
ports the idea that the switching of the predominantly
number of nucleotides between the central nucleotide
expressed isoform involved in cancer progression is
ofmiRNAtargetsitesandRBPbindingsites,whichwe
associated with the modulation of key gene expres-
considered as the distance between miRNA and RBP
sions. These expressions are influenced by the dys-
binding sites. The distances were normalized to 30UTR
regulation of interplay, hinting at the significant role
lengths to correct for variable 30UTR lengths. Cus-
of isoform switching in cancer development and
tomized Practical Extraction and Reporting Language
progression.
Regulatory impactof isoform switching incancers Page 3 of14 31
(PERL) programs were developed to map the binding transcript isoforms in different types of cancers and
sites in 30UTR of target mRNAs and to measure the identified the factors that are involved in this process
distances between miRNA target sites and RBP bind- (figure 1). We identified 438 unique cMDTs but these
ing sites in the 30UTR of target mRNAs. The PERL were not the most dominant of the matched normal
programs are available upon request from the corre- tissue samples spread over 23 different cancer types
sponding author. (supplementary table 1). Out of these, the expressions
of331cMDTswereupregulatedandtheexpressionsof
14 cMDTs were downregulated (supplementary
2.4 Web-based tools table2).Wealsofoundthat89cMDTsweredetectedin
several types of cancer. We checked whether the
Pathway analysis was performed using Database for cMDTs identified in the PCAWG samples were con-
Annotation, Visualization, and Integrated Discovery sistent in other datasets or not. Transcript expression
(DAVID) (Huang et al. 2009). Numbers of exon and data of TCGA samples from the UCSC Xena database
transcript isoforms existing for a set of genes were showed that around 50% of the cMDTs identified in
calculated from ShinyGO v0.61 (Ge et al. 2020). The PCAWG samples were also cMDTs in the samples of
Venny 2.1 web-based tool was used to generate Venn the UCSC Xena database (supplementary table 3). To
diagrams. delvedeeper intothe roleof theserepeatedlyoccurring
cMDTsincancer,weexaminedtheirpotential function
as cancer drivers, oncogenes, or tumor suppressor
2.5 LFE calculation
genes, using the resources of the CancerMine database
(Lever et al. 2019). From our study, we found that
The calculation of LFE was conducted by leveraging
about 30% of all examined genes, which translates to
the minimum free energy (MFE) of a specific RNA
165 genes, were reportedly linked to cancer (supple-
sequence or nucleotide space. This was achieved by
mentary table 4). When we checked the expression of
utilizing the RNAfold package included in the
the genes, it was found that 107 genes were upregulated
ViennaRNA software (Lorenz et al. 2011).
and97genesdownregulatedindifferenttypesofcancers.
Outofthesedifferentiallyexpressedgenes,87geneswere
already linked to cancers (supplementary table 5, sup-
2.6 Statistical analysis
plementary figure 1). In terms of cancer types, we
observedthatuterineadenocarcinoma(Uterus-AdenoCA)
The graphical data depicted include either the mean
demonstrated the highest degree of dominant isoform
with a 95% confidence interval or the median along
switching, with 168 different cMDTs (figure 2A). A
with individual sample values. A paired two-tailed
significantquantityofcMDTswasalsoidentifiedinother
Student’s t-test was used to assess statistical signifi-
cancers, including pancreatic adenocarcinoma (Panc-
cance. These distinctions represent the statistical dif-
AdenoCA), cervical squamous-cell carcinoma (Cervix-
ferences between the control group and the specific
SCC), stomach adenocarcinoma (Stomach-AdenoCA),
samples indicated in the figures. Multiple linear
bladder transitional cell carcinoma (Bladder-TCC), pros-
regression analysis was used to predict the factors
tate adenocarcinoma (Prostate-AdenoCA), and ovarian
affecting miRNA and RBP binding on transcripts. In
adenocarcinoma (Ovary-AdenoCA).
regression analysis, the number of miRNA and RBP
Weobservedaswitchinthedominantisoformofthe
binding sites were considered as dependent variables,
transcript to a specific transcript variant in at least five
whereas the length of the transcripts, AU-rich element
cancer types in ten genes (supplementary table 6).
(ARE) score, LFE, and GC% were considered as
These genes are primarily cancer specific, suggesting
dependent variables.
their crucial role in carcinogenesis. Additionally, six
transcripts appeared dominantly in all samples of a
specific cancer type, while those transcripts were not
3. Results dominant in any of the samples from corresponding
normal tissue in the matched GTEx cohort (table 1).
3.1 Pan-cancer distribution of cMDTs We identified six genes [HIPK1, WDR47, RPS19,
KIF22, NDC80, and FOXM1] where a particular tran-
We studied the impact of the interplay between RBP script emergedas themostdominant transcript isoform
and miRNAs for the alteration of most expressing in all samples of a specific cancer type, but those
31 Page4 of 14 SukhenDasMandal andSumitMukherjee
Figure 1. Flowchart to examine the impact of isoform switch in the interplay between RBP and miRNA and factors
involved in this process. The flowchart depicts the identification of the switch of the most dominated expressing transcript
isoformandchangeoftheRBPandmiRNAinteraction.Differentfilteringparametersanddatabasesusedfortheanalysisare
shown.
transcripts were not the most dominant ones in any of significant upregulation of these transcripts in specific
the matched normal tissue samples. This finding sug- cancers highlights their importance in cancer develop-
gests the potential of these transcript isoforms to serve ment and progression (supplementary figure 2). Our
as indicators for detecting specific cancer types. The analysis indicated that genes with a higher number of
Regulatory impactof isoform switching incancers Page 5 of14 31
Figure 2. Distribution of cMDTs in different cancers. (A) Number of cMDTs in different cancers. (B) Histogram
representingthedistributionofthenumberoftranscriptisoformsexistingforthe438genesshowedswitchingofdominating
expressingtranscripts(redbar).Frequencydistributionoftheexpectednumberofisoformsexistingfor438genesamongall
humangenes(graybar).(C)Ahistogramrepresentingthedistributionofthenumberoftranscriptisoformsthatexistforthe
genesthatshowedswitchingofdominantexpressingtranscripts(redbar),comparedtothedistributionoftheaveragenumber
of isoforms that exist for all human genes. (D) Pathway analysis of 438 human mRNAs showing a switch of dominant
expressing transcript.
exonsdemonstratedashiftinthedominantlyexpressed are implicated in various cancer-related pathways like
transcript isoform in cancer (figure 2B). Genes viral carcinogenesis and central carbon metabolism in
exhibiting a switch of the dominant transcript isoform cancer (figure 2D). Taken together, these data suggest
in cancer also had a significantly higher number of that genes with a larger number of exons showed a
transcript isoforms (figure 2C). To check whether this switch of the dominant transcript in cancer, which
observation was linked to specific types of cancer or mightplayasignificantroleincancerdevelopmentand
not,therelationwasexaminedacrossdifferenttypesof potentially serve as a clinically important gene for
cancer having at least 30 cMDTs and a similar pattern specific cancer types.
except for bladder cancer was found (supplementary
figures 3–10). These findings imply that a greater
number of exons allow for the expression of a larger 3.2 RNA isoform switch disrupts interplay
number of isoforms, which, in turn, provides oppor- between miRNA and RBP in cancer
tunities for isoform switching in cancer, and this is
independent of cancer types. Pathway analyses dis- RBP and miRNA are two primary regulators at the
closedthatthegenesshowingtranscriptisoformswitch post-transcriptional level, and gene expression is
31 Page6 of 14 SukhenDasMandal andSumitMukherjee
Table1. Cancer-specificmostdominanttranscripts(cMDTs),whichcouldbeclinicallyimportantforparticularcancerand
aid in its diagnosis, are characterized by their consistent switching in all samples of that cancer type
Normal tissue Tumor tissue Gene Total no. of
(GTEx) (PCAWG) Gene ID cMDT name tumor samples
Pancreas Panc-AdenoCA ENSG00000163349 ENST00000369558 HIPK1 75
Pancreas Panc-AdenoCA ENSG00000133316 ENST00000538098 WDR74 75
Pancreas Panc-AdenoCA ENSG00000105372 ENST00000221975 RPS19 75
Pancreas Panc-AdenoCA ENSG00000079616 ENST00000160827 KIF22 75
Muscle Bone-Leiomyo ENSG00000080986 ENST00000261597 NDC80 34
Breast Breast-LobularCA ENSG00000080986 ENST00000261597 NDC80 6
Bladder Bladder-TCC ENSG00000111206 ENST00000359843 FOXM1 23
dependent on their regulation. Consequently, we suggest that transcript switching diminishes miRNA
investigatedthevariationsinmiRNAandRBPbinding and RBP binding, potentially disrupting the interaction
associated with transcript switching in various cancers. between miRNA and RBP binding in cancer, and was
We found that transcript switches in cancer signifi- limited only to urogenital cancers.
cantly decrease the average numbers of miRNA bind-
ing sites and the number of targeting miRNAs per
transcript (figure 3A). Similarly, transcript isoform 3.3 Association of multiple factors with changes
switching in cancer reduces the average number of in miRNA and RBP binding as a consequence
RBP binding sites and target RBPs per transcript (fig- of isoform switching in cancer
ure 3B). Our analysis indicated that transcript switch-
ing might impact miRNA and RBP binding, and We examined various factors that could affect the
multiple studies have reported that the interaction change in RBP and miRNA binding due to transcript
between miRNA and RBP binding influences the reg- switching.
ulation of gene expression. Therefore, we sought to Multiple regression analysis revealed that the length
understand the impact of transcript isoform switching
ofthe30UTRandLFEaresignificantfactorsthatcould
on the interaction between miRNA and RBP binding affect miRNA and RBP binding to their target isoform
by examining the relative positions of miRNA and expressed in normal tissue. This relationship remains
RBP binding sites on the transcript. The number of valid even when the dominantly expressed RNA iso-
miRNAs and RBP binding pairs within 50, 100, and form changes in cancerous tissue (table 2). We
150 bp of normal tissue samples were 4908, 9725, and observed a robust correlation between changes in
13930, respectively, which decreased to 3750, 7258,
30UTRlengthandLFEwithalterationsinmiRNAsand
and 10412, respectively, in cancer tissue samples (fig- RBPs binding (table 3). These findings suggest that
ure 3C). When we normalized the relative distance longer 30UTR containing transcript isoforms are tar-
between miRNA and RBP binding by the transcript geted by a greater number of miRNAs and RBPs.
length, the pattern remained consistent, suggesting that Additionally, changes in LFE, which are due to local
the disruption of interaction is not dependent on tran- structural modifications of the transcript, also play a
script length (figure 3C). It was found that transcript criticalroleinthechangeofmiRNAandRBPbinding.
isoformswitchesaremajorlyseeninurogenitalcancers
(prostate, bladder, and kidney cancers). So, we
attempted to check whether disruption of the interplay 4. Discussion
between miRNA and RBP was limited only to uro-
genital cancers. Our analysis demonstrated that the The majority of human genes transcribe multiple
number of miRNAs and RBP binding pairs within 50, mRNA isoforms (Pan et al. 2008; Wang et al. 2008;
100, and 150 bp decreased in urogenital cancers with Reyes and Huber 2018), and it is well recognized that
respect to matched normal tissue samples, and nor- variations in the dominantly expressed transcript can
malization by transcript length did not change the modify gene expression. This alteration occurs by
pattern (supplementary figure 11A). A similar obser- expressing the same protein or different proteins,
vation was noticed for non-urogenital cancers (sup- thereby adjusting the translation and stability of the
plementary figure 11B). Therefore, our findings transcript (Geisberg et al. 2014; Wang et al. 2016;
Regulatory impactof isoform switching incancers Page 7 of14 31
Figure 3. An RNA isoform switch disrupts the interplay between miRNA and RBP in cancer. (A) Average number of
miRNAtargetsitespertranscript(leftpanel).AveragenumberoftargetingmiRNAspertranscript(rightpanel).(B)Average
numberofRBPbindingsitespertranscript(leftpanel).AveragenumberofRBP-targetedmRNAspertranscript(rightpanel).
(C) Distance, which represents the number of nucleotides between miRNA and RBP binding sites (left panel). Normalized
distance, which represents the number of nucleotides between miRNA and RBP binding sites (right panel). (*** p B0.001;
paired t-test)
Wong et al. 2016; Zheng et al. 2018). Changes in the elements in the 30UTR (Mayr and Bartel 2009). The
expression of various mRNA isoforms also play a part significance of miRNA-mediated repression of mRNA
in tumor/cancer-related cellular events such as apop- isoforms in the development of cancer has been
tosis, proliferation, invasion, metastasis, epithelial– reported in several studies. For example, it has been
mesenchymal transition (EMT), and angiogenesis observedthatmiR-16-1isunabletobindtoatruncated
(Yuan et al. 2001; Bauer et al. 2013; Tien et al. 2017; form of cyclin D1 (CCND1) mRNA, leading to an
Bowler and Oltean 2019; Mitra et al. 2020; Erdem enhanced expression of the CCND1 protein in mantle
et al. 2021; Pradella et al. 2021; Ly et al. 2022). The cell lymphoma (Chen et al. 2008). In the case of
switching of expressed isoforms has been linked to bladder cancer, changes in mRNA isoforms are known
numerousdiseaseconditions,particularlyvarioustypes to affect miRNA binding (Han et al. 2018). Further-
ofcancer(Zhaoetal.2016;Hanetal.2018;Kahraman more, it has been noted that the RNA-binding protein
et al. 2020; Erdem et al. 2021). For instance, shorter poly(A)-binding protein (Pab1) displays variability in
mRNA isoforms of the proto-oncogene insulin- its affinity to poly(A)-containing isoforms of the same
like growth factor 2 mRNA-binding protein family genes (Moqtaderi et al. 2018). It is also been reported
(IGF2BP1/IMP-1) yield more protein than full-length that the eukaryotic translation initiation factor 3 (eIF3)
mRNA isoforms due to the absence of repressive binds to each polypyrimidine tract binding protein 1
31 Page8 of 14 SukhenDasMandal andSumitMukherjee
Table 2. Relative contributions of possible parameters that can influence miRNA and RBP binding on the number of
miRNA and RBP targeting sites
MDT (GTEx)
Number of miRNA binding site
Dependent variable Independent variables b-value Level of significance
30UTR length 0.969 0.000
ARE score 0.075 0.406
LFE 0.543 0.010
GC% -0.071 0.160
Number of RBP binding site
Dependent variable Independent variables b-value Level of significance
30UTR length -0.010 0.971
ARE score -0.095 0.315
LFE -0.569 0.010
GC% -0.047 0.380
cMTD (PCAWG)
Number of miRNA binding sites
Dependent variable Independent variables b-value Level of significance
30UTR length 1.526 0.000
ARE score 0.047 0.627
LFE 1.101 0.000
GC% 0.007 0.903
Number of RBP binding site
Dependent variable Independent variables b-value Level of significance
30UTR length 0.843 0.017
ARE score -0.217 0.034
LFE 0.203 0.500
GC% 0.057 0.314
(PTBP1)mRNAisoforminamannerthatisdependent the activation of the oncogenic mitogen-activated pro-
on the cell cycle (Arake De Tacca et al. 2019). tein kinase (MAPK) and Jun N-terminal kinase (JNK)
In this study, we have undertaken a comprehensive pathways, as well as the promotion of tumorigenesis
exploration of the switch in dominantly expressed andmetastaticbehavior(Lietal.2005;Blaquiereetal.
isoforms across the transcriptome, its causes, and its 2018). This suggests that the transcript
potentialtoaffectgeneexpressionregulationincancer. ENST00000369558 may be clinically important for
We observed tissue-specific diversity in the change of pancreatic cancer and aids in its diagnosis. Another
dominantly expressed isoforms, which aligns with transcript, ENST00000538098 from the gene WDR74,
previous studies and is related to the number of exons was found expressed in all pancreatic cancer samples.
present in a specific gene. Our analysis shows that in WDR74 playsarole in thebiogenesis of theribosomal
certain cancer types, the change in the dominantly large subunit and enhances cell proliferation by regu-
expressed isoform of key genes can potentially aid in lating the wingless-related integration site (Wnt)/b-
diagnosisandbeclinicallyimportant.Forinstance,one catenin signaling pathway (Hiraishi et al. 2015; Li
of the six transcripts we identified as clinically et al. 2020; Cai et al. 2021). Hence, in pancreatic
importantforaparticularcancer,HIPK1,isinvolvedin cancer, the switching of expressed transcripts may be a
Regulatory impactof isoform switching incancers Page 9 of14 31
Table3. SpearmanrankcorrelationbetweenthenumberofmiRNAandRBPbindingsiteswithpossibleparametersthatcan
influence miRNA and RBP binding
3 0UTR length ARE score LFE GC%
MDTs No. of miRNA target sites 0.604** 0.515** -0.556** -0.271**
No. of RBP target sites 0.508** 0.305** -0.521** -0.052
cMDTs No. of miRNA target sites 0.601** 0.501** -0.549** -0.233**
No. of RBP target sites 0.501** 0.296** -0.508** -0.022
** p B 0.01.
decisive factor and a potential indicator. Ribosomal miRNAs, such as miR-548c (Srikantan et al. 2011),
protein 19 (RPS19), a component of the ribosomal miR-494 (Tominaga et al. 2011), miR-16 (Young et al.
small subunit 40S and a known gene responsible for 2012), and miR-200b (Chang et al. 2013), under var-
Diamond–Blackfan anemia (a cancer-prone genetic ious stress conditions. RBPs other than HuR have also
disorder) (Flygare et al. 2007), along with KIF22, been documented to hinder miRNA-mediated destabi-
NDC80, and FOXM1, which are involved in cell cycle lization or translation repression of target mRNAs.
regulation, were also identified (Tokai et al. 1996; Fu These include the interaction of RNA-binding motif
et al. 2008; Littler et al. 2010; Chen and U¨nal 2021). protein-38 (RBM38) with miR-92-3p in the expression
Their significant role in cell cycle regulation suggests regulation of phosphatase and tensin homolog deleted
that a change in the expressed mRNA isoform of these onchromosome10(PTEN)mRNA(Guanetal.2021),
genes indicates involvement in cancer development DnD1 with miR-430 in regulating NANOS and tudor
and progression. domain-containing protein 7 (TDRD7) mRNA (Kedde
RBPs and miRNAs serve as two key post-tran- etal.2007),heterogeneousnuclearribonucleoproteinL
scriptional regulators that influence mRNA outcomes (HNRNPL) with miR-297 and miR-299 for vascular
by modifying stability, export, localization, and trans- endothelial growth factor A (VEGFA) expression
lation. Beyond the individual regulatory roles of miR- (Jafarifaret al. 2011), and CRDBP1 with miR-183 and
NAs and RBPs, there is a notable interplay between miR-340 in regulating bTrCP1 mRNA and microph-
these two components in managing the transla- thalmia-associated transcription factor (MITF) mRNA,
tion/turnover of multiple mRNAs to fine-tune shared respectively (Elcheva et al. 2009). In all of these
target gene expression. This interaction can be either instances, RBPs are seen to inhibit miRNA-mediated
competitive or cooperative. In the competitive model, destabilization or translational repression of the target
the binding of an RBP impedes the function of an mRNAeitherbydirectlycompetingforthebindingsite
miRNA by blocking the binding of the miR-induced via steric hindrance or by modifying the secondary
silencing complex (miRISC) complex or vice versa. structure of the mRNA, which prevents miRNA
Conversely, in the cooperative model, RBP binding binding.
enhances the function of miRNA by boosting the Cooperative interplay was first observed when TTP
binding of the miRISC complex or vice versa. interacted with the RNA-induced silencing complex
Numerous instances of such interplay have been (RISC) complex, assisting miR-16 to interact with the
identified, and it is likely that many more remain 30UTR of tumor necrosis factor alpha (TNFa) and
undiscovered. For example, the first reported interplay cyclooxygenase-2(COX2)mRNAs,therebypromoting
was observed with the RBP HuR, which moved from mRNAdegradation(Jingetal.2005).RBPpumiliohas
thenucleustothecytoplasmunderconditionsofamino been seen to aid the binding of miR-221 and miR-222
acid deprivation and inhibited the miR-122-mediated to the 30UTR of p27 mRNA (Van Kouwenhove et al.
repressionofcationicaminoacidtransporter-1(CAT-1) 2011) and miR-503 to E2F3 mRNA (Miles et al.
mRNA translation (Bhattacharyya et al. 2006). HuR 2012). HuR has been found to enhance the binding of
hasbeenobservedtoobstructthetranslationrepression miRNA let-7 to suppress the expression of cellular
of PDCD4 mRNA by miR-21 under the inflammatory Myc (c-Myc) (Kim et al. 2009) and also to aid miR-
stimulus and the translation repression of p53 mRNA 19binbindingtothe30UTRofABCB1/P-glycoprotein
by miR-125b under DNA damage (Poria et al. 2015; mRNAs (Thorne et al. 2018). RBPs like poly(rC)-
Ahuja et al. 2016; Guha et al. 2019). A similar com- binding protein 2 (PCBP2) and FUS are also known to
petitive interplay was found between HuR and other cooperate with miRNAs to repress the expression of
31 Page10of 14 SukhenDasMandal andSumitMukherjee
Figure4. AnRNAisoformswitchmediatestheRNAstructure-dependentinterplaybetweenmiRNAandRBPbinding.The
isoformswitchmediatestheRNAstructure-dependentinterplaybetweenmiRNAandRBPbinding.Schematicrepresentation
of the proposed model of isoform-mediated structure-dependent interplay between miRNA and RBP binding to 30UTRs of
commontargetmRNA.Alterationoftranscriptisoform resultsinlocalconformationalchangesinthe30UTRRNA,affecting
the relative accessibility of miRNA and RBP binding sites.
target mRNAs (Lin et al. 2016). In oral cancer cells, caused by lipopolysaccharides (LPSs), where the syn-
RBP fragile X mental retardation protein-1 (FXR1) ergy of RBPs HuR and LA counteracts the effect of
collaborates with miR-301a-3p to target p21WAF1 miR-21 (Kumar et al. 2021). This competitive/coop-
mRNA, thus accelerating its degradation (Majumder erative interplay is context- or stimulus-dependent and
and Palanisamy 2020). An analysis of the transcrip- may change in disease conditions. Thus, the interplay
tome-wide binding sites for 150 human RBPs revealed between RBPs and miRNAs introduces an additional
that most of these RBPs impacted miRNA targeting layer to gene expression regulation. An isoform switch
and cooperatively amplified miRNA targeting (Kim alters the structure of the transcript and thereby can
et al. 2021). A transcriptome-wide correlation study influencetheinteractionandinterplaybetweenmiRNA
showed that RNA modification m6A may also influ- and RBP. Our analysis indicated that a switch could
ence this competitive/cooperative interplay (Das Man- modify the interaction of miRNA and RBPs. The
dal and Ray 2021). In multiple instances, more than spatial correlation between miRNA and RBP was
one RBP affects the binding of a specific miRNA to compromised due to the alteration of dominating
fine-tune the expression of a target gene. We have expressed transcripts. As this interplay between
observedsuchinterplay underinflammatory conditions miRNA and RBP is one way of fine-tuning the
Regulatory impactof isoform switching incancers Page 11 of14 31
expression of crucial genes, disruption of this interplay dependent RNA structural competition/cooperativity
in cancerousconditionscould disturbthe expressionof between miRNAs in various types of cancer and to
many vital genes, contributing to tumorigenesis. determineitseffectonpost-transcriptionalregulationof
30UTR length, GC percentage of 30UTR, AREscore, gene expression in complex regulatory environments.
and LFE are known to influence miRNA and RBP
binding. Longer 30UTR lengths could host a larger
numberofmiRNAandRBPsites.miRNAbindingbias 5. Conclusion
toward low GC-containingmRNAs (Davis et al. 2008)
and low GC content of seed sequence influence Our study elucidates the intricate relationships between
miRNA target recognition (Wang 2014). GC content isoform switching, miRNA, and RBP binding and their
influencesmRNAlocalizationinp-bodies(PB)andthe consequentialeffectsonthedevelopmentandprogression
binding of different RBPs, thus affecting mRNA sta- ofcancers.Ourresultsrevealcorrelationbetweenisoform
bility and translation repression in PBs (Courel et al. switchingandthe alterationofmiRNA andRBPbinding
2019). AREs, measured by calculating the AREscore, sites,underscoringthesignificanceoftheseinteractionsin
are crucial as they are involved in Dicer-dependent post-transcriptional regulation of gene expression. Our
mRNA decay (Jing et al. 2005), a key component of findings demonstrate that switches in the predominant
miRNA systems, and several miRNAs destabilize dif- transcriptisoformscanresultinstructuralmodificationsin
ferent mRNAs through ARE-dependent interactions the mRNAs that influence the accessibility of target sites
(Moore et al. 2011). Conversely, several ARE-depen- to miRNAs and RBPs. This can cause disruptions in the
dent RBPs like TTP, BRF1, AUF1 and KSRP desta- intricate balance between RBPs and miRNAs, possibly
bilize mRNA, while RNA-binding proteins such as leading to the dysregulationof essential genesimplicated
HuR and HuD increase mRNA stability, and TIA-1 in tumorigenesis. Furthermore, our data reveal a direct
represses mRNA translation. Furthermore, RNA sec- relationship between changes in LFE and the subsequent
ondarystructureisadeterminingfactorformiRNAand variation in the binding of miRNAs and RBPs. This
RBPbindingtotheir targetRNAs (Kerteszet al.2007; brings a new dimension to our comprehension of how
Groot et al. 2019). As LFE estimates the strength of structural changes in RNA transcripts can exert wide-
local secondary structure, changes in secondary struc- ranging impacts on gene expression regulation in
ture can be represented by change in LFE of the tran- cancerous conditions. Overall, our findings underscore
script. In this context, we examined the impact of the importance of transcript isoform switches in the
changes in secondary structure on isoform switch in modulation of miRNA and RBP binding and their sub-
miRNAandRBPbindingbyexaminingthecorrelation sequent impact on the delicate interplay between these
between miRNA and RBP binding with LFE. In our key post-transcriptional regulators. This opens up a new
analysisofvariousstructuralandsequencefeaturesthat avenue of research to further delve into the mechanisms
could influence miRNA and RBP interaction, we dis- of isoform-dependent RNA structural competition and
covered that alterations in LFE impact miRNA and cooperativityinvariouscancertypesandhowtheseaffect
RBP binding. Changes in LFE are a result of a struc- the complex post-transcriptional regulation of gene
tural switch. This structural alteration modifies the expression. This could ultimately pave the way for the
accessibility of miRNAs, as part of the miRISC com- development of innovative diagnostic and therapeutic
plex, and RBPs to their target mRNAs. Thus, our strategies for cancer.
analysis implies that structural changes can affect the
isoform-specific accessibility of miRNAs and RBPs,
which, in turn, can influence the interplay between Acknowledgements
RBPs and miRNAs. Such impact on the interplay
We thank Binita Goswami for her help in the devel-
between miRNAs and RBPs could potentially disrupt
opment of the illustration for the proposed model.
the expression of key genes, leading to the develop-
ment of cancers. Based on these observations, we have
proposed models in which isoform-specific changes
either facilitate or obstruct the reciprocal binding of Author contributions
miRNAs and RBPs, thereby positively or negatively
regulating gene expression (figure 4). Hence, our SDM: Conceptualization, methodology, software,
computational analysis paves the way for further investigation, formal analysis, supervision, project
experimentation to validate such dominant isoform- administration, writing – original draft, review, and
31 Page12of 14 SukhenDasMandal andSumitMukherjee
editing. SM: Conceptualization, investigation, super- Chen RW, Bemis LT, Amato CM, et al. 2008 Truncation in
vision, writing – original draft, review, and editing. CCND1mRNAaltersmiR-16-1regulationinmantle cell
lymphoma. Blood 112 822–829
Courel M, Cle´ment Y, Bossevain C, et al. 2019 Gc content
Funding shapes mRNA storage and decay in human cells. eLife 8
e49078
This research did not receive any specific grant from Das Mandal S and Ray PS 2021 Transcriptome-wide
funding agencies in the public, commercial, or not-for- analysis reveals spatial correlation between N6-methy-
profit sectors. ladenosine and binding sites of microRNAs and RNA-
binding proteins. Genomics 113 205–216
Declarations Davis N, Biddlecom N, Hecht D, et al. 2008 On the
relationship between GC content and the number of
Conflict of interest The authors declare no competing predicted microRNA binding sites by MicroInspector.
interests.
Comput. Biol. Chem. 32 222–226
Elcheva I, Goswami S, Noubissi FK, et al. 2009 CRD-BP
protects the coding region of b TrCP1 mRNA from miR-
References
183-mediated degradation. Mol. Cell. 35 240–246
Erdem M,OzgulI˙,DiokenDN,etal.2021Identificationof
Ahuja D, Goyal A and Ray PS 2016 Interplay between
an mRNA isoform switch for HNRNPA1 in breast
RNA-bindingproteinHuRandmicroRNA-125bregulates
cancers. Sci. Rep. 11 24444
p53 mRNA translation in response to genotoxic stress.
Ezkurdia I, Rodriguez JM, Carrillo-De Santa Pau E, et al.
RNA Biol. 13 1152–1165
2015 Most highly expressed protein-coding genes have a
Arake De Tacca LM, Pulos-Holmes MC, Floor SN, et al.
singledominantisoform.J.ProteomeRes.141880–1887
2019 PTBP1 mRNA isoforms and regulation of their
Flygare J, Aspesi A, Bailey JC, et al. 2007 Human RPS19,
translation. RNA 25 1324–1336
thegenemutatedinDiamond-Blackfananemia,encodesa
Bauer M, Be´nard J, Gaasterland T, et al. 2013 WNT5A
ribosomal protein required for the maturation of 40S
encodes two isoforms with distinct functions in cancers.
ribosomal subunits. Blood 109 980–986
PLoS One 8 e80526
Fu Z, Malureanu L, Huang J, et al. 2008 Plk1-dependent
Bhattacharyya SN, Habermacher R, Martine U, et al. 2006
phosphorylation of FoxM1 regulates a transcriptional
Relief of microRNA-mediated translational repression in
programme required for mitotic progression. Nat. Cell
human cells subjected to stress. Cell 125 1111–1124
Biol. 10 1076–1082
Blaquiere JA, Lam Wong KK, Kinsey SD, et al. 2018
Ge SX, Jung D, Jung D, et al. 2020 ShinyGO: a graphical
Homeodomain-interacting protein kinase promotes
gene-set enrichment tool for animals and plants. Bioin-
tumorigenesis and metastatic cell behavior. Dis. Model.
formatics 36 2628–2629
Mech. 11 dmm031146
Geisberg JV, Moqtaderi Z, Fan X, et al. 2014 Global
Bowler E and Oltean S 2019 Alternative aplicing in
analysis of mRNA isoform half-lives reveals stabilizing
angiogenesis. Int. J. Mol. Sci. 20 2067
and destabilizing elements in yeast. Cell 156 812–824
BroydeJ,SimpsonDR,MurrayD,etal.2021Oncoprotein-
Gonza`lez-Porta M, Frankish A, Rung J, et al. 2013
specific molecular interaction maps (SigMaps) for cancer
Transcriptome analysis of human tissues and cell lines
network analyses. Nat. Biotechnol. 39 215–224
reveals one dominant transcript per gene. Genome Biol.
Cai Z, Mei Y, Jiang X, et al. 2021 WDR74 promotes
14 1–11
proliferation and metastasis in colorectal cancer cells
GrootNSDe,ArmaosA,Gran˜a-montesR,etal.2019RNA
through regulating the Wnt/b-catenin signaling pathway.
structure drives interaction with proteins. Nat. Commun.
Open Life Sci. 16 920–929
10 3246
CalabreseC,DavidsonNR,DemirciogluD,etal.2020Genomic
Guan B, Li G, Wan B, et al. 2021 RNA-binding protein
basisforRNAalterationsincancer.Nature578129–136
RBM38 inhibits colorectal cancer progression by partly
Campbell PJ, Getz G, Korbel JO, et al. 2020 Pan-cancer
and competitively binding to PTEN 30UTR with miR-
analysis of whole genomes. Nature 578 82–93
92a-3p. Environ. Toxicol. 36 2436–2447
Chang SH, Lu YC, Li X, et al. 2013 Antagonistic function
Guha A, Ahuja D, Das Mandal S, et al. 2019 Integrated
of the RNA-binding protein HuR and miR-200b in post-
regulation of HuR by translation repression and protein
transcriptional regulation of vascular endothelial growth
degradation determines pulsatile expression of p53 under
factor-Aexpressionandangiogenesis.J.Biol.Chem.288
DNA damage. iScience 15 342–359
4908–4921
Gulfidan G, Turanli B, Beklen H, et al. 2020 Pan-cancer
Chen J and U¨nal E 2021 Meiotic regulation of the Ndc80
mapping of differential protein-protein interactions. Sci.
complex composition and function. Curr. Genet. 67
Rep. 10 3272
511–518
Regulatory impactof isoform switching incancers Page 13of14 31
Han S, Kim D, Shivakumar M, et al. 2018 The effects of Li Y, Chen F, Shen W, et al. 2020 WDR74 induces nuclear
alternative splicing on miRNA binding sites in bladder b-catenin accumulation and activates Wnt-responsive
cancer. PLoS One 13 e0190708 genes to promote lung cancer growth and metastasis.
Hiraishi N, Ishida YI and Nagahama M 2015 AAA-ATPase Cancer Lett. 471 103–115
NVL2 acts on MTR4-exosome complex to dissociate the LinX,YangB,LiuW,etal.2016InterplaybetweenPCBP2
nucleolar protein WDR74. Biochem. Biophys. Res. Com- and miRNA modulates ARHGDIA expression and func-
mun. 467 534–540 tion in glioma migration and invasion. Oncotarget 7
HuangDW,ShermanBTandLempickiRA2009Systematic 19483–19498
and integrative analysis of large gene lists using DAVID Littler DR, Alvarez-Ferna´ndez M, Stein A, et al. 2010
bioinformatics resources. Nat. Protoc. 4 44–57 Structure of the FoxM1 DNA-recognition domain bound
JafarifarF,YaoP,EswarappaSM,etal.2011Repressionof toapromotersequence.NucleicAcidsRes.384527–4538
VEGFA by CA-rich element-binding microRNAs is Liu Y, Pan C, Kong D, et al. 2020 A Survey of regulatory
modulated by hnRNP L. EMBO J. 30 1324–1334 interactions among RNA binding proteins and micro-
Jiang P and Coller H 2012 Functional interactions between RNAs in cancer. Front. Genet. 11 515094
microRNAs and RNA binding proteins. MicroRNA 1 LorenzR,BernhartSH,Ho¨nerzuSiederdissenC,etal.2011
70–79 ViennaRNA package 2.0. Algorithms Mol. Biol. 6 1–14
Jing Q, Huang S, Guth S, et al. 2005 Involvement of LyPT,XuS,WirawanM,etal.2022ZAPisoformsregulate
microRNA in AU-rich element-mediated mRNA insta- unfolded protein response and epithelial-mesenchymal
bility. Cell 120 623–634 transition. Proc. Natl. Acad. Sci. USA 119 e2121453119
Kahraman A, Karakulak T, Szklarczyk D, et al. 2020 Majumder M and Palanisamy V 2020 RNA binding protein
Pathogenic impact of transcript isoform switching in FXR1-miR301a-3p axis contributes to p21WAF1 degra-
1,209 cancer samples covering 27 cancer types using an dation in oral cancer. PLoS Genet. 16 1–25
isoform-specific interaction network. Sci. Rep. 10 14453 Mayr C and Bartel DP 2009 Widespread shortening of
KaragkouniD,ParaskevopoulouMD,ChatzopoulosS,etal. 30UTRs by alternative cleavage and polyadenylation
2018 DIANA-TarBase v8: a decade-long collection of activates oncogenes in cancer cells. Cell 138 673–684
experimentally supported miRNA–gene interactions. MilesWO,Tscho¨pK,HerrA,etal.2012Pumiliofacilitates
Nucleic Acids Res. 46 D239–D245 miRNA regulation of theE2F3 oncogene. GenesDev. 26
Kedde M, Strasser MJ, Boldajipour B, et al. 2007 RNA- 356–368
bindingprotein Dnd1 inhibits microRNA access to target Mitra M, Lee HN and Coller HA 2020 Splicing busts a
mRNA. Cell 131 1273–1286 move:isoformswitchingregulatesmigration.TrendsCell
Kertesz M, Iovino N, Unnerstall U, et al. 2007 The role of Biol. 30 74–85
site accessibility in microRNA target recognition. Nat. Moore AE, Young LE and Dixon DA 2011 MicroRNA and
Genet. 39 1278–1284 AU-rich element regulation of prostaglandin synthesis.
Kim HH, Kuwano Y, Srikantan S, et al. 2009 HuR recruits Cancer Metastasis Rev. 30 419–435
let-7/RISC to repress c-Myc expression. Genes Dev. 23 Moqtaderi Z, Geisberg JV and Struhl K 2018 Extensive
1743–1748 structural differences of closely related 30 mRNA iso-
KimS,KimS,ChangHR,etal.2021Theregulatoryimpact forms: links to Pab1 binding and mRNA stability. Mol.
of RNA-binding proteins on microRNA targeting. Nat. Cell 72 849-861.e6
Commun. 12 5057 MukherjeeSandFrenkel-MorgensternM2022Evolutionary
KumarR,PoriaDKandRayPS2021RNA-bindingproteins impact of chimeric RNAs on generating phenotypic
La and HuR cooperatively modulate translation repres- plasticity in human cells. Trends Genet. 38 4–7
sion of PDCD4 mRNA. J. Biol. Chem. 296 100154 Mukherjee S, Heng HH and Frenkel-Morgenstern M 2021
Lever J, Zhao EY, Grewal J, et al. 2019 CancerMine: a Emerging role of chimeric RNAs in cell plasticity and
literature-mined resource for drivers, oncogenes and adaptive evolution of cancer cells. Cancers 13 4328
tumor suppressors in cancer. Nat. Methods 16 Mukherjee SB, Mukherjee S and Frenkel-Morgenstern M
505–507 2022 Fusion proteins mediate alternation of protein
LiX,ZhangR,LuoD,etal.2005Tumornecrosisfactora- interaction networks in cancers. Adv. Protein Chem.
induced desumoylation and cytoplasmic translocation of Struct. Biol. 131 165–176
homeodomain-interacting protein kinase 1 are critical for Mukherjee S, Mukherjee SB and Frenkel-Morgenstern M
apoptosis signal-regulating kinase 1-JNK/p38 activation. 2023FunctionalandregulatoryimpactofchimericRNAs
J. Biol. Chem. 280 15061–15070 inhuman normal andcancer cells. WIREs RNA 14e1777
Li J, Liu S, Zhou H, et al. 2014 starBase v2.0: decoding Pan Q, Shai O, Lee LJ, et al. 2008 Deep surveying of
miRNA-ceRNA, miRNA-ncRNA and protein–RNA alternative splicing complexity in the human transcrip-
interaction networks from large-scale CLIP-Seq data. tome by high-throughput sequencing. Nat. Genet. 40
Nucleic Acids Res. 42 92–97 1413–1415
31 Page14of 14 SukhenDasMandal andSumitMukherjee
Paull EO, Aytes A, Jones SJ, et al. 2021 A modular master Vitting-Seerup K and Sandelin A 2017 The landscape of
regulator landscape controls cancer transcriptional iden- isoform switches in human cancers. Mol. Cancer Res. 15
tity. Cell 184 334–351 1206–1220
Poria D,GuhaA,NandiI,etal.2015 RNA-binding protein Wang X 2014 Composition of seed sequence is a major
HuR sequesters microRNA-21 to prevent translation determinant of microRNA targeting patterns. Bioinfor-
repression of proinflammatory tumor suppressor gene matics 30 1377–1383
programmed cell death 4. Oncogene 35 1703–1715 Wang ET, Sandberg R, Luo S, et al. 2008 Alternative
Porta-PardoE,Garcia-AlonsoL,HrabeT,etal.2015Apan- isoformregulationinhumantissuetranscriptomes.Nature
cancer catalogue of cancer driver protein interaction 456 470–476
interfaces. PLoS Comput. Biol. 11 e1004518 WangX,HouJ,QuedenauC,etal.2016Pervasiveisoform-
Pradella D, Deflorian G, Pezzotta A, et al. 2021 A ligand- specific translational regulation via alternative transcrip-
insensitive UNC5B splicing isoform regulates angiogen- tion start sites in mammals. Mol. Syst. Biol. 12 875
esis by promoting apoptosis. Nat. Commun. 12 4872 Wong QWL, Vaz C, Lee QY, et al. 2016 Embryonic stem
Reyes A and Huber W 2018 Alternative start and termination cells exhibit mRNA isoform specific translational regu-
sites of transcription drive most transcript isoform differ- lation. PLoS One 11 e0143235
encesacrosshumantissues.NucleicAcidsRes.46582–592 Young LE, Moore AE, Sokol L, et al. 2012 The mRNA
Srikantan S, Abdelmohsen K, Lee EK, et al. 2011 Trans- stability factor HuR inhibits microRNA-16 targeting of
lational control of TOP2A influences doxorubicin effi- COX-2. Mol. Cancer Res. 10 167–181
cacy. Mol. Cell. Biol. 31 3790–3801 Yuan A, Yu CJ, Kuo SH, et al. 2001 Vascular endothelial
Thorne JL, Battaglia S, Baxter DE, et al. 2018 MiR-19b growth factor189mRNAisoformexpression specifically
non-canonical binding is directed by HuR and confers correlates with tumor angiogenesis, patient survival, and
chemosensitivity through regulation of P-glycoprotein in postoperative relapse in non-small-cell lung cancer. J.
breast cancer. BBA Gene Regul. Mech. 1861 996–1006 Clin. Oncol. 19 432–441
Tien JF, Mazloomian A, Cheng SWG, et al. 2017 CDK12 ZhaoW,HoadleyKA,ParkerJS,etal.2016Identificationof
regulates alternative last exon mRNA splicing and mRNA isoform switching in breast cancer. BMC
promotes breast cancer cell invasion. Nucleic Acids Res. Genomics 17 181
45 6698–6716 ZhengD,WangR,DingQ,etal.2018Cellular stress alters
TokaiN,Fujimoto-NishiyamaA,ToyoshimaY,etal.1996Kid,a 30UTRlandscapethroughalternativepolyadenylationand
novel kinesin-like DNA binding protein, is localized to isoform-specific degradation. Nat. Commun. 9 2268
chromosomesandthemitoticspindle.EMBOJ.15457–467
Tominaga K, Srikantan S, Lee EK, et al. 2011 Competitive Springer Nature or its licensor (e.g. a society or other
regulation of nucleolin expression by HuR and miR-494. partner) holds exclusive rights to this article under a
Mol. Cell. Biol. 31 4219–4231 publishing agreement with the author(s) or other rightsh-
Van Kouwenhove M, Kedde M and Agami R 2011 older(s); author self-archiving of the accepted manuscript
MicroRNA regulation by RNA-binding proteins and its versionofthisarticleissolelygovernedbythetermsofsuch
implications for cancer. Nat. Rev. Cancer. 11 644–656 publishing agreement and applicable law.
Corresponding editor: RAMRAY BHAT
