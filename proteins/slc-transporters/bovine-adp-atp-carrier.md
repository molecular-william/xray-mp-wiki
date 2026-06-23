---
title: "Bovine ADP/ATP Carrier"
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##J.FEBSLET.2005.09.061]
verified: false
---

# Bovine ADP/ATP Carrier

## Overview

The bovine ADP/ATP carrier (AAC) is a mitochondrial inner membrane protein that exchanges ADP and [ATP](/xray-mp-wiki/reagents/ligands/atp) across the membrane. It is a key player in cellular energy metabolism and exists as a dimer stabilized by cardiolipins.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##J.FEBSLET.2005.09.061 | 2C3E | 2.8 A | C2221 | Bovine AAC residues 1-293 with ([CATR](/xray-mp-wiki/reagents/ligands/carboxyatractyloside) | [Carboxyatractyloside (CATR)](/xray-mp-wiki/reagents/ligands/carboxyatractyloside) (CATR); 3 cardiolipins per monomer |

## Expression and Purification

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Extraction | Detergent extraction | -- | 2% LAPAO, [Carboxyatractyloside (CATR)](/xray-mp-wiki/reagents/ligands/carboxyatractyloside) present | Extracted from bovine heart muscle mitochondria |
| Hydroxylapatite chromatography | HTP chromatography | Hydroxylapatite (HTP) | not specified | not specified |
| Gel filtration | Gel filtration | -- | 0 or 5 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride) | Low salt conditions favor dimeric form |
| Detergent reduction | Bio-Beads incubation | -- |  | Detergent-to-protein ratio reduced |
| Concentration | Ultrafiltration | Amicon Ultra (Millipore) | ~5 mg/mL |  |


## Crystallization

### doi/10.1016##J.FEBSLET.2005.09.061

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | AAC-[CATR](/xray-mp-wiki/reagents/ligands/carboxyatractyloside) complex at ~5 mg/ml |
| Reservoir | 28-32% Jeffamine M600, 10-20 mM NiSO4 (or 5 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride)) |
| Temperature | not specified |
| Growth time | Days |
| Cryoprotection | Flash-frozen in liquid nitrogen under nitrogen stream |
| Notes | Plate-shaped crystals 100x20x5 um3. Data collected at ESRF BM30A. Space group C2221 with unit cell a=80, b=109, c=89 A (low salt or a=76, b=111, c=90 A (5 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride)). Role in stabilizing the carrier's conformational changes during nucleotide exchange. |


## Biological / Functional Insights

### Transport mechanism and conformational changes

Two natural inhibitors, [Carboxyatractyloside (CATR)](/xray-mp-wiki/reagents/ligands/carboxyatractyloside) and bongkrekic acid, interact with two different conformations representing extreme states during the transport process. The M1 loop fluctuates during transport, modifying helix h1-2. Cardiolipins may transmit conformational changes from one monomer to the other and participate in triggering concerted ADP/ATP exchange.

### Cardiolipin-mediated dimerization

Two cardiolipins (CDL801A and CDL801B) are sandwiched between monomers on the matrix side, gluing the monomers together through hydrogen bonds between phosphate groups and protein main chain nitrogens. Aromatic residues (W70, Y173, F270) stack with acyl chains. The interacting surface between monomers A and B is 446 A2 (excluding lipids: 132 A2).


## Cross-References

- [LAPAO](/xray-mp-wiki/reagents/detergents/lapao/) — Extraction detergent at 2% (w/v) for AAC isolation from mitochondria
- [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) — 3 cardiolipins tightly bound per monomer; 2 mediate dimerization on matrix side
- [Jeffamine M600](/xray-mp-wiki/reagents/additives/jeffamine-m600/) — Crystallization precipitant at 28-32% in [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion)
- [Carboxyatractyloside (CATR)](/xray-mp-wiki/reagents/ligands/carryatractyloside/) — Inhibitor co-crystallized with AAC
- [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Used in crystallization conditions
- [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) — Crystallization method used for structure determination
- [ATP](/xray-mp-wiki/reagents/ligands/atp) — Ligand or small molecule used in this study
- [Carboxyatractyloside (CATR)](/xray-mp-wiki/reagents/ligands/carboxyatractyloside) — Ligand or small molecule used in this study
