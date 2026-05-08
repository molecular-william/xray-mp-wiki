---
title: NavAe1p Prokaryotic Sodium Channel Pore
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [sodium-channel, bacnav, pore-domain, membrane-protein, xray-crystallography, prokaryotic]
sources: [doi/10.1016##j.jmb.2013.10.010]
---

# NavAe1p Prokaryotic Sodium Channel Pore

## Overview

NavAe1p is a pore-only construct of the prokaryotic voltage-gated sodium channel (BacNav) NavAe1 from Alkalilimnicola ehrlichei, a bacterium from Mono Lake, California. The structure at 4.0 A resolution (PDB: 4J4Q) reveals a closed conformation of the complete pore domain with a cytoplasmic tail, including a helical neck and coiled-coil region. Key findings include: (1) the S6 activation gate at Met241, (2) a cytoplasmic tail with neck and coiled-coil domains that stabilize the closed state, (3) an "outer ion" binding site at the selectivity filter outer mouth coordinated by Ser198 side-chain oxygens and water molecules, revealing a partially hydrated calcium ion. The structure provides insights into gating mechanisms and ion selectivity shared with eukaryotic NaV and CaV channels.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2013.10.010 | 4J4Q | 4.0 A (3.46 A based on CC1/2) | I222 | NavAe1p pore-only construct from Alkalilimnicola ehrlichei; includes pore domain (S5, P, S6) and cytoplasmic tail (neck + coiled-coil); tetramer | Calcium ion at outer ion binding site (selectivity filter), 4 water molecules |

## Expression and Purification

- **Expression system**: Mammalian cells (HEK 293) or Xenopus oocytes for functional studies
- **Construct**: NavAe1p pore-only construct (PD + cytoplasmic tail); full-length NavAe1 for electrophysiology

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Transient transfection | — | Described in prior publication (ref 19) | Expressed and purified in DDM as described in Shaya et al. 2013 (ref 19) |
| Concentration | Ultrafiltration | Amicon Ultra-15 100-kDa cutoff | 0.25 mM DDM, 200 mM NaCl, 20 mM Na-Hepes pH 8.0 | ~15 mg/mL for high-calcium condition; ~13.5 mg/mL for low-calcium condition |


## Crystallization

### doi/10.1016##j.jmb.2013.10.010

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 13.5 mg/mL NavAe1p, 0.25 mM DDM, 0.5 M TMAO |
| Reservoir | 200 mM CaCl2, 30% PEG 400, 100 mM Na-acetate pH 5.0 (high-Ca condition); or 200 mM MgCl2, 30% PEG 400, 100 mM MOPS pH 6.5 (low-Ca condition) |
| Temperature | 4 C |
| Growth time | ~3 weeks (high-Ca); ~2 weeks (low-Ca) |
| Cryoprotection | Not specified |
| Notes | I222 crystals ~200 um x 70 um x 15 um (high-Ca). P42 crystals ~200 um x 50 um x 50 um (low-Ca). Anomalous scattering confirmed Ca2+ at outer ion site. |


## Biological / Functional Insights

### S6 activation gate

The intracellular gate is occluded by Met241 at the S6 C-terminus. Mutation M241A causes dramatic negative shifts in both activation (delta V1/2 = -49.8 mV) and inactivation (delta V1/2 = -40.0 mV) voltage dependence, indicating this residue stabilizes the closed state. Residues above the gate (F233, I237 equivalent) affect inactivation only, not activation.

### Cytoplasmic tail neck stabilizes closed state

The neck region (6 helical turns connecting S6 to coiled-coil) is rich in charged/polar residues (15/20). Destabilizing the neck with glycine substitutions causes negative shifts in activation voltage dependence (up to 7Gly: delta V1/2 = significant). The neck appears to stabilize the closed state through its helical structure. Opening proceeds with radial expansion of the gate region and order-to-disorder transition in the neck.

### Outer ion binding site

A calcium ion binds at the selectivity filter outer mouth, coordinated by 4 Ser198 side-chain oxygens and 4 water molecules (coordination number 8). This "outer ion" site is 10.7 A from the inner ion site and marks the entry/dehydration point for ions entering the selectivity filter. The (+1) position serine is conserved and analogous to a previously unrecognized calcium binding determinant in mammalian CaV channels.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent (0.25-0.3 mM during purification)
- [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate/) — Crystallization buffer at 100 mM pH 5.0 (high-Ca condition)
- [HEPES (4-(2-Hydroxyethyl)-1-piperazineethanesulfonic Acid)](/xray-mp-wiki/reagents/buffers/hepes/) — Purification buffer at 20 mM pH 8.0
