---
title: Hanging-Drop Vapor Diffusion
created: 2026-05-27
updated: 2026-05-27
type: method
category: methods
layout: default
tags: [crystallization-hanging-drop, crystallization-vapor-diffusion, subdirectory-crystallization]
sources: [doi/10.1016##j.jmb.2007.11.080, doi/10.1016##j.jmb.2018.02.026, doi/10.1038##nature13306, doi/10.1038##nsmb.3029]
verified: false
---

# Hanging-Drop Vapor Diffusion

## Overview

Hanging-drop vapor diffusion is a widely used protein crystallization technique where a small drop containing protein and precipitant solution is suspended over a larger reservoir of precipitant solution. As water vapor diffuses from the drop to the reservoir, the drop gradually concentrates, eventually reaching supersaturation and nucleation. This method is one of the most common approaches for membrane and soluble protein crystallization.

## Protocol

### Reagents and Materials

- {'protein_sample': 'Protein solution at appropriate concentration (typically 2-20 mg/mL)', 'reservoir': 'Precipitant solution (varies widely depending on target; common precipitants include PEGs, salts, and organic solvents)'}
- {'cryoprotectant': 'Optional cryoprotectant added to reservoir (e.g., glycerol, ethylene glycol, or high concentration of precipitant component)'}

### Steps

1. {'step': 'Drop preparation', 'description': 'Mix equal volumes of protein solution and reservoir solution (typically 1 uL each) on a coverslip. The drop should form a convex meniscus.'}
2. {'step': 'Sealing', 'description': 'Invert the coverslip over a reservoir well containing 0.5 mL of reservoir solution. Seal the drop with grease or sealant to prevent evaporation.'}
3. {'step': 'Equilibration', 'description': 'Allow the drop to equilibrate against the reservoir over hours to weeks. Water vapor diffuses from the drop to the reservoir, concentrating the protein until crystallization occurs.'}
4. {'step': 'Harvesting', 'description': 'When crystals appear, harvest them by looping and transferring to cryoprotectant solution (reservoir with added cryoprotectant, e.g., 20% glycerol) before flash-cooling in liquid nitrogen.'}


## Advantages

- Uses very small sample volumes (0.5-4 uL total)
- Simple setup with minimal equipment
- Fine control over equilibration rate
- Widely used with extensive optimization protocols
- Compatible with automated liquid handling robots

## Disadvantages

- Slow equilibration can delay crystal appearance
- Drop may detach from coverslip if not properly sealed
- Evaporation rate depends on seal quality and temperature stability
- Limited to small-scale screening compared to sitting-drop robots

## Related Methods

- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Alternative crystallization method, especially for membrane proteins
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Related vapor diffusion method with drop sitting on platform instead of hanging

## Related Reagents

- [Polyethylene Glycol (PEG)](/xray-mp-wiki/reagents/additives/peg/) — Common precipitant used in crystallization reservoir solutions
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Common cryoprotectant used in cryosolvent for flash-cooling crystals
