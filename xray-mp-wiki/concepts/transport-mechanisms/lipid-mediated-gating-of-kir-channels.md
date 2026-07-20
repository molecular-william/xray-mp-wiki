---
title: "Lipid-Mediated Gating of Kir Potassium Channels"
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-functional, concept-transport-mechanism, subdirectory-transport-mechanisms]
sources: [doi/10.1038##s41467-022-28148-4]
verified: regex
---

# Lipid-Mediated Gating of Kir Potassium Channels

## Overview
Kir (inwardly rectifying) potassium channels conduct K+ through a narrow pore that does not require the canonical conformational widening of the inner helix bundle for permeation. The limiting barrier to K+ permeation lies within the ion conduction pathway at a collar of branched aliphatic side chains (Leu124 in KirBac3.1). This gate is operated by the fatty acyl tails of lipids that infiltrate the conduction pathway via conserved fenestrations in the pore walls. Acyl tails compete with and displace the leucine side chains, drawing them away from the central conduction pathway and allowing ions to pass. Anionic phospholipids (particularly PG and PE) bind tightly and specifically to the pore, with their head groups occupying the canonical Arg-Pro basic motif binding site. The nexus of electrostatic contacts between anionic lipid head groups and both pore and intracellular elements couples interdomain motions to the lipid tail movement that operates the gate.


## Mechanism/Details
(1) Anionic lipid head groups (PG, PE, and by analogy PI(4,5)P2 in eukaryotic Kir channels) bind to the Arg137/Trp46/His37 canonical lipid-binding site at the membrane-cytosol interface. (2) The lipid's acyl tails extend along surface crevices and enter the pore through conserved fenestrations below the selectivity filter. (3) Aliphatic attraction between the lipid tails and the Leu124 branched side chains draws individual leucine residues away from the conduction pathway. (4) This disrupts the tetrameric Leu124 cluster, creating an aperture of ~5 A diameter. (5) K+ ions pass through the aperture retaining a coordination shell of 4-5 water molecules. (6) The binding of anionic lipid head groups to both pore and interdomain linker regions couples interdomain conformational changes to the movement of the lipid tails, providing the regulatory link between PI(4,5)P2 binding and channel gating. The L124M mutant (methionine is unbranched and more flexible) is essentially ungated, demonstrating leucine's specific role as the steric barrier.


## Examples in Membrane Protein Work
- [KirBac Potassium Channels](/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/) — MD simulations showed K+ permeation through KirBac3.1 occurs when acyl tails engage Leu124, creating an ~5 A opening. Umbrella sampling revealed 13 kJ/mol barrier with lipid interaction vs 41 kJ/mol without. The L124M mutant conducts even with fenestrations blocked.
- [KirBac Potassium Channels](/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/) — Alkyl-MTS derivatization of Cys119 showed decyl chains increase activity (Po=0.69) while hexyl chains reduce it by blocking fenestrations without reaching Leu124, confirming length-dependent gating.
- [KirBac Potassium Channels](/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/) — Native MS of purified KirBac3.1 showed adduct masses of +765 Da (1 lipid), +1513 Da (2 lipids), and +2270 Da (3 lipids). Lipidomics confirmed PG enrichment and preferential binding of long-chain (>34 C) lipids.

## Related Concepts


## Cross-References
- [KirBac Potassium Channels](/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/) — KirBac3.1 is the primary system where lipid-mediated gating was characterized
- [Selective Lipid Binding](/xray-mp-wiki/concepts/membrane-mimetics/selective-lipid-binding/) — The anionic lipid binding specificity of Kir channels is an example of selective lipid-protein interaction
- [Force-From-Lipid Principle](/xray-mp-wiki/concepts/membrane-mimetics/force-from-lipid-principle/) — Kir channel gating by lipid tails represents a direct force-from-lipid mechanism
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — The nexus between lipid head group binding and tail-mediated gate operation represents an allosteric mechanism
