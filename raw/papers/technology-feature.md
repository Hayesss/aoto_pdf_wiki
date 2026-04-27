---
source_path: /mnt/c/Users/Administrator/Zotero/storage/ZDAMQXUT/Marx - 2025 - Taking control with RNA.pdf
ingested: 2026-04-23
sha256: df647baaa5e969aa
---

Technology feature
https://doi.org/10.1038/s41592-025-02596-4
Taking control with RNA
Check for updates
As they study the emerging roles of RNA in disease and homeostasis, some scientists use
RNA editing to direct precise RNA changes that shape cellular events.
By Vivien Marx
Since he started his lab nearly 15 years and academic labs explore RNA-editing is ever-changing, for instance, because of
ago, Stanford University geneticist approaches both for rare genetic disorders environmental influences or developmental
and RNA biologist Jin Billy Li has been and for complex ones such as neurodegen- stages.
exploring an endogenous process erative diseases. A big challenge in the field, An RNA molecule contains the ribonucleo-
in metazoan cells called RNA edit- in both applied and basic research, she says, tide bases adenine, cytosine, guanine and ura-
ing, along with ways to harness it to target and is how to best identify RNA editing sites. cil in a sequence set by the DNA template that
manipulate RNAs inside human cells. Other the RNA is transcribed from. When the RNA in
researchers work on this, too, to learn more RNA roles cells is modified — or edited — in certain ways,
about the role of RNA editing and how that RNA seized the global limelight when a modi- this can cause dysfunction, such as neurode-
process can recode and diversify proteins in fied RNA was used in the vaccine against generative and autoimmune diseases. Cells
ways that do not involve changes to DNA1–5. the virus SARS-CoV-2 that caused a global also edit their own RNA to maintain healthy
There were barely any empty seats in the pandemic. Separately, RNAs are harnessed homeostasis. So, RNA offers a plethora of roles
room during the session on RNA editing at the as guide RNA constructs in the gene-editing to explore.
2024 American Society of Human Genetics technology CRISPR. But long before COVID- RNA editing is part of the innate immune
annual meeting. Li, one of the presenters, is 19 and CRISPR, RNA intrigued researchers reaction to cellular invaders, such as viruses.
glad to see interest in this area rising. “Frankly, as the go-between between the genome and Sensing mechanisms govern how cells distin-
I think the level of interest should be much proteins and also because it fulfills many guish between problematic RNAs to attack
higher than the current status,” he says. The gene-regulatory roles in a variety of organ- and ‘self-RNAs’ to leave be. Brenda Bass of the
field is still ramping up, and “we’re at a very, isms. RNA leads a dynamic, often transient, University of Utah showed how cells distin-
very early stage.” life — it travels within the cell and can have guish between their own double-stranded
What contributes to the current interest, varied 3D structures as the single strand folds RNA (dsRNA) and viral dsRNA, which the
says University of California, Los Angeles RNA upon itself. innate immune system pounces on. “It looked
and computational biologist Xinshu Grace As an assessment by the US National Acad- like it was being unwound, but it was actually
Xiao, who co-organized the session, is that emies of Sciences, Engineering, and Medi- being edited,” says Carl Walkley from the Hud-
unlike DNA-based editing, RNA editing is tran- cine notes6, each gene gives rise to dozens, son Institute of Medical Research in Clayton,
sient and thus has a lower risk of permanent sometimes thousands, of RNA molecules, and Australia, an RNA biologist who also calls
off-target effects. Those would be changes at “importantly, these RNA molecules are also himself an ‘accidental immunologist’. Over
sites other than the one planned. subject to biological processes that chemi- time, especially as RNA sequencing (RNA-seq)
In her view, RNA-editing research is at an cally alter, or modify, their sequence.” Each cell has advanced, RNA editing has grown easier
exciting juncture, with therapeutics devel- in an organism has a distinct set of modified to study, he says. The general approach is to
opment moving rapidly as companies RNA molecules, and this epitranscriptome compare the RNA sequencing transcripts,
nature methods
Volume 22 | February 2025 | 226–230 | 226
ERUTANREGNIRPS
,SPILLIHP
.T
:TIDERC
Technology feature
or RNA-seq reads, to the human reference
genome and to distinguish RNA edits from
other types of changes such as single nucleo-
tide variants.
Editing RNA, writing RNA
The adenosine deaminase acting on RNA
(ADAR) family of enzymes are specific to
dsRNA and are found in humans and other
mammals. These endogenous enzymes cata-
lyze deamination of the base adenosine to ino-
sine, which is read by the cell’s machinery as
guanine. In dsRNA, adenine pairs with uracil,
but the A-to-I-change leads adenine to be read
as if it were paired with guanine.
“The great appeal of the endogenous RNA
editing machinery: it can be hijacked to fix
erroneous RNA without manipulating the
genome,” says Christoph Dieterich, a com-
putational biologist at the University of Hei-
delberg. “Other solutions may work, too, but
seem more complex or sophisticated.”
To study the effect of RNA changes, scien-
tists can choose different approaches. They
can target an RNA segment using CRISPR–
The Walkley lab determined that the endogenous enzyme ADAR1 edits dsRNA such that the
Cas and a guide RNA. Or, they can harness
innate immune system no longer targets it.
endogenous trans-splicing, which is when
cells remove introns from RNA precursors
and exons are spliced together. One can strive shares with Jonathan Gootenberg, is called transcriptome and protein function at will,
to replace mutated exons and fix different ‘Programmable RNA Editing & Cleavage for as it relates to disease, will be huge, he says.
mutations. Insertion, Substitution, and Erasure’ (PRECISE)7.
In his mind, says Li, trans-splicing isn’t quite It’s a way to write RNA of an arbitrary length Computed RNA
classic RNA editing. And, he says, CRISPR and sequence into existing pre-mRNAs via In her group’s work on autism8, Xiao and her
involves the use of an exogenous protein that 5′ or 3′ trans-splicing. team found that RNA editing is less frequent
can activate the immune system. He thinks The fact that protein-free trans-splicing for genes that have roles in neuronal function
more highly of RNA-editing methods that use doesn’t require exogenous proteins makes it and that have been connected to autism risk.
the cell’s own machinery and enzymes. easier to deliver and reduces its immunogenic- She sees much interest in how RNA editing may
ity, says Abudayyeh. “We can package these contribute to fine-tuning neuronal processes
This approach could RNA ‘surgeons’ into vectors for long-term edit- and the molecular basis of neurodevelopmen-
ing in a wide range of tissues,” he says. This is a tal disorders such as autism.
“potentially enable us to
way to potentially treat diseases that are chal- In that autism project and others, “we
make any edit we want,
lenging to address with current gene-editing applied stringent thresholds to minimize false
large or small, opening methods, such as triplet repeat disorders. “It’s positives in identifying RNA editing sites,”
up the possibility of true an incredibly promising area of research, and she says. The software package REDItools is
I believe it represents the next frontier in RNA often used for this, she says. She and her lab
‘RNA writing’,” says Omar
editing technology,” he says. has also developed L-GIREMI9 for analyzing
Abudayyeh. Certainly, says Walkley, who collaborates long-read sequencing data, based on their
with Li on some projects, RNA editing is over- earlier short-read tool, GIREMI.
shadowed by CRISPR–Cas9-based editing, There is no one computational pipeline with
Harvard Medical School researcher Omar which has seen enormous uptake across the which scientists profile RNA-editing sites, says
Abudayyeh finds protein-free trans-splicing biomedical community. Clinical approval Xiao. “I think the most important aspect is to
fascinating because, he says, it’s essentially of CRISPR-based therapies strengthens its improve read alignment procedures and apply
RNA surgery. “We can replace entire exons or reputation. stringent filters to remove likely false positives,”
even whole genes by using specially designed What “will quickly push the field forward,” she says. In her view, “in the future, standard-
RNA molecules,” he says. This approach could says Walkley, is when clinical trial results ized pipelines and benchmarks are needed to
“potentially enable us to make any edit we want, about RNA editing accumulate and positive improve reproducibility across studies.”
large or small, opening up the possibility of true results continue to emerge in studies using What draws him to RNA editing, says Winston
‘RNA writing’.” The method, developed in the RNA editing with endogenous enzymes. Cuddleston, a postdoctoral fellow in the
Abudayyeh–Gootenberg lab, which Abudayyeh Having the option to transiently recode the Raj lab at the Icahn School of Medicine at
nature methods
Volume 22 | February 2025 | 226–230 | 227
HCRAESER
LACIDEM
FO
ETUTITSNI
NOSDUH
,BAL
YELKLAW
:TIDERC
Technology feature
are highly edited, they align poorly; there
might be 10 alignment errors in a 150-base-pair
read, says Walkley. Computational software
is designed to ditch these sites as unmapped
reads, which removes them from further anal-
ysis. To keep hunting, he and his team deploy
what they have nicknamed “dumpster diving,”
which is foraging through the unaligned read
pool to find RNA-editing sites.
A useful tool, says Walkley, that helps with
this hunt is RNAEditingIndexer. The tool11,
developed by Erez Levanon and colleagues at
Bar Ilan University in Ramat-Gan in Israel and
colleagues at Tel Aviv University, calculates
the Alu Editing Index, the weighted average
of observed editing levels over all adenosines.
Says Walkley, it delivers an editing level for a
given sample and it’s “really useful for looking
at editing levels across samples.” To detect
hyper-editing in RNA-seq datasets and to
improve alignment and avoid mismatches,
Levanon and colleagues transform the
RNA-seq data into a three-letter alphabet, in
RNA editing is transient and, compared to DNA-based editing, it’s less likely to cause permanent place of the four-letter alphabet normally used
off-target effects, says UCLA RNA and computational biologist Xinshu Grace Xiao, shown here with to represent bases.
members of her lab. Clockwise from top left: Jae Hoon Bahn; Xinshu Grace Xiao, Thuy Linh Nguyen; Levanon says that what can make detec-
Armen Khanbabaei, Ting Fu, Carlos Gonzalez-Figueroa. tion of editing events tricky is that editing
levels are typically quite low, and that’s why
“unique tools need to be further developed.”
Mount Sinai in New York, is that findings in Says Cuddleston, the overwhelming majority Another tool the Walkley lab uses frequently
human genetics are showing how deficient of SNPs that GWAS identify, sit in non-coding is JACUSA12, developed by Dieterich and col-
RNA editing underlies a substantial por- regions of the genome. He and others work leagues. Its design, says Dieterich, takes into
tion of disease risk for autoimmune and to tease apart the connections between reg- account errors that can happen when sequence
inflammatory diseases. Given that chronic ulation of gene expression, RNA editing and analysis software ‘calls’ bases. JACUSA runs on
inflammation is a key factor in many serious splicing. Among the next steps are to work out any modern desktop or laptop.
diseases, “this hypothesis has broad applica- the molecular consequences that connect the Short-read sequencing limits the extent
bility,” he says, both for understanding dis- observed associations with disease. to which one can find RNA-editing sites, says
ease biology and for developing therapies. Cuddleston works on BigBrain, a project Dieterich. “Long-read sequencing together
Genome-wide association studies (GWAS) focused on the human brain in which the team with JACUSA resolves problematic corner
reveal variants that indicate genetic risk. But applies statistical power to datasets in order cases where hyper-editing occurs,” he says.
finding the molecular mechanisms that drive to resolve how gene expression is regulated
such disease-related variants is challeng- through splicing and RNA editing. From over Pushing forward
ing. Quantitative trait locus (QTL) mapping 4,600 healthy individuals as well as persons with A number of companies have started up in
helps. That’s a statistical method one can use various types of brain disorders, they have more the RNA-editing therapeutics space. Li and
to map variants with molecular phenotypes than 10,000 RNA-seq and genotype datasets. University of Göttingen researcher Thorsten
such as gene expression and splicing when Their analysis, he hopes, could reveal mecha- Stafforst co-founded the RNA-editing com-
studying the genetic underpinnings of com- nisms that connect GWAS loci to neurodegen- pany AIRNA. Other companies include Korro
plex traits. But it does not map all variants. erative diseases and psychiatric disorders. Bio, ProQR Therapeutics and many others. In
QTL mapping has come into play to more a clinical trial involving RNA editing in people
tightly link phenotypes and genotypes RNA-editing research is at with α-1-antitrypsin (AAT) deficiency, Wave
related to RNA editing. Li and colleagues Life Sciences recently announced that after
an exciting juncture, says
applied QTLs to RNA editing. They identi- the treatment, two people with the condition
Xinshu Grace Xiao.
fied and characterized over 30,000 genetic had regained the ability to produce functional
variants — cis-RNA-editing QTLs or edQTLs, AAT, the protein they had lacked.
which are variants correlated with the editing Wave harnesses an endogenous enzyme
levels of a nearby RNA-editing site — across When hunting for RNA-editing sites, not all called ADAR1, says Walkley, who is not involved
49 human tissues and found these sites map of the mismatches one finds are truly sites of with the company. In his view, the result sig-
to regions associated with autoimmune and RNA editing — they might be SNPs or sequenc- nals that this approach is safe in humans and
immune-mediated conditions10. ing errors, among other things. When regions efficacious, which could provide a big push
nature methods
Volume 22 | February 2025 | 226–230 | 228
ALCU
,BAL
OAIX
,IEABABNAHK
.A
:TIDERC
Technology feature
out, the cytosol contains MDA5, a sensor that
AGTT G G A A C C A A A A G G T T T TA G T TGA T T T T A A ATCGCAAGC T T C C A A T T T T A A C C T T T T A A G G A A T T G G T T TTGCAGTGGTTATT GGACTTTATGGAA detects dsRNA16. “If we knocked down MDA5,
RNA-seq reads GACAAGTTGTGATTA AGCCGGGTCATTACTAGATGTGCTGTTGC GGACTTTATGGAA the cells were protected,” says Walkley.
GACAAGTTGTGATTA AGCCGGGTCATTACT TTGCAGTGATTATT
Whole-genome AATTGACAAGTTAT TTAATCGCAAGC TCATTACTTAGATGT TTGCAGTGGTTATTGAACTTTATGGAA This work from the Walkley lab, says Xiao,
sequence A A G AT T T T G G A A C C A A A A G G T T T T A A T T GATTAATCACA A A G G C C C C G A G A G A T T C C A A T T T T A A C C T TT A A G G A A T TA G T T G G C C T T G G T T T T G G C C AGTGATTATTAA GA A A A C C T T T T T T A A T T G G G G A A A A “was a landmark piece in the field.” ADAR1
Reference AATTGACAAATTATGATTAATCACAAGCCAAATCATTACTTAGATATGCTGTTACAGTGATTATTAAAACTTTATGGAA
genome essentially allows tolerance of cellular dsRNA.
“It changes the structure of the RNA to stop it
With RNA-seq data, finding A-to-I RNA editing involves aligning RNA-seq reads to the being perceived as an immunogenic RNA in
reference and distinguishing A-to-G mismatches that are RNA-editing sites (white) from the cytoplasm,” says Walkley.
single-nucleotide variants (gray). Alignment gets challenging as the number of RNA-editing As they dug into this, the team initially
sites increases, but computational tools help with this task. lacked a cell line to work with, but they found
that immortalized mouse bone marrow cells —
myeloid cells — activated this pathway. And
for both basic, preclinical and translational involvement in immune regulation,” says they developed an animal model for this
applications and drive uptake and testing of Levanon. RNA editing is often studied in the ADAR1–MDA5 loop, an ADAR1-deficient
the methods and targets. “This will lead to new brain but, he says, several recent publications mutant mouse called E861A. Over time, more
knowledge but also refine the applications have shown that loss of RNA editing can cause findings have emerged about the effects of
where this might be useful,” he says. inflammation and the death of beta cells in the ADAR1 loss, he says, and consensus has grown
The promise of this trial in a small number of pancreas, leading to type 1 diabetes. about the way ADAR1 edits dsRNA to pre-
patients is likely to radiate into the field, says There are three endogenous ADAR proteins. vent MDA5 activation. Newer work indicates
University of California, San Diego researcher One, ADAR3, has regulatory roles but is cata- that this mechanism might enhance cancer
Prashant Mali. Beyond therapeutics, RNA edit- lytically inactive and not involved in endog- immunotherapy.
ing “can be used also for modulating protein enous RNA editing. Most research efforts Much about the mechanisms still needs to
function or protein interactions where occa- have focused on ADAR1, which is expressed be worked out, but it’s likely, says Walkley, that
sionally only transient changes are desired,” he throughout the body and which has two cells have a cellular pool of RNA that “normally
says. The useful applications include turning isoforms, and ADAR2, which is expressed sits below the threshold.” When a virus or
on a protein’s active site or inhibiting an onco- mainly in the brain and central nervous sys- other immunogenic factor comes onto the
genic interaction. “ADARs are having impact tem and has one isoform. One ADAR1 isoform, scene, the balance shifts and triggers a reac-
beyond RNA editing primarily given the way ADAR1p150, is found mainly in the cytoplasm, tion. In autoimmune conditions, this balance
they modulate the innate immune response,” and studies are revealing that it acts as an is disrupted. “ADAR is the safeguard,” says Li.
he says. ADARs mainly edit in non-coding RNA innate immune checkpoint, says Li. In particu- The mechanism is similar to the well-known
regions, but they do also edit coding regions lar, if not edited by ADARp150, cellular long cGAS–STING pathway that activates innate
in a highly specific fashion. dsRNAs, which are often located in noncod- immunity, which involves the DNA-sensing
As Levanon and colleagues point out14, vari- ing regions, would activate MDA5, which is an receptor cyclic GMP–AMP synthase (cGAS)
ous site-directed RNA-editing methods are innate immune sensor. and its downstream signaling effector stimula-
being developed that use ADAR’s catalytic tor of interferon genes (STING).
activity to perform RNA engineering. One can Having the option to What motivated him to focus on ADAR
use an RNA oligonucleotide to build a dsRNA after his postdoctoral fellowship in the lab
transiently recode the
that guides an ADAR to edit a target adenosine. of George Church, says Li, was the dramatic
transcriptome and protein
They note that “a major challenge in this field effect of ADAR loss. ADAR1-deficient mice die
is achieving high on-target editing efficiency.” function at will as it relates in the womb, and ADAR2-deficient mice have
Evolution can guide researchers in how to disease will be huge, says seizures and die shortly after birth.
to engineer ADARs with greater efficiency. Abudayyeh sees much promise in oligo-
Carl Walkley.
Levanon and his colleagues have found that based ADAR editing. These small RNA mole-
the mallard duck’s ADAR is “an exceptionally cules can guide natural ADAR enzymes to make
potent A-to-I editor,” much more active than specific edits in RNA. What makes this so excit-
the human one. This may be because the duck As Walkley says, with CRISPR-based editing, ing to him is that these oligos are relatively easy
has evolved a higher core body temperature14. one cuts the target and destroys the RNA, and to deliver into cells and tissues, which opens up
To achieve more programmable A-to-I RNA with RNA interference, small interfering RNA an array of therapeutic options. “We’re already
editing that does not require co-delivery (siRNA) is used to block an RNA — “whereas seeing very promising results in vivo, and even
of any exogenous proteins, Mali and col- ADAR is really changing the function of the in humans, demonstrating the high efficiency
leagues at Shape Therapeutics, a company protein.” Early studies on ADARs, particularly of this approach,“ he says. Another major trend
he co-founded, have developed15 circular ADAR2, looked into RNA editing and neuro- is the ongoing development of sophisticated
ADAR-recruiting guide RNAs (cadRNAs), transmitters, he says, and RNA editing in the computational tools.
which they see as a good way to bring ADARs brain has been intensely studied. He and his Unlike DNA editing, says Abudayyeh, RNA
to chosen RNA sites in vivo. team found that loss of ADAR1 led to what editing is transient. Treating diseases without
“RNA editing is interesting not only from looked like an antiviral response from the making permanent changes to the genome is a
a technological development perspective innate immune system, including produc- huge advantage, especially as an understand-
but also due to its endogenous activity and tion of interferon. As he and his team worked ing of diseases evolves. Such a level of control
nature methods
Volume 22 | February 2025 | 226–230 | 229
NOTSELDDUC
.H
MAILLIW
FO
YSETRUOC
,31
.FER
MORF
DETPADA
:TIDERC
Technology feature
RNA-guided CRISPR-based RNA targeting, Vivien Marx
which has advantages for efficiency and speci- Nature Methods.
ficity,” says Abudayyeh. Delivery has been an e-mail: v.marx@us.nature.com
issue with CRISPR-based systems given the
need to package multiple components, includ- Published online: 4 February 2025
ing the Cas enzyme and guide RNAs. He thinks
highly of efforts at HuidaGene Therapeutics, References
which has developed a way to package all 1. Bass, B. L. Annu. Rev. Biochem. 71, 817–846
CRISPR components into a single AAV vec- (2002).
2. Nishikura, K. Nat. Rev. Mol. Cell Biol. 17, 83–96
tor that he sees as “a game-changer for in vivo
(2016).
delivery.” 3. Walkley, C. R. & Li, J. B. Genome Biol. 18, 205 (2017).
In the lab, Li and his group use CRISPR-based 4. Eisenberg, E. & Levanon, E. Y. Nat. Rev. Genet. 19,
473–490 (2018).
DNA editing more than RNA-based editing 5. Picardi, E. & Pesole, G. RNA Editing Methods and
with ADAR methods. The emerging studies Protocols (Springer Science + Business Media, 2021).
on ADAR-based RNA editing make him hope- 6. National Academies of Sciences, Engineering, and
Medicine. Charting a Future for Sequencing RNA and Its
ful about the field’s future related to harness- Modifications: A New Era for Biology and Medicine
ing RNA biology for RNA editing and sensing (The National Academies Press, 2024).
to treat common autoimmune diseases. The 7. Schmitt-Ulms, C. et al. Preprint at biorXiv https://www.
biorxiv.org/content/10.1101/2024.01.31.578223v1
RNA connection to common diseases such as (2024).
He is drawn to RNA editing, says Winston autoimmune conditions and complex diseases 8. Tran, S. S. et al. Nat. Neurosci. 22, 25–36 (2019).
9. Liu, Z. et al. Genome Biol. 24, 171 (2023).
Cuddleston, because human genetics matters for basic and applied research, too.
10. Li, Q. et al. Nature 608, 569–577 (2022).
studies increasingly reveal that deficient As a tool, ADAR-based RNA editing does not 11. Roth, S. H., Levanon, E. Y. & Eisenberg, E. Nat. Methods
RNA editing can lead to autoimmune and provide 100% editing efficiency, but “there’s 16, 1131–1138 (2019).
12. Piechotta, M., Wyler, E., Ohler, U., Landthaler, M. &
inflammatory diseases. almost no off-targets,” says Li. With this new Dieterich, C. BMC Bioinformat. 18, 7 (2017).
modality, “we all harness a human endo- 13. Cuddleston, W. H. Adenosine-to-Inosine RNA Editing in
genous enzyme to do the job, which is not what the Brain: Developmental Dynamics, Cellular Specificity,
and Cis-Genetic Regulation. PhD thesis 31558117, Icahn
and flexibility is hard to achieve with other CRISPR does.” In terms of getting attention in
School of Medicine at Mount Sinai (2024).
gene-editing approaches, he says. the research community, however, “ADAR is 14. Avram-Shperling, A. et al. PLoS Genet https://doi.org/
“While there’s a lot of justifiable excite- a loser,” says Li. “We’re the underdog.” But he 10.1371/journal.pgen.1010661 (2023).
15. Katrekar, D. et al. Nat. Biotechnol. 40, 938–945
ment around ADAR-based editing, I’m par- and others believe that this underdog status
(2022).
ticularly enthusiastic about the potential of will change. 16. Liddicoat, B. Science 349, 1115–1120 (2015).
nature methods
Volume 22 | February 2025 | 226–230 | 230
IANIS
TNUOM
TA
ENICIDEM
FO
LOOHCS
NHACI
:TIDERC
