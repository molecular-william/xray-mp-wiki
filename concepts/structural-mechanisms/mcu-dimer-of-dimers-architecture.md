---
title: MCU Dimer-of-Dimers Architecture
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-structural, membrane-protein]
sources: [doi/10.1038##s41586-018-0330-9]
verified: false
---

# MCU Dimer-of-Dimers Architecture

## Overview
The mitochondrial calcium uniporter (MCU) assembles as a tetrameric channel with a dimer-of-dimers architecture, where two pairs of protomers come together to form the central ion conduction pore. Each protomer contains two transmembrane helices (TM1 and TM2) and an N-terminal soluble domain (NTD). The tetramer is arranged with near four-fold symmetry in the transmembrane domain but two-fold symmetry in the NTD, creating a symmetry mismatch. The transmembrane domain has the shape of a truncated pyramid, with TM2 helices from all four subunits lining the central pore. The conserved DXXE motif on TM2 forms the selectivity filter, with Glu336 carboxylates coordinating a bound Ca2+ ion. This architecture was determined by X-ray crystallography (MaMCU from Metarhizium acridum at 3.5 A, P2_1_2_1_2 space group) and cryo-EM (FgMCU from Fusarium graminearum in nanodiscs at 4.8-5 A) and represents a previously undescribed ion channel architecture fundamentally different from the pentameric assembly observed by NMR for C. elegans MCU.


## Mechanism/Details
The dimer-of-dimers assembly of MCU is stabilized by two types of interfaces: (1) intimate TM1-TM2 interactions between neighbouring subunits, creating a domain-swapped connectivity where TM1 of one subunit packs against TM2 of an adjacent subunit; and (2) a coiled-coil interface between the C-terminal helices of the soluble domain. The TM1-TM2 linker forms the entrance to the pore on the intermembrane space side. The selectivity filter is formed by the DXXE motif (Asp333-X-X-Glu336 in MaMCU) located at the first helical turn of TM2, with Glu336 side chains pointing into the pore centre. A strong Ca2+ density is observed at the centre surrounded by Glu336 carboxylate oxygens, indicating direct Ca2+ coordination by the selectivity filter ring. This architecture is conserved from fungi to humans, as demonstrated by structural comparison of the MaMCU and human MCU NTDs (r.m.s.d. 1.6 A).


## Examples in Membrane Protein Work
- mitochondrial-calcium-uniporter-mcu — MCU from M. acridum (MaMCU) and F. graminearum (FgMCU) both show the dimer-of-dimers architecture. The tetrameric assembly was confirmed by site-directed disulfide crosslinking in membranes and validated across multiple crystal forms and cryo-EM reconstructions. The human MCU NTD crystallizes with the same dimer interface, supporting conserved architecture.

## Related Concepts


## Cross-References
- [Mitochondrial Calcium Uniporter (MCU)](/xray-mp-wiki/proteins/voltage-gated-channels/mitochondrial-calcium-uniporter-mcu/) — MCU is the primary example of this architecture
- [Calcium Bowl](/xray-mp-wiki/concepts/miscellaneous/calcium-bowl/) — Related Ca2+ coordination concept; MCU uses a carboxylate ring for Ca2+ selectivity
- [Intramembrane Ion Coordination](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/intramembrane-ion-coordination/) — MCU's Glu336 ring represents an intramembrane Ca2+ coordination site
