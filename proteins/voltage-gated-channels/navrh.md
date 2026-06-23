---
title: NavRh (NaChBac Orthologue from HIMB114)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11054]
verified: false
---

# NavRh (NaChBac Orthologue from HIMB114)

## Overview

NavRh is a bacterial voltage-gated sodium channel from the marine alphaproteobacterium HIMB114 (Rickettsiales sp.) that is an orthologue of the [NaChBac Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/nachbac/) family. The 3.05 A crystal structure of NavRh (PDB 4F4L) reveals an asymmetric homotetramer with the selectivity filter in a closed conformation and voltage sensors in a depolarized (up) conformation. A hydrated Ca2+ ion is bound at an inner site within the selectivity filter, formed by the carbonyl oxygen atoms of Thr178 and Leu179. The structure is proposed to represent an inactivated conformation of a voltage-gated sodium channel, providing insights into the electromechanical coupling mechanism and C-type inactivation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11054 | 4F4L | 3.05 A | P42 | Full-length NavRh (G208S variant for improved diffraction), C-terminal His6 tag removed, expressed in E. coli BL21(DE3), purified in [NG](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/) with [POPC](/xray-mp-wiki/reagents/lipids/popc/):[POPE](/xray-mp-wiki/reagents/lipids/pope/):[POPG](/xray-mp-wiki/reagents/lipids/popg/) (3:1:1) lipids; crystallized with 100 mM CaCl2 | Ca2+ (bound in selectivity filter inner site) |
| doi/10.1038##nature11054 | -- | 3.7 A | P42 | Wild-type NavRh (same expression/purification as G208S variant) | Ca2+ |
| doi/10.1038##nature11054 | -- | 4.4 A | P41212 | Wild-type NavRh (alternative crystal form) | Ca2+ |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)
- **Construct**: Full-length NavRh (codon-optimized for E. coli), with or without C-terminal His6 tag; G208S or G208A mutations for improved diffraction

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and expression | E. coli BL21(DE3) overexpression induced with 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at D600nm of 1.5, grown at 30 C for 12 h | -- | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + -- | Cells harvested by centrifugation; no protease inhibitors used |
| Cell lysis | Sonication | -- | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + -- | Cell debris removed at 27,000g for 10 min |
| Membrane preparation | Ultracentrifugation at 150,000g for 1 h | -- | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl + -- | Membrane fraction collected |
| Solubilization | Membrane solubilization with detergent | -- | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 500 mM NaCl, 50 mM imidazole-HCl pH 8.0 + 1.6% n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) for 2 h at 4 C | After solubilization, supernatant clarified at 150,000g for 30 min |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni2+-nitrilotriacetate (Qiagen) | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 500 mM NaCl, 50 mM imidazole-HCl pH 8.0, 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted with 400 mM imidazole-HCl pH 8.0; His6 tag removed for crystallization |
| Size-exclusion chromatography | SEC ([Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/30) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (GE Healthcare) | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.4% [NG](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/), 0.1 mg/mL [POPC](/xray-mp-wiki/reagents/lipids/popc/):[POPE](/xray-mp-wiki/reagents/lipids/pope/):[POPG](/xray-mp-wiki/reagents/lipids/popg/) (3:1:1) + 0.4% [NG](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/) | Detergent exchanged to [NG](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/) during purification; lipids added for stability |


## Crystallization

### doi/10.1038##nature11054

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | NavRh (G208S variant) at ~10 mg/mL in 0.4% [NG](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/), [POPC](/xray-mp-wiki/reagents/lipids/popc/):[POPE](/xray-mp-wiki/reagents/lipids/pope/):[POPG](/xray-mp-wiki/reagents/lipids/popg/) (3:1:1), 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl |
| Reservoir | 16% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 (v/v), 100 mM MES-NaOH pH 6.0, 100 mM CaCl2 |
| Temperature | 18 C |
| Growth time | Overnight |
| Cryoprotection | Cryo-cooled in liquid nitrogen; [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 in reservoir serves as cryoprotectant |
| Notes | Crystals belonged to space group P42 with one tetramer per asymmetric unit. CaCl2 (100 mM) was a prerequisite for obtaining well-diffracting crystals. Initial phases derived from mercury-based single-wavelength anomalous dispersion (SAD). Wild-type crystals also obtained in P41212 space group diffracting to ~4.5 and 3.7 A. |


## Biological / Functional Insights

### Asymmetric tetramer structure of NavRh

NavRh crystallizes as an asymmetric homotetramer at 3.05 A resolution. The four protomers (Mol A-D) show subtle conformational variations in the selectivity filter and more prominent divergences in the voltage-sensing domains, particularly the S3-S4 linkers. S3-S4 linkers in Mol A and Mol C are unresolved, while those in Mol B and Mol D show distinct conformations, suggesting flexibility that may allow S4 movement during voltage sensing.

### Selectivity filter binds hydrated Ca2+ in inner site

A Ca2+ ion is bound at an inner site within the selectivity filter, coordinated by the eight carbonyl oxygen atoms from Thr178 and Leu179 at distances of 3.5-4.6 A, suggesting the ion is stabilized in a fully or mostly hydrated state. The outer mouth of the selectivity filter, defined by Ser181 and Glu183, is closed. This provides structural evidence that Nav channels allow passage of mostly hydrated Na+ and that Ca2+ can block Na+ permeation by occluding the pore at the Leu179/Thr178 site.

### Voltage sensors in depolarized conformation

All four voltage-sensing domains (VSDs) of NavRh exhibit a depolarized (up) conformation with all four conserved arginine residues (R1-R4) on the S4 segment pointing extracellularly. The external negative clusters stabilize gating charges through two invariant interactions: R4 interacts with Asp48 on S2, and R3 is hydrogen-bonded to the carbonyl of Ile90 on S3. This is consistent with the 0 mV field during crystallization.

### NavRh represents an inactivated conformation

The combination of a closed inner (activation) gate, depolarized VSDs (up conformation), and closed outer mouth of the selectivity filter (Glu183 and Ser181 closing the filter entry) indicates that NavRh represents an inactivated conformation. The Glu183 residue (and its equivalents in rat Nav1.4: Glu403, Glu758, Asp1241, Asp1532) are known to be important for C-type inactivation, and their conformation in NavRh supports a role for the selectivity filter outer negative charges in the inactivation process.

### One helical turn shift of S4 compared to NavAb

Comparison of NavRh with [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) reveals a one helical turn shift of the S4 segment towards the extracellular side in NavRh relative to [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) when the charge transfer centers (CTCs) are superimposed. For each NavRh VSD, one more gating charge is transferred than for each [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) VSD. In NavRh, the segment from R1-R2 forms an alpha-helix, while in [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) the corresponding segment is a 3(10)-helix, suggesting different degrees of activation between the two channels.

### Anti-clockwise rotation of VSDs relative to pore

Viewed from the cytoplasm, the VSDs of NavRh are rotated anticlockwise around the pore axis by approximately 30 degrees compared to [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/). The relative positions of NavRh VSDs are more similar to those in the depolarized and open conformation of Kv1.2, consistent with NavRh being in a more fully activated VSD conformation despite having a closed pore.


## Cross-References

- [NavAb Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) — Key structural comparison for voltage-sensing mechanism and S4 movement
- [NaChBac Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/nachbac/) — NavRh is an orthologue of NaChBac; functional comparison for inactivation
- [Sodium Channel Gating and Selectivity](/xray-mp-wiki/concepts/sodium-channel-gating/) — Paper discusses electromechanical coupling and voltage-sensing mechanism
- [C-Type Inactivation](/xray-mp-wiki/concepts/c-type-inactivation/) — NavRh structure proposed to represent an inactivated conformation
- [Sodium Channel Inactivation Gating](/xray-mp-wiki/concepts/sodium-channel-inactivation-gating/) — Structural insights into inactivation mechanism of voltage-gated sodium channels
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
