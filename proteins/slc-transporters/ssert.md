---
title: Human Serotonin Transporter (SERT)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17629, doi/10.1038##ncomms11673, doi/10.1038##s41594-018-0026-8]
verified: false
---

# Human Serotonin Transporter (SERT)

## Overview

The human [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) transporter (SERT, also known as SLC6A4) is a [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/nss-family/) member that terminates serotonergic signalling through the Na+/Cl--coupled reuptake of [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) (5-HT) from the synaptic cleft into presynaptic neurons. SERT is a primary target for antidepressant drugs including selective [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) reuptake inhibitors (SSRIs) such as (S)-citalopram and [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/), as well as psychostimulants. X-ray crystal structures of human SERT bound to antidepressants revealed how diverse SSRIs lock the transporter in an outward-open conformation and identified an allosteric site at the extracellular vestibule.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature17629 | not specified | 3.14 | C222_1 | SERT ts3 — human SERT with thermostabilizing mutations Y110A, I291A, T439S, surface cysteine mutations C554A, C580A, C622A, fused to C-terminal GFP, twin Strep tag, and His10 tag; complexed with [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) and 8B6 Fab | [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/), [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), N-acetylglucosamine, Na+, Cl-, 8B6 Fab |
| doi/10.1038##nature17629 | not specified | 3.15 | C222_1 | SERT ts3 — human SERT with thermostabilizing mutations Y110A, I291A, T439S, surface cysteine mutations C554A, C580A, C622A; complexed with (S)-citalopram and 8B6 Fab | (S)-citalopram (central site and allosteric site), [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), N-acetylglucosamine, Na+, Cl-, 8B6 Fab |
| doi/10.1038##nature17629 | not specified | 4.53 | C222_1 | SERT ts2 — human SERT with thermostabilizing mutations I291A, T439S, surface cysteine mutations C554A, C580A, C622A; complexed with [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) and 8B6 Fab | [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/), [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), N-acetylglucosamine, Na+, Cl-, 8B6 Fab |
| doi/10.1038##s41594-018-0026-8 | 6AWN | 3.62 | C222_1 | SERT ts2 (Thr439) with [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) — human SERT with thermostabilizing mutations I291A, T439S, surface cysteine mutations C554A, C580A, C622A; complexed with [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) and 8B6 Fab | [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) |
| doi/10.1038##s41594-018-0026-8 | 6AWP | 3.80 | C222_1 | SERT ts3 with [Fluvoxamine](/xray-mp-wiki/reagents/ligands/fluvoxamine/) — human SERT with thermostabilizing mutations Y110A, I291A, T439S, surface cysteine mutations C554A, C580A, C622A; complexed with [Fluvoxamine](/xray-mp-wiki/reagents/ligands/fluvoxamine/) and 8B6 Fab | [Fluvoxamine](/xray-mp-wiki/reagents/ligands/fluvoxamine/) |
| doi/10.1038##s41594-018-0026-8 | 6AWO | 3.53 | C222_1 | SERT ts3 with [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) — human SERT with thermostabilizing mutations Y110A, I291A, T439S, surface cysteine mutations C554A, C580A, C622A; complexed with [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) and 8B6 Fab | [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) |
| doi/10.1038##s41594-018-0026-8 | 6AWQ | 4.05 | C222_1 | SERT ts3 with [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) — human SERT with thermostabilizing mutations Y110A, I291A, T439S, surface cysteine mutations C554A, C580A, C622A; complexed with [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) and 8B6 Fab (data collected at ALS 5.0.2) | [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) |

## Expression and Purification

- **Expression system**: HEK293S GnT- cells via baculovirus-mediated transduction (BacMam)
- **Construct**: C-terminal GFP fusion with twin Strep and His10 tags, thrombin cleavage sites
- **Notes**: SERT ts2 and ts3 variants derived from human SERT gene

### Purification Workflow

*Source: doi/10.1038##nature17629*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent solubilization |  | 50 mM Tris pH 8, 150 mM NaCl, 20 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 2.5 mM [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 0.5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/), 1 uM inhibitor + 20 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Membranes harvested and solubilized |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Strep-Tactin [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Strep-Tactin resin | 20 mM Tris pH 8, 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Large-scale purification of SERT |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 20 mM Tris pH 8, 150 mM NaCl, 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.1 mM [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Monodisperse fractions collected |

### Purification Workflow

