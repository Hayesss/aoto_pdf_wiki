---
source_path: /mnt/c/Users/Administrator/Zotero/storage/I47TUI4R/Upadhya和Ryan - 2022 - Experimental reproducibility limits the correlation between mRNA and protein abundances in tumor pro.pdf
ingested: 2026-04-23
sha256: d45fe3b7b671bac6
---

Resource
Experimental reproducibility limits the correlation
between mRNA and protein abundances in tumor
proteomic profiles
Graphical abstract Authors
SwathiRamachandraUpadhya,
Reproducibility ColmJ.Ryan
ofprotein
abundance …
Correspondence
measurements
variesacross colm.ryan@ucd.ie
proteins
In brief
UpadhyaandRyanidentifiedsubstantial
Aggregated Aggregatedproteinreproducibilityrank variationinthereproducibilityofprotein
reproducibility
Low High abundancemeasurementsacross
scoreintegrates
multiple proteins.Theydevelopanaggregate
reproducibility proteinreproducibilityscoreandshow
estimates ProteinX ProteinY thatthisscoreexplainsvariationin
mRNA-proteincorrelationsacross
multipleproteogenomicstudies.They
showthatpathwayswithhigher-than-
Measurement
reproducibility averagemRNA-proteincorrelationsmay
explainsvariation simplybemorereproduciblymeasured.
in mRNA-protein
correlation
Highlights
d Thereproducibilityofproteinabundancemeasurements
variesacrossproteins
d Measurementreproducibilitycontributestovariationin
mRNA-proteincorrelations
d Aggregatedproteinreproducibilityscoreintegratesmultiple
reproducibilityestimates
d PathwayswithhighmRNA-proteincorrelationsmayjustbe
morereproduciblymeasured
Upadhya&Ryan,2022,CellReportsMethods2,100288
September19,2022ª2022TheAuthors.
ll
https://doi.org/10.1016/j.crmeth.2022.100288
ll
OPENACCESS
Resource
Experimental reproducibility limits
the correlation between mRNA and protein
abundances in tumor proteomic profiles
SwathiRamachandraUpadhya1,2andColmJ.Ryan1,2,3,*
1SchoolofComputerScience,UniversityCollegeDublin,Dublin,Ireland
2SystemsBiologyIreland,UniversityCollegeDublin,Dublin,Ireland
3Leadcontact
*Correspondence:colm.ryan@ucd.ie
https://doi.org/10.1016/j.crmeth.2022.100288
MOTIVATION Becausetheyareeasiertomeasureinhighthroughput,mRNAabundancesareoftenusedas
aproxymeasurementforproteinabundances.However,thereisonlyamoderatecorrelationbetweenthe
two,anditisuncleartowhatextentthismoderatecorrelationreflectspost-transcriptionalregulationandto
what extent it can be attributed to measurement error. Here, by analyzing samples with replicate pro-
teomes,wequantifytheextenttowhichreplicatemeasurementsofthesameproteinsarecorrelated.We
rank proteins according to their reproducibility and show that more reproducibly measured proteins
havehighermRNA-proteincorrelation,suggestingthatmeasurementerrorlimitsmRNA-proteincorrelation.
SUMMARY
Large-scalestudiesofhumanproteomeshaverevealedonlyamoderatecorrelationbetweenmRNAandpro-
teinabundances.Itisuncleartowhatextentthismoderatecorrelationreflectspost-transcriptionalregulation
andtowhatextentitreflectsmeasurementerror.Here,byanalyzingreplicateprofilesoftumorsandcelllines,
weshowthatthereisconsiderablevariationinthereproducibilityofmeasurementsoftranscriptsandpro-
teins from individual genes. Proteins with more reproducible measurements tend to have a higher mRNA-
protein correlation, suggesting that measurement reproducibility accounts for a substantial fraction of the
unexplainedvariationbetweenmRNAandproteinabundances.Thereproducibilityofindividualproteinsis
somewhat consistent across studies, and we exploit this to develop an aggregate reproducibility score
that explains a substantial amount of the variation in mRNA-protein correlations across multiple studies.
Finally,weshowthatpathwayspreviouslyreportedtohaveahigher-than-averagemRNA-proteincorrelation
maysimplycontainmembersthatcanbemorereproduciblyquantified.
INTRODUCTION ease samples from humans have therefore primarily focused
onDNAsequencevariationandtranscriptomicvariation.
Proteins are the primary actors in our cells, responsible for As transcriptomes are easier to quantify than proteomes,
almost all biological activities. Therefore, understanding how mRNAabundancesareoftenusedasaproxyforproteinabun-
protein abundances vary between healthy and disease states dances.However,therelationshipbetweenmRNAabundances
canprovideaninsightintohowbiologicalactivitiesarealtered and protein abundances is complex and non-linear and varies
in disease conditions. Among patients with the same disease, significantlyfromproteintoprotein.Consistentwiththis,large-
e.g.,breastcancer,variationinproteinabundancesmayexplain scale studies in humans and model organisms have revealed
}
differencesinsurvivaloutcomes(Oszetal.,2021)anddrugre- thatformostgenesthereisonlyamoderatecorrelationbetween
sponses(Shenoyetal.,2020).Consequently,significantefforts mRNA and protein abundances (Buccitelli and Selbach, 2020;
have been made recently to characterize proteomes across VogelandMarcotte,2012).Wenotethatcorrelationsbetween
largepatientcohorts(Ellisetal.,2013).However,ourabilityto mRNA and protein abundances can be calculated in two
quantifyproteinabundancesatscalehaslaggedbehindourabil- differentways:acrossallproteinswithinagivensample(i.e.,in
ity to sequence genomes and quantify mRNA abundances. agivencellline,arethemostabundantproteinsalsothemost
Large-scaleeffortstomolecularlycharacterizehealthyanddis- abundant transcripts?) or for a single protein across multiple
CellReportsMethods2,100288,September19,2022ª2022TheAuthors. 1
ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).
ll
Resource
OPENACCESS
samples(i.e.,dothesampleswiththehighestlevelsofaspecific Here, we analyze studies of tumors and cancer cell lines with
protein also have the highest number of transcripts coding for replicate proteomic profiles in order to assess the impact of
thatprotein?)(Franksetal.,2017;Liuetal.,2016;VogelandMar- measurementreproducibility onmRNA-proteincorrelation that
cotte,2012).Here,weareconcernedwithvariationacrossindi- canbeobservedforindividualproteinsacrosssamples.
viduals,andsothroughoutwhenwediscussmRNA-proteincor-
relations,wearecalculatingthecorrelationbetweentheprotein RESULTS
and transcript abundance for an individual protein across
samples. Astandardizedpipelinerevealsdifferencesinthe
Tumorsamples in particular have beensubject to transcrip- mRNA-proteincorrelationacrossstudies
tomicandproteomicprofilingefforts,andthesehaveprovided TheaveragemRNA-proteincorrelationreportedfordifferenttu-
insightintohowvariationinmRNAabundancesacrossindivid- mor proteomic profiling efforts varies substantially across
uals isassociated withvariation inprotein abundancesacross studies—rangingfrom0.23inanearlyproteomicstudyofcolo-
the same individuals. These studies have reported an average rectal cancer (Zhang et al., 2014) to 0.53 in a recent study of
mRNA-protein correlation in the range of (cid:1)0.2–0.5 (Mertins lungadenocarcinoma(Gilletteetal.,2020)(Table1).However,
etal.,2016;Zhangetal.,2014,2016).Thismoderatecorrelation itisnotmeaningfultodirectlycomparethereportedcorrelations
between mRNA and protein abundances can be attributed to becausethemethodsusedtoquantifythemRNA-proteincorre-
both biological and technical factors. Major biological factors lation have varied across studies—different studies have used
thatinfluencemRNA-proteincorrelationincludetranslationrates differentsummarystatistics(meanversusmedian),differentcor-
that vary across proteins and conditions, highly variable half- relation metrics (Pearson versus Spearman), and different
livesforbothproteinsandmRNAs,andpost-translationalmod- criteria for protein inclusion (e.g., no missing values, at least
ificationsthatcanalterproteinstabilityanddegradation(Bucci- 30%measuredvalues,onlythe10%mostvariableproteins)(Ta-
telliandSelbach,2020). ble1).Toenableamoredirectcomparisonacrossstudies,we
Differentproteinshavebeenobservedtohaveverydifferent calculatedthemRNA-proteincorrelationforthirteenproteomic
mRNA-protein correlations, and pathway enrichment analyses studies using a standardized pipeline. The datasets analyzed
haveidentifiedspecificfunctionalgroupswithlower-orhigher- comprisetenstudiesoftumorsamples(Clarketal.,2019;Dou
than-averagemRNA-proteincorrelations.Forinstance,anum- etal.,2020;Gilletteetal.,2020;Huangetal.,2021;Krugetal.,
ber of metabolic pathways have been shown to have higher- 2020; Mertins et al., 2016; Vasaikar et al., 2019; Wang et al.,
than average mRNA-protein correlations (Clark et al., 2019; 2021;Zhangetal.,2014,2016),twostudiesofcancercelllines
Huangetal.,2021;Jarnuczaketal.,2021;Mertinsetal.,2016; (Guoetal.,2019;Nusinowetal.,2020),andonestudyofhealthy
Zhangetal.,2014,2016),suggestinglimitedpost-transcriptional tissues(Jiangetal.,2020).Withineachstudy,wecalculatedthe
regulationoftheseproteins.Incontrast,subunitsoflargeprotein medianSpearmancorrelationbetweenmRNAandproteinforall
complexes have been shown to have lower-than-average proteinsthatweremeasuredinatleast80%ofsamples(STAR
mRNA-protein correlations, suggesting significant post-tran- Methods; Tables 1 and S1). Applying the same pipeline using
scriptionalregulation(Gonc¸alvesetal.,2017;Ryanetal.,2017; Pearsoncorrelation ratherthanSpearmancorrelation revealed
Taggartetal.,2020;Wangetal.,2017;Wuetal.,2013).Another broadlysimilarresults(Table1),andsothroughouttheremainder
factor that might influence mRNA-protein correlations across ofthepaper,wefocusouranalysisoncorrelationcalculatedus-
samplesistheintrinsicvariabilityinmRNAexpression.mRNAs ingSpearmancorrelationasitisthemetricmostcommonlyused
thatdonotvaryacrosssamples,suchasthosewhoseexpres- inproteogenomicstudies(9of13studies).
sionisusuallytightlyregulated,willnotcorrelatewiththeircorre- Across all studies, the median recalculated correlation was
spondingproteinsbecausevariationisessentialtoobservecor- 0.43withamaximumof0.55(lungadenocarcinoma[LUAD];Gil-
relation. As we focus our analysis on tumor profiles, where lette et al., 2020) and a minimum of 0.21 (colorectal cancer
extensivecopy-numberalterationsresultinsignificantvariation [CRC];Zhangetal.,2014).Insomeinstances,therecalculated
inmRNAabundances,thisissueisasmallerconcern. correlationwassimilartothatoriginallyreported,butinothers
Our technical ability to accurately and reproducibly quantify therewasasubstantialdifference.Forexample,thecorrelation
bothmRNAsandproteinsispotentiallyamajorfactorthatinflu- recalculatedforendometrialcancer(0.48)wasthesameasorig-
encesthemRNA-proteincorrelation.Iftheerrorinourmeasure- inallyreported(Douetal.,2020),whiletherecalculatedcorrela-
mentsislarge,wewouldexpectthiserrortoreducethecorrela- tionforcoloncancerwasmuchlowerthanthatreportedbythe
tion between mRNA and protein even in the absence of the authors(0.27versus0.48)(Vasaikaretal.,2019).Thisisbecause
biological factors outlined above. A number of studies have thecoloncancerstudyreportedthemeanmRNA-proteincorre-
separately assessed the reproducibility of either mRNA (’t lationforonlythe10%mostvariableproteinsratherthanthefull
Hoen et al., 2013; Marioni et al., 2008; SEQC/MAQC-III Con- setofproteins.Thesehighlyvariableproteinshavehigherthan
sortium, 2014) or proteomic (Casey et al., 2017; Tabb et al., averagemRNA-proteincorrelations.
2010)profilingapproaches.Othershaveexploredhowmeasure- MorerecentstudiesappeartohavehighermRNA-proteincor-
menterrorsinmRNAorproteomicprofilingcaninfluencethere- relations,e.g.,weobserveameanof0.49forstudiespublished
ported correlation between mRNA and protein abundances after 2019 versus 0.35 for studies published in 2016 or earlier
within sample correlations (across all proteins within a single (Table1).Thiscannotsimplybeattributedtodifferencesinthe
sample/cellline)ratherthanacrosssamples(forindividualpro- cancertypesstudiedindifferentyears,asthetwocancertypes
teinsacrossmanysamples)(Csa´rdietal.,2015;Lietal.,2014). profiledtwice(colonandbreast)seeanimprovementfromthe
2 CellReportsMethods2,100288,September19,2022
ll
Resource
OPENACCESS
Table1. AnalysisofmRNA-proteincorrelationusingastandardizedpipeline
Published Reported Proteininclusioncriterionin Computedmedian Computedmedian
Data year correlation reportedcorrelation Spearmancorrelation Pearsoncorrelation
GTEx32healthytissues 2020 0.46 <5tissueswithmissingvaluesfor 0.51 0.59
(GTEx) bothproteinandRNAmeasurements
CancerCellLine 2020 0.48 quantifiedinatleastoneten-plex 0.46 0.48
Encyclopaedia(CCLE) (9celllines)
NCI-60cancercelllines 2019 notreported – 0.36 0.40
(NCI60)
Glioblastoma(GBM) 2021 notreported – 0.50 0.51
Headandnecksquamous 2021 0.52 <50%missingvalues 0.54 0.56
cell
carcinoma(HNSCC)
Lungadenocarcinoma 2020 0.53 <50%missingvalues 0.55 0.56
(LUAD)
Endometrialcancer(EC) 2020 0.48 containmRNAandprotein 0.48 0.51
measurementsacrossallpatients
Breastcancer(BrCa2020) 2020 0.41 containmRNAandprotein 0.44 0.43
measurements(proteins
<70%missingvalues)
Clearcellrenalcarcinoma 2019 0.43 containmRNAandprotein 0.41 0.42
(ccRCC) measurementsacrossallpatients
Coloncancer(colon) 2019 0.48 top10%mostvariablyexpressed 0.27 0.28
proteinsquantifiedinbothplatforms
Ovariancancer(ovarian) 2016 0.45 containmRNAandprotein 0.41 0.41
measurementsacrossallpatients
Breastcancer(BrCa2016) 2016 0.39 containmRNAandproteinmeasurements 0.42 0.42
acrossallpatientspassingqualitycontrol
checks.
Colonandrectalcancer 2014 0.23 proteinmeasurementwithaveragespectral 0.21 0.22
(CRC2014) countacrossallpatientsR1.4
earlierstudies(Table1).Thiswouldsuggestthattechnicaland Many biological factors that influence mRNA-protein corre-
experimentalfactorsmayinfluencethereportedmRNA-protein lation,suchaspost-transcriptionalregulation,arenotrelevant
correlations and that improvements in either technology or inthecaseofreplicate measurementsofproteins, andsowe
experimentalprotocolshaveresultedinimprovedmRNA-protein expected the replicate proteomic profiles to be more highly
correlationsovertime. correlated than mRNA and protein profiles. This was indeed
thecaseforallstudies.Themedianprotein-proteinreproduc-
Thecorrelationacrossreplicateproteomicprofilesis ibilityforthereplicateproteomicprofilesfromtheCCLEdata-
onlymoderate set was 0.72 (Figure 1B; Table S2), whereas the median
Toassessthereproducibilityofmassspectrometry-basedpro- mRNA-proteincorrelationwasonly0.48(Table1).Themedian
teomic measurements, we analyzed three studies containing protein-proteinreproducibilityforthe replicateproteomicpro-
replicate proteomic profiles: ovarian tumor samples (Zhang files of ovarian tumors was 0.57 (Figure 1B), which is higher
et al., 2016), colon tumor samples (Vasaikar et al., 2019), and than the median mRNA-protein correlation of 0.41 (Table 1).
cancer cell lines of mixed lineages from the Cancer Cell Line Thereplicateprotein-proteinreproducibilityforthecolonstudy
Encyclopedia(CCLE)(Nusinowetal.,2020)(Figure1A).Thena- (median0.28)wasmuchlowerthanthatobservedfortheother
ture of the replicates varies across the different studies: for studies. However, it was still higher than the median-calcu-
ovarian cancer, the same tumor sample was profiled in two lated mRNA-protein correlation (0.21). One reason for the co-
different laboratories, for the cancer cell lines, biological repli- lonstudyto havealowmedianprotein-protein reproducibility
cates were performed within the same lab 1 year apart, while isthatoneofthetworeplicateproteomicprofilesisquantified
for colon cancer, the same tumor samples were profiled with using label-free/spectral counting MS, which is not as accu-
twodifferentmassspectrometry(MS)techniques,i.e.,isotope- rate as the stable isotope-based protein quantification
based protein quantification (TMT-10) and label-free spectral methods (Liu et al., 2016). Overall, we can conclude that
countingMS.Thus,thereisdiversityinthereplicateproteomic although protein-protein reproducibility is consistently higher
profiles in terms of sample types (tumor samples and cancer thanmRNA-proteincorrelations,theprotein-proteinreproduc-
celllines),sites,andtechniquesusedtoquantifytheproteins. ibility is still only moderate.
CellReportsMethods2,100288,September19,2022 3
A
Mass Spectrometry Replicates
Colon Cancer Ovarian Cancer CCLE
Samplescount:32
Samplescount:92 Proteincount:5774 Samplescount:18
Proteincount:2972 Ovarian tumor samples Proteincount:6891
Colon tumor samples from 2 different labs Cancer cell lines
quantified using 2 (JHU, PNNL) quantified replicatesfrom2different
different MS labelling using iTRAQ reagents in years quantified using
techniques(TMT,LF) conjunction with RPLC, TMT10-plexMS.
MS.
B
2.0
1.5
1.0
0.5
0.0
−0.2 0.0 0.2 0.4 0.6 0.8
Colon Protein (TMT) - Protein (LF)
Correlation
ProteinswithhigherreproducibilityhavehighermRNA- of0.37.Thisindicatesthatthereproducibilityofproteomicmea-
proteincorrelation surementshasamajorimpactonthecalculatedmRNA-protein
ThemoderatecorrelationsreportedbetweenmRNAandprotein correlation. We used a linear regression model to understand
abundanceshavebeenattributedtoavarietyofbiologicalfac- howmuchofthevariationinmRNA-proteincorrelationcanbe
tors,includingpost-transcriptionalregulation,varyingtranslation explained by variation in protein-protein reproducibility and
rates, and varying degradation rates (Buccitelli and Selbach, found that it explains approximately 14%, 17%, and 23% in
2020; Payne, 2015; Vogel and Marcotte, 2012). However, our the ovarian, CCLE, and colon studies, respectively (STAR
observation that some proteins can be quantified more repro- Methods;Figure2andS1A).
ducibly than others suggests that noise in quantification may Previousworkhasidentifiedproteincomplexmembershipas
alsobeamajorfactor.Ifthisisthecase,wewouldexpectthat thefactormostpredictiveofvariationinmRNA-proteincorrela-
proteins that can be more reproducibly quantified will have a tion,withsubunitsofproteincomplexestypicallyhavinglower-
highermRNA-proteincorrelation.Toassessthis,foreachstudy than-average mRNA-protein correlation (Gonc¸alves et al.,
weusedthereplicateproteomicprofilestostratifytheproteins 2017; Ryan et al., 2017). Using the same linear modeling
into deciles, ranging from the 10% of proteins with the lowest approachasabove,wefoundthatproteincomplexmembership
protein-proteinreproducibilitytothe10%withthehighestpro- explainsapproximately3%,8%,and6.7%ofthevariationinthe
tein-proteinreproducibility(STARMethods).Wethencalculated ovarian,CCLE,andcolonstudies,respectively(FigureS1A).This
themRNA-proteincorrelationforalloftheproteinswithineach suggeststhatnoiseinthequantificationofproteinabundances
decile.Wefound,forallthreestudies,thatthemedianmRNA- explains much more (on average (cid:1)3 times) of the variance in
proteincorrelationincreaseswithprotein-proteinreproducibility mRNA-protein correlation than the most predictive previously
(Figure2).Thecoloncancerstudyshowsadifferenceintheme- identified factor. Combined, the protein-protein reproducibility
dianmRNA-proteincorrelationof0.33betweenthefirstandlast and protein complex membership features explained approxi-
decilesofproteinreproducibility.Similarly,ovariancancerdata mately 17%, 23%, and 26% of the variation in mRNA-protein
showadifferenceof0.35,andtheCCLEdatashowadifference correlationintheovarian,CCLE,andcolonstudies,respectively
ytisneD
ll
Resource
OPENACCESS
Median = 0.72
Median = 0.28 Median = 0.57
−0.5 0.0 0.5 1.0 −0.5 0.0 0.5 1.0
Ovarian Protein (JHU) - Protein(PNNL) CCLE Protein (R1) -Protein (R3)
Correlation Correlation
Figure1. Protein-proteinreproducibilityacrossreplicatesismoderateandvariable
(A)Overviewofthereplicatesavailableforthethreedifferentproteomicstudies.
(B)Foreachstudy,wecalculatetheSpearmancorrelationforindividual proteinsacrosstheproteomic replicates.Thedistribution oftheprotein-protein
reproducibilityisshowninthehistogramforallmeasuredproteins.Foreachstudy,theblackdashedlinerepresentsthemedian.
4 CellReportsMethods2,100288,September19,2022
ll
Resource
OPENACCESS
A (Figure S1A). This is significantly more than protein complex
membershiporprotein-proteinreproducibilityalone(p<0.001,
likelihoodratiotest),suggestingthatproteincomplexmember-
shipandproteinreproducibilityindependentlycontributetothe
variation in mRNA-protein correlation. This is also evident
when binning proteins into reproducibility deciles—although
proteinsthatarecomplexsubunitsarepresentineverydecile,
they have consistently lower mRNA-protein correlations
(FiguresS1B–S1D).
Proteinswithhighreproducibilityinonestudyarealso
highlyreproducibleinotherstudies
Inadditiontoprovidingasummaryofhowreproduciblethepro-
teinmeasurementsfromeachstudyareonaverage,thereplicate
profilesenableustoseewhichproteinsaremostreproducibly
B
quantifiedoverall.IntheCCLEstudy,themediancorrelationbe-
tween replicate measurements calculated across all proteins
was0.72,butthisrangedfrom(cid:3)0.2to1.0forindividualproteins.
Similarly, the median for all proteins in the ovarian study was
0.57, but the individual correlations ranged from (cid:3)0.6 to 1.0,
andthemedianforthecolontumorstudywas0.28witharange
from (cid:3)0.2 to 0.8. This suggests that, at least within individual
studies, some proteins may be more reproducibly quantified
thanothers.
Tounderstandwhetherthesameproteinswerereproducibly
quantifiedacrossmultiplestudies,weanalyzedpairsofstudies
together. We found that there was a moderate correlation
(0.38) between the protein reproducibility calculated using the
ovarian tumor replicates and the colon cancer replicates (Fig-
C ure3A).Combinationsofotherpairsofstudiesrevealedsimilar
moderatecorrelations:colonandCCLE(0.31)andovarianand
CCLE(0.24)(Figures3Band3C).Althoughthenatureofthesam-
ples (tumorversus cell line)and thequantification approaches
(TMT/label-free quantification) varied across studies, this sug-
geststhatthereissomeagreementintermsofwhichproteins
canbereproduciblyquantified.Ingeneral,proteinsthatarehigh-
ly reproducible in one study tend to be highly reproducible in
others,whileproteinsthatshowpoorreproducibilityinonestudy
tend to show poor reproducibility in others (Figure 3). For
example, GBP1 is one of the proteins with reproducibility that
is consistently high across all three studies (Figure 3D), while
RPS29hasconsistentlowreproducibility(Figure3E).
Figure 2. Proteins with higher reproducibility have higher mRNA-
proteincorrelation Anintegratedrankingofproteinreproducibilitypartially
(A–C)BoxplotsshowingthedistributionofmRNA-proteincorrelationforpro- explainsthevariablemRNA-proteincorrelationin10
teinsbinnedaccordingtotheirprotein-proteinreproducibilityinthecolon(A), additionalstudies
ovarian(B),andCCLE(C)studies.Thetotalnumberofproteinsconsideredfor
Proteogenomicstudieswithlargenumbersofreplicates,suchas
each plot is indicated at the top right corner. The bins are deciles—each
containing(cid:1)10%oftheproteins.Thedecileisindicatedonthexaxisalong thethreeweanalyzedabove,aretheexceptionratherthanthe
withthehighestcorrelationbetweenexperimentalreplicatespresentwithin rule.Consequently,formoststudies,wedonotknowhowrepro-
thatdecile.Foreachboxplot,theblackcentrallinerepresentsthemedian,the ducible the proteomic measurements are. However, as noted
topandbottomlinesrepresentthe1stand3rdquartiles,andthewhiskers above, proteins that are highly reproducibly quantified in one
extendto1.5timestheinterquartilerangepastthebox.Outliersarenotshown. study are more likely to be highly reproducible in others. We
Themedianofeachdecileisindicatedabove/belowtheblackcentrallinefor
thereforesoughttoaggregatethereplicateproteincorrelations
eachboxplot.ThemedianmRNA-proteincorrelationacrossallproteinsfor
fromallthreestudies(CCLE,ovarian,colon)intoasinglelistcon-
eachstudyisindicatedasadottedgraylineineachplot.TheR2obtainedfrom
regressingthemRNA-proteincorrelationonprotein-proteinreproducibilityis tainingarankingofproteinreproducibility(STARMethods;Fig-
inthebottomrightcorner. ureS2A;TableS2).Weevaluatedanumberofdifferentaggrega-
tionapproachesandfoundthatasimplemethodusingaverage
normalizedrank explained themostvariancein mRNA-protein
CellReportsMethods2,100288,September19,2022 5
ll
Resource
OPENACCESS
correlationsofthethreestudiescontainingproteomicreplicates Proteinmeasurementreproducibilityisinfluencedby
(STARMethods;FigureS2B).Weusedthisapproachtocreatea abundance,variance,anduniquepeptides
rankedorderofproteinreproducibilityforthe5,211proteinsthat Tounderstandwhatcausessomeproteinstobemorereproduc-
werequantifiedinatleasttwooutofthethreestudies.Wethen iblymeasuredthanothers,weanalyzedanumberoffactorsthat
usedthisaggregatedlisttoassesstheextenttowhich‘‘average’’ we hypothesized might influence the reliability of their
proteinreproducibilityexplainsthevaryingmRNA-proteincorre- measurements.
lations observed in ten other studies (Clark et al., 2019; Dou Allofthestudiesanalyzedheremakeuseof‘‘bottom-up’’quan-
etal.,2020;Gilletteetal.,2020;Guoetal.,2019;Huangetal., tificationapproacheswhereproteinsarefirstdigestedintopep-
2021;Jiangetal.,2020;Krugetal.,2020;Mertinsetal.,2016; tides;thesepeptidesarethenquantifiedusingamassspectrom-
Wang et al., 2021; Zhang et al., 2014) (Figure 4). For all these eter, and peptide quantifications are converted into protein
studies,wefindthatproteinswithmorereproduciblemeasure- abundances computationally.Thisquantification isa stochastic
mentstendtohavehighermRNA-proteincorrelations.Although process,andthereisnoguaranteethateverypeptideinagiven
theaggregatedranksarebasedondatafromcancerstudies,we samplewillbedetectedbythemassspectrometer.Thequantifica-
observe the same trend in healthy tissues obtained from the tionofproteinsthathavelowabundance,andhencefewerdetect-
GTEx project (Figure 4J). Similarly, although the aggregated ablepeptides,isespeciallylikelytobesubjecttosubstantialsto-
ranksaregeneratedusingstudiesthatquantifyproteinsthrough chasticvariation.Asmallnumberofpeptidesmissedcanmake
data-dependentacquisition(DDA)approaches,weobservedthe abigdifferencetothequantificationoftheselowabundancepro-
sametrendforastudythatquantifiedproteinsusingdata-inde- teins,whileforhighlyabundantproteins,afewextraormissing
pendentacquisition(DIA)-basedproteomics(sequentialwindow peptideswillmakeonlyasmalldifference.Toassessthecontribu-
acquisitionofalltheoreticalmassspectra[SWATH-MS])inthe tionofproteinabundancetoproteinmeasurementreproducibility,
NCI-60cancercelllines(Figure4I).Ingeneral,themRNA-protein weobtainedtheproteinabundancesmeasuredin201tissuesam-
correlation increases with protein reproducibility for samples plesfrom32healthyhumantissuescollectedbytheGTExproject
from both healthy and diseased conditions and irrespective of (Jiangetal.,2020).Foreachprotein,wecalculatedthemeanabun-
theproteomicquantificationapproach. danceacrossallsamplesandtissues.Wefoundaclearrelation-
ToquantifytheamountofvariationinmRNA-proteincorrela- shipbetweenthemeanproteinabundanceandtheaggregated
tionthatcouldbeexplainedbyouraggregatedproteinreproduc- protein reproducibility rank—more abundant proteins are more
ibility ranks, we used a linear regression model for the ten reproduciblymeasured(Figure5A).Weperformedasimilaranal-
different studies. We found that the aggregated ranks explain ysisforthethreeindividualproteomicreplicatestudiesandfound
(cid:1)10%–20% (median 14%) of the variation in these studies theresulttobeconsistent(FiguresS5A–S5C).
(Figure4). Proteinswhoseabundancesdonotvarysignificantlyacross
Totestiftherewasanadvantagetousingtheaggregatepro- individualsareunlikelytohavehighmRNA-proteincorrelations,
tein reproducibility over protein reproducibility measured in ascorrelationmeasuresaredependentontherebeingmeaning-
eitherofthethreeindividualstudies(CCLE,ovarian,colon),we fulvariationinthedata.Furthermore,asthevariationobserved
compared the variance explained by the aggregate rankswith experimentallyislikelyacombinationofbothrealbiologicalvari-
thatexplainedbyeachindividualstudy.Inalltenstudieswithout ationandexperimentalnoise,proteinswithlowerbiologicalvari-
proteomicreplicates,theaggregatedranksexplainedthevaria- ation inabundance willtendto bemore affectedbymeasure-
tioninmRNA-proteincorrelationbetterthantheranksfromany ment noise. For each protein, we computed the variance in
individualdataset(FigureS3). proteinabundanceacrosssamplesfromtheGTExproject(Jiang
Anumberofeffortshavebeenmadetousemachinelearning etal.,2020).Wethenassessedtheinfluenceofthisvarianceon
to predict protein abundances from mRNA abundances (For- the reproducibility of measurements of individual proteins.
telny et al., 2017; Li et al., 2019; Yang et al., 2020). Recently, Similar to the mean protein abundance above, we found that
the NCI-CPTAC DREAM proteogenomics challenge engaged proteinswithahighervarianceofproteinabundancearemore
the community to predict protein abundances of breast and reproducibly measured (Figure 5B). Furthermore, the variance
ovarian tumor profiles using their corresponding genomic and of protein abundance explains (cid:1)20% of the variation in the
transcriptomicinformation(Yangetal.,2020).Wehypothesized aggregated protein reproducibility ranks. Similar trends were
that proteins whose measurements are highly reproducible observed for the three individual proteomic replicate studies
could be predicted better using machine-learning algorithms. (FiguresS5A–S5C).
Hence, we analyzed the prediction scores from the best-per- Thenumberofuniquepeptidesgeneratedperproteinisalso
forming model using the protein reproducibility data. We crucial for protein quantification by MS. To assess the impact
observedastarkdifferenceinthepredictionscoresofthelowest of this, we identified the number of unique peptides identified
and highest deciles of the protein reproducibility (Figures S4A perproteinusingtheGTExstudy.Westratifiedallproteinsinto
andS4B).Whilethelowestdecilehasacorrelationof(cid:1)0.35be- decilesbasedonthenumberofuniquepeptidesidentifiedand
tweenthemeasurementsandpredictions,thehighestdecilehas found that the aggregated protein reproducibility increased
a correlation of (cid:1)0.7. The aggregated protein reproducibility witheverydecileofuniquepeptidesidentified(Figure5C).This
rankscouldexplain(cid:1)25%and26%ofthevariationinthepredic- patternwasalsoevidentintheproteinreproducibilitymeasured
tion scoresofbreastandovariancancerstudies,respectively, ineachofthethreeindividualstudies(FiguresS5A–S5C).Thus,
againoutperformingthereproducibilitymeasuredinanyindivid- themoreuniquepeptidesidentifiedperprotein,thehigherthe
ualstudy(FigureS4C). confidenceofthemeasuredproteinlevels.
6 CellReportsMethods2,100288,September19,2022
1.00
0.75
0.50
0.25
0.00
−0.25
−0.50
−0.5 0.0 0.5 1.0
Ovarian Protein
Reproducibility Correlation
OneofthebiologicalreasonsproposedfortheweakmRNA- 2.6–7h,whileproteinshavehalf-livesrangingfromafewseconds
proteincorrelationisthedifferenceinmRNAandproteinhalf-lives toafewdays(VogelandMarcotte,2012).Recently,proteinswith
(Vogel and Marcotte, 2012). mRNAs typically have a half-life of longerhalf-liveswerefoundtobemorepredictableusingmachine
nietorP
noloC
noitalerroC
ytilibicudorpeR
1.00
0.75
0.50
0.25
0.00
−0.25 N = 2828;
ρ = 0.38, p = 1.4e-98
−0.50
−0.5 0.0 0.5 1.0
CCLE Protein Reproducibility
Correlation
nietorP
noloC
noitalerroC
ytilibicudorpeR
1.00
0.75
0.50
0.25
0.00
−0.25 N = 2703;
ρ = 0.31, p = 2.6e-59
−0.50
−0.5 0.0 0.5 1.0
CCLE Protein Reproducibility
Correlation
nietorP
nairavO
noitalerroC
ytilibicudorpeR
N = 4980;
ρ = 0.24, p = 1.4e-65
4
3
2
1
0
−2 0 2
Colon MS-TMTmeasurement
tnemerusaem
FL-SM
noloC
GBP1 protein reproducibility
0.5
0.0
−0.5
−1.0
ρ = 0.73, p= 2.95e-16
−1.0 −0.5 0.0 0.5
Ovarian PNNLmeasurement
tnemerusaem
UHJ
nairavO
1
0
−1
ρ = 0.88, p = 4.70e-11
−2
−1 0 1
CCLE R1 measurement
tnemerusaem
3R
ELCC
ρ = 0.9, p = 4.66e-7
3.5
3.0
2.5
2.0
1.5
1.0
0.5
−1 0 1
Colon MS-TMTmeasurement
tnemerusaem
FL-SM
noloC
RPS29 protein reproducibility
0.6
0.4
0.2
0.0
ρ = -0.07, p = 0.48 −0.2
−0.5 0.0 0.5
Ovarian PNNLmeasurement
tnemerusaem
UHJ
nairavO
0.75
0.50
0.25
0.00
−0.25
ρ = 0.07, p = 0.69 −0.50
−0.25 0.00 0.25 0.50
CCLE R1 measurement
tnemerusaem
3R
ELCC
ll
Resource
OPENACCESS
A B C
20 30 50
25
40
15
20
30
10 15
20
10
5 10
5
D
E
ρ = 0.18, p = 0.47
Figure3. Proteinswithhighreproducibilityinonestudyarealsohighlyreproducibleinotherstudies
(A–C)Binnedheatmapsshowingtherelationshipbetweentheprotein-proteinreproducibilitycalculatedindifferentstudies.Eachheatmapshowstherelationship
betweentwostudies,indicatedonthexandyaxes.Theregionsoftheheatmapsarecoloredaccordingtothenumberofproteinspresentintheregionas
indicatedinthecolorbar.ThenumberofproteinsincommonandSpearmancorrelationbetweenthetwostudies,withtheassociatedpvalue,arespecifiedinthe
boxforeachoftheplots.
(DandE)Foreachstudywithexperimentalproteinreplicates,scatterplotsillustratingtherelationshipbetweenprotein-proteinreproducibilityareshownfora
proteinwithhighreproducibility,GBP1(D),andaproteinwithlowreproducibility,RPS29(E).Foreachscatterplot,theSpearmancorrelationcoefficientofthe
protein-proteinreproducibilityandtheassociatedpvalueisindicatedatthebottom.
CellReportsMethods2,100288,September19,2022 7
ll
Resource
OPENACCESS
A B
C D
E F
G H
I J
(legendonnextpage)
8 CellReportsMethods2,100288,September19,2022
ll
Resource
OPENACCESS
learning,irrespectiveofthetranscripthalf-lives(Yangetal.,2020). Weusedalinearregressionmodeltoquantify,inallthirteenpro-
Thisledustoassessproteinhalf-lifeasapotentialfactorforthe teogenomicstudies,howmuchofthevariationinmRNA-protein
reproducibility of protein measurements. We obtained protein correlationcouldbeexplainedbytranscriptomicreproducibility.
half-lives estimations from a previous publication (Zecha et al., Wefoundthatthemedianvarianceexplainedwas15%.Inmost
2018) and divided them into two categories—long and short studies(8/13),ouraggregatedproteinreproducibilityexplaineda
half-lives (STAR Methods)—as was done in Yang et al. (2020). higherproportionofthevariancethanthemRNAreproducibility
Although both categories contain proteins with reproducibility (Figure6B).
scoresrangingfrom0to1,proteinswithalonghalf-lifehavea Compared with the other studies, the CCLE study had a
higher median protein reproducibility score (p = 9.70e(cid:3)25, strikingly higher percentage of variance explained by tran-
Mann-WhitneyUtest,two-sided;Figures5DandS5A–S5C). scriptomic reproducibility (40%). This is presumably because
Wenotethatthereissomecorrelationbetweentheattributes thereisalargeoverlapinthesetofsamplesusedtocompute
considered, in particular more abundant proteins tend to have the transcriptomic reproducibility and the CCLE mRNA-pro-
moreuniquepeptidesidentified.Tounderstandtherelativecontri- tein correlation, unlike the other studies. For the CCLE, the
butionofeachfactor,weperformedrankregressionbyusingthe variance explained by mRNA-mRNA reproducibility is higher
individualfactorsastheexplanatoryvariablesandtheranksofthe thanthevarianceexplainedbyprotein-proteinreproducibility.
proteomic reproducibility as the response variable (STAR However,themRNA-mRNAreproducibilitywasestimatedus-
Methods).Wefoundinallcasesthatamodelincludingallfourfac- ingamuchhighernumberofcelllines(382versus18forpro-
torsperformedbetterthanamodelincludingonlythebestindivid- tein-proteinreproducibility),whichwereasonedcouldexplain
ualfactor,suggestingthatvarianceinreproducibilitycanbestbe the increasedvarianceexplained.Totestthishypothesis,we
explainedbyacombinationoffactors(FigureS5D). downsampled the available transcriptomic data to make the
Thefactorsaboveallcontributetoprotein-proteinreproduc- comparisonmoreequal(sampling18celllineswithtranscrip-
ibility, raising the question of whether they themselves might tomes at random; STAR Methods). We found that, using this
be sufficient to explain variation in mRNA-protein correlation. approach, the protein-protein reproducibility explained more
Toassessthis,weperformedlinearregressionwiththesefactors of the mRNA-protein variability than the mRNA-mRNA repro-
(abundance,variance,uniquepeptides,andproteinhalf-lives)as ducibility (on average, (cid:1)2.8 times). This suggests that pro-
explanatoryvariablesandthemRNA-proteincorrelationofeach tein-protein reproducibility may influence mRNA-protein cor-
ofthe13differentstudiesasresponsevariables.Wefoundthata relation more than mRNA-mRNA reproducibility does but
combinedmodelofthefactorsexplained(cid:1)3%–17%ofthevari- that 18 cell lines is not sufficient to obtain a robust estimate
ation in mRNA-protein correlation of the different studies (Fig- of protein-protein reproducibility.
ure S6). However, the aggregated protein reproducibility ex- The Spearman correlation between aggregated protein
plains a considerably higher percentage of the variation in reproducibility and CCLE transcriptomic reproducibility is
mRNA-proteincorrelation in 12of13studies.TheGTExstudy 0.37 across 4,795 proteins. This suggests that there is
istheloneexception,likelyaresultoftheindependentvariables some agreement between the reproducibility of proteins
(proteinabundance,variance,numberofuniquepeptides)being and transcripts and that, to some extent, proteins that are
calculatedfromtheGTExstudyitself(FigureS6). reproducibly measured are encoded by transcripts that are
more reproducibly measured. To assess if both mRNA and
Transcriptomicreproducibilityalsocontributestothe protein reproducibility independently contribute to the vari-
varianceinmRNA-proteincorrelation ability of mRNA-protein correlation across all 13 studies,
Thusfar,wehaveprimarilyfocusedonunderstandingtheinfluence we used a linear model with the two factors as independent
ofproteinquantificationreproducibilityonmRNA-proteincorrela- variables and mRNA-protein correlation as the dependent
tion.However,itisalsolikelythatthereproducibilityofmRNAmea- variable. We found that in all cases, the two factors together
surements is an important factor in determining mRNA-protein explained a higher proportion of variance than either factor
correlations. To assess the impact of transcriptomic reproduc- alone (p < 0.001, likelihood ratio test). In the case of the
ibilityonmRNA-proteincorrelation,wecomparedtranscriptomic CCLE study (used to calculate the mRNA reproducibility
profiles for 382 cancer cell lines from the CCLE (Ghandi et al., and one of the three studies used to calculate protein repro-
2019) with those generated in a separate profiling effort (Klijn ducibility), the two factors together explained 48% of the
etal.,2015).Wefindthatthemediangene-wiseSpearmancorre- variance. For the 12 other studies, the two factors together
lationacrossstudieswas0.75(STARMethods;Figure6A).Again, explained (cid:1)14%–26% of the variance (Figure 6B). These ob-
thisvariedsignificantlyacrosstranscripts,rangingfrom(cid:3)0.05to servations suggest that the reproducibility in transcriptomic
0.96.Aswithproteinreproducibility,wefindthattranscriptomic and proteomic data contribute strongly and somewhat inde-
reproducibilityisinfluencedbybothmRNAabundanceandvari- pendently to the variability observed in mRNA-protein
ance(STARMethods;FigureS5E). correlation.
Figure4. AggregatedproteinreproducibilityrankspartiallyexplainsthevariablemRNA-proteincorrelationin10additionalstudies
(A–J)Forstudieswithoutexperimentalproteomicreplicates,boxplotsshowingthedistributionsofmRNA-proteincorrelationforproteinsineachdecileofthe
aggregatedproteinreproducibilityranks.(A)–(H)aretheCPTACtumorstudies;(I)istheNCI-60cancercelllinesstudywhereinproteinquantification,usedfor
computingthemRNA-proteincorrelation,isobtainedfromdata-independentacquisition-baseduntargetedproteomics(SWATH-MS);and(J)isthehealthy
tissuesstudyfromtheGTExConsortium.BoxplotdetailsasinFigure2.
CellReportsMethods2,100288,September19,2022 9
ll
Resource
OPENACCESS
A C
B D
Figure5. Proteinreproducibilityismainlyinfluencedbyabundance,variance,anduniquepeptidesandnotproteinhalf-lives
(A–C)Boxplotsshowingthedistributionofaggregatedproteinreproducibilityranksforproteinsbinnedaccordingtoproteinabundance(A),variance(B),and
numberofuniquepeptides(C).BoxplotdetailsasinFigure2.
(D)Boxplotshowingthedistributionofaggregatedproteinreproducibilityranksforproteinswithshortandlongproteinhalf-lives.
Metabolicpathwayswithhigher-than-averagemRNA- thishypothesis,wefirstperformedpathwayenrichmentanalysis
proteincorrelationsmayreflectdifferential onthemRNA-proteincorrelationsfromtheCCLEandovarianda-
reproducibilityratherthandifferentialpost- tasets(STARMethods;Figures7andS7).Consistentwithprevi-
transcriptionalregulation ousstudies,weobservedthatproteinswithhighmRNA-protein
Previousworkhasfoundthatcertainpathwaysandprocesses correlationsareenrichedingenesetsinvolvedinenvironmental
areenrichedinproteinsthathavehigher-orlower-than-average informationprocessingandmetabolicpathways,whileproteins
mRNA-protein correlations. For instance, ribosomal subunits withlowmRNA-proteincorrelationsareenrichedinannotations
have been found to have consistently lower-than-average related to housekeeping protein complexes (Figure 7;
mRNA-proteincorrelationsacrossmultiplestudies(Clarketal., TablesS3andS4).Toassesswhethertheseenrichmentscould
2019;Mertinsetal.,2016;Zhangetal.,2014,2016),whilemem- simply be attributed to variable reproducibility, we next per-
bersofpathwaysrelatedtoaminoacidmetabolismhavebeen formedpathwayenrichmentanalysisontheCCLEandovarian
found to have higher-than-average mRNA-protein correlation mRNA-proteincorrelationdataafteraccountingforvariationin
(Clarketal.,2019;Huangetal.,2021;Jarnuczaketal.,2021;Mer- protein-protein and mRNA-mRNA reproducibility (STAR
tinsetal.,2016;Zhangetal.,2014,2016).Thisvariationacross Methods).Wefoundinbothstudiesthatthe‘‘housekeeping’’pro-
functional groups has been attributed to differential post-tran- teincomplexeswerestillidentifiedasbeingenrichedamongpro-
scriptionalregulation.However,ourobservationthatbothpro- teins with lower-than-average mRNA-protein correlations but
tein-protein measurement reproducibility and mRNA-mRNA thatthemetabolicpathwayswerenolongerenrichedinproteins
measurementreproducibilitycontributesignificantlytothevaria- withhigher-than-averagemRNA-proteincorrelations(Figures7
tioninmRNA-proteincorrelationacrossgenessuggestsanalter- and S7; Tables S3 and S4). Other pathways with higher-than-
nativeexplanation—somepathwaysmayhavehigher-orlower- average mRNA-protein correlations related to environmental
than-average mRNA-protein correlations simply because their informationprocessingwerealsonolongersignificantafterad-
component proteins are more reproducibly measured. To test justing for reproducibility. This suggests that while large
10 CellReportsMethods2,100288,September19,2022
3.0
2.5
2.0
1.5
1.0
0.5
0.0
0.0 0.2 0.4 0.6 0.8 1.0
CCLE - KlijnTranscriptomic Correlation
housekeeping protein complexes such as the ribosome have Aftertakingthisintoaccount,wefoundthatsomepathwayspre-
lower-than-average mRNA-protein correlation that may be viouslyidentifiedashavingahighmRNA-proteincorrelationare
attributedtopost-transcriptionalmechanisms,thehigher-than- likely just more reproducibly measured. We therefore suggest
averagemRNA-proteincorrelationpreviouslyobservedformeta- that conclusions about functional groups with higher or lower
bolicpathwaysmaysimplyreflectmorereproduciblemeasure- mRNA-proteincorrelations,especiallywithregardtothepoten-
mentsoftheirconstituentproteinsandtranscripts. tial role played by post-transcriptional regulation, should be
made only after accounting for variation in the measurement
DISCUSSION reproducibility of their constituent proteins. To this end, we
have generated an aggregate protein reproducibility rank for
Here,wehavedemonstratedthatthereproducibilityofprotein eachproteinthatcanexplainasignificantamountofthevariance
and transcript measurements is a very significant factor in the acrossmultipleproteogenomicstudiesandthatmaybeuseful
observedcorrelationsbetweenmRNAandproteinabundances. for identifying those proteins that can be reliably and
ytisneD
ll
Resource
OPENACCESS
A
Median = 0.75
B
BrCa(2016) Feature
(N=4067)
CCLETranscriptomic
NCI60 Reproducibility
(N=2590)
Aggregated Protein
LUAD Reproducibility Rank
(N=4418)
CCLETranscriptomic +
Colon Aggregated Protein
(N=4014) Reproducibility Rank
HNSCC
(N=4723)
ccRCC
(N=4462)
CRC(2014)
(N=2761)
GBM
(N=4721)
GTEx
(N=4479)
BrCa(2020)
(N=4489)
Ovarian
(N=4231)
EC
(N=4746)
CCLE
(N=4676)
10 15 20 25 30 35 40 45 50
R-squared (%)
Figure6. TranscriptomicreproducibilitycontributestothevarianceinmRNA-proteincorrelation
(A)Histogramshowingthedistributionofthegene-wisecorrelationbetweenexperimentaltranscriptomicreplicatesof382cancercelllines.Theblackline
representsthemedian.
(B)Foreachofthe13studiesanalyzedhere,theR-squaredobtainedbyregressingmRNA-proteincorrelationontranscriptomicreproducibilityandaggregated
proteinreproducibilityscoresindividuallyandincombinationoverthesamesetofproteinsisshowninthedotplot.Thenumberofproteinsanalyzedforeach
studyisindicatedinbracketsbelowthestudyontheyaxis.
CellReportsMethods2,100288,September19,2022 11
ll
Resource
OPENACCESS
CCLE
MedianmRNA-protein correlation
ECM-receptor interaction Environmental Higher
Cell adhesion molecules Information Processing Lower
Butanoate metabolism
Lysine degradation
Tryptophan metabolism
Tyrosine metabolism
Arginine biosynthesis
Glycerolipid metabolism
Arginine and proline metabolism
Biosynthesis of unsaturated fatty acids
Valine, leucine and isoleucine degradation
Phenylalanine metabolism
Glycine, serine and threonine metabolism Metabolism
Galactose metabolism
Glutathione metabolism
Alanine, aspartate and glutamate metabolism
Cysteine and methionine metabolism
Histidine metabolism
Arachidonic acid metabolism
Pyrimidine metabolism
Purine metabolism
Ubiquitin mediated proteolysis
Oxidative phosphorylation
mRNA surveillance pathway
RNA polymerase Genetic
Proteasome Information
Spliceosome Processing
Ribosome
40 20 0 0 20 40
-log10 FDR -log10 FDR
(before) (after)
Figure7. Metabolicpathwayswithhigher-than-averagemRNA-proteincorrelationsmayreflectdifferentialreproducibility
BarchartsdisplayingtheKEGGpathwayenrichmentanalysisoftheCCLEmRNA-proteincorrelationbefore(left)andafter(right)accountingforprotein-protein
andmRNA-mRNAreproducibility.The(cid:3)log ofBenjamini-Hochbergfalsediscoveryrate(FDR)-correctedpvaluescalculatedusingMann-WhitneyUtestis
10
usedtoassessenrichmentforthepathway.Foreachbarchart,thegraylineindicatesthethresholdconsideredforsignificantenrichment(FDR<0.05).Ifthe
enrichmentisbelowthethreshold,thenitisnotconsideredsignificant.ThebarsarecoloredorangeifthemedianmRNA-proteincorrelationofgeneswithinthe
pathwayisgreaterthanthemedianmRNA-proteincorrelationofgenesnotinthepathway;otherwise,thebarsarecoloredblue.
reproducibly measured by mass spectrometry. Such proteins tomesquantifiedfrom‘‘replicates’’ofthesamesample.These
maybemoreusefultoassayin,e.g.,diagnosticpanels. includerealbiologicalvariation(e.g.,tumorheterogeneityresult-
Recently,therehavebeenanumberofattemptstopredictpro- ingintwosamplesofthesametumorhavingdifferentprofiles)
tein abundances from transcriptomic data that have achieved andtechnicalvariation(e.g.,variationinsamplepreparationbe-
modest success (Barzine et al., 2020; Fortelny et al., 2017; Li tweendifferentrunsofthesamesample).Wehavenotbeenable
etal.,2019;Yangetal.,2020).Wefoundherethatproteinsthat toaddresshowmuchofthevarianceinthemeasurementsofin-
aremorereproduciblymeasuredacrossexperimentalreplicates dividualproteinscanbeattributedtotheseglobalfactors.Itis
arebetterpredictedusingmachine-learning.Thissuggeststhat likely that reducing these sources of global variation, e.g.,
one of the factors limiting the accuracy of machine-learning throughautomatedsamplepreparation,willimprovetheoverall
methodstopredictproteinabundancesisthattheproteinabun- reproducibilityofproteinmeasurements.Wenotealsothatour
dance measurements themselves are not reproducible. It may analysesdonotreflectthebestpossiblereproducibilityofprote-
thereforebeworthevaluatingfuturemethodsonthesubsetofpro- omicandtranscriptomicmeasurements,butrathertheyreflect
teinsthatcanbereproduciblymeasured. the reproducibility observed in existing large-scale proteoge-
nomicdatasets.Indeed,weseethatmorerecentproteogenomic
Limitationsofthestudy studieshavehighermRNA-proteincorrelations,suggestingthat
Ouremphasisherehasbeenonunderstandinghowvariabilityin methodologicalimprovementsarealreadyreducingthesources
the measurements of individual proteins can influence the ofnoiseintheseapproaches.
mRNA-proteincorrelationsobservedinpublishedtumorproteo- OurresultsfromanalyzingtheCCLEdataset,wheretherepli-
genomicstudies.Wehaveshownthatproteins/transcriptsthat catecorrelationishighest,givewhatislikelythemostrealistic
aremorereproduciblymeasuredtendtohavehighermRNA-pro- assessmentofproteomicreproducibilityusingmodernMSpipe-
tein correlations, and we have identified a number of factors lines.ThereplicatesintheCCLEstudyweregenerated bythe
(e.g., protein abundance) that influence variation in measure- samelab,usingthesamemethodology,1yearapart.Incontrast,
mentreproducibility.Thereareofcourseadditionalfactorsthat the ovarian cancer study contains replicates generated in
influencetheglobalreproducibilityofproteomesandtranscrip- different labs (introducing significant measurement
12 CellReportsMethods2,100288,September19,2022
ll
Resource
OPENACCESS
heterogeneity),whilethecoloncancerstudymakesuseofrepli- B Proteincomplexmembership
catesgeneratedusingtwoentirelydifferentMSapproaches(la- B Proteinhalf-lives
belfreeversusTMT).Consequently,theselikelyrepresentlower- B Rankaggregation
boundestimatesofthereproducibilitythatcanbeobservedus- B Linearregressionmodels
ing modern MS proteomic pipelines. Nonetheless, they likely B Rankregression
reasonably approximate the non-biological heterogeneity B Pathwayenrichmentanalysis
observedbetweentranscriptomesandproteomesinthestudies d QUANTIFICATIONANDSTATISTICALANALYSIS
analyzed, where mRNA and proteins are quantified separately
usingorthogonaltechniques. SUPPLEMENTALINFORMATION
InthecaseoftheCCLEdata,wehaveasmallnumber(18)of
Supplemental information can be found online at https://doi.org/10.1016/j.
sampleswithreplicateproteomicprofilesavailableandalarger
crmeth.2022.100288.
number (382) with replicate transcriptomes. However, only 8
sampleshavebothreplicatetranscriptomesandreplicatepro- ACKNOWLEDGMENTS
teomes.Havingalargernumberofsampleswithbothreplicate
proteomesandreplicatetranscriptomeswouldallowustobetter S.R.U.wasfundedthroughtheSchoolofComputerScience,UniversityCol-
estimate the actual correlation between mRNA and protein legeDublin,andC.J.R.wasfundedbyIrishResearchCouncilLaureateAwards
acrosssamplesaftercorrectionformeasurementerror,ashas 2017/2018.WethankDr.DirkFey,Dr.GiorgioOliviero,Dr.LuisIglesiasMarti-
nez,andmembersoftheRyanlabforcarefulreadingofthemanuscriptand
previously been done to estimate the true "within sample"
helpfulfeedback.WealsothankDr.TheodorosRoumeliotisforsuggesting
mRNA-protein correlation in yeast (Csa´rdi et al., 2015;
proteinvarianceasafactorinfluencingproteinreproducibility.
Spearman,1904).
Here,wehaveshownthatanumberoffactorsmeasuredusing AUTHORCONTRIBUTIONS
the GTEx dataset, including measured protein abundance,
measured protein variance, and measured unique peptides, Conceptualization,S.R.U.andC.J.R.;methodology,S.R.U.andC.J.R.;formal
areassociatedwithproteomicreproducibilityincancerstudies. analysis, S.R.U.; data curation, S.R.U.; writing – original draft, S.R.U. and
C.J.R.;writing–reviewandediting,C.J.R.;visualization,S.R.U.;supervision,
Acrossstudies,amodelthatincorporatesallthreefactorsout-
C.J.R.;fundingacquisition,C.J.R.
performed models using each variable alone. However, this
may be because all three represent imperfect measurements DECLARATIONOFINTERESTS
of the same underlying variable—real average protein abun-
dance. Previous work has demonstrated that statistical Theauthorsdeclarenocompetinginterests.
modeling that integrates multiple mRNA and protein datasets
andexplicitlytakesintoaccountdifferentsourcesofnoiseand Received:February12,2022
Revised:July14,2022
errorcanbeusedtoprovideimprovedestimatesofmRNA-pro-
Accepted:August16,2022
teincorrelationwithinsamples(Csa´rdietal.,2015).Asadditional
Published:September8,2022
studieswithproteomicreplicatesandtranscriptomicreplicates
become available, it may be possible to develop improved REFERENCES
modelsthatprovidemorereliableestimatesofproteinreproduc-
ibilityandthefactorsthatinfluenceit.Suchestimatescouldbe ’tHoen,P.A.C.,Friedla¨nder,M.R.,Almlo¨f,J.,Sammeth,M.,Pulyakhina,I.,An-
improved through the incorporation of additional estimates of var,S.Y.,Laros,J.F.J.,Buermans,H.P.J.,Karlberg,O.,Bra¨nnvall,M.,etal.
(2013).Reproducibilityofhigh-throughputmRNAandsmallRNAsequencing
average protein abundance and variation (e.g., from Wang
acrosslaboratories.Nat.Biotechnol.31,1015–1022.
etal.,2019).
Aslam,J.A.,andMontague,M.(2001).Modelsformetasearch.InProceedings
of the 24th Annual International ACM SIGIR Conference on Research and
STAR+METHODS DevelopmentinInformationRetrieval(AssociationforComputingMachinery),
pp.276–284.
Detailedmethodsareprovidedintheonlineversionofthispaper Barzine,M.P.,Freivalds,K.,Wright,J.C.,Opmanis,M.,Rituma,D.,Ghavidel,
andincludethefollowing: F.Z.,Jarnuczak,A.F.,Celms,E.,C (cid:2) era(cid:3)ns,K.,Jonassen,I.,etal.(2020).Using
deeplearningtoextrapolateproteinexpressionmeasurements.Proteomics
d KEYRESOURCESTABLE 20,e2000009.
d RESOURCEAVAILABILITY Buccitelli,C.,andSelbach,M.(2020).mRNAs,proteinsandtheemergingprin-
ciplesofgeneexpressioncontrol.Nat.Rev.Genet.21,630–644.
B Leadcontact
B Materialsavailability CancerGenomeAtlasNetwork(2012).Comprehensivemolecularcharacter-
izationofhumancolonandrectalcancer.Nature487,330–337.
B Dataandcodeavailability
CancerGenomeAtlasResearchNetwork(2011).Integratedgenomicanalyses
d METHODDETAILS
ofovariancarcinoma.Nature474,609–615.
B Datacollection
Casey,T.M.,Khan,J.M.,Bringans,S.D.,Koudelka,T.,Takle,P.S.,Downs,
B Pre-processingproteomicandtranscriptomicprofiles
R.A.,Livk,A.,Syme,R.A.,Tan,K.-C.,andLipscombe,R.J.(2017).Analysis
B Computationofcorrelationcoefficient
of reproducibility of proteome coverage and quantitation using isobaric
B Assessing proteomic and transcriptomic reproduc- masstags(iTRAQandTMT).J.ProteomeRes.16,384–392.
ibility Cerami,E.,Gao,J.,Dogrusoz,U.,Gross,B.E.,Sumer,S.O.,Aksoy,B.A.,Ja-
B Computationofdeciles cobsen,A.,Byrne,C.J.,Heuer,M.L.,Larsson,E.,etal.(2012).ThecBiocancer
CellReportsMethods2,100288,September19,2022 13
ll
Resource
OPENACCESS
genomicsportal:anopenplatformforexploringmultidimensionalcancerge- Jiang,L.,Wang,M.,Lin,S.,Jian,R.,Li,X.,Chan,J.,Dong,G.,Fang,H.,Rob-
nomicsdata.CancerDiscov.2,401–404. inson,A.E.,GTExConsortium,etal.(2020).Aquantitativeproteomemapofthe
humanbody.Cell183,269–283.e19.
Ciriello,G.,Gatza,M.L.,Beck,A.H.,Wilkerson,M.D.,Rhie,S.K.,Pastore,A.,
Zhang,H.,McLellan,M.,Yau,C.,Kandoth,C.,etal.(2015).Comprehensive Kanehisa,M.(2019).Towardunderstandingtheoriginandevolutionofcellular
molecularportraitsofinvasivelobularbreastcancer.Cell163,506–519. organisms.ProteinSci.28,1947–1951.
Clark,D.J.,Dhanasekaran,S.M.,Petralia,F.,Pan,J.,Song,X.,Hu,Y.,daVeiga Kanehisa,M.,andGoto,S.(2000).KEGG:kyotoencyclopediaofgenesand
Leprevost,F.,Reva,B.,Lih,T.-S.M.,Chang,H.-Y.,etal.(2019).Integratedpro- genomes.NucleicAcidsRes.28,27–30.
teogenomiccharacterizationofclearcellrenalcellcarcinoma.Cell179,964– Kanehisa,M.,Furumichi,M.,Sato,Y.,Ishiguro-Watanabe,M.,andTanabe,M.
983.e31. (2021).KEGG:integratingvirusesandcellularorganisms.NucleicAcidsRes.
Csa´rdi,G.,Franks,A.,Choi,D.S.,Airoldi,E.M.,andDrummond,D.A.(2015). 49,D545–D551.
Accounting for experimental noise reveals that mRNA levels, amplified by Klijn,C.,Durinck,S.,Stawiski,E.W.,Haverty,P.M.,Jiang,Z.,Liu,H.,Degen-
post-transcriptionalprocesses,largelydeterminesteady-stateproteinlevels hardt,J.,Mayba,O.,Gnad,F.,Liu,J.,etal.(2015).Acomprehensivetranscrip-
inyeast.PLoSGenet.11,e1005206. tionalportraitofhumancancercelllines.Nat.Biotechnol.33,306–312.
Dou,Y.,Kawaler,E.A.,CuiZhou,D.,Gritsenko,M.A.,Huang,C.,Blumenberg, Kolde,R.,Laur,S.,Adler,P.,andVilo,J.(2012).Robustrankaggregationfor
L.,Karpova,A.,Petyuk,V.A.,Savage,S.R.,Satpathy,S.,etal.(2020).Proteo- genelistintegrationandmeta-analysis.Bioinformatics28,573–580.
genomiccharacterizationofendometrialcarcinoma.Cell180,729–748.e26.
Krug,K.,Jaehnig,E.J.,Satpathy,S.,Blumenberg,L.,Karpova,A.,Anurag,M.,
Dwork,C.,Kumar,R.,Naor,M.,andSivakumar,D.(2001).Rankaggregation Miles,G.,Mertins,P.,Geffen,Y.,Tang,L.C.,etal.(2020).Proteogenomicland-
methodsfortheWeb.InProceedingsofthe10thInternationalConference scapeofbreastcancertumorigenesisandtargetedtherapy.Cell183,1436–
onWorldWideWeb(AssociationforComputingMachinery)),pp.613–622. 1456.e31.
Ellis,M.J.,Gillette,M.,Carr,S.A.,Paulovich,A.G.,Smith,R.D.,Rodland,K.K., Li,H.,Siddiqui,O.,Zhang,H.,andGuan,Y.(2019).Jointlearningimproves
Townsend,R.R.,Kinsinger,C.,Mesri,M.,Rodriguez,H.,etal.(2013).Connect- proteinabundancepredictionincancers.BMCBiol.17,107.
inggenomicalterationstocancerbiologywithproteomics:theNCIclinicalpro- Li, J.J., Bickel, P.J., and Biggin, M.D. (2014). System wide analyses have
teomictumoranalysisConsortium.CancerDiscov.3,1108–1112. underestimatedproteinabundancesandtheimportanceoftranscriptionin
Fortelny,N.,Overall,C.M.,Pavlidis,P.,andFreue,G.V.C.(2017).Canwepre- mammals.PeerJ2,e270.
dictproteinfrommRNAlevels?Nature547,E19–E20. Lindgren,C.M.,Adams,D.W.,Kimball,B.,Boekweg,H.,Tayler,S.,Pugh,S.L.,
Franks,A.,Airoldi,E.,andSlavov,N.(2017).Post-transcriptionalregulation andPayne,S.H.(2021).Simplifiedandunifiedaccesstocancerproteoge-
acrosshumantissues.PLoSComput.Biol.13,e1005535. nomicdata.J.ProteomeRes.20,1902–1910.
Gao,J.,Aksoy,B.A.,Dogrusoz,U.,Dresdner,G.,Gross,B.,Sumer,S.O.,Sun, Liu,Y.,Beyer,A.,andAebersold,R.(2016).Onthedependencyofcellularpro-
Y.,Jacobsen,A.,Sinha,R.,Larsson,E.,etal.(2013).Integrativeanalysisof teinlevelsonmRNAabundance.Cell165,535–550.
complex cancer genomics and clinical profiles using the cBioPortal. Sci. Marioni,J.C.,Mason,C.E.,Mane,S.M.,Stephens,M.,andGilad,Y.(2008).
Signal.6,l1. RNA-seq: anassessment oftechnicalreproducibilityandcomparisonwith
Ghandi,M.,Huang,F.W.,Jane´-Valbuena,J.,Kryukov,G.V.,Lo,C.C.,McDo- geneexpressionarrays.GenomeRes.18,1509–1517.
nald,E.R.,3rd,Barretina,J.,Gelfand,E.T.,Bielski,C.M.,Li,H.,etal.(2019). McKinney,W.(2011).pandas:afoundationalPythonlibraryfordataanalysis
Next-generationcharacterizationofthecancercelllineencyclopedia.Nature andstatistics.PythonforHighPerformanceandScientificComputing14.
569,503–508.
Mertins,P.,Mani,D.R.,Ruggles,K.V.,Gillette,M.A.,Clauser,K.R.,Wang,P.,
Gillette,M.A.,Satpathy,S.,Cao,S.,Dhanasekaran,S.M.,Vasaikar,S.V.,Krug, Wang,X.,Qiao,J.W.,Cao,S.,Petralia,F.,etal.(2016).Proteogenomicscon-
K.,Petralia,F.,Li,Y.,Liang,W.-W.,Reva,B.,etal.(2020).Proteogenomic nectssomaticmutationstosignallinginbreastcancer.Nature534,55–62.
characterizationrevealstherapeuticvulnerabilitiesinlungadenocarcinoma.
Nusinow,D.P.,andGygi,S.P.(2020).AGuidetotheQuantitativeProteomic
Cell182,200–225.e35.
Profiles of the Cancer Cell Line Encyclopedia (BioRxiv). https://doi.org/10.
Giurgiu,M.,Reinhard,J.,Brauner,B.,Dunger-Kaltenbach,I.,Fobo,G.,Frish- 1101/2020.02.03.932384.
man,G.,Montrone,C.,andRuepp,A.(2019).CORUM:thecomprehensive Nusinow,D.P.,Szpyt,J.,Ghandi,M.,Rose,C.M.,McDonald,E.R.,3rd,Kaloc-
resource of mammalian protein complexes-2019. Nucleic Acids Res. 47, say,M.,Jane´-Valbuena,J.,Gelfand,E.,Schweppe,D.K.,Jedrychowski,M.,
D559–D563. et al. (2020).Quantitative proteomics of the cancercell line encyclopedia.
Gonc¸alves,E.,Fragoulis,A.,Garcia-Alonso,L.,Cramer,T.,Saez-Rodriguez, Cell180,387–402.e16.
J., and Beltrao, P. (2017). Widespread post-transcriptional attenuation of O } sz,A´.,La´nczky,A.,andGyo}rffy,B.(2021).Survivalanalysisinbreastcancer
genomiccopy-numbervariationincancer.CellSyst.5,386–398.e4. usingproteomicdatafromfourindependentdatasets.Sci.Rep.11,16787.
Guo,T.,Luna,A.,Rajapakse,V.N.,Koh,C.C.,Wu,Z.,Liu,W.,Sun,Y.,Gao,H., Payne,S.H.(2015).TheutilityofproteinandmRNAcorrelation.TrendsBio-
Menden,M.P.,Xu,C.,etal.(2019).Quantitativeproteomelandscapeofthe chem.Sci.40,1–3.
NCI-60cancercelllines.iScience21,664–680.
Ryan,C.J.,Kennedy,S.,Bajrami,I.,Matallanas,D.,andLord,C.J.(2017).A
Harris,C.R.,Millman,K.J.,vanderWalt,S.J.,Gommers,R.,Virtanen,P.,Cour- compendium of Co-regulated protein complexes in breast cancer reveals
napeau,D.,Wieser,E.,Taylor,J.,Berg,S.,Smith,N.J.,etal.(2020).Arraypro- collaterallossevents.CellSyst.5,399–409.e5.
grammingwithNumPy.Nature585,357–362.
Seabold,S.,andPerktold,J.(2010).Statsmodels:econometricandstatistical
Huang,C.,Chen,L.,Savage,S.R.,Eguez,R.V.,Dou,Y.,Li,Y.,daVeigaLep- modelingwithpython.InProceedingsofthe9thPythoninScienceConfer-
revost,F.,Jaehnig,E.J.,Lei,J.T.,Wen,B.,etal.(2021).Proteogenomicin- ence,p.61.
sightsintothebiologyandtreatmentofHPV-negativeheadandnecksqua-
SEQC/MAQC-IIIConsortium(2014).AcomprehensiveassessmentofRNA-
mouscellcarcinoma.CancerCell39,361–379.e16.
seq accuracy, reproducibility and information content by the Sequencing
Hunter,J.D.(2007).Matplotlib:a2DGraphicsenvironment.Comput.Sci.Eng. QualityControlConsortium.Nat.Biotechnol.32,903–914.
9,90–95.
Shenoy,A.,BelugaliNataraj,N.,Perry,G.,LoayzaPuch,F.,Nagel,R.,Marin,I.,
Jarnuczak,A.F.,Najgebauer,H.,Barzine,M.,Kundu,D.J.,Ghavidel,F.,Perez- Balint,N.,Bossel,N.,Pavlovsky,A.,Barshack,I.,etal.(2020).Proteomicpat-
Riverol,Y.,Papatheodorou,I.,Brazma,A.,andVizca´ıno,J.A.(2021).Aninte- ternsassociatedwithresponsetobreastcancerneoadjuvanttreatment.Mol.
gratedlandscapeofproteinexpressioninhumancancer.Sci.Data8,115. Syst.Biol.16,e9443.
14 CellReportsMethods2,100288,September19,2022
