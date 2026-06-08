---
title: NorM-NG (Neisseria gonorrhoeae NorM) - MATE Family Na+-Coupled Transporter
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11403, doi/10.1038##ncomms8995]
verified: false
---

# NorM-NG (Neisseria gonorrhoeae NorM) - MATE Family Na+-Coupled Transporter

## Overview

NorM-NG is a multidrug and toxic compound extrusion (MATE) family transporter from Neisseria gonorrhoeae that functions as a Na+-coupled multidrug efflux pump. It belongs to the NorM subfamily of MATE transporters and exports a broad range of organic cations including ethidium bromide, doxorubicin, and rhodamine 6G. NorM-NG features the characteristic bilobate 12-transmembrane-helix architecture of the MATE family with pseudo-symmetric N- and C-lobes (TM1-6 and TM7-12), residues 5-230 and 231-459 respectively. In the verapamil-bound structure, NorM-NG undergoes pronounced conformational changes in two extracellular loops (L3-4 and L9-10) that cap the multidrug-binding cavity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11403 | 3P3M | 3.0 | P 212121 | NorM-NG wild type, residues 5-459 | Rhodamine 6G (R6G) |
| doi/10.1038##ncomms8995 | 5C6P | 3.0 | P 212121 | NorM-NG wild type, residues 5-459 | Verapamil |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3) transformed with membrane protein expression vectors
- **Construct**: IPTG induction at 37 C for 3 h

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and induction | E. coli BL21(DE3) in LB media to OD600 = 0.5; induced with 0.5 mM IPTG at 37 C for 3 h | -- | LB media + -- |  |
| Cell lysis | Multiple passages through pre-cooled microfluidizer | -- | -- + -- |  |
| Membrane extraction | Ultracentrifugation for membrane collection; extracted with 1% DDM | -- | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 20% glycerol, 1 mM TCEP + 1% DDM (Anatrace) |  |
| Ni-NTA affinity chromatography | Ni-NTA resin; eluted with 500 mM imidazole | Ni-NTA | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 25% glycerol, 0.02% DDM, 1 mM TCEP + 0.02% DDM |  |
| Thrombin cleavage | Incubated with thrombin protease overnight | -- | -- + -- |  |
| Size-exclusion chromatography | Superdex 200 SEC | Superdex 200 | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 15% glycerol, 0.02% DDM, 1 mM TCEP + 0.02% DDM |  |


## Crystallization

### doi/10.1038##ncomms8995

| Parameter | Value |
|---|---|
| Method | Co-crystallization with verapamil; hanging-drop vapor diffusion at 22 C |
| Protein sample | NorM-NG incubated with verapamil |
| Reservoir | -- |
| Temperature | 22 C |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Phasing by molecular replacement and MIRAS; verapamil-bound structure differs from R6G-bound by rmsd >2 A over 459 aligned Ca positions; notable conformational changes in L3-4 and L9-10 loops |


## Biological / Functional Insights

### Na+-coupled transport mechanism via transmembrane helix shifting

NorM-NG uses a Na+-coupled mechanism distinct from the H+-coupled DinF-BH. Cation binding triggers substrate unbinding by shifting several transmembrane helices, contrasting with the direct-competition mechanism of DinF-BH where protonation of D40 triggers release without substantial conformational changes. The D41 residue (equivalent to DinF-BH D40) is essential for transport but is substituted by asparagine in eukaryotic MATE members.

### Verapamil-binding site and folded ligand conformation

Verapamil in NorM-NG adopts a folded conformation with both aromatic rings stacked on top of each other — a double-layered conformation unlike the extended form seen in DinF-BH. Direct contacts involve S61 (TM2), Q284 (TM8) via H-bonding and A57 (TM2), F265, V269 (TM7), P357 (L9-10) via van der Waals. D41 (TM1) and D356 (L9-10) carboxylate groups are ~6 and 3.5 A from verapamil N8, implying moderate electrostatic attraction.

### Extracellular loop dynamics upon verapamil binding

Upon verapamil binding, NorM-NG undergoes pronounced conformational changes in L3-4 and L9-10 extracellular loops. L3-4 shifts the most, losing ability to insert side chains into the central cavity. L9-10 also shifts away from the multidrug-binding cavity, interacting with verapamil only modestly. These changes contrast with DinF-BH which remains largely unaltered upon ligand exchange.

### Mutational analysis of the verapamil-binding site

Mutations of D41, S61, F265L, V269, Q284, D356 and P357 abolished cellular resistance to verapamil, confirming these residues as essential for verapamil transport. Unlike DinF-BH, none of the tested NorM-NG mutations enabled drug resistance in the presence of verapamil, underscoring mechanistic differences between the DinF and NorM subfamilies.


## Cross-References

- [DinF-BH (Bacillus halodurans DinF)](/xray-mp-wiki/proteins/dinf-bh/) — Co-reported in same paper; mechanistic comparison between NorM and DinF subfamilies
- [NorM-VC (Vibrio cholerae NorM)](/xray-mp-wiki/proteins/norm-vc/) — Earlier NorM subfamily structure; Na+-coupled MATE transporter
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for NorM-NG solubilization and purification
- [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/) — Broad-spectrum MATE inhibitor that co-crystallized with NorM-NG
- [MATE Transporter Family](/xray-mp-wiki/concepts/mate-transporter-family/) — NorM-NG is a NorM subfamily member of the MATE family
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — MATE transporters operate via alternating access mechanism
