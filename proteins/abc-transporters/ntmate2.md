---
title: NtMATE2 (Nicotiana tabacum MATE2) - Nicotine MATE transporter
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1002##1873-3468.14136]
verified: false
---

# NtMATE2 (Nicotiana tabacum MATE2) - Nicotine MATE transporter

## Overview

NtMATE2 is a multidrug and toxic compound extrusion (MATE) family transporter from Nicotiana tabacum (tobacco) that mediates vacuolar sequestration of [[Nicotine](/xray-mp-wiki/reagents/ligands/nicotine)(/xray-mp-wiki/reagents/ligands/nicotine/)], a specialized alkaloid. As one of three MATE transporters in tobacco roots, NtMATE2 transports [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine) from the cytosol into the vacuolar lumen in exchange for protons, protecting the plant from its own toxic metabolite. The crystal structures reveal two outward-facing conformations with unprecedented TM7 movement distinct from other eukaryotic MATE proteins.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1002##1873-3468.14136 | 7DQK | 3.5 A | P212121 | NtMATE2-EFPGENLYFQGQF-eGFP(3-239)-H8, residues 18-493 (Mol-A), 15-493 (Mol-B) | Unidentified molecule in Mol-B C-lobe cavity (possibly partial [[Nicotine](/xray-mp-wiki/reagents/ligands/nicotine)(/xray-mp-wiki/reagents/ligands/nicotine/)] mimic) |

## Expression and Purification

- **Expression system**: Pichia pastoris yeast strain SMD1168
- **Construct**: C-terminal [GFP(/xray-mp-wiki/reagents/protein-tags/gfp/)]-[His8 tag(/xray-mp-wiki/reagents/protein-tags/his8-tag/)] fusion, induced with 0.5% [[Methanol](/xray-mp-wiki/reagents/additives/methanol)(/xray-mp-wiki/reagents/additives/methanol/)] in BMMY medium at 20 C for 72 h

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvesting and membrane fractionation | Cell lysis using Microfluidizer at 22,000 p.s.i. (five passes); membrane fraction separated by centrifugation | -- | 300 mM [[Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride)(/xray-mp-wiki/reagents/additives/sodium-chloride/)], 20 mM [[TRIS](/xray-mp-wiki/reagents/buffers/tris)(/xray-mp-wiki/reagents/buffers/tris/)]-HCl pH 8.0, 10% [[Glycerol](/xray-mp-wiki/reagents/additives/glycerol)(/xray-mp-wiki/reagents/additives/glycerol/)] + -- | Transformed cells selected with stepwise [[G418](/xray-mp-wiki/reagents/additives/g418)(/xray-mp-wiki/reagents/additives/g418/)] at 50, 100, and 200 ug/mL on YPD medium plates |
| Solubilization | Detergent solubilization of membrane fraction | -- | 300 mM [[Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride)(/xray-mp-wiki/reagents/additives/sodium-chloride/)], 20 mM [[TRIS](/xray-mp-wiki/reagents/buffers/tris)(/xray-mp-wiki/reagents/buffers/tris/)]-HCl pH 8.0, 10% [[Glycerol](/xray-mp-wiki/reagents/additives/glycerol)(/xray-mp-wiki/reagents/additives/glycerol/)] + 2% [[DDM](/xray-mp-wiki/reagents/detergents/ddm)(/xray-mp-wiki/reagents/detergents/ddm/)] (Glycon), 2 h incubation | After solubilization, centrifuged at 130,000 g for 30 min; supernatant collected |
| Affinity chromatography | [[TALON](/xray-mp-wiki/reagents/additives/talon)(/xray-mp-wiki/reagents/additives/talon/)] cobalt affinity chromatography (Clontech) | [TALON](/xray-mp-wiki/reagents/additives/talon) cobalt affinity resin (Clontech) | Equilibration: 300 mM [[Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride)(/xray-mp-wiki/reagents/additives/sodium-chloride/)], 50 mM [[HEPES](/xray-mp-wiki/reagents/buffers/hepes)(/xray-mp-wiki/reagents/buffers/hepes/)]-Na pH 7.0, 5% [[Glycerol](/xray-mp-wiki/reagents/additives/glycerol)(/xray-mp-wiki/reagents/additives/glycerol/)], 0.05% [[DDM](/xray-mp-wiki/reagents/detergents/ddm)(/xray-mp-wiki/reagents/detergents/ddm/)], 0.005% [CHS(/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)], 20 mM [[Imidazole](/xray-mp-wiki/reagents/additives/imidazole)(/xray-mp-wiki/reagents/additives/imidazole/)] pH 8.0 + 0.05% [[DDM](/xray-mp-wiki/reagents/detergents/ddm)(/xray-mp-wiki/reagents/detergents/ddm/)], 0.005% [CHS(/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)] | [His8-tag(/xray-mp-wiki/reagents/protein-tags/his8-tag/)]-tagged NtMATE2 bound; washed with buffer containing 0.03% [[LMNG](/xray-mp-wiki/reagents/detergents/lmng)(/xray-mp-wiki/reagents/detergents/lmng/)], 0.003% [CHS(/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)], 20-40 mM [[Imidazole](/xray-mp-wiki/reagents/additives/imidazole)(/xray-mp-wiki/reagents/additives/imidazole/)] pH 8.0; eluted with 200 mM [[Imidazole](/xray-mp-wiki/reagents/additives/imidazole)(/xray-mp-wiki/reagents/additives/imidazole/)] pH 8.0 |
| Tag cleavage and SEC polishing | [TEV protease(/xray-mp-wiki/reagents/protein-tags/tevp-protease/)] tag cleavage followed by [size-exclusion chromatography(/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)] | Superdex 200 Increase 10/30 GL (GE Healthcare) | 300 mM [[Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride)(/xray-mp-wiki/reagents/additives/sodium-chloride/)], 50 mM [[HEPES](/xray-mp-wiki/reagents/buffers/hepes)(/xray-mp-wiki/reagents/buffers/hepes/)]-Na pH 7.0, 1% [[Glycerol](/xray-mp-wiki/reagents/additives/glycerol)(/xray-mp-wiki/reagents/additives/glycerol/)], 0.03% [[LMNG](/xray-mp-wiki/reagents/detergents/lmng)(/xray-mp-wiki/reagents/detergents/lmng/)], 0.003% [CHS(/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)] + 0.03% [[LMNG](/xray-mp-wiki/reagents/detergents/lmng)(/xray-mp-wiki/reagents/detergents/lmng/)], 0.003% [CHS(/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)] | Eluate concentrated using Amicon Ultra 100K filter; mixed with [TEV(S219V) protease(/xray-mp-wiki/reagents/protein-tags/tevp-protease/)] at 4 C for 16 h to remove GFP-His8 tag; concentrated to 12 mg/mL for crystallization |


