---
title: E. coli Phosphatidylglycerophosphate Phosphatase B (ecPgpB)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1403097111]
verified: false
---

# E. coli Phosphatidylglycerophosphate Phosphatase B (ecPgpB)

## Overview

ecPgpB is an E. coli membrane-integrated type II [Phosphatidic Acid](/xray-mp-wiki/reagents/lipids/phosphatidic-acid/) phosphatase (PAP2) that catalyzes
removal of the terminal phosphate group from the lipid carrier undecaprenyl pyrophosphate. It is essential
for transport of hydrophilic small molecules across the membrane. The 3.2 A crystal structure revealed
a six-transmembrane helix topology with a V-shaped TM helix pair (TM2-TM3) forming the substrate
entrance cleft, allowing lateral movement of lipid substrates from the membrane bilayer into the active site.
The structure serves as a prototype for eukaryotic PAP2 enzymes including human -6-phosphatase.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1403097111 | not specified | 3.2 | P2(1)2(1)2(1) | ecPgpB WT and I116M/E120K mutant |  |

## Expression and Purification

- **Expression system**: E. coli BL21
- **Construct**: Full-length PgpB cloned from E. coli BL21 genome
- **Notes**: Expressed as recombinant protein

### Purification Workflow

- **Expression system**: E. coli BL21

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | Detergent solubilization and purification | — |  + [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) () |  |


## Crystallization

### doi/10.1073##pnas.1403097111

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified ecPgpB in detergent combination |
| Notes | I116M/E120K double mutant gave better resolution. Space group P2(1)2(1)2(1). |


## Biological / Functional Insights

### V-shaped TM helix pair substrate entrance

A V-shaped TM helix pair (TMs 2 and 3) forms a surface cleft at the membrane-solvent interface,
allowing membrane-associated lipid substrates to enter the active site. The lipid substrate inserts
its phosphate head toward the nucleophilic His207(3.08) to form the phosphate-enzyme intermediate.

### Induced-fit substrate binding

The crystal structure represents an apo-form. TM3 packs loosely, placing Lys97(1.01) ~9 A from
its active position. Substrate binding drives TM3 movement toward TM2, completing the active site.
This induced-fit mechanism restricts activity to properly bound lipid substrates.

### Conserved active site with soluble PAP2 enzymes

Despite different substrate binding mechanisms, the catalytic residues (His163, His207, Asp211)
and overall fold of TMs 4-6 are nearly identical to soluble PAP2 enzymes ebNSAP (PDB 1EOI)
and ciCPO (PDB 1VNC), confirming evolutionary relationship between soluble and TM PAP2 proteins.


## Cross-References

- [Type II Phosphatidic Acid Phosphatase (PAP2) Family](/xray-mp-wiki/concepts/pap2-family/) — ecPgpB is prototypical transmembrane PAP2 enzyme
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Referenced in ecpgb text
- [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) — Referenced in ecpgb text
- [Nonyl Beta D Glucopyranoside](/xray-mp-wiki/reagents/nonyl-beta-d-glucopyranoside/) — Referenced in ecpgb text
- [Phosphatidic Acid](/xray-mp-wiki/reagents/lipids/phosphatidic-acid/) — Referenced in ecpgb text
