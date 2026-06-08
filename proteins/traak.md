---
title: Human TRAAK Potassium Channel
created: 2026-05-28
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.neuron.2021.07.009, doi/10.1038##nature22988]
verified: false
---

# Human TRAAK Potassium Channel

## Overview

TRAAK (tandem pore domain potassium channel 4, KCNK4) is a mechanosensitive two-pore domain K+ (K2P) channel expressed in the nervous system of jawed vertebrates. It is localized to nodes of Ranvier in myelinated axons where it accounts for approximately 25% of nodal background K+ conductance, maintaining the resting membrane potential and voltage-gated Na+ channel availability required for high-frequency spiking. TRAAK displays basal (leak) K+ activity that can be activated approximately 100-fold by mechanical force. Gain-of-function mutations (A198E, A270P) cause the neurodevelopmental disorder FHEIG (facial dysmorphism, hypertrichosis, epilepsy, intellectual disability, and gingival outgrowth). This paper reports four crystal structures of TRAAK revealing distinct basal and mechanically activated open states.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.neuron.2021.07.009 | 7LJ5 | 2.3 A | P21 | Human TRAAK (KCNK4, UniProt Q9NYG8-2) with N-terminal extension, C-terminal truncation (119 aa removed), His-tag, co-crystallized with mouse monoclonal antibody Fab fragment, grown in K+ | K+ (crystallized in KCl), Fab fragment |
| doi/10.1016##j.neuron.2021.07.009 | 7LJ6 | 2.7 A | P21 | Human TRAAK (KCNK4, UniProt Q9NYG8-2) A198E mutant with N-terminal extension, C-terminal truncation (119 aa removed), His-tag, co-crystallized with mouse monoclonal antibody Fab fragment, grown in K+ | K+ (crystallized in KCl), Fab fragment |
| doi/10.1016##j.neuron.2021.07.009 | 7LJ7 | 2.9 A | P21 | Human TRAAK (KCNK4, UniProt Q9NYG8-2) A270P mutant with N-terminal extension, C-terminal truncation (119 aa removed), His-tag, co-crystallized with mouse monoclonal antibody Fab fragment, grown in K+ | K+ (crystallized in KCl), Fab fragment |
| doi/10.1016##j.neuron.2021.07.009 | 7LJ8 | 3.3 A | P21 | Human TRAAK (KCNK4, UniProt Q9NYG8-2) G158D mutant with N-terminal extension, C-terminal truncation (119 aa removed), His-tag, grown in K+ | K+ (crystallized in KCl) |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: Human TRAAK (UniProt Q9NYG8-2) with additional 26 amino acid N-terminal sequence for improved heterologous expression, C-terminally truncated by 119 amino acids, His-tag for purification. Cloned into PGEM vector. Plasmids available upon request.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Pichia pastoris expression | -- | -- + -- | Human TRAAK expressed in Pichia pastoris cells |
| Cell lysis | Microfluidizer | -- | -- + -- | Cells lysed using microfluidizer |
| Membrane collection | Centrifugation | -- | -- + -- | Membrane fraction collected by centrifugation |
| Solubilization | Detergent solubilization | -- | -- + 1% DM | Membranes solubilized in 1% DM |
| Affinity purification | Ni-NTA affinity chromatography | Ni-NTA | -- + 1% DM | His-tag purification with imidazole elution at 250 mM |
| Size-exclusion chromatography | SEC | Superdex 200 | 20 mM Tris (pH 8.8), 150 mM NaCl + 0.03% DM | Final sample buffer: 20 mM Tris (pH 8.8), 150 mM NaCl, 0.03% DM |


## Crystallization

### doi/10.1016##j.neuron.2021.07.009

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Purified TRAAK mutants in 0.03% DM, 20 mM Tris (pH 8.8), 150 mM NaCl, co-crystallized with mouse monoclonal antibody Fab fragment |
| Reservoir | 50 mM Tris (pH 8.8), 64-200 mM CaCl2, 27-33% (vol/vol) PEG400 |
| Temperature | 4 C |
| Growth time | 1-5 weeks |
| Cryoprotection | Mother liquor supplemented to 30% (vol/vol) PEG400, crystals transferred with cryoloop and plunged into liquid nitrogen |
| Notes | Lower calcium concentrations gave increased nucleation and rapid growth. A198E crystals grew to ~100 um x 100 um x 200 um. A270P and G158D crystals rarely exceeded 70 um x 70 um x 100 um after 5 weeks. Structures solved by molecular replacement using Phaser with input models from PDB 4WFF (G158D) and PDB 4WFE (A198E, A270P). |


