---
title: AcrB multidrug efflux pump
created: 2026-05-26
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1007##s10969-013-9154-x, doi/10.1016##j.jsb.2011.01.014, doi/10.1016##j.str.2007.09.023, doi/10.1038##nature12300, doi/10.1038##ncomms13819]
verified: false
---

# AcrB multidrug efflux pump

## Overview

AcrB is the principal multidrug transporter in Escherichia coli, functioning as an inner membrane resistance-nodulation-cell division (RND) efflux pump that forms part of the AcrAB-TolC tripartite efflux system. The crystal structure of the AcrB-Linezolid complex was determined at 3.5 A resolution, revealing that Linezolid binds to the A385/F386 loops of the symmetric trimer. A conformational change in a loop at the bottom of the periplasmic cleft was also observed, which is important for substrate transport and [AcrA(/xray-mp-wiki/proteins/acrA/)] binding. DARPin-mediated crystallization has yielded asymmetric AcrB structures at higher resolution (2.54 A), revealing the rotary transport mechanism through three distinct protomer conformations (access, binding, extrusion). The first inhibitor-bound structure of AcrB was solved with the pyridopyrimidine derivative ABI-PP, revealing that the inhibitor binds to a hydrophobic trap in the distal drug-binding pocket, sterically hindering the functional rotation mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1007##s10969-013-9154-x | 4K7Q | 3.5 A | R32 | Wild-type AcrB with C-terminal polyhistidine tag | Linezolid |
| doi/10.1016##j.jsb.2011.01.014 | 2JBS | 2.54 A | P2$_{1}$2$_{1}$2$_{1}$ | AcrB in complex with DARPin#1 crystallization chaperone | DARPin#1 |
| doi/10.1016##j.jsb.2011.01.014 | 3NOC | 2.70 A | P2$_{1}$2$_{1}$2$_{1}$ | AcrB in complex with DARPin#2 crystallization chaperone | DARPin#2 |
| doi/10.1016##j.jsb.2011.01.014 | 3NOG | 3.34 A | P2$_{1}$2$_{1}$2$_{1}$ | AcrB in complex with DARPin#3 crystallization chaperone | DARPin#3 |
| doi/10.1016##j.str.2007.09.023 | 2RDD | 3.5 A | P3221 | AcrB in complex with endogenous YajC transmembrane subunit | Ampicillin |
| doi/10.1038##nature12300 | not specified | 3.05 A | C2 | Wild-type AcrB with C-terminal polyhistidine tag, complexed with ABI-PP inhibitor | ABI-PP (tert-butyl thiazolyl aminocarboxyl pyridopyrimidine) |
| doi/10.1038##nature12300 | not specified | 3.60 A | C2 | AcrB(F178W) mutant with C-terminal polyhistidine tag | None (drug-free) |
| doi/10.1038##ncomms13819 | 4DX5 | 2.5 A | P2$_{1}$2$_{1}$2$_{1}$ | Wild-type AcrB in complex with DARPin crystallization chaperone | Fusidic acid |

## Expression and Purification

- **Expression system**: E. coli JM109 (wild-type), E. coli W3104 (acrB-deficient, for F178W mutant)
- **Construct**: Wild-type AcrB with C-terminal polyhistidine tag, overproduced from the histidine-tagged AcrB-overexpression plasmid pAcBH. AcrB(F178W) mutant expressed from plasmid pAcBHF178W in acrA/acrB-deficient E. coli strain W3104.

### Purification Workflow

