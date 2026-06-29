---
title: "Human 5-HT2C Serotonin Receptor"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2018.01.001]
verified: false
---

# Human 5-HT2C Serotonin Receptor

## Overview

The 5-HT2C [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) receptor is a class A G protein-coupled receptor (GPCR) and a validated therapeutic target for anti-obesity medications (e.g., lorcaserin/Belviq), as well as a potential target for depression, schizophrenia, and drug addiction. The 5-HT2C receptor exhibits several RNA-edited isoforms, where the non-edited INI isoform displays high constitutive activity. Crystal structures of the 5-HT2C INI isoform were determined in complex with the polypharmacological agonist [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) (ERG) at 2.7 Å (PDB: 6BQG) and the selective inverse agonist ritanserin (RIT) at 2.8 Å (PDB: 6BQH), revealing the structural basis of GPCR polypharmacology. The structures reveal key differences in ligand binding modes, activation states, and microswitch conformations between the agonist-bound active-like state and the inverse agonist-bound inactive state.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2018.01.001 | 6BQG | 2.7 | unknown | Human 5-HT2C INI isoform with thermostabilizing mutations, expressed in Sf9 insect cells, purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm/)/CHS, crystallized in LCP, complexed with [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) (ERG) | [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) (ERG) — polypharmacological agonist |
| doi/10.1016##j.cell.2018.01.001 | 6BQH | 2.8 | unknown | Human 5-HT2C INI isoform with thermostabilizing mutations, expressed in Sf9 insect cells, purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm/)/CHS, crystallized in LCP, complexed with ritanserin (RIT) | Ritanserin (RIT) — selective inverse agonist |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: Human 5-HT2C INI isoform with thermostabilizing mutations. N-terminal HA signal sequence followed by FLAG tag, 10xHis tag, and TEV protease site.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus infection of Sf9 insect cells | -- | -- + -- | Cells harvested 48 h post-infection |
| Membrane preparation and solubilization | Dounce homogenization and ultracentrifugation | -- | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 50 mM NaCl, 2 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), protease inhibitors + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (n-dodecyl-β-D-maltopyranoside) + 0.2% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) ([Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) hemisuccinate) | Membranes solubilized for 2 h at 4°C |
| TALON IMAC affinity purification | Immobilized metal [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) IMAC resin (Clontech) | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)/0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); elution with 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)/0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Receptor eluted and concentrated |
| TEV protease cleavage and FLAG purification | [TEV](/xray-mp-wiki/reagents/enzymes/tev-protease/) cleavage followed by [FLAG](/xray-mp-wiki/reagents/protein-tags/flag-tag/) [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Anti-[FLAG](/xray-mp-wiki/reagents/protein-tags/flag-tag/) M1 agarose resin (Sigma) | 20 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 500 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)/0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)/0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | [FLAG](/xray-mp-wiki/reagents/protein-tags/flag-tag/) tag cleaved, receptor concentrated to ~30 mg/mL for crystallization |


## Crystallization

### doi/10.1016##j.cell.2018.01.001

| Parameter | Value |
|---|---|
| Method | [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) |
| Protein sample | Purified 5-HT2C at ~30 mg/mL in [DDM](/xray-mp-wiki/reagents/detergents/ddm/)/[CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), reconstituted into [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/)/[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) (9:1) [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) |
| Temperature | 20 |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals harvested and flash-cooled in liquid nitrogen. Data collected at SSRF beamline BL17U1 (Shanghai) or APS GM/CA-CAT. Structure solved by molecular replacement using 5-HT2B receptor (PDB: 4IB4) as search model. |


## Biological / Functional Insights

### Distinct binding modes of ergotamine and ritanserin

[ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) (ERG) and ritanserin (RIT) bind to 5-HT2C with fundamentally different poses. ERG adopts a shallower binding pose within the TM helical bundle with its ergoline core sandwiched between helices III and VI, forming a salt bridge with D134^3.32. Its terminal benzyl moiety extends toward the extracellular loops. In contrast, RIT binds deeper in the receptor, with one of its 4-fluorophenyl groups forming tight π-π stacking interactions with W324^6.48 (the 'toggle switch'), I142^3.40, and F320^6.44 of the P-I-F motif. RIT's thiazolopyrimidine group extends toward helices II and VII. The deeper binding pose of RIT effectively prevents the conformational changes of key activation microswitches, stabilizing the inactive state and producing inverse agonism.

### Structural basis for RIT's 5-HT2 selectivity

Ritanserin shows selectivity for 5-HT2 receptors over other aminergic GPCRs. Key determinants include G218^5.42 and V354^7.39, which are exclusive to 5-HT2 receptors. The second 4-fluorophenyl group of RIT 'pushes' against the backbone of helix V at G218^5.42. Mutation G218A^5.42 attenuates RIT binding affinity more than 10-fold but only has modest effect on ERG affinity. W324^6.48 is a major determinant of RIT's binding mode, and mutations W324F^6.48 and W324Y^6.48 (preserving aromatic character) had substantially less effect on RIT binding compared to alanine substitution.

### P-I-F motif and toggle switch in inverse agonism

The P-I-F motif (P^5.50-I^3.40-F^6.44) and W^6.48 toggle switch are critical for RIT's inverse agonist activity. Mutations of W324^6.48 and F320^6.44 selectively abolish RIT's Gαq inverse agonism without affecting β-arrestin2 inverse agonist activity. The I142A^3.40 mutation also selectively abolishes RIT's Gαq inverse agonism, and I142F^3.40 transforms RIT into a Gαq partial agonist. These results support a model whereby RIT's 4-fluorophenyl moiety stabilizes an inactive state via interference with the toggle switch and trigger motif, and that these microswitch residues are critical for the Gαq activation process at 5-HT2C.

### Ergotamine polypharmacology across the aminergic GPCRome

ERG shows appreciable affinity (Ki < 10 µM) for nearly 70% of all human aminergic GPCRs with low or sub-nanomolar affinity for 15 receptors. The ergoline core is recognized by nine key residues across helices III, V, VI, and VII, eight of which have specific conserved amino acid properties. The cyclic tripeptide and benzyl substituents display only non-specific side-chain van der Waals contacts, tolerating high amino acid diversity. The conservation of a small aliphatic residue at the EL2 position (L209 in 5-HT2C) is critical for ERG binding across all receptors showing high ERG affinity.


## Cross-References

- [Human 5-HT2A Receptor](/xray-mp-wiki/proteins/gpcr/5ht2a-receptor/) — Closely related 5-HT2 family member; off-target for 5-HT2C agonists causing hallucinations
- [Human 5-HT2B Receptor](/xray-mp-wiki/proteins/gpcr/5ht2b-receptor/) — Closely related 5-HT2 family member; ERG co-crystal structure (PDB: 4IB4) used as MR model
- [Ergotamine](/xray-mp-wiki/reagents/ligands/ergotamine/) — Polypharmacological agonist co-crystallized with 5-HT2C (PDB: 6BQG)
- [Ritanserin](/xray-mp-wiki/reagents/ligands/ritanserin/) — Selective inverse agonist co-crystallized with 5-HT2C (PDB: 6BQH)
- [Serotonin (5-Hydroxytryptamine)](/xray-mp-wiki/reagents/ligands/serotonin/) — Endogenous ligand for 5-HT2C receptor
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for membrane solubilization and purification
- [Cholesterol Hemisuccinate (CHS)](/xray-mp-wiki/reagents/lipids/chs/) — Lipid additive for receptor stabilization during purification
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipidic cubic phase (LCP) host lipid for crystallization
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein mentioned in the study
