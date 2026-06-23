---
title: Cruxrhodopsin-3 (cR3) from Haloarcula vallismortis
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1371##journal.pone.0108362]
verified: false
---

# Cruxrhodopsin-3 (cR3) from Haloarcula vallismortis

## Overview

Cruxrhodopsin-3 (cR3) is a light-driven proton pump from the archaeon Haloarcula vallismortis, belonging to the microbial rhodopsin family. It forms a trimeric assembly in the claret membrane with [Bacterioruberin](/xray-mp-wiki/reagents/lipids/bacterioruberin/) bound to crevices between neighboring subunits. The crystal structure was solved at 2.1 Å resolution in space group P321 using the membrane fusion method. cR3 exhibits several distinctive structural features including a long DE loop that stabilizes the trimer, a bent helix E creating a large cytoplasmic cavity, and a rigid retinal-binding pocket that slows the K-state decay in the photocycle.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1371##journal.pone.0108362 | ~ | 2.1 | P321 | Full-length cR3 (wild-type) |  |

## Expression and Purification

- **Expression system**: Native Haloarcula vallismortis cells transformed with cop3 gene; claret membrane vesicles isolated by repeated washing with distilled water

- **Construct**: Full-length cR3
- **Notes**: Claret membrane containing cR3 as the major protein was isolated from transformed H. salinarum cells

### Purification Workflow

- **Expression system**: Haloarcula vallismortis (transformed H. salinarum)
- **Expression construct**: Full-length cR3

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvesting | Centrifugation | — |  | Cells transformed with cop3 gene were harvested and washed repeatedly with distilled water |
| Membrane isolation | Differential centrifugation | — |  | Claret membrane vesicles containing cR3 as the major protein were isolated; absorption peaks at 475, 505, 541 [NM](/xray-mp-wiki/reagents/detergents/nm/) ([Bacterioruberin](/xray-mp-wiki/reagents/lipids/bacterioruberin/)) and ~560 [NM](/xray-mp-wiki/reagents/detergents/nm/) ([Retinal](/xray-mp-wiki/reagents/ligands/retinal/)) |


## Crystallization

### doi/10.1371##journal.pone.0108362

| Parameter | Value |
|---|---|
| Method | Membrane fusion / sitting drop vapor diffusion |
| Protein sample | Claret membrane (~3 mg/ml cR3) solubilized with [NG](/xray-mp-wiki/reagents/detergents/nonylglucoside/) |
| Reservoir | 2.2-2.8 M ammonium sulfate, 0.1 M sodium [Citrate](/xray-mp-wiki/reagents/buffers/citrate/) (pH 4) |
| Mixing ratio | Not specified |
| Temperature | 15 |
| Growth time | ~1 month |
| Cryoprotection | Soaked in 2.2 M ammonium sulfate, 0.1 M pH buffer ([Hepes](/xray-mp-wiki/reagents/buffers/hepes/) or [Citrate](/xray-mp-wiki/reagents/buffers/citrate/)), 30% [Trehalose](/xray-mp-wiki/reagents/trehalose/) for ~10 min; flash-cooled in liquid propane |
| Notes | Mixture contained claret membrane (~3 mg/ml), 5 mg/ml [NG](/xray-mp-wiki/reagents/detergents/nonylglucoside/), 1 M ammonium sulfate, 0.08 M sodium chloride, 0.04 M sodium azide, 0.04 M sodium [Citrate](/xray-mp-wiki/reagents/buffers/citrate/) (pH 4). Trigonal crystals (P321) with typical size 50x50x5 um^3. Crystal maintained trimeric assembly with [Bacterioruberin](/xray-mp-wiki/reagents/lipids/bacterioruberin/) bound. |


## Biological / Functional Insights

### Trimeric assembly with bacterioruberin stabilizes the proton pump

cR3 forms a trimeric structure in the P321 crystal, with [Bacterioruberin](/xray-mp-wiki/reagents/lipids/bacterioruberin/) bound to crevices between neighboring subunits. The DE loop is unusually long and extends toward a neighboring subunit, forming hydrogen bonds with the N-terminal polypeptide and helix B. Additional inter-subunit hydrogen bonds occur between helix D (Asn104, Arg105) and helix A (Ser35, Gln38, Lys39) of the neighboring subunit. This trimeric architecture is conserved among microbial rhodopsins crystallized by the membrane fusion method (bR, aR2, dR3, pHR).

### Rigid retinal-binding pocket slows K-state decay

The decay rate of the K state in cR3 (~30 us at 24°C) is ten times slower than in bR (~3 us). This is attributed to a more rigid environment around the C13 methyl of [Retinal](/xray-mp-wiki/reagents/ligands/retinal/). Leu149 (replacing Met145 in bR) pushes the indole ring of Trp186 toward helix G, restricting its motional freedom. The conformational relaxation of [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) from a twisted 13-cis configuration to a planar configuration (the K-to-L transition) is inhibited by this rigid packing.

### Bent helix E creates a pre-formed cavity for rapid proton uptake

The cytoplasmic end of helix E is greatly bent, creating a large cavity between helices E and F that can accommodate a water molecule. This cavity is near Arg179 (the counterpart of Lys215 in pHR, which forms a linear water cluster during proton pumping). The pre-formed cavity likely facilitates rapid formation of a water cluster during the M-to-N transition, explaining why this transition occurs much faster in cR3 than in bR.

### Photostability depends on trimeric assembly

In the membrane state, photobleaching of [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) scarcely occurs in cR3. Upon solubilization with excess [NG](/xray-mp-wiki/reagents/detergents/nonylglucoside/), the trimeric assembly dissociates into monomers and photobleaching becomes significant. Blue-native PAGE confirmed that cR3 maintains a trimeric assembly at low detergent concentrations (13 mM [NG](/xray-mp-wiki/reagents/detergents/nonylglucoside/)) but dissociates at higher concentrations. This demonstrates that the trimeric structure and native protein-lipid interactions protect [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) from photobleaching.

### Conserved proton-release pathway with paired glutamate structure

The paired structure of two glutamates (Glu198 and Glu208 in cR3) in the proton-release channel is conserved among aR2, bR, cR3, and dR3. The close distance (2.4 Å) between these residues is explained by a low-barrier hydrogen bond. In the P321 crystal of cR3, this neutral purple form was stable across pH 4-7, unlike bR where the paired structure can be disrupted at extreme pH or in certain crystal forms.


## Cross-References

- [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) — cR3 is a microbial rhodopsin (light-driven proton pump) with the conserved seven-transmembrane helix architecture and retinal chromophore
- [Bacterioruberin](/xray-mp-wiki/reagents/lipids/bacterioruberin/) — Bacterioruberin binds to inter-subunit crevices in the cR3 trimer, strengthening the trimeric assembly
- [Nonyl-beta-D-glucopyranoside](/xray-mp-wiki/reagents/detergents/nonyl-beta-d-glucopyranoside/) — Detergent used for cR3 solubilization and crystallization; excess concentration causes trimer dissociation and photobleaching
- [Bacterioruberin](/xray-mp-wiki/reagents/lipids/bacterioruberin/) — Referenced in the context of Bacterioruberin
- [NM](/xray-mp-wiki/reagents/detergents/nm/) — Referenced in the context of NM
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Referenced in the context of Retinal
- [NG](/xray-mp-wiki/reagents/detergents/nonylglucoside/) — Referenced in the context of NG
- [Citrate](/xray-mp-wiki/reagents/buffers/citrate/) — Referenced in the context of Citrate
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in the context of Hepes
- [Trehalose](/xray-mp-wiki/reagents/trehalose/) — Referenced in the context of Trehalose
