---
title: Eca CLCF (CLC-type F-/H+ Antiporter from Enterococcus casseliflavus)
created: 2026-06-22
updated: 2026-06-22
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-018-0082-0]
verified: false
---

# Eca CLCF (CLC-type F-/H+ Antiporter from Enterococcus casseliflavus)

## Overview

Eca CLCF is a fluoride/proton (F-/H+) antiporter from the bacterium
Enterococcus casseliflavus, belonging to the CLCF clade of the CLC
superfamily of anion transport proteins. It exports F- from the
cytoplasm to combat fluoride toxicity. Unlike conventional Cl-/H+
CLC antiporters, Eca displays 1:1 F-/H+ stoichiometry (versus 2:1
for Cl- CLCs) and lacks the conserved Cl--coordinating serine
residue. Crystal structures were captured in two novel conformations
with simultaneous accessibility of F- and H+ via separate pathways
on opposite sides of the membrane, leading to a proposed 'windmill'
model of antiport.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41594-018-0082-0 | 6D0J | 3.0 | P2(1)2(1)2(1) | WT Eca with M4I mutation, C-terminal His6; monobody chaperone X1 | F- |
| doi/10.1038##s41594-018-0082-0 | 6D0K | 3.35 | P2(1)2(1)2(1) | E118Q mutant, C-terminal His6; monobody chaperone X1 |  |
| doi/10.1038##s41594-018-0082-0 | 6D0N | 3.12 | P2(1)2(1)2(1) | V319G mutant, C-terminal His6; monobody chaperone X1 | F- |

## Expression and Purification

- **Expression system**: BL21(DE3) E. coli
- **Construct**: Eca (GenBank EEV30821.1) with M4I mutation, C-terminal GSGG-HHHHHH in pASK90
- **Induction**: 0.2 µg/mL anhydrotetracycline for 3 h at 37°C
- **Media**: Terrific broth

### Purification Workflow

- **Expression system**: BL21(DE3) E. coli
- **Expression construct**: Eca with M4I mutation, C-terminal GSGG-HHHHHH tail
- **Tag info**: C-terminal hexahistidine, uncleaved

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest and lysis | Sonication | — | 100 mM NaCl, 50 mM Tris pH 7.5, DNase, lysozyme |  |
| Detergent extraction | Solubilization | — | 100 mM NaCl, 50 mM Tris pH 7.5 + 4% DM (n-decylmaltoside) | 2 h at room temperature |
| Affinity chromatography | TALON cobalt resin | Talon cobalt resin (Takara Bio) | 100 mM NaCl, 5 mM DM, 20 mM Tris pH 7.5 | Wash with 40 mM imidazole, elute with 400 mM imidazole |
| Size-exclusion chromatography | SEC | Superdex 200 Increase (GE Healthcare) | 10 mM HEPES, 100 mM NaCl, 5 mM DM, pH 7 (functional assays) + 5 mM DM |  |

**Final sample**: Purified in DM-containing buffer


## Crystallization

### doi/10.1038##s41594-018-0082-0

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, hanging drop |
| Protein sample | Eca in 10 mM HEPES, 100 mM NaF, 5 mM DM, pH 7, with monobody X1 |
| Reservoir | 18-22% PEG 3350, 200 mM NaF, 100 mM HEPES pH 7.0 |
| Temperature | 22 |
| Notes | Crystals grew in 2-4 days; data collected at APS (Advanced Photon Source) |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, hanging drop |
| Protein sample | Eca E118Q mutant in 10 mM HEPES, 100 mM NaF, 5 mM DM, pH 7, with monobody X1 |
| Reservoir | 18-22% PEG 3350, 200 mM NaF, 100 mM HEPES pH 7.0 |
| Temperature | 22 |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, hanging drop |
| Protein sample | Eca V319G mutant in crystallization buffer with monobody X1 |
| Reservoir | 18-22% PEG 3350, 200 mM NaF, 100 mM HEPES pH 7.0 |
| Temperature | 22 |


## Biological / Functional Insights

### Glu_g (E118) Gating Glutamate and Anion Selectivity

The critical gating glutamate E118 (Glu_g) controls both H+ and F-
transport. Mutation to glutamine (E118Q) or alanine (E118A)
completely inhibits F- and H+ transport while unexpectedly
allowing rapid uncoupled Cl- flux (~350-370 ions/s), reversing
the normal F- over Cl- selectivity. The shorter side chain in
E118D impairs transport (16 F-/s vs 150 F-/s for WT).
Replacement of E118 with glutamine or alanine reverses anion
selectivity, demonstrating that the gating glutamate is a key
determinant of F-/Cl- discrimination.

### Ion-Swapped Conformations and the Windmill Model

Two novel conformations were captured: (1) WT structure with
Glu_g in the Up position, exposing F- to the intracellular side
while Glu_g is accessible from the extracellular side for proton
exchange; (2) V319G mutant with Glu_g in the Down position,
occluding F- extracellularly while Glu_g faces the intracellular
vestibule for proton exchange. These structures reveal separate
ion-specific pathways for F- and H+ on opposite sides of the
membrane simultaneously. The proposed 'windmill' model involves a
clockwise rotary trajectory of the Glu_g side chain through Up,
Middle, and Down positions to couple F- export to H+ import with
1:1 stoichiometry.

### F- Binding Site and Selectivity

The F- ion at the extracellular binding site (F-ex) is coordinated
by backbone amides and a hydrogen bond from T320. The conserved
methionine M79 (replacing the Cl--coordinating serine found in
conventional CLCs) contributes to F- specificity. Mutation Y396A
unexpectedly preserved H+ coupling, contrasting with the
equivalent mutation in Cl- CLCs. V319G weakens F- binding
affinity ~5-fold (Kd ~1 mM vs ~0.2 mM WT) and partially
uncouples F-/H+ transport.


## Cross-References

- [CLC Proton Transport Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/clc-proton-transport-mechanism/) — Eca CLCF is a CLC superfamily antiporter with a distinct 1:1 F-/H+ stoichiometry
- [CLC Chloride Channel Glutamate Gating](/xray-mp-wiki/concepts/transport-mechanisms/clc-chloride-channel-glutamate-gating/) — The gating glutamate E118 plays a central role in F-/H+ coupling and selectivity in Eca
- [Glu_ex Conformational States in CLC Proteins](/xray-mp-wiki/concepts/transport-mechanisms/gluex-conformational-states-clc/) — Eca structures capture Glu_g in Up (WT) and Down (V319G) conformations, distinct from typical Cl- CLCs
