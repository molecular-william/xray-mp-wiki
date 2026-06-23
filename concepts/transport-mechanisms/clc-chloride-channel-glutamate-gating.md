---
title: CLC Chloride Channel Glutamate Gating
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-structural, concept-functional, subdirectory-concepts]
sources: [doi/10.1126##science.1082708]
verified: false
---

# CLC Chloride Channel Glutamate Gating

## Overview
CLC chloride channel gating is mediated by a conserved glutamate residue (E148 in EcCLC, E166 in ClC-0 from Torpedo ray) whose carboxyl side chain acts as a gate by physically occluding the Cl- ion conduction pathway. In the closed state, the glutamate carboxyl group occupies the extracellular Cl- binding site (Sext) at the selectivity filter, mimicking a Cl- ion and blocking ion flow. In the open state, the glutamate side chain is displaced and the Sext site is occupied by a Cl- ion, allowing continuous anion conduction through the pore. This mechanism, known as the "glutamate gate," explains the "fast gating" process in CLC channels: each pore in the homodimeric channel is gated independently by its own glutamate residue, and the gating is coupled to Cl- ion concentration because the glutamate carboxyl competes directly with Cl- for the Sext binding site. The open pore contains three Cl- binding sites (Sint, Scen, Sext) that form an uninterrupted queue of anions connecting the intracellular and extracellular solutions.

## Mechanism/Details
The structural basis of the glutamate gate was revealed by X-ray crystal
structures of wild-type and mutant E. coli CLC (EcCLC) channels bound to a
monoclonal Fab fragment:

1. Closed state (wild-type): The side chain of Glu148 projects into the
   pore, inserting its carboxyl group between the N-termini of helices αN
   and αF. Hydrogen bonding bridges these helices together. Two Cl- ions
   are bound at the Sint and Scen sites, but the Sext site is occupied by
   the glutamate carboxyl group, blocking the pore.

2. Open state (E148A mutant): With the glutamate side chain removed, a
   Br- ion (substituting for Cl-) occupies the Sext site. An uninterrupted
   anion queue connects the intracellular and extracellular solutions
   through Sint, Scen, and Sext, representing the open, conducting
   conformation.

3. Open-like state (E148Q mutant): The glutamine side chain is directed
   toward the extracellular solution rather than into the pore. Ions bind
   at all three sites as in E148A, suggesting this mimics the open
   conformation of the wild-type channel.

Electrophysiological studies on ClC-0 from Torpedo ray expressed in
Xenopus oocytes confirmed the functional role of the glutamate gate.
Mutation of the corresponding residue (E166) to Ala, Gln, or Val abolished
or severely diminished fast gating, causing both pores of the double-barreled
channel to remain open most of the time. The mutation of E166 also
eliminated the pH dependence of gating observed in wild-type ClC-0,
consistent with the model that protonation of the glutamate carboxyl group
(with a pKa perturbed toward physiological pH due to its proximity to Cl-)
is required for gate closure.

Key features of the glutamate gate mechanism:
- The two pores of the CLC homodimer are gated independently, consistent
  with each pore having its own glutamate residue and the gating
  conformational change being small and local (limited to side chain
  rotation).
- The glutamate gate is coupled to Cl- ion concentration: both internal
  and external Cl- ions affect gating because the glutamate carboxyl and
  Cl- compete for the same Sext binding site.
- The mechanism is pH-dependent: lowering pH favors protonation of the
  glutamate, which stabilizes the closed state.
- This "gate by side chain occlusion" is fundamentally different from
  activation gating in K+ channels, which involves global transmembrane
  helix motions.

The glutamate gate mechanism is distinct from the two-gate mechanism of
CLC transporters (which involve both E148 and Y445 as internal and external
gates), explaining how CLC channels evolved to mediate passive Cl- flow
while CLC transporters achieve coupled Cl-/H+ exchange.

## Examples in Membrane Protein Work
- [CLC-ec1](/xray-mp-wiki/proteins/slc-transporters/clc-ec1/) — E. coli CLC channel; paradigmatic system for studies of the glutamate gate. Glu148 = Egate (gating glutamate)
- [StClC](/xray-mp-wiki/proteins/slc-transporters/stclc/) — Salmonella enterica CLC channel; related structure used in the original fold determination
- ClC-0 from Torpedo ray — Eukaryotic CLC channel used for electrophysiological validation. Glu166 = Egate

## Related Concepts
- [CLC Two-Gate Transport Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/clc-two-gate-mechanism/) — In CLC transporters, both Glu148 (external gate) and Tyr445 (internal gate) are used, while CLC channels use only the glutamate gate for fast gating
- [Selectivity Filter](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) — The glutamate gate operates within the Cl- selectivity filter of CLC channels, occupying the extracellular anion binding site

## Cross-References

