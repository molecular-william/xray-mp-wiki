---
title: CmABCB1 (Homodimeric P-glycoprotein from Cyanidioschyzon merolae)
created: 2026-06-08
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-018-08007-x, doi/10.1073##pnas.1321562111]
verified: false
---

# CmABCB1 (Homodimeric P-glycoprotein from Cyanidioschyzon merolae)

## Overview

CmABCB1 is a homodimeric P-glycoprotein from the red alga Cyanidioschyzon
merolae, a member of the ABC Transporter Family that mediates active efflux
of diverse hydrophobic xenobiotics. A pair of X-ray crystal structures were
determined in a 2018 study: an outward-facing nucleotide-bound state at
1.9 Å resolution (PDB 6A6M) and an inward-facing apo state at 3.0 Å
resolution (PDB 6A6N), revealing conformational changes between states.

A subsequent study determined the structure of CmABCB1 in an inward-open
conformation at 2.6 Å resolution (unbound) and 2.4 Å resolution (bound to
the macrocyclic peptide inhibitor aCAP). The aCAP clamps the transmembrane
helices from the outside, fixing the inward-open conformation. These
structures reveal the detailed architecture of the transporter gating
apparatus, including extracellular, intramembranous, and cytosolic gates.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-018-08007-x | 6A6M | 1.9 | P4₁32 | QTA CmABCB1 (E610A/E620A/D621A) | [Mg²⁺·AMP-PNP](/xray-mp-wiki/reagents/ligands/amp-pnp/) |
| doi/10.1038##s41467-018-08007-x | 6A6N | 3.0 | R32 | QTA CmABCB1 (E610A/E620A/D621A) |  |
| doi/10.1073##pnas.1321562111 | — | 2.60 | R32 | WT CmABCB1 with N-terminal region (1-92) cleaved, C-terminal His₁₀ tag removed |  |
| doi/10.1073##pnas.1321562111 | — | 2.40 | R32 | WT CmABCB1 with N-terminal region (1-92) cleaved, bound to aCAP | aCAP (macrocyclic peptide inhibitor) |

## Expression and Purification

- **Expression system**: Saccharomyces cerevisiae AD1-8u⁻ (for 2018 structures); Pichia pastoris SMD1163 (for WT CmABCB1 in 2014 paper)
- **Construct**: QTA mutant (E610A, E620A, D621A) for ATPase-deficient crystallization

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Emulsiflex-C3 homogenization followed by differential centrifugation | — | 20 mM Tris pH 7.0, 150 mM NaCl | Crude membranes collected at 100,000 × g |
| Solubilization | Detergent extraction | — | 20 mM Tris pH 7.0, 300 mM NaCl, 20 mM Imidazole + 1% (w/v) C12E9 | 1 h solubilization |
| IMAC | Immobilized metal-ion affinity chromatography | Bio-Rad IMAC resin | 20 mM Tris pH 7.0, 300 mM NaCl, 300 mM imidazole |  |
| Trypsin cleavage | Enzymatic cleavage | — |  | N-terminal flexible region (1–92) cleaved by Trypsin treatment |
| Size-exclusion chromatography | Gel filtration | Superdex 200 Increase (GE Healthcare) | 20 mM Tris pH 7.0, 150 mM NaCl, 0.2% (w/v) β-DM |  |

**Final sample**: 10 mg/mL in 20 mM Tris·HCl pH 7.0, 150 mM NaCl, 0.2% n-decyl-β-D-maltopyranoside


## Crystallization

### doi/10.1038##s41467-018-08007-x

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | 10 mg/ml CmABCB1 |
| Reservoir | 19–21% PEG 2000 MME, 50 mM KNO₃ pH 7.4, 50 mM Mg(NO₃)₂ pH 4.1 |
| Temperature | 20 °C |
| Cryoprotection | 30% PEG 2000 MME, 5% 1,4-Butanediol |
| Notes | Outward-facing (P4₁32 space group) |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | 10 mg/ml CmABCB1 |
| Reservoir | 14% PEG 2000 MME, 100 mM Mg(NO₃)₂ pH 4.1 |
| Temperature | 20 °C |
| Cryoprotection | 30% PEG 2000 MME, 5% 1,4-Butanediol |
| Notes | Inward-facing (R32 space group) |

