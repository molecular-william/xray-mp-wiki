---
title: "Engineered Disulfide Bridge Conformational Trapping"
created: 2026-06-11
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-construct-design, membrane-protein, subdirectory-structural-mechanisms]
sources: [doi/10.1107##s205979832001517x]
verified: regex
---

# Engineered Disulfide Bridge Conformational Trapping

## Overview
Engineered disulfide bridge conformational trapping is a protein engineering strategy to stabilize specific conformational states of membrane proteins for structural and functional studies. Cysteine mutations are introduced at positions predicted to form a disulfide bond only in a target conformation, thereby locking the protein in that state. The method preserves native residues (including Na+- and substrate-binding sites) and allows the protein to undergo physiological movements until cross-linking restricts it to the desired conformation. This approach was applied to trap ASBT_Yf in an outward-facing conformation, providing evidence for the physiological relevance of the bile acid transporter's proposed elevator-style alternating-access mechanism.

## Mechanism/Details
Design criteria for engineered disulfide bridges: (1) One cysteine mutation in the panel domain, the other in the core domain; (2) sulfhydryl groups <4 A apart only in the target conformation; (3) avoid residues important for Na+ or substrate binding; (4) validate that the un-cross-linked mutant behaves like wild-type. For ASBT_Yf, the program Disulfide by Design 2.0 plus manual design identified six candidate pairs, with Y113C/P190C (Pair1, TM4/TM7) and V110C/I197C (Pair2, TM4/TM7) selected for further study. Cross-linking efficiency was assessed by PEGylation assay using mPEG-Mal-5K, which modifies free thiol groups. Disulfide formation was catalyzed by copper(II)(1,10-phenanthroline)3 or CuSO4. Structures before and after cross-linking confirmed the intended conformational transition (inward-facing to outward-facing).

## Examples in Membrane Protein Work
- ASBT_Yf (Yersinia frederiksenii) — Y113C/P190C disulfide bridge trapped ASBT_Yf in an outward-facing conformation (PDB 6lh1, 2.86 A), resembling the E254A mutant structure (PDB 4n7x) but with WT-like Na+- and substrate-binding sites. The un-cross-linked mutant (PDB 7cyg) showed inward-facing WT-like conformation.

## Related Concepts


## Cross-References
- [ASBT_Yf (Apical Sodium-Dependent Bile Acid Transporter)](/xray-mp-wiki/proteins/slc-transporters/asbt-yf/) — Disulfide bridge trapping was applied to ASBT_Yf
- [Outward-Facing Conformation of ABC Transporters](/xray-mp-wiki/concepts/transport-mechanisms/outward-facing-conformation/) — The trapping method validates the outward-facing conformation in a non-ABC transporter
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — Conformational trapping enables study of transport cycle states
