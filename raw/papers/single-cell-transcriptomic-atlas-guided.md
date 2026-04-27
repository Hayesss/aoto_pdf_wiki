---
source_path: /mnt/c/Users/Administrator/Zotero/storage/VE8IMAPL/Gottschlich 等 - 2023 - Single-cell transcriptomic atlas-guided development of CAR-T cells for the treatment of acute myeloi.pdf
ingested: 2026-04-23
sha256: f10d72d96e5d4998
---

nature biotechnology
Article https://doi.org/10.1038/s41587-023-01684-0
Single-cell transcriptomic atlas-guided
development of CAR-T cells for the treatment
of acute myeloid leukemia
Received: 30 March 2022 Adrian Gottschlich 1,2,3,21, Moritz Thomas 4,5,21, Ruth Grünmeier 1,21,
Stefanie Lesch 1, Lisa Rohrbacher3,6, Veronika Igl 1, Daria Briukhovetska 1,
Accepted: 20 January 2023
Mohamed-Reda Benmebarek1, Binje Vick 7,8, Sertac Dede 9,
Published online: 13 March 2023 Katharina Müller9, Tao Xu9, Dario Dhoqina1, Florian Märkl 1,
Sophie Robinson10,11, Andrea Sendelhofert12, Heiko Schulz12, Öykü Umut1,
Check for updates Vladyslav Kavaka13,14, Christina Angeliki Tsiverioti1, Emanuele Carlini1,
Sayantan Nandi1, Thaddäus Strzalkowski 1, Theo Lorenzini 1,
Sophia Stock 1,3,15, Philipp Jie Müller1, Janina Dörr1, Matthias Seifert 1,
Bruno L. Cadilha 1, Ruben Brabenec1,4, Natalie Röder1, Felicitas Rataj1,
Manuel Nüesch1, Franziska Modemann 16,17, Jasmin Wellbrock16,
Walter Fiedler16, Christian Kellner 18, Eduardo Beltrán 11,13,14,
Tobias Herold 3,15, Dominik Paquet 10,11, Irmela Jeremias7,8,15,
Louisa von Baumgarten 15,19, Stefan Endres1,15,20, Marion Subklewe3,6,15,
Carsten Marr 4,22 & Sebastian Kobold 1,15,20,22
Chimeric antigen receptor T cells (CAR-T cells) have emerged as a
powerful treatment option for individuals with B cell malignancies but
have yet to achieve success in treating acute myeloid leukemia (AML) due
to a lack of safe targets. Here we leveraged an atlas of publicly available
RNA-sequencing data of over 500,000 single cells from 15 individuals with
AML and tissue from 9 healthy individuals for prediction of target antigens
that are expressed on malignant cells but lacking on healthy cells, including
T cells. Aided by this high-resolution, single-cell expression approach, we
computationally identify colony-stimulating factor 1 receptor and cluster
of differentiation 86 as targets for CAR-T cell therapy in AML. Functional
validation of these established CAR-T cells shows robust in vitro and in vivo
efficacy in cell line- and human-derived AML models with minimal off-target
toxicity toward relevant healthy human tissues. This provides a strong
rationale for further clinical development.
Chimeric antigen receptor T cells (CAR-T cells) are human-derived effec- suffering from different B cell malignancies, such as B cell lymphoma,
tor cells that are genetically engineered to therapeutically target a spe- B cell acute lymphoblastic leukemia and multiple myeloma2–4. However,
cific epitope on malignant cells1. CAR-T cells targeting the B cell lineage CAR-T cells targeting non-B cell-associated epitopes have yet to show
antigens cluster of differentiation 19 (CD19) or B cell maturation antigen similar response rates5. For instance, in myeloid malignancies, such as
(BCMA) have shown clinical efficacy in heavily pretreated individuals acute myeloid leukemia (AML), common target structures are often
A full list of affiliations appears at the end of the paper. e-mail: sebastian.kobold@med.uni-muenchen.de
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1618
Article https://doi.org/10.1038/s41587-023-01684-0
coexpressed on vital tissues, such as endothelial cells or hematopoietic (1) overexpressed in malignant cells and (2) located on the cell surface.
stem and progenitor cells (HSPCs), increasing the risk for on-target In terms of CAR safety, the candidate should (3) not be expressed on
off-tumor toxicity6,7. Identifying safe target structures is thus pivotal to T cells and (4) show minimal expression across vital, healthy tissues
translate the vast potential of CAR-T cell therapy to myeloid neoplasms. (Fig. 1a). Applying our approach to AML, we used publicly available
AML is the most common acute leukemia in adults, and its molecu- scRNA-seq data from 15 individuals with AML21. From these, a total of
lar heterogeneity has complicated the successful development of 28,404 sequenced healthy and malignant bone marrow cells passed
new therapeutic agents8. Despite upfront curative intent in most indi- quality control (Fig. 1b,c; see Methods for a detailed description of
viduals with combinatorial chemotherapy, disease relapse is frequent, quality control steps). For maximal CAR efficacy, we sought to identify
occurring in over 50% of treated individuals9. After relapse, alloge- candidates with higher expression on malignant HSPC-like cells (herein
neic hematopoietic stem cell transplantation (allo-HSCT) remains termed hematopoietic stem cell (HSC)-like and progenitor (Prog)-like)
the only curative approach; but even then, long-term survival prob- than on healthy cells. Differential gene expression analyses between
abilities are below 20%. Therefore, innovative treatment options rep- malignant and healthy HSPCs revealed 96 genes that were strongly
resent a high unmet medical need. Currently, CAR-T cells targeting overexpressed in HSPC-like cells and were used for further downstream
AML-associated target antigens CD33 and interleukin-3 receptor-α analyses (Extended Data Fig. 1a).
(IL3RA, CD123) are undergoing clinical investigation. Due to preclini- To identify candidates accessible for CAR-T cells on the target cell
cal evidence of off-tumor toxicity toward HSPCs, most clinical trials surface, we used OmniPath22, a large-scale molecular database, to inte-
are evaluating the potential of anti-CD123 or anti-CD33 CAR-T cells grate data from multiple resources23–26 into a comprehensive human
as a bridge-to-transplant regimen before allo-HSCT. Early reports of surface gene library of 4,924 genes (Fig. 1d). Of the 96 genes overex-
these trials have shown only limited therapeutic efficacy10–12. Yet, more pressed in HSPC-like cells, 36 were present in this library. Genes that
complete results of these clinical studies in AML are eagerly awaited. passed all previous filters but showed high expression on T cells (for
Meanwhile, other targets, such as CD70, C-type lectin-like molecule-1, example, CD52 and CRIP1) were excluded from further analysis (Fig. 1e).
FMS-like tyrosine kinase-3 (FLT3), CD44 variant 6 (CD44v6), sialic To minimize on-target off-tumor effects, we processed and harmo-
acid-binding Ig-like lectin-6 (Siglec-6) or CD117, have been tested in nized 11 scRNA-seq datasets from nine healthy human tissues (brain,
preclinical studies as alternative CAR targets13–17. However, clinical vali- lung, lymph nodes, heart, skin, liver, kidney, colon and esophagus)
dation is pending, and expression profiles of most of the targets raise into a massive cross-organ off-target transcriptomic atlas (COOTA)
at least some uncertainties regarding their clinical safety and efficacy. consisting of over 500,000 single healthy cells (Fig. 1f)27–37. A detailed
Newly developed CAR-T cells are often directed to target struc- summary of all datasets used for COOTA is provided in Extended Data
tures that have already been used for antibody therapy. By contrast, Fig. 1b,c. Targets highly expressed in vital non-immune cell lineages
unbiased de novo target screenings for CAR-T cell therapy have rarely or on cell types of tissues in direct proximity to infused T cells (that is,
been conducted18. In addition, until recently, off-tumor antigen pro- endothelium, arteries, veins, bronchial vessels, capillary and smooth
jections could only leverage bulk sequencing data, missing detailed muscle cells) were excluded from further analyses (Fig. 1f).
information about cell-type-specific target antigen expression pat- Using this stringent and rigorous approach, 12 potential can-
terns. Conveniently, the revolution in single-cell technologies in the didates for CAR development remained. Interestingly, most of the
last decade has generated massive single-cell expression datasets described CAR targets for AML (n = 20) failed the thresholds of our
that provide precise information about the transcriptomic anatomy analyses at different levels (Extended Data Fig. 1d). For example, pro-
of healthy and malignant cells19, a mostly untapped resource for thera- totypic AML antigens CD33 and CD123 did not fulfill our strict criteria
peutic development, at least in the context of de novo antigen predic- of overexpression in malignant HSPCs (see Methods for applied thresh-
tions and CAR-T cell development. These advancements allow in-depth olds), most likely due to expression of both antigens on healthy HSPCs.
on- and off-tumor antigen prediction20, offering unique insights into In addition, CD123 had high expression levels across endothelial and
healthy and malignant cells at an unmatched resolution. various lung cell types (see Fig. 2d for detailed analysis).
We thus developed a single-cell RNA-sequencing (scRNA-seq)- To further optimize the safety profile of newly developed
based approach specifically tailored to identify promising antigens CAR-T cells, we reasoned that, if targeted therapies for any of the 12
for CAR-T cell therapy on a discovery AML cohort of 15 individuals21. identified candidates have already been approved by the Food and
We generated a transcriptomic atlas from publicly available datasets, Drug Administration (FDA), the risk for unexpected, severe on-target
consisting of over 28,000 healthy and malignant bone marrow cells off-tumor toxicities of newly developed CAR-T cells will be minimized.
from these individuals and over 500,000 healthy cells from nine of In addition, this could shorten the length of time and decrease reg-
the most vital human tissues. We screened these data for cell surface ulatory hurdles for translation of newly developed CAR-T cells into
antigens expressed on malignant cells with minimal coexpression on clinical routines, as safety of target-directed therapies was previously
healthy cells, including T cells. With rigorous cutoffs, we identified demonstrated. Thus, we used an accessible database of all monitored
two unrecognized targets for CAR-T cells in AML: colony-stimulating FDA-approved drugs that contains information on the interactions,
factor 1 receptor (CSF1R) and CD86. We developed CAR-T cells against pharmacology and chemical structures of drugs and drug targets38. We
both targets and tested their efficacy in vitro and in vivo in cell lines and identified two targets, CD86 and CSF1R, which have already undergone
human-derived models, including primary AML blasts. We assessed the clinical investigation (Fig. 1g). To the best of our knowledge, neither
safety of these CAR-T cells in vitro using advanced primary cell cultures anti-CD86 nor anti-CSF1R CAR-T cells have been implicated for CAR-T cell
for target-expressing cell types, demonstrating a better discrimina- therapy in AML. We thus decided to further investigate their potential.
tory capacity than established anti-CD33 CAR-T cells. In addition, we Both antigens were highly expressed across malignant cells in
used several in vivo models to mitigate safety concerns. Our results 100% of the individuals with AML with captured malignant blasts (11
illustrate the translational potential of an unbiased scRNA-seq-based of 15; Extended Data Fig. 2a,b), despite the heterogeneous molecular
screening approach and lay the basis for clinical development of our profile of the participant collective (see van Galen et al.21 for participant
CAR candidates. characteristics).
To ensure the validity of our analyses and to better reflect the
Results cytogenetic diversity of AML as a disease, we next sought to further
Development of scRNA-seq-based screening algorithm increase the size of our cohort. Thus, we obtained a second publicly
We created an unbiased scRNA-seq-based discovery approach for iden- available scRNA-seq dataset of five additional individuals with AML39
tification of CAR targets. To ensure CAR efficacy, a suitable candidate is (Extended Data Fig. 2c). For the cross-validation of our computational
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1619
Article https://doi.org/10.1038/s41587-023-01684-0
a
e
CD52 CRIP1 CSF1R CD86
Expression
f
COOTA
50
Arterial Capillary Venous 40
30
Predicted
Critical cell clusters Endothelial safe 20 CSF1R
target genes
10
CD86
Smooth muscles
0
0 1 2 3 4 5
9 organs 544,764 single cells log 2 (fold change)
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1620
)eulav
P(
gol– 01
Efficacy Safety
Defined Overexpressed on Cell surface Low expression Minimal off-tumor FDA-approved
criteria malignant cells coding on T cells expression drug targets
CSPA
ap Fi p lt l e ie r d D e H x i S ff p P e r C e re s s n si t o ia n l on O p m at n h i H C P e A llPhoneDB s v c a R n N G A a - l s e e n q e A t M al L . C s A c M O R L O N T A A -seq D ba ru n g k
scRNA-seq AML In silico
van Galen et al. surfaceome
CSF1R
CD86
Genes 17,434 96 36 29 12 2
Illustrated Fig. 1b,c Fig. 1e Fig. 1f
in Extended Data Fig. 1a Fig. 1d Extended Data Fig. 1a Extended Data Fig. 1b,c Fig. 1g
b c d
Mono CellPhoneDB 977
T cells B cells
Cytotoxic cDC
T cells pDC Human protein
NK cells LateEry atlas 2,987
Plasma cells
HSCs Omni 4,924
P G r M og P H Pr S o C g - - l l i i k k e e p C r e o l t l e s i u n r a fa tl c a e s 996 path surface genes
GMP-like
ProMono ProMono-like
Malignant
P Ea ro rl B y E c r e y lls M cD o C n - o li - k li e ke Healthy su I r n fa s c il e ic o o me 2,799
T cells
g
Fig. 1 | A scRNA-seq-based screening approach identifies CSF1R and CD86 expression of newly identified targets. Red crosses indicate targets with high
as potential CAR targets in AML. a, Workflow of computational CAR target expression on T cells, which were excluded from further analyses. Green check
antigen identification by stepwise evaluation against a set of criteria for an marks indicate no significant expression on T cells. f, Harmonization of 11 scRNA-
ideal and effective CAR target antigen. The decreasing numbers of screened seq datasets from nine healthy human tissues into a COOTA consisting of 544,764
AML target genes are shown on the bottom. b,c, UMAP showing 28,404 healthy cells. A detailed summary of all used datasets is provided in Extended Data Fig. 1b.
and malignant cells from data of 15 previously published individuals with AML Targets highly expressed in non-immune cell lineages or on cell types in direct
harboring 15 different mutations21. Normalized gene expression values were proximity to infused T cells (critical cell clusters: arterial, capillary, venous,
log transformed. Colors highlight the different cell types (b) and condition (c). endothelial and smooth muscle cells) were excluded from further analysis.
Cell annotations are provided; NK cells, natural killer cells; GMP, granulocyte– g, Volcano plot showing the remaining two target antigens with their respective
monocyte progenitors; ProMono, promonocytes; EarlyEry, early erythrocytes; FDR-adjusted log (P value) and log (fold change) values from differential
10 2
ProB cells, pro-B cells; Mono, monocytes; cDC, conventional dendritic cells; expression analysis between malignant HSPC-like cells and healthy HSPCs using a
pDC, plasmacytoid dendritic cells; LateEry, late erythrocytes. d, Summary of t-test with overestimated variance. Dashed lines indicate applied thresholds at a
databases used to identify cell surface coding genes. e, Quantification of T cell log (fold change) of 2 and P value of 0.01.
2
Article https://doi.org/10.1038/s41587-023-01684-0
e
THP-1 6 ∆ , M 49 F 3 I ∆ 1, M 62 F 1 I 1 ∆ 1, M 40 F 0 I 100 CSF1R
CD86
Mv4-11 3,241 1,058 8,176 CD33
OCI-AML-3 2,369 287 912
50
PL-21 3,184 1,159 12,389
MOLM-13 585 1,621 2,0977
U937 4,494 –3 5,347
NALM-6 3 0 2 0
–103 0 103 104 105 –103 0 103 104 105 –103 0 103 104 105 CSF1R-APC CD123-BV421 CD33-PE
target identification approach, we used scANVI, a semisupervised vari- (Extended Data Fig. 2d). Next, after extending our target identifica-
ational autoencoder40, to map the data from Petti et al.39 onto a newly tion approach to these five additional individuals with AML (Fig. 1a),
generated reference map of van Galen et al.21 (Extended Data Fig. 2e). both CSF1R and CD86 were again identified as suitable target antigens
In line with the results above, CSF1R and CD86 were preferentially for CAR therapy in this second AML cohort (Extended Data Fig. 2f,g).
expressed in malignant cells compared to healthy hematopoietic cells In summary, using two independent single-cell AML cohorts consisting
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1621
fo
egatnecreP
sllec
evitisop-tegrat
a b
c
f
tnangilaM
yhtlaeH
Cand. Ref.
HSC-like
Prog-like
Mono-like
ProMono-like
GMP-like
cDC-like
HSC
Prog
Mono
ProMono
GMP
cDC
EarlyEry
LateEry
ProB cells Expression
B cells
T cells
Cytotoxic T cells
NK cells
Plasma cells
pDC
CSF1R CD86 CD123 CD33
d
M M e M E F s u n i e S e b l E E d t n s e p r r i o o c c S o c y i t t t i h t r t b l h h h h e r i y l a o e e e t r a m t o o m l l l s e i i i r i t a a a a d d a y s l l l l M M e M E F s u n i e S e b l E E d t n s e p r r i o o c c S o c y i t t t i h t r t b l h h h h e r i y l a o e e e t r a m t o o m l l l s e i i i r i t a a a a d d a y s l l l l M M e M E F s u n i e S e b l E E d t n s e p r r i o o c c S o c y i t t t i h t r t b l h h h h e r i y l a o e e e t r a m t o o m l l l s e i i i r i t a a a a d d a y s l l l l M M e M E F s u n i e S e b l E E d t n s e p r r i o o c c S o c y i t t t i h t r t b l h h h h e r i y l a o e e e t r a m t o o m l l l s e i i i r i t a a a a d d a y s l l l l
M In e n M g at a a N e M k c D e M L a l r o u y y e o r a N n y m m t n p s r o o B K T d o t h p p c c r p a c c c c h h y y i g t e e e e h o o t t i l l l l c e e e i i i l l l l l d d s s s s s s s s s M In e n M g at a a N e M k c D e M L a l r o u y y e o r a N n y m m t n p s r o o B K T d o t h p p c c r p a c c c c h h y y i g t e e e e h o o t t i l l l l c e e e i i i l l l l l d d s s s s s s s s s M In e n M g at a a N e M k c D e M L a l r o u y y e o r a N n y m m t n p s r o o B K T d o t h p p c c r p a c c c c h h y y i g t e e e e h o o t t i l l l l c e e e i i i l l l l l d d s s s s s s s s s M In e n M g at a a N e M k c D e M L a l r o u y y e o r a N n y m m t n p s r o o B K T d o t h p p c c r p a c c c c h h y y i g t e e e e h o o t t i l l l l c e e e i i i l l l l l d d s s s s s s s s s
Neuron I a n l t A s e M s t r e N t n i r m c e e o r u u c o c r r y g o o e t l n n l e i l a s s s s Neuron I a n l t A s e M s t r e N t n i r m c e e o r u u c o c r r y g o o e t l n n l e i l a s s s s Neuron I a n l t A s e M s t r e N t n i r m c e e o r u u c o c r r y g o o e t l n n l e i l a s s s s Neuron I a n l t A s e M s t r e N t n i r m c e e o r u u c o c r r y g o o e t l n n l e i l a s s s s
Oligodendrocytes Oligodendrocytes Oligodendrocytes Oligodendrocytes
Alveolar Alveolar Alveolar Alveolar
Arterial Arterial Arterial Arterial
Bronchial Bronchial Bronchial Bronchial
Capillary Capillary Capillary Capillary
Venous Venous Venous Venous
Smooth muscle Smooth muscle Smooth muscle Smooth muscle
Cardiomyocytes Cardiomyocytes Cardiomyocytes Cardiomyocytes
Basal Basal Basal Basal
Keratinocytes Keratinocytes Keratinocytes Keratinocytes
Melanocytes Melanocytes Melanocytes Melanocytes
Glands Glands Glands Glands
Hepatic stellate Hepatic stellate Hepatic stellate Hepatic stellate
Hepatocytes Hepatocytes Hepatocytes Hepatocytes
Loop of Henle Loop of Henle Loop of Henle Loop of Henle
Podocytes Podocytes Podocytes Podocytes
Proximal tubule Proximal tubule Proximal tubule Proximal tubule
niarB gnuL
edonpmyL
reviL yendiK noloC
sugahposE
nikS traeH niarB gnuL
edonpmyL
reviL yendiK noloC
sugahposE
nikS traeH niarB gnuL
edonpmyL
reviL yendiK noloC
sugahposE
nikS traeH niarB gnuL
edonpmyL
reviL yendiK noloC
sugahposE
nikS traeH
HSC-like Prog-like HSC Prog
3
CSF1R 3 Cand.
CD86
3
CD123 3 Ref.
CD33
CSF1R CD86 CD123 CD33
Exp-
ression
CSF1R CD86 CD123 CD33
Expression
Hb20 T 1 i 7 20 M 2 n 0 20 R 1 n 9 2 K 0 m 18 2 K 0 m 20 20 M 2 d 0 20 R 1 a 8 20 S 19 t20 J 1 s 9 20 M 2 n 0 20 C 1 g 9 2 H 0 n 18 2020 Hb20 T 1 i 7 20 M 2 n 0 20 R 1 n 9 2 K 0 m 18 2 K 0 m 20 20 M 2 d 0 20 R 1 a 8 20 S 19 t20 J 1 s 9 20 M 2 n 0 20 C 1 g 9 2 H 01 n 8 2020 Hb20 T 1 i 7 20 M 2 n 0 20 R 1 n 9 2 K 0 m 18 2 K 0 m 20 20 M 2 d 0 20 R 1 a 8 20 S 19 t20 Js 19 20 M 2 n 0 20 C 1 g 9 2 H 01 n 8 2020 Hb20 T 1 i 7 20 M 2 n 0 20 R 1 n 9 2 K 0 m 18 2 K 0 m 20 20 M 2 d 0 20 R 1 a 8 20 S 19 t20 J 1 s 9 20 M 2 n 0 20 C 1 g 9 2 H 0 n 18 2020
∆MFI 756
2,416
8,684
2,700
6,216
3,137
– C 1 D 0 8 3 6-A 0 PC 103 104 10
7
5
5 Granulocytes
B
cells
T
cells
NK
ce
C
l
M
ls CD14+CD1
I
6–
M
CD14+CD
N
16+
M
CD14–CD16+
Fig. 2 | CSF1R and CD86 are preferentially expressed on malignant HSPC-like were log transformed and visualized in a UMAP embedding. d, Single-cell COOTA
cells compared to healthy HSPCs, and off-tumor expression is restricted screening for target (CSF1R and CD86) and reference (CD123 and CD33) genes.
to infiltrating or tissue-resident immune cells. a, Expression of target and The single-cell transcriptomic atlas consists of a total of 544,764 sequenced cells
reference genes (CD123 and CD33) in single healthy and malignant cell types. from nine different organs. Each field represents the mean expression value per
Normalized expression values were log transformed and scaled to unit variance; cluster. Blank fields indicate cell types not present in a study. e, Representative
Cand., candidates; Ref., references. b, Expression of CSF1R and CD86 target genes flow cytometry images of target gene expression on a panel of six different AML
in malignant (HSC-like and Prog-like; left) and healthy (HSC and Prog; right) cell lines or NALM-6 control cells. Staining for target antigens was performed
stem cells. For visualization purposes, normalized expression values of healthy at least twice; MFI, mean fluorescence intensity. f, Expression of target antigens
HSPCs and a random subsample of malignant HSPCs were log transformed and on human immune cell populations quantified by flow cytometry. Data are
scaled to unit variance. Each peak corresponds to a cell, and peak height indicates shown as mean ± s.e.m. from four different donors; CM, classical monocytes; IM,
expression intensity. c, Expression of CSF1R and CD86 target genes in healthy and intermediate monocytes; NM, non-classical monocytes.
malignant cells from 15 individuals with AML. Normalized gene expression values
Article https://doi.org/10.1038/s41587-023-01684-0
of a total of 20 individuals, we identified CSF1R and CD86 as potential were still broader than those of candidates in clinical use (CD19 and
CAR targets for AML therapy. BCMA), which are almost entirely confined to B cells or B cell sub-
sets11. Therefore, we first tested the safety of the developed anti-target
On- and off-tumor expression analysis of CSF1R and CD86 CAR-T cells in fully immunocompetent syngeneic mouse models. To
Next, we benchmarked the two target antigens CSF1R and CD86 to the ensure similar target expression in mice and humans, we compared
reference genes CD123 and CD33 to ease interpretation of receptor expression of candidates in different organs using available bulk
expression on a transcriptomic level (Fig. 2a–c). CSF1R was expressed sequencing data (Fig. 3a). CSF1R showed higher expression in organs
in all six malignant cell clusters, but was expressed the highest on of both mice and humans, while CD86 was only detected in the spleen.
monocyte-like or conventional dendritic cell-like clusters. CD86 was Also, in line with our COOTA prediction, CSF1R is known to be expressed
most strongly expressed in monocyte-like, promonocyte-like and con- on microglia42, raising additional safety concerns. scRNA-seq analy-
ventional dendritic cell-like clusters (Fig. 2a). In terms of expression in sis of archived mouse brain tissue27 confirmed expression of Csf1r in
malignant HSPC clusters, CSF1R expression was higher than CD86, albeit microglia and similar expression patterns in tissue-resident myeloid
lower than CD123 and CD33 reference genes (Fig. 2a,b). In contrast, cells (Fig. 3b).
CD123 or CD33 were detected in healthy HSCs and progenitors, while Given the above, we decided to use CSF1R to model poten-
both CSF1R and CD86 were only minimally expressed among these cells tial off-target toxicity in mice. We sequenced an mCSF1R
(Fig. 2b). Visualized in a uniform manifold approximation and projec- antibody-producing hybridoma and designed second-generation
tion (UMAP) embedding, the expression profiles of CSF1R and CD86 mCSF1R CART (Extended Data Fig. 3a). Mouse anti-EpCAM CAR-T cells
were very comparable to CD123 and CD33 reference genes (Fig. 2c). (mEpCAM CART) or mCherry-transduced T cells were used as negative
COOTA analysis revealed target antigen expression mainly controls for all experiments (Extended Data Fig. 3a). mCSF1R CAR
in immune cells of myeloid origin (monocytes, macrophages and construct could be efficiently transduced into primary mouse T cells
dendritic cells), similar to the peripheral expression profile of CD33 (Fig. 3c). mCSF1R CART were dose-dependently activated through
(Fig. 2d). CSF1R and CD86 were not highly expressed on epithelial Fc-immobilized recombinant mouse CSF1R protein, as seen by upregu-
or stromal cells (Fig. 2d, top). In organ-specific cell clusters (Fig. 2d, lation of the activation marker CD69 (Fig. 3d, left) and cell surface
bottom), expression was restricted to microglia cells in the brain, as exposure of degranulation marker CD107a (Fig. 3d, right) compared
described in the literature41. We next sought to assess expression of to mEpCAM CART.
the target antigens on a protein level. We performed primary screen- To further validate functionality of the developed mCSF1R CART,
ing using a panel of six different human AML cell lines (THP-1, Mv4-11, we investigated killing capacity toward mCSF1R-expressing cell lines.
OCI-AML-3, PL-21, MOLM-13 and U937) and B cell malignant NALM-6 Therefore, we selected the mouse reticulum cell sarcoma cell line
cells as negative-staining control cells (Fig. 2e). CSF1R and CD86 were J774A.1, which expresses mCSF1R43. Using flow cytometry, we verified
detected on all screened AML cell lines. CD123 and CD33 expression was expression of mCSF1R on J774A.1 cells, while mEpCAM was not detected
measured as a reference (Fig. 2e). Given the similar expression profile (Extended Data Fig. 3b). Coculturing mCSF1R or mEpCAM CART with
on mature, healthy immune cells of our targets to CD33, we decided to J774A.1 tumor cells demonstrated efficient lysis of J774A.1 tumor cells
use CD33 as the main control for all subsequent experiments. by mCSF1R CART (Fig. 3e, left). As a marker of selective activation,
To validate the transcriptomic profiles predicted by COOTA, we high amounts of interferon-γ (IFNγ) were secreted by mCSF1R CART
assessed receptor expression of each candidate antigen on periph- (Fig. 3e, right).
eral blood immune cells from healthy donors using multicolor flow Next, we used in vivo experiments to assess the risk for on-target
cytometry (Fig. 2f). In accordance with our transcriptomic prediction, toxicities. Initially, mCSF1R CART or controls were injected intra-
expression of CSF1R and CD86 was mainly restricted to monocytic cell venously (i.v.) into healthy C57BL/6 mice with limited engraftment
populations with no expression on granulocytes or T cells (Fig. 2f). (Extended Data Fig. 3c–e). To enhance persistence of the T cells, mice
were next preconditioned using whole-body irradiation (WBI; 5 Gy)
Anti-mouse CSF1R CAR-T cells (mCSF1R CART) do not cause 5 d before adoptive cell transfer (ACT) of mCSF1R CART (Fig. 3f). High
toxicity in mice counts of mEpCAM CART were used as positive controls, while mCherry
Despite the stringent thresholds set by our approach and our in-depth T cells were used as negative controls. Following transfer of T cells, we
off-tumor antigen projection, expression patterns of CSF1R and CD86 did not detect a measurable change of weight in mCSF1R CART-treated
Fig. 3 | mCSF1R CART do not cause toxicity in mice. a, Target expression measured with LEGENDplex; n = 3 mice. Statistically significant increases in
(transcripts per million) across organs in humans (top) or mice (bottom) serum cytokine levels (mEpCAM versus mCSF1R CART or mCherry T cell-
quantified using bulk RNA-seq. b, Target expression in single mouse brain treated mice) occurred at day 7; IFNγ (P = 0.0371), CXCL9 (P = 0.0096) and
cells. A UMAP embedding of sequenced brain cells is shown on the left. Each CXCL10 (P < 0.0001); TNFα, tumor necrosis factor-α; VEGF, vascular endothelial
peak corresponds to a cell, and peak height indicates expression intensity. growth factor; GM-CSF, granulocyte–macrophage colony-stimulating factor.
Normalized, log-transformed antigen expression per cell type is shown on j, Treatment regimen to assess neurological toxicity in CX3CR1–GFP reporter
the right. c, Construct expression on transduced primary mouse T cells. mice. k, Weight curves of mice after i.c. (2 × 105) or i.v. (3 × 106) injection of
d, Activation of mCSF1R or mEpCAM CART after incubation with plate-bound mCSF1R CART or mCherry T cells. l,m, Quantification of transferred T cells (l)
mCSF1R measured by flow cytometry. e, mCSF1R or mEpCAM CART cocultured or microglia (m) by TPLSM. The indicated P values in m apply to comparisons
with J774A.1-Luc+ for 48 h. Cell lysis was quantified by BLI (left). Secretion of between all groups. n, Mean body volume of microglia. The indicated P values
mouse IFNγ (mIFNγ) was quantified by enzyme-linked immunosorbent assay apply to comparisons between mCSF1R CART i.c. and mCherry T cells i.c. o,
(ELISA; right). Data in d and e are shown as mean ± s.e.m of three independent Representative maximum intensity projection of microglia or macrophages
experiments. For data in e (right), statistical significance was calculated by (green) in CX3CR1–GFP mice after i.c. injection of mCSF1R CART (red, top)
unpaired t-test. f, Treatment schedule for in vivo toxicity assessment of mCSF1R or mCherry T cells (red, bottom). White arrowheads indicate microglia and
CART. g, Weight curves of mice treated with 3 × 106 mCSF1R CART (n = 9) or macrophages with higher mean density and mean body volume of microglia;
mCherry T cells (n = 11); 6 × 106 mEpCAM CART (n = 5) were transferred as a depth from brain surface, 0–100 µm. Data in k, m and n are shown as
toxicity control. Error bars indicate s.e.m.; NS, not significant. h, Quantification mean ± s.e.m.; mCSF1R CART: i.c. n = 5 and i.v. n = 4; mCherry T cells: i.c./i.v.
of mCherry+ T cells of the parent population (top; parent population: CD3+CD8+ n = 2. Data in l are shown as mean ± s.e.m.; mCSF1R CART: i.c. n = 3 and i.v. n = 4;
cells) or CD11b+ cells (bottom) by flow cytometry. Data are shown as mean mCherry T cells: i.c. one control mouse. For all data, if not otherwise indicated,
± s.e.m. of n = 6 mice. The shown statistical significance applies to day 7. statistical significance was calculated by two-way analysis of variance (ANOVA)
i, Serum cytokine levels 1 d (d1) or 7 d (d7) after ACT. Cytokine levels were with a Sidak multiple-comparison correction.
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1622
Article https://doi.org/10.1038/s41587-023-01684-0
mice as a sensitive surrogate for toxicity in mice (Fig. 3g). In com- criteria, organs were collected for subsequent analyses. Remaining
parison, as described in the literature44, mEpCAM CART-treated mice mCSF1R CART- or mCherry T cell-treated mice were killed 2 weeks
rapidly lost weight 1 week after ACT (Fig. 3g). On day 7, when mEpCAM after ACT, and organ-derived cell suspensions were analyzed by flow
CART-treated mice reached the predefined experimental endpoint cytometry. We detected higher percentages of mCSF1R CART in all
a b
Microglia
Astrocytes
Endothelial cells
Interneurons Microglia
Oligodendrocytes
Smooth muscle cells
Neurons
Neuronal stem cells
Csf1r
c d e
f g h i
j k l
CX3CR1-GFP
1,000
500
Day –28
Implantation cranial mCSF1R 0 window CART
Day 0 -500
ACT 0 4 7 1014 2128
mCherry
T cells
In vivo TPLSM Days 4, 7, 10, 14, 21 and 28
Injection
position Imaging region Cranial
window
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1623
derrefsnart
fo ytisneD
3mm
rep
sllec
800 P =
0.0357
600 NS NS NS 400 NS NS
200
0
0 4 7 1014 2128
ydob
naem ailgorciM
)llec
rep 3mµ(
emulov
100 80
60
40
20
0 mCSF1R CART mCherry T cells
Time after T cell
transfer (d)
Time after T cell
transfer (d)
+yrrehCm
fo
egatnecreP
sllec
T
Brain Lung Liver Kidne
C
y olo
H
n eart Musc
S
le plee
T
n estis
CSF1R Exp-
CD86 ression
Csf1r
Cd86
P < P < P < 0.0001 0.00010.0001 P < P = 0.0001 P = P < 0.0019 0.00020.0001
22
20 18
16
14 –5–3–1025714
Time after T cell transfer (d)
)g( thgieW
Microglia
2
100
50
0
0.125:1 0.25:1 0.5:1
C57BL/6
Day 5 Gy –5 WBI
100 NS
D A a C y T 0 80 NS
60 NS 40 NS
Day 14 FACS 20
Cytokine measurement 0
Histology Blood Brain Kidney Liver
L m
un
p
g
h
node Spleen
o mCSF1R CART i.c.
Ly Baseline Day 7 Day 10 Day 14
50 µm
Day 21
Day 28
20 µm
Baseline Day 4 Day 7 Day 10
m n 50 µm
Day 14
Day 28
20 µm
Microglia or macrophages Activated microglia
Transferred T cells or macrophages Time after T cell
transfer (d)
)%(
sisyl
cificepS
500
400
300
200
100
0
)1–lm
gn(
γNFIm
100 P = 0.003 P < 0.0001 80
250K 80
200K 60
60 150K 40
100K 40
A 20
S
C- 50K
71.2
20
F 0 0 0
–1030 103 104 105 BSA 0.010.1 1 10 BSA 0.010.1 1 10
mCherry
Fc-tagged mCSF1R Fc-tagged mCSF1R
protein (µg ml–1) protein (µg ml–1)
fo
egatnecreP sllec
+96DC
sllec
+a701DC
fo
egatnecreP
MACpEm TRAC R1FSCm TRAC yrrehCm sllec T SBP
P < 0.0005 IFNγ NS IL-10
CCL4
IFNα
CXCL9
CXCL10 1,500 C o TNFα n c e IL-6 n
VEGF 1,000 tra
IL-4
tio
n CCL3 500 (p g CCL2 m
GM-CSF 0 l ) –1
d1d7d1d7d1d7d1d7
30
20
mCSF1R CART i.c.
mCherry T cells i.c. 10 mCSF1R CART i.v. NS
mCherry T cells i.v.
0
–1 5 10 14 19 24 28
Time after T cell
transfer (d)
NS NS NS NS NS
)g(
thgieW
+b11DC
fo egatnecreP sllec
P = 0.0029
P < 0.0001
P < 0.0001 P < 0.0001 P < 0.0001
P < 0.0001
72.0
–1030 103 104 105
mCSF1R CART P = P = P =
mEpCAM 0.01960.00560.0330 CART
mCherry T cells
3,000
2,000
1,000
0
0 7 10 14 21 28
ailgorcim
fo
ytisneD
3mm
rep
sllec
Csf1r Cd86
mCSF1R CART mEpCAM CART
mCSF1R CART mEpCAM CART
mCherry T cells i.c.
Article https://doi.org/10.1038/s41587-023-01684-0
organs than mCherry-transduced T cells, indicative of better persis- into the preexisting anti-mCSF1R CAR backbone, which allows
tence (or antigen-dependent proliferation) of mCSF1R CART (Fig. 3h, direct cross-comparisons of CAR-T cell activation thresholds of both
top). We observed lower numbers of tissue-resident CD11b+ cells in the anti-mouse and anti-human CAR-T cells in mice and humans. In addi-
kidney, liver and lung but not in other analyzed organs (Fig. 3h, bot- tion, we created two fully human anti-CSF1R CAR constructs harboring
tom), most likely due to on-target effects of mCSF1R CART. Multiplex either a CD8 or CD28 hinge domain (hCSF1R CART 1–3; Extended Data
serum cytokine measurements on day 1 or day 7 after ACT revealed Fig. 4a, left). First, we extensively cross-compared the functionality
no differences in cytokine levels on d7 between mCSF1R CART- and of the different anti-hCSF1R CAR constructs. All constructs could be
mCherry T cell- or PBS-treated mice (Fig. 3i). By contrast, high levels efficiently introduced into primary human T cells (Extended Data
of proinflammatory cytokines, such as IFNγ, CXCL9 or CXCL10, were Fig. 4b) and were dose-dependently activated by recombinant
detected in the sera of mice that received mEpCAM CART (Fig. 3i). plate-bound hCSF1R protein (Extended Data Fig. 4c). CAR products effi-
Similarly, serum levels of clinically used markers of organ damage ciently lysed all six human AML cell lines tested but not antigen-negative
(for example, urea, bilirubin and liver enzymes) were elevated in mice NALM-6 cells (Extended Data Fig. 4d). Constructs harboring CD8
treated with mEpCAM CART but not in mice that received mCSF1R hinge domains showed a tendency for higher lytic potency at lower
CART or mCherry T cells (Extended Data Fig. 3g). Finally, we performed effector-to-target (E:T) cell ratios (Extended Data Fig. 4d). To evaluate
histopathological analysis of organs with known high expression of antigen-specific proliferation, we cocultured CSF1R CAR-T cells with
CSF1R. mCSF1R CART-treated mice did not exhibit any signs of organ AML cell lines for 4 or 7 d. All CSF1R CAR-T cells showed antigen-specific,
damage in hematoxylin and eosin-stained lungs, livers or spleens time-dependent proliferation (Extended Data Fig. 4e). Absolute quan-
(Extended Data Fig. 3h). Notably, as previously reported44, lungs of tification of T cell numbers revealed a more robust expansion of CD8
mEpCAM CART-treated mice showed thickening of the alveolar epi- hinge-based anti-CSF1R CAR constructs (Extended Data Fig. 4f). All
thelium, indicative of on-target off-tumor toxicities of the transferred CSF1R CAR-T cells secreted high amounts of IFNγ after coculture with
mEpCAM CART (Extended Data Fig. 3h). THP-1, Mv4-11 or OCI-AML-3 AML cell lines but not when cocultured
To investigate the homing and killing potential of CAR-T cells in the with NALM-6 control cells (Extended Data Fig. 4g). Building on these
brain, we made use of CX3CR1–GFP reporter mice, which enable direct results, we decided to further proceed with CSF1R CAR-T cells harbor-
visualization of CAR-T cell–microglia interaction by two-photon laser ing a CD8 hinge domain (hCSF1R CART 1, herein named hCSF1R CART).
scanning microscopy (TPLSM). After implantation of cranial windows, Constructs for human CD86 CAR-T cells (CD86 CART) and human
mCSF1R CART or mCherry-transduced T cells were either i.v. or intrac- CD33 CAR-T control cells (CD33 CART) were similarly designed
ranially (i.c.) implanted into CX3CR1–GFP reporter mice (Fig. 3j–o). (Extended Data Fig. 4a, right). All CAR-T cell products could be effi-
T cell–microglia interactions, change in microglia morphology and ciently introduced into primary human T cells (Fig. 4a). To validate
reduction of overall microglia counts were monitored using TPLSM functionality of CD86 CART and to compare sensitivity thresholds of
for a total of 28 d (Fig. 3l–o). Again, we observed no changes in weight both newly developed therapeutics, both CAR-T cells were incubated
or behavior across all treatment groups (Fig. 3k). We detected high with their respective plate-bound antigens (Fig. 4b). Activation of
T cell numbers following i.c. implantation of mCSF1R CART or mCherry CD86 CART was already observed at very low concentrations of target
T cells (Fig. 3l,o). These numbers gradually declined over the course of protein (0.01 µg ml–1). In comparison, hCSF1R CART required concen-
28 d, regardless of whether mice were implanted with mCSF1R CART or trations of 1 µg ml–1 or higher (Fig. 4b). We cocultured all CAR-T cells
mCherry T cells. At day 28, no transferred T cells could be detected in any with AML cell lines and assessed both specific lysis of AML cells and
group (Fig. 3l,o). Furthermore, microglia numbers did not substantially antigen-dependent proliferation (Fig. 4c,d). hCSF1R and CD86 CART
differ between any of the groups (Fig. 3m,o). Following i.c. implantation efficiently lysed all six AML cell lines, comparable to CD33 CART
of T cells, mean body volume of microglia increased, most likely due to (Fig. 4c), and proliferated to a similar extent (Fig. 4d). CD19 CAR-T cells
activation of the cells45 (Fig. 3n,o). This activation was most pronounced (CD19 CART) were used as control-transduced cells.
in mice injected with mCSF1R CART (Fig. 3n,o). However, by day 28, To prove in vivo efficacy of newly developed CAR-T cells, we
signs of microglia activation diminished in all groups (Fig. 3n,o). After injected NOD-scid Il2rgnull (NSG) mice with a lethal dose of Mv4-11 AML
i.v. injection of T cells, we detected neither mCSF1R CART nor mCherry cells and treated them with hCSF1R, CD86, CD33 or CD19 (control)
control T cells in the brain and observed no signs of microglia activation CART (Fig. 4e). We monitored tumor progression using biolumines-
or depletion (Fig. 3k–o and Extended Data Fig. 3i). Our results suggest cence imaging (BLI). Both hCSF1R and CD86 CART eliminated Mv4-11
that, despite expression of target antigens on tissue-resident immune tumor burden in vivo (Fig. 4f–h). To deliver in vivo proof for another
cells in different organs and on microglia, there were no relevant safety AML model, we injected a lethal dose of THP-1 cells i.v. into NSG mice
signals that would prevent further therapeutic development. and treated them with CSF1R, CD33 or control CART (Fig. 4e). Again,
hCSF1R CART efficiently controlled experimental leukemia with similar
Anti-human CAR-T cells exhibit high potency in AML xenograft complete remission (CR) rates as CD33 CART (hCSF1R CART: CR in
models seven of ten; CD33 CART: CR in eight of ten), with overall survival of up
After proving the safety of CSF1R in various syngeneic mouse models, to 80 d after tumor cell injection (Fig. 4i–k). In summary, we were able
we next aimed to validate the targets in human models. We cloned to demonstrate both in vitro and in vivo efficacy of newly developed
an anti-human CSF1R-binding single-chain fragment variable (scFv) hCSF1R and CD86 CART toward a large panel of human AML cell lines.
Fig. 4 | Anti-target CAR-T cells are functional and efficiently lyse AML cell for 7 d at an E:T ratio of 0.5:1 to assess proliferation. One representative image
lines in vitro and in vivo. a, Representative flow cytometric images of construct of three different donors is shown. e, Diagram of the treatment scheme used for
expression on primary human T cells. b, Activation of hCSF1R or CD86 CART after in vivo experiments. f–h, BLI images (f) survival curves (g) and quantification of
incubation with plate-bound hCSF1R or hCD86 protein was quantified by flow tumor burden (h) in Mv4-11 tumor-bearing mice after treatment with different
cytometry. Data are shown as mean ± s.e.m of three different donors. c, hCSF1R or CAR-T cells; n = 5 mice per group. i–k, BLI images (i), survival curves (j) and
CD86 CART were cocultured with luciferase-positive target antigen-expressing quantification of tumor burden (k) of THP-1-bearing mice treated with hCSF1R
AML tumor cell lines or antigen-negative NALM-6 control cells expressing CART or control-transduced T cells; n = 10 mice per group. Shown are pooled
luciferase for 48 h at the indicated E:T ratios. CD33 and CD19 CART (CTRL- data ± s.e.m. from two independent experiments. Red crosses in f and i indicate
transduced) were used as positive or negative controls, respectively. Cell lysis mice that succumbed to disease. For all experiments, statistical significance was
was quantified by BLI. Data are shown as mean ± s.e.m of three different donors. calculated by two-way ANOVA with a Sidak multiple-comparison correction. For
d, Dye-labeled CAR-T cells were cocultured with the above indicated cell lines Kaplan–Meier curves, statistical significance was calculated with a log-rank test.
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1624
Article https://doi.org/10.1038/s41587-023-01684-0
b
100
50
0
–50
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1625
)%(
sisyl
cificepS
d
g
weeks) 0
mice ( 1
0
g bearin 2
4-11-
3 Mv
on
in
4
h
me after T
cell
injecti
5
7 Ti 9
0
i j k
THP-1
hCSF1R CART CD33 CART CTRL transduced
0
Ti me after T
cell
injecti on
in
T HP-1- bearin
g
mice (
weeks)
6
4
2
10
A-CSF
80 250K
200K 60
150K 40 100K
20 50K 49.8 52.7 62.0 50.3
0 0
–103 0 103 104 105 –103 0 103 104 105 –103 0 103 104 105 –103 0 103 104 105
c-Myc-FITC Fc-tagged protein Fc-tagged protein
(µg ml–1) (µg ml–1)
hCSF1R CART CD86 CART CD33 CART CTRL transduced
100 100 100 100 100 100
50 50 50 50 50 50
0 0 0 0 0 0
–50 –50 –50 –50 –50 –50
0.125:1 0.25:1 0.5:1 0.125:1 0.25:1 0.5:1 0.125:1 0.25:1 0.5:1 0.125:1 0.25:1 0.5:1 0.125:1 0.25:1 0.5:1 0.125:1 0.25:1 0.5:1 0.125:1 0.25:1 0.5:1
NALM-6 Target
control cell
+ –
– +
+ –
– +
+ –
– +
+ –
– +
Far Red proliferation dye
+96DC
fo egatnecreP sllec T
P < 0.0001 50 P < 0.0001 P < P <
0.00010.0001 40 P = P <
0.00010.0001
P = 30 P = 0.0039 P < 0.0208 0.0001 20
10 P =
0.0192
0
BSA0.01 0.1 1 10 BSA0.01 0.1 1 10
+a701DC
fo egatnecreP sllec T
hCSF1R CART CD86 CART CD33 CART
THP-1
M 1 v 0 4 6 -11 D – a 3 y D – a 3 y 1 i. 0 v 6 . i.v.
hCSF1R CD86 CART CART
4 × 106 to 6 × 106
CAR-T cells Day
i.v. 0
CTRL CD33 transduced CART BLI survival
109
108
107
NS 106 P < 0.0001 105
104
103
ecnaidaR
)1–rs
2–mc
1–s p(
f
Mv4-11
CD86 CART CD33 CART CTRL transduced
P = 0.0330P = 0.0023
NS
P = 0.0023
109
108
107
106 NS NS 105 104
103
1 2 3 4 5 7 9
Time after T cell injection in
Mv4-11-bearing mice (weeks)
100
50 NS
P < 0.0001
0 0 20 40 60 80 Time after THP-1 injection (d)
lavivrus
fo ytilibaborP
100
50
0
0 20 40 60 80
Time after Mv4-11 tumor injection (d)
ytilibaborP lavivrus
fo
a
CTRL transduced
c
THP-1 Mv4-11 OCI-AML-3 PL-21 MOLM-13 U937 NALM-6 (control)
101 102 103 104 105 101 102 103 104 105 101 102 103 104 105 101 102 103 104 105 101 102 103 104 105 101 102 103 104 105
e
Mv4-11 NSG THP-1 hCSF1R CART 1.00
(f–h) (i–k)
) rs
mc s
p(
1–
2–
1– ecnaidaR
Minimum 1 × 105 Maximum 1 × 107
1.00
) rs mc s p( 1– 2– 1– ecnaidaR P < 0.00 P 0 < 1 0.0001
ecnaidaR
)1–rs
2–mc 1–s
p(
Minimum 1 × 106
Maximum 1 × 108
1.00
) rs
mc
s p(
1–
2–
1– ecnaidaR
0 Minimum 1 × 105
Maximum 1 × 107 1.00
) rs mc s p( 1– 2– 1– ecnaidaR Tim 0 e a 2 fter 4 T c 6 ell i 7 njec 9 tion 10 in 0 THP-1-bearing mice (weeks)
Minimum 1 × 106
Maximum 1 × 108
Article https://doi.org/10.1038/s41587-023-01684-0
hCSF1R and CD86 CART are effective in primary human models CD33 CART in PDX-388, derived from an individual with AML at initial
We next assessed receptor expression in primary AML samples. diagnosis with KMT2A rearrangement (European LeukemiaNet 2017,
Until now, CSF1R expression on primary AML blasts was thought to adverse prognosis; Fig. 5k–m). Notably, expression of CSF1R on PDX-
be restricted to ‘AML-supportive cells’ or only to mature leukemic 388 samples mimicked the above-described pattern; following thawing
cells46. Indeed, when analyzing surface CSF1R expression on frozen of the cells, CSF1R was not expressed on PDX-388 cells but was detect-
bone marrow samples immediately after thawing, we could not detect able after at least 24 h of in vitro culture (Extended Data Fig. 5h) and
any measurable receptor expression by flow cytometry (Fig. 5a,b). also in vivo in bone marrow sections of control-treated PDX-388 mice
However, when primary AML cells were cocultured on MS-5 mouse (Extended Data Fig. 5i). hCSF1R and CD86 CART induced sustained
bone marrow stromal cells (Extended Data Fig. 5b), we observed a remission in all treated mice over a period of 85 d (CR in ten of ten for
strong, time-dependent increase of CSF1R expression (Fig. 5a,b). We CSF1R CART and three of three for CD86 CART; Fig. 5k–m).
hypothesized that these discrepancies in measurable surface CSF1R Interestingly, in this model, CD33 CART completely failed to con-
expression were most likely due to receptor downmodulation during trol tumor growth in all mice (CR zero of ten). We excluded manufactur-
the freezing and thawing process. To probe this, we analyzed receptor ing failure of CD33 CART in vitro (Extended Data Fig. 5j). Furthermore,
expression on AML cell lines after freeze–thaw cycles. Similar to the in a separate cohort, we verified that CD33 CART were present in the
results seen on primary AML blasts, CSF1R was undetectable directly circulation of treated mice (Extended Data Fig. 5k, left) and expressed
after thawing but regained high expression after 24 to 48 h of culture the CAR on the cell surface (Extended Data Fig. 5k, right). Ex vivo flow
(Extended Data Fig. 5a). To further exclude any cell culture artifacts, cytometric measurement of CD33 on PDX-388 blasts revealed a strong
we analyzed surface receptor expression on primary AML blasts after decrease of CD33 surface expression on PDX cells of mice treated
culturing in cytokine-rich medium47 (Extended Data Fig. 5c). Again, with CD33 CART compared to CD19 CART (Extended Data Fig. 5l,m).
CSF1R was highly expressed on malignant primary AML blasts after Failure of CD33 CART to control tumor burden was thus most likely
culture (Extended Data Fig. 5d). We also confirmed expression of CD86 due to downregulation of surface CD33 expression on PDX-388 blasts.
on primary AML blasts (Fig. 5c). However, the detailed biological mechanism remains elusive and still
Our single-cell gene expression analysis revealed lower expression requires further characterization.
of CSF1R and CD86 in malignant HSPCs than CD123 and CD33 reference To unambiguously validate the potential of hCSF1R CART in vivo, we
genes. Thus, we analyzed the protein expression of CSF1R and CD86 on used a third PDX model (PDX-372; Extended Data Fig. 6a–e) and a third
malignant HSPC-like cells (Extended Data Fig. 5e–g). Both, CSF1R and cell line xenograft model (OCI-AML3; Extended Data Fig. 6f–h). PDX-372
CD86 were expressed on malignant HSPC-like cells, showing no differ- samples were again derived from an individual with relapsed AML with
ences in expression between these cell types (Extended Data Fig. 5f,g), high-risk cytogenetics and TP53 mutation (Extended Data Table 1). In
illustrating the conserved expression of target antigens on these cells. addition, to create more challenging models, we transferred reduced
Next, we cocultured primary AML samples with CAR-T cells and numbers of CAR-T cells into PDX-372-bearing mice (Extended Data
determined specific lysis by flow cytometry. hCSF1R and CD86 CART Fig. 6a). hCSF1R CART stunted AML growth in three of five mice. Detected
specifically lysed primary AML samples comparable to CD33 CART at BLI signal did not vary between hCSF1R and CD33 CART (Extended Data
low E:T ratios (Fig. 5d). To reflect the genetic heterogeneity of AML, Fig. 6b,c). As previously described for PDX-388, immunohistochemical
seven different primary AML specimens with differing cytogenetics analysis revealed high expression of CSF1R on PDX cells in vivo (Extended
were used for in vitro assays. To probe whether new anti-target CAR Data Fig. 6e). hCSF1R CART transferred into OCI-AML3 tumor-bearing
can be introduced into T cells derived from individuals with AML, we mice were similarly effective (Extended Data Fig. 6f–h).
transduced anti-hCSF1R CAR constructs into T cells of individuals To gain a better understanding of the expression patterns of CSF1R
suffering from AML (Fig. 5e). Human-derived hCSF1R CART were then and CD86 in the complex molecular landscape of AML and of poten-
cocultured with autologous primary AML blasts, resulting in potent tially differing expression patterns in different AML subtypes, we used
lysis of primary samples (Fig. 5f). a published large-scale dataset (the Leukemia MILE study) and analyzed
To prove efficacy of hCSF1R and CD86 CART in more relevant the expression of CSF1R and CD86 compared to CD123 and CD33 refer-
in vivo models, we transplanted cytogenetically distinct human-derived ence genes. Similar to CD33, CSF1R and CD86 were broadly expressed in
xenograft (PDX) models48 into mice and treated them with the respec- different subtypes, with highest expression observed in KMT2A::MLLT3
tive CAR-T cells. First, we selected PDX-573, a model that was derived (MLL::AF9), t(15;17) and inv(16)-mutated AML (Extended Data Fig. 6i).
from an individual with relapsed AML with high-risk cytogenetics Given the comprehensive panel of different in vitro and in vivo
(European LeukemiaNet 2017, adverse prognosis; see Extended Data models used throughout our studies, we next sought to investigate
Table 1 for detailed characteristics). Three weeks later, we injected whether we can determine an antigen threshold for effective CAR-T cell
hCSF1R, CD86, CD33 or CD19 CART (Fig. 5g–j). All CAR-T cells were therapy in AML. However, we did not observe correlations between
highly effective, inhibiting tumor outgrowth in all treated mice (five antigen site density measured with flow cytometry and lysis capacity
of five; Fig. 5h–j). Next, we tested the efficacy of hCSF1R, CD86 and of CAR-T cells for any of the tested antigens (Extended Data Fig. 6j).
Fig. 5 | CSF1R and CD86 are readily detected on primary AML samples, and were cocultured with primary AML samples from the same donor. Experiments
hCSF1R CART show efficient lysis of primary AML samples in vitro and in vivo. were performed as outlined in d. Data in e and f are shown as mean ± s.e.m. of
a, Expression of CSF1R following thawing of primary AML samples over 72 h. Each three different autologous donors. g, Summary of treatment scheme used for in
line represents one individual. b, Representative histograms of CSF1R (colored) vivo experiments. h–j, BLI images (h), survival curves (i) and BLI quantification
expression on primary AML samples over time in comparison to isotype control of tumor burden (j) of PDX-573 tumor-bearing mice injected with 6 × 106 hCSF1R,
(gray). c, Expression of CD86 on primary AML samples. Each dot represents one CD33 CART or control-transduced T cells (n = 5 mice per group). P values in j
individual. Left: percentage of CD86+ cells gated to isotype. Right: representative were calculated at week 8. White crosses in h indicate censored mice, while red
histograms of four different individuals. Data are shown as mean ± s.e.m. of 11 crosses indicate mice that succumbed to disease. k–m, BLI images (k), survival
different primary AML samples. d, hCSF1R, CD86 or CD33 CART or untransduced curves (l) and BLI quantification of tumor burden (m) of PDX-388 tumor-bearing
T cells (UT) were cocultured with primary AML samples for 72 h. Specific lysis mice injected with 6 × 106 hCSF1R, CD86 or CD33 CART, control-transduced T
was assessed by flow cytometry. Data are shown as mean ± s.e.m. of seven cells or PBS (n = 3–10 mice per group). CD86 CART treatment was performed
different primary AML samples. Indicated P values apply to an E:T ratio of 0.5:1. separately. For all experiments, statistical significance was calculated by two-way
e, hCSF1R CAR construct transduced into T cells of individuals with AML. Left: ANOVA with a Sidak multiple-comparison correction. For Kaplan–Meier curves,
transduction efficiency of human AML-derived CAR-T cells. Right: representative statistical significance was calculated with a log-rank test.
flow cytometry image. f, Human-derived CAR-T cells or untransduced T cells
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1626
Article https://doi.org/10.1038/s41587-023-01684-0
In summary, using three different, cytogenetically distinct PDX cells with hCSF1R, CD86 and CD33 CART or untransduced T cells for
models and three cell line xenograft models, we were able to pro- 24 h (Fig. 6c). CD34+ HSPCs were exclusively lysed by CD33 CART
vide strong evidence of functionality of newly developed anti-target (Fig. 6c, left). Also, CD33 CART secreted more IFNγ into coculture
CAR-T cells in vitro and in vivo. supernatant than hCSF1R or CD86 CART (Fig. 6c, right). To further
validate these results, we performed conventional colony-forming
Toxicity analyses of hCSF1R and CD86 CART unit (c.f.u.) assays. Colony counts of c.f.u.-E and burst-forming unit
After having verified the expression on malignant AML cells, we next (BFU)-E were higher when HSPCs were cocultured with hCSF1R CART
evaluated target antigen expression on CD34+ HSPCs. Using flow than when they were cocultured with CD33 CART, indicative of bet-
cytometry, we demonstrated lower expression of CSF1R and CD86 ter survival of stem cells in the presence of hCSF1R CART (Fig. 6d).
than CD33 on healthy HSPCs (Fig. 6a,b). To directly assess toxicity Importantly, colony counts of HSPCs cocultured with either hCSF1R
toward HSPCs, we cocultured enriched bone marrow-derived CD34+ CART or untransduced T cells did not vary (Fig. 6d).
a b
72 h
48 h
24 h
0 h
–103 0 103 104 –103 0 103 104 –103 0 103 104 –103 0 103 104 –103 0 103 104
CSF1R-APC
c d e f
g h
eks) 0
e
w
e ( 2
c
mi
g eari n 4
b 3- 57 6 X-
D
P n n i 8 o cti
e
ell i nj 9 1.00
m e
aft er T c 10
) rs
mc s p(
1–
2– 1– ecnaidaR
Ti 12 0
k
0
0
1
2
3 0
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1627
ni noitcejni
llec
T
retfa
emiT
)skeew(
ecim
gniraeb-883-XDP
100 AML12
AML13
AML14
AML15
50 AML16
AML17
AML18
AML19
0 AML20
0 24 48 72
Time after thawing (h)
150
250K
200K 100
150K
50 100K
50K 64.0
0 0
–103 0 103 104 –103 0 103 104 105
CD86-APC c-Myc-FITC
i
Days
PDX-573 Day −18, −27 PDX-388 i.v. –22 and −45 i.v.
hCSF1R CD86 CART CART j
4 × 106 to 6 × 106 CART Day
i.v. 0
CTRL CD33 transduced CART
BLI survival
PDX-388 m
hCSF1R CART CD86 CART CD33 CART CTRL transduced
sllec
+68DC
fo
egatnecreP
80
60
40
20
0
RAC fo
egatnecreP
decudsnart
150
100
50
0
)%( sisyl
cificepS
100
NS NS NS
NS P < 0.0001
50
0
)%( sisyl
cificepS
)1–rs 2–mc
1–s p(
ecnaidaR
100
NS P = 0.0316
NS
P = 0.0259
50
0 0 50 100
Time after PDX-573 tumor injection (d)
NS P < 0.0001
NS P < 0.0001
NS P < P < 0.0001 NS P = P < 0.0001
P = 0.00600.0001 P = 0.02820.0005
P = 0.0056 P = 0.0007
109 108
107
106
105
104
103
0 1 2 3
Time after T cell injection in PDX-388-bearing mice (weeks)
lavivrus
fo
ytilibaborP
Primary AML blasts
AML human-
derived T cells
Time after T cell injection in PDX-573-bearing mice (weeks)
A-CSF
107
106
105
104
103
)1–rs 2–mc
1–s p(
ecnaidaR
Time after PDX-388 tumor injection (d)
lavivrus
fo ytilibaborP
P < 0.0001
hCSF1R CART
CD86 CART
CD33 CART
UT
PDX-573
PDX-573 NSG PDX-388 hCSF1R CART CD86 CART CD33 CART CTRL transduced (h–j) (k–m)
l
100
50
0
0 50 100
sllec
+R1FSC
fo
egatnecreP
AML 1:1 0.5:1 U
C
T SF1R 1:1 0.5:1
0 2 4 6 8 10 12
Minimum 1.00 × 104 Maximum 1.00 × 107
1.00
) rs mc s
p(
1– 2– 1– ecnaidaR
Minimum 1.00 × 105 Maximum 1.00 × 107
1.00
) rs
mc s
p(
1– 2–
1– ecnaidaR
Minimum 1.00 × 106 Maximum 1.00 × 108
Article https://doi.org/10.1038/s41587-023-01684-0
a b c d
800
600
400
200
0
c.f.u.-E BFU-E c.f.u.-G M
e f g
i
h CSF1R CD86 CD33
Astrocytes
Endothelial cells
Interneurons
Microglia
Oligodendrocytes
Smooth muscle cells
Neurons
Neuronal stem cells
Expression
CSF1R 4
CD86 3
CD33 4
l
105
104
iMGL 81.5 ∆MFI ∆MFI ∆MFI
12
4
103 1,120 1,001 1,703
V
B -5 0
4 D C–103
–103 0 103 104 105 0 102 103 104 105 –103 0 103 104 –103 0 103 104
CD11b-BV786 CX3CR1-BV510 CSF1R-APC CD33-PE-Cy5
Next, we analyzed expression of target antigens on samples of untransduced T cells with HD samples revealed higher lysis of HD
healthy human bone marrow donors (HD samples; Fig. 6e,f). Again, samples (Fig. 6g, left) and increased secretion of IFNγ by CD33
surface CSF1R expression could only be detected after at least 24 h CART (Fig. 6g, right). Both lysis of HD samples and IFNγ secretion
of culture (Fig. 6e), but its expression remained lower than that of did not differ between hCSF1R CART and untransduced T cells
CD86 or CD33 (Fig. 6f). Cocultures of hCSF1R and CD33 CART or (Fig. 6g).
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1628
tnuoc
ynoloc
dezilamroN
NS NS
80 NS
60 NS
40 NS
20
0
)1–lm
gn(
γNFIh
100
NS 50
0
–50
hCSF1R CART CD86 CART
CD33 CART UT
)%(
sisyl
cificepS
P = 0.0035 P = 0.0478
100 P = 0.0018 P = 0.0154 P = 0.0002
250K
P = 200K 0.0414
150K 50 100K
50 15.4
C- A 50K 48.3 98.9
S
0 F 0
–103 0 103 104 –103 0 103 104 –103 0 103 104
CSF1R-APC CD86-BV605 CD33-PE-Cy5
sllec
evitisop
fo egatnecreP
P < 0.0001
P = 0.0009 Healthy donor-derived HSPCs
P = 0.0156
CSF1R CD86 CD33
100
50
0
–50
)%(
sisyl
cificepS
800
600
400
200
0
)1–lm
gn(
γNFIh
100
250K 80
200K
72 h 60
150K
48 h 40 100K
2
0
4
h
h 2
0
0
S S
C- A 50
0
K
35.8 56.3
–1
C
03
SF1R-APC
0 103 104 CSF1R CD86 CD33 –1
C
03
SF1R-A
0
PC
103 104
C
–1
D
0
8
3
6-BV
0
605
103 104
C
–
D
10
3
3
3-P
0
E-Cy
10
5
3 104
sllec
evitisop
fo
egatnecreP
100 HD1
HD2 NS HD3
50
0
02448 72
Time after
thawing (h)
sllec
+R1FSC
fo
egatnecreP
hCSF1R CART CD33 CART
UT
10 NS
8
6 NS
NS 4
2
0
hCSF1R CART CD33 CART UT
)1–lm
gn(
γNFIh
NS NS
100 NS
50
0
–50
–200
1:1 0.2:1 1:1 0.2:1
)%(
sisyl
cificepS
NS NS
P = 0.0005 HD samples P = P < P = P = P = 0.00120.0001 0.04740.0095
0.0037
72.1
j k
iMGLs iMGLs
Fig. 6 | hCSF1R CART show better discriminatory capacity toward healthy shown as mean ± s.e.m. from three different donors. g, hCSF1R and CD33 CART or
human hematopoietic cells than CD33 CART. a, Target expression on magnetic- untransduced T cells were cocultured with HD for 72 h at the indicated E:T ratios.
activated cell sorting-enriched, bone marrow-derived CD34+ HSPCs. Data are Left: off-tumor lysis of CAR-T cells assessed by flow cytometry. Right: activation
shown as mean ± s.e.m. of two to three independent, pooled HSPC donors. of T cells quantified by IFNγ secretion. Data are shown as mean ± s.e.m. from
b, Representative flow cytometric image of target expression on HSPCs. c, CSF1R, 11 different samples. h,i, Quantification of log-transformed normalized target
CD86 or CD33 CART or untransduced T cells were cocultured with HSPCs for expression in 13,067 single human brain cells (h). Each peak corresponds to a
24 h at an E:T ratio of 2:1. Left: lysis of HSPCs was quantified by flow cytometry. cell, and peak height indicates expression intensity. A UMAP plot illustrating the
Right: IFNγ secretion was measured by ELISA; hIFNγ, human IFNγ. d, CSF1R and expression patterns of CSF1R, CD86 and CD33 in human brain cells is shown (i).
CD33 CART or untransduced T cells were cocultured with HSPCs for 24 h at an j, Phenotype of human iMGL. k, Representative histograms of CSF1R and CD33
E:T ratio of 2:1, and a c.f.u. assay was performed. Colony count was quantified expression on iMGL. l, hCSF1R CART, CD33 CART or untransduced T cells were
after 14 d. Data in c and d are shown as mean ± s.e.m. from three (c) or four (d) cocultured with iMGL for 24 h at the indicated E:T ratios. Left: lysis of iMGL was
different donors. e, CSF1R expression on HD samples. Left: percentage of CSF1R+ quantified by flow cytometry. Right: T cell activation was quantified by ELISA.
cells gated to isotype. Right: representative histograms of CSF1R expression Data are shown as mean ± s.e.m. from five T cell donors. For all experiments,
on HD. f, Quantified target expression on HD. Left: percentage of positive cells statistical significance was calculated by two-way ANOVA with a Sidak multiple-
gated to isotype. Right: representative flow cytometric image. Data in e and f are comparison correction.
Article https://doi.org/10.1038/s41587-023-01684-0
scRNA-seq analysis of single human brain cells confirmed expres- might increase the risk of immunosuppression and ensuing severe
sion of CSF1R in microglia (Fig. 6h,i). On a single-cell level, CSF1R infection. However, CTLA-4 fusion proteins, such as abatacept (target-
showed higher expression in microglia than CD86 or CD33 (Fig. 6h,i). ing both CD80 and CD86), have received approval by the FDA and are
To model toxicity of CAR-T cells toward human microglia, we generated clinically used for the treatment of autoinflammatory disorders61. In
induced pluripotent stem cell (iPSC)-derived human microglia-like clinical studies, abatacept was generally well tolerated61.
cells (iMGLs)49,50 and verified their phenotype (Fig. 6j). Both CSF1R For both CSF1R and CD86, the measured antigen site densities were
and CD33 were highly expressed on iMGLs (Fig. 6k). Cocultures of rather low, especially compared to CD33 expression, which was high.
human iMGLs with CSF1R CART, CD33 CART or untransduced T cells Yet, despite our extensive functional validation, we did not observe
demonstrated lysis of human iMGLs by both CAR at high E:T ratios of marked differences between CSF1R and CD86 CART compared to estab-
1:1 (Fig. 6l, left). At more physiological E:T ratios (0.2:1), neither CSF1R lished CD33 CART. Along these lines, we did not observe a correlation
nor CD33 CART were able to lyse human iMGLs, consistent with our between lysis capacity of CAR-T cells and site density of the respective
in vivo data (Fig. 6l, left). IFNγ release mimicked the results obtained target antigen. To a certain extent, these findings are in line with recent
from flow cytometric analyses (Fig. 6l, right). In summary, our data reports observed for anti-mesothelin CAR-T cells in solid tumors62.
suggest a superior discriminative capacity toward healthy hemat- Several factors, such as affinity and binding properties of the used scFv
opoiesis of our newly developed CAR-T cells compared to CD33 CART and conformation of the target antigen, can positively or negatively
and indicate that microglia might not be a relevant off-tumor target influence these CAR–tumor cell interactions. Ultimately, while high
of anti-CSF1R CAR-T cells. target antigen expression undoubtedly increases killing efficacy, our
data suggest that, in some cases, functional cross-comparison might
Discussion help to identify promising target antigens, despite, on first glance
We developed an unbiased scRNA-seq approach for de novo target rather low antigen expression.
identification and in-depth, high-resolution off-tumor mapping across Similar to previous results in AML18, we were not able to identify
multiple tissues that is specifically tailored to predict potential candi- target antigens with expression limited to a single immune cell line-
dates for CAR-T cell therapy. Applying our approach to AML, we identi- age, as is the case for CD19 or BCMA in B cell malignancies. However,
fied two target antigens: CSF1R and CD86. Extensive in vitro and in vivo expression of our prime candidates is limited to immune cells of mye-
validation revealed broad expression on AML blasts, strong and durable loid origin (monocytes, tissue-resident macrophages and dendritic
treatment responses of newly developed CAR-T cells in vitro and in vivo cells), with minimal detection on stem or progenitor cells. Thus, our
and minimal toxicities toward relevant healthy cells and tissue. candidates could bear the advantage of clinical application without
For primary target screening, we leveraged single-cell sequencing the risk for severe bone marrow toxicity, which is a current concern of
data from 15 primary AML specimens with differing cytogenetic proper- AML-targeted treatments10. It should be noted, however, that to date,
ties21. In addition, we validated the obtained results in an independent the clinical outcomes of off-tumor gene expression on HSPCs remains
cohort of five additional individuals with AML39. The top hits of the elusive. Along these lines, precise projection of off-tumor antigen
present study were reliably found overexpressed in large bulk sequenc- expression is one of the central objectives of our single-cell approach,
ing AML cohorts (n = 615). Given the highly complex molecular land- because unwanted toxicity may be inferred from high transcriptomic
scape of AML, rare AML subtypes might still not be fully represented off-target antigen expression20,63. Yet, as outlined above, the risk of
in our analyses. Despite this limitation, our study clearly demonstrates severe adverse effects caused by off-tumor activity of CAR-T cells is
the translational potential of unbiased, scRNA-seq-based screening not fully understood, and different outcomes have been reported64.
approaches and provides proof of principle of the whole spectrum of As such, the latest trials evaluating the safety of CD123 CAR-T cells
scRNA-seq-guided drug development spanning from computational did not show sustained cytopenia64. However, in most anti-CD123
target identification to preclinical investigation of newly developed CAR-T cell trials currently being conducted, participants eventually
CAR-T cells. received allo-HSCT, which presumably eradicated CAR-T cells. Of note,
CSF1R has been previously implicated as a target for small- the development of fatal cytokine release syndrome and capillary leak
molecule inhibition in AML46. However, its expression was thought syndrome following CD123 CAR-T cell infusion, potentially due to
to be restricted to a small subset of AML-supportive cells in certain off-target expression of CD123 on small vessels, has been reported7.
individuals, while the majority of human blasts are regarded as antigen Altogether, current clinical evidence does not support a clear defini-
negative51. Using various techniques, including transcriptomic analysis, tion of the critical cell types and expression thresholds that would
flow cytometry, immunohistochemistry and comprehensive functional preclude the development of CAR-T cells against a certain target to
investigation of CSF1R-directed CAR therapy, we were able to confirm avoid unmanageable toxicities. In any case, in the long run, detailed
high CSF1R expression on AML blasts. These reported ambiguities knowledge of off-tumor expression will allow vigilant monitoring of
of CSF1R expression on malignant AML blasts encourage the use of ‘high-risk off-tumor organs’ in clinical trials and might enable rapid side
unbiased, RNA-based screening algorithms for target identification effect-mitigating treatments. Similarly, clinical lessons from anti-CD19
and prioritization, as methodological or biological confounders can or anti-BCMA CAR-T cell therapy deem lineage-restricted expression
easily mask protein expression analysis. Nevertheless, it is crucial to patterns as highly desirable, providing further strong evidence for
bear in mind that scRNA-seq-centered strategies come with their own the use of single-cell technologies for de novo target identification, as
limitations (for example, the zero or dropout problem of singe-cell gene these technologies might be able to aid the search for unrecognized
expression52) and in any case require protein validation. target antigens with minimal off-tumor expression in healthy tissues.
CD86 is expressed on malignant AML blasts, and high receptor Many of the currently investigated CAR targets in AML failed
expression is associated with shortened overall survival of individuals the thresholds of overexpression on malignant HSPCs compared to
with AML53,54, but, to the best of our knowledge, CD86 has never been their healthy counterparts in our analyses. Herein, to a certain extent,
explored as a target for (immuno)therapy of cancer. The expression our data contradict data from publications of our colleagues13,65.
of CD86 is not limited to AML and has also been reported in numerous Sauer et al., for example, illustrated higher expression of CD70 in
B cell malignancies55. As such, the use of CD86 CART promises not only bone marrow biopsies of individuals with AML than in bone marrow
treatment options for AML but also applications for a variety of other samples of healthy donors by using immunohistochemistry13. This
hematological diseases, such as multiple myeloma56 and childhood discrepancy is most likely due to our restrictive analyses, in which we
B cell precursor acute lymphoblastic leukemia57. Nevertheless, CD86 have chosen rather high cutoff criteria to ensure maximal safety of
is also expressed on healthy macrophages and dendritic cells58–60 and identified target antigens. Dynamic adjustment of these thresholds
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1629
Article https://doi.org/10.1038/s41587-023-01684-0
might yield different results, and many of the previously identified tar- 10. Cummins, K. D. & Gill, S. Chimeric antigen receptor T-cell therapy
get antigens (for example, CD123, CD33, CD70, FLT3, C-type lectin-like for acute myeloid leukemia: how close to reality? Haematologica
molecule-1 and CD44v6) will most likely be of aid to improve clinical 104, 1302–1308 (2019).
care of individuals with refractory or relapsed AML. Nonetheless, our 11. MacKay, M. et al. The therapeutic landscape for cells
data clearly demonstrate the value of CSF1R and CD86 as targets for engineered with chimeric antigen receptors. Nat. Biotechnol. 38,
CAR-T cell therapy in AML, and, especially considering the complex 233–244 (2020).
molecular landscape of AML and its highly diverse subsets, these tar- 12. Tambaro, F. P. et al. Autologous CD33-CAR-T cells for treatment of
gets are expected to be valuable additions to the immunotherapeutic relapsed/refractory acute myelogenous leukemia. Leukemia 35,
repertoire in AML. 3282–3286 (2021).
Unsurprisingly, CSF1R was expressed on microglia, which share 13. Sauer, T. et al. CD70-specific CAR T-cells have potent activity
a common monocytic precursor, as also known for CD33 (ref. 66). against acute myeloid leukemia (AML) without HSC toxicity.
Clinical investigation of the so far only CSF1R-directed monoclonal Blood 138, 318–330 (2021).
antibody did not reveal neurotoxicity as a concern when depleting 14. Jetani, H. et al. Siglec-6 is a novel target for CAR T-cell therapy in
CSF1R+ cells from the periphery67. However, given the different mode acute myeloid leukemia (AML). Blood 138, 1830–1842 (2021).
of action of cellular- versus antibody-based therapies, these results 15. Myburgh, R. et al. Anti-human CD117 CAR T-cells efficiently
might not be directly transferable to anti-CSF1R CAR-T cell therapy. eliminate healthy and malignant CD117-expressing hematopoietic
In addition, CAR-T cells are known to be able to cross the blood–brain cells. Leukemia 34, 2688–2703 (2020).
barrier already at steady state68,69, and peak levels of proinflammatory 16. Tashiro, H. et al. Treatment of acute myeloid leukemia with
cytokines further increase permeability of this tightly regulated bar- T cells expressing chimeric antigen receptors directed to C-type
rier70,71. Because of these considerations, we rigorously tested the pos- lectin-like molecule 1. Mol. Ther. 25, 2202–2213 (2017).
sibility for neurotoxicity in numerous models. These models included 17. Casucci, M. et al. CD44v6-targeted T cells mediate potent
fully syngenic mouse models in which we implanted large quantities antitumor effects against acute myeloid leukemia and multiple
of CAR-T cells directly into mouse brains. Yet, we did not observe any myeloma. Blood 122, 3461–3472 (2013).
signs of neurotoxicity. Nevertheless, future clinical validations will 18. Perna, F. et al. Integrating proteomics and transcriptomics for
need to include well-designed protocols to vigilantly detect any signs systematic combinatorial chimeric antigen receptor therapy of
of neurotoxicity. AML. Cancer Cell 32, 506–519 (2017).
Our results highlight the potential of using unbiased, 19. Suva, M. L. & Tirosh, I. Single-cell RNA sequencing in cancer:
high-resolution, single-cell transcriptomic data for target selection lessons learned and emerging challenges. Mol. Cell 75, 7–12 (2019).
and drug development. Leveraging these data and the appropriate 20. Jing, Y. et al. Expression of chimeric antigen receptor therapy
high-dimensional analyses as standard operating procedures promises targets detected by single-cell sequencing of normal cells may
to improve safety and efficacy of newly engineered CAR-T cells and contribute to off-tumor toxicity. Cancer Cell 39, 1558–1559 (2021).
enables identification of new target structures for targeted immuno- 21. van Galen, P. et al. Single-cell RNA-seq reveals AML hierarchies
therapy in malignant disorders. relevant to disease progression and immunity. Cell 176,
1265–1281 (2019).
Online content 22. Turei, D. et al. Integrated intra- and intercellular signaling
Any methods, additional references, Nature Portfolio reporting sum- knowledge for multicellular omics analysis. Mol. Syst. Biol. 17,
maries, source data, extended data, supplementary information, e9923 (2021).
acknowledgements, peer review information; details of author contri- 23. Bausch-Fluck, D. et al. A mass spectrometric-derived cell surface
butions and competing interests; and statements of data and code avail- protein atlas. PLoS ONE 10, e0121314 (2015).
ability are available at https://doi.org/10.1038/s41587-023-01684-0. 24. Bausch-Fluck, D. et al. The in silico human surfaceome. Proc. Natl
Acad. Sci. USA 115, E10988–E10997 (2018).
References 25. Efremova, M., Vento-Tormo, M., Teichmann, S. A. & Vento-Tormo,
1. June, C. H. & Sadelain, M. Chimeric antigen receptor therapy. R. CellPhoneDB: inferring cell–cell communication from
N. Engl. J. Med. 379, 64–73 (2018). combined expression of multi-subunit ligand–receptor
2. Maude, S. L. et al. Tisagenlecleucel in children and young complexes. Nat. Protoc. 15, 1484–1506 (2020).
adults with B-cell lymphoblastic leukemia. N. Engl. J. Med. 378, 26. Thul, P. J. et al. A subcellular map of the human proteome.
439–448 (2018). Science 356, eaal3321 (2017).
3. Schuster, S. J. et al. Tisagenlecleucel in adult relapsed or 27. Habib, N. et al. Massively parallel single-nucleus RNA-seq with
refractory diffuse large B-cell lymphoma. N. Engl. J. Med. 380, DroNc-seq. Nat. Methods 14, 955–958 (2017).
45–56 (2019). 28. Kim, N. et al. Single-cell RNA sequencing demonstrates the
4. Raje, N. et al. Anti-BCMA CAR T-cell therapy bb2121 in molecular and cellular reprogramming of metastatic lung
relapsed or refractory multiple myeloma. N. Engl. J. Med. 380, adenocarcinoma. Nat. Commun. 11, 2285 (2020).
1726–1737 (2019). 29. Stewart, B. J. et al. Spatiotemporal immune zonation of the
5. Lesch, S. et al. Determinants of response and resistance to CAR human kidney. Science 365, 1461–1466 (2019).
T cell therapy. Semin. Cancer Biol. 65, 80–90 (2020). 30. Travaglini, K. J. et al. A molecular cell atlas of the human lung
6. Lamers, C. H. et al. Treatment of metastatic renal cell carcinoma from single-cell RNA sequencing. Nature 587, 619–625 (2020).
with CAIX CAR-engineered T cells: clinical evaluation and 31. Madissoon, E. et al. scRNA-seq assessment of the human lung,
management of on-target toxicity. Mol. Ther. 21, 904–912 (2013). spleen, and esophagus tissue stability after cold preservation.
7. Cummins, K. D. & Gill, S. Will CAR T cell therapy have a role in Genome Biol. 21, 1 (2019).
AML? Promises and pitfalls. Semin. Hematol. 56, 155–163 (2019). 32. Reyfman, P. A. et al. Single-cell transcriptomic analysis of human
8. Cancer Genome Atlas Research Network et al. Genomic and lung provides insights into the pathobiology of pulmonary
epigenomic landscapes of adult de novo acute myeloid leukemia. fibrosis. Am. J. Respir. Crit. Care Med. 199, 1517–1536 (2019).
N. Engl. J. Med. 368, 2059–2074 (2013). 33. MacParland, S. A. et al. Single cell RNA sequencing of human
9. Thol, F. & Ganser, A. Treatment of relapsed acute myeloid liver reveals distinct intrahepatic macrophage populations. Nat.
leukemia. Curr. Treat. Options Oncol. 21, 66 (2020). Commun. 9, 4383 (2018).
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1630
Article https://doi.org/10.1038/s41587-023-01684-0
34. Ramachandran, P. et al. Resolving the fibrotic niche of human 56. Gavile, C. M. et al. CD86 regulates myeloma cell survival. Blood
liver cirrhosis at single-cell level. Nature 575, 512–518 (2019). Adv. 1, 2307–2319 (2017).
35. Cheng, J. B. et al. Transcriptional programming of normal and 57. Sedek, L. et al. Differential expression of CD73, CD86 and
inflamed human epidermis at single-cell resolution. Cell Rep. 25, CD304 in normal vs. leukemic B-cell precursors and their utility
871–883 (2018). as stable minimal residual disease markers in childhood B-cell
36. James, K. R. et al. Distinct microbial and immune niches of the precursor acute lymphoblastic leukemia. J. Immunol. Methods
human colon. Nat. Immunol. 21, 343–353 (2020). 475, 112429 (2019).
37. Han, X. et al. Construction of a human cell landscape at 58. Guinan, E. C., Gribben, J. G., Boussiotis, V. A., Freeman, G.
single-cell level. Nature 581, 303–309 (2020). J. & Nadler, L. M. Pivotal role of the B7:CD28 pathway in
38. Wishart, D. S. et al. DrugBank 5.0: a major update to the DrugBank transplantation tolerance and tumor immunity. Blood 84,
database for 2018. Nucleic Acids Res. 46, D1074–D1082 (2018). 3261–3282 (1994).
39. Petti, A. A. et al. A general approach for detecting expressed 59. Zhou, L. J. & Tedder, T. F. CD14+ blood monocytes can differentiate
mutations in AML cells using single cell RNA-sequencing. into functionally mature CD83+ dendritic cells. Proc. Natl Acad.
Nat. Commun. 10, 3660 (2019). Sci. USA 93, 2588–2592 (1996).
40. Xu, C. et al. Probabilistic harmonization and annotation of 60. Smyth, C. et al. Identification of a dynamic intracellular
single-cell transcriptomics data with deep generative models. reservoir of CD86 protein in peripheral blood monocytes
Mol. Syst. Biol. 17, e9620 (2021). that is not associated with the Golgi complex. J. Immunol. 160,
41. Jurga, A. M., Paleczna, M. & Kuter, K. Z. Overview of general and 5390–5396 (1998).
discriminating markers of differential microglia phenotypes. 61. Blair, H. A. & Deeks, E. D. Abatacept: a review in rheumatoid
Front. Cell Neurosci. 14, 198 (2020). arthritis. Drugs 77, 1221–1233 (2017).
42. Erblich, B., Zhu, L., Etgen, A. M., Dobrenis, K. & Pollard, J. W. 62. Adusumilli, P. S. et al. A phase I trial of regional
Absence of colony stimulation factor-1 receptor results in loss of mesothelin-targeted CAR T-cell therapy in patients with
microglia, disrupted brain development and olfactory deficits. malignant pleural disease, in combination with the anti-PD-1
PLoS ONE 6, e26317 (2011). agent pembrolizumab. Cancer Discov. 11, 2748–2763 (2021).
43. Chihara, T. et al. IL-34 and M-CSF share the receptor FMS but are 63. Parker, K. R. et al. Single-cell analyses identify brain mural
not identical in biological activity and signal activation. Cell Death cells expressing CD19 as potential off-tumor targets for CAR-T
Differ. 17, 1917–1927 (2010). immunotherapies. Cell 183, 126–142 (2020).
44. Qin, D. et al. Potential lung attack and lethality generated by 64. Majzner, R. G. & Mackall, C. L. Clinical lessons learned from the
EpCAM-specific CAR-T cells in immunocompetent mouse first leg of the CAR T cell journey. Nat. Med. 25, 1341–1355 (2019).
models. Oncoimmunology 9, 1806009 (2020). 65. Jetani, H. et al. CAR T-cells targeting FLT3 have potent
45. Nayak, D., Roth, T. L. & McGavern, D. B. Microglia development activity against FLT3−ITD+ AML and act synergistically with the
and function. Annu. Rev. Immunol. 32, 367–402 (2014). FLT3-inhibitor crenolanib. Leukemia 32, 1168–1179 (2018).
46. Edwards, D. K. T. et al. CSF1R inhibitors exhibit antitumor activity 66. Griciuc, A. et al. TREM2 acts downstream of CD33 in modulating
in acute myeloid leukemia by blocking paracrine signals from microglial pathology in Alzheimer’s disease. Neuron 103,
support cells. Blood 133, 588–599 (2019). 820–835 (2019).
47. Pabst, C. et al. Identification of small molecules that support 67. Cassier, P. A. et al. CSF1R inhibition with emactuzumab in locally
human leukemia stem cell activity ex vivo. Nat. Methods 11, advanced diffuse-type tenosynovial giant cell tumours of the
436–442 (2014). soft tissue: a dose-escalation and dose-expansion phase 1 study.
48. Vick, B. et al. An advanced preclinical mouse model for acute Lancet Oncol. 16, 949–956 (2015).
myeloid leukemia using patients’ cells of various genetic 68. O’Rourke, D. M. et al. A single dose of peripherally infused
subgroups and in vivo bioluminescence imaging. PLoS ONE 10, EGFRvIII-directed CAR T cells mediates antigen loss and induces
e0120925 (2015). adaptive resistance in patients with recurrent glioblastoma.
49. McQuade, A. et al. Development and validation of a simplified Sci. Transl. Med. 9, eaaa0984 (2017).
method to generate human microglia from pluripotent stem cells. 69. Gust, J. et al. Endothelial activation and blood–brain barrier
Mol. Neurodegener. 13, 67 (2018). disruption in neurotoxicity after adoptive immunotherapy with
50. Reifschneider, A. et al. Loss of TREM2 rescues hyperactivation of CD19 CAR-T cells. Cancer Discov. 7, 1404–1419 (2017).
microglia, but not lysosomal deficits and neurotoxicity in models 70. Sterner, R. M. et al. GM-CSF inhibition reduces cytokine release
of progranulin deficiency. EMBO J. 41, e109108 (2022). syndrome and neuroinflammation but enhances CAR-T cell
51. Sletta, K. Y., Castells, O. & Gjertsen, B. T. Colony stimulating function in xenografts. Blood 133, 697–709 (2019).
factor 1 receptor in acute myeloid leukemia. Front. Oncol. 11, 71. Tan, A. H. J., Vinanica, N. & Campana, D. Chimeric antigen
654817 (2021). receptor-T cells with cytokine neutralizing capacity. Blood Adv. 4,
52. Haque, A., Engel, J., Teichmann, S. A. & Lonnberg, T. A practical 1419–1431 (2020).
guide to single-cell RNA-sequencing for biomedical research and
clinical applications. Genome Med. 9, 75 (2017). Publisher’s note Springer Nature remains neutral with regard to
53. Tamura, H. et al. Expression of functional B7-H2 and B7.2 jurisdictional claims in published maps and institutional affiliations.
costimulatory molecules and their prognostic implications
in de novo acute myeloid leukemia. Clin. Cancer Res. 11, Springer Nature or its licensor (e.g. a society or other partner) holds
5708–5717 (2005). exclusive rights to this article under a publishing agreement with
54. Re, F. et al. Expression of CD86 in acute myelogenous leukemia the author(s) or other rightsholder(s); author self-archiving of the
is a marker of dendritic/monocytic lineage. Exp. Hematol. 30, accepted manuscript version of this article is solely governed by the
126–134 (2002). terms of such publishing agreement and applicable law.
55. Zheng, Z. et al. Expression patterns of costimulatory molecules
on cells derived from human hematological malignancies. © The Author(s), under exclusive licence to Springer Nature America,
J. Exp. Clin. Cancer Res. 17, 251–258 (1998). Inc. 2023
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1631
Article https://doi.org/10.1038/s41587-023-01684-0
1Division of Clinical Pharmacology, University Hospital, LMU Munich, Member of the German Center for Lung Research (DZL), Munich, Germany. 2Bavarian
Cancer Research Center (BZKF), Munich, Germany. 3Department of Medicine III, University Hospital, LMU Munich, Munich, Germany. 4Institute of AI for
Health, Helmholtz Munich, Neuherberg, Germany. 5School of Life Sciences Weihenstephan, Technical University of Munich, Freising, Germany. 6Laboratory
for Translational Cancer Immunology, Gene Center, LMU Munich, Munich, Germany. 7Research Unit Apoptosis in Hematopoietic Stem Cells, Helmholtz
Munich, German Research Center for Environmental Health (HMGU), Munich, Germany. 8Department of Pediatrics, University Hospital, LMU Munich,
Munich, Germany. 9Department of Neurology, University Hospital, LMU Munich, Munich, Germany. 10Institute for Stroke and Dementia Research (ISD),
University Hospital, LMU Munich, Munich, Germany. 11Munich Cluster for Systems Neurology (SyNergy), Munich, Germany. 12Institute of Pathology, LMU
Munich, Munich, Germany. 13Institute of Clinical Neuroimmunology, University Hospital, LMU Munich, Munich, Germany. 14Biomedical Center (BMC),
Faculty of Medicine, LMU Munich, Martinsried, Germany. 15German Cancer Consortium (DKTK), Partner Site Munich, Munich, Germany. 16Department
of Oncology, Hematology and Bone Marrow Transplantation with Section Pneumology, Hubertus Wald University Cancer Center, University Medical
Center Hamburg-Eppendorf, Hamburg, Germany. 17Mildred Scheel Cancer Career Center, University Cancer Center Hamburg, University Medical Center
Hamburg-Eppendorf Hamburg, Hamburg, Germany. 18Division of Transfusion Medicine, Cell Therapeutics and Haemostaseology, University Hospital, LMU
Munich, Munich, Germany. 19Department of Neurosurgery, LMU Munich, Munich, Germany. 20Einheit für Klinische Pharmakologie (EKLiP), Helmholtz Munich,
Research Center for Environmental Health (HMGU), Neuherberg, Germany. 21These authors contributed equally: Adrian Gottschlich, Moritz Thomas, Ruth
Grünmeier. 22These authors jointly supervised this work: Carsten Marr, Sebastian Kobold. e-mail: sebastian.kobold@med.uni-muenchen.de
Nature Biotechnology | Volume 41 | November 2023 | 1618–1632 1632
