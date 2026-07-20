---
title: "Proton Wire (Chain of Hydrogen Bonds)"
created: 2026-06-08
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, concept-functional, subdirectory-transport-mechanisms]
sources: [doi/10.1016##j.jmb.2007.04.082, doi/10.1073##pnas.2006027117, doi/10.1073##pnas.2016328118, doi/10.1038##s41594-022-00762-2, doi/10.1038##s41594-023-01020-9, doi/10.1126##science.aaw8634]
verified: regex
---

# Proton Wire (Chain of Hydrogen Bonds)

## Overview
A proton wire (also known as a chain of hydrogen bonds, CHB, or proton conduit) is a linear array of hydrogen-bonded water molecules and amino acid side chains that provides a pathway for rapid proton translocation through proteins. First proposed in 1978 as a mechanism for anomalous proton transport beyond the Grotthuss mechanism, proton wires are now recognized as essential elements in the function of enzymes, proton transporters, microbial rhodopsins, G protein-coupled receptors, and nanomaterials. True-atomic-resolution structures of bacteriorhodopsin (BR) at 1.05-1.53 Å resolution and of the inward proton pump BcXeR at 1.6-1.7 Å resolution have experimentally demonstrated that CHBs serve as proton pathways, long-range signaling conduits, and modulators of proton affinity of key functional groups.


## Mechanism/Details
A proton wire operates through a Grotthuss-type hopping mechanism in which a proton is relayed along a chain of hydrogen-bonded water molecules and polar residues without requiring the physical diffusion of individual proton carriers. The proton enters one end of the wire, transiently protonates a water molecule or residue, and a different proton exits at the opposite end — effectively translocating a proton across the wire on sub-picosecond timescales. The directionality and efficiency of proton transfer depend on the tuning of pKa values along the chain, which is modulated by the electrostatic environment and hydrogen-bond geometry.

In [bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/), a global CHB passes through the highly conserved residues D96–T89–D85–Y57–D212–R82–E194–E204. During the photocycle, CHBs are switched on and off in the cytoplasmic and extracellular parts through dehydration/hydration events triggered by retinal isomerization. The switching of CHBs regulates the proton affinities of the Schiff base, D85, and D96, enabling vectorial proton translocation against the electrochemical gradient. A Newton's cradle-like mechanism transmits polarization changes from D85 to the proton release group (E194–E204) via a single linear CHB formed in the L state. The true-atomic-resolution structures of BR (1.05–1.53 Å, PDB 7Z09–7Z0E) also revealed that CHBs can serve as long-range signaling conduits: the single CHB connecting D85 to the PRG in the L state transmits the information of D85 protonation to trigger proton release from the PRG hundreds of residues away, analogous to a Newton's cradle. Additionally, the number of CHBs around a functional group directly modulates its proton affinity — two CHBs maintaining low pKa of D85 in the ground state, versus one CHB in the L state increasing D85's affinity, enabling the switch from a poor proton acceptor to an efficient one.

In [BcXeR](/xray-mp-wiki/proteins/rhodopsins/bcxer/), proton wires form the core of the inward proton translocation mechanism. A cytoplasmic proton wire connects the retinal Schiff base to the proton transfer group (PTG, D214–E34–T88) via three water molecules in the L state. A separate extracellular proton wire connects the RSB to a water-filled concavity for reprotonation. Two internal gates (a hydrophobic gate near L81/F210 and an extracellular gate near Y49) open sequentially to ensure unidirectional proton transport, distinguishing inward pumps from channelrhodopsins where all gates open simultaneously.

Key structural features of proton wires include:
- Low-barrier hydrogen bonds (LBHBs) with distances of 2.3-2.5 Å where the proton is delocalized (shared) between donor and acceptor, enabling rapid proton transfer without significant energy barriers.
- Water-mediated chains of 3-5 well-ordered water molecules that rearrange dynamically during the functional cycle.
- Switching between on and off states mediated by conformational changes (e.g., R82 reorientation, L81 side-chain flip) and hydration/dehydration of internal cavities.
- The ability to serve as both selectivity filters (excluding other ions) and translocation pathways.

## Examples in Membrane Protein Work
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — True-atomic-resolution structures of BR in ground, K, L, and M states (PDB 7Z09–7Z0E) reveal CHBs connecting D85 to R82 (ground/K states) and the RSB to D96 (L state). A single CHB in the L state connects D85 to the PRG, mediating long-range signaling and proton release.
- [BcXeR](/xray-mp-wiki/proteins/rhodopsins/bcxer/) — Structures of BcXeR in ground, L, and M states (PDB 7ZMY, 7ZN3, 7ZN0) show a water-mediated CHB connecting the RSB to the PTG in the L state, serving as the pathway for inward proton translocation. A separate CHB on the extracellular side reprotonates the RSB.
- [Schizorhodopsin (SzR4)](/xray-mp-wiki/proteins/rhodopsins/schizorhodopsin/) — SzR4 uses a water-mediated transport network from the retinal Schiff base to the cytosol for untrapped inward H+ release, involving E81 and L78 as key residues in the proton pathway.

## Related Concepts
- [Low-Barrier Hydrogen Bond](/xray-mp-wiki/concepts/structural-mechanisms/low-barrier-hydrogen-bond/) — Short hydrogen bonds (2.3-2.5 Å) that serve as key components of proton wires, enabling delocalized proton sharing
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — The photocycle drives CHB switching that enables vectorial proton translocation
- [Grotthuss Mechanism]() — The fundamental physical mechanism by which protons hop along hydrogen-bonded water chains in proton wires

## Cross-References
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — BR provided the first true-atomic-resolution experimental structures of CHBs in action
- [BcXeR (Xenorhodopsin from Bacillus coahuilensis)](/xray-mp-wiki/proteins/rhodopsins/bcxer/) — BcXeR structures demonstrated proton wires in inward proton translocation
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — The photocycle provides the functional context for proton wire switching
- [Retinal Isomerization](/xray-mp-wiki/concepts/rhodopsin-mechanisms/retinal-isomerization/) — Retinal isomerization triggers the conformational changes that switch CHBs on/off
- [Retinal Chromophore Conformation](/xray-mp-wiki/concepts/structural-mechanisms/retinal-chromophore-conformation/) — The retinal conformation determines the hydration state of internal cavities controlling CHB formation
- [Proton Release Complex](/xray-mp-wiki/concepts/rhodopsin-mechanisms/proton-release-complex/) — The PRG in BR is the terminus of the extracellular proton wire
- [Proton-Locked Conformation](/xray-mp-wiki/concepts/structural-mechanisms/proton-locked-conformation/) — The ionic lock formed in the BR M state prevents proton backflow after wire-mediated release
