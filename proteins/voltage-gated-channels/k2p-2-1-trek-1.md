---
title: "K2P 2.1 (TREK-1) Potassium Channel"
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature22988, doi/10.1126##sciadv.abc9174]
verified: false
---

# K2P 2.1 (TREK-1) Potassium Channel

## Overview

K2P 2.1 (also known as TREK-1, encoded by KCNK2) is a polymodal thermo- and mechanosensitive two-pore domain potassium channel of the TREK subfamily. It generates leak currents that regulate neuronal excitability and responds to lipids, temperature, and mechanical stretch. Unlike other potassium channels, K2P channels use a selectivity filter C-type gate as the principal gating site. Structural studies have revealed a cryptic binding pocket at the P1-M4 intrasubunit interface behind the selectivity filter and have uncovered unprecedented asymmetric, potassium-dependent conformational changes that underlie K2P C-type gating. These include order-disorder transitions in the selectivity filter that encompass SF1 pinching and SF2 dilation, disrupting the S1 and S2 ion binding sites.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature22988 | 5VK5 | 3.1 A | P212121 | K2P 2.1cryst (residues 21-322) with surface mutations K84R, Q85E, T86K, I88L, A89R, Q90A, A92P, N95S, S96D, D797Q, N119A, S300A, E306A; domain-swapped M1 helix, extracellular CAP domain, C-terminal tail (residues 307-321), unimpeded aqueous path between intracellular side and selectivity filter. C-terminal TEV cleavage site and GFP for [FSEC](/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/) screening. | K+ ions at selectivity filter sites S1-S4 |
| doi/10.1038##nature22988 | 5VKN | 3.0 A | P212121 | K2P 2.1cryst same construct as 5VK5, co-crystallized with [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/) activator | K+ ions, [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/) (2 molecules per channel) |
| doi/10.1038##nature22988 | 5VKP | 2.8 A | P212121 | K2P 2.1cryst same construct as 5VK5, co-crystallized with [ML402 (thiophene-carboxamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml402/) activator | K+ ions, [ML402 (thiophene-carboxamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml402/) (2 molecules per channel) |
| doi/10.1126##sciadv.abc9174 | 6W7B | 3.3-3.9 A |  | K2P 2.1cryst (same construct as 5VK5) crystallized at seven potassium concentrations (0, 1, 10, 30, 50, 100, 200 mM [K+]) and in complex with [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/) |  |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: K2P 2.1cryst (residues 21-322) with additional C-terminal GFP and His10 tag. Cloned into pPICZ vector. Plasmids linearized with PmeI and transformed into P. pastoris SMD1163H by electroporation. Multi-integration recombinants selected on zeocin plates (1-4 mg/ml).
- **Notes**: Construct K2P 2.1cryst identified through [FSEC](/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/) screening of mutants and deletion constructs expressed in HEK293 cells.

### Purification Workflow

- **Expression system**: Pichia pastoris SMD1163H
- **Expression construct**: K2P 2.1cryst (residues 21-322), C-terminal GFP-His10 tag
- **Tag info**: C-terminal His10 tag via GFP fusion

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Construct screening | [FSEC](/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/) (fluorescence-detection size-exclusion chromatography) | -- | -- + -- | Set of mutants and deletion constructs expressed in HEK293 cells screened for expression level and peak quality using [FSEC](/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/). Construct K2P 2.1cryst identified as optimal. |
| Large-scale expression | Pichia pastoris fermentation in 7L Bioreactor | -- | Minimal medium (4% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.93 g/l CaSO4·2H2O, 18.2 g/l K2SO4, 14.9 g/l MgSO4·7H2O, 9 g/l (NH4)2SO4, 25 g/l sodium hexametaphosphate, PTM1 trace metals) + -- | Fed-batch phase at 15-30% pump speed until wet cell mass reached ~250 g/l. pH maintained at 5.0 by 30% ammonium hydroxide. pO2 kept at minimum 30%. |
| Cell harvesting and membrane preparation | Centrifugation | -- | -- + -- | Cells pelleted by centrifugation (3,000g, 10 min, 20C). Membranes prepared for solubilization. |
| Solubilization | Detergent solubilization | -- | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Membranes solubilized in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) detergent. |
| Affinity purification | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | His10-tag purification. |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM Tris (pH 8.0), 150 mM NaCl + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final sample buffer: 20 mM Tris (pH 8.0), 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/). |

**Final sample**: Purified in 20 mM Tris (pH 8.0), 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)


## Crystallization

