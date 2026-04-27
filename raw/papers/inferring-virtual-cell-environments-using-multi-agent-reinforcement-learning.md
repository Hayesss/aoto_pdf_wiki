---
source_path: /mnt/c/Users/Administrator/Zotero/storage/GNNY8LQJ/Kalafut 等 - Inferring virtual cell environments using multi-agent reinforcement learning.pdf
ingested: 2026-04-23
sha256: 5800c52136f03088
---

bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
Inferring virtual cell environments using multi-agent reinforcement learning
1
Noah Cohen Kalafut1,2, , Chenfeng He1,3, , Jie Sheng1,3, , Pramod Bharadwaj Chandrashekar1,3, ,
2
Jerome Choi1,4, , and Daifeng Wang1,2,3,*,
3
1Waisman Center, University of Wisconsin-Madison, Madison, WI, USA
4
2Department of Computer Sciences, University of Wisconsin-Madison, Madison, WI, USA
5
3Department of Biostatistics and Medical Informatics, University of Wisconsin-Madison, Madison, WI,
6
USA
7
4Department of Population Health Sciences, University of Wisconsin-Madison, Madison, WI, USA
8
*Corresponding Author (daifeng.wang@wisc.edu)
9
1 Abstract
10
Single cells interact continuously to form a cell environment that drives key biological processes. Cells
11
and cell environments are highly dynamic across time and space, fundamentally governed by molecular
12
mechanisms, such as gene expression. Recent sequencing techniques measure single-cell-level gene ex-
13
pression under specific conditions, either temporally or spatially. Using these datasets, emerging works,
14
such as virtual cells, can learn biologically useful representations of individual cells. However, these
15
representations are typically static and overlook the underlying cell environment and its dynamics. To
16
address this, we developed CellTRIP, a multi-agent reinforcement learning method that infers a virtual
17
cell environment to simulate the cell dynamics and interactions underlying given single-cell data. Specif-
18
ically, cells are modeled as individual agents with dynamic interactions, which can be learned through
19
self-attention mechanisms via reinforcementlearning. CellTRIPalso applies noveltruncated rewardboot-
20
strapping and adaptive input rescaling to stabilize training. We can in-silico manipulate any combination
21
of cells and genes in our learned virtual cell environment, predict spatial and/or temporal cell changes,
22
and prioritize corresponding genes at the single-cell level. We applied and benchmarked CellTRIP on
23
various simulated and real gene expression datasets, including recapitulating cellular dynamic processes
24
simulated by gene regulatory networks and stochastic models, imputing spatial organization of mouse
25
cortical cells, predicting developmental gene expression changes after drug treatment in cancer cells, and
26
spatiotemporal reconstruction of Drosophila embryonic development, demonstrating its outperformance
27
and broad applicability. Interactive manipulation of those virtual cell environments, including in-silico
28
perturbation, can prioritize spatial and developmental genes for single-cell-level changes, enabling the
29
generation of new insights into cell dynamics over time and space. CellTRIP is open source as a general
30
tool and available at github.com/daifengwanglab/CellTRIP.
31
2 Introduction
32
Single cells continually interact and establish a cell environment to coordinate many key biological
33
processes, such as development and disease progression. For example, within tissue microenvironments,
34
cells develop along different lineages and migrate to specific regions during maturation of cell types,
35
such as T cell lineages1. Furthermore, gene expression, a key single-cell-level mechanism to determine
36
cellular function, can be controlled by intracellular gene regulation and through intercellular molecular
37
interactions with neighboring cells2,3. These interactions are dynamic, developing the cell environment
38
to drive specific biological processes. These environments are sensitive to small perturbations. Varying
39
conditionscanleadtoheterogeneousfunctionaloutcomes. Forexample,inter-individualvarianceintumor
40
immune microenvironments can dictate responsiveness to chemo-immunotherapy4. Characterizing these
41
environments is critical to understanding a wide range of developmental, pathological, and embryonic
42
processes, among others.
43
Next-generation sequencing techniques enable measurement of genome-wide molecular activities,
44
1
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
including gene expression, especially at the single-cell level5. Many of those datasets can also pro-
45
vide dynamic information, including spatial positioning6 and temporal annotation7,8. Typically, these
46
sequencing-based measurements are limited to one or few time points over the course of a particular
47
biological process. This temporal scarcity challenges a deeper understanding of dynamic interactions
48
within the cell environment governing many biological processes, including developmental trajectories
49
and perturbation outcomes. Some recent single-cell datasets can contain time-dependent information,
50
such as for cell maturity and disease progression. Thus, many trajectory inference methods have been
51
developed to computationally learn dynamic patterns of single cells using these datasets. For example,
52
MOSCOT9 uses optimal transport across multimodalities to recover cell developmental trajectories from
53
time-seriesandspatialdata. OthermethodslikeURD10 andSTREAM11 recovergeneexpressionchanges
54
along cell developmental timepoints. None of these methods, however, focus on modeling underlying
55
dynamic cell-cell interactions and cellular behaviors, and are therefore unable to characterize the cell
56
environment.
57
Reinforcement learning (RL), a machine learning approach for modeling agent-environment interac-
58
tions and discovering optimal strategies through interaction, has been widely applied across many fields,
59
including robotics12,13, DNA and protein sequence design14, and manufacturing15. Broadly speaking,
60
RL seeks to train decision-making agents to optimize a reward function through interaction with a given
61
environment. This optimization is performed through repeated trial-and-error, reinforcing behaviors that
62
lead to positive outcomes. One of the most prevalent and flexible RL approaches is Proximal Policy
63
Optimization (PPO). PPO was developed as an efficient objective function and training procedure that
64
uses several user-adjustable parameters to efficiently reinforce model behaviors that increase a reward
65
value16. RL can also model a typical cellular process. In particular, cells can be represented as agents
66
that interact in an unseen cell environment. For example, reinforcement learning has been applied to
67
modeling cell movement and division and validated related pathways during embryonic development of
68
C elegans17. Some RL-based methods have started to analyze single-cell data, including scRL18, which
69
uses an actor-critic architecture to predict cell fate under disease, development, and gene-knockdown
70
conditions. CNRein19 also uses single-cell data to infer realistic copy number aberrations by inferring a
71
cancer evolutionary model for individual patients. However, neither method models the underlying cell
72
environment or incorporates dynamic information. Despite its potential, RL has not been widely applied
73
to general analysis of emerging large-scale single-cell data, which is readily available and can provide
74
useful dynamic information from the cell environment under many temporal and spatial conditions.
75
To address this, we developed CellTRIP, a multi-agent reinforcement learning method to infer a
76
scalable and interactive virtual cell environment that can be manipulated at the gene or cell level.
77
CellTRIP is able to perform spatial or temporal imputation, predict in-silico perturbation using single-cell
78
data in both time and space domains, and recover missing cell developmental stages. CellTRIP utilizes
79
PPO combined with generalized advantage estimation20, PopArt21, and well-known optimizations22,23.
80
We show that CellTRIP (1) outperforms existing methods for recovering developmental trajectories
81
on simulation data24, (2) imputes spatial transcriptomics data from the mouse cortex25, (3) predicts
82
the effects of gene knockdown on drug perturbation datasets from cancer cell lines7, and (4) recovers
83
spatiotemporalcellorganizationofdevelopmentalstagesandinfersdevelopmentandtissue-specificgenes
84
during Drosophila embryonic and larval development8.
85
3 Methods
86
CellTRIP infers a virtual cell environment from the single-cell data (e.g., gene expression) for spatiotem-
87
poral imputation and perturbation prediction. Given a single-cell dataset, each Cell i has |K| types of
88
measurements, such as gene expression and spatial location, where K is a set of indices representing
89
each type of measurement. Let m⃗ ( i k) ∈ Rn mk represent measured data for Cell i in modality k ∈ K with 90
n
mk
features. We also define the matrix M(k) ∈ Rnc×n mk, where each row is m⃗ (
i
k) over all n
c
cells in the
91
2
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
Figure 1: CellTRIP uses multi-agent reinforcement learning techniques to infer virtual cell environments
from static biological data for spatiotemporal imputation and perturbation prediction. The model learns
to optimally construct environment spaces to maximize data retention from source modalities. Retention
quality and reliability are communicated to the model through environmental rewards, while the model
can interact with the environment by imparting forces on each cell, independently. A residual self-
attention module is utilized cell and neighbor embeddings to determine the velocity changes of each
cell from one timestep to another. After training, the model can be used in various environments for
spatiotemporal imputation, to simulate cell development, or for perturbation prediction.
dataset.
92
CellTRIP consists of three interconnected components that are iteratively updated during learning
93
and inference: The environment space, environmental reward, and residual self-attention policy. In
94
CellTRIP (Figure 1), single cells are represented as independent agents within an environment space.
95
The environment space is a coordinate space of reduced dimensionality, defining cell positions and
96
velocities. Cell positions, velocities, and single-cell data are supplied to the residual self-attention policy,
97
which computes cell actions (i.e., changes in velocity) for all cells simultaneously. Cells use such actions
98
to interact with and navigate through the environment space. CellTRIP agents try to maximize the
99
environmental reward, which increases as the imputation loss inferred from the environment space (cell
100
positions and velocities) decreases. An additional pinning module is utilized to impute or align single-
101
cell modalities, including spatial coordinates. Based on the optimized virtual cell environment, we can
102
perform spatiotemporal imputation and predict perturbation outcomes.
103
3.1 Environment Space
104
The environment space calculates cell positions and velocities, simulating cell state changes over time.
105
Each simulation runs for a user-specified amount of time, 128 seconds by default, with each timestep
106
t representing ∆t seconds of simulation time, defaulting to 0.1s (totaling 1,280 timesteps). During
107
training, the total simulation time is uniformly sampled between 64 and 128 seconds (See Supplementary
108
Section S6). At a particular timestep t, each Cell i has a cell position ⃗x i t ∈ Rn d and cell velocity 109
⃗v
i
t ∈ Rn d, where n
d
is the user-specified dimensionality of the environment space (32 by default). Cell
110
positions and velocities of all given cells may also be represented as matrices Xt,Vt ∈ Rnc×n d, where
111
row i corresponds to ⃗xt or⃗vt, respectively. Aggregating cell positions, velocities, and single-cell data, we
i i 112
get the cell states St = {Xt,Vt}+{M(k) for k ∈ K }. The environment also stores a list of source
sources 113
and target modalities, K ,K ⊆ K, which determine the policy input and predicted modalities,
sources targets 114
respectively (Supplementary Section S5.1). For instance, we can use single-cell gene expression data
115
(source modality) to predict spatial locations (target modality).
116
At each timestep t, the environment space gives a state matrix St to the policy (Section 3.3), which
117
3
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
returns a cell action matrix ∆Vt. The cell velocities and positions are then updated according to the
118
following rules:
119
Vt+1 = Vt +∆t·∆Vt, Xt+1 = Xt +∆t·Vt, (1)
If trained correctly, the cell positions typically converge after a certain number of timesteps, i.e., ∥⃗vt∥
i 2 120
is small. We refer to the converged cell positions as the steady state. For a visual representation of this
121
process, see Supplementary Figure S2.
122
3.2 Environmental Reward
123
The goal of the environmental reward is to maximize the ability of the policy to impute target modalities
124
from the environment space (Supplementary Figure S3). This is accomplished through the combination
125
of three rewards: the pinning reward, velocity penalty, and action penalty. We provide minimal guidance
126
during training to allow the model to infer the inter-cell relationships of the input data, rather than
127
relying on modality-specific prior knowledge.
128
⃗rt = (2·∆t)−1⃗rt +(10·∆t)−1⃗rt +10−3⃗rt . (2)
pinning velocity action
The default coefficients for each reward are shown in Equation 2, but can be tuned by users. Note that
129
the scales of ⃗r and ⃗r are dependent on ∆t. So, their coefficients are divided by ∆t to remove
pinning velocity 130
this dependence.
131
 (cid:13) (cid:13)2−1
