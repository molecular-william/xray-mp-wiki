---
title: V1-ATPase from Thermus thermophilus
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [rotary-atpase, v-atpase, membrane-protein, xray-crystallography, thermophilic]
sources: [doi/10.1016##j.jmb.2013.04.022]
---

# V1-ATPase from Thermus thermophilus

## Overview

The V1-ATPase from Thermus thermophilus is the extrinsic membrane domain of the V-type ATPase, a rotary ATPase complex that converts chemical energy of ATP into ion gradients. This paper reports the crystal structure at 3.9 A resolution (PDB: 3W3A) of the complete V1 subcomplex consisting of three A subunits, three B subunits, one D subunit, and one F subunit (A3B3DF). The structure reveals asymmetry at the intersubunit interfaces among the three AB pairs in different reaction states, realized by rigid-body rearrangements rather than large interdomain movements. This contrasts with F1-ATPase from other species and provides insight into the torque generation mechanism of rotary ATPases.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2013.04.022 | 3W3A | 3.9 A | I422 | V1-ATPase A3B3DF subcomplex from T. thermophilus; 3 A subunits, 3 B subunits, 1 D subunit, 1 F subunit | ADP (2 molecules bound at P-loops of A subunits) |

## Expression and Purification

- **Expression system**: Thermus thermophilus HB8 (native extraction)
- **Construct**: V1-ATPase subcomplex A3B3DF, full-length subunits

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | Described in prior publication (Miki lab, ref 18) | — | 1.6 M [ammonium sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/), 10% [dioxane](/xray-mp-wiki/reagents/additives/dioxane/), 100 mM [MOPS](/xray-mp-wiki/reagents/buffers/mops/) pH 6.0, 10 mM [ADP](/xray-mp-wiki/reagents/ligands/adp/), 10 mM [magnesium chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 1.0 mM aluminum nitrate, 1.0 mM [potassium fluoride](/xray-mp-wiki/reagents/additives/potassium-fluoride/) | Purification and crystallization procedures described in Nagamatsu et al. prior work (ref 18) |


## Crystallization

### doi/10.1016##j.jmb.2013.04.022

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | V1-ATPase at concentration suitable for crystallization |
| Reservoir | 1.6 M [ammonium sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/), 10% (v/v) dioxane, 100 mM [MOPS](/xray-mp-wiki/reagents/buffers/mops/) pH 6.0, 10 mM [ADP](/xray-mp-wiki/reagents/ligands/adp/), 10 mM [magnesium chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 1.0 mM aluminum nitrate, 1.0 mM [potassium fluoride](/xray-mp-wiki/reagents/additives/potassium-fluoride/) |
| Temperature | 20 C |
| Growth time | Not specified |
| Cryoprotection | Flash-frozen with nitrogen gas streams at -183 C |
| Notes | Diffraction data merged from 7 crystals (20 incident points). MIRAS phasing with 5 heavy-atom derivatives. DEN refinement with CNS. Rwork 32.7%, Rfree 38.1%. Collected at SPring-8 BL41XU and BL44XU. |


## Biological / Functional Insights

### Asymmetry at intersubunit interfaces

Three AB pairs (ANBN, AN'BN', AWBW) take different conformations. AN and AN' bind ADP, AW does not. The contact area between AW and BW (4559 A2) is smaller than AN-BN (6768 A2) and AN'-BN' (6594 A2). However, AB-DF contact is largest at AWB-W (2266 A2), supplementing the smaller AW-BW contact. Asymmetry is realized by rigid-body rearrangements of relative positions between A and B subunits, not large interdomain motion in catalytic A subunits.

### Torque generation mechanism

Nucleotide binding triggers conformational changes relayed from P-loop to interfaces. Arg360 of B subunit binds diphosphate and main-chain carbonyl of Tyr331 upon nucleotide binding, triggering rotational movement of the bottom part. The small movement of B bottom and intersubunit motion in AB pairs participate in closure of the cleft between AW and BW. DF subcomplex shifts along the coiled-coil axis during rotation, indicating translational movement attends rotational motion.

### DF subcomplex interactions

The D subunit coiled-coil plugs into the large cleft between AW and BW. Trp97 at the tip of the D subunit beta-hairpin interacts with Val471 and Ala475 of AN. The C-terminal region of D alpha3 helix exclusively interacts with AWBW pair. The N-terminal extension of D mainly interacts with AN'BN' pair. These asymmetric interactions couple the central stalk to the catalytic A3B3 subcomplex.


## Cross-References

- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Crystallization precipitant at 1.6 M in hanging-drop vapor diffusion
- [MOPS (3-(N-Morpholino)propanesulfonic Acid)](/xray-mp-wiki/reagents/buffers/mops/) — Buffer at 100 mM pH 6.0 in crystallization solution
- [ADP](/xray-mp-wiki/reagents/ligands/adp/) — Nucleotide substrate, 10 mM in crystallization, 2 molecules bound in structure
