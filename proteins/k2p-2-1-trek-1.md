---
title: K2P 2.1 (TREK-1) Potassium Channel
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature22988]
verified: false
---

# K2P 2.1 (TREK-1) Potassium Channel

## Overview

K2P 2.1 (also known as TREK-1, encoded by KCNK2) is a polymodal thermo- and mechanosensitive two-pore domain potassium channel of the TREK subfamily. It generates leak currents that regulate neuronal excitability and responds to lipids, temperature, and mechanical stretch. Unlike other potassium channels, K2P channels use a selectivity filter C-type gate as the principal gating site. This paper reports three crystal structures of K2P 2.1 alone and in complex with two selective activators (ML335 and ML402), revealing a cryptic binding pocket at the P1-M4 intrasubunit interface behind the selectivity filter. The activators function as molecular wedges that stabilize the C-type gate in the leak mode.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature22988 | 5VK5 | 3.1 A | P212121 | K2P 2.1cryst (residues 21-322) with surface mutations K84R, Q85E, T86K, I88L, A89R, Q90A, A92P, N95S, S96D, D797Q, N119A, S300A, E306A; domain-swapped M1 helix, extracellular CAP domain, C-terminal tail (residues 307-321), unimpeded aqueous path between intracellular side and selectivity filter. C-terminal TEV cleavage site and GFP for FSEC screening. | K+ ions at selectivity filter sites S1-S4 |
| doi/10.1038##nature22988 | 5VKN | 3.0 A | P212121 | K2P 2.1cryst same construct as 5VK5, co-crystallized with ML335 activator | K+ ions, ML335 (2 molecules per channel) |
| doi/10.1038##nature22988 | 5VKP | 2.8 A | P212121 | K2P 2.1cryst same construct as 5VK5, co-crystallized with ML402 activator | K+ ions, ML402 (2 molecules per channel) |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: K2P 2.1cryst (residues 21-322) with additional C-terminal GFP and His10 tag. Cloned into pPICZ vector. Plasmids linearized with PmeI and transformed into P. pastoris SMD1163H by electroporation. Multi-integration recombinants selected on zeocin plates (1-4 mg/ml).

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Construct screening | FSEC (fluorescence-detection size-exclusion chromatography) | -- | -- + -- | Set of mutants and deletion constructs expressed in HEK293 cells screened for expression level and peak quality using FSEC. Construct K2P 2.1cryst (residues 21-322) identified as optimal. |
| Large-scale expression | Pichia pastoris fermentation in 7L Bioreactor | -- | Minimal medium (4% glycerol, 0.93 g/l CaSO4·2H2O, 18.2 g/l K2SO4, 14.9 g/l MgSO4·7H2O, 9 g/l (NH4)2SO4, 25 g/l sodium hexametaphosphate, PTM1 trace metals) + -- | Fed-batch phase at 15-30% pump speed until wet cell mass reached ~250 g/l. pH maintained at 5.0 by 30% ammonium hydroxide. pO2 kept at minimum 30%. |
| Cell harvesting and membrane preparation | Centrifugation | -- | -- + -- | Cells pelleted by centrifugation (3,000g, 10 min, 20C). Membranes prepared for solubilization. |
| Solubilization | Detergent solubilization | -- | -- + DDM | Membranes solubilized in DDM detergent. |
| Affinity purification | Ni-NTA affinity chromatography | Ni-NTA | -- + DDM | His10-tag purification. |
| Size-exclusion chromatography | SEC | Superdex 200 | 20 mM Tris (pH 8.0), 150 mM NaCl + 0.03% DDM | Final sample buffer: 20 mM Tris (pH 8.0), 150 mM NaCl, 0.03% DDM. |


## Crystallization

