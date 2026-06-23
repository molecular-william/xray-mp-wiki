---
title: "IrtAB ABC Exporter from Mycobacterium thermoresistibile"
created: 2026-06-21
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-020-2136-9]
verified: false
---

# IrtAB ABC Exporter from Mycobacterium thermoresistibile

## Overview

IrtAB is a heterodimeric ATP-binding cassette (ABC) transporter from
Mycobacterium thermoresistibile that imports iron-bound mycobactin and
carboxymycobactin siderophores across the inner mycobacterial membrane. Despite
having an ABC exporter fold, IrtAB functions as an importer — an unusual feature
for this structural class. The protein comprises IrtA and IrtB subunits, each
containing a transmembrane domain (TMD) and a nucleotide-binding domain (NBD).
IrtA additionally features an N-terminal siderophore interaction domain (SID)
that binds flavin adenine dinucleotide (FAD) and reduces Fe(III)-mycobactin to
Fe(II), facilitating iron release. The structure reveals a collapsed inward-facing
cavity with a lateral opening to the inner membrane leaflet, positioning the SID
to capture membrane-embedded mycobactin.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-020-2136-9 | 6TEJ | 2.7 | P2₁ | IrtAB lacking SID domain (IrtAB(ΔSID)) with sybody Syb_NL5 | None (apo, inward-facing) |
| doi/10.1038##s41586-020-2136-9 | 6TEJ | 1.8 | P2₁ | Isolated SID domain (residues 1-...) | FAD |
| doi/10.1038##s41586-020-2136-9 | 6TEJ | 6.9 |  | Full-length IrtAB (including SID) |  |

## Expression and Purification

- **Expression system**: E. coli MC1061
- **Construct**: Full-length IrtAB with C-terminal GFP-His10 on IrtB; SID constructs with N-terminal His10-3C tag
- **Notes**: IrtAB expressed in E. coli; membrane vesicles prepared by ultracentrifugation

### Purification Workflow

- **Expression system**: E. coli MC1061
- **Expression construct**: Full-length IrtAB with C-terminal GFP-His10 tag on IrtB
- **Tag info**: C-terminal His10 tag on IrtB (cleavable by 3C protease)

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Ultracentrifugation | — | TBS (50 mM Tris pH 7.5, 150 mM NaCl) | Cells broken, debris removed at 8,000g, membranes pelleted at 170,000g |
| Membrane extraction | Solubilization | — | TBS + 1% (w/v) β-DDM | Extracted for 2 h at 4°C, followed by ultracentrifugation at 170,000g |
| Affinity chromatography | Ni-NTA | Ni-NTA gravity flow column | TBS with 20-250 mM imidazole gradient + 0.03% β-DDM | Imidazole added to 20 mM before loading; elution with 250 mM imidazole |
| Ion exchange chromatography | Anion exchange | Resource-Q (GE Healthcare) | 15 mM Tris pH 8.0, 20-350 mM NaCl gradient + 0.03% β-DDM | Protein eluted at ~150 mM NaCl |
| Size-exclusion chromatography | SEC | Superose 6 Increase 10/300 GL | TBS + Various (0.3% DM, 0.03% β-DDM, 0.03% LMNG) | Final polishing step; buffer exchanged to desired detergent during SEC |

**Final sample**: Purified IrtAB in 0.03% β-DDM for nanodisc reconstitution or crystallization


## Crystallization

### doi/10.1038##s41586-020-2136-9

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | IrtAB(ΔSID) with sybody Syb_NL5 in 0.03% β-DDM |
| Temperature | 20°C |
| Notes | IrtAB(ΔSID) was crystallized with the aid of sybody Syb_NL5; SID domain was crystallized separately |


## Biological / Functional Insights

### ABC exporter fold with import function

IrtAB adopts an ABC exporter fold despite functioning as an importer. The inward-facing cavity is collapsed at the upper region compared to canonical ABC exporters like TM287/288. TMH6 of IrtB protrudes into the cavity, TMH3 is strongly kinked, and the domain-swap helices (TMH4 and TMH5) of IrtA are bulged out, forming a lateral opening to the inner membrane leaflet where the SID is located.

### Siderophore Interaction Domain (SID) function

The SID is an N-terminal domain of IrtA with a flavoreductase fold and bound FAD. It reduces Fe(III)-mycobactin to Fe(II) using NADPH as electron donor, facilitating iron release. The SID is essential for iron utilization via Fe-MBT (membrane-bound mycobactin) but dispensable for Fe-cMBT (soluble carboxymycobactin), which can diffuse into the cytoplasm and be reduced by other ferric reductases.

### Transport and reduction mechanism

IrtAB imports both Fe-MBT and Fe-cMBT across the inner mycobacterial membrane. Fe-MBT, being lipid-bound, remains anchored to the inner membrane leaflet after import and is positioned for reduction by the SID. Fe-cMBT, being water-soluble, can diffuse freely into the cytoplasm. The transport mechanism likely involves a credit-card-swipe mechanism similar to the glycolipid ABC transporter PglK, with the lipid tail of Fe-MBT remaining embedded in the bilayer during import.


## Cross-References

- [Flavin Adenine Dinucleotide (FAD)](/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/) — FAD is the redox cofactor bound by the SID domain of IrtA
- [n-Decyl-beta-D-Maltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used in purification and crystallization of IrtAB
- [n-Dodecyl-beta-d-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane extraction and purification of IrtAB
- [Nanodisc Reconstitution](/xray-mp-wiki/methods/solubilization/nanodisc-reconstitution/) — IrtAB was reconstituted into nanodiscs for ATPase activity measurements
- [ABC Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — IrtAB belongs to the ABC transporter superfamily with an exporter fold
