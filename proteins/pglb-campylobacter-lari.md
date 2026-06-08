---
title: PglB (Campylobacter lari Oligosaccharyltransferase)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3491]
verified: false
---

# PglB (Campylobacter lari Oligosaccharyltransferase)

## Overview

PglB is a single-subunit oligosaccharyltransferase (OST) from the Gram-negative pathogenic bacterium Campylobacter lari, a model system for studying N-linked protein glycosylation. OST catalyzes the transfer of glycans from lipid-linked oligosaccharides (LLOs) onto asparagine side chains within N-X-(S/T) sequons, the first step in protein N-glycosylation. This paper reports the crystal structure of PglB trapped in a ternary complex state, bound simultaneously to an acceptor peptide (DQNATF) and a nonhydrolyzable synthetic LLO analog ((omega ZZZ)-PPC-GlcNAc) at 2.7-A resolution. The structure reveals the critical role of the external loop EL5 in substrate recognition: its N-terminal half binds the LLO while its C-terminal half interacts with the acceptor peptide. The glycan moiety of LLO must thread under EL5 to access the active site. This work defines the chemistry of a key intermediate in the OST reaction mechanism and provides opportunities for glycoengineering through rational design of PglB.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.3491 | 5OGL | 2.7 | P212121 | Sequence-optimized PglB variant from C. lari with mutations K2E, C17A, C30A, A108T, C360L, N535Q, Q536K, K549P, D550N, F553I, N556P, A600P, A602D, T606K, T607Q, V610I, M611T, I619S, F622Y, A624S, V627I, A630N, F663Y, F670Y; cysteineless, removed glycosylation sites | Acceptor peptide DQNATF and synthetic LLO analog (omega ZZZ)-PPC-GlcNAc |

## Expression and Purification

- **Expression system**: Escherichia coli BL21-Gold (DE3)
- **Construct**: Cysteineless PglB optimized for crystallization with multiple lattice-contact mutations. Grown in Terrific Broth with 1% glycerol, induced with 0.1% arabinose at 37 C for 4 h at A600 of 3.0.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell resuspension and lysis | Microfluidizer disruption at 15,000 psi | -- | 25 mM Tris-HCl pH 8.0, 250 mM NaCl + -- | Cells disrupted at 15,000 psi chamber pressure; membranes pelleted by centrifugation at 100,000g for 30 min |
| Solubilization | Detergent solubilization | -- | 25 mM Tris-HCl pH 8.0, 250 mM NaCl, 10% glycerol + 1% N-dodecyl-beta-D-maltopyranoside (DDM, Anatrace) | Membranes solubilized for 1.5 h at 4 C |
| Affinity purification | Immobilized metal affinity chromatography | Ni-NTA Superflow column (Qiagen) | 25 mM Tris-HCl pH 8.0, 250 mM NaCl, 0.016% DDM + 0.016% DDM | Purified on Ni-NTA column |
| Desalting | Desalting | -- | 10 mM MES pH 6.5, 100 mM NaCl, 3% glycerol, 0.016% DDM + 0.016% DDM | Desalted for crystallization experiments |
| Concentration | Ultrafiltration | -- | 10 mM MES pH 6.5, 100 mM NaCl, 3% glycerol, 0.016% DDM + 0.016% DDM | Concentrated to 6 mg/ml using Amicon Ultra-15 concentrator (100 kDa MWCO) |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 10/300 column (GE Healthcare) | 10 mM MES pH 6.5, 100 mM NaCl, 3% glycerol, 0.016% DDM + 0.016% DDM | Concentrated to 12 mg/ml after SEC for crystallization |


## Crystallization

### doi/10.1038##nsmb.3491

| Parameter | Value |
|---|---|
| Method | Not specified in this paper |
| Protein sample | PglB at 12 mg/ml in 10 mM MES pH 6.5, 100 mM NaCl, 3% glycerol, 0.016% DDM, cocrystallized with peptide DQNATF and LLO analog (omega ZZZ)-PPC-GlcNAc |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Crystals diffracted to 2.7-A resolution, space group P212121. SAD or molecular replacement not specified. |


## Biological / Functional Insights

### Dual function of external loop EL5 in substrate recognition

The structure reveals that EL5 has a dual function: the N-terminal half (N-EL5) forms an alpha-helix at the membrane boundary and binds the LLO substrate, while the C-terminal half (C-EL5) pins the acceptor peptide against the periplasmic domain. N-EL5 was previously disordered in the peptide-only structure but adopts a defined conformation upon LLO binding, suggesting that LLO binding induces ordering of this loop. The glycan moiety of LLO must thread under EL5 to access the active site. Enzymatic cleavage of EL5 results in only a slight reduction in activity, indicating the two functions are independent and modular.

### LLO-binding site and pyrophosphate interactions

The polypropenyl tail of LLO reaches approximately halfway across the membrane, embedded in a hydrophobic groove of the transmembrane domain with van der Waals contacts to N-EL5. The pyrophosphate moiety forms a salt bridge with conserved residue R375 and hydrogen bonds with Y293 from N-EL5. The phosphate connected to GlcNAc forms a salt bridge with R375, while the second phosphate (connected to the polypropenyl tail) forms multiple hydrogen bonds. The shortest distance between pyrophosphate oxygens and the catalytic Mn2+ ion is approximately 5 A, with no direct contact. These polar and electrostatic interactions explain why R375 and Y293 are essential for glycosylation activity but not for sequon binding.

### Ternary complex intermediate and conformational change requirement

The distance between the carboxamide nitrogen of the acceptor asparagine and the C1 atom of the reducing-end GlcNAc is approximately 6 A in the ternary complex structure, too long for the glycan transfer reaction. This requires a conformational change during which the LLO must shift toward the peptide, involving repositioning of the pyrophosphate moiety. The DGGK loop imposes steric constraints during this transfer reaction, blocking LLO from further approaching the acceptor asparagine. Molecular dynamics simulations implicate this motif in correctly orienting the carboxamide group of the acceptor asparagine residue.


## Cross-References

- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer (25 mM pH 8.0) for PglB resuspension and purification
- [DDM (N-Dodecyl-beta-D-maltoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent (1% during extraction, 0.016% during purification)
- [MES Buffer](/xray-mp-wiki/reagents/buffers/mes/) — Used at 10 mM pH 6.5 for desalting and SEC buffers
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — 250 mM NaCl in resuspension buffer, 100 mM in purification buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — 10% glycerol in solubilization buffer, 3% in purification buffers
- [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — MgCl2 mentioned in transport assay buffers
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/protein-tags/nickel-nta/) — Used for His-tag affinity purification of PglB
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Superdex 200 SEC used for final purification before crystallization
