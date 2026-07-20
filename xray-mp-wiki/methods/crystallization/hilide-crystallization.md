---
title: "HiLiDe Crystallization"
created: 2026-06-02
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [crystallization-vapor-diffusion, subdirectory-crystallization]
sources: [doi/10.1038##NSMB.2721, doi/10.1038##NSMB.2894, doi/10.1038##ncomms4110, doi/10.7554##eLife.73124]
verified: none
---

# HiLiDe Crystallization

## Overview

HiLiDe (Hydrophobic Interaction-Driven) crystallization is a membrane protein crystallization technique that exploits the natural tendency of membrane proteins to aggregate into stacked bilayers through hydrophobic interactions between their transmembrane domains. Unlike lipidic cubic phase (LCP) crystallization which embeds the protein in a lipid matrix, HiLiDe relies on the protein's own hydrophobic surfaces to drive crystal packing.

## Principle

In HiLiDe crystallization, membrane proteins in detergent solution are mixed with crystallization conditions that promote hydrophobic interactions between the transmembrane domains. The proteins arrange themselves into stacked bilayer-like arrays, held together by hydrophobic contacts between their membrane-spanning helices. This arrangement reduces the entropic penalty of crystallization by pre-organizing the proteins into a membrane-like environment. The technique is particularly effective for integral membrane proteins with large hydrophobic surfaces.

## Protocol

### Reagents and Materials

- {'name': 'Membrane protein in detergent', 'concentration': '--', 'notes': 'Protein solubilized in appropriate detergent'}
- {'name': 'Crystallization buffer', 'concentration': '--', 'notes': 'Standard crystallization conditions (precipitant, pH, salts)'}
- {'name': 'Lipid (optional)', 'concentration': '--', 'notes': 'Exogenous lipid (e.g., [DOPC](/xray-mp-wiki/reagents/lipids/dopc/)) can be added to facilitate crystal formation'}

### Steps

1. {'step': 'Protein preparation', 'description': 'Purify membrane protein and solubilize in mild detergent'}
2. {'step': 'Lipid mixing', 'description': 'Mix protein-detergent complex with lipid (e.g., [DOPC](/xray-mp-wiki/reagents/lipids/dopc/)) and incubate overnight'}
3. {'step': 'Mixing', 'description': 'Mix protein-lipid-detergent solution with crystallization reservoir solution'}
4. {'step': 'Crystallization', 'description': 'Allow crystals to grow via hydrophobic interaction-driven stacking'}
5. {'step': 'Cryoprotection', 'description': 'Flash-freeze crystals for X-ray data collection'}

### Typical Conditions

- **temperature**: Room temperature or 4 C
- **growth_time**: Days to weeks
- **notes**: Crystals form as stacked bilayers with hydrophobic interactions between membrane-spanning regions


## Advantages

- Exploits natural hydrophobic interactions of membrane proteins, reducing the need for exogenous lipids
- Produces well-ordered crystals with stacked bilayer packing
- Can yield multiple crystal forms from the same protein
- Particularly effective for P-type ATPases and other large membrane proteins

## Disadvantages

- Limited to proteins with sufficient hydrophobic surface area for stacking
- May produce limited crystal diversity compared to LCP methods
- Requires optimization of detergent conditions

## Related Methods

- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Alternative method for membrane protein crystallization using lipid matrix
- [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) — Another membrane protein crystallization technique using lipid-detergent mixtures
