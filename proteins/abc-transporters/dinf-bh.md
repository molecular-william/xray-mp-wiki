---
title: DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter
created: 2026-06-05
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17975, doi/10.1038##ncomms8995, doi/10.1038##nsmb.2687]
verified: false
---

# DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter

## Overview

DinF-BH is a multidrug and toxic compound extrusion (MATE) family transporter from Bacillus halodurans that functions as an H+-coupled multidrug efflux pump. It belongs to the DinF subfamily of MATE transporters and exports a broad range of organic cations including [Ethidium](/xray-mp-wiki/reagents/ligands/ethidium/) bromide, rhodamine 6G, and [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/). DinF-BH features the characteristic bilobate 12-transmembrane-helix architecture of the MATE family with pseudo-symmetric N- and C-lobes (TM1-6 and TM7-12). The protonation site D40 (equivalent to [Pfmate](/xray-mp-wiki/proteins/abc-transporters/pfmate/) D41) has a physiologically relevant pKa of ~7, supporting a direct-competition mechanism wherein H+ and substrate compete for DinF-BH D40. The crystal structure of apo DinF-BH was determined at 3.2 A resolution, revealing an asymmetric arrangement of 12 transmembrane helices distinct from the pseudo-two-fold symmetry of NorM subfamily transporters.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms8995 | 5C6N | 3.0 | P 21 21 21 | DinF-BH D40N mutant, residues 3-448 | N40 (protonation-mimetic asparagine) |
| doi/10.1038##ncomms8995 | 5C6O | 3.0 | P 21 21 21 | DinF-BH wild type, residues 3-448 | [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/) |
| doi/10.1038##nature17975 | 4D9A | 3.0 | P 21 21 21 | DinF-BH wild type, residues 3-448 | Rhodamine 6G (R6G) |
| doi/10.1038##nsmb.2687 | 4LZ6 | 3.2 | P 21 21 21 | DinF-BH wild type, residues 3-448, C-terminal His6 tag | none (apo) |
| doi/10.1038##nsmb.2687 | 4LZ9 | 3.7 | P 21 21 21 | DinF-BH wild type, residues 3-448, C-terminal His6 tag | Rhodamine 6G (R6G) |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI

- **Construct**: Full-length DinF-BH cloned into pET15b with C-terminal His6 tag; induced with 0.1 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/)


### Purification Workflow

*Source: doi/10.1038##nsmb.2687*

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI
- **Expression construct**: Full-length DinF-BH, pET15b, C-terminal His6 tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and expression | E. coli culture in LB medium | -- | LB medium + -- | Induced with 0.1 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/) at OD600 ~0.5 |
| Cell lysis | Microfluidizer, multiple passages | -- | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Membranes collected by ultracentrifugation; solubilized with 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Ni-NTA affinity chromatography | Ni-NTA resin | Ni-NTA | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 25% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted with 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Size-exclusion chromatography | Superdex 200 10/300 GL | Superdex 200 | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |

### Purification Workflow

*Source: doi/10.1038##ncomms8995*

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI
- **Expression construct**: Full-length DinF-BH, pET15b, C-terminal His6 tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and induction | E. coli culture in LB media | -- | LB media + -- | OD600 = 0.5; induced with 0.5 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/) at 37 C for 3 h |
| Cell lysis | Microfluidizer, multiple passages | -- | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| Membrane extraction | Ultracentrifugation | -- | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (Anatrace) | Extracted with 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Ni-NTA affinity chromatography | Ni-NTA resin | Ni-NTA | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 25% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted with 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Thrombin cleavage | Thrombin protease incubation overnight | -- | -- + -- | Cleaved C-terminal His6 tag |
| Size-exclusion chromatography | Superdex 200 SEC | Superdex 200 | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |

### Purification Workflow

*Source: doi/10.1038##nature17975*

