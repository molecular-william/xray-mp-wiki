---
title: QseE Periplasmic Sensor Domain (E. coli)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1107##s2053230x23009123]
verified: false
---

# QseE Periplasmic Sensor Domain (E. coli)

## Overview

QseE is a histidine kinase (HK) and the sensor component of the QseE/F/G three-component system from enterohemorrhagic Escherichia coli (EHEC). It regulates virulence gene expression in response to environmental signals such as sulfate, phosphate, and host hormones (epinephrine and norepinephrine). The crystal structure of the periplasmic sensor domain (amino acids 41-167) was determined at 1.33 Å resolution. The domain forms a four-α-helix bundle, similar to other periplasmic sensor domains of HKs such as NarX, KinB, and McpN. Conserved arginine residues (Arg70, Arg74, Arg154) at the putative dimer interface suggest QseE interacts with negatively charged ligands. Cys76 and Cys126 form a disulfide bond. The structure was solved with the aid of AlphaFold models and is monomeric in both solution and the crystal environment.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1107##s2053230x23009123 |  | 1.33 | P2_12_12_1 | Periplasmic domain (amino acids 41-167) of QseE from E. coli with N-terminal His-tag | None |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: QseE periplasmic domain (residues 41-167) with N-terminal His-tag and TEV cleavage site in pET-28a

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and lysis | E. coli cells grown at 17°C for 20 h after induction with 0.1 mM IPTG. Cells collected by centrifugation and sonicated in buffer with protease inhibitors. | -- | 50 mM Tris-HCl pH 8.0, 200 mM NaCl, cOmplete Protease Inhibitor Cocktail | Centrifugation at 20,000g for 1 h at 4°C |
| Affinity chromatography | Supernatant loaded onto HiTrap TALON column | HiTrap TALON | 50 mM Tris-HCl pH 8.0, 200 mM NaCl | TEV protease added after elution for tag removal |
| Reverse affinity chromatography | Dialyzed sample loaded onto HisTrap column; flowthrough collected | HisTrap | 20 mM Tris-HCl pH 8.0, 300 mM NaCl | Cleaved tag and undigested protein bind; flowthrough contains pure QseE |
| Size-exclusion chromatography | Flowthrough fraction purified on HiLoad 16/60 Superdex 200 gel-filtration column | Superdex 200 | 20 mM Tris-HCl pH 8.0, 100 mM NaCl | Final purification step |


## Crystallization

### doi/10.1107##s2053230x23009123

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor-diffusion |
| Protein sample | 10 mg/mL QseE in 20 mM Tris-HCl pH 8.0, 100 mM NaCl |
| Reservoir | 0.15 M sodium formate, 0.1 M HEPES pH 7.2, 18% (w/v) PEG 3350 |
| Temperature | 20°C |
| Cryoprotection | Soaked in crystallization solution supplemented with 20% ethylene glycol before flash-cooling in liquid nitrogen |
| Notes | Crystals also obtained in condition B (0.1 M sodium malonate pH 8.0, 0.1 M Tris pH 8.0, 30% PEG 1000). X-ray data collected at SPring-8 BL41XU with EIGER X 16M detector at 1.0 Å wavelength. |


## Biological / Functional Insights

### Conserved arginine residues define the putative ligand-binding site

Three conserved arginine residues (Arg70, Arg74, Arg154) are positioned at the putative dimer interface of QseE, analogous to other HK sensor domains that bind negatively charged ligands (nitrate/nitrite for NarX, phosphate for PhoQ). This suggests QseE senses negatively charged signals such as sulfate and phosphate through electrostatic interactions with these arginine residues. Sequence alignment shows these arginines are conserved across Enterobacteriaceae.

### QseG interacts with QseE in the periplasm

QseG, an outer membrane lipoprotein, co-localizes with QseE in the periplasmic space and is required for QseE/F activity. The positively charged surface of QseE (opposite the ligand-binding site) may interact with the negatively charged C-terminal coiled-coil region (α7c) of QseG. The structural flexibility of QseG's C-terminal region, derived from weakened hydrophobic interactions in its coiled-coil interface, likely facilitates complex formation with QseE.


## Cross-References

- [QseG Outer Membrane Lipoprotein](/xray-mp-wiki/proteins/enzymes/qseg-outer-membrane-lipoprotein/) — QseG interacts with QseE in the periplasm to form the three-component system
- [QseE/F/G Three-Component System](/xray-mp-wiki/concepts/qse-efg-three-component-system/) — QseE is the histidine kinase sensor component of this system
