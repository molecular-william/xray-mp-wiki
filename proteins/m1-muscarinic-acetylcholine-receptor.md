---
title: M1 Muscarinic Acetylcholine Receptor
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2021.11.001, doi/10.1038##nature17188]
verified: false
---

# M1 Muscarinic Acetylcholine Receptor

## Overview

The M1 muscarinic acetylcholine receptor (M1 mAChR) is a class A G protein-coupled receptor that mediates cholinergic neurotransmission in the central nervous system. It is highly expressed in the hippocampus and cortex, areas critical for learning and memory. The M1 receptor couples to Gq/11 proteins to activate phospholipase C-beta, leading to intracellular calcium release. It is a major therapeutic target for Alzheimer disease, as cholinergic deficits in the hippocampus and cortex are a hallmark of the disease. The M1 receptor has been crystallized in complex with multiple orthosteric agonists, revealing the molecular basis for agonist-induced activation and subtype selectivity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature17188 | 5CXV | 2.7 A | P 21 21 21 | Human M1 muscarinic receptor, N-terminal FLAG epitope tag, N-glycosylation mutants (N2Q, N12Q, unintentionally N110Q 3.37), residues 226-389 of ICL3 replaced by T4 lysozyme fusion protein, C-terminal 8x histidine tag
 | Tiotropium |
| doi/10.1016##j.cell.2021.11.001 | 6ZFZ | 2.17 A | C 2 2 21 | M1-StaR-T4L (12 thermostabilizing mutations, M4 N-terminus chimera, C-terminal truncation, T4L in ICL3) | 77-LH-28-1 |
| doi/10.1016##j.cell.2021.11.001 | 6ZG4 | 2.17 A | C 2 2 21 | M1-StaR-T4L (12 thermostabilizing mutations, M4 N-terminus chimera, C-terminal truncation, T4L in ICL3) | HTL9936 |
| doi/10.1016##j.cell.2021.11.001 | 6ZG9 | 2.17 A | C 2 2 21 | M1-StaR-T4L (12 thermostabilizing mutations, M4 N-terminus chimera, C-terminal truncation, T4L in ICL3) | GSK1034702 |

## Expression and Purification

- **Expression system**: Sf21 insect cells (baculovirus expression vector system)
- **Construct**: M1-StaR-T4L construct with N-terminal GP64 signal sequence, chimeric M4 N-terminus (residues 1-95 of M4 replacing residues 1-87 of M1), residues 88-438 of M1 receptor, C-terminal truncation (residues 439-460 removed), T4-lysozyme inserted into ICL3 between residues 219 and 354, and C-terminal deca-histidine tag. The StaR variant contains 12 thermostabilizing mutations: F27A, T32A, V46L, L64A, T95A, W101A, S112A, A143L, A196T, K362A, A364L, S411A.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and infection | Sf21 cells infected with baculovirus at multiplicity of infection 2, harvested 48 hours post-infection | -- | -- + -- | Cells grown at 27 degrees Celsius with constant shaking in ESF 921 medium supplemented with 10% FBS and 1% penicillin/streptomycin |
| Cell disruption and membrane preparation | Cell disruption at 15000 psi using microfluidizer, membranes pelleted by ultracentrifugation at 200000 g for 50 min, high salt washes | -- | PBS, 5 mM EDTA, protease inhibitor cocktail; wash buffer: PBS, 1 M NaCl, protease inhibitor cocktail + -- | Membranes resuspended in 40 mM Tris pH 7.6, 500 mM NaCl with protease inhibitors and stored at -80 degrees Celsius |
| Solubilization | Membranes incubated with ligand (40 uM HTL9936 or GSK1034702 or 77-LH-28-1) for 40 min at room temperature, then solubilized with 1.5% DDM for 1 hour at 4 degrees Celsius | -- | 40 mM Tris-HCl pH 7.6, 500 mM NaCl, protease inhibitor cocktail + 1.5% DDM | Solubilized material clarified by centrifugation at 145000 g for 60 min |
| Ni-NTA affinity chromatography | Batch binding to Ni-NTA Superflow resin for 3 hours, gradient wash (10 to 60 mM imidazole), elution with 245 mM imidazole | Ni-NTA Superflow resin | 40 mM Tris-HCl pH 7.6, 150 mM NaCl, 10 mM imidazole, 0.05% DDM (binding); 40 mM Tris-HCl pH 7.6, 500 mM NaCl, 0.05% DDM, 70 mM imidazole (wash); 40 mM Tris-HCl pH 7.6, 500 mM NaCl, 0.05% DDM, 245 mM imidazole (elution) + 0.05% DDM | Ligand (20 uM) included in all binding and wash buffers |
| Size-exclusion chromatography | SEC on Superdex 200 column pre-equilibrated with buffer containing ligand | Superdex 200 | 40 mM Tris-HCl pH 7.6, 150 mM NaCl, 0.03% DDM, 40 uM ligand + 0.03% DDM | Protein concentrated to approximately 60 mg/mL using 100 kDa cut-off membrane prior to crystallization |


## Crystallization