## Crystallization

### doi/10.1002##1873-3468.14136

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified NtMATE2 at 12 mg/mL in 300 mM NaCl, 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes)-Na pH 7.0, 1% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng), 0.003% CHS; [[Nicotine](/xray-mp-wiki/reagents/ligands/nicotine)(/xray-mp-wiki/reagents/ligands/nicotine/)] added to 2.5 mM, incubated at 4 C for 10 min; mixed 1:1 with [[Monoolein](/xray-mp-wiki/reagents/lipids/monoolein)(/xray-mp-wiki/reagents/lipids/monoolein/)] (NU-CHEK-PREP) using twin-syringe mixing method |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | LCP crystallization performed in glass sandwich plates; 30 nL LCP mixed with 30 nL reservoir. Two outward-facing conformations (Mol-A and Mol-B) found in asymmetric unit. Initial phases calculated by molecular replacement using [CasMATE (Camelina sativa MATE Transporter)](/xray-mp-wiki/proteins/casmate) (PDB 5XJJ) with PHASER. Rwork/Rfree = 0.265/0.313. Data collected at SPring-8 BL32XU beamline. Final model contains residues 18-493 for Mol-A and 15-493 for Mol-B. |


## Biological / Functional Insights

### Bilobate V-shaped architecture with pseudo-symmetry

The overall NtMATE2 structure has a bilobate V-shape with pseudo-symmetrical assembly of the N- and C-lobes (TM1-6 and TM7-12), consistent with the MATE family architecture. The N- and C-terminal regions form alpha-helices parallel to the membrane on the cytoplasmic surface. The N-terminal region, not modeled in previous structures of AtDTX14 and [CasMATE (Camelina sativa MATE Transporter)](/xray-mp-wiki/proteins/casmate) (PDB 5XJJ), contributes to NtMATE2 stability as N-terminal deletion mutants could not be purified.

### Outward-releasing form (Mol-B) stabilized by unidentified ligand

Mol-B contains an elongated non-water electron density adjacent to N316 in TM8, near E285 in TM7. This density is not present in Mol-A. The average B-factor for Mol-B (93.2) is lower than Mol-A (101.5), suggesting the unidentified ligand stabilizes Mol-B. The site is surrounded by Y288, F289, F320, Y430, and W453, which may participate in substrate recognition via cation-pi interactions similar to those observed for [[Nicotine](/xray-mp-wiki/reagents/ligands/nicotine)(/xray-mp-wiki/reagents/ligands/nicotine/)] in PDB structures 6PV7 and 2YK1.

### Unprecedented TM7 conformational movement

