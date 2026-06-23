---
title: Exiguobacterium sibiricum Rhodopsin (ESR)
created: 2026-06-21
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1221629110]
verified: false
---

# Exiguobacterium sibiricum Rhodopsin (ESR)

## Overview

Exiguobacterium sibiricum rhodopsin (ESR) is a light-driven proton pump
from the permafrost bacterium Exiguobacterium sibiricum. ESR belongs to
the proteorhodopsin family and exhibits three unique features compared to
bacteriorhodopsin and xanthorhodopsin: (i) the proton donor is a lysine
residue (Lys-96) situated close to the bulk solvent, (ii) the alpha-helical
structure in the middle of helix F is replaced by 3_10- and pi-helix-like
elements stabilized by Trp-154 and Asn-224, and (iii) the proton release
region is connected to the bulk solvent by a chain of water molecules
already in the ground state. The 2.3 A crystal structure (PDB 4RYJ) reveals
a conserved Schiff base environment despite these unusual features. ESR
represents the first high-resolution structure of a proteorhodopsin.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1221629110 | 4RYJ | 2.3 | P321 | Full-length ESR with C-terminal hexahistidine tag; residues Met1 to Ala... | All-trans retinal (chromophore) |

## Expression and Purification

- **Expression system**: E. coli Rosetta2(DE3)pLysS
- **Construct**: Full-length ESR with C-terminal hexahistidine tag
- **Notes**: Fermenter for 3 days at 30 C in 2x ZYM5052 autoinduction medium with 100 ug/mL ampicillin and 34 ug/mL chloramphenicol

### Purification Workflow

- **Expression system**: E. coli Rosetta2(DE3)pLysS
- **Expression construct**: Full-length ESR with C-terminal hexahistidine tag
- **Tag info**: C-terminal hexahistidine tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane fraction isolation | Centrifugation | — |  | Obtained membrane fraction after cell lysis |
| Extraction | Detergent solubilization | — | 50 mM Tris, 10 mM imidazole, pH 8.0 + 1% n-dodecyl-beta-D-maltopyranoside (DDM) | Overnight at 4 C |
| Ni-NTA affinity chromatography | Affinity chromatography | Ni-Sepharose 6 Fast Flow (GE Healthcare) | Buffer 1: 50 mM sodium phosphate, 500 mM NaCl, 2 M urea, 0.1% DDM, 10 mM imidazole, pH 8.0; Buffer 2: 50 mM sodium phosphate, 200 mM NaCl, 0.1% DDM, 20 mM imidazole, pH 8.0 | Wash with buffer 1 and buffer 2; eluted with 50 mM sodium phosphate, 200 mM NaCl, 0.1% DDM, 0.01% Na azide, 300 mM imidazole, pH 7.4 |
| Imidazole removal and concentration | Ultrafiltration | Amicon regenerated cellulose membrane, 10 kDa MWCO |  | Final concentration up to 2 mg/mL |

**Final sample**: ESR at up to 2 mg/mL in 50 mM sodium phosphate, 200 mM NaCl, 0.1% DDM, 0.01% Na azide, pH 7.4


## Crystallization

### doi/10.1073##pnas.1221629110

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (in meso) crystallization |
| Protein sample | Purified ESR at 35 mg/mL in crystallization buffer |
| Lipid | Monoolein (Nu-Chek Prep) |
| Protein-to-lipid ratio | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Crystals grown using the in meso approach. Best crystals obtained at protein concentration of 35 mg/mL. |


## Biological / Functional Insights

### Lysine as proton donor in proteorhodopsins

ESR's proton donor is Lys-96, a lysine side chain situated very close to
the bulk solvent. This contrasts with BR (Asp-96) and XR (Glu-107),
where the proton donor is a carboxylic acid far from the bulk. Lys-96
is immersed in a mostly hydrophobic cavity and may have a pKa as low
as 5.3, allowing it to function as a proton donor. The cavity is
separated from the bulk solvent only by Thr-43, providing easy direct
access of protons from the cytoplasm.

### Helix F structural disruption in proteorhodopsins

The alpha-helical structure in the middle of helix F is replaced by
3_10- and pi-helix-like elements stabilized by Trp-154 and Asn-224 side
chains. This feature is characteristic of the proteorhodopsin family of
proteins and distinguishes them from other microbial rhodopsins. The
structural disruption is unique to ESR among known retinylidene protein
structures.

### Proton release region with continuous water chain

The proton release region is connected to the bulk solvent by a chain
of water molecules already in the ground state. In ESR, the histidine
residue (His-57) of the putative proton release group (Asp-221/His-57)
is immersed in a cavity of sufficient size for a water molecule from
the bulk to contact it. This continuous cavity contains ordered water
molecules and transitions into the bulk.

### Broad pH range proton pumping

ESR functions across a broad pH range (4.5-8.5). The Asp-85/His-57 pair
allows stabilization of Asp-85 in the unprotonated state across this
wide pH range. Lys-96 with its reduced pKa may serve as a key element
of stabilization of proton pumping under varying environmental
conditions, consistent with E. sibiricum's permafrost habitat
characterized by pH 5.6-7.8.


## Cross-References

- [Bacteriorhodopsin (bR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archetypal light-driven proton pump; ESR shares the seven-helix retinylidene protein fold but with unique structural features
- [Xanthorhodopsin](/xray-mp-wiki/proteins/rhodopsins/xanthorhodopsin/) — Eubacterial proton pump with dual chromophore; comparison of proton uptake regions reveals ESR's unique lysine proton donor
- [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) — ESR is the first high-resolution proteorhodopsin structure within the microbial rhodopsin family
- [Proton Pump Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/proton-pump-mechanism/) — ESR reveals unusual proton pumping features including lysine as proton donor and continuous water chain to bulk solvent
- [n-Dodecyl-beta-D-Maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and purification of ESR
