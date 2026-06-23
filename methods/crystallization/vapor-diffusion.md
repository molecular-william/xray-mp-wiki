---
title: Vapor Diffusion Crystallization
created: 2026-06-22
updated: 2026-06-22
type: method
category: methods
layout: default
tags: [subdirectory-crystallization, crystallization-vapor-diffusion]
sources: [doi/10.1107##s2053230x14024558]
verified: false
---

# Vapor Diffusion Crystallization

## Overview

Vapor diffusion is the most widely used method for protein crystallization. A droplet containing protein, precipitant, and buffer is placed in a sealed chamber with a reservoir containing a higher concentration of precipitant. Water vapor diffuses from the droplet to the reservoir, slowly concentrating the protein and precipitant until supersaturation is reached, leading to crystal nucleation and growth. Two formats exist: hanging-drop (droplet on a coverslip) and sitting-drop (droplet on a pedestal). The method is compatible with both manual and robotic setups.

## Principle

Vapor diffusion relies on the equilibration of water vapor between a small protein-containing droplet and a larger reservoir of precipitant solution. The difference in precipitant concentration creates a vapor pressure gradient, causing water to evaporate from the droplet and condense into the reservoir. As the droplet volume decreases, both protein and precipitant concentrations increase, driving the solution into the supersaturation zone of the phase diagram where nucleation and crystal growth occur. The rate of equilibration depends on temperature, the concentration gradient, and the geometry of the setup.

## Protocol

### Reagents and Materials

- {'name': 'Protein solution', 'description': 'Purified membrane protein at 2-20 mg/mL in appropriate buffer with detergent'}
- {'name': 'Reservoir solution', 'description': 'Precipitant solution containing salts, PEGs, or other precipitants at higher concentration than in the drop'}
- {'name': 'Cryoprotectant solution', 'description': 'Reservoir solution supplemented with 15-30% glycerol, ethylene glycol, or other cryoprotectant'}

### Steps

1. {'step': 'Drop preparation', 'description': 'Mix equal volumes of protein solution and reservoir solution (typically 0.5-2 uL each) on a coverslip (hanging-drop) or in a pedestal well (sitting-drop)'}
2. {'step': 'Sealing', 'description': 'Invert the coverslip over a reservoir well containing 0.5-1 mL of reservoir solution and seal with grease or adhesive film; for sitting-drop, seal the well directly'}
3. {'step': 'Equilibration', 'description': 'Incubate at constant temperature (typically 4 C, 18 C, or 20 C) for hours to weeks until crystals appear'}
4. {'step': 'Harvesting', 'description': 'Loop crystals, transfer to cryoprotectant solution briefly, and flash-cool in liquid nitrogen for X-ray data collection'}

### Typical Conditions

- **temperature**: 4-20 C (typically)
- **drop_ratio**: 1:1 protein:reservoir (can vary 1:3 to 3:1)
- **equilibration_time**: Hours to weeks

