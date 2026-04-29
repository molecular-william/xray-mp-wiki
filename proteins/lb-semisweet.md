---

title: LbSemiSWEET
created: 2026-04-27
updated: 2026-04-27
type: protein
tags: [transporter, membrane-protein]
sources: [doi/10.1016##j.cell.2017.03.010]

category: proteins
---
layout: default


# LbSemiSWEET

## Overview

LbSemiSWEET is a sugar transporter from the SWEET (SWEET homolog) family, isolated from *Leptospira biflexa*. It is among the smallest characterized transporters at < 20 kDa, forming a symmetric dimer of three-helix bundles. Members of the SWEET family play critical roles in phloem loading, nectar secretion, pollen development, seed filling, and metabolic homeostasis in plants and animals.

## Structure Determination

- **Organism**: *Leptospira biflexa*
- **Outward-open structure**: 2.8 Å resolution, D57A extracellular mutant, glucose-bound
- **Inward-open structure**: 2.8 Å resolution, Q20A intracellular mutant (domain-swapped configuration)
- **Previously reported occluded state**: Xu et al., 2014 (from LbSemiSWEET)
- **Note**: To the best of the authors' knowledge, this is the first complete set of all three conformational states (outward-open, occluded, inward-open) captured for a single SWEET family transporter

## Expression and Purification

- **Expression system**: *E. coli* BL21(DE3) cells
- **Construct**: Full-length LbSemiSWEET with N-terminal His-tag
- **Detergent**: [ddm](/reagents/detergents/ddm/) (n-dodecyl-β-D-maltopyranoside) for membrane solubilization
- **Purification**: [affinity-chromatography](/methods/purification/affinity-chromatography/) (His-tag), followed by [size-exclusion-chromatography](/methods/purification/size-exclusion-chromatography/) ([superdex-columns](/methods/purification/superdex-columns/))
- **SEC buffer**: 20 mM [hepes-buffer](/reagents/buffers/hepes-buffer/) pH 7.5, 150 mM [sodium-chloride](/reagents/additives/sodium-chloride/), 0.05% [ddm](/reagents/detergents/ddm/)

## Crystallization

- **Method**: [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) (LCP) — [monoolein](/methods/crystallization/monoolein/)-based mesophase
- **Lipid**: [monoolein](/methods/crystallization/monoolein/) (Nu-Chek Prep)
- **Protein-to-lipid ratio**: 1:1 (w/w)
- **Reservoir**: 0.1 M [sodium-acetate](/reagents/additives/sodium-acetate/) pH 4.5, 18–20% [peg-400](/reagents/additives/peg-400/), 0.2 M [sodium-chloride](/reagents/additives/sodium-chloride/)
- **Temperature**: 20 °C
- **Crystal growth**: 1–3 weeks
- **Space group**: P2₁2₁2₁

## Conformational States

1. **Outward-open**: Substrate-binding pocket accessible from extracellular side; glucose bound
2. **Occluded**: Binding pocket sealed from both sides; on-pathway intermediate
3. **Inward-open**: Binding pocket accessible from intracellular side

The D57A mutation (extracellular) stabilizes the outward-open state and exhibits >2x higher glucose affinity than wild-type (Km ~70 µM vs ~160 µM). The Q20A mutation (intracellular) stabilizes the inward-open state.

## Gating Mechanism

### Extracellular Gate
- **Residues**: Tyr51 (TM2), Ile60 (TM3), Arg55, Asp57 (extracellular surface)
- **Closure**: TM3 tilts inward toward the central axis, packing Ile60 against Tyr51 of the opposite protomer; ionic contacts form between Asp57 and Arg55
- **Key interaction**: Hydrophobic and electrostatic contacts between cross-protomer gate residues

### Intracellular Gate
- **Residues**: Phe17 (TM1), Phe17 (TM3 interface), Met37, Tyr38, Phe41 (TM2, near intracellular surface)
- **Opening**: TM1 kinks at Pro19; Phe17 flips to pack against TM3; Met37, Tyr38, Phe41 shift away from central pore
- **Driving force**: TM1 energetically favors kinked conformation (backbone H-bonds between Thr13-Phe17 and Thr14-Leu18), but is prevented by TM1-TM3 packing in outward-open state

### Allosteric Coupling
The occluded state creates an unstable TM1 configuration — neither kinked nor well-packed against TM3. This drives gate opening in a negative-cooperativity pattern: once one gate opens, there is no driving force for the other to open, preventing the "forbidden state" of both gates simultaneously open.

## Substrate Recognition

- **Substrate**: [glucose](/reagents/ligands/glucose/) (Km ~160 µM wild-type, ~70 µM D57A)
- **Binding pocket**: Glucose ring in vertical plane, off-center from two-fold axis, partially sandwiched between Trp48 pyrrole rings on each protomer
- **Direct contacts**: Asn64 and Thr13 (on only one protomer) coordinate substrate hydroxyl groups
- **Notable**: SemiSWEET forms fewer direct H-bonds with glucose compared to other sugar transporters (e.g., vSGLT, vSGLT homologs)
- **Key residues**: Trp48 (pi-stacking), Asn64 (H-bond), Thr13 (H-bond) — alanine mutations of all three reduce or ablate transport

## Transport Mechanism

**"Free ride" model**: The substrate takes a passive role — simulations with and without glucose show essentially identical conformational states and transition sequences. The substrate does not cause major structural rearrangements; instead, it passively translocates as the transporter undergoes its conformational cycle.

## MD Simulations

- **Total**: >175 µs of unguided (unbiased) atomic-level MD
- **Key finding**: Spontaneous outward-open → inward-open transitions captured without any prior structural knowledge
- **Validation**: Simulated conformations match crystal structures of occluded and inward-open states
- **Transition rate**: ~1 transition per ~14 µs of simulation of outward-open and occluded states

## Cross-References

- [nTMATE2-transporter](/proteins/nTMATE2-transporter/) — Another LCP-crystallized transporter; shows conformational plasticity
- [xray-crystallography](/methods/structure-determination/xray-crystallography/) — Structure determination method
- [molecular-replacement](/methods/structure-determination/molecular-replacement/) — Phasing method used
- [monoolein](/methods/crystallization/monoolein/) — [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) matrix for LCP crystallization
- [peg-400](/reagents/additives/peg-400/) — Crystallization precipitant
- [ddm](/reagents/detergents/ddm/) — Solubilization detergent
- [superdex-columns](/methods/purification/superdex-columns/) — SEC column type
- [glucose](/reagents/ligands/glucose/) — Substrate
- [sotb](/proteins/sotb/) — E. coli MFS transporter; rocker-switch mechanism
- [mfs-transporter](/concepts/mfs-transporter/) — Major facilitator superfamily
- [adenine-nucleotide-transporter](/proteins/adenine-nucleotide-transporter/) — Mitochondrial carrier with [alternating-access](/concepts/alternating-access/)