---
title: Vps45 SM Protein (C. thermophilum)
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [sm-protein, membrane-trafficking, xray-crystallography]
sources: [doi/10.7554##eLife.60724]
---

# Vps45 SM Protein (C. thermophilum)

## Overview

Vps45 is a Sec1/Munc18-family (SM) protein from the filamentous fungus Cryptococcus thermophilum that functions in membrane trafficking from the endosome to the trans-Golgi network. Vps45 is a member of the fourth SM protein family and binds the Qa-SNARE Tlg2, holding it in an open conformation with its SNARE motif disengaged from its Habc domain. The domain 3a helical hairpin of Vps45 adopts an unfurled conformation, exposing the presumptive R-SNARE binding site to allow template complex formation. Vps45 prevents Tlg2 from homo-oligomerization by rescuing Tlg2 tetramers into stoichiometric Vps45-Tlg2 complexes.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.60724 | 6XJL | 2.00 A | P212121 | C. thermophilum Vps45 (residues 1-372, with N-terminal His7 tag) | none |
| doi/10.7554##eLife.60724 | 6XMD | 3.88 A | P21221 | C. thermophilum Vps45 in complex with Tlg2(1-310) | none |
| doi/10.7554##eLife.60724 | 6XM1 | 2.80 A | P212121 | C. thermophilum Vps45 in complex with full-length Tlg2 | none |

## Expression and Purification

- **Expression system**: E. coli BL21 Rosetta (individual) or BL21-Codon Plus (co-expression)
- **Construct**: C. thermophilum Vps45 (XP_006692860.1 homolog) with N-terminal His7 tag for individual expression, or C-terminal His7 tag for co-expression with Tlg2

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Emulsiflex-C5 homogenizer | -- | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/)-HCl pH 8.0, 150 mM NaCl, 5 mM beta-mercaptoethanol | Native Vps45 overproduced in BL21 Rosetta grown in LB media |
| Affinity chromatography | Ni-affinity | His60 Ni Superflow Resin | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/)-HCl pH 8.0, 100 mM NaCl, 20 mM imidazole, 5 mM beta-mercaptoethanol | Wash buffer with 20 mM imidazole, eluted with 300 mM imidazole |
| Size-exclusion chromatography | [Size-exclusion chromatography (SEC)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Superdex 200 HR 16/60 | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/)-HCl pH 8.0, 150 mM NaCl, 5 mM DTT | Gel filtration buffer for analytical SEC |

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Emulsiflex-C5 homogenizer | -- | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 8.0, 150 mM NaCl, 5% glycerol, 5 mM beta-mercaptoethanol | Co-expressed Vps45-Tlg2 overproduced in BL21-Codon Plus at 16C |
| Affinity chromatography | Ni-affinity | His60 Ni Superflow Resin | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 8.0, 50 mM NaCl, 400 mM imidazole, 5% glycerol | Low salt wash buffer, eluted with 400 mM imidazole |
| Anion exchange chromatography | MonoQ 10/100 | MonoQ 10/100 | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 8.0, 5% glycerol | Gradient from 50 mM to 500 mM NaCl |
| Size-exclusion chromatography | [Size-exclusion chromatography (SEC)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | not specified | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 8.0, 5% glycerol, 5 mM TCEP | Final purification step |


## Crystallization

### doi/10.7554##eLife.60724

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop, implied) |
| Protein sample | Vps45 monomer (4 mg/ml) |
| Reservoir | 0.2 M potassium [citrate](/xray-mp-wiki/reagents/buffers/citrate/), 14% (w/v) [PEG 3350](/xray-mp-wiki/reagents/additives/peg/), 5 mM TCEP |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Vps45 alone. Space group P212121, 2.0 A resolution. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion with streak seeding |
| Protein sample | Vps45-Tlg2 V306D,F335R mutant (4 mg/ml) |
| Reservoir | 0.2 M potassium [citrate](/xray-mp-wiki/reagents/buffers/citrate/), 14% (w/v) [PEG 3350](/xray-mp-wiki/reagents/additives/peg/), 5 mM TCEP |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Mutant Vps45-V306D,F335R in complex with Tlg2. Space group P21, 5.12 A resolution. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | SeMet-labeled Vps45-Tlg2 L258M,I272M (5 mg/ml) |
| Reservoir | 0.1 M [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 0.2 M NaCl, 10% (v/v) 2-propanol, 5 mM TCEP |
| Temperature | not specified |
| Growth time | ~3 days |
| Notes | Diamond-shaped crystals improved by streak seeding. Used for SAD phasing. |


## Biological / Functional Insights

### Open conformation of Qa-SNARE

Vps45 holds Tlg2 in an open conformation where the Habc domain does not pack against the SNARE motif, leaving it free to initiate SNARE complex assembly. This contrasts with the Munc18-Stx1 complex where the Qa-SNARE is clamped in a closed conformation. The Vps45-Tlg2 structure establishes that SM proteins can engage the N-peptide, Habc domain, and SNARE motif without simultaneously clamping the SNARE shut.

### Unfurled helical hairpin

The domain 3a helical hairpin of Vps45 adopts an unfurled, extended conformation in the Vps45-Tlg2 complex, exposing the R-SNARE binding site. This conformation resembles that seen in Vps33-SNARE complexes and suggests Vps45 is primed to bind an R-SNARE and catalyze SNARE complex assembly.

### Prevention of Tlg2 oligomerization

Vps45 rescues Tlg2 from homo-tetrameric oligomers into 1:1 complexes. Tlg2 has a pronounced tendency to form homo-tetramers driven by SNARE motif bundling. Vps45 captures transiently dissociated Tlg2 monomers through high-affinity N-peptide binding (27 nM for mammalian orthologues) and SNARE motif layer 0-4 binding, preventing off-pathway oligomerization.


## Cross-References

- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used in Vps45 purification
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in Vps45-Tlg2 complex purification
- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — Related protein stabilization tag used in SM protein studies
