---
title: Methanococcus jannaschii SecY Translocation Channel
created: 2026-05-28
updated: 2026-05-28
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.molcel.2007.05.002]
verified: false
---

# Methanococcus jannaschii SecY Translocation Channel

## Overview

SecY from Methanococcus jannaschii is the core channel-forming subunit of the archaeal Sec translocon, a heterotrimeric protein-conducting complex essential for protein translocation across the membrane. The protein comprises 10 transmembrane helices arranged in two linked halves (TMs 1-5 and 6-10) that form an hourglass-shaped channel with a lateral gate and a plug helix (TM2a) that seals the periplasmic side. This paper reports crystal structures of plug deletion mutants that reveal how the plug domain stabilizes the closed state of the channel and how its displacement mediates channel gating during protein translocation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.molcel.2007.05.002 | 1RH5 (model used for molecular replacement) | 3.5 A | P21212 | M. jannaschii SecY half-plug deletion mutant (Delta60-65); part of SecYEG complex | None |
| doi/10.1016##j.molcel.2007.05.002 | 1RH5 (model used for molecular replacement) | 3.6 A | P21212 | M. jannaschii SecY full-plug deletion mutant (Delta57-67); part of SecYEG complex | None |

## Expression and Purification

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### Plug domain stabilizes the closed state of the SecY channel

The plug helix (TM2a) sits in the periplasmic funnel abutting the pore ring, sealing the channel in its closed state. In wild-type SecY, the plug makes extensive contacts with both the lateral gate helices (TM2b and TM7) and the pore ring residues, locking the channel closed. This prevents uncontrolled ion flux while the channel awaits a translocation substrate.

### New plugs form in plug deletion mutants

Despite deletion of the native plug domain, both half-plug (Delta60-65) and full-plug (Delta57-67) deletion mutants form new alpha-helical plugs from adjacent sequences. In the half-plug mutant, the new plug comprises residues Ile55-Trp59. In the full-plug mutant, the new plug is recruited from a different segment. These new plugs lack many of the stabilizing contacts found in the wild-type, explaining why deletion mutants are functional but have destabilized closed states.

### Channel gating mechanism via plug displacement

The paper proposes a gating model where signal sequence intercalation at the lateral gate displaces the plug helix. The plug acts as both a seal and a lock: its displacement reduces contacts with the lateral gate and pore ring, allowing TM2b and TM7 to separate and the pore ring to widen for polypeptide passage. This mechanism explains the signal-sequence-suppressor phenotype of plug deletion mutants.

### Plug deletion mutants suppress defective signal sequences

Plug deletion mutants in E. coli SecY are functional and efficiently translocate proteins with defective or missing signal sequences (prl suppressor phenotype). The destabilized closed state of the mutant channels allows easier opening even without proper signal sequence recognition, explaining the strong suppressor activity.


## Cross-References

- [Thermus thermophilus SecY Core Channel Subunit](/xray-mp-wiki/proteins/secy/) — Homologous SecY protein from a different organism with similar structural features
- [Thermus thermophilus SecYEG Translocon Complex](/xray-mp-wiki/proteins/secyeg/) — The SecY subunit is the core channel-forming component of the SecYEG heterotrimer
