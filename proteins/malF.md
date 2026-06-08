---
title: MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature06264]
verified: false
---

# MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)

## Overview

MalF is a transmembrane subunit of the Escherichia coli maltose uptake system, an ATP-binding cassette (ABC) importer. MalF contains 8 transmembrane helices and 514 residues. Together with MalG, it forms the transmembrane domain of the transporter that creates a solvent-filled cavity for substrate translocation. MalF contributes the substrate-binding site within the transmembrane domain, where aromatic residues stack with the sugar rings of maltose. Six of the ten residues contacting maltose had been previously identified through genetic studies to be critical for transport.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature06264 | not specified | 2.8 | not specified | Full-length MalF (514 residues) from E. coli maltose transporter | maltose (transmembrane binding site) |

## Expression and Purification

- **Expression system**: E. coli HN741
- **Construct**: Full-length MalF with MalG and MalK(E159Q); engineered C-terminal His6 tag on MalK

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | Terrific Broth + -- | Cells grown at 37 C, induced with 50 uM IPTG at 22 C for 24 h |
| Membrane isolation | High-pressure homogenization and centrifugation | -- | 20 mM Tris-HCl pH 8, 100 mM NaCl, 10% glycerol, 5 mM MgCl2 + -- | 100,000g for 30 min at 4 C |
| Membrane solubilization | Detergent solubilization | -- | 20 mM Tris-HCl pH 8, 100 mM NaCl, 10% glycerol, 5 mM MgCl2 + 0.35% DDM | Solubilized for 4 h at room temperature; 100,000g for 20 min at 4 C |
| Affinity chromatography | Cobalt-affinity chromatography | Cobalt-affinity resin (Clontech) | 10 mM Tris-HCl pH 8, 100 mM NaCl, 10% glycerol, 0.01% DDM + 0.01% DDM | Wash with 5 mM imidazole, elute with 100 mM imidazole |
| Dialysis | Dialysis | -- | 10 mM Tris-HCl pH 8, 200 mM NaCl, 0.01% DDM + 0.01% DDM | -- |
| Size-exclusion chromatography | SEC | -- | 10 mM Tris-HCl pH 8, 200 mM NaCl, 0.01% DDM + 0.01% DDM | -- |

**Final sample**: Not specified
**Yield**: Not specified


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Intertwined transmembrane helix architecture

MalF and MalG assemble into two crescent-shaped structures with concave surfaces facing each other, enclosing maltose about halfway into the lipid bilayer. TM helices 1-3 of MalF cross over the dimer interface to contact TM2-6 of MalG, while TM1 of MalG packs against the helical bundle formed by TM4-8 of MalF. A pseudo-twofold symmetry is observed in the core region, with TM3-8 of MalF related to TM1-6 of MalG by about 180 degrees rotation.

### Transmembrane substrate-binding site

MalF contains the substrate-binding site within the transmembrane domain. Aromatic side chains of MalF Y383 and F436 make stacking interactions with the sugar rings of maltose. Hydrogen-bonding and van der Waals interactions with MalF Y325, S329, N376, L379, G380, S433, N437 and N440 confer specificity and stabilize substrate binding. Six of the 10 residues contacting maltose had been identified through genetic studies to severely decrease or eliminate maltose transport.


## Cross-References

- [MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/malG/) — Partner transmembrane subunit; forms the TM cavity with MalF
- [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK/) — Cytoplasmic ATP-binding subunit; EAA motif coupling
- [MBP (Escherichia coli Maltose-Binding Protein)](/xray-mp-wiki/proteins/maltose-binding-protein/) — Periplasmic binding protein; docks onto MalF and MalG
- [Maltose](/xray-mp-wiki/reagents/additives/maltose/) — Substrate bound in the transmembrane cavity of MalF
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — Energy source; binds to MalK dimer interface
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane solubilization and purification
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — ABC transporter transport mechanism described in this paper
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Phasing method used to solve the structure
