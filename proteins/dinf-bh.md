---
title: DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17975, doi/10.1038##ncomms8995]
verified: false
---

# DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter

## Overview

DinF-BH is a multidrug and toxic compound extrusion (MATE) family transporter from Bacillus halodurans that functions as an H+-coupled multidrug efflux pump. It belongs to the DinF subfamily of MATE transporters and exports a broad range of organic cations including ethidium bromide, rhodamine 6G, and verapamil. DinF-BH features the characteristic bilobate 12-transmembrane-helix architecture of the MATE family with pseudo-symmetric N- and C-lobes (TM1-6 and TM7-12). The protonation site D40 (equivalent to PfMATE D41) has a physiologically relevant pKa of ~7, supporting a direct-competition mechanism wherein H+ and substrate compete for DinF-BH D40.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms8995 | 5C6N | 3.0 | P 212121 | DinF-BH D40N mutant (protonation-mimetic), residues 3-448 | N40 (protonation-mimetic asparagine); structural H-bond network |
| doi/10.1038##ncomms8995 | 5C6O | 3.0 | P 212121 | DinF-BH wild type, residues 3-448 | Verapamil |
| doi/10.1038##nature17975 | 4D9A | 3.0 | P 212121 | DinF-BH wild type, residues 3-448 | Rhodamine 6G (R6G) |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3) transformed with membrane protein expression vectors
- **Construct**: IPTG induction at 37 C for 3 h; also at 30 C for 4 h for some variants

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
| Method | Hanging-drop vapor diffusion at 22 C |
| Protein sample | DinF-BH D40N mutant at ~5 mg/ml |
| Reservoir | 100 mM HEPES-NaOH pH 7.0, 100 mM NaCl, 30-35% PEG400, 0.02% DDM, 1 mM TCEP |
| Temperature | 22 C |
| Growth time | Crystals appeared within 2 weeks; full size in 1 month |
| Cryoprotection | Transfer to low pH solution: 100 mM Na Acetate or Citrate pH 4.0, 200 mM NaCl, 35-40% PEG400, 0.03% DDM, 1 mM TCEP |
| Notes | DinF-BH D40N crystals for low pH form soaked in acetate or citrate buffer at pH 4.0 for >12 h; heavy atom derivatization with 10 mM heavy metal compounds for 3 h at 22 C |

| Parameter | Value |
|---|---|
| Method | Co-crystallization with verapamil; hanging-drop vapor diffusion at 22 C |
| Protein sample | DinF-BH at ~3 mg/ml incubated with 0.4 mM verapamil for >24 h at 4 C |
| Reservoir | -- |
| Temperature | 22 C |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Phasing by molecular replacement and MIRAS; verapamil-bound structure very similar to R6G-bound form (rmsd <0.5 A for 447 Ca positions) |


## Biological / Functional Insights

### Direct-competition-based antiport mechanism

DinF-BH uses a direct-competition mechanism wherein H+ and substrate compete for the protonation site D40. The calculated and experimentally determined pKa for DinF-BH D40 converged to ~7, making it a physiologically relevant protonation site. Protonation of D40 triggers substrate release without requiring substantial conformational changes such as TM1 bending, distinguishing it from the indirect coupling mechanism proposed for PfMATE.

### Verapamil-binding site and poly-specific drug recognition

The verapamil-binding chamber in DinF-BH is hydrophobic and methionine-rich, featuring interactions with side chains of N37 (TM1), Q252 (TM7), M33, Y36 (TM1), F60, M63, M64, M67 (TM2), F150, F154 (TM4), M286 and M293 (TM8). The extended conformation of verapamil across the membrane bilayer allows contacts with both N and C domains. The methionine-rich chamber design enables 'poly-specific' binding of chemically and structurally diverse drugs.

### Mutational analysis of the verapamil-binding site

Mutations of M33, N37, D40 and M286 abolished cellular resistance to verapamil, confirming their critical roles in verapamil transport. Mutations of Y36, F60, M63, M64, F150 and Q252 rendered DinF-BH-mediated drug efflux resistant to verapamil treatment, suggesting these residues play regulatory roles in transport function by affecting protein conformational changes.

### Mechanistic differences between MATE subfamilies

DinF-BH (DinF subfamily) differs mechanistically from NorM-NG (NorM subfamily) in how cation binding triggers substrate release. DinF-BH uses direct competition at D40, while NorM-NG shifts transmembrane helices upon Na+ binding. Eukaryotic MATE transporters including hMATE1 are mechanically more similar to NorM-NG than to DinF-BH, despite sequence similarity between DinF-BH and PfMATE.


## Cross-References

- [NorM-NG (Neisseria gonorrhoeae NorM)](/xray-mp-wiki/proteins/nor-mng/) — Co-reported in same paper; mechanistic comparison between DinF and NorM subfamilies
- [NorM-VC (Vibrio cholerae NorM)](/xray-mp-wiki/proteins/norm-vc/) — Earlier MATE family structure; NorM subfamily member
- [NtMATE2 (Nicotiana tabacum MATE2)](/xray-mp-wiki/proteins/ntmate2/) — Another MATE family member for structural comparison
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for DinF-BH solubilization and purification
- [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/) — Broad-spectrum MATE inhibitor that co-crystallized with DinF-BH
- [MATE Transporter Family](/xray-mp-wiki/concepts/mate-transporter-family/) — DinF-BH is a DinF subfamily member of the MATE family
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — MATE transporters operate via alternating access mechanism
