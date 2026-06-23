---
title: "XTRIC-B (Xenopus TRIC-B Channel)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1817271116]
verified: false
---

# XTRIC-B (Xenopus TRIC-B Channel)

## Overview

XTRIC-B is the Xenopus tropicalis ortholog of the TRIC-B subtype of trimeric intracellular cation (TRIC) channels. TRIC-B synchronizes with inositol 1,4,5-trisphosphate receptors (IP3Rs) to mediate Ca2+ release from intracellular stores. XTRIC-B shares 48% sequence identity with [GgTRIC-A (Chicken Trimeric Intracellular Cation Channel A)](/xray-mp-wiki/proteins/voltage-gated-channels/ggtric-a/), 46% with human HsTRIC-A, and 54% with human HsTRIC-B. The structure was determined at 3.1 A resolution by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using the [GgTRIC-A (Chicken Trimeric Intracellular Cation Channel A)](/xray-mp-wiki/proteins/voltage-gated-channels/ggtric-a/) structure.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1817271116 |  | 3.1 |  | Xenopus XTRIC-B, full-length |  |
| doi/10.1073##pnas.1817271116 |  |  |  | Xenopus XTRIC-B, Ca2+-free state |  |

## Expression and Purification

- **Expression system**: Schizosaccharomyces pombe (yeast)
- **Construct**: Full-length XTRIC-B with codon optimization
- **Notes**: Gene synthesized with codon optimization for S. pombe expression; identified as stable candidate for structural and functional characterization

### Purification Workflow

- **Expression system**: Schizosaccharomyces pombe
- **Expression construct**: Full-length XTRIC-B

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Affinity purification | Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — | 20 mM HEPES pH 7.5, 150 mM KCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.06% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) | Solubilized in octyl glucose-neopentyl glycol ([OGNG](/xray-mp-wiki/reagents/detergents/ogng/)) amphiphiles; purification similar to [GgTRIC-A (Chicken Trimeric Intracellular Cation Channel A)](/xray-mp-wiki/proteins/voltage-gated-channels/ggtric-a/) |


## Crystallization

### doi/10.1073##pnas.1817271116

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified XTRIC-B in 20 mM HEPES pH 7.5, 150 mM KCl, 0.06% [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) |
| Reservoir | Multiple conditions (see SI Appendix Table S2) |
| Notes | Crystallized in multiple lattices. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using [GgTRIC-A (Chicken Trimeric Intracellular Cation Channel A)](/xray-mp-wiki/proteins/voltage-gated-channels/ggtric-a/) as search model. Structures determined in both Ca2+-bound and Ca2+-free states at resolutions down to 3.1 A. |


## Biological / Functional Insights

### Conserved TRIC architecture across subtypes

XTRIC-B adopts the same overall fold as [GgTRIC-A (Chicken Trimeric Intracellular Cation Channel A)](/xray-mp-wiki/proteins/voltage-gated-channels/ggtric-a/), with an rmsd of 0.92 A for 221 superimposed C-alpha atoms of the protomer and 1.14 A for 665 superimposed C-alpha atoms of the trimer. Both share similar topological organization, trimeric assembly architecture, and surface electrostatic characteristics with prokaryotic TRICs and invertebrate TRICs from C. elegans. The transmembrane helices are more inclined within the membrane compared to prokaryotic TRICs and adopt a more expanded conformation.

### TRIC-B as a counter-ion channel for IP3R-mediated Ca2+ release

TRIC-B functionally couples with IP3Rs (rather than RyRs) to mediate intracellular Ca2+ release. Purified XTRIC-B reconstituted into planar lipid bilayers conducts K+ currents with characteristics similar to those of mammalian TRIC-B, validating the structural studies as representative of functional TRIC-B channels.


## Cross-References

- [GgTRIC-A (Chicken TRIC-A)](/xray-mp-wiki/proteins/voltage-gated-channels/ggtric-a/) — Vertebrate TRIC-A subtype used as molecular replacement model; high sequence identity (48%) and conserved architecture
- [Diacylglycerol (DAG)](/xray-mp-wiki/reagents/lipids/dag/) — Lipid identified at protomer interfaces in TRIC channels; DAG binds at lateral fenestrations
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) — Detergent used in purification or crystallization
