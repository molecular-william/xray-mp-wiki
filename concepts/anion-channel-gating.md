---
title: Anion Channel Gating via Phenylalanine Gate
created: 2026-06-02
updated: 2026-06-02
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, membrane-protein]
sources: [doi/10.1038##nature09487]
verified: false
---

# Anion Channel Gating via Phenylalanine Gate

## Overview
Anion channel gating via a conserved phenylalanine gate is a mechanism of ion channel regulation in which a bulky phenylalanine side chain occludes the central ion conduction pore in the closed state. This gating mechanism was first characterized in the SLAC1 superfamily of anion channels, where Phe 450 in Arabidopsis SLAC1 (Phe 262 in the bacterial homologue HiTehA) blocks the central pore. The gate can be opened by substitution with smaller residues (alanine, glycine), revealing a pore with approximately 5 A diameter. The gating is regulated by phosphorylation in the plant SLAC1 channels, where OST1 kinase-mediated phosphorylation unlatches the phenylalanine from its high-energy conformation, allowing ion conductance.


## Mechanism/Details
In the wild-type structure of HiTehA, the side chain of Phe 262 adopts a high-energy conformation with chi1/chi2 dihedral angles at -160 degrees/-4 degrees. While chi1 is in a preferred trans conformation, the phenyl ring is restricted by steric contacts with Val 210 and Leu 18 to a chi2 value near 0 degrees rather than the preferred 90 degrees orientation. This restrained conformation effectively occludes the central pore.
Substitution of Phe 262 by alanine (F262A) or glycine (F262G) opens the pore to a uniform diameter of approximately 5 A across the full transmembrane distance of approximately 30 A. The F450A and F450G mutants of AtSLAC1 show correspondingly large Cl- currents relative to wild-type levels. The F262L variant adopts a preferred trans/gauche+ conformation (chi1/chi2 = 177 degrees/63 degrees), similar to Val 262 in F262V (chi1 = -176 degrees).
In plant SLAC1, gating is controlled by OST1 kinase phosphorylation. Phosphorylation of SLAC1 at conserved Ser/Thr residues in cytoplasmic loops is thought to induce conformational changes that unlatch Phe 450 from its restrained orientation. Proline-mediated kinks in helices TM7 and TM9 adjacent to the gate may facilitate this unlatching. The F450L variant of SLAC1 remains inactive despite OST1 activation, suggesting that the restrained latch is necessary for OST1 to exert its effect on channel gating.
Anion selectivity in these channels is largely determined by the energetic cost of ion dehydration, with the relative permeability sequence I- > NO3- > Br- > Cl- correlating inversely with hydration energies. The pore surface is electropositive throughout, promoting anion conductance and discrimination against cations.


## Examples in Membrane Protein Work
- **HiTehA (Haemophilus influenzae TehA)**: Wild-type structure shows Phe 262 gating
  the central pore. F262A mutant has a wide-open pore at 1.15 A resolution. F262V,
  F262L, and G15D mutants also crystallized, showing pore sizes consistent with residue
  side chain volumes.
- **AtSLAC1 (Arabidopsis thaliana SLAC1)**: Homology model based on HiTehA reveals
  Phe 450 as the gating residue. F450A, F450G, F450T, F450V, and F450L mutants show
  graded conductance responses consistent with pore opening. Electrophysiological
  measurements in Xenopus oocytes confirm the gating mechanism.
- **SLAC1 superfamily**: The phenylalanine gate is conserved across the SF1A plant
  subfamily and bacterial TehA homologues, suggesting a fundamental gating mechanism
  for anion channels in this superfamily.


## Related Concepts
- Alternating-access mechanism in transporters - Proline kinks in transmembrane helices - Ion selectivity by dehydration energy - OST1 kinase regulation of SLAC1


## Cross-References
- [HiTehA (TehA from Haemophilus influenzae)](/xray-mp-wiki/proteins/hiteha/) — Structural basis of Phe 262 gate characterized in HiTehA
- [SLAC1 (SLOW ANION CHANNEL 1 from Arabidopsis thaliana)](/xray-mp-wiki/proteins/slac1/) — Phe 450 gate mechanism confirmed by SLAC1 mutational analysis
- [SLAC1 Superfamily](/xray-mp-wiki/concepts/slac1-superfamily/) — Phenylalanine gate is conserved across the SLAC1 superfamily
