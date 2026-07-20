---
title: "Bicelle Crystallization for Membrane Proteins"
created: 2026-06-16
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [crystallization-lcp, subdirectory-crystallization]
sources: [doi/10.1016##j.jmb.2011.01.029]
verified: regex
---

# Bicelle Crystallization for Membrane Proteins

## Overview

Bicelle crystallization uses a lipid-detergent mixture (typically DMPC/CHAPSO) that forms small bilayered micelles (bicelles) to crystallize membrane proteins in a lipid-like environment. The method was used to determine the 1.7 Å structure of GlpG rhomboid protease (PDB 2XTV) revealing an ordered lipid annulus. Bicelles provide a membrane-mimetic environment that preserves native lipid-protein interactions.

## Principle

Bicelles are disc-shaped aggregates of lipid and detergent that contain a planar lipid bilayer region stabilized by detergent at the edges. When mixed with membrane proteins at the appropriate ratio, bicelles can form type I membrane protein crystals where proteins are arranged in stacked membranous layers with their transmembrane regions embedded in the bicelle bilayer, mimicking the native membrane environment.

## Protocol

### Reagents and Materials

- DMPC (dimyristoyl phosphatidylcholine)
- CHAPSO (3-[(3-cholamidopropyl)dimethylammonio]-2-hydroxy-1-propanesulfonate)
- Detergent-solubilized membrane protein

### Steps

1. {'step': '1. Prepare bicelle stock: mix DMPC and CHAPSO at 2.6:1 ratio (w/w) in water to 20% total concentration', 'method': 'Dissolve and vortex'}
2. {'step': '2. Mix protein with bicelles at protein:bicelle ratios of 10:1 to 2.5:1 (w/w)', 'method': 'Incubate on ice for 1 hour'}
3. {'step': '3. Set up crystallization by mixing protein-bicelle solution with reservoir solution at 1:1 ratio', 'method': 'Vapor diffusion (hanging drop)'}
4. {'step': '4. Incubate at 25°C until crystals appear (typically days to weeks)', 'method': 'Temperature-controlled incubation'}
5. {'step': '5. Cryo-protect and flash-freeze in liquid nitrogen', 'method': 'Add 25% glycerol to mother liquor'}

### Typical Conditions

- **temperature**: 298 K (25°C)
- **protein_concentration**: 8-10 mg/mL
- **bicelle_concentration**: 1-4% (final)
- **reservoir**: 1.5 M NaCl, 0.1 M Bis-Tris (pH 7) for GlpG


## Advantages

- Membrane protein remains in a lipid-like bilayer environment
- Preserves native lipid-protein interactions
- Can yield high resolution data (1.7 Å for GlpG)
- Type I crystals with alternating up-down orientation mimic native membrane stacking

## Disadvantages

- Requires optimization of protein-to-bicelle ratio
- Small crystal size typical
- Detergent still present in crystallization drop may complicate interpretation

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [GlpG (E. coli rhomboid protease)](/xray-mp-wiki/proteins/GlpG (E. coli rhomboid protease)/) | 1.7 | 2XTV | DMPC/CHAPSO bicelles at 2% final concentration. 14 ordered lipid molecules modelled forming an annulus around the protein. |
