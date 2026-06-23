---
title: "Salmonella enterica Citrate/Sodium Symporter (SeCitS)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.7554##eLife.09375]
verified: false
---

# Salmonella enterica Citrate/Sodium Symporter (SeCitS)

## Overview

SeCitS is a [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/)/sodium symporter from the human pathogen *Salmonella enterica*. It belongs to the 2-hydroxycarboxylate transporter (2-HCT) family and mediates sodium-dependent uptake of [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) (HCit2-) as a carbon source. The 2.5 A X-ray structure revealed an asymmetric dimer with three distinct conformational states -- one outward-facing and two inward-facing -- which together elucidated a six-step transport mechanism involving a 31-degree rigid-body rotation of a helix bundle that translocates substrates by 16 A across the membrane.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.09375 | 5a1s | 2.5 | P1 | Full-length SeCitS with N-terminal His10-tag (cleaved by thrombin) | [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/), Na+ |
| doi/10.7554##eLife.09375 | 5a1s | 3.9 | P21 | Selenomethionine-substituted SeCitS | [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/), Na+ |

## Expression and Purification

- **Expression system**: E. coli C41-(DE3)
- **Construct**: N-terminal His10-tag, thrombin cleavage site
- **Induction**: Autoinduction (native); [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600 0.5 (SeMet)
- **Media**: ZYM-5052 autoinduction medium (native); defined medium with methionine biosynthesis inhibition (SeMet)

### Purification Workflow

- **Expression system**: E. coli C41-(DE3)
- **Expression construct**: Full-length SeCitS, N-His10-thrombin
- **Tag info**: His10-tag removed by on-column thrombin cleavage

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and harvest | Microfluidizer (M-110L) | — | 20 mM Tris/HCl pH7.4, 150 mM NaCl, 5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), 5 mM beta-ME | Cells resuspended after harvest |
| Membrane isolation | Ultracentrifugation | — | 20 mM Tris/HCl, 140 mM [Choline](/xray-mp-wiki/reagents/ligands/choline/) chloride, 250 mM [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/), 1 mM Na-[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/), 5 mM beta-ME | 100,000 g for 1 h; resuspended at 15 mg/ml total protein |
| Solubilization | Detergent solubilization | — | 20 mM Tris/HCl pH7.4, 150 mM NaCl, 1 mM Na-[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/), 5 mM beta-ME + 1.5% [DM](/xray-mp-wiki/reagents/detergents/dm/) (DM) | 1:1 dilution of membranes with 3% DM buffer; 100,000 g clarification |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | Ni-NTA agarose | 20 mM Tris/HCl pH7.4, 300 mM NaCl, 45 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 1 mM Na-[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/), 0.15% DM, 5 mM beta-ME | On-column thrombin cleavage overnight at 4 C (1 U/mg) |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM Tris/HCl pH8.2, 150 mM NaCl, 1 mM Na-[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/), 0.15% DM, 1 mM TCEP | Concentrated to 5 mg/ml (50 kDa cutoff) before SEC |

**Final sample**: 5 mg/ml in 20 mM Tris/HCl pH8.2, 150 mM NaCl, 1 mM Na-[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/), 0.15% DM, 1 mM TCEP


## Crystallization

### doi/10.7554##eLife.09375

| Parameter | Value |
|---|---|
| Method | [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | Native SeCitS supplemented with 1% [OG](/xray-mp-wiki/reagents/detergents/og/) (OG) |
| Reservoir | 100 mM MES pH6.5, 200 mM NaCl, 29% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) |
| Mixing ratio | 1:1 |
| Temperature | 20 C (room temperature) |
| Growth time | 3-7 days |
| Cryoprotection | Al's oil |
| Notes | Rhombic crystals, ~150 um |

| Parameter | Value |
|---|---|
| Method | [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | SeMet SeCitS supplemented with 2% [HG](/xray-mp-wiki/reagents/detergents/n-heptyl-beta-d-glucopyranoside/) (HG) |
| Reservoir | 100 mM MES pH6.5, 250 mM NaCl, 30% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) |
| Mixing ratio | 1:1 |
| Temperature | 20 C |
| Growth time | Up to 7 days |
| Notes | Thin needle-like crystals, ~400 um; vitrified directly in liquid nitrogen |


## Biological / Functional Insights

### Asymmetric dimer with three conformational states

The SeCitS crystal structure captured an asymmetric dimer where one protomer is in the outward-facing state and two are in different inward-facing states (B and B'). This is unique for a membrane transporter crystal structure. The dimer asymmetry cannot be attributed to crystal packing as both dimers in the asymmetric unit are almost identical (rmsd 0.5 A).

### Six-step transport mechanism

A six-step transport cycle was deduced: (1) Two Na+ ions bind to the outward-facing empty transporter; (2) [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) (HCit2-) binds from the external medium; (3) [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) binding triggers a 31-degree arc-like rigid-body rotation of the helix bundle, translocating bound substrates by 16 A; (4) [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) is released to the cytoplasm; (5) Na+ ions are released (Na2 before Na1); (6) The empty protomer reverts to the outward-facing state. The process is electroneutral and driven by the inward-directed Na+ gradient.

### Substrate binding and release order

[Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) is released before Na+ ions in the inward-facing state. Comparison of protomers B and B' shows unambiguous evidence: B' has an empty Na2 site while [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) is already partially released. The Na2 site empties before Na1. Both Na+ ions must bind before [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) can bind to the outward-facing state.


## Cross-References

- [MES (2-(N-Morpholino)ethanesulfonic Acid)](/xray-mp-wiki/reagents/buffers/mes/) — MES was used as crystallization buffer for SeCitS
- [n-Decyl-beta-D-Maltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — DM was used for solubilization and purification of SeCitS
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Method used in structure determination or purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [PEG400](/xray-mp-wiki/reagents/additives/peg-400/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) — Buffer component in purification or crystallization
