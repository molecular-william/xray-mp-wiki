---
title: "MFS Motif A and Charge-Helix Dipole Interactions"
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, subdirectory-structural-mechanisms]
sources: [doi/10.1073##pnas.1308127110]
verified: regex
---

# MFS Motif A and Charge-Helix Dipole Interactions

## Overview
Motif A is a highly conserved sequence motif (GxxxD rxGR kp) found in most MFS
(Major Facilitator Superfamily) transporters. Located in the loop connecting TMs 2
and 3 (L2-3), it functions as a molecular switch regulating the conformational
changes between inward and outward states. The motif mediates interdomain interactions
through charge-helix dipole interactions and a charge-relay system, stabilizing the
outward conformation and coupling protonation state in the central cavity to domain
movements.


## Mechanism/Details
Motif A is located in the L2-3 loop connecting transmembrane helices 2 and 3. In YajR,
the sequence is G69LLSD73RIGR77KP. Key functional elements:

1. Gly(+1) — Forms close helix-helix contacts with conserved Gly residues on TM11,
   creating an interdomain helical bundle essential for the outward conformation.

2. Asp(+5) — Acts as an N-cap for TM11, stabilizing the helix through a charge-helix
   dipole interaction. This residue is completely buried in the outward conformation
   (zero solvent accessibility). Mutation (D73R) decreases Tm by ~20°C and increases
   occupancy of the inward conformation.

3. Arg(+6) — May interact with surrounding lipid molecules.

4. Arg(+9) — Forms part of a charge-relay system with Asp(+5) and a conserved Asp
   on TM4 (Asp126 in YajR). The charge-relay delocalizes electron movement, allowing
   signals from the central cavity to regulate the charge-helix dipole interaction.

5. Lys(+10) — Interacts with the C-terminal end of TM6.

The charge-helix dipole interaction provides ~4 kJ/mol stabilization energy. The
charge-relay system likely connects protonation events in the central cavity (e.g.,
His225-Glu320 pair in YajR) to the cytoplasmic interdomain interface, enabling
cooperative conformational switching. Point mutations at the +5, +9 positions, or the
conserved Asp on TM4 disrupt transport activity in multiple MFS proteins.

## Examples in Membrane Protein Work
- [YajR Transporter](/xray-mp-wiki/proteins/mfs-transporters/yajr-transporter/) — First crystal structure illustrating the functional role of motif A in the outward conformation of an MFS transporter.
- [LacY](/xray-mp-wiki/proteins/mfs-transporters/lac-y/) — Asp68 (equivalent to Asp73 in YajR) in LacY shows reduced periplasmic opening probability upon mutation, consistent with motif A stabilizing the outward conformation.

## Related Concepts
- [Rocker-Switch Mechanism]() — The rocker-switch conformational changes in MFS transporters are regulated by motif A.
- [Major Facilitator Superfamily (MFS)]() — Motif A is a conserved signature of MFS transporters.
- [Charge-Helix Dipole Interaction]() — The Asp(+5) residue of motif A stabilizes TM11 via a charge-helix dipole interaction.

## Cross-References
- [YajR Transporter (E. coli MFS Drug Efflux Transporter)](/xray-mp-wiki/proteins/mfs-transporters/yajr-transporter/) — Primary structural study elucidating the functional role of motif A in MFS transporters
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — Motif A is a defining signature of the MFS transporter family
- [Rocker-Switch Mechanism](/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/) — Motif A regulates the rocker-switch conformational changes in MFS transporters
