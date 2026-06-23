---
title: "VcmN MATE Transporter"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2018.10.004]
verified: false
---

# VcmN MATE Transporter

## Overview

VcmN is a multidrug and toxic compound extrusion (MATE) transporter from the pathogenic bacterium Vibrio cholerae. It belongs to the DinF subfamily of MATE transporters and is driven by an H+ gradient across the membrane. High-resolution crystal structures revealed two distinct conformations associated with different pH conditions: a straight form (PDB 6IDP, 2.2 A) at pH 7.5-8.0 and a bent form (PDB 6IDR, 2.5 A) at pH 5.0, demonstrating that protonation of the conserved Asp35 induces bending of transmembrane helix 1 (TM1) via rearrangement of the hydrogen-bonding network in the N-lobe. The D35N mutant structure (PDB 6IDS, 2.79 A) captured an intermediate conformation, revealing that Asn substitution does not fully mimic protonation. The transport cycle involves a common step among prokaryotic H+-coupled MATE transporters: rearrangement of the N-lobe hydrogen-bonding network, TM1 bending, and shrinkage of the substrate-binding cavity.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2018.10.004 | 6IDP | 2.21 A | P2(1)2(1)2(1) | VcmN C-terminally truncated (residues 1-434) from Vibrio cholerae, crystallized by LCP at pH 7.5-8.0 | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (mimic of substrate in N-lobe cavity) |
| doi/10.1016##j.str.2018.10.004 | 6IDR | 2.50 A | P2(1)2(1)2(1) | VcmN C-terminally truncated (residues 1-434) from Vibrio cholerae, crystallized by LCP at pH 5.0 | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (mimic of substrate in N-lobe cavity) |
| doi/10.1016##j.str.2018.10.004 | 6IDS | 2.79 A | P2(1)2(1)2(1) | VcmN C-terminally truncated (residues 1-434) D35N mutant from Vibrio cholerae | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (mimic of substrate in N-lobe cavity) |

## Expression and Purification

- **Expression system**: E. coli C41(DE3) Rosetta strain
- **Construct**: VcmN (1-434) with C-terminal His-tag from Vibrio cholerae

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Homogenization and ultracentrifugation | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 100 mM NaCl + -- | Cells disrupted by sonication; membranes collected by ultracentrifugation |
| Solubilization | Detergent solubilization | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 100 mM NaCl + n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Membranes solubilized in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA resin | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 100 mM NaCl, [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | His-tag purification |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) Increase 10/300 GL | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 100 mM NaCl + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final polishing step |


## Crystallization

### doi/10.1016##j.str.2018.10.004

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified VcmN in [DDM](/xray-mp-wiki/reagents/detergents/ddm/), reconstituted into [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) LCP |
| Temperature | 20 C |
| Growth time | Crystals appeared within 1-2 weeks |
| Cryoprotection | Crystals frozen in liquid nitrogen with reservoir solution supplemented with 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Notes | Two crystal forms obtained from different pH conditions: straight form (crystal I, pH 7.5-8.0) and bent form (crystal II, pH 5.0). The D35N mutant was crystallized similarly. X-ray data collected at SPring-8 BL32XU (crystals I, II) and Diamond Light Source I24 (D35N). Structures solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using [PFMATE](/xray-mp-wiki/proteins/abc-transporters/pfmate/) structure (PDB 3VVN) as search model. |


## Biological / Functional Insights

### H+-dependent conformational change of TM1

The crystal structures of VcmN in two distinct conformations (straight and bent forms) revealed that protonation of the conserved Asp35 in TM1 induces bending of the TM1 helix at Pro20 and Gly24. This rearrangement of the hydrogen-bonding network in the N-lobe causes shrinkage of the substrate-binding cavity, which likely extrudes bound substrates toward the extracellular side. The D35N mutation only partially mimics protonation, capturing an intermediate TM1 conformation.

### Conserved transport mechanism in prokaryotic H+-coupled MATE transporters

Structural comparison of VcmN with [PFMATE](/xray-mp-wiki/proteins/abc-transporters/pfmate/) (Pyrococcus furiosus) reveals a similar TM1 bending mechanism, suggesting a conserved step in the transport cycle shared among prokaryotic H+-driven MATE transporters. The key residues involved in the hydrogen-bonding network (Asp35, Asn174, Asp178, Thr196) and the TM1 kink (Pro20) are conserved in both H+-driven and Na+-driven DinF subfamily members.

### D35N does not fully mimic protonation

The D35N mutant structure shows that Asn substitution does not completely reproduce the protonated state of Asp35. The TM1 helix of the D35N mutant occupies a conformation intermediate between the straight and bent forms, indicating that the differences in chemical properties between Asp and Asn are not negligible for functional studies of proton-driven transporters.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization and purification detergent
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Used for LCP crystallization; monoolein molecules in N-lobe cavity mimic substrates
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Primary crystallization method for VcmN
- [PfMATE Transporter](/xray-mp-wiki/proteins/abc-transporters/pfmate/) — Homologous MATE transporter used as search model for molecular replacement
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
