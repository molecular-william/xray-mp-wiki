---
title: Human K2P1 (TWIK-1) Potassium Channel
created: 2026-06-21
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1213274]
verified: false
---

# Human K2P1 (TWIK-1) Potassium Channel

## Overview

Human K2P1 (also known as TWIK-1, encoded by KCNK1) is a two-pore domain potassium (K2P) channel that generates background leak K+ currents and contributes to the resting membrane potential. K2P1 is unusual among K2P channels in that it can conduct Na+ when extracellular K+ is below approximately 3 mM (hypokalemia), depolarizing cardiomyocytes and potentially contributing to cardiac arrhythmia. The crystal structure of human K2P1 was determined at 3.4 A resolution, revealing a dimeric channel with a distinctive extracellular cap domain, an interfacial C helix, and subunit interface openings that expose the central cavity to the lipid membrane.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1213274 |  | 3.4 A | P2(1) | Human K2P1 residues 19-288 (removed N-terminal 18 residues and C-terminal 48 residues), C22S, N95Q mutations | K+ ions at selectivity filter sites S1-S4; Tl+ ions (surrogate for K+) at selectivity filter |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: Human K2P1 residues 19-288, C22S, N95Q mutations
- **Notes**: Protein confirmed functional by flux assay when reconstituted into lipid vesicles (fig. S2)

### Purification Workflow

- **Expression system**: Pichia pastoris
- **Expression construct**: Human K2P1 residues 19-288, C22S, N95Q

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression and purification | Standard Pichia pastoris expression and purification | — |  | Purified protein was functional, forming K+ channels when reconstituted into lipid vesicles as confirmed by flux assay |


## Crystallization

### doi/10.1126##science.1213274

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified human K2P1 |
| Reservoir | 150 mM K+ |
| Notes | Crystals grown in presence of 150 mM K+. Soaked in Tl+ solutions for anomalous phasing. Space group P2(1) with four copies per asymmetric unit forming two channels. Experimental SAD/MAD phasing using Hg, Au, and Tl derivatives. |


## Biological / Functional Insights

### Extracellular cap domain

K2P1 has a ~55-amino acid extracellular region between M1 and pore helix 1 forming a structured cap domain extending approximately 35 A above the membrane. The cap is an A-frame structure with E1 and E2 helices from each subunit, positioned directly above the selectivity filter. Pro47 (conserved among K2P channels) creates a ~30 degree bend between M1 and E1. Cys69 (conserved in most K2P channels) forms a disulfide bond covalently linking the two subunits at the cap apex. The C-terminal ends of E2 helices are positioned above the selectivity filter, with helix dipole moments concentrating cations near the filter.

### Interfacial C helix and inner helix gating

A conserved amphipathic C helix located at the membrane/cytosol interface runs along the inner surface of the M2 and M4 inner helices. The C helix contacts the M2-M3 loop and the M4 helix of the adjacent subunit, appearing structurally poised to affect inner helix gating. Conserved glycine residues Gly141 and Gly256 in the inner helices serve as gating hinges. This region in TREK-1 is known to respond to phospholipids, intracellular acidification, and membrane stretch.

### Dimeric K2P architecture and selectivity filter

K2P channels assemble as dimers with each protomer containing two P domain sequences arranged in tandem. The selectivity filter sequences differ between P domain 1 (TTGYGH) and P domain 2 (TIGLGD), deviating from the canonical K+ channel filter sequence TXGYGD. Despite this, the filter adopts a conductive, four-fold symmetric configuration for K+ ion coordination. Thr118 (the second T in TTGYGH) is associated with the ability of K2P1 to conduct Na+ in low extracellular K+.

### Subunit interface fenestrations

K2P1 has openings between subunits (between M2 of one subunit and M4 of the other) that expose the central cavity to the hydrophobic core of the lipid membrane. These openings span much of the inner leaflet. Electron density maps revealed alkyl chains of approximately 11 carbons within these openings, likely from bound lipids or detergent. Pro143 (conserved in most K2P channels) creates a bend in M2 that contributes to these openings, which may allow lipophilic compounds like tetrahexylammonium (THA) to access the central cavity via the membrane.

### Extracellular ion pathway

The extracellular cap restricts access to the selectivity filter to two side portals (funnel-shaped, approximately 6 A van der Waals opening at the narrow end). The portals are lined by negatively charged residues (Glu84, Ser86, Asn87, Ser91, Glu235) and the C-terminal ends of E2 helices, creating an electrostatic gradient that concentrates cations near the filter. An external K+ binding site coordinated by two water molecules was observed above the filter. Sequence variation in portal-lining residues among K2P channels may account for electrophysiological differences.


## Cross-References

- [K2P 2.1 (TREK-1) Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/k2p-2-1-trek-1/) — Fellow K2P channel member; both are two-pore domain potassium channels
- [Human TASK-1 (K2P 3.1)](/xray-mp-wiki/proteins/voltage-gated-channels/human-task-1-k2p3-1/) — Fellow K2P channel member; structural and functional comparisons
- [Human TRAAK Potassium Channel (K2P 4.1)](/xray-mp-wiki/proteins/voltage-gated-channels/traak/) — K2P channel family comparison
- [Ion Channel Selectivity Filter](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) — K2P1 has a pseudo-tetrameric selectivity filter with two different P domain sequences (TTGYGH and TIGLGD)
- [C-type Inactivation](/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/) — K2P channels use a selectivity filter C-type gate as the principal gating site
