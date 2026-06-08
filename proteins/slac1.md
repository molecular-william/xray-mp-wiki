---
title: SLAC1 (SLOW ANION CHANNEL 1 from Arabidopsis thaliana)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09487]
verified: false
---

# SLAC1 (SLOW ANION CHANNEL 1 from Arabidopsis thaliana)

## Overview

SLAC1 (SLOW ANION CHANNEL 1) is a plant anion channel from Arabidopsis thaliana that controls turgor pressure in guard cells, thereby regulating stomatal aperture and the exchange of water vapour and photosynthetic gases. SLAC1 is activated by phosphorylation from the OST1 kinase in response to environmental signals such as drought, high CO2 levels, and abscisic acid (ABA). The crystal structure of its bacterial homologue HiTehA from Haemophilus influenzae was used to build a homology model of SLAC1, revealing a ten- transmembrane-helix architecture with a central pore gated by the conserved phenylalanine residue Phe 450. Electrophysiological studies of SLAC1 mutants confirmed the gating mechanism and anion selectivity properties.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature09487 | Not available (homology model) | Not applicable (homology model based on HiTehA) | Not applicable | SLAC1 transmembrane domain (residues 188-504) homology model on HiTehA scaffold | Not applicable (homology model) |

## Expression and Purification

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### OST1 kinase activation of SLAC1

SLAC1 is activated by phosphorylation from the OST1 kinase. OST1 activity is negatively regulated by the ABI1 phosphatase, which is inhibited by ABA receptors PYR and RCAR in a ternary hormone-receptor-phosphatase complex. Resulting Cl- efflux through SLAC1 causes membrane depolarization, activating outward-rectifying K+ channels, leading to KCl and water efflux that reduces turgor and causes stomatal closure.

### Phe 450 gate in SLAC1

The SLAC1 pore is gated by the conserved phenylalanine residue Phe 450 (Phe 262 in HiTehA). In wild-type SLAC1, Phe 450 occludes the central pore. Substitution of Phe 450 by smaller residues (F450A, F450G) results in constitutively opened channels with very large Cl- currents. The F450A mutation abolishes OST1-mediated activation, suggesting that the gate must remain restrained for OST1 to exert its effect. The F450T and F450V variants are still activated by OST1, indicating that the gate can be unlatched with these residues.

### Mutational analysis of SLAC1 gating and conductance

The slac1-2 mutation (G194D) points into the pore from TM1 and blocks ion conductance, consistent with the structural prediction that Asp 194 would repel anions. The slac1-1 mutation (S456F) points away from the pore and is structurally disruptive, as the phenyl bulk cannot fit at position 456. Double mutants F450A/G194D show abolished conductance, confirming that pore blockage by G194D overrides the gate opening from F450A.

### Anion selectivity of SLAC1

SLAC1 conducts anions but not cations and is selective among anions with the relative permeability sequence I- > NO3- > Br- > Cl-, corresponding to the selectivity sequence inversely correlated with the hydration energies of monovalent anions. Selectivity is largely a function of the energetic cost of ion dehydration. The pore has an electropositive electrostatic potential throughout, promoting anion conductance and discrimination against cations.


## Cross-References

- [HiTehA (TehA from Haemophilus influenzae)](/xray-mp-wiki/proteins/hiteha/) — Bacterial homologue; HiTehA structure used as template for SLAC1 homology model
- [Anion Channel Gating via Phenylalanine Gate](/xray-mp-wiki/concepts/anion-channel-gating/) — Phe 450 gate mechanism identified through SLAC1-HiTehA structural comparison
- [SLAC1 Superfamily](/xray-mp-wiki/concepts/slac1-superfamily/) — SLAC1 is the founding member of the SF1A plant subfamily
