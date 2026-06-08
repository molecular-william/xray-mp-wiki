---
title: MalK (Escherichia coli Maltose Transporter ATPase Subunit)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature06264]
verified: false
---

# MalK (Escherichia coli Maltose Transporter ATPase Subunit)

## Overview

MalK is the cytoplasmic ATP-binding cassette (NBD) subunit of the Escherichia coli maltose uptake system, an ATP-binding cassette (ABC) importer. MalK forms a homodimer that hydrolyzes ATP to power substrate translocation. In the nucleotide-free resting state, the NBDs are separated. Upon ATP binding, the NBDs close into a tight dimer with two ATP molecules engulfed along the dimer interface. Each ATP contacts Walker A and B motifs from one monomer and the LSGGQ signature motif of the opposite monomer. The E159Q mutation prevents ATP hydrolysis, trapping the transporter in a catalytic intermediate conformation for structural studies.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature06264 | not specified | 2.8 | not specified | MalK(E159Q) dimer from E. coli maltose transporter | ATP (2 molecules at dimer interface) |
| doi/10.1038##nature06264 | 1Q12 | not specified | not specified | Wild-type MalK dimer (ATP-bound, closed form) | ATP |

## Expression and Purification

- **Expression system**: E. coli HN741
- **Construct**: Full-length MalK with E159Q mutation; engineered C-terminal His6 tag

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

### ATP-bound closed MalK dimer

Two ATP molecules are bound along the MalK dimer interface, contacting residues in the Walker A and B motifs from one monomer and the LSGGQ motif of the opposite monomer. The structure of MalK2(E159Q) in the complex is essentially identical to that of isolated wild-type MalK dimer in the ATP-bound closed form (RMSD 0.6 A for 740 C-alpha positions). This closed NBD architecture is shared with the bacterial exporter Sav1866, suggesting importers and exporters share a common mechanism of coupling ATP hydrolysis to substrate translocation.

### MalK-TMD interface through EAA motif

MalK binds to MalF and MalG primarily through contacts with the EAA motif (EAA-X(3)-G) of the TM subunits. The coupling helix of the EAA loop docks into a surface cleft on each MalK subunit, formed by two helices from the helical subdomain, the helix following the Walker A motif, and residues in the Q loop. The glutamate in the EAA loop engages in a salt bridge with R47 on MalK. Hydrophobic residues M405 (MalF) and L194 (MalG) insert into a hydrophobic pocket on MalK formed by A50, L52, A73, V77, M79 and F81.

### Q loop ordering by MalG

In the intact transporter, the Q loop of MalK (residues 79-90) becomes well ordered and contains a beta-strand, unlike the flexible Q loop observed in isolated MalK structures. The MalG C-terminal tail (residues 290-296) packs along the Q loop of one MalK monomer, with the terminal carboxyl group making three hydrogen bonds with backbone atoms of the Q loop in the other monomer (S83, A85, L86). This coupling contributes to Q loop ordering and formation of the catalytic intermediate.


## Cross-References

- [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/malF/) — TM subunit; EAA motif coupling helix contacts MalK
- [MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/malG/) — TM subunit; C-terminal tail inserts into MalK dimer interface
- [MBP (Escherichia coli Maltose-Binding Protein)](/xray-mp-wiki/proteins/maltose-binding-protein/) — Periplasmic binding protein; stimulates ATP hydrolysis upon docking
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — Energy source; 2 ATP molecules bound at MalK dimer interface
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane solubilization and purification
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — ABC transporter transport mechanism described in this paper
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Phasing method used to solve the structure
