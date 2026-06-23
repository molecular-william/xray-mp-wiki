---
title: "Drosophila melanogaster Orai (CRAC Channel)"
created: 2026-06-08
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1228757, doi/10.7554##eLife.36758]
verified: false
---

# Drosophila melanogaster Orai (CRAC Channel)

## Overview

Orai is the pore-forming subunit of the calcium release-activated calcium (CRAC) channel in metazoans. The Drosophila melanogaster Orai shares 73% sequence identity with human Orai1 in the transmembrane region and is the most studied non-human Orai channel. CRAC channels govern Ca2+ influx through the plasma membrane of non-excitable cells, opening in response to depletion of Ca2+ stored in the endoplasmic reticulum (ER) via STIM sensors. The channel is a hexameric assembly of six Orai subunits surrounding a single ion pore, with the six M1 helices forming the pore walls. The closed pore structure (PDB 4HKR, 3.35 A, 2012) revealed a narrow, 55 A-long pore with four sections: a glutamate ring selectivity filter (Glu178), a hydrophobic section, a basic section, and a cytosolic section. The open conformation (H206A mutant, PDB 6BBF, 6.7 A) revealed dramatic dilation of the cytosolic side of the pore by ~10 A at Lys159, with the M1-M4a portion undergoing outward rigid-body rotation. The quiescent-to-open transition requires release of cytosolic latches (M4b-M3 interaction and M4-ext helix pairing) as a necessary but not sufficient step for pore opening.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1228757 | 4HKR | 3.35 | P 21 3 | Drosophila melanogaster Orai residues 132-341 (Orai_cryst), C224S/C283T, M3-M4 loop mutations | -- |
| doi/10.7554##eLife.36758 | 6BBF | 6.70 | I 41 | H206A Orai (Drosophila melanogaster residues 133-341, C224S/C283T, crystallized with C-terminal YL1/2 tag) | none (open conformation, H206A constitutively active mutant) |
| doi/10.7554##eLife.36758 | 6BBG | 6.90 | I 41 | WT Orai (Drosophila melanogaster residues 133-341, C224S/C283T) | none (unlatched-closed conformation) |
| doi/10.7554##eLife.36758 | 6BBH | 6.10 | I 41 | K163W Orai (Drosophila melanogaster residues 133-341, C224S/C283T) | none (unlatched-closed conformation, loss-of-function mutant) |
| doi/10.7554##eLife.36758 | 6BBI | 4.35 | P 42 21 2 | K163W Orai (Drosophila melanogaster residues 133-341, C224S/C283T), P42212 form | none (unlatched-closed conformation) |

## Expression and Purification

- **Expression system**: Pichia pastoris
- **Construct**: Drosophila melanogaster Orai (amino acids 133-341) with C-terminal YL1/2 antibody affinity tag (EGEEF), C224S and C283T mutations

### Purification Workflow

- **Expression system**: Pichia pastoris
- **Expression construct**: Drosophila melanogaster Orai residues 133-341, C224S/C283T, C-terminal YL1/2 tag
- **Tag info**: C-terminal YL1/2 tag (EGEEF), not removed

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Homogenization | -- | 150 mM KCl, 10 mM sodium phosphate pH 7.0, 0.1 mg/mL DNase I, 1:1000 Protease Inhibitor Cocktail Set III, 1 mM [Benzamidine](/xray-mp-wiki/reagents/ligands/benzamidine/), 0.5 mM AEBSF, 0.1 mg/mL soybean [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) inhibitor + -- | Lysed P. pastoris cells resuspended in buffer at 3.3 mL/g cells |
| Membrane preparation | Centrifugation | -- | 150 mM KCl, 10 mM sodium phosphate pH 7.0 + -- | Membranes isolated by centrifugation |
| Membrane solubilization | Detergent extraction | -- | 150 mM KCl, 100 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.5, 0.1 mg/mL lipids + 5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Membranes solubilized in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Affinity purification | YL1/2 antibody affinity | YL1/2 antibody column (anti-tubulin) | 150 mM KCl, 100 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.5, 5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1 mg/mL lipids + 5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted with buffer containing 5 mM Asp-Phe peptide |
| SEC | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 75 mM KCl, 10 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.5, 0.1 mg/mL lipids, plus detergents + 4 mM [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) (P42212 form) or 0.5 mM [Dmng](/xray-mp-wiki/reagents/detergents/dmng/) + 3 mM [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) (I41 form) or 0.5 mM [Dmng](/xray-mp-wiki/reagents/detergents/dmng/) (H206A) | Protein concentrated to ~25 mg/mL. For H206A, 3 mM [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) added just before crystallization. Typical yield ~2 mg from 20 g cells. |

**Final sample**: ~25 mg/mL in 75 mM KCl, 10 mM Tris-HCl pH 8.5, 0.1 mg/mL lipids, detergent mixture
**Yield**: ~2 mg from 20 g cells
**Purity**: >95%


