---
title: "Voltage-Sensor Trapping"
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-construct-design]
sources: [doi/10.1126##science.aac5464]
verified: regex
---

# Voltage-Sensor Trapping

## Overview
Voltage-sensor trapping is a mechanism of ion channel inhibition in which a small-molecule or toxin binds to a voltage-sensor domain (VSD) and stabilizes it in a specific conformation, preventing normal gating transitions. In the context of Nav1.7, aryl sulfonamide antagonists like GX-936 bind to the activated state of VSD4, preventing its deactivation and thereby stabilizing inactivated states of the channel.


## Mechanism/Details
Voltage-gated ion channels contain voltage-sensor domains (VSDs) that undergo conformational changes in response to membrane potential. Each VSD contains a highly conserved S4 helix with positively charged residues (gating charges, R1-R4/K1-K4) that move across the membrane electric field during channel activation and deactivation.

In voltage-sensor trapping, an inhibitor (small molecule or gating modifier toxin) binds to a specific conformational state of the VSD and prevents its transition to other states. The trapping mechanism involves:

1. State-dependent binding: The inhibitor only binds with high affinity when the VSD is in a specific conformation (typically the activated/depolarized state).

2. Direct engagement of gating charges: The anionic warhead of aryl sulfonamide inhibitors directly engages the guanidinium group of the R4 gating charge through a bidentate salt bridge. This interaction locks the S4 helix in its activated position.

3. Stabilization of inactivated states: By preventing VSD4 deactivation, the inhibitor effectively traps the channel in a nonconductive inactivated state, as VSD4 activation is necessary and sufficient to produce fast inactivation in Nav channels.

4. Voltage-dependent relief: Strong hyperpolarizing voltages can disrupt the inhibitor-receptor interaction, allowing current recovery and demonstrating the voltage dependence of the trapping mechanism.

The voltage-sensor trapping mechanism contrasts with pore-blocking inhibition (where drugs physically occlude the ion-conducting pore) and with gating modifier toxins that impair VSD activation. Instead, trapping stabilizes a naturally occurring gating state, effectively preventing recovery from inactivation.

For Nav1.7, the state dependence of GX-674 inhibition shows >2,000-fold difference in potency between depolarized (-40 mV, IC50 0.1 nM) and hyperpolarized (-120 mV, IC50 240 nM) holding potentials, consistent with trapping the activated VSD4 conformation.

## Examples in Membrane Protein Work
- [Human Nav1.7](/xray-mp-wiki/proteins/voltage-gated-channels/nav1-7/) — Aryl sulfonamide antagonists (GX-936, GX-674) trap VSD4 in activated state to produce isoform-selective inhibition

## Related Concepts
- []() — Voltage-sensor trapping is a specific subtype of gating modification where the modifier stabilizes rather than prevents a gating transition

## Cross-References
- [Human Nav1.7 Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/nav1-7/) — Voltage-sensor trapping mechanism demonstrated in Nav1.7 VSD4 with aryl sulfonamide antagonists
- [GX-936](/xray-mp-wiki/reagents/ligands/gx-936/) — Aryl sulfonamide antagonist that traps Nav1.7 VSD4 via voltage-sensor trapping mechanism
