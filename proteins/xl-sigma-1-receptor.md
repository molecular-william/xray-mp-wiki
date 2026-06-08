---
title: Sigma-1 Receptor from Xenopus laevis (xlS1R)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-022-28946-w]
verified: false
---

# Sigma-1 Receptor from Xenopus laevis (xlS1R)

## Overview

The sigma-1 receptor (S1R) from Xenopus laevis (xlS1R) is a non-opioid transmembrane receptor that shares 67% sequence identity and 89% sequence homology with the human sigma-1 receptor. It is an ER-resident receptor implicated in neurodegenerative disorders and cancer. This paper presents multiple crystal structures of xlS1R in both closed and open-like conformations, providing experimental evidence for the ligand entry pathway. The structures reveal that ligand access to the binding site is achieved through conformational changes involving the carboxy-terminal two-helix bundle (alpha4/alpha5), supporting the PATH2 hypothesis over the previously proposed cupin-fold domain rearrangement pathway (PATH1).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-022-28946-w | 7W2B | 3.33 | P21 | Wild-type sigma-1 receptor from Xenopus laevis (xlS1R), full-length | unknown endogenous molecule (closed-endo conformation) |
| doi/10.1038##s41467-022-28946-w | 7W2C | 3.33 | P21 | Wild-type sigma-1 receptor from Xenopus laevis (xlS1R), full-length | PRE084 (closed conformation, soaked) |
| doi/10.1038##s41467-022-28946-w | 7W2D | 3.47 | P21 | Wild-type sigma-1 receptor from Xenopus laevis (xlS1R), full-length | S1RA (closed conformation) |
| doi/10.1038##s41467-022-28946-w | 7W2E | 3.56 | P222 | Wild-type sigma-1 receptor from Xenopus laevis (xlS1R), full-length | unknown endogenous molecule (open-endo conformation) |
| doi/10.1038##s41467-022-28946-w | 7W2F | 3.10 | P222 | Wild-type sigma-1 receptor from Xenopus laevis (xlS1R), full-length | PRE084 (open conformation, co-crystallized) |
| doi/10.1038##s41467-022-28946-w | 7W2G | 2.85 | P222 | Wild-type sigma-1 receptor from Xenopus laevis (xlS1R), full-length | PRE084 (open conformation, soaked) |
| doi/10.1038##s41467-022-28946-w | 7W2H | 3.80 | P21 | xlS1R C179/C203 double mutant with C91S background, full-length | S1RA |

## Expression and Purification

- **Expression system**: Pichia pastoris yeast strain GS115
- **Construct**: Full-length xlS1R with N-terminal decahistidine tag and TEV protease recognition site following hemagglutinin signal peptide; cysteine mutants introduced by site-directed mutagenesis
- **Induction**: 1% methanol and 2.5% DMSO at OD600 of ~1, 20 C for 48 h

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure homogenization (ATS AH-1500) | — | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 10% glycerol, 1 mM PMSF, 2 mM beta-mercaptoethanol | Cell pellets resuspended and lysed |
| Solubilization | Detergent solubilization | — | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 1 mM DDM, 0.005% CHS | Membranes solubilized |
| Affinity chromatography | Ni-NTA affinity resin | Ni-NTA | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 1 mM DDM, 0.005% CHS, 250 mM imidazole (elution) |  |
| Tag cleavage | TEV protease | — |  |  |
| Size-exclusion chromatography | Superose 6 Increase column | — | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 1 mM DDM, 0.005% CHS |  |


## Crystallization

### doi/10.1038##s41467-022-28946-w

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified xlS1R at ~15 mg/mL mixed with monoolein at 2:3 protein:lipid ratio by mass |
| Temperature | 4 C |
| Notes | Crystals grew over 2-4 weeks; some structures obtained by soaking ligands (PRE084, S1RA) into pre-formed crystals |

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Protein sample | xlS1R C179/C203 mutant |
| Reservoir | 1.5 M ammonium citrate, 0.1 M MES pH 5.5, 5 mM beta-mercaptoethanol |
| Temperature | Not specified |
| Notes | 5.0 mM 06:0 Lyso PC (Avanti) used as additive for final data |


## Biological / Functional Insights

### Ligand entry pathway (PATH2)

The xlS1R structures support PATH2, where ligands access the binding site through the opening between alpha4 and alpha5 helices of the carboxy-terminal two-helix bundle. The open-like conformation shows a solvent pathway connecting the ligand binding site to the extracellular milieu. Blocking the entrance between alpha4 and alpha5 (via disulfide crosslinking or PEGylation of Cys179/Cys203) significantly reduces ligand binding, confirming this pathway.

### Cupin-fold domain rigidity

Crystal packing analysis shows that the cupin-fold domain tip region (Trp133-Tyr144) is tightly buried by adjacent protomers, preventing the conformational changes required for PATH1 (cupin-fold domain rearrangement). This steric hindrance from crystal packing supports the PATH2 hypothesis as the physiological ligand entry mechanism.

### Homotrimeric organization

xlS1R crystallizes as a homotrimer in all conformations. Each protomer comprises a single transmembrane helix (alpha1), a cupin-fold beta-barrel body containing the ligand-binding site, and a membrane-adjacent V-shaped two-helix bundle (alpha4/alpha5) at the carboxy-terminus. Superposition of xlS1R and human S1R (excluding alpha1) yields an all-Ca RMSD of 0.35 A, indicating high structural conservation.


## Cross-References

- [PD144418](/xray-mp-wiki/reagents/ligands/pd144418/) — Sigma-1 antagonist used in human S1R structures (PDB 5HK1) for comparison
- [Human Sigma-1 Receptor](/xray-mp-wiki/proteins/sigma-1-receptor/) — Human ortholog used for structural comparison (PDB 5HK1)
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for xlS1R crystallization
