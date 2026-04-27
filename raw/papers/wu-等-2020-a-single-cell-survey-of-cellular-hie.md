---
source_url: zotero://select/items/23ZKCYAJ
ingested: 2026-04-22
sha256: b27951a85e96a7f7
---

# Wu 等 - 2020 - A single-cell survey of cellular hierarchy in acut

> Zotero Item Key: 23ZKCYAJ
> Original File: Wu 等 - 2020 - A single-cell survey of cellular hierarchy in acut.pdf

## Extracted Text

Wuetal.JournalofHematology&Oncology (2020) 13:128
https://doi.org/10.1186/s13045-020-00941-y
RESEARCH Open Access
A single-cell survey of cellular hierarchy in
acute myeloid leukemia
Junqing Wu1,4† , Yanyu Xiao1,4† , Jie Sun3† , Huiyu Sun1,4† , Haide Chen1,4† , Yuanyuan Zhu3, Huarui Fu3,
Chengxuan Yu1,4, Weigao E.1,4, Shujing Lai1,4, Lifeng Ma1,4, Jiaqi Li1,4, Lijiang Fei1,4, Mengmeng Jiang1,4,
Jingjing Wang1,4, Fang Ye1,4, Renying Wang1,4, Ziming Zhou1,4, Guodong Zhang1,4, Tingyue Zhang1,4, Qiong Ding5,
Zou Wang5, Sheng Hao5, Lizhen Liu3, Weiyan Zheng3, Jingsong He3, Weijia Huang3, Yungui Wang2, Jin Xie6,
Tiefeng Li7, Tao Cheng8,9, Xiaoping Han1,4,10*, He Huang2,3,4,9,10* and Guoji Guo1,2,4,9,10*
Abstract
Background: Acutemyeloidleukemia(AML)isafatalhematopoieticmalignancyandhasaprognosisthatvarieswith
itsgeneticcomplexity.However,therehasbeennoappropriateintegrativeanalysisonthehierarchyofdifferentAML
subtypes.
Methods:UsingMicrowell-seq,ahigh-throughputsingle-cellmRNAsequencingplatform,weanalyzedthecellular
hierarchyofbonemarrowsamplesfrom40patientsand3healthydonors.Wealsousedsingle-cellsingle-molecule
real-time(SMRT)sequencingtoinvestigatetheclonalheterogeneityofAMLcells.
Results:Fromtheintegrativeanalysisof191727AMLcells,weestablishedasingle-cellAMLlandscapeandidentified
anAMLprogenitorcellclusterwithnovelAMLmarkers.Patientswithribosomalproteinhighprogenitorcellshada
lowremissionrate.WededucedtwotypesofAMLwithdiverseclinicaloutcomes.Wetracedmitochondrialmutations
intheAMLlandscapebycombiningMicrowell-seqwithSMRTsequencing.Weproposetheexistenceofaphenotypic
“cancerattractor”thatmighthelptodefineacommonphenotypeforAMLprogenitorcells.Finally,weexploredthe
potentialdrugtargetsbymakingcomparisonsbetweentheAMLlandscapeandtheHumanCellLandscape.
Conclusions:WeidentifiedakeyAMLprogenitorcellcluster.Ahighribosomalproteingenelevelindicatesthepoor
prognosis.WededucedtwotypesofAMLandexploredthepotentialdrugtargets.Ourresultssuggesttheexistenceof
acancerattractor.
Keywords:Acutemyeloidleukemia,Single-cellmRNAsequencing,Microwell-seq,Ribosomalprotein,Single-molecule
real-timesequencing,Cancerattractor
*Correspondence:xhan@zju.edu.cn;huanghe@zju.edu.cn;ggj@zju.edu.cn
†JunqingWu,YanyuXiao,JieSun,HuiyuSunandHaideChencontributed
equallytothiswork.
1CenterforStemCellandRegenerativeMedicine,TheFirstAffiliatedHospital,
ZhejiangUniversitySchoolofMedicine,Hangzhou310058,China
2InstituteofHematology,TheFirstAffiliatedHospital,ZhejiangUniversity
SchoolofMedicine,Hangzhou310003,China
Fulllistofauthorinformationisavailableattheendofthearticle
©TheAuthor(s).2020OpenAccessThisarticleislicensedunderaCreativeCommonsAttribution4.0InternationalLicense,
whichpermitsuse,sharing,adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreativeCommonslicence,andindicateif
changesweremade.Theimagesorotherthirdpartymaterialinthisarticleareincludedinthearticle'sCreativeCommons
licence,unlessindicatedotherwiseinacreditlinetothematerial.Ifmaterialisnotincludedinthearticle'sCreativeCommons
licenceandyourintendeduseisnotpermittedbystatutoryregulationorexceedsthepermitteduse,youwillneedtoobtain
permissiondirectlyfromthecopyrightholder.Toviewacopyofthislicence,visithttp://creativecommons.org/licenses/by/4.0/.
TheCreativeCommonsPublicDomainDedicationwaiver(http://creativecommons.org/publicdomain/zero/1.0/)appliestothe
datamadeavailableinthisarticle,unlessotherwisestatedinacreditlinetothedata.
Wuetal.JournalofHematology&Oncology (2020) 13:128 Page2of19
Introduction cluster was associated with a dysregulation of RPs and
Acute myeloid leukemia (AML) is a hematopoietic ma- revealed that patients with RP high progenitor cells had
lignancy with recurrent genetic abnormalities [1, 2]. a low remission rate. We deduced two types of AML
New therapeutic options such as targeted therapies and with diverse clinical outcomes. We suggested the exist-
monoclonal antibodies may improve the long-term sur- ence of a phenotypic “cancer attractor” that might help
vival in patients with AML [3, 4]. However, the progno- todefineacommonphenotype forAMLprogenitorcells
sis of AML remains poorin some patients, suggesting its by combining Microwell-seq with SMRT sequencing. Fi-
genetic and cellular complexity [5–7]. Therefore, it is of nally, we investigated the potential targets by making
great importance to understand the major hierarchy and comparisons with the Human Cell Landscape. These
cellularcompositionsindifferent individualswith AML. datasets have deepened our understanding and might
Flow cytometry is widely used for exploring cell het- open a way for novel diagnostic and therapeutic strat-
erogeneity in leukemia; however, it is limited to the egies inAML.
choice of surface markers [8]. Bulk population sequen-
cing can probe into the cell genome and transcriptome,
Results
but misses the information of individual cells. Moreover,
AnalysisofnormalBMMChierarchy
integrative analyses of samples from different patients
To gain insights into the heterogeneity of normal and
with leukemia prove difficult, due to a lack of assay
malignant hematopoiesis, we first profiled the hetero-
consistency and precision. The advances in single-cell
geneity in normal BMMCs. We used Microwell-seq on
techniques have made systematic analyses of leukemia
three healthy donors and established the analysis pipe-
cells possible [9, 10]. Several studies have applied single-
line (Fig. S1A) [21]. We performed t-Distributed sto-
cell analysis to normal and malignant hematopoietic
chastic neighbor embedding (t-SNE) analysis of
cells [11–13]. However,becauseof thelimited scales and
individuals(Fig. S1BandSupplementaryTable 1).The t-
technical consistency in these studies, an overall picture
SNE map of 8561 normal BMMCs of three healthy do-
of AML and the common hierarchy among different pa-
nors is shown in Fig. 1a, b. According to the gene ex-
tients havenotyetbeendescribed.
pression patterns, we identified lymphoid, erythroid, and
One hallmark of cancer is the reprogramming of en-
myeloid lineages (Fig. 1a, c and Supplementary Table 2)
ergy metabolism to fuel cell growth and division [14].
[22, 23]. Neutrophils are divided into three main types,
Ribosome biogenesis is an energy-demanding process,
neutrophil A, B, and C, along with three extended types,
and it has been proposed that ribosomal proteins (RPs)
neutrophil D, E, and F (Fig. S2A and Supplementary
have an effect on tumorigenesis [15]. A previous study
Table 2). The related marker genes are shown in Fig.
reported that RPs exhibited strong dysregulation in par-
S2B,C.
ticular cancer types, such as breast cancer, melanoma,
To performlineagetrajectoryanalyses,weintegratedan-
and thyroid carcinoma [16]. Some RPs are involved in
other 2000 hematopoietic stem/progenitor cells (HSPCs)
the specification of hematopoietic lineages, and their al-
and 2719 peripheral blood mononuclear cells (PBMCs)
terations lead to hematologic disorders, like Diamond-
fromourpreviousstudytogetatotalof13280healthycells
Blackfan anemia, Chromosome 5q deletion syndrome,
[24]. Using partition-based graph abstraction (PAGA), we
and Shwachman-Diamond syndrome [17, 18]. However,
revealed distinct developmental branches and built a tran-
there is a lack of knowledge on the dysregulation of RPs
scriptional landscape for normal human hematopoiesis
inAML.
(Fig. 1d-f and Supplementary Table 3). The expression
Mitochondrial mutations can suggest clonal relation-
levels ofmarker genes change in themyeloid path, incon-
ships [19]. They may preserve information about cell
formitytothet-SNEanalysesabove(Fig.1g).
lineage relationships at single-cell resolution [20]. How-
ever, no study has examined single-cell mitochondrial
mutations in AML to explore the relationship between IdentifyingtheprogenitorcellclusterofdenovoAMLs
clonotype andphenotype. We then moved on to understand the cellular hier-
Herein using Microwell-seq, we analyzed 191727 si

... [truncated]
