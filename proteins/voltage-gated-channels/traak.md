---
title: Human TRAAK Potassium Channel
created: 2026-05-28
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.neuron.2021.07.009, doi/10.1038##nature22988, doi/10.1016##j.neuron.2014.11.017, doi/10.1038##nature14013, doi/10.1073##pnas.1218950110, doi/10.7554##eLife.50403, doi/10.1126##science.1213808]
verified: false
---

# Human TRAAK Potassium Channel

## Overview

TRAAK (tandem pore domain potassium channel 4, KCNK4) is a mechanosensitive two-pore domain K+ (K2P) channel expressed in the nervous system. It is localized exclusively to nodes of Ranvier in myelinated axons throughout the mammalian central and peripheral nervous system, where it accounts for approximately 20-25% of nodal background K+ conductance, maintaining the resting membrane potential. Approximately 80% of myelinated nerve fibers contain TRAAK in an all-nodes or no-nodes per axon fashion. TRAAK displays basal leak K+ activity that can be activated ~100-fold by mechanical force. Gain-of-function mutations (A198E, A270P) cause the neurodevelopmental disorder FHEIG. The channel is twofold symmetric, formed from two polypeptide chains each encoding two nonidentical repeats corresponding to canonical K+ channel subunits.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.neuron.2021.07.009 | 7LJ5 | 2.3 | P21 | Human TRAAK with N-terminal extension, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) (119 aa removed), His-tag, co-crystallized with mouse monoclonal Fab | K+, Fab |
| doi/10.1016##j.neuron.2021.07.009 | 7LJ6 | 2.7 | P21 | Human TRAAK A198E mutant with N-terminal extension, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/), His-tag, co-crystallized with Fab | K+, Fab |
| doi/10.1016##j.neuron.2021.07.009 | 7LJ7 | 2.9 | P21 | Human TRAAK A270P mutant with N-terminal extension, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/), His-tag, co-crystallized with Fab | K+, Fab |
| doi/10.1016##j.neuron.2021.07.009 | 7LJ8 | 3.3 | P21 | Human TRAAK G158D mutant with N-terminal extension, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/), His-tag | K+ |
| doi/10.1038##nature14013 | 4WFE | 2.5 | P21 | Human TRAAK residues 1-290, N104Q/N108Q, C-terminal PreScission-cleavable EGFP-10xHis tag, co-crystallized with mouse monoclonal 13E9 Fab | K+, Fab (13E9) |
| doi/10.1038##nature14013 | 4WFG | 3.0 | P21 | Human TRAAK residues 1-290, N104Q/N108Q, C-terminal PreScission-cleavable EGFP-10xHis tag, co-crystallized with mouse monoclonal 13E9 Fab | Tl+, Fab (13E9) |
| doi/10.1038##nature14013 | 4WFF | 2.5 | P21 | Human TRAAK residues 1-290, N104Q/N108Q, C-terminal PreScission-cleavable EGFP-10xHis tag, co-crystallized with mouse monoclonal 13E9 Fab | K+, Fab (13E9) |
| doi/10.1038##nature14013 | 4WFH | 3.0 | P21 | Human TRAAK residues 1-290, N104Q/N108Q, C-terminal PreScission-cleavable EGFP-10xHis tag, co-crystallized with mouse monoclonal 13E9 Fab | Tl+, Fab (13E9) |
| doi/10.7554##eLife.50403 | 6PIS | 2.8 | not reported | Mouse TRAAK (human TRAAK 1-26 signal + mouse TRAAK 1-275 N81Q/N84Q) with C-terminal PreScission-cleavable EGFP-10xHis, co-crystallized with Armenian hamster monoclonal 1B10 Fab | K+, Fab (1B10) |
| doi/10.1126##science.1213808 | 3UM7 | 3.8 | P212121 | Human TRAAK residues 1-300 (C-terminally truncated), N104Q/N108Q, no fusion tag | K+ |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: Human TRAAK (UniProt Q9NYG8-2) with additional 26 aa N-terminal extension, C-terminally truncated by 119 aa (residues 1-300 or similar), His-tag
- **Notes**: For 2014 Nature paper, construct was residues 1-290 with N104Q/N108Q and C-terminal PreScission-cleavable EGFP-10xHis fusion. Same construct used for 2021 Neuron paper and 2013 PNAS paper.

### Purification Workflow

*Source: doi/10.1038##nature14013*

