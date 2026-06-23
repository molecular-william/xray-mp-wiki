---
title: MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)
created: 2026-06-02
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature06264, doi/10.1038##nature12232]
verified: false
---

# MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)

## Overview

MalG is a transmembrane subunit of the Escherichia coli [Maltose](/xray-mp-wiki/reagents/additives/maltose/) uptake system, an ATP-binding cassette (ABC) importer. MalG contains 6 transmembrane helices and 296 residues. Together with [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malF/), it forms the transmembrane domain of the transporter. MalG features a periplasmic loop (P3) that inserts into the maltose-binding protein cleft to dislodge bound [Maltose](/xray-mp-wiki/reagents/additives/maltose/), acting as a scoop mechanism. Its C-terminal tail (residues 290-296) packs along the Q loop of [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/), contributing to Q loop ordering and catalytic intermediate formation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature06264 | not specified | 2.8 | not specified | Full-length MalG (296 residues) from E. coli [Maltose](/xray-mp-wiki/reagents/additives/maltose/) transporter | [Maltose](/xray-mp-wiki/reagents/additives/maltose/) (transmembrane binding site) |

## Expression and Purification

- **Expression system**: E. coli HN741
- **Construct**: Full-length MalG with [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malF/) and [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/)(E159Q); engineered C-terminal His6 tag on [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | Terrific Broth + -- | Cells grown at 37 C, induced with 50 uM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 22 C for 24 h |
| Membrane isolation | High-pressure homogenization and centrifugation | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8, 100 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM MgCl2 + -- | 100,000g for 30 min at 4 C |
| Membrane solubilization | Detergent solubilization | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8, 100 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM MgCl2 + 0.35% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Solubilized for 4 h at room temperature; 100,000g for 20 min at 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Cobalt-[Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Cobalt-affinity resin (Clontech) | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8, 100 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Wash with 5 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), elute with 100 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Dialysis | Dialysis | -- | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8, 200 mM NaCl, 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | -- |
| Size-exclusion chromatography | SEC | -- | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8, 200 mM NaCl, 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | -- |

**Final sample**: Not specified
**Yield**: Not specified


## Crystallization

No crystallization described.

## Biological / Functional Insights

### P3 loop scoop mechanism

The periplasmic loop P3 of MalG inserts into the MBP sugar-binding cleft, physically dislodging the [Maltose](/xray-mp-wiki/reagents/additives/maltose/) molecule from the binding protein. This scoop mechanism ensures efficient transfer of sugar from MBP to the transmembrane subunits. A mutant with a 31-residue insertion in this loop was defective in transport but retained the ability to assemble a MalFGK2 complex. This insertion mechanism was also observed in the BtuCD-F structure.

### C-terminal tail interaction with MalK

Residues 290-296 of MalG pack along the Q loop (residues 83-89) of one [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) monomer, with the terminal carboxyl group of MalG making three hydrogen bonds with backbone atoms of the Q loop in the other monomer (residues S83, A85 and L86). Although not required for closure of the isolated [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) dimer, the coupling between [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) monomers by MalG contributes to Q loop ordering and may be important in forming the catalytic intermediate conformation.


## Cross-References

- [Maltose Transporter (MalFGK2)](/xray-mp-wiki/proteins/abc-transporters/maltose-transporter/) — Full transporter complex; EIIA^Glc binding structure solved in this paper
- [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malF/) — Partner transmembrane subunit; forms the TM cavity with MalG
- [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) — Cytoplasmic ATP-binding subunit; C-terminal tail of MalG inserts into MalK dimer
- [MBP (Escherichia coli Maltose-Binding Protein)](/xray-mp-wiki/proteins/abc-transporters/maltose-binding-protein/) — Periplasmic binding protein; MalG P3 loop inserts into MBP cleft
- [Maltose](/xray-mp-wiki/reagents/additives/maltose/) — Substrate transferred from MBP to MalG via scoop mechanism
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — Energy source; binds to MalK dimer interface
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane solubilization and purification
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — ABC transporter transport mechanism described in this paper
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Phasing method used to solve the structure
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
