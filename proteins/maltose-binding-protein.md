---
title: MBP (Escherichia coli Maltose-Binding Protein)
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature06264]
verified: false
---

# MBP (Escherichia coli Maltose-Binding Protein)

## Overview

MBP (maltose-binding protein) is the periplasmic binding protein component of the Escherichia coli maltose uptake system, an ATP-binding cassette (ABC) importer. MBP binds maltose and malto-oligosaccharides (up to 7 glucose units) with high affinity in a cleft between two lobes that completely engulf the substrate upon lobe rotation. MBP docks onto the transmembrane subunits MalF and MalG, delivering the substrate and stimulating ATP hydrolysis. In the maltose transporter complex, MBP remains in its open, ligand-free conformation, stabilized by interactions with the TM subunits, which promotes sugar release and ensures unidirectional translocation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature06264 | not specified | 2.8 | not specified | Open apo conformation of MBP from E. coli maltose transporter | none (open, ligand-free form) |
| doi/10.1038##nature06264 | 1OMP | not specified | not specified | Open apo MBP (search model for molecular replacement) | none |
| doi/10.1038##nature06264 | 1JW5 | not specified | not specified | Open maltose-bound MBP (used for modeling sugar transfer) | maltose |

## Expression and Purification

- **Expression system**: E. coli BAR1000
- **Construct**: MBP under mal promoter; increased expression strain

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | Luria-Bertani medium supplemented with 4 g/L maltose + -- | Cells cultured overnight with maltose induction |
| Osmotic shock | Osmotic shock | -- | 30 mM Tris-HCl pH 8, 20% sucrose; then ice-cold 5 mM MgSO4 + -- | Cells resuspended in sucrose buffer, centrifuged, then resuspended in MgSO4 to release periplasmic MBP |
| Ion-exchange chromatography | Ion-exchange chromatography | Source 15Q (GE Healthcare) | 20 mM Tris-HCl pH 8 + -- | FPLC (AKTA) at 4 C |
| Size-exclusion chromatography | SEC | Superdex 200 (GE Healthcare) | 20 mM Tris-HCl pH 8 + -- | FPLC (AKTA) at 4 C |

**Final sample**: 1 mg/mL in 20 mM Tris-HCl pH 8
**Yield**: Not specified


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Open apo conformation in the transporter complex

MBP docks onto MalF and MalG in an open, ligand-free conformation at the periplasmic surface. The open form has lower affinity for maltose because it makes fewer contacts than the closed form. Interactions with the TM subunits stabilize MBP in the open state, presumably to promote sugar release. The absence of maltose electron density in the MBP binding site demonstrates that maltose has been translocated to the TM subunits. This is a key feature of the catalytic intermediate state.

### MBP as a cap for unidirectional transport

MBP serves as a cap at the periplasmic entrance of the translocation cavity, ensuring unidirectional translocation of the sugar molecule. Two notable interactions include the insertion of the MalG periplasmic loop (P3) into the MBP sugar-binding cleft and contacts by mostly the N-lobe of MBP with a large periplasmic loop (P2) of MalF that folds into an Ig-like domain and extends about 30 A away from the membrane surface. MBP also stimulates ATP hydrolysis, ensuring that substrate is transported during each cycle.

### Maltose scoop mechanism by MalG P3 loop

Insertion of the MalG P3 loop into the MBP sugar-binding site physically dislodges the sugar from the binding protein. Modeling a sugar molecule into the binding site based on the open maltose-bound MBP structure (1JW5) shows that even the smallest substrate, maltose, clashes with the P3 loop. This scoop mechanism ensures efficient transfer of substrate from MBP to the transmembrane subunits.


## Cross-References

- [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/malF/) — TM subunit; MBP N-lobe contacts MalF P2 loop (Ig-like domain)
- [MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/malG/) — TM subunit; MalG P3 loop scoops maltose from MBP binding cleft
- [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/malK/) — Cytoplasmic ATPase; MBP docks onto MalF/MalG and stimulates ATP hydrolysis
- [Maltose](/xray-mp-wiki/reagents/additives/maltose/) — Physiological substrate; binds in MBP cleft and transmembrane cavity
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — MBP stimulates ATP hydrolysis upon delivering substrate to TM subunits
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used for MBP purification and storage
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — ABC transporter transport mechanism described in this paper
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — MBP structure (1OMP) used as search model for phasing
