---
title: "Human Platelet-Activating Factor Receptor (PAFR)"
created: 2018-05-28
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-018-0068-y]
verified: false
---

# Human Platelet-Activating Factor Receptor (PAFR)

## Overview

The human platelet-activating factor receptor (PAFR) is a class A [G Protein](/xray-mp-wiki/concepts/signaling-receptors/gpcr-g-protein-coupling/)-coupled receptor that responds to platelet-activating factor (PAF), a phospholipid mediator of cell-to-cell communication involved in inflammation, immune responses, and cardiovascular regulation. The first crystal structures of PAFR were determined in complex with the antagonist SR 27417 at 2.8 A resolution (PDB 5ZKP) and the inverse agonist ABT-491 at 2.9 A resolution (PDB 5ZKQ) (Cao et al., 2018). The structures reveal an unusual conformation in the SR 27417-bound state, with the intracellular tips of helices II and IV shifting outward by 13 A and 4 A, respectively, and helix VIII adopting an inward conformation across the helical bundle. Combined with smFRET and functional assays, the structures suggest that the conformational change in the helical bundle is ligand dependent and plays a critical role in PAFR activation.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41594-018-0068-y | 5ZKP | 2.8 A | P 21 21 21 | Human PAFR with ICL3 replaced by residues 2-148 of modified flavodoxin (P2A Y98W), C-terminal truncation (C317-N342 removed), five point mutations (F116Y, N169D, A230D, V234A, D289N), N-terminal HA signal peptide, C-terminal PreScission site and decahistidine/FLAG tag | SR 27417 (antagonist) |
| doi/10.1038##s41594-018-0068-y | 5ZKQ | 2.9 A | P 21 21 21 | Human PAFR with ICL3 replaced by mT4L fusion, C-terminal truncation (C317-N342 removed), five point mutations (F116Y, N169D, A230D, V234A, D289N), N-terminal HA signal peptide, C-terminal PreScission site and decahistidine/FLAG tag | ABT-491 (inverse agonist) |

## Expression and Purification

- **Expression system**: [Sf9](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) insect cells ([Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system)
- **Construct**: Human PAFR with ICL3 replaced by flavodoxin or mT4L fusion, C-terminal truncation (C317-N342), five point mutations (F116Y, N169D, A230D, V234A, D289N), N-terminal HA signal peptide, C-terminal PreScission site and decahistidine/FLAG tag

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) infection of [Sf9](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) cells at MOI 5 for 48 h; 1 uM SR 27417 or ABT-491 added during expression | -- | 10 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 10 mM MgCl2, 20 mM KCl, EDTA-free [protease inhibitor cocktail](/xray-mp-wiki/reagents/additives/protease-inhibitor-cocktail/) + -- | Cells disrupted by hypotonic buffer and Dounce homogenization; extensive washing of membranes by repeated centrifugation |
| Solubilization | Detergent solubilization | -- | 30 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5 mM MgCl2, 10 mM KCl, 7.5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 25 uM ligand (SR 27417 or ABT-491), 1 mg/ml [iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/), EDTA-free [protease inhibitor cocktail](/xray-mp-wiki/reagents/additives/protease-inhibitor-cocktail/) + 0.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% [cholesterol hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Membranes solubilized at 0.5% DDM + 0.1% CHS |
| Affinity purification | [TALON](/xray-mp-wiki/reagents/additives/talon/) [IMAC](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) IMAC resin (Clontech) | Same as solubilization buffer with ligand + 0.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Imidazole removed via PD MiniTrap G-25 column after elution |
| Tag cleavage | [PreScission protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) cleavage (overnight) | -- | Same as solubilization buffer + 0.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Histidine-tagged PreScission protease (30 ul) treated overnight to remove C-terminal His tag |
| Negative purification | Negative [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) purification | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) superflow resin (Qiagen) | Same as solubilization buffer + 0.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Cleaved His tag and PreScission protease removed by passage through Ni-NTA resin |
| Concentration | Concentration by ultrafiltration | -- | Same as solubilization buffer + 0.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | PAFR-flavodoxin concentrated to 30-40 mg/ml; PAFR-mT4L concentrated to 40-45 mg/ml; Vivaspin concentrator with 100 kDa MWCO |


## Crystallization

### doi/10.1038##s41594-018-0068-y

