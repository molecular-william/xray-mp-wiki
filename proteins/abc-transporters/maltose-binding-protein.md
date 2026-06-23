---
title: MBP (Escherichia coli Maltose-Binding Protein)
created: 2026-06-02
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature06264, doi/10.1038##nature12232, doi/10.1073##pnas.1311407110, doi/10.1126##science.1200767]
verified: false
---

# MBP (Escherichia coli Maltose-Binding Protein)

## Overview

MBP (maltose-binding protein) is the periplasmic binding protein component of
the Escherichia coli maltose uptake system, an ATP-binding cassette (ABC)
importer. MBP binds maltose and malto-oligosaccharides (up to 7 glucose units)
with high affinity in a cleft between two lobes that completely engulf the
substrate upon lobe rotation. MBP docks onto the transmembrane subunits
[MalF](/xray-mp-wiki/proteins/abc-transporters/malF/) and [MalG](/xray-mp-wiki/proteins/abc-transporters/malG/),
delivering the substrate and stimulating ATP hydrolysis. In the maltose
transporter complex, MBP remains in its open, ligand-free conformation,
stabilized by interactions with the TM subunits, which promotes sugar release
and ensures unidirectional translocation. Crystal structures of MBP bound to
maltoheptaose show the first four glucosyl units from the reducing end (g1-g4)
bound in the MBP binding groove through 14 direct hydrogen bonds and 118 van
der Waals interactions with a continuous surface of four stacking aromatic
residues.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature06264 | not specified | 2.8 | — | Open apo conformation of MBP from E. coli maltose transporter |  |
| doi/10.1038##nature06264 | 1OMP |  | — | Open apo MBP (search model for molecular replacement) |  |
| doi/10.1038##nature06264 | 1JW5 |  | — |  | maltose |

## Expression and Purification

- **Expression system**: E. coli BAR1000
- **Construct**: MBP under mal promoter; increased expression strain
- **Notes**: Cells cultured overnight with maltose induction

### Purification Workflow

- **Expression system**: E. coli BAR1000
- **Expression construct**: MBP under mal promoter

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | — | Luria-Bertani medium supplemented with 4 g/L maltose | Cells cultured overnight with maltose induction |
| Osmotic shock | Osmotic shock | — | 30 mM Tris-HCl pH 8, 20% sucrose; then ice-cold 5 mM MgSO4 | Cells resuspended in sucrose buffer, centrifuged, then resuspended in MgSO4 to release periplasmic MBP |
| Ion-exchange chromatography | Ion-exchange chromatography | Source 15Q (GE Healthcare) | 20 mM Tris-HCl pH 8 | FPLC (AKTA) at 4 C |
| Size-exclusion chromatography | SEC | Superdex 200 (GE Healthcare) | 20 mM Tris-HCl pH 8 | FPLC (AKTA) at 4 C |

**Final sample**: 1 mg/mL in 20 mM Tris-HCl pH 8


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Open apo conformation in the transporter complex

MBP docks onto MalF and MalG in an open, ligand-free conformation at the periplasmic surface. The open form has lower affinity for maltose because it makes fewer contacts than the closed form. Interactions with the TM subunits stabilize MBP in the open state, presumably to promote sugar release. The absence of maltose electron density in the MBP binding site demonstrates that maltose has been translocated to the TM subunits. This is a key feature of the catalytic intermediate state.

### MBP as a cap for unidirectional transport

MBP serves as a cap at the periplasmic entrance of the translocation cavity, ensuring unidirectional translocation of the sugar molecule. Two notable interactions include the insertion of the MalG periplasmic loop (P3) into the MBP sugar-binding cleft and contacts by mostly the N-lobe of MBP with a large periplasmic loop (P2) of MalF that folds into an Ig-like domain and extends about 30 A away from the membrane surface. MBP also stimulates ATP hydrolysis, ensuring that substrate is transported during each cycle.

### Maltose scoop mechanism by MalG P3 loop

Insertion of the MalG P3 loop into the MBP sugar-binding site physically dislodges the sugar from the binding protein. Modeling a sugar molecule into the binding site based on the open maltose-bound MBP structure (1JW5) shows that even the smallest substrate, maltose, clashes with the P3 loop. This scoop mechanism ensures efficient transfer of substrate from MBP to the transmembrane subunits.

### MBP binding of maltoheptaose and interaction with MalG

In the pretranslocation state bound with maltoheptaose, the first four glucosyl units from the reducing end (g1-g4) are bound in the MBP binding groove. The maltoheptaose forms 14 direct hydrogen bonds with polar residues and 118 van der Waals interactions with MBP. Four stacking aromatic residues form a continuous surface matching the curvature of the left-handed helix of the malto-oligosaccharide. The MalG scoop loop reaches to the reducing end via conserved Q256, which hydrogen bonds to OH6 and ring oxygen of the g1 unit.


## Cross-References

- [Maltose Transporter MalFGK2 (E. coli)](/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/) — MBP delivers substrate to the MalFGK2 ABC transporter complex
- [Maltose](/xray-mp-wiki/reagents/additives/maltose/) — Physiological substrate; binds in MBP cleft
- [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) — MBP stimulates ATP hydrolysis upon delivering substrate to TM subunits
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used for MBP purification and storage
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — ABC transporter transport mechanism
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — MBP structure (1OMP) used as search model for phasing