- **Expression system**: Pichia pastoris
- **Expression construct**: TRAAK residues 1-290, N104Q/N108Q, C-terminal PreScission-cleavable EGFP-10xHis tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Milling (Retsch MM301) | — | 50 mM Tris pH 8.0, 150 mM KCl + 60 mM DM | Frozen Pichia cells milled 5x3 min at 25 Hz, 1 g pellet per 4 ml lysis buffer with protease inhibitors (pepstatin, leupeptin, aprotinin, soy [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) inhibitor, benzamidine, PMSF) and 0.1 mg/ml DNase I |
| Membrane extraction | Stirring extraction | — | 50 mM Tris pH 8.0, 150 mM KCl + 6 mM DM | Extraction for 3 h stirring at 4 C, followed by centrifugation at 35,000g for 45 min |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Cobalt affinity | Cobalt resin (Clontech) | 50 mM Tris pH 8.0, 150 mM KCl + 6 mM DM | 1 ml resin per 5 g cell pellet, 3 h stirring. Washes in 10 mM, 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); elution in 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) pH 8.0 |
| Tag cleavage | [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) cleavage | — | 50 mM Tris pH 8.0, 150 mM KCl, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) + 6 mM DM | [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) at ~1:50 (wt:wt), incubated with gentle rocking overnight at 4 C |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (GE Healthcare) | 20 mM Tris pH 8.0, 150 mM KCl, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) + 4 mM DM | Concentrated 50 kDa MWCO before SEC |
| Fab complex formation | Complex formation | — | SEC buffer (20 mM Tris pH 8.0, 150 mM KCl, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/)) + 4 mM DM | Purified TRAAK (~10 mg/ml) incubated with purified 13E9 Fab (~30 mg/ml) at 1:2.5 molar ratio for 10 min at 4 C; complex separated from excess Fab on [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) |

### Purification Workflow

*Source: doi/10.1016##j.neuron.2021.07.009*

- **Expression system**: Pichia pastoris
- **Expression construct**: Human TRAAK with N-terminal extension, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/), His-tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Pichia pastoris expression | — |  | Human TRAAK expressed in Pichia pastoris cells |
| Cell lysis | Microfluidizer | — |  |  |
| Membrane collection | Centrifugation | — |  |  |
| Solubilization | Detergent solubilization | — | 1% DM |  |
| Affinity purification | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | 1% DM | His-tag purification with [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) elution at 250 mM |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM Tris (pH 8.8), 150 mM NaCl + 0.03% DM |  |

### Purification Workflow

*Source: doi/10.7554##eLife.50403*

- **Expression system**: Pichia pastoris SMD1163
- **Expression construct**: Human TRAAK 1-26 signal - mouse TRAAK 1-275 (N81Q/N84Q) - PreScission-cleavable EGFP-10xHis

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | [Methanol](/xray-mp-wiki/reagents/additives/methanol/) induction in fermenter | — |  | P. pastoris SMD1163 transformed, expressed via [Methanol](/xray-mp-wiki/reagents/additives/methanol/) induction in fermenter |
| Cell lysis | Milling | — | 50 mM Tris pH 8.0, 150 mM KCl, 60 mM DM | Frozen cells milled with protease inhibitors and DNase I |
| Extraction | Stirring extraction | — | 50 mM Tris pH 8.0, 150 mM KCl + 6 mM DM | 3 h stirring at 4 C, then centrifugation at 35,000g for 45 min |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Cobalt affinity | Cobalt resin | 50 mM Tris pH 8.0, 150 mM KCl + 6 mM DM | 1 mL resin/5 g cell pellet, 3 h stirring. Serial washes with 10 mM, 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); elution with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag cleavage | [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) | — | 50 mM Tris pH 8.0, 150 mM KCl, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) + 6 mM DM | ~1:50 (wt:wt) [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/), overnight at 4 C |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (GE Healthcare) | 20 mM Tris pH 8.0, 150 mM KCl, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) + 1 mM DM | Concentrated 50 kDa MWCO. Peak fractions pooled for subsequent procedures |

### Purification Workflow

*Source: doi/10.1073##pnas.1218950110*

