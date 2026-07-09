---
title: "Root-Mean-Square Deviation (RMSD)"
created: 2026-07-06
updated: 2026-07-06
type: concept
category: concepts
layout: default
tags: [concept-structural, subdirectory-methods-techniques]
sources: [doi/10.1002##prot.340150304, doi/10.1016##s0022-2836(05)80111-6]
verified: none
---

# Root-Mean-Square Deviation (RMSD)

## Overview
Root-Mean-Square Deviation (RMSD) is a quantitative measure of the average atomic distance between superimposed sets of atoms in two protein structures, most commonly calculated over the C-alpha backbone atoms. It is expressed in angstroms (A) and calculated as the square root of the mean of the squared distances between corresponding atoms after optimal superposition. RMSD is a standard metric in structural biology for comparing conformational states of the same protein (e.g., open vs closed conformations), assessing structural similarity between homologous proteins, validating computational models against experimental structures, and evaluating the quality of molecular dynamics trajectories. An RMSD value of <1.0 A between equivalent C-alpha atoms indicates high structural similarity (e.g., alternative conformations of the same protein), 1.0-2.5 A indicates moderate similarity, and >2.5 A generally indicates substantial conformational changes or divergent folds. The choice of atoms included, the superposition method, and any sequence alignment preprocessing all affect computed RMSD values.

## Mechanism/Details


## Examples in Membrane Protein Work
- Maltose Transporter MalFGK2 — Comparison of inward-facing (PDB 3FH6) and outward-facing (PDB 2R6G) states shows RMSD values of 5-10 A for the transmembrane domains, indicating large conformational changes during the transport cycle.
- MsbA ABC Transporter — The nucleotide-bound and open-apo states of MsbA show RMSD values exceeding 10 A for the periplasmic domains, reflecting the large opening required for substrate export.

## Related Concepts
- [Structure Superposition](/xray-mp-wiki/concepts/methods-techniques/structure-superposition/) — RMSD calculation requires optimal structural superposition of the compared molecules
- [Conformational Change](/xray-mp-wiki/concepts/structural-mechanisms/conformational-change/) — RMSD quantifies the magnitude of conformational changes between different functional states

## Cross-References
- [X-ray Crystallography](/xray-mp-wiki/concepts/methods-techniques/xray-crystallography/) — RMSD is routinely used to assess structural similarity between crystallographic models
