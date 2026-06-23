---
title: "Glycophorin A Transmembrane Domain (GpA-TM)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1021##jacs.5b11354]
verified: false
---

# Glycophorin A Transmembrane Domain (GpA-TM)

## Overview

Glycophorin A (GpA) is a type I single-pass transmembrane sialoglycoprotein found on erythrocytes. Its transmembrane (TM) domain forms a right-handed homodimeric alpha-helical bundle driven by a well-characterized LlxxGVxxGVxxT dimerization motif (GxxxG motif). The crystal structure of a GpA TM peptide was determined at 2.81 Angstrom resolution using lipidic cubic phase (LCP) crystallization in monoolein, yielding PDB 5EH4. The structure shows a right-handed crossing angle of -37 degrees and aligns closely with previously determined NMR structures (pairwise RMSD < 0.6 Angstrom in the dimerization interface region), providing compelling evidence that LCP crystallization reveals physiologically relevant packing interfaces for single-pass TM interactions. A second crystal form (5EH6) contained only one GpA-TM helix per asymmetric unit, suggesting a monomer-dimer equilibrium existed in the lipid phase.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1021##jacs.5b11354 | 5EH4 | 2.81 | — | GpA TM peptide residues E70-L98 (EPEITLIIFGVIAGVIGTILLISYGIRRL) with M81I substitution, C-terminal Cys protected with S-methyl methanethiosulfonate |  |
| doi/10.1021##jacs.5b11354 | 5EH6 |  | — | Same GpA TM peptide sequence as 5EH4 |  |

## Expression and Purification

- **Expression system**: Recombinant (in vitro reconstitution)
- **Construct**: GpA TM peptide with sequence EPEITLIIFGVIAGVIGTILLISYGIRRL and C-terminal Cys. M81I substitution (a conserved change) introduced for production purposes. Peptide reconstituted into monoolein LCP from hexafluoroisopropanol (HFIP) or from detergents DDM, TDPC, or LMPG.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Peptide reconstitution | Organic solvent evaporation / detergent-mediated reconstitution | -- | -- + DDM, TDPC, or LMPG (optional); HFIP for detergent-free reconstitution | Peptide pre-combined with monoolein in organic solvent (HFIP), solvent removed by evaporation, cubic phase formed by mixing with water or buffer. FRAP confirmed >70% diffusible fraction in LCP. |


## Crystallization

### doi/10.1021##jacs.5b11354

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) crystallization |
| Protein sample | GpA-TM peptide at 40 mg/mL in monoolein cubic phase |
| Temperature | 20 |
| Growth time | 2-48 hours |
| Notes | Two crystal forms identified from 26/384 conditions. Datasets from two isomorphous crystals merged to solve dimer structure. LCP media shows type-I packing. |


## Biological / Functional Insights

### LCP crystallization validates physiological TM interface

The GpA-TM LCP crystal structure aligns closely with NMR structures determined in DPC micelles (1AFO), DMPC/DHPC bicelles (2KPF), and phospholipid bilayers (ssNMR), with pairwise RMSD < 0.6 Angstrom in the dimerization interface. The presence of extended non-native (antiparallel) contacts between neighboring dimers does not perturb the native interface, validating LCP as a method for determining biologically relevant TM interfaces.

### GxxxG dimerization motif and hydrogen bond network

The defining feature of the GpA dimer interface is close helix-helix packing around the G79xxxG83 motif, providing favorable van der Waals contacts and facilitating backbone-backbone C-alpha-H...O hydrogen bonds. Three such interactions were identified at I76-G79, G79-V80, and V80-G83. The T87 side-chain hydroxyl participates in stabilizing interhelical hydrogen bonds, acting as both donor (intra-helical to G83 carbonyl) and acceptor (to V84 amide groups).

### Template for single-pass TM crystallography

The GpA-TM peptide readily crystallized despite inclusion of membrane-proximal sequences that were poorly ordered in NMR structures (N-terminal EPE, C-terminal RRL). This provides a template for designing peptide constructs for crystallographic studies of other single-pass TM interactions, including receptor-tyrosine kinases, cytokine receptors, and immune receptors.


## Cross-References

- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Primary crystallization method using monoolein LCP media
- [N-Dodecyl-beta-D-maltopyranoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for peptide reconstitution into LCP
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — LCP-forming host lipid for crystallization