- **Expression system**: Pichia pastoris
- **Expression construct**: Human TRAAK residues 1-300 (C-terminally truncated by 119 aa), N104Q/N108Q, C-terminal PreScission-cleavable EGFP-10xHis fusion (same construct as original TRAAK structure)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Milling (Retsch MM301) | — | 50 mM Tris (pH 8.0), 150 mM KCl, 60 mM DM, 0.1 mg/mL DNase I, protease inhibitors | Frozen Pichia cells milled 5x3 min at 25 Hz, 1 g pellet per 4 mL lysis buffer |
| Membrane preparation | Stirring extraction + centrifugation | — | 6 mM DM | Membranes prepared for 3 h with gentle stirring, then centrifugation at 35,000 x g for 45 min |
| Cobalt [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Cobalt resin (Clontech) | 50 mM Tris (pH 8.0), 150 mM KCl + 6 mM DM | 1 mL resin per 5 g cell pellet; serial washes with 10 mM, 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); elution with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Tag cleavage | [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) | — | 50 mM Tris (pH 8.0), 150 mM KCl, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) + 6 mM DM | ~1:50 (wt:wt) [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/), overnight at 4 C |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (GE Healthcare) | 20 mM Tris (pH 8.0), 150 mM KCl, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) + 4 mM DM | Concentrated using 50-kDa MWCO |

### Purification Workflow

*Source: doi/10.1126##science.1213808*

- **Expression system**: Pichia pastoris
- **Expression construct**: Human TRAAK residues 1-300 (C-terminally truncated by 119 aa), N104Q/N108Q, no fusion tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Pichia pastoris expression | — |  | Human TRAAK recombinantly expressed and purified from Pichia pastoris. Mutations N104Q/N108Q removed N-linked glycosylation sites. |
| Purification | Not detailed in main text | — |  | Full purification details in Supporting Online Material. Construct was truncated at Gln300 to remove predicted intrinsically unstructured C-terminal region. |


## Crystallization

### doi/10.1016##j.neuron.2021.07.009

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Purified TRAAK mutants in 0.03% DM, 20 mM Tris (pH 8.8), 150 mM NaCl, co-crystallized with mouse monoclonal antibody Fab fragment |
| Reservoir | 50 mM Tris (pH 8.8), 64-200 mM CaCl2, 27-33% (vol/vol) [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) |
| Temperature | 4 |
| Growth time | 1-5 weeks |
| Cryoprotection | Mother liquor supplemented to 30% (vol/vol) [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), crystals plunged into liquid nitrogen |
| Notes | Lower calcium concentrations gave increased nucleation and rapid growth |

### doi/10.1038##nature14013

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Purified TRAAK-Fab complex concentrated to 30 mg/ml in SEC buffer (20 mM Tris pH 8.0, 150 mM KCl, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 4 mM DM) for K+ conditions; 150 mM TlNO3 replaced KCl for Tl+ conditions |
| Notes | Drops of 0.25-0.35 ul protein added to equal volume of reservoir |

### doi/10.1073##pnas.1218950110

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (Fab-mediated crystallization) |
| Protein sample | TRAAK-Fab complex (mouse monoclonal Fab against TRAAK) |
| Notes | Mouse monoclonal antibodies raised against TRAAK purified in dodecyl-beta-D-maltopyranoside. Positive clones identified by ELISA and Western blot. Fab from one antibody clone used for crystallization. Diffraction data collected to 2.75 A Bragg spacings. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using a Fab search model. |

### doi/10.1126##science.1213808

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified TRAAK (untagged construct, N104Q/N108Q, truncated to Gln300) in 150 mM KCl |
| Reservoir | 150 mM KCl (native); TINO3 substituted for KCl (derivative) |
| Temperature | 4 |
| Notes | Native crystals diffracted to 3.8 A. Structure solved by multi-wavelength anomalous dispersion (MAD) using TINO3-soaked crystals. Additional CH3Hg+ derivatized crystals used for sequence register assignment. Space group P212121. No Fab or antibody used for crystallization. |


## Biological / Functional Insights

### Domain-swapped chain connectivity in TRAAK

The 2.75-A resolution TRAAK-Fab structure reveals a domain-swapped
chain connectivity in which two opposing outer helices exchange 180
degrees around the channel. This was not apparent in the original
3.8-A structure (PDB 3UM7). The domain swap involves only four
amino acids (His76-Val79) at the top of the helical cap, which adopt
an unambiguous crossover conformation. Fluorescent Fab labeling on
live HEK cells confirmed that domain-swapped TRAAK exists in cell
membranes, suggesting this is the generally correct model.

### Gated membrane side opening

A conformational change in inner helix 2 (IH2) of one subunit seals
a side opening to the membrane bilayer. The intracellular C-terminus
of IH2 is elevated, its extracellular N-terminal end moves, and the
connecting segment undergoes substantial reorganization. New
interactions between Phe272, Val275, Ile279, and Leu283 on IH2 and
residues on IH1 and pore helix 2 close the opening. The other
subunit retains an open conformation similar to the original
structure, suggesting this gating may relate to mechanosensitivity.

### Implications for mechanosensitivity

