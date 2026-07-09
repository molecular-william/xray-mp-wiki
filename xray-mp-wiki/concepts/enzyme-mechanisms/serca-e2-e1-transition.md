---
title: SERCA E2 to E1 Transition Mechanism
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, subdirectory-concepts]
sources: [doi/10.1073##pnas.1815472115]
verified: false
---

# SERCA E2 to E1 Transition Mechanism

## Overview
The E2→E1 transition in SERCA (sarco(endo)plasmic reticulum Ca²⁺-ATPase) is the
conformational change that converts the low-affinity, protonated Ca²⁺-binding sites
in E2 to high-affinity sites in E1, enabling Ca²⁺ binding from the cytoplasm. This
transition is triggered by deprotonation of the gating residue Glu309, which acts
as the first chemical event in the reaction cycle. Crystal structures of Glu309Gln
and Glu309Ala mutants trapped the initial stages of this transition, revealing that
the E2 state does not require a compact headpiece or bowed M5 helix — instead, it
depends on the hydrogen bonds between Glu771 and Asn796 that lock the unwound part
of M6 in place, and these bonds are disrupted by Glu309 deprotonation.


## Mechanism/Details
The E2→E1 transition proceeds through a multi-step mechanism:

1. Spontaneous deprotonation of Glu309 opens the M4 hinge by electrostatic
   repulsion between the newly negative Glu309 and other acidic residues,
   which in turn opens the headpiece (A-domain rotates ~120° to an E1-like
   azimuthal position, M5 straightens somewhat).

2. Deprotonation of Glu309 pulls the Asn796 side chain toward Val304 (at the
   top of M4L), destroying one of the two hydrogen bonds between Glu771 (M5)
   and Asn796 (M6). This unlocks the latch that prevents the unwound part of
   M6 from taking a different conformational path.

3. Anticlockwise rotation of the unwound M6 part (residues Leu797-Gly801,
   which contains Ca²⁺-coordinating Thr799 and Asp800) brings Thr799 and Asp800
   into the Ca²⁺-binding cavity, pushing M4C primarily through Val314.

4. The cytoplasmic half of M4 (M4C) inclines toward M3 near the hinge, detaching
   from M5 and M6.

5. M5 straightens completely, bringing the entire M4 helix upward to the E1
   position, establishing high-affinity Ca²⁺-binding sites.

Quantum chemical calculations [CCSD(T)] showed that the hydrogen bond between a
protonated carboxyl (Glu309) and the Val304 carbonyl is optimized at 2.8 Å, while
an amide-carbonyl bond (Gln309) is optimal at 3.16 Å. This subtle 0.33 Å difference
in hydrogen bond length propagates through the structure to cause the large
conformational rearrangements observed. Charge movement studies confirmed that
Glu309 deprotonation (apparent pKa ~6.7) is prerequisite for proton release from
other acidic residues (Glu771, Asp800) which have higher apparent pKa (~7.8 in
the Glu309Gln mutant).

## Examples in Membrane Protein Work
- [SERCA1a](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) — Primary system studied. Glu309Gln and Glu309Ala mutants crystallized in E2 state with thapsigargin reveal the structural basis of the E2→E1 transition.

## Related Concepts
- [P-type ATPase Mechanism]() — The E2→E1 transition is a key step in the P-type ATPase reaction cycle.
- [Phosphoenzyme E2P State]() — The E2P state follows E2 in the reaction cycle.

## Cross-References
- [SERCA1a (Sarcoplasmic Reticulum Ca²⁺-ATPase 1a)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) — Primary protein; the E2→E1 transition was characterized using SERCA1a Glu309 mutants
- [P-type ATPase Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/p-type-atpase-mechanism/) — The E2→E1 transition is a fundamental step in the P-type ATPase catalytic cycle
- [Phosphoenzyme E2P State](/xray-mp-wiki/concepts/enzyme-mechanisms/phosphoenzyme-e2p-state/) — The E2P state follows the E2→E1→E1P transitions in the reaction cycle
