---
title: PglB (Campylobacter lari Oligosaccharyltransferase)
created: 2026-06-08
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10151, doi/10.1038##nsmb.3491, doi/10.1038##s41598-018-34534-0]
verified: false
---

# PglB (Campylobacter lari Oligosaccharyltransferase)

## Overview

PglB is a single-subunit oligosaccharyltransferase (OST) from the Gram-negative pathogenic bacterium Campylobacter lari, a model system for studying N-linked protein glycosylation. OST catalyzes the transfer of glycans from lipid-linked oligosaccharides (LLOs) onto asparagine side chains within N-X-(S/T) sequons, the first step in protein N-glycosylation. The first X-ray structure of a bacterial OST was determined for PglB at 3.4 A resolution (Nature 2011), revealing a 13-transmembrane-helix architecture with a C-terminal periplasmic domain. A subsequent higher-resolution structure (NSMB 2017) trapped PglB in a ternary complex bound simultaneously to an acceptor peptide (DQNATF) and a nonhydrolyzable synthetic LLO analog ((omega ZZZ)-PPC-GlcNAc) at 2.7 A resolution, revealing the critical role of external loop EL5 in substrate recognition. This work defines the chemistry of a key intermediate in the OST reaction mechanism and provides opportunities for glycoengineering through rational design of PglB. A subsequent structure (Sci Rep 2018) captured PglB bound to a reactive LLO analog and an inhibitory Dab-containing peptide, revealing a conformation closer to the transition state with the substrates ~3.4 A apart and direct coordination of the LLO pyrophosphate by the catalytic Mn2+ ion, identifying D56 as a key residue in the hydrogen bonding network.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature10151 | 3RCE | 3.4 | P212121 | Full-length PglB from C. lari with C-terminal His tag | Acceptor peptide DQNATF |
| doi/10.1038##nsmb.3491 | 5OGL | 2.7 | P212121 | Sequence-optimized PglB variant from C. lari with mutations K2E, C17A, C30A, A108T, C360L, N535Q, Q536K, K549P, D550N, F553I, N556P, A600P, A602D, T606K, T607Q, V610I, M611T, I619S, F622Y, A624S, V627I, A630N, F663Y, F670Y; cysteineless, removed glycosylation sites | Acceptor peptide DQNATF and synthetic LLO analog (omega ZZZ)-PPC-GlcNAc |
| doi/10.1038##s41598-018-34534-0 |  | 3.4 | P212121 | Cysteineless PglB variant from C. lari (sequence optimized, same construct as 5OGL) | Reactive LLO analog (nerylneryl-PP-GlcNAc) and inhibitory Dab-containing peptide Ac-DQ(Dab)ATF(p-NO2)-NH2 |

## Expression and Purification

- **Expression system**: Escherichia coli BL21-Gold (DE3)
- **Construct**: Cysteineless PglB optimized for crystallization with multiple lattice-contact mutations. Grown in Terrific Broth with 1% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), induced with 0.1% arabinose at 37 C for 4 h at A600 of 3.0.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell resuspension and lysis | Microfluidizer disruption at 15,000 psi | -- | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 250 mM NaCl + -- | Cells disrupted at 15,000 psi chamber pressure; membranes pelleted by centrifugation at 100,000g for 30 min |
| Solubilization | Detergent solubilization | -- | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 250 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + 1% N-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm), Anatrace) | Membranes solubilized for 1.5 h at 4 C |
| Affinity purification | Immobilized metal affinity chromatography | Ni-NTA Superflow column (Qiagen) | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 250 mM NaCl, 0.016% [DDM](/xray-mp-wiki/reagents/detergents/ddm) + 0.016% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Purified on Ni-NTA column |
| Desalting | Desalting | -- | 10 mM [MES](/xray-mp-wiki/reagents/buffers/mes) pH 6.5, 100 mM NaCl, 3% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.016% [DDM](/xray-mp-wiki/reagents/detergents/ddm) + 0.016% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Desalted for crystallization experiments |
| Concentration | Ultrafiltration | -- | 10 mM [MES](/xray-mp-wiki/reagents/buffers/mes) pH 6.5, 100 mM NaCl, 3% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.016% [DDM](/xray-mp-wiki/reagents/detergents/ddm) + 0.016% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Concentrated to 6 mg/ml using Amicon Ultra-15 concentrator (100 kDa MWCO) |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 10/300 column (GE Healthcare) | 10 mM [MES](/xray-mp-wiki/reagents/buffers/mes) pH 6.5, 100 mM NaCl, 3% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.016% [DDM](/xray-mp-wiki/reagents/detergents/ddm) + 0.016% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Concentrated to 12 mg/ml after SEC for crystallization |


## Crystallization

### doi/10.1038##nature10151

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | PglB at ~5 mg/ml in 10 mM MES pH 6.5, 100 mM NaCl, 0.02% DDM, cocrystallized with acceptor peptide DQNATF |
| Reservoir | 0.1 M MES pH 6.5, 0.2 M NaCl, 30% PEG 400 |
| Temperature | 20 C |
| Growth time | Not specified |
| Notes | Crystals diffracted to 3.4 A resolution, space group P212121. SAD phasing using selenomethionine derivative. R_work = 23.8%, R_free = 27.1%. |

### doi/10.1038##nsmb.3491

