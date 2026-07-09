---
title: Orthosteric–Allosteric Dual Inhibition of Transporters
created: 2026-06-11
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-concepts]
sources: [doi/10.1073##pnas.2017749118]
verified: false
---

# Orthosteric–Allosteric Dual Inhibition of Transporters

## Overview
Orthosteric–allosteric dual inhibition is a paradigm-shifting drug design strategy in which a single small molecule simultaneously targets both the orthosteric (substrate-binding) site and an adjacent allosteric site of a protein target. This approach was successfully applied to design selective inhibitors of PfHT1 (P. falciparum hexose transporter 1) over human glucose transporters for antimalarial therapy. The strategy involves tethering a pharmacophore that occupies the orthosteric site to a second pharmacophore that engages a protein-specific allosteric pocket, connected by a flexible linker that traverses the channel connecting the two sites. This dual-targeting approach enhances both potency and selectivity by exploiting structural features unique to the target protein.


## Mechanism/Details
The orthosteric–allosteric dual inhibition strategy was inspired by the discovery of a unique allosteric pocket adjacent to the glucose-binding site in PfHT1 that is more hydrophobic than the corresponding region in human GLUT1. The design approach involves three key components:
1. A sugar moiety (glucose core) that binds to the conserved orthosteric
   glucose-binding pocket of PfHT1
2. A heteroaromatic tail group (e.g., quinoline) that occupies the PfHT1-specific
   allosteric pocket
3. A flexible C9 polymethylene linker that connects the two moieties and traverses
   the narrow hydrophobic channel linking the orthosteric and allosteric sites

Structure–activity relationship (SAR) studies demonstrated that: - A C9 polymethylene linker is optimal; shorter or longer chains decrease activity - Bicyclic rings (naphthyl, quinolinyl, biphenyl) enhance allosteric pocket binding - Introduction of nitrogen into the tail group (quinoline vs. naphthyl) enhances
  potency through polar interactions with K51 and D447
- The hydrophobicity of the connecting channel is critical for selectivity:
  mutations to increase polarity (F85S, V44T) decrease inhibitor potency
- The dual inhibition strategy achieved selectivity ratios (CC50/EC50) of 36-107
  over mammalian cells

The strategy was validated by molecular docking simulations, alanine-scanning mutagenesis, and experimental counterflow assays with recombinant PfHT1 mutants. The TH-PF series compounds demonstrated equipotency against both drug-sensitive and multidrug-resistant P. falciparum strains, confirming that this approach can overcome existing drug resistance mechanisms.

## Examples in Membrane Protein Work
- [PfHT1](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) — TH-PF01, TH-PF02, and TH-PF03 simultaneously target the orthosteric glucose-binding site and the PfHT1-specific allosteric pocket via a C9 linker.

## Related Concepts
- [Selective Starvation of Malaria Parasites](/xray-mp-wiki/concepts/miscellaneous/selective-starvation/) — The dual inhibition approach enables the selective starvation strategy by achieving PfHT1 selectivity over hGLUT1
- [Allosteric Regulation](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — Exploits a naturally occurring allosteric pocket in PfHT1 for inhibitor design

## Cross-References
- [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) — PfHT1 is the target protein with both orthosteric and allosteric sites exploited by this strategy
- [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) — Selectivity over hGLUT1 was achieved by exploiting structural differences in the allosteric pocket
- [hGLUT3 (Human Glucose Transporter 3)](/xray-mp-wiki/proteins/mfs-transporters/hglut3/) — Crystal structure of hGLUT3-C3361 confirmed the PfHT1-specific nature of the allosteric pocket
- [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) — Reference compound used to identify the allosteric pocket and inspire the dual inhibitor design
- [TH-PF01](/xray-mp-wiki/reagents/ligands/th-pf01/) — Exemplar dual inhibitor with sugar moiety for orthosteric site and quinoline tail for allosteric site
- [TH-PF03](/xray-mp-wiki/reagents/ligands/th-pf03/) — Most potent dual inhibitor from the TH-PF series
- [Selective Starvation of Malaria Parasites](/xray-mp-wiki/concepts/miscellaneous/selective-starvation/) — The dual inhibition strategy enables the broader selective starvation antimalarial approach
