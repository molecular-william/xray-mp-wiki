---
title: Human D2 Dopamine Receptor (DRD2)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature25758, doi/10.1038##s41467-020-20221-0, doi/10.1038##s41467-020-14884-y, doi/10.1038##s41593-021-00971-w]
verified: false
---

# Human D2 Dopamine Receptor (DRD2)

## Overview

The human D2 dopamine receptor (DRD2) is a class A G protein-coupled receptor that serves as the primary target for both typical and atypical antipsychotic drugs. DRD2 mediates dopamine actions in reward, addiction, coordinated movement, metabolism, and hormonal secretion. Multiple inactive-state structures of DRD2 have been solved in complex with different antipsychotics including [RISPERIDONE](/xray-mp-wiki/reagents/ligands/risperidone) (6C38), haloperidol, and spiperone (7DFP). The spiperone-bound structure (7DFP, 3.1 A) revealed a dynamic extracellular loop 2 (ECL2) conformation and an extended binding pocket that accommodates spiperone phenyl ring, contributing to its selectivity for D2R and 5-HT2AR. The haloperidol-bound structure (2020) revealed a second extended binding pocket (SEBP) formed by TM2, TM3, EL1, and EL2 that is critical for DRD2 activation and subtype selectivity.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature25758 | 6C38 | 2.9 A | P212121 | Human DRD2 long variant with N-terminal [TRUNCATION](/xray-mp-wiki/concepts/truncation), T4L fused into ICL3, thermostabilizing mutations I122A, L375A, L379A | [RISPERIDONE](/xray-mp-wiki/reagents/ligands/risperidone) |
| doi/10.1038##s41467-020-20221-0 | 7DFP | 3.1 A | C2 | Human DRD2-mbIIIG S121K/L123W with N-terminal [TRUNCATION](/xray-mp-wiki/concepts/truncation) (residues 1-34), ICL3 replaced by loop-modified cytochrome b562 (mbIIIG), Fab3089 bound | [SPIPERONE](/xray-mp-wiki/reagents/ligands/spiperone) |
| doi/10.1038##s41467-020-14884-y |  |  |  | Human DRD2 long variant with N-terminal truncation, engineered with thermostabilizing mutations, crystallized with [HALOPERIDOL](/xray-mp-wiki/reagents/ligands/haloperidol) | [HALOPERIDOL](/xray-mp-wiki/reagents/ligands/haloperidol) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: DRD2-mbIIIG S121K/L123W with C-terminal TEV protease site, GFP, and octa-histidine tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Baculovirus expression in Sf9 cells | -- | Not specified + -- | Sf9 cells infected at 1.5 x 10^6 cells/ml, MOI 0.05, harvested 84 h later |
| Cell lysis and membrane preparation | Cell lysis in hypotonic buffer followed by membrane collection | -- | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.4, 1 mM EDTA + -- | Membranes resuspended in lysis buffer |
| Solubilization | [DDM](/xray-mp-wiki/reagents/detergents/ddm) solubilization | — | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.4, 150 mM NaCl, 0.5% DDM + 0.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Solubilized for 2 h at 4 C |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA beads | 10 mM HEPES pH 7.4, 150 mM NaCl, 0.05% DDM, 20 mM [IMIDAZOLE](/xray-mp-wiki/reagents/additives/imidazole) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Eluted with 250 mM [IMIDAZOLE](/xray-mp-wiki/reagents/additives/imidazole) |
| Tag cleavage and SEC | TEV protease cleavage followed by size-exclusion chromatography | Superdex 200 10/300 GL column | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.4, 150 mM NaCl, 0.05% DDM + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Purified DRD2-mbIIIG complexed with [SPIPERONE](/xray-mp-wiki/reagents/ligands/spiperone) and Fab3089 |


## Crystallization

