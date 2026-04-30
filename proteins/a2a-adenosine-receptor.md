---
title: A2A Adenosine Receptor
created: 2026-04-26
updated: 2026-04-30
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, receptor]
sources: [doi/10.1002##anie.202115545, doi/10.1016##j.bbrc.2023.149393]
---

# A2A Adenosine Receptor (A2AAR)

## Overview

The human A2A adenosine receptor is a class A GPCR that couples to Gs proteins and plays a pivotal role in immunological processes and neurodegenerative diseases. It is an important drug target in immuno-oncology and Parkinson's disease research.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| Claff et al. (Angew. Chem. 2022) | 7PX4 | 2.25 Å | P2₁2₁2₁ | A2A-PSB1-bRIL (S91³·³⁹K, BRIL fusion in ICL3, C-terminal truncation) | PSB-2113 (PEGylated Preladenant) |
| Claff et al. (Angew. Chem. 2022) | 7PYR | 2.6 Å | P2₁2₁2₁ | A2A-PSB1-bRIL (S91³·³⁹K, BRIL fusion in ICL3, C-terminal truncation) | PSB-2115 (BODIPY-labeled Preladenant) |
| Araya et al. (Biochem. Biophys. Res. Commun. 2024) | 8WDT | 3.34 Å | — | A2AAR-Rag31 (thermostabilized mutant, Fab 35.1) | trans-photoNECA (blue) |

## Expression and Purification

- **Expression system**: HEK293 (mammalian, stable expression for PSB-2113/PSB-2115 structures); Sf9 (insect, baculovirus for photoNECA structure)
- **Construct**: A2A-PSB1-bRIL — single S91³·³⁹K mutation (lysine occupies allosteric sodium binding site), [bril](/xray-mp-wiki/reagents/protein-tags/bril/) (thermostabilized apocytochrome b562RIL, M7W/H102I/R106L) fused into ICL3, C-terminal truncation. A2AAR-Rag31 — thermostabilized mutant for agonist-bound structure.

### Purification Workflow

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Solubilization (PSB structures) | Detergent | — | 1% [ddm](/xray-mp-wiki/reagents/detergents/ddm/) in membrane buffer | HEK293 cell membranes |
| 2. Affinity | His-tag IMAC | His-tag on [bril](/xray-mp-wiki/reagents/protein-tags/bril/) | — | Elution with imidazole |
| 3. SEC | Size-exclusion | Superdex 200 increase 10/300 | 20 mM [hepes-buffer](/xray-mp-wiki/reagents/buffers/hepes-buffer/) pH 7.5, 150 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 0.05% [ddm](/xray-mp-wiki/reagents/detergents/ddm/), 1 μM ligand | PSB-2113 or PSB-2115 |
| 4. Solubilization (photoNECA) | Detergent | — | 1% [ddm](/xray-mp-wiki/reagents/detergents/ddm/) in buffer | SF9 cell membranes |
| 5. Complex formation | Mixing | — | — | A2AAR-Rag31 + Fab 35.1 fragment |
| 6. SEC | Size-exclusion | — | Buffer with [ddm](/xray-mp-wiki/reagents/detergents/ddm/) | Gel filtration of complex |

**Final sample**: 1 μM ligand in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% DDM (PSB structures); A2AAR-Rag31 + Fab 35.1 complex in DDM buffer (photoNECA structure)

## Crystallization

### Claff et al. (Angew. Chem. 2022) — Sitting-drop vapor diffusion

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | A2A-PSB1-bRIL in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% DDM, 1 μM ligand |
| Reservoir | 0.1 M sodium acetate pH 4.5, 18–20% [peg-400](/xray-mp-wiki/reagents/additives/peg-400/) |
| Mixing ratio | 1:1 protein:reservoir |
| Temperature | 20 °C |
| Growth time | 1–2 weeks |

### Araya et al. (BBRC 2024) — Lipidic cubic phase

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | A2AAR-Rag31 + Fab 35.1 + trans-photoNECA in DDM buffer |
| Lipid | [monoolein](/xray-mp-wiki/methods/crystallization/monoolein/) |
| Protein-to-lipid ratio | 1:2 (w/w) |
| Temperature | 20 °C |
| Growth time | 1–2 weeks |
| Notes | Crystallization performed in dark/red light (640–660 nm) to prevent trans-to-cis photoisomerization |

## Biological / Functional Insights

### Ligand Binding Pocket

- PSB-2113 binds in the same orientation as ZM241385
- Key interactions: H-bond to N253⁶·⁵⁵ and E169ᴱᶜˡ² via furan oxygen and 5-amino group
- π-π stacking to F168ᴱᶜˡ²
- Hydrophobic contacts to L249⁶·⁵¹ and I274⁷·³⁹
- Displacement of "unhappy waters" from binding pocket contributes to high affinity

### photoNECA Binding Mode

- NECA moiety binds in orthosteric site
- Photoswitching moiety binds in hydrophobic pocket (Ser67²·⁶⁵, Leu167ᴱᶜˡ², Leu267⁷·³², Tyr271⁷·³⁶)
- Explains A2AAR vs A1R subtype selectivity: hydrophobic pocket in A2AAR vs. polar pocket in A1R (Asn70²·⁶⁵, Glu170ᴱᶜˡ², Ser267⁷·³²)

### Thermostabilization Strategy

- Single S91³·³⁹K mutation provides superior thermostability compared to 9-mutation A2A-StaR2
- A2A-StaR2 mutations T88³·³⁶A and S277⁷·⁴²A are located in the orthosteric ligand-binding pocket and interfere with agonist binding
- A2A-PSB1-bRIL avoids mutations in the orthosteric pocket

## Cross-References

- [etb-receptor](/xray-mp-wiki/proteins/etb-receptor/) — ETB-Y5-T4L: thermostabilized GPCR with BRIL fusion
- [kappa-opioid-receptor](/xray-mp-wiki/proteins/kappa-opioid-receptor/) — Opioid GPCR crystallized with nanobody
- [bril](/xray-mp-wiki/reagents/protein-tags/bril/) — Thermostabilized apocytochrome b562RIL fusion partner
- [vapor-diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion/) — Vapor diffusion crystallization method
- [lipidic-cubic-phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization method
- [hep293-cells](/xray-mp-wiki/methods/expression-systems/hek293-cells/) — HEK293 mammalian expression system
- [sf9-cells](/xray-mp-wiki/methods/expression-systems/sf9-cells/) — Sf9 insect cell expression system
- [baculovirus-expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression/) — Baculovirus expression system