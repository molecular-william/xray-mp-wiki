---
title: PsbS from Spinach (Spinacia oleracea)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3068]
verified: false
---

# PsbS from Spinach (Spinacia oleracea)

## Overview

PsbS is a photosystem II protein essential for qE-type non-photochemical quenching (NPQ) in plants. It protects plants from photodamage under excess light conditions by sensing lumenal acidification and triggering thermal dissipation of excess absorbed light energy. The low-pH crystal structures of PsbS from spinach (Spinacia oleracea) revealed that PsbS adopts a unique folding pattern within the light-harvesting-complex (LHC) superfamily and is a noncanonical pigment-binding protein. Unlike other LHCs, PsbS has four transmembrane helices (TM1-TM4) with a compact structure that leaves no internal void space for pigment binding. Both active (low pH) and inactive (neutral pH) PsbS form homodimers in the thylakoid membrane, with activation involving a conformational change associated with altered lumenal intermolecular interactions rather than a dimer-to-monomer transition. The pH-sensing residues are two lumen-exposed glutamates (Glu69 and Glu173 in spinach), and DCCD binding to these residues disrupts lumenal intermolecular hydrogen bonds, inhibiting qE.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.3068 | Not yet assigned (native 1) | 3.10 | P2(1)2(1)2(1) | PsbS from spinach (residues after limited proteolysis removing N-terminal LFKSK) | Hg (derivative), Chl a |
| doi/10.1038##nsmb.3068 | Not yet assigned (native 2) | 2.35 | P2(1)2(1)2(1) | PsbS from spinach (residues after limited proteolysis) | Chl a |
| doi/10.1038##nsmb.3068 | Not yet assigned (DCCD-modified) | 2.70 | P2(1)2(1)2(1) | PsbS from spinach, DCCD-soaked crystal | DCCD, Chl a |

## Expression and Purification

- **Expression system**: Native purification from fresh market spinach
- **Construct**: PsbS selectively precipitated from BBY membranes (photosystem II-enriched thylakoid fragments)
- **Notes**: BBY membranes were solubilized with 0.4% [n-octyl-β-D-thioglucopyranoside](/xray-mp-wiki/reagents/detergents/otg/) (OTG) at pH 6.0. PsbS was selectively precipitated, then solubilized with 2% [n-octyl-β-D-glucopyranoside](/xray-mp-wiki/reagents/detergents/og/) (OG) overnight at 4 °C. The solubilized PsbS was purified by Resource S cation-exchange chromatography in buffer containing 0.4% [n-nonyl-β-D-glucopyranoside](/xray-mp-wiki/reagents/detergents/ng/) (NG), followed by limited proteolysis with subtilisin and [size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) on a Superdex 200 column. The first five residues (LFKSK) were removed by subtilisin treatment.

### Purification Workflow

- **Expression system**: Native (spinach)
- **Expression construct**: PsbS from BBY membranes

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| BBY membrane preparation | Differential centrifugation | — | 20 mM MES pH 6.0, 15 mM NaCl, 0.4 M sucrose | From fresh market spinach |
| Selective precipitation | Detergent solubilization and precipitation | — | 20 mM MES pH 6.0, 15 mM NaCl, 0.4 M sucrose + 0.4% OTG | Solubilization on ice for 10 min, then centrifugation at 40,000g for 40 min |
| Resolubilization | Detergent extraction | — | 20 mM sodium acetate pH 5.0, 20 mM NaCl + 2% OG | Overnight incubation at 4 °C, then centrifugation at 40,000g for 30 min |
| Cation-exchange chromatography | [Ion-exchange chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) | Resource S (GE Healthcare) | 20 mM sodium acetate pH 5.0, 20 mM NaCl + 0.4% NG | Eluted by NaCl gradient |
| Limited proteolysis | [Limited proteolysis](/xray-mp-wiki/methods/purification/limited-proteolysis/) | — |  | Incubation with subtilisin (0.01 mg/ml) at 20 °C for 2 h; removes N-terminal LFKSK |
| Size-exclusion chromatography | [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Superdex 200 (GE Healthcare) | 20 mM sodium acetate pH 5.0, 100 mM NaCl + 0.4% NG |  |

**Final sample**: PsbS at 10 mg/ml in 20 mM sodium acetate pH 5.0, 100 mM NaCl, 0.4% NG


## Crystallization

### doi/10.1038##nsmb.3068

| Parameter | Value |
|---|---|
| Method | [Sitting-drop vapor-diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) |
| Reservoir | 100 mM sodium acetate pH 5.0, 25-28% PEG 300, 1% ethyl acetate |
| Temperature | 20 |
| Cryoprotection | Reservoir solution plus 0.5% NG and 18% glycerol |
| Notes | Crystals of maximal size obtained after 10 d. DCCD-modified crystals obtained by soaking native crystals in 10 mM DCCD for 3 d. Heavy atom derivative by soaking in 10 mM mercury nitrate for 1 d. |


## Biological / Functional Insights

### PsbS is a noncanonical LHC protein without internal pigment binding

PsbS is a noncanonical LHC protein that does not bind internal pigments like other LHCs. TM2 (equivalent to LHCII helix C) and TM4 (unique to PsbS) are positioned too close to the central supercoil to accommodate chlorophylls, neoxanthin, or lutein molecules. The compact structure is stabilized by close interactions of TM2 and TM4 with the central TM1-TM3 supercoil, serving a similar structural role as lutein molecules in LHCII.

### Active and inactive PsbS both form homodimers

Both active (pH 5.0) and inactive (neutral pH) PsbS form homodimers in thylakoid membranes. The dimer interface involves TM2 and TM3 in the transmembrane region, 13 hydrogen bonds plus one salt bridge at the stromal side, and four hydrogen bonds at the lumenal side mediated by Glu173. The dimer has a large interfacial area of over 1,600 A2.

### Activation involves conformational change while maintaining dimeric state

Activation of PsbS by low pH involves a conformational change while maintaining dimeric state. The pH-sensing Glu173 residue is protonated at low pH (active) and deprotonated at neutral pH (inactive), altering lumenal intermolecular hydrogen bonds. DCCD binding to Glu173 induces a rotameric switch that disrupts lumenal hydrogen bonds, producing a looser dimer conformation similar to the neutral pH state.


## Cross-References

- [Non-photochemical Quenching (NPQ) in LHC-II](/xray-mp-wiki/concepts/miscellaneous/non-photochemical-quenching/) — PsbS is essential for qE-type NPQ in plants
- [Spinach Light-Harvesting Complex II (LHC-II)](/xray-mp-wiki/proteins/photosynthesis/spinach-light-harvesting-complex-ii/) — PsbS belongs to the LHC superfamily; structural comparison with LHCII
- [CP29 Light-Harvesting Complex from Spinach](/xray-mp-wiki/proteins/photosynthesis/cp29-spinach/) — Structural comparison with other LHC proteins; gel-filtration standard
- [Photosystem II](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/) — PsbS is a photosystem II protein