### doi/10.1038##s41467-020-20221-0

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | DRD2-mbIIIG-S121K/L123W complexed with [SPIPERONE](/xray-mp-wiki/reagents/ligands/spiperone) and Fab3089 at ~30 mg/ml |
| Temperature | 20 C |
| Growth time | Microcrystals appeared after 2 days, grew to 20 x 2 x 2 um within a week |
| Cryoprotection | Not specified |
| Notes | Protein-laden LCP prepared by mixing protein with monoolein and 10% [CHOLESTEROL](/xray-mp-wiki/reagents/lipids/cholesterol) at 2:3 volume ratio. Data collected by serial femtosecond crystallography at SACLA XFEL. |


## Biological / Functional Insights

### Dynamic ECL2 conformation in DRD2

The spiperone-bound DRD2 structure (7DFP) revealed that ECL2 adopts an extended conformation distinct from the helical conformation seen in the [RISPERIDONE](/xray-mp-wiki/reagents/ligands/risperidone)-bound structure (6C38). In the spiperone structure, ECL2 does not form a hydrophobic patch with Trp100, Leu94, and Ile184, making the binding pocket more exposed. MD simulations suggested the extended ECL2 conformation represents a lower energy state, while the helical conformation in 6C38 is higher energy.

### Extended binding pocket in spiperone-bound DRD2

The spiperone-bound structure reveals an extended binding pocket (EBP) formed by a flipped Phe110 side chain that stacks with Trp90. This EBP accommodates spiperone's phenyl ring and extends from subsite B to subsite C. The EBP is unique among the inactive state DRD2 structures and may contribute to spiperone's high selectivity for D2R over other aminergic receptors. The bottom hydrophobic cleft in the spiperone structure is stabilized by steric contact between TM5 and ECL2, preventing the TM5 shift observed in [RISPERIDONE](/xray-mp-wiki/reagents/ligands/risperidone) and haloperidol structures.

### Second Extended Binding Pocket (SEBP) in DRD2-haloperidol structure

The DRD2-haloperidol complex structure revealed an unexpected second extended binding pocket (SEBP) formed by TM2, TM3, EL1, and EL2. The SEBP partially overlaps with the previously identified DRD3 EBP but is distinct. The outward movement of EL2 makes additional space for the SEBP at DRD2 compared to DRD3. Phe110^3.28 is a key residue: the F110A mutation enhances haloperidol binding 15.33-fold and L-741626 binding 144.18-fold, while F110W or F110Y mutations greatly reduce binding. The SEBP plays a critical role in both DRD2 antagonist binding and agonist activation. Using the SEBP and OBP structures, highly subtype-selective DRD2 agonists (O4SE6 and O8LE6) were discovered that show no activity at DRD3 or DRD4.


## Cross-References

- [Serotonin 5-HT2A Receptor](/xray-mp-wiki/proteins/gpcr/5ht2a-receptor/) — Spiperone binds with high affinity to both D2R and 5-HT2AR; structural comparison reveals shared binding features
- [Spiperone](/xray-mp-wiki/reagents/ligands/spiperone/) — Typical antipsychotic ligand co-crystallized with DRD2 in 7DFP structure
- [Risperidone](/xray-mp-wiki/reagents/ligands/risperidone/) — Atypical antipsychotic; risperidone-bound DRD2 (6C38) used for structural comparison
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component of the lipidic cubic phase crystallization matrix
- [Tris (Tris-HCl buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer (0.1 M, pH 8.0) used in crystallization reservoir
- [Polyethylene glycol 400 (PEG400)](/xray-mp-wiki/reagents/additives/peg-400/) — Precipitant (28-32%) used in crystallization reservoir
- [Dimethyl sulfoxide (DMSO)](/xray-mp-wiki/reagents/additives/dimethyl-sulfoxide/) — Additive (5%) used in crystallization reservoir
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to crystallize DRD2-Fab3089-spiperone complex
- [IMIDAZOLE](/xray-mp-wiki/reagents/additives/imidazole) — Reagent used in this study
- [DDM](/xray-mp-wiki/reagents/detergents/ddm) — Reagent used in this study