| Parameter | Value |
|---|---|
| Method | Not specified in this paper |
| Protein sample | PglB at 12 mg/ml in 10 mM [MES](/xray-mp-wiki/reagents/buffers/mes) pH 6.5, 100 mM NaCl, 3% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.016% [DDM](/xray-mp-wiki/reagents/detergents/ddm), cocrystallized with peptide DQNATF and LLO analog (omega ZZZ)-PPC-GlcNAc |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Crystals diffracted to 2.7-A resolution, space group P212121. SAD or molecular replacement not specified. |

### doi/10.1038##s41598-018-34534-0

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | PglB at 12 mg/ml with 0.75 mM Ac-DQ(Dab)ATF(p-NO2)-NH2, 1.5 mM nerylneryl-PP-GlcNAc, 2 mM MnCl2 |
| Reservoir | 100 mM [Glycine Buffer](/xray-mp-wiki/reagents/buffers/glycine) pH 9.4, 50-200 mM [Magnesium Acetate](/xray-mp-wiki/reagents/additives/magnesium-acetate), 27-31% [PEG400](/xray-mp-wiki/reagents/additives/peg-400) |
| Mixing ratio | 2:1 protein-to-reservoir |
| Temperature | 20 |
| Growth time | 10-14 days to appear, 3-4 weeks to full size |
| Cryoprotection | Stepwise addition of PEG400 to 30% final, flash frozen in liquid N2 |
| Notes | Crystals diffracted to 3.4-A resolution, space group P212121. Data collected at SLS X06SA beamline at 1.000 A. R_work = 0.249, R_free = 0.283. PDB ID not available in raw text. |


## Biological / Functional Insights

### First structure of a bacterial oligosaccharyltransferase

The 3.4 A X-ray structure of PglB from C. lari represents the first three-dimensional structure of a bacterial OST. PglB has 13 transmembrane helices and a C-terminal periplasmic globular domain. The structure reveals the architecture of the sequon-binding pocket and the catalytic site containing a bound Mn2+ ion coordinated by D56 and E319, with the catalytic mechanism involving direct SN2 attack of the asparagine side chain on the lipid-linked oligosaccharide.

### Dual function of external loop EL5 in substrate recognition (NSMB 2017)

The ternary complex structure reveals that EL5 has a dual function: the N-terminal half (N-EL5) forms an alpha-helix at the membrane boundary and binds the LLO substrate, while the C-terminal half (C-EL5) pins the acceptor peptide against the periplasmic domain. N-EL5 was previously disordered in the peptide-only structure but adopts a defined conformation upon LLO binding, suggesting that LLO binding induces ordering of this loop.

### LLO-binding site and pyrophosphate interactions (NSMB 2017)

The polypropenyl tail of LLO reaches approximately halfway across the membrane, embedded in a hydrophobic groove of the transmembrane domain. The pyrophosphate moiety forms a salt bridge with conserved residue R375 and hydrogen bonds with Y293 from N-EL5. The shortest distance between pyrophosphate oxygens and the catalytic Mn2+ ion is approximately 5 A, with no direct contact.

### Ternary complex intermediate and conformational change requirement (NSMB 2017)

The distance between the carboxamide nitrogen of the acceptor asparagine and the C1 atom of the reducing-end GlcNAc is approximately 6 A in the ternary complex structure, too long for the glycan transfer reaction. This requires a conformational change during which the LLO must shift toward the peptide. The DGGK loop imposes steric constraints during this transfer reaction.

### Transition-state-like ternary complex with reactive LLO (Sci Rep 2018)

The X-ray structure of PglB bound to a reactive LLO analog (nerylneryl-PP-GlcNAc) and an inhibitory Dab-containing peptide captured a conformation closer to the transition state of the glycosylation reaction. The distance between C-1 of GlcNAc and the -NH2 group of Dab is ~3.4 A, compared to ~6 A in the previous structure with non-hydrolyzable LLO. The pyrophosphate group of LLO directly coordinates the catalytic Mn2+ ion at a distance of ~4 A, providing direct evidence that the metal stabilizes the pyrophosphate leaving group. Residue D56 mediates a hydrogen bonding network between the reducing-end GlcNAc, the acceptor peptide, and Mn2+.

### Role of Mn2+ in activating the glycosidic oxygen (Sci Rep 2018)

The Mn2+ ion coordinates the glycosidic oxygen of LLO rather than the negatively charged phosphate oxygens, suggesting the metal may directly activate the glycosidic oxygen during the reaction by generating a reactive electrophile. This mechanism could compensate for the poor nucleophilicity of the carboxamide group of the acceptor asparagine, potentially allowing glycan transfer without amide activation.


## Cross-References

- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer (25 mM pH 8.0) for PglB resuspension and purification
- [DDM (N-Dodecyl-beta-D-maltoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent (1% during extraction, 0.016% during purification)
- [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) — Used at 10 mM pH 6.5 for desalting and SEC buffers
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — 250 mM NaCl in resuspension buffer, 100 mM in purification buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — 10% glycerol in solubilization buffer, 3% in purification buffers
- [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — MgCl2 mentioned in transport assay buffers
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/protein-tags/nickel-nta/) — Used for His-tag affinity purification of PglB
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Superdex 200 SEC used for final purification before crystallization
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) — Buffer component in purification or crystallization
