---
title: Cubic Lipid Phase Crystallization
created: 2026-06-16
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [crystallization-lcp, subdirectory-crystallization]
sources: [doi/10.1006##jmbi.1999.3027, doi/10.1016##S0022-2836(03)00751-4, doi/10.1021##bi900545e]
verified: false
---

# Cubic Lipid Phase Crystallization

## Overview

Cubic lipid phase (CLP) crystallization is a method for crystallizing membrane proteins within a lipidic cubic phase matrix. Developed by Landau & Rosenbusch (1996), it was used to obtain the 1.55 Å resolution structure of bacteriorhodopsin (PDB 1C3W). The method maintains membrane proteins in a lipid environment that mimics the native bilayer during crystallization. The related lipidic sponge phase (LSP) variant uses additives to create a less viscous phase suitable for proteins with large hydrophilic domains, as demonstrated with the Blastochloris viridis photosynthetic reaction center (PDB 2WJM, 1.86 Å).

## Principle

The lipidic cubic phase is a bicontinuous lipid-water system with a curved bilayer that provides a membrane-like environment. Membrane proteins diffuse within the bilayer and can form crystal nuclei at controlled rates, yielding tightly packed crystals with low solvent content.

## Protocol

### Reagents and Materials

- Monoolein (mono-oleoyl-glycerol)
- Salt/precipitant solution (e.g., 3 M sodium phosphate)

### Steps

1. {'step': '1. Prepare lipid cubic phase by mixing monoolein with aqueous protein solution', 'method': 'Mechanical mixing (centrifugation/syringe mixing)'}
2. {'step': '2. Add precipitant solution to trigger crystallization', 'method': 'Vapor diffusion or batch method'}
3. {'step': '3. Incubate until crystals appear (days to weeks)', 'method': 'Temperature-controlled incubation'}
4. {'step': '4. Harvest crystals and remove adhering lipid phase', 'method': 'Soaking in mild detergent solution (e.g., 0.1% octylglucoside)'}

### Typical Conditions

- **temperature**: 293 K (room temperature)
- **protein_concentration**: Typically 5-10 mg/mL
- **lipid_to_protein_ratio**: Typically 60:40 to 70:30 (w/w)
- **reservoir**: 3 M sodium phosphate (pH 5.6) for bacteriorhodopsin


## Advantages

- Membrane protein remains in lipid environment
- Produces tightly packed crystals with low solvent content
- Can yield very high resolution data (e.g., 1.55 Å for bacteriorhodopsin)
- Preserves native lipid interactions

## Disadvantages

- Small crystal size typical (~80 um)
- Requires mechanical extraction of crystals from viscous lipid phase
- Difficult to visualize crystals in opaque lipid matrix

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Bacteriorhodopsin](/xray-mp-wiki/proteins/Bacteriorhodopsin/) | 1.55 | 1C3W | First membrane protein structure solved by CLP method; atomic resolution. |
| [Rhodobacter sphaeroides reaction centre](/xray-mp-wiki/proteins/Rhodobacter sphaeroides reaction centre/) | 2.35 | 1ogv | First type I crystal packing for a purple bacterial reaction centre; cardiolipin-mediated crystal contacts identified. |
| [Blastochloris viridis Photosynthetic Reaction Center (RC_vir)](/xray-mp-wiki/proteins/Blastochloris viridis Photosynthetic Reaction Center (RC_vir)/) | 1.86 | 2WJM | LSP-grown (lipidic sponge phase variant of LCP) crystals revealing diacylglycerol modification, monoolein at QB site, and 36 Å lipid feature. Type I crystal packing, no membrane-plane crystal contacts. |
| [Human GPR40 Receptor (FFAR1)](/xray-mp-wiki/proteins/Human GPR40 Receptor (FFAR1)/) | 2.3 | 4PHU | First GPCR structure of the free fatty-acid receptor 1. TAK-875 (fasiglifam) bound to a non-canonical allosteric pocket. T4L fusion in ICL3. 2.3 A structure solved by molecular replacement. |
| [Human OX2 Orexin Receptor (OX2R)](/xray-mp-wiki/proteins/Human OX2 Orexin Receptor (OX2R)/) | 2.5 | 4S0V | First structure of the human OX2 orexin receptor. Suvorexant (Belsomra) bound in orthosteric pocket. Novel PGS fusion chimera in ICL3. 2.5 A structure solved by molecular replacement. |
