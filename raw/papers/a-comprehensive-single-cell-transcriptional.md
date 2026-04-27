---
source_path: /mnt/c/Users/Administrator/Zotero/storage/VJQRN4ST/Pellin 等 - 2019 - A comprehensive single cell transcriptional landsc.pdf
ingested: 2026-04-23
sha256: 2d5f1079ce569ac0
---

ARTICLE
OPEN
https://doi.org/10.1038/s41467-019-10291-0
A comprehensive single cell transcriptional
landscape of human hematopoietic progenitors
Danilo Pellin1,5, Mariana Loperfido 1,5, Cristina Baricordi1, Samuel L. Wolock 2, Annita Montepeloso1,
Olga K. Weinberg3, Alessandra Biffi1, Allon M. Klein 2 & Luca Biasco1,4
Hematopoietic Stem/Progenitor cells (HSPCs) are endowed with the role of maintaining a
diversepoolofbloodcellsthroughoutthehumanlife.Despiterecentefforts,thenatureofthe
early cell fate decisions remains contentious. Using single-cell RNA-Seq, we show that
existing approaches to stratify bone marrow CD34+ cells reveal a hierarchically-structured
transcriptional landscape of hematopoietic differentiation. Still, this landscape misses
important early fate decisions. We here provide a broader transcriptional profiling of bone
marrowlineagenegativehematopoieticprogenitorsthatrecoversakeymissingbranchpoint
into basophils and expands our understanding of the underlying structure of early adult
human haematopoiesis. We also show that this map has strong similarities in topology and
gene expression to that found in mouse. Finally, we identify the sialomucin CD164, as a
reliablemarkerfortheearliestbranches ofHSPCsspecificationandweshowedhowitsuse
can foster the design of alternative transplantation cell products.
1GeneTherapyProgram,Dana-Farber/BostonChildren’sCancerandBloodDisordersCenter,HarvardMedicalSchool,Boston,MA02115,USA.
2DepartmentofSystemsBiology,HarvardMedicalSchool,Boston,MA02115,USA.3DepartmentofPathology,BostonChildren’sHospitalandHarvard
MedicalSchool,Boston,MA02115,USA.4UniversityCollegeofLondon(UCL),GreatOrmondStreetInstituteofChildHealthFacultyofPopulationHealth
Sciences,London,WC1N1EH,UK.5Theseauthorscontributedequally:DaniloPellin,MarianaLoperfido.Correspondenceandrequestsformaterialsshouldbe
addressedtoA.M.K.(email:Allon_Klein@hms.harvard.edu)ortoL.B.(email:l.biasco@ucl.ac.uk)
NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications 1
;,:)(0987654321
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
I
n humans, there have been conflicting proposals for the scRNA-Seq data to infer the structure of cell states in high-
hierarchical relationships linking different hematopoietic dimensional gene expression space (Fig. 1c). We applied a
progenitors1–7.
In the conventional depiction of human visualization method previously developed for mouse hemato-
haematopoiesis, supported by lineage-tracing studies in the poieticprogenitors24,wherebyeachcellrepresentsagraphnode,
mouse8, the earliest branching splits lymphoid vs myelo/ery- with graph edges linking nearest neighbor cells. The scRNA-Seq
throidfatecommitment.Conversely,inarecentchallengeofthe graph, visualized using SPRING force-directed layout25, shows a
classicalview,ithasbeensuggestedthatmultipotentprogenitors hierarchical, tree-like continuum of states, with branches that
could undergo a very early fate decision towards the mega- terminate at cells expressing recognizable transcriptional sig-
karyocyte lineage followed by a single step-wise transition to natures of lineage commitment before the expression of final
either erythroid, myeloid, or lymphoid commitment9. The maturationmarkers(Fig.1c,d)(megakaryocytes(Meg),erythroid
adventofsingle-cellRNAsequencing(scRNA-Seq)hasnotonly cells (E), granulocytes (G), dendritic cells (DC), lymphoid cells
created an opportunity to improve our understanding of the (Ly1-2)). The structure of the single-cell data broadly partitions
nature of human haematopoiesis through the study of tran- based on immunophenotypic subpopulations, but, significantly
scriptional single-cell states10–12, but also generated conflicting andinlinewithrecentsuggestions9,weobservedthatpreviously
observations. Initial use of this technology in humans led to an defined HSPC subpopulations hide substantial transcriptional
alternative view that early haematopoiesis is composed by a heterogeneity (Supplementary Fig. 2a).
continuum of low-primed undifferentiated haematopoietic Our scRNA-Seq map of CD34+ subpopulations suggests
stem and progenitor cells (CLOUD-HSPCs) from which that HSPCs do not undergo a single-step transition from
unilineage-restricted cells emerge10. Recently, scRNA-Seq data CLOUD-HSPCs to unilineage states. Instead, they form a
combined with assays of chromatin accessibility supported structured hierarchy (Fig. 1c). The earliest fate split separates
instead the notion of a structured hierarchy, revealing a var- erythroid–megakaryocyte progenitors from lymphoid–myeloid
iegated hematopoietic landscape13, the existence of lineage- progenitors (LMPs), which separate further into lymphoid, DC
biased stem cells in mice14,15 and of different stages of human and granulocytic progenitors. This hierarchy is highlighted by
lymphoid commitment in humans16,17. both inferred transcriptional trajectories (Fig. 1e and Supple-
Human HSPCs are commonly identified by expression of the mentary Fig. 3a) and formal high-dimensional analysis of graph
antigen CD3418. CD34+ cells are heterogeneous, and there are structure using the population balance analysis (PBA) algo-
ongoing efforts to classify their substructure by immunopheno- rithm24 (Fig. 1f)24. We conclude that human HSPCs are more
typingandaccordingtotheirdifferentiationandinvivosurvival organized than recently hypothesized and show more structure
potential5. The CD34+ cell population structure is unresolved, than appreciated by classical immunophenotyping.
with recent studies showing that the current immunophenoty-
picallydefinedCD34+subsetscouldbemoreheterogeneousthan
previouslythought9,19.Apossiblereasonforthelackofresolution Extending the scRNA profiling to all BM progenitors. In the
is that enrichment methods for CD34+ cells may bias the 1980s, the wide adoption of monoclonal antibodies for immu-
representation of cell states during early hematopoietic commit- nophenotyping revealed that the CD34 antigen is an effective
ment, as the CD34 marker is downregulated at different rates marker to isolate immature HSPCs from humans18. Since then,
along commitment to different cell fates20,21. In this regard, one efforts have been made to define the hierarchical structure of
should note that previous single-cell studies on human hemato- HSPCs purified from immunomagnetic-selected CD34+ cells,
poiesis focused exclusively on the whole CD34+ population undertheassumptionthatthiscellpopulationeffectivelycaptures
(comprising both Lin− and Lin+ cells)11, or on in silico mod- all early fate choices. Although our above analysis supports such
eling of the fate commitment of the CD34+ fraction containing efforts, we reasoned that a focus on CD34+ cells purified with
the least differentiated HSPCs10. magneticbeadsenrichmentmightprovideanincompleteviewof
Wehereaimatprovidinginsightsonthepopulationstructure the earliest branching events in haematopoiesis. We noted, for
of early hematopoietic commitment, by profiling human HSPCs example, that branches towards basophils/eosinophils/mast cells
withhigh-throughputscRNA-Seq22,23.Differentlyfromprevious andmonocytescommitmentsweremissinginourinitialscRNA-
works,inthepresentstudywenotonlyisolatetheimmaturecells SeqanalysisofCD34cells,despitetheseappearingasearlyevents
expressing the CD34 antigen, but we also extend our analysis to in mouse haematopoiesis24. In addition, many cells negative for
thewholebonemarrow(BM)fractionlackingthemainmarkers mature lineage markers in human BM are
CD34low/−
and could
of terminal differentiation (Lineage negative, Lin− cells). The account for additional transitional states at which CD34 expres-
resulting scRNA maps provide a comprehensive transcriptional sion is rapidly downregulated, thus greatly reducing their prob-
snapshot of the early human hematopoietic cell fates, shedding abilityofcapture.Therefore,togenerateacompletelandscapeof
lightontheoriginofthebasophilbranchingandonapreviously early haematopoiesis, we extended our analysis to encompass
unappreciated surface marker for fractionating the HSPCs cell human CD34low and CD34− cells. To this aim, we collected
product. from a second healthy donor four fractions of BM Lin− cells,
covering different degrees of maturation (Fig. 2a). The graded
fluorescence-activated cell (FACS) sorting used in this analysis
Results corrects for expansion of cells as they differentiate, allowing
Generating a high-resolution scRNA map of CD34+ pro- examinationofearlystatesalongsidelateronesthatcomprisethe
genitors. To establish a reference data set and to address the vast majority of Lin− progenitors. In fractionating the cells by
heterogeneity and fate potential of the known CD34+ subsets, maturity, we made use of a cell surface marker, CD164, that we
our first investigations aimed at mapping at high-resolution the identified from the initial data set as expressed by cells that are
single-cell transcriptional states of cells commonly defined as multipotent until just beyond the first E/Meg–LMP branchpoint
humanHSPCs(Fig. 1a).To thisgoal, weseparated CD34+cells (Fig. 1g, h). This fractionation strategy allowed us to preserve
purified by magnetic beads selection into seven subpopulations5, resolution of the single-cell events of the more-primitive com-
marking cells of differing fate potential (Fig. 1b) and tagged and partments, whereas at the same time maintaining a full repre-
sequencedthetranscriptomeof6011singlecells(Supplementary sentation of the late cell fate branching (Fig. 2b; Supplementary
Fig. 1a and Supplementary Table 1). We then used the Figs. 1b, 2b).
2 NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications
a Fig.2
Healthy donor Bone marrow MNC CD34+ cells
Fig.1
Ficoll
Transcriptional trajectories discovery
Grouping
GEA
HSC
MPP
MLP
PreB/NK 150 K
As predicted, the transcriptional map of the Lin− fraction, identify later cell fate decisions. Monocyte progenitors seem to
derivedfromthehigh-throughputclusteringof15,401singlecells emerge from a common neutrophil/monocyte precursor later in
(Fig. 2b; Supplementary Fig. 4 and Supplementary Table 1), the myeloid commitment and after the branching decision
revealed important early features that were missing from the towards DC progenitors, with a possible contribution from DC
analysis of the immune-selected CD34+ population. Using the progenitors as recently shown in the mouse24,26. These data also
same graph-based technique as for CD34+ cells, we could now suggest that the identity of the remaining CD34− Lin− cells
A-CCS 83DC 09DC A-CSS 01DC 531DC
A 3 2 2 8 24 20 16 12
Skeletonization SADC A
SPRING plot PBA
CD38+
CD34+ LIN– CD38– CD7– CD10–
MEP
CMP
GMP
LIN CD34 CD45RA CD7 CD45RA CD45RA
PLEK HBB MPO
Ly1
SPIB CD79A DNTT
Ly2
Meg
E
G
DC
Me E g 3 2 2 2 8 4 B C C S D D T 3 1 2 7 64 CD34 2 1 3 10 L L D y y G C 2 1 Ly1Ly2G DC EMeg M 2 1 1 8 4 0 0 6 2 erge sig. High K I C E C I C P C T I V R D D S G T A I O F 4 6 2 M A 4 3 2 M B 2 3 R B 1 B
E MegLy1Ly2DCG couplings CD34
7 ATP1B3
11 20.0 G CD Y 4 P 7 C Normalized expr. value
4 5 6 9 8 Ly1 E , , M L D y e 2 G C g , 1 1 1 1 7 5 2 0 7 5 2 0 . . . . 5 0 5 0 . . . . 5 0 5 0 Low I C M I C C I L L T D S D M 2 7 G F R R 7 9 E B 9 3 9 G 2 A R CD164 0 5 10 15 20 25
Ly1, Ly2, G E,Meg CD53
DC CD48
LAIR1
FLT3
CD74
SELL
E MegLy1Ly2DC G 1 2 3 4 5 6 7 8 91011
ecnaci ) f e in r g o i c s s g -z n ( ilpuoC
ecnaci ) f e in r g o i c s s g -z n ( ilpuoC
ecnacifingis gnilpuoC )erocs-z(
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
Single-cell RNA-seq
FACS-sorting
Magnetic
enrichment
B C D E 8
F 4 0
B C D E F
b
250 K 105 105 250 K 105 105
200 K 200 K 104 104 104 104
150 K 100 K 103 103 100 K 103 103
50 K 0 0 50 K 0 0
0 0
0 103 104 105 0 103 104 105 0 103 104 105 0 103 104 105 0 103 104 105 0 103 104 105
c d
e f g h
NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications 3
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
Fig.1ExperimentalworkflowandtranscriptionalmapforhumanHSPCs.aSchematicforexperimentaldesignandworkflowofdataanalysis.Two
experimentshavebeenperformedontwoseparatehealthydonorstogeneratetwosingle-celltranscriptomemaps(MNC,mononuclearcells;PBA,
populationbalanceanalysis;GEA,Geneexpressionanalysis).bGatingstrategyusedfortheFACSsortingofsevenHSPCsubsetsfrommagneticbeads
purifiedCD34+cellsofahealthydonorBM(HSC,hematopoieticstemcells;MPP,multipotentprogenitors;MLP,multi-lymphoidprogenitors;Pre-B/NK,
Pre-Blymphocytes/naturalkillercells;MEP,megakaryocyte-erythroidprogenitors;CMP,commonmyeloidprogenitors;GMP,granulocyte–monocyte
progenitors).cSPRINGplotofthesevenHSPCssingle-celltranscriptomes.Eachpointisonecell.Labelsattheedgesrepresentthetranscriptionalstates
associatedtoearlylineagecommitment(Meg,megakaryocytes;E,erythroidcells;G,granulocytes;DC,dendriticcells;Ly1/Ly2,lymphoidB,T,NKcells).
Colorlegendasinb.dRepresentativegeneexpressionmapsoflineagedefininggenes(PLEK,Meg;HBB,E;MPO,G;SPIB,DC;CD79A,andDNTT,Ly1/2).
eClassificationofindividualcellsintohomogenoustranscriptionalgroupsnumberedfrom1to11,basedoninferredprincipaltrajectories(Supplementary
Fig.3afordetails).fPredictedhierarchybasedontwostepsPBA.gHeatmapshowingtheexpressionaverageingroupsshownineforstatistically
significantgenescodingforCDmarkers(likelihoodratiotest[LRT]adjustedpvalue<0.05).hGeneexpressionmapsofCD34andCD164
consistsmostlyoflateneutrophilprogenitors,andofacontinuum (MEP) (Fig. 3a). Building on these results, we thus designed and
of differentiating states towards erythroid commitment. Our conducted a series of in vitro differentiation assays starting from
results could be formalized, on a computational basis, by both FACS sorting Lin−CD34+ cells into CD135+ (FLT3+) (by
high dimensions (using PBA algorithm, Fig. 2c) and inferred definition containing common myeloid progenitors (CMP) and
transcriptional trajectories (Fig. 2d and Supplementary Fig. 3b) granulocyte–monocyte progenitors; GMP) and CD135−(FLT3−)
andwereconfirmeduponanalyzingthedatawithanindependent (by definition containing MEP) cells (Fig. 3b–d and Supplemen-
method(DiffusionMaps27,SupplementaryFig.5,6)thatdoesnot tary Fig. 9c). These two groups of cells were separately put in
rely on a limited amount of k-nearest neighbors (kNN) for data- culture in myeloid-, megakaryocytes (MK)-, and basophil-
embeddingcalculation.Togeneratearesourceforfurtherstudies, differentiating conditions under the hypothesis that if basophils
weinvestigatedtheassociationbetweengeneexpressiondynamics are generated by CMP or GMP (as suggested by the classical
andcellsprogressionalongtheestimateddifferentiationpaths.We modelofhaematopoiesis)theCD135+fractionshouldbetheone
identifiedputativetranscriptionalswitchesoccurringduringearly capableofdifferentiatingintobasophilsafterculture.Asreported
hematopoietic cell fate choices and genes exhibiting significant inFig.3,theLin−CD34+4+CD135−andLin−CD34+CD135+
variations during lineage commitments (Fig. 2e; Supplementary populations had, as expected, specific growth preferences toward
Fig.7andSupplementaryInformationforthecompletelists).This MK(theformer)andmyeloid(thelatter)cellfates(Fig.3e,f).The
analysiscontainsvaluableinformationforinvitroreprogramming twopopulationsgrewatsimilarrateinbasophilicconditions,but
efforts and for investigations into the origin of blood cell whiletheLin−CD34+CD135+fractiongeneratedmostlyCD14+
differentiation disorders and cancers. monocytes (Fig. 3g, h), the Lin−CD34+CD135− fraction
To understand how the enrichment of CD34+ subsets could emerged as the only population capable of giving rise with high
limit our view of early haematopoiesis, we projected the CD34+ efficiencytobonafidebasophils(Fig.3g,h;SupplementaryFig.9b,
HSPCs subpopulations onto the Lin− state map (Fig. 2f). The d,e)definedasSSC-AlowCD14-CD15-FceRIA+CCR3+IL5RA+
analysis confirmed that large portions of the Lin− map are cells(asinMorietal.200930andinourimmunophenotypingon
strongly under-represented upon the magnetic pulldown of the humanperipheralbloodreportedinSupplementaryFig.9a).This
CD34+ population (namely the ones identifying basophils, observation is in line with our scRNA data showing that the
monocytes progenitors, and the stages of late erythroid differ- basophil branch emerges from CD135− cells already committed
entiation). This supports the concept that the Lin− population toward a mixed MK/Erythroid/Basophil potential. Notably,
structureprovidesamorecompleteviewofkeycellfatedecisions becauseourexperimentaldesignpurposelyincludedalsoCD38−
alonghumanhematopoieticcommitmentandsuggeststhat,fora multipotent progenitors, one could have expected that basophils
complete classification of HSPCs, analyses should be performed would have been generated at similar rates by the CD38− HSC/
on FACS-sorted CD34+, CD34low and CD34− compartments. MPP that were present in both CD135+ and CD135− cell frac-
Finally,withthisprojectionwecouldappreciatetheheterogeneous tions(Fig.3d).Conversely,theobservationthatonlytheCD135−
nature of the currently defined HSPC subsets, showing that they cells were endowed with substantial basophilic potential strongly
can be further fractionated into distinct and more homogenous support the notion that the Lin−CD34+CD38−CD135− popu-
transcriptional states (Supplementary Fig. 8). lation might be already enriched in stem cells with very early
priming towardsa basophilic cell fate.
Exploring the origin of the human basophilic branch.
Themost-notableresultemergingfromtheexplorationofourBM Comparing human vs mouse hematopoietic scRNA-seq pro-
Lin−mapwastheidentificationofabranchtowardcellscarrying files. Another question of practical interest for modeling human
atranscriptionalprofileofearlybasophilsspecification.Strikingly, disease is the relationship between human and mouse haemato-
this class of basophils progenitors (BaP) was found to associate poiesis. Although cell surface markers used to isolate HSPC
witherythroidandmegakaryocytefatesandnotwithgranulocytes subpopulations are known to differ between the two species,
precursors. Our data, generated on adult human BM, align with scRNA-Seq provides anopportunitytolinkpopulationstructure
and expand on preliminary observations done in human cord using whole-transcriptome information. We compared the
blood CD34+ cells11,28, and in murine haematopoiesis29. To scRNA-SeqmapofthehumanLin−populationtothatofmouse
elaborate on this observation, we computationally projected the HSPCs,usingdatathatwerecentlypublishedonKit+mouseBM
BasophilbranchofourBMLin−mapontotheLin−HSPCmap progenitors24. This analysis unveiled a strong similarity among
to identify which, among the HSPC single cell states, had the thebranchingstructuresofhaematopoiesisinthetwoorganisms,
highestscRNAsimilaritytothisbranch.Thetopologicaloriginof with almost a 1:1 correspondence between hierarchies of cell
the early basophil cell specification in the HSPC map was in states (Fig. 4a vs Fig. 2d, Supplementary Figs. 3c, 10). Further-
strikingaccordancewithwhatobservedintheBMLin−mapand more, by comparing branch-specific gene signatures, we could
the highest level of similarity was detected with respect to the identify that the vast majority of gene orthologous in the ery-
CD135− progenitors with knownmegakaryo–erythroid potential throid branch were equivalently expressed in human and mouse
4 NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications
a LIN-CD34+CD164+
MNC
b c d
Meg P Ly N 3 2 2 2 8 4 20 1 14 4 2 13
15 5 3
10
12
6 9 11
8
7
e
f
ecnaci)feinrgoicss g-zn(ilpuoC
ecnaci)feinrgoicss g-zn(ilpuoC
M DC Ly 16 BaP 12 Meg 8
E 4 0 E
E
40
M,N 35 30 Ly,DC 2 2 5 0 15
10 5 0 CD,yL N,M E,Meg, BaP
EMegBaPLyDCMGN
,geM,E PaB
Merge sig.
MegBaPLyDCM N couplings
geM PaB yL CD M N DC
M
BaP
E
N
CD99 GATA2
2 2.0 3
GATA2
6 11
6 9 12
12
9
11
Sorted
HSPC
Sor L te in d
-CD34/CD164
Projection
noisserpxe
dezilamron
2goL
noisserpxe
dezilamron
2goL
noisserpxe
dezilamron
2goL
noisserpxe
dezilamron
2goL
105 105 105 105 105 105
104 104 104 104 104 104
103 103 103 103 103 103
0 0 0 0 0
–103 0 –103 –103 –103 –103
–103 0 103 104 105 0 103 104 105 –103 0 103 104 105 –103 0 103 104 105 –103 0103 104 105 –103 0 103 104 105
CD71
Groups Diff. expr.genes Transcription factors Groups Diff. expr.genes Transcription factors
ENO1 PBX1 IRF8 SATB1 RUNX2
I E G N L O L1 1 14 3 14
N G S A A T P P M 1 D N L H 1 1 1.5 2 15 2 15
SMIM24 1.0 3
SPINK2
GA S T E A L 2 L 0.5 1
PBX1
SOD2 0.0 0
1 0 1 0 1 1 0 1 0 1
4 GATA1 KLF1 1.5 IRF8 JUNB GFI1
3
1.0
2
0.5
1
0 0.0
1 0 1 0 1 1 0 1 0 1
Pseudotime Pseudotime Pseudotime Pseudotime
HSC MPP MLP
PreB/NK MEP CMP GMP
NIL
461DC
NIL
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
LIN-CD34lowCD164high LIN-CD34-CD164high LIN-CD34-CD164low
LIN–
CD34 CD71
Fig.2HumanLin−compartmentinvestigationbymeansofCD34/CD164fractionating.aGatingstrategyfortheFACSsortingoffoursubsetsinsidethe
Lin—fractionofahealthydonorBM,accordingtoCD34andCD164expression(leftpanels).RelativecontributionofCD71+progenitorsisshowninthe
rightpanels.bSPRINGplotofthefourLin−CD34/CD164subsetssingle-celltranscriptomes.Eachpointisonecell.Labelsattheedgesrepresentthe
transcriptionalstatesassociatedtoearlylineagecommitment(P,earlyprogenitorcells;Meg,megakaryocytes;E,erythroidcells;BaP,basophilprogenitors;
N,neutrophils;M,monocytes;DC,dendriticcells;Ly-T/B/NK,lymphoidT/B/NKcells).Colorlegendasina.Geneexpressionmapsareavailablein
SupplementaryFig.4.cPredictedhierarchybasedontwostepsPBA.dClassificationofindividualcellsintohomogenoustranscriptionalgroupsnumbered
from1to15,basedoninferredprincipaltrajectories.Solidlinesshowresultsbasedonfinalconvergediteration(SupplementaryFig.3bfordetails).Dashed
linesaddedmanuallytohighlightapotentialadditionaltrajectorynotpresentinfinaliterationandinferredbyvisualinspection(DC-M).eGenedynamics
associatedtobranchingandfatedecisions.Plotsontheleft,branchingandgroups;mirrorheatmaps,expressionofstatisticallysignificantgenes
differentiallyexpressedalongeachbranchpseudotime(LRTadjustedpvalue<0.05).Plotsontheright,aselectionofthreetranscriptionfactors
differentiallyexpressedalongeachbranch(LRTadjustedpvalue<0.05).fProjectionofthetranscriptionalstatesofthesevenHSPCsontotheLin−CD34/
CD164map
NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications 5
a b Bone marrow MNC
Ficoll
c d
100
71.7%
sc-RNA
similarity
HSC
MPP
CMP
GMP
PreBNK
MEP
e f
CD135– CD135+
100 My 25 Mk 150 Baso 30 My 20 Mk 30 Baso
* *
20 15
100 20 20
15
10
10 * 50 10 10
5
5
0 0 0 0 0
C
D135–
C
D135+
C
D135–
C
D135+
C
D135–
C
D135+
g h
(Fig. 4b). Recently, we showed that erythroid progenitors in the in humans. In this regard, our data also confirm and
mousecanbeclassifiedasearly,whichuniquelygiverisetoburst- expand the information on the divergence of human and mouse
forming units (BFU-E) and are marked by Trib2; and as com- erythropoiesis31 (Fig. 4c). Of note, when analyzing the
mitted, which give rise to colony-forming units (CFU-E) and human–mouse orthologous that are differently expressed along
expressCar2.Notably,weseethesameprogressionfromTRIB2- the erythroid branch, we discovered that the most significant
expressing to CA2-expressing erythroid progenitors (Fig. 4c), distinction is the expression of genes involved in the molecular
suggesting the existence of the same two precursors subclasses apparatussupportingproteintranslation(SupplementaryFig.10).
esaercni
dloF
esaercni
dloF
esaercni
dloF
CS
morf
seinoloc
fo
#
CS
morf
seinoloc
fo
#
CS
morf
seinoloc
fo
#
80
60
40
20
0
A-CSS 41DC AIRecF
On SSC-Alow On CD14–CD15– On CD14–CD15– CD135–
CD15 CCR3 IL5RA Baso diff.
FceRIA-
CD14+ Baso Baso
SSC-Alow CD15+
FceRIA-
CD14+ Baso Baso
CD15+
FceRIA-
Baso CD14+ Baso
CD15+
FceRIA-
Baso CD14+ Baso
CD15+
sllec
wol
A-CSS
fo
%
sllec
wol
A-CSS
fo
%
sllec
wol
A-CSS
fo %
CD135+
FSC-A My diff.
250 K 105 105 100 30 Baso Baso
104 104 80 *
60
103 103 40 20
0 0 20
0
0 103 104 105 0 103 104 105 –103 0 103 104 105 10
105 105 100
104 104 80 0
103 103 6 4 0 0 30 CD14+ CD14+
0 0 20 *
0 20
0 103 104 105 0 103 104 105 –103 0 103 104 105
105 105 100 10
80 104 104
60
103 103 40 0
0 0 20 60 CD15+ CD15+
0
0 103 104 105 0 103 104 105 –103 0 103 104 105
105 105 100 40
104 104 80
103 103 6 4 0 0 20
0 20 0
0 0
0 103 104 105 0 103 104 105 –103 0 103 104 105 – + – +
–531DC
Baso diff.
+531DC
–531DC
+531DC
C
D135–
C
D135+
GMP
CMP
CD10-CD45RA+
MEP
PREB/NK ETP
MLP
MPP
HSC
5 10 15 5 10 15 5 10 15
Time (days) Time (days) Time (days)
200 K
150 K
100 K
50 K
0
0 50 K100 K150 K200 K250 K
250 K
200 K
150 K 100 K
50 K SSC-Alow
0
0 50 K100 K150 K200 K250 K
250 K
200 K
150 K
100 K
50 K SSC-Alow
0
0 50 K100 K150 K200 K250 K
My diff.
250 K
200 K
150 K 100 K
50 K SSC-Alow
0
0 50 K100 K150 K200 K250 K
sllec
fo
%
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
CD34+ cells
Sor L t i e n d
-CD34/CD164 Li
C
n
D
-C
1
D
3
3
5
4
–
+
Sorted
HSPC
e M nr a ic g h n m et e ic nt FACS-sorting
L
C
in
D
-C
1
D
3
3
5
4
+
+
Growth curves
Projection
FLT3+
Im
S
m
in
u
g
n
le
o p
ce
h
l
e
l
n
a
o
s
t
s
y
a
p
y
in
s
g
(CD135+)
80
60
40
FLT3– 20
(CD135–) 15
10
5
0
6 NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications
Fig.3CellfateanalysesofLin−CD34+CD135−cellssupporttheMEP-associatedoriginofbasophilprogenitors.aProjectionofthetranscriptionalprofile
ofcellsbelongingtogroup9inLin−CD34/CD164datasetontosortedHSPCsmap.Piechartonthebottomrepresentstheimmunophenotipic
characteristicforHSPCcellsidentifiedasmostsimilar.bExperimentaldesign.Lin−CD34+CD135−andLin−CD34+CD135+populationsweresorted
fromtheBMCD34+cellsofthreehealthydonorsandtheirlineagepotentialwasinvestigatedthroughinvitrofunctionalassays.cSpatialdistribution
estimatedbyusingatwo-dimensionalkerneldensityestimatorforcellexhibiting:topgraph,highexpression(atRNAlevel)ofFLT3gene(normalized
expression>0.9);bottomgraph,noexpressionofFLT3gene(normalizedexpression=0).dBargraphshowingthecontentofHSPCsinCD135−and
CD135+fractions.Valuesareproportionsestimates±SE,estimatedusingmethodofmomentsandDirichlet-Multinomialmodel.Hypothesistestinghas
beenperformedbymeansofindependentsamples,heteroscedastic,two-tailedStudent’sttest.DetailsareprovidedinSupplementaryTable3.eGrowth
curvesfromthreedifferentcultureconditions.My,Myeloiddifferentiatingculture;Mk,Megakaryocytedifferentiationculture;Baso,Basophildifferentiation
culture.Valuesaremedian±error.Statisticsbyindependentsamples,two-tailedStudent’sttestforeachtimepointconsideredindependentlyfromthe
others(*p<0.05).fSingle-cell(SC)assayshowingthetotalnumberofcoloniesobtainedfromCD135−andCD135+fractionsattheendofthethree
differentcultureconditions.Shownaremedian±error.Statisticsbyindependentsamples,two-tailedStudent’sttest(*p<0.05).gFACSanalysisofbona
fideBasophils(Baso)definedasCD14−CD15−FceRIA+CCR3+IL5RA+cellsonCD135−andCD135+populationsuponbasophil(upperpanel)and
myeloid(lowerpanel)differentiationculture.FceRIA−pickindicatesthenegativecontrol.hBargraphssummarizingthecytometricanalysisdescribedin
g.ShownarethepercentageofBaso,CD14+cellsandCD15+cellsonCD135−andCD135+populationsfromthebasophil(leftpanel)andmyeloid(right
panel)differentiationculture.Valuesaremedian±error.Statisticsbyindependentsamples,two-tailedStudent’sttest(*p<0.05)
a b c
Human
Meg Ly
BE
9 4 14 DC
1
15
2/5
3/13 12
6 MPP 10
MPP
11
E B/EMeg LyDC M G
E G
This difference in the expression of the machinery of ribosome transplantation, CD38+ myeloid progenitor cells (CMP and
biogenesis during erythropoiesis could explain why mouse GMP) must be provided separately to support short-term gran-
models of red blood cells disorders caused by a partial loss of ulopoiesis in conditioned neutropenic patients33,34. Third, we
ribosomal function, such as Diamond–Blackfan anemia, are not showherethatexpressionofCD38israpidlylostincultureupon
able to recapitulate the human phenotype32. cytokine exposure (Supplementary Fig. 11), meaning that the
viability and composition of early progenitors cannot be verified
in transplantation products after in vitro expansion using the
Exploring CD164 as amarker of earlyhuman HSPC. We next CD38− cytometric gating. We propose here that the cell surface
asked whether we could take advantage of the data to rationally antigen CD164 could be used to overcome all three of these
select a cell surface marker to fractionate human HSPCs for shortcomings.
transplantation and gene therapy (Fig. 5). To date, the CD38 TheCD164geneencodesforamembrane-associatedsialomu-
antigen has served to negatively enrich for the primitive pro- cin, endolyn, whose function is that of an adhesion receptor35.
genitors for transplantation. Yet this marker suffers three short- The few investigations on the membrane expression of this
comingsandthusmotivated ustosearchforanalternativefrom protein in the human blood cell population suggest that CD164
thedata.First,thereisnoconsensusonthegatingstrategytobe could have a role in early erythropoiesis, stem cell maintenance
used for CD38 expression to define CD38− primitive cells33, andhomingcapacity36,37.AnearlystudyshowedthattheCD164
resulting in variable efficiencies of progenitor cell enrichment. population is enriched in CD34+CD38− progenitors38, but
Second, in strategies proposing a CD38− cells selection for following these investigations the use of CD164 for defining
seneG
6 4
3
2
1
0
1.0
1 0 0 0
Pseudotime
.rpxe
.mron
2gol
esuoM
.rpxe
.mron
2gol
esuoM
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
Mouse
CA2
Car2 5 TRIB2
Trib2
M 4
3
2
1
0
2.5
2.0 0.8
1.5 0.6
1.0 0.4
0.5 0.2
CD47 ZFPM1
0.0 Cd47 Zfpm1 0.0
1 1
Pseudotime Pseudotime
Fig.4HumanLin−CD34/CD164versusmouseKit+transcriptomemapandgeneexpressiondynamicsanalysis.aClassificationofindividualcellsinto11
homogenoustranscriptionalgroups,basedoninferredprincipaltrajectoriesonmouseKit+transcriptomedata(SupplementaryFig.3cfordetails).Group
labelsandcolorshavebeensettohighlightsimilaritieswithLin−CD34/CD164fractionatingmap.Solidlinesshowresultsbasedonfinalconverged
iteration(SupplementaryFig.3cfordetails).Dashedlinesaddedmanuallytohighlightapotentialadditionaltrajectorynotpresentinfinaliterationand
suggestedbyPBAanalysisreportedinthemiddle(DC-M).MPP,MultiPotentprogenitorcells;Meg,megakaryocytes;BE,baso/eosinophils;E,erythroid
cells;Ly,lymphoidcells;DC,dendriticcells;M,monocytes;G,granulocytes.bComparisonofhumanandmousetranscriptionalstatesduring
erythropoiesis.Upperpanels,schemesofthecomparison.Mirrorheatmaps,expressionofthe721orthologousgenesselectivelyexpressedalongthe
humanandmouseerythroiddifferentiation(LRTadjustedpvalue<0.05).cRepresentativecomparabledynamicsoftheorthologuesTRIB2/Trib2and
CA2/Car2reportedinTusietal.24vsdivergentdynamicsoftheorthologuesCD47/Cd47andZFPM1/Zfpm1reportedinPisheshaetal.31
NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications 7
In vitro In vitro
a (Fig. 5 f–h) (Fig. 5 i–k)
Bone marrow MNC CD34+ cells CD34+
CD34+CD164high
Ficoll
e
M
nr
a
ic
g
h
n
m
et
e
ic
nt
CD34+CD164low
Immunophenotyping FACS-sorting
b (Fig. 5 c–e)
c d e
f g
h i k
j
primitive progenitors was abandoned. Up until now, the CD164 emerged as the gene whose expression displayed the
expression of CD164 inside the currently defined HSPC most-pronounced difference in early vs late progenitors. By
subpopulations and upon in vitro manipulation of CD34+ cells, contrast, neither CD38 nor CD90 (common marker used for
were not appreciated. identification of primitive HSPCs) stood out as genes whose
Interrogating scRNA-Seq data for enrichment of transcripts transcripts strongly discriminate between early vs late stages of
encoding for surface antigens in early progenitors (Fig. 1g), bloodcellfatecommitment.AlthoughmRNAabundancesdonot
43DC
Functional
assays
105 Low High
104
103
0
0 103 104 105
hgiH
woL
A-CSS
CD38+
CD34+ LIN– CD38– CD7– CD10–
CD164 LIN CD34 CD45RA CD7 CD45RA CD45RA
83DC 09DC A-CSS 01DC A-CSS
250 K 105 105 250 K 250 K
2 1 0 5 0 0 K K 104 104 2 1 0 5 0 0 K K 2 1 0 5 0 0 K K
100 K 103 103 100 K 100 K
50 K 0 0 50 K 50 K 0 0 103 104 105 0 103 104 105 0 103 104 105 0 0 103 104 105 0 103 104 105 0 0 103 104 105
250 K 105 105 250 K 250 K
2 1 0 5 0 0 K K 104 104 2 1 0 5 0 0 K K 2 1 0 5 0 0 K K
100 K 103 103 100 K 100 K
50 K 0 0 50 K 50 K
0 0 103 104 105 0 103 104 105 0 103 104 105 0 0 103 104 105 0 103 104 105 0 0 103 104 105
105 Low
CD164
43DC
105
104
103
0
105
104
103
0
CD164high LIN– HSC PREB/NK CD164high
CD164low LIN+ CD38– CD90+ M M P LP P C G M M P P /MEP CD164low
ETP LIN+
120
100
CD164high BFU-E CD164high CD164low CD34+
CD164low CFU-E
High 400 * CD34+ CFU-GM
104
103 300
0
–103
–103 0 103 104 105
2.5×105 CD164high
2.5×105 CD164low BM composition
CD164high CD164low CD34+ 5.0×105 CD34+ CD3+
CD19+
Mk My PB hCD45+ BM hCD45+ C C D D 3 4 3 1 + + /CD13+
*
CS morf
seinoloc
fo #
sCFC
fo #
CS morf
seinoloc
fo #
sCFC
fo #
sllec
evil
fo
%
sllec
evil
fo
%
esaercni
dloF
sllec
+54DCh
fo
%
sllec
–54DCh
fo
%
Expansion Mk My
20
200 15
200 10
5 *** *
*
***
***
***
**
***
80
60
40
20
0
250 20 100
80 15
150
60
10 100 40
100
50 5
20
0 0
0 0 0
0 5 10 15 0 5 10 15 0 5 10 15
Time (days)
Transplant Bleeding Sacrifice
0 3–14 16 weeks
GpA+
30 30 40 100 100 50
30
80 80 40 20 20 20
10 60 60 30
40 40 20
10 10 0.3
0.2 20 20 10
0.1
0 0 0.1 0 0 0 0 3 5 7 10 14
Weeks after transplant
sllec
+43DC
fo
%
120
100
80
60
40
20
0
sllec fo
%
sllec fo
%
sllec fo
%
sllec fo
%
**
*** ** 20 ** ** 20 * * 120 CD34+CD38–
100
80
15 15 60
40 10 10 2 2 0 0
15
5 5 10
5
0 0 0
HD
BM CD164high CD164low CD34+ CD164high CD164low CD34+ CD164high CD164low CD34+ CD164high CD164low CD34+
CD164high CD164low CD34+ CD164high CD164low CD34+
CD164hig
C
h D164low CD34+ CD164hig
C
h D164low CD34+ CD164hi
C
gh D164low CD34+ CD164high CD164low CD34+
CD16 C
4h
D
ig
1
h 64lo
C
w D34+
dettimmoC
evitimirP
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
HSC MPP MLP CD34+CD38+
ETP PREB/NK MEP/CMP GMP
8 NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
Fig.5Immunophenotypingandinvitro/invivofunctionalassaysofCD164expressingsubsetsinBMCD34+cells.aExperimentaldesign.bRepresentative
FACSplotsshowingthecontributionofLin−/+cellsandHSPCsubsetsinCD164highandCD164lowfractionsofCD34+cells.cPercentageofCD164high
andCD164lowfractionsinCD34+cells.ShownareMean±SDfromnineindependentBM.dBargraphsshowingthecontentofLin−/+,CD38−,CD90+
cellsandHSPCsinCD164highandCD164lowfractions,andinCD34+cells.ValuesareMean±SDfromnineindependentBM.Statisticsbyindependent
samples,heteroscedastic,two-tailedStudent’sttest(*p<0.05,**p<0.0005,***p<0.0001).FortheHSPCsbargraph,plottedvaluesareproportion
estimates±SE,estimatedusingmethodofmomentsandDirichlet-Multinomialmodel.DetailsareprovidedinSupplementaryTable4.ePiechart
distributionofCD164highandCD164lowfractionsonHSPCsubsetsfromnineindependentBM.fBargraphsshowingthetotalnumber(left)andtypeof
colonies(right)scoredatday14inamethylcellulose-basedcolony-formingunit(CFU)assay.Topleft,sortinggatingstrategy(CFCs,colony-formingcells,
BFU-E,burst-formingunit-erythroidcells,CFU-E,colony-formingunit-erythroidcells,CFU-GM,colony-formingunit-granulocyte/macrophages).Shownare
mean±SDfromsixindependentBM.Statisticsbyindependentsamples,heteroscedastic,two-tailedStudent’sttest(*p<0.05).gGrowthcurvesfrom
threedifferentcultureconditions.Mk,Megakaryocyte;My,Myeloid.Valuesaremean±SDfromnineindependentBM.Statisticsbyindependentsamples,
heteroscedastic,two-tailedStudent’sttest(*p<0.05,**p<0.0005,***p<0.0001).hSingle-cell(SC)assayshowingthetotalnumberofcolonies
obtainedfromeachpopulationintheMk(left)andMy(right)differentiatingculture.Shownaremedian±errorfromthreeindependentBM.Statisticsby
independentsamples,two-tailedStudent’sttest(*p<0.01).iExperimentaldesign.SortedCD164highandCD164lowpopulationsweretransplantedin
NBSGWmiceeachatthedoseof2.5×105cells/mouse.InordertoreflecttherealproportionsinthehumanBM,immunomagnetic-selectedCD34+cells
weretransplantedatthedoseof5.0×105cells/mouse.Thehumanengraftmentwasevaluatedinthemurineperipheralbloodatdifferenttimepoints,and
inBMandspleenat16weeksposttransplant.jHumanCD45+cellengraftmentinmurinePB(left;CD164high,n=3;CD164low,n=3;CD34+,n=4mice)
andBM(right;CD164high,n=3;CD164low,n=2;CD34+,n=4mice).kRelativecontributionofhumancellpopulationsinsidethehCD45+andhCD45−
compartmentsinmurineBM.(CD164high,n=3;CD164low,n=2;CD34+,n=4mice)
necessarily correlate with protein abundance, we found that the differentiating conditions (Fig. 5f–h). Cytometric analysis of dif-
CD34+ population can be split into two sub-fractions on the ferentiation states after culture confirmed the more primitive
basisoftwoclearlydistinctlevelsofCD164transcriptabundances natureofCD34+CD164highcells(SupplementaryFigs.12,15).At
(Fig. 1h), which tracked fractionation by CD164 antibody-based last,theCD34+CD164highcellsexpandedmorerapidlyinculture
sorting.TheCD164RNAisselectivelyexpressedathighlevelnot conditions used in clinical gene therapy for in vitro stem cell
only in CD38− multipotent progenitors (as previous studies enrichment prior to autologous transplantation39 (Fig. 5g).
suggested) but also in CD90+ precursors (which in humans Importantly, in this context we observed that CD164 allows, as
comprise both HSC and early CMP), in the most primitive comparedwithCD38,amorerobustcytometricestimationofthe
fractionofMEPand toalesser extent,in MLP(Fig.1g).During primitive progenitor content upon in vitro manipulation of
later stages of commitment, the CD164 mRNA and protein CD34+ cells, as its loss of expression coincides with the pro-
surface expressions levels begin to diverge (e.g., in the gressive cell differentiation upon cytokine exposure (Supplemen-
CD34–CD164high erythroid-committed cells). taryFig.11).Thisisamajoradvantageovertheuseoftheclassical
CD38 marker whose expression dynamics were instead not con-
sistentwiththeexpectedphenotypechangesofdifferentiatingcells.
CD164 selects an alternative CD34+ cell product. To investi- Anotherkeysurfacemarkerusedfortheidentificationofstem/
gatetheutilityofCD164roleinfractionatingearlyhematopoietic multipotent vs committed progenitor is CD9040. We thus
progenitors, we performed a series of immunophenotypic and conducted additional differentiation assays on three healthy
functional assays on human BM CD34+ cells (Fig. 5a). In line donors comparing the performance of FACS-sorted CD34+
with scRNA-Seq results, a cytometric analysis combining anti- CD90+ cells to CD34+CD164high population. The results
CD164 antibody with the other classical HSPCs markers, con- displayed in Supplementary Figs. 16 and 17 show that the
firmed that the CD34+ population contains two clearly distinct CD34+CD164high fraction has a much higher discriminatory
fractionsofCD164highandCD164low-expressingcells,thefirstof potential,ascomparedwiththeCD34+CD90+selection,forcells
which was highly enriched in cells with cytometric markers of capable of growing in myeloid- and MK-differentiating condi-
primitive progenitors, MEPs and early CMPs and, notably, was tions and for clonogenic progenitors (Supplementary Figs. 16g,
almost entirely depleted of pre-B-NK and Lin+ cells (Fig. 5b–e 17c). Furthermore, as in the case of CD38, the CD90 marker
and Supplementary Fig. 12a). Importantly, we could show that presented inconsistent expression dynamics in culture, being
this differential composition between CD164high and CD164low upregulated (and not downregulated) upon cell differentiation
populations in the human BM is not merely owing to the dif- (Supplementary Figs. 18–20), again pointing to the superior
ferences in the relative CD34 surface expression or in the Lin+ performance of CD164 in allowing a more reliable evaluation of
cellcontent.Indeed,weobtainedthesameresultsuponanalyzing the stem cell content of in vitro manipulated CD34+ cell
CD34+ cells from G-CSF- and plerixafor-mobilized peripheral products (Supplementary Fig. 21).
blood where the CD34 expression is uniform in both CD164high We have shown above that the CD34+CD164high population
and CD164low cell fractions and where the contribution of the contains both multipotent progenitors and early CMP. On the
Lin+ population is negligible (Supplementary Figs. 13, 14). To basisofthemodelofhematopoieticreconstitutionemergingfrom
date,theliteraturereportsonlytheresultsofaclonogenicassayas our recent clonal tracking data in humans6,41, we reasoned that
test of the in vitro differentiation potential of CD34+CD164+ the CD34+CD164high fraction might constitute a suitable self-
cells38. To integrate these data, we here conducted a set of sufficient cell product for transplantation that would not require
functional tests on FACS-sorted CD34+CD164high and CD34+ the co-infusion of other cells to support recovery from
CD164lowcellsfromtheBMofseveralhealthydonors(Fig.5f–h). neutropenia and early myelopoiesis. To test this hypothesis, we
The CD34+CD164high population displayed a superior in vitro sorted and transplanted CD34+CD164high vs CD34+CD164low
differentiation potential as compared with the CD34+CD164low populations into NOD.Cg-KitW-41JTyr + PrkdcscidIl2rgtm1Wjl/
fractionandeventothetotalCD34+population,showinghigher ThomJ (NBSGW) mice (Fig. 5i–k, Supplementary Fig. 22). The
rate of colonies generation (confirming previously published results confirmed that the CD34+CD164high cell product is
results38)andofexpansionnotonlyinMyeloidbutalsoinMK- capable of sustaining both the early and late phases of
NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications 9
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
hematopoietic reconstitution, whereas the CD34+CD164low selectionstrategiesthatwouldlikelyrequireco-transplantationof
population did nothave a role in blood cell production at either committed precursors to sustain early myelopoiesis33,34. Before
stage, making its use in transplantation virtually dispensable. suggesting its use in the clinic, further investigations are under-
Remarkably and in line with this observation, the dynamics and wayinourlaboratorytotestthesafetyandefficacyperformance
size of human lymphoid and myeloid cells output in the mice of the CD34+CD164high population upon different in vitro
infused with FACS-sorted CD34+CD164high cells was compar- manipulation protocols and after transplantation in multiple
able to the mice infused with CD34+ cells, despite the latter recipient animal models.
receiving twice the amount of cells. Overall, our data clearly Despite the high-resolution achieved upon our scRNA profil-
highlight the biological relevance of the CD164 gene in early ingitshouldberemindedthatsuchanalyticalmethodgeneratesa
haematopoiesis, reviving the use of this marker for the study of static snapshot of the transcriptional landscape and cannot pro-
humanHSPCandsettingthebasisforexploringthepotentialuse vide, as such, conclusive information on the dynamics occurring
of the CD34+CD164high fraction in clinical transplantation and alongcellstatetransitions.Ongoingandfutureeffortstowardfate
gene therapy, where there is a high demand for reducing the mappinginvitroandinvivowillberequiredtoconfirmorrefine
production costs for genetic engineering. theinferencesofourstudy.Inthisregard,ourresultsinhumans
align with the ones of Tusi et al. in the mouse in supporting the
hypothesis of an early separation of cells with erythroid vs neu-
Discussion trophil potential, a concept that would challenge some earlier
We here report the generation of high-resolution scRNA maps of deductions made in other studies of murine hematopoietic cell
human hematopoietic cell fate commitment and the interrogation dynamics8,42.
of our transcriptional profiling for conducting investigations into In conclusion, we show here that the transcriptional informa-
thebasicbiologyofearlyhematopoiesis.Ourfractionationstrategy tion represented in our hierarchy fosters basic investigation into
of the BM Lin− cells extended outside the CD34+ compartment human hematopoiesis and enables the identification of human
constitutesamainadvanceoverpreviousstudiesinthatallowedus HSPCs subsets potentially suitable for clinical application.
to preserve high resolution at both primitive and lineage-primed
progenitors level. The results of the in silico, in vitro, and in vivo
Methods
analyses reported in this work strongly suggests that human hae-
Cellpreparation.BMsampleswerecollectedfromadulthealthydonorsatChil-
matopoiesisdevelopsalongearlycellfatebifurcationsoccurringina dren’sHospitalinBostonwiththeapprovaloftheCommitteeonClinicalInves-
continuum of states forminga hierarchical-like structure. tigationsChildren’sHospitalBostonandconsentfromthesubjectsunderthe
Our investigations into the origin of the basophil branch protocol#09-04-0167.Mononuclearcells(MNCs)wereisolatedusingFicoll-
suggestthataveryearlyprimingofCD38−progenitorsmightbe Hypaquegradientseparation(Lymphoprep,STEMCELLTechnologies).CD34+
cellswerepurifiedfromMNCswiththehumananti-CD34MicroBeadsIsolation
in place toward either the MK/erythroid/basophil or the lym- Kit(MiltenyiBiotec)accordingtothemanufacturer’sspecificationsorwerepur-
phoid/granulo/DC/monocytecommitmentandthatthismightbe chasedfromcommercialsources(AllCells).
dependent on the expression of the CD135 surface marker. This
observation calls for further studies into the potential hetero-
geneouscompositionoftheCD34+CD38−compartment.Inthis C
fr
e
o
l
m
ls
t
o
h
r
e
ti
C
ng
D3
a
4
n
+
di
f
m
ra
m
ct
u
io
n
n
op
of
h
a
en
h
o
e
t
a
y
lt
p
h
i
y
ng
d
.
o
S
n
e
o
v
r
en
BM
HS
c
P
el
C
ls
s
t
u
h
b
ro
p
u
o
g
p
h
ul
a
at
t
i
w
on
o
s
-s
w
te
e
p
re
fo
p
u
u
r
r
-
i
w
fie
a
d
y
regard,wewouldliketoraiseawarenessonthearbitrarynatureof sortingusingFACSAriaII(BDBiosciences)andprocessedtogeneratethetran-
thecurrentstrategiesforthecytofluorimetricidentificationofthe scriptomenetworkinFig.1.Thefollowingcombinationsofcellsurfacemarkers
CD38− compartment. Indeed, despite using a very stringent wereusedtoidentifyandseparatetheHSPCsubsets.Hematopoieticstemcells
CD38− sorting strategy we still observed an overlap of tran- − (H C S D C 3 ): 4 L + i C n− D C 38 D − 3 C 4+ D C 90 D − 3 C 8- D C 4 D 5 9 R 0 A + − C ; D m 4 u 5 l R ti A -l - y ; m m p u h l o ti i p d o p te r n o t ge p n r i o t g o e r n s i ( t M or L s P (M ): PP):Lin
scriptionalstatesbetweenCD38−HSC/MPPandCD38+CMP/ Lin−CD34+CD38−CD90−CD45RA+;pre-Blymphocytes/naturalkillercells
MEP(SupplementaryFig.2a).Thisisowingtothecontinuumof (PREB/NK):Lin−CD34+CD38+CD7−CD10+;MEP:Lin−CD34+CD38+CD7−
CD38 expression, which does not provide a clear-cut way to
CD10−CD135−CD45RA−;CMP:Lin−CD34+CD38+CD7−CD10−CD135+
CD45RA−;GMP:Lin−CD34+CD38+CD7−CD10−CD135−CD45RA+.
isolate with high purity primitive progenitors. We therefore
ForthegenerationofthetranscriptomenetworkinFig.2,fourcellfractions
suggest that, upon validating potential early lineage priming of werepurifiedfromahealthydonorBMMNCsthroughafour-waysortingusing
human HSC or MPP, one should commit to the use of an thefollowingcombinationsofcellsurfacemarkers:Lin−CD34+CD164+;Lin
extremelyconservativeCD38−gateinordertoobtainhighpurity −CD34lowCD164high;Lin−CD34–CD164high;Lin−CD34–CD164low.CD71was
of bona fide multipotent progenitors. includedtoidentifyerythroidprogenitors.
Forinvitrofunctionalassays,Lin−CD34+CD135−andLin−CD34+CD135+
Our in vitro and in vivo data support the hypothesis that the fractionswerepurifiedfromtheCD34+cellsofthreeindependentBMthrougha
CD34+CD164highpopulationmighthaveaclinicalrelevancefor two-waysorting.ThecellsubsetsCD34+CD164highandCD34+CD164lowwere
transplantation purposes. Among the advantages of using such FACS-sortedfromtheCD34+cellsofnineindependentBM.Ofthese,threeBM
fraction of CD34+ cells in the clinic we would like to underline werealsousedtopurifyCD34+CD90+andCD34+CD90−cells.
thefollowing:(1)itexcludesPre-BprecursorsandCD34+Lin+
sort
F
e
o
d
r
a
i
n
n
d
vi
p
v
u
o
ri
s
fi
tu
ed
die
fr
s
o
,
m
CD
a
3
p
4
o
+
o
C
l
D
of
16
B
4
M
hig
C
h
D
an
3
d
4+
CD
ce
3
ll
4
s
+
fr
C
o
D
m
16
tw
4l
o
ow
ad
ce
d
l
i
l
t
s
io
w
n
e
a
r
l
e
h
F
e
A
al
C
th
S
y
-
cells(inlargepartcomposedbyCD34+CD19+cells),providing
donors.
a system worth exploring for the potential exclusion of residual ImmunophenotypingwasperformedonBMCD34+cellslabeledwithCD135
leukemic cells with early B-cell commitment in transplantation orCD164incombinationwithHSPCsubsetsmarkersbyusingLSRFortessa(BD
Biosciences).CD15andCD19wereincludedtoidentifythelineagepositivecells.
products for B-cell leukemia; (2) it could reduce of about a half
FlowcytometrydatawereanalyzedwithFlowJo10.2(TreeStar).Theantibodies
the number of target cells needed for genetic engineering in wereasfollows:CD34PB(1:40,#343512),CD38PE/Cy5(1:40,#303508),CD90
clinical gene therapy, in turn reducing of 50% the costs for APC(1:33,#328114),CD10PE/Cy7(1:33,#312214),CD135PE(1:10,#313306),
manufacturing of gene transfer/gene editing platforms. Notably, LinBV510(1:10,#348807),CD15BV510(1:50,#323028),CD164FITC(1:20,
#324806clone67D2),CD164PE(1:10,#324808clone67D2),CD71PerCP/Cy5.5
because it combines only two surface markers (CD34 and
(1:20,#334114),CD41APC(1:20,#303710),CD19PE/Cy7(1:20,#302216),all
CD164), this fractionation method allows designing strategies
Biolegend.CD45RAAPC-H7(1:17,#560674),CD7AF700(1:20,#561603),CD15
based on magnetic beads selection, a more suitable and scalable FITC(1:20,#555401),CD15PE(1:10,#555402),allBDBiosciences.Glycophorin
approachfortheclinicalarenathanFACSsorting.Wealsoshow AAPC-Vio770(1:11,#130-100-268),MiltenyiBiotec.
here that this fraction might constitute a self-sufficient product Tocharacterizethebasophilscontributioninthehumanperipheralbloodand
uponinvitrodifferentiation,thegatingstrategyreportedinSupplementaryFig.9a
capableofsustainingbothearlyandlatephasesofhematopoietic
hasbeensetusingthefollowingantibodies:CD34PB(1:40,#343512),FceRIAAPC
reconstitution41, another advantage over the currently proposed (1:10,#334612),CD14AF700(1:10,#367114),CD19PE/Cy7(1:20,#302216),
10 NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
CD15FITC(1:20,#555401),CCR3PerCP/Cy5.5(1:10,#310718),allBiolegend. Cellfilteringanddatanormalization.EachlibraryofsortedHSPCsorCD34/
IL5RAPE(1:10,#555902),BDBiosciences. CD164cellswasprocessedaccordingtothefollowingprocedure.Uponinspection
Toevaluatethehumancellengraftmentinthemurineperipheralblood,BM ofthehistogramsreportingthetotalreadspercell,barcodeswereinitiallyfiltered
andspleentheantibodieswereasfollows:CD33PE(1:40,#561816),CD13PE accordingtoacustomizedthresholdinordertoincludeonlythemostabundant
(1:40,#555394),CD3V500(1:20,#561416),CD19PE/Cy7(1:80,#557835), ones(transcriptcountsthresholdusedforthesortedHSPC:HSC,1000;CMP,800;
mCD45APC(1:100,#561018),mCD45PE(1:100,#553081),7-AAD(1:12, MEP,1000;GMP,1000;Pre-B-NK,800;MLP,2000;MPP,2000;transcriptcounts
#559925),allBDBiosciences.CD45PB(1:40,#368540)andCD41APC(1:50, thresholdusedforthesortedCD34/CD164cells:Lin−CD164highCD34lowRep
#303710)allBiolegend.GlycophorinAAPC-Vio770(1:22,#130-100-268), (Replicate)1,1000;Lin−CD164highCD34lowRep2,1000;Lin−CD164highCD34-
Miltenyi. Rep1,800;Lin−CD164highCD34-Rep2,800;Lin−CD164highCD34+Rep1,1000;
Lin−CD164highCD34+Rep2,800;Lin−CD164lowCD34-,700).Next,forall
samplesweexcludedthecellswith>25%oftheirtranscriptscomingfrommito-
Invitrofunctionalassays.Fortheinvitrofunctionalassays,sort-purified chondrialgenesasthisisamarkerofstressedordyingcells.Thefinalnumberof
populationsandCD34+cellswereseededinthedifferentcultureconditionswitha
barcodesusedinthedownstreamanalysisissummarizedinSupplementary
startingcellnumberof20,000cells,unlessotherwiseindicated. Table1.Thegeneexpressioncountsofeachcellwerenormalizedusingatotal-
Totestforbasophilpotential,cellswereculturedinIscove'sModified
countnormalizationvariantthatavoidsdistortionfromveryhighlyexpressed
D s n u g u p / l m p b l e l e ) c m c f o o e ' n r s t 3 m ed d e a d w y i i u s th , m w IL ( h I - e M 3 re ( D a 2 s M 0 s n ) u g p c / o p m n le l t ) m a , i I e n L n in - t 5 e g d ( 1 2 o % 0 n n l P y g / / w S m / i G t l) h l , u S I , L C 2 - F 3 0% ( ( 2 2 0 F 0 B n n g S g / / m ( m G l l ) e ) , m G a i n n M d i) - I C L an S -5 F d ( ( 2 5 0 0 g co en u e n s t , s a f s or in ge K Pn le e in ji e n t c a e l (cid:2) . l 4 l 3 i . , S f p ro e m cifi t c h a e lly r , aw we co ca u l n cu ts la x t i e ,j d a ^x s i; f j o , l t l h o e w n s: o ^x rm i;j a ¼ liz x e i d ;j X (cid:2) tr = a X n i s , c i r n ipt
ng/ml)fromday4today14.Cellswerecountedondays7,11,14.Freshmedium whichX i ¼ x i;j andXistheaverageofX i overallcells.Topreventveryhighly
wasaddedasneeded,tokeepthecellconcentrationat0.5×106/mL.Attheendof expressedgenesfromcorrespondinglydecreasingtherelativeexpressionofother
theculture,cellswereanalyzedbyflowcytometryforthebasophilmarkersand genes,weexcludedgenescomprising>5%ofthetotalcountsofanycellwhen
mountedoncytospinpreparationtodefinethepresenceofbasophilsbyGiemsa calculatingX (cid:2) andX
i
.
staining.
MyeloidpotentialwasevaluatedinIMDMmediumcontaining1%P/S/Gluand
10%FBS(Gemini)andsupplementedwithIL-3(60ng/ml),SCF(300ng/ml),IL-6
DatavisualizationandkNNgraphs.Afterfiltering,thedatawereusedtocon-
(60ng/ml)for2weeks.Cellswerecountedondays7,11,14.Freshmediumwas structak-NNgraph,inwhichcellscorrespondtographnodesandedgesconnect
addedasneeded,tokeepthecellconcentrationat1×106/mL.Attheendofthe cellstotheirnearestneighbors.AnindependentkNNgraphwasgeneratedforeach
culture,cellswereanalyzedbyflowcytometryforimmunophenotypingand datasetasfollows.GeneswerefurtherfilteredbyselectingonlygeneswithFano
lineage-positivemarkersCD15andCD19,andforbasophilmarkers.
factor43(measureofdispersion)aboveameandependentthreshold(medianvalue)
Expansionculturewassetupinserum-freeCellGroSCGMmedium(Cell
andrequiringatleastthreeUMIFM(UniqueMolecularIdentifiersFilteredMap-
Genix)containing1%penicillin/streptomycin/glutamine(P/S/Glu,Lonza)and
ped)tobedetectedinatleastthreecells(sortedLin−HSPCs,n=5596genes;
supplementedwithFLT3-L(300ng/ml),IL-3(60ng/ml),SCF(300ng/ml),TPO
sortedLin−CD34/CD164cells,n=7156genes).Expressionvaluesforeachgene
(100ng/ml)for8days.Cellswerecountedondays4and8.Immunophenotyping werestandardizedindependentlybyapplyingZscoretransformation.Unless
andflowcytometricanalysisforlineage-positivemarkersCD15andCD19were otherwisestated,foralltheanalysesandgraphicalrepresentationsthroughoutthe
performedatday4.Allgrowthfactorsandcytokineswerepurchasedfrom paper,zscoreshavebeenusedasameasureofgeneactivity.Fromprevious
Peprotech.
experiments24,wefoundthatcellcycleandribosomalassociatedgenescanhavea
MegakaryocytepotentialwasassessedinStemSpanSFEMIIserum-free
significantimpactonthedefinitionofcellclusteringandoncell-to-celltran-
mediumsupplementedwithStemSpanMegakaryocyteExpansionSupplement
scriptionaldistance.Forthisreason,wedefinedaG2/Mgenesset(UBE2C,
(STEMCELLTechnologies)for2weeks.Cellswerecountedondays7,11,14.Fresh HMGB2,HMGN2,TUBA1B,MKI67,CCNB1,TUBB,TOP2A,TUBB4B)and
mediumwasaddedasneeded,tokeepthecellconcentrationat1×106/mL.
ribosomalgenesset(RPL−andRPS−).WethenconstructedaG2/Manda
ImmunophenotypingandflowcytometricanalysisforCD41,CD71,and ribosomalsignaturescorebysummingtheaveragezscoreofrespectivegenessets
GlycophorinAwereperformedattheendoftheculture. andremovinggenesthatwerehighlycorrelated(Pearsonr>0.2)withthesesig-
Totesttheclonogenicpotentialofsort-purifiedpopulationsandCD34+cells, natures(sortedLin−HSPC,n=117genes;sortedCD34/CD164cells,n=304
single-sortedcellsweredepositedin96-wellplatesindifferentcultureconditions. genes).Finally,weperformeddimensionalityreductionbyprincipalcomponent
Mediumwasaddedatday7andcolonieswerescoredatday14.FromCD34+cells analysis(PCA).KNNgraphswereconstructedbysettingk,numberofneighbors,
andeachfreshlysortedCD164highandCD164lowpopulations,theclonogenic
equaltofour,usingthefirst40principalcomponentsandaEuclideanmetricto
potentialwasalsoassessedbyseeding3500cellswith2.4mlofMethocultmedium measuredistancebetweentranscriptomes.ThekNNgraphswerevisualizedby
(H4434,STEMCELLTechnologies)for2weeks.Erythroid(BFU-EorCFU-E)and meansofaforce-directedlayoutusingthecustominteractivesoftwareinterface
granulocyte–macrophage(GM)colonieswerescoredfromduplicateplateson SPRING25.Thefinallayout,correspondingtoaminimalfree-energyconfiguration,
day14. showedahighdegreeofrobustnesswithrespecttodifferentinitialization(except
forlayoutrotationthatdonotaffectsubsequentanalyses).Nomanualadjustments
wereperformedonthevisualizations.VisualinspectiononSPRINGplotforLin−
Transplantationintohumanizedmousemodel.NOD.Cg-KitW-41JTyr+Prkdcsci- CD34/CD164transcriptomedatasetshowedthepresenceofaclusterofcells(860
dIl2rgtm1Wjl/ThomJ(NBSGW)micewerepurchasedfromtheJacksonLaboratory. barcodes),highlyinterconnectedandverypoorlylinkedtotherestofthelayout.
Allanimalprocedureswereperformedaccordingtoethicalregulationsforanimal Investigatingforthepresenceofaparticulargeneexpressionsignaturechar-
testingandresearch,uponapprovalbytheInstitutionalCareandUseCommittee acterizingthissubpopulation,weobservedhighlevelofexpressionformito-
(IACUC)attheDana-FarberCancerInstitute.Six-week-oldmiceweretransplanted chondrialgenes(MT.CYB,MT.ATP6,MT.ND4,MT.ND1,MT.CO3,MT.ND3).
withhumanHSPCsbytailinjectionwithoutundergoingirradiationorother
Weconcludedthattheseeventshadapeculiartranscriptionalprofileindicatorof
conditioningregimen.Micewererandomizedinthefollowingtransplantation
stressedordyingcells,whichwasnotdetecteduponthededicatedfilteringstepand
groups:sortedpurifiedCD34+CD164high(2.5×105cells/mouse)andCD34 wethereforemanuallyremovedthemfromthefinalkNNgraph.
+CD164low(2.5×105cells/mouse),immunomagnetic-selectedCD34+
(5×105cells/mouse).Foreachsortedpopulation,threemiceweretransplanted
(fourmiceforthewholeCD34+population).Humancellengraftmentwasassessed ProjectionofscRNAdataacrossexperiments.Toprojectsubsetsofcellsfrom
byserialbleedingandimmunophenotypingat3,5,7,10,14weeksposttransplant
onemaptotheother,wefirstneededtodefineacommonlowerdimensionalspace
andinBMandspleenatsacrifice16weeksposttransplant.TheCD34+CD164high tobeusedasreferencetocompareexpressionprofiles,calculatetranscriptional
selectionmethodisunderprovisionalPatentApplicationU.S.SerialNo.:62/737,483 distancesandlocatecellswithanhighdegreeofsimilarityamongthetwomaps.
filedintheUnitedStatesPatentandTrademarkOffice(USPTO). Forthisreason,weidentifiedtheintersectionsetamonggenesusedtogeneratethe
twokNNgraphs(n=5116genes).GiventhatLin−CD34/CD164maprepresentsa
broaderviewonLin−compartmentwithrespecttothesortedLin−HSPCdataset,
InDropsscRNA-Seqanddataanalysis.Single-cellmRNAbarcodingandpre- weperformedPCAonLin−CD34/CD164reducedexpressionmatrixretainingthe
parationoflibrariesforsequencingwereperformedfollowingtheinDropprotocol first40principalcomponents.SortedLin−HSPCswereprojectedontheLin
previouslydescribedinZillionisetal.22,withmodificationsasdescribedforthe −CD34/CD164principalcomponentspaceuponzscoretransformationofgenes
FACSsubsetssamplesinTusietal.24.FACS-sortedsubpopulationswereindivi- expressiondatawithgenespecificcenteringandscalingparametersderivedfrom
duallyprocessedfordropletbarcoding(SupplementaryTable1).Emulsionswere Lin−CD34/CD164data.Withthisprocedureweobtainedacommon40-
splitinaliquotseachcontaining~2500single-cellbarcodedtranscriptomes. dimensionalsupportthatallowsforadirectcomparisonamongtranscriptomedata
LibrariesgeneratedfromeachFACSsortingwerepreparedinparalleland derivedfromthetwoexperiments.Foreachcellbelongingtoaspecificgroup
sequencedonIlluminaNextSeq500usingaNextSeqHighOutput1×75cyclekit. (FACS-sortedsubpopulationorcomputationallyidentifiedgroup)ineithersorted
Rawsequencingdata(FASTQfiles)wereprocessedusingthepreviouslydescribed Lin−HSPCorLin−CD34/CD164map,weidentifiedthek=4mostsimilarcellsin
inDrops.pybioinformaticspipeline24(availableathttps://github.com/indrops/ theothermap,usingPCAscoresandEuclideandistance.Thegraphicalrepre-
indrops).Bowtiev.1.1.1wasusedwithparameter-e100.Allambiguouslymapped sentationsinFig.2fandSupplementaryFig.8showsortedHSPCcellgroups
readswereexcludedfromanalysisandreadswerealignedtotheEnsemble projectionintoLin−CD34/CD164mapandhavebeengeneratedbyrescalingthe
GRCh38.85versionofhumangenome. two-dimensionalLin−CD34/CD164SPRINGlayouttoaunitsquaredarea.We
NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications 11
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
calculatedcellspatialdistributionusingatwo-dimensionalkerneldensityestimator withfλ1;λ2;¼;λmgandfv1;v2;¼;vmg,respectively,firstmeigenvectorsand
i i i i i i
(bandwidthsforxandydirectionsbothsetto0.035)anduseacontourplotfor eigenvaluesofthek×nmatrixinwhichthek-throwisequaltothen-dimensional
densitylevel1e-05tohighlightareascharacterizedbyanon-negligibleprobability. vectorsx
k
(t)−x
i
(t).TheiterativeproceduPrecontinuesuntilthesumof
Wethenoverlaidadensityestimation(bandwidthsforxandydirectionsbothset consolidationpointsdisplacement,ΔX¼ ½xðt(cid:2)1Þ(cid:2)xðtÞ(cid:3)2isgreaterthana
to0.1)forthespatialdistributionofcellsselectedasmostsimilar.InFig.3a,Lin givensmallε(0.001).Intheupdatingformula i itispossibl i etorecognizetwo
−CD34/CD164group9havebeenprojectedintosortedLin−HSPClayout.Set- components:thefirstone,calledthedata-term,pullsconsolidationpointstoward
tingsusedtogenerategraphshavebeenkeptequaltothoseaforementioned.In localextrema(high-densityregions)ofthenoisyinputdensity.Thesecond,called
additionwealsoinvestigatetheimmunophenotypicdistributionforsortedLin repulsion-term,preventsclumpingofconsolidationpointsbypushingthemalong
−HSPCs,reportedaspiechartinFig.3a
locallyoptimaldirections,enhancinglatentcontinuousm-dimensionalstructures.
AgraphicalrepresentationisgiveninSupplementaryFig.23a.Inthiswork,we
Observedandadjustedcell-densityestimations.Thetranscriptionalstate performedstructure-awarefilteringonthetwo-dimensionalrepresentationof
relatedtosmallsubpopulationssuchasthemost-primitiveones,aredifficultto SPRINGgeneratedlayouts,uponrescalingtotheunitsquaretwo-dimensional
investigatebymeansofsingle-cellprofilingonbulkheterogeneouspopulations. spaceaspreviouslydescribed.Thegoalwastohighlighttheunderlyingone-
IntroducingafractionationstrategythroughFACSsortingbeforeinDropsbar-
dimensional(curves)representations(m=1).Ingeneral,givenavalueforradius
coding,wewereabletoovercomethislimitationbyartificiallyover-representing sizer,itreturnsanestimatedoptimalstructureprovidinganaccurate
primitivefractionsinsidetheCD34+andLin−compartments.Thisaspectis representationofdatalayoutcomplexityandallowingforaninterpretationin
showninthetwo-dimensionaldensityestimationplottedinSupplementaryFig.1a, biologicalterms.Intheirpaper44,authorssuggestamethodtohelpuserinsetting
b(leftplots)wherehigh-densityvaluescanbefoundingraphareasassociatedto thiscriticalparameter.UndertheassumptionofGaussiandistributedinputdata
bothprimitiveandcommittedcells.Toprovidearepresentationofwhatwould withknownvariance,thismethodestimatesalowerboundforrabletoguarantee
havebeeninsteadtheexpectedcontributionofsinglecelleventstothebulkhuman convergencetothetruem-dimensionalmanifold.Wechosealgorithminput
CD34+andLin−populationweassignedtoeachcellaweight,definedaccording parameterscomplyingwiththeseindications,setting,respectively,forthesorted
totheproportionofeventsobservedinthecorrespondingFACSgate.Thegraphs
Lin−HSPCandsortedLin−CD34/CD164cellgraphs:requalto0.05and0.02;μ
ofSupplementaryFig.1a,b(right),showdensitiesobtainedbykeepingcells equalto0.3forboth.Toensurereproducibilityoftheresults,weinitializedtheset
locationconstantandtakingintoaccountthecalculatedcellweights.Detailsforthe ofconsolidationpointswiththewholesetofdatapoints.InSupplementaryFig.3,
calculationofweightsareprovidedintheSupplementaryTable2.
initial,temporary(2ndand10thiterations)andthefinalconfigurationsareshown.
(2)Branchingreconstructionbyminimumspanningtreeonreduced
consolidatingpoints.Structure-awarefilteringreturnscoordinatesofconsolidation
Transcriptionalprincipaltrajectoriesidentification.Boththetopologiesgener-
pointsinthen-dimensionalinputspacesuchthattheydescribeacontinuumof
atedwithSPRINGrevealthepresenceofacontinuumoftranscriptionalstates
locallyoptimalm-dimensionalstructures.Inordertoinfertheprincipal
connectingthemostprimitivesubpopulationstomorecommittedones.Although transcriptionaltrajectories,weproceedasfollows.Wefirstreducedthesetof
somedegreeofvariabilityisobserved,layouttopologiesalsosuggestthepresenceof
consolidationpointsbyiterativelyaveragingpointscloserthan0.01
principaltranscriptionaltrajectoriesduringthedifferentiationprocess.Wecon-
(SupplementaryFig.3,Mergingplots).Thisstephasaregularizationgoaland
sideredthattheestimationandcharacterizationofthesetrajectoriescould
allowsforaconsiderablereductionofthedatasetsizefordownstreamanalyses.To
potentiallyallowusto:(a)establishanorderamongtranscriptionalstateswith
connectpointsanddesignthegraphskeleton,weoptedfortheminimumspanning
respecttodifferentiationprocess;(b)grouptogethercellswithacommonfate;(c)
treealgorithm,withEuclideandistancebasededgesweighting.Onlyinthesorted
investigatethegeneregulatorydynamicsunderlyingfatedecisionandlineages
HSPCanalysisweleftunconnectedthesmallclusterlocatedbetweenerythroidand
commitment.Forthesepurposes,weimplementedaprocedurecomposedbythe
neutrophilsduetoitslargedistancefromothersconsolidationpoints.The
followingmainsteps:(1)structure-awarefilteringperformedontranscriptome
minimumspanningtreeonreducedpointsisvisibleinSupplementaryFig.3,
graph;(2)branchingreconstructionbyminimumspanningtreeonreducedcon-
MSTplots.
solidatingpoints;(3)associationandorderingofcellsaccordingtoinferred (3)Branchassociationandcellsordering.Throughtheidentificationof
branchingstructure.Tofollowthedescriptionofthesesteps.
bifurcationnodes,wesubdividedtheminimumspanningtreeinsegments(or
(1)Structure-awarefiltering.Thestructure-awaretechniquethatweadoptedin
trajectories,orbranches)asshowninSupplementaryFig.3,Principaltrajectories
thispaperworkisaimedtoatrevealingandconsolidatingcontinuous,low-
plots.Eachcellhasbeenassociatedtoonesegment,basedonminimumdistance
dimensional,andhigh-densitystructuresintheunderlyinghigher-dimensional criteria.Inordertoexcludecellswithatranscriptionalprofiletoodifferentfrom
data,whereasignoringnoiseandoutliers.Thetheory,proofofconvergencetothe
thosecapturedbytheprincipaltrajectories,cellsmoredistantthan0.05fromany
exactunderlyingdatamanifolds(underGaussiannoiseassumption)andan
ofthebranchesremainedunlabeled.Toordercellsalongthecorresponding
investigationofitsperformanceunderdifferentscenariocanbefoundinWu
trajectory,wecalculatedthedistancebetweentheinitialnode(markedwith0in
etal.44.Herewewillbrieflydescribeitsdiscretizedversionformulation,i.e.,
SupplementaryFig.23b)andtheprojectionofeachcellontothetrajectory.
representingdensitiesbysetsofsamplepoints.Observeddatapoints,p i ,are Rescaleddistances(0–1interval),havebeencalculatedandusedaspseudotime
consideredsampledfromanunderlyingn-dimensionaldensityf(z),supposedto
p valuesinallgeneexpressionanalysesdescribedinthenextsessionanddiscussedin
havebeengeneratedbyaddingnoisetoanunderlyinglower(m<n)m-
themanuscript.
dimensionaldatamanifold.Consolidationpoints,x i (t),areconsideredtobe AllthealgorithmshavebeenimplementedinR45andaremadeavailablefor
sampledfromatime-dependentdistributionf(z,t),initializedasf(z,0)=f(z),that
x x p downloadathttps://github.com/BiascoLab/PrincipalDevelopementalTrajectories.
changesovertime(iterations)guidedbyatime-dependentvelocityfieldthat
graduallyremovenoisewhilerevealingtheunderlyingm-dimensionalstructurein
theinputdensityf(z).Initially,consolidationpointscanbeeitherarandom GenerationofDiffusionmap.Inordertoverifytherobustnessofourresults
sampleofdatapoi p ntsor,aswedid,thewholedataset.Althoughdatapointsare withrespecttotheadopteddataanalysisapproach,wecomparedtheLin−CD34/
fixedinthen-dimensionalmanifold,thepositionofeveryconsolidationpointis CD164kNN-basedtranscriptometopologyandinferreddifferentiationtrajec-
iterativelyupdatedaccordingtothefollowingformula: toriestothosederivedfromanalternativemethod,notrelyingonkNN,suchas
P pK′ (cid:3) 1 (cid:2) (cid:2) (cid:2)p (cid:2)xðtÞ (cid:2) (cid:2) (cid:2) 2 (cid:4) a D v i a ff i u la s b io le n in ma p p a 2 c 7 k . a W ge e d t e o s ok ti a n dv y a 4 n 6, ta t g h e at o i f s R sp i e m c p ifi le c m all e y nt d a e t s i i o g n ne o d fd fo if r fu sc si R o N n A m -s a e p q
x i ðtþ1Þ′¼ x i ðtÞ P j K j ′ (cid:3) 1 2 (cid:2) (cid:2) (cid:2)p j (cid:2)xð i tÞ (cid:2) (cid:2) (cid:2) 2 (cid:4) d re a p ta o . rt W in e g p th a e ss 4 e 0 d p a r s in in ci p p u a t l a c r o g m u p m o e n n e t n t t o sr D e i p f re f s u en s t i at o io n n Ma of p fi f l u te n r c e t d io -a n n t d h - e no m rm at a ri l x ized
j 2 j i expressiondata,obtainedasdescribedintheDatavisualizationandconstruction
(cid:2)μ P k A′Aðx Pk ðtÞ(cid:2) (cid:5) x i ðtÞÞL′ (cid:5) 1 2 kAðx k ðtÞ(cid:2) (cid:6) x i ðtÞÞk2 (cid:6) b o e f e k n -n k e e a p r t es t t o n d e e i f g a h u b lt or c s on g fi ra g p u h ra s t s io ec n t s i . o T n. he Al d l if o f t u h s e io r n Di m f a f p u f s or i L o i n n M − a C p D s 3 e 4 tt / i C n D gs 16 h 4 av i e s
k
L′ 1
2
kAðx
k
ðtÞ(cid:2)x
i
ðtÞÞk2 showninSupplementaryFig.5.Weconfirmedthetranscriptionalprincipal
whereK′andL′arefirstderivativesofastandardandmodifiedGaussian
trajectoriesidentifiedstartingfromSPRINGlayout(Fig.2d)byapplyingour
smoothingkernelsdefinedas algorithmtothethree-dimensionaldiffusionmap.Theresultsarereportedin
(cid:3) (cid:2) (cid:2) (cid:4) (cid:5) (cid:6) SupplementaryFig.6.
K′ 1
2
(cid:2) (cid:2)p
j
(cid:2)x
i
ðtÞ (cid:2) (cid:2) 2 ¼e(cid:2) kpj(cid:2)xiðtÞk2 =2r2
Geneexpressionanalysis.Throughoutthemanuscript,differenttypesofgene
and expressionanalysishavebeenshown.Thestatisticalmodelunderlyingeachof
(cid:3) (cid:4) themhasbeendefinedaccordingtothespecificquestionofinterest.Theanalyses
L′ 1 kA½x ðtÞ(cid:2)xðtÞ(cid:3)k2 ¼(cid:5) e(cid:2)ðkA½xkðtÞ(cid:2)xiðtÞ(cid:3)k2Þ=2r2 (cid:6); canbegroupedinthefollowingcategorieswithrelatedexamplesshowninSup-
2 k i kA½x ðtÞ(cid:2)xðtÞ(cid:3)k2 plementaryFig.23c:(1)differentiallyexpressedgenesacrosscellgroups(Fig.1c;
k i SupplementaryFig.5a,c);(2)identificationofgeneswithasignificantassociation
betweenexpressionlevelandbranch-specificpseudotimeordering(Fig.3b,c;
jandkmark,respectively,dataandconsolidationpointswithinaradially SupplementaryFig.7);(3)investigationofdifferencesingeneexpressiondynamics
symmetric,n-dimensionalneighborhoodo(cid:7)fuser-definedradius(cid:8)rcenteredonx i (t); amongtrajectories(Fig.2e;SupplementaryFig.5b).Similarlytowhatproposedin
0<μ<1isauser-definedconstant;A ¼ λ1v1;λ2v2;¼;λmvm isan×mmatrix Trapnelletal.47,weoptedforaGeneralizedAdditiveModels48approach,that
i i i i i i i
12 NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
allowstotestthedependencebetweentheresponsevariableanddifferenttypesof heatmapinFig.3b(bottom).Wefurtherinvestigateddis/similaritiescalculating
predictorsinamoreflexiblemanner.Forexample,byestimatingregression Pearsoncorrelationscoefficientsforeachcoupleofhuman/mousehomologous
coefficientsbyusingdifferentlossfunctions(M-estimators)orbymodelingtrend genes(SupplementaryFig.10,tableavailableinSupplementaryInformation),and
withnonparametricfunctions.Topreventthepotentiallyhighimpactofexpression performedpathwayenrichmentanalysisusingReactomedatabase55onthe89
valueoutliersanddropouts,frequentlyobservedinsinglecellRNA-Seqdata,inall humangenesexhibitingalow-or-negativecorrelation(Pearsoncorrelation<0.5).
fittingproceduresweemployedtheHuberlossfunctionforregression.Huberloss
functioniscommonlyusedinrobustregressionandconsistsinapiecewisepenalty
Populationbalanceanalysis.Toinferthestructureofthehematopoieticlineage
f d u if n f c e t r i e o n n ce i s n . w Its hi t c u h ni a ng qu c a o d n r s a t t a i n c t p h e a n s al b iz e a e t n io s n et is to re k pl = ac 0 e . d 86 b 2 y ,m al e i a n n e i a n r g o t n h e at fo t r he la l r i g n e ear c tr o e u e p f l r in om gs t b h e e tw s e c e R n N e A a - c s h eq pa d ir at o a f ,w fa e te a s. p F p o li r ed th P e B L A in ( − W H e S in P r C eb su e b t s a e l t .5 d 6 a ) t a a n s d et c , a P lc B u A la w te a d s
lossisappliedtodifferencesbelowthe10thandabove90thpercentile,assuminga
runonthemergeddata,usingthekNNgraphconstructedasabove(Datavisua-
cen
D
tra
if
l
fe
G
re
a
n
u
t
s
ia
si
l
a
ly
n
e
p
x
a
p
r
r
t
es
o
s
f
ed
th
g
e
en
d
e
is
s
tr
a
i
c
b
r
u
o
t
s
i
s
on
cel
o
l
f
g
r
r
e
o
s
u
id
p
u
s
a
h
ls
a
.
vebeenidentifiedbyfitting
lizationandconstructionofkNNgraphs).PBAwasrunasinTusietal.24.Inbrief,
weassignednegativevaluesofR(thelocalimbalancebetweencelldivisionandcell
andcomparingthetwofollowingmodelsforeachgeneseparately.Thefullmodel loss)tothefivecellswithhighestgenesignaturescoreforeachfate(sePenext
assumesgeneexpressionaveragestobegroup-dependent.Fromapracticalview-
p l M f a o o b r 1 i e n a l : t s , μ g G m ð e Y n i o ; e Þ i d . ¼ e ¼ T l h l β 1 i e k ; 0 e r ¼ þ l e i s h t β ; o r 1 i k o c G , d te w 1 d a þ h n ( e d n r ¼ e u c l o k l) e þ i f m s fi β c t o i k h e d G e n e k t l n s , M u w h m 0 a h v b e : e e r μ r e b ð o μ Y ee f ( Þ Y n g ¼ ) r c o i a u s β lc p 0 t u h s l i , e a n a t s a e s t v d e d e a r u b d a m y , g a e u m s s s e y i u x n m p v g r a e e g r s s i r a s o n i b u o o l p n e - s, value fi u H p Se n a v e t r e i r t f a i e o c n g , r e r g m w l a l p s t e . h h w A e r ) e i d t s a s h t i n i r f m d f i h u c i i t s l a g e a i h d o r s n e in p t s h t r g c o e l o H e c n a e S p s n d C t o a a u s l n r y i s t e t i s i g i v t w s n o e a a t v o t 1 s u a , c t r l w u h a e r e e e h ri t C fi a e o d t d D t t h a 1 o h v 6 e u e e 4 t r r e h e a f x i m o g g i h r t e a C r t i f h D n a a t t e i 3 e n e s 4 L g p + i f n r c o o e − p r b l o l e C a s p a b D s u c i u h l l 3 i a c t 4 t h f i i / e a o C s t t n e h D w , a s 1 i a t u t 6 s h c 4 h i t n h d i t i R h a 1 s t a % i a c t ¼ o s t o n h e f 0 - t e . .
differencesinmeanexpressionvaluesamonggroupsandconsidersvariationonly
tainedalluncommittedprogenitorsandtheearliestunilineageprogenitors.The
owingtotheintrinsicnoiseofexpressionmeasurements.Derivedfromthisanalysis
kNNgraphforPBAwasconstructedsettingkto40toimprovetherobustnessof
areheatmapsinFig.1gandSupplementaryFig.5a,cwherestatisticallysignificant
theanalysis,andwesetthediffusionconstantto0.5andused10cellsperfateand
geneswithinspecificsubsets(CDmarkergenes49,HumanandMousetranscription
10HSCstofittheexitrates.
factors50,bloodcancerassociatedproto-oncogenes51)areshown.Information Weusedthefollowinggenesetstodefinethelineage-specificsignaturesforthe
regardingallsignificantgenesareavailableinSupplementaryInformation.Detection
Lin−HSPCsubsetdataset:
ofgenesthatsignificantlychangeasafunctionofpseudotime,t,hasbeendoneby
comparingthelikelihoodofthemodelM 1 :μðY;tÞ¼β 0 þsðtÞ,whereexpression Meg:ITGA2B,PF4,VWF
valuetrendμ(Y,t)variesaccordingtoacubicsplines(withfourdegreeoffreedom),s E:CA1,HBB,KLF1,TFR2
(t),toaflatnullhypothesisM 0 :μðYÞ¼β 0 inwhichexpressionisassumedto DC:CCR2,IRF8,MPEG1
randomlyfluctuatesaroundaconstantvaluealongthewholebranch.Allgeneshave G:ELANE,MPO,LYZ,CSF1R,CTSG,PRTN3,AZU1
beentestedforassociationwithrespecttoeachbranchandallestimatedregression Ly1:RGS1,NPTX2,DDIT4,ID2
functionsareavailableinSupplementaryInformation.PanelsinFig.3b,cand Ly2:DNTT,RAG1,RAG2
SupplementaryFig.7arebasedonthismodelingapproach.Finally,tofinddifferences HSC:CRHBP,HLF,DUSP1
ingeneexpressiondynamicsunderlyingfatedecisionsanddivergentdifferentiation AndfortheLin−CD34/CD164dataset:
trajectories,weproceedasfollows.Asaforementioned,cellpseudotimevaluecanbe E:KLF1,CA1
interpretedasameasureofcelldegreeofmaturationalongaspecificsegmentofthe Meg:ITGA2B,PLEK
differentiationprocess.Eventhoughitisdifficulttomakeadirectcomparisonamong BEM:CLC,CPA3,HDC
theregulatorydynamicsunderlyingcommitmenttowarddifferentlineages,by Ly:DNTT,CD79A,VPREB1
rescalingthebranchtotallengthtotheunitinterval,itispossibletotestwhethera DC:IRF8,SPIB,IGKC
genebehavesdifferentlyamongbranches.Thisisasimplisticapproachthatonly M:LYZ,MS4A6A,ANXA2
partiallytakesintoaccountthepotentialpresenceofdifferentmaturationpacesor N:ELANE
otherconfoundingfactorssuchasvaryingduplication/differentiation/deathrates.In HSC:HLF,ADGRG6,CRHBP,PCDH9
theformulationofthefullmodelemployedinthisgeneexpressionanalysis,wealso
Forbothdatasets,weusedthePBA-predictedfateprobabilitiestoinfera
assumedthatcellsbelongingtotrajectoriesstemmingfromacommonbifurcation differentiationhierarchy,asinTusietal.24(Figs1f,2c).Afatecouplingscore(see
node,exhibitanexpressionpatternhighlysimilarforpseudotimevaluescloseto0,
thatwilltheneventuallyprogressivelydivergetowardmorebranch-specific n
si
e
g
x
n
t
ifi
p
c
a
a
r
n
a
t
g
l
r
y
ap
h
h
ig
)
h
w
er
as
th
c
a
o
n
m
e
p
x
u
p
t
e
e
c
d
te
f
d
or
un
ea
d
c
e
h
rt
p
h
a
e
ir
n
o
u
f
ll
fa
m
te
o
s
d
,
e
a
l
n
w
d
e
p
re
ai
j
r
o
s
in
w
e
i
d
th
an
sc
d
or
th
es
eirfate
transcriptionalstates.Thisassumptionmotivatedtheformulationofthemodel
M :μðY;tÞ¼β þsðtÞG þsðtÞG,inwhichbranch-specificgeneregression probabilitiesmergedbyaddition.Thisprocesswascarriedoutiterativelyuntilall
1 0 i i j j fateswerejoined.
curvescanevolveaccordingtodistinctpseudo-temporaldynamicss i (t)ands j (t), ThecouplingscorebetweentwofatesAandBisthenumberofcellswithP(A)P
constrainedtohavethesameexpressionvaluefort=0(commonintercept).The (B)>ε,usingε=1/14throughout.Wegeneratedanulldistributionforeachpairof
reducedmodelM 0 :μðY;tÞ¼β 0 þsðtÞ,allowsgeneexpressionaveragetovaryover fatesbycomputingthecouplingscoresfor1000permutationsoftheoriginalfate
pseudotimeaccordingtoanon-linearfunction,butassumesacommons(t)forboth probabilities,re-normalizingeachcell’sprobabilitiesateachrandomization.The
groups.InFig.2e,SupplementaryFig.5bandtablesinSupplementaryInformation significanceoftheobservedcouplingswasmeasuredusingthezscorewithrespect
significantfateassociatedgenesarereported.TranscriptionfactorsshowninFig.2e,
tothenulldistribution.
SupplementaryFig.5bhavebeenselected(amongthosesignificant)becausealready
proposedintheliteraturehascorrelatedwithlineagecommitted.
Inallcases,thedifferencesinexplanatorypowerbetweenM andnestedmodel Reportingsummary.Furtherinformationonresearchdesignisavailablein
1
M,havebeentestedbyChi-squaredlikelihoodratiotest(LRT).Statisticvalue, theNatureResearchReportingSummarylinkedtothisarticle.
0
alongwithassociatedpvalues,genename,andestimatedmean/regressioncurves
arereportedinSupplementaryInformationonlyforthosegeneswithadjustedp Data availability
valueα<0.05(Holmmethod52formultiplecomparisons).Alltheanalyseshave
RawdataareavailablewithGEOaccessioncodeGSE117498[https://www.ncbi.nlm.nih.
b B e ia e s n co p L e a rf b o / r P m ri e n d ci b p y alD m e e v a e n lo s p o e f m c e u n st t o a m lTr R aj 4 e 5 ct s o c r r i i e p s t . s F a o v r ai r l e a g b r le es a si t o h n tt fi p t s t : i / n /g g it a h n u d b. m co o m de / l f g o o l v lo /g w e i o n / g qu li e n r k y s / : ac M c. o c u gi s ? e ac K c i = t+ G , S [ E h 1 tt 1 p 7 s 4 :/ 9 / 8 k ] l . ei S n P t R oo IN ls. G hm pl s o .h ts ar a v r a e r a d v .e a d il u ab /t l o e o f l o s r / inspectionatthe
testing,weusedtheVGAMlibrary53,andinparticularvgam(),huber1()andsm.
springViewer_1_6_dev.html?datasets/mouse_HPCs/basal_bone_marrow/full];Human
bs(),respectively,forestimate,lossfunctionandsplinesinterpolationandlrtest()
Lin−CD164/CD34,[https://kleintools.hms.harvard.edu/tools/springViewer_1_6_dev.
fortesting.
html?datasets/CD34_CD164/CD34_CD164];HumansortedHSPC,[https://kleintools.
hms.harvard.edu/tools/springViewer_1_6_dev.html?datasets/sortedHSPC/sortedHSPC].
Comparisonofhumanvsmouseerythropoiesis.Inordertocomparethegene ThesourcedataunderlyingFigs.1g,2e,3,4b,c,5,SupplementaryFigs.7,10,12,13,15–
expressiondynamicsassociatedtohumanandmouseerythropoiesis,wetook 17,21–23areprovidedasaSourceDataFile.
advantageofdatageneratedbyusinginDropstechnologyonmouseKit+cells24.
Formousedataset,differentiationtrajectorieswereidentifiedandcellslabeled
Code availability
(Fig.3a)accordingtothemethodologyaforedescribed.Weconsideredasrepre-
SPRINGsoftwareisavailableathttps://github.com/AllonKleinLab/SPRING.PBA
sentativeoferythroidcommitmentsubgroup6inmouseandsubgroups6,7,8in
humanLin−CD34/CD164map(Fig.3btop).Genesweretestedforassociationto algorithmisavailableathttps://github.com/AllonKleinLab/PBA.Structure-awaredata
pseudotimeinthetwoorganismsseparately(human:3821;mouse:1071statisti-
consolidationalgorithmdescribedinWu,Shihaoetal.44hasbeenimplementedinRis
callysignificantgenes,LRTadjustedpvalue<0.05;completelistsanddetailsare availableathttps://github.com/BiascoLab/PrincipalDevelopementalTrajectories.
availableinSupplementaryInformation).Amongthosesignificant,weretrieved
720orthologousgenesbasedonMouseGenomeDatabase(MGD)54(Mouse Received: 11 January 2019 Accepted: 3May 2019
GenomeInformaticswebsite,TheJacksonLaboratory,BarHarbor,Maine,http://
www.informatics.jax.org),forwhichbehaviorisplottedbymeansofsymmetric
NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications 13
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
References 31. Pishesha,N.etal.Transcriptionaldivergenceandconservationofhumanand
1. Kawamoto,H.,Ikawa,T.,Masuda,K.,Wada,H.&Katsura,Y.Amapfor mouseerythropoiesis.Proc.Natl.Acad.Sci.111,4103–4108(2014).
lineagerestrictionofprogenitorsduringhematopoiesis:Theessenceofthe 32. McGowan,K.A.&Mason,P.J.AnimalmodelsofdiamondBlackfananemia.
myeloid-basedmodel.Immunol.Rev.238,23–36(2010). Semin.Hematol.48,106–116(2011).
2. Ema,H.,Morita,Y.&Suda,T.Heterogeneityandhierarchyofhematopoietic 33. Masiuk,K.E.etal.Improvinggenetherapyefficiencythroughthe
stemcells.Exp.Hematol.42,74–82(2014). enrichmentofhumanhematopoieticstemcells.Mol.Ther.25,2163–2175
3. Eaves,C.Hematopoieticstemcells:concepts,definitions,andthenewreality. (2017).
Blood125,2605–2614(2015). 34. Zonari,E.etal.Efficientexvivoengineeringandexpansionofhighlypurified
4. Laurenti,E.etal.Thetranscriptionalarchitectureofearlyhuman humanhematopoieticstemandprogenitorcellpopulationsforgenetherapy.
hematopoiesisidentifiesmultilevelcontroloflymphoidcommitment.Nat. StemCellRep.8,977–990(2017).
Immunol.14,756–763(2013). 35. Watt,S.M.etal.Cd164,anovelsialomucinoncd34+anderythroidsubsets,
5. Doulatov,S.,Notta,F.,Laurenti,E.&Dick,J.E.Hematopoiesis:ahuman islocatedonhumanchromosome6q21.Blood92,849–866(1998).
perspective.Cell.Stem.Cell.10,120–136(2012). 36. Watt,S.M.etal.FunctionallydefinedCD164epitopesareexpressedon
6. Biasco,L.etal.Invivotrackingofhumanhematopoiesisrevealspatternsof CD34(+)cellsthroughoutontogenybutdisplaydistinctdistribution
clonaldynamicsduringearlyandsteady-statereconstitutionphases.CellStem patternsinadulthematopoieticandnonhematopoietictissues.Blood95,
Cell19,107–119(2015). 3113–3124(2000).
7. Haas,S.,Trumpp,A.&Milsom,M.D.Causesandconsequencesof 37. Forde,S.etal.Endolyn(CD164)modulatestheCXCL12-mediated
hematopoieticstemcellheterogeneity.CellStemCell22,627–638(2018). migrationofumbilicalcordbloodCD133+cells.Blood109,1825–1833
8. Pei,W.etal.Polyloxbarcodingrevealshaematopoieticstemcellfatesrealized (2007).
invivo.Nature548,456–460(2017). 38. Zannettino,aC.etal.ThesialomucinCD164(MGC-24v)isanadhesive
9. Notta,F.etal.Distinctroutesoflineagedevelopmentreshapethehuman glycoproteinexpressedbyhumanhematopoieticprogenitorsandbone
bloodhierarchyacrossontogeny.Science351,aab2116(2016). marrowstromalcellsthatservesasapotentnegativeregulatorof
10. Velten,L.etal.Humanhaematopoieticstemcelllineagecommitmentisa hematopoiesis.Blood92,2613–2628(1998).
continuousprocess.Nat.CellBiol.19,271–281(2017). 39. Aiuti,A.etal.Lentiviralhematopoieticstemcellgenetherapyinpatientswith
11. Zheng,S.,Papalexi,E.,Butler,A.,Stephenson,W.&Satija,R.Molecular wiskott-aldrichsyndrome.Science341,1233151(2013).
transitionsinearlyprogenitorsduringhumancordbloodhematopoiesis.Mol. 40. Notta,F.etal.Isolationofsinglehumanhematopoieticstemcellscapableof
Syst.Biol.14,e8041(2018). long-termmultilineageengraftment.Science333,218–221(2011).
12. Hay,S.B.,Ferchen,K.,Chetal,K.,Grimes,H.L.&Salomonis,N.TheHuman 41. Scala,S.etal.Dynamicsofgeneticallyengineeredhematopoieticstemand
CellAtlasbonemarrowsingle-cellinteractivewebportal.Exp.Hematol.68, progenitorcellsafterautologoustransplantationinhumans.Nat.Med.24,
51–61(2018). 1683–1690(2018).
13. Buenrostro,J.D.etal.Integratedsingle-cellanalysismapsthecontinuous 42. Rodriguez-Fraticelli,A.E.etal.Clonalanalysisoflineagefateinnative
regulatorylandscapeofhumanhematopoieticdifferentiation.Cell173, haematopoiesis.Nature553,212–216(2018).
1535–1548.e16(2018). 43. Klein,A.M.etal.Dropletbarcodingforsingle-celltranscriptomicsappliedto
14. Sanjuan-Pla,A.etal.Platelet-biasedstemcellsresideattheapexofthe embryonicstemcells.Cell161,1187–1201(2015).
haematopoieticstem-cellhierarchy.Nature502,232–236(2013). 44. Wu,Shihao,etal.Structure-awareDataConsolidation.IEEETrans.Pattern
15. Carrelha,J.etal.Hierarchicallyrelatedlineage-restrictedfatesofmultipotent Anal.Mach.Intell.40,2529–2537(2018).
haematopoieticstemcells.Nature554,106–111(2018). 45. Team,R.Core.R.:alanguageandenvironmentforstatisticalcomputing.R
16. Karamitros,D.etal.Single-cellanalysisrevealsthecontinuumof FoundationforStatisticalComputing,Vienna,Austria.https://www.R-project.
humanlympho-myeloidprogenitorcellsarticle.Nat.Immunol.19,85–97 org/(2013).
(2018). 46. Angerer,Philippetal.destiny:diffusionmapsforlarge-scalesingle-celldatain
17. Goardon,N.etal.CoexistenceofLMPP-likeandGMP-likeleukemiastem R.Bioinformatics32,1241–1243(2015).
cellsinacutemyeloidleukemia.CancerCell.19,138–152(2011). 47. Trapnell,Cole,etal.Thedynamicsandregulatorsofcellfatedecisionsare
18. Civin,C.I.etal.Antigenicanalysisofhematopoiesis.III.Ahematopoietic revealedbypseudotemporalorderingofsinglecells.Nat.Biotechnol.
progenitorcellsurfaceantigendefinedbyamonoclonalantibodyraised 32,381–386(2014).
againstKG-1acells.J.Immunol.133,157–165(1984). 48. Hastie,TrevorJ.Generalizedadditivemodels.StatisticalmodelsinS.
19. Psaila,B.etal.Single-cellprofilingofhumanmegakaryocyte-erythroid Routledge249–307(2017).
progenitorsidentifiesdistinctmegakaryocyteanderythroiddifferentiation 49. Uhlen,Mathiasetal.Thehumanproteinatlas.http://www.proteinatlas.Org
pathways.GenomeBiol.17,1–19(2016). (2015).
20. Basso-Ricci,L.etal.Multiparametricwholeblooddissection:aone-shot 50. Ravasi,Timothyetal.Anatlasofcombinatorialtranscriptionalregulationin
comprehensivepictureofthehumanhematopoieticsystem.Cytom.PartA91, mouseandman.Cell140,744–752(2010).
952–965(2017). 51. Forbes,SimonA.etal.COSMIC:somaticcancergeneticsathigh-resolution.
21. DeJong,M.O.,Wagemaker,G.&Wognum,aW.Separationofmyeloidand NucleicAcidsRes.45,D777–D783(2016).
erythroidprogenitorsbasedonexpressionofCD34andc-kit.Blood86, 52. Holm,S.Asimplesequentiallyrejectivemultipletestprocedure.Scand.J.Stat.
4076–4085(1995). 2,65–70(1979).
22. Zilionis,R.etal.Single-cellbarcodingandsequencingusingdroplet 53. Yee,ThomasW.Vectorgeneralizedlinearandadditivemodels:withan
microfluidics.Nat.Protoc.12,44–73(2017). implementationinR.XXIV,589(Springer-Verlag,NewYork,2015).
23. Klein,A.M.&Macosko,E.InDropsandDrop-seqtechnologiesforsingle-cell 54. Smith,CynthiaL.etal.MouseGenomeDatabase(MGD)-2018:
sequencing.Lab.Chip.17,2540–2541(2017). knowledgebaseforthelaboratorymouse.NucleicAcidsRes.46,D836–D842
24. Tusi,B.K.etal.Populationsnapshotspredictearlyhaematopoieticand (2017).
erythroidhierarchies.Nature555,54–60(2018). 55. Croft,Davidetal.TheReactomepathwayknowledgebase.NucleicAcidsRes.
25. Weinreb,C.,Wolock,S.&Klein,A.M.SPRING:akineticinterfacefor 42,D472–D477(2013).
visualizinghighdimensionalsingle-cellexpressiondata.Bioinformatics34, 56. Weinreb,Calebetal.Fundamentallimitsondynamicinferencefromsingle-
1246–1248(2017). cellsnapshots.Proc.Natl.Acad.Sci.USA115,E2467–E2476(2018).
26. Yáñez,A.etal.Granulocyte-monocyteprogenitorsandmonocyte-dendritic
cellprogenitorsindependentlyproducefunctionallydistinctmonocytes.
Immunity47,890–902.e4(2017).
27. Haghverdi,L.,Buettner,F.&Theis,F.J.Diffusionmapsforhigh-dimensional Acknowledgements
single-cellanalysisofdifferentiationdata.Bioinformatics31,2989–2998 L.B.,D.P.,M.L.,andC.B.weresupportedbythestart-upfundsoftheGene
(2015). TherapyProgramatDana-Farber/BostonChildren’sCancerandBloodDisorders
28. Görgens,A.etal.Revisionofthehumanhematopoietictree:granulocyte Center.TheworkofL.B.wasalsosupportedbyTheWellcomeTrust(104807/Z/14/Z,
subtypesderivefromdistincthematopoieticlineages.CellRep.3,1539–1552 PrincipalResearchFellowshipawardedtoA.JThrasher),andtheNationalInstitute
(2013). forHealthResearchBiomedicalResearchCentreatGreatOrmondStreetHospital
29. Drissen,R.etal.EuropePMCFundersGroupDistinctmyeloidprogenitor forChildrenNHSFoundationTrust,London,UK.A.M.K.andS.L.W.weresupported
differentiationpathwaysidentifiedthroughsinglecellRNAsequencing.Nat. byNCIgrantR33CA212697-01andseedfundingfromtheHarvardStemCell
Immunol.17,666–676(2016). InstituteBloodProgram.WeacknowledgetheSinglecellcore(HarvardMedical
30. Mori,Y.etal.Identificationofthehumaneosinophillineage-committed School)andtheDFCIFlowCytometryCoreFacility(Harvard)forthetechnical
progenitor:revisionofphenotypicdefinitionofthehumancommonmyeloid support.WethankDavidWilliamsandChristianBrendelforthecriticalreviewofthe
progenitor.J.Exp.Med.206,183–193(2009). manuscript.
14 NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-10291-0
Author contributions Publisher’snote:SpringerNatureremainsneutralwithregardtojurisdictionalclaimsin
D.P.performedsingle-celldataanalysisandinformatics.S.L.W.carriedoutinDrops
publishedmapsandinstitutionalaffiliations.
experimentsandinitialdataanalysis,andallP.B.A.modeling.M.L.performedand
analyzedtheexperiments,assistedbyC.B.andA.M.O.W.performedandanalyzedthe
Giemsastaining.A.B.supervisedtheinvivostudies.L.B.andA.M.K.designedthestudy Open Access This article is licensed under a Creative Commons
andwrotethemanuscript.L.B.supervisedthestudy. Attribution 4.0 International License, which permits use, sharing,
adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
Additional information appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreative
SupplementaryInformationaccompaniesthispaperathttps://doi.org/10.1038/s41467- Commonslicense,andindicateifchangesweremade.Theimagesorotherthirdparty
019-10291-0.
materialinthisarticleareincludedinthearticle’sCreativeCommonslicense,unless
indicatedotherwiseinacreditlinetothematerial.Ifmaterialisnotincludedinthe
Competinginterests:Theauthorsdeclarenocompetinginterests.
article’sCreativeCommonslicenseandyourintendeduseisnotpermittedbystatutory
regulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfrom
Reprintsandpermissioninformationisavailableonlineathttp://npg.nature.com/ thecopyrightholder.Toviewacopyofthislicense,visithttp://creativecommons.org/
reprintsandpermissions/ licenses/by/4.0/.
Journalpeerreviewinformation:NatureCommunicationsthanksSimonHaasand
©TheAuthor(s)2019
otheranonymousreviewer(s)fortheircontributiontothepeerreviewofthiswork.
NATURECOMMUNICATIONS| (2019) 10:2395 |https://doi.org/10.1038/s41467-019-10291-0|www.nature.com/naturecommunications 15
