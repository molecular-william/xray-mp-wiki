---
title: Yeast V1-ATPase from Saccharomyces cerevisiae
created: 2026-06-09
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.15252##embj.201593447]
verified: false
---

# Yeast V1-ATPase from Saccharomyces cerevisiae

## Overview

V-type ATPase (V-ATPase) is a rotary ATPase complex that couples ATP hydrolysis to proton
pumping across cellular membranes. In Saccharomyces cerevisiae, the ~640 kDa V1 domain
(A3B3CDE3FG3H) catalyzes ATP hydrolysis and undergoes reversible dissociation from the
membrane-embedded Vo domain as a regulatory mechanism. Dissociated V1 is autoinhibited
to prevent wasteful ATP consumption. The X-ray crystal structure of the autoinhibited
yeast V1-ATPase was determined at 6.2-6.5 Å resolution, revealing the molecular mechanism
by which subunit H acts as a molecular brake. The structure shows that the C-terminal
domain of subunit H (HCT) undergoes a ~150° rotation from its position in the holoenzyme
to dock at the bottom of the catalytic hexamer, where it contacts the D subunit and the
open catalytic site, stabilizing an ADP-inhibited state.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.15252##embj.201593447 | 5BW9 | 6.5 A | Not stated in raw paper | Yeast V1-ATPase (A3B3CDE3FG3H) from S. cerevisiae, C subunit deleted for homogeneity | ADP (inhibitory nucleotide, ~1.3 mol/mol V1) |
| doi/10.15252##embj.201593447 | 5D80 | 6.2 A | Not stated in raw paper | Yeast V1-ATPase (A3B3CDE3FG3H) from S. cerevisiae, C subunit deleted for homogeneity | ADP (inhibitory nucleotide) |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae (native yeast strain)
- **Construct**: V1-ATPase complex consisting of A3B3CDE3FG3H subunits; C subunit (VMA5) deleted for homogeneous preparation

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Native expression in Saccharomyces cerevisiae | — | Not specified | V1-ATPase purified from yeast strain deleted for the C subunit (VMA5) to ensure homogeneity; B subunit (VMA2) C-terminally tagged for affinity purification |
| Affinity purification | Affinity capture via tagged B subunit | — | Standard V-ATPase purification buffer | Purified V1 from yeast cytoplasm; [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) precipitation and [Ion-Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) |
| Size-exclusion chromatography | SEC | — | SEC buffer | Final polishing step; V1 elutes as monodisperse ~600 kDa complex |


## Crystallization

### doi/10.15252##embj.201593447

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion / Hanging-drop vapor diffusion |
| Temperature | 20 C |
| Growth time | Variable (multiple datasets collected) |
| Notes | Structure determined from multiple datasets. Initial 7 Å dataset from one crystal
used for [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) with EhA3B3 (Enterococcus hirae A3B3) as search model.
Higher resolution 6.2-6.5 Å datasets collected at APS and NSLS beamlines. Two
independent structures deposited: 5BW9 and 5D80. [NCS](/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/) averaging and density modification
were essential for interpretable maps at this resolution.
 |


## Biological / Functional Insights

### Subunit H as a molecular brake

The C-terminal domain of subunit H (HCT) undergoes a ~150° rotation from its position
in the holo V1Vo complex to dock at the bottom of the V1 catalytic hexamer. In its
inhibitory position, HCT binds simultaneously to the D subunit (central rotor) and the
B subunit of the open catalytic site (AB)1, preventing rotation of the central stalk
and stabilizing an open conformation that traps inhibitory ADP at an adjacent closed site.

### Asymmetric peripheral stalk conformations

The three peripheral stalks (EG1, EG2, EG3) adopt different conformations in the
autoinhibited state. EG1 binds to the N-terminal domain of subunit H (HNT), while EG3
contacts the C-terminal domain of the A subunit at the (AB)2 closed catalytic site.
The EG3 stalk shows a partially disordered "bulge" region in subunit G that provides
flexibility for conformational changes during disassembly. The EG3 N-terminus,
which binds subunit C in the holoenzyme, moves to contact the A subunit C-terminal
domain in the autoinhibited V1.

### Subunit C deletion and purification strategy

Subunit C is released into the cytoplasm during V-ATPase disassembly but variably
co-purifies with V1 (from substoichiometric to significant amounts). Deletion of
subunit C (VMA5) was essential for a homogeneous preparation suitable for crystallization.
The resulting V1 shows no detectable MgATPase activity, confirming that subunit C is
not required for autoinhibition by subunit H.


## Cross-References

- [V1-ATPase from Thermus thermophilus](/xray-mp-wiki/proteins/pumps-atpases/v1-atpase-t-thermophilus/) — Related bacterial V1-ATPase structure used for comparison of catalytic core and rotary mechanism
- [Bovine F1-ATPase](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/) — Related rotary ATPase; comparison of central rotor and catalytic mechanism
- [NCS](/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/) — Related biological concept
- [Ion-Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Additive used in purification or crystallization buffers
