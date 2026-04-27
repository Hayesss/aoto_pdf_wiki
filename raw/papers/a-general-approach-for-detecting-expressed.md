---
source_path: /mnt/c/Users/Administrator/Zotero/storage/BF8Q4JNE/Petti 等 - 2019 - A general approach for detecting expressed mutations in AML cells using single cell RNA-sequencing.pdf
ingested: 2026-04-23
sha256: cb88666d657f9460
---

ARTICLE
OPEN
https://doi.org/10.1038/s41467-019-11591-1
A general approach for detecting expressed
mutations in AML cells using single cell
RNA-sequencing
Allegra A. Petti 1,2,7, Stephen R. Williams3,7, Christopher A. Miller1,2, Ian T. Fiddes3, Sridhar N. Srivatsan1,
David Y. Chen4, Catrina C. Fronick2, Robert S. Fulton2, Deanna M. Church 5 & Timothy J. Ley1,2,6
Virtuallyalltumorsaregeneticallyheterogeneous,containingmutationally-definedsubclonal
cell populations that often have distinct phenotypes. Single-cell RNA-sequencing has
revealed that a variety of tumors are also transcriptionally heterogeneous, but the relation-
ship between expression heterogeneity and subclonal architecture is unclear. Here, we
addressthisquestioninthecontextofAcuteMyeloidLeukemia(AML)byintegratingwhole
genome sequencing with single-cell RNA-sequencing (using the 10x Genomics Chromium
SingleCell5’GeneExpressionworkflow).ApplyingthisapproachtofivecryopreservedAML
samples, we identify hundreds to thousands of cells containing tumor-specific mutations in
each case, and use the results to distinguish AML cells (including normal-karyotype AML
cells)fromnormalcells,identifyexpressionsignaturesassociatedwithsubclonalmutations,
and find cell surface markers that could be used to purify subclones for further study. This
integrative approach for connecting genotype to phenotype is broadly applicable to any
sample that is phenotypically and genetically heterogeneous.
1DivisionofOncology,WashingtonUniversitySchoolofMedicine,St.Louis,MO,USA.2McDonnellGenomeInstitute,WashingtonUniversitySchoolof
Medicine,St.Louis,MO,USA.310xGenomics,Inc.,Pleasanton,CA,USA.4DivisionofDermatology,WashingtonUniversitySchoolofMedicine,St.Louis,
MO,USA.5Inscripta,Inc.,Boulder,CO,USA.6DepartmentofGenetics,WashingtonUniversitySchoolofMedicine,St.Louis,MO,USA.7Theseauthors
contributedequally:AllegraA.Petti,StephenR.Williams.CorrespondenceandrequestsformaterialsshouldbeaddressedtoT.J.L.(email:timley@wustl.edu)
NATURECOMMUNICATIONS| (2019) 10:3660 | https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications 1
;,:)(0987654321
There are amendments to this paper
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
C
onnectinggenotypetophenotypeatthesingle-celllevelis each case, and bulk RNA-sequencing was used to determine
widely appreciated as a central challenge in the analysis which mutations were expressed in each tumor sample
and interpretation of scRNA-seq data, with applications (Methods)25. eWGS (Fig. 1a) revealed that these cases were
ranging from cell lineage tracing1 and eQTL discovery2, to the genetically representative of AML, containing on average 26
analysis of subclonal architecture in
tumors3–14.
In cancer, mutations within coding regions, with many in well-established
mutationally distinct subclones can differ with respect to key driver genes (e.g. DNMT3A, FLT3, NPM1, TP53, NRAS, IDH1,
clinical properties such as drug sensitivity and growth rate, and CEBPA,etc.).Todefinetheclonalarchitectureofeachtumor,the
this phenotypic diversity may contribute to drug resistance and SciClone algorithm26 was used to cluster mutations and infer
tumor evolution15. However, it is currently difficult to purify subclones. At least one subclone was identified in every case
individual subclones for use in downstream studies that address (Table 1, Supplementary Data 1)23. Bulk RNA-sequencing
the biological basis of these differences. Meanwhile, a growing showed that on average, fewer than half of the mutations detec-
body of work has demonstrated that tumors are also tran- ted by eWGS were expressed (Table 1).
scriptionally heterogeneous, but it has been challenging to relate
t d h u i a s l ep tu ig m en or e s ti 3 c –1 h 4, e 1 t 6 e . ro W ge e ne s i o ty ug t h o t ge to net a i d c d h r e e t s e s ro t g h e i n s ei c t h y al i l n en i g n e div b i y - c S o in m g p le a - r c e e d ll ge t n ra o n m sc e r - i w p i t de co tr v a e n r s a c g r e ipt a c n o d ve r r e a p ge re o s b en ta t i a n t e io d n f . ro W m e th fi e r 5 st ′
detecting cells that express somatic single nucleotide variants (v1) and 3′ (v2) 10x Genomics Chromium Single Cell Gene
(SN D V et s e ) ct in ing sc g R e N n A et - ic se v q a d ri a a t n a t . s in scRNA-seq reads is difficult due t E w x o pre s s c s R io N n A w -s o e r q kfl l o ib w ra s. ri F e o s r w o i n th e c e a a s c e h , U w P o N rk 5 fl 0 o 8 w 0 , 84 a , n w d e s g e e q n u e e r n a c te e d d
to the low transcript abundance, allelic dropout, and incomplete
them tohighdepth,targeting200,000reads/cell.Transcriptome-
transcript coverage inherent to this platform. Despite these
wide coverage for each data set was assessed using 20,090 genes,
challenges, previous studies of intratumoral heterogeneity each having one annotated isoform (Methods). Both workflows
have demonstrated that single-cell copy number alterations yielded consistent low-level coverage at least 10kbp from the 5′
(CNAs) can be robustly detected in full-length cDNAs, com- and3′endsoftheaveragetranscript(Fig.1b).However,the5′kit
monlygeneratedusingtheFluidigmC1/SMART-seqplatform,in
dozens3–5,7 to hundreds6,8,10,11,14,17,18 of cells per tumor, and yielded slightly higher transcript-wide coverage in distal regions
oftranscripts.Fortheaveragegeneassayedusingthatkit,atleast
specialized tools have been developed for this purpose12,19.
2.5% of the unique sequenced transcripts mapped to any given
O
de
t
t
h
e
e
c
r
t
s
sp
h
e
a
c
v
i
e
fic
bu
m
il
u
t
ta
u
t
p
io
o
n
n
s
p
w
la
it
t
h
e-
v
b
a
a
r
s
i
e
a
d
bl
s
e
c
s
R
e
N
ns
A
it
-
i
s
v
e
i
q
ty2
t
0
e
,
c
2
h
1.
nologies to baseupto10kbpawayfromthe5′transcriptionstartsiteofthe
gene. Coverage metrics for 200 cancer-relevant genes are sum-
The ability to detect CNAs in single cells has advanced the
marized in Supplementary Data 2 and provided at nucleotide
study of cancers where structural alterations and/or aneuploidy
arecommon3–10,13,14,18.However,CNAsarerareinsometumor resolution at https://github.com/genome/scrna_mutations. Sub-
sequent sequencing and analyses were performed using only the
types, such as AML22,23. Moreover, CNAs rarely capture the 5′ workflow application.
complete subclonal complexity of any tumor, and are often
We then asked whether bulk and single-cell RNA-seq data
subclonal progression-associated events24. The ability to detect
capturethesametranscriptstructureforthemutatedgenesinthis
multiple,arbitrarySNVsinscRNA-seqreadsisanidealattribute
study. Using one canonical isoform for each gene, we compared
for any generally-applicable approach to the study of intratu-
coverage in the single-cell data (unique barcode/UMI pairs at
m
th
o
at
ra
s
l
o
h
m
e
e
ter
S
o
N
g
V
en
s
ei
c
t
a
y
n
. A
b
l
e
th
id
ou
en
g
t
h
ifi
p
e
r
d
ev
f
i
r
o
o
u
m
s s
f
t
u
u
l
d
l-
i
l
e
e
s
ng
h
t
a
h
ve
cD
es
N
ta
A
b
s
li
,
sh
lo
e
w
d eachposition)tothatinthebulkRNA-seqdata(quantifiedusing
numbers of identified mutant cells made downstream analyses bamCoverage and 1bp bins), and visualized it using the UCSC
dif I fi n cu w lt o 4 r ,5 k ,1 in 4. g with the 10x Genomics Chromium Single Cell 3′ G ea e c n h o g m e e ne B s r t o u w d s ie e d r , ( b M u e lk th - o a d n s d ). s T in h g e le- r c e e su ll lt d s at d a em id o e n n s ti t fi ra e t d e t t h h e at s , am fo e r
(v2) and 5′ (v1) Gene Expression workflows, we observed setoftranscripts(Fig.1c).Coverageplotsforallmutatedgenesin
sequence coverage far from the 3′ and 5′ ends of genes (respec- this study are provided at https://github.com/genome/
scrna_mutations.
tively).Thiswasunexpected,giventheend-biasoftheChromium
librarydesign,andraisedthepossibilitythattheresultingscRNA-
seqdatacouldbeusedforvariantdetection.Becausethisplatform Mutation identification in single cells. We next sought to
can sample up to 10,000 cells per library, we hypothesized that identify cells containing any of the somatic variants discovered
even sparse transcript coverage – which would permit the iden- usingeWGS.ForeachcellandeachvariantpositionintheeWGS
tification of mutations in a fraction of cells – might allow us to data, unique wild-type, and mutant reads were counted using
combine variant detection with high-throughput transcriptome cb_sniffer, a tool that extends the PySam library to do barcode-
characterization. Here, we evaluate the utility of 10x scRNA-seq aware pileups (see Methods: https://github.com/genome/
data for somatic variant detection in cryopreserved AML bone cb_sniffer). In most high-throughput scRNA-seq datasets, the
marrow samples. Because genome sequencing of paired tumor/ median gene is represented in the median cell by one transcript
normal samples is the gold standard for de novo discovery of read.Consistentwiththis,mostSNVlocationswerecoveredbya
somatic mutations and inference of subclonal architecture, we single read in most cells (although SNVs in several highly
firstuse“enhanced”whole-genomesequencing(eWGS)ofpaired expressed, high-coverage genes (e.g. U2AF1, NPM1, SRSF2, and
tumor/normal samples to discover somatic mutations, and then NRAS) were more likely to have multiple reads per cell) (Sup-
focus on detecting those mutations in the scRNA-seq data. plementaryFig.1a).Foraheterozygousmutation,therefore,there
isa50%chancethattheobservedtranscriptismutant,anda50%
chancethatitiswild-type,leadingtothephenomenonknownas
Results allelic dropout. This has two main consequences: first, it is
eWGS and bulk RNA-sequencing. Four cases of de novo AML impossible to conclude that a cell is wild-type; secondly, the
and one of secondary AML were selected for study (clinical sensitivity of mutation detection is reduced by a factor of two.
details in https://github.com/genome/scrna_mutations). eWGS Therefore,barringsequencingerrors,onecaninprincipleclassify
was used in conjunction with well-established variant detection a cell’s genotype as “mutant” if it contains one or more mutant
pipelines to generate a set of high-confidence mutation calls for transcripts, and “unknown” if it does not. We measured the
2 NATURECOMMUNICATIONS| (2019) 10:3660 |https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications
a b
0.25
0.20
0.15
0.10
0.05 0.00
d
Single-cell RNA barcode depth Bulk RNA depth Mutation location
1300
TP53 0
508084 0
400
4300
NPM1 0
548327 0
2200
1800
GATA2 0 721214 0
600
700
DNMT3A 0
721214 0
150
frequencyoffalsepositivesoriginatingfromsequencingerrorsby depending on the sample), a small fraction of cells in each case
examining thepositionsof knownsomatic mutationsinsamples containedmultiplemutations,particularlywhenafoundingclone
that did not harbor those mutations. The false-positive rate (the mutation was readily detectable (Table 2). Specifically, two
rate at which wild-type UMIs are called mutant in the control mutationswerefoundin1.6–12%ofthemutantcellsinasample;
samples)wassite-specific,andhadamaximumrateofonly0.39% three mutations were found in 0.21–0.29% of mutant cells; and
(Supplementary Data 3). We also searched for these variants in fourmutationswerefoundinonecell(0.012%)insample721214.
8057bonemarrowcellsfromfourhealthydonors,andfoundno The observed mutation combinations were consistent with the
false positives. known subclonal architecture (although the mutation data was
Wethereforelabeledacell“mutant”ifitcontainedatleastone generally not dense enough for accurate de novo subclonal
variant-containing read, and “unknown” if only wild-type reads inference). For example, case 548327 contained an NPM1W288fs
or no reads were detected. We found an average of 49 mutant mutation in the founding clone, and several hundred cells
cells per variant (range: 1–3944), and 3732 mutant cells (22% of contained both this mutation and one subclonal mutation. Case
thetotalcells)persample,butthisvariedwidelyamongsamples 721214iscomposedofthreesubclonessequentiallynestedwithin
(range: 396–8200, or 1.8–52%), depending on the mutations the founding clone. One cell was found to have one mutation
present in each (Table 1). Most mutant cells contained one from each (sub)clone.
detectedmutation,withonereadmappingtothevariantposition Mutationdetectioninsinglecellswascomparedtothatinbulk
(Supplementary Fig. 1). Founding clone mutations, subclonal RNA-seq and eWGS data using a read-based metric, “single-cell
mutations,andputativedrivermutationsweredetectableineach VariantAlleleFrequency”(scVAF),whichenabledustocompare
case, and these included SNVs, insertions and deletions (indels, VAFsacrossdatatypes,andtwocell-basedmetrics,“MutantCell
including FLT3-ITD and NPMc), and one gene fusion (NUP98- Fraction” (MCF) and “Mutant Cell Detection Rate” (MCDR),
NSD1) (Table 1, Supplementary Data 1). Although the vast which allowed us to measure and compare the sensitivity of
majority of mutant cells contained only one mutation (88–98%, mutant cell identification (Methods). In terms of mutant reads,
noitcarf
IMU/BC
3′ scRNAseq assay
5′ scRNAseq assay
0.25 10kb
0.20 0.15
0.10
0.05
0.00
noitcarf
IMU/BC
1.00
0.75
0.50
0.25
0.00
0.00 0.25 0.50 0.75
WGS VAF
FAV
ANR
1
0.1
0.01
0.001
0
0.000.250.500.751.00
Bulk RNA VAF
etar
noitceted
llec
tnatuM
1.00
0.75
0.50
0.25
0.00
0.00 0.25 0.50 0.75
WGS VAF
noitcarf
llec
tnatuM
Library Sequencing Data Integration
preparation processing
C A r M y c o e L p l l p s re a f s t r i o e e m r n v t e s d Sin G g E le M c s ell ∼ ∼ 3 2 b 0 i , l 0 lio 0 n 0 r c e e a ll d s s B T a ra rc n A o s l d c ig e ri n p p t r r e c o a o c d u e s n ss ti i n n g g
Cells
RN D A NA ∼45x W co G v S erage 5 2 0 5 va A r l i i a g n n t r c e a a l d lin s g 0
RN B A u - l S k eq –25
−50 −25 0 25 50
c
2_ENSt
Mutant cell identification
tSNE_1
1
0.1
0.01
0.001
0
0 2500 5000 7500 10,000
cDNA Position
etar
noitceted
llec
tnatuM
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
5′ 10kb 3′
c
5′ 3′
Fig.1Workflow,coverage,andperformancemetricsforvariantdetectioninsinglecells.aCryopreservedbonemarrowcellsfromAMLpatientsunderwent
eWGS,bulkRNA-seq,andscRNA-seq.SomaticmutationswerediscoveredusingeWGSdata,identifiedinindividualcellsusingscRNA-seqdata,and
interpretedinthecontextofexpressionheterogeneity.bFractionofuniquetranscripts(molecules)whosereadsmaptoanygivenpositionupto10kbp
awayfromthecapturesiteinboththe5’and3’kits.cComparisonofsingle-cellandbulkRNA-seqcoveragedataforspecificgenesofinterest.
dRelationshipbetweenRNAandeWGSVAF;dependenceofMutantCellFractiononeWGSVAF;dependenceofMutantCellDetectionRateonbulkRNA
VAF,anddependenceofMutantCellDetectionRateonpositionofthemutationinthecDNA
NATURECOMMUNICATIONS| (2019) 10:3660 |https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications 3
atad
qes-ANRcs
dnaSGWeni
noitceteddna
yrevocsidnoitatum
foweivrevO1
elbaT
]DS[naeM
356908
823287
412127
723845
480805
elpmaS
]9793[569,71
830,12
137,12
474,02
026,11
469,41
sllec.oN
]547,26[298,322
157,981
482,412
530,671
569,643
724,291
llec/sdaeR
]92.4[78
09
8.97
2.29
2.78
9.48
deppamsdaeR otyltnedfinoc
)%(emoneg
]40.4[66
8.86
9.16
37
7.36
2.46
deppamsdaeR otyltnedfinoc
)%(emotpircsnart
]824[1581
9281
6731
0622
3831
5042
detcetedsenegnaideM
llecrep
]1401[304,32
201,32
983,52
673,32
305,22
546,22
detcetedseneglatoT
4.62
82
13
14
31
91
stnairavSGW
6.9
8
7
81
5
01
SGWdesserpxE
)klub(stnairav
4.01
8
21
71
7
8
stnairavqes-ANRcs
%711
%001
%071
%49
%041
%08
desserpxeegatnecreP
stnairavSGW
-ANRcsniderevocsid
qes
2373
163
4533
5794
1753
966
sllectnatumlatoT
7402–4.3
702–1
9162–1
4493–1
2103–1
354–31
tnairavrepsllectnatuM
5.84
5.12
111
03
84
23
tnairavrepsllectnatuM
)naidem(
A/N
)2141(D21GSARN
)949(S21GSARN
)904(H288RA3TMND
)811(H231R1HDI
)051(M616VBKBKI
.on(stnairavSGWyeK
)932(G682E35PT
)159(D21GSARN
)974(DTI-3TLF
)1955(sf882W1MPN
)707(DTI-3TLF
qes-ANRcshtiwsllec
sf241RAPBEC
)9054(F43S1FA2U
)603(L216F3TLF
)9432(H59P2FSRS
)1(1SDN-89PUN
tnairavtaegarevoc
)48(
)276,11(sf882W1MPN
)noitisop
)9261(C163R2ATAG
A/N
)612(K436EULGAN
)301(01FNR
htiwstnairavlanoitiddA
erutangisnoisserpxe htiwsllecforebmun(
)egarevoc
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
4 NATURECOMMUNICATIONS| (2019) 10:3660 | https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
Table2 Frequencyof cellscontainingmultiple mutations ineachcase
Sample 508084 548327 721214 782328 809653
Totalmutantcells 669 3571 4975 3354 361
1mutation(%) 658(98) 3280(92) 4694(94) 3176(95) 354(98)
2mutations(%) 11(1.6) 460(13) 268(5.4) 171(5.1) 7(1.9)
3mutations(%) 0 11(0.31) 12(0.24) 7(0.21) 0
4mutations(%) 0 0 1(0.02) 0 0
thesensitivityofmutationdetectionwascomparableinsinglecell We first used principal component analysis to summarize the
and bulk RNA-seq data: on average, a slightly higher fraction of expression heterogeneity in each case (Methods) to better
known mutations was detected in the scRNA-seq data, but not understand the composition of each sample. As expected, this
necessarily in a large number of cells (Table 1). We then revealed complex relationships among clusters (such as partially
examined the relationship between bulk VAF (either eWGS or overlapping expression signatures), and multiple sources of
bulk RNA-seq) and single-cell VAF (scVAF) and detection heterogeneity in all samples, including variable expression of
sensitivity (MCF): for expressed mutations that were identifiable known hematopoietic cell-type markers (e.g. CD3D (T-cells),
in bulk and single-cell RNA-seq data, single-cell MCFs and CD79A, or CD19 (B-cells), and HBA1 (erythrocytes)), cell cycle
scVAFs were more highly correlated with eWGS VAFs (r=0.69 genes (e.g. TUBA1B, TOP2A), markers of myeloid lineage (e.g.
and 0.68, respectively) than were bulk RNA VAFs (r=0.52; AZU1, ELANE, MPO, PRTN3), mitochondrial genes, and
Table 1). scVAFs were positively correlated with bulk RNA-seq ribosomalgenes(Fig.2a,b;SupplementaryFig.2–5,Supplemen-
VAFs (r=0.34; Fig. 1d, Supplementary Fig. 1c). Although taryData4).Thisindicatedthatthedistributionofcelltypesisa
mutation-detection in scRNA-seq is sensitive from a read-based major source of expression heterogeneity, and varies among
perspective, sensitivity from a cell-based perspective is very low samples, as expected.
and mutation-specific; we identified only a small fraction of the To investigate sample composition in a more unsupervised
cellsthatwouldbeexpectedtocontainmutationsbasedoneWGS manner, we identified the nearest hematopoietic lineage of each
VAFs (MCDR, Fig. 1d). This fraction depends on multiple cellbymatchingeachcell’sexpressionprofiletothemostsimilar
variables, including bulk RNA VAF, distance from the 5′ end of lineage-specific expression profile in the DMAP database27
the transcript, and single-cell gene expression (Fig. 1d, Supple- (Methods, Figs. 3c and 4). The inferred sample composition
mentary Fig. 1c, d). varied widely among subjects, particularly with respect to the
The ability to detect mutations in scRNA-seq data therefore fraction of lineage-defined cells (e.g. cells resembling myelomo-
depends on a number of variables, including VAF, expression nocytic cells, T-cells, B-cells, and erythrocytes). All five samples
level of the mutated gene, position of the mutation in the contained clusters of immature cells, including cells resembling
transcript, sequencing depth, fraction of tumor cells in the hematopoietic stem cells (HSCs), common myeloid progenitors
sample,andnumberofcellssequenced.Theprobabilityoffinding (CMPs), and megakaryocyte-erythroid progenitors (MEPs),
atleastonecellcontainingaparticularheterozygousmutationm which could represent either immature non-malignant cells or
is approximately: AML cells.
Toclarifytheidentityoftheseclusters,wecombinedsingle-cell
PðmÞ¼naðf½1(cid:2)ð1(cid:2)ctÞr(cid:3)þð1(cid:2)fÞeÞ(cid:4)nafrctþnað1(cid:2)fÞe mutation detection with expression-based clustering and lineage
inference. Using the bone marrow sample from 809653 (which
ð1Þ
contained many non-AML cells, based on morphology and flow
cytometry) we overlaid mutation data on the t-SNE projections
Where f is twice the variant allele frequency of the mutation in by highlighting mutant cells (Fig. 3e–g). A highly expressed
theeWGSdata,tistherelativeexpressionlevelofthegene(e.g.in germline SNP in the BAG1 gene served as a positive control,
countspermillion),ristheaveragenumberofUMIspermutant markingSNP-containingcellsinallexpressionclusters(Fig.3h).
cell, c is the fraction of UMIs that have coverage at the mutant ByscRNA-seq,wedetectedcellsexpressingmutationsin8genes,
position, e is the site-specific false-positive rate (frequency with including TP53, NRAS, and CEBPA (Table 1, Supplementary
whichawild-typecelliscalledmutant),aisthefractionofcellsin Data 1). Several clusters were significantly enriched (p≤0.05,
thesamplethataretumorcells,andnisthetotalnumberofcells one-sided Fisher exact test) for mutant cells; other cells in these
sequenced. clusters presumably contained undetected mutations in these
genes (Fig. 3b–g). Two of these clusters were composed of cells
Using SNVs to distinguish between tumor and normal cells. that had stem/progenitor expression signatures (HSCs and
Single-cellCNAdetectionisoftenusedtoidentifytumorcellsin MEPs). The other two were composed of cells expressing
samples that contain a mixture of tumor and normal cells, but erythrocyte or monocyte markers; in terms of gene expression,
sensitivity is limited by the fact that CNAs are frequently sub- theseclustersaredistinctfromnormalcellclusters,buttheycould
clonal, even in the (non-AML) tumors that contain them24. not have been labeled as AML-derived using expression
Therefore,weinvestigatedtheutilityofsingle-cellSNVdetection data alone.
for this purpose. A straightforward approach would involve This was the only case with multiple CNAs, allowing us to
selectingonlythosecellsthatcontainamutation;wedetectedan benchmark SNV-based cell classification against the better-
average of 3732 mutant cells per sample (Table 1). Despite the established CNA-based methods. CONICSmat19 was used to
wide range (396–8200), this is substantially more than the total identifycellscontainingtheCNAsdiscoveredbyeWGS,andhigh
numberofcells/sampleanalyzedinprevioussingle-cellmutation-
concordancewasobservedwithSNV/expression-basedclassifica-
detection studies3–10,13,14. However, we retained the additional tion of AML cells: 95.5% of cells classified as AML by copy
cells in each sample (which contained valuable expression number were also classified as AML by SNV and expression
information), and instead used single-cell SNVs as markers for signature (Fig. 2c). Conversely, 94.9% of cells classified as AML
tumor vs. wild-type cell clusters. by SNVs and expression were confirmed by CNA analysis. This
NATURECOMMUNICATIONS| (2019) 10:3660 | https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications 5
a
50
9 1617
11
25 3 18 2 13
12 8 15 7
14 0 10
6
1 4
0 −25
5
−50 −25 0 25 50
tSNE_1
2_ENSt
b
0
1
10
11
12
13 14
15
16
17 18
2
3
4
5
6
7
8
9
1 0 31 4 6 61 9 71 7 11 3 8 41 2 81 51 21 5 01
809653
AML clusters
AML PCSK1N
cells AML T C K O L 1 C 0 R o 3 1 r A f1 I 0 P2
cells A C H A S 1 P
S H L B C A 2 1 5A37 Red blood cell
A H L B A D S2 differentiation CHST2 HMBS SELENBP1
EPB42 SLC4A1
CFAP161 ARG2 CALCRL
AJ006998.2 SPINK2 ANGPT1 CYTL1
ADGRG1 NPW
IGLL1
GATA2
FCER1A
TPSD1
TPSAB1 TPSB2 MS4A3
CSF2RB
CEBPD
RNASE2
MCEMP1
S100A9
S100A8 RETN
AML cells M FC N E D R A 1G Granulocyte,
M CL S E 4 C A 1 6 0 A A neutrophil
L C Y S Z T3 migration LMNA
SERPINA1
FCN1
CD300E
APOBEC3A
c TPPP3
PADI4
CD1C 50 P P L P D P 4 1R14A
CTSG Myeloid
MPO
PRTN3 differentiation
AZU1
IRF8
HLA-DRA
S100B
S100A4
25 FOS
RP11-291B21.2
CD248
IL2RA
IL7R
ADTRP CD4+ T-cells
TNFAIP3
FOXP3
TNFRSF4
JCHAIN
0 DERL3
IGKC
MZB1
CD79A
LINC00926 B-cells,
FAM129C
FCER2 MHC Class II
MS4A1
HLA-DQA1
−25 B IG A H N M K1
HLA-DQB1
CCR6
TRIB3
DDIT3
MYOM2
FCGR3A
FGFBP2
KLRF1
GZMB
−50 −25 0 25 50 K G L N R L D Y 1 CD8+ T-cells
CCL4
tSNE_1 CST7
NKG7
GZMK
CD8B
CCL5
GZMA
CD8A
SERTAD1
DUSP1
IER2
JUNB
JUN
NFKBIA
SLC7A11
FAM132B
ATF5
FAM178B
NMU PKLR
CCNB2 CDC20
PLK1
AKR1C3
TUBA1B
HIST1H4C Cell cycle
ASPM
TOP2A
NUSAP1
MKI67
TYMS
KIAA0101
CKS2 AML
clusters
2_ENSt
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
CNV
No Cov
Scaled
expression
–1 0 1
Fig.2Clustering,overviewofexpressionheterogeneity,andcopynumberanalysisin809653.at-SNEprojectionofscRNA-seqdata,withcellscolored
accordingtograph-basedclusterassignment;putativeAMLclusters(basedonlateranalyses)circled.bHierarchicalclusteringofthemostheavily
weightedgenesineachprincipalcomponent,averagedwithingraph-basedclusters.Eachcolumnrepresentsaclusterfrompanela.cCNVanalysis:blue,
cellswithdetectedCNVs;gray,nodetectedCNVs
6 NATURECOMMUNICATIONS| (2019) 10:3660 |https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
a b c d
Clonality Clusters Lineage Cell cycle phase G1
B-cell S
RBC G2/M
Non-AML
HSC
NRAS
MEP
TP53 MD
CEBPA
T-cell
809653 NF1
M0 Mono
36% Blasts cytic
e f g h
TP53 E286G CEBPA R142fs NRAS G12D BAG1 SNP
WT WT WT
Fig.3Single-cellmutationdetectionandinterpretationincase809653.aClonalityinferredfromeWGS,withsubclonaldrivergeneslabeled.bt-SNE
projectionofscRNA-seqdatawithcellscoloredaccordingtograph-basedclusterassignment.Inpanelsb–g,putativeclustersofAMLcellsarecircled.
cCellscoloredaccordingtoinferredlineage;RBC=redbloodcell,HSC=hematopoieticstemcell,MEP=myeloid-erythroidprogenitor,MD=myeloid
dendriticcell.dCellscoloredaccordingtocellcyclephase.e–gCellscoloredaccordingtosingle-cellgenotypeattheTP53E286G,CEBPAR142fs,and
NRASG12Dsites:blue,atleastonemutantreaddetected;yellow,wild-typereadsonly;gray,nocoverage.hCellscoloredaccordingtosingle-cellgenotypeat
thehomozygousBAG1germlineSNP:blue,atleastonemutantreaddetected;gray,nocoverage
demonstrated two key points: first, SNV-based classification of cells can have a variety of abnormal expression signatures, cor-
AML clusters can perform comparably to CNA-based methods, responding to different lineages and states of differentiation.
and second, cells in mutation-enriched clusters are also likely to
be AML cells, even if they contain no detectable mutation.
Expression signatures of mutation-containing cells. In the
Intheother4cases,somaticmutationswerealsoconcentrated
in specific cell clusters, suggesting that they represented AML approach described above, we treated mutation-containing cells
cells (Fig. 4). This approach to AML cell identification, which asmarkersforentireclustersofputativeAMLcells.However,the
abilitytomapmutationsinmanycells(3732mutantcells/sample
assumesthatallcellsinmutation-enrichedclustersarelikelytobe
on average) facilitates more conservative, direct analyses of
AMLcells,maymisssmallclustersofmutantcells,andrareAML
intratumoral expression heterogeneity, using only the cells that
c a e p l p ls ro th ac a h tco is -cl t u o ste a r n w al i y t z h e ce o l n ls ly of ( d a i n ff d ere a n ll t ) lin ce e l a l g s es w ; i a t n h a i l d te e r n n t a ifi ti e v d e f e o x r p e r , e w ss e a an c a o l n y fi ze rm d e th d e so m m u a ta ti t c io m na u ll t y at d io e n fi . n F ed or A e M ac L h c s e a l m ls p s l e e p , a t r h a e t r e e ly -
mutations (below). Overall, combining expression and mutation
(Methods,SupplementaryFigs.6and7).Asexpected,allsamples
datadelineatedclustersofAMLcellsmorecomprehensivelythan
showed intercellular heterogeneity in the expression of cell cycle
either method alone, and allowed us to identify abnormally-
differentiated AML cells (“lineage infidelity”28). genes (as expected) and genes that function in the immune sys-
tem,especiallytheMHCClassIIgenesand/orCD74.Allbutone
case (782328) showed intercellular variability in expression of
TP53-interacting genes29. Three cases (508084, 548327, and
Evaluating tumor differentiation state. By combining lineage
inference with single-cell mutation identification, we estimated 721214) showedintercellular heterogeneityingenes thatinteract
withthevascularcelladhesiongeneVCAM1,andthree(721214,
theextentofdifferentiationofeachtumor.Ourconclusionswere
supportedbyflowcytometryandmorphology,butprovidedmore 7
lo
8
i
2
d
32
d
8
i
,
ff
a
e
n
re
d
nt
8
i
0
at
9
i
6
o
5
n
3)
g
s
e
h
n
o
e
w
s.
ed
Th
h
e
e
r
t
e
ero
w
g
e
e
r
n
e
eo
a
u
l
s
so
ex
c
p
a
r
s
e
e
s
-
s
s
i
p
on
eci
o
fi
f
c
m
s
y
ig
e-
-
insight into the differentiation state of AML cells in individual natures, such as “response to reactive oxygen species” in
samples (Figs. 3 and 4). In two cases (809653 and 782328), a
72121429. As discussed further below, a GATA2R361C expression
considerable fraction of the mutant cells had expression sig-
signature is evident in cells expressing this mutation. Thus, the
natures consistent with differentiated cells: erythrocytes and reduced,mutant-onlydatasetissufficienttocapturemuchofthe
monocytesin809653(Fig.3c),andmonocytesandNK-Tcellsin
expression heterogeneity observed in the total sample.
782328 (Fig. 4d). Likewise, case 548327 contained mutant cells
that co-clustered with wild-type B- and T-cells, again suggesting
thatsomeAMLcellsdisplaylineageinfidelity(Fig.4b).Thus,this Mutation-associated expression signatures. We next investi-
integrative genomic approach validates the concept that AML gatedtheextenttowhichmutationalheterogeneitywasassociated
NATURECOMMUNICATIONS| (2019) 10:3660 |https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications 7
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
a b c d
Clonality Clonality Clonality Clonality
DNMT3A IDH1 FLT3
SRSF2 IKBKB NRAS
NPM1
NUP98/NSD1
FLT3ITD
U2AF1
FLT3F612L NPM1
RNF10
NRAS
GATA2
721214 548327 508084 782328
M1 M1 M4 AML w/ MDS
91% Blasts 75% Blasts 52% Blasts 33% Blasts
Lineage B-cell Lineage Monocytic Lineage Monocytic Lineage NK-T
Dendritic Dendritic
RBC (myeloid) (myeloid) T-cell
RBC
Monocytic
HSC HSC/CMP HSC
HSC
B-cell
T-cell
T-cell
B-cell
Cell cycle phase Cell cycle phase Cell cycle phase G1 Cell cycle phase G1
S S
G2/M G2/M
G1 G1
S S
G2/M G2/M
DNMT3A SRSF2 FLT3 ITD U2AF1 S34F
WT WT
R882H P95H
WT WT
NPM1 IDH1 IKBKB V616M NRAS G12D G12D
WT WT
W288fs R132H
WT WT
GATA2 NPM1 RNF10 12:120575331 NRAS G12S G12S
WT WT
R361C W288fs
WT WT
Fig.4Single-cellmutationdetectionandinterpretationinadditionalcasesorderedbythedifferentiationsignatureofAMLcells.a721214,toptobottom:
clonalityinferredfromeWGS;cellscoloredaccordingtoclosestinferredlineage(RBC=redbloodcell,HSC=hematopoieticstemcell,CMP=common
myeloidprogenitor);cellscoloredaccordingtocellcyclephase;cellscoloredaccordingtosingle-cellgenotypeattheindicatedsite:blue,atleastone
mutantreaddetected;yellow,wild-typereadsonly;gray,nocoverage.b548327,putativeAMLcellscircled.c508084.d782328
8 NATURECOMMUNICATIONS| (2019) 10:3660 |https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
with transcriptional heterogeneity in each case. A subclonal of genes involved in immune response, apoptosis, and leukocyte
mutationthatdrivesanexpressionsignatureshouldberestricted adhesion29 (Fig. 5c, Supplementary Table 1). Notably, the gene
inexpressionspace.Incontrast,afoundingorsubclonalmutation whoseexpressionismoststrikinglycorrelatedwiththissubclone
not associated with an expression signature should be present isVIM,whichencodesatypeIIIintermediatefilamentandisan
throughout expression space. Furthermore, this should not established target of the GATA2/SPI1 (PU.1) transcriptional
dependonrestrictedexpressionofthemutantgene.Tothisend, circuit (Fig. 5d)31,32.
we highlighted mutant cells on the t-SNE projection of each As described above, we also analyzed this sample using only
sample, and identified mutations that are nonuniformly dis- the cells of known (i.e. mutant) genotype, and again found that
tributed, even after controlling for that gene’s expression GATA2R361Csubclonalmutationswerenonuniformlydistributed
(Figs. 3e–g and 4, Supplementary Fig. 8). We performed two in expression space. We compared mutant-rich clusters (muta-
versionsofthisanalysis:a“whole-sample”analysisusingallcells, tion fraction >10%) to the remaining clusters using a Wilcoxon
anda“mutant-cell”analysisusingonlymutation-containingcells. ranksumtestfordifferentialexpression33(Fig.5e–h).Consistent
Thewhole-sampleanalysiscapitalizedonthehighthroughputof with the above results, subclonal mutations were associated with
this platform by incorporating expression information from all higher expression of VIM, CRIP1, AHNAK, CD74, and other
~20,000cellspersample,therebyimprovingourabilitytodiscern genes associated with immune response, apoptosis, and cell
distinctexpressionsignatures.Ontheotherhand,thelimitations adhesion (Supplementary Data 5c).
of genotype assignment imposed by low coverage and allelic ManyoftheGATA2R361Csubclone-associatedgenesarehighly
dropout required that we compare a relatively small number of correlated with each other (and with VIM), in the TCGA AML
mutant cells to a much larger number of cells of unknown gen- gene expression data34. To quantify the overlap between TCGA
otype (representing a mixture of mutant and wild-type cells). VIM-associated genes and GATA2R361C subclone-associated
Therefore, instead of performing a straightforward comparison genes, we identified 2191 genes that are highly correlated with
between mutant and wild-type cells, we looked for evidence that VIM in TCGA (q<0.001, Pearson correlation, Benjamini-
the mutant cells were nonuniformly distributed among the Hochbergcorrection),andusedahypergeometrictesttocompare
“unknown” cells: when defining expression signatures, as them to the GATA2R361C subclone-associated genes (Fig. 5h).
describedfurtherbelow,wesearchedforgeneswhoseexpression The intersection of these gene sets was statistically significant
was correlated with the density of mutant cells. (p=3.5×10 –95,hypergeometrictest),suggestingtheexistenceof
The results of the whole-sample analysis indicated that the a VIM “regulon” whose expression is influenced by oneor more
relationship between expression heterogeneity and mutational mutations in the GATA2R361C subclone. To further characterize
heterogeneity is case- and mutation-dependent. Two cases, this regulon, we examined the functional enrichment of the 198
721214and508084,containedsubclonalmutationswithnonuni- genesintheintersection(SupplementaryTable2,Supplementary
formdistributions(Fig.4a,c).BasedoneWGS,721214contained Data 5d), and found that they are enriched for Gene Ontology
asubclonedefinedbyGATA2R361C.InthescRNA-seqdata,cells (GO) terms related to immune response (in particular, the Fc-
expressingGATA2R361Cwerelargelyrestrictedtothesamespace gamma receptor pathway), cytoskeletal organization, and focal
on one side of the t-SNE projection, suggesting that AML cells adhesion, and for genes that interact with WAS. WAS, which
containing this mutation have a unique expression signature encodes Wiscott-Aldrich Syndrome Protein, transduces signals
(Fig. 4a). Two cases (809653 (Fig. 3f–g) and 782328 (Fig. 4d)) from the cell surface to the actin cytoskeleton in response to
exhibitedcomplexmutation-associatedexpressionprofiles,anda infection, and is required for a variety of immunological cell
third, 548327 (Fig. 4b), showed expression heterogeneity in the functions. WAS mutations are associated with a broad spectrum
absence of discernable genetic heterogeneity. The GATA2R361C of clinical manifestations, including immunodeficiencies and
gradient in 721214 was of particular interest, because GATA2 hematologic malignancies35. Like VIM, WAS may also be
encodes a transcription factor that is a key regulator of regulated by PU.136. Together with our data, this suggests that
hematopoiesis, and is recurrently mutated in AML23,30. We a subset of PU.1 target genes coordinates immune function with
therefore sought to characterize the associated expression cytoskeletal reorganization in hematopoietic cells, and that at
signature. leastoneofthemutationsintheGATA2R361Csubcloneinfluences
As noted above, scRNA-seq data allows us to distinguish the expression of these genes. Because GATA2 is a transcription
between mutant cellsand cellsof unknown genotype; wecannot factor that negatively regulates PU.132, it is likely that the
conclusivelylabelacellas“wild-type.”Toaddressthislimitation GATA2R361C mutation itself is at least partly responsible for the
while incorporating expression information from cells of observed transcriptional effects in this sample. Furthermore,
unknown genotype, we employed a regression-based method GATA2haswell-documentedrolesinbothimmunefunctionand
that identifies genes whose expression is correlated with the hematological malignancies: autosomal dominant mutations in
densityofmutantcells(Methods),foragivenmutationorsetof GATA2 can also lead to immunological disorders and hemato-
subclonal mutations. This approach makes use of expression logic malignancies37,38.
clusters to smooth the expression and density data, but does The success of this method depends on a number of factors,
not depend on the exact clustering, and does not require us to including steepness of the expression gradient and number of
identify cluster-specific gene expression. It also permitted us to mutant cells (the moresubtle theexpression signature, the more
controlforpotentialcovariates,suchastheexpressionofGATA2, mutant cells required). Moreover, irrelevant or hidden variables
whichwasslightlycorrelatedwiththemutationdensitygradient. can affect the distribution of mutant cells in expression space,
We applied this method to the full data set in two ways: first, such as expression level of the mutated gene, cell cycle phase,
by searching for genes whose expression was correlated with ribosomaltranscriptcontent,mitochondrialtranscriptcontent,or
anymutationintheGATA2R361Csubclone(Fig.5a),andsecond, other variables for which we could not account. We therefore
for genes associated with GATA2R361C per se. Each analysis used an independent experimental approach to test for the
yielded several hundred genes whose expression was positively GATA2R361C-associated expression gradient, in which we com-
correlated with GATA2R361C density (FDR-adjusted p-value paredthefrequencyofGATA2R361CingenomicDNAfromcells
for the regression coefficient <0.05; Fig. 5b, c, Supplementary drawn from each extreme of the expression gradient. First,
Data 5a, b). Clusters with a higher density of expressed scRNA-seq was used to identify cell-surface markers whose
GATA2R361C subclonal mutations exhibited higher expression expression was correlated with the GATA2R361C mutation
NATURECOMMUNICATIONS| (2019) 10:3660 |https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications 9
a b c
Subclonal mutations Clusters –2 0 2
8
13
8 5 10
5 4
4 9 3
3 11 7
9
11
7 0 1
1 12
0
14 10 2 6 6
2
GATA2 R361C
TIMM17B L122fs
d
VIM
0
1 2
3
4
5
6
7
8
Other
NPM1 W288fs
FLT3 F612L
FLT3−ITD
DNMT3A R882H
GATA2 R361C
gradient.ThisanalysisyieldedCD99,awell-describedcell-surface controlmutation,DNMT3AR882,wasnotsignificantlyenrichedin
marker associated with AML and MDS cells39 (Fig. 6a). Then, the CD99hi cells, because it is present in all of the AML cells in
peripheral blood and bone marrow samples from this patient thissample(itwastheinitiatingevent).GATA2R361Cabundance
were stained with CD99 FITC-conjugated antibody, and flow varies more dramatically in the scRNA-seq data, possibly due to
cytometry was used to isolate cells with high or low CD99 allele-specific expression of the mutant allele, a documented
expression (top or bottom 15%, Fig. 6b, c; Methods). Genomic phenomenon in GATA2-mutated AML40. These results support
DNA was prepared from each population, and targeted sequen- theconclusionthatGATA2R361Cisassociatedwithadistinctgene
cingwasusedtomeasurethefrequencyofGATA2R361mutations expression profile, and shows that SNV detection in scRNA-seq
(aswellasacontrolDNMT3AR882mutation,whichisfoundinall data can be used to identify mutation-associated expression
AML cells in this sample) in each cell population. This signatures. Moreover, the ability to identify cell surface markers
demonstrated that GATA2R361C is significantly more abundant for the purification and analysis of subclones is an important
(p=0.0081 (marrow), p=0.0432 (peripheral blood), Fisher application of scRNA-seq data that should have broad
Exact test) in the genomes of the CD99hi cells (Fig. 6d). The applications.
noitcarf
tnatuM
0.6
e
VIM-correlated TCGA genes
Subclone genes
2191 579
198
Total genes = 33,641 p = 3.5×10–95
1PIRC
MIV
4A001S 47DC 1SLAGL KANHA 11A001S 2NAPST 6FLK 6A001S 2NLGAT 2SCOS 2ATAG MDAYM LRCLAC ARD-ALH 3PME 99DC GH551RIM 3A1YCUG 01BSMT 1BRD-ALH 1BPD-ALH 1MIP 3D22CST
f
g h
0.2 1
5
6
78
4
2
3
0
noitcarf
tnatuM
3.0
–2 0 2
noisserpxe
naeM
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
2.0
0.01 0.03 0.05
Mutant cell fraction
Fig.5GATA2R361CSubclonalexpressionsignature.at-SNEprojectionshowingmutation-expressingcellsinblue(GATA2R361C)andpink(TIMM17BL122fs).
bCellscoloredaccordingtograph-basedclusterassignment.cHeatmapoftop50mutation-dependentgenes,withbargraphshowingmutantcellfraction
ineachAMLcluster(labeledtotherightoftheheatmap).dCellscoloredaccordingtoVIMexpression(left),andscatterplotshowingaverageVIM
expressionineachclusterasafunctionofthesubclonalmutationfractionofeachcluster(right).et-SNEplotconstructedfrommutantcells,whichare
coloredaccordingtothemutationtheycontain:GATA2R361C,yellow;DNMT3AR882H,pink;FLT3-ITD,green;FLT3F612L,purple;NPM1W288FS;othersomatic
mutation(s),gray.fMutantcellscoloredaccordingtograph-basedcluster.gHeatmapoftop25subclonalmutation-dependentgenes,withbargraph
showingmutantcellfractionineachcluster(labeledtotherightoftheheatmap).GenesthatarehighlycorrelatedwithVIMinTCGAareindicatedwith
bluedots.hVenndiagramindicatinggenesetsusedtoidentifytheVIMregulome
10 NATURECOMMUNICATIONS| (2019) 10:3660 |https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications
60 60
50 50
40 40
30 30
20 20
10 10
0 0
DNMT3A GATA2 DNMT3A GATA2
In case 508084, a mutation in RNF10, a putative transcription sample. Notably, cells expressing CEBPAR142fs were restricted to
factor of unknown function, was also restricted to a subset of oneAMLcluster thatdiffered fromthe otherAMLclusters with
expressionclusters(Fig.7a,b).Comparedtoclusterswithfewor respect to differentiation state and cell cycle status: compared to
nomutantcells,mutant-richclustersdisplayedaclearexpression CEBPA wild-type AML clusters, the CEBPA-mutant cluster was
signature marked by high expression of genes involved in enriched for cells in S-phase, and cells with progenitor-like
immune-related cell adhesion. This included genes involved in expression signatures. Differential expression analysis of the
MHCClass IIreceptoractivity and Tcellaggregation, as well as CEBPA-mutant cluster showed that it overexpressed genes
genes that interact with MCM2 (a regulator of TP53) and NPM associated with a variety of biological processes, most notably
(which is frequently mutated in AML) (Fig. 7c, Supplemen- ribosome biogenesis, which probably reflects the increased
tary Table 3, Supplementary Data 5e). protein synthesis requirements of rapidly proliferating cells
Theremainingthreecasesshowedmorecomplexrelationships (Fig. 7f, Supplementary Table 4, Supplementary Data 5f). The
between expression and mutations. Based on the eWGS results, cluster also expressed a variety of key transcription factors
809653 contained TP53E286G and CEBPAR142fs in the founding involved in myeloid differentiation, particularly targets of Myc,
clone,andasubclonedefinedbyNRASG12DandNF1I679fs.Inthe consistent with the observed perturbation of cellular differentia-
single-cell data, however, the distribution of CEBPAR142fs was tion in this cluster.
markedly nonuniform, suggesting that CEBPAR142fs may be in a In 782328, NRASG12D and NRASG12S also display subtle
subclone (Fig. 7d, e); the clonal architecture of this case may be expressionsignatures(Fig.4d).Theyarepredominantlylocalized
more complicated than can be discerned from a single eWGS to cellsinthe S,G2, andM phasesof thecell cycle, suggestinga
)%(
elella
tnairaV
Bone marrow Peripheral blood
CD99 low CD99 high CD99 low CD99 high
15.5% 16.4% 15.8% 17.8%
rettacs
ediS
)%(
elella
tnairaV
a
CD99
2.3
1.5
60 k 60 k
2.0
40 k 40 k
1.0
20 k 20 k
0.01 0.03 0.05
Mutant cell fraction
0 0
0 103 104 0 103 104
CD99-FITC
n.s. n.s. Pre-sort
n.s. n.s. n.s. n.s. CD99 high
CD99 low
n.s. n.s.
*** ** * *
*p < 0.05
**p < 0.01
***p < 0.0001
Fisher’s exact test
noisserpxe
naeM
b
Viable cells
Sytox-blue
c
d
rettacs
ediS
ediS
rettacs
drawroF W-rettacs
ediS
rettacs
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
CD99 CD99
low high
Single cells
Forward scatter Forward scatter-A CD99-FITC
Fig.6OrthogonalconfirmationofGATA2R361Cexpressionsignaturebyflowcytometryandtargetedsequencing.aCellscoloredaccordingtoCD99
expression(top),andscatterplotshowingaverageCD99expressionineachclusterasafunctionoftheGATA2mutationfractionofeachcluster(bottom).
bSortingstrategy:CellsstainingpositiveforthedeadcelldyeSytox-bluewereexcluded,thendebriswasexcluded.Singletsweregatedforfinalsortingof
CD99-lowandCD99-highexpressingpopulations.cGatingofcellsbasedonCD99expressionusingflowcytometry(bonemarrow,left;peripheralblood,
right).dVariantallelefractionofthefoundingcloneDNMT3AR882HmutationandthesubclonalGATA2R361Cmutationinunsortedcells(gray),CD99-high
cells(blue),andCD99-lowcells(red)(bonemarrow,left;peripheralblood,right)
NATURECOMMUNICATIONS| (2019) 10:3660 |https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications 11
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
a c d f
Mutant WT 9 Non-AML Mut. W
6 16 17
2 3 11
8 18
2
13
7
0 14 8 12 15
5 4 10
3 10 6
1 4
0
7 1
9 5
b e
RNF10 CEBPA
12:120575331
WT R142fs
WT
Fig.7Additionalmutation-associatedgeneexpressionsignatures.at-SNEplotof508084,cellscoloredbygraph-basedcluster.bCellscoloredaccording
tocoverageattheRNF10NULLsite(mutant=blue,wild-type=yellow).cGenesthataredifferentiallyexpressedbetweenmutant-richandmutant-poor
clusters.dt-SNEplotof809653,cellscoloredbygraph-basedcluster.eCellscoloredaccordingtocoverageattheCEBPAR142fssite(mutant=blue,wild-
type=yellow).fGenesthataredifferentiallyexpressedbetweenmutant-richandmutant-poorclusters;non-AMLcellsshownforcomparison
rolefor thesemutationsin cellcycleprogression orproliferation Previous studies have demonstrated that CNAs and specific
rate. Further work will be required to characterize and confirm genetic variants, such as the BCR-ABL fusion, can be identified
these putative mutation-expression associations. with high sensitivity in full-length transcripts from dozens to
hundreds ofsinglecellsusingplate-based techniques suchasthe
Fluidigm C1/Smartseq platform, and that SNVs can also be
Interaction between genetic and epigenetic heterogeneity. The identified, albeit with lower sensitivity, using that data. Because
interplaybetweengeneticandepigeneticheterogeneitycouldhave CNAs rarely reflect the complete clonal architecture of a tumor
important consequences for intratumoral phenotypic hetero-
(and are rare in most AML samples), we were interested in
geneity: a mutation will likely have functional effects only in the findingawaytoidentifySNVsinsinglecells.Wenoticedthatthe
c in ell s s cR in N w A h -s i e c q h d it at is a e a x s p a re m ss u e t d a . ti T o h n is th p a h t e i n s o c m on e fi n n o e n d w to ou a ld po m rt a i n on ife o st f 1 w 0 o x rk G fl e o n w o s m y i i c e s ld Ch u r n o e m xp iu ec m ted Si ly ng h le ig C h e t ll ra 3 n ′ s a c n ri d pt 5′ co G v e e n ra e g E e x f p a r r es fr s o io m n
expression space by virtue of the fact that the mutation- the3′and5′endsoftranscripts.Althoughthisdistalcoverageis
containing gene is only expressed in that region; the converse is sparse,itissufficientforlow-sensitivityvariantdetectioninsingle
notnecessarilytrue,duetothepotentialfordropoutsinscRNA-
cells: SNVs were detectable in 22.7% of the cells in our samples,
seqdata.Incase508084,weobservedasubtlemutationgradient
on average. Coupled with the high throughput of the platform,
fortheFLT3-ITDmutationincase508084,whichwascausedbya
this sensitivity enables the detection of SNVs in hundreds to
corresponding FLT3 expression gradient. This phenomenon was
thousandsofcellspersample.Althoughthesecellscanbestudied
also observed in the CEBPAR142fs mutation gradient in 809653,
inisolation,weanalyzedtheminthecontextoftheentiresample,
which was partly due to heterogeneous CEBPA expression.
thereby leveraging the expression information provided by the
additional, non-genotyped cells.
Discussion AcommonapplicationofvariantdetectioninscRNA-seqdata
The ability to link genetic and transcriptomic information in is to distinguish tumor from normal cells in heterogenous sam-
single cells has important implications for the study of hetero- ples. However, because malignant cells can have expression
geneous cell populations. By combining eWGS and scRNA-seq profiles thatmimic more highly differentiated normal cells, gene
data from a high-throughput platform, we can distinguish expression dataalone isnotsufficient toidentify bonafideAML
between tumor and non-tumor cells, identify tumor cells dis- cells. Moreover, AML cells sometimes display lineage infidelity,
playing lineage infidelity, evaluate the differentiation state of wheresomeAMLcellsdisplaythecharacteristicsofdifferentiated
individual tumor samples, derive mutation-associated expression cell types from other lineages, such as T-cells. These AML cells,
signatures, study transcriptional heterogeneity within confirmed which would have been missed if classification had been per-
tumorcells,andidentifycell-surfacemarkersthatcanbeusedto formedusingexpressionsignaturesalone,canbeidentifiedwhen
isolate specific cells for downstream studies. Further, the mutation information is also considered.
approachdescribedhereshouldbeapplicable–withoutadditional Transcriptional heterogeneity in AML samples clearly arises
modifications or customization–to virtually any tumor type. from multiple sources, including the differentiation states of
12 NATURECOMMUNICATIONS| (2019) 10:3660 |https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
normal and tumor cells, cell cycle states, mutations that are (~150×)oftheexome,andlowergenome-widecoverageinthetumor(~45×)and
present in subsets of cells (i.e. subclones), or non-genetic het- normal(~25×)samples.Usingapreviouslydescribedprotocol25,eWGSsequen-
erogeneity that arises as a consequence of stochastic gene cinglibraries,includingWGSlibraries(350bpinserts)andtargetedlibraries
(250bpinserts),wereconstructedwithaKAPAHTPkitonaSciCloneinstrument.
expression or other perturbations. Incorporating variant detec-
TargetedlibrarieswerecapturedwiththeIDTexomereagentspikedwithAML
tion into scRNA-seq analysis helps to distinguish among these recurrentlymutatedgenes51(~40Mb).TheseweresequencedonanIllumina
sourcesbyfacilitatingthedistinctionbetweentumorandnormal HiSeq4000,producing~150Xcoverageofeachenhancedregion.Sequencedata
cells, and by revealing correlations between mutational and
werealignedtoreferencesequencebuildGRCh37-lite-build37usingBWA-MEM52
version0.7.10(params:-t8),thenmergedanddeduplicatedusingPicardversion
transcriptional heterogeneity. Equally, importantly, it suggests
1.113(https://broadinstitute.github.io/picard/).Germlinemutationswerecalled
that genetic heterogeneity plays a limited role in establishing usingGATKHaplotypeCallerv3.553(parameters-stand_emit_conf10-stand_-
transcriptional heterogeneity: we routinely observed expression call_conf30)andfilteredusingrecommendedparameters(–filterExpression“QD
heterogeneity in the absence of detectable genetic heterogeneity.
<2.0||FS>60.0||MQ<40.0||MQRankSum<−12.5||ReadPosRankSum<
−8.0”).SNVsweredetectedusinganensemblemutationcallingapproach54
Insomecases,thismaybedueinparttothelimitedsensitivityof
thatconsiderstheunionoffourcallers:(1)Samtools55versionr982(params:
mutation detection. In others, it may exemplify the well- mpileup-BuDs)intersectedwithSomaticSniper56version1.0.4(params:-Fvcf–G
established phenomenon whereby stochastic gene expression -L-q1-Q15)andprocessedthroughfalse-positivefilterv1(params:–bam-read-
gives rise to phenotypic heterogeneity in clonal populations of count-version0.4–bamreadcount-min-base-quality15–min-mappingquality
cells41–43. Non-genetic transcriptional heterogeneity can influ- 40–min-somatic-score40),(2)VarScan57version2.3.6filteredbyvarscan-
highconfidencefilterversionv1andprocessedthroughfalsepositivefilterv1
ence phenotype (such as drug sensitivity44,45, growth rate46, and (params:–bamreadcount-version0.4–bam-readcount-min-base-quality15),(3)
cell fate43) and persist across generations46–48, and might there- Strelka58version1.0.11(params:isSkipDepthFilters=0),and(4)Mutect59v1.1.4.
foreserveasasubstratefornaturalselection49.Thisunderscores Indelsweredetectedusingtheunionof3callers:(1)GATK53somatic-indelversion
theideathatacombinationofgeneticandnon-geneticsourcesof
5336,(2)VarScan57version2.3.6filteredbyvarscan-high-confidence-indelversion
v1,and(3)Strelka5version1.0.11(params:isSkipDepthFilters=0).SNVsand
heterogeneity may help to govern tumor biology and evolution. Indelswerefurtherfilteredbyremovingartifactsfoundinapanelof905normal
As additional scRNA-seq studies of primary tumor samples are exomes60,removingsitesthatexceeded0.1%frequencyinthe1000genomesor
undertaken by many groups, the relative contributions of these NHLBIexomesequencingprojects,andthenusingabayesianclassifier(https://
sources of heterogeneity for each tumor type should become github.com/genome/genome/blob/master/lib/perl/Genome/Model/Tools/
Validation/IdentifyOutliers.pm)andretainingvariantsclassifiedassomaticwitha
more clear.
binomiallog-likelihoodofatleast10.Copynumberaberrationsweredetected
The detection of cells with expressed mutations in scRNA-seq usingcopyCatversion1.6.10(https://github.com/chrisamiller/copyCat)(default
data is subject to several limitations. Dropout (including tran- parameters).SomaticstructuralvariantsweredetectedusingMantav0.2961.
script dropout and allelic dropout) occurs with most scRNA-seq Finally,GRCh37genomiccoordinatesweretranslatedintoGRCh38coordinates
usingthe“liftover”utilityprovidedbytheUCSCGenomeBrowser(http://genome.
platforms.Asaresult,itisimpossibletodeterminewhetheracell
ucsc.edu/)62.SublconalarchitecturewasinferredusingtheSciClonealgorithm26.
is truly wild-type for a given mutation. In addition, dropout
reduces the sensitivity of mutation detection by a factor of two.
Partialtranscriptcoverageisspecifictoend-biasedplatformssuch BulkRNA-sequencing.RNAlibrarieswerepreparedusingtheTruSeqstranded
as the Chromium platform, and also limits the sensitivity of kit,sequencedontheIlluminaHiSeqplatform,andalignedasdescribedpre-
viously54.ExpressionquantificationwasperformedusingKallisto0.43.163and
variant detection. Moreover, coverage drops non-linearly across
transcriptsfromensemblversion74.
the length of the transcript, so some variants are much more
easily detectable than others. The utility of this approach there-
fore depends on the specific mutational composition of the FlowsortingforlivecellsforscRNA-seq.CryovialsofAMLcellswerethawedas
sampleinquestion,andwilllikelyperformbetterforothertumor follows:while9mlofFetalBovineSerum(FBS)wasallowedtocometo~24°C,
AMLcryovialswereremovedfromliquidnitrogen,andwarmedina37°Cwater
types, almost all of which have higher mutation burdens
bathuntilthecellsbegantothaw.After1min,1mlofroomtemperatureFBSwas
than AML. addedtothewarmingcryovialwithaP1000pipettipandallowedtomixwith
A number of other approaches to identify expressed thawingcells.ThefreshlyaddedFBSwasremovedfromthecellpelletand
mutations in single-cell RNA-sequencing data have been
transferredbacktotheFBSstock.Thisprocesswasrepeated3–4timesuntilallcells
described3–8,10–12,14,17–21.
Each method has different
fromthecryovialcouldbepoureddirectlyintotheFBSstock.Theemptycryovial
wasrinsedoncemorewiththeFBSmixture.Cellswerethenpelletedbycen-
strengths and weaknesses that should influence the choice of trifugationat300Gfor5minandresuspendedinPhosphate-bufferedsaline(PBS)
platform for a specific experimental question. Key variables ataconcentrationof1×106cell/mlin1xPBS.Cellswerethenpipettedthrougha
include library insert size, end-bias, and complexity, sequen-
70-µmfilterintoa5-mltubeforsorting.Cellswerethenstainedwith1µl7-AAD
per1mlofcellsfor30minat4°C.Ifcellviabilitywas≤85%,stainedcellswere
cing depth and read length, dropout rate, and throughput. filteredthrougha40-µMFlowmicellstrainer(Miltenyi),flowsorted,andgated
Furthermore,technologiesthatenablesimultaneousDNAand usingtheFACSChorussoftware(BDBiosciences).
RNA sequencing of single cells, such as G&T-seq50, may
become very powerful with increased throughput. The rapid
pace of technological advancement in this area will likely
5-primesingle-cellRNAlibraryconstructionandsequencing.Cellswerepro-
cessedusingthe10xGenomicsChromiumControllerandtheChromiumSingle
increase the power of scRNA-seq to identify and distinguish Cell5′Library&GelBeadKit(PN1000006)followingthestandardmanufacturer’s
among different sources of transcriptional heterogeneity in protocols(https://tinyurl.com/y96l7lns).Twotechnicalreplicateswererunin
primary tumor samples. parallelforeachsample.Inbrief,between14,000and21,000livecellswereloaded
ontotheChromiumcontrollerinanefforttorecoverbetween10,000and15,000
cellsforlibrarypreparationandsequencing.Gelbeadswerepreparedaccordingto
Methods standardmanufacturer’sprotocols.Oilpartitionsofsingle-cell+oligocoatedgel
Ethicalapprovalandconsent.Sampleswereobtainedaspartofastudythatwas beads(GEMs)werecapturedandreversetranscriptionwasperformed,resultingin
approvedbytheHumanResearchProtectionOfficeatWashingtonUniversity cDNAtaggedwithacellbarcodeanduniquemolecularindex(UMI).Next,GEMs
SchoolofMedicine(HRPO#201011766).Allthepatientsprovidedwritten
werebrokenandcDNAwasamplifiedandquantifiedusinganAgilentBioanalyzer
informedconsentthatpermittedwhole-genomesequencing,inaccordancewitha HighSensitivitychip(AgilentTechnologies).
protocolthatwasapprovedbytheinstitutionalreviewboardattheWashington
Topreparethefinallibraries,amplifiedcDNAwasenzymaticallyfragmented,
UniversitySchoolofMedicine. end-repaired,andpolyAtagged.FragmentswerethensizeselectedusingSPRIselect
magneticbeads(BeckmanCoulter).Next,Illuminasequencingadapterswere
ligatedtothesize-selectedfragmentsandcleanedupusingSPRIselectmagnetic
eWGS,germlineSNPdetection,andsomaticvariantdetection.Foreachcase, beads(BeckmanCoulter).Finally,sampleindiceswereselectedandamplified,
weperformedenhancedwhole-genomesequencing(eWGS)onbonemarrowand followedbyadoublesidedsizeselectionusingSPRIselectmagneticbeads
matchednormaltissuetoidentifygermlineandsomaticvariants.eWGScombines (BeckmanCoulter).FinallibraryqualitywasassessedusinganAgilentBioanalyzer
whole-genomesequencingwithtargetedexoncapturetoyieldhighcoverage HighSensitivitychip.SampleswerethensequencedontheIlluminaNovaSeqwith
NATURECOMMUNICATIONS| (2019) 10:3660 |https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications 13
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
atargetof150,000reads/cell(2×150pairedendreads),yieldingamedianper- Read-basedandcell-basedmetrics.Theread-basedmetric“single-cellVariant
librarydepthof192,427readspercell. AlleleFrequency,”orscVAF,wasdefinedforeachvariantdiscoveredintheeWGS
dataasthenumberofmutantreadsdividedbythetotalnumberofreadsmapping
tothevariantpositioninthescRNA-seqdata.Thetwocell-basedmetricswere(1)
Evaluatingtranscriptcoverageasafunctionofdistance.Transcriptalignment, MutantCellFraction(MCF)and(2)MutantCellDetectionRate(MCDR)).The
counting,andinter-librarynormalizationwereperformedusingtheCellRanger MCFforeachvariantwasdefinedasM/T,whereTisthenumbercellshaving
pipeline(10xGenomics,defaultsettings,Version2.1.1,GRCh38reference)64.For
coverageatthemutantsite,andMisthenumberofcellshavingatleastonemutant
thegenesTP53,NPM1,GATA2,andDNMT3A,thedepthateachtranscriptwas readatthatsite.TheMutantCellDetectionRate(MCDR)wasdefinedastheratio
evaluatedusingbothscRNA-seqdataaswellasbulkRNA-seqdata.Foreachgene, ofobservedmutantcellstothenumberofexpectedmutantcells;forvariantswith
acanonicalisoformwaschosenbyconsultingtheAPPRISdatabase65
coverageinbulkRNA-seqdata,thenumberofexpectedmutantcellsistwicethe
(ENST00000445888.6,ENST00000296930.9,ENST00000341105.6,and eWGSVAF.
ENST00000264709.7respectively).ForthescRNA-seqdata,thenumberofunique
barcode/UMIpairswascountedateachposition.ForthebulkRNA-seqdata,the
toolbamCoverage66wasusedtogenerateawigglefileoverthetranscriptat1bp Mutationdetectioninnormalbonemarrowsamples.Weusedcb_snifferto
binsize.TheresultingtrackswerevisualizedusingtheUCSCGenomeBrowser67. searchfournormalbonemarrowsamplesforthesomaticmutationsdiscoveredby
Toreducevisualnoisefromintergenicreads,positionsnotoverlappingthe eWGS.Thesesampleshadbeenpreviouslygeneratedusingthemethodsdescribed
canonicalisoformwerenotconsidered.Coverageplotsforallmutatedgenesinthis
aboveandtheChromiumSingleCell3′Library&GelBeadKit(v2).
studyareprovidedathttps://github.com/genome/scrna_mutations.
Toevaluatetranscriptome-widecoverage,weusedtheannotationset scRNA-seqexpressionanalysisandmutationintegration.Transcriptalign-
GENCODEV27toextract20,090geneswithonlyoneannotatedisoformbetween ment,counting,andinter-librarynormalizationwereperformedusingtheCell
250bpand11,000bp,withanaveragesizeof1569bpandmediansizeof829bp. Rangerpipeline(10xGenomics,defaultsettings,Version2.1.1).UsingtheSeuratR
Restrictingtosingleisoformgenesreducednoiserelatedtoalternativetranscription package33,cellsthatcontainedfewerthan10expressedgenes,morethan50%
start(TSS)andstop(TTS)sites.Foreachtranscriptineachsampleinthisstudy, ribosomaltranscripts,ormorethan10%mitochondrialtranscriptswereremoved.
single-celltranscriptome-widecoveragewasquantifiedbycountingthenumberof
Genesthatwereexpressedinfewerthanthreecellswerealsoremoved.Foreach
uniquebarcode/UMIpairsseenacrossthewholetranscript.Then,foreachposition cell,expressionofeachgenewasnormalizedtothesequencingdepthofthecell,
alongthetranscript,thenumberofuniquepairswasdividedbythistotal.This scaledtoaconstantdepth(10,000),andlog-transformed.Variablegeneswere
valuewascalculatedasdistancefromtheTSSfor5′kitdata,anddistancefromthe selected(x.low.cutoff=0.0125,x.high.cutoff=5,y.cutoff=0.5,defaultsettings
TTSfor3′kitdata.Toplottheresults,theaveragevalueacrossalltranscriptsforall
otherwise).Principalcomponentanalysiswasperformedonthevariablegenes,and
sampleswascalculatedateachposition.Forshortertranscripts,positionswithno theoptimalnumberofprincipalcomponents(PCs)foreachsamplewaschosen
datawerenotincludedintheaverage.Theplotwasalsotruncatedto10,000bpto usingacombinationofelbowplots,jackstrawresampling,andPCexpression
avoidedgeeffectsrelatedtothetranscriptselectionprocess.Coverageplotswere heatmaps(508084:6,548327:8,721214:5,782328:7,809653:6,809653AMLcells:
generatedusingtheGviz68andBiomaRt69Rpackages,versions1.22.3and2.34.2 6).PCswereusedfordimensionalityreductioniftheyexplainedatleast2%ofthe
respectively.Foreachlocus,bothcodingandnon-codingexonicnucleotideswere variance;werestatisticallysignificantaccordingtojackstrawresampling;exhibited
consideredata1bpbinsize.Generegiontrackswereretrieveddirectlyfrom consistentexpressionvariationinheatmaps;andwerenotcomposedentirelyof
Ensemblv93.scRNAtotalreadcoveragewasgeneratedusingbamCoverage,partof ribosomal,mitochondrial,orimmunegenes.Dimensionalityreductionand
thedeepToolspackage66,andscRNAcellbarcodecoveragecanbefoundathttps:// visualizationwereperformedwiththet-SNEalgorithm(Seuratimplementation)
github.com/genome/scrna_mutations. usingthePCsselectedabove.Unsupervisedgraph-basedclusteringofcellswas
performedusingtheindicatedPCs,withresolution=0.7.Cellcyclephasewas
determinedusingmethodologyprovidedinSeurat,basedonrelativeexpressionof
Copynumberanalysis.GeneexpressionmatriceswereanalyzedwiththeCON- phase-specificgenes6.Thedistributionofmutationsonthet-SNEprojectionwas
ICSmatpackageforR19.Thedefaultfilteringandnormalizationprocedureswere
robusttofilteringformitochondrialandribosomaltranscripts,thenumberofPCs
followed,asoutlinedinhttps://goo.gl/tFYLEh.Themixturemodelresultswere
used,theclusteringresolution,andnormalizationforcellcyclephase.Themuta-
obtained,thenrestrictedtoregionsofknowncopynumbereventsfromtheeWGS
tiondistributionwasalsorobusttotheparticularimplementationofthet-SNE
withthebestlog-likelihoodscoresfromthemodeling:Forsample809653,these
algorithm,withtheSeuratandCellRangerimplementationsgivingconsistent
werechromosomes1pand7q.Thez-scoredposteriorprobabilitieswereclustered,
results.Toassesstherelationshipbetweenmutationdistributionandexpressionof
usingk=4,andcellbarcodesfromthethreeclusterscontainingoneormoreofthe
themutatedgene,wecoloredeachclusterineacht-SNEplotaccordingtothe
expectedeventsweregatheredandvisualizedontheexpressiont-SNEprojection.
expression-normalizedmutantcellfraction(mutantcellfractiondividedbythe
averageexpressionofthemutantgeneinthatcluster).
Single-cellmutationidentificationandanalysis.Weprocessedthealigned Mutation-expressingcellswereanalyzedinisolationusinganalogousmethods,
sequencedatausingaPysam70-basedtool(https://github.com/sridnona/ withtheexceptionthatfewerPCswererequiredtocapturethevariabilityinthe
cb_sniffer).ForeachcellbarcodeinthefilteredCellRangerbarcodelist,andeach data(508084:4,548327:3,721214:6,782328:7,809653:6).
somaticvariantintheeWGSdata,variantbaseswereidentified,excludingexclude
thosewithbasequalityandmappingquality<1.Onlyreadsthathadbotha Expressionheatmaps.Anexpressionheatmapwasgeneratedforeachsampleby
ChromiumCellularBarcode(CB)tagandaChromiumMolecularBarcode(UB) selectingthetop10genesineachofthetop20PCs.Toconnectheterogeneityto
tagwereincluded.Wethenobtainedthecell-associatedtagfordownstreamana- thegraph-basedclusters,andtoexaminerelationshipsamongclusters,weaveraged
lysisofUMIs.InrarecaseswhereduplicatereadsexistedforagivenUBandthe theexpressionofeachgenewithineachcluster,andhierarchicallyclusteredthe
baseatthemutantpositionwasnotidenticalacrossallreads,weselectedthemost results.Fortheanalogousanalysisperformedonmutantcellsinisolation,weused
commonbaseifitwaspresentinatleast75%ofthereads;otherwiseallreadsinthe thetop20genesfromeachofthetopnPCs,wherenwaschosenseparatelyfor
groupcorrespondingtothatUBwerediscarded.Werarelyobservedsuchdis- eachsampletominimizenoise(508084:4,548327:3,721214:6,782328:7,
cordantreads(forexample,theyoccurredin782328atafrequencyof4/6218,or 809653:6).
0.06%).
Severalvariantsrequiredadditionalstepsinordertoaccuratelyidentifymutant LineageinferenceandAMLcellidentification.Cell-typeinferencewasper-
cells:Manualreviewrevealedthattwosmallindelsinrepetitiveregions(CEBPA
(19:33301989–33301990)andNPM1(5:171410538–171410546))werefrequently formedinanunsupervised,marker-freemannerbytraininganearest-neighbor
algorithmonexpressiondatafromtheDMAPdatabase27,usingSpearmancor-
misalignedtoseveraladjacentbases.Thiswasresolvedbyparsingthebamcigar
relationasthedistancemetric.Usingthisapproach,cellsthatco-clusterbygraph-
stringtoidentifyreadscontaininginsertionsordeletionsattheappropriate
basedclusteringtendtohavethesameinferredlineageandexpressthecorre-
locationsusinganadditionalPysam-basedtool(https://github.com/genome/
spondingcell-typemarkers(whenknown).InthecaseofAMLcells,theassigned
scrna_mutations/tree/master/misc_scripts),whichextractsoverlappingreadsusing
SAMtools‘view’55.Inaddition,thelargesizeofthecharacteristiclargeinternal lineagerepresentsthenormallineagetowhichtheAMLcellismosttran-
scriptionallysimilar.ToidentifyAMLcellsinhighlyheterogeneoussamples
tandemduplication(ITD)inFLT3resultedinincorrectalignmentofmany
(549327and809653),aone-sidedFisherexacttestwasusedtoidentifycellclusters
variant-containingreads.Toaddressthis,wecreatedacontigcontainingthe thatwereenrichedforsomaticmutations(p≤0.05).Incaseswheremostcellsare
variantsequence(±250bp),appendedittothetranscriptomereference,and AMLcells,normalcellclusterswereidentifiedusingaone-sidedFisherexacttest
realignedthescRNAdatatotheexpandedreference.Barcodesfromreadsuniquely forunder-enrichment(p≤0.05).
aligningtothemutantFLT3sequencewerethenextracted.Similarly,theNUP98-
NSD1fusionin508084wasdetectedbyappendingthefusiontranscripttothe
inputGTFfile,thenusingkallisto63anditscompaniontool,pizzly,toidentify GATA2R361C-associatedexpressionsignatures.Eachcellcontaininga
fusion-supportingtranscripts. GATA2R361Cmutationwasassignedtoanexpressioncluster.Inordertoincor-
AfterusingSciClone26toassigneachsomaticvarianttoasubclone,weassigned porateexpressioninformationfromallcellsinthedataset,includingthoseof
mutation-containingcells(“mutantcells”)totheircorrespondingsubclones.Cell- undeterminedgenotype,andtomakeuseofquantitativeinformationaboutlocal
variantassignmentcannowalsobeperformedinanautomatedmannerusingthe mutationdensity,weusedaregressionmodeltoidentifygeneswhoseexpression
VarTrixtool(https://github.com/10xgenomics/vartrix). dependsonmutantcellconcentration.Foreachgenei,multipleregressionwas
14 NATURECOMMUNICATIONS| (2019) 10:3660 |https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-11591-1
usedtoquantifytherelationshipbetweenmeanexpression(E)andGATA2R361C References
i
mutantcellfraction(m)acrossthe12AMLclusters,whilecontrollingformean 1. Ding,J.,Lin,C.&Bar-Joseph,Z.CelllineageinferencefromSNPandscRNA-
cluster-wiseGATA2expression(g): Seqdata.NucleicAcidsRes.47,56–64(2018).
E i ¼x i þy i mþz i g ð2Þ 2. s v p a e n ci d fi e c r c W is- ij e s Q t, T M Ls .G an . d P. co et -e a x l p . r S e in ss g i l o e n -c Q ell T R Ls N . A Na s t e . q G ue e n n c et in . g 50 i , de 1 n – t 9 ifi ( e 2 s 01 ce 8 l ) l . type-
Weselectedgeneswhoseq-value(F-testwithBenjamini-Hochbergcorrection 3. Lee,M.-C.W.etal.Single-cellanalysesoftranscriptionalheterogeneityduring
formultiplehypotheses)fory i wasatmost0.05.Toconsidertheentiresubclone drugtolerancetransitionincancercellsbyRNAsequencing.Proc.NatlAcad.
containingtheGATA2mutation,weperformedthisprocedureusingcells Sci.USA111,E4726–E4735(2014).
containinganydetectedmutationinthatsubclone(GATA2R361Cor
4. Patel,A.P.etal.Single-cellRNA-seqhighlightsintratumoralheterogeneityin
TIMM17BL122fs),withoutthecorrectionforGATA2expression.Toanalyzethe primaryglioblastoma.Science344,1396–1401(2014).
mutant-onlydata,weusedaWilcoxontesttoperformabinarycomparisonof 5. Kim,K.-T.etal.Single-cellmRNAsequencingidentifiessubclonal
mutation-richclusterstomutation-poorclusters,withanalogousp-value
heterogeneityinanti-cancerdrugresponsesoflungadenocarcinomacells.
correctionandcutoffs. GenomeBiol.16,1–15(2015).
6. Tirosh,I.etal.Dissectingthemulticellularecosystemofmetastaticmelanoma
IdentificationandanalysisoftheVIMregulon.Genesthatexhibitedsubclone- bysingle-cellRNA-seq.Science352,189–196(2016).
specificexpression(above)werecomparedtogeneswhoseexpressionwashighly 7. Müller,S.etal.Single-cellsequencingmapsgeneexpressiontomutational
VIM-correlatedinTCGA(q<0.001,Pearsoncorrelation,Benjamini-Hochberg phylogeniesinPDGF-andEGF-drivengliomas.Mol.Syst.Biol.12,889
correctionformultiplehypotheses).Genesintheintersectionwereconsideredpart (2016).
ofthe“VIMregulon,”andToppfun29wasusedtocharacterizetheirfunctional
8. Brady,S.W.etal.Combatingsubclonalevolutionofresistantcancer
enrichment. phenotypes.Nat.Commun.8,1231(2017).
9. Lee,J.-K.etal.Spatiotemporalgenomicarchitectureinformsprecision
OrthogonalconfirmationofGATA2R361Csignature.Primary,humanAML oncologyinglioblastoma.Nat.Genet.49,594–599(2017).
peripheralbloodandbonemarrowaspiratesamples(721214)werethawedfrom 10. Venteicher,A.S.etal.Decouplinggenetics,lineages,andmicroenvironment
cryopreservedstocksandlabeledwithCD99FITC-conjugatedantibody(clone inIDH-mutantgliomasbysingle-cellRNA-seq.Science355,eaai8478–13
3B2/TA8,ThermoFisher)instainingbuffer(2%fetalbovineserum,0.25mM (2017).
EDTAinPBS)for30minat4°Cfollowedbyviabilitydyefor5minatroom 11. Puram,S.V.etal.Single-celltranscriptomicanalysisofprimaryand
temperature(SytoxBlue,ThermoFisher).LivecellswereanalyzedusingaSony metastatictumorecosystemsinheadandneckcancer.Cell171,1611.e1–1611.
SY3200Synergyflowcytometer,gatedforsortingonthetop15%andbottom15% e24(2017).
withrespecttoCD99expression,andcollectedforanalysis.GenomicDNAwas 12. Fan,J.etal.Linkingtranscriptionalandgenetictumorheterogeneitythrough
preparedwiththeQIAmpDNAmicrokit(Qiagen)accordingtothemanu- alleleanalysisofsingle-cellRNA-seqdata.GenomeRes.28,1217–1227(2018).
facturer’sprotocol.Targetedsequencingwasachievedbygeneratingampliconsto 13. Tirosh,I.&Suvà,M.L.Dissectinghumangliomasbysingle-cellRNA
capturemutationsatDNMT3AR882(forward:CGCAAAATACTCCTTCAGCG, sequencing.NeuroOncol.20,37–43(2018).
reverse:TTTCTCCCCCAGGGTATTTG)andGATA2R361(forward: 14. Kim,C.etal.Chemoresistanceevolutionintriple-negativebreastcancer
TGTGCAGCTTGTAGTAGAGG,reverse:TGAGATTTAGCCCTCCTTGAC). delineatedbysingle-cellsequencing.Cell173,879–893.e13(2018).
Ampliconswereindexedandspikedinto2x150dualindexedrunsonanIllumina 15. Klco,J.M.etal.Functionalheterogeneityofgeneticallydefinedsubclonesin
MiniSeqsequencer.FastQC71wasusedforqualityanalysisofsequencedreads acutemyeloidleukemia.CancerCell25,379–392(2014).
(FASTQfiles).Readswerecheckedforcontamination,adaptersequencesandbase
16. Saadatpour,A.,Guo,G.,Orkin,S.H.&Yuan,G.-C.Characterizing
quality,thenalignedagainsthumanreferencesequence(GRCh37)usingbwa heterogeneityinleukemiccellsusingsingle-cellgeneexpressionanalysis.
(version0.7.15)72.Varscan257wasusedtoidentifySNVsandcalculatevariant GenomeBiol.15,313–313(2014).
allelefrequencies(VAF).
17. Tirosh,I.etal.Single-cellRNA-seqsupportsadevelopmentalhierarchyin
humanoligodendroglioma.Nature539,309–313(2016).
RNF10NULLandCEBPAR142fsmutantexpressionsignatures.WeusedaWil- 18. Filbin,M.G.etal.DevelopmentalandoncogenicprogramsinH3K27M
coxonranksumtesttoperformabinarycomparisonofmutation-richclustersto gliomasdissectedbysingle-cellRNA-seq.Science360,331–335(2018).
mutation-poorAMLcellclusters,withp-valuecorrectionandcutoffsasdescribed 19. Müller,S.,Cho,A.,Liu,S.J.,Lim,D.A.&Diaz,A.CONICSintegrates
above.Mutation-richclustersweresignificantlyenrichedformutations(p= scRNA-seqwithDNAsequencingtomapgeneexpressiontotumorsub-
0.00085(CEBPAR142fs)andp=0.0044(RNF10NULL),FisherExacttest). clones.Bioinformatics34,3217–3219(2018).
20. Giustacchini,A.etal.Single-celltranscriptomicsuncoversdistinctmolecular
Functionalenrichment.Functionalenrichmentanalyseswereperformedusing
signaturesofstemcellsinchronicmyeloidleukemia.Nat.Med.23,692–702
ToppFun(https://toppgene.cchmc.org/enrichment.jsp)29. (2017).
21. vanGalen,P.etal.Single-cellRNA-seqrevealsAMLhierarchiesrelevantto
diseaseprogressionandimmunity.Cell176,1265–1281.e24(2019).
Reportingsummary.Furtherinformationonresearchdesignisavailablein
22. Zack,T.I.etal.Pan-cancerpatternsofsomaticcopynumberalteration.Nat.
theNatureResearchReportingSummarylinkedtothisarticle. Genet.45,1134–1140(2013).
23. Ley,T.J.etal.CancerGenomeAtlasResearchNetwork.Genomicand
Data availability epigenomiclandscapesofadultdenovoacutemyeloidleukemia.N.Engl.J.
Enhancedwhole-genomesequence(eWGS),bulkRNA-sequence,andsingle-cellRNA-
Med.368,2059–2074(2013).
sequence(scRNA-seq)datageneratedduringthecurrentstudyareavailableindbGaP 24. Jolly,C.&VanLoo,P.Timingsomaticeventsintheevolutionofcancer.
(https://www.ncbi.nlm.nih.gov/gap/)withtheprimaryaccessioncodephs000159.The GenomeBiol.19,95(2018).
SRAIDsforthisstudyare:SRR7904017,SRR7904018,SRR7904019,SRR7904020, 25. Miller,C.A.etal.Resistance-promotingeffectsofependymomatreatment
SRR7910353,SRR7910351,SRR7910349,SRR7904016,SRR7903979,SRR7825447, revealedthroughgenomicanalysisofmultiplerecurrencesinasinglepatient.
SRR7825459,SRR7825446,SRR7825444,SRR7825491,SRR7825473,SRR7825453, ColdSpringHarb.Mol.CaseStud.4,a002444(2018).
SRR7825466,SRR7825499,SRR7825482,andSRR7939318.Processedsingle-cellRNA- 26. Miller,C.A.etal.SciClone:inferringclonalarchitectureandtrackingthe
seqandmutationdatapertainingtoAMLsamplesandnormalbonemarrowarealso spatialandtemporalpatternsoftumorevolution.PLoSComputBiol.10,
available[https://doi.org/10.5281/zenodo.3345981].Alltheotherdatasupportingthe e1003665(2014).
findingsofthisstudyareavailablewithinthearticleanditssupplementaryinformation 27. Novershtern,N.etal.Denselyinterconnectedtranscriptionalcircuitscontrol
filesandfromthecorrespondingauthoruponreasonablerequest.Areportingsummary cellstatesinhumanhematopoiesis.Cell144,296–309(2011).
forthisarticleisavailableasaSupplementaryInformationfile. 28. Smith,L.J.etal.Lineageinfidelityinacuteleukemia.Blood61,1138–1145
(1983).
29. Chen,J.,Bardes,E.E.,Aronow,B.J.&Jegga,A.G.ToppGeneSuiteforgene
Code availability
listenrichmentanalysisandcandidategeneprioritization.NucleicAcidsRes.
Single-cellmutationidentificationwasperformedusingPysam-basedtoolsavailableat 37,W305–W311(2009).
https://github.com/sridnona/cb_snifferandhttps://github.com/genome/ 30. Papaemmanuil,E.etal.Genomicclassificationandprognosisinacutemyeloid
scrna_mutations/tree/master/misc_scripts.Acomparabletoolprovidedby10xGenomics leukemia.N.Engl.J.Med.374,2209–2221(2016).
isavailableathttps://github.com/10xgenomics/vartrix. 31. Imoto,A.etal.Metallothionein-1isoformsandvimentinaredirectPU.1
downstreamtargetgenesinleukemiacells.J.Biol.Chem.285,10300–10309
Received: 10February 2019 Accepted: 23July 2019 (2010).
32. Zhang,P.etal.Negativecross-talkbetweenhematopoieticregulators:GATA
proteinsrepressPU.1.Proc.NatlAcad.Sci.USA96,8705–8710(1999).
NATURECOMMUNICATIONS| (2019) 10:3660 |https://doi.org/10.1038/s41467-019-11591-1|www.nature.com/naturecommunications 15
