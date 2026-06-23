---
title: Bacteriorhodopsin Photocycle
created: 2026-06-10
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-functional, membrane-protein]
sources: [doi/10.1107##S0907444913017575, doi/10.1126##science.286.5438.255, doi/10.1016##S0022-2836(02)00681-2, doi/10.1038##s41594-022-00762-2, doi/10.1006##jmbi.1999.3027]
verified: false
---

# Bacteriorhodopsin Photocycle

## Overview
The bacteriorhodopsin photocycle is a sequence of light-induced conformational
and protonation state changes that drive unidirectional proton translocation
across the membrane. Light absorption triggers all-trans to 13-cis
isomerization of the retinal chromophore, initiating a cascade through
spectroscopically distinct intermediates (J, K, L, M, N, O). True-atomic-resolution
structures at 1.05–1.53 Å (PDB 7Z09–7Z0E) resolved chains of hydrogen bonds
(CHBs) and low-barrier hydrogen bonds (LBHBs) across ground, K, L, and M
states, revealing that CHBs serve as proton pathways, long-range signaling
conduits, and modulators of proton affinity. The triple conformation of the
proton release group (E194/E204) and a Newton's cradle-like mechanism for
proton release were discovered, settling long-standing debates on the
proton-pumping mechanism.


## Mechanism/Details
Upon photon absorption, the retinal chromophore isomerizes from all-trans to
13-cis,15-anti configuration. This isomerization displaces the polyene chain:
C-14 moves 1.7 A and the 13-methyl group moves 1.3 A toward the cytoplasmic
side. The side chains of Trp182, Leu93, and Trp86 are displaced to
accommodate the steric conflict. The Schiff base nitrogen moves 0.9 A toward
the cytoplasmic side, and its electron pair turns away from Asp85.

**CHB switching mechanism.** The true-atomic-resolution structures reveal that
chains of hydrogen bonds (CHBs) are dynamically switched on and off during
the photocycle, controlling proton affinities and enabling unidirectional
transport:

- **Ground and K states:** Two CHBs connect D85 to R82, maintaining low
  proton affinity of D85. The cytoplasmic part lacks any CHB and is inactive.
  The PRG (E194/E204) exists in three conformations: one with a short 2.4 Å
  LBHB (delocalized proton, ~50% occupancy) and two with longer 2.9 Å
  distances (localized proton, ~25% each).

- **K-to-L transition:** N-H+ of the RSB reorients to the cytoplasmic side,
  causing dehydration of the extracellular region. D85 and R82 reorient
  toward the PRG. The number of CHBs connecting D85 to R82 reduces to one,
  increasing D85's proton affinity. Simultaneously, the cytoplasmic region
  hydrates: five water molecules appear, with three mediating a linear CHB
  between the RSB and D96. The PRG resolves to a single conformation with
  an extremely short 2.3 Å LBHB between E194 and E204, plus short H-bonds
  connecting R82–E194 (2.4 Å) and E204–w408' (2.5 Å), suggesting the excess
  proton is delocalized within a short proton wire ready for release.

- **L-to-M transition (proton release):** The RSB-D96 CHB disappears,
  decreasing RSB proton affinity. Together with increased pKa of D85, this
  leads to RSB deprotonation to D85 via a short RSB-T89-D85 proton wire.
  The protonation of D85 triggers polarization changes along the single CHB
  connecting D85 to the PRG — a Newton's cradle-like mechanism. R82's
  positive charge redistributes from the NE atom toward NH1 and NH2,
  coinciding with proton release from the PRG. The PRG loses all LBHBs,
  and R82 forms an ionic lock with E204 preventing proton backflow. Two
  very short H-bonds (2.4 Å) appear near S193 and P77 at the surface,
  suggesting transient proton storage.

- **M-to-N-to-O (reprotonation):** A CHB similar to the L state is formed
  in the cytoplasmic region between the RSB and D96, serving as a pathway
  for RSB reprotonation from D96.

Directionality is ensured by a "protonation switch" mechanism where the
shuttling of Arg82 between inward and outward orientations couples the
protonation states of Asp85 and the proton release site. After proton
release to the extracellular surface, the high pKa of Asp85 keeps it
protonated, ensuring reprotonation of the Schiff base occurs from the
cytoplasmic side only. The CHB switches regulate proton affinities of key
functional groups (RSB, D85, D96) to enforce strictly unidirectional
proton transport against the electrochemical gradient.

## Examples in Membrane Protein Work
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archetypal light-driven proton pump; true-atomic-resolution structures (PDB 7Z09–7Z0E) provide the complete picture of CHB switching, LBHB formation, and the Newton's cradle proton release mechanism

## Related Concepts
- [Microbial Rhodopsins](/xray-mp-wiki/concepts/microbial-rhodopsins/) — Bacteriorhodopsin is the prototypical microbial rhodopsin; its photocycle is the reference for understanding other microbial rhodopsins
- [Channelrhodopsin Photocycle](/xray-mp-wiki/concepts/channelrhodopsin-photocycle/) — Both photocycles involve retinal isomerization but differ in function (ion pumping vs. passive channel gating)
- [Proton Wire](/xray-mp-wiki/concepts/proton-wire/) — CHBs (proton wires) are the key structural elements that mediate proton translocation, signaling, and affinity modulation during the photocycle
- [Low-Barrier Hydrogen Bond](/xray-mp-wiki/concepts/low-barrier-hydrogen-bond/) — LBHBs in the PRG enable proton delocalization and storage across multiple photocycle states
- [Proton Release Complex](/xray-mp-wiki/concepts/proton-release-complex/) — The PRG (E194/E204) undergoes conformational changes during the photocycle, adopting triple conformation in ground/K states and single conformation in L/M states

## Cross-References
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — The D96N mutant M state crystal structure and the true-atomic-resolution structures (PDB 7Z09–7Z0E) provide the structural evidence for the photocycle mechanism
- [Microbial Rhodopsins](/xray-mp-wiki/concepts/microbial-rhodopsins/) — Context for how the bacteriorhodopsin photocycle fits within the broader microbial rhodopsin family
- [Proton Wire](/xray-mp-wiki/concepts/proton-wire/) — CHB switching during the photocycle provides the mechanistic basis for vectorial proton transport
- [Low-Barrier Hydrogen Bond](/xray-mp-wiki/concepts/low-barrier-hydrogen-bond/) — LBHBs observed in PRG across ground, K, and L states enable proton delocalization central to the photocycle
