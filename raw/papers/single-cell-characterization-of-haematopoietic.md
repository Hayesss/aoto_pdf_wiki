---
source_path: /mnt/c/Users/Administrator/Zotero/storage/NI74ADB3/Giladi 等 - 2018 - Single-cell characterization of haematopoietic pro.pdf
ingested: 2026-04-23
sha256: 6c5cd74849b23adc
---

ResouRce
https://doi.org/10.1038/s41556-018-0121-4
Single-cell characterization of haematopoietic
progenitors and their trajectories in homeostasis
and perturbed haematopoiesis
Amir Giladi1,7, Franziska Paul1,7, Yoni Herzog2, Yaniv Lubling2, Assaf Weiner1, Ido Yofe1, Diego Jaitin1,
Nina Cabezas-Wallscheid3,4,5, Regine Dress6, Florent Ginhoux 6, Andreas Trumpp3, Amos Tanay 2,8*
and Ido Amit 1,8*
The dynamics of haematopoietic stem cell differentiation and the hierarchy of oligopotent stem cells in the bone marrow remain
controversial. Here we dissect haematopoietic progenitor populations at single cell resolution, deriving an unbiased reference
model of transcriptional states in normal and perturbed murine bone marrow. We define the signature of the naive haemato-
poietic stem cell and find a continuum of core progenitor states. Core cell populations mix transcription of pre-myeloid and pre-
lymphoid programs, but do not mix erythroid or megakaryocyte programs with other fates. CRISP-seq perturbation analysis
confirms our models and reveals that Cebpa regulates entry into all myeloid fates, while Irf8 and PU.1 deficiency block later
differentiation towards monocyte or granulocyte fates. Our transcriptional map defines a reference network model for blood
progenitors and their differentiation trajectories during normal and perturbed haematopoiesis.
Haematopoietic stem cells (HSCs) are currently classified by a HSC populations and their immediate derivatives in the bone mar-
combination of specific surface markers and their functional row. We find a spectrum of transcriptional states with progressively
long-term reconstitution capacity towards all blood lineages more relaxed quiescent HSC signature. Nevertheless, single-cell
in transplantation experiments1–3. There is compelling evidence for analyses of mice treated with granulocyte-colony stimulating fac-
the existence of stem cells within the bone marrow4,5. Nevertheless, tor (G-CSF) or erythropoietin (Epo) suggest that cytokine stimu-
the dynamics and differentiation steps by which stem cells give rise lation disrupts HSC dormancy non-specifically before expanding
to diverse blood and immune cell types are difficult to character- either myeloid or erythrocyte progenitor populations, respectively.
ize6–11. Given that haematopoiesis is one of the most studied models In transcriptional states that show a weak HSC transcriptional sig-
for somatic development in animals, and aberrant haematopoietic nature, we observe co-expression of early myeloid and lymphoid
differentiation is a major cause for human malignancies12,13, the genes, but no mixing of erythrocyte genes with myeloid or lym-
gap between HSCs and functional blood lineages remains a field phoid genes. Moreover, myeloid and lymphoid progenitor states are
of active research for which many models are being proposed11,14–23. defining a non-hierarchical network of possible differentiation tra-
Single-cell RNA sequencing (scRNA-seq) was recently applied to jectories that precede ultimate functional commitment. CRISP-seq
dissect haematopoietic progenitors and other cell populations20,24–30. analyses of Cebpa, Irf8 and PU.1 show that the loss of either of these
The major advantages of this approach include bypassing the need transcription factors modifies the spectrum of progenitor transcrip-
for a priori markers that define progenitor populations, and the tional states. This leads to the accumulation of weakly differentiated
sensitivity to detect rare or even transient transcriptional states de states, rather than blocking hierarchically the initiation of transcrip-
novo, provided that sufficient single cells are sampled31. Current tional priming. Interestingly, we observe an apparent gap between
studies using scRNA-seq have redefined the transcriptional states the progenitor states that are linked with HSCs and bona fide B-cell
of myeloid subtypes and other stem and progenitor populations in progenitors strongly expressing Vpreb1–3, suggesting that the ori-
the bone marrow15,16,20,32–39, suggesting that the differentiation from gin of B cell and other lymphoid populations may be distinct. Our
HSCs is more complex and less sequential than previously appre- data thus suggest an scRNA-based reference map as a generaliza-
ciated9,40. However, inference of lineage relationships between cell tion of current hierarchical and discrete models of haematopoietic
populations in the bone marrow, when relying solely on a snapshot progenitor cell types.
sample of a priori unrelated single cells, remains practically and
theoretically challenging. Results
Here we apply a comprehensive multi-tier scRNA-seq approach Reference map for bone marrow transcriptional states. To char-
coupled with index sorting and CRISP-seq41 perturbation analysis acterize HSC differentiation systematically, we sought to derive a
to perform de novo transcriptional characterization of dormant comprehensive map of the transcriptional landscape in the bone
1Department of Immunology, Weizmann Institute of Science, Rehovot, Israel. 2Department of Computer Science and Applied Mathematics, Department
of Biological Regulation, Weizmann Institute of Science, Rehovot, Israel. 3Division of Stem Cells and Cancer, Deutsches Krebsforschungszentrum
(DKFZ) and DKFZ-ZMBH Alliance, Heidelberg, Germany. 4Heidelberg Institute for Stem Cell Technology and Experimental Medicine (HI-STEM GmbH),
Heidelberg, Germany. 5Max Planck Institute of Immunobiology and Epigenetics, Freiburg, Germany. 6Singapore Immunology Network (SIgN), Agency for
Science, Technology and Research (A*STAR), Singapore, Singapore. 7These authors contributed equally: Amir Giladi, Franziska Paul. 8These authors jointly
supervised: Amos Tanay, Ido Amit. *e-mail: amos.tanay@weizmann.ac.il; ido.amit@weizmann.ac.il
836 NATuRe CeLL BIoLoGY | VOL 20 | JULY 2018 | 836–846 | www.nature.com/naturecellbiology
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
NaTuRe Cell BIOlOgy ResouRce
a b
1 Tier 1 (total BM) 47% 18% 18% 6% 15% No marker Prss34
1,901 cells Pf4 Prg2
2 Car1 Cd74
3 c Hba-a2 Siglech
T 1 ie ,8 r 7 2 8 ( L c i e n l – ls ) 6% 7% 5% 11% 63% L L y y 8 z1 6 V C p cl r 5 eb1
Gstm1 Myl4
d Fcnb Fcrla
Ltf
Tier 3 (c-Kit+ Lin–) 18% 11% 9% 9% 9% 9% 18%
12,051 cells
Fig. 1 | Multi-tier single-cell sequencing of haematopoietic progenitors. a, A multi-tiered approach for unbiased sequencing and characterization of
mouse bone marrow progenitors. Each circle represents a tier (Supplementary Fig. 1a,b). Circle size is proportional to tier frequency in the bone marrow.
b–d, Gene expression of lineage markers across single cells from whole bone marrow (b, tier 1: 1,901 cells); Lin− cells (c, tier 2: 1,878 cells) and Lin− c-Kit+
cells (d, tier 3: 12,051 cells). Each cell is annotated by its dominant lineage marker. Cells represented in a lower tier are marked in white.
marrow by implementing a multi-tier sampling design (Fig. 1a Transcriptional program of quiescent HSC. To better identify tran-
and Supplementary Fig. 1a,b). Because different haematopoietic scriptional states representing stem cells and their immediate tran-
cells span several orders of magnitude in abundance, we combined scriptional derivatives, we focused on cells lacking strong expression
broad sampling of single cells with minimal bias and data-driven of differentiation markers (Supplementary Fig. 4a and Methods).
depletion and enrichment strategies to deeply probe specific popu- We named this group of cells and the transcriptional state they rep-
lations. Overall, we profiled 80,108 cells in this study using MARS- resent the ‘haematopoietic core’. We then enhanced the resolution
seq to simultaneously capture RNA and key surface markers across around the core, by additional sequencing of 2,524 cells further
several tiers (Supplementary Fig. 1c–i and and Supplementary depleted of differentiated contaminants (tier 5: Lin− CD19− NK1.1−
Table 1). Our design included 1,901 cells sorted from whole bone CD71− CD24− CD11c− MHC-II− Siglec-H− CD22− FcgR− c-Kit+),
marrow (tier 1, Fig. 1b), 1,878 cells depleted of mature haema- 1,812 LSK cells (tier 6: Lin− c-Kit+ Sca-1+) and 704 HSC (tier 7: Lin−
topoietic cells expressing classical lineage markers (tier 2: Lin−; c-Kit+ Sca-1+ CD34− Flt3− CD150+)45, and recomputed a meta-cell
Fig. 1c) and 12,051 cells that were further enriched for progeni- model for a combined core data set (Fig. 3a,b and Supplementary
tor and stem cell subpopulations42 (tier 3: Lin−, c-Kit+; Fig. 1d). Fig. 4b,c). To identify the most transcriptionally naive stem cell state
The low depth analysis of tier 1 or 2 allowed us to put progenitors in the map we focused on sorted HSCs (tier 7), which were further
and stem cell populations into context (Supplementary Fig. 2). We purified in silico by excluding cells mapping to meta-cells with ini-
identified tier 3 differential genes as those showing expression dis- tial activation of differentiation markers (Fig. 3c and Supplementary
tributions peaking significantly in a small fraction of the sampled Fig. 4d). We identified Hlf46,47 as the only transcription factor
population (see Methods and Supplementary Fig. 3a–c). We then linked with highest enrichment in HSCs (more than fivefold
used the MetaCell pipeline (Supplementary Note 1) to identify higher; P < 1 × 10−15, Mann–Whitney test; Supplementary Fig. 4e).
homogeneous groups of cells (meta-cells) consisting of 29–183 cells We then searched directly for genes correlated with Hlf expres-
and 34,071–1,210,878 RNA molecules per group to facilitate robust sion at single cell resolution (Fig. 3d and Supplementary Table 2),
quantitative analysis (Fig. 2a). Bootstrap analysis was used to con- characterizing a gene module associated with the most naive HSC
firm meta-cell reproducibility and identify large-scale clusters in state (for example, Ly6a/Sca1, Ifitm1)11,47. We note that, unlike Hlf,
the data (Supplementary Fig. 3d,e). which is HSC-specific, some of the observed naive HSC genes are
Using the expression of 15 established lineage markers reused in more mature fates. For example, Ifitm1, a gene associ-
(Supplementary Fig. 3f) we associated 82% of the cells with spe- ated with cell quiescence48, is strongly co-expressed with Prss34 and
cific lineage fates (Supplementary Fig. 3g), and 18% of the cells were other basophil genes, possibly due to the relatively non-proliferative
classified as early progenitors (Fig. 2a,b). Our reference map of hae- basophil state. Defining developmental relatedness in the data based
matopoiesis includes B cell (marked by Vpreb1 and Fcrla), innate on transcription profiles must therefore be approached cautiously.
lymphocyte (ILC, Ccl5), erythrocyte (Hba-a2 and Car1), monocyte We defined the HSC signature by pooling the single-cell expres-
(Ly86 and Csf1r), macrophage (C1qb), neutrophil (Gstm1, Fcnb and sion of the Hlf-correlated naive HSC gene module (stem-score,
Ltf), conventional dendritic cells (cDC, Cd74), plasmacytoid (pDC, Fig. 3e,f). As expected we found that high-stem-score cells are
Siglech), basophil (Prss34), eosinophil (Prg2) and megakaryocyte defined by low proliferation (Fig. 3g and Supplementary Fig. 4f).
(Pf4) progenitors. Interestingly, we observed a transcriptional con- We next analysed data from a label retention assay48 involving dox-
tinuum connecting all lineages, with the exception of B-cell progen- ycycline-inducible inhibition of H2B-GFP expression in six mice
itors and innate lymphocytes (Fig. 2c and Supplementary Fig. 3h). followed by analysis of green fluorescent protein (GFP) retention
We projected recorded fluorescence-activated cell sorting (FACS) in progenitor cells collected after 150 days (Supplementary Fig. 4g).
surface marker levels onto our reference map, and performed We found that genes defining the naive HSC gene module were
in silico gating to align the map with known functional classes expressed in the label retaining CD150+ CD48− HSCs and down-
(Fig. 2d and Supplementary Fig. 3i,j). We found multipotent pro- regulated in cells that lost GFP expression (Supplementary Fig. 4h).
genitors (MPPs), short-term (ST) and long-term (LT) HSCs17,43,44 Together, our data define and validate a unique quiescent transcrip-
to be co-localized with specific transcriptional clusters at the core tional footprint for the naive HSC state.
of the projected map. We inferred variable proliferation intensities
across the map by pooling the expression from genes associated Transcriptional bifurcation along the HSC exit from quiescence.
with cell cycle (Fig. 2e and Supplementary Table 2). Together, the Strong antagonistic expression patterns of gene modules are char-
detailed and unbiased profiling of progenitor transcriptional states acteristic of lineage bifurcations49,50 driven by lineage transcription
in the bone marrow with recorded surface markers form a detailed factors. To examine if such mechanisms are observed in the earliest
and unbiased reference model for haematopoiesis, which is readily HSC lineage decisions we stratified cells by their stem-score and
extendible by enrichment and perturbation strategies, as demon- studied the build-up of coordinated lineage specific expression in
strated in the following sections. stem cells as they exit the naive state. Pairwise gene correlations in
NATuRe CeLL BIoLoGY | VOL 20 | JULY 2018 | 836–846 | www.nature.com/naturecellbiology 837
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
ResouRce NaTuRe Cell BIOlOgy
2
1
0
10 100 10 100 10 100 10 100 10 100 10 100 10 100 10 100 10 100 10 100 10 100
Pf4 Car1 Hba-a2 Ly86 Gstm1 Ltf Prss34 Cd74 Siglech Vpreb1 Ccl5
Proliferation-score
cells within the top five stem-score percentiles (group I) showed progenitor program. Together, our analysis suggests that tran-
lack of strong antagonistic gene modules, as well as a weak initial co- scriptional plasticity is initially retained in naive HSCs, and that
expression of lymphoid/myeloid genes (Dntt, Mpo, Igh) (Fig. 4a). low and uncorrelated expression of lineage genes is unlikely to
Cells that started to egress from the naive HSC state (groups II–III) indicate hierarchical fate commitment (Supplementary Fig. 4j).
developed two strongly negatively correlated gene modules associ- Importantly, Vpreb1 expressing B-cell progenitor populations
ated with either an erythrocyte (for example, Car1, Apoe, Gata2) (Fig. 1) are not Flt3 positive and cannot be linked with the tran-
or a joint lymphoid–myeloid (for example, Flt3, Cd34, Igh, Dntt, scriptional variation of lymphoid states found in the core model
Cd52, Mpo) program (Fig. 4b,c). We identified a strong separa- (Supplementary Fig. 3h). Their developmental dynamics in the
tion between the erythrocyte and myeloid–lymphoid programs17, bone marrow or outside it therefore remains difficult to assess
but could not identify groups of cells with early transcriptional using scRNA-seq data alone. In contrast, the megakaryocyte pro-
separation of myeloid and lymphoid progenitors. For example, grams are linked with a core population showing strong stem-ness,
Flt3-expressing cells with intermediate stem-scores co-expressed supporting their possible very early bifurcation51.
Mpo, Cd52, Sfpi1 (PU.1), Eltd1 and additional myeloid progeni-
tor factors (Fig. 4d,e and Supplementary Fig. 4i), alongside Dntt, Lineage cytokines relax HSC quiescence before triggering differ-
Igh, Satb1 and other genes that are the hallmark of the lymphoid entiation. To perturb in vivo the stem cell differentiation landscapes,
ytisneD
a b
Ifitm1
Ifitm3
Txnip
Pf4 Vpreb1
Cd34
Flt3 Hba-a2
Gata1
Car2
Mt2
Car1
Hba-a2 Car1
Hbb-b1
Fcgr3
Ctsg
Mpo
L L y6 y8 c2 6 Pf4 Siglech
F13a1
Csf1r
Lyz1 E ;L la y n z2 e Prss34
Fcnb
G C s a t m m p 1 Ccl5
Ltf
Pr C s d s 6 3 3 4 Prg2
Prg2
Cd74 Cd74
H2-Aa
Ly6d Ly86 Sig D le n c t h t 8.2 Fcnb Gstm1 Fcrla
Vpreb1 Vpreb3
Cd79b
Fcrla Ltf
Ccl5
Nkg7
C1qb
0
c d
Pf4 Car1 Fcnb Prss34 LT ST MPP
Hba-a2 Csf1r Siglech Cd74 MEP CMP GMP
e
IMU
dezilamron
gol
Max
Min
ytisned
IMU
C1qb
Fig. 2 | Characterization of lineage-primed haematopoietic progenitors. a, MetaCell analysis of 12,051 tier 3 single cells. Colour bar: annotation of meta-
cells into functional populations (see Methods). b, Two-dimensional (2D) projection of cells onto a graph representation of the meta-cells. c, Expression
of key marker genes on top of the 2D visualization. d, FACS-based conventional haematopoietic progenitor populations (Supplementary Fig. 3i,j) projected
onto the 2D graph. e, Distribution of the pooled expression of cell cycle related genes (proliferation-score, Supplementary Table 2) across different
progenitor populations, determined by the expression of lineage markers.
838 NATuRe CeLL BIoLoGY | VOL 20 | JULY 2018 | 836–846 | www.nature.com/naturecellbiology
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
NaTuRe Cell BIOlOgy ResouRce
a b Cd74 c Tier 7 HSC
Ly86
Stringent (61%)
3: c-Kit+ Lin– 5: c-Kit+ extended Lin– Others (39%)
Mpo
Siglech
All
Filtered
Dntt
6: LSK 7: HSC
Lmo4
All
0 0.5 1 0 0.5 1 Car1 Apoe Pf4
Frequency
d e
Ly6a
AK079675
Rbp1 1 20
Ifitm1 Expression quantile
Myct1
Procr
Serpina3f
Pdzk1ip1 0.05
Cd274
Ptplad2
Tgtp2
Txnip Leprel2 0.03
Mecom
Mllt3
Ldhb
Gimap6
Plk1s1 0.01
Marveld2
Oasl2
Stem-score Proliferation-score 0 0.4 0.8 1.2
Hlf+/Hlf– fold change (log)
2
we treated mice with Epo and G-CSF (Supplementary Fig. 5a–c), of the naive HSC signature was consistently reduced in both stimuli,
which are known to induce erythropoiesis and granulocyte produc- and the overall response to Epo and G-CSF was correlated (Fig. 5k
tion, respectively50,52,53. Expression of Epor and Csf3r, the receptors and Supplementary Fig. 8e). Importantly, genes implicated with dif-
for Epo and G-CSF, in tier 3 (Lin− c-Kit+) untreated cells highlights ferentiation to either fate were induced in naive HSCs in a cytokine-
potentially responsive single-cell populations in the c-Kit populations independent manner. These data support the downregulation of a
(Fig. 5a,b). We profiled 1,582 c-Kit+ cells from Epo-treated mice stem cell quiescent program as preceding the increase of differen-
(n = 4) and projected their transcriptional states onto the reference tiation potential through unspecific activation of haematopoietic
map, colour-coded according to their enrichment relative to con- lineage gene expression50. Activation of downstream differentiation
trols (Fig. 5c). This showed an increase of early erythrocyte pro- programs can then occur in ligand-receptor positive cells that develop
genitor clusters (marked by Car1, P ≪ 1 × 10−5 by Fisher’s exact test). (initially non-specifically) in the relaxed HSC population.
Accumulation of these progenitors did not reduce the fraction of
myeloid progenitors in the bone marrow, but was correlated with Initiation of neutrophil and monocyte transcriptional programs.
depletion of B-cell progenitors (marked by Vpreb1, P ≪ 1 × 10−5; To focus on initiation of the myeloid and lymphoid programs we
Fig. 5d and Supplementary Fig. 8d). Similarly, profiling and map- expanded our cohort of myeloid and lymphoid progenitors with
ping to our model of 1,438 c-Kit+ cells from G-CSF-treated mice 1,838 additional Lin− CD19− NK1.1− CD71− c-Kit+ cells (tier 4), for
(n = 3) showed an increase in neutrophil signatures (marked by Fcnb; which we recorded monocyte and DC surface markers described
P ≪ 1 × 10−5), and depletion of late erythrocyte and B-cell progenitors in the literature54–57 (Supplementary Fig. 6a−d ). We then re-
(P < 0.001), but not of earlier erythrocyte progenitors (Fig. 5e,f and analysed the single-cell data depleted in silico from cells specifically
Supplementary Fig. 8d). Interestingly, we observed increased Ifitm1 expressing markers of B cells, ILC, erythrocytes and basophiles (see
expression, typically marking the HSC quiescent state in early eryth- Methods) and visualized the resulting meta-cells on the reference
rocytes or myeloid progenitors following Epo or G-CSF treatments, map (Fig. 6a and Supplementary Fig. 6e). We found a complex net-
respectively (Fig. 5g,h, P ≪ 1 × 10−5, Fisher exact test). work of transcriptional states, making simple hierarchical models
To study the effects of these stimulations on naive HSC gene pro- difficult to support. Genes associated with lymphoid (Dntt, Flt3,
grams, we sorted and sequenced additional tier 7 HSCs following Ly6d), pDC (Siglech, Cd7), cDC (Itgb7, Naaa), monocyte (Csf1r,
both stimulations and mapped these cells to the reference core map F13a1) and neutrophil (Elane, Fcnb) fates showed mixed and par-
(427 Epo and 270 G-CSF cells, Fig. 5i,j). We found that the expression tially overlapping expression profiles over meta-cells (Fig. 4a).
ytisneD
Filtered
f g
Stringent HSC
Core cells
Percentile I II III
0 10 20 30 40 50
Stem-score
Fig. 3 | Identification of a transcription program associated with dormant stem cells. a, In silico filtering of lineage primed cells from the different
tiers (Supplementary Fig. 4a). Colours represent annotation by expression of lineage markers as in Fig. 1b–d b, MetaCell analysis and 2D projection
of 9,307 core single cells grouped into 50 meta-cells (Supplementary Fig. 4b,c). Cells are coloured by functional markers. c, Projection of HSCs (tier
7: 667 cells) onto the core model. Colours indicate stringent definition of tier 7 cells (406 cells; Supplementary Fig. 4d). d, Differential expression of
genes highly correlated with Hlf expression. Values represent log fold change between cells with and without Hlf expression. e, Distribution of the stem
2
cell transcriptional signature (stem-score; Supplementary Table 2) across all core cells, or stringent HSCs (as in c). f,g, Projection of the stem (f) and
proliferation (g) transcription signatures onto the core model.
NATuRe CeLL BIoLoGY | VOL 20 | JULY 2018 | 836–846 | www.nature.com/naturecellbiology 839
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
ResouRce NaTuRe Cell BIOlOgy
a b c
III: 95–100% II: 80–95%
percentile percentile
Dntt Dntt Dntt
Flt3 Flt3 Flt3
Cd52 Cd52 Cd52
IGH IGH IGH
H2afy H2afy H2afy
Mpo Mpo Mpo
Car1 Car1 Car1
Car2 Car2 Car2
Itga2b Itga2b Itga2b
Gata2 Gata2 Gata2
Apoe Apoe Apoe
d e
Ifitm1 Gpr56 Apoe Hlf Gata2
Car1 Eltd1 Cd52 Klf1 PU.1
Flt3 Dntt Mpo Satb1 Irf8
9
1
Transcription factors (Irf8, Cebpa, Cebpe, Sfpi1 (PU.1) and Satb1) of the neutrophil program, and Cebpe peaking in the fully mature
showed similarly complex and overlapping expression profiles granulocytes (Fig. 6h). Similar analysis for the monocyte signature
(Fig. 6b). To understand the dynamics of lineage-specific tran- (Fig. 6i,j) identified a gradual increase in monocyte genes (Fcer1g,
scriptional programs within such a complex mixture of progeni- F13a1) and allowed for the identification of potential antagonistic
tor states, we scored neutrophil and monocyte transcriptional transcription factors involved in monocyte and granulocyte differ-
signatures by pooling the expression of neutrophil- or monocyte- entiation (Supplementary Fig. 6g). In summary, our data suggest
specific gene modules (Fig. 6c,d and Supplementary Table 2) and that quantitative activation of the lineage-specific transcriptional
visualized these lineage-specific programs over the reference map programs for neutrophils and monocytes can be traced in early pro-
(Fig. 6e,f). We could not identify meta-cells with intermediate lev- genitors, despite their complex structure, and potential plastic dif-
els of both monocyte and granulocyte programs (Supplementary ferentiation trajectories that characterize their transcriptional space.
Fig. 6f). Importantly, even though our scoring is based on the selec-
tion of highly enriched lineage genes alone (for example, Ngp), we Dynamic role of PU.1 in neutrophil and monocyte d ifferentiation.
observed negatively correlated dynamics in HSC/progenitor genes We used CRISP-seq perturbations to characterize in single cell reso-
(Cd34, Gpr56, Eltd1), and transient dynamics for genes associated lution the regulation of neutrophil and monocyte cell fate differ-
with early granulocyte differentiation (Elane, Mpo, Gstm1; Fig. 6g). entiation. We collected LSK cells (tier 6, 50,000 cells per recipient
The transcription factors enriched in the process also showed varied mouse) from Cas9-GFP donor mice and infected them with a pool of
dynamics, with Gfi1 peaking in cells with intermediate activation blue fluorescent protein (BFP)-tagged guide RNA (gRNA) t argeting
noisserpxE
elitnauq
I: 60–80%
percentile
–0.38 0.38
Spearman
Fig. 4 | exit from the HSC state is characterized by a myeloid–erythrocyte bifurcation. a–c, Gene pairwise Spearman correlation within the 95–100th (a),
80–95th (b) and 60–85th (c) percentiles of the stem-score. Upper maps show projection of corresponding cells onto the core model: n = 347 (a), 1,040
(b) and 1,388 (c) single cells. d,e, Expression patterns of prominent marker genes (d) and transcription factors (e) on the core model.
840 NATuRe CeLL BIoLoGY | VOL 20 | JULY 2018 | 836–846 | www.nature.com/naturecellbiology
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
NaTuRe Cell BIOlOgy ResouRce
Epor 48 h Epo
3
2
1
0
–1
–2
Csf3r 48 h G-CSF
3
2
1
0
–1
–2
major myeloid transcription factors (Supplementary Table 3). analysis on Cas9-GFP+ BFP+ Lin− c-Kit+ cells, measuring both
We then transplanted infected cells into lethally irradiated recipi- the gRNA and transcriptome in the same single cell41 (Fig. 7a).
ent mice (see Methods). After 9–11 days we performed CRISP-seq Projecting the BFP+ gRNA infected donor single-cell transcription
dlof
lortnoc/FSC-G
egnahc
dlof
lortnoc/opE
) 2 gol(
egnahc
a c d g
Car1 ( P<<1 × 10–5 H G ) b s a t - m a2 1
V
L (
p
P y re 8 = b 6 1 0 . ( 0 P 4 ) < F < c 1 n × b 10–5)
b e f h
Hba-a2 ( P<< C 1 a r × 1 10 F –5 c ) n V b L p y ( r 8 P e 6 G < b < s 1 t 1 m ( P × 1 = 1 0 3 –5 × ) 10–5)
i
gol
- 1mtfiI
2
)lortnoc
/ opE(
1.5
1
0.5
0
Hba-a2 L ( P y C 8 G = 6 a s 0 r t ( 1 m . P 0 1 0 = 0 F ( 0 5 P c . ) < 0 n < 0 b 1 0 ( 2 P × ) = 1 0 1 –5 × ) 10–4 V ) preb1
gol
-
1mtfiI
2
)lortnoc
/FSC-G(
*** * ***
*** *
** ** *** ** 1.5
*** *** **
1
0.5
Max
0
Min
ytisned
IMU
Max
Min
tnemhcirnE
j k
48 h Epo 48 h G-CSF 2
1
0
–1
)gol(
egnahc
dlof
–/+opE
2
Max
Min
–2 –1 0 1 2
G-CSF+/– fold change (log)
2
tnemhcirnE
Car1 ( P <<1 × L 1 y 0– 8 5 6 H ) b ( P a - = a 2 0.001 G ) st m1 Fcn V b preb1
121 genes
7% 36%
Rps25 Car1
53% 4%
Rps24 Mt1
B2m Ctla2a
Mt2
Tmsb4x Gas5 Pccb
Rpl9
Rpl19
Rpl13
Prtn3
Slc18a2
Dlk1
Stmn1
Tspan31
Mycn
Stat1
H2-Aa Myc
Cd74 Tgtp2
Ywhae
Pdia3
Fig. 5 | Stimulation by different cytokines activates a convergent exit from the HSC state. a,b, Expression of haematopoietic cytokine receptors Epor and
Csf3r across the tier 3 model (Fig. 2b). c, c-Kit+ cells (tier 3) were collected from n = 4 mice treated with Epo for 48 h and projected onto the tier 3 model
(Fig. 2b and Supplementary Fig. 5). Colour coding represents map regions enriched over PBS-injected control. d, Bar plots showing enrichment of lineage-
annotated groups following Epo treatment compared to PBS-injected control. n = 4 mice. Values represent log 2 fold change between cytokine- and PBS-
treated mice. Error bars represent 95% confidence intervals. e,f, As in c and d but for n = 3 mice treated with G-CSF for 48 h. g,h, Changes in expression of
the stem cell marker Ifitm1 across lineage-annotated populations following Epo (n = 4 mice) (g) and G-CSF (n = 3 mice) (h) treatments. Values represent
log fold change between cytokine- and PBS-treated mice. i,j, Projection of HSC (tier 7) following 48 h of Epo (i) and G-CSF (j) treatments onto the core
2
model (Fig. 3b). k, Differential gene expression between treated and untreated stringent HSCs (as in Fig. 3c; values represent log fold change) after 48 h
2
Epo (x axis) and G-CSF (y axis) treatments. Inset, Fraction of differentially expressed genes (fold change > 2) in each quartile. n = 1,582 (Epo-treated),
n = 1,438 (G-CSF-treated), n = 717 (Epo control) and n = 457 (G-CSF control) single cells. P values represent false discovery rate (FDR)-adjusted two-sided
Fisher’s exact test. *P < 0.05; **P < 0.001; ***P < 1 × 10−5.
NATuRe CeLL BIoLoGY | VOL 20 | JULY 2018 | 836–846 | www.nature.com/naturecellbiology 841
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
ResouRce NaTuRe Cell BIOlOgy
Gpr56 Dntt Flt3 Ly6d
Siglech Cd7 Itgb7 Naaa
Csf1r F13a1 Elane Fcnb
Irf8 Cebpa Cebpe PU.1 Satb1
Elane Cebpe
1.2
20
Ltf
Ngp 0.8
Lcn2
C C d a 1 m 77 p 10 0.4 S100a9
Chi3l3 1100001G20Rik Ifitm6 0 0 Chi3l1 Itgb2l Pglyrp1 Ngp Gfi1 S100a8 O L r r m g 1 1 80 0.15
Fcnb AK028782
Gp1bb 0.1
Lyz2 40
Syne1
0.05
0 6
Neutrophils/rest 0 0
fold change (log)
2
Neutrophil signature in meta-cell (log )
10
Fcer1g Irf5
1.5 0.2
1
0.1
0.5
F13a1 Klf4 1.2 0.3
0.8 0.2
0 2 0.4 0.1
Monocytes/rest
0 0
fold change (log)
2
Monocyte signature in meta-cell (log )
10
profiles onto the reference map, we reproduced the early progeni- Fig. 7a–c). In this relatively early time point of transplantation,
tors, erythrocyte, neutrophil, basophil, monocyte and B cell states we did not detect several populations including pDC and ILC. As
observed in normal haematopoiesis (Fig. 7b and Supplementary transplantation experiments are known to suffer from clonal biases,
llec-atem
ni noisserpxe
dezilamroN
llec-atem
ni noisserpxe
dezilamroN
a
8 41.6
Median stem
score
b
Max
Min
c e g h
d f i j
F13a1
Ms4a6c Ly6c2
Ly6c1 S100a4
Tifab Rassf4
Klf4 Csf1r Glipr1 Hpse
Ly86
Trem2 Prdx4 Emb
Tcfec
Ass1
Papss2 Ctss Slpi
ytisned
IMU
Single cells
Ifitm6
Chi3l3
S100a9
Ngp
Syne1
S100a8 Orm1 Chi3l1
Ltf Cdcrel-1 Lrg1 Pglyrp1 Itgb2l Camp Cd177 Lcn2 Fcnb Mpo
Elane Gstm1
Ifitm1
Gpr56
Cd34
Eltd1
Serpina3f
0 7.7 5 50 500 5 50 500
Log normalized UMI
Single cells
Papss2 Ass1
Tcfec Trem2
Rassf4 Ly6c2
Ms4a6c F13a1
Ctss Klf4 S100a4 Slpi Prdx4
Hpse
Tifab Csf1r Ly86
Emb
Glipr1
Irf8 Elane Ifitm1 Gpr56
Cd34 Eltd1
Serpina3f
0 5.5 10 20 10 20
Log normalized UMI
Fig. 6 | Initiation of neutrophil and monocyte transcriptional programs. a, MetaCell analysis of 8,395 single cells from tiers 3 (c-Kit+), 4 (Lin− CD19− NK1.1− CD71−
c-Kit+, Supplementary Fig. 6a) and 5 grouped into 36 meta-cells. Meta-cells were projected onto Fig. 2b graph model, and are coloured by median stem-score.
Insets, Expression of prominent marker genes across the myeloid map. b, Expression of transcription factors across the myeloid map. c,d, Enrichment (log fold
2
change) of most differentially expressed genes between neutrophil and non-neutrophil meta-cells (defining the neutrophil score, c), and between monocytes
and non-monocyte meta-cells (defining the monocyte score, d; Supplementary Table 2). e,f, Expression of neutrophil (e) and monocyte (f) scores on meta-cells,
stratified into four expression levels. g, Single-cell gene expression profiles along the neutrophil differentiation axis. h, Pooled meta-cell expression of key neutrophil
genes along the neutrophil differentiation axis. i,j, Gene expression of single cells and meta-cells along the monocyte developmental trajectory, as in g and h.
842 NATuRe CeLL BIoLoGY | VOL 20 | JULY 2018 | 836–846 | www.nature.com/naturecellbiology
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
NaTuRe Cell BIOlOgy ResouRce
we expected that single cells sharing a gRNA barcode (gRNA-clone) the bone marrow (Supplementary Fig. 8a). To further examine this
could represent monoclonal or oligo-clonal populations. We found effect in a setting not affected by competition with other gRNA, we
a significant (P = 0.022, Kolmogorov–Smirnov test) imbalance in infected LSK cells separately with either PU.1 gRNA labelled with
the fates of control gRNA-clones towards erythroid and myeloid mCherry, or control gRNA labelled with BFP, and transplanted a
fates (Fig. 7c, compared to shuffle control in Fig. 7d; Supplementary mix of equal numbers of PU.1 KO and control donor cells into four
Fig. 7d), suggesting gRNA-sharing cells are in many cases monoclo- recipient mice. After 11 days, cells were analysed by flow cytome-
nal. To experimentally control for this clonal effect, we supported try, showing that donor cells were highly enriched for PU.1 gRNA
all analysis below using statistical analysis across multiple mice and infected cells, compared to control gRNA (10.6-fold; P < 0.05 by
batches (see Methods). two-tailed, paired Student’s t-test, Fig. 8a). However, PU.1 KO cells
Of the 12 genes used in our screen (22 gRNA), three genes had failed to generate Ly6G+ CD11b+ neutrophils, containing instead a
a significant effect compared to control gRNA (Supplementary large population of Ly6G+ CD11b− cells, not found in the control
Fig. 7e). Analysing populations of cells with gRNA targeting Cepba gRNA or homeostatic bone marrow59,60 (Fig. 8b,c and Supplementary
and Irf8, we found that Cebpa loss of function leads to the depletion Fig. 8b). MARS-seq analysis of cells from the same mice, sorted for
of both monocyte and neutrophil fates and Irf8 depletion strongly Lin− c-Kit+ and Ly6G+ gates, revealed marked differences between
affected monocyte, but not neutrophil development (Fig. 7e, PU.1 KO cells and control (Fig. 8d and Supplementary Fig. 8c). These
marked by Ly86 and Gstm1 expression, respectively). We observed included higher expression of genes critical for neutrophil differen-
that loss of monocyte potential in Irf8-deficient gRNA-clones tiation and function (Mmp8, Itgam, Il1b and Ccl6; Fig. 8e). To better
also correlated with increase in the Gstm1-marked neutrophils understand the effect of the knockout on neutrophil differentiation,
(Supplementary Fig. 7f), suggesting that loss of Irf8 and blocked we projected PU.1 KO and control meta-cells onto our derived neu-
monocyte differentiation may result in compensatory activation of trophil differentiation signature (stage I; Fig. 6c), and on a mature
genes linked with other fates. neutrophil signature defined by genes upregulated in the most dif-
According to consensus myeloid differentiation models, PU.1 ferentiated neutrophil population (stage II; Supplementary Fig. 8d).
is the master regulator of all myeloid lineages58. Surprisingly, PU.1 This showed that the initial increase in neutrophil differentiation is
knockout (KO) in Lin− c-Kit+ Sca-1+ (LSK) haematopoietic pro- independent of PU.1, but further neutrophil maturation and activa-
genitors resulted in the accumulation of neutrophil progenitors in tion of stage II genes is completely blocked in PU.1 KO (Fig. 8f).
noitubirtsid
epyt
lleC
noitubirtsid
epyt
lleC
a Cas9-GFP BM donor
Wild-type recipient
9–11 days
Infection of Transplantation CRISP-seq
LSK gRNA-UGI library
16 h
b c d
1 1 No marker
Pf4
Car1
Mt2
Hba-a2
Ly86
Gstm1
0.5 0.5
Fcnb
Camp
Prss34
Prg2
Cd74
Vpreb1
0 0 Ccl5
Control gRNA-clones Control gRNA-clones
(shuffled)
e
Car1 Ly86 Gstm1
P = 0.03
P = 0.01 P = 0.01 P = 0.0001
1
0.1
0.01
Control
Cebpa
K O
Irf8
K O Control
Cebpa
K O
Irf8
K O Control
Cebpa
K O
Irf8
K O
ni
ycneuqerF
enolc-ANRg
Fig. 7 | Hierarchy of myeloid regulators revealed by CRISP-seq. a, Schematic of the CRISP-seq experiment. b, Projection of 23,641 donor-derived (GFP+)
c-Kit+ cells infected with 21 different gRNA (BFP+, Supplementary Fig. 7a,b, mix 1 and mix 2 in Supplementary Table 3) onto the haematopoietic model
(Fig. 2b). c,d, Imbalance of the cellular output in CRISP-Seq experiments (c) compared to the expected distribution from a shuffled matrix (d). Each
column represents the lineage output of all cells sharing a unique control gRNA combination (gRNA-clone) in a single recipient mouse. n = 27 clones over
17 independent animals. P = 0.02, two-sided Kolmogorov–Smirnov test. e, Frequencies of selected lineages (marked by Car1, Ly86 or Gstm1 as in Fig. 1) in
n = 31 Cebpa, n = 25 Irf8 or n = 50 control gRNA-clones. P values represent FDR-adjusted two-sided Mann–Whitney test.
NATuRe CeLL BIoLoGY | VOL 20 | JULY 2018 | 836–846 | www.nature.com/naturecellbiology 843
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
ResouRce NaTuRe Cell BIOlOgy
To validate that this effect is intrinsic to PU.1 and not due to Discussion
systemic effects, we infected LSK cells with the same constructs Multiple lines of evidence support the hypotheses that bone mar-
and cultured the progenitors ex vivo in monocyte (GM-CSF) row differentiation is by far less hierarchical and canalized in the
and granulocyte (G-CSF) differentiation media. Similar to the in Waddington sense than previously assumed. Although HSCs are
vivo experiment, MARS-seq analysis revealed that PU.1 KO cells suggested to occupy specific niches in the bone marrow63,64, their
produced neutrophil progenitors arrested in stage I (Fig. 6g and downstream differentiation dynamics from the ground state have so
Supplementary Fig. 8e). However, the proliferation of these cells far been linked only to dynamic and complex microenvironments65,
was markedly different in the G-CSF versus GM-CSF supple- which serve as transient organizational units as cells migrate from
mented media: G-CSF, but not GM-CSF triggered a large expansion the bone marrow and further differentiate into other tissues. This
of the PU.1 KO neutrophil progenitors (Supplementary Fig. 8f). implies that haematopoietic progenitors are typically not protected
Importantly, GM-CSF could initiate the monocyte differentiation from receiving multiple signals early in their differentiation, includ-
program in PU.1 KO cells ex vivo, showing that the in vivo absence ing various inflammatory and other immune/metabolic signals, and
of monocytes is not intrinsically dependent on PU.1 function open the way for incomplete cell lineage sorting as a natural part
(Supplementary Fig. 8g,h). Taken together, our analysis shows that of their dynamics66,67. Because haematopoiesis is highly dynamic
initial differentiation into the granulocyte and monocyte lineages and adaptive, avoiding tightly regulated and irreversibly committed
is not dependent on PU.1. The aberrant CD11b− Ly6G+ neutrophil progenitor subpopulations and maintaining differentiation flexibil-
observed in PU.1 KOs exhibits morphological segmentation, but ity may increase the system responsiveness, as supported here by
failed to express several mature neutrophil genes, including genes the distribution of progenitor states following cytokine stimulation.
related to secondary and tertiary granule formation61,62 (Fig. 8h and Moreover, even as stem cells acquire a neutrophil, lymphocyte or
Supplementary Fig. 8i). erythrocyte progenitor state in the bone marrow, their plasticity is
rep
tnuoc
lleC
sllec
ronod
+9saC
000,1
a b c d e
Mmp8 Itgam
Control PU.1 KO
Ccl6
Control PU.1 KO Control PU.1 KO
f
b11DC
ronod
fo
b11DC
egatnecreP
sllec
+G6yL
devired PU.1
KO
Ly6G
b11DC
P = 0.03 P = 0.0003
Max
Control
Ly6G Min
ytisned
IMU
100 30
20
50 Il1b
10
0 0
g h
Ctsg Clu Orm1
4 Gstm1 Elane Serpine2
Nkg7
Thbs4
2 Spp1
0
–2
Il1b
Il1rn Capg Gsn
Myadm –4 Fpr2 Tyrobp
Chi3l3 Cc S l6 tfa2l1 Cybb Ltf Mmp9
Mmp8
–4 –2 0 2 4
In vivo (PU.1 / CTL) fold change (log)
2
)gol(
egnahc
dlof
)LTC
/
1.UP(
oviv
xE
2
485 genes
6% 38%
47% 9%
600 600
400 400
200 200
0 0
erutangis
lihportuen
I egatS
Sorting scheme Tier 3 Ly6G+
0 20 40 60 0 20 40 60 Stage II neutrophil signature
erutangis
lihportuen
I egatS
Cytokine GM-CSF G-CSF
Stage II neutrophil signature
Fig. 8 | Dynamic role of Pu.1 in neutrophil and monocyte differentiation. a, Frequencies of PU.1 KO gRNA and control infected cells in the GFP+ donor
populations. Values represent mean and error bars represent s.e.m.; two-tailed, paired Student’s t-test, n = 4 independent animals (Supplementary Table 5).
b, Representative FACS plot showing loss of CD11b surface marker expression in PU.1 KO Ly6G+ cells. See also Supplementary Fig. 8b. c, Quantification
of CD11b surface marker presence in Ly6G+ donor cells. Values represent mean and error bars represent s.e.m.; two-tailed, paired Student’s t-test, n = 4
independent animals (Supplementary Table 5). d, MetaCell analysis and projection of PU.1 KO and control single cells sorted from c-Kit+ and Ly6G+
populations. e, Projection of neutrophil specific genes onto the meta-cell 2D map. f, Meta-cell pooled expression of the neutrophil program as determined
in Fig. 6c–h (stage I; y axis) versus the exhausted neutrophil program derived from the in vivo CRISPR experiment (stage II; x axis; Supplementary Fig. 8d).
g, Ex vivo PU.1 KO (purple) and control gRNA infected LSK cells treated with GM-CSF (triangles) or G-CSF (squares). h, Differential gene expression
between PU.1 KO and control guide infected cells in the in vivo (x axis) and ex vivo (y axis) experiments. Values represent log fold change between KO and
2
control infected cells. Inset, Fraction of differentially expressed genes (fold change > 4) in each quartile.
844 NATuRe CeLL BIoLoGY | VOL 20 | JULY 2018 | 836–846 | www.nature.com/naturecellbiology
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
NaTuRe Cell BIOlOgy ResouRce
maintained and full commitment often established in other tissues 14. Spitzer, M. H. et al. An interactive reference framework for modeling a
(for example, thymus, spleen, blood) after migration68. dynamic immune system. Science 349, 1259425 (2015).
15. Guo, G. et al. Mapping cellular hierarchy byÿsingle-cellÿanalysis of the cell
Although the concept of plastic and network-like haematopoi-
surface repertoire. Cell Stem Cell 13, 492–505 (2013).
etic differentiation is far from new, the high-resolution prism facili- 16. Perie, L., Duffy, K. R., Kok, L., de Boer, R. J. & Schumacher, T. N. The branching
tated by scRNA-seq provides a detailed substitute for the traditional point in erythro–myeloid differentiation. Cell 163, 1655–1662 (2015).
coarse-grain tree models of haematopoietic differentiation. The 17. Adolfsson, J. et al. Identification of Flt3+ lympho–myeloid stem cells lacking
model we introduce here is initiated from transcriptional states and erythro-megakaryocytic potential a revised road map for adult blood lineage
commitment. Cell 121, 295–306 (2005).
their potential similarities, but the inference of dynamics on it must
18. Kondo, M. Lymphoid and myeloid lineage commitment in multipotent
be taken with caution and can only be fully resolved by adding the
hematopoietic progenitors. Immunol. Rev. 238, 37–46 (2010).
dimension of time (for example, pulse chase), sophisticated lineage 19. Gorgens, A. et al. Revision of the human hematopoietic tree: granulocyte
tracing, epigenomics and additional functional perturbations10,51,69. subtypes derive from distinct hematopoietic lineages. Cell Rep. 3,
Nevertheless, the map we outline represents a reference haemato- 1539–1552 (2013).
20. Paul, F. et al. Transcriptional heterogeneity and lineage commitment in
poietic differentiation model with resolution and reproducibility
myeloid progenitors. Cell 163, 1663–1677 (2015).
that facilitate the integration of all these additional layers of infor-
21. Naik, S. H. et al. Diverse and heritable lineage imprinting of early
mation and dynamics. We show that gene regulation continuously haematopoietic progenitors. Nature 496, 229–232 (2013).
repurposes genes across lineages and fates, bringing single cells 22. Notta, F. et al. Distinct routes of lineage development reshape the human
from different lineages closer in transcriptional space and poten- blood hierarchy across ontogeny. Science 351, aab2116 (2016).
23. Sanjuan-Pla, A. et al. Platelet-biased stem cells reside at the apex of the
tially skewing models for differentiation dynamics. By anchor-
haematopoietic stem-cell hierarchy. Nature 502, 232–236 (2013).
ing models on functionally characterized ground states (CD150+
24. Jaitin, D. A. et al. Massively parallel single-cell RNA-seq for marker-free
LT-HSC in our case), and by combining scRNA with stimulations decomposition of tissues into cell types. Science 343, 776–779 (2014).
(cytokines) and perturbations (CRISP-seq), we can highlight poten- 25. Grun, D. et al. Single-cell messenger RNA sequencing reveals rare intestinal
tial differentiation trajectories in the model and examine the regula- cell types. Nature 525, 251–255 (2015).
26. Zeisel, A. et al. Brain structure. Cell types in the mouse cortex and
tory mechanisms controlling them. The remarkable reproducibility
hippocampus revealed by single-cell RNA-seq. Science 347, 1138–1142 (2015).
of the inferred transcriptional states (between mice, in vivo as well
27. Habib, N. et al. Div-Seq: single-nucleus RNA-seq reveals dynamics of rare
as ex vivo stimulations and genetic perturbation) confirms that the adult newborn neurons. Science 353, 925–928 (2016).
scRNA-based model of haematopoiesis is becoming the ideal refer- 28. Treutlein, B. et al. Reconstructing lineage hierarchies of the distal lung
ence for future quantitative and functional analysis of the system, epithelium using single-cell RNA-seq. Nature 509, 371–375 (2014).
29. Scialdone, A. et al. Resolving early mesoderm diversification through
both in normal and disease states.
single-cell expression profiling. Nature 535, 289–293 (2016).
30. Han, X. et al. Mapping the mouse cell atlas by microwell-Seq. Cell 172,
Methods 1091–1107 (2018).
Methods, including statements of data availability and any asso- 31. Tanay, A. & Regev, A. Scaling single-cell genomics from phenomenology to
ciated accession codes and references, are available at https://doi. mechanism. Nature 541, 331–338 (2017).
32. Nestorowa, S. et al. A single-cell resolution map of mouse hematopoietic stem
org/10.1038/s41556-018-0121-4.
and progenitor cell differentiation. Blood 128, e20–e31 (2016).
33. Drissen, R. et al. Distinct myeloid progenitor-differentiation pathways
Received: 5 March 2018; Accepted: 11 May 2018;
identified through single-cell RNA sequencing. Nat. Immunol. 17,
Published online: 18 June 2018 666–676 (2016).
34. Schlitzer, A. et al. Identification of cDC1- and cDC2-committed DC
References progenitors reveals early lineage priming at the common DC progenitor stage
1. Orkin, S. H. & Zon, L. I. Hematopoiesis: an evolving paradigm for stem cell in the bone marrow. Nat. Immunol. 16, 718–728 (2015).
biology. Cell 132, 631–644 (2008). 35. Olsson, A. et al. Single-cell analysis of mixed-lineage states leading to a
2. Till, J. E. & Mc, C. E. A direct measurement of the radiation sensitivity of binary cell fate choice. Nature 537, 698–702 (2016).
normal mouse bone marrow cells. Radiat. Res. 14, 213–222 (1961). 36. See, P. et al. Mapping the human DC lineage through the integration of
3. Spangrude, G. J., Heimfeld, S. & Weissman, I. L. Purification and high-dimensional techniques. Science 356, eaag3009 (2017).
characterization of mouse hematopoietic stem cells. Science 241, 37. Velten, L. et al. Human haematopoietic stem cell lineage commitment is a
58–62 (1988). continuous process. Nat. Cell Biol. 19, 271–281 (2017).
4. Meuwissen, H. J., Gatti, R. A., Terasaki, P. I., Hong, R. & Good, R. A. 38. Tusi, B. K. et al. Population snapshots predict early haematopoietic and
Treatment of lymphopenic hypogammaglobulinemia and bone-marrow erythroid hierarchies. Nature 555, 54–60 (2018).
aplasia by transplantation of allogeneic marrow. Crucial role of 39. Zheng, S., Papalexi, E., Butler, A., Stephenson, W. & Satija, R. Molecular
histocompatibility matching. N. Engl. J. Med. 281, 691–697 (1969). transitions in early progenitors during human cord blood hematopoiesis.
5. Tho, E. D., Lochte, H. L., W, C. L. U. & Ferrebee, J. W. Intravenous infusion Mol. Syst. Biol. 14, e8041 (2018).
of bone marrow in patients receiving radiation and chemotherapy. 40. Sun, J. et al. Clonal dynamics of native haematopoiesis. Nature 514,
N. Engl. J. Med. 257, 491–496 (1957). 322–327 (2014).
6. Arinobu, Y. et al. Reciprocal activation of GATA-1 and PU.1 marks initial 41. Jaitin, D. A. et al. Dissecting immune circuits by linking CRISPR-pooled
specification of hematopoietic stem cells into myeloerythroid and screens with single-cell RNA-seq. Cell 167, 1883–1896 (2016).
myelolymphoid lineages. Cell Stem Cell 1, 416–427 (2007). 42. Ogawa, M. et al. Expression and function of c-kit in hemopoietic progenitor
7. Pronk, C. J. et al. Elucidation of the phenotypic, functional, and molecular cells. J. Exp. Med. 174, 63–71 (1991).
topography of a myeloerythroid progenitor cell hierarchy. Cell Stem Cell 1, 43. Morrison, S. J. & Weissman, I. L. The long-term repopulating subset of
428–442 (2007). hematopoietic stem cells is deterministic and isolatable by phenotype.
8. Schroeder, T. Hematopoietic stem cell heterogeneity: subtypes, not Immunity 1, 661–673 (1994).
unpredictable behavior. Cell Stem Cell 6, 203–207 (2010). 44. Yang, L. et al. Identification of Lin– Sca1+ kit+ CD34+ Flt3– short-term
9. Yamamoto, R. et al. Clonal analysis unveils self-renewing lineage-restricted hematopoietic stem cells capable of rapidly reconstituting and rescuing
progenitors generated directly from hematopoietic stem cells. Cell 154, myeloablated transplant recipients. Blood 105, 2717–2723 (2005).
1112–1126 (2013). 45. Kiel, M. J. et al. SLAM family receptors distinguish hematopoietic stem and
10. Lara-Astiaso, D. et al. Immunogenetics. Chromatin state dynamics during progenitor cells and reveal endothelial niches for stem cells. Cell 121,
blood formation. Science 345, 943–949 (2014). 1109–1121 (2005).
11. Cabezas-Wallscheid, N. et al. Identification of regulatory networks in HSCs 46. Shojaei, F. et al. Hierarchical and ontogenic positions serve to define the
and their immediate progeny via integrated proteome, transcriptome, and molecular basis of human hematopoietic stem cell behavior. Dev. Cell 8,
DNA methylome analysis. Cell Stem Cell 15, 507–522 (2014). 651–663 (2005).
12. Sawyers, C. L., Denny, C. T. & Witte, O. N. Leukemia and the disruption of 47. Riddell, J. et al. Reprogramming committed murine blood cells to induced
normal hematopoiesis. Cell 64, 337–350 (1991). hematopoietic stem cells with defined factors. Cell 157, 549–564 (2014).
13. Sykes, M. & Nikolic, B. Treatment of severe autoimmune disease by stem-cell 48. Cabezas-Wallscheid, N. et al. Vitamin A–retinoic acid signaling regulates
transplantation. Nature 435, 620–627 (2005). hematopoietic stem cell dormancy. Cell 169, 807–823 (2017).
NATuRe CeLL BIoLoGY | VOL 20 | JULY 2018 | 836–846 | www.nature.com/naturecellbiology 845
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
ResouRce NaTuRe Cell BIOlOgy
49. Laslo, P. et al. Multilineage transcriptional priming and determination of 67. Essers, M. A. et al. IFNα activates dormant haematopoietic stem cells in vivo.
alternate hematopoietic cell fates. Cell 126, 755–766 (2006). Nature 458, 904–908 (2009).
50. Huang, S., Guo, Y. P., May, G. & Enver, T. Bifurcation dynamics in lineage- 68. Rieger, M. A., Hoppe, P. S., Smejkal, B. M., Eitelhuber, A. C. & Schroeder, T.
commitment in bipotent progenitor cells. Dev. Biol. 305, 695–713 (2007). Hematopoietic cytokines can instruct lineage choice. Science 325, 217–218 (2009).
51. Rodriguez-Fraticelli, A. E. et al. Clonal analysis of lineage fate in native 69. Giladi, A. & Amit, I. Single-cell genomics: a stepping stone for future
haematopoiesis. Nature 553, 212–216 (2018). immunology discoveries. Cell 172, 14–21 (2018).
52. Metcalf, D. The granulocyte-macrophage colony-stimulating factors. Science
229, 16–22 (1985). Acknowledgements
53. Cohen, A. M. et al. In vivo stimulation of granulopoiesis by recombinant
The authors thank members of the Tanay and Amit laboratories for critical discussions.
human granulocyte colony-stimulating factor. Proc. Natl Acad. Sci. USA 84,
Research by I.A. and A.Ta. is supported by the Chan Zuckerberg Initiative. I.A. is supported
2484–2488 (1987).
by a Howard Hughes Medical Institute International Scholar Award, the European Research
54. Zhang, J. et al. Characterization of Siglec-H as a novel endocytic receptor
Council (309788), the Israel Science Foundation, the Ernest and Bonnie Beutler Research
expressed on murine plasmacytoid dendritic cell precursors. Blood 107,
Program of Excellence in Genomic Medicine, the Helen and Martin Kimmel award for
3600–3608 (2006).
innovative investigation, a Minerva Stiftung research grant, the Israeli Ministry of Science,
55. Fogg, D. K. et al. A clonogenic bone marrow progenitor specific for
Technology and Space, the David and Fela Shapell Family Foundation and the Abramson
macrophages and dendritic cells. Science 311, 83–87 (2006).
Family Center for Young Scientists. I.A. is the incumbent of the Alan and Laraine Fischer
56. Onai, N. et al. Identification of clonogenic common Flt3+ M-CSFR+
Career Development Chair. Research in the A.Ta. laboratory is supported by the European
plasmacytoid and conventional dendritic cell progenitors in mouse bone
Research Council, FAMRI, the I-CORE for chromatin and RNA regulation, and a grant
marrow. Nat. Immunol. 8, 1207–1216 (2007).
from the Israel Science Foundation. A.Ta. is a Kimmel investigator. A.G. is a recipient of the
57. Waskow, C. et al. The receptor tyrosine kinase Flt3 is required for dendritic cell
Clore fellowship. F.P. is a fellow of the German–Israeli Helmholtz Research School in Cancer
development in peripheral lymphoid tissues. Nat. Immunol. 9, 676–683 (2008).
Biology. This work was supported by the Deutsche Forschungsgemeinschaft (SFB873),
58. Scott, E. W., Simon, M. C., Anastasi, J. & Singh, H. Requirement of
the José Carreras Leukämie-Stiftung and the Dietmar Hopp Stiftung (all to A.Tr.).
transcription factor PU.1 in the development of multiple hematopoietic
lineages. Science 265, 1573–1577 (1994).
59. Anderson, K. L., Smith, K. A., Pio, F., Torbett, B. E. & Maki, R. A. Author contributions
Neutrophils deficient in PU.1 do not terminally differentiate or become A.G., F.P., A.Ta. and I.A. conceived the project and designed the experiments. F.P. performed
functionally competent. Blood 92, 1576–1585 (1998). the experiments. A.G. analysed the data. A.G., Y.H. and Y.L. developed computational
60. McKercher, S. R. et al. Targeted disruption of the PU.1 gene results in algorithms. F.P., A.W., I.Y. and D.J. implemented the CRISP-Seq pipeline. N.C-W. and A.Tr.
multiple hematopoietic abnormalities. EMBO J. 15, 5647–5658 (1996). contributed the label retention assay. R.D. and F.G. supplied evidence of myeloid fate choice.
61. Lominadze, G. et al. Proteomic analysis of human neutrophil granules. A.G., F.P., A.Ta. and I.A. wrote the paper. A.Ta. and I.A. supervised the project.
Mol. Cell Proteom. 4, 1503–1521 (2005).
62. Theilgaard-Monch, K. et al. The transcriptional program of terminal Competing interests
granulocytic differentiation. Blood 105, 1785–1796 (2005).
The authors declare no competing interests.
63. Zhang, J. et al. Identification of the haematopoietic stem cell niche and
control of the niche size. Nature 425, 836–841 (2003).
64. Mendez-Ferrer, S. et al. Mesenchymal and haematopoietic stem cells form a Additional information
unique bone marrow niche. Nature 466, 829–834 (2010). Supplementary information is available for this paper at https://doi.org/10.1038/
65. Cordeiro Gomes, A. et al. Hematopoietic stem cell niches produce s41556-018-0121-4.
lineage-instructive signals to control multipotent progenitor differentiation. Reprints and permissions information is available at www.nature.com/reprints.
Immunity 45, 1219–1231 (2016).
Correspondence and requests for materials should be addressed to A.T. or I.A.
66. Haas, S. et al. Inflammation-induced emergency megakaryopoiesis driven by
hematopoietic stem cell-like megakaryocyte progenitors. Cell Stem Cell 17, Publisher’s note: Springer Nature remains neutral with regard to jurisdictional claims in
422–434 (2015). published maps and institutional affiliations.
846 NATuRe CeLL BIoLoGY | VOL 20 | JULY 2018 | 836–846 | www.nature.com/naturecellbiology
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
NaTuRe Cell BIOlOgy ResouRce
Methods described previously24. To record marker levels of each single cell, the FACS Diva
Mouse strains. MARS-seq was performed on six- to eight-week-old female 7 ‘index sorting’ function was activated. During index sorting, the intensities
C57BL/6 mice. For cytokine-mediated in vivo challenge of native adult of all FACS markers were recorded and linked to each cell’s position within the
haematopoiesis, seven-week-old mice (~15 g) were injected intraperitoneally 384-well plate20. Four empty wells were kept in each 384-well plate as a no-cell
(i.p.) with 150 IU human Epo (Recormon/Epoitin beta; in 200 µ l PBS; n = 4, 3 control during data analysis. Immediately after sorting, each plate was spun down
independent experiments) or subcutaneously (s.c.) with 4.8 µ g human G-CSF to ensure cell immersion into the lysis solution, snap frozen on dry ice and stored
(Neupogen; in 100 µ l PBS; n = 3, 2 independent experiments) over two consecutive at −8 0 °C until processed.
days and killed on the third day together with their respective i.p. and s.c. injected
PBS controls. Cas9-GFP mice were purchased from The Jackson Laboratory and RNA-seq library preparation. Single-cell transcriptome libraries were prepared
backcrossed with C57BL/6 mice to produce homozygotes41. Animal studies were as previously described24. Briefly, mRNA from cells sorted into MARS-seq capture
performed without randomization or blinding. plates was barcoded and converted into cDNA and pooled using an automated
pipeline. The pooled sample was then linearly amplified by T7 in vitro
Ethical compliance. All animals were housed according to guidelines at the transcription and the resulting aRNA was fragmented and converted into a
Weizmann Institute of Science and the German Cancer Research Center. All sequencing-ready library by tagging the samples with pool barcodes and Illumina
experimental procedures were approved by the Institutional Animal Care and Use adapter sequences during ligation, followed by reverse transcription and PCR. For
Committee (IACUC), application no. 24120116-3. This work complies with all CRISP-seq, 12% of the in vitro transcription material was used for UGI-library
relevant ethical regulations pertaining to animal experiments. preparation as described previously41. Briefly, fragmentation was omitted, the
aRNA ligated to a common sequence that was used as a primer dock for reverse
Isolation of haematopoietic progenitors from bone marrow. Bone marrow was transcription, and a pool barcode and Illumina adapter sequences introduced
isolated from mouse tibiae, femora and ilia leg bones by crushing in MACS buffer during a two-step PCR to complete UGI-seq libraries. Library quality and
(PBS supplemented with 2 mM EDTA and 0.5% BSA) and filtered through a concentration were assessed as described in ref. 24. All MARS-seq/UGI-seq libraries
70 μ m cell strainer. Omitting enrichment, single-cell suspensions were stained for were sequenced using an Illumina NextSeq 500 at a median sequencing depth of
30 min on ice with fluorophore-conjugated antibodies, filtered through a 40 μ m 46,426 (2,125 UGI) reads per single cell.
cell strainer and FACS-sorted with a FACSAria Fusion cell sorter (BD Biosciences)
according to the sorting strategies listed in Supplementary Fig. 1b. Antibody clones Unique molecular identifier table generation. Sequences were demultiplexed,
and quantities (six hindleg bones per mouse were stained in 100 μ l MACS buffer) mapped and filtered as previously described20, extracting a set of unique
used for single-cell sorting are specified in Supplementary Table 4. molecular identifiers (UMIs) that define distinct transcripts in single cells for
further processing (1,718 median; Supplementary Table 1). We estimated the
CRISPR loss-of-function screening. gRNA oligos were ordered from iDT and level of spurious UMIs in the data using statistics on empty MARS-seq wells,
cloned into a guide RNA lentiviral vector plasmid as previously described41. Briefly, implicating between 0.5 and 10% (1.8% median) of the UMIs as potential cross-
pairs of oligonucleotides with BsmBI-compatible overhangs were phosphorylated well contamination. We note that such contamination should be considered
with T4 polynucleotide kinase (NEB) and annealed. The fragments were then when quantifying low expression levels of genes that are strongly expressed in a
ligated into a pool of purified BsmBI-digested CRISP-seq plasmids (BFP backbone subpopulation. We considered this potential bias in the MetaCell analysis (see
#85707, mCherry backbone #85708, Addgene) that contained a unique gRNA Supplementary Note 1 for a detailed explanation), and by excluding tier 3 cells
identifier41 (UGI). Ligated constructs were transformed into competent bacteria from correlation analysis in Fig. 4a–c.
and single clones were picked and propagated. Presence of a gRNA and unique
UGI was verified by Sanger sequencing. CRISP-seq-UGI lentiviral particles were Index sorting processing. FACS recorded surface markers were matched with
produced by transfection of 293T cells (jetPEI transfection reagent, Polyplus) single-cell labels based on well coordinate and combined into a unified data set.
followed by concentration in Amicon 100 kDa 15 ml columns (Millipore), as Different sorting tiers used a different combination of markers, such that not all
described previously41. cells were characterized by all indices. For virtual FACS gating we used established
For the in vivo CRISP-seq assay, bone marrow from Cas9-GFP donor mice sorting strategies found in the literature11,20,32,43,44,54–57 (Supplementary Figs. 2i and 6c).
was enriched for c-Kit (CD117) using magnetic cell separation (MACS, Miltenyi We compared overall FACS index distributions between sorting batches, confirming
Biotec) and FACS-sorted for GFP+ Lin− c-Kit+ Sca-1+ bone marrow progenitors. that sorting batch settings do not affect gate distributions.
Donor progenitors were infected with various combinations of lentiviral gRNAs
(Supplementary Table 3) in StemSpan Serum-Free Expansion medium (SFEM, Defining broadly expressed gene modules. Identification of ribosomal, cell
StemCell Technologies) supplemented with 1% penicillin/streptavidin, cycle, stress or other broadly expressed gene modules was done by clustering
2 μ g ml−1 polybrene, Flt3, Il-3, Tpo and stem cell factor (SCF) (all at 10 ng ml−1 genes in a downsampled UMI matrix (545 molecules per cell). We filtered
from Peprotech) for 18 h on a non-tissue culture treated 96-well plate41. Note that genes with a total molecule (UMI24) count lower than 5 and variance-to-
for the stringent PU.1 experiment, half the cells were infected with BFP+ control mean ratio lower than 1.2. Hierarchical clustering using Ward’s method was
guides and the other half with PU.1-mCherry (mixes 3 and 4 in Supplementary performed to detect 500 fine-grained clusters. After removing clusters with a
Table 3); both were combined before transplantation. Nine-week-old female mean Pearson intra-correlation lower than 0.05, 22 gene modules were retained.
C57BL/6 recipient mice were lethally irradiated (950 cGy) 18 h before retro-orbital Manual annotation of the gene clusters was performed and modules linked to
injection of 50,000 PBS-washed infected donor cells and 200,000 recipient isogenic the haematopoietic differentiation process were filtered. This resulted in the
flushed whole bone marrow carrier cells. Drinking water was supplemented with identification of eight modules with 10–74 genes associated with either cell cycle
200 mg ml−1 ciprofloxacin. or stress response for further processing.
For the ex vivo CRISP-seq assay, Cas9-GFP+ LSK cells were infected with PU.1-
mCherry and BFP+ control guides as described above. 10,000 PU.1-mCherry and UMI transformation and gene module score. For downstream analysis
10,000 control-BFP infected cells were cultured together for 5 days in StemSpan we normalized UMI statistics u′c g = (1,000/N c ) × uc g and transformed this as
supplemented with 10% FBS, 1% penicillin/streptavidin, SCF, Tpo and either murine vc g = log(1 + k u′c g ). Here k is an expansion parameter that heuristically accounts
GM-CSF (all at 10 ng ml−1 from PeproTech) or 10 ng ml−1 human recombinant G-CSF for the imperfect RNA recovery in scRNA data. The a posteriori gain in absolute
(Neupogen, Filgrastim) on non-tissue culture treated 24-well plates. Medium was expression between cells with 0 sampled UMIs and cells with 1 sampled UMI
topped up on day 4. On day 6, StemSpan was replaced with Iscove’s Base Medium for a gene is typically higher than the gain observed between 1 and 2 UMIs, or
(Biological Industries, Israel) while retaining all supplements listed above, and cells 2 and 4 UMIs. Transforming the data as described above partly compensates for
were re-seeded onto 24-well plates. On day 9, 50% of the cells were taken for FACS, this effect. In particular, k is set to conservatively bound 1/(sampling efficiency),
and the remainder were seeded on 12-well plates. After another medium top-up on to scale the expected number of RNA molecules given UMI observation
day 12, cells were analysed by flow cytometry on day 14. (informally, E(RNA|UMI = 0) ~ E(RNA|UMI = 1)/k). More refined approaches
for inferring the posterior probability of absolute RNA count from UMI
Giemsa staining. For May-Gruenewald Giemsa (MGG) staining, cells were FACS- statistics70 depend on parametric assumptions on the data, which we preferred
sorted into MACS buffer and concentrated in microscope slides by cytospin. Slides not to implement at this stage.
were air-dried and fixed in methanol for 5 min for long-term storage. Fixed and Given a set of genes G, the normalized gene module score e(G,c) is defined as
dried slides were stained for 5 min in May-Gruenewald solution (Sigma), rinsed the total normalized UMI u′c
g
over the genes in G. Similarly, the log gene module
briefly with PBS and stained with Giemsa (Sigma) for 40 min. Stained slides were score f(G,c) is defined as the sum of transformed vc values over the genes in G
g
rinsed under running tap water and air-dried for 10 min. Images were obtained and can be used to align cells on the expression levels of both weakly and highly
under a microscope with a × 100 objective, using immersion oil. expressed genes, and the goal is to maximize sensitivity.
Single-cell index sorting. Isolated cells were single-cell-sorted into 384-well cell MetaCell analysis and clustering. The MetaCell pipeline was used to derive
capture plates containing 2 µ l of lysis solution and barcoded poly(T) reverse- informative genes and compute cell-to-cell similarity, to compute K-nn graph
transcription (RT) primers24 for scRNA-seq. Barcoded single-cell capture plates covers and derive the distribution of RNA in cohesive groups of cells (or meta-
were prepared with a Bravo automated liquid handling platform (Agilent) as cells), and to derive strongly separated clusters using bootstrap analysis and
NATuRe CeLL BIoLoGY | www.nature.com/naturecellbiology
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
ResouRce NaTuRe Cell BIOlOgy
computation of graph covers on resampled data. The MetaCell package is expressed in these cells compared to the rest of the myeloid data set (χ2 test;
described in detail in Supplementary Note 1. Default parameters were used unless P < 1 × 10−9 with fourfold or higher change, Supplementary Table 2). We computed
otherwise stated. the neutrophil signature across clusters as the share of G expression from the
neut
total UMIs in each cluster.
Mapping cells to an existing MetaCell model. Given an existing reference single-cell Monocyte signature was defined similarly, comparing between high monocyte
data set and meta-cell model, and a new set of single-cell profiles, we extracted for clusters (two- and twofold enrichment of Csf1r and Ly86). We extracted a set of genes
each new cell the K reference cells with top Pearson correlation over the normalized G differentially expressed in monocytes compared to the rest of the myeloid data
ref mon
gene features defined for the reference model, as described in Supplementary Note 1. set (χ2 test; P < 1 × 10−9 with twofold or higher change, Supplementary Table 2).
The distribution of cluster memberships over these K-neighbours was used to
associate the new cell with a reference meta-cell (by majority voting) or to project CRISP-seq low-level processing. Sequenced reads containing the UGI-seq
the cell in 2D by weighted average of the linked reference clusters’ mapped x and y 5′ primer (TCCCCGCGTCGACGGATCC) with up to 2 bp mismatches were
coordinates. In the applications here we set K to 50. extracted for further UGI-seq processing. We first extract plate barcode, cell-
ref
specific barcode (7 bp), random molecular tags (RMTs, 8 bp) and unique guide
Filtering and clustering tier 3 cells. A total of 105 amplification batches of tier identifier (UGI, 8 bp) for each read. Reads with low quality (Phred < 27) or without
3 cells (Supplementary Fig. 1c) were collected. Cells with UMI count < 500 a valid UGI sequence (up to 1 bp mismatch), cell barcode (up to 1 bp mismatch) or
and genes with UMI count < 10 were discarded, resulting in 12,051 cells plate barcode (exact match) were discarded. Triplets with fewer than 30 reads were
(Supplementary Table 1). MetaCell gene selection identified 376 markers discarded as errors, and each cell received a vector of UGI molecule counts. To
(excluding ribosomal and cell cycle genes from Supplementary Table 2). Graph assign a binary label per cell, we consider UGI molecules > 1 as positive cells.
coverage was performed using K range = 150 and N min = 20. Visualization of tier 3 was
performed with T edge = 0.05 and graph maximum degree set to 8. Meta-cells were Clonal analysis of CRISP-seq experiments. All the Cas9+ BFP+ donor-derived
annotated with specific differentiation fates if the geometric mean of UMIs for cells in the CRISP-seq experiment come from a pool of cells infected with a small
one of the 15 established lineage markers was fourfold (or tenfold higher for the set of unique gRNA. Hence, the cellular output on days 9–11 in each mouse may
neutrophil Ltf) higher than the median meta-cell geometric mean. derive from one or more founder cells infected with the same combination of
gRNA. Consequently, it is not possible to deduce the exact clonal composition of
Defining and clustering the core data set. To sensitively filter out cells that are donor-derived cells. However, if we set a lower bound on the number of founder
significantly committed toward a differentiation fate and focus on more early cells by pooling together all cells sharing the same gRNA combination in a single
progenitor cells, we first identified sets of genes G fate that are significantly over- recipient mouse (which we term ‘gRNA-clone’), we find a significant variance in
expressed in each of the fates identified in tier 3. This was done by analysis of the erythroid contribution for each gRNA-clone (Fig. 7c,d and Supplementary
pooled expression in the groups of tier 3 clusters that were associated with specific Fig. 7d). We note that this effect stands even when considering gRNA-clones
lineages using marker genes as described above, and identification of genes with containing control gRNA only.
at least 50 UMIs and at least twofold enrichment in this pool over the background. We surmise that there is a strong clonal effect on cellular output in our
For each G fate , we analysed the distribution of e(G fate ,c) over all cells and determined transplantation assay (probably due to a strong selective pressure), which may
thresholds for filtering for each lineage separately (Supplementary Fig. 4a). This obscure the real quantitative phenotype when inactivating a specific transcription
resulted in filtering 7,075 cells and retaining 9,348 cells for further analysis. factor. To overcome clonality, we turned to assessing cellular output at the gRNA-
Clustering was performed using MetaCell analysis (but excluding specifically the clone level instead of the single cell level (Fig. 7e). We calculated P values using
strong neutrophil differentiation module, including Camp, Ltf, S100a8, S100a9 FDR-adjusted Mann–Whitney tests on all gRNA with more than 500 singly
and the haemoglobin genes Hba-a2, Hbb-b1 and Beta-s), using bootstrap to derive infected cells, testing enrichment for erythrocytes (Car1 and Hba-a2), monocytes
robust clustering (resampling 70% of the cells in each iteration, and clustering the (Ly86), neutrophils (Gstm1 and Fcnb) or B cells (Vpreb1) (Supplementary Fig. 7e).
co-cluster matrix with minimal cluster size set to 20, and number of bootstrap
clusters set to 50). Analysis of in vivo and ex vivo PU.1 KO experiment. We pooled PU.1 and control
infected cells from Lin− c-Kit+ and Ly6G+ sorting gates and used MetaCell to
Proliferation-score. The proliferation-score for each cell c was defined as f(G prolif ,c) analyse 6,529 single cells. To position meta-cell on the neutrophil differentiation
where G prolif includes the cell cycle gene module identified as described above gradient, we used the neutrophil program defined in Fig. 6 (stage I), as well as an
(Supplementary Table 2). additional set of genes (stage II, Supplementary Fig. 8d and Supplementary Table 2)
expressed in Ly6G+ control cells, but not in the myeloid data set. To define these
Stem-score. Genes with statistically significant correlation with Hlf expression in a genes, we identified clusters of the myeloid map exhibiting fourfold enrichment of
UMI matrix downsampled to 800 UMIs per cell (FDR-adjusted P < 1 × 10−3; Fisher’s Ccl6, and chose all genes differentially expressed in these cells compared to the rest
exact test) were used to defined the set G stem (Supplementary Table 2). The stem-score of the data set (χ2 test; P < 1 × 10−9 with 2.8-fold or higher change).
was defined for each cell as f(G ,c) (see section ‘UMI transformation and gene
stem
module score’) using log-transformed expanded values to maximize information Statistics and reproducibility. All biological and technical replicates in the
extracted from genes with low expression mean. study are documented in Supplementary Fig. 1c and Supplementary Table 1,
which state the number of mice (including identities), batches and cells. All
Correlations within the core data set. Cells within the core data set were stratified experiments were performed at least three times, except for the Giemsa staining,
by their stem-score (III, 95–100%; II, 80–95%; I, 60–80% percentiles). Spearman which was performed twice, and the ex vivo PU.1 KO, which was performed
correlations were calculated within each percentile on the log-transformed UMI once. All replication attempts were successful. No statistical method was used
matrix downsampled to 1,200 UMIs per cell. Only genes negatively correlated to predetermine sample size. The experiments were not randomized. The
with the stem-score are shown in Fig. 4a–c. Supplementary Fig. 4j shows Pearson investigators were not blinded to animal allocation during experiments and
correlations over the log geometric mean of UMI in each cluster. outcome assessment.
Defining and clustering the myeloid progenitor data set. The myeloid progenitor Reporting Summary. Further information on experimental design is available in
data set was extracted from cells from tiers 3, 4 and 5 similarly to the creation of the Nature Research Reporting Summary linked to this article.
the core data set. Cells were filtered for high expression of gene sets G of the
fate
following excluded lineages: ILC (Ccl5), megakaryocytes (Pf4), erythrocytes (Car1 Code availability. Scripts and auxiliary data needed to reconstruct analysis
and Hba-a2), basophils (Prss34) and eosinophils (Prg2), and B cells (Vpreb1). This files from count matrices to full figures are available in a git repository: https://
resulted in filtering 4,886 cells and retaining 11,960 cells for further analysis. The bitbucket.org/tanaylab/hematopoiesis2018.
myeloid data set was analysed by MetaCell with bootstrap (resampling rate = 70%,
minimal cluster size set to 20, and K = 60). Clusters featuring high mean levels Data availability. RNA-seq, MARS-seq and CRISP-seq data that support the
of excluded lineage genes were also removed from the data set (Prss34, Prg2, findings of this study have been deposited in the Gene Expression Omnibus (GEO)
Mcpt8, Vpreb1, Vpreb3, Car1, Mt2, Klf1, Ccl5, Pf4, Apoe and Cd79b), providing under accession codes GSE113495, GSE92575 and GSE113494.
additional filtering and retaining for analysis a total of 36 clusters and 8,395 cells. Source data for Fig. 6 and Supplementary Figs. 4, 5 and 8 are provided as
2D visualization was performed as described in the section ‘Mapping cells to an Supplementary Table 5. All other data supporting the findings of this study are
existing Metacell model’. available from the corresponding author on reasonable request.
Neutrophil and monocyte differentiation gradients. To define the neutrophil
differentiation program we identified clusters of the myeloid map exhibiting high References
expression of neutrophil genes (16-fold enrichment of Camp compared to the 70. Vallejos, C. A., Marioni, J. C. & Richardson, S. BASiCS: Bayesian analysis of
median expression across clusters). We extracted a set of genes G differentially single-cell sequencing data. PLoS Comput. Biol. 11, e1004333 (2015).
neut
NATuRe CeLL BIoLoGY | www.nature.com/naturecellbiology
© 2018 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
1
nature
research
|
reporting
summary
April
2018
Corresponding author(s): Ido Amit
Reporting Summary
Nature Research wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency
in reporting. For further information on Nature Research policies, see Authors & Referees and the Editorial Policy Checklist.
Statistical parameters
When statistical analyses are reported, confirm that the following items are present in the relevant location (e.g. figure legend, table legend, main
text, or Methods section).
n/a Confirmed
The exact sample size (n) for each experimental group/condition, given as a discrete number and unit of measurement
An indication of whether measurements were taken from distinct samples or whether the same sample was measured repeatedly
The statistical test(s) used AND whether they are one- or two-sided
Only common tests should be described solely by name; describe more complex techniques in the Methods section.
A description of all covariates tested
A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons
A full description of the statistics including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient) AND
variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals)
For null hypothesis testing, the test statistic (e.g. F, t, r) with confidence intervals, effect sizes, degrees of freedom and P value noted
Give P values as exact values whenever suitable.
For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings
For hierarchical and complex designs, identification of the appropriate level for tests and full reporting of outcomes
Estimates of effect sizes (e.g. Cohen's d, Pearson's r), indicating how they were calculated
Clearly defined error bars
State explicitly what error bars represent (e.g. SD, SE, CI)
Our web collection on statistics for biologists may be useful.
Software and code
Policy information about availability of computer code
Data collection No open-source or custom code was used to collect data for this paper
Data analysis For FACS analysis, we used the following sofrware:
FACSDiva 7
FlowJo 10.4.2
All data analysis was done in R.
Data analysis was done with the custom made MetaCell package. Scripts and auxiliary data needed to reconstruct analysis files from
count matrices to full figures are available in a git repository (https://bitbucket.org/tanaylab/hematopoiesis2018).
For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors/reviewers
upon request. We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Research guidelines for submitting code & software for further information.
2
nature
research
|
reporting
summary
April
2018
Data
Policy information about availability of data
All manuscripts must include a data availability statement. This statement should provide the following information, where applicable:
- Accession codes, unique identifiers, or web links for publicly available datasets
- A list of figures that have associated raw data
- A description of any restrictions on data availability
RNA–seq, MARS-seq and CRISP-seq data that support the findings of this study have been deposited in the Gene Expression Omnibus (GEO) under accession code
GSE113495, GSE92575, and GSE113494.
Source data for Fig. 6 and Supplementary Fig. 4, 5 and 8 have been provided as Supplementary Table 5. All other data supporting the findings of this study are
available from the corresponding author on reasonable request.
Field-specific reporting
Please select the best fit for your research. If you are not sure, read the appropriate sections before making your selection.
Life sciences Behavioural & social sciences Ecological, evolutionary & environmental sciences
For a reference copy of the document with all sections, see nature.com/authors/policies/ReportingSummary-flat.pdf
Life sciences study design
All studies must disclose on these points even when the disclosure is negative.
Sample size We chose to sequence and analyze 12051 tier 3 cells so that 0.019%-0.122% of the whole bone marrow is captured by each meta-cell. This
allows an extensive coverage of all distinct transcriptional profiles and conforms to the gold standard in the field. Full description of sample
sizes is detailed in Supplementary Fig. 1. No statistical tool was used to apriori choose sample size.
Data exclusions Exclusion of single cells was done according to detection depth (less than 500 UMI per cell). Exclusion criteria for specific analyses is described
in the Methods section, paragraphs: 'Filtering and clustering tier 3 cells', 'Defining and clustering the core dataset', 'Defining and clustering the
myeloid progenitor dataset'
Replication Single cells were collected form a total of 47 independent mice. For tier 3 analysis (Figure 1), cells were collected from 5 different mice, at
least on four independent sorting sessions. All replication attempts were successful. CRISP-Seq samples were collected from 17 independent
mice, on two independent experiments.
Randomization No randomization was done, since all animals used were isogenic mice.
Blinding No blinding was done, since the computational framework was identical for all processed animal samples.
Reporting for specific materials, systems and methods
Materials & experimental systems Methods
n/a Involved in the study n/a Involved in the study
Unique biological materials ChIP-seq
Antibodies Flow cytometry
Eukaryotic cell lines MRI-based neuroimaging
Palaeontology
Animals and other organisms
Human research participants
Antibodies
Antibodies used A list of all antibodies used in this study can be found in Supplementary Table 4
Validation For each experiment, each FACS antibody was compared (separately) to an unstained sample. Only FACS antibodies that yielded
