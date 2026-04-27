---
source_path: /mnt/c/Users/Administrator/Zotero/storage/7LZP6MUC/Gonçalves 等 - 2017 - Widespread Post-transcriptional Attenuation of Genomic Copy-Number Variation in Cancer.pdf
ingested: 2026-04-23
sha256: 8d0c9fc659aea603
---

Article
Widespread Post-transcriptional Attenuation of
Genomic Copy-Number Variation in Cancer
Graphical Abstract Authors
EmanuelGonc¸alves,
AthanassiosFragoulis,
LuzGarcia-Alonso,ThorstenCramer,
JulioSaez-Rodriguez,PedroBeltrao
Correspondence
saezrodriguez@gmail.com(J.S.-R.),
pedrobeltrao@ebi.ac.uk(P.B.)
In Brief
Post-transcriptionalregulation,likelyvia
controlofproteindegradation,can
attenuatecopy-numberalterationsin
tumorsforatleast23%ofmeasured
proteins.Thiseffectisenrichedinprotein
complexes,withsomecomplexmembers
actingasrate-limitingfactorsforcomplex
formation.
Highlights
d 23%–33%oftheproteinshavecopy-numberchanges
attenuated,likelyviadegradation
d Proteincomplexmembersaremoreco-regulatedatprotein
levelthanmRNAlevel
d Systematicidentificationofrate-limitingmembersforthe
assemblyofthecomplex
d AP3B1,GTF2E2,andGTF2E1arelimitingmembersoftheir
complexes
Gonc¸alvesetal.,2017,CellSystems5,386–398
October25,2017ª2017TheAuthors.PublishedbyElsevierInc.
https://doi.org/10.1016/j.cels.2017.08.013
Cell Systems
Article
Widespread Post-transcriptional Attenuation
of Genomic Copy-Number Variation in Cancer
EmanuelGonc¸alves,1AthanassiosFragoulis,3LuzGarcia-Alonso,1ThorstenCramer,3,4,5JulioSaez-Rodriguez,1,2,*
andPedroBeltrao1,6,*
1EuropeanMolecularBiologyLaboratory,EuropeanBioinformaticsInstitute(EMBL-EBI),WellcomeGenomeCampus,Cambridge
CB101SD,UK
2RWTHAachenUniversity,FacultyofMedicine,JointResearchCentreforComputationalBiomedicine,52057Aachen,Germany
3MolecularTumorBiology,DepartmentofGeneral,VisceralandTransplantationSurgery,RWTHUniversityHospital,Pauwelsstraße30,
52074Aachen,Germany
4NUTRIMSchoolofNutritionandTranslationalResearchinMetabolism,MaastrichtUniversity,Maastricht,theNetherlands
5ESCAM–EuropeanSurgeryCenterAachenMaastricht,GermanyandtheNetherlands
6LeadContact
*Correspondence:saezrodriguez@gmail.com(J.S.-R.),pedrobeltrao@ebi.ac.uk(P.B.)
https://doi.org/10.1016/j.cels.2017.08.013
SUMMARY ficationsandotherCNVsarethoughttobedetrimentaldueto
changes in gene expression that cause an imbalance to the
Copy-number variations (CNVs) are ubiquitous in cell.Infemales,oneofthetwoXchromosomesisinactivated
cancerandoftenactasdriverevents,buttheeffects byaspecializedRNA-basedsilencingmechanism(Avnerand
ofCNVsontheproteomeoftumorsarepoorlyunder- Heard, 2001; Lyon, 1961), but such a mechanism does not
stood. Here, we analyze recently published geno- exist for gene-dosage imbalances in the autosomal chro-
mics, transcriptomics, and proteomics datasets mosomes. Protein and mRNA abundance measurements in
models of aneuploidy in yeast and human cells have shown
made available by CPTAC and TCGA consortia on
that most autosomal gene duplications are propagated to
282 breast, ovarian, and colorectal tumor samples
the protein level, with the notable exception of protein com-
to investigate the impact of CNVs in the proteomes
plex subunits that showed attenuated (i.e., less than ex-
of these cells. We found that CNVs are buffered
pected) changes in protein abundance (Dephoure et al.,
by post-transcriptional regulation in 23%–33% of
2014; Stingele et al., 2012). In yeast aneuploid strains, the
proteins that are significantly enriched in protein discrepancy between gene copy-number and protein abun-
complexmembers.Ouranalysesshowthatcomplex dancehasbeenshowntobemostlyduetocontrolofprotein
subunits are highly co-regulated, and some act as abundancebydegradation(Dephoureetal.,2014).Forprotein
rate-limiting steps of complex assembly, as their complexes in particular, this observation fits with a model
depletion induces decreased abundance of other where subunits are degraded when free from the complex
complex members. We identified 48 such rate- (Abovich et al., 1985). Given that not all subunits were
observed to be attenuated, it has been hypothesized that
limiting interactions and experimentally confirmed
these non-attenuated subunits could act as scaffolding pro-
our predictions on the interactions of AP3B1 with
teins orbe rate-limiting forthe assemblyof thecomplex (De-
AP3M1 and GTF2E2 with GTF2E1. This study high-
phoure et al., 2014). In addition, duplicated chromosomes
lightstheimportanceofpost-transcriptionalmecha-
have been shown to cause global stress responses that
nisms in cancer that allow cells to cope with their
include cell-cycle and metabolic defects and proteotoxic
alteredgenomes. stress among others (Tang and Amon, 2013). While somatic
CNVs are known to be drivers of cancer development, and
thataneuploidyisacommonfeatureoftumorcells,theimpact
INTRODUCTION ofgene-dosagechangesontheproteomeofcancercellshas
yettobestudied.Wethereforedecidedtostudytheextentby
Cancer development is driven by the acquisition of somatic which changes in gene copy number are propagated to pro-
genetic variation that includes point mutations, copy-number teinabundance incancerpatient samples,aswell asthe po-
variations (CNVs), and large chromosome rearrangements or tential mechanisms underlying the attenuation of protein
duplications (i.e., aneuploidy) (Beroukhim et al., 2010). These abundance changes.
events can result in a fitness advantage and cancer progres- In this study, we investigated the implications of CNVs
sion, but they are most often detrimental to cellular fitness. on the proteome of tumors by taking advantage of the com-
While somatic gene amplification of key oncogenes such as prehensive datasets made available by The Cancer Genome
MYCN, AKT2, ERBB2, and others (Santarius et al., 2010) Atlas (TCGA) and the Clinical Proteomic Tumor Analysis
can drive cancer development, germline CNVs are rare and Consortium (CPTAC), consortia comprising copy-number,
areundernegativeselection(Itsaraetal., 2009).Gene ampli- transcript, and protein measurements for hundreds of tumors
386 CellSystems5,386–398,October25,2017ª2017TheAuthors.PublishedbyElsevierInc.
ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).
(Cancer Genome Atlas Network, 2012a, 2012b; Cancer tomics, by regressing-out batch effects associated with
Genome Atlas Research Network, 2011; Mertins et al., 2016; experimental technologies used, patient gender and age, and
Zhang et al., 2014, 2016). These data revealed that CNVs are tumor type (see the STAR Methods). The associations be-
often propagated to the protein level, although we observed tween these possible confounding factors and the principal
that post-transcriptional mechanisms attenuate this impact in components were completely removed after correction (Fig-
23%–33% of the measured proteins. Protein complexes ures S1 and S2).
were notably attenuated and showed strong protein abun- Havingassembledthiscompendiumofdatasetswethenset
danceco-regulationacrosssamples.Notallcomplexsubunits outtounderstandtheimplicationofCNVeventsintheexpres-
are attenuated, with some acting as potential rate-limiting sion of the proteome (Figure 1C). For each gene/protein we
factorsforcomplexassembly.Hereweidentified48regulatory calculated, across all samples, the agreement between the
interactionswherebytheabundanceofoneofthesubunitscan CNVsandtranscriptomicsandtheCNVsandproteomicsusing
modulate the abundance of other complex members. We thePearsoncorrelationcoefficient(Figure1D).Transcriptabun-
experimentally assessed the role of AP3B1 and GTF2E2 as dance is, on average, well correlated with gene CNV changes
potential rate-limiting subunits through knockdown experi- (medianPearson’sr=0.43),andthiscontrastswiththesignifi-
ments. In addition, ranking the samples by their potential to cantdecrease(Welch’sttestpvalue<1310(cid:1)4)ofagreement
attenuategene-dosageeffectsidentifiedputativemechanisms of CNVs with protein abundance (median Pearson’s r = 0.20)
involved in autosomal gene-dosage compensation. Finally, a (Figure1D;TableS2).Wehypothesizethat,astranscriptionisin-
gene expression signature of attenuation potential was found termediate between the copy-number alterations and protein
tobeassociatedwithdrugstargetingchaperones,theprotea- abundance,itsetsthemaximumpossibleagreementbetween
some,andtheE3ligasemurinedoubleminute2(MDM2).Us- both. Then, using a Gaussian mixture model, we defined as
ing 282 tumor samples we revealed the widespread impor- attenuatedproteinsthosethathavealoweragreementbetween
tance of post-transcriptional mechanisms to ameliorate the CNVs and protein abundance than expected by their CNV to
impact of CNVs in cancer cells. gene expression correlation (see the STAR Methods). In these
sampleswefoundthat,bythisdefinition1,496–2,119proteins
RESULTS are significantly attenuated, corresponding to 23%–33% of all
genes with available measurements (6,418). This result shows
TumorPan-cancerProteomicsRevealsAttenuationof that a significant fraction of the proteome undergoes gene-
Copy-NumberAlterationsinProteinComplexSubunits dosagebalancing.Inaddition,thisgroupofattenuatedproteins
To study the implication of gene-dosage changes on the highlightsthecomplexityoftheregulationofproteinabundance,
proteomeofcancercellswecompiledandstandardizedexist- hintingatconstraintsthatcontrolproteintranslationordegrada-
ingdatasetsmadeavailablebytheTCGAandCPTACconsor- tionrates.
tia, comprising three different cancer types: breast (BRCA) To understand the biological processesthat areaffected by
(Cancer Genome Atlas Network, 2012b; Mertins et al., 2016), thisattenuationweperformedanunbiasedenrichmentanalysis
high-grade serous ovarian (HGSC) (Cancer Genome Atlas usinggeneontologyterms(Ashburneretal.,2000;Subramanian
Research Network, 2011; Zhang et al., 2016), and colon and etal.,2005;TheGeneOntologyConsortium,2015)(Figure2A)
rectal (COREAD) (Cancer Genome Atlas Network, 2012a; (see the STAR Methods). The enrichment analysis revealed
Zhang et al., 2016) (Figure 1A). These datasets provide mole- thatproteinsinvolvedincomplexesandmodulesoffunctionally
cular characterization of gene CNVs, gene expression, and interacting proteins displayed a significant agreement withthe
protein abundance of solid tumor samples of 282 patients copy-number measurements at the transcript level, but this
for which clinical information is also available (Figure 1A, agreementisgenerallylostattheproteinlevel(Figure2B).This
Table S1). recapitulatespreviousfindingsinmodelsofaneuploidyinyeast
Current methods can reliably measure the complete ex- (Dephoure et al., 2014) and human cell lines (Stingele et al.,
pressed transcriptome, but measuring the total proteome is 2012), showing that these observations generalize from the
still a challenge with current techniques only providing partial aneuploidy models to the hundreds of patient tumor samples
snapshots(Nagarajetal.,2011).Thus,wequantifiedthefrac- studiedhere.Tovalidatethegeneralityofthesetofattenuated
tion of expressed transcripts measured in the proteomics ex- proteins,weconfirmedthatthesearealsorecapitulatedininde-
periments in each tumor sample (Figure 1B) (see the STAR pendentproteomiccelllinepanelsoftriple-negativebreastcan-
Methods). COREAD samples displayed the lowest average cer and ovarian cancer (Coscia et al., 2016; Lawrence et al.,
coverage of the expressed transcriptome (22.3%) compared 2015)(Figure2C).Totestifdegradationplaysaroleintheatten-
with the coverage measured for the HGSC (42.0%) and uationobservedinhumancells,weusedpubliclyavailabledata
BRCA (56.1%) samples. The proteomics experiments were onchangesinproteinubiquitinationafterproteasomeinhibition
not conducted using the same methodologies, and therefore asmarkersofdegradation(Kimetal.,2011).Weobservedthat
itiscrucialtotakeintoconsiderationpotentialconfoundingef- proteins defined as attenuated in our study show a faster
fects. In particular, the COREAD (Zhang et al., 2014) quantifi- increaseinubiquitinationafterproteasomeinhibitionthanother
cations were done with a label-free approach, while the proteins (Figure 2D), suggesting that degradation plays a key
HGSC and BRCA were quantified using isobaric labeling roleintheattenuation.Theseresultssuggestthattheabundance
(Mertinsetal.,2016;Zhangetal.,2016).Toensurecompara- ofproteinsubunitsoflargestableproteincomplexesareunder
ble measurements among datasets we removed confounding activecontroltomaintaintheirco-regulation,possiblytoguar-
and systematic effects from the proteomics and transcrip- anteethestabilityandformationoftheassociationsorprevent
CellSystems5,386–398,October25,2017 387
Figure1. Pan-cancerEffectsofCopy-NumberVariationonTranscriptandProteinAbundances
(A)Overviewofthenumberofsamplesusedinthisstudyoverlappingwiththeproteomicsmeasurementsforeachtumortype.
(B)Proteomicscoverageoftheexpressedtranscriptsineachsampleandforeachtumortype.
(C)Diagramdepictingtheimplicationofcopy-numberalterationsalongthecentraldogmaofbiology.
(D)Eachdotinthescatterplotrepresentsatranscript/protein.ThexaxisrepresentsthePearsoncorrelationcoefficientbetweencopy-numbervariationand
transcriptomics,andtheyaxisthePearsoncorrelationbetweencopy-numbervariationandproteomics.AGaussianmixturemodelwithtwomixturecomponents
wasusedtoidentifyproteinswithhighattenuationlevels(coloredinred).
the accumulation of free subunits that might be prone to tumor types (see the STAR Methods). Consistently, proteins
aggregate. withinthesamecomplexesdisplaycoordinatedchangesofabun-
danceacrosssamples(Figure3A).Then,weassessedifthisco-
ProteomicCorrelationAnalysisUncoversStrongCo- regulationeffectisubiquitousinacuratedsetofhumanprotein
regulationofProteinComplexes complexesfromtheCORUMdatabase(Rueppetal.,2010).Pairs
Totestthehypothesisthattheattenuationofmembersservesto ofproteinspresenttogetherinacomplexdisplayadegreeofco-
tune the stoichiometry of all complex members, we performed regulation (meanPearson’s r = 0.25) that is significantlyhigher
protein-protein correlation analysis using the proteomics mea- thanthatobservedforrandompairs(meanPearson’sr=0).We
surements and compared this with gene expression-based also assessed if this co-regulation was visible at the transcript
correlations (Figure 3A). We performed all possible pairwise level,and,whilethereisasignificantincreaseoverrandomasso-
correlation of protein abundance for all the 6,434 proteins ciations(meanPearson’sr=0.15),thiscorrelationissignificantly
measuredinatleast50%ofthesamplesacrossthethreedifferent lowerthantheoneseenattheproteinlevel(Figure3B).Protein
388 CellSystems5,386–398,October25,2017
Figure2. EnrichmentAnalysisoftheProteinsUndergoingCopy-NumberAttenuation
(A)Enrichmentanalysisofthecorrelationdifferencesbetweencopy-numbervariationandtranscriptomicsandcopy-numbervariationandproteomics.Protein
subsetsusedrepresentbiologicalprocesses(BP,green),cellularcomponents(CC,red),andpost-translationalmodifications(PTM,blue).Genesetslistedareall
significantlyenrichedatFDR<5%.
(B)Thedistributionoftheenrichmentscoresfortermsreferringtoproteincomplexesorsubunitsarerepresentedinredandalltherestingray.
(C)Proteinsclassifiedaccordingtotheirattenuationprofileintumorsaremappedagainsttheirattenuationinbreastandovariancancercelllines.
(D)Ubiquitinationsitefoldchangesovertimeafterproteasomeinhibitionwithbortezomibdiscretizedaccordingtheproteinattenuationlevelintumors.
pairsthathavefunctionalinteractionsbutarenotcomplexsub- betteragreementattheproteinthanatthetranscriptlevel(Wang
unitsshowalowerdegreeofabundancecorrelation(meanPear- etal.,2016).Wenoticedthatproteininteractionsderivedfrom
son’sr=0.15)thatisalsoclosertotheobservedatthetranscript signaling networks displayed in general poor agreement at
level(meanPearson’sr=0.11)(Figure3B). the protein and transcript abundance levels (AROC = 0.55
Inlightofthisagreementbetweenfunctionallyrelatedproteins and0.54)(Figure3C),suggestingthattheabundanceofsignaling
weexaminedthecapacityofprotein-proteincorrelationprofiles proteinsinthesamepathwaydoesnotnecessarilyneedtobe
to predict different types of protein-protein interactions coordinated. Furthermore, metabolic enzymes involved in the
(Figure3C)(seetheSTARMethods).Wefoundthatdirectand samemetabolicpathwaysdisplayedsomedegreeofagreement
indirectfunctionalinteractionscouldbewellidentifiedwithpro- at the protein and transcript level (AROC = 0.65 and 0.62)
teomics (area under the receiving operating characteristic (Figure3C).
curves AROC = 0.86 and 0.75, respectively), and worse with Our resultsshown thatproteincomplex subunits oftenhave
transcriptomics(AROC=0.69and0.67,respectively)(Figure3C). copy-number changes that are attenuated at the protein level
This finding goes in line with a recent work that showed that andthatneverthelessalsoshowhigherco-regulationofprotein
proteinswithinsimilarbiologicalprocessesorpathwaysdisplay abundancethanobservedatmRNAlevel.
CellSystems5,386–398,October25,2017 389
Figure3. Copy-NumberVariationAttenuationforProteinComplexSubunitsResultsinStrongCo-regulationofTheirAbundancesacross
Samples
(A)Protein-proteincorrelationmatrixusingPearsoncorrelationcoefficientandtworepresentativecasesoftopcorrelatedproteincomplexes.
(B)Distributionofallprotein-proteincorrelationsattheproteinlevel(proteomics)andtranscriptlevel(transcriptomics).Proteininteractionswithincomplexesare
representedbythecomplexlabel,andproteinfunctionalinteractions,whicharenotnecessarilydirect,arerepresentedbythefunctionallabel.
(C)Enrichmentanalysisbythemeansoftheareaunderthereceivingoperatingcharacteristiccurves(AROC)usingpairwisecorrelationcoefficients,forboth
proteomicsandtranscriptomicsmeasurements.Errorbarsdisplaythevariabilityobtainedwithfiverandomizedtruenegativesets.
ProteogenomicsAnalysisIdentifiesSubunitsthat protein abundance variation of the paired protein (Py) (Fig-
ControltheProteinAbundanceLevelsofOther ure 4A) (see the STAR Methods). To consider the differences
MembersoftheComplex indegradationortranslationratesoftheprotein,thetranscript
It has been hypothesized that non-attenuated subunits could measurementswereregressed-outfromtheproteinabundance
act as scaffolding proteins or rate-limiting for the assembly of measurements (Figure 4A) (see the STAR Methods). This
the complex (Dephoure et al., 2014). However, past studies allowedustoconsiderthevariabilityarisingpost-transcription-
based on aneuploidy models were conducted on a small ally and, importantly, to discard possible confounding effects
number of yeast strains or cell lines (Dephoure et al., 2014; occurring at the genomic and transcript level, such as close
Stingeleetal.,2012).Giventhelargenumberoftumorsamples genomic localization. Out of the 58,627 possible directed pro-
analyzedherewereasonedthatwecouldmorereadilyidentify tein interactions, 64 were found to be significantly associated
suchsubunitsthatcanactasdriversofcomplexassembly.To (false-discovery rate FDR <5%) (Figure 4A; Table S3) (see the
study this we assessed if the CNVs of a given gene product STAR Methods). To ensure that the association was not only
within a protein complex could explain the changes in abun- visible at the genomic but also at the transcript level, the
dance of other subunits once we discount their transcriptional same associations were performed using transcriptomics
changes (see the STAR Methods). In other words, if the pres- measurements. As expected since that transcript abundance
ence or absence of certain proteins of the complex could be is a closer measurement to the protein abundance, we found
associatedwiththeproteindegradationrateofothermembers. a substantial increase of significant associations, 2,846
This was performed systematically for all identifiable protein (FDR<5%)(FigureS3;TableS3).Also,75%(48)oftheassoci-
pairs within protein complexes using linear regression models ations foundat the genomic levelwere foundto besignificant
where the CNVs of a protein (Px) was used to estimate the atthetranscript level(Figure4A;TableS3).
390 CellSystems5,386–398,October25,2017
Figure4. ProteinComplexRegulators
(A)Volcanoplotdisplayingtheeffectsizeandadjustedpvalueofallthetestedregulatoryinteractions.Associationswereperformedusingthecopy-number
variation of the putative regulatory protein, Px, and the protein residuals of the regulated protein, Py. Significant associations found with the transcript
measurementsofPxaredenotedwitharedborder.
(B)Representativesignificantassociations.Boxplotsshowtheagreementbetweenthecopy-numbervariationofPxandtheresidualsoftheregulatedPy.
Scatterplotshowtheagreementbetweentheproteinpairsintheproteomicsmeasurements.
Giventhattheassociationsaremadebetweenthecopylevel associatedwithCOG2(Figure4).Additionalpositiveregulatory
ofonegeneandtheresidualabundanceoftheinteractorpartner interactionswerefoundforsubunitsoftheeukaryoticinitiation
theyareexpectedtobecausalrelationships.Itisunlikelythatthe factor 3 (EIF3), transcription factor IIH, adaptor-related protein
residual abundance of a protein would cause a change in the complex3(AP3),amongothers(TableS3),providingwithinfor-
DNAcopynumberoftheinteractingpartner.Therefore,thisanal- mationontheputativeassemblypathwaysofthesecomplexes.
ysisidentifiedinteractionsthatmayactasrate-limitingstepsof The number of significant negative associations was lower
theassemblyofproteincomplexes.Wefound,forexample,an thanthenumberofpositiveassociations(Figures4AandS3C).
associationbetweenthecopynumberofCOG3andtheprotein SMARCA2copy-numberalterationsweresignificantlyandnega-
variability of COG2 (Pearson’s r = 0.39, p value 9.90 3 1012) tivelyassociatedwiththedegradationofSMARCA4(Figure4A)
(Figure 4B). COG3 is also significantly associated with COG4 andthiswasalsovisibleattheproteinlevel(Figure4B).Negative
(Figure 4B), increasing the possibility that COG3 is a regulator associations are likely to represent mutually exclusive events
oftheassemblyoftheconservedoligomericGolgi(COG)com- withinproteincomplexes,thuswhenoneproteinispresentthe
plex.Thesefindingsarecorroboratedbyanexistingstudywhere otherwillnotbenecessaryforthecomplexformationandmay
COG3 knockdown leads to a decreased abundance of COG2 undergodegradation.Indeed,currentevidenceintheliterature
andCOG4(BaileyBlackburnetal.,2016;ZolovandLupashin, suggestthatSMARCA2andSMARCA4areparalogsandmutu-
2005).Besidesidentifyingknownrate-limitingmembersofcom- allyexclusivewithintheSWI/SNFcomplex(Karnezisetal.,2016;
plexes, our analysis also predicts two possibly novel associa- Orietal.,2016).Thelowernumberofnegativeassociationssug-
tions within the COG complex, with COG6 being significantly geststhatthesetypesofeventsarelessfrequent.
CellSystems5,386–398,October25,2017 391
(legendonnextpage)
392 CellSystems5,386–398,October25,2017
AP3B1andGTF2E2ProteinAbundanceLevelsIndirectly eachtumorsample.Wereasonedthat,bystratifyingthesamples
ControltheAbundanceofInteractionPartners bytheircapacitytoattenuatetheCNVchanges,wecouldiden-
Weexperimentally validated twoof the top significant positive tifytheunderlyingattenuationmechanisms.Similarlytothepro-
associations(Figure5).Thesewerefoundwithinproteincomplex tein analysis (Figure 1D), we performed a correlation analysis
subunits of the AP3 and the transcription initiation factor IIE between the CNVs and transcriptomics and proteomics for
(TFIIE),AP3B1-AP3M1,andGTF2E2-GTF2E1,respectively(Fig- eachsample(Figure7A),insteadofeachprotein.Furthermore,
ures5Aand5C).Toassesstheirimplicationweperformedsmall recurringtoaGaussianmixturemodelweclassified50samples
hairpin RNA (shRNA) knockdown of the putative rate-limiting (18%)asthosehavingageneralstrongattenuationeffect(see
proteins,AP3B1andGTF2E2,inshRNAtransfectedHCT116hu- theSTARMethods).Suchtumorsampleshaveahighernumber
mancoloncancercelllinesfollowedbywesternblot.Knocking of genes with strong attenuation, suggesting either an overall
down AP3B1 and GTF2E2 not only affected their abundance increaseindegradationordecreaseintranslationratesinthese
butalsotheabundanceoftheinteractingproteinswithinthepro- samples.Toattempttounderstandtheunderlyingdifferencesin
teincomplexsubunit,AP3M1andGTF2E1(Figures5Band5D). attenuation potential we first correlated this metric with the
Whilefortheputativerate-limitinginteractionstheinverseasso- degree of somatic copy-number alterations from Davoli et al.
ciationwasnotfoundsignificant(FDR>5%),wecannotexclude (2017)andobservedasignificantcorrelation(r=0.33,pvalue=
thattheymightexistaswearelimitedbythecoverageoftheda- 1.2310(cid:1)7).Thiswouldsuggestthatinpartthehigherapparent
tasets.Forexample,thelackofvariabilityatthecopy-number attenuationpotentialisduetolargercopy-numberalterations.It
levelmightleadtouninformativeassociationsofthegeneprod- alsoindirectlysuggeststhatthereisnotaverystrongsaturation
uctwiththeothermembersofthecomplex.Toaddressthis,we wherebylargernumbersofgene-dosagealterationswouldresult
also performed the reverse experiment by knocking down inlowerattenuationcapacity.Wedidnotfindasignificantasso-
AP3M1 and GTF2E1 and measured the impact in protein ciationbetweenattenuationpotentialandsampleploidyorsam-
abundance. We observed that AP3M1 knockdown did not ple purity (r = 0.031 and (cid:1)0.11, respectively, Figures S4B
haveanyimpactintheabundanceofAP3B1(Figure5B)asex- and S4C). We then searched for complexes and complex
pectedbythelowassociationcoefficientofthelinearmodel(Fig- subunitsthataremorelikelytobeamplifiedordeletedinthetu-
ure5A).Ontheotherhand,GTF2E1knockdownresultedinthe morswithstrongerattenuationandcouldthereforecontributeto
depletionofGTF2E2(Figure5D)suggestingthatthisrate-limiting theattenuationpotential(seetheSTARMethods).Tumorswith
interaction is bidirectional. The lack of any strong depletion of strong attenuation effects displayed a significant enrichment
GTF2E1inthecopy-numberdatasetmayexplainwhythisasso- of gene amplifications in several complex subunits, including
ciationcannotbecapturedonthisdirection(Figure5C). genesinvolvedintheendoplasmicreticulum-associateddegra-
To further assess if our associations were capable of dation(ERAD)pathway(DERL1andVIMP),cellpolarity(SCRIB,
identifyingtherate-limitinginteractionsoccurringinbothdirec- LLGL2, and VANGL2), GPI-anchor biosynthesis (PIGT and
tions we used two independent studies where members of PIGU), and RNAi (AGO2) (Figures 7B and 7C). We also found
COGandEIF3weresystematicallyknockeddownwithshRNAs, significantenrichmentfordeletionsinGTF2E2involvedintran-
andtheabundanceofthecomplexmemberswasmeasuredwith scriptionregulationcomplexTFIIE.
westernblot(BaileyBlackburnetal.,2016;Wagneretal.,2014).
Wefoundasignificant(Spearman’sr=(cid:1)0.4,pvalue3.4310(cid:1)4) GeneExpressionProfileofProteinAttenuationIs
agreementbetweenourpredictedassociationeffectandthose AssociatedwithSpecificDrugResponses
measured experimentally (Figure 6A). Moreover, all the signifi- SincethetumorswithstrongattenuationoftheeffectsofCNVs
cant associations captured within these complexes showed displayedparticularcharacteristics,wedefinedageneexpres-
significantlyhigherimpactonabundance(Figure6B).Thishigh- sionsignaturebysystematicallycorrelatingeachgenewiththe
lighted that our approach is able to capture well rate-limiting attenuation potential (see the STAR Methods). We then per-
associationswithstrongeffectsandcanidentifywithmoderate formed gene set enrichment analysis on this gene expression
confidenceiftheassociationoccursinbothdirections. signature (Figures S4E and S4F) and we found that samples
withhigherattenuationpotentialhaveincreasedexpressionsof
MolecularFeaturesAssociatedwithHighAttenuation cell-cycle-related functions (e.g., meiotic recombination, sister
Potential chromatidsegregation,G1phaseofthemitoticcellcycle),and
Having assessed the attenuation of the effects of CNVs in the decreased expression of metabolic-related function (e.g.,
proteomewesetouttoquantifytheextentofthisregulationin phagocytosis, respiratory chain complex I, and glucosamine
Figure5. ExperimentalValidationofRegulatoryInteractionsamongProteinComplexSubunits
Rate-limitinginteractionswithintheadaptorproteincomplex3(AP3)andthetranscriptioninitiationfactorIIE(TFIIE)complexes.
(AandC)Correlationofthecopy-numberprofileoftheregulatoryproteinwiththeproteinresidualsoftheregulatedprotein(leftplot)andagreementattheprotein
levelbetweenthetwoproteins(rightplot).
(BandD)shRNAknockdownoftheregulatoryproteins,AP3B1andGTF2E2,showstrongdecreaseintheproteinabundanceoftheregulatedproteins,AP3M1
andGTF2E1,respectively.KnockingdownGTF2E1showedasignificantdownregulationofGTF2E2,indicatingabidirectionalrelationbetweenthoseproteins.In
contrast,AP3M1shRNAdidnotaffectAP3B1proteinabundance.Proteinabundancechangesaremeasuredandquantifiedbywesternblotusingantibodies
specificforthecorrespondingproteins.ThequantifiedbandsintheshAP3B1,shAP3M1,shGTF2E2,andshGTF2E1experimentswerescoredrelativetothe
controlshRNA(shNT).GAPDHwasusedasaloadingcontrol.
ErrorbarsshownaretheSDfromthemean(n=3independentexperiments).*p<0.05comparedwithshNT,two-tailedunpairedttest.
CellSystems5,386–398,October25,2017 393
Figure6. COG3andEIF3ComplexesRate-
LimitingInteractions
(A)Agreementbetweenexperimentallymeasured
COGandEIF3complexelementknockdownwith
insilicoestimatedimpact.
(B) Welch’s t test comparing the computational
rate-limiting interactions (FDR <5%) and all the
otherexperimentallymeasuredinteractions.
profile (Pearson’s r = 0.20 and 0.16,
respectively). Both compounds target
the oncoprotein E3 ligase MDM2 which,
in p53wild-typetumors,suppresses the
activity of p53 by ubiquitination and
thereby is a potential therapeutic target
(ShangaryandWang,2008).Theprotein
attenuation potential predicted for the
celllinesalsodisplayedtissuespecificity,
supportingtheideathatproteasomalca-
pacity is constrained by the tissue of
metabolic process). Among the downregulated functions are origin.Thisanalysissuggeststhatthegeneexpressionsignature
alsosomerelatedtoimmuneresponse(e.g.,cytokinesecretion for the proteome attenuation may be associated with an
andcellulardefenseresponse).Thisisconsistentwiththeobser- increasedcapacityoftheproteinqualitycontrolmachineryand
vation that samples with higher somatic copy-number alter- anincreasedresistancetodrugsthattargetthissystem.
ationshavedownregulationofimmune-relatedgenesets(Davoli
etal.,2017).However,whileourmeasureofattenuationpotential DISCUSSION
persampleiscorrelatedwithtotalSCNAsscores,itisnotcorre-
latedwithsamplepurity(r=(cid:1)0.11,pvalue=8.5310(cid:1)2),indi- Gene-DosageChangesAreAttenuatedfor23%–33%of
cating that there is no strong difference of immune infiltration Proteins
acrosssamplesofdifferentattenuationpotential.Thesechanges We aimed here to study the extent by which gene dosage is
in gene expression are more likely reflective of the degree of attenuatedincancerattheproteinlevelandwhatarethemech-
copy-numberalterationsandmaynotbeimmediatelyinforma- anismsthatgovernthisprocess.Weobservedthat,whileCNVs
tive to understand the mechanisms underlying the differences have on average a good agreement with transcript measure-
in attenuation potential. We observed that this signature is ments, 23%–33% of the proteins undergo post-transcriptional
capable of discriminating samples with strong versus weak regulation, which attenuates the impact of CNVs (Figures 1C
attenuation using a cross-validation approach (Figure S4A; and 1D). We cannot rule out the possibility that some of the
AROC=0.69).Thissignatureprovidesaputativerankingofthe apparent protein level attenuation may be due to higher mea-
agreementbetweengeneexpressionandtheattenuationprofile surement error in the protein abundance relative to the gene
ofthesamples.Next,weexploredthecapacityofthissignature expression measurements. However, this is not expected to
to identify particular cellular states that can be informative for altertherankingofproteinsfromstrongesttoweakestattenua-
drugresponse.Sampleswithastrongcorrelationwiththesigna- tionasshownbythereplicationwiththecelllinedata(Figure2C).
turewouldbepredictedtohavehigherattenuationandcould,for Theidentificationofattenuatedproteinsaloneisveryrelevantfor
example, display a higher proteasomal capacity. Thus, we the identification of causal genes within amplified genome re-
considered an independent cell line panel for which gene gions. Since copy-number changes are buffered and not
expressionanddrugresponseisavailable(Iorioetal.,2016b), observed at the protein level, these are therefore less likely to
and ranked the cell lines according to their predicted protein be drivers of cancer progression and similarly less likely to
attenuation potential (see the STAR Methods). Then we as- explainchangesindrugassociations.Notably,thisattenuation
sessedtheassociationbetweenthispredictedattenuationpo- was more pronounced in protein subunits and complexes, in
tential and drug-response measurements for 265 compounds agreement with previous observations (Dephoure et al., 2014;
(seetheSTARMethods)(Figures7DandS4D).Amongthetop Stingele et al., 2012). This is likely explained by the fact that
predicted compounds are a proteasome (Bortezomib and the stoichiometry of complexes needs to be preserved, and
MG-132) and chaperone inhibitors (AUY922, 17-AAG, Elesclo- that proteins over-represented compared with other members
mol,CCT018159,andSNX-2112),whichdisplayedasignificant ofthecomplexarelikelydegradedduetoincreasedinstability
(FDR <5%) positive association, suggesting that a stronger (McShaneetal.,2016).Furthermore,weobservedthatproteins
predicted attenuation potential is associated with increased with stronger attenuation are more quickly ubiquitinated (Kim
resistancetoproteasome/chaperoneinhibitors(TableS4).This et al., 2011) (Figure 2D), suggesting that the attenuation may
unbiasedsearchalsorevealedsignificantlypositiveassociations bemostlydrivenbychangesindegradationinsteadoftransla-
of Nutlin-3a and JNJ-26854165 and the proteome attenuation tion rates. In line with this, it has been shown, in time-series
394 CellSystems5,386–398,October25,2017
Figure7. PutativeMechanismsforTumorAttenuationPotentialandTheirAssociationwithChaperone/ProteasomeDrugResistance
(A)Tumorsamplecorrelationsofthecopy-numberchangesandthetranscript(xaxis)andprotein(yaxis)measurements.Samplesclassifiedwithhighattenuation
potential,inred,displaystrongerattenuationofthecopy-numbervariation.
(B)Proteincomplexessignificantlyenrichedforgeneamplifications(FDR<5%)onthesampleswithhighproteinattenuation.
(C)Topstronglyamplifiedgeneswithinthesignificantlyenrichedcomplexes.
(D)Drug-responseassociationsperformedinalargecelllinepanelusingthecelllinesusingputativeattenuationpotentialasthepredictivefeature.Significant
associations(FDR<5%)ofchaperoneandproteasomeinhibitorsarelabeledandmarkedinred.Boxplotsrepresentingthedistributionsofthedrugassociations
effectsizesofalltheproteasomeandchaperonesinhibitorsinthedrugpanel.
experiments,thatmanyproteincomplexsubunitshavedegrada- knockingdownRPA2orEIF3Aprovedtobelethalforthetrans-
tion profiles that arebest fit bya two-state model, suggesting fectedHCT116coloncancercelllines.Potentialmutualexclusiv-
thatthedegradationrateoftheseproteinschanges,presumably ityassociationswerepresentinmuchlowernumbers.Themost
whenfreeorwhenassembledintothecomplex(McShaneetal., compelling negative association was SMARCA2-SMARCA4,
2016).Attenuationofabnormalgenecopynumbersbyprotein whichwassupportedbycurrentliteraturewherethetwoarere-
degradationseemstobeageneralandconservedeffectinaneu- portedtobemutuallyexclusiveATPases(Karnezisetal.,2016)
ploidycells,asalsoshowninMcShaneetal.(2016).Wenotethat andparalogs(Orietal.,2016)withintheSWI/SNFcomplex.
wecannotruleoutthatcontroloftranslationratemightalsoplay Identification of trans-regulatory effects is still a challenging
animportantroletobuffercopy-numberalterations. taskanditisestimatedtorepresent70%ofmRNAheritability
(Priceetal.,2011).Theseresultsprovideexamplesandputative
SomeProteinsCanIndirectlyControltheAbundanceof mechanistic explanations for how variation in copy number or
InteractionPartners gene expression of a protein can have trans effects in the
Weidentified48putativerate-limitingproteinsforcomplexas- abundanceofinteractingproteins,asseeninproteinquantitative
sembly,capableofregulatingtheabundanceofothercomplex traitlocianalyses(Battleetal.,2015;Chicketal.,2016).Identifi-
subunits(Figure4A).Theseresultssuggestthatproteininterac- cationofrate-limitinginteractionsinproteincomplexassembly
tionsandcomplexassemblyareimportantcontrolpointsforpro- willhelpunderstandhowprotein-proteininteractionsarestruc-
teinlevelgene-dosagecompensation.Thissystematicanalysis turedandwillbeimportanttounderstandcomplextraits(Boyle
recapitulated previously known rate-limiting interactions in etal.,2017).
COGandEIF3,anditalsofoundpotentiallynovelassociations.
Ofthese,wehaveexperimentallyvalidatedtworate-limitingin- AssociationAnalysisSuggestsMechanismsAssociated
teractions, AP3B1-AP3M1 and GTF2E2-GTF2E1, within the withGene-DosageAttenuation
AP3andTFIIEcomplexes,respectively(Figure5).TheAP3B1- TumorsampleswithstrongattenuationoftheeffectsofCNVsin
AP3M1 interaction was not bidirectional in contrast to the proteinabundancedisplayedasignificantenrichmentforampli-
GTF2E2-GTF2E1. This latter case is of particular importance ficationsofseveralproteincomplexesinvolvedintheresponse
as it illustrates a case where we did not predict but observed to misfolded proteins in the endoplasmic reticulum (ER), cell
an indirect effect on abundance of an interacting protein. The polarity, trafficking, and gene repression. Consistent with the
absenceofapredictedindirecteffectcouldbeduetolackofsta- increased protein attenuation profile of these tumors, we
tisticalpower,forexamplealimitednumberofstrongdepletions observe amplifications of the ERAD components, DERL1 and
and amplifications of a given gene. We also designed experi- VIMP,whicharepartofanERcomplexthatisresponsible for
mental validations for RPA2-RPA3 and for EIF3A-EIF3E, but the retrotranslocation of misfolded proteins to the cytosol for
CellSystems5,386–398,October25,2017 395
proteasomal degradation (Lilley and Ploegh, 2004; Ye et al., d QUANTIFICATIONANDSTATISTICALANALYSIS
2004). While this association is expected, the others are less B DataCompendium
obviously linked to post-transcriptional control. The cell polar- B DataProcessingandNormalisation
ity-related SCRIB protein complexes have been previously re- B ProteomeAttenuationAnalysis
portedtoplayanimportantroleincancerprogressioninbreast B PairwiseCorrelationAnalysis
cancer,andtheirinhibitionhasbeenlinkedtoadecreaseincell B ProteogenomicsAnalysistoIdentifyProteinComplex
migration (Anastas et al., 2012). The proteasome system is Regulators
importantfortheregulationoffocaladhesionsinmigratingcells B LogisticClassificationofSamplesProteinAttenuation
(TeckchandaniandCooper,2016),andinhibitionoftheprotea- Potential
some inhibits migration and invasion in breast cancer cells B StatisticalAnalysisofExperimentalData
(Xieetal.,2009).However,itisnotclearhowtheoverexpression B CodeAvailability
of these cell polarity factors would result in an increase in
attenuation potential. The association between increased SUPPLEMENTALINFORMATION
attenuation and amplification of AGO2 could be explained by
SupplementalInformationincludesfourfiguresandfourtablesandcanbe
itsroleinrepressingtheinitiationofmRNAtranslation(Kiriakidou
foundwiththisarticleonlineathttps://doi.org/10.1016/j.cels.2017.08.013.
etal.,2007).
AUTHORCONTRIBUTIONS
DifferentialDrug-ResponseAssociationwithGene
ExpressionSignatureofProteomeAttenuation J.S.R.andP.B.conceivedandledthestudy.E.G.carriedouttheanalysis.A.F.
andT.C.designedtheexperimentalvalidations.A.F.carriedoutcellcultures
Incelllines,proteomeattenuation,predictedbyageneexpres-
and knocking down experiments. L.G.A. contributed to the analysis. E.G.,
sion signature, was associated with increased resistance to
J.S.R.,andP.B.wrotethepaper.
proteasome and chaperone inhibitors (Figure 7D), suggesting
that tumors, where attenuation is more pronounced, are more ACKNOWLEDGMENTS
resistant to perturbations in the chaperone/proteasome sys-
tem. The two compounds in the screen targeting MDM2 were WethankMichaelSchubertforhelpintegratingthecopy-numbervariation
data and Paolo Casale for helping define the linear models. We gratefully
amongthetopassociatedwiththegeneexpressionsignature,
acknowledgehelpfulcommentsfromColmRyan,MarcBrehme,DavidOchoa,
suggesting that tumors with high predicted attenuation poten-
DanishMemon,RomainStuder,HarunaImamura,andTheodorosRoumelio-
tial may have a high proteasome capacity and therefore be
tis.WethankJessicaBaileyandVladimirLupashinforkindlyprovidingexper-
lesssensitivetotheinhibitionofMDM2,whichistheE3ligase imentalmeasurementsontheCOGknockdownexperiment.
responsible for the degradation of TP53 in p53 wild-type
tumors (Shangary and Wang, 2008). While we show that the Received:February1,2017
geneexpressionsignaturehassomepowertopredictattenua- Revised:June21,2017
Accepted:August23,2017
tion potential in cross-validation tests, additional work will be
Published:October11,2017
required to conclusively validate the putative associations be-
tween the attenuation potential and the drug responses. The REFERENCES
increasingavailabilityofproteomicsstudiesincancercelllines
will enable the estimation of protein attenuation directly and Abovich,N.,Gritz,L.,Tung,L.,andRosbash,M.(1985).EffectofRP51gene
without the need to rely on an attenuation potential gene dosage alterations on ribosome synthesis in Saccharomyces cerevisiae.
Mol.Cell.Biol.5,3429–3435.
expression signature defined in tumor samples. This will
Anastas,J.N.,Biechele,T.L.,Robitaille,M.,Muster,J.,Allison,K.H.,Angers,
augment our power to study gene-dosage compensation and
S., and Moon, R.T. (2012). A protein complex of SCRIB, NOS1AP and
its effect ondrugresponse.
VANGL1regulatescellpolarityandmigration,andisassociatedwithbreast
In this study, we provide insights into how cancer cells
cancerprogression.Oncogene31,3696–3708.
manage to cope with often dramatic chromosomal rearrange-
Ashburner,M.,Ball,C.A.,Blake,J.A.,Botstein,D.,Butler,H.,MichaelCherry,
ments(ThompsonandCompton,2011),andthesecanpossibly J., Davis, A.P., Dolinski, K., Dwight, S.S., Eppig, J.T., et al. (2000). Gene
provideinsightsintotheirfunctionalimplicationsandhopefully ontology:toolfortheunificationofbiology.Nat.Genet.25,25–29.
opennoveltherapeuticopportunities. Avner,P.,andHeard,E.(2001).X-Chromosomeinactivation:counting,choice
andinitiation.Nat.Rev.Genet.2,59–67.
STAR+METHODS Bailey Blackburn, J.,Pokrovskaya, I.,Fisher,P., Ungar, D.,and Lupashin,
V.V.(2016).COGcomplexcomplexities:detailedcharacterizationofacom-
pletesetofHEK293TcellslackingindividualCOGsubunits.Front.CellDev.
Detailedmethodsareprovidedintheonlineversionofthispaper
Biol.4,23.
andincludethefollowing:
Battle,A.,Khan,Z.,Wang,S.H.,Mitrano,A.,Ford,M.J.,Pritchard,J.K.,and
Gilad,Y.(2015).Genomicvariation.ImpactofregulatoryvariationfromRNA
d KEYRESOURCESTABLE
toprotein.Science347,664–667.
d CONTACTFORREAGENTANDRESOURCESHARING
Beroukhim,R.,Mermel,C.H.,Porter,D.,Wei,G.,Raychaudhuri,S.,Donovan,
d EXPERIMENTALMODELANDSUBJECTDETAILS
J.,Barretina,J.,Boehm,J.S.,Dobson,J.,Urashima,M.,etal.(2010).Theland-
d METHODDETAILS
scapeofsomaticcopy-numberalterationacrosshumancancers.Nature463,
B CellLinesDrugResponseAnalysis 899–905.
B shRNADeliveryviaLentiviralTransduction Boyle,E.A.,Li,Y.I.,andPritchard,J.K.(2017).Anexpandedviewofcomplex
B WesternBlotValidation traits:frompolygenictoomnigenic.Cell169,1177–1186.
396 CellSystems5,386–398,October25,2017
CancerGenomeAtlasNetwork.(2012a).Comprehensivemolecularcharacter- McKinney,W.,(2010).Datastructuresforstatisticalcomputinginpython.In
izationofhumancolonandrectalcancer.Nature487,330–337. Proceedingsofthe9thPythoninScienceConference,pp.51–56.
CancerGenomeAtlasNetwork.(2012b).Comprehensivemolecularportraits McShane,E.,Sin,C.,Zauber,H.,Wells,J.N.,Donnelly,N.,Wang,X.,Hou,J.,
ofhumanbreasttumours.Nature490,61–70. Chen,W.,Storchova,Z.,Marsh,J.A.,etal.(2016).Kineticanalysisofprotein
CancerGenomeAtlasResearchNetwork.(2011).Integratedgenomicana- stabilityrevealsage-dependentdegradation.Cell167,803–815.e21.
lysesofovariancarcinoma.Nature474,609–615. Mermel,C.H.,Schumacher,S.E.,Hill,B.,Meyerson,M.L.,Beroukhim,R.,and
Chick,J.M.,Munger,S.C.,Simecek,P.,Huttlin,E.L.,Choi,K.,Gatti,D.M., Getz,G.(2011).GISTIC2.0facilitatessensitiveandconfidentlocalizationofthe
Raghupathy, N., Svenson, K.L., Churchill, G.A., and Gygi, S.P. (2016). targetsoffocalsomaticcopy-numberalterationinhumancancers.Genome
Definingtheconsequencesofgeneticvariationonaproteome-widescale. Biol.12,R41.
Nature534,500–505. Mertins,P.,Mani,D.R.,Ruggles,K.V.,Gillette,M.A.,Clauser,K.R.,Wang,P.,
Coscia,F.,Watters,K.M.,Curtis,M.,Eckert,M.A.,Chiang,C.Y.,Tyanova,S., Wang,X.,Qiao,J.W.,Cao,S.,Petralia,F.,etal.(2016).Proteogenomicscon-
Montag,A.,Lastra,R.R.,Lengyel,E.,andMann,M.(2016).Integrativeprote- nectssomaticmutationstosignallinginbreastcancer.Nature534,55–62.
omicprofilingofovariancancercelllinesrevealsprecursorcellassociatedpro- Nagaraj,N.,Wisniewski,J.R.,Geiger,T.,Cox,J.,Kircher,M.,Kelso,J.,Pa€a€bo,
teinsandfunctionalstatus.Nat.Commun.7,12645. S.,andMann,M.(2011).Deepproteomeandtranscriptomemappingofahu-
Davoli,T.,Uno,H.,Wooten,E.C.,andElledge,S.J.(2017).Tumoraneuploidy mancancercellline.Mol.Syst.Biol.7,548.
correlateswithmarkers ofimmuneevasionandwithreducedresponseto Ori,A.,Iskar,M.,Buczak,K.,Kastritis,P.,Parca,L.,Andre´s-Pons,A.,Singer,
immunotherapy.Science355,https://doi.org/10.1126/science.aaf8399. S.,Bork,P.,andBeck,M.(2016).Spatiotemporalvariationofmammalianpro-
Dephoure,N.,Hwang,S.,O’Sullivan,C.,Dodgson,S.E.,Gygi,S.P.,Amon,A., teincomplexstoichiometries.GenomeBiol.17,47.
andTorres,E.M.(2014).Quantitativeproteomicanalysisrevealsposttransla- Pedregosa,F.,Varoquaux,G.,Gramfort,A.,Michel,V.,Thirion,B.,Grisel,O.,
tionalresponsestoaneuploidyinyeast.Elife3,e03023. Blondel,M.,Prettenhofer,P.,Weiss,R.,Dubourg,V.,etal.(2011).Scikit-learn:
Edwards,N.J.,Oberti,M.,Thangudu,R.R.,Cai,S.,McGarvey,P.B.,Jacob,S., machinelearninginpython.J.Mach.Learn.Res.12,2825–2830.
Madhavan,S.,andKetchum,K.A.(2015).TheCPTACdataportal:aresource Perfetto, L., Briganti, L., Calderone, A., Perpetuini, A.C., Iannuccelli, M.,
forcancerproteomicsresearch.J.ProteomeRes.14,2707–2713. Langone, F., Licata, L., Marinkovic, M., Mattioni, A., Pavlidou, T., et al.
Franceschini,A.,Szklarczyk,D.,Frankild,S.,Kuhn,M.,Simonovic,M.,Roth, (2016).SIGNOR:adatabaseofcausalrelationshipsbetweenbiologicalen-
A.,Lin,J.,Minguez,P.,Bork,P.,vonMering,C.,etal.(2013).STRINGv9.1: tities.NucleicAcidsRes.44,D548–D554.
protein-proteininteractionnetworks,withincreasedcoverageandintegration. Price, A.L., Helgason, A., Thorleifsson, G., McCarroll, S.A., Kong, A., and
NucleicAcidsRes.41,D808–D815. Stefansson, K. (2011). Single-tissue and cross-tissue heritability of gene
Hunter,J.D.(2007).Matplotlib:a2Dgraphicsenvironment.Comput.Sci.Eng. expressionviaidentity-by-descentinrelatedorunrelatedindividuals.PLoS
9,90–95. Genet.7,e1001317.
Iorio,F.,Knijnenburg,T.A.,Vis,D.J.,Bignell,G.R.,Menden,M.P.,Schubert, Rahman,M.,Jackson,L.K.,Johnson,W.E.,Li,D.Y.,Bild,A.H.,andPiccolo,
M.,Aben,N.,Gonc¸alves,E.,Barthorpe,S.,Lightfoot,H.,etal.(2016a).Aland- S.R. (2015). Alternative preprocessing of RNA-sequencing data in The
scapeofpharmacogenomicinteractionsincancer.Cell166,740–754. CancerGenomeAtlasleadstoimprovedanalysisresults.Bioinformatics31,
3666–3672.
Iorio, F., Garcia-Alonso, L., Brammeld, J., Martincorena, I., Wille, D.R.,
McDermott,U.,andSaez-Rodriguez,J.(2016b).Pathway-baseddissection Ritchie,M.E.,Phipson,B.,Wu,D.,Hu,Y.,Law,C.W.,Shi,W.,andSmyth,G.K.
ofthegenomicheterogeneityofcancerhallmarkswithSLAPenrich.BioRxiv. (2015). limma powers differential expression analysesfor RNA-sequencing
https://doi.org/10.1101/077701. andmicroarraystudies.NucleicAcidsRes.43,e47.
Itsara,A.,Cooper,G.M.,Baker,C.,Girirajan,S.,Li,J.,Absher,D.,Krauss, Robinson,M.D.,andOshlack,A.(2010).Ascalingnormalizationmethodfor
R.M.,Myers,R.M.,Ridker,P.M.,Chasman,D.I.,etal.(2009).Populationanal- differentialexpressionanalysisofRNA-seqdata.GenomeBiol.11,R25.
ysisoflargecopynumbervariantsandhotspotsofhumangeneticdisease. Robinson, M.D., McCarthy, D.J., and Smyth, G.K. (2010). edgeR: a
Am.J.Hum.Genet.84,148–161. Bioconductor package for differential expression analysis of digital gene
Kanehisa,M.,Sato,Y.,Kawashima,M.,Furumichi,M.,andTanabe,M.(2016). expressiondata.Bioinformatics26,139–140.
KEGGasareferenceresourceforgeneandproteinannotation.NucleicAcids Ruepp,A.,Brauner,B.,Dunger-Kaltenbach,I.,Frishman,G.,Montrone,C.,
Res.44,D457–D462. Stransky,M.,Waegele,B.,Schmidt,T.,Doudieu,O.N.,Stu€mpflen,V.,etal.
Karnezis,A.N.,Wang,Y.,Ramos,P.,Hendricks,W.P.,Oliva,E.,D’Angelo,E., (2008). CORUM: the comprehensive resource of mammalian protein com-
Prat,J.,Nucci,M.R.,Nielsen,T.O.,Chow,C.,etal.(2016).DuallossoftheSWI/ plexes.NucleicAcidsRes.36,D646–D650.
SNFcomplexATPasesSMARCA4/BRG1andSMARCA2/BRMishighlysensi- Ruepp, A., Waegele, B., Lechner, M., Brauner, B., Dunger-Kaltenbach, I.,
tiveandspecificforsmallcellcarcinomaoftheovary,hypercalcaemictype. Fobo,G.,Frishman,G.,Montrone,C.,andMewes,H.-W.(2010).CORUM:
J.Pathol.238,389–400. the comprehensive resource of mammalian protein complexes – 2009.
Kim,W.,Bennett,E.J.,Huttlin,E.L.,Guo,A.,Li,J.,Possemato,A.,Sowa,M.E., NucleicAcidsRes.38,D497–D501.
Rad, R., Rush, J., Comb, M.J., et al. (2011). Systematic and quantitative Santarius,T.,Shipley,J.,Brewer,D.,Stratton,M.R.,andCooper,C.S.(2010).
assessmentoftheubiquitin-modifiedproteome.Mol.Cell44,325–340. Acensus ofamplifiedandoverexpressedhumancancer genes.Nat.Rev.
Kiriakidou,M.,Tan,G.S.,Lamprinaki,S.,DePlanell-Saguer,M.,Nelson,P.T., Cancer10,59–64.
andMourelatos,Z.(2007).AnmRNAm7Gcapbinding-likemotifwithinhuman Shangary,S.,andWang,S.(2008).TargetingtheMDM2-p53interactionfor
Ago2repressestranslation.Cell129,1141–1151. cancertherapy.Clin.CancerRes.14,5318–5324.
Law,C.W.,Chen,Y.,Shi,W.,andSmyth,G.K.(2014).voom:precisionweights Stingele,S.,Stoehr,G.,Peplowska,K.,Cox,J.,Mann,M.,andStorchova,Z.
unlocklinearmodelanalysistoolsforRNA-seqreadcounts.GenomeBiol. (2012).Globalanalysisofgenome,transcriptomeandproteomerevealsthe
15,R29. responsetoaneuploidyinhumancells.Mol.Syst.Biol.8,608.
Lawrence,R.T.,Perez,E.M.,Herna´ndez,D.,Miller,C.P.,Haas,K.M.,Irie,H.Y., Subramanian, A., Tamayo, P., Mootha, V.K., Mukherjee, S., Ebert, B.L.,
Lee,S.-I.,Blau,C.A.,andVille´n,J.(2015).Theproteomiclandscapeoftriple- Gillette,M.A.,Paulovich,A.,Pomeroy,S.L.,Golub,T.R.,Lander,E.S.,etal.
negativebreastcancer.CellRep.11,630–644. (2005).Genesetenrichmentanalysis:aknowledge-basedapproachforinter-
Lilley,B.N.,andPloegh,H.L.(2004).Amembraneproteinrequiredfordisloca- preting genome-wide expressionprofiles.Proc. Natl. Acad. Sci.USA 102,
tionofmisfoldedproteinsfromtheER.Nature429,834–840. 15545–15550.
Lyon,M.F.(1961).GeneactionintheX-chromosomeofthemouse(Musmus- Tang, Y.-C., and Amon, A. (2013). Gene copy-number alterations: a cost-
culusL.).Nature190,372–373. benefitanalysis.Cell152,394–405.
CellSystems5,386–398,October25,2017 397
Teckchandani,A.,andCooper,J.A.(2016).Theubiquitin-proteasomesystem Xie,Y.,Wolff,D.W.,Wei,T.,Wang,B.,Deng,C.,Kirui,J.K.,Jiang,H.,Qin,J.,
regulatesfocaladhesionsattheleadingedgeofmigratingcells.Elife5,https:// Abel,P.W.,andTu,Y.(2009).Breastcancermigrationandinvasiondependon
doi.org/10.7554/eLife.17440. proteasomedegradationofregulatorofG-proteinsignaling4.CancerRes.69,
TheGeneOntologyConsortium(2015).GeneOntologyConsortium:goingfor- 5743–5751.
ward.NucleicAcidsRes.43,D1049–D1056. Ye,Y.,Shibata,Y.,Yun,C.,Ron,D.,andRapoport,T.A.(2004).Amembrane
TheUniProtConsortium(2015).UniProt:ahubforproteininformation.Nucleic protein complex mediates retro-translocation from the ER lumen into the
AcidsRes.43,D204–D212. cytosol.Nature429,841–847.
Thompson,S.L.,andCompton,D.A.(2011).Chromosomesandcancercells. Zhang, B., Wang, J., Wang, X., Zhu, J., Liu, Q., Shi, Z., Chambers, M.C.,
ChromosomeRes.19,433–444. Zimmerman,L.J.,Shaddox,K.F.,Kim,S.,etal.(2014).Proteogenomiccharac-
Wagner,S.,Herrmannova´,A.,Malı´k,R.,Peclinovska´,L.,andVala´(cid:2)sek,L.S. terizationofhumancolonandrectalcancer.Nature513,382–387.
(2014). Functional and biochemical characterization of human eukaryotic Zhang,H.,Liu,T.,Zhang,Z.,Payne,S.H.,Zhang,B.,McDermott,J.E.,Zhou,
translationinitiationfactor3inlivingcells.Mol.Cell.Biol.34,3041–3052. J.-Y.,Petyuk,V.A.,Chen,L.,Ray,D.,etal.(2016).Integratedproteogenomic
Wang,J.,Ma,Z.,Carr,S.A.,Mertins,P.,Zhang,H.,Zhang,Z.,Chan,D.W., characterization of human high-grade serous ovarian cancer. Cell 166,
Ellis,M.J.C.,Townsend,R.R.,Smith,R.D.,etal.(2016).Proteomeprofilingout- 755–765.
performstranscriptomeprofilingforco-expressionbasedgenefunctionpre- Zolov,S.N.,andLupashin,V.V.(2005).Cog3pdepletionblocksvesicle-medi-
diction.Mol.Cell.Proteomics16,121–134. atedGolgiretrogradetraffickinginHeLacells.J.CellBiol.168,747–759.
398 CellSystems5,386–398,October25,2017
STAR+METHODS
KEYRESOURCESTABLE
REAGENTorRESOURCE SOURCE IDENTIFIER
Antibodies
Mousemonoclonalanti-AP3B1 Abnova Cat.#H00008546-B01P;RRID:AB_10714215
Rabbitmonoclonalanti-AP3M1 Abcam Cat.#ab201227;RRID:AB_2715538
Rabbitmonoclonalanti-GTF2E1/TFIIEalpha Abcam Cat.#ab140634;RRID:AB_2715539
Rabbitmonoclonalanti-GTF2E2/TFIIEbeta Abcam Cat.#ab187143;RRID:AB_2715540
Rabbitmonoclonalanti-GAPDH(D15H11) CellSignalingTechnologies Cat.#5174S;RRID:AB_10622025
Goat-anti-rabbitIgG(HRP-linked) CellSignalingTechnologies Cat.#7074S;RRID:AB_2099233
Horse-anti-mouseIgG(HRP-linked) CellSignalingTechnologies Cat.#7076S;RRID:AB_330924
BacterialandVirusStrains
OneShot(cid:2)TOP10ChemicallyCompetentE.coli ThermoFisher Cat.#C404003
Chemicals,Peptides,andRecombinantProteins
jetPEItransfectionreagent Polyplustransfection Cat.#101-10N
CriticalCommercialAssays
DC(cid:2)proteinassay Bio-Rad Cat.#500-0116
DepositedData
CPTACproteomicsofBRCA,HGSCandCOREAD CPTACConsortium(Mertinsetal.,2016; https://cptac-data-portal.georgetown.edu/
Zhangetal.,2016andZhangetal.,2014) cptacPublic/
TCGAtranscriptomicsRNA-seqrawcounts TCGAConsortium(Rahmanetal.,2015) GSE62944
TCGAcopy-numberGISTICthresholdedscores TCGAConsortium(Mermeletal.,2011) http://firebrowse.org/
Celllinesgeneexpression Iorioetal.,2016b E-MTAB-3610
Celllinesdrugresponse Iorioetal.,2016b TableS4
ExperimentalModels:CellLines
Human:HCT116 ATCC–LGCstandards Cat.#CCL-247;RRID:CVCL_0291
Human:HEK293 ATCC–LGCstandards Cat.#CRL-1573;RRID:CVCL_0045
RecombinantDNA
psPAX2–lentiviralpackagingvector DidierTronoLab Addgeneplasmid
#12260
pMD2.G–lentiviralEnvelopevector DidierTronoLab Addgeneplasmid
#12259
pLKO.1-shAP3B1(TRCN0000286136)–shRNA SigmaAldrich Cat.#SHCLND-NM_003664
pLKO.1-shAP3M1(TRCN0000065101)–shRNA SigmaAldrich Cat.#SHCLND-NM_012095
pLKO.1-shGTF2E1(TRCN0000020722)–shRNA SigmaAldrich Cat.#SHCLND-NM_005513
pLKO.1-shGTF2E2(TRCN0000020775)–shRNA SigmaAldrich Cat.#SHCLND-NM_002095
pLKO.1-shNT–shRNA SigmaAldrich Cat.#SHC016-1EA
SoftwareandAlgorithms
QuantityOne(cid:3)Basicsoftware Bio-Rad N/A(Freeware)
GraphPadPrism5.03software GraphPad https://www.graphpad.com/
JMP(cid:3)10software SASInstituteInc. https://www.jmp.com/en_us/home.html
Limma Ritchieetal.,2015 http://bioconductor.org/packages/release/
bioc/html/limma.html
edgeR Robinsonetal.,2010 https://bioconductor.org/packages/release/
bioc/html/edgeR.html
SLAPenrich Iorioetal.,2016a https://github.com/francescojm/SLAPenrich
Sklearn Pedregosaetal.,2011 http://scikit-learn.org/
CellSystems5,386–398.e1–e4,October25,2017 e1
