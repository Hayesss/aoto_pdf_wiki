---
source_path: /mnt/c/Users/Administrator/Zotero/storage/C2FUKIY7/Gao 等 - 2021 - Transcriptome-wide quantification of double-stranded RNAs in live mouse tissues by dsRIP-Seq.pdf
ingested: 2026-04-23
sha256: 65f35858a0e918b9
---

ll
OPEN ACCESS
Protocol
Transcriptome-wide quantification of double-
stranded RNAs in live mouse tissues by dsRIP-
Seq
YimengGao,Shirui
Chen,Stephanie
Halene,Toma
Tebaldi
stephanie.halene@yale.
edu(S.H.)
toma.tebaldi@yale.edu
(T.T.)
HIGHLIGHTS
Purificationand
sequencingof
double-stranded
RNAs(dsRNAs)inlive
tissues
Open-source
computational
frameworkforthe
quantificationand
comparisonof
dsRNAs
Double-strandedRNAs(dsRNAs)areabundantlypresentincells,playingmultipleregulatory
functions.dsRNAsofviraloriginactivateinnateimmuneresponses.SinceRNAeditingand
modificationsaffectthestructureandrecognitionofRNAs,theiralterationcanresultinthe
accumulationofaberrantendogenousdsRNAsinducingadeleteriousinnateimmuneresponse.
Here,wepresentacompleteprotocolforthemeasurementofdsRNAsinalivemousetissue
usingdsRIP-Seq.Thisprotocolfocusesontissueisolation,dsRNAimmunoprecipitationand
downstreamcomputationalanalysis.
Gaoetal.,STARProtocols2,
100366
March19,2021ª2021The
Author(s).
https://doi.org/10.1016/
j.xpro.2021.100366
ll
OPEN ACCESS
Protocol
Transcriptome-wide quantification of double-stranded
RNAs in live mouse tissues by dsRIP-Seq
Yimeng Gao,1,2,5 Shirui Chen,3 Stephanie Halene,1,2,6,* and Toma Tebaldi1,2,4,5,*
1SectionofHematology,YaleCancerCenterandDepartmentofInternalMedicine,YaleUniversitySchoolofMedicine,New
Haven,CT06520,USA
2YaleStemCellCenterandYaleRNACenter,YaleUniversitySchoolofMedicine,NewHaven,CT06520,USA
3DepartmentofComputationalBiologyandMedicalSciences,GraduateSchoolofFrontierSciences,TheUniversityofTokyo,
Bunkyo-ku,Tokyo113-0032,Japan
4DepartmentofCellular,ComputationalandIntegrativeBiology(CIBIO),UniversityofTrento,Trento38123,Italy
5Technicalcontact
6Leadcontact
*Correspondence:stephanie.halene@yale.edu(S.H.),toma.tebaldi@yale.edu(T.T.)
https://doi.org/10.1016/j.xpro.2021.100366
SUMMARY
Double-stranded RNAs (dsRNAs) are abundantly present in cells, playing
multiple regulatory functions. dsRNAs of viral origin activate innate immune
responses. Since RNA editing and modifications affect the structure and
recognition of RNAs, their alteration can result in the accumulation of aberrant
endogenous dsRNAs inducing a deleterious innate immune response. Here, we
present a complete protocol for the measurement of dsRNAs in a live mouse
tissue using dsRNA immunoprecipitation and sequencing (dsRIP-Seq). This pro-
tocol focuses on tissue isolation, dsRNA immunoprecipitation and downstream
computationalanalysis.
For complete details on the use and execution of this protocol, please refer to
Gaoetal.(2020).
BEFOREYOUBEGIN
Timedbreeding
Timing:15–20days
1. Timedbreedingtoobtainfetalliver.
a. Setupmatingbetweenonemaleandtwofemalemice(8–16weeksold)percageintheafternoon
15–20daysbeforeexperiment.Setupasmanycagesasneededtoobtaindesirednumberoffetal
liverspergenotype,takingintoaccountbreedingsuccessformousestrainandseason.
b. Checkforvaginalplugeachmorningaftermatinghasbeensetup.Movefemalemousewith
plugtoaseparatecage.ThemorningaplugisdetectediscountedasdayE0.5.
c. OndayE14.5proceedwithfetalliverisolation.Usually,oneE14.5fetalliverwillyieldapprox-
imately30mgRNA((cid:1)40–50millionnucleatedcells),sufficientforasingleexperimentalsample.
Isolationofmurinefetallivers
Timing:2h
2. Thoroughly clean the bench and dissection tools with 70% ethanol and a cleaning agent to
removeRNases(e.g.,RNaseAwayTM).
STARProtocols2,100366,March19,2021ª2021TheAuthor(s). 1
ThisisanopenaccessarticleundertheCCBY-NC-NDlicense(http://creativecommons.org/licenses/by-nc-nd/4.0/).
ll
OPEN ACCESS Protocol
Figure1. MorphologyofmurineE14.5embryosandfetallivers
3. Prepare sterile petri dishes, dissection scissors, microdissection forceps (2) and tweezers
(2,41/4"extrafinepoint),24-wellplates,1.5mLEppendorftubes.
4. IsolatefetalliversfromthepregnantmouseatE14.5.
a. Preparetwotofourmatching24-wellplatesperpregnantfemaleandfilleachwellwith1mL
13PBS.Labeleachwellwithmouseidentifierandfetallivernumber.Ingeneral,expect4–10
fetalliversperpregnantfemale.
b. Sacrificethepregnantmousebyisofluoraneanesthesiaandcervicaldislocationperinstitu-
tional animal care and use committee guidelines. Disinfect the abdominal wall with 70%
ethanol.
c. Usingforceps,tentskinofthelowerabdomenandcutuptowardssternumtoexposeinternal
organs.Removebilateraluterinehornsandplacein10cmdiameterpetridishwith13PBSto
rinsematernalblood.
d. Gentlyremoveonefetal-placentalunitfromuteriatatimeusingextra-finepointtweezersand
separatefetusfromplacentaandplacefetusina24-wellfilledwith13PBS.Placethe24-well
plateonice.
e. Dissectthefetalliversfromthefetuses.Gentlyholdthebodyofthefetuswithonetweezer
while gently pulling the fetal liver (recognizable by its dark red color) away from the body
withthesecondtweezer.Placefetalliverinmatchingwellofsecond 24-well plate, also on
ice.Removeremnantconnectivetissuefromfetallivers.
5. Storethefetalliversinthe24-wellplateoniceforfurtherexperiments(Figure1).
CRITICAL: If genotyping of each fetal liver is required, clean utensils with 10% bleach
followedby70%ethanolin-betweeneachfetusandfetalliverprep.Afterisolationoffetal
livers, remove a small piece of fetus from each corresponding well for genotyping
followingstandardtissuelysisandDNAgenotypingprotocol.
2 STARProtocols2,100366,March19,2021
ll
Protocol OPEN ACCESS
KEYRESOURCESTABLE
REAGENTorRESOURCE SOURCE IDENTIFIER
Antibodies
NormalmouseIgG MilliporeSigma Cat#12-371;RRID:AB_145840
MouseMonoclonalAntibody English&Scientific Cat#10010200;RRID:AB_2651015
SCICONSJ2 ConsultingKft.
Chemicals,peptides,andrecombinantproteins
Sodiumchloride,5Msolution AmericanBio Cat#AB13198-01000
Magnesiumchloride,1Msolution AmericanBio Cat#AB09006-00100
Tris-HCl,1Msolution,pH7.4 AmericanBio Cat#AB14044-01000
IGEPALCA-630 Sigma-Aldrich Cat#I8896-50ML
cOmplete(cid:2),Mini,EDTA-free Sigma-Aldrich Cat#11836170001
ProteaseInhibitorCocktail
SUPERasedIn(cid:2)RNaseInhibitor ThermoFisherScientific Cat#AM2696
Water,RNasefree AmericanBio Cat#AB02128-00500
Dynabeads(cid:2)ProteinGfor ThermoFisherScientific Cat#10004D
Immunoprecipitation
TRIzol(cid:2)Reagent ThermoFisherScientific Cat#15596026
Chloroform J.T.Baker Cat#9180-01
GlycoBlue(cid:2)Coprecipitant ThermoFisherScientific Cat#AM9515
Criticalcommercialassays
RNeasyPlusMiniKit QIAGEN Cat#74134
KAPARNAHyperPrepKitwith Roche Cat#KK8560
RiboErase
Depositeddata
Mousegenomeandtranscript GencodeM15 https://www.gencodegenes.org/
annotation mouse/release_M15.html
Transcriptsequences Ensembl90 https://useast.ensembl.org/info/
website/archives/index.html
Experimentalmodels:organisms/strains
Mouse:Vav-Cre;Mettl3fl/fl (Gaoetal.,2020) N/A
Mouse:C57BL/6J Inhousecolony JAX:000664
Softwareandalgorithms
STARv2.3.3a N/A https://github.com/alexdobin/STAR
edgeR Bioconductor https://bioconductor.org/packages/
release/bioc/html/edgeR.html
FastUniqv1.1 N/A https://sourceforge.net/projects/fastuniq/
RNAfoldv2.4.11 ViennaRNApackage https://www.tbi.univie.ac.at/RNA/
FastQCv0.11.5 N/A https://www.bioinformatics.babraham.ac.uk/
projects/fastqc/
Other
TapeStation2200 AgilentTechnologies Cat#G2964AA
HiSeq2500SequencingSystem Illumina Cat#SY–401–2501
MATERIALSANDEQUIPMENT
dsRIPlysisbuffer
Reagent Finalconcentration Volume(100mL)
NaCl 100mM 2mL
Tirs-HClpH7.4 50mM 5mL
MgCl2 3mM 0.3mL
IGEPALCA-630 0.5% 0.5mL
H2O,RNase-free n/a 92.2mL
Total n/a 100mL
STARProtocols2,100366,March19,2021 3
ll
OPEN ACCESS Protocol
Onthedayoftheexperiment,to10mLdsRIPlysisbufferadd0.4mLof253CompleteProteinase
Inhibitorand20mLSUPERase,In(cid:2)RNaseInhibitorforimmediateuse;maintainat4(cid:3)C.
CRITICAL: The dsRIP lysis buffer can be stored at 4(cid:3)C for one month. Make fresh lysis
bufferiflongertimeperiodelapsesbetweenexperiments.
STEP-BY-STEPMETHODDETAILS
Double-strandedRNAimmunoprecipitation(dsRIP)fromfetallivers
Timing:4h
Thisprotocolallowsfortheisolationofdouble-strandedRNAs(dsRNAs)fromtissues,suchasmurine
fetallivers.Itispredictedtoworkwithothertissues,suchasbonemarrow,andcellpelletsofcelllines
orprimarycells.Cellnumbersequivalentto(cid:1)30mgRNAshouldbeused.Lysatesareincubatedwith
the mouse monoclonal anti-dsRNA antibody J2 followed by isolation with magnetic beads
(ProteinGDynabeads(cid:2))(BlangoandBass,2016;Lybeckeretal.,2014;Sonetal.,2015).
1. SetasideapproximatelyonefifthofeachfetalliverforpreparationoftotalRNAasinputcontrol
fordsRNAanalysis.ThetotalRNAcanbeextractedperstandardprotocoloftheQIAGENRNeasy
PlusMiniKit(Cat#74134)orfollowingthestandardTRIzolisolationprocedure.
2. Place the remainder of each fetal liver ((cid:1)30 million nucleated fetal liver cells) into a 1.5 mL
Eppendorftubewith600mLdsRIPlysisbuffer.Vortexandincubateoniceforexactly5min.If
thetissuesarefirmandhardtodissociateandlysebylysisbuffer,theyshouldbemincedprior
tolysisintosmallerfragments.
3. Spindowncelllysatesinatabletopcentrifugeatmaximumspeed(13,0003g)for10minat4(cid:3)C.
4. Carefullypipetequalvolumesofthesupernatantfromeachfetalliverintotwonew1.5mLtubes
placedonice.Add5mLanti-dsRNAJ2antibody(1mg/mL)toonetubeand5mgmouseIgGtothe
secondtubeandincubateat4(cid:3)Cfor2hwithrotation.Duringthisstep,dsRNAwillberecognized
and bound by J2 antibody while non-specific binding is expected to occur with mouse IgG
(Schonbornetal.,1991).Themousemonoclonalanti-dsRNAJ2antibodymaybereplacedby
other antibodies of interest, but readers should ensure specificity and that appropriate
Dynabeadsareused,accordingtothespeciesantibodiesareraisedin.
5. Towardstheendoftheincubationperiodofcelllysateswithanti-dsRNAJ2antibody,prepare
25mLProteinGDynabeadsforeachsample.
a. Aliquot25mLDynabeadsProteinGeachintotwo1.5mLtubesforeachfetalliverandadd
500mLdsRIPlysisbufferandvortex.
b. PlacethetubesonamagneticrackandallowbeadstocollectonsidewallofEppendorftube
for2min.
c. Carefully pipette off supernatant without dislodging beads while tube remains on the
magneticrack.Repeatthewashstep31.
d. Discardthesupernatantandkeepthebeadsforthenextstep.
6. Attheendofthetwo-hourlysate/antibodyincubationperiod,transferlysatestothetubeswith
theProteinGDynabeadsandincubateat4(cid:3)Cfor1hwithrotation.
7. Attheendoftheincubationperiod,placethetubesonthemagneticrackandallowbeadsto
collectonsidewalloftubes,removesupernatantandwashbeadsasunder5b–5d4timeswith
500mLdsRIPlysisbuffer.Thisstepshouldbeperformedinacoldroom.
8. PlacethetubeswithwashedbeadsoniceforRNAextraction.
ExtractionofimmunoprecipitateddsRNAs
Timing:1h
ThisprotocolallowsforisolationofJ2-immunoprecipitateddsRNAsfromfetallivers.
4 STARProtocols2,100366,March19,2021
ll
Protocol OPEN ACCESS
9. Add1mLTRIzoltoeachtubewithProteinGDynabeads(cid:2)andmixwellbypipettingupand
down.
10. Add200mLchloroformtotheTRIzolsolution,mixwellandincubateonicefor5min.
11. Spinat13,0003gfor15minat4(cid:3)C.
12. Carefullyremoveaqueousphase(530mL)withoutdisruptingproteinlayerordisturbingphenol
phase.Add200mLchloroformandincubateonicefor5min.
Note:Thesecondroundofincubationwithchloroformservestoreducecontaminationwith
phenol,whichisacommonproblemintheextractionoflowamountofRNAsinhibitingdown-
streamreactions(Tonietal.,2018).
13. Spinat4(cid:3)Cand13,0003gfor15min.
14. Transfer480mLoftheupperaqueousphaseasaboveintoequalvolume(480mL)isopropanol.
Add1mLGlycoBlueorRNAse-freeglycogenofchoice,invertbyhand10timestomixandincu-
bateat(cid:4)20(cid:3)Cfor20min.
15. Spindownat4(cid:3)Cand13,0003gfor10mintoprecipitateRNA.
Note:AdditionofglycogenservestomaketheRNApelletvisiblefollowingprecipitationand
topreventlossofRNAduringthenextwashandprecipitationsteps.
16. Pipetoffanddiscardthesupernatantandadd800mL75%ethanolinnuclease-freewatertothe
RNApellet.
17. Centrifugeat4(cid:3)Cand80003gfor5min.
18. Pipetoffanddiscardthesupernatant.
19. Pulsespinsamplesat(cid:1)23(cid:3)C.
20. CarefullyremovetheremainderofthesupernatantwithoutdisturbingtheRNApellet.
21. Air-drythepelletwiththelidopenat(cid:1)23(cid:3)Cfor5min.
22. Add15–20mLRNase-freewatertothepelletanddissolvedsRNAs.
23. Quantify RNA using a Nanodrop or other instrument to determine concentration and purity.
Usually,onesamplecanproducearound2ng/mLdsRNAcorrespondingto(cid:1)30ngintotal.Clear
absorbancepeaksat260nmand280nmshouldbeseen.
24. Perform quality control analysis on aTapeStationSystem using HighSensitivity RNA Screen-
Tape(Figure2).
Pausepoint:TheextractedRNAcanbestoredat(cid:4)80(cid:3)Cforuseinsubsequentsteps.
Librarypreparationandnext-generationsequencing
Timing:2–5days
25. Atthisstep,submitbothINPUTandexperimental(J2-dsRIPGIgG-dsRIP)samplesforlibrary
generation.NotethatIgGimmunoprecipitationmaynotyieldRNAsufficientforlibraryprepa-
ration(inourhands,IgGcontrolsyieldedconcentrationslowerthan0.1ng/mLandlessthan2ng
intotal,insufficientforsequencing).InthiscaseonlyINPUTandJ2-dsRNAsamplesshouldbe
processedfurther.
26. RibosomalRNA(rRNA)depletionandlibraryconstructionareperformedfollowingtheinstruc-
tionsoftheKAPARNAHyperPrepKitwithRiboErase.
27. Samplesarereadyforhigh-throughputsequencingonIlluminaorotherplatforms.Generally,60
millionreads/sampleshouldbesequencedtoyieldgoodresults.
rRNA depletion instead of mRNA selection is important for the dsRIP-seq to capture all possible
dsRNAsthatmayormaynothavepoly-Atails,suchascircularRNA(circRNA),forsequencing.
STARProtocols2,100366,March19,2021 5
ll
OPEN ACCESS Protocol
Figure2. ExamplesofRNAprofilesobtainedbydsRIPontheTapeStationSystem
EXPECTEDOUTCOMES
TheresultsofyourTapeStationqualitycontrolanalysis,performedpriortorRNAdepletionandli-
brarypreparation,willlikelydependonyourtissuesandexperimentalconditions.Weobserveda
randomdistributionofRNArangingfrom50nucleotides(nt)to4000ntlengthontheTapeStation
systemwithapeakaround200ntinthewildtypesamples.Weobservedsharppeakscorresponding
tothesizesofthe18Sand28SrRNAs(Figure2).
QUANTIFICATIONANDSTATISTICALANALYSIS
Pre-processingofnext-generationsequencingdata
This section lists all the computational steps necessary to obtain gene or transcript specific read
counts starting from sequencing raw data (FASTQ). In the simplest experimental design, dsRIP
andINPUTlibrarieswithideally3ormorebiologicalreplicatesareexpected.Inourworkedexample,
wesequencedlibrarieswithIllumina,23100pairedendsequencing,obtainingapproximately60
millionofreadpairsforeachsample.
28. PerformqualitycontrolofFASTQfileswithFastQCorsimilartools.QCmetricsshouldresemble
those obtained by RNA-seq of the same tissue, in our worked example we only observed a
higherpercentageofduplicatedreads(Table1).
29. Optionally,removeduplicatedreadsfromFASTQfileswithFastUniq(Xuetal.,2012)orsimilar
tools.Inourworkedexamplewedecidedtoperformthisstep,promptedbytherelativelyhigh
amountofduplicates.Tobesuretopreventtheremovalofnaturalduplicates,UMIs(Unique
MolecularIdentifiers)shouldbeused(Kiviojaetal.,2011)UMIs,ormolecularbarcodes,arestan-
dardinalmostallsingle-cellRNA-seqandCLIP-seqprotocols.
30. Alignreadstoareferencegenomewithasplice-awarealigner.Inourworkedexample,reads
werealignedtothemousegenome,assemblyGRCm38.p5,withSTARversion2.5.3a(Dobin
etal.,2013)anddefaultparameters(seehttps://github.com/alexdobin/STARforafulltutorial
onthisaligner).
6 STARProtocols2,100366,March19,2021
ll
Protocol OPEN ACCESS
Table1. Sequencingstatisticsinourworkedexample
Sample Sequencedreadpairs Afterdeduplication Duplication%
dsRIP_ctrl_rep1 55162796 15529442 72%
dsRIP_ctrl_rep2 65336514 15878260 76%
dsRIP_trt_rep1 60185224 15682440 74%
dsRIP_trt_rep2 48709914 13363489 73%
INPUT_ctrl_rep1 65554565 12143560 81%
INPUT_ctrl_rep2 67722509 13159257 81%
INPUT_trt_rep1 66321387 13885129 79%
INPUT_trt_rep2 53744307 12558777 77%
31. QuantifyreadcountspergeneorpertranscriptfromBAMfiles.Inourworkedexample,gene-
specificreadcountswereobtainedrunningSTARwiththe–quantModeGeneCountsoption.We
usedtheGencodeM15transcriptannotationastranscriptomeguide.Alternativetoolscanbe
used,suchasFeatureCountsorHTSeq.
32. Loadthetableofreadcounts,witheachcolumnassociatedwithasampleandeachrowasso-
ciatedwithageneortranscript,intheRsoftwareenvironment.Filteroutgenesortranscripts
withloworabsentsignals.Inourworkedexample,weselectedgeneswithatleast10rawreads
in all the replicates of at least 1 condition (dsRIP or INPUT). This filter selected 13779 out of
52640annotatedgenes.ThespecificRcodeusedfortheworkedexampleisavailableanden-
ablesthereproductionoftheanalysesshowninthisprotocol:https://github.com/tomateba/
dsRIP-Seq.
33. Normalizecounts across samples. Inourworked example, we used theTMM method imple-
mented in the edgeR Bioconductor package (McCarthy et al., 2012) (see https://www.
bioconductor.org/packages/release/bioc/html/edgeR.htmlforafulltutorialonedgeR).Alter-
natively,similarpackagessuchasDESeq2canbeusedforthenormalizationandfortheidenti-
ficationofdsRNA(seehttps://bioconductor.org/packages/release/bioc/html/DESeq2.htmlfor
atutorialonDESeq2).
IdentificationofdsRNAsbycomparingdsRIPandINPUTnormalizedsignals
Inthesimplestexperimentaldesign,notinvolvingdifferentialconformationanalysis,genesortran-
scriptsthataremorelikelytobeindsRNAconformationcanbeidentifiedbycomparingdsRIPand
INPUTsignals(Figure3).
34. IdentifydsRIPenrichedgenesortranscripts.Inourworkedexample,weusedgeneralizedlinear
models implemented in edgeR (glmQLFTest function). The contrast used for this analysis is:
ðdsRIP (cid:4)INPUTÞ.Afterapplyingthiscontrast,selectgenesortranscriptsindsRNAconforma-
tion applying a significance threshold (p(cid:4) value<0:05) and a fold enrichment threshold
ðlog dsRIP=INPUTÞ>0.
2
DifferentialanalysisofdsRNAscomparingtwoconditions
Inthisexperimentaldesign,theaimoftheanalysisistoidentifychangesinthedsRNAconformation
ofgenesortranscriptsbycomparingtwoconditions.Inthegeneralcase,theseconditionscanbe
namedcontrol(ctrl)andtreatment(trt).GenesortranscriptswithenricheddsRNAconformationin
thetreatmentconditioncanbeidentifiedapplying3differentcriteria,explainedbelow(Figure3).
35. IdentifydsRIPenrichedgenesortranscripts,consideringbothcontrolandtreatmentconditions.
ThiscriterionselectsgenesortranscriptsthataremorelikelytobeinadsRNAconformation.In
ourworkedexample,weusedgeneralizedlinearmodelsimplementedinedgeR(glmQLFTest
function).Thecontrastusedforthiscriterionis:
STARProtocols2,100366,March19,2021 7
ll
OPEN ACCESS Protocol
Figure3. ComputationalanalysistoidentifyandcomparedsRNAs,withexamples
ðdsRIP
ctrl
+dsRIP
trt
Þ(cid:4)ðINPUT
ctrl
+INPUT
trt
ÞAfterapplyingthiscontrast,selectgenesortranscripts
in dsRNA conformationapplying a significance threshold (p(cid:4)value<0:05)and a fold enrichment
thresholdðlog dsRIP=INPUTÞ>0.
2
36. Identify genes or transcripts showing significant changes in dsRNA conformation comparing
treatmentandcontrolcondition,normalizingforINPUT.Thiscriterionselectstranscriptsthat
arespecificallyalteredinthedsRIPsignalofthetreatmentversuscontrolcondition,normalizing
forvariationsintheINPUT,thatcouldbeduetoexpressionchanges.Usinggeneralizedlinear
modelsimplementedinedgeR(glmQLFTestfunction),thecontrastusedforthiscriterionis:
ðdsRIP
trt
(cid:4)dsRIP
ctrl
Þ(cid:4)ðINPUT
trt
(cid:4)INPUT
ctrl
Þ,thatisalsoequivalenttothecontrast:
ðdsRIP (cid:4)INPUT Þ(cid:4)ðdsRIP (cid:4)INPUT Þ
trt trt ctrl ctrl
After applying this contrast, select genes or transcripts applying a significance threshold
(p(cid:4) value<0:05) and a fold change threshold, for example ðlog 2 dsRIP trt (cid:4)log 2
INPUT trt Þ>ðlog 2 dsRIP ctrl (cid:4)log 2 INPUT ctrl Þ to look for increased dsRNA conformation in the
treatmentcondition,orðlog
2
dsRIP
trt
(cid:4)log
2
INPUT
trt
Þ<ðlog
2
dsRIP
ctrl
(cid:4)log
2
INPUT
ctrl
Þtolookfor
decreaseddsRNAconformationinthetreatmentcondition.
37. IdentifygenesortranscriptswithmajorcontributionofdsRIPchangesoverINPUTchanges.This
criterionselectsgenesortranscriptsforwhichthechangeindsRIPlevels(treatmentvscontrol)is
larger,inabsolutevalues,thanthechangeinINPUTlevels.Thiscriterionisimportanttoexclude
genesthat,forexample,decreaseinbothdsRIPandINPUT,butmoreinthelatter.Thesegenes
8 STARProtocols2,100366,March19,2021
ll
Protocol OPEN ACCESS
Figure4. ExamplesofdownstreamanalysisoftheidentifieddsRNAs
couldresultenrichedintheanalysisdescribedatpoint34,justbecausetheirdecreaseindsRIPis
lowerthantheirdecreaseinINPUT.Yetforthesegenesvariationsinexpressionlevelsarelarger
thanvariationsinconformations,thereforetheyshouldbeconsideredwithcautionorexcluded
from the analysis. Considering average expression values among replicates, select genes or
transcriptswithjlog
2
dsRIP
trt
(cid:4)log
2
dsRIP
ctrl
j>jlog
2
INPUT
trt
(cid:4)log
2
INPUT
ctrl
j.Inourworked
example,thiscriterionwasnotassociatedwithanedgeRcontrast,thereforeitisnotdependent
onapvalue.
DownstreamstructuralandfunctionalanalysisofdsRNAs
ThepopulationsofrelevantgenesortranscriptswithdsRNAconformationidentifiedbydsRIP-Seq
canbefurthercharacterizedwithstructuraloffunctionalcomputationalanalysistools(Figure4).
38. Predictthesecondarystructureoftheidentifiedgenesortranscripts.Inourworkedexample,we
usedtheRNAfoldalgorithmcontainedintheViennaRNApackage(v2.4.11)(Lorenzetal.,2011)
(seehttps://www.tbi.univie.ac.at/RNA/RNAfold.1.htmlforatutorialonRNAfold).Thisalgorithm
requiresasinputafastafileoftranscriptsequencesandenablesthepredictionoftheminimum
free energy (MFE) structure, with the corresponding free folding energy, and also more
advanced features such as thermodynamic ensemble prediction and the ensemble diversity,
describing the flexibility of the expected RNA structure by measuring the diversity of the
ensemblestructures.Inourworkedexample,weexecutedRNAfoldstartingwiththefastafile
ofwholetranscriptsequenceswiththefollowingcode:RNAfold–infile=input.fasta–MEA-d2
-p. Numerical features such as folding free energy and ensemble diversity can be used to
compare the population of dsRIP enriched vs non-enriched transcripts. Predicted secondary
structures for each transcript, in the commonly used dot-bracked notation, can be displayed
withmultipleonlinetoolssuchasforna(http://rna.tbi.univie.ac.at/forna/)orfurtherdissected
toidentifylongdsRNAregionsandstructuralmotifs.
STARProtocols2,100366,March19,2021 9
ll
OPEN ACCESS Protocol
LIMITATIONS
TheapproachpresentedhereisbasedontheJ2antibodytospecificallyrecognizedsRNAsand
performtheimmunoprecipitation.SinceithasbeenreportedthatJ2antibodymainlyrecognizes
dsRNAslongerthan40bp,dsRNAswhichareshorterthan40bpmaybemissedinthisanalysis.
Besides fetal livers, other tissues and cells can also be used for the dsRIP-Seq, as long as they
can provide enough RNA for the immunoprecipitation. As far as we have tested, a E14.5 fetal
liver can yield more than 20 mg RNA. Therefore, any fresh tissue or cultured cell lines that can
provide similar RNA quantities, can be considered as a feasible starting material. While
the dsRIP-Seq approach enables the identification of RNAs enriched in double stranded
conformation, the specific location of dsRNA regions within long transcripts cannot be directly
sequenced, as the RNA fragmentation step is performed after RNA immunoprecipitation. RNA
fragmentation or partial digestion before immunoprecipitation would theoretically enrich the
library with specific dsRNA regions, but this approach would require more starting material, a
more complex experimental protocol and computational workflows based on peak callers such
as those used in the context of identifying RNA-protein interactions (CLIP-seq) or m6A
enrichment sites (m6A-RIP).
TROUBLESHOOTING
Problem
Uncertaintyoffetallivertiming.
Potentialsolution
Itisbesttocheckforvaginalplugsearlyinthemorning,especiallyinmultigravidamiceasitcanfall
out.Ifaplugisnotobvious,abluntsurgicalprobecanbeusedtodetectaplugthatisstillsituated
deeperinthefemalemouse’svagina.
Problem
InsufficientRNAisisolatedafterdsRNAimmunoprecipitation.
Potentialsolution
SteriletechniqueandRNAsefreesurfaces,tools,andreagentsarekey.Incubationstepsshouldbe
exactly timed. Avoid unnecessary delays between steps. Long-term storage of RNA should be
avoided prior to sequencing. A positive control to confirm the dsRNA immunoprecipitation pro-
cess is1 mg polyinosinic:polycytidylic acid (pI:pC). 1 mg can be used to monitor and confirm the
efficiency of each step, as pI:pC is a well-characterized dsRNA which can be recognized by J2
antibody.
Problem
ContaminationofphenolafterRNAextractionidentifiedbyanunexpectedpeakat270nmduring
TapeStationsystemqualitycontrolanalysisofisolatedRNAs.
Potentialsolution
RNAmaybecontaminatedwithPhenol,inhibitingdownstreamsteps.RNAresuspendedin20mL
RNAsefreewatercanbere-extractedbyadding1mLTRIzolfollowedbycarefulexecutionofsteps
10–20.Especiallysteps16–20servetoeliminateallremnantphenolcontamination.Withatweezer
manipulateacleanKimwipestowipethesideoftheEppendorftubeaftereachchloroformstepto
furthereliminatephenol.BecarefulnottotouchtheRNApelletvisualizedbyadditionofGlycoBlue.
Ifasecondclean-upstepfails,theexperimentshouldberepeatedfromthebeginningstartingwith
newtissuetoobtainhigh-qualityRNAfordownstreamsequencing.
Problem
InterpretationofTapeStationqualitycontrolresultsandchoiceofdsRNAantibody.
10 STARProtocols2,100366,March19,2021
ll
Protocol OPEN ACCESS
Figure5. ExampleofanalysisanddsRNAquantificationoftransposableelements
Potentialsolution
If performed for the first time and under experimental conditions where expected results are
unknown,itisessentialtostrictlyadheretoRNAsefreeconditions,ensurehighqualityofreagents
andbuffersandexactdocumentationofexperimentalsteps.Itisadvisedthatsamplesfromcontrol
andexperimentalcondition(suchaswildtypeversusknockout)arealwaysperformedinparallel.At
least3biologicreplicatesshouldbeperformedforeachcondition.Thequalityoftheanti-dsRNAJ2
orotherantibodiesareessentialforthespecificimmunoprecipitationofdsRNA.Theprovidedinfor-
mation for the J2 antibody reflects the one with best performance in our hands. At the time of
receipt,researchersshouldresuspendaccordingtomanufacturerinstructionandgeneratemultiple
aliquots to avoid multiple freeze-thaw cycles. J2 antibodies produced by other companies or
provided in different forms may yield differing results. Although other dsRNA antibodies may
producesimilarresultstotheoneswithJ2antibody,wesuggestresearchersstartwithJ2antibody
sinceitisthemostwidelyusedandwell-characterizedanti-dsRNAantibody.
Problem
Analysisoftransposableelements
Potentialsolution
Transposableelements(TEs)compriseapproximatelyhalfofthemammaliangenomes.Iftheanalysisof
repetitivesequencestranscribedfromtransposableelementssuchasretrotransposonsisanimportant
aspectoftheexperiment,thedsRIPprotocolmayrequiresomemodifications,bothintheexperimental
and the computational parts. First, unique molecular identifiers (UMIs) should be ideally included in
librarypreparationtodiscriminatebetweentechnicalduplicates(duetoPCR)andnaturalduplicates,
such as repetitive elements (Kivioja et al., 2011). Libraries should be sequenced with a paired end
approach,asinourworkedexample,tryingtomaximizereadlength.Sequencedreadscomingfrom
repeatedelementsalsointroduce ambiguities inthe mapping step. Therefore, mapping parameters
can be adjusted to allow higher number of multi-mapped reads. Finally, the quantification of
transposableelementscanbeperformedwithdedicatedtools,recentlyreviewedin(Teissandieretal.
2019).Inourworkedexample,theanalysisofTransposableElements,includingtheirclassificationin
classes and families, was based on GTF filescurated bythe Hammell Lab: (http://labshare.cshl.edu/
shares/mhammelllab/www-data/TEtranscripts/TE_GTF/mm10_rmsk_TE.gtf.gz). Reads mapped on
transposableelementswereidentifiedandquantifiedwiththeRsubreadBioconductorpackage.Our
resultssuggestthatsomeretrotransposonclassesareenrichedindsRNAconformation(Figure5)
RESOURCEAVAILABILITY
Leadcontact
Further information and requests for resources and reagents should be directed to and will be
fulfilledbytheleadcontact,StephanieHalene(stephanie.halene@yale.edu).
STARProtocols2,100366,March19,2021 11
ll
OPEN ACCESS Protocol
Materialsavailability
Thisstudydidnotgeneratenewuniquereagents.
Dataandcodeavailability
Thisstudydidnotgenerateanyuniquedatasetsorcode.Rawandanalyzedsequencingdataforthe
workedexamplewerepreviouslydepositedunderGEO:GSE148882.
Software used for the analyses are described and referenced in the quantification and statistical
analysis subsections and are listed in the key resources table. The specific R code used for the
analysisoftheworkedexampleareavailableathttps://github.com/tomateba/dsRIP-Seq.
ACKNOWLEDGMENTS
This study was supported in part by the State of Connecticut under the Regenerative Medicine
ResearchFund(toS.H.;itscontentsaresolelytheresponsibilityoftheauthorsanddonotnecessarily
representtheofficialviewsoftheStateofConnecticutorConnecticutInnovations),theNIH/NIDDK
R01DK102792(toS.H.),andTheFrederickA.DelucaFoundation(toS.H.);Y.G.wassupportedby
the James Hudson Brown-Alexander Brown Coxe Postdoctoral Fellowships. T.T. was supported
byapilotgrantfromtheYaleCooperativeCenterofExcellenceinHematology(YCCEH)(NIDDK
U54DK106857)andbyAIRCunderMFAG2020-ID.24883project.
AUTHORCONTRIBUTIONS
Conceptualization,Y.G.,T.T.,andS.H.;experimentalmethodology,Y.G.andS.C.;computational
methodology,T.T.;writing,Y.G.,T.T.,andS.H.;fundingacquisitionandsupervision,S.H.
DECLARATIONOFINTERESTS
Theauthorsdeclarenocompetinginterests.
REFERENCES
Blango,M.G.,andBass,B.L.(2016).Identificationof Lorenz,R.,Bernhart,S.H.,HonerZuSiederdissen, Son, K.N., Liang, Z., and Lipton, H.L. (2015).
thelong,editeddsRNAomeofLPS-stimulated C.,Tafer,H.,Flamm,C.,Stadler,P.F.,andHofacker, Double-stranded RNA is detected by
immunecells.GenomeRes.26,852–862. I.L.(2011).ViennaRNAPackage2.0.Algorithms immunofluorescence analysis in RNA and
Mol.Biol.6,26. DNA virus infections, including those by
Dobin,A.,Davis,C.A.,Schlesinger,F.,Drenkow,J., negative-stranded RNA viruses. J. Virol. 89,
Zaleski,C.,Jha,S.,Batut,P.,Chaisson,M.,and Lybecker, M., Zimmermann, B., Bilusic, I., 9383–9392.
Gingeras,T.R.(2013).STAR:ultrafastuniversal Tukhtubaeva, N., and Schroeder, R. (2014). The
RNA-seqaligner.Bioinformatics29,15–21. double-stranded transcriptome of Escherichia Teissandier,A.,Servant,N.,Barillot,E.,and
coli. Proc. Natl. Acad. Sci. U S A 111, 3134– Bourc’his,D.(2019).Toolsandbestpracticesfor
Gao,Y.,Vasic,R.,Song,Y.,Teng,R.,Liu,C.,Gbyli,R.,
3139. retrotransposonanalysisusinghigh-throughput
Biancon,G.,Nelakanti,R.,Lobben,K.,Kudo,E.,etal.
sequencingdata.Mob.DNA10,52.
(2020).m(6)Amodificationpreventsformationof
McCarthy,D.J.,Chen,Y.,andSmyth,G.K.(2012).
endogenousdouble-strandedRNAsand
Differential expression analysis of multifactor Toni,L.S.,Garcia,A.M.,Jeffrey,D.A.,Jiang,X.,
deleteriousinnateimmuneresponsesduring
RNA-Seq experiments with respect to biological Stauffer,B.L.,Miyamoto,S.D.,andSucharov,C.C.
hematopoieticdevelopment.Immunity52,1007–
variation. Nucleic Acids Res. 40, 4288–4297. (2018).Optimizationofphenol-chloroformRNA
1021.e8.
extraction.MethodsX5,599–608.
Kivioja,T.,Va¨ha¨rautio,A.,Karlsson,K.,Bonke,M., Schonborn,J.,Oberstrass,J.,Breyel,E.,Tittgen,J.,
Enge,M.,Linnarsson,S.,andTaipale,J.(2011). Schumacher,J.,andLukacs,N.(1991).Monoclonal- Xu,H.,Luo,X.,Qian,J.,Pang,X.,Song,J.,Qian,G.,
Countingabsolutenumbersofmoleculesusing antibodiestodouble-stranded-Rnaasprobesof Chen,J.,andChen,S.(2012).FastUniq:afastde
uniquemolecularidentifiers.Nat.Methods9(1), Rnastructureincrudenucleic-acidextracts. novoduplicatesremovaltoolforpairedshort
72–74. NucleicAcidsRes.19,2993–3000. reads.PLoSOne7,e52249.
12 STARProtocols2,100366,March19,2021
