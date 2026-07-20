---
title: "Activation Gate–Selectivity Filter (AG–SF) Coupling"
created: 2026-06-10
updated: 2026-06-10
type: concept
category: concepts
layout: default
tags: [concept-functional, membrane-protein, subdirectory-transport-mechanisms]
sources: [doi/10.1038##s41467-019-13227-w, doi/10.1038##nature13453, doi/10.1038##nature23269]
verified: regex
---

# Activation Gate–Selectivity Filter (AG–SF) Coupling

## Overview
AG–SF coupling is the allosteric communication mechanism between the activation gate (AG) and the selectivity filter (SF) in potassium channels. In many K+ channels, including [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/), [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), BK, and K2P channels, the SF acts as the primary gate controlling ion conduction, while the AG (typically the helix bundle crossing or inner helix gate) regulates SF conformation through long-range allosteric interactions. This coupling underlies fundamental channel properties including C-type inactivation, subconductance states, and the wide range of single-channel conductances observed across the K+ channel superfamily.


## Mechanism/Details
The molecular mechanism of AG–SF coupling was elucidated through combined X-ray crystallography and molecular dynamics simulations of the [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) potassium channel. Key elements include:

1. **Hydrophobic relay**: A conserved hydrophobic contact between an isoleucine residue on the M2 inner helix (I84 in [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/), I100 in [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/)) and the threonine side chain at the S4 ion binding site of the selectivity filter (T59 in [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/)) transmits conformational changes from the AG to the SF.

2. **Collective helix motion**: AG opening induces a collective outward movement of both M1 and M2 transmembrane helices. As I84 residues move apart with AG opening, T59 residues follow to maintain favorable hydrophobic interactions, progressively widening the SF aperture at the S4 level.

3. **Conductance modulation**: The SF opening at T59 controls K+ ion permeation. At narrow openings, high energy barriers between S4 and S3 binding sites block conduction. At optimal openings, barriers are minimized enabling efficient direct knock-on conduction with maximum single-channel current. At excessive openings, water enters the SF and disrupts K+–K+ contacts, reducing current.

4. **Inactivation coupling**: Prolonged or excessive AG opening promotes water entry into the SF, causing carbonyl flipping of the conserved valine at the S3 binding site (V60 in [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/)). This water-mediated disruption is proposed as the initial step of C-type inactivation in SF-activated K+ channels.

This mechanism was first characterized in [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), where Cuello et al. (Nature 2010) identified the structural basis for coupling between activation and inactivation gates. The [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) studies extended this by providing a quantitative framework linking AG opening to SF conformation, ion occupancy, and conductance, demonstrating that the SF functions as the primary gate whose opening is allosterically regulated by the AG.

## Examples in Membrane Protein Work
- [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) — I84-T59 hydrophobic contact mediates AG-SF coupling. MD simulations show bell-shaped conductance-opening relationship with maximum current at AG openings matching crystal structure (PDB 6OLY).
- [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — I100 and F103 on M2 helix regulate SF conformation. AG opening triggers C-type inactivation through SF collapse.
- BK channels — SF activation proposed with conductance up to ~300 pS. Dewetting of cavity serves as alternative AG mechanism.
- K2P channels ([TRAAK](/xray-mp-wiki/proteins/voltage-gated-channels/traak/), TREK-1) — SF activation demonstrated with similar coupling through isoleucine residues equivalent to I84 in [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/).

## Related Concepts
- [](/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/) — 
- [](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) — 
- [](/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/) — 

## Cross-References
- [MthK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) — MthK is the primary model system in which AG-SF coupling was quantitatively characterized
- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — KcsA provided the first structural evidence for AG-SF coupling in potassium channels
- [TRAAK](/xray-mp-wiki/proteins/voltage-gated-channels/traak/) — Related protein structure