*Source: doi/10.1016##j.str.2007.09.023*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane isolation | Cell disruption with X-Press, membrane fractions collected by ultracentrifugation at 185,000 x g for 90 min | -- | -- + -- | E. coli JM109 strain grown in LB media with 100 mg/L ampicillin for 16 hr |
| Solubilization | Membrane solubilization | -- | -- + 1.75% n-Dodecyl-beta-D-maltopyranoside (DDM) | Membranes solubilized in 1.75% DDM (Anatrace) |
| Ni-affinity chromatography | Ni-affinity chromatography (Chelating Sepharose Fast Flow) | Chelating Sepharose Fast Flow (GE Healthcare) | 60 mM NaPO4 (pH 7.5), 0.7 M NaCl, 33 mM imidazole, 1 mM beta-mercaptoethanol, 0.03% DDM + 0.03% DDM | AcrB bound to Ni2+ media overnight; unbound material washed out. Endogenous AcrB co-purified with YajC transmembrane subunit. |
| Elution | Ni-affinity chromatography elution | Chelating Sepharose Fast Flow (GE Healthcare) | 30 mM NaPO4 (pH 7.5), 0.1 M NaCl, 10 mM imidazole, 1 mM beta-mercaptoethanol, 0.03% DDM (elution with 150 mM imidazole) + 0.03% DDM | AcrB eluted with 150 mM imidazole |
| Size exclusion chromatography | Size exclusion chromatography (Sephacryl S300 16/60) | Sephacryl S300 16/60 (GE Healthcare) | 20 mM HEPES (pH 7.0), 150 mM NaCl, 0.03% DDM + 0.03% DDM | SEC used to improve sample homogeneity. Protein concentrated to 10 mg/mL prior to crystallization. |

### Purification Workflow

*Source: doi/10.1007##s10969-013-9154-x*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption and membrane isolation | Cells disrupted with Microfluidizer, membrane fractions collected by ultracentrifugation at 150,000g for 90 min | -- | -- + -- | Membranes washed using several ultracentrifugation steps at 150,000g for 90 min |
| Solubilization | Membranes solubilized by ultracentrifugation at 170,000g for 60 min | -- | 50 mM Tris-HCl (pH 7.0), 10% glycerol + 2% n-Dodecyl-beta-D-maltoside (DDM) | Lipids and debris removed by ultracentrifugation at 170,000g for 60 min |
| Affinity chromatography | Metal affinity column chromatography (Ni-NTA) | Nickel-NTA agarose | 20 mM Tris-HCl (pH 7.5), 0.3 M NaCl, 10% glycerol, 0.2% DDM + 0.2% DDM | Column washed stepwise with 25 mM and 100 mM [imidazole(/xray-mp-wiki/reagents/additives/imidazole/)]. Purified AcrB eluted with 300 mM imidazole. Imidazole removed by three concentration-dilution steps using an ultrafiltration membrane |
| Concentration and storage | Concentration-dilution with ultrafiltration membrane | -- | 20 mM sodium phosphate (pH 6.2), 10% glycerol, 0.2% DDM + 0.2% DDM | Protein concentrated to 28 mg/mL and frozen in liquid nitrogen |


## Crystallization

### doi/10.1016##j.str.2007.09.023

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 10 mg/mL AcrB:YajC complex in 20 mM HEPES (pH 7.0), 150 mM NaCl, 0.03% DDM |
| Reservoir | 14%-28% PEG1000 or PEG1500, 0.1 M Tris (pH 7.5), 0.1 M Li2SO4, 18 mM n-Octyl-beta-D-Thioglucopyranoside, 20% 1,2,3-heptanetriol |
| Mixing ratio | equal volumes protein to reservoir |
| Temperature | 293 K |
| Growth time | 3-4 days |
| Cryoprotection | 20% w/v glycerol |
| Notes | Crystals grown from endogenous AcrB purified from E. coli JM109 grown in ampicillin-containing media. Space group P3221 with unit cell dimensions a=145.1, b=145.1, c=511.6 A, alpha=90, beta=90, gamma=120. The structure revealed a novel single transmembrane subunit (YajC) associated with AcrB. Six ampicillin molecules bound in the central cavity. Data collected at 100 K at ESRF ID14-2 beamline. Rcryst 27.9%, Rfree 31.7%. |

### doi/10.1007##s10969-013-9154-x

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 28 mg/mL AcrB in 20 mM sodium phosphate (pH 6.2), 10% glycerol, 0.2% DDM |
| Reservoir | 0.1 M NaCl, Na-phosphate (pH 6.2), 8% PEG 4000 |
| Temperature | 21 C (Linezolid soaking) |
| Growth time | not specified |
| Cryoprotection | 25% glycerol (cryosolvent containing crystallization reagents plus 25% glycerol) |
| Notes | Apo-AcrB crystals were transferred to the cryosolvent and incubated at 21 C for 10 min before flash cooling in liquid nitrogen. Linezolid (6 mM) was added to the cryosolvent and crystals were soaked prior to data collection. Linezolid stock solution (30 mM) was prepared with water. X-ray diffraction data collected at 100 K on beamline 5.0.1 (ALS). Space group R32 with cell dimensions a=144.7, b=144.7, c=519.4 A, alpha=90, beta=90, gamma=120. Matthews coefficient 4.8 A3/Da, solvent content 74.2%. Final R-factor 25.1%, free-R factor 30.4% for data between 50 and 3.5 A. |

