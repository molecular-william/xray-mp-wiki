---
title: E. coli MlaA Outer Membrane Lipoprotein
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.03.019]
verified: false
---

# E. coli MlaA Outer Membrane Lipoprotein

## Overview

MlaA is an outer membrane lipoprotein from Escherichia coli that forms a complex with the outer membrane porin proteins OmpC and OmpF. MlaA is a key component of the Mla lipid transport system, where it functions at the outer membrane to receive phospholipids from the periplasmic shuttle protein MlaC and insert them into the outer membrane leaflet. MlaA is encoded elsewhere in the genome, separate from the mlaFEDCB operon, and is essential for maintaining outer membrane lipid asymmetry in Gram-negative bacteria. The MlaA-OmpC/OmpF complex represents the outer membrane component of the Mla lipid transport system.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2017.03.019 | not determined | not determined | not applicable | Mature MlaA (signal peptide-cleaved, residues 1-251) in complex with OmpF porin | none |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Mature MlaA (residues 1-251), signal peptide-cleaved, cloned into custom pET vector (pDCE587)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Co-expression and solubilization | Co-expression of MlaA with OmpF, solubilization with detergent | -- | 50 mM Tris pH 8.0, 300 mM NaCl + n-Dodecyl-beta-D-maltopyranoside (DDM) | MlaA-OmpF complex solubilized from outer membrane fraction |
| Complex purification | Affinity chromatography and gel filtration | Not specified | 20 mM Tris pH 8.0, 150 mM NaCl + DDM | MlaA-OmpC/OmpF complex purified for biolayer interferometry studies |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### MlaA-OmpC/OmpF outer membrane complex

MlaA forms a stable complex with the outer membrane porin proteins OmpC and OmpF.
This complex serves as the outer membrane anchor of the Mla lipid transport system,
receiving phospholipids from the periplasmic shuttle protein MlaC and inserting
them into the outer membrane leaflet. The MlaA-OmpF complex was used in biolayer
interferometry experiments to demonstrate direct interaction with MlaC.

### Direct interaction with periplasmic lipid shuttle MlaC

Biolayer interferometry (Octet RED384) demonstrated that MlaC interacts directly
with the MlaA-OmpC/OmpF outer membrane complex. Biotinylated MlaC loaded onto
streptavidin-coated biosensors showed binding to the MlaA-OmpF complex, supporting
the model where MlaC ferries lipids from the inner membrane MlaFEDB complex to
the outer membrane MlaA-OmpC/OmpF complex. This interaction is essential for maintaining
outer membrane lipid asymmetry.

### Non-essential but critical for outer membrane integrity

While individual MCE system components are non-essential for E. coli growth in rich
media, mutations in mla genes result in increased sensitivity to SDS and EDTA,
indicative of outer membrane defects. The MlaA-OmpC/OmpF complex is required for
the complete Mla system to function, and its disruption leads to accumulation of
phospholipids in the outer leaflet of the outer membrane, disrupting lipid asymmetry.


## Cross-References

- [E. coli MlaC Lipid-Binding Protein](/xray-mp-wiki/proteins/mlaC/) — MlaC directly interacts with MlaA-OmpF complex to deliver lipids to the outer membrane
- [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/mlaD/) — MlaA is the outer membrane partner of MlaD at the inner membrane in the Mla system
- [E. coli YebT Tube-like MCE Protein](/xray-mp-wiki/proteins/yebT/) — YebT may associate with YebS in the inner membrane and PqiC in the outer membrane similarly
- [E. coli PqiB Syringe-like MCE Protein](/xray-mp-wiki/proteins/pqiB/) — PqiB may interact with outer membrane lipoprotein PqiC similarly to MlaA
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM used for MlaA-OmpF complex solubilization from membranes
- [MCE Protein Family](/xray-mp-wiki/concepts/mce-protein-family/) — MlaA is a key component of the Mla system, an MCE protein family member
