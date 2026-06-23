---
title: "MjNhaP1 Sodium/Proton Antiporter"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.7554##ELIFE.03583]
verified: false
---

# MjNhaP1 Sodium/Proton Antiporter

## Overview

MjNhaP1 is an electroneutral Na+/H+ antiporter from the archaeon *Methanocaldococcus jannaschii*, belonging to the CPA1 family of cation-proton antiporters. It exchanges one Na+ for one H+ and plays roles in pH, ion, and volume homeostasis. The structure was determined in two complementary states: an inward-open state by X-ray crystallography at pH 8 with sodium (3.5 Å resolution, PDB 4CZB), and an outward-open state by electron crystallography at pH 4 without sodium (6 Å resolution, EMDB-2636). The conformational transition involves a ~7° tilt of a 6-helix bundle and a ~5 Å vertical relocation of the ion binding site, consistent with a rocking bundle mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##ELIFE.03583 | 4CZB | 3.5 | P21 | Full-length MjNhaP1 (untagged, CPD fusion) | Na+ |
| doi/10.7554##ELIFE.03583 | EMD-2636 | 6.0 | — | 2D crystals at pH 4, no NaCl |  |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)
- **Construct**: MjNhaP1 with C-terminal CPD fusion (untagged after cleavage)
- **Notes**: CPD fusion removed by low pH elution during purification
- **Induction**: ZYM-5052 autoinduction medium, 37°C

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest and lysis | Microfluidizer | — | 50 mM Tris/HCl pH 7.5, 140 mM [Choline](/xray-mp-wiki/reagents/ligands/choline/) chloride, 250 mM [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) |  |
| Membrane isolation | Ultracentrifugation | — |  | 100,000×g, 4°C, 1 hr |
| Membrane protein extraction | Detergent extraction | — | 150 mM MOPS/KOH pH 7.0, 45% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + ~2.0% [Foscholine-12](/xray-mp-wiki/reagents/detergents/foscholine-12/) | 2 hr at 4°C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | IgG affinity (CPD binding) | — | 500 mM NaCl, 15 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (wash); sodium-free buffer (15 mM Tris/HCl pH 7.5, 200 mM KCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)) (wash) | CPD fusion binds to IgG resin via its pro-domain |
| Elution and tag cleavage | pH elution | — | 50 mM [Potassium acetate](/xray-mp-wiki/reagents/additives/potassium-acetate/) pH 4, 100 mM KCl, 5 mM MgCl2 + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Low pH elution also cleaves CPD tag |

**Final sample**: Purified untagged MjNhaP1 in elution buffer
**Purity**: Monodisperse on SEC


## Crystallization

### doi/10.7554##ELIFE.03583

| Parameter | Value |
|---|---|
| Method | [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | Purified MjNhaP1 (heat-treated 85°C, 15 min; centrifuged 125,000×g, 1 hr; filtered) |
| Reservoir | 100 mM Tris/Cl pH 8.2, 24% [PEG](/xray-mp-wiki/reagents/additives/peg/) 1000 |
| Temperature | 20 |
| Growth time | 10-14 days |
| Cryoprotection | Direct vitrification in liquid nitrogen |
| Notes | 3D crystals for X-ray; maximal size 350 µm |


## Biological / Functional Insights

### Two-state conformational cycle

MjNhaP1 adopts inward-open (pH 8 + Na+) and outward-open (pH 4, no Na+) states. The 6-helix bundle (H3, H4, H5, H6, H12, H13) tilts by ~7° as a rigid body, closing the extracellular cavity while opening the cytoplasmic funnel. The ion binding site (coordinated by Asp132, Thr131 backbone, Ser157, Asp161) moves vertically by ~5 Å during the transition.

### Transport mechanism

The transport cycle involves four steps: (i) a proton from the cell replaces bound Na+, releasing Na+ to the cytoplasm; (ii) upon protonation of Asp161, the antiporter switches to the outward-open state; (iii) extracellular Na+ displaces the proton at Asp161; (iv) deprotonation and Na+ binding trigger the switch back to the inward-open state. This is consistent with a rocking bundle alternating-access mechanism.

### Electroneutral vs electrogenic transport

MjNhaP1 is electroneutral (1 Na+:1 H+), characteristic of CPA1 antiporters. The ND motif (Asn160-Asp161) in H6 is essential for function. Replacing N160 with alanine abolishes activity; N160D retains reduced activity but is not electrogenic. CPA2 antiporters (EcNhaA, TtNapA) use a DD motif and exchange 2 H+:1 Na+. Despite different stoichiometries, the overall fold and conformational changes are similar across [CPA](/xray-mp-wiki/reagents/ligands/cyclopiazonic-acid/) families.


## Cross-References

- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Method used in structure determination or purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Potassium acetate](/xray-mp-wiki/reagents/additives/potassium-acetate/) — Additive used in purification or crystallization buffers
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
- [Foscholine-12](/xray-mp-wiki/reagents/detergents/foscholine-12/) — Detergent used in purification or crystallization
- [Choline](/xray-mp-wiki/reagents/ligands/choline/) — Related ligand or cofactor
- [CPA](/xray-mp-wiki/reagents/ligands/cyclopiazonic-acid/) — Related ligand or cofactor
