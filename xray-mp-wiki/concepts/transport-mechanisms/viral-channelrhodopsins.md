---
title: "Viral Channelrhodopsins (VirChR)"
created: 2026-06-11
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-protein-family, concept-functional, membrane-protein, subdirectory-transport-mechanisms]
sources: [doi/10.1038##s41467-020-19457-7]
verified: regex
---

# Viral Channelrhodopsins (VirChR)

## Overview
Viral channelrhodopsins (VirChR1s) represent a distinct family of light-gated ion channels encoded by nucleocytoplasmic large DNA viruses (NCLDV) that infect marine phytoplankton. They belong to the VR1 group within the broader viral rhodopsin superfamily, which also includes VR2 group proton pumps. Unlike chlorophyte channelrhodopsins (e.g., CrChR2), viral channelrhodopsins are selective for Na+ and K+ ions and are uniquely impermeable to Ca2+ cations. This Ca2+ impermeability makes them valuable optogenetic tools for controlling cellular processes without Ca2+-induced side effects. In nature, VirChR1s likely mediate phototaxis of algal hosts, enhancing anabolic processes to support virus reproduction.

## Mechanism/Details
Viral channelrhodopsins share the canonical 7-transmembrane helix architecture of microbial rhodopsins with a covalently bound all-trans retinal chromophore linked to a conserved lysine residue via a Schiff base. However, their ion-conducting pathway differs markedly from known channelrhodopsins. The OLPVR1 structure (PDB: 7AKX, 1.4 A) reveals three constriction sites: an intracellular constriction site (ICS) formed by E44, a central constriction site (CCS) with an S-E-N triad (S11, E51, N197), and an extracellular constriction site (ECS) with R73, E132, K192, N193, and N197. Unlike CrChR2, OLPVR1 lacks prominent extracellular cavities and instead has a unique intracellular pore connected to a hydrophilic cavity near the retinal binding pocket. The photocycle features K-like (540 nm), L-like (460 nm), and N-like (560 nm) intermediates but lacks a detectable M-state, with the L/N equilibrium likely representing the ion-conducting state. Ca2+ blocks both inward and outward ionic fluxes when concentrations exceed a few mM, providing a unique regulatory mechanism.


## Examples in Membrane Protein Work
- [OLPVR1](/xray-mp-wiki/proteins/rhodopsins/olpvr1/) — OLPVR1 from Organic Lake phycodnavirus solved at 1.4 A resolution; demonstrates unique intracellular pore architecture and Ca2+ impermeability
- [VirChR1](/xray-mp-wiki/proteins/rhodopsins/virchr1/) — VirChR1 functionally characterized in HEK293S and SH-SY5Y cells; drives neural firing in neurons upon illumination with 470 nm light

## Related Concepts
- [Channelrhodopsin Photocycle](/xray-mp-wiki/concepts/transport-mechanisms/channelrhodopsin-photocycle/) — VirChR1s exhibit a distinct photocycle lacking the M-state characteristic of CrChR2 and other channelrhodopsins
- [GPCR Active Conformation](/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/) — OLPVR1 architecture closely resembles G-protein coupled receptors with TM3 helix protruding to protein center
- [Rhodopsin Superfamily](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-superfamily/) — Viral channelrhodopsins are a distinct monophyletic branch within the type-1 microbial rhodopsin superfamily
- [Ion-Conducting Pathway](/xray-mp-wiki/concepts/transport-mechanisms/ion-conducting-pathway/) — VirChR1s feature unique three constriction site architecture with intracellular pore formation

## Cross-References
- [OLPVR1](/xray-mp-wiki/proteins/rhodopsins/olpvr1/) — Structural model of VR1 group viral channelrhodopsin solved at 1.4 A resolution
- [VirChR1](/xray-mp-wiki/proteins/rhodopsins/virchr1/) — Functionally characterized representative of VR1 group; drives neural firing in neurons
- [Channelrhodopsin C1C2](/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/) — Chlorophyte channelrhodopsin reference for comparison of ion selectivity and photocycle
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archetypal microbial rhodopsin; VR1 group includes proton-pumping members (VirRDTS)
- [All-trans retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore covalently bound to conserved lysine in all viral channelrhodopsins
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to crystallize OLPVR1 at 22 C
- [Whole-Cell Patch-Clamp Recording](/xray-mp-wiki/methods/quality-assessment/two-electrode-voltage-clamp/) — Electrophysiology method used to characterize VirChR1 ion channeling activity
- [Drosophila Dopamine Transporter](/xray-mp-wiki/proteins/slc-transporters/d-dat/) — dDAT used as surrogate for norepinephrine transporter in structural studies
