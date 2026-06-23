---
title: "Human Complement C5a Receptor 1 (C5aR1)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature25025, doi/10.1038##s41594-018-0067-z]
verified: false
---

# Human Complement C5a Receptor 1 (C5aR1)

## Overview

The human complement C5a receptor 1 (C5aR1, also known as CD88) is a class A G protein-coupled receptor that mediates the pro-inflammatory effects of the anaphylatoxin C5a. It is expressed on cells of myeloid origin and plays a critical role in the complement cascade. C5aR1 has been implicated in inflammatory disorders including sepsis, arthritis, and Alzheimer's disease. Crystal structures of C5aR1 in complex with peptide and non-peptide antagonists revealed both orthosteric and allosteric binding mechanisms, providing a structural framework for drug development.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature25025 | 5O9H | 2.7 | P12_11 | C5aR1 StaR (residues 30-333), thermostabilized with 11 mutations (S85A, I91A, I142A, N146R, L156A, F172A, R232A, A234E, L311E, S317E, N321E), N-terminal 29 residues deleted, C-terminal 17 residues deleted | [NDT9513727](/xray-mp-wiki/reagents/ligands/ndt9513727/) |
| doi/10.1038##s41594-018-0067-z | 6C1Q | 2.9 | P2_1 | [BRIL (Thermostabilized Apocytochrome b562RIL)](/xray-mp-wiki/reagents/protein-tags/bril/)-C5aR chimera (N-terminal [BRIL (Thermostabilized Apocytochrome b562RIL)](/xray-mp-wiki/reagents/protein-tags/bril/) fusion replacing residues 1-29), TEV cleavage site after R330, C-terminal 8xHis tag | PMX53, [NDT9513727](/xray-mp-wiki/reagents/ligands/ndt9513727/) |
| doi/10.1038##s41594-018-0067-z | 6C1R | 2.2 | P2_1 | [BRIL (Thermostabilized Apocytochrome b562RIL)](/xray-mp-wiki/reagents/protein-tags/bril/)-C5aR chimera (N-terminal [BRIL (Thermostabilized Apocytochrome b562RIL)](/xray-mp-wiki/reagents/protein-tags/bril/) fusion replacing residues 1-29), TEV cleavage site after R330, C-terminal 8xHis tag | PMX53, avacopan |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda Sf9 cells using pFastBac baculovirus method
- **Construct**: [BRIL (Thermostabilized Apocytochrome b562RIL)](/xray-mp-wiki/reagents/protein-tags/bril/)-C5aR chimera with N-terminal signal peptide plus [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), TEV cleavage site, C-terminal 8xHis tag
- **Notes**: Ligand ([NDT9513727](/xray-mp-wiki/reagents/ligands/ndt9513727/) or avacopan) added at 100 [NM](/xray-mp-wiki/reagents/detergents/nm/) to cell media during expression

### Purification Workflow

#### Source: doi/10.1038##nature25025


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Transient transfection of HEK293T cells |  |  | cDNA encoding human C5aR1 or C5aR1 StaR construct; cells collected after 48 h |
| Membrane preparation | Homogenization and ultracentrifugation |  | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.4, 1 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) | Homogenized 30 s at max speed, centrifuged at 48,000g for 30 min at 4 C |
| Solubilization | Detergent solubilization |  | 50 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/)-NaOH pH 7.5, 150 mM NaCl, 1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Incubated at 4 C for 1 h; cleared by centrifugation at 16,000g for 15 min |

#### Source: doi/10.1038##s41594-018-0067-z


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Osmotic shock |  | 10 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 ug/ml [Benzamidine](/xray-mp-wiki/reagents/ligands/benzamidine/), 0.2 ug/ml leupeptin, 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) | Sf9 cells lysed by osmotic shock; membrane fractions collected at 25,000g for 30 min at 4 C |
| Solubilization | Detergent solubilization |  | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.8, 750 mM NaCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 150 ug/ml [Benzamidine](/xray-mp-wiki/reagents/ligands/benzamidine/), 0.2 ug/ml leupeptin, 2 mg/ml [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/), 5 U Salt Active Nuclease + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.2% CHS, 0.2% cholate | 2 h at 4 C; all steps in presence of 100 [NM](/xray-mp-wiki/reagents/detergents/nm/) [NDT9513727](/xray-mp-wiki/reagents/ligands/ndt9513727/) (or avacopan) and 100 [NM](/xray-mp-wiki/reagents/detergents/nm/) PMX53 |
| Affinity chromatography (Ni-NTA) | Immobilized metal affinity chromatography | [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 500 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% CHS, 150 ug/ml [Benzamidine](/xray-mp-wiki/reagents/ligands/benzamidine/), 0.2 ug/ml leupeptin, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% CHS | Batch binding for 2 h at 4 C; washed three times |
| Affinity chromatography (anti-Flag M1) | Anti-Flag M1 affinity chromatography | Anti-Flag M1 antibody resin (homemade) | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 100 mM NaCl, 0.01% MNG, 0.001% CHS, 200 ug/ml Flag peptide, 5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) + 0.01% MNG, 0.001% CHS | Detergent exchanged from [DDM](/xray-mp-wiki/reagents/detergents/ddm/) to MNG on the M1 resin; eluted with Flag peptide and [EDTA](/xray-mp-wiki/reagents/additives/edta/) |
| TEV cleavage | Overnight TEV protease digestion |  | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 100 mM NaCl, 0.01% MNG, 0.001% CHS + 0.01% MNG, 0.001% CHS | TEV protease (homemade); 4 C overnight |
| Size exclusion chromatography | Size exclusion chromatography | Superdex 200 Increase (GE Healthcare) | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 100 mM NaCl, 0.01% MNG, 0.001% CHS + 0.01% MNG, 0.001% CHS | Monodisperse receptor obtained; concentrated to 40-50 mg/ml with ligands at 10 uM each |


