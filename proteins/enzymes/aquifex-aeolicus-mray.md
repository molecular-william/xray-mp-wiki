---
title: Aquifex aeolicus MraY Phospho-MurNAc-pentapeptide Translocase
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-10957-9, doi/10.1126##science.1236501, doi/10.1038##nature17636]
verified: false
---

# Aquifex aeolicus MraY Phospho-MurNAc-pentapeptide Translocase

## Overview

MraY (phospho-MurNAc-pentapeptide translocase) from Aquifex aeolicus
(MraY_AA) catalyzes the transfer of phospho-MurNAc-pentapeptide from
UDP-MurNAc-pentapeptide (UM5A) to the lipid carrier undecaprenyl phosphate
(C55-P), producing Lipid I. This is the first committed membrane step of
bacterial peptidoglycan biosynthesis and is essential for bacterial
viability. MraY is the target of five classes of nucleoside natural
product antibiotics: liposidomycins/caprazamycins, capuramycins,
mureidomycins, muraymycins, and tunicamycins. Crystal structures of
MraY_AA in complex with carbacaprazamycin, capuramycin, and
3'-hydroxymureidomycin A revealed cryptic druggable hotspots on the
shallow inhibitor binding site, providing a barcode system (HS1-HS6)
for rational antibiotic design. Each inhibitor class exploits a unique
combination of binding pockets: the uridine pocket, uridine-adjacent
pocket, TM9b/Loop E pocket, hydrophobic groove (HS4), Mg2+ site (HS5),
and caprolactam pocket (unique to capuramycins).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1236501 | 4J72 | 3.50 | P212121 | Full-length MraY from Aquifex aeolicus (MraY_AA) | None (apo structure) |
| doi/10.1038##nature17636 | 5CKR | 2.95 | P212121 | Full-length MraY from Aquifex aeolicus (MraY_AA), His10-MBP fusion, PreScission cleavable | Muraymycin D2 (MD2) |
| doi/10.1038##s41467-019-10957-9 | 6OYH | 2.95 | P21 | Full-length MraY from Aquifex aeolicus (MraY_AA) with NB7 nanobody | Carbacaprazamycin |
| doi/10.1038##s41467-019-10957-9 | 6OYZ | 3.62 | P21 | Full-length MraY from Aquifex aeolicus (MraY_AA) with NB7 nanobody | Capuramycin |
| doi/10.1038##s41467-019-10957-9 | 6OZ6 | 3.70 | P21 | Full-length MraY from Aquifex aeolicus (MraY_AA) with NB7 nanobody | 3'-hydroxymureidomycin A |

## Expression and Purification

- **Expression system**: Escherichia coli C41(DE3)
- **Construct**: Full-length MraY_AA with N-terminal His10-MBP tag, PreScission Protease cleavable

### Purification Workflow

*Source: doi/10.1038##s41467-019-10957-9*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Cell lysis | Microfluidizer | — | Lysis buffer with protease inhibitors |  |
| 2. Membrane solubilization | Detergent solubilization | — | Solubilization buffer with dodecyl-maltoside (DDM) |  |
| 3. Affinity chromatography | Co2+-affinity column | Co2+-affinity resin |  | His10-MBP tag; tag cleaved overnight by PreScission Protease |
| 4. Size-exclusion chromatography | Gel filtration | Superdex 200 10/300 GL | 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 2 mM DTT, 5 mM decyl-maltoside (DM) | Final purification step at 4 C |

### Purification Workflow

*Source: doi/10.1038##nature17636*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Cell lysis | Microfluidizer | — |  |  |
| 2. Membrane solubilization | Solubilization with 40 mM DDM | — |  |  |
| 3. Affinity chromatography | Co2+-affinity column | Co2+-affinity resin |  | His10-MBP tag; cleaved overnight with PreScission Protease |
| 4. Size-exclusion chromatography | Gel filtration | Superdex 200 10/300 GL | 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 2 mM DTT, 5 mM DM |  |


## Crystallization

