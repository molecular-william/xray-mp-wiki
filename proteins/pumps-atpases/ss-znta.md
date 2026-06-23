---
title: SsZntA (Shigella sonnei Zn2+-ATPase)
created: 2026-06-09
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1107##S2052252515008969]
verified: false
---

# SsZntA (Shigella sonnei Zn2+-ATPase)

## Overview

SsZntA is a Zn2+-ATPase from Shigella sonnei, a P-type ATPase that functions
as a heavy metal transporter. It belongs to the P1B-type ATPase subfamily that
exports heavy metals such as Zn2+, Cd2+, and Pb2+ from the cytoplasm. The protein
was used as a model system for testing [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) (SFX)
at the LCLS XFEL as a method for ligand screening with P-type ATPases. Microcrystals
of SsZntA bound to the inhibitor aluminium tetrafluoride (AlF4-) were grown by
batch crystallization and diffracted to ~4 A resolution at the LCLS XFEL. However,
only 55 of ~280,000 collected diffraction images could be indexed due to the long
c axis of 320 A, preventing successful phasing by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1107##S2052252515008969 | -- | 4.0 | P422 | Shigella sonnei Zn2+-ATPase (SsZntA) expressed in E. coli C41 cells,
purified by Ni2+-NTA and gel filtration, crystallized with AlF4- inhibitor | AlF4- |

## Expression and Purification

- **Expression system**: Escherichia coli C41 cells
- **Construct**: SsZntA from Shigella sonnei expressed with 1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 20 C
- **Notes**: Cells resuspended in 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.6, 200 mM KCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM BME; lysed with high-pressure homogenizer

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Differential centrifugation | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.6, 200 mM KCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM BME, 1 mM MgCl2 + -- | Membranes isolated by ultracentrifugation at 250,000g at 4 C for 5 h |
| Solubilization | Detergent solubilization | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.6, 200 mM KCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM BME, 1 mM MgCl2 + 1% (w/v) [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) | Solubilization for 1 h at 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (IMAC) | Ni2+-NTA | Buffer D (20 mM MOPS-KOH pH 6.8, 80 mM KCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM BME, 1 mM MgCl2, 0.15 mg/ml [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/)) + [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) | Solid KCl and [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) added to final concentrations of 500 and 50 mM before loading |
| Gel filtration | Size-exclusion chromatography | Superose 6 10/300 GL | Buffer D + [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) | Purified protein concentrated to 8 mg/ml |


## Crystallization

### doi/10.1107##S2052252515008969

| Parameter | Value |
|---|---|
| Method | Batch crystallization |
| Protein sample | 8 mg/ml SsZntA in buffer D, supplemented with 2 mM AlF4-, 2 mM [EGTA](/xray-mp-wiki/reagents/additives/egta/), 10 uM N,N,N',N'-tetrakis-2-pyridylmethyl-ethylenediamine, 72x CMC [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) |
| Reservoir | 100 mM MOPS pH 6.8, 0.5 M lithium acetate, 15% [PEG](/xray-mp-wiki/reagents/additives/peg/) 2K MME, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 3% [tert-Butanol](/xray-mp-wiki/reagents/additives/tert-butanol/), 5% D-[Sorbitol](/xray-mp-wiki/reagents/additives/sorbitol/), 5 mM BME |
| Temperature | 19 |
| Growth time | 2 days |
| Cryoprotection | Not specified |
| Notes | Rod-shaped microcrystals ~5 um in length, grown in clusters surrounded by amorphous precipitate. Suspension passed through 400 um syringe needle to homogenize before SFX injection. SFX data collected at LCLS, 6 keV, 120 Hz repetition rate using CSPAD detector. Only 0.3% indexing rate due to long c axis. |


## Biological / Functional Insights

### SFX feasibility for recombinant heavy metal P-type ATPase

SsZntA served as a model for testing SFX with recombinantly expressed P-type ATPase microcrystals. Despite the very low indexing rate (0.3%), the microcrystals diffracted to ~4 A resolution, demonstrating that SFX is feasible for bacterial P-type ATPase ligand complexes. However, the long c axis of 320 A in the P422 space group remains a challenge for SFX data processing with CrystFEL.


## Cross-References

- [P-type ATPase Family](/xray-mp-wiki/concepts/p-type-atpase/) — SsZntA belongs to the P1B-type (heavy metal transporting) ATPase subfamily
- [Serial Femtosecond Crystallography (SFX)](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — SFX at LCLS XFEL used for structure determination attempt
- [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) — SERCA1a is a related P-type ATPase studied in the same SFX ligand screening project
- [sCoaT (Co2+/Zn2+-transporting PIB-4-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/sulfitobacter-scoat/) — Related PIB-ATPase; sCoaT structures used SsZntA as MR search model
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [EGTA](/xray-mp-wiki/reagents/additives/egta/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [IPTG](/xray-mp-wiki/reagents/additives/iptg/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
