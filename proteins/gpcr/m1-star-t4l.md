---
title: "M1-StaR-T4L"
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2021.11.001]
verified: false
---

# M1-StaR-T4L

## Overview

M1-StaR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) is a thermostabilized, engineered construct of the human [M1 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/) designed for X-ray crystallography. It combines multiple stability-enhancing modifications: a chimeric M4 N-terminus, 12 thermostabilizing mutations (StaR), C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), and [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) ([T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)) fusion in the third intracellular loop (ICL3). This construct enabled the determination of three high-resolution structures of the M1 receptor bound to orthosteric agonists ([77-LH-28-1](/xray-mp-wiki/reagents/ligands/77-lh-28-1/), [HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/), [GSK1034702](/xray-mp-wiki/reagents/ligands/gsk1034702/)), providing key insights into muscarinic receptor activation and agonist selectivity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2021.11.001 | 6ZFZ | 2.17 A | C 2 2 21 | M1-StaR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) (12 thermostabilizing mutations, M4 N-terminus chimera, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) in ICL3) | [77-LH-28-1](/xray-mp-wiki/reagents/ligands/77-lh-28-1/) |
| doi/10.1016##j.cell.2021.11.001 | 6ZG4 | 2.17 A | C 2 2 21 | M1-StaR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) (12 thermostabilizing mutations, M4 N-terminus chimera, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) in ICL3) | [HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/) |
| doi/10.1016##j.cell.2021.11.001 | 6ZG9 | 2.17 A | C 2 2 21 | M1-StaR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) (12 thermostabilizing mutations, M4 N-terminus chimera, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) in ICL3) | [GSK1034702](/xray-mp-wiki/reagents/ligands/gsk1034702/) |

## Expression and Purification

- **Expression system**: Sf21 insect cells (baculovirus expression vector system)
- **Construct**: M1-StaR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) construct with N-terminal GP64 signal sequence, chimeric M4 N-terminus (residues 1-95 of M4 replacing residues 1-87 of M1), residues 88-438 of M1 receptor, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (residues 439-460 removed), [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) inserted into ICL3 between residues 219 and 354, and C-terminal deca-histidine tag. The StaR variant contains 12 thermostabilizing mutations: F27A, T32A, V46L, L64A, T95A, W101A, S112A, A143L, A196T, K362A, A364L, S411A.


### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and infection | Sf21 cells infected with baculovirus at multiplicity of infection 2, harvested 48 hours post-infection | -- | -- + -- | Cells grown at 27 degrees Celsius with constant shaking in ESF 921 medium supplemented with 10% FBS and 1% penicillin/streptomycin |
| Cell disruption and membrane preparation | Cell disruption at 15000 psi using microfluidizer, membranes pelleted by ultracentrifugation at 200000 g for 50 min, high salt washes | -- | PBS, 5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/), protease inhibitor cocktail; wash buffer: PBS, 1 M NaCl, protease inhibitor cocktail + -- | Membranes resuspended in 40 mM Tris pH 7.6, 500 mM NaCl with protease inhibitors and stored at -80 degrees Celsius |
| Solubilization | Membranes incubated with ligand (40 uM [HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/) or [GSK1034702](/xray-mp-wiki/reagents/ligands/gsk1034702/) or [77-LH-28-1](/xray-mp-wiki/reagents/ligands/77-lh-28-1/)) for 40 min at room temperature, then solubilized with 1.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) for 1 hour at 4 degrees Celsius | -- | 40 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.6, 500 mM NaCl, protease inhibitor cocktail + 1.5% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Solubilized material clarified by centrifugation at 145000 g for 60 min |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Batch binding to Ni-NTA Superflow resin for 3 hours, gradient wash (10 to 60 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/)), elution with 245 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) | Ni-NTA Superflow resin | 40 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.6, 150 mM NaCl, 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (binding); 40 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.6, 500 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 70 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (wash); 40 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.6, 500 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 245 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) (elution) + 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Ligand (20 uM) included in all binding and wash buffers |
| Size-exclusion chromatography | SEC on [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) column pre-equilibrated with buffer containing ligand | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 40 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.6, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 40 uM ligand + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Protein concentrated to approximately 60 mg/mL using 100 kDa cut-off membrane prior to crystallization |


## Crystallization

### doi/10.1016##j.cell.2021.11.001

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified M1-StaR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) at approximately 60 mg/mL in 40 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.6, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 40 uM ligand |
| Temperature | 20 degrees Celsius |
| Growth time | Not specified |
| Cryoprotection | Crystals were flash-cooled in liquid nitrogen |
| Notes | Three structures were solved: M1-StaR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) with [77-LH-28-1](/xray-mp-wiki/reagents/ligands/77-lh-28-1/) (PDB 6ZFZ), [HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/) (PDB 6ZG4), and [GSK1034702](/xray-mp-wiki/reagents/ligands/gsk1034702/) (PDB 6ZG9). All structures were solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using the turkey beta1-adrenergic receptor (PDB 2Y00) as the search model. Iterative rounds of model refinement with BUSTER were interspersed with manual model building in COOT. Two TLS groups corresponding to the receptor and [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) were defined.
 |


## Biological / Functional Insights

### StaR thermostabilization mutations

The M1-StaR construct contains 12 thermostabilizing mutations: F27A (1.34),
T32A (1.39), V46L (1.53), L64A (2.43), T95A, W101A (3.28), S112A (3.39),
A143L (4.43), A196T (5.46), K362A (6.32), A364L (6.34), S411A (7.46).
These mutations were identified through a directed evolution approach that
selected for thermostability in the presence of radioligand. The W101A
mutation was additionally designed to enable direct access of small molecule
agonists to the orthosteric binding site.

### T4-lysozyme fusion strategy

[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) ([T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)) was inserted into the third intracellular loop (ICL3) of
the M1 receptor between residues R220 and F355, replacing residues R220-F355.
This fusion strategy, pioneered for GPCR crystallization, replaces the flexible
ICL3 loop with a rigid, well-folded protein domain that promotes crystal
contacts. The [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion did not alter the ligand binding properties of the
receptor compared to wild-type M1 receptor.

### Construct engineering for crystallization

The M1-StaR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) construct was engineered through a stepwise approach:
first, a chimeric M4 N-terminus (residues 1-95 of M4 replacing residues
1-87 of M1) was introduced to reduce toxicity associated with high
expression levels. Second, 12 thermostabilizing mutations (StaR) were
introduced. Third, the C-terminal 22 residues were truncated. Fourth,
[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) was inserted into ICL3. These modifications together
enabled the crystallization of the M1 receptor in complex with agonists.


## Cross-References

- [M1 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/) — Wild-type M1 receptor; M1-StaR-T4L is the crystallization-optimized construct
- [Turkey Beta1-Adrenergic Receptor M23](/xray-mp-wiki/proteins/gpcr/turkey-beta1-ar-m23/) — Template structure (PDB 2Y00) used for molecular replacement
- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — Alternative fusion protein tag used for GPCR crystallization
- [N-Dodecyl-beta-D-Maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for solubilization and purification
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for all M1-StaR-T4L structures
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [EDTA](/xray-mp-wiki/reagents/additives/edta/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
