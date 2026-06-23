---
title: TM6 Kinking and Export Directionality in ABC Transporters
created: 2026-06-11
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, subdirectory-concepts]
sources: [doi/10.1073##pnas.2006526117]
verified: false
---

# TM6 Kinking and Export Directionality in ABC Transporters

## Overview
In the [NaAtm1 ABC Exporter from Novosphingobium aromaticivorans](/xray-mp-wiki/proteins/abc-transporters/naatm1/) ABC exporter, kinking of transmembrane helix 6 (TM6) serves as a conformational switch that regulates substrate binding and enforces export directionality. TM6 adopts distinct conformations across the transport cycle: kinked in inward-facing states (enabling GSSG/glutathione binding), straight in occluded prehydrolysis states (restructuring the binding site for substrate release), and kinked again in the post-ATP hydrolysis state (eliminating the substrate-binding cavity entirely). The posthydrolysis cavity is too small (< 740 A3) to accommodate GSSG, preventing re-binding of substrate during the return stroke — providing an elegant mechanism for maintaining unidirectional export.


## Mechanism/Details
The mechanism operates through the following cycle: 1) In the inward-facing state, TM6 is kinked adjacent to a 310 helix at residues 314-317. The amide NH of residues 319-320 hydrogen bonds to the alpha-carboxyl of gamma-Glu of GSSG, while the alpha-amino group of GSSG hydrogen bonds to carbonyl CO of residue 316, creating a specific substrate-binding site. 2) As the transporter transitions to the occluded (prehydrolysis) state with ATP bound, TM6 straightens to a regular alpha-helical conformation. This increases separation between the two TM6s and restructures the binding pocket, making it no longer suitable for GSSG binding — promoting substrate release toward the outward-facing side. 3) Following ATP hydrolysis and phosphate release, the transporter resets to an inward-facing conformation. However, in the MgADPVO4-stabilized posthydrolysis state, TM6 adopts a kinked conformation that collapses the substrate-binding cavity, making it too small to accommodate GSSG. 4) This cavity collapse means the transporter returns to the inward-facing state without a functional binding site, preventing substrate re-binding and ensuring that only forward (export) transport occurs.


## Examples in Membrane Protein Work
- [NaAtm1 ABC Exporter from Novosphingobium aromaticivorans](/xray-mp-wiki/proteins/abc-transporters/naatm1/) from Novosphingobium aromaticivorans — Eight structures across the transport cycle reveal TM6 kinking dynamics. The posthydrolysis MgADPVO4 state lacks a viable cavity (< 740 A3 vs ~740 A3 for GSSG). NaS526C retains ~60% transport activity.
- [Sav1866 Multidrug ABC Transporter](/xray-mp-wiki/proteins/abc-transporters/sav1866/) from Staphylococcus aureus — Outward-facing structure has ~3400 A3 cavity, providing comparison for the range of cavity volumes across ABC transporter states.

## Related Concepts


## Cross-References
- [NaAtm1 ABC Transporter](/xray-mp-wiki/proteins/abc-transporters/naatm1/) — NaAtm1 is the primary model system for this mechanism
- [ABC Transporter Family](/xray-mp-wiki/concepts/abc-transporter-family/) — ABC exporters generally must maintain unidirectional transport
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — TM6 kinking enforces directionality within the alternating access framework
- [Sav1866 Multidrug ABC Transporter](/xray-mp-wiki/proteins/abc-transporters/sav1866/) — Related protein structure
