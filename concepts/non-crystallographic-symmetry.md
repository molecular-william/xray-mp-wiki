---
title: Non-Crystallographic Symmetry (NCS)
created: 2026-06-11
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-crystallography-principle, xray-crystallography]
sources: [doi/10.1107##S0907444908017162, doi/10.1038##nature10867, doi/10.1038##nature12357]
verified: false
---

# Non-Crystallographic Symmetry (NCS)

## Overview
Non-crystallographic symmetry (NCS) refers to symmetry relationships between molecules within the asymmetric unit of a crystal that do not correspond to the crystallographic symmetry operations of the space group. In NCS, two or more copies of a molecule (or domains within a molecule) are related by rotation and translation that are not part of the space group symmetry. NCS is exploited during structure determination through averaging techniques that improve electron density maps by exploiting the redundancy of information from multiple copies of the same molecule.


## Mechanism/Details
When a crystal asymmetric unit contains multiple copies of a macromolecule that share the same sequence and fold, these copies are related by non-crystallographic symmetry operations. During structure refinement, NCS averaging enforces that the electron density for all NCS-related molecules should be similar. This constraint significantly improves the signal-to-noise ratio of electron density maps, particularly at lower resolution or in cases of incomplete or anisotropic data. NCS restraints are typically applied during refinement to prevent overfitting while maintaining the symmetry constraints.


## Examples in Membrane Protein Work
- M3 Muscarinic Acetylcholine Receptor: The asymmetric unit of the M3-wtT4L crystal
  structure contains four M3 receptor molecules each fused to one T4 lysozyme molecule.
  NCS averaging compensated for anisotropic diffraction (superior quality along a*
  and b* axes compared to c*), yielding highly interpretable electron density maps
  despite data completeness dropping to 85.9% in the highest resolution shell. The
  four molecules showed relatively minor NCS deviations, except for a pronounced
  shift in a lysozyme helix in two of the four molecules.
- M2 Muscarinic Acetylcholine Receptor: NCS was used during refinement of the M2-T4L
  structure, where multiple copies of the receptor in the asymmetric unit provided
  redundant information for improving electron density map quality.


## Related Concepts
- [Epitaxial Twinning](/xray-mp-wiki/concepts/epitaxial-twinning/) — related crystallographic phenomenon - [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — phasing method often used with NCS - [Antiparallel Dimerization in GPCR Crystallization](/xray-mp-wiki/concepts/antiparallel-dimerization/) — crystal packing arrangement


## Cross-References

