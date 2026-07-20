---
title: "Side-Entry Ion Conduction Pathway"
created: 2026-06-11
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, membrane-protein, subdirectory-transport-mechanisms]
sources: [doi/10.1107##s205225252100213x]
verified: regex
---

# Side-Entry Ion Conduction Pathway

## Overview
The side-entry ion conduction pathway is a non-canonical mechanism for ion permeation through the selectivity filter of ion channels, first identified in the NaK nonselective cation channel from Bacillus cereus. In this pathway, a backbone carbonyl flip of Asp66 in the selectivity filter creates an additional ion binding site adjacent to the canonical pore, enabling ions (particularly Na+) to enter the selectivity filter from the side rather than through the top of the filter. This mechanism provides an explanation for how nonselective cation channels can efficiently conduct both Na+ and K+ despite having a selectivity filter sequence (TVGDG) that differs from the canonical K+-selective filter sequence (TVGYG).


## Mechanism/Details
In the NaK channel, the Asp66 backbone carbonyl can flip between two conformations. In one conformation, the carbonyl points into the canonical pore; in the flipped conformation, it creates a side pocket that can coordinate a Na+ ion. This side-entry site is coordinated by the backbone carbonyl of Phe69 (2.27 A), the backbone carbonyl of Asp66 on a symmetry-related molecule (2.59 A), a water molecule (2.63 A), and the side-chain hydroxyl of Ser70 (2.84 A). Molecular dynamics simulations demonstrate that this deformation away from the fourfold symmetric pore domain enables side-entry permeation for both K+ and Na+ ions.


## Examples in Membrane Protein Work
- NaK Channel (Bacillus cereus) — The 1.53 A structure of NaKΔ19 (PDB 6v8y) shows the Asp66 carbonyl flip in the B subunit, creating a side-entry Na+ binding site. This was confirmed by MD simulations which showed side-entry permeation when the SF deviates from fourfold symmetry.

## Related Concepts


## Cross-References
- [NaK Channel from Bacillus cereus](/xray-mp-wiki/proteins/voltage-gated-channels/nak-channel/) — The side-entry pathway was discovered in NaK, a nonselective cation channel
- [Ion Channel Selectivity Filter](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) — Side-entry permeation is a non-canonical mechanism for ion passage through the selectivity filter