| Parameter | Value |
|---|---|
| Method | [Lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) crystallization |
| Protein sample | PAFR-flavodoxin (for SR 27417 complex) or PAFR-mT4L (for ABT-491 complex), concentrated to 30-45 mg/ml in purification buffer |
| Temperature | 20 C |
| Growth time | 2-3 weeks |
| Cryoprotection | Reservoirs with 32-40% PEG 400; crystals flash-cooled in liquid nitrogen |
| Notes | Protein reconstituted into LCP with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/).
PAFR-SR 27417 (flavodoxin fusion): 30-40 mg/ml, 28-30% PEG 400, 100 mM Na citrate
pH 5.0, 100 mM Na malonate pH 7.0, 100 mM imidazole, no sarcosine. PAFR-ABT-491
(mT4L fusion): 40-45 mg/ml, 30-32% PEG 400, 100 mM Na citrate pH 5.0, 100 mM
Na malonate pH 7.0, 20 mM imidazole, 3% sarcosine. Data merged from 36 crystals
(SR 27417) and 52 crystals (ABT-491) due to radiation damage. |


## Biological / Functional Insights

### First crystal structures of PAFR reveal ligand-dependent conformational changes

The crystal structures of PAFR bound to antagonist SR 27417 (2.8 A) and inverse agonist ABT-491 (2.9 A) are the first reported structures of this receptor. The SR 27417-bound structure shows an unusual conformation where the intracellular tips of helices II and IV shift outward by 13 A and 4 A, respectively, compared to the ABT-491-bound structure, while helix VIII adopts an inward conformation across the helical bundle.

### Unique helix VIII conformation in the SR 27417-bound state

PAFR helix VIII in the SR 27417 complex adopts a conformation not seen in other known GPCR structures. It extends across the helical bundle flanked by ICL1 and ICL2, with its C terminus wedged into a gap between helices II and IV. Residue F300 on the N terminus of helix VIII, together with L304, forms a hydrophobic-packing core with F295(7.55) and L296(7.56) in helix VII. This unique conformation may facilitate G-protein coupling.

### Helices II and IV as key regulators of PAFR activation

smFRET assays confirmed the conformational difference between SR 27417- and ABT-491-bound states. The FRET efficiency for PAFR-SR 27417 was 0.75 vs 0.90 for PAFR-ABT-491, consistent with a longer distance between intracellular tips of helices II and IV in the SR 27417 complex. The agonist PAF-bound receptor showed an FRET efficiency of 0.70, suggesting helices II and IV in the agonist-bound receptor adopt an outward conformation similar to the SR 27417 complex. Mutations F66(2.53)A, F97(3.32)A, and F152(4.60)A decreased PAFR-mediated IP production.

### Lipid receptor structural features

Similarly to other lipid receptors (S1P1, FFAR1, LPA1, CB1), the PAFR ligand-binding pocket is capped by the N terminus and extracellular loops (mainly ECL2). The roof-like structure over the binding pocket may be a general structural feature shared by lipid GPCRs. Unlike most class A GPCRs, PAFR has a valine at position 5.50 (instead of the conserved proline), resulting in a straight helix V without the canonical helical bend.

### PAF binding mode revealed by molecular docking

Molecular docking of PAF into the PAFR-SR 27417 structure revealed that the sn-1 alkyl chain extends into a tunnel formed by aromatic and hydrophobic residues of helices III-VI and ECL2, with its tail squeezing into the lipid bilayer between helices IV and V. The sn-2 and sn-3 groups occupy a subpocket bordered by helices I, II, VI, VII and ECL2. Mutagenesis of residues in the subpocket (W73(2.60)A, Y77(2.64)A, H248(6.51)W, W255(6.58)A, H275(7.35)A, H275(7.35)W) substantially decreased PAF binding.


## Cross-References

- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent (0.5%) used for membrane solubilization and purification
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Stabilizing additive (0.1%) used with DDM in purification buffers
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer (30 mM, pH 7.5) used in purification and crystallization
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Salt (150 mM) included in purification buffer
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Cryoprotectant/stabilizer (7.5%) in purification buffer
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used for LCP crystallization matrix
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for both PAFR complexes
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Protein expressed in Sf9 cells using baculovirus system
- [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Expression host for recombinant PAFR production
- [TALON IMAC Resin](/xray-mp-wiki/reagents/additives/talon/) — Used for affinity purification of PAFR
- [Ni-NTA Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) — Used for negative purification after tag cleavage
- [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) — Added (1 mg/ml) during solubilization
- [GPCR Active Conformation](/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/) — PAFR structures reveal ligand-dependent conformational changes in helical bundle
- [Bovine Rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) — Prototypical class A GPCR for structural comparison
