---
title: M2 Proton Channel Conformational Equilibrium
created: 2026-05-29
updated: 2026-05-29
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-concepts]
sources: [doi/10.1021##jacs.9b02196, doi/10.1073##pnas.1007071107]
verified: false
---

# M2 Proton Channel Conformational Equilibrium

## Overview
The [Influenza A M2 Proton Channel](/xray-mp-wiki/proteins/other-ion-channels/influenza-a-m2-proton-channel/) exists in two principal conformational states: Inward_closed and Inward_open. These states interconvert during the proton transport cycle, with the equilibrium governed by the protonation state of the His37 tetrad gating residue and influenced by environmental factors such as pH and detergent composition. The Inward_closed state is stable at neutral pH where His37 is neutral or monoprotonated; the Inward_open state predominates at low pH where the His37 tetrad is multi-protonated.


## Mechanism/Details
The conformational equilibrium is directly coupled to the protonation state of the His37 tetrad. At neutral pH, the channel primarily adopts the Inward_closed state with helices kinked at Gly34 and a tightly packed C-terminus. As pH decreases, protonation of His37 residues causes electrostatic repulsion that triggers a transition to the Inward_open state, characterized by straightened helices and an opened C-terminal gate. The Inward_closed state reaches maximum stability at pH 6, after which further acidification destabilizes it, becoming undetectable below pH 4.3. The computed pKa values for the Inward_closed state are pK1: 6.4, pK2: 7.4, and pK3: 4.4, with a single pKa of 5.9 for the Inward_open state. This behavior reflects M2's ability to stabilize protons in the transmembrane pore, with special stabilization of the +2 charge state.


## Examples in Membrane Protein Work
- **Influenza A M2 WT (M2(19-49))**: In [LPPG](/xray-mp-wiki/reagents/detergents/lppg/) detergent, exclusively Inward_open
  conformation. In [MNG-3-C8](/xray-mp-wiki/reagents/detergents/mng-3-c8/) detergent, exclusively Inward_closed conformation.
  In [Tetradecylbetaine (C14-betaine)](/xray-mp-wiki/reagents/detergents/c14-betaine/) detergent, both states observable with pH-dependent population
  shifts; Inward_closed peaks at pH 6.
- **Influenza A M2 S31N mutant (M2(22-46))**: Crystallized in both Inward_open
  and Inward_closed states (PDB 6MJH) in the same crystal lattice. The S31N
  mutation alters the structural properties of both states, conferring adamantane
  resistance through steric blocking (Inward_open) and pore constriction
  (Inward_closed).


## Related Concepts
- Channel gating mechanisms in ion channels
- Protonation-coupled conformational changes
- Water networks in membrane protein function

## Cross-References
- [Influenza A M2 Proton Channel](/xray-mp-wiki/proteins/other-ion-channels/influenza-a-m2-proton-channel/) — Primary system for studying conformational equilibrium between Inward_open and Inward_closed states
- [Channel Gating](/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/) — M2 conformational switching is a form of ion channel gating
- [Water Networks in Ligand Binding](/xray-mp-wiki/concepts/signaling-receptors/water-network-in-ligand-binding/) — Water-mediated interactions in M2 channel are coupled to conformational changes
- [Tetradecylbetaine (C14-betaine)](/xray-mp-wiki/reagents/detergents/c14-betaine/) — Detergent used in purification or crystallization
- [LPPG](/xray-mp-wiki/reagents/detergents/lppg/) — Detergent used in purification or crystallization
- [MNG-3-C8](/xray-mp-wiki/reagents/detergents/mng-3-c8/) — Detergent used in purification or crystallization
