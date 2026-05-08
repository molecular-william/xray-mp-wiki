---
title: Bovine ADP/ATP Carrier
created: 2026-05-05
updated: 2026-05-05
type: protein
category: proteins
layout: default
tags: [transporter, mitochondrial-carrier, membrane-protein, xray-crystallography]
sources: [doi/10.1016##J.FEBSLET.2005.09.061]
---

# Bovine ADP/ATP Carrier

## Overview

The bovine mitochondrial ADP/ATP carrier (AAC) is the most abundant protein in the inner mitochondrial membrane, importing ADP into the matrix while exporting ATP to the cytosol. This paper reports the crystal structure at 2.8 A resolution (PDB: 2C3E) in a new crystal form (C2221 space group) revealing lipid-mediated dimerization. Three cardiolipin molecules are tightly bound per AAC monomer, with two cardiolipins sandwiched between monomers on the matrix side, mediating protein-protein interactions. The structure supports the dimeric functional unit hypothesis and provides structural evidence for cardiolipin's role in stabilizing the carrier's conformational changes during nucleotide exchange.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##J.FEBSLET.2005.09.061 | 2C3E | 2.8 A | C2221 | Bovine AAC residues 1-293 with carboxyatractyloside (CATR) | Carboxyatractyloside (CATR); 3 cardiolipins per monomer |

## Expression and Purification

- **Expression system**: Bovine heart muscle mitochondria (native extraction)
- **Construct**: Native AAC, residues 1-293 (C-terminus residues 294-297 disordered)

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Extraction | Detergent extraction | — | 2% LAPAO, carboxyatractyloside present | Extracted from bovine heart muscle mitochondria |
| Hydroxylapatite chromatography | HTP chromatography | Hydroxylapatite (HTP) |  |  |
| Gel filtration | Gel filtration | — | 0 or 5 mM NaCl | Low salt conditions favor dimeric form |
| Detergent reduction | Bio-Beads incubation | — |  | Detergent-to-protein ratio reduced |
| Concentration | Ultrafiltration | Amicon Ultra (Millipore) | ~5 mg/mL |  |


## Crystallization

### doi/10.1016##J.FEBSLET.2005.09.061

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | AAC-CATR complex at ~5 mg/ml |
| Reservoir | 28-32% Jeffamine M600, 10-20 mM NiSO4 (or 5 mM Na citrate + 50 mM Na arseniate), 100 mM HEPES pH 7.0 (or 100 mM Tris pH 8.5) |
| Temperature | 20 C |
| Growth time | Days |
| Cryoprotection | Flash-frozen in liquid nitrogen under nitrogen stream |
| Notes | Plate-shaped crystals 100x20x5 um3. Data collected at ESRF BM30A. Space group C2221 with unit cell a=80, b=109, c=89 A (low salt) or a=76, b=111, c=90 A (5 mM NaCl). |


## Biological / Functional Insights

### Cardiolipin-mediated dimerization

Two cardiolipins (CDL801A and CDL801B) are sandwiched between monomers on the matrix side, gluing the monomers together through hydrogen bonds between phosphate groups and protein main chain nitrogens. Aromatic residues (W70, Y173, F270) stack with acyl chains. The interacting surface between monomers A and B is 446 A2 (excluding lipids: 132 A2). Cardiolipins are not essential for yeast growth but reduce AAC activity to 20% in their absence.

### Transport mechanism and conformational changes

Two natural inhibitors, CATR and bongkrekic acid, interact with two different conformations representing extreme states during the transport process. The M1 loop fluctuates during transport, modifying helix h1-2. Cardiolipins may transmit conformational changes from one monomer to the other and participate in triggering concerted ADP/ATP exchange.


## Cross-References

- [LAPAO](/xray-mp-wiki/reagents/detergents/lapao/) — Extraction detergent at 2% (w/v) for AAC isolation from mitochondria
- [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) — 3 cardiolipins tightly bound per monomer; 2 mediate dimerization on matrix side
- [Jeffamine M600](/xray-mp-wiki/reagents/additives/jeffamine-m600/) — Crystallization precipitant at 28-32% in hanging-drop vapor diffusion
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Hydroxylapatite chromatography used for AAC purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Gel filtration used after HTP chromatography