### doi/10.1038##s41467-019-10957-9

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | MraY_AA with NB7 nanobody (1:1.2 molar ratio) in 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 5 mM DDM, 2 mM DTT; plus 500 uM inhibitor |
| Reservoir | 40% PEG400, 50 mM MgCl2, 100 mM Na cacodylate pH 5.6 |
| Temperature | Room temperature (20 C) |
| Growth time | 3-5 days |
| Notes | Crystals in P21 space group with two MraY_AA dimers and 4 NB7 molecules per asymmetric unit |

### doi/10.1038##nature17636

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 10 mg/mL (250 uM) MraY_AA + 400-500 uM MD2 in 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 5 mM DDM, 2 mM DTT |
| Reservoir | 40% PEG400, 50 mM MgCl2, 100 mM Na cacodylate pH 5.6 |
| Growth time | 10-14 days |
| Notes | MD2 added to protein before crystallization; crystals flash frozen in liquid nitrogen |


## Biological / Functional Insights

### Chemical logic of MraY inhibition by five classes of nucleoside inhibitors

Crystal structures of MraY_AA bound to carbacaprazamycin, capuramycin, and 3'-hydroxymureidomycin A, together with previous MraY-muraymycin D2 and MraY-tunicamycin structures, reveal a barcode system of six druggable hotspots (HS1-HS6). Each inhibitor class exploits a unique combination: HS1 (uridine pocket - common to all), HS2 (uridine-adjacent pocket), HS3 (TM9b/Loop E pocket), HS4 (hydrophobic groove), HS5 (Mg2+ site), and HS6 (caprolactam pocket, unique to capuramycins).

### Cryptic druggable hotspots on a shallow binding surface

Unlike typical deep, enclosed enzyme active sites, the MraY inhibitor binding site is a shallow surface on the cytoplasmic face formed by TMs 5, 8, and 9b and Loops C, D, and E. Despite its shallowness, structural analyses revealed cryptic druggable pockets (uridine-adjacent pocket, caprolactam pocket, TM9b/Loop E helical pocket) that were not previously appreciated.

### Structural plasticity accommodates diverse inhibitor scaffolds

Comparison of the five inhibitor-bound structures shows how MraY's structural plasticity enables it to accommodate very different chemical moieties. For example, Loop E is ordered in carbacaprazamycin, muraymycin D2, and 3'-hydroxymureidomycin A complexes but disordered in the capuramycin complex. The uridine-adjacent pocket accommodates 5-aminoribose (carbacaprazamycin/muraymycin), meta-tyrosine (mureidomycin), or the caprolactam moiety (capuramycin).

### Guide for rational design of MraY-targeted antibiotics

The barcode system provides a framework for engineering improved pharmacological properties. Strategies include: (1) introducing additional pharmacophores to capture interactions with more HSs, (2) targeting HS5 (Mg2+ coordinating D265) for broader-spectrum activity, (3) modifying the caprolactam moiety of capuramycin/SQ641 to improve activity against M. tuberculosis and C. difficile, (4) exploiting the uridine-adjacent pocket (HS2) for selectivity over the eukaryotic GPT paralog.


## Cross-References

- [PNPT Superfamily](/xray-mp-wiki/concepts/pnpt-superfamily/) — MraY is the structurally characterized prototype of the PNPT superfamily; this paper extends structural understanding of inhibitor binding
- [Clostridium boltrea MraY with Tunicamycin](/xray-mp-wiki/proteins/enzymes/clostridium-boltrea-mray/) — Related MraY structure from a different species; comparison of inhibitor binding reveals species-specific differences
- [Capuramycin](/xray-mp-wiki/reagents/additives/capuramycin/) — Capuramycin is one of the three inhibitors whose MraY-bound structure is reported in this paper
- [Muraymycin D2](/xray-mp-wiki/reagents/additives/muraymycin-d2/) — Muraymycin D2 is another nucleoside inhibitor; its binding mode is compared with the three new structures
- [Tunicamycin](/xray-mp-wiki/reagents/antibiotics/tunicamycin/) — Tunicamycin binding is compared across structures; it uniquely targets the eukaryotic GPT paralog causing cytotoxicity
