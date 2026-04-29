---
title: Adenosine A1 Receptor (A1-AR)
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [gpcr, receptor, membrane-protein, xray-crystallography, adenosine-receptor]
sources: [doi/10.1016##j.cell.2017.01.042]
category: proteins
---
layout: default

# Adenosine A1 Receptor (A1-AR)

## Overview

The adenosine A1 receptor is a G protein-coupled receptor involved in cardiac, renal, and neuronal processes. This paper reports the 3.2 Å crystal structure of the A1-AR bound to the selective covalent antagonist DU172, revealing the molecular basis for subtype selectivity among adenosine receptor subtypes.

## Structure

- **Protein**: Human adenosine A1 receptor (A1-AR)
- **Ligand**: DU172 (covalent selective antagonist, 8-cyclohexyl-2,6-dioxo-1-propyl-1,2,6,7-tetrahydro-3H-purine-3-sulfonate)
- **Resolution**: 3.2 Å
- **Crystal**: Two receptor copies per asymmetric unit in parallel orientations
- **Data collection**: 29 crystals merged

### Key Structural Differences from A2A-AR

- **More open binding site cavity**: Accommodates both orthosteric and allosteric ligands
- **ECL2 conformation**: Distinct rearrangement compared to A2A-AR
- **TMs 1, 2, 3, 7 rearrangements**: Contribute to subtype-selective binding pocket
- **Single amino acid at position 270**: Key determinant of selectivity
- **No H264-E169 salt bridge**: ECL2-ECL3 interaction absent (unlike most A2A-AR structures)

### Ligand Binding

- **DU172**: Covalent binding to A1-AR; largest thermal stability increase among tested ligands
- **Binding site**: Xanthine ring interacts with L88³·³⁴ and W247⁶·⁴⁸ at binding site bottom
- **Allosteric pocket**: Wider cavity allows binding of bitopic molecules targeting both orthosteric and allosteric sites

## Expression and Purification

- **Construct**: A1cryst — M4 muscarinic N-terminus (22 aa, 3 N-glycosylation sites) + 3C protease site + A1-AR + BRIL (b562 RIL) in ICL3 (residues 211–220) + N159A mutation + TM6 first 8 aa replaced with A2A-AR residues + C-terminal 3C site after residue 311
- **Expression**: Sf9 cells, Baculovirus system (Best-Bac, Expression Systems), pVL1392 vector
- **Expression yield**: 200–400 μg/L culture (vs. <70 μg/L without M4 N-terminus)
- **Ligand**: 0.2 μM DU172 maintained throughout purification
- **Cell lysis**: Osmotic shock in 10 mM Tris pH 7.5, 1 mM EDTA, 1 mM MgCl₂, 1 mg/ml iodoacetamide + benzonase + protease inhibitors
- **Solubilization**: 30 mM HEPES pH 7.5, 1% DDM, 0.03% CHS, 750 mM NaCl, 30% glycerol, 1 mM MgCl₂, 1 mg/ml iodoacetamide + benzonase, 2 hr at 4°C
- **Purification**:
  - Ni-chelating resin batch bind (1.5 hr at 4°C)
  - Wash: 30 mM HEPES pH 7.5, 0.1% DDM, 0.003% CHS, 750 mM NaCl, 30% glycerol, 5 mM imidazole
  - Elution: Wash buffer + 250 mM imidazole + 2 mM CaCl₂
  - Anti-Flag M1 antibody column
  - Detergent exchange: 30 mM HEPES pH 7.5, 0.1% MNG, 0.01% CHS, 100 mM NaCl, 2 mM CaCl₂
  - Final wash: 10xCMC buffer (30 mM HEPES pH 7.5, 0.01% MNG, 0.001% CHS, 100 mM NaCl) + 2 mM CaCl₂
  - Elution: 10xCMC + 10 mM EDTA + 0.2 mg/ml FLAG peptide
  - 3C protease digest (1:7 w/w, overnight at 4°C, 22 μM DU172)
  - SEC: Superdex S200 Increase in 10xCMC buffer
  - Final concentration: 200 μM DU172

## Crystallization

- **Method**: Lipidic cubic phase (LCP)
- **Conditions**: Not explicitly stated (referenced as previous LCP work)
- **Data processing**: 29 crystals merged to 3.2 Å
- **Space group**: P2₁2₁2₁ (implied from parallel orientation)
- **Refinement**: Molecular replacement, iterative manual building

## Thermal Stability

- **Assay**: CPM fluorescence-based thermal shift (Alexandrov et al., 2008)
- **Ligands tested**: Multiple non- and subtype-selective AR agonists/antagonists
- **Most stabilizing**: Covalent antagonists FSCPX and DU172

## Pharmacological Significance

- **Therapeutic target**: A1-AR targeted for cardiac, renal, and neurological diseases
- **No selective agonists/antagonists**: Currently no clinically approved A1-AR selective drugs
- **Allosteric modulators**: A1-AR structure explains differential effects of allosteric ligands
- **Anti-target**: Can screen for A2A-AR selective antagonists in development for Parkinson's and cancer immunotherapy

## Related Receptors

- [a2a-adenosine-receptor](/proteins/a2a-adenosine-receptor/) — A2A Adenosine Receptor (comparison structure)
- [a2a-star2](/proteins/a2a-star2/) — A2A-STAR2
- [5ht2b-receptor](/proteins/5ht2b-receptor/) — 5-HT2B Receptor with BRIL fusion

## References

- Glukhova et al. (2017) Cell 168:867-877 — A1-AR structure with DU172
- Beauglehole et al. (2000) — DU172 compound characterization
- Chun et al. (2012) — BRIL fusion toolchest