(cid:13)ρ(k)(⃗xt)−m⃗ (k),t(cid:13)
(cid:88) (cid:13) i i (cid:13)
⃗rt+1 = ⃗ δt − ⃗ δt+1, δt = −1+10· 2 , (3)
pinning i  |K |·var(M) 
targets
k=Ktargets
Thecentralobjectiveisthepinningreward, whichincreasesasthepolicy-imputedmodalitiesapproach
132
the target modalities. where ρ(k) is the pinning module (Section 3.4.1) for modality k, var(·) is the
133
variance across all matrix values, and δt is the element of ⃗ δt+1 corresponding to Cell i. The result is then
i 134
a weighted sum of the inverted mean squared error (MSE) between the imputed and target modalities.
135
Observe that, as the MSE rises or drops, δt approaches 0 or −1, respectively. Also note that the result
i 136
is invariant to the number of features, ensuring equitable weighting of multiple modalities.
137
(cid:13) (cid:13)
⃗rt+1 = ∥⃗v i t∥ 1 −(cid:13)⃗v i t+1 (cid:13) 1. ⃗rt = n−1 (cid:13) (cid:13)∆⃗vt (cid:13) (cid:13) 2 . (4)
velocity,i n action,i d i 2
d
The velocity penalty is added for stability. This penalty increases with velocity in the environment
138
space, incentivizing slower movement and disincentivizing unbounded exploration.
139
The pinning reward and velocity penalties reflect changes in the pinning MSE and velocity, respec-
140
tively. This leads to the properties ⃗ δ0 −⃗rt = ⃗ δt and ∥⃗v0∥ −⃗n ·rt = ∥⃗vt∥ . The cumulative
pinning i 1 d pinning i 1 141
reward across a whole simulation then reflects the corresponding cumulative change in pinning accuracy
142
and velocity and, crucially, is not dependent on the number of timesteps.
143
Finally, the action penalty is used to incentivize smooth changes in velocity. Erratic movements are
144
more difficult to predict and coordinate between agents.
145
3.3 Residual Self-Attention Policy
146
The residual self-attention policy is the decision-making component of CellTRIP, responsible for evaluat-
147
ing cell states from the environment space and predicting optimal cell actions to iteratively maximize the
148
resultant environmental reward. Policy inference consists of several steps, including cell and neighbor em-
149
bedding, cell summary embedding, and action sampling. The cell and neighbor embeddings encode cell
150
4
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
positions, velocities, and single-cell modalities in one unified representation. The cell summary embed-
151
dings add further environmental context to each cell embedding by computing residual self-attentions
152
between the cell and neighbor embeddings. Finally, cell actions are sampled from the cell summary
153
embeddings to be given to the environment space.
154
During forward computation, for each Cell i, cell positions and velocities (i.e., ⃗xt,⃗vt totaling 2n
i i d 155
features) are concatenated with the corresponding cell information for modalities k ∈ K , resulting
sources 156
in a vector of size n = 2n + (cid:80)Ksourcesn . Cell and neighbor embeddings ⃗at, ⃗ bt ∈ Rne are then
concat d k mk i i 157
computed using multilayer perceptrons (MLPs) of dimension n ×n ×n with a Parametric
concat hidden hidden 158
ReLU (PReLU) activation function between each layer, where n is a user-defined parameter. We
hidden 159
call these MLPs E and E for cell and neighbor encoders, respectively.
a b 160
(cid:16) (cid:17) (cid:16) (cid:17)
⃗at = E (cid:2) ⃗xt,⃗vt (cid:3) ||Ksourcesm⃗ (k) , ⃗ bt = E (cid:2) ⃗xt,⃗vt (cid:3) ||Ksourcesm⃗ (k) , (5)
i a i i k i i b i i k i
where || denotes vector concatenation. CellTRIP contains an additional parameter to generate neighbor
161
embeddings relative to each cell by concatenating⃗at to each neighbor input vector, as in Baker et al.26.
i 162
However, this increases the complexity of the forward computation by a factor of n .
c 163
Sets of cell and neighbor embeddings are then run through a residual self-attention model individually.
164
Inparticular, thecellembeddings(queries)andneighborembeddings(keyandvalue)arelayer-normalized
165
and fed through a multiheaded attention layer. The number of neighbors per cell is user-adjustable and
166
defaults to 1k. The unnormalized cell embeddings are added to the attention output, implementing the
167
residual component. The layer-normalized intermediate output is then fed through an additional residual
168
two-layer MLP of hidden layer sizes 4n × n × 4n with PReLU activation and added to
hidden hidden hidden 169
the unnormalized input to the MLP, generating the cell summary embeddings, ⃗s
i
t ∈ Rn hidden. The cell
170
summary embeddings may also be represented as a matrix St ∈ Rnc×n hidden. CellTRIP contains an option
171
to stack multiple of these blocks in sequence, but the default model only uses one.
172
The cell summary embeddings are fed through PReLU activation and the decider module, an MLP
173
E , with layer sizes n ×2n ×n with intermediate PReLU activations followed by Tanh. The output,
s d d d 174
E (St), determines the final cell actions. The outputs are used as means in normal distributions with
s 175
trainable variance σ for each dimension in the environment space. This is equivalent to the multivariate
176
normal distribution, ∆⃗v i t ∼ N(E s (⃗s i t),diag(σ2)), where diag(σ2) ∈ Rn d ×n d is a diagonal covariance 177
matrix with all nonzero entries σ. Note that, internally, σ is stored in log-form to prevent negative
178
values for σ from backpropagation. The computed cell actions are then applied to the environment
179
space according to Equation 1 to iterate the cell positions and velocities. The model is trained using
180
proximal policy optimization (PPO), simulating multiple environments in parallel and iterating at fixed
181
step intervals until convergence. We additionally utilize novel input scaling techniques derived from
182
PopArt normalization21. For more details concerning model training or the distributed environment, see
183
Supplementary Section S1 and Supplementary Section S6.
184
3.4 Cell Spatiotemporal Imputation and Perturbation Prediction
185
With the trained CellTRIP model, specifically π and ρ(k), we can perform spatiotemporal imputation and
θˆ 186
perturbationprediction. Spatiotemporalimputationcanbeviewedastwomajorcomponents, thosebeing
187
spatialandtemporalimputation. CellTRIPusespinningmodules, ρ(k), toestimatetargetmodalitiesfrom
188
the environment space, Xt (Section 3.4.1). These pinning modules also enable imputation of single-cell
189
spatial coordinates from gene expression data. Temporal imputation can recover intermediate timepoints
190
or stages from developmental data through interpolation in the environment space using the CellTRIP
191
model, with optimal generation of pseudocells. This enables imputation of intermediate developmental
192
stages from embryonic development time-series data. Perturbation prediction can also use the predictive
193
capabilities of CellTRIP to predict perturbation outcomes, including gene expression, and to prioritize
194
genes across dataset conditions. For example, if we define a perturbation function ψ to replace the
195
5
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
expression of gene g with 0, we can prioritize larval developmental genes by anatomical region using
196
time-series Drosophila data.
197
3.4.1 Spatial Imputation
198
CellTRIP relies on pinning modules, ρ(k) to impute from the environment space to M(k) space, for
199
k ∈ K . Each pinning module is an MLP with dimension n ×2n ×n with PReLU activations
targets d d mk 200
between layers, trained concurrently with the policy. Each pinning module uses MSE between the
201
predicted and imputed environment spaces as its loss function.
202
ℓ = ∥M ˆ(k) −M(k)∥2. (6)
pinning,k F
In non-spatial modalities, M ˆ(k) = D(k)(X ), where X is the matrix of environment cell positions at a
e e 203
user-defined timestep (typically 1 through training) in each simulation. When working with spatial data,
4 204
or any data whose primary significance lies in inter-cell distances, we instead solve for a rotation matrix R
205
andtranslationvector⃗τ minimizingtheMSEbetweenρ(k)(X )andM(k), (cid:80)nc∥R×ρ(k)(⃗x )+⃗τ−m⃗ (k)∥2
e i e,i i 206
and set M ˆ(k) = R × ρ(k)(X ) + ⃗τ. For additional details on solving for R and ⃗τ using SVD, see
e 207
Supplementary Section S3.
208
3.4.2 Temporal Imputation
209
We can also use CellTRIP to impute intermediate time points and cell types, even with unmatched
210
cells. If dataset timepoints do not contain matched cells, we can use optimal transport27,28to estimate
211
correspondence between the observed initial and terminal stages in the environment or imputed space.
212
Specifically, we solve
213
Q = argmin⟨Q,C⟩ , s.t. (Q⃗1) = (QT⃗1) = 1, Q ≥ 0. (7)
F i i
Q
where n and n are the numbers of cells in the initial and terminal stages, respectively, and C ∈
c1 c2 214
Rnc1×nc2 is the euclidean distance matrix between the (properly rotated) cells in the two stages. Once we
215
have the transition matrix Q, we compute pseudocells by taking the mean of cells with nonzero entries
216
in each row of Q. Then, we have a 1 : 1 mapping of cells in the initial and terminal stages. In practice,
217
we preempted this process by generating pseudocells using K-means in each stage.
218
Wethenbeginsimulationoftheinitialstagepseudocells. Oncethesteadystateisreached, wereplace
219
the input modalities M(k) for k ∈ K with those of the terminal stage pseudocells. Simulating to
source 220
steady state provides a transition tensor of dimension [timesteps×pseudocells×positions]. We can then
221
manually choose a timestep as an intermediate timepoint. This process is outlined in Figure S1.
222
3.4.3 Perturbation Prediction
223
In general, CellTRIP feature perturbation revolves around modification of M(k),k ∈ K . We notate
sources 224
this modification through a perturbation function ϕ({M(k) for k ∈ K }). Any number of feature
sources 225
perturbation techniques can be applied to CellTRIP, but we primarily focus on feature knockdown.
226
In particular, we define ϕ ,ϕ ,...,ϕ , each replacing the corresponding modal feature in a chosen
1 2 n 227
mk
modality k with 0. In the case of gene expression features, starting from our steady state position and
228
velocity, X0,V0, calculated without perturbation, we can simulate each perturbation function ϕ ,
g g g 229
∆Vt = π ({Xt,Vt}+ϕ ({M(k) for k ∈ K })). (8)
g θˆ g g g sources
6
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
TheendingpositionsattimeT aredenotedXT. CellTRIPalsocontainsadditionalknockdownstrategies,
g 230
which can be found in Supplementary Section S7.1. The transition states between X0 and XT are then
g g 231
computed to quantify the gene effect size and gene trajectory length for each Cell i,
232
T−1
(cid:88)
gene effect size = n−1||⃗x0 −⃗xT ||, gene trajectory length = n−1 ||⃗xt −⃗xt+1||. (9)
i c g,i g,i i c g,i g,i
t=0
We may also compute the gene effect size and gene trajectory length after imputation using the pinning
233
module, if desired. For example, we can calculate gene effect size in environment or gene expression
234
space.
235
4 Results
236
4.1 Recapitulating Cellular Dynamic Processes Simulated by Gene Reg-
237
ulatory Networks and Stochastic Models
238
To showcase the ability of CellTRIP to recover cell state developmental genes and trajectories, we
239
generated 1,500 simulation cells with 2,400 gene and protein expression features each using Dyngen24.
240
The data consists of cells at seven distinct stages in development (Figure 2a). Possible developmental
241
paths bifurcate twice, ending at one of three terminal cell states.
242
We began by examining the per-modality reconstructions from CellTRIP, which were predicted from a
243
common environment space after it reached steady state. Comparing CellTRIP reconstructions to similar
244
methods with the same dimensionality, we observed that CellTRIP has the second lowest MSE of ~221,
245
closely behind scScope at ~211, and the highest label-transfer accuracy (0.248, Figure 2b). We see that
246
celltrajectoriesaredistinctintheCellTRIP-reconstructedUMAPsandmatchtheground-truthsimulation
247
data closely (Figure 2c). In particular, cell state lineages match the ground-truth developmental tree.
248
After accurately reconstructing gene and protein expression modalities, we performed in-silico knock-
249
out of individual TFs per module, finding that we were able to accurately match expected gene effect
250
size trends from the ground truth data (Figure 2d). Specifically, we chose one module from each cell
251
state and used the mean environment space gene effect sizes from the TF knockdowns to generate a
252
heatmap of module downstream effects across trajectories and cell states. We observed greater gene
253
effect sizes in cells at later stages of development. Moreover, the magnitude of the gene effect sizes
254
tended to increase with the lineage distance between cell states. The resultant gene effect size patterns
255
also matched the expected trends from the ground-truth data, i.e., that child cell states were the most
256
affected. Similar patterns are also seen across all modules (Supplementary Figure S5).
257
Looking into module C8 in particular, performing knockdown of all TFs simultaneously caused large
258
expression changes in differentiated cell states (Figure 2e). Interestingly, some terminal cell states were
259
less affected towards the end of their development. Namely, terminal cell states originating from cell
260
state D (i.e., Cell states E and F), itself a child of cell state C, seemingly exhibit gene expression changes
261
of lower magnitude than those with closer lineage to cell state C (i.e., cell state G). Looking at individual
262
TF knockdowns for module C8, we observe the gene effect size increasing as the cells developed further
263
from cell state C, indicating a deviating developmental trajectory caused by TF knockdown. Knockdown
264
of modules corresponding to a terminal state results in the expected isolated effect, as can be seen
265
from the knockdown of modules G2 or F1, consisting of only one TF each (Figure 2f, Supplementary
266
Figure S4).
267
4.2 Imputing Spatial Organization of Mouse Cortical Cells
268
To demonstrate the ability of CellTRIP to impute single-cell spatial coordinates from gene expression,
269
we trained a CellTRIP model on Visium gene expression data from 1,075 spatially-resolved cells from
270
7
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
Figure 2: Gene prioritization and knockdown on simulation data generated from gene regulatory net-
works and stochastic models24. a. Ground-truth developmental module progression (Left) and cell state
developmental tree (Right), shaded by cell state. Red and blue arrows indicate positive and negative reg-
ulatory effects, respectively. b. Label transfer accuracy (x-axis) and pairwise MSE (y-axis) for CellTRIP
and comparable method reconstructions of gene expression, limited to 32 dimensions (See Section S2.1).
c. UMAP of CellTRIP-reconstructed (Top) and ground-truth simulated (bottom) gene expression (Left)
and protein expression (Right), colored by cell trajectory. d. Heatmap of mean CellTRIP-predicted gene
effect sizes in environment space by cell trajectory (x-axis) and module (y-axis). Dots and lines indicate
ground-truth developmental paths from (a), while red outlines indicate expected regions of effect for
module knockdown. e. CellTRIP-predicted gene expression trajectory (Left) and gene effect size (Bot-
tom) under module C8 knockdown and knockdown of constituent transcription factors, respectively (See
Section 3.4.3). f. Panel (e), repeated for module G2.
the adult mouse frontal cortex across six cortical layers29,30. As independent validation, we imputed the
271
spatial coordinates of 4,785 cells from an independent scRNA-seq dataset in the adult mouse frontal
272
cortex25. We also used smFISH data, consisting of 2,360 cells, from the primary visual cortex33,34 to
273
provide additional per-layer reference cell type proportions.
274
We compared several mapping-based spot assignment methods with CellTRIP. We note that Cell-
275
TRIPhasseveralkeydistinctionsfromthesemethods, includingbeingaregressionmodelwhichcomputes
276
spatial coordinates directly from gene expression, rather than choosing from a list of known spot po-
277
sitions. CellTREK30 and Cytospace32 also have additional cell filtering methodologies, with CellTREK
278
predicting 3,899 possible coordinates for 2,347 validation cells and Cytospace predicting assigning ex-
279
actly 1,075 unique validation cells to the 1,075 spatially-resolved training cells. CellTRIP imputed spatial
280
coordinates match the shape of the observed training data, overcoming the main challenge of imputing
281
spatial coordinates directly (Figure 3a). When evaluating cell type distributions by cortical layer, we
282
observe that CellTRIP has comparable performance to all other methods and mimics cell type enrich-
283
ments (Section S2.2) from the reference dataset closely (Figure 3b, Supplementary Figure S6). Among
284
the surveyed methods, CellTRIP layer classifications have the lowest matrix MSE (Section S2.2) for
285
8
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
Figure 3: Single-cell spatial imputation and gene prioritization in the adult mouse frontal cortex. For
computational details, see Section S2.2. a. Reference spatial transcriptomics training data29 from Wei
et al.30 and imputed spatial coordinates of single cells from independent mouse cortical scRNA-seq
data25. We compared CellTRIP with mapping-based spot assignment methods including CellTREK30,
Tangram31, andCytospace32. b. Celltypeenrichment(log transformed)ofinferredreferencesubclasses
2
(left) compared with imputed coordinates from (a) across cortical layers. c. Single-cell layer score
distributions per cell type for methods shown in (a) to assess separability of subclasses by cortical layer,
particularly for excitatory neurons. Significances of distribution differences between inferred adjacent
cortical layers are computed using a one-tailed Mann-Whitney U test and annotated as *: p < 5×10−2,
**: p < 1 × 10−2, ***: p < 1 × 10−3, ****: p < 1 × 10−4. d. Imputed spatial coordinates from
CellTRIP, colored by gene effect sizes after short (.5s) in-silico gene knockdown by CellTRIP. 60 random
genes were chosen for visualization. Plots were sorted using hierarchical clustering of genes by single-cell
effect sizes. e. Number of cells transitioning to (x-axis) and from (y-axis) cortical layers under gene
knockdown by CellTRIP for the two top genes with the highest number of layer transitions, along with
one representative gene for average layer transitions. Knockdown was fully simulated for the top 1,000
genes by effect size. f. Gene set enrichment of top 100 genes by number of transitioning cells.
excitatory cells (CellTRIP 0.042, CellTREK 0.066, Tangram 0.108, Cytospace 0.073, Supplementary
286
Figure S7). CellTRIP outperforms other methods when classifying L5 PT and L6b cell types as layers 5
287
and 6b, respectively. In particular, CellTRIP achieves the highest AUROC on single-layer classifiers for
288
layers L5 and L6b (Supplementary Figure S8). Layer L6b has traditionally been difficult to identify and
289
analyze given its relatively thin width, heterogeneous cell distributions, and lack of agreed-upon marker
290
9
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
genes35. We define a layer score for each reference and imputed single-cell (Section S2.2) and observed
291
that CellTRIP has significantly different (p < 10−4, Mann-Whitney U test) distributions between most
292
excitatory cell types, as well as astrocytes and L2/3, which was only identified by CellTRIP and Tangram
293
(Figure 3c).
294
We then used CellTRIP for in-silico perturbation prediction of gene knockdown and calculated spatial
295
gene effect sizes (Section S2.2) on validation data across all genes (Figure 3d). The distribution of gene
296
effect sizes is heavily right skewed, indicating that many genes have little to no effect on the spatial
297
imputation (Supplementary Figure S9). We then checked cell movement across layers under knockdown
298
for the top 1,000 genes by effect size (Section S2.2). We examine the layer transitions of two such genes
299
with high numbers, Camk2n1 and Tub1a, as well as one with an average number of transitioning cells,
300
Srp9 (Figure 3e). Under CellTRIP-predicted perturbation, both Camk2n1 and Tub1a cause catastrophic
301
layer migration towards L6b and L1, respectively. Knockdown of Camk2n1 impairs maintenance of long-
302
term memory by preventing typical post-retrieval autophosphorylation36. Tub1a also plays a critical,
303
noncompensated role in neuronal saltatory migration. Performing functional enrichment on the top 100
304
genesbygeneeffectsize, weobtainthesignificanttermneuronprojectionmorphogenesis, whichisheavily
305
interrelated with neuronal migration (Figure 3f). interestingly, we see an additional enriched term for
306
long-term memory, which aligns with the prioritization of Camk2n1.
307
4.3 Predicting Developmental Gene Expression Changes After Drug Treat-
308
ment in Cancer Cells
309
Next, we sought to evaluate the accuracy CellTRIP perturbation trajectories, particularly for intermediate
310
timepoints. To do so, we used a dataset consisting of 13,713 cells, 5,992 of which have been treated
311
with trametinib and subsequently measured for gene expression at 3, 6, 12, 24, and 48 hour timepoints.
312
During training, we held out the 24 hour timepoint completely for both control and trametinib.
313
CellTRIP demonstrated superior perturbation prediction from dimethyl sulfoxide (DMSO) control to
314
trametinib at 48 hours for all cell lines. Before benchmarking, we verified that the cell line distributions
315
were similar across observed DMSO and trametinib cells (Supplementary Figure S10a). For CellTRIP
316
and GEARS, we simulated drug perturbation by simulating knockdown on the two main targets of
317
trametinib, MAP2K1 and MAP2K2, whose expressions appeared to decrease monotonically over the
318
courseoftreatment(SupplementaryFigureS10b). Weutilizedthreepostprocessingadjustmentstrategies
319
when evaluating CellTRIP, namely No Adjustment, Steady-State Adjustment, and PCA Adjustment
320
(Section S2.3). We see that PCA-adjusted CellTRIP (MSE = 3.87, Pearson delta = 0.650) outperforms
321
CPA37 (MSE = 5.52, Pearson delta = −0.092) and GEARS38 (MSE = 68.74, Pearson delta = 0.414)
322
in both MSE and Pearson delta (Figure 4a). We note that the comparison methods only predict one
323
perturbation at a time (e.g., control → Tram_48hr) while CellTRIP can evaluate multiple timepoints in
324
one perturbation trajectory.
325
Using the continuous and interactive environment from CellTRIP, we can predict perturbation tra-
326
jectories over long periods of time, and thereby predict multiple timepoints simultaneously. To do so,
327
we first ran the environment to steady state on control cells. Then, we knocked down MAP2K1 and
328
MAP2K2. The knockdown perturbation provided a trajectory from 0 to 48 hours, which we then com-
329
pared to our expectations. Specifically, we compute the Pearson delta between different timepoints of
330
trametinib perturbation to determine the similarity between perturbed states, and, correspondingly, the
331
expected distribution of these timepoints in our simulated trajectory (Figure 4b). We note that the latter
332
four timepoints (6 hours onward) are more similar to each other than the 3 hour timepoint. Additionally,
333
closer timepoints are generally more similar. Performing the same analysis with Pearson delta between
334
perturbation timepoints and CellTRIP timesteps, we see a similar trend to that of the ground truth
335
(Figure 4c). Importantly, peaks of the computed Pearson deltas appear in each perturbation timepoint
336
sequentially, suggesting that the CellTRIP trajectory is nearing each perturbation timepoint in the correct
337
10
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
Figure 4: Gene knockdown perturbation prediction and missing timepoint recovery for trametinib in
cancercells7. a. CellTRIPknockdownpredictionperformanceagainstcomparablemethodsusingPearson
delta (See Section S2.3). b. Pearson delta between recorded timepoints after trametinib perturbation,
using the unperturbed control (DMSO) at 48 hours as a baseline. c. Normalized Pearson delta between
timepoints from (e) and CellTRIP perturbation after knockdown of MAP2K1 and MAP2K2 genes to
the same values as trametinib at 48 hours. Lines indicate the earliest points where the value of a sliding
mean window with size four reaches within leniency of the maximal mean Pearson delta for each row. d.
Maximal Pearson delta of CellTRIP-predicted knockdown for each timepoint of trametinib perturbation.
e. Wasserstein distance (EMD) between observed 12, 24, and 48 hour timepoints after trametinib
perturbation and CellTRIP transition states between 12 and 48 hours. Observed data was limited to
the top 512 principal components. Expected closest timesteps are outlined for each series, as well as a
manually chosen timestep for 24 hours to be used in (d). f. Observed and predicted gene expression for
12, 24, and 48 hour timepoints.
order. CellTRIP is also able to achieve a high Pearson delta of 0.72 at 24 hours, sharing positive results
338
with all but the 3 hour timepoint (Figure 4d).
339
To showcase the continuous perturbation trajectory from CellTRIP, we imputed trametinib-perturbed
340
gene expression at 24 hours, using 12 and 48 hour measurements as referenceo. Following the method-
341
ology in Supplementary Figure S1, we generated 948 pseudocells for the 12 and 48 hour timepoints, 948
342
being the minimum cell count between the two, and estimated pseudocell correspondence between the
343
timepoints using discrete optimal transport. We then ran the environment to steady state on the 12 hour
344
pseudocells before replacing cell expression with the corresponding 48 hour cells, giving us a trajectory
345
between the two timepoints. We observed that the distribution of pseudocells began closest to that of
346
the12hourtimepoint, approachedtheheldout24hourtimepointatthemidpointofthesimulation, then
347
finally converged to the 48 hour timepoint, as expected (Figure 4e). We manually picked a timestep
348
from this trajectory to represent the 24 hour timepoint. We then compared CellTRIP-predicted and
349
actual gene expression at the beginning, manually-chosen, and ending timepoints (Figure 4f). Meadian
350
CellTRIP expressions across all timepoints were significantly correlated for three of the top eight genes
351
by change from 12 to 48 hours, and positively correlated with three others.
352
11
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
Figure 5: Spatiotemporal developmental stage imputation, recovery, and knockdown in developing
Drosophila. a. Visualization of observed and predicted spatial coordinates for fly embryonic develop-
ment8 across developmental timesteps (columns) and methods (rows), colored by cell annotations. Stage
E16-18h_a (red) was not included in training. b. Mean squared error for select annotations compared
across methods. c. Heldout developmental stage recovery using CellTRIP. Wasserstein distance (EMD)
is computed between predicted and observed cell distributions, including baseline linear interpolation
(LERP) at a few transitional fractions. Further methodological details can be found in Section 3.4.1
and Figure S1. d. Heatmap of genes (x-axis) with developmentally-correlating perturbation significance
values as predicted by CellTRIP, segmented by annotation (y-axis). Stronger Pearson correlation signifi-
cance is indicated by higher opacity while positive and negative correlation is indicated by red and blue
coloration, respectively. e. Gene set enrichment of top 200 CellTRIP developmental genes from select
cell annotations.
4.4 Spatiotemporal Reconstruction of Drosophila Embryonic Develop-
353
ment
354
We further trained a single CellTRIP model on a single-cell spatiotemporal gene expression dataset in
355
Drosophila larvae, demonstrating its capability for imputation in both temporal and spatial domains,
356
as well as for perturbation prediction. This dataset measures both gene expression and the spatial
357
coordinates of 155,684 single cells across five developmental stages (two embryonic and three larval).
358
Note that we held out the intermediate developmental stage E16-18h_a from training for imputation
359
evaluation.
360
We applied CellTRIP to the task of imputing spatial coordinates from measured gene expression (Sec-
361
tion 3.4.1). CellTRIP spatial imputation outperformed MLP- and KNN-based methods (Section S2.4).
362
In methods other than CellTRIP, we observed overfitting to later larval stages, evidenced by the stretched
363
distribution of cell spatial coordinates in embryonic and early larval stages (Figure 5a). CellTRIP spatial
364
12
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
imputation performance was comparable to other methods on most training stages, but had the lowest
365
prediction MSE (CellTRIP 90.41, MLP 333.86, KNN 360.33) and highest classification accuracy of 10
366
tissue types (CellTRIP 0.237, MLP 0.231, KNN 0.207, Baseline 0.100) on the heldout developmental
367
stageE16-18h_a andinamajorityofconstituenttissuetypes(Figure5bandSupplementaryFigureS11).
368
Wethenperformedtemporalimputationtoinferthespatialtrajectoryofcellsbetweenknowndevelop-
369
mental timepoints, and subsequently recover the cellular spatial distribution of our held out intermediate
370
developmental stage (Section 3.4.2, Figure S1). First, we use optimal transport to match pseudocells
371
between the stages immediately preceding and following E16-18h_a, namely, E14-16h_a and L1_a. We
372
then used CellTRIP to compute a spatial trajectory between the two timepoints, selecting an interme-
373
diate trajectory timestep to recover the cell spatial distribution of E16-18h_a (Figure 5c). CellTRIP
374
outperformed linear interpolation (LERP) using the Wasserstein distance (EMD) between observed and
375
imputed spatial coordinates (CellTRIP 24.5, LERP 82.7, Section S2.4).
376
We further utilized CellTRIP to make in-silico gene perturbation predictions to prioritize tissue type
377
developmental genes. In particular, we calculated gene effect sizes (Section 3.4.3) for the top 2,000
378
highly-variable genes by tissue type and developmental stage. We then computed Pearson correlations
379
of our gene effect sizes with developmental stages to prioritize developmental genes (Section S2.4,
380
Figure 5d).
381
We focused on tissue types where developmental progression is morphologically well-characterized
382
and mechanistically linked to stage remodeling. Based on this criterion, we selected central nervous
383
system (CNS), muscle, and tracheal tissue types, representing neuronal maturation39, skeletal muscle
384
development40, and respiratory tube branching41, respectively (Figure 5e). In CNS, the top 10% devel-
385
opmental genes by correlation were significantly enriched for innate immune response (p < 2.36×10−4),
386
a key aspect of the Drosophila CNS which plays a key role in preventing harmful effects from injury,
387
infection, and neurodegenerative diseases42. Performing a similar analysis in muscle tissue, we obtain a
388
top enrichment of proteolysis (p < 2.12×10−5), p < 1.07×10−2)). Muscle proteolysis is critical for
adj 389
maintaining glucose supply under starvation conditions and may share pathways responsible for muscle
390
atrophy43. Lastly, many metabolic processes are prioritized for tracheal tissue (small molecule metabolic
391
process, p < 1.05×10−4), and metabolic depression under starvation uses insulin as to stimulate tracheal
392
progenitor cells for regeneration or remodeling44.
393
5 Discussion
394
We have shown the outperformance and predictive capabilities of CellTRIP for trajectory interpolation,
395
imputation, and perturbation prediction on a diverse range of temporal and spatial datasets. CellTRIP
396
is also interactive, biologically interpretable, and can provide importance estimates with respect to indi-
397
vidual genes, spatial locations, and developmental stages. To our knowledge, this is the first application
398
of reinforcement learning to generate virtual cell environments based on single-cell omics data. We also
399
contribute to existing reinforcement literature by extending PopArt21 to support input layer normalization
400
and weight rescaling. CellTRIP has the distinct advantage of being interactive. CellTRIP can be gener-
401
alized to other dynamic datasets, such as disease progression or tissue-level analysis with bulk expression
402
data.
403
CellTRIP has some limitations. In Section 4.2, we note that imputation of the uncorrected validation
404
data yields spatial coordinate predictions shifted from the observed data. We choose to apply batch
405
correction to the validation dataset. Further analysis would be needed, however, to determine how much
406
of this shift was caused by batch effects or was driven by true spatial expression variance. We note that
407
stage L3_b from Section 4.4 displays a tendency of CellTRIP to distribute cells only across the primary
408
spatial axis, likely due to the focus of CellTRIP on generality across time points. If sufficient information
409
exists in gene expression alone, then this may be solved by running more simulations in parallel during
410
training, allowing for a more representative training set each backward pass. We run CellTRIP with a
411
13
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
low-dimensional environment space because the training time for a continuous reinforcement learning
412
model scales rapidly. This is a well-known side effect of continuous output in PPO models and can
413
be solved with either greater memory size or discretization of the model outputs. We found that the
414
environment space performs better when diagonal action vectors remain unnormalized. This has the
415
consequence that cells in the environment can move faster diagonally, which is unideal. The runtime
416
of CellTRIP also typically scales with the number of simulated and visible cells, as expected. However,
417
distributed computing for forwards and backwards passes and user-adjustable inference settings mitigate
418
this runtime limitation significantly. CellTRIP needs to employ additional strategies to ensure minimal
419
usage of both memory and VRAM throughout the running process. CellTRIP can also be extended to
420
predict cell death, proliferation, or the spread of disease in tissue samples through modifications to the
421
environment space and policy actions.
422
References
423
1. Yayon, N., Kedlian, V. R., Boehme, L., Suo, C., Wachter, B. T., Beuschel, R. T., Amsalem, O.,
424
Polanski, K., Koplev, S., Tuck, E., Dann, E., Van Hulle, J., Perera, S., Putteman, T., Predeus,
425
A. V., Dabrowska, M., Richardson, L., Tudor, C., Kreins, A. Y., Engelbert, J., Stephenson, E.,
426
Kleshchevnikov, V., De Rita, F., Crossland, D., Bosticardo, M., Pala, F., Prigmore, E., Chipampe,
427
N.-J., Prete, M., Fei, L., To, K., Barker, R. A., He, X., Van Nieuwerburgh, F., Bayraktar, O. A.,
428
Patel, M., Davies, E. G., Haniffa, M. A., Uhlmann, V., Notarangelo, L. D., Germain, R. N., Radtke,
429
A. J., Marioni, J. C., Taghon, T., and Teichmann, S. A. (2024). A spatial human thymus cell atlas
430
mapped to a continuous tissue axis. Nature 635, 708–718. URL: https://doi.org/10.1038/
431
s41586-024-07944-6. doi:10.1038/s41586-024-07944-6.
432
2. Binan, L., Jiang, A., Danquah, S. A., Valakh, V., Simonton, B., Bezney, J., Manguso, R. T.,
433
Yates, K. B., Nehme, R., Cleary, B., and Farhi, S. L. (2025). Simultaneous crispr screening and
434
spatial transcriptomics reveal intracellular, intercellular, and functional transcriptional circuits. Cell
435
188, 2141–2158.e18. URL: https://doi.org/10.1016/j.cell.2025.02.012. doi:10.1016/j.
436
cell.2025.02.012.
437
3. Kim, J., Rothová, M. M., Madan, E., Rhee, S., Weng, G., Palma, A. M., Liao, L.,
438
David, E., Amit, I., Hajkarim, M. C., Vudatha, V., Gutiérrez-García, A., Moreno, E.,
439
Winn, R., Trevino, J., Fisher, P. B., Brickman, J. M., Gogna, R., and Won, K. J.
440
(2023). Neighbor-specific gene expression revealed from physically interacting cells during
441
mouse embryonic development. Proceedings of the National Academy of Sciences 120,
442
e2205371120. URL: https://www.pnas.org/doi/abs/10.1073/pnas.2205371120. doi:10.
443
1073/pnas.2205371120. arXiv:https://www.pnas.org/doi/pdf/10.1073/pnas.2205371120.
444
4. Liu, Z., Yang, Z., Wu, J., Zhang, W., Sun, Y., Zhang, C., Bai, G., Yang, L., Fan, H., Chen, Y.,
445
Zhang, L., Jiang, B., Liu, X., Ma, X., Tang, W., Liu, C., Qu, Y., Yan, L., Zhao, D., Wu, Y., He,
446
S., Xu, L., Peng, L., Chen, X., Zhou, B., Zhao, L., Zhao, Z., Tan, F., Zhang, W., Yi, D., Li, X.,
447
Gao, Q., Zhang, G., Wang, Y., Yang, M., Fu, H., Guo, Y., Hu, X., Cai, Q., Qi, L., Bo, Y., Peng,
448
H., Tian, Z., She, Y., Zou, C., Zhu, L., Cheng, S., Zhang, Y., Zhong, W., Chen, C., Gao, S., and
449
Zhang,Z.(2025).Asingle-cellatlasrevealsimmuneheterogeneityinanti-pd-1-treatednon-smallcell
450
lung cancer. Cell 188, 3081–3096.e19. URL: https://doi.org/10.1016/j.cell.2025.03.018.
451
doi:10.1016/j.cell.2025.03.018.
452
5. Hu, T., Chitnis, N., Monos, D., and Dinh, A. (2021). Next-generation sequencing technologies: An
453
overview. Human Immunology 82, 801–811. URL: https://www.sciencedirect.com/science/
454
article/pii/S0198885921000628. doi:https://doi.org/10.1016/j.humimm.2021.02.012.
455
Next Generation Sequencing and its Application to Medical Laboratory Immunology.
456
14
bioRxiv preprint doi: https://doi.org/10.1101/2025.11.21.689815; this version posted November 24, 2025. The copyright holder for this
preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission.
6. Jiang, F., Zhou, X., Qian, Y., Zhu, M., Wang, L., Li, Z., Shen, Q., Wang, M., Qu, F., Cui, G.,
457
Chen, K., and Peng, G. (2023). Simultaneous profiling of spatial gene expression and chromatin
458
accessibility during mouse brain development. Nature Methods 20, 1048–1057. URL: https://
459
doi.org/10.1038/s41592-023-01884-1. doi:10.1038/s41592-023-01884-1.
460
7. McFarland, J. M., Paolella, B. R., Warren, A., Geiger-Schuller, K., Shibue, T., Rothberg, M.,
461
Kuksenko, O., Colgan, W. N., Jones, A., Chambers, E., Dionne, D., Bender, S., Wolpin, B. M.,
462
Ghandi, M., Tirosh, I., Rozenblatt-Rosen, O., Roth, J. A., Golub, T. R., Regev, A., Aguirre, A. J.,
463
Vazquez, F., and Tsherniak, A. (2020). Multiplexed single-cell transcriptional response profiling to
464
definecancervulnerabilitiesandtherapeuticmechanismofaction. NatureCommunications11,4296.
465
URL: https://doi.org/10.1038/s41467-020-17440-w. doi:10.1038/s41467-020-17440-w.
466
8. Wang, M., Hu, Q., Lv, T., Wang, Y., Lan, Q., Xiang, R., Tu, Z., Wei, Y., Han, K., Shi, C., Guo,
467
J., Liu, C., Yang, T., Du, W., An, Y., Cheng, M., Xu, J., Lu, H., Li, W., Zhang, S., Chen, A.,
468
Chen, W., Li, Y., Wang, X., Xu, X., Hu, Y., and Liu, L. (2022). High-resolution 3d spatiotemporal
469
transcriptomicmapsofdeveloping<em>drosophila</em>embryosandlarvae. DevelopmentalCell
470
57, 1271–1283.e4. URL: https://doi.org/10.1016/j.devcel.2022.04.006. doi:10.1016/j.
471
devcel.2022.04.006.
472
9. Klein, D., Palla, G., Lange, M., Klein, M., Piran, Z., Gander, M., Meng-Papaxanthos, L., Sterr,
473
M., Saber, L., Jing, C., Bastidas-Ponce, A., Cota, P., Tarquis-Medina, M., Parikh, S., Gold,
474
I., Lickert, H., Bakhti, M., Nitzan, M., Cuturi, M., and Theis, F. J. (2025). Mapping cells
475
through time and space with moscot. Nature 638, 1065–1075. URL: https://doi.org/10.1038/
476
s41586-024-08453-2. doi:10.1038/s41586-024-08453-2.
477
10. Farrell, J. A., Wang, Y., Riesenfeld, S. J., Shekhar, K., Regev, A., and Schier, A. F. (2018). Single-
478
cell reconstruction of developmental trajectories during zebrafish embryogenesis. Science 360.
479
11. Chen, H., Albergante, L., Hsu, J. Y., Lareau, C. A., Lo Bosco, G., Guan, J., Zhou, S., Gorban,
480
A. N., Bauer, D. E., Aryee, M. J., Langenau, D. M., Zinovyev, A., Buenrostro, J. D., Yuan,
481
G.-C., and Pinello, L. (2019). Single-cell trajectories reconstruction, exploration and mapping of
482
omics data with stream. Nature Communications 10, 1903. URL: https://doi.org/10.1038/
483
s41467-019-09670-4. doi:10.1038/s41467-019-09670-4.
484
12. Haarnoja, T., Moran, B., Lever, G., Huang, S. H., Tirumala, D., Humplik, J., Wulfmeier, M., Tun-
485
yasuvunakool, S., Siegel, N. Y., Hafner, R., Bloesch, M., Hartikainen, K., Byravan, A., Hasenclever,
486
L., Tassa, Y., Sadeghi, F., Batchelor, N., Casarini, F., Saliceti, S., Game, C., Sreendra, N., Patel,
487
K., Gwira, M., Huber, A., Hurley, N., Nori, F., Hadsell, R., and Heess, N. (2024). Learning agile
488
soccer skills for a bipedal robot with deep reinforcement learning. Science Robotics 9, eadi8022.
489
URL: https://www.science.org/doi/abs/10.1126/scirobotics.adi8022. doi:10.1126/
490
scirobotics.adi8022. arXiv:https://www.science.org/doi/pdf/10.1126/scirobotics.adi8022.
491
13. Abeyruwan, S. W., Graesser, L., D’Ambrosio, D. B., Singh, A., Shankar, A., Bewley, A., Jain,
492
D., Choromanski, K. M., and Sanketi, P. R. (2023). i-sim2real: Reinforcement learning of robotic
493
policies in tight human-robot interaction loops. In: Liu, K., Kulic, D., and Ichnowski, J., eds.
494
Proceedings of The 6th Conference on Robot Learning vol. 205 of Proceedings of Machine Learning
495
Research. PMLR ( 212–224). URL: https://proceedings.mlr.press/v205/abeyruwan23a.
496
html.
497
14. Angermueller, C., Dohan, D., Belanger, D., Deshpande, R., Murphy, K., and Colwell, L. (2020).
498
Model-based reinforcement learning for biological sequence design. In: International Conference on
499
Learning Representations. URL: https://openreview.net/forum?id=HklxbgBKvr.
500
15