### doi/10.1016##j.cell.2021.11.001

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | Purified M1-StaR-T4L at approximately 60 mg/mL in 40 mM Tris-HCl pH 7.6, 150 mM NaCl, 0.03% DDM, 40 uM ligand |
| Temperature | 20 degrees Celsius |
| Growth time | Not specified |
| Cryoprotection | Crystals were flash-cooled in liquid nitrogen |
| Notes | Three structures were solved: M1-StaR-T4L with 77-LH-28-1 (PDB 6ZFZ), HTL9936 (PDB 6ZG4), and GSK1034702 (PDB 6ZG9). All structures were solved by molecular replacement using the turkey beta1-adrenergic receptor (PDB 2Y00) as the search model. Iterative rounds of model refinement with BUSTER were interspersed with manual model building in COOT. Two TLS groups corresponding to the receptor and T4-lysozyme were defined.
 |


## Biological / Functional Insights

### Agonist binding mode and activation mechanism

All three agonist-bound structures reveal that the orthosteric agonists are
primarily held in place via a charge-charge interaction between the protonated
nitrogen of the ligand and the conserved aspartate D105 (3.32) in the amine
pocket. Agonist binding causes rearrangement of the tyrosine cage (Y82, Y85,
Y104, Y378, Y381, Y404, Y408) that is characteristic of the inactive state.
The piperidine ring of HTL9936 makes contact with Y404 (7.39), causing a
rotation that confers a unique conformation of Y381 (6.51). The base of the
amine pocket is formed by C407 (7.42) making hydrophobic contacts to the
homopiperidine ring, and W378 (6.48) forming an edge-to-face pi-stacking
arrangement with the carbamate moiety.

### Structural basis for M1 subtype selectivity

Comparative analysis of the three agonist-bound structures revealed that
HTL9936 achieves M1 selectivity over M2 and M3 receptors through specific
interactions in the orthosteric pocket. The extended structure of HTL9936
fills a sub-pocket defined between Tyr106 (3.33), Trp378 (6.48), Tyr381
(6.51), and Cys407 (7.42) more efficiently than the smaller agonist
77-LH-28-1. The tyrosine cage rearrangement induced by HTL9936 differs
from that seen in the M2 receptor iperoxo agonist structure, providing a
structural basis for the reduced M2 and M3 activity of HTL9936 compared
to orthosteric agonists like xanomeline and GSK1034702.

### Partial agonism mechanism

Molecular dynamics simulations revealed that HTL9936 forms stable
water-mediated polar interaction networks in the major pocket with Y106
(3.33), T196 (5.46), Y381 (6.51), and N382 (6.52) via its carbamate
moiety, and in the minor pocket and extracellular vestibule with C178
(4.5.50) and Y404 (7.39) via its amide group. Analysis of binding site
volumes from MD simulations showed that HTL9936 has a more restricted
binding site volume compared to full agonists 77-LH-28-1 and
GSK1034702, aligning more closely with the antagonist tiotropium. This
restricted binding site volume likely underlies the partial agonism of
HTL9936.

### StaR thermostabilization strategy

The M1-StaR construct incorporates 12 thermostabilizing mutations
distributed throughout the transmembrane domains, which collectively
enhance receptor stability without disrupting ligand binding. The W101A
(3.28) mutation was specifically designed to enable direct access of
small molecule agonists to the orthosteric binding site. The chimeric
M4 N-terminus (residues 1-95) replaced the native M1 N-terminus
(residues 1-87) to reduce toxicity associated with high expression
levels. The C-terminal truncation (removal of residues 439-460) and
T4-lysozyme insertion in ICL3 (between residues 219 and 354) were
added to promote crystallization.

### Comparison with M2 receptor agonist structure

The M1 agonist-bound structures were compared with the M2 receptor
iperoxo agonist structure (Fish et al., 2017). The M1 structures
revealed that agonist binding induces a different rearrangement of the
tyrosine cage compared to the M2 receptor. Specifically, the M1
receptor shows inward movement of Y104 (3.33), Y403 (6.51), and Y426
(7.39) upon agonist binding, which differs from the M2 receptor
conformation. This structural divergence provides insights into the
molecular basis for subtype-selective agonist design.


## Cross-References

- [Turkey Beta1-Adrenergic Receptor M23](/xray-mp-wiki/proteins/turkey-beta1-ar-m23/) — Template structure (PDB 2Y00) used for molecular replacement in all M1 structure determinations
- [M1-StaR-T4L](/xray-mp-wiki/proteins/m1-star-t4l/) — Specific thermostabilized M1 receptor construct with T4L fusion used for crystallization
- [N-Dodecyl-beta-D-Maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for membrane solubilization and throughout purification
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for all three M1-StaR-T4L structures
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Final purification step for monodisperse M1-StaR-T4L sample
- [Biased Agonism in G Protein-Coupled Receptors](/xray-mp-wiki/concepts/biased-agonism/) — HTL9936 was characterized as an unbiased agonist of the M1 receptor across multiple signaling pathways
- [HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/) — Selective M1 partial agonist co-crystallized (PDB 6ZG4)
- [GSK1034702](/xray-mp-wiki/reagents/ligands/gsk1034702/) — Bitopic M1 agonist co-crystallized (PDB 6ZG9)
- [Human M4 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/m4-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor subtype; M1 and M4 structures solved in same study (PDB 5CXV)
- [Pirenzepine](/xray-mp-wiki/reagents/ligands/pirenzepine/) — M1-selective antagonist used in induced fit docking studies on M1 structure (PDB 5CXV)
