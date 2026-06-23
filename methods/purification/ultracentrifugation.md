---
title: Ultracentrifugation
created: 2026-06-22
updated: 2026-06-22
type: method
category: methods
layout: default
tags: [subdirectory-purification, purification-fractionation]
sources: [doi/10.1016##j.jbc.2021.100479]
verified: false
---

# Ultracentrifugation

## Overview

Ultracentrifugation uses high centrifugal force (100,000-500,000 x g) to separate particles based on density and size. In membrane protein purification, it is used for: (1) membrane isolation after cell lysis, separating membranes from soluble proteins at 100,000-200,000 x g; (2) density gradient centrifugation to separate membrane sub-types; (3) removal of insoluble aggregates after solubilization. Ultracentrifugation is also a key quality-control step to assess sample homogeneity.

## Principle

Ultracentrifugation exploits differences in sedimentation velocity and buoyant density between particles. When subjected to high centrifugal force in a rotor, particles sediment at rates proportional to their size and density, according to the Svedberg equation. Membrane fragments and vesicles have distinct sedimentation properties from soluble proteins and cellular debris. In density gradient ultracentrifugation, a pre-formed gradient (e.g., sucrose, iodixanol) allows separation of membrane sub-types based on their equilibrium buoyant density. The high g-force required (100,000-500,000 x g) necessitates specialized rotors and vacuum-operated ultracentrifuges to minimize frictional heating.

## Protocol

### Reagents and Materials

- {'name': 'Homogenization buffer', 'description': '25 mM Tris-HCl pH 8.0, 150 mM NaCl, protease inhibitors'}
- {'name': 'Sucrose or iodixanol gradient solution', 'description': 'For density gradient ultracentrifugation (e.g., 10-60% sucrose or 5-50% iodixanol)'}

### Steps

1. {'step': 'Low-speed clarification', 'description': 'Centrifuge cell lysate at 5,000-10,000 x g for 10-15 min at 4 C to remove unbroken cells and debris'}
2. {'step': 'Membrane sedimentation', 'description': 'Centrifuge the supernatant at 100,000-200,000 x g for 45-60 min at 4 C to pellet membrane fractions'}
3. {'step': 'Wash step', 'description': 'Resuspend membrane pellet in fresh homogenization buffer and repeat ultracentrifugation to remove soluble contaminants'}
4. {'step': 'Resuspension', 'description': 'Resuspend washed membrane pellet in storage buffer for downstream solubilization or storage at -80 C'}

### Typical Conditions

- **temperature**: 4 C
- **centrifugation_speed**: 100,000-200,000 x g for membrane isolation
- **centrifugation_time**: 45-60 min for membrane pelleting

