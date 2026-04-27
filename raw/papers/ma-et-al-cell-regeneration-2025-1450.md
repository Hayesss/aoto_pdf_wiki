---
source_path: /mnt/c/Users/Administrator/Zotero/storage/SHS6RYBC/Ma 等 - 2025 - A single-cell hematopoietic microenvironmental atlas reveals progressive maturation of bone marrow v.pdf
ingested: 2026-04-23
sha256: 1da228b6c3639c15
---

Ma et al. Cell Regeneration (2025) 14:50
https://doi.org/10.1186/s13619-025-00265-7
RESEARCH ARTICLE Open Access
A single-cell hematopoietic
microenvironmental atlas reveals progressive
maturation of bone marrow vascular niche
Lan‑Yue Ma1,2,3,4†, Zhao‑Hua Deng1,2,3,4†, Ke Bai5, Yan‑Mei Yu1,2,3,4, Yin Huang5, Rong‑Rong Gao1,2,3,4,
Yu‑Yan Li1,2,3,4, Xiao‑Ling Li1,3,4, Jia‑Xin Yang5, Ya‑Hai Shu1, Jinjin Ma5,6, Yang Liu5* and Qi Chen1,3,4*
Abstract
The interaction between hematopoietic stem and progenitor cell (HSPC) and its vascular niche is essential for sup‑
porting the homeostasis and reconstitution of hematopoietic system in adult bone marrow (BM), but a comprehen‑
sive atlas covering this HSPC‑vascular niche crosstalk in multiple developmental stages and species is lacking. Here,
we integrated single‑cell transcriptomic data of HSPC and its vascular niches from fetal liver until aged BM, covering
two species, two organs, and six developmental time points. Comparative analyses revealed dramatic differences
in the gene expression, enriched pathway, and cell–cell communication between human fetal and adult BM. Notably,
many of these differences were conserved between humans and mice. Multi‑timepoint profiling of murine BM vascu‑
lar niches revealed a stepwise maturation of gene expression, including critical niche factors such as SCF and CXCL12.
Furthermore, analysis of this dynamic vascular niche atlas highlighted organ‑specific features between fetal liver
and BM niches, significant transcriptional changes in aged BM endothelial cells, and identified midkine as a previ‑
ously unknown niche factor. Functional validation showed that transplanting HSPC into midkine knockout mice
or treating with a midkine inhibitor (iMDK) enhanced hematopoietic reconstitution. In contrast, recombinant midkine
suppressed HSPC differentiation. Together, our work presents a cross‑species and multi‑stage atlas of HSPC–vascular
niche interactions, offering valuable insights into the dynamic changes of vascular niche through lifelong HSPC devel‑
opment and a platform to identify unknown niche factors.
Keywords Hematopoietic microenvironment, Niche atlas, scRNA‑seq, Midkine
†Lan‑Yue Ma and Zhao‑Hua Deng these authors contribute equally to the
work.
*Correspondence:
Yang Liu
yangl005@scut.edu.cn
Qi Chen
chen_qi@gibh.ac.cn
Full list of author information is available at the end of the article
© The Author(s) 2025. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this
licence, visit http://creativecommons.org/licenses/by/4.0/.
Ma et al. Cell Regeneration (2025) 14:50 Page 2 of 20
Graphical Abstract
Background proliferation of HSPCs are tightly regulated by the bone
Hematopoiesis is a fundamental biological process marrow niche—a highly specialized microenvironment
responsible for the continuous generation of blood and within the bone (Asada et al. 2017; Birbrair and Frenette
immune cells throughout an individual’s life (Kasbekar 2016).
et al. 2023). These cells originate from hematopoietic This niche comprises a complex network of cellular
stem and progenitor cells (HSPC), which primarily reside components, including bone marrow endothelial cells
in the bone marrow (BM) of mammals (Comazzetto et al. (BMEC), mesenchymal stromal cells (BMSC), osteolin-
2021). The self-renewal, multipotent differentiation, and eage cells (OLC), nerves, adipocytes, and differentiated
M a et al. Cell Regeneration (2025) 14:50 Page 3 of 20
hematopoietic cells (Pinho and Frenette 2019). Among Results
these, BMEC and BMSC are closely associated and A single‑cell atlas of HSPC and vascular niche from embryo
together form the vascular niche, which plays a critical to aging
role in maintaining HSPC function (Tuckermann and To comprehensively assess the interactions between
Adams 2021). While various niche components influ- HSPC and their vascular niche across developmen-
ence HSPC via paracrine signaling and direct cell–cell tal stages, organs, and species, we integrated scRNA-
interactions, mounting evidences indicate that most seq datasets. These included vascular endothelial cells,
HSPC reside within 10 μm of the vascular niche, under- perivascular mesenchymal cells, and HSPC from six
scoring the pivotal role of BMEC and BMSC in HSPC developmental stages: fetal liver, fetal BM, neonatal BM,
regulation (Acar et al. 2015; Chen et al. 2019; Christo- juvenile BM, adult BM, and aged BM (Fig. 1A-B). In total,
doulou et al. 2020). this atlas includes 112,166 cells across two organs and
HSPC ensures the lifelong production of blood cells two species, providing a robust framework for analyzing
and respond to physiological demands. However, the vascular microenvironment and its regulatory role
the structure, composition, and function of the vas- in hematopoiesis after dataset integration (Fig. 1C, Fig.
cular niche evolve significantly from fetal develop- S1A-F, Table S1). The following sections demonstrated
ment through adulthood and into old age (Kara et al. how this atlas enabled comparative analyses and the
2023; Langen et al. 2017). For instance, our previous identification of unknown therapeutic targets.
research has highlighted the essential role of caveo- Firstly, we used the dataset in our atlas to compare the
lin-1+ BMEC in fetal mouse BM (Liu et al. 2022), while fetal and adult BM vascular niche in human (Fig. 1D-E
aging is associated with the decline of type-H and and Fig. S1G-I). Comparative analysis identified human
arterial-like BMEC populations (Kusumbe et al. 2016). genes enriched within either fetal or adult BM, independ-
Despite these findings, most studies of HSPC-niche ent of cell type (Fig. 1F). This analysis also delineated cell
interactions have focused on steady-state conditions or type-enriched temporal signatures of BMEC and BMSC
responses to myeloablative injury in adult bone marrow (Fig. 1F), revealing substantial transcriptional divergence
(Hoggatt et al. 2016). Consequently, how the vascular between fetal and adult BM in human (Fig. 1G). Gene
niche develops and changes from the embryonic stage ontology (GO) analysis indicated that genes in BMEC
through adulthood—and how these changes affect its were associated with angiogenesis and leukocyte-medi-
interaction with HSPC—remain poorly understood, ated immunity at corresponding stages (Fig. 1H), whereas
particularly in humans, where bone marrow samples BMSC exhibited differences in extracellular matrix
are scarce and experimental manipulation is limited. organization and hematopoietic regulation (Fig. 1I). Path-
In this study, we integrate single-cell RNA sequenc- way scoring revealed that fetal BMEC showed stronger
ing (scRNA-seq) datasets to construct a temporally VEGF signaling and proliferative capacity (Fig. 1J and
dynamic atlas of the bone marrow vascular niche. This Fig. S1J), while adult BMEC demonstrated better vehicle
atlas enables us to compare fetal and adult bone mar- transmission ability (Fig. 1K and Fig. S1K). Fetal BMSC
row, examine cross-organ and cross-species differ- showed increased skeletal development potential (Fig. 1L
ences, and identify previously uncharacterized niche and Fig. S1L), whereas adult BMSC exhibited adipogenic
factors. differentiation preference (Fig. 1M and Fig. S1M), which
(See figure on next page.)
Fig. 1 Generation of the hematopoietic microenvironment atlas and comparison of human embryonic and adult bone marrow. A Schematic
representation of the hematopoietic microenvironment atlas (HMA) framework integrating multi‑datasets and analysis. B UMAP visualization
of single‑cell transcriptomes cells based on developmental stages and species in hematopoietic microenvironment atlas (HMA). C Diagram
highlighting key functional modules in the HMA. D Diagram showing data integration for human embryonic and adult BM. E UMAP plot showing
cell types in human embryonic and adult BM. F Heatmap displaying different stage enriched genes across human BM cell types. G Quantitative
comparison of differentially expressed genes (DEG) counts between human embryonic and adult BM. H‑I Gene Ontology (GO) enrichment analysis
of DEG and dot plot showing selective genes associated with GO in human bone marrow endothelial cell (BMEC) or bone marrow stromal cell
(BMSC). J‑K Violin plot showing endothelial proliferation activity and vesicle mediated transport scores and dot plot showing genes associated
with human embryonic and adult BMEC. L‑M Violin plot showing skeletal system development and fat cell differentiation scores and dot plot
showing genes associated with human embryonic and adult BMSC. N–O Violin plots comparing niche factor expressions (BMP1, VEGFB, CXCL12,
PDGFB, PTN, VEGFA, ANPGT1, KITLG) in human embryonic and adult BMEC (N) or BMSC (O). P‑Q Quantification of incoming (P) or outgoing (Q)
crosstalk strength in human embryonic and adult BMEC and BMSC. R Comparison of cell–cell communication pathway numbers in BMEC, BMSC,
and HSPC in human embryonic and adult. S Enrichment signaling from BMEC or BMSC to HSPC in human embryonic and adult BM
Ma et al. Cell Regeneration (2025) 14:50 Page 4 of 20
Fig. 1 (See legend on previous page.)
M a et al. Cell Regeneration (2025) 14:50 Page 5 of 20
was consistent with reported murine properties (Shu morphogenesis and angiogenesis were predominantly
et al. 2021). enriched in embryo, whereas chemokine production
One typical feature of the BM vascular niche was their were more prominent in adult (Fig. 2G-H and Fig. S2E-
ability to release microenvironmental factors (Mendez- F), that was consistent with growth and maintenance
Ferrer et al. 2020; Sanchez-Aguilera and Mendez-Ferrer function of BMEC in fetal and adult BM, respectively
2017). A developmental shift in niche factor expres- (Liu et al. 2022). In BMSC, fetal cells were enriched for
sion was detected in human BM, including key regula- chondrocyte differentiation, while adult cells exhibited
tors such as stem cell factor (SCF, encoded by KITLG), increased activity in fatty acid metabolism (Fig. 2I-J and
CXCL12, ANGPT1, PTN, VEGF, and PDGF (Fig. 1N-O Fig. S2G-H). These pathway activities and gene expres-
and Fig. S1N-O). Comparative analysis of vascular sion changes demonstrated consistent evolutionary
niche-HSPC interactions revealed an overall stronger trends across species and were consistent with their
interaction strength in fetal human BM (Fig. 1P-Q) with known function.
similar number of cell–cell interactions across fetal and Analysis of microenvironmental factor expression
adult human BM (Fig. 1R). However, HSPC received showed that both fetal and adult BMEC and BMSC
unidentical signals from BMEC and BMSC in the adult exhibited stage-specific niche factor expression pattern
niche and their fetal counterparts (Fig. 1S), suggesting that was conserved between humans and mice (Fig. 2K-
fetal and adult BM provided different microenviron- L). Notably, the CXCL12 expression in BMEC and the
ment to support HSPC that was similarly detected in SCF expression in BMSC significantly increased during
mice (Liu et al. 2022). adulthood in both species (Fig. 2K-L). Cell–cell interac-
These data indicated that human fetal and adult bone tion analysis demonstrated increased signaling percent-
marrow vascular niche cells differed substantially in age from BMEC and BMSC to HSPC in both human and
transcriptional profiles, enriched signaling, niche factor mouse adult BM compared to embryonic stage (Fig. 2M),
secretion, and interaction networks with HSPC. together with conserved vascular microenvironment-
mediated signaling pathways, including SCF-KIT,
Evolutionary conservation of vascular niche development CXCL12-CXCR4, IGF2-IGF1R and SPP1-integrin signal-
between humans and mice ing in these two mammals (Fig. 2N-O and Fig. S2I).
To determine whether the observed developmental shift Collectively, these findings demonstrated evolution-
was evolutionarily conserved across mammals, we con- ary conservation of vascular microenvironmental gene
ducted a cross-species comparison between human and expression dynamics and their functional interactions
mice (Fig. 2A-B and Fig. S2A-D). Differential expres- with HSPC between humans and mice.
sion analysis identified genes enriched in either fetal or
adult stages within both BMEC and BMSC, revealing Developmental dynamics of the murine bone marrow
largely consistent temporal expression dynamics across vascular microenvironment
species (Fig. 2C-D). GO analysis of these differentially- Because of the evolutionary similarities between human
expressed genes (DEG) highlighted conserved biologi- and murine BM microenvironments and the availabil-
cal processes, including cell–cell junction organization, ity of samples from the BM of mice, we analyzed the
response to peptide, bone development and regulation developmental dynamics of BMEC and BMSC across
of leukocyte differentiation in BMEC or BMSC, with cor- fetal, postnatal, juvenile, and adult stages from the atlas
responding genes exhibiting similar expression trends in (Fig. 3A-B and Fig. S3A-C). Multiple developmental time
both humans and mice (Fig. 2E-F). Pathway scoring in point analysis identified a list of genes showing tempo-
BMEC revealed that genes associated with blood vessel ral transition in the gene expression level from embryo
(See figure on next page.)
Fig. 2 Evolutionarily conserved features between human and mice BM microenvironment. A Schematic of cross‑species data integration
strategy for embryonic and adult human/mouse BM. B UMAP plot showing cell types in human/mouse BM with embryonic and adult. C‑D
Conserved cross‑species DEG between embryonic and adult stages, and heatmap of human‑mouse conserved gene expression in BMEC or BMSC
at each developmental stage. E–F GO enrichment analysis of cross‑species conserved DEG and heatmap of representative GO‑associated
genes in embryonic and adult BMEC or BMSC. G‑H Violin plots of blood vessel morphogenesis and chemokine production scores and heatmap
of cross‑species conserved and stage‑specific genes in BMEC. I‑J Violin plots of chondrocyte differentiation and fat acid metabolic process scores
and heatmap of cross‑species conserved and stage‑specific genes in BMSC. K‑L Heatmap and violin plot of species‑conserved niche factor
expressions between embryonic and adult in human/mouse BMEC or BMSC. M River plot showing percentage differences of HSPC as signal
receivers between embryonic and adult stages in human and mouse. N–O Cross‑species shared enriched from BMEC or BMSC to HSPC interactions
in embryonic and adult stages
Ma et al. Cell Regeneration (2025) 14:50 Page 6 of 20
Fig. 2 (See legend on previous page.)
M a et al. Cell Regeneration (2025) 14:50 Page 7 of 20
to adult (Fig. 3C). Pearson correlation analysis revealed HSPC expansion (Khan et al. 2016). However, the vas-
a gradual transcriptional transition in BMEC and BMSC cular niche comparison between fetal BM and fetal liver
from embryo through postnatal/juvenile until adult- was very limited. Therefore, we extracted these data-
hood (Fig. 3D). Similarly, the number of DEG, compar- sets from our atlas (Fig. 4A and Fig. S4A-D), identifying
ing adult BMEC or BMSC to other developmental stages, organ-specific genes including Sumo2 or Cul3 that were
decreased during the maturation of these cells (Fig. 3E). highly enriched in the fetal liver or bone marrow, respec-
Representative gene sets could be selected to assess tively (Fig. 4B). Pearson’s coefficient correlation analysis
the developmental dynamics of key pathway, including revealed that the endothelial and mesenchymal cells in
angiogenesis in BMEC and hematopoiesis regulation in fetal liver were dramatically different from the corre-
BMSC, further supported this step-by-step maturation sponding cells across all stages in BM (Fig. 4C). BMEC
pattern (Fig. 3F-G and Fig. S3D-E). and BMSC subpopulation analysis revealed that the
Analyzing the developmental dynamics of vascular endothelial and mesenchymal cells in fetal liver were not
niche factors revealed gradual downregulation of SCF identical to any subtype of corresponding fetal BM cells
and Pdgfb, alongside upregulation of CXCL12 and Selp (Fig. S4E). These data suggested substantial organ-spec-
in BMEC (Fig. 3H-I and Fig. S3F). Meanwhile, BMSC ificity in the vascular microenvironments, with fetal liver
showed decreasing expression of IGF1 and Ptn together niche cells showing limited resemblance to any subtype
with upregulating Vegfc and Spp1 (Fig. 3J-K and Fig. of BM vascular niche. DEG analysis further underscored
S3G). Notably, cell–cell interaction analysis revealed peak microenvironmental divergence, identifying numerous
interaction number among BMEC, BMSC and HSPC genes differentially expressed between fetal liver and
at the postnatal and juvenile stages, rather than embry- BM in endothelial and mesenchymal compartments (Fig.
onic or adult periods (Fig. 3L and Fig. S3H). Crosstalk S4F). GO analysis linked hepatic endothelial DEG to liver
strengths were relatively stable in HSPC, but the interac- regeneration (Fig. 4D-E and Fig. S4G-H). While liver
tion strengths were gradually reduced after postnatal in mesenchymal DEG were associated with erythrocyte dif-
BMSC and BMEC (Fig. 3M). Among these interactions, ferentiation, bone marrow mesenchymal DEG showed
30–50% were conserved across all timepoints, while preference to osteoblast differentiation that was consist-
10–20% were developmental stage-specific (Fig. 3N), ent with their organotypic function (Fig. 4F-G and Fig.
including relative enrichment of individual pathway with S4I-J).
stronger signaling strength at each developmental stage Niche factor analysis revealed that fetal liver endothe-
(Fig. 3O). lial and mesenchymal cells showed higher expression
These findings indicated that while BMEC and BMSC of some growth factor or chemokine in the CCL family,
underwent gradual maturation in transcription and FGF family and interleukin family (Fig. 4H-I). Bone mar-
niche factor secretion, their putative interactions with row expressed higher levels of SCF (Kitl), CXCL12, and
HSPC were potentially more active during postnatal pleiotrophin, even though the fetal liver was enriched for
development. Tgfb1 and Tgfb2, which remained minimally expressed in
BM (Fig. 4J-K). Cell–cell interaction analysis showed that
Organ‑specific vascular microenvironments in fetal bone fetal liver had fewer and weaker interactions among vas-
marrow and liver cular endothelial cells, mesenchymal cells compared to
Before HSPC engraftment into the fetal BM at E16.5 to fetal BM (Fig. 4L-M). In detailed signaling, the fetal liver
interact with BM vascular niche (Lee et al. 2021; Liu et al. and fetal BM displayed enrichment of individual signal-
2022), the hepatic vascular microenvironments promote ing in each organ, but the key SCF and CXCL12 signaling
(See figure on next page.)
Fig. 3 The dynamic changes of murine BM microenvironment during developmental maturation. A Schematic of developmental data integration
from embryo, postnatal, juvenile and adult BM. B UMAP plot showing cell types in developmental mouse BM. C Dynamic gene expression
trajectories in developmental BMEC and BMSC. D Heatmap of inter‑stage correlations during BMEC and BMSC development. E Dynamic changes
in DEG across embryonic, postnatal, and juvenile stages versus adult in BMEC and BMSC. F Developmental dynamics of sprouting angiogenesis
and acute inflammation response scores and associated gene expression in mouse developmental BMEC. G Developmental dynamics of collagen
fibril organization and regulation of hematopoiesis scores and associated gene expression in mouse developmental BMSC. H‑I Heatmap of niche
factor expression and violin plots of Kitl and Cxcl12 expression levels across developmental BMEC. J‑K Heatmap of niche factor expression and violin
plots of Igf1 and Vegfc expression levels across developmental BMSC. L Number of cell–cell communication pathways in BMEC, BMSC, and HSPC
across developmental BM. M Quantification of incoming and outgoing crosstalk strength across developmental BM. N Percentage of interaction
types across developmental BM. O Heatmap of BMEC or BMSC as sender and HSPC as receiver signaling strength across developmental stages
of BM
Ma et al. Cell Regeneration (2025) 14:50 Page 8 of 20
Fig. 3 (See legend on previous page.)
M a et al. Cell Regeneration (2025) 14:50 Page 9 of 20
was highly enriched in fetal BM (Fig. 4N), suggesting a other microenvironmental factors (Fig. 5N-O). Therefore,
superior ability of the BM niche to attract and retain although there was no dramatic change of cell–cell inter-
HSPC. action numbers between adult and aging BM (Fig. S5L-
These findings revealed fundamental differences in M), the aging 1 showed reduced ability to interact with
the vascular niche between fetal liver and bone marrow, other cell types (Fig. 5P-Q).
which may underlie the eventual preference of HSPC for These data indicated that aging dramatically modified
bone marrow residency. the transcriptome of BMEC.
Aging‑associated endothelial changes in the bone marrow
niche Midkine was an uncharacterized microenvironmental
Next, we extended our analysis to compare the adult and factor
aged BM microenvironments (Fig. 5A-B and Fig. S5A-C). Our previous analysis revealed dynamic expression pat-
Our analysis identified expression of genes which were terns of vascular niche factors across different devel-
mostly associated with aging 3 cell types and enriched opmental stages in the BM. To identify a common
in specific cell type (Fig. 5C). However, aging resulted in microenvironmental factor that persistently existed dur-
greater impact on gene expression in vascular endothe- ing vascular niche-HSPC crosstalk, we screened our atlas
lial cells than in mesenchymal cells or HSPC that was discovering midkine, a homolog of niche factor pleiotro-
similarly detected comparing adult and aging BM cells in phin, constantly formed putative communications with
DEG numbers and Pearson’s coefficient correlation anal- HSPC from fetal liver to aged bone marrow (Fig. 6A-B
ysis (Fig. 5D-E and Fig. S5D), which triggered us to focus and Fig. S6A-B). However, the function of midkine to
on BMEC comparison between adult and aged BM. regulate HSPC was not validated in genetically-modified
Clustering of adult and aged endothelial subpopula- mice in vivo. Therefore, we generated a midkine knock-
tions revealed a unique endothelial subtype enriched in out mice (Mdk KO) which exhibited normal hematopoie-
aged bone marrow (defined as aging 1), which was dis- sis under steady-state condition (Fig. S6C-D). However,
tinct from arterial, capillary, and sinusoidal endothelial wildtype HSPC transplantation into Mdk KO recipient
cells in the aged bone marrow (Fig. 5F-G and Fig. S5E- mice resulted in increased LSK cell and leukocyte per-
G). This aging 1 subpopulation showed higher CD38 centage (Fig. 6C-E), suggesting absence of midkine in
expression, which was low in postnatal and young adult niche may promote hematopoietic reconstitution after
BMEC (Fig. S5H-I). This aging 1 subpopulation displayed transplantation.
transcriptional profiles that differed from embryonic, This triggered us to test whether midkine was a poten-
neonatal, juvenile, and adult BMEC (Fig. S5J), as well as tial target to enhance hematopoietic transplantation effi-
from other aged BMEC subtypes (Fig. 5H). DEG analy- ciency. Pharmacological inhibition of midkine synthesis
sis identified more than 300 genes that distinguished using iMDK, an antagonist that inhibit midkine genera-
aging 1 with other aged endothelial subtypes (Fig. 5I- tion (Khan et al. 2016), elevated LSK and leukocyte cell
J), with GO analysis linking them to weaker association percentage after transplantation (Fig. 6F and Fig. S6E).
with blood coagulation and permeability (Fig. 5K and Fig. This evidence suggested that iMDK, a reagent without
S5K). Genes associated with endothelial function, includ- apparent harmful effect in normal cells and mice (Ishida
ing Klf2, Sox18, Nrp1, Lrg1, were changed in the aging 1 et al. 2015), had the potential to promote bone marrow
cluster (Fig. 5L). We noted that some microenvironmen- transplantation. CD45.1/CD45.2 competitive transplan-
tal factors were highly expressed in the aging 1, including tation assay confirmed that midkine inhibition enhanced
Kitl and Cxcl12 (Fig. 5M-O). However, aging 1 showed the proportion of HSPC in BM (Fig. 6G), which was pos-
overall weaker expression of a substantial number of sibly because iMDK promoted the proliferative EdU+
(See figure on next page.)
Fig. 4 scRNA‑seq comparison of murine fetal liver and BM. A Diagram showing data integration for embryonic liver and BM. B Heatmap displaying
tissue‑specific expressed genes across cell types. C Heatmaps showing correlation between liver and developmental BM in Endothelial cell (EC)
and Stromal cell (SC). D‑E Violin plot showing liver regeneration and angiogenesis scores and dot plot showing genes associated with embryonic
liver and BM in EC. F‑G Violin plot showing regulation of erythrocyte differentiation and osteoblast differentiation scores and dot plot showing
genes associated with embryonic liver and BM in SC. H‑I Heatmap of niche factor expression in embryonic liver and developmental BM in EC or SC.
J‑K Violin plots comparing niche factor expressions (Tgfb1, Bmp2, Kitl, Pdgfb, Tgfb2, Wnt5b, Cxcl12, Vegfa) between embryonic liver and BM in EC
or SC. L Comparison of cell–cell communication pathway numbers of EC, SC, and HSPC in embryonic liver and BM. M Quantification of incoming
and outgoing crosstalk strength between embryonic liver and BM in EC and SC. N Enrichment signaling from EC or SC to HSPC in embryonic liver
and BM
Ma et al. Cell Regeneration (2025) 14:50 Page 10 of 20
Fig. 4 (See legend on previous page.)
M a et al. Cell Regeneration (2025) 14:50 Page 11 of 20
HSPC (Fig. 6H). Similar to BM, iMDK treatment influ- fetal BM, arterial blood vessels mediate initial HSPC
enced hematopoiesis in fetal liver (Fig. S6F-H). engraftment, while Lepr⁺ BMSC are largely absent (Liu
To confirm the inhibitory effect of midkine, we per- et al. 2022). In the postnatal and juvenile stages, BMEC
formed the colony forming unit (CFU) assay in which support HSPC maintenance via membrane-bound SCF,
iMDK increased colony proliferation and blood cell and Lepr⁺ BMSC begin contributing to myeloid and
number, while supplementing recombinant midkine erythroid lineage expansion (Kara et al. 2023). In adult-
suppressed the number of hematopoietic cells (Fig. 6I). hood, Lepr⁺ BMSC become more prevalent, promoting
Moreover, co-culture of HSPC with endothelial cells a shift in HSPC from a proliferative, oxidative metabolic
overexpressing midkine resulted in reduced leukocyte state to a quiescent state with enhanced immunomodu-
generation ability in vitro (Fig. 6J and Fig. S6I). Finally, latory function. Simultaneously, endothelial SCF expres-
when iMDK was added together with Mirdametinib, an sion declines, and HSPC transition to specialized,
inhibitor of MEK/ERK signaling, the number of hemat- quiescence-promoting niches (Kara et al. 2023; Kasbekar
opoietic cells significantly decreased in CFU assay et al. 2023; Takizawa et al. 2011). Adult HSPC relies more
(Fig. 6K and Fig. S6J), suggesting MEK/ERK was associ- on glycolytic metabolism to maintain quiescence, sup-
ated with midkine signaling. porting long-term preservation and adaptive responses
These findings suggested our atlas could be utilized to to stress through crosstalk with the BM vascular niche
identify midkine as a putative microenvironmental factor (Kasbekar et al. 2023). The dynamic transcriptional
that influenced HSPC proliferation and inhibiting mid- changes observed in our study align closely with these
kine signaling as a potential approach to enhance hemat- known developmental transitions of the vascular niche.
opoietic reconstitution after transplantation. Notably, our atlas includes multiple datasets with notice-
able variation because of batch effect or platform hetero-
Discussion
geneity before data integration. However, SCTransform
This work establishes a vascular niche atlas that system- effectively integrate these datasets generating compre-
atically compares developmental and adult BM, revealing hensive and convincing atlas.
evolutionarily conserved inter-species features between Prior to engraftment into fetal BM, the fetal liver serves
murine and human BM. The dataset spans embryonic, as the primary hematopoietic organ, supporting HSPC
postnatal, juvenile, and adult vascular niches, facilitat- expansion and erythro-myeloid differentiation through
ing comparisons between fetal liver and fetal BM micro- a specialized microenvironment, including SCF⁺DLK1⁺
environments, and enabling the identification of unique stromal cells (Lewis et al. 2021). However, this support
transcriptomic endothelial profile in aged BM. Multi- is transient and developmentally limited. For instance,
timepoint analysis uncovers midkine as a previously fetal liver-derived B lymphocytes develop independently
uncharacterized microenvironmental factor that con- of IL-7Rα signaling, but this characteristic disappears
strains excessive HSPC proliferation. This finding leads within one to two weeks after birth (Tsuneto et al. 2013).
to the identification of iMDK as a pharmacological agent HSPC from the fetal liver also shows weaker competi-
with the potential to enhance hematopoietic reconstitu- tive potential when transplanted into adult bone marrow
tion following HSPC transplantation. (Kikuchi and Kondo 2006). Single-cell transcriptomic
During mammalian hematopoietic development, the data suggest that fetal liver HSPC, particularly in early
BM microenvironment of HSPC undergoes significant gestation, exhibits low stemness, genomic instability, and
changes (Deng et al. 2023; Kasbekar et al. 2023). In the abnormal interferon signaling, which may contribute to
(See figure on next page.)
Fig. 5 Aging‑associated transcriptional changes in BM vascular microenvironment. A Diagram showing data integration for adult and aging BM. B
UMAP plot showing cell types in adult and aging BM. C Heatmap displaying stage‑specific expressed genes across BM cell types. D Number of DEG
across cell types between adult and aging BM. E Heatmap showing correlation between aging and developmental BMEC. F UMAP plot showing
BMEC from adult and aging. G UMAP plot of BMEC subpopulations in adult, aging 1 and aging 2. H Heatmap of correlation between aging 1
and aging 2 subclusters in BMEC. I MA plot of DEG between aging 1 and aging 2 in aging BMEC. J UMAP plots showing selected aging 1 signature
genes (Ablim3, Slc28a2) in BMEC. K Violin plots showing blood coagulation and cell adhesion scores and dot plot showing genes associated
with aging 1 and aging 2 in aging BMEC. L Dot plot of aging 1 and aging 2 BMEC signature genes associated with angiogenesis, endothelial cell
proliferation, vascular tube morphogenesis, and VEGF signaling pathways. M Heatmap of niche factor expressions in developmental BM, aging
1 and aging 2 in BMEC. N Heatmap of niche factor expressions in adult, aging 1 and aging 2 in BMEC. O Violin plots comparing niche factor
expressions (Tgfb1, Dll4, Kitl, Cxcl12) in aging 1 and aging 2. P Number of cell–cell communication pathways across different cell types, BMEC were
stratified into aging 1/2 subclusters, while BMSC and HSPC remained unstratified. Q Enrichment signaling from BMEC to HSPC in aging 1 and aging
2 BM
Ma et al. Cell Regeneration (2025) 14:50 Page 12 of 20
Fig. 5 (See legend on previous page.)
M a et al. Cell Regeneration (2025) 14:50 Page 13 of 20
the fetal origin of childhood leukemia (Xie et al. 2024). (Helbling et al. 2019). Reduced IGF1 levels have also been
Additionally, their reliance on oxidative phosphoryla- shown to accelerate HSPC aging and increase suscepti-
tion renders them metabolically inefficient in the hypoxic bility to myeloid malignancies (Young et al. 2021). These
adult BM, limiting post-transplant reconstitution capac- microenvironmental changes are tightly associated with
ity (Lewis et al. 2021; Xie et al. 2024). Although the fetal HSPC dysfunction and point to the potential of niche-
liver microenvironment supports HSPC during embryo- targeted therapies to combat age-related hematopoietic
genesis, our analysis suggests that it is fundamentally decline.
distinct from the BM niche, with organ-specific char- Midkine is a heparin-binding growth factor com-
acteristics reminiscent of recent studies uncovering posed of N- and C-terminal domains flanking a hinge
endothelial cell heterogeneity across tissues (Augustin region, which mediates interactions with heparan and
and Koh 2017; Gomez-Salinero et al. 2021; Petrova and chondroitin sulfate proteoglycans (Muramatsu 2014). It
Koh 2018; Trimm and Red-Horse 2023). is abundantly expressed in the embryonic central nerv-
The aging of HSPC is driven not only by intrinsic mech- ous system, where it promotes neurogenesis, neuronal
anisms but also by progressive remodeling of the bone survival, and oligodendrocyte precursor differentiation
marrow microenvironment. In aged BM, BMSC exhibit a (Neumaier et al. 2023). Under pathological conditions,
shift from osteogenic to adipogenic differentiation poten- midkine expression is upregulated by hypoxia-inducible
tial, impairing the secretion of niche factors essential for factor-1α (HIF-1α) and NF-κB, linking it to both hypoxia
maintaining HSPC quiescence (Ho and Mendez-Ferrer and inflammation (Neumaier et al. 2023). In cancer biol-
2020). Aging is also associated with dysregulated sym- ogy, midkine has been implicated in tumor progression
pathetic signaling, with reduced β3-adrenergic recep- in glioblastoma and neuroblastoma through ALK/NF-κB
tor activity promoting vasoconstriction and excessive and Notch2/Hes1 signaling pathways (Muramatsu and
β2-adrenergic signaling contributing to myeloid and Kadomatsu 2014; Neumaier et al. 2023). The midkine
megakaryocytic bias in HSPC fate (Gadomski et al. 2022; inhibitor iMDK has shown anti-tumor efficacy in non-
Maryanovich et al. 2018). Transcriptomic profiling of small cell lung cancer by blocking the PI3K-AKT pathway
aged BMEC reveals a distinct Aging 1, consistent with (Ishida et al. 2015). Additionally, iMDK induces apoptosis
vascular decline in aged marrow (Kusumbe et al. 2016). in primary effusion lymphoma cells by inhibiting CDK1
Furthermore, aged bone marrow exhibits upregulation of phosphorylation (Ueno et al. 2022). Our findings extend
pro-inflammatory cytokines (e.g., IL-1β, IL-6, CXCL9/10) the biological relevance of midkine to hematopoiesis.
and activation of the complement system, reflect- While midkine knockout mice exhibit no overt hemat-
ing a chronic low-grade inflammatory state (Helbling opoietic defects under homeostatic conditions, they
et al. 2019). Concurrent downregulation of extracellu- show enhanced hematopoietic reconstitution after HSPC
lar matrix genes, such as collagens and matrix-remode- transplantation. Similarly, pharmacological inhibition
ling enzymes, further degrades bone marrow integrity with iMDK increases the number of LSK and leukocyte
(See figure on next page.)
Fig. 6 Midkine was an uncharacterized microenvironmental factor. A Quantifying the type of cell–cell interaction across all stages in the atlas.
B Upset plot showing HSPC as receiver between common and unique cell–cell interactions across all stages in the atlas. C Diagram depicting
treatment of Mdk+/+and Mdk−/− mouse after lethal irradiation and transplantation as well as corresponding analyzing time point. D Representative
FACS contour plot and quantification about the percentage of Lin− c‑Kit+ sca1+(LSK cell, Mdk+/+ = 9, Mdk−/− = 8), hematopoietic stem cell (HSC,
Mdk+/+ = 9, Mdk−/− = 8) 21 days after transplantation. Error bars, mean ± SEM. p values, t‑ test. E Representative FACS contour plot of CD45
(Mdk+/+ = 8, Mdk−/− = 7), CD11b (Mdk+/+ = 8, Mdk−/− = 7) and quantification about the percentage of CD45, CD11b and Gr‑1 (Mdk+/+ = 8, Mdk−/− = 7)
at 21 days after transplantation. Error bars, mean ± SEM. p values, t‑ test. F Representative FACS contour plot of CD45 (DMSO = 9, iMDK = 10),
CD11b (DMSO = 9, iMDK = 10) and quantification about the percentage of CD45, CD11b, Gr‑1(DMSO = 9, iMDK = 10) LSK (DMSO = 8, iMDK = 9),
HSC (DMSO = 8, iMDK = 9) after transplantation. Error bars, mean ± SEM. p values, t‑ test. G Competitive repopulation assay donated by DMSO
(CD45.2, n = 4) or iMDK (CD45.2, n = 4) mice bone marrow cells which were approximately 1:1.5 mixed with CD45.1 donor cells and transplanted
into lethally irradiated CD45.1 host mice. Peripheral blood was analyzed at indicted time points. Error bars, mean ± SEM. p values, t‑ test. H FACS
plot quantifying the percentage of EdU+ cell percentage in LSK in both DMSO (n = 5) and iMDK (n = 5) mice after drug treatment. Error bars,
mean ± SEM. p values, t‑ test. I Representative images (dish at day 8 after seeding) and quantification of CFU total cell number, CD45 number
or CD11b number derived from 20,000 Lin− cell isolated from WT mice. DMSO or iMDK was added to MethoCult medium (DMSO = 6, iMDK = 4,
Vehicle = 5, MDK = 5). Error bars, mean ± SEM. p values, t‑ test. J Control (n = 7) or MDK(n = 7) overexpression of HUVEC influence myeloid cell
production when HUVEC were co‑cultured with lineage‑negative HSPC. Error bars, mean ± SEM. p values, t‑ test. K Representative images (dish
at day 8 after seeding) and quantification of CFU total cell number (DMSO + iMDK = 4, iMDK + Mirdametinib = 4), CD45 number (DMSO + iMDK = 4,
iMDK + Mirdametinib = 4) or CD11b number (DMSO + iMDK = 4, iMDK + Mirdametinib = 3) derived from 20,000 Lin− cell isolated from WT mice.
DMSO + iMDK or iMDK + Mirdametinib was added to MethoCult medium. Error bars, mean ± SEM. p values, t‑ test
Ma et al. Cell Regeneration (2025) 14:50 Page 14 of 20
Fig. 6 (See legend on previous page.)
M a et al. Cell Regeneration (2025) 14:50 Page 15 of 20
populations post-transplantation, with no apparent toxic- after iMDK treatment. EdU analysis was performed fol-
ity in normal cells suggesting iMDK as potential approach lowing manufacture’s instruction.
to enhance transplantation efficiency. The proliferation
of HSPC is properly balanced in both physiological con- Irradiation and transplantation
dition and hematopoietic reconstitution. Even though Mice were exposed to a lethal dosage of irradiation fol-
HSPC displayed robust ability to replenish the bone mar- lowed by bone marrow cells transplanted at 4 to 6 h after
row after injury (Cheshier et al. 1999), unlimited HSPC irradiation. For competitive repopulating assays, CD45.1
proliferation is harmful for hematopoietic system and the host mice were lethally irradiated and transplanted with
health. Unnecessary HSPC proliferation leads to DNA approximate 2 × 106 donor-derived (CD45.2 treated by
damage accumulation, which induced malfunction of DMSO or iMDK) BM cells together with approximate 3
this important cell type (Tasdogan et al. 2017). Continu- × 106 host-derived (CD45.1 background) bone marrow
ous replenishment of the immune system and blood cells cells. Peripheral blood from tail vein were analyzed by
places a high demand on HSPC, and sustained high lev- FACS to determine chimaeras level every 4 weeks.
els of stress on these cells can lead to an exhausted HSPC
pool (Zhang et al. 2016), reducing their ability to respond Flow cytometry
to additional emergent condition. During continuous
Bones were dissected and crashed by pestle for more
proliferation, HSPC is easier to become malignant (Car-
than 3 times before cells were collected in 2% FCS-PBS
roll and St Clair 2018). A hallmark of leukemic hemat-
solution. The tissue was immersed in 3 ml dissociation
opoiesis is unlimited generation of hematopoietic cells
solution (2% FCS-PBS solution with approximate 145U/
(Passegue et al. 2003). Therefore, the essential function
ml type 4 Gibco collagenase) and incubated at 37 °C
of bone marrow niche is to properly control the prolif-
for 30 min. Samples were filtered using 100 μm Nylon
eration of HSPC rather than enhancing its proliferation
cell strainer (Biosharp, BS-100-XBS) to get single cell
without any hurdle (Pinho and Frenette 2019). That may
suspensions.
explain, at least partially, why the bone marrow niche
Cells were washed by 2% FCS-PBS solution and then
needs inhibitory factor for HSPC proliferation.
incubated with primary antibodies on ice for 30 min.
Taken together, our vascular niche atlas provides a
Cells were washed again and resuspended in 2% FCS-PBS
powerful resource to decipher the dynamic changes in
for flow cytometry. The following primary antibodies
the bone marrow microenvironment and its interac-
were used in this study: mouse lineage cocktail (Biole-
tion with HSPC. Through this approach, we propose the
gend, 133,307), Sca1-PE/Cy7 (BD, 558,162), cKit-APC
inhibition of midkine as a promising strategy to enhance
(Biolegend, 105,812), CD150-PE (Biolegend, 115,904),
bone marrow transplantation.
CD48-APC/Cy7 (Biolegend, 103,432), CD45.1 (Bioleg-
end, 110,706), CD45.2 (Biolegend, 109,808), CD45-PE/
Cy7 (Biolegend, 103,114), CD11b-FITC (Biolegend,
Materials and methods
101,206), Gr-1-APC (Biolegend, 108,412). Cells were
Animal experiments
washed times by 2% FCS-PBS solution and incubated
C57BL/6 J male mice were used for all analysis of wild- with secondary antibodies for 30 min if necessary. Cells
type mice. Mice were sacrificed between 8 and 10 am. were washed times and used for flow cytometry. Cell
Animals were housed in the animal facility of Guangzhou sorting was performed on a FACS AriaIIu cell sorter (BD
Institutes of Biomedicine and Health. Animal experi- Biosciences, LSR Fortessa SORP).
ments were performed according to the institutional For intracellular staining of EdU by FACS after surface
guidelines and laws, following the protocols (2,021,059) staining of LSK cells, EdU staining was performed fol-
approved by local animal ethics committees. lowing the manufacturer’s instructions (K1078 EdU Flow
Mdk knockout mice (C57BL/6JGpt-Mdkem5Cd3216/ Cytometry Assay Kits (Cy5), APExBIO, K1078). Next,
Gpt) were generated by GemPharmatech (Strain NO. cells were stained with mouse lineage cocktail (Biole-
T012092, Nanjing, China). All animals were routinely gend, 133,307), Sca1-PE/Cy7 (BD, 558,162), cKit-APC
genotyped using respective PCR protocols. Protocols and (Biolegend, 105,812) at room temperature for 20 min.
primer sequences can be provided upon request. iMDK Cells were washed times and used for flow cytometry.
(MCE, HY-110171; 12.8 mg/kg; in DMSO) was adminis- Cell sorting was performed on a FACS AriaIIu cell sorter
trated by intraperitoneal injection (i.p.) for 4 times after (BD Biosciences, LSR Fortessa SORP).
irradiation. In the fourth time, mice were analyzed in 12
h after pharmacological treatment. 10 mg/kg EdU (K1078 Methylcellulose assay
EdU Flow Cytometry Assay Kits (Cy5), APExBIO, K1078) Approximate 2 × 104 Lin− cells from wildtype mice were
was administrated by intraperitoneal injection (i.p.) in 4 h
sorted by FACS and cultured in MethoCultTm medium
