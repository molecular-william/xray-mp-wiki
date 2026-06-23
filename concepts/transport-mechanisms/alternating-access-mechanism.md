---
title: Alternating Access Mechanism
created: 2026-06-08
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, membrane-protein]
sources: [doi/10.1038##nature03018, doi/10.1186##s12915-021-01102-4, doi/10.1085##jgp.201411219, doi/10.1073##pnas.2006526117, doi/10.1073##pnas.2006027117, doi/10.1038##s41594-020-0425-5, doi/10.1038##nature12233, doi/10.1073##pnas.0709388104, doi/10.1126##science.aah3497, doi/10.1016##j.molcel.2009.01.035, doi/10.1038##nature05155, doi/10.1038##nature14655]
verified: false
---

# Alternating Access Mechanism

## Overview
The alternating access mechanism is a fundamental transport mechanism
employed by secondary active transporters, including members of the Major
Facilitator Superfamily (MFS). In this mechanism, the transporter alternates
between two major conformational states: an inward-facing state where the
central substrate-binding cavity is open to the cytoplasmic side, and an
outward-facing state where the cavity is open to the extracellular or
periplasmic side. Substrate binding triggers a conformational switch that
occludes the binding site from one side and opens it to the opposite side,
allowing vectorial transport of substrates across the membrane.


## Mechanism/Details
The alternating access cycle typically proceeds through at least three
conformational states: outward-open, occluded, and inward-open. In the
outward-open state, the binding site is accessible from the extracellular
side. Substrate binding (often coupled with a co-transported ion such as H+
or Na+) induces closure of the extracellular gate and opening of an
intracellular gate, transitioning through an occluded intermediate where the
substrate is sequestered from both sides. The substrate is then released on
the opposite side.

For antiporters such as LtaA (PDB 6S7V), the cycle involves an additional
proton-coupling step: in the inward-facing conformation, deprotonated LtaA
binds the anchor-LLD substrate. Conformational change to the outward-facing
state releases the substrate into the membrane. Residue E32 becomes
protonated, facilitating the return to the inward-facing state where
deprotonation occurs. This mechanism explains the stimulation of transport
by a proton gradient, and in the absence of one, transport is driven by the
outwardly directed substrate gradient maintained by biosynthetic enzymes.

Key structural features enabling alternating access include the pseudo-
twofold symmetry of the N-terminal and C-terminal domains, which undergo a
rocker-switch type motion around a central pivot point. The conserved MFS
motif (G(X)8G(X)3GP(X)2GG) in the C-terminal domain contributes to the
conformational flexibility required for this switching.

## Examples in Membrane Protein Work
- [Maltose Transporter MalFGK2](/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/) — The E. coli maltose transporter (ABC importer) demonstrates alternating access via concerted rigid-body rotations. Comparison of inward-facing (PDB 3FH6, nucleotide-free) and outward-facing (PDB 2R6G, ATP-bound) structures shows 22-23 degree rotations of the TM cores and a 14 degree rotation of the NBDs, coupled through a ball-and-socket joint at the coupling helix interface. A hydrophobic gate of four kinked TM helix loops seals the periplasmic side in the inward-facing state.
- [MsbA](/xray-mp-wiki/proteins/abc-transporters/msba/) — MsbA ABC transporter demonstrates alternating access with a twist — four structures (nucleotide-bound, open-apo, closed-apo) reveal that nucleotide binding causes a packing rearrangement of transmembrane helices switching accessibility from inward-facing to outward-facing via a flexible hinge formed by extracellular loops 2 and 3.
- [LtaA](/xray-mp-wiki/proteins/mfs-transporters/ltaa/) — LtaA from S. aureus is a proton-coupled antiporter flippase that follows the alternating access cycle to translocate the lipid-linked disaccharide anchor-LLD across the membrane. Its outward-open structure (PDB 6S7V) and the modeled inward-facing conformation demonstrate the conformational changes involved.
- [Vcx1](/xray-mp-wiki/proteins/slc-transporters/vcx1/) — The S. cerevisiae vacuolar Ca2+/H+ exchanger Vcx1 (PDB 4KNA, 2.3 Å) provides the first cytosol-facing conformation of the CaCA superfamily, demonstrating an alternating access mechanism where M1/M6 helices act as a piston to alternately occlude and expose the active site pathway.
- [Sav1866 Multidrug ABC Transporter](/xray-mp-wiki/proteins/abc-transporters/sav1866/) — Sav1866 from S. aureus captured in the outward-facing ATP-bound conformation (PDB 2HYD, 3.0 Å), providing the first high-resolution structural evidence for the alternating access mechanism in ABC exporters. The NBD dimer closure upon ATP binding is coupled to opening of the TMDs toward the extracellular space.

## Related Concepts
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/) — MFS transporters, including LtaA, operate via the alternating access mechanism
- [Ca2+:Cation Antiporter (CaCA) Superfamily](/xray-mp-wiki/concepts/transport-mechanisms/caca-superfamily/) — CaCA superfamily transporters, including Vcx1, operate via an alternating access mechanism driven by M1/M6 helix translation

## Cross-References
- [LtaA — S. aureus Lipid-Linked Disaccharide Flippase](/xray-mp-wiki/proteins/mfs-transporters/ltaa/) — LtaA exemplifies the alternating access mechanism for lipid flipping
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/major-facilitator-superfamily/) — MFS transporters employ alternating access as their core transport mechanism
- [Vcx1 (S. cerevisiae Ca2+/H+ Exchanger)](/xray-mp-wiki/proteins/slc-transporters/vcx1/) — Vcx1 structure demonstrates the alternating access mechanism in the CaCA superfamily via M1/M6 piston-like motion
- [Ca2+:Cation Antiporter (CaCA) Superfamily](/xray-mp-wiki/concepts/transport-mechanisms/caca-superfamily/) — The CaCA superfamily uses alternating access for Ca2+ transport across membranes
