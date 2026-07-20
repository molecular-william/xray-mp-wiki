---
title: "2D Crystallization by Detergent Dialysis"
created: 2026-06-16
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [crystallization-dialysis, subdirectory-crystallization]
sources: [doi/10.1016##j.jmb.2011.01.029]
verified: regex
---

# 2D Crystallization by Detergent Dialysis

## Overview

2D crystallization by detergent dialysis reconstitutes detergent-solubilized membrane proteins back into lipid bilayers by gradual removal of detergent, forming crystalline membranes suitable for electron crystallography. This method was used to obtain 2D crystals of GlpG rhomboid protease in E. coli polar lipids, which diffracted to ~4 Å and validated the bicelle-derived 3D structure.

## Principle

Membrane proteins solubilized in detergent are mixed with exogenous lipids at an optimal lipid-to-protein ratio. Dialysis against detergent-free buffer gradually removes detergent, allowing the lipids and proteins to self-assemble into ordered 2D arrays within continuous lipid bilayers. The resulting 2D crystals can be studied by electron cryo-microscopy and image processing.

## Protocol

### Reagents and Materials

- Detergent-solubilized membrane protein (e.g., in n-Decyl-beta-D-maltopyranoside)
- E. coli polar lipids (or other native lipid extract)
- Dialysis buffer (detergent-free)

### Steps

1. {'step': '1. Mix protein at 1 mg/ml in 0.2% DM with E. coli polar lipids at 5 mg/ml in 1% DM', 'method': 'Lipid-to-protein ratio 0.45-0.55 (w/w); incubate 1 hour at room temperature'}
2. {'step': '2. Transfer mixture to dialysis unit (10 kDa cutoff)', 'method': 'Slide-A-lyzer or dialysis bag'}
3. {'step': '3. Dialyze against detergent-free buffer at 37°C for 7 days', 'method': 'Buffer: 25 mM Bis-Tris (pH 7), 0.05 M NaCl, 5% glycerol, 5% 2-4-methylpentanediol, 3 mM NaN3, 1 mM DTT'}
4. {'step': '4. Screen for crystallinity by negative-stain electron microscopy', 'method': '1% uranyl acetate staining, Tecnai 12 screening'}
5. {'step': '5. Record cryo-EM images for structure determination', 'method': 'Polara G2 at 300 kV, 59,000x magnification'}

### Typical Conditions

- **temperature**: 310 K (37°C)
- **protein_concentration**: 1 mg/mL
- **lipid_to_protein_ratio**: 0.45-0.55 (w/w)
- **dialysis_time**: 7 days


## Advantages

- Protein is in native lipid environment (E. coli polar lipids)
- Produces large 2D crystalline arrays for electron crystallography
- Can achieve near-atomic resolution projections
- Validates 3D crystal structures obtained in non-native environments

## Disadvantages

- Limited to projection maps at intermediate resolution (~4-8 Å) without extensive data collection
- Crystals tend to form multilayers (thin 3D crystals rather than true monolayers)
- Requires access to electron microscopy facilities
- Time-consuming optimization of lipid-to-protein ratio

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [GlpG (E. coli rhomboid protease)](/xray-mp-wiki/proteins/GlpG (E. coli rhomboid protease)/) | 4 | 2XTV | 2D crystals had nearly identical unit cell to bicelle 3D crystals. Projection map at 8 Å confirmed same packing arrangement. |