TM7 shows the highest RMSD between Mol-A and Mol-B (1.671 A) among all transmembrane helices. Unlike [CasMATE (Camelina sativa MATE Transporter)](/xray-mp-wiki/proteins/casmate) (PDB 5XJJ) and AtDTX14 where TM7 bends around G255-P257, NtMATE2 TM7 undergoes an overall arrangement change without alpha-helix bending. The conserved Asp in TM10 of [CasMATE (Camelina sativa MATE Transporter)](/xray-mp-wiki/proteins/casmate) (PDB 5XJJ)/AtDTX14 is replaced by Asn403 in NtMATE2, which may interact with E285 via hydrogen bonding instead. Q406 can also hydrogen bond with E285. This suggests a different TM7 conformational transition mechanism in NtMATE2.

### Proton-coupled transport mechanism

NtMATE2 is proposed to transport [[Nicotine](/xray-mp-wiki/reagents/ligands/nicotine)(/xray-mp-wiki/reagents/ligands/nicotine/)] in exchange for protons. The vacuolar pH (~5.1) versus cytoplasmic pH (~7.6) creates a proton gradient. At the near-neutral pH of crystallization (pH 7.5), the conserved E285 on the cavity surface is deprotonated. At the lower pH in the vacuole lumen, E285 is more likely protonated in outward-facing forms, potentially converting NtMATE2 to its inward-open form. The Na+-binding site in the N-lobe did not show sodium or water molecules, though a phosphate ion was observed between TM1 and TM2.

### Rocker switch model with three conformational states

NtMATE2 follows the [rocker switch(/xray-mp-wiki/concepts/rocker-switch-mechanism/)] mechanism of alternating-access transport. The proposed mechanism: NtMATE2 interacts with its substrate ([[Nicotine](/xray-mp-wiki/reagents/ligands/nicotine)(/xray-mp-wiki/reagents/ligands/nicotine/)]) in an inward-facing form, converts to the outward-releasing form (Mol-B) with substrate, releases the substrate into the vacuole, and then changes into the outward-open form (Mol-A). Mol-B is proposed as the stable outward-releasing state. This contrasts with [CasMATE (Camelina sativa MATE Transporter)](/xray-mp-wiki/proteins/casmate) (PDB 5XJJ) and AtDTX14 where the transition involves TM7 bending.


## Cross-References

- [NtMATE1 - Tobacco Nicotine MATE Transporter](/xray-mp-wiki/proteins/ntmate1/) — NtMATE1 is 95% identical to NtMATE2 and also functions as a nicotine transporter in tobacco roots
- [CasMATE (Camelina sativa MATE Transporter)](/xray-mp-wiki/proteins/abc-transporters/casmate/) — CasMATE (PDB 5XJJ, 2.9 A) was used as the search model for molecular replacement; key reference for eukaryotic MATE structural comparisons
- [AtDTX14 - Arabidopsis thaliana MATE Transporter](/xray-mp-wiki/proteins/atdtx14/) — AtDTX14 is another eukaryotic MATE transporter from Arabidopsis; structural comparisons reveal conserved features and NtMATE2-specific differences
- [NtJAT2 - Tobacco Leaf-Specific Nicotine MATE Transporter](/xray-mp-wiki/proteins/ntjat2/) — NtJAT2 is another tobacco nicotine transporter; TM7 sequence identity between NtMATE2 and NtJAT2 is higher than other TM regions
- [Nicotine](/xray-mp-wiki/reagents/ligands/nicotine/) — Nicotine is the physiological substrate of NtMATE2; added at 2.5 mM before LCP crystallization
- [N-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — 2% DDM used for initial membrane solubilization of NtMATE2 from Pichia pastoris
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — 0.03% LMNG used as maintenance detergent during TALON affinity chromatography and SEC polishing
- [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — 0.005% CHS during equilibration and 0.003% during wash/elution for protein stabilization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Monoolein used as the lipidic cubic phase matrix for LCP crystallization (1:1 protein-to-lipid ratio)
- [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) — TALON cobalt affinity resin used for initial His-tag capture of NtMATE2
- [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Superdex 200 Increase 10/30 GL used for final SEC polishing step
- [G418 (Geneticin)](/xray-mp-wiki/reagents/additives/g418/) — G418 (geneticin) used at 50, 100, and 200 ug/mL for selection of Pichia pastoris transformants
- [Pichia Pastoris Expression System](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/) — Pichia pastoris SMD1168 used as the expression host for NtMATE2
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization method used to grow NtMATE2 microcrystals
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Size-exclusion chromatography used for final polishing of NtMATE2
- [Rocker-Switch Mechanism in MFS Transporters](/xray-mp-wiki/concepts/rocker-switch-mechanism/) — NtMATE2 operates via the rocker switch alternating-access mechanism
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — HEPES-Na (pH 7.0 for purification, pH 7.5 for crystallization) used throughout