*Source: doi/10.1038##s41594-018-0026-8*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent solubilization |  | 50 mM Tris pH 8, 150 mM NaCl, 20 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 2.5 mM [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 20 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | HEK293S GnT- cells solubilized |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Strep-Tactin [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Strep-Tactin resin | 20 mM Tris pH 8, 100 mM NaCl (TBS), 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.2 mM [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 25 uM lipid mixture ([POPC](/xray-mp-wiki/reagents/lipids/popc/):[POPE](/xray-mp-wiki/reagents/lipids/pope/):[POPG](/xray-mp-wiki/reagents/lipids/popg/) 1:1:1) + 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Eluted protein digested by thrombin and [ENDOH](/xray-mp-wiki/reagents/additives/endoh/); combined with 8B6 Fab at 1:1.2 ratio |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) |  | TBS supplemented with 40 mM n-octyl beta-D-maltoside, 0.5 mM [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 25 uM lipid mixture ([POPC](/xray-mp-wiki/reagents/lipids/popc/):[POPE](/xray-mp-wiki/reagents/lipids/pope/):[POPG](/xray-mp-wiki/reagents/lipids/popg/) 1:1:1) + 40 mM n-octyl beta-D-maltoside | SERT-8B6 complex purified; concentrated to 2 mg/ml; SSRIs added to 50 uM |


## Crystallization

### doi/10.1038##nature17629

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | SERT ts3-[Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) complex with 8B6 Fab |
| Reservoir | not specified |
| Notes | Outward-open conformation, C222_1 space group |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | SERT ts3-(S)-citalopram complex with 8B6 Fab |
| Reservoir | not specified |
| Notes | (S)-citalopram bound to both central and allosteric sites |

### doi/10.1038##s41594-018-0026-8

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | SERT-Fab complex (ts2 or ts3) with SSRI inhibitor at 50 uM |
| Reservoir | 50-100 mM Tris pH 8.5, 25-75 mM Li2SO4, 25-75 mM Na2SO4, 33.5-36% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400, 0.5% 6-aminohexanoic acid |
| Temperature | 4 |
| Cryoprotection | Crystals flash cooled directly in liquid nitrogen |
| Notes | 2 ul protein to 1 ul reservoir ratio |


## Biological / Functional Insights

### Antidepressant binding to the central site

(S)-citalopram and [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) both bind to the central binding site (S1) located between transmembrane helices 1, 3, 6, 8 and 10. The amine groups of both drugs occupy subsite A and interact with the conserved Asp98 carboxylate. Tyr95 forms a cation-pi interaction beneath the amine groups. The drugs lock SERT in an outward-open conformation, wedging between scaffold helices 3, 8, 10 and core helices 1, 6, directly blocking [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) binding.

### Allosteric site identification

A second (S)-citalopram molecule was found in an allosteric site at the periphery of the extracellular vestibule, approximately 13 A from the central site. Occupancy of this allosteric site sterically hinders ligand unbinding from the central site, providing a structural explanation for (S)-citalopram's action as an allosteric ligand.

### Diverse SSRI binding modes at the central site

Structures of SERT bound to [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/), [Fluvoxamine](/xray-mp-wiki/reagents/ligands/fluvoxamine/), and [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) revealed that chemically diverse SSRIs occupy the central binding site with different binding poses, explaining how the transporter accommodates structurally distinct antidepressants. In subsite A, the distance from the amine of [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) to Asp98 is longer, while for [Fluvoxamine](/xray-mp-wiki/reagents/ligands/fluvoxamine/) and [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) it is shorter. In subsite B, the meta chlorine of [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) engages with Ser439 while the fluorines of [Fluvoxamine](/xray-mp-wiki/reagents/ligands/fluvoxamine/) form closer interactions. In subsite C, the naphthalene group of [Sertraline](/xray-mp-wiki/reagents/ligands/sertraline/) is localized higher than the benzofuran of (S)-citalopram and [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/). Phe341 and Phe335 undergo different rotamer conformations to accommodate different drugs. These structural differences help explain the varying affinities of different SSRIs.


## Cross-References

- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/) — NSS family prototype sharing the LeuT-fold architecture
- [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/nss-family/) — SERT is a human member of the NSS family (SLC6A4)
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — SERT transport follows alternating access
- [Sertraline](/xray-mp-wiki/reagents/sertraline/) — SSRI antidepressant bound in ts3-sertraline structures
- [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/serotonin/) — Endogenous substrate of SERT
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for solubilization and purification
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used throughout purification and crystallization
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Method used in structure determination or purification
- [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Additive used in purification or crystallization buffers