## Crystallization

### doi/10.1038##nature25025

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | C5aR1 StaR with [NDT9513727](/xray-mp-wiki/reagents/ligands/ndt9513727/) |
| Notes | Two-syringe mixing method; [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) used as lipid; 11 crystals used for data collection |

### doi/10.1038##s41594-018-0067-z

| Parameter | Value |
|---|---|
| Method | Lipidic mesophase (LCP) |
| Protein sample | [BRIL (Thermostabilized Apocytochrome b562RIL)](/xray-mp-wiki/reagents/protein-tags/bril/)-C5aR with PMX53 and [NDT9513727](/xray-mp-wiki/reagents/ligands/ndt9513727/) (or avacopan) |
| Notes | Protein mixed with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/); crystals grown in lipidic mesophase |


## Biological / Functional Insights

### Extra-helical allosteric binding mechanism of NDT9513727

[NDT9513727](/xray-mp-wiki/reagents/ligands/ndt9513727/) binds between transmembrane helices 3, 4, and 5 in an extra-helical pocket within the lipid bilayer. The extended benzodioxolane packs against TM4, the 2-phenyl group interacts between TM3 and TM5 involving Ile124(3.40), Ala128(3.44), and Pro214(5.50), and the [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) core hydrogen bonds to Trp213(5.49). This Trp213 interaction is key for species selectivity.

### Orthosteric binding of PMX53 to C5aR

The cyclic hexapeptide PMX53 binds in the orthosteric site of C5aR, occupying the central binding pocket with its tryptophan residue accommodated by a hydrophobic cage formed by F44(1.39), L92(2.60), I96(2.64), P113(3.29), I116(3.32), and V286(7.39). Polar interactions are mediated by R175(4.64), R178, C188, Y258(6.51), T261(6.54), and D282(7.35), along with ordered water molecules. PMX53 stabilizes the inactive conformation by restraining the I116(3.32) and V286(7.39) activation switch.

### Allosteric action of non-peptide C5aR antagonists

Avacopan and [NDT9513727](/xray-mp-wiki/reagents/ligands/ndt9513727/) bind to the same allosteric site between TM3, TM4, TM5, and TM6, but with different binding poses. Both antagonists form hydrophobic interactions with a conserved 'core triad' of I124(3.40), P214(5.50), and F251(6.44), stabilizing the inactive state of the receptor. Docking studies suggest that other non-peptide antagonists (W54011, CP-447697) also bind to this allosteric site. The hydrogen bond interaction with W213(5.49) is critical for antagonist activity.

### Unique conformation of helix 8

C5aR features a unique reversed orientation of helix 8 that inserts between the cytoplasmic segments of TM1 and TM7, with its C-terminal end pointing to the center of the cytoplasmic surface. This conformation may provide minimal steric hindrance for G protein binding but could sterically block arrestin recruitment, providing a structural basis for the minimal involvement of arrestins in C5aR signaling.

### Water-mediated polar networks in C5aR

An extensive water-mediated polar network exists in the orthosteric site, mediating PMX53 binding. On the cytoplasmic side, a polar network involving ordered water molecules and conserved residues (N55(1.50), D82(2.50), N119(3.35), S123(3.39), W255(6.48), N292(7.45), N296(7.49), Y300(7.53) in the NPxxY motif) helps stabilize the inactive state. A sodium ion coordinated by D82(2.50), N292(7.45), and water molecules was also assigned.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane solubilization
- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in purification and crystallization
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used in cell lysis
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used in final purification steps after exchange from DDM
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for C5aR crystallization
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Final purification step using Superdex 200 Increase
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-NTA and anti-Flag M1 affinity steps used in purification
- [Baculovirus Expression System in Sf9 Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Expression system used for BRIL-C5aR production
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein structure
- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Related protein structure
