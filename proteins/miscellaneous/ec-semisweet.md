---
title: E. coli SemiSWEET (EcSemiSWEET)
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms7112]
verified: false
---

# E. coli SemiSWEET (EcSemiSWEET)

## Overview

EcSemiSWEET is a sugar transporter from the SWEET family found in Escherichia coli. It is a bacterial homolog of eukaryotic SWEET transporters and belongs to the PQ-loop family characterized by a conserved Pro-Gln motif. EcSemiSWEET functions as a dimer of three-helix bundles and mediates facilitative diffusion of sugars across biological membranes. Crystal structures in both inward-open and outward-open conformations reveal a 'binder clip-like' conformational mechanism driven by the PQ-loop hinge motif.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms7112 | 4X1F | 2.0 | P212121 | [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet)-LESSGEN-LYFQGQFTS-H8 | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| doi/10.1038##ncomms7112 | 4X1G | 3.0 | C2 | [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet)-LESSGEN-LYFQGQFTS-H8 | -- |

## Expression and Purification

- **Expression system**: Escherichia coli Rosetta 2 (DE3)
- **Construct**: [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet)-LESSGEN-LYFQGQFTS-H8
- **Induction**: 0.2 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg), OD600 0.6, 20 C for 20 h

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Microfluidizer processor | -- | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl, 0.1 mM PMSF | Three passes at 15,000 psi; debris removed by 10,000g for 10 min |
| Membrane isolation | Ultracentrifugation | -- | -- | 138,000g for 1 h to collect membrane fraction |
| Solubilization | Detergent solubilization | -- | 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) + [DDM](/xray-mp-wiki/reagents/detergents/ddm) (2%), CHS (0.4%) | 90 min at 4 C; insoluble removed by 138,000g for 30 min |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) resin (Qiagen) | 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 0.05% DDM, 0.01% CHS | Incubated 90 min; washed; eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) |
| Tag cleavage | [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease) cleavage | -- | [Imidazole](/xray-mp-wiki/reagents/additives/imidazole)-free Tris buffer | His8-tag cleaved by tobacco etch virus protease; dialysed overnight |
| Secondary affinity purification | [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) resin | [Imidazole](/xray-mp-wiki/reagents/additives/imidazole)-free Tris buffer | Remove cleaved His8-tag and [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease) |


## Crystallization

### doi/10.1038##ncomms7112

| Parameter | Value |
|---|---|
| Method | Sitting drop [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet)-H8 (inward-open) |
| Notes | Inward-open structure (Crystal-I) with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) in substrate pocket |

| Parameter | Value |
|---|---|
| Method | Sitting drop [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet)-H8 (outward-open) |
| Notes | Outward-open structure (Crystal-II); both conformations captured simultaneously |


## Biological / Functional Insights

### Binder clip-like conformational mechanism

EcSemiSWEET undergoes intramolecular conformational changes in each protomer, not rigid-body movement. The conserved PQ-loop motif (Pro21, Gln22) serves as a flexible molecular hinge enabling a 'binder clip-like' motion. TM1 bends at Pro21, allowing the structural unit (TM1b, TM2, TM3, TM1a') to rotate relative to its counterpart in the dimer.

### Dual gating mechanism

Two gates control substrate access to the central binding pocket. The extracellular gate (Tyr53, Arg57, Asp59) seals the pocket from outside in the inward-open state via salt bridges and hydrogen bonds. The intracellular gate (Phe19, Met39, Tyr40, Phe43) blocks access from the cytoplasm in the outward-open state via hydrophobic interactions. Mutagenesis reveals opposite effects: disrupting extracellular gate increases activity, while disrupting intracellular gate decreases it.

### Substrate binding pocket

The central pocket (8-9 A wide, 11 A long) is lined by Trp50 and Asn66 residues. [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) bound in the inward-open structure mimics sugar substrate via its glycerol head group forming hydrogen bonds with Asn66 and sandwiched between Trp50 aromatic rings. N66A mutation significantly decreases sucrose uptake. W50A mutation increases uptake (enlarged pocket), while W50F has no effect.

### Low-affinity sucrose transport

EcSemiSWEET mediates slow but significant [14C]-[Sucrose](/xray-mp-wiki/reagents/ligands/sucrose) uptake in proteoliposomes. Uptake rate increases linearly with sucrose concentration up to 300 mM without saturation, indicating low-affinity binding. This contrasts with higher-affinity eukaryotic SWEET transporters, suggesting sucrose may not be the physiological substrate.

### Transport cycle model

Proposed transport cycle: inward-open state captures substrate -> PQ-loop hinge enables transition -> slight TM2 bend closes intracellular gate (occluded state) -> extracellular gate opens -> substrate exits -> inward-open and outward-open conformations can interconvert spontaneously without substrate.


## Cross-References

- [LbSemiSWEET](/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/) — Related bacterial [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/semisweet) from Leptospira biflexa with solved outward-open and occluded structures
- [SWEET Transporter Family](/xray-mp-wiki/concepts/sweet-transporter/) — EcSemiSWEET is a bacterial member of the SWEET family of sugar transporters
- [PQ-Loop Family](/xray-mp-wiki/concepts/pq-loop-family/) — EcSemiSWEET is a PQ-loop family member characterized by conserved Pro-Gln motif
- [Binder Clip Motion](/xray-mp-wiki/concepts/binder-clip-motion/) — EcSemiSWEET undergoes binder clip-like conformational change mediated by PQ-loop hinge
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for solubilization of EcSemiSWEET membrane fraction
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Stabilizing additive used with [DDM](/xray-mp-wiki/reagents/detergents/ddm) during solubilization and purification
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Inducer for protein expression at 0.2 mM
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer component (50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0) for expression and purification
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/affinity-resins/ni-nta/) — Affinity resin used for His8-tag purification of EcSemiSWEET
- [TEV Protease](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) — Tobacco etch virus protease used to cleave His8-tag from EcSemiSWEET
