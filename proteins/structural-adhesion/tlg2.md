---
title: Tlg2 (Cryptococcus thermophilum Qa-SNARE Protein)
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.60724]
verified: false
---

# Tlg2 (Cryptococcus thermophilum Qa-SNARE Protein)

## Overview

Tlg2 is a Qa-SNARE protein from the filamentous fungus Cryptococcus thermophilum that functions in membrane trafficking from the endosome to the trans-Golgi network. Tlg2 has a pronounced tendency to form homo-tetramers driven by SNARE motif bundling. When bound to the SM protein [VPS45](/xray-mp-wiki/proteins/vps45), Tlg2 adopts a novel open conformation in which the Habc domain does not pack against the SNARE motif, leaving it free to initiate SNARE complex assembly. [VPS45](/xray-mp-wiki/proteins/vps45) rescues Tlg2 from homo-oligomeric tetramers into stoichiometric 1:1 complexes.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.60724 | 6XMD | 3.88 A | P21221 | C. thermophilum Tlg2 (residues 1-310) cytoplasmic domain in complex with Vps45 | None |
| doi/10.7554##eLife.60724 | 6XM1 | 2.80 A | P212121 | C. thermophilum full-length Tlg2 (residues 1-327) cytoplasmic domain in complex with Vps45 | None |

## Expression and Purification

- **Expression system**: Escherichia coli BL21-Codon Plus (Agilent)
- **Construct**: C. thermophilum Tlg2 (XP_006697074.1 homolog) with N-terminal His7-MBP tags followed by TEV protease cleavage site. Tlg2(1-327) overproduced at 16 C.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Pressure homogenization (Emulsiflex-C5) | -- | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 8.0, 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol) + -- | Tlg2(1-327)-His7-MBP overproduced in BL21-Codon Plus at 16 C |
| Affinity chromatography | Ni-affinity chromatography | His60 Ni Superflow Resin | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 8.0, 50 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + -- | Low salt wash, eluted with 400 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) |
| Anion exchange chromatography | Ion-exchange chromatography | MonoQ 10/100 | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 8.0, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + -- | Gradient from 50 mM to 500 mM NaCl |
| Tag cleavage | Protease digestion (TEV protease) | His60 Ni Superflow (cleaved His7-MBP tags removed) | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 8.0, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 50 mM NaCl + -- | TEV protease cleaved His7-MBP tags overnight at 4 C |
| Size-exclusion chromatography | Size-exclusion chromatography | Not specified | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 8.0, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) + -- | Final purification |


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| SUMO tag cleavage (Tlg2 Habc domain, residues 79-200) | Protease digestion (Ulp1 protease) | His60 Ni Superflow | 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 50 mM NaCl + -- | SUMO tag removed by Ulp1 protease |


## Crystallization

### doi/10.7554##eLife.60724

| Parameter | Value |
|---|---|
| Method | Vapor diffusion with streak seeding |
| Protein sample | Tlg2(1-310)-[VPS45](/xray-mp-wiki/proteins/vps45) complex at 4 mg/ml in 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 8.0, 50 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) |
| Reservoir | 0.2 M potassium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate), 14% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg) 3350, 5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) |
| Temperature | Room temperature |
| Growth time | ~3 days |
| Cryoprotection | Not specified |
| Notes | P21221 crystal form with single complex in asymmetric unit. Streak seeded with Tlg2(1-310)-[VPS45](/xray-mp-wiki/proteins/vps45) crystals. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Tlg2(1-327)-[VPS45](/xray-mp-wiki/proteins/vps45) full-length complex at 4 mg/ml in 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 8.0, 50 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) |
| Reservoir | 0.2 M potassium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate), 14% (w/v) [PEG](/xray-mp-wiki/reagents/additives/peg) 3350, 5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep) |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | P212121 crystal form with two complexes in asymmetric unit. |


## Biological / Functional Insights

### Open conformation mechanism of Qa-SNARE clamping

Tlg2 adopts an open conformation when bound to [VPS45](/xray-mp-wiki/proteins/vps45), with the Habc domain making only a limited contact with the SNARE motif at an approximately 45 degree angle. The linker between Habc and SNARE motif is disordered/unfolded, unlike the Munc18-Stx1 complex where this linker forms a short helix packing against the closed Habc-SNARE motif bundle. This demonstrates that Qa-SNARE clamping is a specialized property of Munc18 rather than a general SM protein property.

### Homo-tetramerization through SNARE motif bundling

Tlg2 has a pronounced tendency to form homo-tetramers through SNARE motif bundling, as demonstrated by size-exclusion chromatography and sedimentation velocity analytical ultracentrifugation (33.8 kDa experimental vs 33.6 kDa expected for tetramer). The Habc domain alone sediments as a monomer. This oligomerization is reversible and [VPS45](/xray-mp-wiki/proteins/vps45) can rescue Tlg2 tetramers into 1:1 complexes.


## Cross-References

- [Vps45 SNARE Protein](/xray-mp-wiki/proteins/structural-adhesion/vps45/) — Cognate SM protein that forms 1:1 complexes with Tlg2; co-crystallized in PDB entries 6XMD and 6XM1
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Primary buffer (25 mM, pH 8.0) used in all purification and crystallization steps
- [Citrate Buffer](/xray-mp-wiki/reagents/buffers/citrate/) — Crystallization buffer component (0.2 M potassium citrate)
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Stabilizing additive at 5% (w/v) used throughout purification and crystallization
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used at 400 mM for Ni-affinity elution and at lower concentrations in tag cleavage buffer
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Used at 150 mM in cell lysis buffer and in anion exchange gradient (50-500 mM)
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Crystallization precipitant (PEG 3350, 14% w/v)
- [BRIL Fusion Protein](/xray-mp-wiki/reagents/additives/bril/) — Related protein stabilization approach used in membrane protein crystallography
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-affinity chromatography used for initial purification of His-tagged Tlg2 constructs
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC used for final purification of Tlg2-Vps45 complexes
