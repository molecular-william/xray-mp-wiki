---
title: TcdB2-TccC3 Toxin Complex B-C Fusion from Photorhabdus luminescens
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##nature13015]
verified: false
---

# TcdB2-TccC3 Toxin Complex B-C Fusion from Photorhabdus luminescens

## Overview

TcdB2-TccC3 is a fusion protein from Photorhabdus luminescens subsp. akhurstii composed of the TcB and TccC3 subunits of the Tc toxin complex. It forms a large cocoon structure that encapsulates and protects the toxic ADP-ribosyltransferase domain (TccC3 C-terminal hypervariable region). The TcB subunit contains a six-bladed beta-propeller that functions as a gate, opening upon binding to TcA to allow translocation of the toxic domain. The structure was solved at 2.35 A resolution by experimental phasing and represents a central component of the Tc toxin translocation machinery.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13015 | not specified | 2.35 A | not specified | TcdB2-TccC3 fusion protein from P. luminescens subsp. akhurstii (1.1 MDa cocoon) | None |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)
- **Construct**: TcdB2-TccC3 fusion protein from P. luminescens subsp. akhurstii, overexpressed and purified as previously described

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and expression | Overexpression in E. coli BL21(DE3) | -- | not specified + -- | TcdB2-TccC3 overexpressed and purified as previously described |
| Dialysis | Dialysis | -- | 50 mM Tris pH 8.0, 100 mM NaCl, 0.05% Tween-20, 5% glycerol + Tween-20 | Dialysis of TcdB2-TccC3 against purification buffer |
| Size-exclusion chromatography | Size-exclusion chromatography | Superose 6 10/300 GL column (GE Healthcare Life Sciences) | 50 mM Tris pH 8.0, 100 mM NaCl, 0.05% Tween-20, 5% glycerol + Tween-20 | Final purification step, concentrated to 10 mg/mL using Amicon filter devices |


## Crystallization

### doi/10.1038##nature13015

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 10 mg/mL TcdB2-TccC3 in 50 mM Tris pH 8.0, 100 mM NaCl, 0.05% Tween-20, 5% glycerol |
| Reservoir | 0.1 M trisodium citrate pH 5.5, 0.1 M MgCl2, 0.1 M NaCl, 12% PEG 4000 |
| Temperature | 4 C |
| Growth time | 3-5 days |
| Cryoprotection | Reservoir solution with 25% glycerol, flash frozen in liquid nitrogen |
| Notes | Crystals reached approximately 100 x 60 x 60 micrometers. Data collected at PXII-X10SA beamline at Swiss Light Source. Structure solved by experimental phasing using K2Pt(NO2)4 and EMTS heavy metal derivatives. |


## Biological / Functional Insights

### Cocoon structure and toxic domain encapsulation

TcB and TcC are built by large beta-sheets that wind to form a large cocoon structure with upper and lower chambers. The TcB subunit comprises the TcA-binding domain that folds into a non-symmetrical six-bladed beta-propeller. The TccC3 subunit contains the toxic ADP-ribosyltransferase domain (C-terminal hypervariable region) trapped inside the cocoon. The cocoon interior provides a hostile environment where the toxic domain is probably unfolded and autoproteolytically cleaved by the intrinsic aspartyl protease activity of TcC.

### Beta-propeller gate mechanism

The six-bladed beta-propeller of TcB forms a distorted gate that is closed in isolation but opens upon binding to the pentameric funnel of TcA. The gate opening creates a continuous channel connecting the cocoon interior with the TcA translocation pore. The beta-propeller adapts to the symmetry mismatch by acquiring pseudo-five-fold symmetry. The major part of the open beta-propeller pore is hydrophobic, acting similarly to the phi-clamp in anthrax toxin to protect hydrophobic patches in the translocated protein.

### Intrinsic aspartyl protease activity of TccC3

The TccC3 subunit contains an intrinsic aspartyl protease domain with a catalytic dyad (D651 and D674) that autoproteolytically cleaves the C-terminal toxic domain. The hyperconserved region of TcC contains two highly conserved catalytic aspartate residues. Mass spectrometry analysis confirmed that the ADP-ribosyltransferase domain is trapped inside the TcB-TccC3 cocoon in its cleaved form.

### TcA-TcB interaction interface

The beta-propeller of TcB and the funnel domain of TcA interact strongly with each other, identifying them as the TcA-binding and TcB-binding domains respectively. In the absence of complementary charges or matching hydrophobic patches, shape complementarity and induced fit drive the specific interaction. The conformational changes induce rearrangement of the beta-propeller blades, opening the gate and allowing passage of the toxic component into the target cell.


## Cross-References

- [TcdA1 Toxin Complex A Subunit](/xray-mp-wiki/proteins/tcdA1/) — TcB binds to TcA, forming the holotoxin complex and opening the beta-propeller gate
- [Tween-20](/xray-mp-wiki/reagents/additives/tween-20/) — 0.05% Tween-20 in TcdB2-TccC3 purification buffer
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — 50 mM Tris pH 8.0 in TcdB2-TccC3 purification and storage buffer
- [Magnesium Chloride](/xray-mp-wiki/reagents/additives/mgcl2/) — 0.1 M MgCl2 in TcdB2-TccC3 crystallization reservoir
- [Polyethylene Glycol 4000](/xray-mp-wiki/reagents/peg-4000/) — 12% PEG 4000 precipitant in TcdB2-TccC3 crystallization
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/hanging-drop-vapor-diffusion/) — Crystallization method used for TcdB2-TccC3
- [Multi-Wavelength Anomalous Diffraction](/xray-mp-wiki/methods/multi-wavelength-anomalous-diffraction/) — SAD phasing used for TcdB2-TccC3 structure solution
- [Syringe-Like Injection Mechanism](/xray-mp-wiki/concepts/syringe-injection-mechanism/) — TcdB2-TccC3 delivers toxic domain through TcA translocation channel
