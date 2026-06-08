---
title: Batch Crystallization with Free Interface Diffusion
created: 2026-06-03
updated: 2026-06-03
type: method
category: methods
layout: default
tags: [crystallization-microbatch, subdirectory-crystallization]
sources: [doi/10.1038##nature13453]
verified: false
---

# Batch Crystallization with Free Interface Diffusion

## Overview

Batch crystallization with free interface diffusion is a membrane protein crystallization technique that combines batch precipitation with a free interface diffusion approach for higher yield. Nucleation is initiated at the interface between a high-density precipitant solution and a lower-density protein solution containing detergent-solubilized membrane protein micelles. The slow addition of the denser precipitant creates a two-phase system where crystals grow at the interface and then sediment into the precipitant layer, where crystal growth terminates due to the absence of protein.

## Protocol

### Reagents and Materials

- {'name': 'PIPES buffer (100 mM, pH 7.0)', 'role': 'Buffer'}
- {'name': 'Calcium chloride (5 mM)', 'role': 'Cofactor stabilizer'}
- {'name': 'Tocopherol (10 mM)', 'role': 'Antioxidant additive'}
- {'name': 'Beta-dodecylmaltsyl (0.03%)', 'role': 'Detergent for solubilization'}
- {'name': 'PEG 2000 (10–17%)', 'role': 'Precipitant'}

### Steps

1. {'step': 'Protein solubilization', 'description': 'Dissolve the PSII precipitate in solubilization buffer containing 100 mM PIPES pH 7.0, 5 mM CaCl2, 10 mM tocopherol, and 0.03% beta-dodecylmaltsyl (DDM). Adjust chlorophyll concentration to 0.5 mM.'}
2. {'step': 'Precipitant preparation', 'description': 'Prepare precipitant solution with 100 mM PIPES pH 7.0, 5 mM CaCl2, 10 mM tocopherol, and 10–17% PEG 2000. The optimal concentrations are determined experimentally for each protein batch.'}
3. {'step': 'Free interface diffusion', 'description': 'Add the PEG precipitant solution to the PSII protein solution at approximately 20 µl per second. The higher density of the precipitant causes it to settle at the bottom of the tube, creating a two-phase system with a small mixed zone between the top protein layer and bottom PEG layer.'}
4. {'step': 'Crystal growth and sedimentation', 'description': 'Allow crystals to form at the interface for approximately 48 hours. Once crystals reach sufficient size, they sediment into the precipitant solution at the bottom and form a pellet. The supernatant is then removed and replaced with stabilizing buffer to terminate further crystal growth.'}
5. {'step': 'Stabilization', 'description': 'Remove supernatant after 48 hours and replace with stabilizing buffer. Handle all crystals in dim green light to limit exposure to light that could damage photosensitive cofactors.'}

### Typical Conditions

- **temperature**: 10 °C
- **duration**: 48 hours
- **light_conditions**: Dim green light throughout
- **crystal_size**: Approximately 1 µm


## Advantages

- High yield compared to traditional batch crystallization
- Controlled nucleation at the interface reduces crystal defects
- Crystal growth terminates naturally when crystals sediment into the precipitant layer
- Easily scalable for large protein volumes
- Well-suited for serial femtosecond crystallography which requires large quantities of microcrystals
- Minimizes pre-illumination of light-sensitive samples when performed in darkness

## Disadvantages

- Broad size distribution of crystals due to high supersaturation conditions
- May coexist with amorphous precipitate
- Optimal PEG and protein concentrations must be determined empirically for each batch
- Requires careful density matching between protein and precipitant solutions
- Not suitable for very small volumes used in vapor diffusion methods
