---
title: "TH-PF01 (Orthosteric–Allosteric Dual PfHT1 Inhibitor)"
created: 2026-06-11
updated: 2026-06-11
type: reagent
category: reagents
layout: default
tags: [ligand, subdirectory-ligands]
sources: [doi/10.1073##pnas.2017749118]
verified: regex
---

# TH-PF01 (Orthosteric–Allosteric Dual PfHT1 Inhibitor)

## Overview

TH-PF01 is a lead compound from the TH-PF series of orthosteric–allosteric dual inhibitors targeting Plasmodium falciparum hexose transporter 1 ([PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/)). It contains a sugar moiety ([Glucose](/xray-mp-wiki/reagents/additives/glucose/) core) that binds to the orthosteric glucose-binding pocket, a quinoline-containing heteroaromatic tail group that occupies the PfHT1-specific allosteric pocket, and a flexible C9 polymethylene linker connecting the two moieties. TH-PF01 selectively inhibits [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) over [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/). In biochemical assays (proteoliposome-based counterflow), TH-PF01 showed an IC50 of 1.46 ± 0.01 uM. Against blood-stage P. falciparum, EC50 values were 0.371 ± 0.026 uM (3D7 strain) and 0.349 ± 0.003 uM (Dd2 multidrug-resistant strain). The CC50 against HEK293T17 cells was >13.4 uM, giving a therapeutic window (CC50/EC50) of 36.1–38.4. Predicted ClogP is 4.01.


## Properties

- **Chemical name**: TH-PF01
- **Class**: [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) dual inhibitor (lead compound)

## Use in Membrane Protein Work

### Antimalarial lead compound

TH-PF01 demonstrated potent growth inhibition against both drug-sensitive (3D7)
and multidrug-resistant (Dd2) strains of P. falciparum with sub-micromolar EC50
values. It showed equipotency to both strains, unlike quinine which lost activity
against Dd2. TH-PF01 disrupts glycolysis in blood-stage parasites, as confirmed
by Seahorse extracellular flux analysis showing dose-dependent reduction in
extracellular acidification rate (ECAR).


## Examples from This Wiki

| Protein | Concentration | Context | Result |
|---|---|---|---|
| [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) | 1 uM | Counterflow assay with wild-type and mutant [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) to validate binding mode | Reduced potency against K51A, Q169A, Q305A, N341A, F85S, F85Y, V44T mutants |
| P. falciparum 3D7 and Dd2 | 0.3-0.4 uM (EC50) | 72-h parasite growth inhibition assay | Equipotent against both drug-sensitive and multidrug-resistant strains |

## Binding Mode

### Binding to [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/)

The sugar moiety of TH-PF01 binds to the orthosteric glucose-binding pocket of [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/). The quinoline fragment occupies the allosteric site, forming a hydrogen bond network between TH-PF01, Lys51 (K51), and Asp447 (D447) of [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/). The C9 polymethylene linker traverses the hydrophobic connecting channel. [Molecular Docking](/xray-mp-wiki/methods/structure-determination/molecular-docking/) simulations confirmed this dual-binding mode, and alanine scanning mutagenesis (K51A, Q169A, Q305A, N341A, K51A/D447A) validated the predicted interactions.

- **Key residues**: ['K51 (hydrogen bond with quinoline tail)', 'D447 (hydrogen bond with quinoline tail)', 'Q169 (interaction with sugar moiety)', 'Q305 (interaction with sugar moiety)', 'N341 (interaction with sugar moiety)', 'F85 (hydrophobic channel residue, selectivity determinant)', 'V44 (hydrophobic channel residue, selectivity determinant)']

## Advantages and Disadvantages

No advantages/disadvantages recorded.

## Comparison with Related Reagents

No comparison data available.

## Cross-References

- [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) — Molecular target of TH-PF01
- [C3361 (PfHT1 Inhibitor)](/xray-mp-wiki/reagents/ligands/c3361/) — Reference compound that inspired the design of the TH-PF series
- [TH-PF02](/xray-mp-wiki/reagents/ligands/th-pf02/) — Analogous lead compound from the same TH-PF series
- [TH-PF03](/xray-mp-wiki/reagents/ligands/th-pf03/) — Most potent analog from the TH-PF series
- [Orthosteric–Allosteric Dual Inhibition](/xray-mp-wiki/concepts/transport-mechanisms/orthosteric-allosteric-dual-inhibition/) — TH-PF01 exemplifies the dual inhibition strategy
- [Selective Starvation of Malaria Parasites](/xray-mp-wiki/concepts/miscellaneous/selective-starvation/) — TH-PF01 works through the selective starvation mechanism
- [Molecular Docking](/xray-mp-wiki/methods/structure-determination/molecular-docking/) — Method used in structure determination or purification
- [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) — Related protein structure
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Additive used in purification or crystallization buffers
