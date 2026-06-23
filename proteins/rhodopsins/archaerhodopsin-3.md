---
title: "Archaerhodopsin-3 (AR3)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-20596-0]
verified: false
---

# Archaerhodopsin-3 (AR3)

## Overview

Archaerhodopsin-3 (AR3) is a light-driven proton pump from the archaebacterium Halorubrum sodomense. It has seven transmembrane helices and a single extracellular-facing two-stranded beta-sheet, with [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) covalently bound to Lys226 via a Schiff base linkage. AR3 is particularly suitable for optogenetics due to its faster photocycle kinetics compared to homologs like [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/). Two high-resolution crystal structures have been solved: the light-adapted (LA) ground state (6S6C, 1.1 A) and the dark-adapted (DA) desensitized state (6GUX, 1.3 A). These structures revealed that the DA state permits thermal equilibrium between [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomers, while the LA state favors [All-Trans Retinal](/xray-mp-wiki/reagents/ligands/retinal/), and that internal water network dynamics underpin receptor sensitization.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-020-20596-0 | 6S6C | 1.1 A | not specified | Wild-type AR3 from Halorubrum sodomense, full-length proton pump | All-trans retinal (LA ground state) |
| doi/10.1038##s41467-020-20596-0 | 6GUX | 1.3 A | not specified | Wild-type AR3 from Halorubrum sodomense, full-length proton pump in dark-adapted state | Mixed 13-cis and all-trans retinal (70% cis, 30% trans) |

## Expression and Purification

- **Expression system**: Halorubrum sodomense (wild-type, non-genetically modified)
- **Construct**: Wild-type AR3 purified from native purple membrane

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Sucrose density gradient ultracentrifugation | -- | 4 M [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) for resuspension; 0.1 M [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) for dialysis; distilled water + -- | Cells collected by centrifugation, resuspended in 4 M [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), stirred 2 h, homogenized, dialyzed overnight in 0.1 M [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/). [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) gradient (30-60% w/v) at 110,000 x g for 15 h at 15 C. AR3-rich membrane band collected, [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) removed by overnight dialysis. Final concentration 20 mg/ml, AR3 content 78 +/- 2% w/w. |
| Crystallization | Lipidic cubic phase (LCP) crystallization without detergents | -- | Not applicable + -- | Purification and crystallization performed in absence of detergents. AR3 mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) at 40:60 volume ratio. Crystals grown in 30% [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/), 100 mM [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) pH 5.5, 150 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 150 mM Ca2+ at 20 C. |


## Crystallization

### doi/10.1038##s41467-020-20596-0

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Non-delipidated AR3 at 20 mg/ml mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) at 40:60 volume ratio |
| Temperature | 20 C |
| Growth time | 2-3 days |
| Cryoprotection | Crystals flash-frozen in liquid nitrogen |
| Notes | All crystallization procedures performed under dim light. LA structure from crystals illuminated with white tungsten light for 2 min prior to cryo-freezing. DA structure from crystals not exposed to light. Data collected at Diamond Light Source I24 microfocus beamline. |


## Biological / Functional Insights

### Dark-adapted state enables thermal retinal isomerization equilibrium

The DA state structure (6GUX) reveals both [13-Cis Retinal](/xray-mp-wiki/reagents/ligands/13-cis-retinal/) (70%) and all-trans (30%) [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomers in the binding pocket. QM/MM calculations show the [13-Cis Retinal](/xray-mp-wiki/reagents/ligands/13-cis-retinal/) isomer is energetically favored in the DA state (Delta G = -1.9 kcal/mol), consistent with thermal equilibrium established in the absence of light. In contrast, the LA state strongly favors [All-Trans Retinal](/xray-mp-wiki/reagents/ligands/retinal/) (Delta G = 10.9 kcal/mol), requiring photon absorption for isomerization. The activation energy for interconversion is 4.4 kcal/mol higher in the LA state (21.5 vs 17.1 kcal/mol).

### Internal water network dynamics govern receptor sensitization

Comparison of DA and LA structures reveals subtle changes in the Schiff base electronic environment. In the LA state, the SB nitrogen atom moves 0.5 A, destabilizing a pentagonal H-bond network involving Wat402, Thr99, and Asp95. Wat402 becomes disordered in the LA state, and Asp95 adopts two conformations. W401 shows dual positions in both states (absent in [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) ground state). These water network changes reduce the activation energy for [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) isomerization in the DA state, enabling thermal equilibration between cis and trans isomers.


## Cross-References

- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Closest homolog to AR3 (59% sequence identity); archaerhodopsin-1 (AR1, PDB: 1UAZ) used as molecular replacement search model
- [All-trans retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore covalently bound to conserved Lys226 via Schiff base
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid component of the lipidic cubic phase crystallization matrix
- [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) — Buffer (100 mM, pH 5.5) used in crystallization reservoir
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Salt (150 mM) used in crystallization reservoir
- [Calcium Chloride (CaCl2)](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Calcium (150 mM) used in crystallization reservoir
- [Polyethylene glycol 600 (PEG 600)](/xray-mp-wiki/reagents/additives/peg-600/) — Precipitant (30%) used in crystallization reservoir
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used to grow AR3 crystals at 20 C
- [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) — Referenced in archaerhodopsin-3
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Referenced in archaerhodopsin-3