### doi/10.1073##pnas.1321562111

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | CmABCB1 at 10 mg/mL in 20 mM Tris·HCl pH 7.0, 150 mM NaCl, 0.2% n-decyl-β-D-maltopyranoside; with or without aCAP (2:1 molar ratio) |
| Reservoir | 14-16% (wt/vol) PEG 2000 MME, 100 mM magnesium nitrate |
| Temperature | 20 °C |
| Cryoprotection | Frozen crystal |
| Notes | Data collected at BL41XU of SPring-8 using MAR225HE detector. Space group R32. Initial phases from MAD on mercury derivative.
 |


## Biological / Functional Insights

### Conformational states

The inward-facing apo structure reveals a large kernel-shaped inner chamber surrounded by all 12 TM helices. The outward-facing Mg·AMP-PNP-bound structure shows chamber contraction, driven by NBD dimerization.

### Chamber contraction regulator

Residues Gln398(TM6) and Ala240(TM3) form van der Waals contacts that regulate chamber volume. Mutation decreases transport activity.

### RE-latch

Glu620(α6) and Arg644(α7) form a salt bridge (RE-latch) at the NBD dimer interface that stabilizes the outward-facing conformation.

### Extracellular gate mechanism

TM1, TM2, TM5, and TM6 form a four-layered cluster of aromatic and hydrophobic
residues near the extracellular side. The GXXXG motif in TM2 and TM5 enables
close helix-helix contact. Opening of the extracellular gate occurs when TM1
and TM6 move in opposite directions (11.2 and 7.8 Å, respectively), dissociating
the helix bundle. ATP binding to NBDs causes rigid-body NBD rotation (19°),
tilt (10°), and translation (10 Å), transmitted through IH1 and IH2 to TM2 and TM5.

### Intramembranous gate and TM4 flexibility

A wide cleft between TM4 and TM6 spans the hydrophobic interface between the
TMD and inner leaflet of the lipid bilayer. TM4 exhibits intrinsic flexibility
(Gly277-Gly286 disordered) and is kinked at Pro271 and Gly299, acting as a
"gatekeeper" for substrate entry from the membrane bilayer. GAA/VVV mutation
and P271A substitution both reduce transport activity.

### aCAP allosteric inhibition

aCAP (anti-CmABCB1 peptide) is a macrocyclic peptide inhibitor that acts as a
surface clamp, binding TM2 and TM6 from the extracellular surface. It reinforces
TM1-TM6 interaction and prevents the extracellular gate from opening. aCAP
inhibits both basal and rhodamine 6G-stimulated ATPase activities (K_i 46-fold
tighter than K_m for rhodamine 6G). This confirms that extracellular gate opening
is required for the substrate-dependent ATP hydrolysis cycle.

### Vacuum cleaner model support

Structural comparison between inward-open CmABCB1 and outward-open Sav1866
(RMSD 2.4 Å for Cα) reveals that NBD dimerization drives structural changes.
The movement is transmitted to TM2 and TM5 through IH1 and IH2 coupling helices.
This mechanism is consistent with the "vacuum cleaner" model of ABC multidrug
transport, where substrates are extracted from the inner leaflet of the lipid
bilayer.


## Cross-References

- [ABC Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — CmABCB1 is a member of the ABC transporter superfamily
- [Inward-Facing Conformation](/xray-mp-wiki/concepts/transport-mechanisms/inward-facing-conformation/) — Structures capture inward-open apo and inhibitor-bound states
- [Outward-Facing Conformation](/xray-mp-wiki/concepts/transport-mechanisms/outward-facing-conformation/) — The 1.9 Å structure captures the outward-facing nucleotide-bound state
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — IMAC was used for initial purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC was used as a final purification step
- [Sitting Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Crystals were grown by sitting drop vapor diffusion
- [Sav1866 Multidrug ABC Transporter](/xray-mp-wiki/proteins/abc-transporters/sav1866/) — Outward-open ABC transporter used for gating comparison
- [Mouse P-glycoprotein (Pgp, ABCB1)](/xray-mp-wiki/proteins/abc-transporters/mouse-p-glycoprotein/) — Closest mammalian homolog
