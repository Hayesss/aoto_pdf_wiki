---
source_path: /mnt/c/Users/Administrator/Zotero/storage/ZDP6V9UA/Choi 等 - 2018 - How Messenger RNA and Nascent Chain Sequences Regulate Translation Elongation.pdf
ingested: 2026-04-23
sha256: 5b871d3a348c7dfa
---

HHS Public Access
Author manuscript
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Published in final edited form as:
Annu Rev Biochem. 2018 June 20; 87: 421–449. doi:10.1146/annurev-biochem-060815-014818.
How mRNA and nascent chain sequences regulate translation
elongation
Junhong Choi1,2, Rosslyn Grosely1, Arjun Prabhakar1,3, Christopher P. Lapointe1, Jinfan
Wang1, and Joseph D. Puglisi1,*
1Department of Structural Biology, Stanford University School of Medicine, Stanford, CA
94305-5126, USA
2Department of Applied Physics, Stanford University, Stanford, CA 94305-4090, USA
3Program in Biophysics, Stanford University, Stanford, CA 94305, USA
Abstract
Translation elongation is a highly coordinated, multistep, multi-factor process that ensures
accurate and efficient addition of amino acids to a growing nascent-peptide encoded in the
sequence of translated mRNA. While translation elongation is heavily regulated by external
factors, there are clear evidences that mRNA and nascent-peptide sequences control elongation
dynamics, determining both sequence and structure of synthesized proteins. Advances in methods
have driven experiments that revealed the basic mechanisms of elongation as well as the
mechanisms of regulation by mRNA and nascent-peptide sequences. In this review, we highlight
how mRNA and nascent-peptide elements manipulate the translation machinery to alter the
dynamics and pathway of elongation.
Keywords
Protein synthesis; Ribosome; Recoding; Translation control; mRNA; Nascent-peptide chain
1. Introduction
Translation is the end-point of genetic information transfer, where the nucleotide sequence
of the messenger RNA (mRNA) dictates the sequence and structure of the nascent protein.
The mechanism of protein synthesis is conserved across the domains of life and is driven by
the ribosome, a two-subunit RNA-protein machine. Thus, fundamental insights into how the
ribosome and the broader translation machinery function have been and will be crucial to
understand gene expression. During translation, ribosomes assemble at the start site marked
by a set of three consecutive nucleotides (a “codon”), adds one amino acid encoded by the
next codon (“decodes”), moves to the next non-overlapping codon (“translocates”), and
repeats the decoding and translocation steps until a stop codon reaches the decoding center
of the ribosome. Repeats of decoding and translocation events are referred to as the
*Corresponding Author: Joseph D. Puglisi, puglisi@stanford.edu; Tel: 650-723-9151.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 2
elongation phase of translation, where the nascent peptide is elongated by amino acids to
build a functional protein.
Our view of translation elongation has evolved over the past decades. In a simplistic model,
decoding and translocation events are metrically repeated to produce a nascent protein
faithful to the codon sequence within the mRNA. Yet, this model insufficiently accounted
for numerous instances where mRNA sequence fails to predict the sequence of the resulting
protein. Studies of these special cases of elongation further revealed that local elongation
dynamics are influenced by the surrounding mRNA sequences, which create competing
elongation pathways that may alter the definition of individual codons. Re-definition of
codons due to dynamic interactions with neighboring mRNA elements are collectively
referred to as ‘recoding’ (1). Recoding is pervasive throughout the domains of life and is
especially enriched in viruses. Thus, the static and deterministic view of elongation must be
adjusted to include the statistical and dynamic process of recoding. A dynamic view of
translation is poised to integrate recent developments in other relevant fields of biology, such
as the emerging field of epitranscriptomics, where mRNA can be chemically modified to
alter translation.
An enriched genetic code emerges after accounting for the dynamic nature of translation.
Various stretches of nucleotide sequences within the mRNA (“mRNA elements”) regulate
the rhythm of its own translation elongation, which in turn dictate the protein structure and
function. mRNA elements may cooperatively interact with the translation machinery and
alter protein synthesis in a programmed manner. For example, mRNA structures within the
coding region have been implicated in recruiting translation factors to aid alternative
decoding or disrupt translocation to enhance recoding phenomena (2, 3). In addition, the
nature of the newly-synthesized protein (“nascent-peptide elements”) also affects translation,
which adds yet another layer of control (4, 5). Nascent-peptide elements together with the
mRNA elements can alter translocation or decoding dynamics during recoding (6, 7). This
review aims to provide a framework for how various mRNA and nascent-peptide elements
affect the dynamics of protein synthesis.
Our richer view of dynamic translation has been driven by improved biochemical, genetic,
structural, biophysical and computational methods. We will first discuss the technological
developments that have led to our current model of translation elongation. We will then
review how known mRNA and nascent-peptide elements perturb the dynamics of translation
elongation both in decoding and in translocation. Finally, we will discuss how mRNA and
nascent-peptide elements work cooperatively to define the decoding pathway in specific
cases of recoding.
2. Current methods to study dynamics of translation elongation
The molecular mechanism of translation elongation involves various dynamic structural
rearrangements and their coupled chemical reactions. Over the last fifty years, numerous
structural, biophysical and biochemical tools have been developed to observe these different
aspects of translation. Integrating data from various methods, a detailed molecular
mechanism of translation elongation cycle has been constructed.
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 3
2.1. Structural methods
Structural methods continue to be fundamental in delineating the molecular basis of
translation. X-ray crystallography has provided high-resolution views of translational
components, including ribosomes. NMR spectroscopy is used to determine structural
dynamics of ribosomal domains (8) and nascent protein chains (9), and recently whole
ribosomes using solid state methods (10–13), but is hindered by fundamental limitations in
solution for large (>500 kDa) systems. Recent advances in cryogenic electron microscopy
(cryoEM) have yielded much excitement in the field of translation by providing high-
resolution information about translational intermediates and larger complexes that have been
previously inaccessible by other structural methods.
X-ray crystallography exposed the first atomic-resolution structures of the translation
complex in various functional states. The high resolution (2–3.5Å) of ribosomal
crystallography arises from the constructive interference of scattered x-rays generated by a
regular ordering of biomolecules within a crystal lattice (14), which creates strong x-ray
diffraction patterns. The diffraction patterns are used to derive 3-dimensional electron
densities and, with molecular modeling, the structures of biomolecules are determined. X-
ray crystallography has been used to ascertain dozens of high-resolution structures of both
bacterial and eukaryotic translation complexes in various functional states. Techniques for
crystallization have advanced to allow ligands such as mRNA, tRNA and various translation
factors to be stably bound to the ribosome during or after crystallization (14). These
structures have revolutionized our understanding of translation, and provide a molecular
blueprint for subsequent engineering of translational components (14). However, high-
resolution is achieved by molecular ordering, thus eliminating intrinsic macromolecular
heterogeneity. Packing of translational complexes within a crystal lattice may induce non-
biological contacts or prevent crystallization of larger assemblies. X-ray crystallography also
proves to be difficult in solving unstable intermediates of biological processes that are too
transient to be captured and ordered during crystallization.
CryoEM avoids many of pitfalls of x-ray crystallography: sample heterogeneity is well
tolerated, ribosomes can be prepared in a wide-range of near-physiological conditions prior
to imaging, and ribosome complexes, which are embedded in vitreous ice rather than forced
into a crystal lattice, retain biological contacts. These factors coupled with recent advances
in cryoEM hardware and software have made cryoEM a powerful method for ribosome
structural studies, achieving a near-atomic resolution of intermediate states of translation
(15–17). The ensemble of structures in a sample represents the most populated, stable
intermediates along the reaction pathway. Similar to x-ray crystallography, cryoEM does not
provide dynamic information, but different structural classes can be ordered post-hoc based
on structural similarity (17). Time-resolved cryoEM techniques that uses microfluidic chips
and environmental chambers for sample preparation rather than the standard sample
preparation, which includes mixing, pipetting onto the grid, and plunge-freezing, can be
used to capture sub-second intermediates (18, 19). The combination of cryoEM with time-
resolved methods will be a strong driver of future structural work on translation.
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 4
2.2. Bulk kinetics
The static views of molecular architecture provided by the structural methods require a
temporal axis. Bulk kinetics (also referred to as ensemble kinetics) based on stopped-flow or
quench-flow approaches allow for the determination of rates of chemical reactions with high
(millisecond to second) temporal resolution. In a typical bulk kinetics experimental scheme,
two solutions are rapidly mixed for a set short period of time, and a fluorescence signal
(stopped-flow) or reaction quenching and product concentration (quench-flow) is measured
as a function of time. A reaction must be initiated such that all reactants begin their chemical
journey simultaneously. However, during multistep or repetitive processes, a bulk collection
of molecules can rapidly desynchronize, obfuscating the presence of intermediate states. The
usual detection method for quench-flow involves measuring radio-labeled chemicals such as
an amino acid or GTP in the reaction quenched at different time points (20). Unlike many
chemical transformations, structural changes may be complex and reversible, requiring real-
time measurements not accessible using the quench-flow approach. In the stopped-flow
apparatus, conformational changes during a reaction can be measured via fluorescence or
light-scattering changes in real time (21). These kinetic measurements can be fit to reaction
mechanism model from which the kinetic parameters for the biochemical reactions can be
extrapolated. Measuring kinetics of multi-step reactions requires careful formulation of
kinetic models, which involves fitting multiple parameters for each reaction step to limited
experimental time-points.
Recent advances in the bulk kinetics methods have resolved rate constants and processivity
factors for multi-step chemical reactions, such as penta-peptide formations (22, 23).
Measuring kinetics of multi-step reactions requires careful formulation of kinetic models,
which involves fitting multiple parameters for each reaction step to limited experimental
time-points. This has been done either by global fitting of multiple parameters (22) or by
deriving necessary kinetic reactions to model the process (23). Tracking changes of
elongation kinetics during the translation of multiple codons is a crucial feature in studying
different mRNA and nascent-peptide elements during translation, where the kinetic effect
may occur over multiple cycles of elongation.
2.3. Single-molecule methods
Single-molecule methods probe the dynamics of translation due to their ability to detect and
sort structural and compositional heterogeneity and observe multiple parallel pathways.
Using relatively simple surface functionalization methods, individual biomolecules can be
immobilized on an optically transparent surface for prolonged tracking. Single-molecule
method provides a tracking of translation over multiple codons without complications
arising from complex kinetic models, which is extremely useful in studying mRNA and
nascent peptide elements. Improvements over the last two decades in camera and dye
technologies coupled to advances in image analysis methods have led to the explosion of
single-molecule fluorescence microscopy methods, allowing detection of temporal changes
in composition and conformation of single biomolecules during translation (24–30). The
development of optical and magnetic trapping technologies has enabled direct measurement
of forces and mechanical stability of molecular complexes (31). Combination of
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 5
fluorescence and force methods will be a powerful tool to study translation, but is still
technically challenging (32).
Single-molecule fluorescence methods applied to translation led to the identification of key
intrinsic dynamic features of the ribosome and its ligands. To track the composition of
translational complexes, fluorophores are covalently attached to tRNAs, translation factors,
and ribosome, through numerous methods (26). Observing conformational changes requires
pairs of conjugated fluorophores to be proximally located within a typical dynamic range of
20–80 Å to observe single-molecule Förster resonance energy transfer (smFRET) between
the two or more dyes. Based on the efficiency of FRET, the distance changes between the
dye-labeling sites can be detected. Interpreting single-molecule fluorescence data requires
specific care to avoid artifacts arising from the experimental setup, which is well out-lined in
the classic review by the Ha group (33). A combination of multiple smFRET-pairs and direct
labeling of translational factors has been used to correlate conformational and compositional
changes during translation in real time (34–36).
2.4. Ribosome profiling (RiboSeq)
Novel DNA and RNA sequencing-based techniques have revolutionized biological
measurement. Ribosome profiling (RiboSeq) was specifically developed to study
translational activity over the entire transcriptome (37–39). The method utilizes the ability of
the ribosome to protect actively translated portions of mRNA from RNase degradation,
thereby defining, with nucleotide resolution, the position of the ribosome on that mRNA by
sequencing the ribosome protected segments (RPS) of mRNA. These data are compared
with sequencing data on the entire transcriptome in parallel, to discriminate transcriptional
control effects from observed translational control effects. By using the number of
sequencing reads and individual mRNA expression levels as standards, RiboSeq exposes
global translational dynamics with a single-base resolution.
Notably, RiboSeq is highly sensitive in detecting unexpected and alternative potential
protein products synthesized by translating previously unannotated coding regions. Further,
subsets of ribosomes can be purified based on their location within a cell or interaction with
another factor, revealing different translational profiles within the same cell (40). However,
each step in the sample preparation workflow can introduce experimental biases or artifacts.
Antibiotic treatments prior to harvesting can bias against rare codons, and lead to artificial
accumulation of reads at initiation sites (41). The experimental procedure used to generate
the deep-sequencing library can also introduce bias (42). Despite such pitfalls, RiboSeq can
uncover much about the translational dynamics from the whole-organism to the level of
specific cell types (43). Such sequencing-based approaches will continue to have a large
impact on analysis of genome-wide biophysics during translation and other processes.
3. General overview of translation
The ribosome spatially and temporally coordinates molecular interactions during translation,
which can be organized into four phases of initiation, elongation, termination, and recycling.
During initiation, the small (30S in bacteria, 40S in eukaryotes; referred to as 30S) and large
(50S in bacteria, 60S in eukaryotes; referred to as 50S) ribosomal subunits assemble at the
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 6
start codon to begin protein synthesis via elongation. Elongation ends when the ribosome
reaches a stop codon, whereby a protein factor for termination is recruited to release the
synthesized nascent polypeptide from the translation complex. The post-termination
complex is then disassembled immediately during recycling. While the initiation,
termination, and recycling phases of translation have been shown to be heavily regulated to
control the quality and abundance of nascent proteins synthesized from translation (44–49),
this review will focus on presenting kinetic and structural schematics of each elongation
cycle, where its regulation may lead to different structures and functions of nascent proteins.
Mechanisms of how mRNA and nascent-peptide elements regulate protein synthesis will be
discussed in the context of schematics presented here.
3.1. Elongation cycle: Decoding
During each elongation cycle, the conformation and composition of the translational
complex evolve temporally through several structures (14, 16) (Figure 1). Kinetic parameters
for each structural transition are well tuned to provide both processivity and fidelity, which
is achieved through proofreading steps that monitor the correct codon-anticodon pairing (50,
51). The elongation cycle begins with decoding, where the cognate tRNA is accommodated
into the aminoacyl-acceptor tRNA site (A site) for the peptidyl-transfer reaction (14, 16, 20,
52, 53) with the peptidyl-tRNA site (P site) bound peptidyl-tRNA. During the elongation
cycle, tRNAs assume various hybrid conformation within the ribosome, such as A/P state,
where the first letter denotes its contact to the 30S, and the second letter denotes its contact
to the 50S.
Results from different methods have been essential to understand the process of initial tRNA
selection (Figure 2). Bulk kinetics were crucial in constructing early models of decoding
(20, 52, 53), which are now supported by observations made using other methods such as
cryoEM (16, 54) and single-molecule fluorescence microscopy (24). Collectively, these
studies have revealed that decoding begins when aminoacyl-tRNA (aa-tRNA) samples the T
site of the ribosome (Figure 1; (i) Decoding: Initial Selection) as a ternary complex (TC)
with a GTP molecule and an elongation factor (EF-Tu in bacteria, eEF1A in eukaryotes;
referred to as EF-Tu here), which increases the affinity of tRNA to the ribosome (55). The
anticodon of the sampling tRNA initially does not base pair with the A-site presented codon
(16, 54), but the tRNA dynamically deforms to form codon-anticodon helix, placing the
tRNA in the A*/T state (14). Dynamic formation of the codon-anticodon helix stabilizes
tRNA TC binding to the ribosome (20, 24, 52, 53). This is energetically favored for the
cognate pairing, which serves to discriminate the non-cognate and near-cognate species
kinetically before tRNA TC dissociates from the T site (20, 24, 52, 53). Structural methods
such as NMR (56) and x-ray crystallography (57, 58) have identified that the correct
formation of the codon-anticodon helix leads to activation of the universally conserved
monitoring bases (A1492, A1493 and G530 of 16S rRNA within the 30S ribosomal subunit),
which dynamically flip toward the codon-anticodon helix and form multiple hydrogen bonds
with the 2’-OH and other conserved chemical groups of the correctly formed helix. The
proper interaction among monitoring bases and the codon-anticodon helix positions tRNA
TC into the A/T state, providing optimal stereochemistry for the hydrolysis of GTP within
the TC through interaction with the sarcin-ricin loop in the 50S ribosomal subunit (58).
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 7
Recent computational work has shown that the energy landscape of initial selection leading
to GTP-hydrolysis is markedly different between cognate and near-cognate tRNA bound
complexes, where selectivity for the cognate substrate is amplified in multiple steps (20, 52,
53, 59). The irreversible GTP-hydrolysis marks the end of the initial selection phase of
decoding, and subjects the tRNA in the A/T state to additional proofreading steps.
Clever experimental designs using the existing techniques have further elucidated the
pathways of translational fidelity through proofreading steps (Figure 1; (ii) Decoding:
Proofreading). The proofreading mechanism uses the same stability of codon-anticodon
interaction and its interaction with monitoring bases to discriminate kinetically against non-
cognate tRNA species. Recently, bulk kinetics experiments using engineered tRNAs have
suggested that upon GTP-hydrolysis, the on-pathway event of EF-Tu•GDP dissociation
kinetically competes with the dissociation of EF-Tu•GDP•aa-tRNA, which results in a tRNA
rejection pathway (60). Here, the correct stereochemistry among the monitoring bases and
the codon-anticodon helix favors the EF-Tu•GDP dissociation pathway over the EF-
Tu•GDP•aa-tRNA rejection pathway (60, 61), serving as the first stage of proofreading,
although the involved structural mechanism has not been elucidated. Upon EF-Tu•GDP
dissociation, aa-tRNA is subjected to the second stage of proofreading, where the on-
pathway event of the aa-tRNA accommodation to the A site competes with the dissociation
of aa-tRNA from the A/T-state. The A-site accommodation places the amino acid moiety of
the aa-tRNA in a correct stereochemistry in the peptidyl transferase center (PTC) of the
large ribosomal subunit, which then catalyzes a rapid transfer of the peptide from the P-site
tRNA to the amino acid (62).
3.2. Elongation cycle: Translocation
The peptidyl-transfer reaction after tRNA accommodation induces multiple large-scale
conformational changes in the translational complex (63), creating a correct substrate for
translocation (Figure 1; (iii) Translocation) (35). Transfer of the nascent peptide to the A-
site tRNA allows a movement of the acceptor stems of the P-site and A-site tRNAs into the
exit (E) and P sites of the large subunit, respectively (64). These new tRNA conformations
are defined as hybrid states, denoted as P/E and A/P states. In addition to the tRNA
movements, peptide bond formation is also followed by a rapid counterclockwise rotation of
30S subunit by 3–10° with respect to 50S subunit, resulting in a rotated-state conformation
(65, 66). The rotated-state conformation is the cognate substrate of translocation, catalyzed
by an elongation factor (EF-G in bacteria and eEF2 in eukaryotes; referred to as EF-G here).
EF-G interacts with the ribosome to stabilize the tRNAs in the hybrid state (21, 67–70).
Ribosome binding activates the GTPase of EF-G for GTP hydrolysis (71), leading to its
conformational change catalyzing translocation (67–69).
Translocation is by definition dynamic and many of the intermediate states involved are
transient. As such, dynamic methods—bulk kinetics, single-molecule approaches, multiple
structures by cryoEM, computational studies—have been essential to outline the mechanism
of translocation (21, 34, 72–75). Using molecular dynamics simulations, different
translocation intermediate structures from cryoEM have been temporally ordered to build a
structural pathway of translocation (76). Based on these results, combinations of multiple
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 8
single-molecule fluorescence signals or fluorescence signal with the measured kinetics from
bulk methods have produced detailed models of translocation (21, 34, 74, 75). During
translocation, the head of the 30S subunit swivels counterclockwise with respect to the body
by 18–21° followed by a rapid relaxation back, coupled to disengagement of the mRNA and
tRNAs from the decoding center (72, 73, 77). These changes are also accompanied by a
clockwise rotation of the 30S subunit relative to 50S subunit that places the ribosome back
into the non-rotated intersubunit conformation (35, 78, 79). EF-G then dissociates from the
non-rotated post-translocation complex, with tRNAs occupying the P and E sites (80).
After translocation, the dissociation kinetics of deacylated tRNA from the E site determines
the structural pathway following translocation. The post-translocation complex is in the non-
rotated conformation with a vacant A site (80), where tRNAs can sample and decode the
next codon (25, 81). The decoding process is not allosterically affected by the presence or
the absence of the E-site tRNA (25, 81–83). However, upon peptidyl-transfer reaction,
deacylated tRNA needs to be moved to the P/E hybrid state for translocation. Thus, E-site
occupancy, perhaps due to slow E-site tRNA dissociation kinetics, would preclude adoption
of the tRNA hybrid conformation until the E-site tRNA dissociates (36). The E-site tRNA
dissociation kinetics are sensitive to intracellular ionic strength (81, 84), temperature and
tRNA identity (36, 85), and possibly modulated by additional elongation factors, such as
eEF3 in fungi (86, 87) or its bacterial homolog, EF4. More work is required to understand
the detailed role of the E-site in elongation.
4. mRNA elements altering translation elongation
Beyond their intrinsic capacity to encode proteins, mRNAs possess numerous regulatory
elements that impact the rate of protein synthesis at multiple stages. We will focus on the
increasingly prominent role the mRNA plays in controlling the rate of elongation. We will
cover how i) modifications to a single nucleotide, ii) codon usage, and iii) larger regulatory
elements within the mRNA alter translation elongation.
4.1. Nucleotide modifications
A large number of chemical modifications – 163 distinct modifications cataloged to date
(88) – have been detected in RNAs. In particular, the last several years have yielded a vast
expansion of data that document “RNA epigenetics” (89) and the mRNA “epitranscriptome”
(90) – the dynamic co- or post-transcriptional addition of modifications to the nucleotides
within mRNAs. The epitranscriptome field has moved rapidly, and several excellent reviews
have recently been published that highlights recent discoveries around mRNA modifications
and the techniques used to identify them (91–94). Modified nucleotides within mRNA have
been shown to affect all aspects of RNA biology— mRNA splicing, export, localization, and
stability, as well as multiple stages of translation, including elongation (91, 93).
Chemical modifications that occur on nucleotides within the mRNA coding region can be
divided into three broad categories (Figure 3). First, hydrogen-bonding groups on the
nucleotide base can be modified, thereby altering its ability to base pair with incoming
tRNA. Second, the nucleotide base can be modified outside the Watson-Crick edge of the
base, without alteration to its hydrogen-bonding ability. Third, the ribose backbone can be
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 9
modified, which may affect the tertiary structure of mRNA or RNA-specific recognition
mechanisms. Each type of modification is expected to induce different effects during
decoding, thereby suggesting new ways to regulate the dynamics of translation elongation.
In this section, we focus on three known mRNA modifications – methylation of adenosine at
the N6 position (N6-methyladenosine, m6A), the isomerization of uracil (pseudouridine, Ψ),
and ribose methylation at the 2’ position (2′-O-methylation).
m6A is the most common internal mRNA modification, where one of two N6 hydrogens that
participates in the base-pairing is modified to a methyl group (Figure 3). Tens of thousands
of m6A sites have been defined in thousands of mRNAs from human, mouse, yeast, plant,
and bacterial models (95, 96). Substitution of adenosine nucleotides (A) to m6A within the
open-reading frame of mRNAs inhibits translation elongation directly (97). While m6A and
U form canonical base pairs, they are thermodynamically less stable in duplexes than
canonical A-U base pairs (98). While m6A base-pairs with the corresponding U in the tRNA
anti-codon in the ribosomal A site, m6A at any of the three positions in a codon disrupts
decoding, with the greatest kinetic inhibition at the first nucleotide (99). These data suggest
that translation kinetics for particular mRNAs in bacteria and eukaryotes could be modulated
by dynamic m6A (de)modifications. While less common in coding regions (100, 101), N1-
methyladenosine (m1A) also substantially inhibits tRNA selection and accommodation
(102), possibly by preventing codon-anticodon interactions.
The isomerization of uridine to Ψ is the most abundant internal RNA modification, which
rearranges atoms outside the Watson-Crick edge (Figure 3). In the ribosome, Ψ nucleotides
are present in the peptidyl transferase and decoding centers, where they enhance translation
efficiency and fidelity (103, 104). In mRNA, stop codons (UGA, UAA or UAG) with Ψ as
the first nucleotide suppress translation termination and allow read-through of premature
termination codons in vitro and in vivo (105, 106). Structural analyses of bacterial 30S
ribosomal subunits revealed that the presence of a Ψ-A Watson-Crick base pair at the first
position of a codon-anticodon interaction distorts the conformation of the decoding center
(105), allowing typically prohibited non-cognate tRNAs to decode the modified stop codon
via the Hoogsteen base pairing. Yet, among hundreds to thousands of Ψ found within the
coding regions of eukaryotic mRNAs (107, 108), modifications of stop codons were
extremely rare. How sense codons are affected by the presence of Ψ remains unclear and is
an exciting avenue for future studies.
Lastly, 2′-O-methylation is an emerging mRNA modification in eukaryotes. Chemically, by
replacing the reactive 2’-OH group with an unreactive O-methyl group, 2′-O-methylation
decreases the susceptibility of the nucleotide to nucleolytic attack (i.e. hydrolysis) and
stabilizes RNA helices (109). The 2’-OH of RNA is a critical contact point in interactions
that are specific for RNA over DNA. Thus, 2′-O-methylation may have substantial impact
on protein-RNA, RNA-RNA, and DNA-RNA interactions. Thousands of 2′-O-methylation
sites were recently identified within human mRNAs, predominately enriched in the coding
region (110). Intriguingly, 2′-O-methylation stalls translation elongation at the modified
nucleotide during decoding similar to m6A, with the greatest impact when the codon is 2′-
O-methylated at position 2 (in press) (97). A primary cause of the stall is the disruption of
the conserved rRNA monitoring bases, which interact with the mRNA 2′-O-moieties for
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 10
decoding. The distortion of the decoding site leads to both increased rejection of the cognate
tRNAs during the initial tRNA selection and subsequent proofreading phase of translation
elongation, manifesting as a long stall prior to a successful decoding event. While the
functional role of such a pause has not yet uncovered, both m6A and 2′-O-methylation in
mRNA showcase how the rate of translation elongation can be widely tuned by chemical
modifications to mRNA.
4.2. Codon choice alters decoding kinetics and the pathway of elongation
Each amino acid is encoded by up to six synonymous codons and their usage frequencies
vary. In many instances, codon usage is optimally balanced with the abundance of the
corresponding aa-tRNAs that recognize them (111, 112). Indeed, inclusion of non-optimal
codons inhibits elongation and destabilizes the mRNA (113, 114). The abundance of aa-
tRNAs is modulated during cell proliferation and differentiation (115), and in development
(116), cancer (117, 118), and other human diseases (119), which together appears to play an
important role in regulating the rate of protein synthesis. Thus, seemingly silent DNA
mutations that do not impact the encoded amino acid may result in a switch from an optimal
to non-optimal codon (or vice versa), altering the abundance or function of the protein.
Synonymous codon usage has a direct impact on the kinetics of decoding and translocation.
The rate of aa-tRNA binding is dictated by both the codon present in the A site and its
abundance in a cell (120). The usage of rare codons with low concentrations of
corresponding aa-tRNAs thus leads to elongation pauses during the decoding phase. While
the slow decoding rate induced by rare codons may lead to decreased mRNA stability in
cells (113, 114), it may also allow domains of the nascent proteins to co-translationally fold
properly; rare codons are especially enriched at the end of protein secondary structures
(121). The decoding rate of the A-site codon may be further affected by the codon present in
the P site, as permutations of synonymous codons at two adjacent positions contribute to the
overall rate of elongation (122). In tandem, the dissociation kinetics of deacylated tRNA
from the E site may differ across synonymous codons. Slow E-site tRNA dissociation retains
the ribosome in a conformation that is refractory to translocation, where its lifetime depends
on the rate of tRNA dissociation (36). Dissociation kinetics of the E-site tRNA are
dependent on the tRNA species (36, 85), and may differ among synonymous codons. We
speculate that, together with tRNA abundance, the differential usage of synonymous codons
in the A, P and E site of the ribosome may lead to non-uniform rates of elongation across an
mRNA, which awaits full elucidation.
4.3. Stable RNA structures within mRNA
Information encoded in mRNAs occurs in a three-dimensional context. mRNAs can
dynamically fold into complex secondary and tertiary structures that may serve as regulatory
elements via recruiting factors that recognize RNA structures, disrupting translocation
during translation, or modulating more complex translational events on the ribosome.
mRNA structure can be a ligand for translation factors. The incorporation of the 21st amino-
acid, selenocysteine, relies on an RNA-binding protein that specifically recognizes an
mRNA stem-loop. A specialized elongation factor (SelB in bacteria, eEFSec-SBP2 in
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 11
eukaryotes; referred to as SelB) complexed with selenocystenyl-tRNA (Sec-tRNASec) and
GTP binds to an mRNA stem-loop – the selenocysteine insertion sequence (SECIS) (54).
This interaction facilitates timely delivery of Sec-tRNASec ternary complex to the ribosomal
A site, resulting in the recoding of the UGA stop codon. SECIS is an excellent example of
how an mRNA structure and its interaction with an RNA-binding protein can alter decoding.
mRNA structures need to be unfolded prior to decoding by the ribosome. During translation,
the single-stranded mRNA is threaded through the 5–6 nucleotide-long entrance channel that
is composed of three ribosomal proteins (S3, S4 and S5 in bacteria) (123, 124). The
relatively narrow width of the mRNA entrance channel prohibits RNA duplexes from
entering. Therefore, structured mRNA elements need to be unfolded approximately two
codons before it reaches the A site for decoding (125), possibly during translocation step.
The unfolding of mRNA structure requires free energy, likely powered by EF-G, which
hydrolyzes GTP to catalyze translocation. The proposed model of ribosome translocation on
an mRNA involves conformational change of EF-G, which primes the mRNA-tRNA
complex for translocation (75, 126). However, the mechanism of translocation through an
mRNA hairpin is still debated; while the force generated during the EF-G conformational
change may be used directly for helicase activity (75), it has also been suggested that
translocation can capture the breathing of the base of mRNA structure (31). Regardless of its
helicase mechanism, mRNA structures have been known to slow down elongation, and used
to enhance recoding efficiency in many cases (2, 22, 127).
mRNA sequences may base-pair with the rRNA to tether itself to the ribosome. The role of
mRNA-rRNA base-pairing is a key aspect of bacterial translation initiation and integral to
certain recoding phenomena, such as −1/+1 programmed ribosomal frameshifting (128).
However, the mechanism of how mRNA-rRNA base-pairing interactions alters the dynamics
of translation elongation have been debated. Early in the study of translation in bacteria, a
stretch of mRNA sequences named the Shine-Dalgarno sequence (SD-sequence) was
recognized as an important feature of translation initiation, guiding the position of the start
codon on the ribosome by base-pairing with the small ribosomal subunit. Its effect during
elongation surfaced during the study of programmed ribosomal frameshifting, where it has
been hypothesized to “push” or “pull” mRNA to aid frameshifting in both directions. Yet,
recent reports have shown that the effect of the SD-sequence on translation elongation
kinetics may be minimal (129). Therefore, the mechanism of how the SD-sequence and
similar mRNA-rRNA interactions affects translation and enhances recoding phenomena
needs further elucidation.
5. Control of Translation Elongation by Nascent-Peptide Elements
In addition to mRNA elements-mediated regulation, the amino acid sequence of the nascent
protein chain also regulates translation (4, 5). Amino acid side-chain geometries and
chemistries influence substrate positioning within the PTC (5). In the context of the nascent
peptide, amino acids can interact with the ribosomal exit tunnel (a ~100 Å-long conduit that
bridges the PTC and the solvent environment), resulting in changes in the rate of translation
elongation (4). In this section, we will discuss the mechanisms of amino acid sequence-
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 12
induced ribosomal stalling and its basis in regulating molecular mechanisms such as
ribosomal secretion signal and antibiotic resistance.
5.1. Proline-mediated translation stall
The rate of peptidyl transfer for each codon varies depending on how efficient a particular
amino acid is as a P-site peptidyl donor and an A-site peptidyl acceptor (130). Proline is the
most striking example, since it is the only N-alkylated and cyclic proteinogenic amino acid.
As the A-site peptidyl acceptor, the transfer reaction to proline is much slower compared
with that of other amino acids like phenylalanine. The higher pKa of the α-N group brought
about by the alkylation slows down the rate-limiting peptidyl transfer reaction to an A-site
proline (131, 132). Recent ribosomal crystal structures with Pro-tRNA analog in the A site
revealed unfavorable positioning of the substrate in the PTC (133), which likely further
contributes to the slow peptidyl transfer rate of proline. The unfavorable positioning of
proline may also explain its poor activity as the peptidyl donor in the ribosomal P site (134).
The low reactivity of proline in both A and P sites results in an amplified inhibition of
translating consecutive proline (135, 136).
Proline residues can therefore potentially regulate the rate of protein synthesis. The stalling
caused by stretches of proline residues can be alleviated by a special elongation factor (EF-P
in bacteria and eIF5A in eukaryotes; referred to as EF-P here) (134, 137, 138), by decreasing
the activation energy for formation of the next peptide bond via a favorable entropy change
(139). Ribosome profiling results revealed significant ribosomal stalling events at the poly-
Pro regions in mRNAs when EF-P was knocked out (140), reflecting the direct effect of EF-
P/poly-Pro on mRNA translation. The recent cryoEM structure of EF-P bound to the stalled
ribosome suggested that EF-P stabilizes conformation of the nascent peptide and tRNAs to
allow efficient translation of poly-Pro regions (141). Combined with cellular levels of EF-P,
stretches of proline residues directly affect the expression levels of the corresponding
proteins, especially those related in the synthesis of key components of the translation
machinery; this may in turn act as an indirect regulator for the translation of other mRNAs
or global protein synthesis (142, 143).
5.2. Interaction within the nascent peptide exit tunnel affects translation elongation
Unlike proline residues, which only require interaction with the PTC to induce translational
stalling, there are longer nascent peptide sequences that can arrest translating ribosomes
through specific interactions with the constricted region of the ribosomal exit tunnel (4). One
of the most extensively studied examples of nascent chain-induced stalling is secM/secA
ribosomal secretion signaling pathway in bacteria (144). Expression of the SecA protein is
coupled to the cellular protein secretion pathway via a negative feedback mechanism, where
inefficiencies in the secretion pathway involving SecA induce increased translation of the
secA gene. The mechanism of such modulation involves the translation of a secretory
protein SecM, which acts to monitor the efficiency of protein export. SecM includes a
nascent-peptide sequence that induces a stall in translation, which is relieved when the
SecM-stalled ribosomes are docked to the Sec translocon on the cell membrane via the
SecA-mediated protein secretion pathway. The secA initiation site is located in the 3’-UTR
of secM and, under normal conditions, is structurally sequestered away from ribosomal
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 13
binding (Figure 4). The prolonged translation stalling on SecM re-arranges mRNA structures
to expose the initiation site of the secA gene and thus prompts the synthesis of SecA protein.
Biochemical and genetic studies have identified a 17-aa peptide in SecM,
F150XXXXWIXXXXGIRAGP166 (144), that is sufficient for stalling translating ribosomes
at Gly165 (145). Structural studies by cryoEM showed how interactions between the SecM-
stalling peptide and the ribosomal exit tunnel affect positioning of substrates in the PTC and
slow down the peptidyl transfer reaction between Gly165 and Pro166 (146). Disruption in the
PTC and interaction within the nascent peptide exit tunnel may affect translocation as well
as the peptidyl transfer reaction. Using cryoEM, Zhang et al. captured not only the inactive
PTC state that disfavored the accommodation of the incoming A-site tRNA and peptide
bond formation, but also another state where the translocation was impaired after successful
peptide-bond formation (147). Recent single molecule studies uncovered the real-time
dynamic nature of this stalling phenomenon, which involves prolonged decoding and
translocation at several positions on SecM (148). This work suggests that residues in SecM
interact cooperatively with the ribosome to induce a gradual slow-down of translation
elongation. The gradual slow-down of elongation suggests multiple interactions between the
nascent peptide and the ribosome, which evolve over the course of translating a SecM-
stalling peptide (Figure 4).
Other peptide sequences with moderate effects on ribosomal stalling may be used more
pervasively to regulate biomolecular processes. To date, many translation stalling peptide
sequences have been identified (4). New methods to identify peptide sequences that induce
translational stalling continue to be developed: using bioinformatics, Navon et al. identified
underrepresented short-peptide sequences that indeed stall translation (149). Through
genetic selection, Tanner et al. evolved a novel peptide sequence, FXXYXIWPP, that
impairs peptidyl transfer causing translating ribosomes to stall (150). How different nascent
peptide elements are used to induce perturbation in decoding and/or translocation kinetics in
prokaryotic and eukaryotic elongation still needs further clarification.
5.3. Sequence-context dependent action of antibiotics
Many antibiotics target key functions of translation by interacting with active sites within the
ribosome. Certain classes of antibiotics specifically impede the peptidyl-transfer reaction
(151), whereas others, such as macrolides like erythromycin, bind to the ribosomal exit
tunnel and cause ribosomal stalling and abortive translation (152). Initial studies suggested
that erythromycin acted as a plug in the ribosome exit tunnel blocking the passage of the
nascent peptide. However, recent results indicate that the erythromycin mechanism of action
relies on the interplay between the nascent peptide, the tunnel and the drug itself, where the
susceptibility to drug depends on the nascent peptide sequence (153, 154). Similarly, actions
of different antibiotics such as chloramphenicol and linezolid have also been shown to
depend on the distinctive nascent peptide sequence, leading to stable accommodation events
of incoming tRNA but preventing peptide-bond formation on the stalling site only
(unpublished results) (155). Bound antibiotics likely interact with nascent-peptide residues
to disrupt the PTC, which affects the accommodation dynamics of the next A-site tRNA and
results in abortive translation.
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 14
Translational inhibition is blocked through mechanisms of antibiotic resistance. For
erythromycin, the basis for the regulation of resistance is very similar to the translational
attenuation principle as described above for that of the secM-secA gene regulation. The
activation of the macrolide resistance gene ermC relies on translational stalling on the
upstream ermCL gene to upregulate protein synthesis (156). The ermCL gene harbors a
specific nascent peptide sequence that induces a strong translational arrest in the presence of
the erythromycin (Figure 4) (152, 153, 157). The stalled ribosome induces a rearrangement
of mRNA structures to expose the initiation site of the downstream ermC gene and up-
regulates the expression level of the ErmC methyltransferase (Figure 4) (156). The
translation of ermC confers antibiotic resistance by dimethylation of A2058 of 23S rRNA
(158), which likely disrupts the binding of the erythromycin to the ribosome. Similarly, a
strong chloramphenicol-dependent stall-inducing nascent peptide sequence is present in the
catA86L or cmlAL genes to upregulate expression of the downstream catA86 or cmlA genes
to confer resistance to chloramphenicol (159). A nascent-peptide sequence can also confer
antibiotic resistance for translating individual proteins, where bound antibiotics are evicted
through interactions with the growing nascent chain (153, 160). Although distinct
interactions of the nascent chain, the exit tunnel and the small molecules are employed in
different drug actions, these studies underscore how such interactions can modulate
translation dynamics. Therefore, a dynamic view of translation is necessary to understand
the mechanisms of antibiotics and the development of resistance.
6. Recoding
The existence of multiple mRNA and nascent-peptide elements that affect translation
elongation at various steps highlights the flexibility of the translation machinery to utilize
different signals encoded in the mRNA. Individually, the major effect of mRNA and nascent-
peptide elements is to modulate the rate of translation elongation. However, combinations of
multiple effects may break the linearity of elongation and bifurcate its pathway to produce
two different proteins in a tuned ratio from the same mRNA, referred to as “recoding”
events. Across the domains of life, different genes utilize recoding signals to increase the
density of their genetic information or to regulate the production of a functional protein. In
recoding, the normal elongation pathway competes with the recoded pathway, and
determining the exact branch point of pathways is critical in elucidating the mechanism of
specific recoding phenomenon. Different branching points involved in the various recoding
phenomena are starting to be exposed, occurring either during translocation or decoding
steps, or combination of both in the extreme case (Figure 5).
6.1. The repurposing of translocation for −1 frameshifting
Programmed ribosomal −1 frameshifting (referred to as “−1 frameshifting”) is the best-
studied recoding phenomenon to date. During −1 frameshifting, the open reading frame of
the mRNA contains a programmed “slippery sequence”: A sequence of nucleotides where
translation can resume in the original frame (0-frame) or in another shifted one base in the 5’
direction (−1-frame). Translation of a −1 frameshifting signal thus produces two different
proteins that share the same N-terminal sequence with a fixed stoichiometry. The most well-
known usage of −1 frameshifting is in human immunodeficiency virus (HIV), where a −1
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
Choi et al. Page 15
frameshifting signal is used to produce Gag and Gag-Pol proteins at a pre-determined ratio
(1). Regulating protein expressions through −1 frameshifting enriches information density of
genomes and likely benefits viruses such as HIV, where the fitness of viruses is linked to the
compactness of its genome. New instances of −1 frameshifting are still being discovered in
viruses, bacteria and eukaryotes, and its usage may be much higher than anticipated, perhaps
stimulated by external elements such as RNA-binding proteins (161), microRNAs (162) and
antibiotics (163).
Translation normally requires ribosomes to maintain their original reading frame throughout
elongation. Errors resulting from the spontaneous shifting of the reading frame are
energetically costly, resulting in the production of unwanted proteins that may be harmful to
the cell. The error rate for the spontaneous shifting has been estimated as 10−5 (164, 165),
which is an order of magnitude smaller than the 10−4 rate of missense errors (substitution of
a single amino-acid) (166, 167). Therefore, −1 frameshifting signals that result in 30–70%
efficiency present a controlled way to circumvent an error prevention mechanism utilized
during normal elongation (1–3).
The set of factors involved in −1 frameshifting is continually expanding and includes both
mRNA and nascent-peptide elements, as well as external factors. Among them, the slippery
sequence within the mRNA is essential. They typically conform to a tetrameric or
heptameric sequence (N–NNX–XXZ or X–XXX–XXZ, where N, X and Z denotes a
nucleotide, and a dash denotes separation of codons in the original reading frame) that
allows cognate tRNA pairing in two frames. The heptameric sequence generally yields
higher frameshifting efficiency than that of the tetrameric sequence, indicating that it can
involve up to two tRNAs (168).
However, the slippery sequence alone does not induce highly efficient −1 frameshifting,
usually less than 5% (1–3, 169, 170). Downstream mRNA structures are most often required
for highly efficient −1 frameshifting of up to 50–70% (1–3, 169, 170). The involved
structures are strikingly varied, from a simple stem-loop to a pseudoknot to long-range RNA
folding that span distances of thousands of nucleotide bases within a single mRNA molecule
(1–3). The stability of the RNA structures positively correlates with −1 frameshifting
efficiency (170). Moreover, microRNAs (162) and RNA-binding proteins (161) enhance −1
frameshifting efficiency, very likely by increasing the stability of mRNA structure. In
addition to the stability of the mRNA structure, its position relative to the slippery sequence
also affects −1 frameshifting. Highly-efficient frameshifting systems frequently contain 5–6
nucleotides between the 3’ end of the slippery sequence and the 5’ base of the mRNA
structure. Deviation from this distance in either direction decreases frameshifting efficiency
(127, 169).
The mechanism of −1 frameshifting is emerging from a combination of different methods.
Through studies of individual mRNA structures used in −1 frameshifting, it is clear that they
act to induce a pause during translation elongation. The pause most likely occurs during
translocation (22, 171, 172), requiring multiple EF-G bindings to catalyze translocation on
the slippery sequence coupled with the simultaneous unfolding of the mRNA structure
(Figure 5A). Indeed, the distance of 5–6 nucleotides between the slippery sequence and the
Annu Rev Biochem. Author manuscript; available in PMC 2019 June 26.
Author
Manuscript
Author
Manuscript
Author
Manuscript
Author
Manuscript
