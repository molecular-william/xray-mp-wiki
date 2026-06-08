---
title: dsT4L (Disulfide-Stabilized T4 Lysozyme)
created: 2026-05-28
updated: 2026-05-28
type: protein
category: proteins
layout: default
tags: [xray-crystallography, membrane-protein]
sources: [doi/10.1016##j.str.2014.08.022, doi/10.1016##j.jmb.1989.02.050]
verified: false
---

# dsT4L (Disulfide-Stabilized T4 Lysozyme)

## Overview

dsT4L is a disulfide-stabilized variant of T4 lysozyme engineered for use as a fusion partner in GPCR crystallography. It contains two engineered disulfide bridges (Cys3-Cys97 and Cys21-Cys142) that restrict the flexible hinge region between the N- and C-terminal lobes of T4 lysozyme, stabilizing a more closed conformation. When fused to the M3 muscarinic receptor in the third intracellular loop, dsT4L eliminated epitaxial twinning observed with wild-type T4L and enabled crystallization in a higher symmetry space group (P41212). The M3-dsT4L structure was solved at 3.6 A resolution (PDB 4U14).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2014.08.022 | 4U14 | 3.6 A | P41212 | dsT4L fused to M3 muscarinic receptor ICL3 (residues 259-482). Two disulfide bridges: Cys3-Cys97 and Cys21-Cys142.
 | Tiotropium (bound to M3 receptor) |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: dsT4L fused to M3 muscarinic receptor. Four cysteines introduced at positions 3, 21, 97, and 142 to form two disulfide bridges. The third bridge described by Matsumura et al. (Cys9-Cys164) was omitted because residue 164 is truncated for compactness. Iodoacetamide treatment deferred until after Ni-NTA purification to allow disulfide bond formation.


No purification described.

## Crystallization

### doi/10.1016##j.str.2014.08.022

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase crystallization |
| Protein sample | M3-dsT4L bound to tiotropium |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Crystals in higher symmetry space group P41212 compared to P1 for M3-wtT4L (4DAJ). Not twinned. One molecule per asymmetric unit. Resolution 3.6 A. Solved by molecular replacement using wtT4L (PDB 4LZM) as search model.
 |


## Biological / Functional Insights

### Disulfide stabilization restricts T4L lobe flexibility

The Cys21-Cys142 disulfide bridge stabilizes a more closed conformation of dsT4L compared to wtT4L, while the Cys3-Cys97 distance remains nearly the same as in wtT4L. This selective stabilization reduces the flexibility between the N- and C-terminal lobes of T4 lysozyme, which otherwise can vary by as much as 11.8 A in GPCR fusion protein structures. The reduced flexibility leads to more ordered crystal packing.

### Elimination of epitaxial twinning in GPCR crystals

M3-wtT4L crystals exhibit epitaxial twinning due to two different T4L packing arrangements that alternate in successive layers. Replacing wtT4L with dsT4L results in only one T4L packing arrangement, eliminating twinning. The dsT4L variant has a more rigid structure that promotes a single crystal contact interface, yielding crystals in higher symmetry space group P41212.


## Cross-References

- [M3 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/m3-muscarinic-acetylcholine-receptor/) — dsT4L fusion partner; PDB 4U14
- [mT4L (Minimal T4 Lysozyme)](/xray-mp-wiki/proteins/mt4l-lysozyme/) — Alternative T4L variant used in same study
- [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/) — Co-crystallized ligand bound to M3-dsT4L
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — LCP lipid matrix