### doi/10.1038##nature22988

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Purified K2P 2.1cryst in 0.03% DDM, 20 mM Tris (pH 8.0), 150 mM NaCl |
| Reservoir | -- |
| Temperature | 4 C |
| Growth time | -- |
| Cryoprotection | Crystals flash-frozen in liquid nitrogen |
| Notes | All three structures (unliganded, ML335, ML402) crystallized in space group P212121 with similar unit cell dimensions. Crystal lattice contacts involve C-terminal tails from adjacent symmetry mates, stabilized by cadmium ions coordinated between His313 residues of adjacent channels. Structures solved by molecular replacement. |


## Biological / Functional Insights

### Cryptic K2P modulator pocket at the P1-M4 interface

ML335 and ML402 bind to an L-shaped pocket behind the selectivity filter, formed by the P1 pore helix and M4 transmembrane helix intrasubunit interface. Two activator molecules bind per channel dimer. The pocket is unlike other ion channel small-molecule binding sites and defines the first VGIC superfamily pore domain small-molecule activator site. The pocket differs from antagonist sites occupying lateral fenestrations below the selectivity filter. All these small-molecule sites are found at interfaces that move during gating.

### Molecular wedge mechanism of C-type gate activation

ML335 and ML402 function as molecular wedges that restrict interdomain interface movement behind the selectivity filter. The main action of the activators appears to be limiting the conformations sampled by P1-M4 interface elements. The activator-bound selectivity filter is compatible with the up M4 conformation. Direct C-type gate activators stimulate function by reducing the dynamics of the selectivity filter and surrounding structure.

### Cation-pi interaction controls selectivity

Lys271 forms a cation-pi interaction with both ML335 and ML402. Swapping the Lys271 equivalent between K2P 2.1 and K2P 4.1 resulted in a clear phenotype reversal for ML335 and ML402 activation. K2P 2.1(K271Q) was insensitive to ML335 and ML402, whereas K2P 4.1(Q258K) became activated. This cation-pi interaction is a key determinant of activator selectivity.

### C-type gate activation eliminates flux-dependent rectification

ML335 and ML402 activate K2P 2.1 in HEK293 cells and Xenopus oocytes, essentially eliminating flux-dependent outward rectification. The rectification coefficient (I+100mV/I-100mV) approaches 1 upon activator binding, matching physiological activator effects. The K2P 4.1(G124I) gain-of-function mutation reshapes the K2P modulator pocket through structural consequences similar to ML335/ML402 binding, establishing that K2P modulator pocket manipulation directly activates the selectivity filter C-type gate.


## Cross-References

- [ML335 (N-aryl-sulfonamide activator)](/xray-mp-wiki/reagents/ligands/ml335/) — K2P 2.1 activator co-crystallized (PDB 5VKN), EC50 = 14.3 uM for K2P 2.1
- [ML402 (thiophene-carboxamide activator)](/xray-mp-wiki/reagents/ligands/ml402/) — K2P 2.1 activator co-crystallized (PDB 5VKP), EC50 = 13.7 uM for K2P 2.1
- [Human TRAAK Potassium Channel (K2P 4.1)](/xray-mp-wiki/proteins/traak/) — K2P 4.1 (TRAAK) discussed as comparison; K2P 4.1(Q258K) shows reversed activation phenotype; K2P 4.1(G124I) mutant mimics activator binding
- [C-type Inactivation](/xray-mp-wiki/concepts/c-type-inactivation/) — K2P channels use C-type gate as principal gating site; activators stabilize C-type gate leak mode
- [Ion Channel Selectivity Filter](/xray-mp-wiki/concepts/selectivity-filter/) — Selectivity filter S1-S4 sites occupied by potassium ions; C-type gate at selectivity filter is principal gating site
- [Pichia pastoris Expression System](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/) — K2P 2.1cryst expressed in Pichia pastoris SMD1163H
- [Fluorescence Size-Exclusion Chromatography (FSEC)](/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/) — FSEC used for construct screening to identify optimal K2P 2.1cryst construct
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Vapor diffusion crystallization method used for all three K2P 2.1 structures
