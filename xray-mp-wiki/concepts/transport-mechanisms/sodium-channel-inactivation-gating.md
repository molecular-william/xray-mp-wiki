---
title: "Sodium Channel Inactivation Gating"
created: 2026-05-29
updated: 2026-05-29
type: concept
category: concepts
layout: default
tags: [concept-transport-mechanism, subdirectory-transport-mechanisms]
sources: [doi/10.1038##nature11077, doi/10.1038##ncomms3465, doi/10.1038##ncomms14205, doi/10.1085##jgp.201711884]
verified: regex
---

# Sodium Channel Inactivation Gating

## Overview
Sodium channel inactivation gating in prokaryotic voltage-gated sodium channels is mediated by the C-terminal domain (CTD), specifically through a flexible linker region connecting the transmembrane pore to a distal four-helix coiled-coil bundle. This mechanism couples channel opening with inactivation, enabling rapid and voltage-dependent inactivation that is distinct from eukaryotic ball-and-chain inactivation and from C-type inactivation driven by selectivity filter collapse.


## Mechanism/Details
The inactivation mechanism in prokaryotic sodium channels involves a CTD oscillator model: the flexible linker acts as a spring tethered to a mass (the coiled-coil bundle), enabling the linker to reach the intracellular gate after channel opening without requiring unraveling of the coiled-coil. Negatively charged glutamate residues in the linker region (e.g., E229, E230, E231 in NavMs) are critical for rapid inactivation. Truncation of residues before the coiled-coil (e.g., Delta223 in NavMs) slows inactivation ~7-fold and recovery ~155-fold. The coiled-coil restricts the linker so that fast inactivation occurs at the appropriate membrane potential after channel opening. Without the coiled-coil, the inactivation linker is less coordinated to channel opening as a function of voltage.


## Examples in Membrane Protein Work
- **NavMs**: Full-length NavMs inactivates rapidly (tau_inact ~10 ms). Truncation
  of the linker region (Delta223) slows inactivation ~7-fold and recovery ~155-fold.
  Mutation of three linker glutamates to glutamines (EEE/QQQ) slows inactivation
  ~5-fold.
- **NavAb**: NavAb exhibits multiphase slow inactivation. The early voltage-dependent
  phase is controlled by side-chain volume at Thr206 in S6. The late use-dependent
  phase requires the C-terminal tail. Truncation of 10 distal residues (NavAbDelta10)
  abolishes late use-dependent inactivation at 0.2 Hz, while Delta40 accelerates the
  early phase but blocks late inactivation. Structure of NavAbDelta28 (2.3 A) shows
  preserved four-helix bundle despite truncation. (DOI: 10.1085/jgp.201711884)
- **NaChBac**: NaChBac has a considerably shorter linker region and inactivates
  12-19 times slower than NavMs (tau_inact ~203 ms vs ~10 ms), suggesting that
  linker length and flexibility account for kinetic differences between
  prokaryotic sodium channels.


## Related Concepts
- [Sodium Channel Gating and Selectivity](/xray-mp-wiki/concepts/transport-mechanisms/sodium-channel-gating/) —
  General voltage-gating mechanism of sodium channels
- [C-type Inactivation](/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/) —
  Alternative inactivation mechanism in potassium channels via selectivity filter collapse
- [Ball-and-Chain Model](/xray-mp-wiki/concepts/transport-mechanisms/ball-and-chain-model/) —
  Eukaryotic inactivation mechanism involving intracellular inactivation particle


## Cross-References
- [NavMs Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/navms/) — Primary experimental system demonstrating CTD-mediated inactivation gating
- [NaChBac Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/nachbac/) — Founding member used for functional comparison across prokaryotic channels
- [S4-S5 Linker Interaction Motif](/xray-mp-wiki/concepts/structural-mechanisms/s4-s5-linker-interaction-motif/) — Interaction motif central to gate opening/closing regulation