### doi/10.1016##j.jsb.2011.01.014

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | AcrB in complex with DARPin#1, DARPin#2, or DARPin#3 crystallization chaperone |
| Reservoir | 8-10% PEG 4000, 50 mM ADA pH 6.5, 200 mM (NH4)2SO4 |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Crystallization condition optimized for AcrB-DARPin#1 complex; other complexes did not crystallize in this condition. Space group P2$_{1}$2$_{1}$2$_{1}$ for all three complexes. Unit cell parameters: 2JBS (a=146.2, b=157.4, c=246.0 A), 3NOC (a=146.0, b=158.7, c=244.5 A), 3NOG (a=145.4, b=158.0, c=258.6 A). Two DARPin molecules bound per AcrB trimer. |

### doi/10.1038##nature12300

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | ABI-PP-bound AcrB at unspecified concentration, inhibitor:protein molar ratio 5:1 |
| Reservoir | Not specified in paper text |
| Mixing ratio | Not specified |
| Temperature | 25 C |
| Growth time | 5 days for appearance, further 5 days for collection |
| Cryoprotection | Polyethylene glycol 400 concentration increased to 40% (v/v) in three steps; crystals flash frozen in liquid nitrogen or cryostream (100 K) |
| Notes | C2 crystals of ABI-PP-bound AcrB generated using dodecanoyl sucrose. Structure solved at 3.05 A resolution. Difference Fourier map (Finhibitor - Ffree) contoured at 3.5 sigma. Data collected at BL44XU beamline at SPring-8 with MX225-HE CCD detector at 100 K. Crystals processed using HKL2000. |

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Drug-free AcrB(F178W) mutant |
| Reservoir | Not specified in paper text |
| Mixing ratio | Not specified |
| Temperature | 25 C |
| Growth time | 5 days for appearance, further 5 days for collection |
| Cryoprotection | Polyethylene glycol 400 concentration increased to 40% (v/v) in three steps; crystals flash frozen in liquid nitrogen or cryostream (100 K) |
| Notes | C2 crystals of AcrB(F178W) mutant generated using dodecanoyl sucrose. Structure solved at 3.60 A resolution. Data collected at BL44XU beamline at SPring-8. Crystals processed using HKL2000. Mutant expressed from plasmid pAcBHF178W in acrA/acrB-deficient E. coli strain W3104. |

### doi/10.1038##ncomms13819

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 10-15 mg/mL AcrB in complex with DARPin, mixed 1:2 molar ratio, excess DARPin removed by SEC |
| Reservoir | 50 mM ADA pH 6.9, 5% glycerol, 5-10% PEG4000, 150-250 mM ammonium sulfate |
| Mixing ratio | Not specified |
| Temperature | not specified |
| Growth time | Crystals appeared in 1 week, grew to optimum size (100 x 70 x 200 um) within additional 1-2 weeks |
| Cryoprotection | not specified |
| Notes | Fusidic acid (4 mM) was added before crystallization. P2$_{1}$2$_{1}$2$_{1}$ crystals. Structure refined at 2.5 A resolution with R/Rfree of 22.5/26.2. Data collected at beamline X06DA of the Swiss Light Source (Paul Scherrer Institute). Structure refined using phenix.refine from PHENIX package and REFMAC5, validated with MolProbity. Model rebuilding done with COOT. |


## Biological / Functional Insights

### Linezolid binding site on the A385/F386 loop

Each protomer of the symmetric AcrB trimer binds one Linezolid molecule on the wall
of the upper portion of the central cavity near residues A385 and F386. The three
rings of the Linezolid molecule lie approximately parallel to the F386 binding
loop, allowing maximum hydrophobic contact between the drug and AcrB. The binding
interface buries approximately 140 A^2 of Linezolid surface, with almost the whole
molecule except for its acetamide tail participating in hydrophobic stacking interactions.
Several other drugs including [Ethidium(/xray-mp-wiki/reagents/ligands/ethidium/)],
[Nafcillin(/xray-mp-wiki/reagents/antibiotics/nafcillin/)], and [Ampicillin(/xray-mp-wiki/reagents/antibiotics/ampicillin/)]
also bind to this location on symmetric AcrB trimers.

