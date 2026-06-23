---
title: "Angiotensin II Type 2 Receptor"
created: 2026-05-29
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2019.12.003, doi/10.1038##nature22035, doi/10.1038##s41594-018-0079-8]
verified: false
---

# Angiotensin II Type 2 Receptor

## Overview

The [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) type 2 receptor (AT2R) is a class A [G Protein](/xray-mp-wiki/concepts/signaling-receptors/g-protein/)-coupled receptor that counteracts many of the physiological effects of [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) mediated by [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/). AT2R is involved in blood pressure regulation, vasodilation, sodium excretion, and anti-proliferative signaling. Unlike [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/), AT2R does not signal through G proteins or [Beta-Arrestin](/xray-mp-wiki/concepts/signaling-receptors/beta-arrestin/) in a conventional manner and requires additional effector proteins such as ATIP and SHP-1 for signal transduction. Crystal structures of AT2R reveal an active-like conformation of the 7TM bundle with a non-canonical helix VIII position that sterically blocks G protein/beta-arrestin recruitment.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2019.12.003 | 6JOD | 3.2 | C2221 | AT2R-mbIIGN-term; C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) at residue 368; N-terminal HA signal sequence, FLAG tag, TEV cleavage site; C-terminal His8 tag; complex with G-protein mbIIGN-term fragment and Fab4A03 antibody fragment | [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) |
| doi/10.1038##nature22035 | 5UNF | 2.8 | P212121 | BRIL-AT2R fusion; N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/): residues 1-34; C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/): residues 336-363; N-terminal BRIL (apocytochrome b562RIL) fused via 4-residue linker (Gly-Ser-Gly-Ser); N-terminal HA signal sequence, FLAG tag, 10x His tag (cleaved), TEV cleavage site; complex with Cpd 1 | Cpd 1 ([Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)-selective ligand) |
| doi/10.1038##nature22035 | 5UNG | 2.8 | C2 | BRIL-AT2R fusion; N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/): residues 1-34; C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/): residues 336-363; N-terminal BRIL (apocytochrome b562RIL) fused via 4-residue linker (Gly-Ser-Gly-Ser); N-terminal HA signal sequence, FLAG tag, 10x His tag (cleaved), TEV cleavage site; complex with Cpd 1 | Cpd 1 ([Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)-selective ligand) |
| doi/10.1038##nature22035 | 5UNH | 2.9 | P21 | BRIL-AT2R fusion; N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/): residues 1-34; C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/): residues 336-363; N-terminal BRIL (apocytochrome b562RIL) fused via 4-residue linker (Gly-Ser-Gly-Ser); N-terminal HA signal sequence, FLAG tag, 10x His tag (cleaved), TEV cleavage site; complex with Cpd 2 (AT1R/AT2R dual ligand) | Cpd 2 (AT1R/AT2R dual ligand) |
| doi/10.1038##s41594-018-0079-8 | 5XJM | 3.2 | P2(1)2(1)2 | BRIL-AT2R fusion; BRIL replaces ICL3; N-terminal HA signal sequence, FLAG tag, TEV cleavage site; C-terminal His6 tag; complex with [S1I8](/xray-mp-wiki/reagents/ligands/s1i8/) and [Fab4A03](/xray-mp-wiki/reagents/antibodies/fab4a03/) antibody fragment | [S1I8](/xray-mp-wiki/reagents/ligands/s1i8/) |

## Expression and Purification

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) ([Bac-to-Bac System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system)
- **Construct**: BRIL-AT2R chimera; AT2R residues 1-34 and 336-363 truncated; N-terminal BRIL (apocytochrome b562RIL, Met7Trp, His102Ile, Arg106L) fused via 4-residue linker (Gly-Ser-Gly-Ser); N-terminal HA signal sequence, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10x His tag, TEV cleavage site
- **Notes**: AT2R gene sequence (UNIPROT P50052) codon-optimized for insect cell expression, cloned into [pFastBac1](/xray-mp-wiki/reagents/vectors/pfastbac1/) vector. [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) infected with [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/), membranes prepared by hypotonic lysis and high osmotic wash.


### Purification Workflow

#### Source: doi/10.1016##j.str.2019.12.003

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)
- **Expression construct**: AT2R-mbIIGN-term; N-terminal HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) site; C-terminal [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) site, His8 tag; C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) at residue 368
- **Tag info**: [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), His8 (C-terminal, cleaved by [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/))

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane isolation |  | 10 mM [HEPES (HEPES Buffer)](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 20 mM KCl, 10 mM [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/), protease inhibitor cocktail | [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) harvested by centrifugation, flash-frozen at -80 C, lysed under hypotonic conditions, membranes collected by ultracentrifugation at 100,000 x g, washed twice with high osmotic buffer (5 mM [HEPES (HEPES Buffer)](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 0.5 M [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10 mM KCl, 5 mM [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/)) |
| Solubilization | Detergent solubilization |  | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 800 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1.0% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.2% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Membranes solubilized with [DDM](/xray-mp-wiki/reagents/detergents/ddm/) and [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) supplemented with [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) (100 mg/ml) and excess [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/); 1 hour at 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) Cobalt Affinity Resin | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 200 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) + 0.1% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) resin pre-equilibrated with solubilization buffer; incubation 12-16 hours at 4 C; washed with 10 column volumes of wash buffer, 3 CVs of elution buffer containing AngII |
| Elution | Metal affinity elution | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) Cobalt Affinity Resin | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 200 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) + 0.03% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Elution with buffer containing excess AngII to maintain receptor-ligand complex |
| [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 200 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.03% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Monodisperse [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)-mbIIGN-term/Fab4A03 complex isolated for crystallization |

**Final sample**: 10 mg/ml in 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 200 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)
**Purity**: Monodisperse peak by [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)

