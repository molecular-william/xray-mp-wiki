---
title: PCAT1 (Peptidase-Containing ABC Transporter from Clostridium thermocellum)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature14623]
verified: false
---

# PCAT1 (Peptidase-Containing ABC Transporter from Clostridium thermocellum)

## Overview

PCAT1 is a peptidase-containing ATP-binding cassette (ABC) transporter from Clostridium thermocellum that functions as both a maturation protease and exporter for bacteriocin-like polypeptides. PCAT1 represents a dual-function ABC transporter that processes and secretes small proteins. It contains two N-terminal peptidase domains (family C39 cysteine protease), two transmembrane domains (TMDs) forming a large alpha-helical barrel translocation pathway, and two nucleotide-binding domains (NBDs) that hydrolyze ATP. The crystal structures reveal an inward-facing ATP-free conformation with a large transmembrane tunnel sufficient to accommodate small folded proteins, and an ATP-bound occluded conformation where the peptidase domains dissociate. ATP binding alternates access to the transmembrane pathway and regulates protease activity, thereby coupling substrate processing to translocation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature14623 | TBD | 3.6 A | P2(1)2(1)2(1) | Full-length PCAT1 from Clostridium thermocellum (residues 1-727), expressed in E. coli BL21(DE3) codon plus (RIL) cells, N-terminal GST tag removed by TEV protease | None (ATP-free form) |
| doi/10.1038##nature14623 | TBD | 4.1 A | C222(1) | Full-length PCAT1 from Clostridium thermocellum (residues 1-727), expressed in E. coli BL21(DE3) codon plus (RIL) cells, N-terminal GST tag removed by TEV protease | None (ATP-free form, alternative crystal form) |
| doi/10.1038##nature14623 | TBD | 5.5 A | P4(2)2(1)2 | Full-length PCAT1 E648Q mutant from Clostridium thermocellum (residues 1-727), expressed in E. coli BL21(DE3) codon plus (RIL) cells, N-terminal GST tag removed by TEV protease | ATPγS (bound, hydrolysis-deficient mutant) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3) codon plus (RIL) cells
- **Construct**: Full-length PCAT1 (residues 1-727) from Clostridium thermocellum, N-terminal GST tag with TEV protease cleavage site; also isolated peptidase domain (residues 1-148) as GST fusion

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and induction | E. coli expression in Terrific Broth | -- | Terrific Broth (Novagen) supplemented with ampicillin + -- | Induced with 100 μM IPTG at 16 C for 24 h |
| Membrane isolation | High-pressure homogenization and ultracentrifugation | -- | 50 mM Tris-HCl pH 7.0, 500 mM NaCl, 10% glycerol + -- | Cells lysed by two passes through Emulsiflex-C3 homogenizer, membranes pelleted at 80,000g for 40 min |
| Membrane solubilization | Detergent solubilization | -- | 50 mM Tris-HCl pH 7.0, 500 mM NaCl, 10% glycerol, 5 mM DTT + [DDM](/xray-mp-wiki/reagents/detergents/ddm) (n-dodecyl-beta-D-maltopyranoside) at 1% | Solubilized at 4 C for 2 h, insoluble material removed at 70,000g for 20 min |
| GST affinity purification | Glutathione Sepharose affinity chromatography | Glutathione Sepharose 4B (GE Healthcare) | 50 mM Tris-HCl pH 7.0, 500 mM NaCl, 10% glycerol, 5 mM DTT, 2 mM [UDM](/xray-mp-wiki/reagents/detergents/udm) (n-undecyl-beta-D-maltopyranoside) + [UDM](/xray-mp-wiki/reagents/detergents/udm) | On-column TEV protease cleavage overnight at 4 C to remove GST tag |
| Size-exclusion chromatography | SEC on Superdex 200 | Superdex 200 16/60 (GE Healthcare) | 20 mM Tris-HCl pH 7.0, 150 mM NaCl, 2 mM [UDM](/xray-mp-wiki/reagents/detergents/udm), 5 mM DTT + [UDM](/xray-mp-wiki/reagents/detergents/udm) | Final purification step |


## Crystallization

### doi/10.1038##nature14623

| Parameter | Value |
|---|---|
| Method | Lipidic bicelle method |
| Protein sample | PCAT1 at undetermined concentration in [UDM](/xray-mp-wiki/reagents/detergents/udm), reconstituted into DMPC/CHAPSO bicelles (35% bicelle stock, 2.8:1 DMPC:CHAPSO) |
| Reservoir | Not explicitly reported |
| Temperature | 20 C |
| Growth time | Not reported |
| Cryoprotection | Cryocooled |
| Notes | Crystal form 1, space group P2(1)2(1)2(1), unit cell a=87.6, b=89.7, c=296.6 A. Resolution 3.6 A. R_work/R_free not explicitly reported. Two monomers per asymmetric unit forming a dimer. |

