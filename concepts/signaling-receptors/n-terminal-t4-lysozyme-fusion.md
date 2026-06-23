---
title: N-Terminal T4 Lysozyme Fusion for GPCR Crystallization
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-construct-design, concept-functional, membrane-protein]
sources: [doi/10.1371##journal.pone.0046039]
verified: false
---

# N-Terminal T4 Lysozyme Fusion for GPCR Crystallization

## Overview
N-terminal T4 lysozyme ([T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)) fusion is a protein engineering strategy to facilitate crystallization of G protein-coupled receptors (GPCRs) by fusing the highly crystallizable [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) to the extracellular N-terminus of the receptor. This approach provides a rigid hydrophilic surface for crystal lattice contacts without requiring thermostabilizing mutations, stabilizing antibodies, or insertion of [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) into the third intracellular loop. The N-terminal [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion is particularly useful for crystallizing GPCR signaling complexes (e.g., GPCR-G protein or GPCR-arrestin complexes), where intracellular modifications would interfere with complex formation.


## Mechanism/Details
The strategy involves replacing the flexible N-terminal residues of a GPCR with T4 lysozyme from bacteriophage T4. Key design features include:

1. [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) replaces the N-terminus of the receptor (e.g., beta2AR residues preceding Asp29 are replaced by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)), connected via a 2-alanine linker.
2. Flexible regions such as ICL3 and the C-terminus are truncated to minimize unstructured surface area.
3. The [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) moiety is sufficiently rigid relative to the receptor to facilitate crystallogenesis without additional stabilizing factors (thermostabilizing mutations, antibody, G protein, or ICL3-fused [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)).
4. In the crystal lattice, each [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) makes four distinct packing interactions: against ECL1/ECL2 of its fused receptor, against [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) of an adjacent molecule, against [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)/ECL2/ECL3 of a second adjacent molecule, and against ICL3/Helix 8 of a third adjacent molecule.
5. No direct contacts are formed between adjacent receptors — all lattice contacts are mediated by [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/).

The approach was validated using the beta2-adrenergic receptor (beta2AR). The resulting T4L-beta2AR-deltaICL3 structure (PDB 4GBR, 4.0 A resolution) was solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) and found to be virtually identical to the beta2AR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) structure (PDB 2RH1) with ICL3-fused [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) (RMSD 0.32 A), confirming that the N-terminal fusion does not distort the receptor structure.

Unlike the ICL3-fused [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) strategy, the N-terminal fusion leaves the intracellular surface of the receptor unmodified, enabling future studies of GPCR-signaling partner complexes.

## Examples in Membrane Protein Work
- Beta2-Adrenergic Receptor — N-terminal [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion with beta2AR (T4L-beta2AR-deltaICL3 construct) crystallized bound to [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/) in lipid cubic phase, space group P2_1_2_1_2_1, 4.0 A resolution (PDB 4GBR)

## Related Concepts
- [T4 lysozyme fusion strategy](/xray-mp-wiki/concepts/t4-lysozyme-fusion-strategy/) — Describes the broader approach of using T4L to facilitate GPCR crystallization
- [GPCR crystallization](/xray-mp-wiki/concepts/gpcr-crystallization/) — The N-terminal T4L fusion is one method among many for GPCR crystallization
- [Lipidic cubic phase crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for crystallizing the T4L-beta2AR fusion construct

## Cross-References
- [Human Beta2-Adrenergic Receptor (beta2 AR)](/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/) — Primary GPCR used to validate the N-terminal T4L fusion strategy
- [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/) — Inverse agonist ligand bound during crystallization
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid matrix for LCP crystallization of the T4L-fusion construct
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — Fusion tag for crystallization or purification