#### Source: doi/10.1038##nature22035

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)
- **Expression construct**: [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/)-AT2R chimera; AT2R residues 1-34 and 336-363 truncated; N-terminal [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (apocytochrome b562RIL, Met7Trp, His102Ile, Arg106L) fused via 4-residue linker (Gly-Ser-Gly-Ser); N-terminal HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10x [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/), [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) cleavage site
- **Tag info**: [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10x His (N-terminal, cleaved by [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/))

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane isolation |  | 10 mM [HEPES (HEPES Buffer)](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 10 mM [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 20 mM KCl, [EDTA](/xray-mp-wiki/reagents/additives/edta/)-free protease inhibitor cocktail | [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) lysed by repeated washing and centrifugation with hypotonic and high osmotic buffers; membranes treated with [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) (2 mg/ml) for 30 min at 4 C |
| Solubilization | Detergent solubilization |  | 100 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 800 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.5% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.1% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Solubilized for 4 hours at 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) [IMAC](/xray-mp-wiki/methods/purification/affinity-chromatography/) resin | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 400 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash I); 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 200 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash II) + 0.1% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) (wash I); 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) (wash II) | Bound overnight to [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) resin; washed with 10 column volumes each of wash buffers I and II |
| Elution and tag cleavage | Metal affinity elution followed by protease cleavage | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) [IMAC](/xray-mp-wiki/methods/purification/affinity-chromatography/) resin | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 100 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.004% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution); then [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) overnight + 0.02% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.004% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Eluted with 3 CV elution buffer, incubated with 100 uM ligand (Cpd 1 or 2), treated overnight with [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) to remove N-terminal tags, concentrated to 15 mg/ml |

**Final sample**: 15 mg/ml in 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 100 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.004% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)
**Purity**: Tested by analytical [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)

#### Source: doi/10.1038##s41594-018-0079-8

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)
- **Expression construct**: BRIL-AT2R (BRIL replaces ICL3); N-terminal HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) site; C-terminal His6 tag
- **Tag info**: [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), His6 (C-terminal)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis and membrane isolation |  | 10 mM [HEPES (HEPES Buffer)](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 20 mM KCl, 10 mM [Magnesium Chloride](/xray-mp-wiki/reagents/additives/magnesium-chloride/), protease inhibitor cocktail | [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) harvested by centrifugation (7,000g, 10 min, 4 C), flash-frozen at -80 C, resuspended and lysed under hypotonic conditions |
| Solubilization | Detergent solubilization |  | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 800 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1.0% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.2% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Membranes solubilized with [DDM](/xray-mp-wiki/reagents/detergents/ddm/) and [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) supplemented with [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) (100 mg/ml) and excess s-AngII; 1 hour at 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) | 50 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 200 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), s-AngII + 0.1% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) resin pre-equilibrated; incubation 12-16 hours at 4 C; washed with 10 column volumes of wash buffer, 3 CVs of elution buffer containing s-AngII |
| Elution | Metal affinity elution | [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 200 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), s-AngII + 0.03% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Elution with buffer containing excess s-AngII to maintain receptor-ligand complex |
| [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) | 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 200 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.03% [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Monodisperse [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)-BRIL/Fab4A03 complex isolated for crystallization |

**Final sample**: 10 mg/ml in 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 200 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)
**Purity**: Monodisperse peak by [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)


## Crystallization

