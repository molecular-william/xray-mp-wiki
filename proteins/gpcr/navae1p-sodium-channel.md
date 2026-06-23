---
title: NavAe1p Prokaryotic Sodium Channel Pore
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2013.10.010]
verified: false
---

# NavAe1p Prokaryotic Sodium Channel Pore

## Overview

NavAe1p is a pore-only construct of the prokaryotic voltage-gated sodium channel NavAe1 from Alkalilimnicola ehrlichei, a bacterium found in Mono Lake, California. The crystal structure at 4.0 A resolution reveals a closed conformation of the complete pore domain with a cytoplasmic tail including a helical neck and coiled-coil region. Key findings include the S6 activation gate position, the role of the cytoplasmic tail neck in stabilizing the closed state, and an outer ion binding site at the selectivity filter that reveals a previously unknown calcium binding determinant conserved in eukaryotic voltage-gated calcium channels.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2013.10.010 | 4J4Q | 4.0 A | I222 | NavAe1p pore-only construct from Alkalilimnicola ehrlichei; includes transmembrane pore domain (S5, P1, P2, S6) and full cytoplasmic tail (neck + coiled-coil); homotetramer | Calcium ion at outer ion binding site (selectivity filter outer mouth), coordinated by 4 Ser198 side-chain oxygens and 4 water molecules |
| doi/10.1016##j.jmb.2013.10.010 | 4J4Q (low-calcium) | 3.8 A | P4212 | NavAe1p pore-only construct, low-calcium crystallization condition | None (no anomalous density at outer ion site) |
| doi/10.1016##j.jmb.2013.10.010 | 4J4Q (H245G mutant) | 4.0 A | I222 | NavAe1p H245G mutant pore-only construct; no Ca2+ at neck ion or outer ion site | None (no anomalous density for neck ion or outer ion) |

## Expression and Purification

- **Expression system**: HEK 293 mammalian cells (for functional electrophysiology); NavAe1p purified from prior publication (Shaya et al. 2011)
- **Construct**: NavAe1p pore-only construct (residues corresponding to pore domain S5-P1-P2-S6 plus cytoplasmic tail with neck and coiled-coil); full-length NavAe1 for electrophysiology; H245G mutant for structural comparison

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression and solubilization | Transient transfection of HEK 293 cells; membrane extraction and solubilization | -- | Described in prior publication (Shaya et al. 2011) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (N-Dodecyl-Beta-D-Maltoside) at 0.25-0.3 mM | NavAe1p expressed and purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) as previously described in Shaya et al. 2011 (ref 19 in the paper). Full-length NavAe1 expressed in HEK 293 cells for functional studies. |
| Size-exclusion chromatography | Size-exclusion chromatography | -- | 0.25 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 200 mM NaCl, 20 mM Na-HEPES pH 8.0 + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (N-Dodecyl-Beta-D-Maltoside) at 0.25 mM | Final SEC buffer exchange prior to concentration for crystallization |
| Concentration | Ultrafiltration | Amicon Ultra-15 100-kDa molecular mass cutoff (Millipore) | 0.25 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 200 mM NaCl, 20 mM Na-HEPES pH 8.0 + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) at 0.25 mM | Concentrated to ~15 mg/ml for high-calcium condition; ~13.5 mg/ml for low-calcium condition |


## Crystallization

### doi/10.1016##j.jmb.2013.10.010

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 13.5 mg/ml NavAe1p, 0.25 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.5 M TMAO, 200 mM NaCl, 20 mM Na-HEPES pH 8.0 |
| Reservoir | 200 mM CaCl2, 30% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 100 mM Na-acetate pH 5.0 (high-calcium condition) |
| Temperature | 4 C |
| Growth time | ~3 weeks (high-calcium); crystals grew to ~200 um x 70 um x 15 um |
| Cryoprotection | Not specified |
| Notes | I222 crystals. Protein-TMAO solution (0.7 ul) mixed with 0.7 ul mother liquor mixed with agarose (0.25% final) solidified at room temperature. Anomalous scattering confirmed Ca2+ at outer ion site. |

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 13.5 mg/ml NavAe1p, 0.25 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 200 mM NaCl, 20 mM Na-HEPES pH 8.0 |
| Reservoir | 200 mM MgCl2, 30% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 100 mM MOPS pH 6.5 (low-calcium condition) |
| Temperature | 4 C |
| Growth time | ~2 weeks; crystals appeared in 2 days, grew to ~200 um x 50 um x 50 um |
| Cryoprotection | Not specified |
| Notes | P4212 crystals. No anomalous density at outer ion site. |


