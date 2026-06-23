---
title: Human MT2 Melatonin Receptor
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-019-1144-0]
verified: false
---

# Human MT2 Melatonin Receptor

## Overview

The human MT2 melatonin receptor (type 1B, MTNR1B) is a class A G-protein-coupled receptor (GPCR) that binds the neurohormone melatonin and regulates circadian rhythms, sleep patterns, and has been implicated in type 2 diabetes. X-ray free electron laser (XFEL) structures of MT2 in complex with agonists 2-phenylmelatonin (2-PMT) and ramelteon at 2.8-3.3 Angstrom resolution reveal a conserved orthosteric binding pocket with notable conformational differences from the MT1 subtype despite identical binding site residues. The structures show a membrane-buried lateral ligand entry channel between TM4 and TM5 (more constricted than in MT1) and an additional narrow extracellular loop (ECL) opening towards solvent that is absent in MT1. Kinetic ligand dissociation studies demonstrate the importance of both access routes, with the ECL opening providing a potential path for more polar ligands in MT2. These findings explain melatonin receptor subtype selectivity and enable design of highly selective melatonin tool compounds.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-019-1144-0 | 6ME6 | 2.80 | P2_1 | MT2-CC (BRIL fusion, N-term trunc 30 aa, C-term trunc 22 aa, 8 point mutations, rubredoxin in ICL3) | 2-PMT (2-phenylmelatonin) |
| doi/10.1038##s41586-019-1144-0 | 6ME7 | 3.20 | P2_1 | MT2-CC(H208A) mutant | 2-PMT (2-phenylmelatonin) |
| doi/10.1038##s41586-019-1144-0 | 6ME8 | 3.10 | P2_1 | MT2-CC(N86D) mutant | 2-PMT (2-phenylmelatonin) |
| doi/10.1038##s41586-019-1144-0 | 6ME9 | 3.30 | P2_1 | MT2-CC | ramelteon |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Construct**: MT2-CC (human MT2 with N-terminal 30 aa truncation, C-terminal 22 aa truncation, ICL3 residues 232-240 replaced with rubredoxin fusion; 8 thermostabilizing point mutations: D86N, L108F, F129W, N137D, C140L, W264F, A305P, N312D)
- **Notes**: Bac-to-bac baculovirus expression system; D86N mutation critical for expression and stability

### Purification Workflow

- **Expression system**: Sf9 insect cells
- **Expression construct**: MT2-CC
- **Tag info**: N-terminal HA signal + FLAG tag; C-terminal PreScission site + 10x His tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Dounce homogenization and ultracentrifugation | — | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitor cocktail | Washed in hypotonic buffer then high-osmotic buffer (1.0 M NaCl) to remove soluble/membrane-associated proteins |
| Solubilization | Detergent extraction | — | 50 mM HEPES pH 7.5, 150 mM NaCl, 50 uM ligand (2-PMT or ramelteon) + 1% DDM / 0.2% CHS | 3 h incubation at 4C |
| Immobilized metal affinity chromatography (IMAC) | Talon resin | — |  | Overnight binding at 4C; washed with 800 mM NaCl, 10% glycerol, DDM/CHS, 10-20 mM imidazole |
| Size-exclusion chromatography | SEC (Superdex 200) | — |  | Buffer with 100 mM NaCl, DDM/CHS, ligand |


## Crystallization

### doi/10.1038##s41586-019-1144-0

| Parameter | Value |
|---|---|
| Method | LCP (lipid cubic phase) |
| Protein sample | ~30 mg/mL MT2-CC in 50 mM HEPES pH 7.5, 150 mM NaCl, 0.1% DDM/0.02% CHS, 10% glycerol |
| Lipid | Monoolein |
| Protein-to-lipid ratio | 2:3 (w/w) |
| Temperature | 20C |
| Growth time | 2-4 weeks |
| Cryoprotection | 20% glycerol |
| Notes | Crystals appeared in LCP with P2_1 space group; XFEL data collected at LCLS; synchrotron data also used |


## Biological / Functional Insights

### Lateral Ligand Entry Channel

MT2 has a membrane-buried lateral channel between TM4 and TM5 connecting the orthosteric binding site to the lipid bilayer, similar to MT1 but more constricted (~2.6 A diameter). This channel provides the primary access route for lipophilic ligands like melatonin. Mutation of channel-lining residue Y200^5.38A widened the channel and reduced ligand residence time 30-fold, while constricting mutation A171M^4.56 markedly increased residence time to ~20 h.

### Extracellular Loop Opening in MT2

In contrast to MT1, MT2 structures reveal a narrow opening towards solvent in the extracellular part of the receptor, bounded by residues T191^ECL2, Q194^ECL2, and Y294^7.39. The ECL opening provides a potential secondary ligand entry path. Mutations widening this opening (T191A, Q194A, Y294A) reduced ligand residence time 10-22 fold in MT2, while equivalent MT1 mutations had minimal effect.

### Subtype Selectivity Determinants

Despite identical orthosteric binding site residues between MT1 and MT2 (68% sequence identity overall), the binding pocket in MT2 is ~50 A3 (7%) larger, with differences concentrated around the alkylamide tail region and a hydrophobic subpocket. R1 substituents on the melatonin scaffold confer MT1 selectivity, while R2 and R3 substituents confer MT2 selectivity. Docking of selective ligands reveals that the membrane channel in MT1 better accommodates extended R1 alkyl chains, while MT2 selectivity is achieved through interactions in the expanded hydrophobic subpocket.

### Ligand Access Routes and Residence Time

Kinetic [3H]melatonin dissociation studies show substantially longer residence time in wild-type MT2 (koff^-1 >> MT1), consistent with the narrower membrane entry channel. Mutation studies systematically probing both the lateral membrane channel and ECL opening demonstrate functional relevance of both access routes, with the ECL opening playing a more prominent role in MT2 than MT1.


## Cross-References

- [Human MT1 Melatonin Receptor](/xray-mp-wiki/proteins/gpcr/human-mt1-melatonin-receptor/) — Sister subtype; companion paper (10.1038/s41586-019-1141-3) describes MT1 structures used for comparison
- [GPCR Active Conformation](/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/) — MT2 structures represent inactive 'low agonist affinity' state
- [GPCR Inactive Conformation](/xray-mp-wiki/concepts/signaling-receptors/gpcr-inactive-conformation/) — MT2 structures stabilized in inactive state by crystallization construct mutations