### Conformational change in the porter domain loop

Comparison with the apo-AcrB structure reveals a significant local conformational
difference at residues 670-675. While the overall structures superpose with a root-mean-square
C-alpha coordinate deviation of 0.4 A, these residues on the surface of the protein
(but not near crystal contacts) differ by up to 4 A in backbone position. These
residues reside in a loop lining the bottom of the cleft in the porter domain,
thought to be important for substrate transport and [AcrA(/xray-mp-wiki/proteins/acrA/)]
binding.

### Structural basis for Linezolid efflux

Linezolid is an oxazolidinone-type antibacterial agent that inhibits bacterial
protein synthesis by binding to the 50S ribosomal subunit. It is the first FDA-approved
oxazolidinone antibiotic used for treatment of serious infections caused by Gram-positive
bacteria resistant to other antibiotics. Linezolid has no clinically significant
effect on most Gram-negative bacteria, which is attributed to relatively low intracellular
concentration due to efflux. E. coli with inactivated AcrB is more susceptible
to Linezolid than cells with an intact pump. The AcrB-Linezolid crystal structure
provides direct evidence that Linezolid can be extruded by efflux pumps.

### Tripartite efflux system architecture

AcrB is part of the AcrAB-TolC tripartite efflux system consisting of an outer
membrane factor, [TolC(/xray-mp-wiki/proteins/tolC/)], a periplasmic membrane fusion
protein, [AcrA(/xray-mp-wiki/proteins/acrA/)], and the inner membrane RND efflux
pump, AcrB. This integrated three-component molecular complex extrudes a large variety
of cytotoxic substances such as antibiotics, organic solvents, dyes, and detergents
from the cell directly into the medium, bypassing the periplasm and the outer membrane.
Over-expression of the tripartite RND efflux systems is a major factor in multidrug
resistance in Gram-negative bacteria.

### DARPin-mediated crystallization improves diffraction quality

DARPin (Designed Ankyrin Repeat Protein) crystallization chaperones were used to
mediate crystal contacts in AcrB, yielding asymmetric structures in space group P2$_{1}$2$_{1}$2$_{1}$
at resolutions up to 2.54 A. Two DARPin molecules bind per AcrB trimer, interacting
with the DC subdomain of the TolC docking domain at the tip of the periplasmic part
of the transporter. The DARPin-mediated crystal lattice provides equal contacts in
all three dimensions, compared to the layer-like packing in R32 crystals that can
lead to anisotropic diffraction. The DARPin binding site is formed by strand 802-811
on the surface of AcrB, which contains a hydrophobic tryptophan patch that serves
as a hot-spot epitope for DARPin binding.

### Asymmetric conformations reveal rotary transport mechanism

The asymmetric AcrB structures in P2$_{1}$2$_{1}$2$_{1}$ reveal three distinct protomer
conformations representing a snapshot of the transport cycle: access (loose), binding
(tight), and extrusion (open) conformations. This supports a rotary pump mechanism
where each protomer cycles through these states. DARPin binds to subunit A (access/loose)
and subunit B (binding/tight) but not to subunit C (extrusion/open) due to steric
clash with helical portion of subdomain PC2. This conformational selectivity demonstrates
that synthetic binding proteins can trap specific conformations of their target, reducing
conformational heterogeneity and facilitating crystallization.

### Crystal contact plasticity affects diffraction quality

Comparative analysis of three AcrB-DARPin crystal structures (2JBS at 2.54 A, 3NOC
at 2.70 A, 3NOG at 3.34 A) reveals that subtle conformational differences in the
DARPin-AcrB interface significantly affect diffraction quality. In the 3NOG structure,
transmembrane helices TM2, TM7, TM9, and TM12 in subunit A are shifted outward,
causing rigid-body movement of periplasmic domains. This results in a 12 A difference
in the c-axis unit cell parameter and reduced buried surface area at the crystal
contact (409.8 A^2 vs 444.4 A^2 in 2JBS), despite identical residues being involved.
This demonstrates that even identical crystal contact residues can produce different
diffraction quality depending on the precise binding geometry.

### DARPin binding affinity and stoichiometry