## Crystallization

### doi/10.1126##science.1228757

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified Orai_cryst |
| Reservoir | Not specified in main text (see supplementary materials) |
| Temperature | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals formed in space group P2_13 at 3.35 A resolution. Experimental phases from Hg, Ir, and Gd heavy atom derivatives. NCS averaging used for phase improvement. R_free = 28%. |

### doi/10.7554##eLife.36758

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Orai at 10-20 mg/mL in 75 mM KCl, 10 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.5, 0.1 mg/mL lipids, detergent mixture |
| Reservoir | 32-35% [Peg](/xray-mp-wiki/reagents/additives/peg/) 400 (v/v), 0.1 M potassium phosphate pH 7.5 (WT); 24-26% [Peg](/xray-mp-wiki/reagents/additives/peg/) 400, 0.2 M potassium phosphate pH 6.5 (K163W P42212); 26-28% [Peg](/xray-mp-wiki/reagents/additives/peg/) 400, 0.1 M potassium phosphate pH 7.5 (K163W I41) |
| Temperature | 20 C |
| Growth time | Not specified |
| Cryoprotection | Serial transfer into solutions with increasing [Peg](/xray-mp-wiki/reagents/additives/peg/) 400, then flash-cooled in liquid nitrogen |
| Notes | All crystals dehydrated and cryo-protected before flash-cooling. H206A structure at 6.7 A resolution with 24 subunits per asymmetric unit (4 hexameric channels). Crystallographic phases determined by MR-SAD, phases improved by 24-fold NCS averaging. For ion experiments, Ba2+ (5 mM BaCl2 added to protein), Gd3+ (soaked), or I- (NaI substituted for KCl in purification) were used. |


## Biological / Functional Insights

### Hexameric architecture with closed and open pore conformations

Orai forms a hexameric channel with four transmembrane helices (M1-M4) per subunit. The M1 helices line the pore. The quiescent closed conformation (PDB 4HKR, Science 2012) has a narrow 55 A pore with a glutamate ring selectivity filter (Glu178), a 15 A hydrophobic section, a 15 A basic section (three basic residues per subunit: Lys163, Lys159, Arg155), and a cytosolic section. The open conformation (H206A, PDB 6BBF) shows dramatic dilation of the cytosolic pore by ~10 A at Lys159 via outward rigid-body rotation of M1-M4a.

### Unlatching is necessary but not sufficient for pore opening

In the quiescent conformation, M4-ext helices pair through coiled-coil interactions, and M4b interacts with M3. The open structure reveals that M4/M4-ext are repositioned by straightening at Pro288 and the SHK hinge, forming a continuous alpha-helix. An unlatched-closed conformation (WT Orai, PDB 6BBG) has straightened M4/M4-ext but a closed pore, demonstrating that unlatching is necessary but not sufficient for opening. The K163W (corresponding to human R91W) loss-of-function mutant also adopts an unlatched-closed conformation.

### Ion binding and selectivity in the closed pore

The Science 2012 structure revealed the closed state architecture. A glutamate ring (Glu178) at the extracellular end forms the Ca2+ selectivity filter. A basic region near the intracellular side (Lys163, Lys159, Arg155) binds anions ([Iron](/xray-mp-wiki/reagents/additives/iron/), chloride) that may stabilize the closed state. Ca2+ binding was observed at an external site above the glutamate ring. The hydrophobic section between these two regions is remarkably rigid and lined by conserved residues (Val174, Phe171, Leu167). Mutations in the hydrophobic region (V174A) create constitutively active channels.

### Ion binding in the open pore informs selectivity mechanisms

Anomalous-difference electron density maps show Ba2+ and Gd3+ bind at the glutamate ring selectivity filter in the open pore. Gd3+ binding is similar to the closed state, while Ba2+ is positioned within the glutamate ring (vs above it in the closed state), suggesting subtle changes at the selectivity filter upon opening. The basic region binds I- in the open pore, indicating anions may shield positive charges during Ca2+ permeation. The proposed mechanism involves 1-2 Ca2+ ions in single file within the selectivity filter.


## Cross-References

- [Channel Gating](/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/) — Orai activation involves conformational changes including unlatching of M4b-M3 interactions and M4-ext helix rearrangement
- [Selectivity Filter](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) — The Glu178 ring forms the Ca2+ selectivity filter in the Orai pore
- [Non-Crystallographic Symmetry](/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/) — 24-fold NCS averaging was essential for determining phases at modest resolution
- [N-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for membrane protein solubilization and purification
- [Benzamidine](/xray-mp-wiki/reagents/ligands/benzamidine/) — Referenced in context related to Benzamidine
- [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) — Referenced in context related to Trypsin
- [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in context related to Tris Hcl
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in context related to DDM
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Referenced in context related to Superdex 200
- [OGNG](/xray-mp-wiki/reagents/detergents/ogng/) — Referenced in context related to OGNG
