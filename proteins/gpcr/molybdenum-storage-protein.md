---
title: Molybdenum Storage Protein (MOSTO)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-017-00630-4]
verified: false
---

# Molybdenum Storage Protein (MOSTO)

## Overview

Molybdenum storage protein (MOSTO) is a heterohexameric (αβ)₃ cage-like protein complex from Azotobacter vinelandii that stores molybdenum in the form of polyoxomolybdate clusters bound inside the cage. It is highly sensitive to X-ray radiation damage under conventional cryo-crystallographic conditions, making it an ideal test case for serial millisecond crystallography (SMX) at room temperature. The SMX structure was determined at 1.3 Å resolution using data collected in a single 6-hour synchrotron shift, demonstrating that SMX effectively mitigates radiation damage in metalloproteins.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-017-00630-4 | 5NJM | 1.3 | Not specified | Heterologously produced in E. coli BL21 (DE3) with molecular chaperones, purified via Strep-tag affinity chromatography, ion exchange, and size exclusion chromatography. Crystallized from 0.1 M sodium citrate pH 5.6, 1.4 M NH₄H₂PO₄, 20% glycerol. | [Polyoxomolybdate Cluster](/xray-mp-wiki/reagents/ligands/polyoxomolybdate/) |

## Expression and Purification

- **Expression system**: E. coli BL21 (DE3)
- **Construct**: Full-length MOSTO with molecular chaperone coexpression; Strep-tag for affinity purification
- **Notes**: Protein purified via Strep-tag affinity, ion exchange (IEX), and size exclusion chromatography (SEC). Buffer: 50 mM MOPS, 50 mM NaCl pH 6.5.
- **Induction**: Not specified
- **Media**: Not specified

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Strep-tag affinity chromatography | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | StrepTactin | 50 mM MOPS, 50 mM NaCl pH 6.5 + None | First capture step |
| Ion exchange chromatography | Ion exchange chromatography | Not specified | 50 mM MOPS, 50 mM NaCl pH 6.5 | Intermediate purification step |
| Size exclusion chromatography | [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Not specified | 50 mM MOPS, 50 mM NaCl pH 6.5 | Final polishing step. Prior to crystallization, 1 mM ATP, 1 mM MgSO₄, and 1 mM Na₂MoO₄ were added. |


## Crystallization

### doi/10.1038##s41467-017-00630-4

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Protein sample | Purified MOSTO at 25 mg/mL with 1 mM ATP, 1 mM MgSO₄, 1 mM Na₂MoO₄ |
| Reservoir | 0.1 M sodium citrate pH 5.6, 1.4 M NH₄H₂PO₄, 20% glycerol |
| Temperature | 18 °C |
| Growth time | Not specified |
| Notes | Crystallization conditions were modified to produce sub-50 µm crystals suitable for SMX: 1.1–1.7 M NH₄H₂PO₄ gradient screen. Optimal: 1.4 M NH₄H₂PO₄. Drops: 2+2 µL. Crystals harvested by pooling hanging drops and mixing with ~70% monoolein through a 400 µm LCP coupler. |


## Biological / Functional Insights

### SMX overcomes radiation damage in metalloprotein crystallography

MOSTO is highly radiation-sensitive due to its polyoxomolybdate clusters. Conventional cryo-crystallography causes severe radiation damage before complete data can be collected. SMX distributes the dose over approximately 240,000 crystals, yielding a 1.3 Å room-temperature structure with minimal radiation damage. This demonstrates SMX as a general method for radiation-sensitive metalloproteins.


## Cross-References

- [Serial Millisecond Crystallography (SMX)](/xray-mp-wiki/concepts/serial-millisecond-crystallography/) — SMX was essential for the MOSTO structure determination, overcoming radiation damage in this metalloprotein.
