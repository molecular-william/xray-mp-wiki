---
title: Proton Release Complex in Microbial Rhodopsins
created: 2026-06-08
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, concept-functional, subdirectory-concepts]
sources: [doi/10.1038##s41467-020-20596-0, doi/10.1038##s41594-022-00762-2, doi/10.1126##science.280.5371.1934]
verified: false
---

# Proton Release Complex in Microbial Rhodopsins

## Overview
The proton release complex (PRC) is a conserved structural motif in microbial rhodopsins responsible for releasing protons to the extracellular medium during the photocycle. In bacteriorhodopsin (BR), the PRG (proton release group) consists of E194 and E204, forming part of the proton transport pathway. The 2.3 A structure (Luecke et al., 1998) first established the Arg82-W403-Glu204-Glu194 pathway for proton release to the extracellular surface. True-atomic-resolution structures of BR at 1.05–1.53 Å resolution (PDB 7Z09–7Z0E) later revealed that the PRG adopts a triple conformation in the ground and K states, with one low-barrier hydrogen bond (LBHB, 2.4 Å) indicating delocalized proton sharing between E194 and E204. In AR3, the PRC consists of Glu204 and Glu214, which are the functional equivalents of Asp85 and Asp96 in BR.


## Mechanism/Details
The proton release complex in BR and AR3 exhibits dynamic conformational behavior that enables proton storage and release.

**Bacteriorhodopsin PRG.** The PRG (E194/E204 pair) in BR shows distinct behavior across the photocycle:
- **Ground and K states:** Triple conformation of the PRG. Major conformation (~50% occupancy) features a very short H-bond of 2.4 Å between E194 and E204, characteristic of a low-barrier hydrogen bond (LBHB) with delocalized (shared) proton. Two minor conformations (~25% each) show longer distances (2.9 Å), indicating localized proton on one residue.
- **L state:** Single conformation with an extremely short H-bond (2.3 Å) between E194 and E204, plus short H-bonds between R82 and E194 (2.4 Å) and between E204 and w408' (2.5 Å). The excess proton just before release is delocalized within a short proton wire R82-E194-E204-w408'.
- **M state:** No short H-bonds remain in the PRG, consistent with proton release. Instead, R82 and E204 form an ionic lock preventing proton backflow. Two very short H-bonds (2.4 Å each) near S193 and P77 at the surface suggest transient proton storage.

The proton release from the PRG is triggered through a Newton's cradle-like mechanism: D85 protonation on the L-to-M transition causes polarization changes along a linear CHB connecting D85 to the PRG, mediated by R82 charge redistribution.

**AR3 PRC.** In AR3, the PRC consists of Glu204 and Glu214. High-resolution structures (PDB: 6GUX and 6S6C) reveal that Glu214 adopts two conformations at 0.5 partial occupancy in both DA and LA states, distinguished by an 87.4 degree rotation around the Cgamma-Cdelta bond. The distance between the two Glu214 conformations and Glu204 is 2.3 A and 2.9 A, respectively. Free-energy QM/MM calculations indicate that Glu214 is most likely protonated in both DA and LA states, while Glu204 is fully ionized, consistent with the ground state and early photo-intermediates of bacteriorhodopsin.

**Historical context from the 2.3 A structure.** The Luecke et al. (1998) 2.3 A structure first identified W403 as a key water molecule hydrogen-bonded to NE of Arg82 and within 3.5 A of OE2 of Glu204, providing a direct pathway for proton release through Arg82-W403-Glu204-Glu194. This structure showed that the alternative pathway through Thr205 and Glu9 has less favorable distances and orientation, a finding later confirmed by extensive mutational and spectroscopic studies.


## Examples in Membrane Protein Work
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — BR PRG (E194/E204) - the 2.3 A structure (1998) first established the Arg82-W403-Glu204-Glu194 proton release pathway; subsequent true-atomic-resolution structures (PDB 7Z09-7Z0E) revealed triple conformation in ground/K states with LBHB-delocalized proton, single conformation in L state, and ionic lock in M state
- [Archaerhodopsin-3](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-3/) — AR3 PRC consists of Glu204 and Glu214; both DA and LA structures show Glu214 in two conformations with Glu214 protonated and Glu204 ionized

## Related Concepts
- [Low-Barrier Hydrogen Bond](/xray-mp-wiki/concepts/structural-mechanisms/low-barrier-hydrogen-bond/) — The 2.3-2.4 Å H-bonds in the BR PRG are LBHBs containing delocalized protons
- [Bacteriorhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/bacteriorhodopsin-photocycle/) — The PRG evolves through the photocycle, with LBHBs in ground/K/L states and ionic lock in M state
- [Proton Wire](/xray-mp-wiki/concepts/transport-mechanisms/proton-wire/) — The PRG is connected to D85 via a linear CHB that mediates long-range signaling for proton release

## Cross-References
- [Archaerhodopsin-3 (AR3)](/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-3/) — High-resolution structures reveal PRC conformation in both DA and LA states
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archetypal microbial rhodopsin; the 2.3 A structure first defined the PRG pathway; true atomic resolution later resolved PRG conformations
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/) — PRC participates in proton release step of the photocycle
- [Low-Barrier Hydrogen Bond](/xray-mp-wiki/concepts/structural-mechanisms/low-barrier-hydrogen-bond/) — The short H-bonds in the PRG are the primary examples of LBHBs in a membrane protein
- [Merohedral Twinning in Protein Crystallography](/xray-mp-wiki/concepts/methods-techniques/merohedral-twinning/) — The 2.3 A bR structure is a classic example of merohedral twinning in membrane protein crystallography