Nine DARPin binders to AcrB were characterized by surface plasmon resonance. All
dissociation constants are in the medium to low nanomolar range (1.5-89 nM). DARPin#2
shows the highest affinity (Kd=1.5 nM) combining the fastest on-rate with the slowest
off-rate. Stoichiometry varies: DARPin#1, #2, and #3 bind with 2 DARPin per AcrB
trimer; DARPin#4 and #5 bind with 1; DARPin#6 and #7 bind with 3. DARPin#2 also
shows weak cross-reactivity with AcrF. The same randomized sequence positions can
yield different affinities depending on spatial arrangement by the scaffold, highlighting
the importance of exact geometry in protein-protein interactions.

### YajC transmembrane subunit associates with AcrB

The crystal structure of endogenous AcrB revealed a novel single transmembrane subunit
identified by mass spectrometry as YajC. YajC forms an elongated, highly tilted TM helix
of approximately 37 residues (54 A long) that extends across the entire width of the
membrane. YajC interacts with TM helices 2, 7, 11, 12, and Iα2 of AcrB. The average
Cα-to-Cα distance from YajC to AcrB is 7.3 A. The binding interface on AcrB is one of
the most conserved regions on its surface. Growth experiments with yajc-deleted E. coli
revealed a modest increase in susceptibility to beta-lactam antibiotics (ampicillin and
nafcillin), though the functional role could not be conclusively assigned.

### AcrB porter domain twist

The AcrB:YajC structure revealed a significant rotation of the AcrB porter domain
relative to its TM domain, distinct from the conformational changes seen in asymmetric
AcrB structures. A rotational movement of the same nature is preserved when comparing
the porter domain relative to the TolC binding domain. This twist is consistent with
the "twist-to-open" hypothesis for TolC activation, where a specific rotation of the
porter domain could be communicated by AcrA to the superhelical coils of TolC, inducing
a twist that opens the exit duct. This represents another dynamic motion inherent to
AcrB, complementary to the cyclic peristaltic mechanism.

### ABI-PP inhibitor binds hydrophobic trap and blocks functional rotation

The first inhibitor-bound structure of AcrB was solved with the pyridopyrimidine derivative
ABI-PP. ABI-PP binds tightly to a narrow hydrophobic trap composed of a phenylalanine cluster
located in the distal drug-binding pocket. This pit is a hydrophobic trap that branches off
from the substrate-translocation channel. Phe 178 is located at the edge of this trap and
contributes to tight binding of the inhibitor through a pi-pi interaction with the pyridopyrimidine
ring. ABI-PP is not exported by AcrB and sterically hinders the functional rotation mechanism,
thereby potentiating the activities of all antibiotics exported by AcrB, including both
distal-binding and proximal-binding drugs. The inhibitor:protein molar ratio used for
crystallization was 5:1.

### AcrB(F178W) mutant loses inhibitor sensitivity

The AcrB(F178W) mutant was constructed to test the role of Phe 178 in ABI-PP binding.
The crystal structure of AcrB(F178W) at 3.60 A revealed that the indolyl side chain of
W178 protrudes into the narrow space of the hydrophobic trap, sterically blocking ABI-PP
binding. In functional assays, the growth of AcrB(F178W)-expressing cells was considerably
less inhibited by ABI-PP in the presence of erythromycin, and doxorubicin fluorescence
quenching was completely prevented even in the presence of ABI-PP, confirming that the
mutant is no longer inhibited by the drug.

### Fusidic acid binding to the TM1/TM2 groove

The high-resolution (2.5 A) asymmetric AcrB structure in complex with fusidic acid
reveals a novel drug binding site at the interface of transmembrane helix 1 (TM1) and
TM2, located approximately 6 A from the periplasmic side of the lipid bilayer. This
groove is pseudosymmetric to the TM7/TM8 groove postulated to be a binding site for
drugs from the outer leaflet of the inner membrane. Fusidic acid binds specifically in
the tight (T) conformer with the strongest density, while weaker densities were observed
in the loose (L) and open (O) conformers. Key interacting residues include I27 (TM1)
and K334, I337, H338, V341 (TM2). Mutational analysis of I337, H338, and V341 showed
that the I337A variant renders cells more susceptible to fusidic acid and beta-lactams,
confirming the functional importance of this binding site. Site-directed mutagenesis
of these residues (I337A, H338A, H338R, V341A) confirmed that residues in the TM1/TM2
groove are critical for carboxylate drug resistance. Cross-link protection experiments
with the H338C variant showed that fusidic acid and dicloxacillin protect C338 from
MTS-rhodamine modification in a concentration-dependent manner, with apparent Ki values
of ~2.1 mM and ~2.0 mM, respectively.

