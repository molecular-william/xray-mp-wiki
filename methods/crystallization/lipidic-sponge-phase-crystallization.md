---
title: Lipidic Sponge Phase Crystallization
created: 2026-06-16
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [crystallization-lcp, subdirectory-crystallization]
sources: [doi/10.1021##bi900545e]
verified: false
---

# Lipidic Sponge Phase Crystallization

## Overview

Lipidic sponge phase (LSP) crystallization is a variant of lipidic cubic phase (LCP) crystallization in which additives such as Jeffamine M-600 or PEG are added to the LCP to create a less viscous, fluid isotropic sponge phase. The sponge phase consists of a continuous lipid bilayer network permeated by solvent channels, providing a membrane-like environment for crystallization while being easier to handle than the viscous LCP. The LSP method was used to obtain the 1.86 Å resolution structure of the Blastochloris viridis photosynthetic reaction center (PDB 2WJM), revealing lipid molecules on the protein surface including a diacylglycerol modification and monoolein at the QB binding site.

## Principle

The lipidic sponge phase is a fluid isotropic phase derived from the lipidic cubic phase by addition of swelling agents (e.g., Jeffamine M-600, PEG, heptanetriol) that increase the water channel size and reduce viscosity while maintaining the bicontinuous lipid bilayer structure. Membrane proteins diffuse freely in the bilayer and can form type I crystal lattices with stacked planar arrangements. The larger solvent channels (~100 Å vs ~50 Å in LCP) are better suited for proteins with large hydrophilic domains.

## Protocol

### Reagents and Materials

- Monoolein (mono-oleoyl-glycerol)
- LSP initiating solution: 20% Jeffamine M-600, 1 M HEPES pH 8.0, 0.7 M (NH4)2SO4, 2.5% 1,2,3-heptanetriol
- Reservoir solution (e.g., 0.55 M sodium acetate, 0.75 M HEPES pH 6.3, 0.1 g/mL Na/K-PO4)

### Steps

1. {'step': '1. Prepare LCP by mixing monoolein with water (60:40 v/v)', 'method': 'Mechanical mixing until viscous, nonbirefringent LCP formed'}
2. {'step': '2. Convert LCP to LSP by adding LSP initiating solution (1:4 v/v)', 'method': 'Equilibrate until phase separation occurs; harvest upper LSP'}
3. {'step': '3. Set up hanging-drop vapor-diffusion experiment', 'method': 'Mix 1 μL LSP precipitant + 1 μL protein solution + optional additives'}
4. {'step': '4. Incubate at room temperature in darkness', 'method': 'Vapor diffusion; crystals appear after days to weeks'}
5. {'step': '5. Harvest crystals directly from LSP without lipase or cryoprotectants', 'method': 'Direct harvesting'}

### Typical Conditions

- **temperature**: 293 K (room temperature)
- **protein_concentration**: 20-25 mg/mL for RC_vir
- **reservoir**: 0.55 M sodium acetate, 0.75 M HEPES pH 6.3, 0.1 g/mL Na/K-PO4


## Advantages

- Less viscous than LCP, easier to handle and dispense
- Larger solvent channels accommodate proteins with large hydrophilic domains
- Can be used in standard vapor-diffusion crystallization setups
- Maintains membrane protein in lipid bilayer environment
- Crystals can be harvested directly without lipase treatment
- Compatible with sparse matrix screening kits (LSP kit)

## Disadvantages

- Requires optimization of LSP-initiating solution composition
- Phase separation step adds complexity to protocol
- Lipid composition may compete with native ligands (e.g., monoolein at QB site)

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Blastochloris viridis Photosynthetic Reaction Center (RC_vir)](/xray-mp-wiki/proteins/Blastochloris viridis Photosynthetic Reaction Center (RC_vir)/) | 1.86 | 2WJM | LSP-grown crystals revealed diacylglycerol modification on cytochrome c, monoolein at QB site displacing ubiquinone, and 36 Å lipid feature. Type I crystal packing, space group P2(1)2(1)2, one molecule per asymmetric unit. Crystal contacts within membrane plane absent. |
| [Rhodobacter sphaeroides Photosynthetic Reaction Center (RC_sph)](/xray-mp-wiki/proteins/Rhodobacter sphaeroides Photosynthetic Reaction Center (RC_sph)/) | 2.35 | 1OGV | LCP/LSP-grown structure showing cardiolipin-mediated crystal contacts. |
