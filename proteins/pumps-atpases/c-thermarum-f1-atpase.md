---
title: "F1-ATPase from Caldalkalibacillus thermarum"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1612035113]
verified: false
---

# F1-ATPase from Caldalkalibacillus thermarum

## Overview

The F1-ATPase from Caldalkalibacillus thermarum is the water-soluble catalytic domain of the thermoalkaliphilic F1FO-[ATP](/xray-mp-wiki/reagents/ligands/atp/) synthase. It consists of α₃β₃γδε subunits and hydrolyzes [ATP](/xray-mp-wiki/reagents/ligands/atp/) poorly. The crystal structure reveals that although the overall architecture is closely similar to active mitochondrial and bacterial F1-ATPases, the βE-catalytic site is occupied by [ADP](/xray-mp-wiki/reagents/ligands/adp/) (without magnesium ion) and a phosphate ion, which likely forms the basis of inhibition of [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis. Unlike the Geobacillus stearothermophilus enzyme, the ε-subunit does not regulate activity via conformational changes, and neither the γ-subunit nor regulatory [ATP](/xray-mp-wiki/reagents/ligands/atp/) bound to the ε-subunit is involved in the inhibitory mechanism.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1612035113 | 5HKK | 3.0 |  | Wild-type C. thermarum F1-ATPase (α₃β₃γδε subunits expressed with His10 tag on ε-subunit, TEV-cleaved) | Mg-[ADP](/xray-mp-wiki/reagents/ligands/adp/) (α- and β-subunits), [ADP](/xray-mp-wiki/reagents/ligands/adp/) + phosphate (βE-subunit), [ATP](/xray-mp-wiki/reagents/ligands/atp/) + Mg²⁺ (ε-subunit C-terminal helical domain) |
| doi/10.1073##pnas.1612035113 | 5HKK | 2.6 |  | Mutant C. thermarum F1-ATPase (ε-subunit E83A, I88A, D89A, R92A, R99A, R123A, R127A — [ATP](/xray-mp-wiki/reagents/ligands/atp/)-binding deficient ε-subunit) | Mg-[ADP](/xray-mp-wiki/reagents/ligands/adp/) (α- and β-subunits), [ADP](/xray-mp-wiki/reagents/ligands/adp/) + phosphate (βE-subunit) |

## Expression and Purification

- **Expression system**: Escherichia coli C41(Δunc)
- **Construct**: F1-ATPase α₃β₃γδε with His10 tag and TEV protease cleavage site at N-terminus of ε-subunit
- **Notes**: Expressed from pTrc99A plasmid. E. coli C41 strain lacking endogenous unc operon used for overexpression.

### Purification Workflow

- **Expression system**: Escherichia coli C41(Δunc)
- **Expression construct**: C. thermarum F1-ATPase with His10 tag + TEV site on ε-subunit
- **Tag info**: His10 tag on ε-subunit, removed by TEV protease on-column

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Nickel affinity chromatography | Affinity chromatography | [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) | Purification buffer (detailed in SI Materials and Methods) | His10-tagged F1-ATPase bound to Ni-NTA resin |
| TEV protease cleavage | On-column cleavage |  |  | His10 tag cleaved with TEV protease while bound to Ni-NTA column |


## Crystallization

### doi/10.1073##pnas.1612035113

| Parameter | Value |
|---|---|
| Method | Microbatch |
| Protein sample | Purified F1-ATPase (wild-type or mutant) |
| Cryoprotection | Cryocooled |
| Notes | Crystals grown by microbatch method. Data collected at European Synchrotron Radiation Facility, Grenoble, France. Crystallization buffers devoid of nucleotide. |


## Biological / Functional Insights

### ε-subunit does not regulate ATP hydrolysis in C. thermarum F1-ATPase

The ε-subunit is in the down position with an [ATP](/xray-mp-wiki/reagents/ligands/atp/) molecule bound to its C-terminal α-helices. A mutant ε-subunit unable to bind [ATP](/xray-mp-wiki/reagents/ligands/atp/) remains in the down state and does not relieve inhibition. Therefore, unlike G. stearothermophilus F1-ATPase, neither the γ-subunit nor regulatory [ATP](/xray-mp-wiki/reagents/ligands/atp/) bound to ε-subunit mediates the inhibitory mechanism. The enzyme is inhibited by a mechanism independent of ε-subunit conformational changes.

### βE subunit contains bound ADP and phosphate without magnesium ion

The βE catalytic site in both wild-type and mutant structures contains [ADP](/xray-mp-wiki/reagents/ligands/adp/) without a magnesium ion plus a phosphate ion. This occupancy has never been observed in active F1-ATPase structures. The phosphate is ~7 Å from where the γ-phosphate of [ATP](/xray-mp-wiki/reagents/ligands/atp/) would be. Both [ADP](/xray-mp-wiki/reagents/ligands/adp/) and phosphate likely originated from the E. coli overexpression strain. This unique combination of hydrolysis products bound to the βE site is proposed as the basis of inhibition.

### Activated enzyme activity measured with LDAO

[ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis activity of both wild-type and mutant F1-complexes was activated by 0.1% lauryldimethylamine oxide (LDAO) to a specific activity of 33-38 U/mg protein for both enzymes. This confirms that both wild-type and mutant enzymes are in an inhibited basal state that can be artificially activated by detergent.


## Cross-References

- [Bovine F1-ATPase (Mitochondrial ATP Synthase Catalytic Domain)](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/) — Homologous enzyme from bovine mitochondria with similar α₃β₃γ architecture
- [F1-ATPase Rotary Catalytic Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/f1-atpase-rotary-mechanism/) — The rotary catalytic mechanism is the fundamental operating principle of F1-ATPases
- [n-Dodecyl-N,N-dimethylamine-N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/ldao/) — LDAO (0.1%) used to activate ATP hydrolysis activity of inhibited F1-ATPase
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein structure
- [Bovine F1-ATPase (azide-inhibited form)](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/) — Related protein structure
- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Related protein structure
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [F1-ATPase Rotary Catalytic Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/f1-atpase-rotary-mechanism/) — Related concept
- [Lauryldimethylamine N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/ldao/) — Reagent used in the study
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used in the study