### Helix shift mechanism for carboxylate drug transport

The asymmetric AcrB structure reveals a helix shift mechanism for active transport of
carboxylate drugs from the membrane to the periplasm. Superimposition of T and O
conformers shows that TM2 moves upward toward the periplasm by approximately 2.5 A
during the T to O transition. The bound fusidic acid molecule shifts congruently with
TM2, moving from the hydrophobic core of the outer leaflet toward the more hydrophilic
phospholipid headgroup area at the membrane/periplasm interface. During the T to O
transition, the upward helix shift of TM2 drags the drug partially out of the membrane
toward the periplasm. A large part of the fusidic acid alkyl chain is also displaced
during this transition. In the O conformation, fusidic acid locates slightly below a
small hydrophobic cave made up of L300, V32, V333, I337, and the alkyl chain of K334.
Once TM2 returns to its down state in the O to L transition (due to deprotonation of
catalytic D407 and D408 residues), the binding site is partially re-established and
functions as a low-affinity binding site in the L protomer. Carboxylate drugs are
postulated to be elevated from the membrane during the T to O transition by TM2 helix
upward shift, further transported during the O to L transition via the PC1/PN2 down
pathway, and bound to the deep binding pocket in the L to T transition. This mechanism
is linked directly to protonation and deprotonation events during the T to O and O to L
transitions.


## Cross-References

- [E. coli YajC Transmembrane Protein](/xray-mp-wiki/proteins/yajc/) — Forms a stable complex with AcrB; crystal structure determined together (PDB 2RDD)
- [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/concepts/darpin/) — DARPin crystallization chaperones used to solve three high-resolution AcrB structures (2JBS, 3NOC, 3NOG)
- [AcrA multidrug efflux pump periplasmic protein](/xray-mp-wiki/proteins/acrA/) — Periplasmic membrane fusion partner in the AcrAB-TolC tripartite efflux system
- [MexB Efflux Pump](/xray-mp-wiki/proteins/mexB/) — Close homologue (RND family efflux pump); similar multidrug-binding cavity mechanism
- [Polyethylene Glycol (PEG)](/xray-mp-wiki/reagents/additives/peg/) — PEG 4000 at 8-10% used as precipitant in AcrB-DARPin complex crystallization
- [RND Efflux Pumps](/xray-mp-wiki/concepts/rnd-efflux-pumps/) — AcrB is the prototypical RND (Resistance Nodulation Division) family efflux pump
- [Multidrug Resistance](/xray-mp-wiki/concepts/multidrug-resistance/) — AcrB is a major contributor to multidrug resistance in Gram-negative bacteria
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent (2% DDM) used for AcrB solubilization and in all purification steps
- [ABI-PP (tert-butyl thiazolyl aminocarboxyl pyridopyrimidine)](/xray-mp-wiki/reagents/ligands/abi-pp/) — First inhibitor-bound structure of AcrB solved; ABI-PP binds to hydrophobic trap in distal pocket
- [Dodecanoyl Sucrose](/xray-mp-wiki/reagents/detergents/dodecanoyl-sucrose/) — Sucrose-based detergent used for crystallization of ABI-PP-bound AcrB and AcrB(F178W) mutant
- [MexY (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/mexY/) — MexY homologue; F178W mutation in AcrB mimics the W177 steric hindrance naturally present in MexY
- [Fusidic Acid](/xray-mp-wiki/reagents/antibiotics/fusidic-acid/) — Lipophilic carboxylated drug that binds to the TM1/TM2 groove of AcrB; crystal structure solved at 2.5 A (PDB 4DX5)
- [Helix Shift Mechanism for Carboxylate Drug Transport](/xray-mp-wiki/concepts/helix-shift-mechanism/) — Mechanism proposed for active transport of carboxylate drugs from the membrane via TM2 helix upward shift
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM co-bound in the TM1/TM2 groove distal to fusidic acid in each AcrB protomer
