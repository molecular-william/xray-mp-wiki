---
title: Methanococcus jannaschii SecY Translocation Channel
created: 2026-05-28
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature02218, doi/10.1016##j.molcel.2007.05.002]
verified: false
---

# Methanococcus jannaschii SecY Translocation Channel

## Overview

[SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) from Methanococcus jannaschii is the core channel-forming subunit of the archaeal Sec translocon, a heterotrimeric protein-conducting complex essential for protein translocation across the membrane. The protein comprises 10 transmembrane helices arranged in two linked halves (TMs 1-5 and 6-10) that form an hourglass-shaped channel with a lateral gate and a plug helix (TM2a) that seals the periplasmic side. The landmark 2004 crystal structure at 3.2 A resolution (van den Berg et al., Nature) revealed the overall architecture of the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) complex and provided the first atomic-level model for how nascent polypeptides are translocated across or integrated into cellular membranes. Later plug deletion mutant structures revealed how the plug domain stabilizes the closed state of the channel and how its displacement mediates channel gating during protein translocation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature02218 | 1RHZ | 3.2 A | P21212 | M. jannaschii [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) complex (SecY-alpha, SecB-beta, SecE-gamma heterotrimer); wild-type Lys422Arg and Val423Thr (Y1) double mutant used for final structure | None |
| doi/10.1016##j.molcel.2007.05.002 | 1RH5 (model used for molecular replacement) | 3.5 A | P21212 | M. jannaschii [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) half-plug deletion mutant (Delta60-65); part of [SECYEG](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) complex | None |
| doi/10.1016##j.molcel.2007.05.002 | 1RH5 (model used for molecular replacement) | 3.6 A | P21212 | M. jannaschii [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) full-plug deletion mutant (Delta57-67); part of [SECYEG](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) complex | None |

## Expression and Purification

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### First crystal structure of the SecY protein-conducting channel

The 3.2 A crystal structure of the M. jannaschii [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) complex revealed that the heterotrimeric [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/)/Sec61 complex forms a protein-conducting channel. The alpha-subunit has 10 transmembrane helices divided into two linked halves (TM1-5 and TM6-10) related by pseudo-two-fold symmetry, clamped together by the gamma-subunit ([SECE](/xray-mp-wiki/proteins/secretion-translocon/sece/)). Each half consists of three outer and two inner TMs. The beta-subunit has a single TM and is not essential. The structure showed that one copy of the heterotrimer serves as a functional translocation channel.

### Plug helix seals the closed channel

TM2a, a short helix following TM1, acts as a 'plug' that blocks the bottom of a large funnel-like cavity on the cytoplasmic side of the channel. The plug sits about halfway across the membrane, separating the cytoplasmic side from the external aqueous space. The structure represents a closed channel impermeable to polypeptides and small molecules. A cysteine crosslinking experiment in E. coli showed that a disulfide bridge between the plug ([SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) residue 67) and the gamma-subunit ([SECE](/xray-mp-wiki/proteins/secretion-translocon/sece/) residue 120) results in a dominant-negative phenotype, consistent with locking the channel open.

### Hourglass-shaped pore with hydrophobic pore ring

When the plug is displaced, the channel adopts an hourglass shape with aqueous funnels on both sides of a narrow constriction. The constriction is lined by a 'pore ring' of six hydrophobic residues (Ile75, Val79, Ile170, Ile174, Ile260, Leu406 in M. jannaschii). These hydrophobic residues form a gasket-like seal around a translocating polypeptide, hindering the permeation of other molecules. The diameter of the pore ring (~5-8 A) can accommodate an extended polypeptide chain and, with slight expansion, an alpha-helix.

### Signal sequence binding site at the lateral gate

The signal sequence binding site is located between TM2b and TM7 at the front of the cytoplasmic funnel. Intercalation of a signal sequence between these helices would require the front of the alpha-subunit to open via a hinge motion (~15 degrees) between TM5 and TM6 at the back of the molecule. This site explains photocrosslinking results showing signal sequence contacts with TM2, TM7, and TM8, and exposure to lipid. The TM2b-TM7 interface is the lateral gate through which TMs of nascent membrane proteins exit into the lipid phase.

### Protein translocation cycle model

The X-ray structure enabled a refined model for the translocation of secretory proteins: (1) closed channel with plug blocking the pore; (2) channel partner binding (ribosome, SecA, or Sec62/63p); (3) substrate insertion as a loop with signal sequence intercalated between TM2b and TM7 and plug displacement; (4) polypeptide translocation through the pore with the pore ring forming a seal; (5) plug return to closed position after polypeptide passage. For membrane proteins, TMs exit through the lateral gate into lipid.

### Plug deletion mutants suppress defective signal sequences

Plug deletion mutants in E. coli [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) are functional and efficiently translocate proteins with defective or missing signal sequences (prl suppressor phenotype). The destabilized closed state of the mutant channels allows easier opening even without proper signal sequence recognition, explaining the strong suppressor activity.

### New plugs form in plug deletion mutants

Despite deletion of the native plug domain, both half-plug (Delta60-65) and full-plug (Delta57-67) deletion mutants form new alpha-helical plugs from adjacent sequences. In the half-plug mutant, the new plug comprises residues Ile55-Trp59. These new plugs lack many of the stabilizing contacts found in the wild-type, explaining why deletion mutants are functional but have destabilized closed states.


## Cross-References

- [Thermus thermophilus SecY Core Channel Subunit](/xray-mp-wiki/proteins/secretion-translocon/secy/) — Homologous SecY protein from a different organism with similar structural features
- [Thermus thermophilus SecYEG Translocon Complex](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) — The SecY subunit is the core channel-forming component of the SecYEG heterotrimer
- [SECE](/xray-mp-wiki/proteins/secretion-translocon/sece/) — Related protein structure
