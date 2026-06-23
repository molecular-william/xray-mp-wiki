---
title: Normal-Mode-Based X-Ray Crystallographic Refinement
created: 2026-06-08
updated: 2026-06-08
type: method
category: methods
layout: default
tags: [structure-refinement, subdirectory-structure-determination]
sources: [doi/10.1073##pnas.1000142107]
verified: false
---

# Normal-Mode-Based X-Ray Crystallographic Refinement

## Overview

Normal-mode-based X-ray crystallographic refinement is a computational method that models anisotropic thermal parameters (B factors) using a limited number of normal modes, reducing the number of independent thermal parameters compared to conventional isotropic refinement. The method is particularly effective for improving electron density maps of flexible regions in macromolecular structures, enabling the building of previously unresolved loops, side chains, and entire domains.

## Protocol

### Steps

1. {'step': 'Normal mode calculation', 'description': 'Normal modes of the starting structural model are calculated using an elastic network model. Typically 75 modes with appropriate stiffness parameters (e.g., stiffness of 30) are selected to model anisotropic thermal motion while reducing the number of independent thermal parameters.'}
2. {'step': 'Anisotropic B-factor generation', 'description': 'Normal-mode-based anisotropic B factors replace the isotropic B factors in the starting model. The number of independent thermal parameters is substantially reduced (e.g., 2,871 vs 4,997 parameters, ~50% reduction).'}
3. {'step': 'REFMAC5 positional refinement', 'description': 'The structure with normal-mode-based anisotropic B factors is minimized using standard crystallographic refinement software (e.g., REFMAC5) to optimize atomic positions.'}
4. {'step': 'Manual model building', 'description': 'Guided by improved composite OMIT 2Fo-Fc electron density maps, the model is manually adjusted to build missing main chains and side chains, determine unknown residue registers, and retrace incorrect backbone paths.'}
5. {'step': 'Iterative refinement cycles', 'description': 'Steps 1-4 are repeated iteratively (typically 6 rounds) until convergence. In each round, the improved maps reveal additional structural features.'}
6. {'step': 'Multicrystal averaging (optional)', 'description': 'For difficult regions with weak density, multicrystal averaging between the normal-mode-refined model and a related higher-resolution structure can further improve phases and finalize coordinates.'}


## Advantages

- Can recover large missing structural features, including entire loops and domains that are invisible in conventional refinement
- Reduces thermal parameter count, improving the data-to-parameter ratio
- Particularly effective for flexible membrane proteins and large complexes
- Works with existing diffraction data — no new data collection required

## Disadvantages

- Requires expertise in normal mode analysis and manual model building
- Modest R-factor improvement despite significant model changes (low contribution of flexible atoms to diffraction)
- Additional validation may be needed for newly built flexible regions
