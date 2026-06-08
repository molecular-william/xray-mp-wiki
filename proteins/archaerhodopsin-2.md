---
title: Archaerhodopsin-2
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2007.11.039, doi/10.1038##ncomms8177]
verified: false
---

# Archaerhodopsin-2

## Overview

Archaerhodopsin-2 (aR2) is a light-driven proton pump found in the claret membrane of Halorubrum sp. aus-2. It shares 56% sequence identity with bacteriorhodopsin and forms a trimeric complex with the carotenoid bacterioruberin, which plays a striking structural role in stabilizing the trimer. The crystal structure reveals how bacterioruberin binds in the crevices between subunits, trapping specific lipids and creating a suitable environment for the conformational changes required during proton pumping.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2007.11.039 | 2KZB | 2.1 A | P321 | aR2 trimer with bacterioruberin and glycolipid | bacterioruberin, retinal |
| doi/10.1016##j.jmb.2007.11.039 | 2KZC | 2.3 A | P63 | aR2 trimer with bacterioruberin and glycolipid | bacterioruberin, retinal |
| doi/10.1016##j.jmb.2007.11.039 | 1VGO | 2.5 A | C2221 | aR2 monomer (previous crystal form without bacterioruberin) | retinal |

## Expression and Purification

- **Expression system**: Halorubrum sp. aus-2 (native expression)
- **Construct**: Full-length aR2, 238 residues, 7 transmembrane helices (A-G), N-terminal omega loop, anti-parallel beta-sheet in BC loop

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Claret membrane preparation | Cell disruption and membrane fractionation | -- | -- + -- | Claret membrane vesicles from Halorubrum sp. aus-2; contains aR2, bacterioruberin, and endogenous lipids |
| Membrane fusion crystallization | Membrane fusion method | -- | -- + -- | Vesicular assemblies and/or tubular membrane networks formed in protein-rich phase; crystals grew within the protein-rich phase over several months |


## Crystallization

### doi/10.1016##j.jmb.2007.11.039

| Parameter | Value |
|---|---|
| Method | Membrane fusion (vapour-diffusion-based) |
| Protein sample | aR2 claret membrane vesicles |
| Reservoir | High concentration (~1 M) ammonium sulfate |
| Temperature | 15 C |
| Growth time | Several months |
| Notes | Significant phase separation occurred; aR2 molecules moved to protein-rich phase floating in solution or adhering to glass. Trigonal P321 crystals appear as thin plates. Rod-shaped hexagonal P63 crystals grow thicker. Cryocooled to 100 K for X-ray data collection at SPring8-BL38B1 and -BL41XU (wavelength 1.0 A). |


## Biological / Functional Insights

### Bacterioruberin stabilizes the aR2 trimer through specific binding

Bacterioruberin binds to crevices between neighbouring monomers within the trimeric structure. Its polyene chain is inclined ~20 degrees from the membrane normal and is surrounded by hydrophobic residues from helices AB of one subunit and helices DE of an adjacent monomer. This peculiar binding mode suggests that bacterioruberin plays a striking structural role for the trimerization of aR2. The terminal OH groups of bacterioruberin interact with Trp36 and Arg44 in one subunit and Thr112 (or Thr115) and Tyr156 of another subunit.

### Glycolipid binding stabilizes the trimeric structure

Glycolipids bind to the central region of the trimer. The hydrophilic part is composed of three hexoses connected in tandem. The head group interacts with two neighbouring monomers, contributing to the stabilization of the trimeric structure. This lipid may represent a part of archaeal glycocardiolipin.

### Trimerization creates a suitable lipid environment for helix C dynamics

Despite large alteration in the amino acid sequence between aR2 and bacteriorhodopsin, the shape of the intratrimer hydrophobic space filled by lipids is highly conserved. A transmembrane helix (helix C) facing this space undergoes a large conformational change during the proton pumping cycle. Trimerization is an important strategy to capture special lipid components that enable the protein to undergo proper conformational changes.

### Proton release channel conformation depends on trimeric state

When compared with the aR2 structure in the C2221 crystal form (monomeric, no bacterioruberin), the proton release channel takes a more closed conformation in the P321 or P63 crystal form. The native conformation of the protein is stabilized in the trimeric protein-bacterioruberin complex. In the C2221 crystal, the extracellular end of helix C is deformed largely, suggesting the conformation is very sensitive to lipid-protein interaction.

### Trimerization increases thermal stability and widens pH range

The most important contribution of trimerization is to increase the thermal stability of the protein. Trimerization also widens the pH range where the protein can keep the neutral purple conformation: in the trimeric state, the neutral purple conformation is maintained between pH 3 and pH 10, whereas in the monomeric state it is stable only in a very restricted pH range (acid blue transition at pH ~4 and alkaline red transition at pH ~7).

### Inefficient energy transfer from bacterioruberin to retinal

The shortest distance between bacterioruberin and retinal is 17 A. The energy transfer efficiency from bacterioruberin to retinal is estimated to be very low (~0.02) due to the very low fluorescence quantum yield of bacterioruberin (~10^-5 in the apoprotein) and suboptimal mutual orientation. This suggests bacterioruberin does not serve as an antenna molecule for aR2.


## Cross-References

- [Bacteriorhodopsin](/xray-mp-wiki/proteins/bacteriorhodopsin/) — Homologous protein (56% sequence identity), forms trimeric structure without bacterioruberin
- [Bacterioruberin](/xray-mp-wiki/reagents/lipids/bacterioruberin/) — Carotenoid ligand that binds to trimer crevices and stabilizes the aR2 trimeric structure
- [Glycolipid](/xray-mp-wiki/reagents/lipids/glycolipid/) — Binds to central region of the trimer; stabilizes the trimeric structure
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Used at ~1 M concentration in crystallization reservoir solution