## Biological / Functional Insights

### S6 activation gate position at Met241

The intracellular gate is occluded by Met241 at the S6 C-terminus. Mutation of the equivalent residue (NavSp1 M220A) causes dramatic negative shifts in both activation (delta V1/2 = -49.8 mV) and inactivation (delta V1/2 = -40.0 mV) voltage dependence, indicating this residue is critical for stabilizing the closed state. Residues above the gate (F233, I237 equivalent to NavSp1 L212A and I216A) affect inactivation only, not activation, shifting inactivation voltage dependence by ~14 mV without affecting activation.

### Cytoplasmic tail neck stabilizes the closed state

The neck region (6 helical turns connecting S6 to the coiled-coil) is rich in charged/polar residues (15/20). Destabilizing the neck with [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) substitutions causes negative shifts in activation voltage dependence, with the largest perturbation (7Gly mutation) having effects comparable to activation gate disruption. The neck appears to stabilize the closed state through its helical structure, and opening proceeds with radial expansion of the gate region accompanied by an order-to-disorder transition in the neck.

### Outer ion binding site at the selectivity filter

A calcium ion binds at the selectivity filter outer mouth, coordinated by 4 Ser198 side-chain oxygens and 4 water molecules (coordination number 8). This "outer ion" site is 10.7 A from the inner ion site and marks the entry/dehydration point for ions entering the selectivity filter. The (+1) position serine is conserved and analogous to a previously unrecognized calcium binding determinant in mammalian voltage-gated calcium channels (CaV). Mutation of the equivalent residue in CaV1.2 (D707N) reduces calcium affinity by ~6-fold.

### Commonality between BacNav and eukaryotic VGICs

The structural and functional findings underscore deep evolutionary links between bacterial sodium channels (BacNav) and eukaryotic voltage-gated ion channels. The outer ion binding site architecture is conserved between BacNav and CaV channels. The cytoplasmic tail with its coiled-coil domain has parallels in eukaryotic Kv7 and TRP channels. Multiple ion binding sites in the selectivity filter support the multi-ion pore model shared across the VGIC superfamily.

### BacNav gating mechanism

A model for BacNav gating is proposed: in the closed state, the intracellular pore is occluded by the activation gate constriction (Met241). Opening proceeds with radial expansion of this region accompanied by an order-to-disorder transition in the neck. The abundance of polar and charged neck residues may aid the transition to the open/disordered state and assist in permeant ion escape into the cytoplasm. The neck and activation gate are strongly coupled, as mutations at both cause parallel shifts in activation and inactivation voltage dependence.


## Cross-References

- [N-Dodecyl-Beta-D-Maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent used throughout purification (0.25-0.3 mM)
- [HEPES (4-(2-Hydroxyethyl)-1-piperazineethanesulfonic Acid)](/xray-mp-wiki/reagents/buffers/hepes/) — Purification and crystallization buffer at 20 mM pH 8.0
- [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate/) — Crystallization buffer at 100 mM pH 5.0 for high-calcium condition
- [MOPS (4-Morpholineethanesulfonic Acid)](/xray-mp-wiki/reagents/buffers/mops/) — Crystallization buffer at 100 mM pH 6.5 for low-calcium condition
- [PEG (Polyethylene Glycol) 400](/xray-mp-wiki/reagents/additives/peg/) — Crystallization precipitant at 30% in both conditions
- [Calcium Chloride](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Crystallization additive (200 mM) in high-calcium condition; bound at outer ion site
- [Trimethylamine N-Oxide (TMAO)](/xray-mp-wiki/reagents/additives/tmao/) — Crystallization additive (0.5 M) in high-calcium condition to stabilize protein
- [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Crystallization additive (200 mM) in low-calcium condition
- [KirBac Potassium Channels](/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/) — Prokaryotic ion channel with similar modular pore domain architecture
- [Ilyobacter Tartaricus C-Subunit](/xray-mp-wiki/proteins/pumps-atpases/ilyobacter-tartaricus-c-subunit/) — Prokaryotic membrane protein with coiled-coil cytoplasmic domain architecture