### doi/10.1038##nature22988

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Purified K2P 2.1cryst in 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 20 mM Tris (pH 8.0), 150 mM NaCl |
| Reservoir | -- |
| Mixing ratio | -- |
| Temperature | 4 C |
| Growth time | -- |
| Cryoprotection | Crystals flash-frozen in liquid nitrogen |
| Notes | All three structures (unliganded, [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/), [ML402 (thiophene-carboxamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml402/)) crystallized in space group P212121 with similar unit cell dimensions. Crystal lattice contacts involve C-terminal tails from adjacent symmetry mates, stabilized by cadmium ions coordinated between His313 residues of adjacent channels. Structures solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/). |

### doi/10.1126##sciadv.abc9174

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Purified K2P 2.1cryst concentrated to 6 mg/ml |
| Reservoir | 20-25% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 200 mM KCl, 1 mM CdCl2, 100 mM HEPES (pH 8.0) |
| Mixing ratio | 0.2 ul protein + 0.1 ul precipitant over 100 ul reservoir |
| Temperature | 4 C |
| Growth time | 12 hours to full size (200-300 um) in ~1 week |
| Cryoprotection | Buffer D (200 mM KCl, 0.2% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/), 15 mM HTG, 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 1 mM CdCl2, 100 mM HEPES pH 8.0) with 5% step increases of [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) up to 38%. After cryoprotection, crystals incubated for 8 hours in buffer E (38% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 0.2% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/), 15 mM HTG, 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 1 mM CdCl2, 100 mM HEPES pH 8.0) containing appropriate [K+] before freezing. |
| Notes | Structures determined at seven potassium concentrations (0, 1, 10, 30, 50, 100, 200 mM [K+]) and in the presence of [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/) activator. |


## Biological / Functional Insights

### Asymmetric order-disorder transitions in K2P C-type gating

Low potassium concentrations evoke asymmetric conformational changes in the K2P 2.1 selectivity filter. SF1 undergoes pinching at its extracellular side, exposing Asn147 side chains. SF2 and the SF2-M4 loop undergo unwinding and dilation. These changes destroy the S1 and S2 ion binding sites while S3 and S4 sites persist. The two classes of C-type gating (SF1 pinching and SF2 dilation) operate simultaneously in one channel, leveraging the fundamentally heterodimeric K2P architecture.

### M3 glutamate network supports SF2-M4 loop stability

A conserved hydrogen bond network centered on Glu234 (M3 helix), Gly260 (SF2-M4 loop backbone amide), and Tyr270 (M4) supports the SF2-M4 loop structure. Disruption of this network (E234Q, Y270F mutants) enhances C-type gating and blunts responses to temperature, pressure, and [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/) activation. The network is conserved across K2P subfamilies including K2P 3.1 (TASK-1).

### ML335 stabilizes the C-type gate by rigidifying the P1-M4 interface

The K2P activator [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/) binds to the P1-M4 intrasubunit interface ([K2P Modulator Pocket](/xray-mp-wiki/concepts/miscellaneous/k2p-modulator-pocket/)) and stabilizes the SF2-M4 loop. ML335-bound structures show canonical selectivity filter conformations with ions at all four sites (S1-S4) at all potassium concentrations tested. [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/) increases the strength of the Glu234 hydrogen bonding network and suppresses potassium-dependent loop dynamics. Single-channel recordings show [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/) increases open probability.

### SF2-M4 loop integrates diverse gating cues

The uniquely long K2P SF2-M4 loop (6-8 residues longer than canonical potassium channel loops) transduces gating signals from temperature, pressure, and intracellular C-terminal tail to the selectivity filter C-type gate. Shortening the SF2-M4 loop (Loop2sym6 mutant) or disrupting the Glu234 network blunts responses to these stimuli. The loop is a central element of K2P gating and a target for modulator development.


## Cross-References

- [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/) — K2P 2.1 activator co-crystallized (PDB 5VKN, this paper); stabilizes C-type gate by rigidifying P1-M4 interface
- [C-type Inactivation](/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/) — K2P channels use C-type gate as principal gating site; this paper reveals asymmetric SF1 pinching and SF2 dilation mechanisms
- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — Homotetrameric model system; SF1 pinching mechanism of C-type gating shared with K2P channels
- [Human TRAAK Potassium Channel (K2P 4.1)](/xray-mp-wiki/proteins/voltage-gated-channels/traak/) — K2P family member; SF2-M4 loop length comparison across K2P subtypes
- [Human K2P2.1 (TREK-1) Potassium Channel I110D Mutant](/xray-mp-wiki/proteins/voltage-gated-channels/k2p2-1/) — Alternative K2P2.1 construct; RuR inhibition independent of C-type gate activation
- [Human TASK-1 (K2P 3.1)](/xray-mp-wiki/proteins/voltage-gated-channels/human-task-1-k2p3-1/) — K2P subfamily; M3 glutamate network conserved (Glu182, Tyr220); Y220F mutation destabilizes C-type gate
- [K2P Modulator Pocket](/xray-mp-wiki/concepts/miscellaneous/k2p-modulator-pocket/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [FSEC](/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
