---
title: MtrCDE Tripartite Multidrug Efflux Pump
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, concept-protein-family, membrane-protein]
sources: [doi/10.1371##journal.pone.0097475]
verified: false
---

# MtrCDE Tripartite Multidrug Efflux Pump

## Overview
The MtrCDE tripartite multidrug efflux pump from Neisseria gonorrhoeae is a member of the hydrophobic and amphiphilic efflux resistance-nodulation-cell division (HAE-RND) family. It spans both the inner and outer membranes of N. gonorrhoeae and confers resistance to a variety of antibiotics, antimicrobial peptides, and toxic compounds. The pump is assembled as an MtrD3-MtrC6-MtrE3 complex, where MtrD is the inner membrane proton-motive force (PMF)-dependent efflux pump, MtrC is the periplasmic membrane fusion protein (adaptor), and [MTRE](/xray-mp-wiki/proteins/abc-transporters/mtre/) is the outer membrane channel.


## Mechanism/Details
The MtrCDE tripartite efflux pump spans both the inner and outer membranes of Neisseria gonorrhoeae, forming a contiguous conduit for drug export:

1. MtrD (inner membrane): An RND-type proton/drug antiporter that uses the proton motive force to drive substrate transport from the cytoplasm or periplasm into the channel. MtrD likely contains the drug-binding sites and undergoes conformational changes during the transport cycle.

2. MtrC (periplasmic adaptor): A membrane fusion protein that bridges MtrD and [MTRE](/xray-mp-wiki/proteins/abc-transporters/mtre/). Six MtrC molecules form the periplasmic portion of the complex. The alpha-helical hairpin domain of MtrC engages the intra- and inter-protomer grooves on the periplasmic surface of the [MTRE](/xray-mp-wiki/proteins/abc-transporters/mtre/) trimer. MtrC relays conformational changes from MtrD to [MTRE](/xray-mp-wiki/proteins/abc-transporters/mtre/), controlling channel opening and closing.

3. [MTRE](/xray-mp-wiki/proteins/abc-transporters/mtre/) (outer membrane channel): A homotrimeric beta-barrel channel that forms a continuous tunnel from the outer membrane surface to the periplasmic end, with an internal diameter of ~22 A at its widest point. An aspartate ring (six aspartates: D402/D405 from each protomer) at the periplasmic entrance creates a selectivity gate with a ~12 A opening.

The stoichiometry of the tripartite complex is MtrD3-MtrC6-MtrE3, consistent with the CusBA adaptor-transporter co-crystal structure. The opening and closing of the [MTRE](/xray-mp-wiki/proteins/abc-transporters/mtre/) channel is likely controlled by conformational changes in MtrC, which are driven by proton translocation in MtrD.

Overexpression of RND multidrug efflux pumps leads to a resistant phenotype in pathogenic organisms. The MtrCDE pump in N. gonorrhoeae is a major contributor to antibiotic resistance in this important human pathogen, making it a target for rational drug design to block efflux function.

## Examples in Membrane Protein Work
- [MTRE](/xray-mp-wiki/proteins/abc-transporters/mtre/) — The outer membrane channel component; crystal structure determined at 3.29 A in an open conformational state (space group P6_3_22)
- MtrCDE (MtrD/MtrC/MtrE) — Confers resistance to antibiotics, antimicrobial peptides, and toxic hydrophobic compounds; contributes to the alarming rise in drug-resistant gonorrhea

## Related Concepts
- [RND efflux pumps](/xray-mp-wiki/concepts/rnd-efflux-pumps/) — MtrCDE belongs to the HAE-RND family of tripartite efflux systems
- [Tripartite drug efflux systems](/xray-mp-wiki/concepts/tripartite-drug-efflux-systems/) — MtrCDE is a paradigm tripartite efflux system spanning both bacterial membranes
- [Antibiotic resistance mechanisms](/xray-mp-wiki/concepts/antibiotic-resistance-mechanisms/) — Overexpression of MtrCDE contributes to multidrug resistance in N. gonorrhoeae

## Cross-References
- [MtrE Outer Membrane Channel from Neisseria gonorrhoeae](/xray-mp-wiki/proteins/abc-transporters/mtre/) — Structural component of the MtrCDE efflux pump; the crystal structure reveals the open state of the outer membrane channel
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for MtrE solubilization and purification
