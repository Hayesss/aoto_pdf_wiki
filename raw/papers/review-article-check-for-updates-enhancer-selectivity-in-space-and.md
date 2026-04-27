---
source_path: /mnt/c/Users/Administrator/Zotero/storage/8DN9XW3N/Yang和Hansen - 2024 - Enhancer selectivity in space and time from enhancer–promoter interactions to promoter activation.pdf
ingested: 2026-04-23
sha256: 1f54ba2d11c6dc98
---

nature reviews molecular cell biology https://doi.org/10.1038/s41580-024-00710-6
Review article Check for updates
Enhancer selectivity in space and
time: from enhancer–promoter
interactions to promoter activation
Jin H. Yang 1,2,3 & Anders S. Hansen 1,2,3
Abstract Sections
The primary regulators of metazoan gene expression are enhancers, Introduction
originally functionally defined as DNA sequences that can activate
Models of E–P interactions
transcription at promoters in an orientation-independent and
Models of transcription
distance-independent manner. Despite being crucial for gene activation by enhancers
regulation in animals, what mechanisms underlie enhancer selectivity
Models of enhancer selectivity
for promoters, and more fundamentally, how enhancers interact with
From simulated E–P pairs
promoters and activate transcription, remain poorly understood. to biological E–P pairs
In this Review, we first discuss current models of enhancer–promoter
Imaging 3D E–P interactions
interactions in space and time and how enhancers affect transcription
Conclusions and future
activation. Next, we discuss different mechanisms that mediate
outlook
enhancer selectivity, including repression, biochemical compatibility
and regulation of 3D genome structure. Through 3D polymer
simulations, we illustrate how the ability of 3D genome folding
mechanisms to mediate enhancer selectivity strongly varies for different
enhancer–promoter interaction mechanisms. Finally, we discuss how
recent technical advances may provide new insights into mechanisms of
enhancer–promoter interactions and how technical biases in methods
such as Hi-C and Micro-C and imaging techniques may affect their
interpretation.
1Department of Biological Engineering, Massachusetts Institute of Technology, Cambridge, MA, USA.
2Gene Regulation Observatory, Broad Institute of MIT and Harvard, Cambridge, MA, USA. 3Koch Institute for
Integrative Cancer Research, Cambridge, MA, USA. e-mail: ashansen@mit.edu
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 574
Review article
Introduction also known as the sliding or scanning model, posits that the transcrip-
Precise regulation of gene expression in space and time is crucial for the tion machinery, including RNA polymerase II (Pol II), loaded at the
development of a single-cell embryo into a complex organism1. Hun- enhancer tracks along the DNA and eventually reaches the cognate
dreds of functionally distinct cell types arise during development, yet promoter15 (Fig. 1a). A variant of this model proposes that chromatin
they share the same genome, suggesting that different genes undergo remodellers track along the DNA to spread histone PTMs towards the
cell-type-specific activation2. Enhancers are the primary component promoter16,17. Aside from 1D tracking mechanisms, another type of 1D
of metazoan gene regulation, thereby controlling spatiotemporal model postulates that protein scaffolds form a 1D molecular bridge
patterns of transcriptional gene activation3–6. Originally identified along the DNA, thereby connecting an E–P pair18 (Fig. 1a). It should be
in 1981, enhancers were functionally defined as having the capacity noted that these 1D models were proposed for E–P pairs whose dis-
to activate promoters regardless of their orientation and genomic tances range from several kilobases to tens of kilobases. Notably, the
distance from the transcription start site7–10. Despite recent efforts observation that enhancers often skip nearby promoters19–22 to activate
to define enhancers by their physical properties, such as occupancy more distal promoters is difficult to explain with 1D models. This obser-
of transcription factors or co-activators, presence of certain histone vation together with recent studies that strongly suggest enriched 3D
post-translational modifications (PTMs), depletion of nucleosomes proximity between cognate E–P pairs23–32 have substantiated 3D models
or transcription of enhancer RNAs11, unambiguous criteria are yet to of E–P interactions (Fig. 1b).
be established.
Part of the challenge in defining enhancers is our lack of mechanistic Three-dimensional models
understanding of how they interact with and activate promoters. Even In contrast to 1D models, 3D E–P interaction models may explain the
though enhancers are capable of activating different promoters, tran- promoter skipping phenomenon: an enhancer could be in 3D spatial
scription activation by enhancers is often restricted to a selected one or proximity for a longer duration and/or more frequently with one pro-
few promoters12,13, often referred to as their cognate promoters. How do moter than another, despite being further apart on the linear genome
enhancers select cognate promoters over non-cognate ones? Here, we (Fig. 1b). In 3D models of E–P interactions, the 3D distance between
define enhancer selectivity as the fold increase in transcriptional output cognate E–P pairs must be below a distance threshold28,29,33, referred
at cognate promoters over non-cognate promoters owing to the impact to as the interaction radius in this Review, for them to functionally
of a given enhancer. Given that enhancer–promoter (E–P) interaction and interact. We can classify 3D models based on space and time into four
transcription activation are sequential processes, intuitively enhancer categories (Fig. 1c): along the space axis, E–P interactions in 3D can be
selectivity could be achieved by selective interactions of enhancers achieved either through direct contact or through action at a distance;
with their cognate promoters and/or by regulating the ability of specific along the time axis, E–P interactions in 3D can be either dynamic or
classes of enhancers to activate specific classes of promoters. stable based on interaction duration. Action-at-a-distance E–P models
To mechanistically understand how enhancer selectivity is estab- are partly motivated by measured E–P 3D distances of ~200 nm dur-
lished at the E–P interaction level and/or the transcription activation ing transcription activation27,34–38, which vastly exceed the expected
level, we begin this Review by discussing current mechanistic models ~10–20 nm size of transcriptional protein complexes that are presum-
for how these two processes work. We discuss the molecular mecha- ably involved in E–P contact39–47. However, we will discuss how due to
nisms of how an enhancer interacts with and activates its cognate pro- localization noise, measured E–P distances of hundreds of nanometres
moter and how selectivity could be encoded in each of these two steps. may not be incompatible with contact models48.
At the interaction level, we discuss plausible selectivity mechanisms
including CTCF–cohesin-mediated insulation and facilitation. We also Contact models. The textbook E–P interaction model is the stable
discuss plausible selectivity mechanisms at the activation level, includ- contact model, in which an E–P loop forms to mediate stable and
ing repression and biochemical compatibility mechanisms. Finally, we direct contact (Fig. 1c). The notion of stable E–P contact traces back
discuss technical limitations and subtleties inherent to chromosome to studies in prokaryotes49,50. Stable E–P chromatin looping mediated
conformation capture (3C) and imaging-based methods often used to by the bovine papillomavirus E2 protein was also visualized by electron
study E–P interactions. microscopy51. Contact is consistent with the classical notion of tran-
scription activation by recruitment52. More recently in Drosophila mela-
Models of E–P interactions nogaster, interactions between architectural proteins such as CTCF and
Before an enhancer can activate transcription at its cognate promoter, LDB1 were hypothesized to facilitate stable E–P interactions53, and Mcp
a connection must be established between the pair, providing a means elements were shown to mediate stable chromosome–chromosome
for information and/or material transfer between them. In this Review, interactions54. In mammals, forced chromatin looping that brings
we refer to this process as E–P interactions. Although this process is often an E–P pair into contact using artificial zinc-fingers was shown to be
discussed in conjunction with transcription activation, we note that sufficient for transcription activation28,29.
they are two distinct and sequential processes in which interactions Although the precise nature of the DNA–protein complexes bridg-
presumably precede transcription activation. It is also important to ing E–P contacts remains poorly understood, insights were provided by
consider that not all E–P interactions necessarily lead to transcription structural studies of the enhanceosome assembled at the interferon-β
activation. We begin by reviewing classical and current models of E–P enhancer47,55. More recently, the Mediator–Pol II preinitiation complex
interactions. (PIC), which may form the interface of direct E–P contact39–42, has been
captured through cryo-electron microscopy43–45 .The structure showed
One-dimensional models that the Mediator tail module associates with enhancers56 to facilitate
In the framework of a linear, 1D genome, classical models propose PIC assembly at promoters46. However, acute depletion of Mediator
that E–P interactions can be established along the chromatin, without and Pol II had little effect on the E–P ‘contact probability’ measured by
requiring spatial proximity of the E–P pair in 3D14. The tracking model, Hi-C57, although subsequently we discuss some technical limitations
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 575
Review article
a 1D E–P interaction models b 3D models are required to explain promoter skipping
Tracking/sliding/scanning model
Chromatin
Promoter linearly
Pol II remodeller closer in the genome
DNA
Enhancer Promoter
Linking model Promoter linearly
farther in the genome
Transcription Co-activator
factor
c 3D E–P interaction models
Dynamic action-at-a-distance model
Dynamic hit-and-run contact model
and subtleties inherent to 3C assays. Nonetheless, E–P contact models source of a concentration gradient of acetylated transcription factors,
are intuitive and consistent with gene activation models in organisms such that nearby promoters are more likely to encounter acetylated
that lack distal enhancers52. However, recent observations, which we transcription factors that diffuse away from the enhancer34. The weak
discuss next, have called contact models into question. correlation between E–P 3D distance and transcription25–27,35,36,38 seem-
ingly supports action-at-a-distance models as both condensates71
Action-at-a-distance models. The classical view of E–P interactions and TAG34 would alleviate the requirement for direct E–P contact
through protein-mediated direct contact has recently been called (alternative explanations for this weak correlation are discussed
into question by action-at-a-distance models, wherein E–P pairs subsequently48).
functionally interact without forming contact (Fig. 1c). Such interac-
tions at a distance could be mediated by condensates comprising The time dimension: are E–P interactions dynamic or stable? Along
liquid–liquid phase separated assemblies of transcription factors, the time axis, E–P interactions could be dynamic and short-lived or
co-activators and Pol II58–66, whose radius is on the order of hundreds stable. Although these terms are inherently subjective and vague,
of nanometres36,37,58,62,65,67. Evidence supporting condensate-mediated generally speaking a stable E–P chromatin loop or interaction would
E–P interactions comes from the observation of condensate formation be expected to last hours, whereas a dynamic interaction would be on
around super-enhancers58,64,65,68,69. However, it is unclear whether E–P the order of minutes, seconds or less. The stable interaction models
interactions are a product of condensate formation or the other way mainly find support from the stable E–P loops characterized in early
around70. Another action-at-a-distance model is the transcription fac- studies of prokaryotes49–51. By contrast, live-cell imaging studies in
tor activity gradient (TAG) model34. In the TAG model, enhancer-bound animals have generally found chromatin interactions to be relatively
co-activators such as CBP or histone acetyltransferase p300 act as a dynamic25,27,35,72,73. Specifically, because CTCF–cohesin loop lifetimes
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 576
suidar
noitcaretnI
Stable action-at-a-distance model
Condensate
Stable contact model
Interaction duration
Fig. 1 | Models of enhancer–promoter interactions. a, One-dimensional models the enhancer to a higher extent and/or more frequently than a promoter closer
of enhancer–promoter (E–P) interactions. RNA polymerase II (Pol II) or chromatin to the enhancer on the linear genome. c, Three-dimensional models of E–P
remodellers loaded at the enhancer can track along the chromatin to reach the interactions. Along the interaction radius axis, 3D E–P interaction models can
cognate promoter (top); alternatively, protein scaffolds can connect cognate E–P be divided into contact type and action-at-a-distance type; along the interaction
pair as a molecular bridge (bottom). b, Promoter skipping. A promoter further duration axis, 3D E–P interaction models are classified into dynamic and stable
away from an enhancer along the linear genome can be in spatial proximity with categories.
Review article
have been estimated to be on the order of approximately 10–30 min72,73 enhancer-recruited proteins to promoters, enhancer-mediated recruit-
and because E–P interactions appear much weaker than CTCF–cohesin ment of proteins to promoters, enhancer-mediated establishment of
loops in contact maps, even shorter-lived E–P interactions can be high local protein concentrations at promoters and enhancer-mediated
envisaged, with lifetimes of seconds to minutes, in support of dynamic PTMs at promoters. It is important to note that these four categories
E–P interaction models. One such dynamic model is the ‘hit-and-run’ are not mutually exclusive and can function simultaneously, and that
contact model, in which an E–P pair is transiently in contact, and then they are compatible with all four E–P interaction models discussed
diffuses away from each other74,75 (Fig. 1c). Notably, hit-and-run-type earlier (Fig. 1c).
models that include a delay between contact and transcription ini-
tiation may explain how E–P contact and nascent transcription can Direct transfer of enhancer-recruited proteins to the
be causally related, yet exhibit low correlation in static snapshot promoter
studies26,36,38. A variation of the hit-and-run model is the ‘kiss-and-kick’ The first category of models of transcription activation suggests a direct
model, in which the E–P pair is kicked apart by transcription elonga- transfer of enhancer-recruited protein complexes from the enhancer
tion after being in contact76. Consistent with these short-lived E–P to the promoter (Fig. 2a). This category of transcription activation
interaction models, the residence time of most transcription factors models is supported by studies showing that enhancers could function
in mammals is typically on the order of seconds to tens of seconds, as a reservoir of Pol II, transcription factors, chromatin remodellers
which is much shorter than the duration of a typical transcription and co-activators for their cognate promoters61,88,89. Supporting the
burst of minutes to tens of minutes77–86. This timescale difference model of Pol II transfer from an enhancer to its cognate promoter,
suggests that the transcription factors that may facilitate E–P contact insertion of a CTCF-dependent insulator between enhancers and pro-
would have dissociated long before a transcription burst is complete. moters in a transgenic human β-globin locus led to reduced Pol II levels
Similarly, action-at-a-distance models may be either dynamic or stable, at the δ-globin and β-globin promoters, whereas the Pol II level at the
presumably depending on the lifetime of the condensate or TAG and on enhancers was unaffected90. Consistently, promoters can also function
the dynamics of E–P interactions within a condensate34,58,64,87 (Fig. 1c). as enhancers91, potentially by facilitating more efficient recycling of
Despite progress, the functionally relevant E–P interaction duration transcription machinery components such as Pol II (ref. 92) through
remains very poorly understood. extensive promoter–promoter interactions23,93. Aside from the trans-
Regardless of the E–P interaction mechanisms, once an enhancer fer of Pol II, transcription factors IIF and IIE may also pre-assemble
interacts with its cognate promoter, information needs to be trans- on enhancers before being transferred into the PIC at promoters88,94.
ferred from the enhancer to the promoter to activate transcription,
which we discuss next. Enhancer-mediated recruitment of proteins to the promoter
Instead of direct transfer, a second category of models posits that tran-
Models of transcription activation by enhancers scription factors bound at the enhancer help recruit co-activators for
The mechanistic models of transcription activation by enhanc- transcription activation at promoters4,6,95,96 (Fig. 2b). In support of this
ers can be broadly classified into four categories: direct transfer of model, the enhancer-associated co-activators CBP or p300 can help
a Direct transfer of enhancer-recruited proteins to the promoter b Enhancer-mediated recruitment of proteins to the promoter
Co-activator Pol II Transcription
Enhancer factor
DNA
Mediator
complex
GTFs
Promoter
PIC
c Enhancer-mediated enrichment of proteins around the promoter d Enhancer-mediated PTMs at promoters
P
Fig. 2 | Models of transcription activation by enhancers. a, Transcription d, Transcription activation by enhancer-mediated protein post-translational
activation through direct transfer of enhancer-recruited proteins to the promoter. modifications (PTMs) at promoters. The example illustrated here shows the
GTFs, general trascription factors. b, Transcription activation by enhancer- phosphorylation (P) of Pol II by Mediator. For brevity and clarity, the figure
mediated recruitment of proteins to the promoter. c, Transcription activation only illustrates Pol II-mediated transcription activation dial; examples of other
by enhancer-mediated enrichment of proteins around the promoter leading proteins are discussed in the main text.
to the formation of the RNA polymerase II (Pol II) preinitiation complex (PIC).
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 577
Review article
recruit BRD4 and Pol II to the promoter, and in turn BRD4 can facilitate Models of enhancer selectivity
the recruitment of positive transcription elongation factor b and the It is important for enhancers to activate the right genes. Aberrant gene
release of promoter-proximal paused Pol II, leading to productive tran- activation through enhancer mistargeting — also termed enhancer
scription elongation97–100. Furthermore, clusters of Pol II at promoters hijacking — can cause disease, for example, through oncogene overex-
and clusters of transcription factors and co-activators at enhancers pression in cancer116–122. Notably, around 40–50% of enhancers skip the
were found to be spatially separated61, which is also consistent with closest genes to selectively activate genes further away19,21,22, raising
a model in which the enhancer contributes to Pol II recruitment to the question of how enhancers skip genes to activate more distal ones?
the promoter. Considering the two distinct steps of enhancer actions discussed
earlier, enhancer selectivity can be achieved at the E–P interactions
Enhancer-mediated high protein concentrations at promoters level (Fig. 1), the transcription activation level (Fig. 2) or both. In this
In addition to direct transfer and targeted recruitment, enhancers section, we begin with the latter and note that even though E–P inter-
may also establish high local concentrations of transcription factors, actions provide a ‘channel’ for information transfer to permit tran-
co-activators, chromatin remodellers and Pol II near the promoter. scription activation, not all E–P interactions result in transcription
This process may be mediated through clustering61, hub formation101 activation. Indeed, although the probability of E–P interactions cor-
or through liquid–liquid phase separation leading to condensate relates with transcription activation33, ultra-deep 3D genome mapping
formation14,62,64,65,67,69 (Fig. 2c). Clusters can increase the rate of protein revealed the existence of relatively promiscuous E–P interactions in
recruitment102. Analogously, within condensates, enriched proteins some gene-rich regions, suggesting that enhancer selectivity is not
with high local concentration can transiently associate, dissociate exclusively regulated at the E–P interaction level23. Aside from the
and relocate between the interacting E–P pairs, thereby increasing possibility that the strength of the enhancer or the interactions are not
the probability of transcription activation at the promoter91. In sup- sufficient to activate transcription, these findings also point to a poten-
port of this model, when residues important for phase separation tial layer of enhancer selectivity that is regulated at the transcription
were mutated in the transcription factor OCT4, the impaired capac- activation level, which we discuss next.
ity for phase separation observed in vitro correlated with significantly
lower transcription activation in vivo62, although some studies have Repression-mediated enhancer selectivity
suggested that full-scale liquid–liquid phase separation may in fact One type of enhancer selectivity control at the transcription activation
inhibit transcription103,104. Although increasing evidence supports level is promoter repression (Fig. 3a). Any two elements on the same
the establishment of high local concentrations14,61,62,64,65,67,69,101,103,104, chromosome will interact with some probability, but if a promoter is
one potential weakness of condensate models and more generally of sufficiently strongly repressed, interactions with an enhancer may
action-at-a-distance models is selectivity: a typical human cell nucleus not functionally matter. Promoter repression may be regulated by
contains on average 300–400 genes per μm3 or around 40 genes per histone variants and PTMs that can reduce chromatin accessibility
300-nm radius spherical condensate36,37,58,62,65,67 (see part 8 of Supple- at promoters and conceal transcription factor-binding sites within
mentary Box 1), raising the question of how aberrant gene activation nucleosomes to prevent transcription activation123,124 (Fig. 3a). This
is avoided? model is supported by the strong correlation between promoter acces-
sibility and gene expression, as well as the low accessibility and expres-
Enhancer-mediated post-translational modifications at sion of tissue-specific promoters in tissues where these promoters
promoters are inactive125.
Another category of models proposes that enhancers could mediate DNA methylation can also silence promoters through direct
transcription activation through enzymatic modifications, primar- interference with transcription-factor binding and by recruitment of
ily PTMs of promoter-bound transcription machinery and histones. silencing complexes126–129. Consistently, DNA methylation is also highly
Evidence supporting these models includes phosphorylation of correlated with tissue-specific gene expression130,131. Histone PTMs and
promoter-bound Pol II C-terminal domain stimulated by the Media- DNA methylation could be facilitated by binding of co-repressors132,133
tor complex recruited by the enhancer41,105–107 and/or by enhancer such as Polycomb repressive complexes134 (Fig. 3a). Other studies
RNAs108,109, enabling productive transcription elongation (Fig. 2d). also identified long-range repression mediated by the formation of
In addition, histone PTMs and chromatin remodelling at promoters Polycomb-dependent chromatin loops135 and by distal silencers136–138.
mediated by enhancers are strongly correlated with transcription acti- Disrupted co-repressor functions have been associated with aber-
vation and could also contribute to the establishment of ‘transcription rant gene activation, leading to diseases such as Rett syndrome and
memory’24,110,111. adrenal hypoplasia139–142. It should be noted that the aforementioned
Importantly, all four categories of models allow some degree of repression mechanisms also apply to enhancers143,144. Thus, one way
‘memory’ of transcription activation that persists beyond the initial to encode enhancer specificity at the transcription activation level is to
activation24,34,92,110–113. Given the short residence times of most tran- repress non-cognate promoters, thereby rendering them insensitive
scription factors and co-activators — seconds to minutes77,82,84,86 — to enhancer interactions.
chromatin remodelling and histone PTMs, which are thought to last
tens of minutes to hours114,115, may provide longer-term memory. Enhancer selectivity through biochemical compatibility
Thus far we have discussed how one enhancer may interact with Aside from repression, biochemical compatibility could also mediate
and activate one promoter. However, the nucleus is crowded, and the enhancer selectivity at the transcription activation level13 (Fig. 3b). One
genome contains many gene-dense regions, yet many enhancers skip of the early demonstrations of this concept was the little-to-no tran-
their closest promoter to activate more distal promoters19,21,22. Thus, we scription activation when swapping enhancers or promoters between
next discuss enhancer selectivity — how does an enhancer selectively the gsbE–gsb E–P pair and the gsbnE–gsbn E–P pair in D. melanogaster
activate one promoter over another? embryos145. Later efforts discovered that some enhancers prefer
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 578
Review article
a Repression-mediated enhancer selectivity
Promoter Histone
variant Histone
H2A.Z octamer
Enhancer
PRC
Me
b Biochemical-compatibility-mediated enhancer selectivity c Domain model: enhancers only activate promoters within the same TAD
Compatible
core promoter motif
TAD
Incompatible CTCF
core promoter motif
CTCF Cohesin
binding site
d Individual insulator model: CTCF insulates individually without the need for domain formation e Facilitator model: CTCF promotes 3D
proximity of an E–P pair
With an insulating CTCF binding site
Cohesin loads Cohesin extrudes CTCF stalls one motor Cohesin offloads
onto chromatin bidirectionally and insulates enhancer and loop dissolves
from promoter
Without an insulating CTCF binding site
Cohesin loads Cohesin extrudes Cohesin brings E–P Cohesin offloads
onto chromatin bidirectionally pair into proximity and loop dissolves
Cohesin stalled on one side brings
E–P pair into proximity in 3D
Fig. 3 | Models of enhancer selectivity. a, Enhancer selectivity mediated by across topologically associating domain (TAD) boundaries. The fully looped
promoter repression. If a promoter is sufficiently strongly repressed, it may be state is achieved when one or more cohesins bridge together the CTCF loop
insensitive to enhancer–promoter (E–P) interactions. Epigenetic modifications anchors, thereby forming a loop domain that is often assumed to be very stable.
such as histone H3 Lys9 trimethylation (H3K9me3) are associated with loss of d, According to the individual insulator model, it is the ability of a CTCF insulator
chromatin accessibility. By contrast, incorporation of the histone variant H2A.Z to block loop extrusion that reduces E–P interactions across the CTCF boundary
leads to gain of chromatin accessibility (left). Promoters can be repressed also independently of domain formation. In a hypothetical genome with a single CTCF
by binding of co-repressors complexes, such as Polycomb repressive complexes site placed between an E–P pair, no domain could be formed but insulation can
(PRC) (right). b, Enhancer selectivity mediated by biochemical compatibility. still be explained. e, The facilitator role of CTCF promotes 3D E–P proximity and
If distinct classes of enhancers and promoters exist such that enhancers can only thus enhancer selectivity. The models presented in parts a and b function at the
activate promoters of the same class, this could also explain enhancer selectivity. transcription activation level, whereas those presented in parts c–e function at
c, According to the domain model, E–P interactions take place within, but not the E–P interaction level.
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 579
Review article
promoters containing downstream promoter elements (DPEs), whereas E–P interactions and delineate gene-regulatory domains179. These
other enhancers prefer promoters containing TATA box motifs146–148, findings were consistent with a domain model, wherein stable loop
and experiments placing these different E–P pairs at the same genomic domains165,180–182 formed by CTCF and cohesin control enhancer
locations suggest that such preference is likely regulated at the tran- selectivity and gene expression.
scription activation level instead of at the E–P interaction level147. Calling into question the domain model, recent work using
Biochemical compatibility has also been demonstrated for other pro- super-resolution live-cell imaging of two CTCF sites forming a TAD has
moters without any DPE or TATA box motif149,150. Such compatibility is instead suggested that CTCF loops are dynamic, short-lived and rarely
proposed to be determined by the transcription factor and co-activator in the fully CTCF–CTCF looped state72,73. Specifically, in mouse ES cells,
binding profile at the E–P pairs12,146,151,152. Consistently, DPE-containing the CTCF–CTCF loop demarcating the TAD around the Fbn2 gene was
promoters have a higher frequency of H3K27me3 than DPE-less promot- found to be both rare (3–6.5% of the time) and short-lived (median
ers, whereas the transcription activity of TATA-containing promoters lifetime of 10–30 min)72, which seems inconsistent with models of
is less dependent on histone PTM status than TATA-less promoters153. TADs as stable loops165,180–182. Instead of being dominated by the fully
Further supporting the biochemical compatibility model, intrinsically CTCF–CTCF looped state, the Fbn2 TAD was found to overwhelm-
disordered regions (IDRs) in transcription factors and co-activators ingly exist (92% of the time) in a partially extruded state72. Thus, the
interact selectively with their binding partners67,154,155. For example, main functional state of TADs is likely not the fully CTCF–CTCF looped
in budding yeast, the binding specificity of Msn2 and Yap1 to their structure. Instead, in accordance with the classical view that insulators
target promoters is largely explained by their intrinsically disordered insulate individually178, it is the ability of a CTCF-bound insulator to
regions156. Notably, most of these studies demonstrate a quantitative block loop extrusion that reduces interactions between an enhancer
preference instead of all-or-none compatibility146,148–150. and promoter on opposite sides of the CTCF site, thereby mediating
More recently, two studies using massively parallel reporter assays transcription insulation72 (Fig. 3d).
came to opposite conclusions regarding biochemical compatibility. More generally, by being able to block cohesin-mediated loop
One study observed broad compatibility and very little selectivity extrusion, CTCF can function as an E–P insulator (Fig. 3d) and/or
between 1,000 enhancers and 1,000 promoters in human erythroleu- E–P facilitator, depending on the context183,184 (Fig. 3e). Addition-
kaemia cells157. By contrast, the other study found more than half of the ally, promoters can also serve as ‘effective insulators’ through pro-
556 cis-regulatory elements (including enhancers and silencers) tested moter competition, in which two or more promoters compete for the
in mouse embryonic stem (ES) cells to have limited compatibility and same enhancer and therefore loss of one promoter may now allow
strong selectivity158. The contradictory conclusions of these two studies an enhancer to activate another promoter185,186. Supporting the insula-
may be attributed to differences in data analysis, as both papers found tor role of CTCF, loss of CTCF insulation function can result in aberrant
that data of each other supported their own conclusion when analysed E–P interactions causing oncogene activation and overexpression in
with their own computational pipeline159. Nonetheless, both papers cancer121,122. Furthermore, rewiring of E–P interactions at the Wnt6-
support quantitative preference overall-or-none compatibility for Ihh-Epha4-Pax3 locus leads to aberrant limb development in mouse
most enhancer–promoter pairs157,158. Concordantly, transcription factor embryos187. By contrast, if CTCF sites are located near the enhancer
motifs in enhancers and promoters act in a largely additive manner in and/or promoter, CTCF can serve as a facilitator of E–P interactions.
binary STARR-seq (self-transcribing active regulatory region sequenc- The Sonic hedgehog (Shh) locus is a classic example of CTCF acting as
ing) experiments160. Aside from selectivity encoded at the transcription a facilitator of E–P interactions188, as is MYC189. It has been estimated
activation level, enhancer selectivity could be also achieved at the E–P that around 65% of promoters in mouse ES cells and 50% of promot-
interaction level, which we discuss next. ers in mouse neural progenitor cells (NPCs) have at least one CTCF
ChIP–seq (chromatin immunoprecipitation followed by sequencing)
Enhancer selectivity through loop extrusion peak within 10 kb of the transcription start site93, consistent with CTCF
By regulating E–P interactions, 3D genome structure has emerged serving as an E–P facilitator (Fig. 3e). Notably, despite more than 2,300
as an additional mechanism of enhancer selectivity. The genome is genes showing a strong correlation between promoter–proximal CTCF
folded into topologically associating domains (TADs)161–164, which are binding and tissue-specific gene expression, only a small fraction of
also known as loop domains165. TADs increase interactions between loci the studied promoters were downregulated upon acute depletion
within the same TAD and reduce interactions across TAD boundaries. of CTCF in mouse ES cells and NPCs93. One possibility reconciling these
Thus, TADs can mediate enhancer selectivity by promoting E–P interac- observations is that the facilitator role of CTCF might be generally more
tions within the same TAD and by preventing E–P interactions between required for the establishment than for the maintenance of gene expres-
different TADs (Fig. 3c). Mechanistically, TADs are thought to form sion, at least at short timescales23,31,32,93,171–174. The dual functions of CTCF
through loop extrusion, where cohesin loads onto chromatin and bidi- as a context-dependent insulator and facilitator mirror the insulator
rectionally extrudes loops; once cohesin is stalled by chromatin-bound and tethering elements that have been described in D. melanogaster.
CTCF on one side, it is thought to continue to extrude on the other side Fruitfly insulators such as gypsy, 1A2, Wari and CTCF binding sites are
until it encounters a bound CTCF on that side too, thereby forming a full thought to reduce interactions between non-cognate E–P pairs190–192,
CTCF–CTCF loop166–177(Fig. 3c,d). Long before the loop extrusion model whereas tethering elements are hypothesized to promote interactions
was proposed, the insulator role of CTCF was functionally character- between cognate E–P pairs, thus serving a facilitator role193–196.
ized by its ability to block an enhancer from activating transcription Quantitatively, the rarity of a TAD being fully extruded by
at a downstream promoter178. cohesin72,73,197 is consistent with CTCF insulators and TADs providing
Insulators were originally thought of as individual elements178. a relatively modest approximately twofold to threefold drop in contact
However, the discovery of TADs161–165 together with the characteriza- probability across TAD boundaries as measured by 3C assays24,110,111,183.
tion of 747 random insertions of a promoter driving lacZ expression However, as we discuss next, there is subtlety in the interpretation of
into the mouse genome suggested that TADs functionally constrain contact probability reported by such assays.
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 580
Review article
Interpretation of contact probabilities from conformation capture many interactions (Fig. 4d). Only when the capture radius matches the
assays. The notion of ‘contact’ between two loci in 3C assays such interaction radius, will the 3C-measured contact probability be an accu-
as Hi-C and Micro-C typically means that the two loci are within the rate representation of the true E–P interaction probability. Therefore,
3C capture radius and therefore undergo crosslinking, ligation and because we currently do know neither what the E–P interaction radius
sequencing (Fig. 4a). The 3C capture radius should be distinguished is nor precisely what the 3C capture radius is, it remains challenging
from the E–P interaction radius when interpreting 3C maps. The con- to quantitatively interpret E–P contact probabilities from 3C assays.
tact probability reported by 3C assays is likely proportional to the Perhaps surprisingly, several studies using conformation capture
integral of the fraction of cells in which the E–P distance is smaller than assays show that maintenance of most E–P interactions is largely robust
the capture radius (shaded area under the curve in Fig. 4b), where the to short-term loss of loop extrusion23,30–32. Nevertheless, these results are
capture radius is affected by 3C protocol choices including crosslink- still consistent with loop extrusion having important roles in the estab-
ing and digestion, as well as by genomic context198,199. As illustrated in lishment of E–P interactions202,203 and the formation of very long-range
Fig. 4b, a large 3C capture radius could obscure the fold change in 3C E–P interactions204–206. The robustness of most E–P interactions to
contact probability between cognate and non-cognate E–P pairs. This short-term loss of loop extrusion measured by conformation capture
may also provide a plausible explanation for the observed moderate assays can be potentially attributed to several non-mutually exclusive
approximate twofold to threefold change in contact probability across possibilities, including: (1) there is some intrinsic ‘stickiness’ between E–P
TAD boundaries. It has been estimated that the capture radius of Hi-C elements23; (2) the capture radius is larger than the E–P interaction radius
is ~120–150 nm, although the capture radius can depend on the choice leading to the inclusion of non-interacting E–P pairs as being ‘in con-
of crosslinker and may be substantially smaller for Micro-C30,183,198–201. tact’; (3) loop extrusion is required for the establishment but not for the
Whether such a capture radius is suitable for studying E–P interactions maintenance of E–P interactions; and (4) loop extrusion simultaneously
depends on the interaction radii: if the 3C capture radius is bigger than contributes to forming and to breaking of E–P interactions.
the E–P interaction radius, the contact probability of conformation cap- Given that contact type and action-at-a-distance-type E–P inter-
ture assay will overestimate the true interaction probability (Fig. 4c); action models correspond to vastly different E–P interaction radii,
conversely, if the capture radius is smaller than the E–P interaction we next discuss the implications of different E–P interaction radii for
radius, then the corresponding conformation capture assay would miss enhancer selectivity.
a Distance cut-off in 3C assays b Measured fold change in contact probability depends on 3C capture radius
c If 3C capture radius > E–P interaction radius: d If 3C capture radius < E–P interaction radius:
3C contact probability will overestimate E–P interaction probability 3C contact probability will underestimate E–P interaction probability
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 581
ytilibaborP
E–P not ligated: E–P ligated: Capture Capture
E–P distance > 3C capture radius E–P distance ≤ 3C capture radius radius 1 radius 2 Capture Capture
Cognate E–P pair radius 1 radius 2
3C capture radius Non-cognate E–P pair
3C capture radius
Fold change in
contact probability = vs
3D E–P distance
Interaction Capture True interaction Contact probability Capture Interaction True interaction Contact probability
radius radius probability by 3C assays radius radius probability by 3C assays
Capture
3D E–P distance radius
Interaction
radius
ytilibaborP
3D E–P distance
ytilibaborP
Interaction
radius
Capture
radius
Fig. 4 | Interpreting the results of conformation capture assays. ‘contact probability’. Comparing a cognate E–P pair with a non-cognate E–P pair,
a, In chromosome conformation capture (3C) assays, enhancer–promoter the fold change in contact probability could appear a lot smaller with a larger
(E–P) pairs whose 3D distance is smaller than the capture radius are ligated and capture radius. c, Capture radii larger than the true E–P interaction radius would
counted as a ‘contact’. E–P pairs whose 3D distance is larger than the capture lead to the contact probability overestimating the true interaction probability.
radius are not ligated and considered not ‘in contact’. b, Different capture radii d, Capture radii smaller than the true E–P interaction radius would miss E–P
in conformation capture assays could lead to significantly different apparent interactions.
Review article
Loop-extrusion-mediated
E–P interaction with
proximal CTCF binding
Consistent with the
approximate twofold
to threefold drop in
contact probability
across TAD boundaries
measured by Hi-C,
whose capture radius is ~135 nm
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 582
ytilibaborp
noitcaretnI
d Fold increase in interaction probability over
diffusion alone at different interaction radii
ytilibaborp
noitcaretni
ni esaercni
dloF
)ylno
noisuffid
revo(
a Setup of 3D polymer simulation b Interaction radii of contact vs
400 kb ~ 10 Mb 400 kb Loop-extrusion-mediated condensate models
Transcription factor E–P interaction
Co-activator Contact models:
Enhancer interaction
radius tens of
Promoter
Pol II CTCF nanometres
×7
CTCF
E–P interaction mediated by diffusion only binding
site
Condensate
models:
interaction
radius hundreds
of nanometres
c Interaction probability dependency on interaction radii
for different conditions
15,390
0.20 0.0016
1,343
0.030
0.0012 214
0.15 212
0.020
0.0008 82.7
210
18.3 12.6 0.10 0.0004 0.010 28
11.5
5.1
26
3.0
0.0000 0.000 1.3 24 4.5 4.2 3.8
0.05
22
20
0
27 54 135 243 27 54 135* 243
Interaction radius (nm) Interaction radius (nm; * ~Hi-C capture radius)
E–P interactions mediated by diffusion only
Loop-extrusion-mediated E–P interactions
Loop-extrusion-mediated E–P interactions with proximal CTCF binding
e Different capture radii lead to apparent differences between
contact maps of the same underlying chromosome conformations
Capture radius = 27 nm Capture radius = 54 nm Capture radius = 135 nm ~ Hi-C capture radius Capture radius = 243 nm
0 200 400 600 8000 200 400 600 800 0 200 400 600 800 0 200 400 600 800
kb kb kb kb
Review article
Fig. 5 | Enhancer selectivity mediated by 3D genome organization as a probability depends strongly on the interaction radius. There is a differential
function of interaction radius. a, Setup of 3D polymer simulation of seven dependency of interaction probability on the interaction radius for the three
enhancer–promoter (E–P) pairs. Each pair has a 400 kb E–P distance, and two simulated conditions. d, Fold increase in interaction probabilities normalized
adjacent pairs are 10 Mb apart. Three conditions were simulated: diffusion only to the diffusion-only condition. The numbers on the arcs show the fold increase
(orange), loop extrusion without proximal CTCF sites (blue) and loop extrusion in interaction probability between the indicated conditions. c,d, Error bars
with proximal, facilitator CTCF binding (pink, with a 50% CTCF occupancy for represent s.e.m., and n = 7 E–P pairs. e, Simulated contact probability maps with
each CTCF binding site210–212). The simulation parameters for loop extrusion the indicated capture radius, calculated from 3D polymer conformations of
were inferred from live-cell imaging and Micro-C data72. The 3D distances are all seven E–P pairs and the surrounding region in the simulation that includes
monitored for each E–P pair, and when the distance is smaller than the interaction loop extrusion with proximal CTCF binding. An iterative correction247 was
radius, the E–P pair is considered interacting. For the simulation details, see applied to each contact probability map, and the colour bar was adjusted
Supplementary Box 1. b, Interaction radii for contact-type E–P interactions individually to optimize the display contrast of each map. Pol II, polymerase II;
versus action-at-a-distance-type (for example, through condensates) TAD, topologically associating domain.
E–P interactions differ by roughly an order of magnitude. c, Interaction
Enhancer selectivity as a function of E–P interaction radius. To illustrate radius is likely on the order of hundreds of nanometres36,37,58,62,65,67,
the relationship between E–P interaction radius and enhancer selectiv- although it remains very poorly understood (Fig. 5b). Thus, to reflect
ity, we begin by considering how distal enhancers and promoters may action-at-a-distance models, we chose an interaction radius of 243 nm.
find each other. First, chromosomes naturally undergo passive 3D diffu- Given the estimated Hi-C capture radius of ~135 nm183,198,199,201, we also
sion motions owing to thermal fluctuations207. Recent live-cell imaging added an E–P interaction radius of 135 nm in our analysis, to represent
and micromanipulation studies have shown that mammalian chromo- the conditions in which the estimated Hi-C capture radius exactly
somes exhibit Rouse dynamics where the mean squared displacement matches the E–P interaction radius (Fig. 4).
1
is proportional to the square root of time72,73,208 (MSD(t)∝t2). Passive After equilibrating the polymer simulations, we tracked the
3D diffusion is expected to be highly efficient at bringing together 3D distance between each E–P pair and computed their interaction
enhancers and promoters separated by short genomic distances, but to probability (the fraction of the time an E–P pair is within the interac-
be highly inefficient for bridging very distal E–P pairs209. Second, loop tion radius) for interaction radii of 27, 54, 135 and 243 nm. We observe
extrusion reduces the dimensionality of the E–P search process from two clear trends. First, the absolute interaction probability increases
3D to 1D and from passive to active, which can greatly increase the strongly with the interaction radius — this makes sense, as with a 27 nm
efficiency of the search. Third, the ability of loop extrusion to accelerate interaction radius, the enhancer and promoter must be in true contact,
the E–P search process is strongly facilitated by the presence of CTCF whereas with a 243 nm interaction radius, the enhancer and promoter
sites that serve as facilitator elements (Fig. 3e). just have to be near each other (Fig. 5c). Second, loop extrusion consist-
To quantitatively illustrate the relationship between enhancer ently increases the interaction probability compared with diffusion
selectivity mediated by these three E–P search mechanisms and the alone, and loop extrusion with CTCF facilitator sites strongly increases
E–P interaction radius, we performed 3D polymer simulations of a the interaction probability (Fig. 5c).
70 Mb mini-chromosome with seven E–P pairs, each with a 400 kb E–P To show this effect more clearly, we quantified the fold increase
distance and 10 Mb spacing between each two adjacent E–P pairs (Sup- in E–P interaction probability over diffusion alone (Fig. 5d). Loop
plementary Box 1 and Fig. 5a). We subjected the mini-chromosome extrusion without facilitating CTCF sites moderately increases E–P
to simulation conditions that reflect three E–P search mechanisms: interactions by 4–12-fold, with a relatively modest dependence on
(1) by passive 3D diffusion alone; (2) with loop extrusion and 3D dif- interaction radius. By contrast, proximal facilitator CTCF sites can
fusion but no CTCF binding and (3) with loop extrusion, 3D diffusion markedly increase E–P interactions for contact models reaching
and convergent CTCF sites serving as facilitators (with 50% CTCF up to approximately 15,000-fold increase in E–P interactions for a
occupancy210–212) right next to each of the enhancer and promoter 27 nm interaction radius compared with diffusion alone and around
(Fig. 5a). Simulated condition (1) can be experimentally realized 1,300-fold compared with extrusion without CTCF sites. With the
through depletion of RAD21 (a subunit of cohesin)72,73. Simulated interaction radius of 243 nm corresponding to action-at-a-distance
condition (2) can be experimentally realized through CTCF deple- models, adding proximal CTCF facilitator sites only negligibly affects
tion, in which cohesin still extrudes loops but would not be stalled by E–P interactions by 1.3-fold (Fig. 5d). Thus, the sensitivity to proximal
CTCF72,73. Simulated condition (3) corresponds to the wild-type experi- CTCF facilitator sites depends very strongly and nonlinearly on the
mental condition in which both CTCF and loop extrusion are present, E–P interaction radius. Additionally, when ‘performing an in silico
assuming that CTCF facilitator sites are present at the enhancer and/or Hi-C experiment’ by setting the interaction radius to 135 nm, the
promoter. simulated fold increase in E–P interaction probability or contact
The magnitude of enhancer selectivity will depend on the E–P inter- probability with proximal convergent CTCF sites was approximately
action radius. For the E–P interaction models relying on direct contact, threefold, consistent with the previously reported approximately
the interaction radius would be expected to match the diameter of the twofold to threefold change in contact probability across TAD
protein complexes that mediate E–P interactions, which is likely on boundaries24,110,111,183 (Fig. 5d).
the order of tens of nanometres213. For example, the human Mediator– To illustrate these points using the visual language of Hi-C contact
PIC complex is estimated to be around 20 nm by cryo-electron micros- maps, we converted our simulations to normalized Hi-C-like con-
copy structures43–45 (Fig. 5b). Thus, we analysed interaction radii of tact maps using 3C capture radii matching the four E–P interaction radii
27 nm and 54 nm to reflect more and less stringent contact E–P models. of 27, 54, 135 and 243 nm. As expected, using a small capture radius leads
For the action-at-a-distance models of E–P interactions, the interaction to a ‘high contrast’ contact map with clearly visible ‘extrusion stripes’
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 583
Review article
Glossary
Architectural proteins Condensates First-passage time with respect to a reference position,
Proteins that regulate 3D chromatin Refers to formation of membraneless The time taken for a stochastic process to usually calculated over a range
structure by forming chromatin loops compartments of high local reach a specific state for the first time, for of time intervals.
and domains, which can regulate concentration of factors through example, the time taken for an enhancer
interactions between enhancers liquid–liquid phase separation. to find and interact with a promoter. Rouse dynamics
and promoters. The movement and behaviour of
Co-repressors Hub polymers in a bead–spring model,
Biochemical compatibility Enzymatic complexes recruited to DNA Discrete nuclear domains of high in which monomers are connected
The intrinsic ability for an enhancer directly or indirectly by transcription transcription protein concentration, by Hookean springs and a monomer
to activate transcription at some factors to establish and maintain which serve as a focal point of activity; only interacts with its nearest
promoters but not others, which repression of transcription. ‘hub formation’ is often used to indicate neighbours.
may be determined by the binding a formation mechanism that is distinct
profile of transcription factors and Enhanceosome from phase separation. Silencers
co-activators. A protein complex that assembles Regulatory DNA elements that
on an enhancer to regulate the Insulators reduce transcription at cognate
Chromatic aberrations transcription of the cognate promoter. DNA elements bound by specific promoters, including from far away
Owing to the refractive index protein complexes, which may in the genome.
varying with the wavelength of Enhancer RNAs reduce gene expression when placed
light, a perfectly colocalizing Non-coding RNAs transcribed from between an enhancer and a promoter, Super-enhancers
E–P pair (true distance of 0 nm) enhancers, which may have gene presumably by reducing the probability Genomic regions consisting of multiple
may be measured as being far regulatory functions. of their interaction. enhancers that can drive high level
apart. Very accurate correction of of transcription at cognate promoters;
chromatic aberrations is required E–P interaction radius Intrinsically disordered originally defined based on Mediator
for precise measurements of E–P The maximum 3D distance between an regions enrichment.
distances. enhancer and a promoter that enables Protein segments lacking well-defined
them to functionally interact. 3D structure in physiological conditions, Transcription memory
Clustering which form dynamic ensembles of The phenomenon in which the
A cluster corresponds to higher-than- Facilitator conformations and may engage in influence of a stimulus persists beyond
expected local density of molecules. Refers to DNA–protein complexes such multivalent interactions. the initial exposure to the stimulus,
The term cluster is agnostic to the as DNA-bound CTCF, which can increase including promoter memory of
mechanism of cluster formation and the interaction probability between Mean squared displacement past E–P interactions.
clusters are often defined using spatial promoters and regulatory elements The average of the squared
statistics. such as enhancers and silencers. displacement of a particle or locus
and ‘E–P loop dots’, whereas a large capture radius results in a ‘blurred’ Thus, an interesting insight emerging from this analysis is that
low contrast contact map with poorly resolved stripes and dots (Fig. 5e). genes whose enhancer-dependent expression depends strongly on
Although we stress that we have not considered all possible param- proximal CTCF sites may have small E–P interaction radii, which is
eter combinations in these illustrative 3D polymer simulations, our more consistent with a contact mechanism. For example, loss of the
simulation results nevertheless demonstrate that: (1) what we measure promoter-proximal CTCF site upstream of MYC results in 70–80%
in 3C assays depends on the capture radius, for example, Micro-C may downregulation of MYC expression189, which may be indicative of a
produce ‘higher contrast maps’ because Micro-C has a smaller capture relatively small E–P interaction radius. It is also interesting to consider
radius than Hi-C, thus producing quantitatively different maps for the that if different E–P pairs have different E–P interaction radii, they
same biological sample (Fig. 5e); (2) enhancer selectivity mediated by could have very different sensitivities to these regulatory mechanisms.
3D genome organization is likely a strong function of E–P interaction Finally, to explain how a relatively small fold change in contact prob-
radius; (3) loop extrusion without CTCF facilitator sites yields only ability might lead to a large change in transcription, it has been proposed
moderate enhancer selectivity compared with diffusion alone; that transcription is a highly nonlinear and convex function of E–P inter-
(4) with loop extrusion, the addition of proximal facilitator CTCF sites action probability24,110,111,214. Although our simulations are certainly not
can result in up to 1,300-fold increase in E–P interaction probabilities, inconsistent with these models, they also provide a potential alternative
assuming interaction radii roughly corresponding to direct E–P contact explanation: small changes in the 3C-measured contact probability could
(27 nm; Fig. 5d); (5) although CTCF is predominantly thought of as an be due to a large 3C capture radius hiding or obscuring quite large changes
insulator, the quantitative effect of CTCF as a facilitator may be greater in the functionally relevant E–P interaction probability (Figs. 4 and 5e).
in some cases, especially for E–P pairs relying on contact; (6) at an
interaction radius of 243 nm — corresponding to action-at-a-distance From simulated E–P pairs to biological E–P pairs
models — proximal CTCF binding provides negligible enhancer Supporting the potential role of proximal CTCF at cognate E–P pairs,
selectivity nor substantially increased E–P interaction probability. CTCF and cohesin were shown to be enriched at interacting promoters
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 584
Review article
when taking the viewpoint of an enhancer and enriched at interacting In summary, although each E–P pair is unique, many experimen-
enhancers when taking the viewpoint of a promoter215. Some well-known tally validated very long-range E–P pairs do tend to have a CTCF site
examples of cognate E–P pairs with proximal CTCF binding on both sides at either the enhancer and/or the promoter, which is consistent with
include the Shh gene, which interacts with the ZRS (zone of polarizing CTCF being a facilitator of E–P interactions, in addition to an insulator.
activity regulatory sequence) enhancer located ~1 Mb downstream in Having already discussed 3C methods, we next discuss insights
mouse E10.5 embryonic limb buds188, and the MYC gene, which interacts into E–P interaction mechanisms and selectivity coming from imaging
with its distal enhancer cluster ~1.8 Mb away in human acute lympho- methods that can directly estimate 3D distances between enhancers
blastic leukaemia cells216 (Fig. 6a). In addition, as reported by a recent and promoters.
preprint, the PTEN gene in HCT116 cells also has proximal CTCF binding
at the PTEN promoter and at the H9 and H12 enhancers, around 250 kb Imaging 3D E–P interactions
and 500 kb downstream of the promoter, respectively217. In addition to 3C and other 3D genomics assays, which albeit very pow-
A different genome-wide analysis of CTCF binding found proximal erful provide relative measurements confounded by the capture radius,
CTCF binding enriched at the cognate promoter but not at the cognate substantial insights into E–P interactions and transcription regulation
enhancer93. ‘Docking’ of an extruding cohesin at the promoter-proximal have also come from imaging-based studies. Imaging methods can
CTCF site may facilitate reeling-in DNA to more efficiently search for directly measure absolute E–P 3D distances, but also have technical
distal enhancers, thereby alleviating the need for having CTCF binding limitations. Broadly speaking, imaging methods can be divided into
proximal to the enhancer93. E–P pairs with proximal CTCF binding only two categories: fixed-cell and live-cell imaging. DNA fluorescence in situ
at the promoter include the Vcan gene with the Xrcc4/Tmem167 pro- hybridization (DNA-FISH), wherein cells are fixed, permeabilized and
moter acting as an enhancer about 350 kb downstream in mouse NPCs93 typically heated in formamide to allow for fluorescently labelled DNA
and the MYC gene with the MYC endometrial carcinoma super-enhancer probes to hybridize to genomic DNA, is the classic fixed-cell imaging
located 800 kb downstream in Ishikawa cells218,219 (Fig. 6b). method and can measure E–P 3D distances by using probes in differ-
There are also many cognate E–P pairs without proximal CTCF ent colours for the enhancer and the promoter222–227. More recently,
binding, such as the ADAMTS14 gene with its enhancer located 25 kb tiling DNA-FISH techniques, where individual probes are visualized
downstream in K562 cells and the LY9 gene with its enhancer located sequentially in time, have enabled chromatin tracing by visualizing
5 kb downstream in GM12878 cells220 (Fig. 6c). However, given the much dozens of points along the chromosome26,228–234. Although powerful,
shorter genomic separation between these enhancers and promot- limitations of fixed-cell imaging methods include loss of temporal
ers, passive 3D diffusion would be expected to be very efficient, thus dynamics and fixation artefacts82,235. Furthermore, as reported in a
perhaps explaining the lack of proximal CTCF binding in these two recent preprint, the harsh procedures necessary to allow hybridization
examples of E–P pairs. This possibility is consistent with the notion disrupt fine-scale 3D chromatin structure236, although more gentle
that CTCF and cohesin are likely most important for facilitating interac- fixed-cell imaging protocols have been developed, such as single-strand
tions between very distal E–P pairs197,204,205, as the efficiency of passive exonuclease resection (RASER)-FISH, which avoids heat denaturation237.
3D diffusion is highly dependent on genomic E–P separation. To illus- By contrast, live-cell imaging, which typically uses genome-engineered
trate this point, the time it takes an enhancer to find a distal promoter arrays of binding sites for fluorescently labelled DNA-binding proteins
(first-passage time) would be expected to scale super-linearly with or deactivated-Cas9 labelling, allows for direct visualization of 3D
genomic separation, with an exponent ranging from 1.07 (experimental interactions over time48,72,73,238–241 and can be extended to simultane-
estimates25,221) to 2 (a simple Rouse polymer model), such that increas- ously visualize nascent RNA transcription in a third colour25,27,35,242.
ing the genomic E–P separation tenfold from 10 kb to 100 kb could Live imaging methods also face limitations: the genome engineering
increase the first-passage time up to 100-fold. required for fluorescent labelling can be very laborious resulting in
a Proximal CTCF at both the b Proximal CTCF at only the c No proximal CTCF at either the
enhancer and the promoter promoter side promoter or enhancer
Mouse E10.5 embryonic limb buds Mouse neural progenitor cells K562 cells (human myelogenous leukaemia)
~1,000 kb
Transcription factor ~350 kb ~25 kb
Co-activator
CTCF Enhancer
CTCF binding Promoter
site Pol II Vcan gene Xrcc4/Tmem167 promoter ADAMTS14 gene ADAMTS14 enhancer
Shh gene ZRS enhancer (acting as an enhancer)
Human acute lymphoblastic leukaemia cells Ishikawa cells (human endometrial adenocarcinoma) GM12878 cells (B lymphoblastoid cells)
~1,800 kb ~800 kb ~5 kb
MYC gene MYC distal MYC gene MYC-ECSE LY9 enhancer LY9 gene
enhancer cluster
Fig. 6 | Examples of enhancer–promoter pairs with different CTCF binding pairs with proximal CTCF binding only at the promoter side93,218,219. c, Examples
patterns. a, Examples of enhancer–promoter (E–P) pairs with proximal CTCF of E–P pairs with no proximal CTCF binding on either side220. MYC-ECSE, MYC
binding on both the enhancer and the promoter sides188,216. b, Examples of E–P endometrial carcinoma super-enhancer; Pol II, polymerase II.
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 585
Review article
0.002
0.001
0
0 250 500 750 1,000 1,250 0 250 500 750 1,000 1,250
3D E–P distance (nm)
0.002 0.002
0.001 0.001
0 0
0 250 500 750 1,000 1,250 0 250 500 750 1,000 1,250
3D E–P distance (nm) 3D E–P distance (nm)
low throughput, and careful controls are necessary to assess whether radius of 54 nm), resulting in a bimodal E–P 3D distance histogram
the fluorescent labelling perturbs function. (Fig. 7a). Practically, however, DNA-FISH probes tend to be very long
Perhaps surprisingly, imaging-based studies have thus far (10–200 kb)48,222–227 and fluorescent labels are often placed slightly
observed a relatively low correlation between E–P distances and nas- away from the enhancer and the promoter27,35,48,72,73. Assuming an
cent transcription26,36,243 and have generally observed E–P distances of optimistic infinitesimally small fluorescent label at a distance of 3 kb
200 nm27,34–38,244,245. These observations have often been interpreted to from the enhancer or promoter — 3 kb is less than what is used in most
rule out contact-based E–P interaction models in favour of action-at- experimental studies26,35–38,72,244,245 — is enough to make the first peak
a-distance models27,34–38,244,245 (Fig. 1c), but as we discuss next, measured of the bimodal distribution corresponding to E–P contact almost
E–P distances of ~200 nm may not be inconsistent with contact models. disappear in the histogram (Fig. 7b). Localization error further
Although the precision of localization microscopy-based imaging degrades the accuracy of optical measurements, which for E–P 3D
methods is theoretically unlimited246, several technical limitations distances require six measurements (x,y,z for each E–P pair). Although
including localization error, labelling issues, chromatic aberrations there is no theoretical limit to the precision of localization microscopy,
and other issues mean that measured 3D distances will tend to be much it is nevertheless expensive to achieve low error as the standard devia-
greater than true E–P distances48. tion of the error scales inversely with the square root of the number
To illustrate this point, we performed 3D polymer simulations of of detected photons (σ∝ 1 )246. Assuming a localization error of
NPhoton
E–P interactions with strong facilitator CTCF sites at both the enhancer 30 nm in x,y and 60 nm in z — which is relatively optimistic — is suffi-
and the promoter, such that the enhancer and the promoter are in cient to make the bimodality in the 3D distance E–P histogram largely
direct contact around 3% of the time (when assuming an interaction disappear (Fig. 7c). When we combine both label distance and
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 586
ytisned
ytilibaborP
0.002
0 kb label distance 3 kb label distance σ = σ = σ = 0 nm σ = σ = σ = 0 nm
X Y Z X Y Z
0.001
0
3D E–P distance (nm)
ytisned
ytilibaborP
ytisned
ytilibaborP
0 kb label distance 3 kb label distance
σ = σ = 30 nm σ = σ = 30 nm
X Y X Y
σ = 60 nm σ = 60 nm Z Z
3 kb label distance
σ = σ = 30 nm
X Y
σ = 60 nm
Z
ytisned
ytilibaborP
True Observed
0.006
0.004
0.002
0
0 100 200 300 400
3D E–P distance (nm)
ytisned
ytilibaborP
1.0
0 kb label distance
σ = σ = σ = 0 nm
X Y Z
0.5
0
027 100 200 300 400
3D E–P distance (nm)
ytisned
ytilibaborP
a 3D E–P distance distribution without b Effect of label distance from element on Fig. 7 | Interpreting imaging studies of enhancer–
label–element distance and localization error apparent 3D E–P distance promoter interactions. a, Simulation of imaging-
Transcription factor Fluorescent 3 kb 3 kb measured distribution of 3D enhancer–promoter
Fluorescent Co-activator marker (E–P) distances without label–element (enhancer,
marker Enhancer CTCF promoter) distance and localization error. The
Promoter CTCF bimodality of 3D E–P distances arises owing to
Pol II binding loop extrusion stalled by facilitator CTCFs, thereby
site bringing E–P pairs into proximity. b, Label–element
distance can obscure the bimodality of the 3D
E–P distance distribution. c, Localization error
could similarly weaken the bimodality of the 3D E–P
distance distribution. d, Increased label distance
and localization error combined could make the
bimodality of 3D E–P distance disappear. e, With
increased label distance and localization error, true
E–P distances smaller than 27 nm could correspond
to measured E–P distances of ~100–200 nm. The
simulation parameters for loop extrusion were
c Effect of localization error d Combined effects of label distance and
inferred from live-cell imaging and Micro-C data72,
on apparent 3D E–P distance localization error on apparent 3D E–P distance
and a CTCF occupancy of 100% was used to better
illustrate the change in the bimodality of distance
distributions, such that the enhancer and the
promoter are in direct contact 3% of the time when
assuming an interaction radius of 54 nm. For the
simulation details, see Supplementary Box 1.
Pol II, polymerase II.
e Apparent 3D E–P distances of ~200 nm may not be inconsistent with contact models
Review article
localization error, the previously visible E–P contact peak (Fig. 7a) which is not readily possible in fixed-cell imaging. Moreover, spatial
entirely disappears (Fig. 7d). measurements (for example, 3C assays and chromatin tracing) and
To illustrate this point more clearly, if we focus just on true E–P 3D temporal measurements (for example, live imaging) can be integrated
distances smaller than 27 nm and add both label distance (3 kb) and to constrain mechanistic polymer models to obtain a full 4D picture,
modest localization error (30 nm in x,y and 60 nm in z), our measured which can then be tested through perturbations. We anticipate that
E–P 3D distances would be much greater at ~100–200 nm (Fig. 7e). such integrative approaches may greatly improve our understanding
Notably, this illustration includes only the effects of optimistic label of enhancer mechanisms and selectivity over the coming years and
distances and localization error, and no other issues that may further provide many new insights and surprises.
degrade the accuracy such as incomplete chromatic aberration correc-
tions and so on48. Thus, when interpreting imaging-based 3D distance Published online: 27 February 2024
measurements, it is crucial to note that measured 3D distances will
References
typically be much greater than true 3D distances48 (Fig. 7e), meaning 1. Bentovim, L., Harden, T. T. & DePace, A. H. Transcriptional precision and accuracy in
that although measured E–P 3D distances of ~200 nm27,34–38,244,245 might development: from measurements to models and mechanisms. Development 144,
initially seem to rule out contact models, such measurements in most 3855–3866 (2017).
2. Ong, C.-T. & Corces, V. G. Enhancer function: new insights into the regulation of
cases actually remain fully consistent with contact models (Fig. 1c). tissue-specific gene expression. Nat. Rev. Genet. 12, 283–293 (2011).
3. Field, A. & Adelman, K. Evaluating enhancer function and transcription. Annu. Rev.
Conclusions and future outlook Biochem. 89, 213–234 (2020).
4. Zabidi, M. A. & Stark, A. Regulatory enhancer–core-promoter communication via
Although enhancers were discovered already in 19817–10, how enhanc- transcription factors and cofactors. Trends Genet. 32, 801–814 (2016).
ers selectively interact with cognate genes and activate them remains 5. Andersson, R. et al. An atlas of active enhancers across human cell types and tissues.
Nature 507, 455–461 (2014).
very poorly understood. Broadly, regulation of gene expression by
6. Spitz, F. & Furlong, E. E. Transcription factors: from enhancer binding to developmental
distal enhancers can occur in two steps: E–P interaction and transcrip- control. Nat. Rev. Genet. 13, 613–626 (2012).
tion activation. Three-dimensional E–P interaction models provide a 7. Banerji, J., Olson, L. & Schaffner, W. A lymphocyte-specific cellular enhancer is located
downstream of the joining region in immunoglobulin heavy chain genes. Cell 33,
plausible explanation for the promoter skipping phenomenon, which is
729–740 (1983).
difficult to explain within the framework of 1D models (Fig. 1b). Consid- 8. Gillies, S. D., Morrison, S. L., Oi, V. T. & Tonegawa, S. A tissue-specific transcription
ering space, 3D E–P interactions can involve contact or action at a dis- enhancer element is located in the major intron of a rearranged immunoglobulin heavy
chain gene. Cell 33, 717–728 (1983).
tance; considering time, 3D E–P interactions can be either dynamic or
9. Mercola, M., Wang, X.-F., Olsen, J. & Calame, K. Transcriptional enhancer elements in the
stable (Fig. 1c). Although still preliminary, the dynamic 3D E–P distances mouse immunoglobulin heavy chain locus. Science 221, 663–665 (1983).
measured by live-cell imaging studies25,27,35,72,73 suggest that E–P interac- 10. Banerji, J., Rusconi, S. & Schaffner, W. Expression of a β-globin gene is enhanced by
remote SV40 DNA sequences. Cell 27, 299–308 (1981).
tions are unlikely to be very stable and long-lived, although function-
11. Halfon, M. S. Studying transcriptional enhancers: the founder fallacy, validation creep,
ally relevant interaction durations remain very poorly understood. and other biases. Trends Genet. 35, 93–103 (2019).
Furthermore, whether E–P interactions are mediated by contact or 12. Galouzis, C. C. & Furlong, E. E. Regulating specificity in enhancer–promoter
communication. Curr. Opin. Cell Biol. 75, 102065 (2022).
action at a distance also remains to be determined.
13. van Arensbergen, J., van Steensel, B. & Bussemaker, H. J. In search of the determinants
Enhancer selectivity can be regulated at both the E–P interac- of enhancer–promoter interaction specificity. Trends Cell Biol. 24, 695–702 (2014).
tion level and the transcription activation level. Although the latter 14. Furlong, E. E. & Levine, M. Developmental enhancers and chromosome topology.
Science 361, 1341–1345 (2018).
has explained specific cases of enhancer selectivity, E–P interactions
15. Moreau, P. et al. The SV40 72 base repair repeat has a striking effect on gene expression
have received increasing attention with our improving knowledge of both in SV40 and other chimeric recombinants. Nucleic Acids Res. 9, 6047–6068 (1981).
3D genome organization. In particular, we emphasize that although 16. Travers, A. Chromatin modification by DNA tracking. Proc. Natl Acad. Sci. USA 96,
13634–13637 (1999).
CTCF is traditionally thought of as an insulator, its role as a facilitator
17. Hatzis, P. & Talianidis, I. Dynamics of enhancer–promoter communication during
of E–P interactions may be equally or even more important. We high- differentiation-induced gene activation. Mol. Cell 10, 1467–1477 (2002).
light that the ability of different E–P interaction models to mediate 18. Bulger, M. & Groudine, M. Looping versus linking: toward a model for long-distance gene
activation. Genes Dev. 13, 2465–2477 (1999).
enhancer selectivity likely depends on the E–P interaction radius, and 19. Chen, Z. et al. Widespread increase in enhancer–promoter interactions during
that if the 3C capture radius is substantially different from the E–P developmental enhancer activation in mammals. Preprint at bioRxiv https://doi.org/
interaction radius, then contact probabilities from 3C assays may not 10.1101/2022.11.18.516017 (2022).
20. Gasperini, M. et al. A genome-wide framework for mapping gene regulation via cellular
reflect functionally relevant E–P interaction probabilities. Similarly, genetic screens. Cell 176, 377–390 (2019).
although imaging-based methods can directly measure E–P 3D dis- 21. Li, G. et al. Extensive promoter-centered chromatin interactions provide a topological
tances, these measured 3D distances tend to be much larger than true basis for transcription regulation. Cell 148, 84–98 (2012).
22. Sanyal, A., Lajoie, B. R., Jain, G. & Dekker, J. The long-range interaction landscape of gene
E–P distances, such that great care is necessary when interpreting promoters. Nature 489, 109–113 (2012).
measured 3D distances as functionally relevant E–P interaction ranges. 23. Goel, V. Y., Huseyin, M. K. & Hansen, A. S. Region capture Micro-C reveals coalescence of
enhancers and promoters into nested microcompartments. Nat. Genet. 55, 1048–1056
Nevertheless, although both 3C assays and imaging methods
(2023).
have limitations, these limitations are largely orthogonal and can be 24. Zuin, J. et al. Nonlinear control of transcription through enhancer–promoter interactions.
overcome through careful experimental interpretation, perturba- Nature 604, 571–577 (2022).
25. Brückner, D. B., Chen, H., Barinov, L., Zoller, B. & Gregor, T. Stochastic motion and
tions and integrative biophysical modelling. 3C and chromatin tracing
transcriptional dynamics of pairs of distal DNA loci on a compacted chromosome.
methods provide great insights into the 3D spatial organization of Science 380, 1357–1362 (2023).
chromatin, albeit without temporal resolution. Live-cell imaging meth- 26. Mateo, L. J. et al. Visualizing DNA folding and RNA in embryos at single-cell resolution.
Nature 568, 49–54 (2019).
ods can provide temporal information for both E–P interactions and
27. Chen, H. et al. Dynamic interplay between enhancer–promoter topology and gene
nascent transcription, but are limited to labelling only a few genomic activity. Nat. Genet. 50, 1296–1303 (2018).
loci and RNAs. Furthermore, as localization noise is uncorrelated with 28. Deng, W. et al. Controlling long-range genomic interactions at a native locus by targeted
tethering of a looping factor. Cell 149, 1233–1244 (2012).
time, live-cell imaging in combination with statistical inference meth-
29. Deng, W. et al. Reactivation of developmentally silenced globin genes by forced
ods can rigorously detect looping interactions in time trajectories72, chromatin looping. Cell 158, 849–860 (2014).
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 587
Review article
30. Hsieh, T.-H. S. et al. Resolving the 3D landscape of transcription-linked mammalian 64. Cho, W.-K. et al. Mediator and RNA polymerase II clusters associate in transcription-
chromatin folding. Mol. Cell 78, 539–553 (2020). dependent condensates. Science 361, 412–415 (2018).
31. Hsieh, T.-H. S. et al. Enhancer–promoter interactions and transcription are largely 65. Sabari, B. R. et al. Coactivator condensation at super-enhancers links phase separation
maintained upon acute loss of CTCF, cohesin, WAPL or YY1. Nat. Genet. 54, 1919–1932 and gene control. Science 361, eaar3958 (2018).
(2022). 66. Hu, Z. & Tee, W.-W. Enhancers and chromatin structures: regulatory hubs in gene
32. Aljahani, A. et al. Analysis of sub-kilobase chromatin topology reveals nano-scale expression and diseases. Biosci. Rep. 37, BSR20160183 (2017).
regulatory interactions with variable dependence on cohesin and CTCF. Nat. Commun. 67. Chong, S. et al. Imaging dynamic and selective low-complexity domain interactions that
13, 2139 (2022). control gene transcription. Science 361, eaar2555 (2018).
33. Fulco, C. P. et al. Activity-by-contact model of enhancer–promoter regulation from 68. Wang, X., Cairns, M. J. & Yan, J. Super-enhancers in transcriptional regulation and
thousands of CRISPR perturbations. Nat. Genet. 51, 1664–1669 (2019). genome organization. Nucleic Acids Res. 47, 11481–11496 (2019).
34. Karr, J. P., Ferrie, J. J., Tjian, R. & Darzacq, X. The transcription factor activity gradient 69. Hnisz, D., Shrinivas, K., Young, R. A., Chakraborty, A. K. & Sharp, P. A. A phase separation
(TAG) model: contemplating a contact-independent mechanism for enhancer–promoter model for transcriptional control. Cell 169, 13–23 (2017).
communication. Genes Dev. 36, 7–16 (2022). 70. Monfils, K. & Barakat, T. S. Models behind the mystery of establishing enhancer–promoter
35. Alexander, J. M. et al. Live-cell imaging reveals enhancer-dependent Sox2 transcription interactions. Eur. J. Cell Biol. 100, 151170 (2021).
in the absence of enhancer proximity. eLife 8, e41769 (2019). 71. Kent, S. et al. Phase-separated transcriptional condensates accelerate target-search
36. Benabdallah, N. S. et al. Decreased enhancer–promoter proximity accompanying process revealed by live-cell single-molecule imaging. Cell Rep. 33, 108248 (2020).
enhancer activation. Mol. Cell 76, 473–484 (2019). 72. Gabriele, M. et al. Dynamics of CTCF- and cohesin-mediated chromatin looping revealed
37. Bialek, W., Gregor, T. & Tkačik, G. Action at a distance in transcriptional regulation. by live-cell imaging. Science 376, 496–501 (2022).
Preprint at https://arXiv.org/abs/1912.08579 (2019). 73. Mach, P. et al. Cohesin and CTCF control the dynamics of chromosome folding.
38. Heist, T., Fukaya, T. & Levine, M. Large distances separate coregulated genes in living Nat. Genet. 54, 1907–1918 (2022).
Drosophila embryos. Proc. Natl Acad. Sci. USA 116, 15062–15067 (2019). 74. Horikoshi, M., Hai, T., Lin, Y.-S., Green, M. R. & Roeder, R. G. Transcription factor ATF
39. Richter, W. F., Nayak, S., Iwasa, J. & Taatjes, D. J. The mediator complex as a master interacts with the TATA factor to facilitate establishment of a preinitiation complex.
regulator of transcription by RNA polymerase II. Nat. Rev. Mol. Cell Biol. 23, 732–749 Cell 54, 1033–1042 (1988).
(2022). 75. Schaffner, W. A hit-and-run mechanism for transcriptional activation? Nature 336,
40. Osman, S. & Cramer, P. Structural biology of RNA polymerase II transcription: 20 years 427–428 (1988).
on. Annu. Rev. Cell Dev. Biol. 36, 1–34 (2020). 76. Pownall, M. E. et al. Chromatin expansion microscopy reveals nanoscale organization
41. Soutourina, J. Transcription regulation by the mediator complex. Nat. Rev. Mol. Cell Biol. of transcription and chromatin. Science 381, 92–100 (2023).
19, 262–274 (2018). 77. Lammers, N. C., Kim, Y. J., Zhao, J. & Garcia, H. G. A matter of time: using dynamics and
42. Allen, B. L. & Taatjes, D. J. The Mediator complex: a central integrator of transcription. theory to uncover mechanisms of transcriptional bursting. Curr. Opin. Cell Biol. 67,
Nat. Rev. Mol. Cell Biol. 16, 155–166 (2015). 147–157 (2020).
43. Abdella, R. et al. Structure of the human Mediator-bound transcription preinitiation 78. Popp, A. P., Hettich, J. & Gebhardt, J. C. M. Altering transcription factor binding
complex. Science 372, 52–56 (2021). reveals comprehensive transcriptional kinetics of a basic gene. Nucleic Acids Res. 49,
44. Chen, X. et al. Structures of the human Mediator and Mediator-bound preinitiation 6249–6266 (2021).
complex. Science 372, eabg0635 (2021). 79. Stavreva, D. A. et al. Transcriptional bursting and co-bursting regulation by steroid
45. Rengachari, S., Schilbach, S., Aibara, S., Dienemann, C. & Cramer, P. Structure of the hormone release pattern and transcription factor mobility. Mol. Cell 75, 1161–1177
human Mediator–RNA polymerase II pre-initiation complex. Nature 594, 129–133 (2021). (2019).
46. Chen, X. et al. Structural insights into preinitiation complex assembly on core promoters. 80. Fritzsch, C. et al. Estrogen-dependent control and cell-to-cell variability of transcriptional
Science 372, eaba8490 (2021). bursting. Mol. Syst. Biol. 14, e7678 (2018).
47. Panne, D., Maniatis, T. & Harrison, S. C. An atomic model of enhanceosome structure 81. Tantale, K. et al. A single-molecule view of transcription reveals convoys of RNA
in the vicinity of DNA. Cell 129, 1111 (2007). polymerases and multi-scale bursting. Nat. Commun. 7, 12248 (2016).
48. Brandão, H. B., Gabriele, M. & Hansen, A. S. Tracking and interpreting long-range 82. Teves, S. S. et al. A dynamic mode of mitotic bookmarking by transcription factors.
chromatin interactions with super-resolution live-cell imaging. Curr. Opin. Cell Biol. 70, eLife 5, e22280 (2016).
18–26 (2021). 83. Larson, D. R. et al. Direct observation of frequency modulated transcription in single cells
49. Bellomy, G. R. & Record, M. T. Jr Stable DNA loops in vivo and in vitro: roles in gene using light activation. eLife 2, e00750 (2013).
regulation at a distance and in biophysical characterization of DNA. Prog. Nucl. Acids 84. Mazza, D., Abernathy, A., Golob, N., Morisaki, T. & McNally, J. G. A benchmark for
Res. Mol. Biol. 39, 81–128 (1990). chromatin binding measurements in live cells. Nucleic Acids Res. 40, e119 (2012).
50. Krämer, H., Amouyal, M., Nordheim, A. & Müller-Hill, B. DNA supercoiling changes the 85. Suter, D. M. et al. Mammalian genes are transcribed with widely different bursting
spacing requirement of two lac operators for DNA loop formation with lac repressor. kinetics. Science 332, 472–474 (2011).
EMBO J. 7, 547–556 (1988). 86. McNally, J. G., Muller, W. G., Walker, D., Wolford, R. & Hager, G. L. The glucocorticoid
51. Knight, J. D., Li, R. & Botchan, M. The activation domain of the bovine papillomavirus E2 receptor: rapid exchange with regulatory sites in living cells. Science 287, 1262–1265
protein mediates association of DNA-bound dimers to form DNA loops. Proc. Natl Acad. (2000).
Sci. USA 88, 3204–3208 (1991). 87. Zhang, Q., Shi, H. & Zhang, Z. A dynamic kissing model for enhancer–promoter
52. Ptashne, M. & Gann, A. Transcriptional activation by recruitment. Nature 386, 569–577 communication on the surface of transcriptional condensate. Preprint at bioRxiv
(1997). https://doi.org/10.1101/2022.03.03.482814 (2022).
53. Kyrchanova, O. & Georgiev, P. Mechanisms of enhancer–promoter interactions in higher 88. Baek, I., Friedman, L. J., Gelles, J. & Buratowski, S. Single-molecule studies reveal
eukaryotes. Int. J. Mol. Sci. 22, 671 (2021). branched pathways for activator-dependent assembly of RNA polymerase II pre-initiation
54. Vazquez, J., Muller, M., Pirrotta, V. & Sedat, J. W. The Mcp element mediates stable complexes. Mol. Cell 81, 3576–3588 (2021).
long-range chromosome–chromosome interactions in Drosophila. Mol. Biol. Cell 17, 89. Thomas, H. F. et al. Temporal dissection of an enhancer cluster reveals distinct temporal
2158–2165 (2006). and functional contributions of individual elements. Mol. Cell 81, 969–982 (2021).
55. Merika, M., Williams, A. J., Chen, G., Collins, T. & Thanos, D. Recruitment of CBP/p300 by 90. Hou, C., Zhao, H., Tanimoto, K. & Dean, A. CTCF-dependent enhancer-blocking by
the IFNβ enhanceosome is required for synergistic activation of transcription. Mol. Cell 1, alternative chromatin loop formation. Proc. Natl Acad. Sci. USA 105, 20398–20403
277–287 (1998). (2008).
56. Petrenko, N., Jin, Y., Wong, K. H. & Struhl, K. Mediator undergoes a compositional change 91. Andersson, R. & Sandelin, A. Determinants of enhancer and promoter activities of
during transcriptional activation. Mol. Cell 64, 443–454 (2016). regulatory elements. Nat. Rev. Genet. 21, 71–87 (2020).
57. El Khattabi, L. et al. A pliable Mediator acts as a functional rather than an architectural 92. Buckley, M. S. & Lis, J. T. Imaging RNA polymerase II transcription sites in living cells.
bridge between promoters and enhancers. Cell 178, 1145–1158 (2019). Curr. Opin. Genet. Dev. 25, 126–130 (2014).
58. Du, M. et al. Direct observation of a condensate effect on super-enhancer controlled 93. Kubo, N. et al. Promoter-proximal CTCF binding promotes distal enhancer-dependent
gene bursting. Cell 187, 1–14 (2024). gene activation. Nat. Struct. Mol. Biol. 28, 152–161 (2021).
59. Lambert, É., Puwakdandawa, K., Tao, Y. F. & Robert, F. From structure to molecular 94. Gibbons, M. D. et al. Enhancer-mediated formation of nuclear transcription initiation
condensates: emerging mechanisms for mediator function. FEBS J. 90, 286–309 domains. Int. J. Mol. Sci. 23, 9290 (2022).
(2023). 95. Reiter, F., Wienerroither, S. & Stark, A. Combinatorial function of transcription factors and
60. Shrinivas, K. et al. Enhancer features that drive formation of transcriptional condensates. cofactors. Curr. Opin. Genet. Dev. 43, 73–81 (2017).
Mol. Cell 75, 549–561 (2019). 96. Shlyueva, D., Stampfel, G. & Stark, A. Transcriptional enhancers: from properties to
61. Li, J. et al. Single-molecule nanoscopy elucidates RNA polymerase II transcription at genome-wide predictions. Nat. Rev. Genet. 15, 272–286 (2014).
single genes in live cells. Cell 178, 491–506 (2019). 97. Narita, T. et al. Enhancers are activated by p300/CBP activity-dependent PIC assembly,
62. Boija, A. et al. Transcription factors activate genes through the phase-separation capacity RNAPII recruitment, and pause release. Mol. Cell 81, 2166–2182 (2021).
of their activation domains. Cell 175, 1842–1855 (2018). 98. Hsu, E., Zemke, N. R. & Berk, A. J. Promoter-specific changes in initiation, elongation,
63. Lu, H. et al. Phase-separation mechanism for C-terminal hyperphosphorylation of RNA and homeostasis of histone H3 acetylation during CBP/p300 inhibition. eLife 10, e63512
polymerase II. Nature 558, 318–323 (2018). (2021).
Nature Reviews Molecular Cell Biology | Volume 25 | July 2024 | 574–591 588