### doi/10.1016##j.str.2019.12.003

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) |
| Protein sample | [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)-mbIIGN-term/Fab4A03 complex + AngII, 10 mg/ml |
| Lipid | 1:1 [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/):[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) |
| Protein-to-lipid ratio | not specified |
| Temperature | 20 |
| Growth time | not specified |
| Notes | Data collected at 100 K at SPring-8 BL32XU micro-focus beamline. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) with MOLREP. 470 datasets collected with KAMO system and merged. |

### doi/10.1038##nature22035

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) - SFX at XFEL |
| Protein sample | [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/)-AT2R + Cpd 1, 15 mg/ml, reconstituted in [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) + 10% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) at 2:3 protein:lipid ratio |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) + 10% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) |
| Protein-to-lipid ratio | 2:3 (v/v) |
| Temperature | 20 |
| Growth time | 5 days |
| Notes | Microcrystals (5x2x2 um) grown in syringe, injected into [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) injector at LCLS XFEL. Two lattices observed. Data merged using CrystFEL with Cheetah hit finding. Orthorhombic structure used for description. |

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) - Synchrotron radiation |
| Protein sample | [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/)-AT2R + Cpd 2, reconstituted in [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) + 10% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) at 2:3 protein:lipid ratio |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) + 10% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) |
| Protein-to-lipid ratio | 2:3 (v/v) |
| Temperature | 20 |
| Growth time | 21 days |
| Notes | Crystals (70x40x20 um) harvested with micromounts and flash-frozen in liquid nitrogen. Data collected at 23ID-D beamline (GM/CA) at Advanced Photon Source, Argonne National Laboratory. Integrated and scaled with XDS. |

### doi/10.1038##s41594-018-0079-8

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) |
| Protein sample | [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)-BRIL/Fab4A03 complex + s-AngII, 10 mg/ml |
| Lipid | not specified |
| Protein-to-lipid ratio | not specified |
| Temperature | 20 |
| Growth time | not specified |
| Notes | Data collected at 100 K at SPring-8 BL32XU micro-focus beamline. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) with MOLREP. 470 datasets collected with KAMO system and merged. High Rmerge due to large variety of crystals, not poor datasets. |


## Biological / Functional Insights

### Helix 8 conformational change upon AngII binding

In the AngII-bound AT2R structure, helix 8 shifts from a non-canonical bent
conformation (observed in the partial agonist [Sar1,Ile8]-AngII-bound AT2R structure,
PDB 5XJM) to a canonical [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) helix 8 conformation parallel to the membrane. This
shift is caused by pi-pi interactions between Phe325^8.50 in helix 8 and Phe316^7.51
and Phe320^7.55 in TM7. These pi-pi interactions are not visible in the compound
1/2-bound AT2R structure (PDB 5UNF). The canonical helix 8 conformation suggests
that AT2R can engage G proteins and [Beta-Arrestin](/xray-mp-wiki/concepts/signaling-receptors/beta-arrestin/), although downstream signaling
is not transmitted by steric blocking.

### Deep ligand-binding pocket and Met128^3.36 rearrangement

Met128^3.36, located at the deep end of the AT2R ligand-binding pocket, moves away
toward Phe308^7.43 upon AngII binding to accommodate the Phe8 side chain of
[Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/). The equivalent residues in [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/) (Leu112^3.36 and Phe308^7.43) form
a hydrophobic core that must rearrange to accommodate Phe8, leading to rotation of
helix 7. This rearrangement at the bottom of the ligand-binding pocket is a key
feature distinguishing full agonist (AngII) from partial agonist ([Sar1,Ile8]-AngII)
binding.

### Asn111^3.35-Asn295^7.46 internal lock

The internal lock between Asn111^3.35 and Asn295^7.46 (equivalent to Asn127^3.35
and Ser311^7.46 in AT2R numbering) is disrupted upon AngII binding. In the
[Sar1,Ile8]-AngII-[Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) complex (PDB 6DO1), one hydrogen bond is maintained at this
internal lock, whereas two bonds are observed in the antagonist-bound inactive
conformation (PDB 4YAY). The complete disruption of this internal lock by full
agonist AngII binding may lead to full active conformation of AT2R. This internal
lock state differs from [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/) and could provide a molecular basis for the high basal
activity of AT2R.

### Activation mechanism comparison with AT1R

