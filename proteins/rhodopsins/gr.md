---
title: "GR (Halobacterium sp. GR Bacteriorhodopsin)"
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms8177]
verified: false
---

# GR (Halobacterium sp. GR Bacteriorhodopsin)

## Overview

GR (Halobacterium sp. GR [Bacteriorhodopsin](/xray-mp-wiki/proteins/bacteriorhodopsin)) is a [Light-Driven Proton Pump](/xray-mp-wiki/concepts/light-driven-proton-pump/) from Halobacterium sp. strain GR. It is a member of the [Microbial Rhodopsin Family](/xray-mp-wiki/concepts/microbial-rhodopsin/) family and functions as a [Light-Driven Proton Pump](/xray-mp-wiki/concepts/light-driven-proton-pump/). GR was engineered with point mutations to create blue-shifted variants using the same rational design principle applied to C1C2 and [HwBR (Halomonas Water Bacteriorhodopsin)](/xray-mp-wiki/proteins/hwbr). The wild-type GR exhibits a characteristic absorption maximum typical of bacteriorhodopsins. GR was expressed in E. coli BL21(DE3) using [Isopropyl-beta-D-thiogalactoside (IPTG)](/xray-mp-wiki/reagents/additives/iptg/) induction and purified using standard membrane protein purification protocols.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms8177 | 4YZI | not specified | not specified | GR wild-type and mutant variants | all-trans retinal |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: GR expression plasmid constructed as previously described
- **Notes**: Transformed E. coli BL21(DE3) cells grown at 18 C overnight in LB medium containing [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin) (50 ug/ml) and 5 uM [All-trans Retinal](/xray-mp-wiki/reagents/ligands/retinal/). [Isopropyl-beta-D-thiogalactoside (IPTG)](/xray-mp-wiki/reagents/additives/iptg/) induction (0.5 mM) used for GR expression (as opposed to L-arabinose for AR3 and [HwBR (Halomonas Water Bacteriorhodopsin)](/xray-mp-wiki/proteins/hwbr)).
- **Induction**: 0.5 mM [Isopropyl-beta-D-thiogalactoside (IPTG)](/xray-mp-wiki/reagents/additives/iptg/) ([IPTG](/xray-mp-wiki/reagents/additives/isopropyl-beta-d-thiogalactoside))

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell disruption and membrane fractionation | -- | 50 mM [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) (pH 6.5) containing 1 M [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) + -- | Cells harvested by centrifugation at 4 C, disrupted by sonication or French press passage |
| Solubilization | Detergent solubilization | -- | 50 mM [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) (pH 6.5), 1 M [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) + n-[n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) ([n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/)) | Cell membranes solubilized by [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni2+ [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni2+ affinity column (GE Healthcare) | Not specified + [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) | Purified by chromatography on Ni2+ affinity column |
| Concentration and buffer exchange | Ultrafiltration concentration | -- | 1 M [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM [Tris (Hydroxymethyl) Aminomethane](/xray-mp-wiki/reagents/buffers/tris/)-Cl (pH 7.0) + 0.05% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) | Purified sample concentrated using Amicon Ultra filter |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Blue-shifted GR variants created by rational design

GR was engineered with point mutations to create blue-shifted variants using the rational design principle established for C1C2. The mutations at positions equivalent to C1C2 residues 198 and 202 induce rotation of the beta-ionone ring of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal) chromophore, producing blue-shifted absorption spectra. GR variants were characterized by absorption spectroscopy in the presence of [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) at pH 7.0, demonstrating the transferability of the design principle across different [Microbial Rhodopsin Family](/xray-mp-wiki/concepts/microbial-rhodopsin/) families.

### GR as a platform for optogenetics tool development

GR [Bacteriorhodopsin](/xray-mp-wiki/proteins/bacteriorhodopsin) was identified as a suitable platform for rational design of blue-shifted variants. The successful engineering of GR with blue-shifted spectral properties demonstrates the generality of the atomistic design approach across diverse [Microbial Rhodopsin Family](/xray-mp-wiki/concepts/microbial-rhodopsin/) families, including bacteriorhodopsins from different Halobacterium strains.


## Cross-References

- [Archaerhodopsin-2](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-2/) — AR3 shares high sequence similarity with HwBR; same design principle applied to GR
- [C1C2GA (C1C2 T198G/G202A)](/xray-mp-wiki/proteins/rhodopsins/c1c2ga/) — GR was engineered using the same design principle as C1C2GA
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — GR is a bacteriorhodopsin from Halobacterium sp.
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane solubilization and protein purification
- [2-(N-morpholino)ethanesulfonic acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Buffer (50 mM, pH 6.5) used in cell lysis and membrane preparation
- [Isopropyl-beta-D-thiogalactoside (IPTG)](/xray-mp-wiki/reagents/additives/iptg/) — IPTG induction (0.5 mM) used for GR expression in E. coli
- [All-trans retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore covalently bound to conserved lysine via protonated Schiff base
- [IPTG](/xray-mp-wiki/reagents/additives/isopropyl-beta-d-thiogalactoside) — Referenced in gr
- [Light-Driven Proton Pump](/xray-mp-wiki/concepts/light-driven-proton-pump/) — Referenced in gr
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Referenced in gr
