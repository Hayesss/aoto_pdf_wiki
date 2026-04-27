---
source_path: /mnt/c/Users/Administrator/Zotero/storage/GZQ93Q5F/Morse 等 - 2024 - SwiSnf chromatin remodeling regulates transcriptional interference and gene repression.pdf
ingested: 2026-04-23
sha256: 625e00c0c727048f
---

Article
Swi/Snf chromatin remodeling regulates
transcriptional interference and gene repression
Graphical abstract Authors
KaitlinMorse,AlenaL.Bishop,
SarahSwerdlow,JessicaM.Leslie,
Elc¸inU¨nal
Correspondence
elcin@berkeley.edu
In brief
Morseetal.uncoveredaroleforthe
conservedchromatinremodeling
complex,Swi/Snf,inaninducible
transcriptionalinterferencemechanism.
Byemployingbothclassicalgeneticsand
genome-wideapproaches,theirfindings
revealthatSwi/Snfrepressesselect
promotersthataresubjectto
transcriptionalreadthroughfroman
upstreampromoter.
Highlights
d UnbiasedgeneticapproachrevealsaroleforyeastSwi/Snfin
promoterrepression
d Swi/Snfrepressespromoterssubjecttoupstream
transcriptionalreadthrough
d RepressionisassociatedwithSwi/Snf-dependent
nucleosomeremodeling
d Swi/Snf-dependentrepressionregulatesproteinlevelsfor
LUTI-regulatedgenes
Morseetal.,2024,MolecularCell84,1–18
August22,2024ª2024PublishedbyElsevierInc.
ll
https://doi.org/10.1016/j.molcel.2024.06.029
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
Swi/Snf chromatin remodeling regulates
transcriptional interference and gene repression
KaitlinMorse,1AlenaL.Bishop,1SarahSwerdlow,1JessicaM.Leslie,1andElc¸inU¨nal1,2,*
1DepartmentofMolecularandCellBiology,UniversityofCalifornia,Berkeley,BarkerHall,Berkeley,CA94720,USA
2Leadcontact
*Correspondence:elcin@berkeley.edu
https://doi.org/10.1016/j.molcel.2024.06.029
SUMMARY
Alternativetranscriptionstartsitescanaffecttranscriptisoformdiversityandtranslationlevels.Inarecently
describedformofgeneregulation,coordinatedtranscriptionalandtranslationalinterferenceresultsintran-
scriptisoform-dependentchangesinproteinexpression.Specifically,alongundecodedtranscriptisoform
(LUTI)istranscribedfromagene-distalpromoter,interferingwithexpressionofthegene-proximalpromoter.
AlthoughtranscriptionalandchromatinfeaturesassociatedwithLUTIexpressionhavebeendescribed,the
mechanismunderlyingLUTI-basedtranscriptionalinterferenceisnotwellunderstood.Usinganunbiasedge-
neticapproachfollowedbyfunctionalgenomics,weuncoveredthattheSwi/Snfchromatinremodelingcom-
plexisrequiredforco-transcriptionalnucleosomeremodelingthatleadstoLUTI-basedrepression.Weiden-
tified genes with tandem promoters that rely on Swi/Snf function for transcriptional interference during
proteinfoldingstress,includingLUTI-regulatedgenes.ThisstudyprovidesclearevidenceforSwi/Snfplaying
adirectroleingenerepressionviaacistranscriptionalinterferencemechanism.
INTRODUCTION Casestudieshaverevealedthatdiversegenetargetsaresubject
to LUTI-based repression, including the genes encoding the
Gene regulation underlies proper development, homeostasis, kinetochore subunit Ndc80,7,9 the superoxide dismutase
and cellular stress response. According to classical models, enzymeSod1,13theTFSwi4,14andthepurinehydrolaseenzyme
transcriptlevelsdirectlycorrelatewithproteinsynthesis.How- Hnt1.11,15 Importantly, the observation that the human proto-
ever,thehighprevalenceofnon-codingtranscriptionandvaria- oncogene MDM2 is subject to LUTI-based regulation has re-
tionintranslationefficiencyamongtranscriptisoformshaveun- vealedthisformofgenerepressionisbroadlyconserved.16
veileddeepercomplexityintheRNA-to-proteinrelationship.1–6 DespitetheprevalenceofLUTI-regulatedgenes,themecha-
Recently, an unconventional form of gene repression was nism underlying LUTI-based transcriptional interference is not
discovered where messenger RNA (mRNA) and protein levels well understood. In fact, transcript isoform profiling revealed
are inversely correlated. For these genes, transcription from a that the degree of proximal promoter repression during LUTI
distal promoter produces a 50 extended mRNA containing the expressionisvariable,indicatingLUTI-mediatedtranscriptional
downstreamgene’sentirecodingsequence(CDS).7,8Upstream repressionisdifferentiallyregulated.10Severalfactorsarecorre-
openreadingframes(uORFs)intheextendedmRNA’s50leader lated with LUTI-based transcriptional interference in yeast,
restrictCDStranslation.Accordingly,thisdistalmRNAisoformis includinghighLUTIexpression,increasedhistone3lysine36tri-
termedthelongundecodedtranscriptisoform(LUTI).LUTItran- methylation (H3K36me3) at the CDS-proximal promoter, and
scription also interferes with transcription from the CDS-prox- changes in nucleosome positioning around the CDS-proximal
imalpromoterthatcontrolsexpressionofthecodingmRNAiso- promoter.10 However, detangling causality from correlation for
form.9,10 This combined transcriptional and translational these chromatin and transcriptional features requires more in-
interference reduces protein synthesis for the affected gene. depthfunctionalanalysis.Inthisstudy,weusedanunbiasedge-
Thus,LUTIsexplaincaseswheremRNAandproteinlevelsare netic approach to identify new regulatory factors required for
poorlycorrelated.8 LUTI-based transcriptional interference in budding yeast. This
LUTI-basedgenerepressionispervasive.Inyeast,hundreds strategy led us to uncover a direct, repressive function of the
ofgeneshaveanassociatedLUTIthatisexpressedatdistinct Swi/Snf chromatin remodeling complex in establishing tran-
meiotic stages to temporally restrict protein synthesis.8 Addi- scriptionalinterference.
tionally, cellular stress stimulates activation of LUTIs by the The Swi/Snf complex is a conserved, twelve-subunit ATP-
unfoldedproteinresponse(UPR)transcriptionfactor(TF)Hac1 dependent nucleosome remodeling complex.17–21 We show
andduringzincstarvationbythezinc-responsiveTFZap1.11,12 thatinadditiontoitscanonicalfunctioningeneactivation,the
MolecularCell84,1–18,August22,2024ª2024PublishedbyElsevierInc. 1
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
(legendonnextpage)
2 MolecularCell84,1–18,August22,2024
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
Swi/Snfcomplexperformsnucleosomeremodelingdownstream LUTI escape phenotypes (Figures S1B and S1C). Snf11 might
oftheactivetranscriptionstartsite(TSS)foritstargetloci.When haveeludedourselectionduetoitssmallsize(169aminoacids).
theSwi/Snfcomplexisrecruitedtodistalpromoters,thisdown- We only recovered mutations in Swi/Snf subunits, not other
stream remodeling interferes with CDS-proximal promoters, chromatin remodelers like Chd1 or Isw, and remodelers have
leading to gene repression for select LUTI-regulated genes. In known functions in co-transcriptional nucleosome remodel-
addition to furthering our understanding of LUTI-based tran- ing.18,28,29 Deletion of ISW1, ISW2, or CHD1, individually or
scriptional interference, our results clarify a long-standing together,didnotdisruptLUTI-basedrepressionofHIS3LUTIand
questioninthechromatinremodelingfieldbyprovidingconclu- ADE2LUTI(FiguresS1EandS1F).DeletionofFUN30,involvedin
siveevidencethattheSwi/Snfcomplexcandirectlyrepresstran- transcriptional silencing,30 also did not affect HIS3LUTI-based
scriptioninvivothroughitsnucleosomeremodelingactivity. repression(FigureS1E). These resultssuggestthatthe Swi/Snf
complexspecificallyplaysaroleinLUTI-basedgenerepression.
RESULTS
LUTIescapemutationsconferpartiallossofSwi/Snf
Ageneticapproachtoidentifymutantsdefectivein function
LUTI-basedgenerepression AllLUTIescapemutantsconferredrecessivephenotypesexcept
ToidentifyfactorsnecessaryforLUTI-basedrepression,weun- forsnf2-Q928K (TableS1),which displayed apartialdominant
dertookageneticapproach.WegeneratedtwoLUTIreporteral- phenotype(Figure2A;TableS1).Wechosetousethismutant
leles by fusing the 50 leader sequence of a well-characterized along with snf2-W935R and swi3-E815X, a nonsense mutant
LUTI, NDC80LUTI,7,9 to the HIS3 and ADE2 CDSs (Figure 1A). affecting the structural subunit Swi3, for further investigation
Cells with LUTI-based regulation intact are unable to grow (Figures 1E and 1F). These three mutants were chosen based
without supplemented histidine when HIS3LUTI is expressed. ontheirminimalgrowthdefectscomparedwithsnf2Dorswi3D
Therefore,wefirstselectedspontaneousmutantswithdisrupted (Figure S2A) and strong LUTI escape phenotypes (Figures 1C
LUTI-based repressionthatwereableto growduringHIS3LUTI and 1D). For each gene, we constructed strains lacking the
induction on media lacking histidine (Figure 1C; see STAR endogenousalleleandharboringatransgenicrescueconstruct
Methods for details). These were deemed ‘‘LUTI escape mu- containingeitherthewild-typealleleofthegeneasacontrolor
tants’’ based on their inability to repress His3 expression. We theLUTIescapeallele,eachunderthenativegenepromoter.
nextperformedsecondaryscreeningoneachmutantusingthe BecausenullmutationsinSNF2orSWI3arepleiotropic,27we
independentADE2LUTIreporterphenotype:cellswithLUTIregu- wonderedwhethertheLUTIescapemutantsbroadlysharephe-
lation intact appear red, whereas cells with disrupted LUTI- notypeswiththeirrespectivenullmutantsoriftheyinsteadaffect
basedrepressionappearlightpinkorcream(Figure1D). specificfunctionsoftheSwi/Snfcomplex.Wefirstexamineda
To identify the causative mutations behind the LUTI escape well-characterizedSwi/Snfloss-of-functionphenotype:inability
phenotypes, we sequenced the genomes of cells exhibiting to ferment sucrose.31 As expected, snf2D and swi3D mutants
bothHIS3LUTIandADE2LUTIescapephenotypes.Weidentified grew poorly in sucrose media (Figure 2B). By contrast, the
andvalidatedelevenmutationsconferringLUTIescapepheno- swi3-E815X mutant grew at a rate identical to wild-type cells,
types(seeSTARMethodsfordetails).Strikingly,allLUTIescape whilethesnf2-W935Randsnf2-Q928Kmutantsonlyexhibited
mutations fell within genes encoding subunits of the Swi/Snf slightgrowthdefects(Figure2B).
chromatinremodelingcomplex(Figures1B,1F,andS1A).Our TobetterunderstandhowtheLUTIescapemutantsaffectgene
selection-basedstrategyuncoveredmutationsinsixoftheeight expression at a global scale, we performed mRNA sequencing
subunits that are specific to the Swi/Snf complex and are not (mRNA-seq)onswi3-E815X,snf2-W935R,andsnf2-Q928Kmu-
members of other chromatin remodeling complexes,24–26 with tantsalongwiththerespectivewild-typecontrolandnullmutant.
five of the identified mutations falling within SNF2, which en- Although the snf2D and swi3D mutants displayed widespread
codesthecatalyticsubunit(Figure1B). changes in gene expression compared with wild type (Spear-
We did not find mutations in SWP82 or SNF11, which also man’s rank correlation coefficient, r = 0.883 [snf2D], r = 0.892
encode Swi/Snf complex subunits. Deletion of SWP82 did not [swi3D];Figures2CandS2D),theLUTIescapemutantsaffected
affectLUTI-basedrepression(FiguresS1BandS1C),likelydue onlyalimitednumberofgenes(Figure2C).Hierarchicalclustering
to its limited role in Swi/Snf function (Figure S1D), consistent further revealed that swi3-E815X and snf2-W935R mutants
withpreviousresearch.27Bycontrast,snf11Dcellsshowedsubtle were grouped with the wild-type controls and displayed gene
Figure1. MutationsintheSwi/SnfcomplexdisruptLUTI-basedtranscriptionalinterference
(A)SchematicofHIS3LUTIandADE2LUTIallelesinthereporterstrain(UB22912)usedtoselectforLUTIescapemutants.
(B)TableofspontaneousLUTIescapemutationsidentifiedfromHIS3LUTI-basedselectionandADE2LUTIsecondaryscreeningassays.
(C)HIS3LUTIserialdilutionandspottinggrowthassay.Strains(fromtoptobottom):UB29385,UB29188,UB29791,UB24301,UB28911,UB28919,UB28925.
(D)ADE2LUTIcolorassay.Strains:ade2-1(UB7),SNF2ADE2LUTI(UB30034),SWI3ADE2LUTI(UB30190),swi3-E815XADE2LUTI(UB23545),snf2-W935RADE2LUTI
(UB28923),andsnf2-Q928KADE2LUTI(UB30185).
(E)SchematicofprimaryproteinstructureforSwi3(left)andSnf2(right),withLUTIescapemutationsswi3-E815X,snf2-W935R,andsnf2-Q928Kmappedontothe
structure(arrows).
(F)Cryo-EMstructureoftheyeastSwi/Snfcomplexboundtoanucleosome(teal),publishedbyHanetal.22andrenderedinMolStar.23TheSnf2residuesW935
(purple)andQ928(orange),whichareaffectedbythesnf2-W935Randsnf2-Q928Kmutations,arehighlighted.TheCterminusofSwi3,whichisaffectedbythe
swi3-E815Xmutation,ishighlighted;however,thespecificregiontruncatedbytheswi3-E815Xmutationisnotresolvedonthisstructure.
MolecularCell84,1–18,August22,2024 3
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
Figure2. LUTIescapemutationsconferpartiallossofSwi/Snffunction
(A)HIS3LUTIserialdilutionandspottinggrowthassayinhaploidcellsharboringtransgenicallelesforSWI3(UB29792),swi3-E815X(UB29694),SNF2(UB28907),
snf2-Q928K(UB29170),orsnf2-W935R(UB29166).
(B)Growthcurvesforcellsgrowninrichmediawith2%sucroseforSWI3(UB19205,left,black),swi3-E815X(UB19209,left,blue),swi3D(UB27896,left,gray),
SNF2(UB28914,right,black),snf2-Q935R(UB28922,right,purple),snf2-Q928K(UB28915,right,orange),andsnf2D(UB29781,right,gray).Errorbarsrepresent
standarddeviation(n=3).
(C)Heatmapofhierarchicalclusteringperformedonstrainsinbiologicaltriplicate(yaxis,centeredcorrelationsimilaritymetric)producedfrommRNA-seqTPM
values.AllgeneswithTPM>0forallsamples(xaxis)areplottedinorderbasedontheirTPMvalueinthecontrolstrains.Strains(toptobottom)arethesameas
listedin(B).
expression profiles nearly matching that of wild-type cells (r = [swi3D], Figure S2C). The snf2-Q928K mutant downregulated
0.98 [swi3-E815X], r = 0.97 [snf2-W935R]; Figure S2D). By SRG1transcripttothesamedegreeassnf2Dcells(FigureS2B)
contrast, the snf2-Q928K mutant displayed an intermediate and upregulated SER3 (cid:2)40-fold relative to wild type (Fig-
gene expression profile (r = 0.947 [snf2-Q928K vs. wild type], ure S2C), whereas the swi3-E815X and snf2-W935R mutants
r=0.95[snf2-Q928Kvs.snf2D];Figures2CandS2D).Thesefind- regulated this locus normally. Thus, snf2-W935R and swi3-
ings confirm that the snf2-Q928K mutant displays more severe E815X mutants appear to display defects related to transcrip-
and pleiotropic loss-of-function phenotypes compared with tionalinterferenceatspecificloci.Altogether,weconcludethat
snf2-W935Randswi3-E815X. each LUTI escape mutation disrupts Swi/Snf function, but to
The Swi/Snf complex has been implicated in transcriptional varyingdegrees,withsnf2-Q928Kexhibitingmoreseveretran-
interference of the serine biosynthesis gene SER3. In serine- scriptionaldefectsthansnf2-W935Randsnf2-W935Rexhibiting
richconditions, Swi/Snfactivatesanupstreamintergenic non- slightlymoredefectsthanswi3-E815X(Figure2C).
coding RNAcalledSRG1,which reads throughthe SER3pro-
moter,resultinginrepressionofSER3.32–34Inserine-richmedia Swi/Snfregulatesalternativetranscriptisoform
bothsnf2Dandswi3DcellsexhibitedlowerlevelsofSRG1tran- expressioninresponsetoproteinfoldingstress
scriptcomparedwithwildtype(FigureS2B),leadingtosignifi- Direct interference through Swi/Snf chromatin remodeling at a
cant upregulation of SER3 (p = 0.0058 [snf2D], p = 0.0018 silencedpromoterhasnotpreviouslybeenobserved.Toexplore
4 MolecularCell84,1–18,August22,2024
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
(legendonnextpage)
MolecularCell84,1–18,August22,2024 5
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
this activity on a genome-wide scale, we turned to a cellular translation efficiency compared with the proximal isoform
contextduringwhichtranscriptisoformtogglingiswidespread: (TableS2).However,thesegenesremainusefulmodelstoinves-
theUPR.11Inordertoquantifydifferencesintranscriptisoform tigate Swi/Snf’s role in transcriptional interference. For these
expressionforgeneswithalternativeTSSs,weperformedtran- non-LUTIcases,Swi/SnfmayacttorepresstheTSSPROXupon
script leader sequencing (TL-seq)35 in wild-type and LUTI TSSDISTactivation;however,thereisnocorrespondingimpact
escapemutantsthatwereeitheruntreatedortreatedwithdithio- onproteinlevels.Indeed,whenwedeletedthedistalpromoter
threitol(DTT)toinducetheUPR.Torestrictouranalysistolociin forERG27,agenethatdidnotexhibitisoform-dependentprotein
whichthedistalTSS(TSSDIST)drivesreadthroughtranscription level changes (Figure S3C), there was a subtle increase in
across the CDS-proximal TSS (TSSPROX), we also performed ERG27PROXexpression(Figure3G).WeconcludethattheSwi/
Nanopore direct mRNA-seq (direct mRNA-seq) to visualize Snf complex represses transcription at select promoters that
full-length mRNA isoforms. Finally, we excluded indirect gene aresubjecttotranscriptionalreadthrough,includingLUTI-regu-
targets that do not exhibit Snf2 binding by performing Snf2 latedpromoters.
chromatin immunoprecipitation followed by whole genome AmongtheLUTIescapemutants,thesnf2-Q928Kmutantdis-
sequencing(ChIP-seq)(Figure3A). playedthemostchangesingenome-wideTSSexpressionlevels
Weuncovered12TSSPROXlocithatfitthefollowingcriteriaupon relativetowildtype(Figure3F),consistentwithmRNA-seqdata.
proteinfoldingstress:(1)theTSSPROXwassignificantlyupregu- Insnf2-Q928Kcells,theTSSDISTforfivegeneswasdownregu-
lated in one or more of the LUTI escape mutants (DESeq2, lated(HNT1,ODC2,PRY1,ERG27,andFLC1),thusTSSPROXup-
adjusted p > 0.05); (2) a TSSDIST-driven readthrough transcript regulationforthesegeneslikelyresultsfromreducedtranscrip-
wasexpressed;and(3)Snf2wasenrichedatthecorrespondinglo- tional readthrough (Figure 3F; Table S2). The snf2-W935R
cus. Upon induction of TSSDIST transcription, Snf2 occupancy mutant also exhibited downregulation of the TSSDIST for four
levels increased at the 50 regulatory region by an average of genes(ODC2,PRY1,ERG27,andFLC1),albeittoalesserextent
1.4-foldcomparedwithunstressedconditions(pairedttest,two- than in snf2-Q928K cells (Figure 3E). Finally, the swi3-E815X
tailed, p = 0.0423; Figure 3B). Excitingly, the TSSPROX for the mutant had the fewest changes in TSS expression compared
previouslycharacterizedLUTI-regulatedgeneHNT111wassignif- with wild type, both globally and among the 12 transcriptional
icantlyupregulatedinallthreeLUTIescapemutants(Figures3D– interferencetargets(Figure3D).
3F). Furthermore, analysis of a previously published ribosome Overall,TL-seqanalysesrevealthattheSwi/Snfcomplexreg-
profilingdataset11revealedthatADI1and ODC2alsoexhibited ulatestranscriptionalinterferenceinresponsetoproteinfolding
uORFtranslationinthe50leadersequenceoftheirdistalmRNAiso- stress through two routes: activation of distal promoters and
form(FigureS3B). Deletion of the distal promoterfor ADI1and repression of the downstream CDS-proximal promoters. It
ODC2resultedinincreasedabundanceoftheTSSPROX-derived seemsthesnf2-Q928Kmutationreducescanonicaltranscription
mRNA isoform and increased protein levels (Figures 3G and initiation activity by the Swi/Snf complex, consistent with our
S3C),revealingthesearealsoLUTI-regulatedgenes. previousfindingthatSRG1expressionisreducedinthismutant.
Fornineofthe12genes,thedistalmRNAisoformdidnotfitthe However,thesnf2-W935Rmutationonlyslightlyreducesinitia-
criteria of a LUTI because it did not display evidence of lower tion of the TSSDIST for some loci, yet still disrupts repressive
Figure3. Swi/SnfregulatesDTT-inducedalternativetranscriptisoformexpression
(A)SchematicofthestrategytoidentifySwi/Snf-regulatedalternativetranscriptsduringUPRinduction.Twelvegeneswereidentifiedthat(1)exhibitedsignificant
upregulationinoneormoreSwi/SnfmutantoftheTSSPROX(DESeq2,p<0.05),were(2)subjecttotranscriptionalreadthroughfromanupstreamdistalpromoter,
and(3)haveaSnf2ChIPpeakthatwascalledbyMACS2.
(B)Snf2ChIP-seqsignalsplottedforthe12genesidentifiedbythestrategyoutlinedin(A).Snf2enrichmentinwildtype(UB30387andUB30070;seeSTAR
Methodsfordetails)is1.4-foldhigheronaveragewhencellsaretreatedwithDTTcomparedwithpre-stress(pairedttest,two-tailed,p=0.0423,n=4).
(C)Volcanoplotproducedfromtheoutputofdifferentialgeneexpressionanalysis(DESeq2)onTL-seqdataforwild-typecells(UB19205andUB28914,seeSTAR
Methodsfordetails)thatwereuntreatedortreatedwithDTT(n=4).DistalTSSs(pink)andproximalTSSs(darkblue)forgenesthatareSwi/Snfregulatedand
exhibitstress-inducedpromotertogglingarehighlighted.
(D–F)Sameas(C)butcomparing(D)DTT-treatedswi3-E815X(UB19209)cellstoDTT-treatedSWI3(UB19205)cells(n=2),(E)DTT-treatedsnf2-W935R
(UB28922)cellstoDTT-treatedSNF2(UB28914)cells(n=2),and(F)DTT-treatedsnf2-Q928K(UB28915)cellstoDTT-treatedSNF2(UB28914)cells(n=2).
(G)RNAblot(top)andimmunoblot(bottom).BothblotsarespecificfortheV5sequencethatisC-terminallyfusedtoADI1(left),ODC2(middle),orERG27alleles
integratedattheTRP1locus.TransgeneseitherharboredtheTSSDISTanditspromoter(WT)orlackedthissequence(pDISTD).rRNAisdetectedbymethylene
bluestaining.Fortheimmunoblot,a-tubulinisusedasaloadingcontrol.Oneoftwobiologicalreplicatesisshown.Strains:ADI1(UB36511),ADI1pDISTD
(UB36513),ODC2(UB36515),ODC2pDISTD(UB36521),ERG27(UB36594),andERG27pDISTD(UB36596).
(H)GenomebrowsersnapshotsportrayingMNase-seq,TL-seq,andNanoporedirectmRNA-seqfortheHNT1locusforSNF2(UB30387),SWI3(UB30070),swi3-
E815X(UB30071),snf2-W935R(UB30391),andsnf2-Q928K(UB30389)cellsthatwereuntreated(top)ortreatedwithDTT(bottom).Oneoftwobiological
replicatesisportrayed,exceptfordirectmRNA-seqforwhichonlyonereplicatewasperformed.
(I)NucleosomefuzzinessscoresoutputfromDANPOS3forthe(cid:3)1nucleosomerelativetotheTSSPROXinwild-typecells(n=4,strainsUB30387andUB30070)
andswi3-E815X(UB30071),snf2-W935R(UB30391),andsnf2-Q928K(UB30389)mutants(n=2)thatwereuntreatedortreatedwithDTT.Apairedttestwas
performedonwild-typescorescomparinguntreatedtoDTT-treatedcells(two-tailed,p=0.0462)andeachmutant-to-wildtypecomparisoninuntreatedcon-
ditions(p=0.5938[swi3-E815X],p=0.2487[snf2-W935R],p=0.0371[snf2-Q928K])orwithDTTtreatment(p=0.1283[swi3-E815X],p=0.2043[snf2-W935R],
p=0.0129[snf2-Q928K]).
(J)Sameas(I),butforthe+1nucleosomerelativetotheTSSPROX.Apairedttestwasperformedonwild-typescorescomparinguntreatedtoDTT-treatedcells
(two-tailed,p=0.0729)andeachmutant-to-wildtypecomparisoninuntreatedconditions(p=0.4463[swi3-E815X],p=0.9578[snf2-W935R],p=0.4348[snf2-
Q928K])orwithDTTtreatment(p=0.0470[swi3-E815X],p=0.0397[snf2-W935R],p=0.0040[snf2-Q928K]).
6 MolecularCell84,1–18,August22,2024
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
activity by Swi/Snf at the TSSPROX. The swi3-E815X mutation indicatingthatderepressionofproximalmRNAisoformsinthe
alsoreducesrepressiveactivitybySwi/SnfattheTSSPROXbut mutantsmayresultfromincreasedpromoteraccessibility.
toalesserextentthanthesnf2-W935Rmutant.
Swi/Snffacilitatesrapidandsustainedrepressionof
NucleosomeremodelingisreducedattheTSSPROXin HNT1PROXuponHNT1LUTIinduction
Swi/SnfLUTIescapemutants TofurtherdissecttheroleoftheSwi/Snfcomplexintranscrip-
To investigate whether transcriptional interference at loci tionalinterference,wenextexaminedthekineticsofHNT1PROX
affected by LUTI escape mutants is mediated by changes in repressionandchromatinchangeswhenHNT1LUTIisinduced.
chromatinstructure,weperformedmicrococcalnucleasediges- Wild-typecellsinducedHNT1LUTIwithin5minofDTTtreatment,
tion and whole genome sequencing (MNase-seq). When we andHNT1LUTIfurtherincreased3-foldby30min,atwhichtime
analyzed the nucleosome profiles for the LUTI-regulated gene HNT1PROX was almost completely silenced (Figures 4A and
HNT1inwildtype,weobservedashiftfromstablenucleosome 4C).Snf2wasalsorecruitedtotheHNT1locuswithin5minof
positioning for the (cid:3)1 and +1 nucleosomes surrounding the DTTtreatment, andlevelsofSnf2bindingincreasedovertime
HNT1PROX TSS to fuzzy positioning upon DTT treatment (Fig- in a pattern that strikingly resembled the HNT1LUTI expression
ure3H),indicatingthatHNT1LUTIexpressionisassociatedwith pattern (Figures 4C and 4D). Along with this rapid recruitment
nucleosome remodeling downstream of the HNT1LUTITSS. By of the Swi/Snf complex following UPR induction, the (cid:3)1
contrast,the+1nucleosomerelativetotheHNT1PROXTSSre- and +1 nucleosomes surrounding the HNT1PROX TSS were
mainedstablypositionedinallthreeLUTIescapemutants(Fig- alsoremodeledwithin5minofDTTtreatment(Figure4E).
ure 3H), suggesting LUTI-coupled nucleosome remodeling is Consistent with the TL-seq results, snf2-W935R and swi3-
impaired in these mutants. The (cid:3)1 nucleosome relative to the E815X cells induced HNT1LUTI but failed to silence HNT1PROX,
HNT1PROX TSS, which spans the HNT1LUTI TSS in untreated exhibitinghigherlevelsoftheHNT1PROXisoformvisibleasearly
cells, also displayed a stronger MNase-seq signal in the snf2- as 15 min post-DTT treatment (Figure 4A). By contrast, snf2-
Q928Kandsnf2-W935RmutantswithDTTtreatment,although Q928KcellsfailedtoexpressHNT1LUTIandexhibiteddramatic
itspositionwasshiftedcomparedwiththeuntreatedcondition upregulation of HNT1PROX (Figure 4A). The high accumulation
(Figure 3H). Lack of remodeling for this nucleosome may ofHNT1PROXinthismutantresembledtheoutcomeofdeleting
preclude HNT1LUTI expression during UPR induction in snf2- theHNT1LUTIpromoter(FigureS4A),suggestingthatincreased
Q928K cells, as remodeling of the chromatin upstream of the HNT1PROX expression in snf2-Q928K cells was solely due to
HNT1LUTITSSisassociatedwithhighactivationofHNT1LUTIin the lack of HNT1LUTI expression. Importantly, the snf2-Q928K
wild-typecells. mutant properly activated the UPR response, as indicated by
We next investigated whether nucleosome positioning was splicingoftheHAC1mRNA36,37(FigureS4B),suggestingtran-
also stabilized in the LUTI escape mutants for the other 11 scriptionaldefectsinsnf2-Q928Kcellsarespecifictocertaintar-
TSSPROX loci. We compared nucleosome fuzziness scores, a getsanddonotresultfrombroadlyaberrantstressresponse.As
quantitativemeasurementfornucleosomepositioninginwhich expected,increasedlevelsofthecodingHNT1PROXmRNAiso-
higherfuzzinesscorrespondstomorepoorlypositionednucleo- form in each of the Swi/Snf LUTI escape mutants resulted in
somes,acrosswild-typeandmutantcells.Boththe(cid:3)1and+1 increasedHnt1proteinlevels(Figures4Aand4B).
nucleosomes surrounding each TSSPROX became more fuzzy GiventheimportanceoftheSnf2ATPasedomainandbromo-
inwildtypeuponDTTtreatmentcomparedwithunstressedcon- domain for Swi/Snf remodeling function and recruitment, we
ditions,indicatingremodeling ofthesenucleosomesisassoci- wondered whether mutations impacting these domains would
ated with distal promoter expression (paired t test, two-tailed, affectLUTI-basedregulation.RemovaloftheSnf2bromodomain
p=0.0462[(cid:3)1nuc],p=0.0729[+1nuc];Figures3Iand3J). (snf2-bromoD),whichmediatesSwi/Snfcontactwithacetylated
Nucleosome fuzzinessfortheTSSPROX(cid:3)1nucleosome was histones,17,38 resulted in reduced Snf2 occupancy at the LUTI-
not significantly different in the swi3-E815X or snf2-W935R regulatedgenesHNT1,ODC2,andADI1(FigureS4C).Interest-
mutantscomparedwithwildtypeduringstress,buttherewas ingly,basalSnf2occupancyattheselociinunstressedconditions
a significant decrease in fuzziness for the snf2-Q928K mutant seemedtobeimpactedmoresothanduringDTT-inducedstress,
(p=0.0129;Figure3I).AllthreeLUTIescapemutantsexhibited suggestingthereareothermodesbeyondhistoneacetylationfor
reducednucleosomefuzzinessfortheTSSPROX+1nucleosome Snf2recruitmenttoLUTI-regulatedgenesduringstressinduction.
comparedwithwildtype(p=0.0470[swi3-E815X],p=0.0397 WenextaskedwhethermutantsknowntoaffectSnf2ATPase
[snf2-W935R], p = 0.0040 [snf2-Q928K]; Figure 3J). These re- activitywouldimpactHNT1regulation.WeassayedthreeSNF2
sultsalignwiththepreviousfindingthatincreasedTSSPROX+1 aminoacidsubstitutionmutationsthateachhavebeenreported
nucleosome fuzziness was found to be correlated with more toconferlossofinvitroATPaseactivitytovaryingdegrees39,40:
potentLUTI-basedtranscriptionalinterference.10Wealsoexam- K798A (0% of wild-type activity), P824A (13%), and W935A
inedchangesinnucleosomeoccupancywithinthenucleosome- (80%).Thesnf2-K798AmutationresultedinreducedHNT1LUTI
depletedregion(NDR)fortheTSSPROXandfoundthatuponDTT levels and increased HNT1PROX levels (Figure S4F). The snf2-
treatment,nucleosomeoccupancywithintheNDRincreasedon W935A mutant phenotype resembled that of the snf2-W935R
average by 1.9-fold compared with the unstressed condition LUTIescapemutant,showingincreasedHNT1PROXtranscription
(p=0.0445;FigureS3D).EachLUTIescapemutanthadlower without strongly affecting HNT1LUTI transcription (Figure S4F).
nucleosome occupancy within the TSSPROX NDR compared Intriguingly,thesnf2-P824AmutantdidnotaffectHNT1regula-
withwildtypeuponDTTtreatment(notsignificant,FigureS3D), tion(FigureS4F).Thisfindingisconsistentwithpreviousstudies,
MolecularCell84,1–18,August22,2024 7
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
Figure4. Swi/SnffacilitatesrapidandsustainedrepressionofHNT1PROXuponHNT1LUTIinduction
(A)RNAblotprobedfortheHNT1CDS(top)andimmunoblotagainsttheV5epitopeforstrainsharboringanHNT1-3V5fusionallele(bottom).rRNAbandsare
detected by methylene blue staining, and a-tubulin is used as the immunoblot loading control. Strains: SWI3 (UB24251), swi3-E815X (UB24253), SNF2
(UB30152),snf2-W935R(UB30156),andsnf2-Q928K(UB30154).Oneoftwobiologicalreplicatesisshown.
(B)Quantificationofimmunoblotsportrayedin(A).Errorbarsrepresentstandarddeviation(n=2).
(C)RT-qPCRmeasuringrelativeabundanceofHNT1LUTImRNAforcells(UB29161)treatedwithDTT.Errorbarsrepresentstandarddeviation(n=2).
(D)Snf2ChIP-qPCRmeasuringrelativeoccupancyofSnf2-3V5(Swi/Snf)attheHNT1LUTITSS(black)orHNT1PROXTSS(gray).Errorbarsrepresentstandard
deviation(n=2).TheHMRlocuswasusedasaninternalcontrol.
(E)MNase-qPCRmeasuringrelativenucleosomeoccupancyattheHNT150regulatoryregion.Errorbarsrepresentstandarddeviation(n=2).ThePHO5promoter
wasusedasaninternalcontrol.
(F)RNAblot(top)probedfortheHNT1CDSandimmunoblotagainsttheV5epitopeforstrainsharboring3V5-IAA17auxin-inducibledegron(AID)alleleswithand
withoutdepletion(±TIR-F74G).rRNAbandsweredetectedbymethylenebluestaining,anda-tubulinwasusedasaloadingcontrolfortheimmunoblot(n=2).Ahigh-
contrast immunoblot image is presented for visualization of low-abundant proteins. Strains: SNF2-3V5-IAA17 (UB39148), SNF2-3V5-IAA17 + OsTIR1-F74G
(UB39150),INO80-3V5-IAA17(UB39160),INO80-3V5-IAA17+OsTIR1-F74G(UB39162),STH1-3V5-IAA17(UB39166),STH1-3V5-IAA17+OsTIR1-F74G(UB39168).
8 MolecularCell84,1–18,August22,2024
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
which noted milder in vivo phenotypes associated with snf2- hibited decreased occupancy of Snf2 at the HNT1PROX TSS
P824Acomparedwithsnf2-W935A,despitetheformerdisplay- duringstress(FiguresS5Cand S5D)and impairedremodeling
ing a more pronounced defect in in vitro ATPase activity.39 ofthe(cid:3)1and+1nucleosomessurroundingtheHNT1PROXTSS
Accordingly,whilesnf2-K798ArevealedthatSnf2ATPasefunc- (Figure S5E). Altogether, these results revealed that HNT1LUTI
tionisnecessaryforproperHNT1regulation,wefoundnoclear initiationissufficientforSwi/SnfrecruitmenttotheHNT1locus,
correlationbetweeninvitroATPaseactivitylevelsandimpacton butdownstreamSwi/Snfoccupancyandnucleosomeremodel-
LUTIregulation. ingattheHNT1PROXpromoterrequireproductiveelongationof
Swi/Snfinteractsbothcooperativelyandantagonisticallywith HNT1LUTI.
other ATP-dependent chromatin remodelers like the RSC and
INO80 complexes.19,20,41 The RSC complex works with Swi/ Swi/Snfregulatesgene-bodynucleosomeoccupancy
Snftoactivategeneexpressionduringproteinfoldingstress,20 foritscanonicalgenetargets
while the INO80 complex opposes Swi/Snf and RSC at some WewonderedwhetherSwi/Snf-dependenttranscriptionalinter-
genes.41 Null mutants for the catalytic subunits Ino80 (INO80 ferencestemsfromageneralfunctionoftheSwi/Snfcomplexin
complex)orSth1(RSC)arenotviable,sowecreatedconditional nucleosome remodeling during transcription elongation. Previ-
depletion alleles using the auxin-inducible degron (AID2) sys- ous studies implicated Swi/Snf in transcription elongation21,43;
tem.42 Depletion of Snf2 decreased HNT1LUTI expression and however,inthesecases,mutantanalysiswasperformedusing
increased HNT1PROX expression during protein folding stress snf2Dcells,whichexhibitseveretranscriptionaldefects,making
(Figure4F).Bycontrast,depletingIno80orSth1didnotaffect it difficult to uncouple transcription initiation from elongation
HNT1PROX repression (Figure 4F) but did induce HNT1LUTI phenotypes.Theswi3-E815Xandsnf2-W935Rmutantspresent
expression even without stress (Figure 4F), suggesting INO80 auniqueopportunitytoinvestigateSwi/Snfinacontextwhere
andRSCrepressbasalHNT1LUTIexpression. transcriptlevelsareunperturbedacrossmostgenes(Figure2C;
TableS3).
ChromatinchangesattheHNT1locusdependon First,wegeneratedalistofgenesthatweresignificantlydown-
transcriptioninitiationandelongationofHNT1LUTI regulatedinsnf2Dcellscomparedwithwildtypeundernormal,
We next sought to investigate whether Snf2 recruitment and unstressed conditions (DESeq2, adjusted p < 0.05). From this
nucleosome remodeling at the HNT1 locus are dependent on list,wenexteliminatedgenesthatwerenotboundbySnf2based
transcriptioninitiationofHNT1LUTI,itselongationthroughdown- onChIP-seqdata,asthesearenotdirectSwi/Snftargets.Finally,
streamchromatin,orboth.WeengineeredtwoLUTIperturbation we eliminated genes that were also differentially regulated in
mutants: one lacking the HNT1LUTI promoter (LUTID) and the either swi3-E815X or snf2-W935R mutants (Table S3). We did
other containing an insertion of a transcriptional terminator not remove genes affected by the snf2-Q928K mutant, as this
sequence(CYC1t)betweentheHNT1LUTIandHNT1PROXTSSs mutantconfersmoreseverelossofSwi/Snffunction,resembling
(Figure 5A). Both perturbations eliminated full-length HNT1LUTI null transcriptional phenotypes for many loci (Figure 2C). This
expression(Figure5B). yieldedalistof250Swi/Snftargets(Figure6A,left;TableS3).
As the HNT1LUTI TSS chromatin is deleted in the LUTID Asacontrolset,wegeneratedarandomsetof250geneswhose
mutant,thesignalforSnf2bindingwasreducedtobackground transcriptionwasnotsignificantlyaffectedbyanyoftheSwi/Snf
levelsinLUTIDcellsatthisposition(Figure5C).Snf2bindingat mutants(DESeq2adjustedp>0.05)andwerenotboundbySnf2
theHNT1LUTITSSwasunaffectedbyCYC1tinsertion,suggest- (Figure6A,right;TableS3).
ingHNT1LUTIinitiation eventsaresufficientforSwi/Snfrecruit- WenextcomparedaverageSwi/Snfoccupancyandnucleo-
ment upon DTT treatment (Figure 5C). Indeed, recruitment of some profiles for these two sets of genes between wild-type
thepre-initiationcomplexattheHNT1LUTITSSwasunimpaired and LUTI escape mutants. Importantly, Snf2 ChIP-seq and
intheCYC1tmutantasjudgedbyTFIIB(Sua7)enrichment(Fig- MNase-seqexperimentswereperformedwithspike-incontrol,
ure5F).Interestingly,bindingofSnf2attheHNT1PROXTSSwas enablingustocomparebetweensamples44(TableS3).Asex-
reducedinbothLUTIDandCYC1tmutantscomparedwithwild pected, LUTI escape mutants did not exhibit Snf2 binding or
typeuponUPRinduction(two-wayANOVA,p=0.0093[LUTID], nucleosomeprofiledifferencesforthecontrolsetofgenes,apart
p=0.0254[CYC1t];Figure5D).Toassaynucleosomeremodel- fromincreasedoccupancyofthe(cid:3)1and+1nucleosomeinsnf2-
ingintheLUTIperturbationmutants,werestrictedouranalysis Q928Kcellsthatmaybeduetothehigherdegreeofpleiotropyin
to positions with shared sequence identity among all three this mutant (Figures 6B and 6C). The swi3-E815X and snf2-
strains,whichencompassestheHNT1PROX+1nucleosome. In W935R mutants exhibited normal binding of Snf2 for Swi/Snf
contrast to wild type, this nucleosome was not remodeled in targets,withaverageSnf2occupancypeakingattheregionen-
LUTIDorCYC1tmutantswithUPRinduction(Figure5E). compassing the +1 through +3 nucleosomes (Figures 6B and
Although effective at eliminating HNT1LUTI expression, the 6C).Thesnf2-Q928Kmutant,however,exhibitedslightlylower
LUTIDmutationremovesalargestretchofDNAsequencethat Snf2occupancyatpositionsdownstreamoftheTSS(Figure6B).
maycontrolotheraspectsofHNT1regulationindependentlyof On average, the snf2-Q928K mutant also exhibited increased
LUTIexpression.Tofurtherinterrogatetherelationshipbetween nucleosomeoccupancywithintheNDRandatdownstreamnu-
HNT1LUTIexpressionandSwi/Snfactivity,wemadealessinva- cleosomesforSwi/Snftargets(Figures6C,S6C,andS6D).Inter-
sivemutantbyscramblingtheHac1bindingsite(UPRE)inthe estingly, the swi3-E815X and snf2-W935R mutants did not
LUTIpromoter(FigureS5A),whichdampenedbutdidnotelimi- impactthechromatinattheTSSor+1nucleosomeasstrongly
nate HNT1LUTI expression (Figure S5B). The upre mutant ex- asthesnf2-Q928Kmutantbutdidexhibitincreasednucleosome
MolecularCell84,1–18,August22,2024 9
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
Figure 5. Chromatin changes at the HNT1 locus
depend on transcription initiation and elongation of
HNT1LUTI
(A)SchematicofcisregulatoryHNT1mutantalleles.
(B)RNAblotprobedfortheHNT1CDSwithRNAcollected
from wild-type (UB32339), HNT1LUTID (UB32342), and
HNT1LUTI-CYC1t(UB36048)cellsthatwereuntreatedortreated
withDTT.
(C)Snf2ChIP-qPCRmeasuringrelativeoccupancyofSnf2at
theHNT1LUTITSS(n=2).
(D)Snf2ChIP-qPCRmeasuringrelativeoccupancyofSnf2at
theHNT1PROXTSS(n=2).Thereissignificantlydecreased
Snf2bindinginDTT-treatedHNTLUTIDcells(two-wayANOVA,
p=0.0093)andHNT1LUTI-CYC1tcells(two-wayANOVA,p=
0.0254) compared with wild type. Differences between the
HNTLUTIDandHNT1LUTI-CYC1tcellswerenotstatisticallysig-
nificant(two-wayANOVA,p=0.0560).
(E) MNase-qPCR measuring relative occupancy for the
HNT1PROX +1 nucleosome. Error bars represent standard
deviation(n=2).
(F) TFIIB (Sua7) ChIP-qPCR measuring relative occupancy
of Sua7 at the HNT1LUTI TSS in wild-type (UB38450) or
HNT1LUTI-CYC1t(UB38454)cellsharboringaSUA7-HAallele
thatwereuntreatedortreatedwithDTT(n=2).Differences
betweenthewild-typeandHNT1LUTI-CYC1tstrainswerenot
statistically significant (two-way ANOVA, p = 0.9969 [un-
treated]andp=0.4283[DTT]).
10 MolecularCell84,1–18,August22,2024
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
Figure6. Swi/Snfregulatesgene-bodynucleosomeoccupancyforitscanonicalgenetargets
(A)ScatterplotscomparingmRNAabundances(TPM)betweensnf2D(UB29781)andSNF2(UB28914)cells.GenesthatareSwi/Snf-regulated(left,n=250)or
genesfromanon-regulatedcontrolset(right,n=250)arehighlightedinpurple.
(legendcontinuedonnextpage)
MolecularCell84,1–18,August22,2024 11
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
occupancy for gene-body nucleosomes, especially for the +2 promoter, which resides downstream of the distal TSS be-
nucleosome (Figures 6C, S6C, and S6D). Because the overall comesnucleosomeoccupied,therebyresultingintherepres-
ranges for mRNA levels differed between the control set and sion of the protein-coding transcript isoform (Figure 7, top).
Swi/Snftargetset,weperformedthesamemetageneanalysis LUTIescapemutantsswi3-E815Xandsnf2-W935Rhavemini-
using filtered gene sets with closely matched transcripts per maleffectsonSwi/Snf’sabilitytofacilitatetranscriptioninitia-
million(TPM)levels.Nucleosomeprofilesafterfilteringstrongly tion at its target loci. Instead, these mutations specifically
resembledtheunfilteredprofiles(FigureS6E);therefore,remod- disrupt nucleosome remodeling at positions downstream of
elingdifferencesarenotduetoexpressiondifferencesbetween the active TSS, resulting in the repression of the TSSPROX for
groups. Swi/Snf’sTSSDISTtargets(Figure7,middle).Withmoresevere
Giventheireffectsongene-bodynucleosomes,wewondered lossofSwi/Snffunction,asinnullorsnf2-Q928Kmutants,re-
whethertheswi3-E815Xandsnf2-W935Rmutationsconferspe- modeling at the active TSS is reduced, leading to impaired
cific defects in co-transcriptional nucleosome remodeling. transcription initiation. In these cases, transcriptional interfer-
Whilethesemutantsdonotimpairtranscriptionelongationtoa enceattheTSSPROXforSwi/Snf’sTSSDISTtargetsisreduced
degreethatimpactstranscriptlevels(FiguresS6AandS6B),it indirectly, as a result of lower TSSDIST transcription (Figure 7,
ispossiblethattheactivityofothertranscriptionelongationfac- bottom).
torscompensatesforlossofSwi/Snffunctiontopromotenormal
RNApolymeraseII(RNAPolII)elongation.Totestthis,weexam- PhenotypicdifferencesamongLUTIescapemutants
inedtheeffectsofcombiningLUTIescapemutantswiththedele- Striking phenotypic differences were uncovered between the
tion of DST1, which encodes the elongation factor TFIIS.45–47 two missense mutations within the helicase domain of Snf2:
snf2-Q928K dst1D double mutant showed a severe growth snf2-W935R and snf2-Q928K. Binding of Snf2 is not reduced
defect,similartosnf2Ddst1Dcells(Figure6D),consistentwith at Swi/Snf target loci in either mutant (Figures 6B and S3A),
previousstudies.43,46Theswi3-E815Xandsnf2-W935Rmutants indicating these mutations confer remodeling rather than
alsoexhibitedgrowthdefectswhencombinedwithdst1D(Fig- recruitment defects. How might these mutations impact Swi/
ure6D).Additionally,theswi3-E815Xmutantcombinedwithde- Snfremodeling?Mappingtheseconservedresiduesonthecry-
letionsofotherelongationfactorgenes(isw1D,isw2D,chd1D, oelectronmicroscopy(cryo-EM)structureoftheSwi/Snfbound
elf1D, set2D, set3D, spt4D, paf1D) resulted in more severe toanucleosomerevealedthattheQ928residueofSnf2directly
growth defects (Figure 6E). These results indicate that the contactsnucleosomalDNA,whereastheW935residueresides
swi3-E815X and snf2-W935R mutants cause broad defects in inanearbypocketofSnf2thatdoesnotdirectlycontactDNAor
co-transcriptional remodeling, showing that Swi/Snf’s role in histones(Figure1F).Thisstructuralinformation,combinedwith
transcriptionelongationisseparatefromitsroleintranscriptional our findings that the snf2-Q928K impairs Swi/Snf function
activation. moreseverelythansnf2-W935R,suggeststheglutamineresi-
due at position 928 is critical for Snf2 remodeling function.
DISCUSSION Several cancer-associated mutations in humans also affect
residuesinthenucleosome-bindingregionoftheSNF2homo-
MutationsinSwi/Snfsubunitsarefoundin(cid:2)20%ofallhumantu- log BRG1,54 indicating this binding interface is functionally
mors,makingthecomplexoneofthemostcommonlyaffectedin conserved.
cancer.48 A few studies have provided evidence in support CurrentmodelssuggestthatSnf2’sATPhydrolysispromotes
ofSwi/Snfactingingenerepression,34,49–53however,ithasre- DNA translocation and nucleosome sliding.54–56 Missense
mained unclear whether Swi/Snf-dependent transcriptional mutations at nucleosome-binding sites in Snf2 may impair its
repressionoccursdirectlyorindirectly. ATPaseactivity.Thesnf2-W935AmutantreducesATPaseactiv-
Inthisstudy,wehavedemonstratedadirectroleoftheSwi/ ityto80%ofwild-typelevels.Althoughwedidnotmeasurethe
Snf complex in transcriptional repression. This occurs by co- in vitro ATPase activity of snf2-Q928K, similar Snf2 mutations
transcriptional nucleosome remodeling by Swi/Snf down- result in dominant-negative phenotypes, suggesting the snf2-
stream of distal TSSs expressing non-canonical transcripts Q928KphenotypemayarisefromATPbindingorhydrolysisde-
including LUTIs.Consequently,theNDRof theCDS-proximal fects. The snf2-W935R and snf2-Q928K phenotypes resemble
(B)HeatmapsportrayingnormalizedSnf2occupancygeneratedfromSnf2ChIP-seqdataforgenesthatareSwi/Snf-regulated(top)orthenon-regulatedcontrol
set(bottom).Strains:SWI3(UB30070),SNF2(UB30387),swi3-E815X(UB30071),snf2-W935R(UB30391),andsnf2-Q928K(UB30389).
(C)MetageneplotscreatedfromMNase-seqdataforgenesthatareSwi/Snfregulated(top)orthenon-regulatedcontrolset(bottom).Strainsarethesameas
in(B).
(D)SerialdilutionandplatinggrowthassayonYPDmediaforcellsharboringLUTIescapemutationsaloneorincombinationwithdeletionoftheelongationfactor
DST1.Strains:SWI3(UB19205),SWI3dst1D(UB36182),swi3-E815X(UB19209),swi3-E815Xdst1D(UB28096),SNF2(UB28914),SNF2dst1D(UB36185),snf2-
W935R(UB28922),snf2-W935Rdst1D(UB36186),snf2-Q928K(UB28915),andsnf2-Q928Kdst1D(UB36188).
(E)SerialdilutionandplatinggrowthassayonYPDmediaforcellsharboringtheswi3-E815Xmutationaloneorincombinationwithdeletionofvariouselongation
factors.Becauseofitsmoreseverephenotype,thepaf1Dassaywasimagedafter1(top)and2days(bottom)ofgrowthat30(cid:4)C.Allotherassayswereimaged
after1dayofgrowthat30(cid:4)C.Strains:SWI3(UB19205),swi3-E815X(19209),set2D(UB38653),set2Dswi3-E815X(UB38655),set3D(UB38657),set3Dswi3-
E815X(UB38659),isw1D(UB38665),isw1Dswi3-E815X(UB38667),isw2D(UB38669),isw2Dswi3-E815X(UB38671),chd1D(UB38661),chd1Dswi3-E815X
(UB38663), elf1D (UB39085), elf1D swi3-E815X (UB39087), spt4D (UB39097), spt4D swi3-E815X (UB39099), paf1D (UB39091), and paf1D swi3-E815X
(UB39093).
12 MolecularCell84,1–18,August22,2024
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
Figure7. ModelforSwi/SnfregulationofTSSactivationandrepression
Inwild-typecells(top),theSwi/Snfcomplexisrecruitedtocanonicalpromoters(left)ordistalpromoters(right)andperformsnucleosomeremodelingtoaidin
transcriptioninitiation.Swi/SnfperformsasecondaryfunctionatitstargetstoremodelnucleosomesdownstreamoftheactiveTSS,whichrepressesTSSPROX
promotersforitsTSSDISTtargets.Productiveremodelingisindicatedwithtranslucent,‘‘fuzzy’’nucleosomes,andinterferingnucleosomesareindicatedinred.
Middle:inswi3-E815Xandsnf2-W935Rmutants,transcriptioninitiationfunctionbytheSwi/Snfcomplexremainsintact,butdownstreamremodelingisimpaired.
Forcanonicaltargets,thesemutantscompromisenucleosomeremodelingwithinthegenebodywithoutcompromisingtranscriptionlevels.ForTSSDISTtargets,
reducednucleosomeremodelingdownstreamoftheactiveTSSresultsinderepressionoftheTSSPROX.Bottom:insnf2Q928Kcells,nucleosomeremodelingand
transcriptioninitiationatbothcanonicalandTSSDISTpromotersarereduced.ReducedtranscriptionalreadthroughresultsinderepressionoftheTSSPROX.
thoseofsnf2-W935Aandsnf2-K798A(FigureS4D),butimpaired Theswi3-E815XmutationresultsinatruncationofSwi3atits
ATPasefunctionalonedoesnotexplaintheLUTIescapepheno- C-terminal coiled-coil domain. As Swi3 is thought to act as a
type,asthesnf2-P824AmutantdidnotaffectHNT1regulation scaffoldforcomplexassembly,22,57defectsinSwi/Snfremodel-
(FigureS4D). ingcouldarisefromstructuralchangesinthismutantorreduced
MolecularCell84,1–18,August22,2024 13
Pleasecitethisarticleinpressas:Morseetal.,Swi/Snfchromatinremodelingregulatestranscriptionalinterferenceandgenerepression,Molecular
Cell(2024),https://doi.org/10.1016/j.molcel.2024.06.029
ll
Article
interactions between the complex with other TFs. Despite the Snf2ismosthighlyenrichedatthepromoter-proximal nucleo-
role for Swi3 in Swi/Snf assembly, the swi3-E815X mutation somesforitsgenetargets.65Geneswithgreaterdistancesbe-
only slightly reduced Snf2 occupancy at canonical and LUTI tweenthetwoTSSsmayrelyonothermechanismsfortranscrip-
target promoters (Figures 6B, S3A, and S3E), whereas the tionalinterferencetooccur,suchastheH3K36me3pathway.66
swi3DmutantexhibiteddramaticreductionofSnf2occupancy
(Figure S3E). We attribute the minimal effects in the swi3- RolesforSwi/Snfbeyondtranscriptionalactivation
E815XmutanttothesmallimpactthemutationhasonSwi3pro- While most investigations into Swi/Snf cellular function have
teincomposition(Figure1E).Inthecaseoftheswi3-E815Xand focusedonitsroleasaco-activator,67severalstudieshaveun-
snf2-W935R mutants, which primarily disrupt Swi/Snf co-tran- coveredevidenceindicatingtheSwi/Snfcomplexalsofunctions
scriptional remodeling without other pleiotropic defects, it is intranscriptionelongation.Forexample,Snf2bindswithsimilar
possible the mutations confer structural changes that inhibit patternsandkineticsasRNAPolIIalongcodingregionsuponin-
key interactions between the Swi/Snf complex and elongation ductionoftranscription.43Inparticular,Snf2occupiespromoters
factors. Additional work to investigate structural changes andcodingregionsforheat-shockinducedgenes,21andtran-
inducedbyLUTIescapemutationsandphysicalinteractionsbe- scription elongation of human HSF1 is necessary for Swi/Snf
tweenSwi/Snfsubunitswithtranscriptionelongationfactorsis recruitment at the HSF1 locus.68 Finally, snf2D cells exhibit
requiredtoassesshowtheLUTIescapemutationsdifferentially increased nucleosome occupancy at promoters and within
impactSwi/Snffunctionintranscriptioninitiationandelongation. gene bodies.19 However, these studies utilize a snf2D null
mutant, which reduces transcription at Swi/Snf target loci. In
Oneofseveraltranscriptionalinterference snf2D cells, it is difficult to distinguish whether differences in
mechanisms:Disruptingpromoterarchitecture nucleosomeoccupancywithinthegenebodyareduetoreduced
Eukaryoticpromotersconsistofanucleosome-freeregion(NFR) transcription vs.lossofSwi/Snfactivityongene-bodynucleo-
orNDRflankedbytwowell-positionednucleosomeswithacet- somes.Here,weprovideconclusiveevidencethattheSwi/Snf
ylatedhistones.58,59AlthoughtheTSSformostgeneslieswithin complexfunctionsinco-transcriptionalnucleosomeremodeling
10–15basepairsofthe50endofthe+1nucleosome,theNFR/ byuncoveringspecificmutantsthatimpairnucleosomeremod-
NDRisthoughttoallowaccessforsequence-specificTFsand eling within gene bodies. Although overall transcript levels are
thepre-initiationcomplextostarttranscriptionatthegenepro- not impaired for most Swi/Snf targets in the swi3-E815X and
moter.18,60,61 In the case of LUTIs and other transcripts with snf2-W935R mutants, we cannot eliminate the possibility that
distal TSSs relative to the CDS-proximal TSS (TSSPROX), tran- these mutations affect transcription elongation rates or RNA
scriptionproceedsacrosstheTSSPROX,subjectingtheproximal PolIIstallingfrequency.Futureworktospecificallyassaytran-
promotertoco-transcriptionalchromatinchangesthatnormally scriptionelongationwouldaidindeterminingwhetherthephe-
functiontopromoteelongationandinhibitcryptictranscription notypesassociatedwithLUTIescapemutantsstemfromaltered
initiation. Several transcriptional interference pathways have transcriptionelongationrates.
already been uncovered, many of which involving histone Previous studies have also uncovered a role for the Swi/Snf
modificationornucleosomeremodeling.28,29,62–64ForSwi/Snf- complexingenerepressioninyeastaswellasmorecomplexor-
repressed TSSPROX loci uncovered in this study, it seems that ganisms.34,49–52 In yeast, the Swi/Snf complex activates tran-
Swi/Snfremodelingofthe(cid:3)1and+1nucleosomessurrounding scription of the non-coding transcript SRG1 in serine replete
the proximal promoter contributes to TSSPROX repression, conditions. SRG1 transcription results in repression of the
possibly by creating increased nucleosome mobility into what SER3 promoter via co-transcriptional nucleosome deposition
waspreviouslytheNFR/NDR. by the Paf1 complex, Spt6, Spt16, and Spt2.33,34,64 In this
Based on our observations that the snf2-Q928K mutant im- case, Swi/Snf-based repression of SER3 is indirect, whereas
pairstranscriptionofthedistalisoform(Figure3F)andthatacti- direct repression at the SER3 promoter is achieved by other
vationofHNT1LUTIissufficientforSnf2recruitment(Figure5C),it elongation factors, exemplifying the complexity and diversity
seemsthatrecruitmentoftheSwi/Snfcomplextothedistalpro- amongtranscriptionalinterferencepathways.
moterisaprerequisiteforthedownstreamtranscriptionalinter-
ference activity by the complex. Recruitment of Swi/Snf may Concludingremarks
be mediated through interactions with acetylated histones or In our search for novel regulators of LUTI-based gene repres-
sequence-specificTFsatdistalpromoters.Withregardstohis- sion, we discovered that the Swi/Snf complex plays a direct
toneacetylation,wefoundthatwhenlackingitsbromodomain, roleintranscriptionalinterference.TheSwi/Snfcomplex,known
Snf2exhibitedreducedoccupancyattheLUTI-regulatedgenes for gene activation, also activates non-canonical mRNAs
ADI1andODC2butnotHNT1duringstress(FigureS4C).Swi/ from CDS-distal promoters under protein folding stress,
SnfoccupancyatseveralcanonicalUPR-inducedpromotersde- includingLUTIs.Additionally,itrepressesTSSPROXvianucleo-
pendsontheHac1TF.20Swi/SnfinteractionwithHac1mayalso some remodeling downstream of the TSSDIST at these loci.
be the basis for its recruitment to HNT1LUTI, a reported Hac1 For the LUTI-regulated gene HNT1, proper Snf2 occupancy,
target.11AnotherprerequisiteforSwi/Snf-dependenttranscrip- nucleosomeremodeling,andHNT1PROXrepressiondependon
tional interference may be shorter distance between the two HNT1LUTI transcription initiation and elongation, indicating co-
TSSs, based on our observation that swi3-E815X and snf2- transcriptionalnucleosomeremodelingbySwi/Snf.
W935Rdonotstronglyaffectnucleosomesfurtherdownstream Our discovery that the Swi/Snf complex can simultaneously
oftheTSS(Figures6CandS6D)andpreviousobservationsthat act as a transcriptional activator and repressor at the same
14 MolecularCell84,1–18,August22,2024