- **Expression system**: E. coli BL21(DE3) ΔacrABΔmacABΔyojHI
- **Expression construct**: Full-length DinF-BH, pET15b, C-terminal His6 tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | E. coli fermentation | -- | LB medium + -- |  |
| Cell lysis and membrane preparation | Microfluidizer | -- | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Membranes collected; solubilized with 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Ni-NTA affinity chromatography | Ni-NTA resin | Ni-NTA | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 25% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted with 500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Size-exclusion chromatography | Superdex 200 SEC | Superdex 200 | 20 mM HEPES-NaOH pH 7.5, 100 mM NaCl, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |


## Crystallization

### doi/10.1038##nsmb.2687

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion at 22 C |
| Protein sample | DinF-BH wild type at ~10 mg/ml |
| Reservoir | 100 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.5, 100 mM NaCl, 20-30% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) |
| Temperature | 22 C |
| Growth time | Crystals appeared within 2 weeks; full size in 1 month |
| Cryoprotection | Not specified |
| Notes | Native crystals diffracted to 3.2 A. Heavy atom derivatization with 5 mM compounds for 8 h at 22 C. Substrate soaking with 0.5 mM R6G or tetraphenylarsonium (TPP analog) for 48 h at 22 C. Structure solved by combination of molecular replacement and [MIRAS](/xray-mp-wiki/methods/structure-determination/miras/) phasing. |

### doi/10.1038##ncomms8995

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion at 22 C |
| Protein sample | DinF-BH D40N mutant at ~5 mg/ml |
| Reservoir | 100 mM HEPES-NaOH pH 7.0, 100 mM NaCl, 30-35% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) |
| Temperature | 22 C |
| Growth time | Crystals appeared within 2 weeks; full size in 1 month |
| Cryoprotection | Transfer to low pH solution: 100 mM Na [Acetate](/xray-mp-wiki/reagents/buffers/acetate/) or [Citrate](/xray-mp-wiki/reagents/buffers/citrate/) pH 4.0, 200 mM NaCl, 35-40% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) |
| Notes | DinF-BH D40N crystals for low pH form soaked in [Acetate](/xray-mp-wiki/reagents/buffers/acetate/) or [Citrate](/xray-mp-wiki/reagents/buffers/citrate/) buffer at pH 4.0 for >12 h; heavy atom derivatization with 10 mM heavy metal compounds for 3 h at 22 C |

| Parameter | Value |
|---|---|
| Method | Co-crystallization with [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/); hanging-drop vapor diffusion at 22 C |
| Protein sample | DinF-BH at ~3 mg/ml incubated with 0.4 mM [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/) for >24 h at 4 C |
| Reservoir | -- |
| Temperature | 22 C |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Phasing by molecular replacement and [MIRAS](/xray-mp-wiki/methods/structure-determination/miras/); verapamil-bound structure very similar to R6G-bound form (rmsd <0.5 A for 447 Ca positions) |

### doi/10.1038##nature17975

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion at 22 C |
| Protein sample | DinF-BH wild type at ~10 mg/ml |
| Reservoir | 100 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.5, 100 mM NaCl, 20-30% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 1 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep/) |
| Temperature | 22 C |
| Growth time | Crystals appeared within 2 weeks; full size in 1 month |
| Cryoprotection | Not specified |
| Notes | Native crystals diffracted to 3.0 A. Substrate soaking with 0.5 mM R6G for 48 h at 22 C. |


## Biological / Functional Insights

### Direct-competition-based antiport mechanism

DinF-BH uses a direct-competition mechanism wherein H+ and substrate compete for the protonation site D40. The calculated and experimentally determined pKa for DinF-BH D40 converged to ~7, making it a physiologically relevant protonation site. Protonation of D40 triggers substrate release without requiring substantial conformational changes such as TM1 bending, distinguishing it from the indirect coupling mechanism proposed for [Pfmate](/xray-mp-wiki/proteins/abc-transporters/pfmate/).

### Verapamil-binding site and poly-specific drug recognition