The AT2R-AngII structure reveals activation features that can be compared with [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/)
structures. In the active [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/) (PDB 6DO1) bound to partial agonist [S1I8](/xray-mp-wiki/reagents/ligands/s1i8/), one
hydrogen bond is maintained at the Asn111^3.35-Asn295^7.46 internal lock, while
in the inactive [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/) (PDB 4YAY) bound to antagonist [ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/), two bonds are observed.
The full agonist AngII binding to AT2R appears to completely disrupt this internal
lock, similar to AngII binding to [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/). Both AT2R and [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/) share conserved
activation motifs including PIF, [NPxxY Motif](/xray-mp-wiki/concepts/structural-mechanisms/npxxy-motif/), and DRY motifs, but the deep ligand-binding
pocket rearrangement differs between the two receptors.

### Non-canonical helix VIII blocks G protein/beta-arrestin binding

In the Cpd 1- and Cpd 2-bound [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) structures (PDB 5UNF, 5UNG, 5UNH), helix VIII
adopts a non-canonical conformation by flipping over to interact with the intracellular
ends of helices III, V, and VI. This conformation is stabilized by hydrophobic
interactions from Phe325^8.50, Leu329^8.54, Val332^8.57, and Phe333^8.58, as well
as polar interactions from Arg324^8.49, Gln326^8.51, and Lys328^8.53. Molecular
dynamics simulations (4 us total, 8 independent runs) confirm the stability of this
conformation. Helix VIII sterically blocks the G protein/beta-arrestin binding site,
explaining the lack of signaling responses in standard cellular assays. When
experimentally relocated to the canonical position, helix VIII relaxes into a
membrane-bound conformation accompanied by inward shift of helix VI toward the
inactive state.

### Active-like conformation of the 7TM bundle

All three AT2R structures (PDB 5UNF, 5UNG, 5UNH) display an active-like conformation
of the 7TM bundle despite being bound to antagonists. Helix VI shows an ~11.5 A
outward displacement at its intracellular end, while helix VII exhibits a ~4.9 A
inward displacement. Helix V shifts ~4.8 A toward the ligand-binding pocket at its
extracellular end. Conserved activation micro-switches are rearranged: the [PIF Motif](/xray-mp-wiki/concepts/pif-motif/)
(Pro223^5.50-Ile132^3.40-Phe265^6.44), [DRY Motif](/xray-mp-wiki/concepts/dry-motif/) (Arg142^3.50 rotated ~90 degrees),
and [NPxxY Motif](/xray-mp-wiki/concepts/structural-mechanisms/npxxy-motif/) (Tyr318^7.53 shifted ~6.5 A and rotated ~45 degrees). The putative
sodium-binding pocket is collapsed due to helix VII inward shift. AT2R has a rare
alanine at position 6.37 (vs. hydrophobic residue in ~97% of class A GPCRs), which
facilitates activation-related conformational changes.

### Fab4A03 antibody fragment as positive allosteric modulator

The [Fab4A03](/xray-mp-wiki/reagents/antibodies/fab4a03/) antibody fragment binds to the extracellular vestibule of AT2R and acts as a positive allosteric modulator, increasing the binding affinity of both s-AngII (Kd: 2.76 nM without Fab4A03, 0.56 nM with Fab4A03) and [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) for the receptor. No direct interaction between s-AngII and Fab4A03 was observed (distance > 7 A). The Fab4A03 binding site overlaps with the positive allosteric modulator binding site of the M2 muscarinic acetylcholine receptor (PDB 4MQT). The Fab also functioned as a crystallization chaperone, enabling the 3.2 A structure determination of the AT2R-s-AngII complex. 


## Cross-References

- [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) — Close homolog (34% identity); AT2R and [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) have distinct signaling properties and structural differences in ligand-binding pocket and helix VIII conformation
- [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) — Endogenous full agonist peptide ligand of [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [S1I8 Peptide](/xray-mp-wiki/reagents/ligands/s1i8/) — Partial agonist analog used in previous [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) structure (PDB 5XJM) for comparison
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) solubilization and purification
- [Cholesterol Hydrogen Succinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Membrane protein stabilizer used during [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) purification
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used as LCP crystallization matrix for [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) crystallized by LCP method (both synchrotron and XFEL)
- [Iodoacetamide](/xray-mp-wiki/reagents/additives/iodoacetamide/) — Cysteine alkylating agent used during [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) solubilization to prevent disulfide formation
- [Beta-Arrestin](/xray-mp-wiki/concepts/signaling-receptors/beta-arrestin/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [1,6-Hexanediol](/xray-mp-wiki/reagents/additives/16-hexanediol/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [Potassium Formate](/xray-mp-wiki/reagents/additives/potassium-formate/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [NPxxY Motif](/xray-mp-wiki/concepts/structural-mechanisms/npxxy-motif/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [HEPES (HEPES Buffer)](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [TALON Cobalt Affinity Resin](/xray-mp-wiki/reagents/additives/talon/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