| Parameter | Value |
|---|---|
| Method | Lipidic bicelle method |
| Protein sample | PCAT1 at undetermined concentration in [UDM](/xray-mp-wiki/reagents/detergents/udm), reconstituted into DMPC/CHAPSO bicelles |
| Reservoir | Not explicitly reported |
| Temperature | 20 C |
| Growth time | Not reported |
| Cryoprotection | Cryocooled |
| Notes | Crystal form 2, space group C222(1), unit cell a=138.4, b=178.4, c=90.2 A. Resolution 4.1 A. One monomer per asymmetric unit. |

| Parameter | Value |
|---|---|
| Method | Lipidic bicelle method |
| Protein sample | PCAT1 E648Q mutant at undetermined concentration, reconstituted into DMPC/CHAPSO bicelles |
| Reservoir | Not explicitly reported |
| Temperature | 20 C |
| Growth time | Not reported |
| Cryoprotection | Cryocooled |
| Notes | E648Q mutant in complex with ATPγS. Space group P4(2)2(1)2, unit cell a=b=230.0, c=89.4 A. Resolution 5.5 A. R_work=30%, R_free=31%. Peptidase domains disordered (no electron density observed). |


## Biological / Functional Insights

### Dual-function ABC transporter architecture

PCAT1 is a dual-function ABC transporter containing both a protease domain for substrate processing and a translocation channel for secretion. The full-length transporter is a homodimer with each subunit containing an N-terminal peptidase domain (family C39 cysteine protease), six transmembrane helices, and a C-terminal nucleotide-binding domain. The overall architecture resembles other ABC exporters with the TMDs and NBDs forming the core transporter, while the peptidase domains dock onto the cytoplasmic openings of the TM tunnel.

### Large alpha-helical barrel translocation pathway

The translocation pathway is a large alpha-helical barrel traversing nearly the entire lipid bilayer. The cross-section is rhomboidal with an area of approximately 440 A^2 in the membrane-spanning region, sufficient to accommodate small folded proteins (e.g., BPTI). The interior surface is lined with charged residues, providing a hydrophilic environment for the cargo. Near the extracellular surface, hydrophobic residues I190, F194, and L426 form a closed gate.

### Peptidase domain docking and substrate processing

The peptidase domains dock onto the lateral cytoplasmic openings of the TM tunnel, with the catalytic site (Cys21, His100, Asp106) facing the gateway. This positions the domains perfectly to process the leader peptide by enzymatic cleavage while recruiting the substrate into the translocation pathway. The buried surface area at the interface is small (~980 A^2), suggesting weak association.

### ATP binding regulates access and protease activity

ATP binding (ATPγS to E648Q mutant) induces a major conformational change: the NBDs rotate inward to form a closed dimer, TM helices 3-6 shift toward the molecular center, narrowing the TM pathway and closing the lateral openings. The extracellular gate remains closed, resulting in an occluded cavity. In this conformation, the peptidase domains dissociate from the transporter, explaining the reduced protease activity upon ATP binding.

### Primed NBD dimer

In the ATP-free form, the NBD dimer resembles the pre-translocation state of the maltose transporter (MalK), a substrate-induced conformation primed for ATP hydrolysis. Key features include the Walker A serine and switch histidine at the dimer interface making contact with the D-loop of the opposite NBD. This pre-arranged configuration explains why substrate does not stimulate ATP hydrolysis in PCAT1.

### Alternating-access model for protein translocation

Based on the two conformations, the paper proposes an alternating-access model: (1) In the absence of ATP, the substrate is recruited through the peptidase domain and inserted into the translocation pathway. Proteolytic cleavage removes the leader peptide. (2) ATP binding alters the access of the translocation pathway and disengages the peptidase domains. (3) ATP hydrolysis resets the transporter to the inward-facing conformation for the next cycle.


## Cross-References

- [TM287/288 (ABC exporter from Thermotoga maritima)](/xray-mp-wiki/proteins/abc-transporters/tm287-288/) — Homologous ABC exporter used as molecular replacement search model for TMD and NBD
- [ABC Transporters](/xray-mp-wiki/concepts/abc-transporters/) — PCAT1 is a member of the ABC transporter family with dual peptidase/transporter function
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Lipidic bicelle method used for crystallization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Used for membrane solubilization
