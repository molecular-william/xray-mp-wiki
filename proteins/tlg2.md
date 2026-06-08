---
title: 
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, transporter]
sources: [doi/10.7554##eLife.60724]
verified: false
---

# 

## Overview

 is a Qa-SNARE protein from the filamentous fungus Cryptococcus thermophilum that functions in membrane trafficking from the endosome to the trans-Golgi network. [Tlg2(/xray-mp-wiki/proteins/tlg2/) has a pronounced tendency to form homo- tetramers driven by SNARE motif bundling. When bound to the SM protein , [Tlg2(/xray-mp-wiki/proteins/tlg2/) adopts a novel open conformation in which the Habc domain does not pack against the SNARE motif, leaving it free to initiate SNARE complex assembly.  rescues [Tlg2(/xray-mp-wiki/proteins/tlg2/) from homo-oligomeric tetramers into stoichiometric 1:1 complexes. [Tlg2](/xray-mp-wiki/proteins/tlg2/) and its cognate SNAREs (Snc2, Vti1, Tlg1) and the GARP tethering complex function in endosome-to-TGN trafficking.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.60724 | 6XMD | 3.88 A | P21221 | C. thermophilum (1-310) in complex with [Vps45(/xray-mp-wiki/proteins/vps45/) | none |
| doi/10.7554##eLife.60724 | 6XM1 | 2.80 A | P212121 | C. thermophilum  full-length cytoplasmic domain in complex with [Vps45(/xray-mp-wiki/proteins/vps45/) | none |

## Expression and Purification

- **Expression system**: E. coli BL21-Codon Plus (Agilent)
- **Construct**: C. thermophilum [Tlg2](/xray-mp-wiki/proteins/tlg2/) (XP_006697074.1 homolog) with N-terminal His7-MBP tags followed by TEV protease cleavage site

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Emulsiflex-C5 homogenizer | -- | 25 mM  pH 8.0, 150 mM NaCl, 5% [glycerol(/xray-mp-wiki/reagents/additives/glycerol/), 5 mM beta-mercaptoethanol | MBP-[Tlg2](/xray-mp-wiki/proteins/tlg2/)(1-327) overproduced in BL21-Codon Plus at 16C |
| [Affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-affinity | His60 Ni Superflow Resin | 25 mM  pH 8.0, 50 mM NaCl, 400 mM [imidazole(/xray-mp-wiki/reagents/additives/imidazole/), 5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/) | Low salt wash, eluted with 400 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Anion exchange chromatography | MonoQ 10/100 | MonoQ 10/100 | 25 mM  pH 8.0, 5% [glycerol(/xray-mp-wiki/reagents/additives/glycerol/) | Gradient from 50 mM to 500 mM NaCl |
| Tag cleavage | TEV protease cleavage | His60 Ni Superflow (cleaved tags removed) | 20 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 50 mM NaCl | TEV protease cleaved His7-MBP tags overnight at 4C |
| [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | not specified | 25 mM  pH 8.0, 5% [glycerol(/xray-mp-wiki/reagents/additives/glycerol/), 5 mM TCEP | Final purification |


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Tag cleavage (SUMO-[Tlg2](/xray-mp-wiki/proteins/tlg2/)(79-200) Habc domain) | Ulp1 protease cleavage | His60 Ni Superflow | 20 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 50 mM NaCl | SUMO tag removed by Ulp1 protease |


## Crystallization

### doi/10.7554##eLife.60724

| Parameter | Value |
|---|---|
| Method | Vapor diffusion with streak seeding |
| Protein sample | -[Tlg2(/xray-mp-wiki/proteins/tlg2/)(1-310) complex (4 mg/ml) |
| Reservoir | 0.2 M potassium , 14% (w/v) [PEG(/xray-mp-wiki/reagents/additives/peg/) 3350, 5 mM TCEP |
| Temperature | not specified |
| Growth time | ~3 days |
| Notes | P21221 crystal form with single complex in asymmetric unit. Streak seeded with -[Tlg2(/xray-mp-wiki/proteins/tlg2/) crystals. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | -[Tlg2(/xray-mp-wiki/proteins/tlg2/) full-length complex (4 mg/ml) |
| Reservoir | 0.2 M potassium , 14% (w/v) [PEG(/xray-mp-wiki/reagents/additives/peg/) 3350, 5 mM TCEP |
| Temperature | not specified |
| Growth time | not specified |
| Notes | P212121 crystal form with two complexes in asymmetric unit. |


## Biological / Functional Insights

### Open conformation mechanism

 adopts an open conformation when bound to [Vps45(/xray-mp-wiki/proteins/vps45/), with the Habc domain making only a limited contact with the SNARE motif at an approximately 45 degree angle. The linker between Habc and SNARE motif is disordered/unfolded, unlike the Munc18-Stx1 complex where this linker forms a short helix packing against the closed Habc-SNARE motif bundle. This demonstrates that Qa-SNARE clamping is a specialized property of Munc18 rather than a general SM protein property.

### Homo-tetramerization

 has a pronounced tendency to form homo-tetramers through SNARE motif bundling, as demonstrated by [size-exclusion chromatography(/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) and sedimentation velocity AUC (33.8 kDa experimental vs 33.6 kDa expected for tetramer). The Habc domain alone sediments as a monomer. This oligomerization is reversible and  can rescue [Tlg2(/xray-mp-wiki/proteins/tlg2/) tetramers into 1:1 complexes.


## Cross-References

- [Size-Exclusion Chromatography (SEC)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC used for final purification of Tlg2-Vps45 complexes
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer component (25 mM, pH 8.0) in purification and crystallization
- [Citrate Buffer](/xray-mp-wiki/reagents/buffers/citrate/) — Crystallization buffer (0.2 M potassium citrate)
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — Crystallization precipitant (PEG 3350)
- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — Related stabilization approach for membrane protein domains
- [SUMO Tag](/xray-mp-wiki/reagents/protein-tags/sumo/) — Used for Tlg2 Habc domain purification (SUMO-Tlg2(79-200))
- [TEV Protease](/xray-mp-wiki/reagents/enzymes/tevp-protease/) — Used for cleaving His7-MBP tags from Tlg2 constructs
