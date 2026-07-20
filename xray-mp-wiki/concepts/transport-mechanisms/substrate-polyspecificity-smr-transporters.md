---
title: "Substrate Polyspecificity in SMR Transporters"
created: 2026-06-11
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, membrane-protein, subdirectory-transport-mechanisms]
sources: [doi/10.1073##pnas.2403273121, doi/10.1038##s41467-020-19820-8]
verified: regex
---

# Substrate Polyspecificity in SMR Transporters

## Overview
Substrate polyspecificity — the ability to transport multiple structurally
unrelated compounds — is a hallmark of multidrug resistance transporters. In the
small multidrug resistance (SMR) family, the SMR_Gdx subtype (e.g., [Gdx-Clo SMR Transporter (Clostridales oral taxon 876)](/xray-mp-wiki/proteins/abc-transporters/gdx-clo/))
selectively transports guanidinium ion, while the SMR_Qac subtype (e.g., [EMRE](/xray-mp-wiki/proteins/abc-transporters/emre/))
promiscuously exports diverse quaternary ammonium antiseptics and hydrophobic
cations. Despite sharing ~40% sequence identity and nearly identical backbone
structures (1.2 A Calpha rmsd), these subtypes exhibit dramatically different
substrate preferences. Comparative studies have revealed that substrate
polyspecificity is determined not by residues that directly contact the substrate
in the binding pocket, but by peripheral residues that modulate the hydrogen bond
network, sidechain flexibility, and the energetic landscape of the transporter.


## Mechanism/Details
The molecular basis of polyspecificity in SMR transporters involves three
tiers of structural features:

1) Binding pocket plasticity: The conserved central glutamates (E13 in
[Gdx-Clo SMR Transporter (Clostridales oral taxon 876)](/xray-mp-wiki/proteins/abc-transporters/gdx-clo/)) and binding site aromatic residues (Y59, W62) adopt different
rotamers to accommodate substrates of varying size and shape. In [EMRE](/xray-mp-wiki/proteins/abc-transporters/emre/),
the binding pocket has a weak, disorganized hydrogen bond network that
permits greater rotameric freedom, while [Gdx-Clo SMR Transporter (Clostridales oral taxon 876)](/xray-mp-wiki/proteins/abc-transporters/gdx-clo/) has a polarized hydrogen
bond network that constrains the central glutamate.

2) Peripheral mutations remodel the binding landscape: Mutations at
positions distal to the substrate binding pocket (G10I at the TM1-TM2
interface, W16G/A17T/M39Y near the binding site, and A60T/A67I/K101N at
the membrane portal) collectively convert a selective guanidinium exporter
into a promiscuous quaternary ammonium exporter. These peripheral mutations
alter the hydrogen bond network architecture and sidechain flexibility of
the binding site without directly contacting the substrate.

3) Membrane portal access: A cleft between antiparallel TM2 helices
provides a lateral portal for hydrophobic substrate substituents to access
the binding site from the lipid bilayer. The position and hydrophobicity
of the portal determines which substrates can productively engage the
transport cycle.


## Examples in Membrane Protein Work
- [Gdx-Clo SMR Transporter (Clostridales oral taxon 876)](/xray-mp-wiki/proteins/abc-transporters/gdx-clo/) — Wild-type [Gdx-Clo SMR Transporter (Clostridales oral taxon 876)](/xray-mp-wiki/proteins/abc-transporters/gdx-clo/) selectively exports Gdm+ (Kd ~80 uM). Introduction of four peripheral mutations (G10I, W16G, A17T, M39Y) enables promiscuous transport of quaternary ammonium compounds (TPA+, CTA+) while abolishing Gdm+ transport. The A60T mutation alone shifts CTA+ binding position deeper in the pocket.

- [EMRE](/xray-mp-wiki/proteins/abc-transporters/emre/) — [EMRE](/xray-mp-wiki/proteins/abc-transporters/emre/) is a naturally polyspecific SMR_Qac exporter. Its weak hydrogen bond network in the binding pocket allows sidechain rearrangements of E14 and W63 to accommodate diverse substrates. [EMRE](/xray-mp-wiki/proteins/abc-transporters/emre/) transported TPA+ with Km of 800 uM, compared to 6.2 mM for the engineered Gdx-Clo-7x.


## Related Concepts


## Cross-References
- [Gdx-Clo SMR Transporter](/xray-mp-wiki/proteins/abc-transporters/gdx-clo/) — Primary system for studying how peripheral mutations alter substrate specificity
- [EmrE (E. coli SMR transporter)](/xray-mp-wiki/proteins/abc-transporters/emre/) — Prototypical polyspecific SMR_Qac exporter
- [SMR Family (Small Multidrug Resistance Family)](/xray-mp-wiki/concepts/protein-families/sm-family/) — SMR family provides the evolutionary context for understanding substrate specificity divergence
