---
title: ECF-CbrT (ECF-type ABC Transporter for Vitamin B12 from Lactobacillus delbrueckii)
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.7554##eLife.35828]
verified: false
---

# ECF-CbrT (ECF-type ABC Transporter for Vitamin B12 from Lactobacillus delbrueckii)

## Overview

ECF-CbrT is an Energy Coupling Factor (ECF)-type ABC transporter from Lactobacillus delbrueckii subsp. bulgaricus that mediates the specific, -dependent uptake of vitamin B12 () and its precursor cobinamide (Cbi). The complex consists of the S-component CbrT (substrate-binding protein), the transmembrane protein EcfT, and two ATPase subunits EcfA and EcfA'. It is unrelated to the well-characterized B12 transporter BtuCDF, but shares similar biochemical features, indicating functional convergence.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.35828 | 6FNP | 3.4 | — | Full ECF-CbrT complex (CbrT, EcfT, EcfA, EcfA') | apo (inward-facing) |

## Expression and Purification

- **Expression system**: Escherichia coli MC1061
- **Construct**: CbrT inserted into p2BAD_ECF with XbaI/XhoI; [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/ecf-transporter-family/) module expressed from same plasmid
- **Notes**: Expression induced with L-arabinose at 37°C
- **Induction**: 0.00001% L-arabinose

### Purification Workflow

- **Expression system**: Escherichia coli MC1061
- **Expression construct**: Full ECF-CbrT complex
- **Tag info**: C-terminal octa-His-tag on CbrT (solitary) or untagged in complex

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest and membrane preparation | Centrifugation and membrane vesicle preparation | — | 50 mM KPi, pH 7.5 | Cells harvested 3 hr post-induction |
| Membrane solubilization | Detergent solubilization | — | 50 mM KPi, pH 7.5, 300 mM NaCl, 10%  + 1%  | 45 min at 4°C with constant agitation |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | BioRad PolyPrep column, 0.5 mL Ni2+ resin | 50 mM KPi, pH 7.5, 300 mM NaCl, 10%  + 0.05%  |  |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC | — | 50 mM KPi, pH 7.5, 150 mM NaCl + 0.05%  |  |


## Crystallization

### doi/10.7554##eLife.35828

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified ECF-CbrT in 50 mM KPi pH 7.5, 150 mM NaCl, 0.05%  |
| Notes | OH-Cbl was added in excess to crystallization condition but not bound in structure |


## Biological / Functional Insights

### ECF-CbrT is a vitamin B12 transporter

ECF-CbrT supports -dependent growth of an E. coli knockout strain
lacking the endogenous B12 transporter BtuCDF. The full complex (CbrT + ECF
module) is required for transport; solitary CbrT cannot sustain growth.

### Substrate specificity and promiscuity

ECF-CbrT transports both  (Cbl) and cobinamide (Cbi). Competition
assays show promiscuity toward the beta-axial ligand: CN-Cbl, OH-Cbl,
Met-Cbl inhibit uptake strongly, while Ado-Cbl (bulkier) inhibits partially.
Hemin does not compete, confirming specificity for B12-related compounds.

### High-affinity binding

CbrT binds CN-Cbl with Kd of 9.2  and Cbi with Kd of 36  by [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/).
Binding is 1:1 stoichiometry. The apo protein is unstable, indicating
substrate binding has a stabilizing effect.

### Structural comparison with ECF-FolT2

The crystal structure at 3.4 Å reveals the S-component CbrT in a toppled,
inward-facing apo conformation. The identical [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/ecf-transporter-family/) module (EcfA, EcfA',
EcfT) adjusts to interact with different S-components (CbrT vs FolT2)
via conformational changes in the EcfT membrane domain, hinging around
Pro71. Loop 3 of CbrT occludes the empty binding cavity, unlike FolT2.

### Functional convergence with BtuCDF

Despite being structurally and mechanistically unrelated to BtuCDF,
ECF-CbrT shows similar kinetic parameters (Km 2.1  for Cbl,
Vmax 0.06 nmol/mg/s), suggesting convergent evolution of B12 transport.


## Cross-References

- [ECF Transporter Family](/xray-mp-wiki/concepts/ecf-transporter-family/) — ECF-CbrT is a group II ECF transporter
- [Cobalamin](/xray-mp-wiki/reagents/cobalamin/) — Referenced in ecf-cbrt text
- [ATP](/xray-mp-wiki/reagents/ligands/atp/) — Referenced in ecf-cbrt text
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in ecf-cbrt text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in ecf-cbrt text
- [NM](/xray-mp-wiki/reagents/detergents/nm/) — Referenced in ecf-cbrt text
- [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) — Referenced in ecf-cbrt text
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Referenced in ecf-cbrt text
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Referenced in ecf-cbrt text
