---
title: "CLC-sy1 (CLC Cl-/H+ Antiporter from Synechocystis sp. PCC6803)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1021##bi1019258]
verified: false
---

# CLC-sy1 (CLC Cl-/H+ Antiporter from Synechocystis sp. PCC6803)

## Overview

CLC-sy1 (SY) is a CLC Cl-/H+ exchange transporter from the cyanobacterium Synechocystis sp. PCC6803. Its X-ray crystal structure was determined at 3.2 Angstrom resolution, revealing a homodimeric architecture nearly identical to that of the E. coli CLC-ec1 (EC) homologue (39% sequence identity, C-alpha rmsd 1.3 Angstrom). All key residues involved in Cl- binding and proton coupling are structurally conserved. SY actively pumps protons into liposomes against a gradient and moves Cl- at approximately 20 s-1 per subunit, roughly 100-fold slower than EC. Electrostatic calculations identified two residues (F143 and D309) flanking the external binding site that are destabilizing for Cl- binding in SY; mutating these to their EC counterparts (F143R/D309F) accelerates transport to approximately 150 s-1, allowing measurement of the Cl-/H+ stoichiometry at 2:1. SY provides a comparative structural model for understanding the determinants of CLC transport rates.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1021##bi1019258 | 3NCO | 3.2 A | unknown | CLC-sy1 residues 26-450 from Synechocystis sp. PCC6803, expressed in E. coli, treated with lysine-C endoproteinase to remove first 14 N-terminal residues | Cl- (central binding site) |
| doi/10.1021##bi1019258 | 3Q17 | 3.2 A | unknown | Same construct as 3NCO, crystallized with Br- | Br- (anomalous difference data) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: CLC-sy1 from Synechocystis sp. PCC6803. For crystallization, the preparation was treated with lysine-C endoproteinase to remove the first 14 N-terminal residues. Purified on Superdex 200 gel filtration column in 100 mM NaCl, 20 mM Tris-HCl, pH 7.5, and 5 mM DM.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Gel filtration | Size-exclusion chromatography | Superdex 200 | 100 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) (pH 7.5) + 5 mM DM ([Decylmaltoside](/xray-mp-wiki/reagents/detergents/dm/)) | Lysine-C endoproteinase treatment (1 h, 0.01 unit/mg, 25 C) before Superdex 200 step to remove first 14 N-terminal residues |


## Crystallization

### doi/10.1021##bi1019258

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified CLC-sy1 at 18-25 mg/mL with 40 mM DM |
| Reservoir | 30-32% PEG 400, 200 mM [CaCl2](/xray-mp-wiki/reagents/additives/calcium-chloride/), 100 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) (pH 8.0-8.2) |
| Temperature | not specified |
| Growth time | 3-12 days |
| Cryoprotection | not specified |
| Notes | Additives introduced to final concentrations: C-Hega-11 (14 mM), SrCl2 (12 mM), PEG 400 (6.2%), and in some cases Hega-10 (9 mM) and decanoyl sucrose (3 mM). Only crystals larger than 200 um diffracted well. Structure solved by molecular replacement with PHASER using EC homodimer (PDB 1OTS) as search model. Anisotropic diffraction with high mosaicity. High solvent content (80%). |


## Biological / Functional Insights

### Slow transport rate compared to E. coli homologue

CLC-sy1 transports Cl- at ~20 s-1, approximately 100-fold slower than CLC-ec1 (2000-3000 s-1). This refutes the idea that CLC transport mechanisms intrinsically produce high rates. Despite nearly identical structures and shared 2:1 Cl-/H+ antiport stoichiometry, subtle sequence differences produce dramatically different turnover rates.

### Electrostatic determinants of transport rate

Electrostatic calculations identified residues F143 and D309 as key determinants of transport rate. Positioned at the N-terminal ends of helices pointed at the external Cl- site and adjacent to the external glutamate gate (E144), these residues are destabilizing for Cl- binding in SY and stabilizing in EC. The double mutant F143R/D309F increases SY turnover to ~150 s-1 (8% of EC rate).

### Gate removal does not speed transport in SY

In EC, removal of both external and internal gates (E148A/Y445A) produces a continuous pore and increases Cl- transport to ~20000 s-1. However, the equivalent mutation in SY (E144A/Y437A) produces no change in the slow Cl- transport rate, a surprising result that remains unexplained without a crystal structure of the double mutant.


## Cross-References

- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Primary solubilization and purification detergent (5 mM DM)
- [Calcium Chloride (CaCl2)](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Component in crystallization reservoir (200 mM CaCl2)
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Buffer component in purification (100 mM NaCl)
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used in purification and crystallization