The verapamil-binding chamber in DinF-BH is hydrophobic and methionine-rich, featuring interactions with side chains of N37 (TM1), Q252 (TM7), M33, Y36 (TM1), F60, M63, M64, M67 (TM2), F150, F154 (TM4), M286 and M293 (TM8). The extended conformation of [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/) across the membrane bilayer allows contacts with both N and C domains. The methionine-rich chamber design enables 'poly-specific' binding of chemically and structurally diverse drugs.

### Mutational analysis of the verapamil-binding site

Mutations of M33, N37, D40 and M286 abolished cellular resistance to [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/), confirming their critical roles in [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/) transport. Mutations of Y36, F60, M63, M64, F150 and Q252 rendered DinF-BH-mediated drug efflux resistant to [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/) treatment, suggesting these residues play regulatory roles in transport function by affecting protein conformational changes.

### Mechanistic differences between MATE subfamilies

DinF-BH (DinF subfamily) differs mechanistically from NorM-NG (NorM subfamily) in how cation binding triggers substrate release. DinF-BH uses direct competition at D40, while NorM-NG shifts transmembrane helices upon Na+ binding. Eukaryotic MATE transporters including hMATE1 are mechanically more similar to NorM-NG than to DinF-BH, despite sequence similarity between DinF-BH and [Pfmate](/xray-mp-wiki/proteins/abc-transporters/pfmate/).

### Asymmetric architecture of DinF-BH

Unlike the pseudo-two-fold symmetric NorM transporters, DinF-BH exhibits an asymmetric arrangement of its 12 transmembrane helices. Structural superimposition of the N domain (TM1-TM6) and C domain (TM7-TM12) yielded an r.m.s. deviation of 3.30 A for 138 common C-alpha positions, substantially larger than the 2.39 A observed for NorM-NG. The main difference localizes to extracellular halves of TM7 and TM8 (residues 253-288), which are more kinked than their TM1-TM2 counterparts, induced by P247 and P291.

### D40 as dual-function residue for substrate binding and protonation

D40 in DinF-BH serves a dual role in both substrate binding and protonation. Located within a membrane-embedded chamber shielded by TM7 and TM8, D40 has a calculated pKa of 7.4, making it suitable as a protonation site at physiological pH. The D40N mutation abrogated drug resistance and H+ release upon substrate binding, with R6G binding affinity reduced from Kd 3.1 uM (wild type) to 107.2 uM (D40N). This direct competition between H+ and substrate for D40 is the basis of the antiport mechanism.

### Proposed transport mechanism involving 20 degree rotation

Based on the extracellular-facing structure, an intracellular-facing model was generated by rotating the cytoplasmic halves of TM7 and TM8, as well as TM9-TM12, by 20 degrees relative to the rest of the protein. This rotation collapses the solvent-exposed crevice in the C domain and exposes the drug-binding site toward the cytoplasm. Proline (P247, P291) and [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) (G245, G294) residues in TM7 and TM8 accommodate this motion by straightening the kinks. Mutations of L22, V241, V244, F249 and Q297 along the intracellular transport path impaired transport function.


## Cross-References

- [NorM-NG (Neisseria gonorrhoeae NorM)](/xray-mp-wiki/proteins/abc-transporters/nor-mng/) — Co-reported in same paper; mechanistic comparison between DinF and NorM subfamilies
- [NorM-VC (Vibrio cholerae NorM)](/xray-mp-wiki/proteins/norm-vc/) — Earlier MATE family structure; NorM subfamily member
- [MATE Transporter Family](/xray-mp-wiki/concepts/mate-transporter-family/) — DinF-BH is a DinF subfamily member of the MATE family
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — MATE transporters operate via alternating access mechanism
- [Ethidium](/xray-mp-wiki/reagents/ligands/ethidium/) — Referenced in context related to Ethidium
- [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/) — Referenced in context related to Verapamil
- [Pfmate](/xray-mp-wiki/proteins/abc-transporters/pfmate/) — Referenced in context related to Pfmate
- [Iptg](/xray-mp-wiki/reagents/additives/iptg/) — Referenced in context related to Iptg
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in context related to DDM
- [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in context related to Tris Hcl