TRAAK channels gate in response to chemical or mechanical membrane
perturbation. The conformational changes around the selectivity
filter associated with IH2 movement may transmit signals across
the membrane. Although the selectivity filter is not perceptibly
altered, the structural changes around it may alter its dynamics
or dynamics to influence ion conduction. TRAAK is thought to gate
at the selectivity filter rather than through a canonical inner
helical gate.

### Localization to nodes of Ranvier

TRAAK is localized exclusively to nodes of Ranvier throughout the
mammalian central and peripheral nervous system, as shown by
immunohistochemistry with specific monoclonal antibodies. It is not
found in axon initial segments, sensory endings, synapses,
astrocytes, or microglia. Approximately 80% of myelinated nerve
fibers contain TRAAK in an all-nodes or no-nodes per axon fashion.
Within single teased sciatic nerve fibers, all nodes are either
TRAAK-positive or TRAAK-negative, suggesting two distinct classes
of myelinated neurons.

### Role in nodal membrane physiology

TRAAK contributes to the leak K+ current in mammalian nodes of
Ranvier. Using the TRAAK inhibitor RU2 and node-clamp
electrophysiology on rat sciatic nerve fibers, TRAAK was shown to
account for approximately 19% of the total outward nodal current.
TRAAK stabilizes the resting membrane potential by approximately
4 mV hyperpolarization, thereby increasing NaV channel availability
for action potential propagation. Blocking TRAAK with RU2
depolarizes the node, reduces action potential amplitude, and
amplifies spike amplitude rundown during high-frequency (100 Hz)
stimulation.

### Anti-TRAAK monoclonal antibody 1B10 Fab complex structure

The X-ray crystal structure of mouse TRAAK in complex with the
Fab fragment of monoclonal antibody 1B10 was determined at 2.8
angstroms resolution (PDB 6PIS). The antibody binds to a large
1003-square-angstrom epitope spanning both subunits of the dimeric
channel, with cap helix 1 of one protomer forming ~2/3 of the
surface and cap helix 2 from the second protomer forming ~1/3.
Most epitope-forming residues are poorly conserved among K2P
channels, explaining the high specificity for TRAAK.

### Helical cap and extracellular pharmacology of K2P channels

The original 3.8 A TRAAK structure (PDB 3UM7) revealed a
previously unobserved helical cap extending ~35 A above the
membrane, formed by the outer helix-pore helix connection of pore
domain 1. The rigid helical bundle restricts molecular access to
the pore entryway, explaining why K2P channels are resistant to
extracellular pore-blocking toxins that effectively inhibit
tetrameric K+ channels. The cap may also serve as a binding site
for endogenous modulators.

### Two-fold symmetry and fenestrations

TRAAK forms a two-fold symmetric dimer with two non-identical pore
domains per protomer, unlike canonical four-fold symmetric K+
channels. Despite overall asymmetry, the selectivity filter
converges to nearly perfect four-fold symmetry (RMSD 0.6 A vs
[KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/)). Openings between subunits (fenestrations) expose the central
cavity to the lipid membrane, providing access for hydrophobic
inhibitors and coupling membrane properties to channel gating.
Electron density within fenestrations is consistent with bound
alkyl chains of ~11 carbons.

### Amphipathic helix as mechanosensitive element

The pore domain 1 inner helix kinks at Pro155 and projects
laterally along the cytoplasmic membrane surface. This amphipathic
extension, with hydrophobic residues on one face and basic residues
(Arg167, Arg173, His174, His178, Lys185) on the other, is
positioned to interact with both lipid tails and acidic head groups.
This tendril-like structure may be the molecular sensor for TRAAK's
response to mechanical and chemical properties of the lipid bilayer.


## Cross-References

- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Primary solubilization detergent (1% for solubilization, 0.03-0.4% for final sample)
- [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) — PEG400 (27-33%) used as crystallization precipitant and cryoprotectant
- [Calcium Chloride (CaCl2)](/xray-mp-wiki/reagents/additives/calcium-chloride/) — 64-200 mM CaCl2 in crystallization reservoir
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — 50 mM Tris (pH 8.8) in crystallization and 20 mM Tris (pH 8.8) in purification buffer
- [Pichia pastoris Expression System](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/) — TRAAK expressed in Pichia pastoris
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Crystallization method used for all TRAAK structures
- [K2P 2.1 (TREK-1) Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/k2p-2-1-trek-1/) — Related mechanosensitive K2P channel with shared gating mechanism
- [KcsA Potassium Channel](/xray-mp-wiki/proteins/kcsA/) — Canonical K+ channel used for structural comparison; TRAAK differs in fourfold vs twofold symmetry and domain-swapped connectivity
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