## Biological / Functional Insights

### Distinct basal and mechanically activated open states

TRAAK displays two physically distinct open states. Basal openings are low conductance (~1 pA), short duration (~1 ms), and correspond to a TM4-down conductive conformation. Mechanically gated openings are high conductance (~2 pA), long duration (~3 ms or longer), and correspond to a TM4-up conductive conformation. Mechanical force favors the TM4-up state because it involves an expansion in cross-sectional area and increase in cylindricity, which are energetically favored by membrane tension. The TM4-up open state seals the lateral membrane opening above TM4, preventing hydrophobic acyl chains from accessing the channel cavity. The TM4-down state permits hydrophobic acyl chains to access the cavity and block ion passage (lipid-blocked state).

### FHEIG syndrome mutations promote mechanically activated open state

The FHEIG syndrome-causing mutations TRAAK_A198E and TRAAK_A270P promote the high-conductance, long-duration TM4-up open state. TRAAK_A198E has an open probability >= 0.9 at rest, and TRAAK_A270P openings are nearly all high conductance (~2 pA) and long duration (~3 ms or longer). The A270P mutation produces a kink in TM4 that closely approximates the WT TM4-up conformation, creating an approximately 27 degree bend and approximately 9.5 A upward movement of TM4 relative to the WT TM4-down state.

### Pan-K2P activating mutation promotes basal open state

The TRAAK_G158D mutation is a pan-K2P gain-of-function mutation that promotes the low-conductance, short-duration TM4-down open state. It has a resting open probability of approximately 0.7, much higher than WT (~0.04). The mutation increases the polarity of the channel cavity, disfavoring occupancy of hydrophobic acyl chains and preventing lipid-mediated block. Mechanical activation of G158D involves an increase in both open probability and conductance, similar to WT, but with a correspondingly smaller maximum effect due to the high basal activity.

### Four-state kinetic model for TRAAK gating

An integrated four-state kinetic model maps structural conformations to TRAAK gating. C1 (long-duration closed) corresponds to the TM4-down lipid-blocked conformation. O1 (low-conductance, short-duration open) corresponds to the TM4-down conductive conformation. O2 (high-conductance, long-duration open) corresponds to the TM4-up conductive conformation. C2 (short-duration closed) has no defined structural correlate but may represent gating at the selectivity filter or cavity dewetting. Under basal conditions, WT transitions between C1, O1, and C2. FHEIG mutants (A198E, A270P) transition primarily between O2 and C2. G158D transitions between O1 and C2.


## Cross-References

- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/decylmaltoside/) — Primary solubilization detergent (1% for solubilization, 0.03% for final sample)
- [Polyethylene Glycol (PEG)](/xray-mp-wiki/reagents/additives/peg/) — PEG400 (27-33%) used as crystallization precipitant and cryoprotectant
- [Calcium Chloride (CaCl2)](/xray-mp-wiki/reagents/additives/calcium-chloride/) — 64-200 mM CaCl2 in crystallization reservoir
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — 50 mM Tris (pH 8.8) in crystallization and 20 mM Tris (pH 8.8) in purification buffer
- [Pichia pastoris Expression System](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/) — TRAAK expressed in Pichia pastoris with modified construct
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Crystallization method used for all four TRAAK structures
- [Channel Gating via Plug Domain Displacement](/xray-mp-wiki/concepts/channel-gating/) — Related channel gating mechanism; TRAAK gating involves TM4 movement and lipid-blocked states
- [Conformational Dynamics in MFS Transporters](/xray-mp-wiki/concepts/conformational-dynamics-mfs/) — Related conformational dynamics; TRAAK transitions between distinct conformational states
- [K2P 2.1 (TREK-1) Potassium Channel](/xray-mp-wiki/proteins/k2p-2-1-trek-1/) — K2P 2.1 activators ML335 and ML402 target the same modulator pocket; K2P 4.1(Q258K) shows reversed activation phenotype
- [C-type Inactivation](/xray-mp-wiki/concepts/c-type-inactivation/) — K2P channels use C-type gate at selectivity filter as principal gating site; modulator pocket controls gate dynamics
