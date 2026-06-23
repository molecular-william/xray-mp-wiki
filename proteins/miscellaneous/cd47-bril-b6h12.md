---
title: CD47 BRIL-B6H12 complex from Homo sapiens
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-25475-w]
verified: false
---

# CD47 BRIL-B6H12 complex from Homo sapiens

## Overview

CD47 is the only 5-transmembrane (5-TM) spanning receptor of the immune system. Its extracellular domain (ECD) is a heavily glycosylated cell surface marker of self that binds signal regulatory protein alpha (SIRPalpha) and inhibits macrophage phagocytosis, delivering a 'don't eat me' signal. This structural characterization presents the crystal structure of full-length human CD47 in complex with the function-blocking antibody B6H12, which can inhibit the binding of two endogenous partners, SIRPalpha and thrombospondin-1. The structure reveals a unique extracellular loop region (ECLR) architecture, comprised of two extracellular loops and a six-residue linker (RVVSWF) that forms an extended SWF loop. The hydrophobic aromatic side chains of W118 and F119 from the SWF loop are buried deep in the ECLR core, providing an anchor point for tethering the ECD to the transmembrane domain. Molecular dynamics simulations revealed ECD motion between two macrostates (s1 and s2), with a ~22 degree tilt transition mediated by the conformational switch of Tyr184 on ECL1. CD47 is a validated drug target in cancer immuno-therapy, with multiple clinical trials focused on blocking CD47-SIRPalpha interaction.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-021-25475-w | 7MYZ | 2.85 | P 21 21 21 | Full-length CD47 (residues 1-278) with [BRIL](/xray-mp-wiki/reagents/protein-tags/bril) fusion on helix IV, in complex with B6H12 Fab | B6H12 Fab |

## Expression and Purification

- **Expression system**: CHO cells
- **Construct**: CD47 (residues 1-278) with [BRIL](/xray-mp-wiki/reagents/protein-tags/bril) fusion on helix IV, expressed transiently in ExpiCHO-S cells
- **Notes**: B6H12 mAb expressed in ExpiCHO-S cells. Fab prepared from IgG1 using Pierce Fab Preparation kit.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1 | Cell lysis by sonication | — | 50 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 150 mM NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Membrane fraction collected by ultracentrifugation |
| 2 | Affinity chromatography (Protein-A for Fab, Ni-NTA for CD47) | Protein-A affinity resin / Ni-NTA Superflow | 50 mM [TRIS](/xray-mp-wiki/reagents/buffers/tris) pH 8.0, 150 mM NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | B6H12 Fab eluted with 100 mM sodium [Citrate](/xray-mp-wiki/reagents/buffers/citrate) pH 3.3, neutralized |
| 3 | Size-exclusion chromatography | — | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 250 mM NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Final purification step for complex formation and crystallization |


## Crystallization

### doi/10.1038##s41467-021-25475-w

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | CD47-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril)-B6H12 complex at ~10 mg/mL |
| Reservoir | 25% [PEG400](/xray-mp-wiki/reagents/additives/peg400), 0.1 M sodium [Citrate](/xray-mp-wiki/reagents/buffers/citrate) pH 5.5, 0.1 M [MES](/xray-mp-wiki/reagents/buffers/mes) pH 6.0 |
| Temperature | 293 |
| Notes | Full-length CD47-B6H12 complex crystals diffracted to 2.85 Angstrom |


## Biological / Functional Insights

### Unique 5-TM receptor architecture

CD47 is the only known 5-TM receptor of the immune system and the human genome (together with the distantly related prominin family). The TMD forms a pentagon-like helical bundle spanning ~32 Angstrom across the lipid membrane. Helix II is nearly perpendicular to the membrane, while helices I, III, IV, and V span at shallower angles. A proline-induced kink at P131 in helix I allows helical tilt away from the receptor core. An intracellular hydrogen bond network centered on H206 (involving Q141, Q227, and Q264) contributes to local stability of the 5-TM bundle at the intracellular side.

### ECD motion and immune recognition

The relative orientation of the ECD with respect to the TMD is dynamic. Molecular dynamics simulations revealed two macrostates (s1 and s2) separated by a ~22 degree ECD tilt. The transition is mediated by the conformational switch of Tyr184 on ECL1, which hydrogen bonds to ECL2 residues I242 and A244 in the s1 state. Departure of Y184 from the ECLR pocket triggers ECD rigid body shifts. The ECD transition from s1 to s2 is accompanied by shortening of the RVVSWF linker, allowing R114 to dock into a negatively charged ECLR pocket between helix I and V. This dynamic ECD positioning may be relevant for recognition by different endogenous protein partners including SIRPalpha, integrins, and thrombospondin-1.


## Cross-References

- [TRIS](/xray-mp-wiki/reagents/buffers/tris) — Entity mentioned in overview or biological insights
- [DDM](/xray-mp-wiki/reagents/detergents/ddm) — Entity mentioned in overview or biological insights
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate) — Entity mentioned in overview or biological insights
- [BRIL](/xray-mp-wiki/reagents/protein-tags/bril) — Entity mentioned in overview or biological insights
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes) — Entity mentioned in overview or biological insights
- [MES](/xray-mp-wiki/reagents/buffers/mes) — Entity mentioned in text
- [PEG400](/xray-mp-wiki/reagents/additives/peg400) — Entity mentioned in text
