---
title: CmCLC Cl-/H+ Antiporter
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1205764109, doi/10.1126##science.1194640, doi/10.1126##science.1195230]
verified: false
---

# CmCLC Cl-/H+ Antiporter

## Overview

CmCLC is a CLC Cl-/H+ antiporter from the red alga Cyanidioschyzon merolae. Unlike the E. coli homolog [Clc Ec1](/xray-mp-wiki/proteins/slc-transporters/clc-ec1/), the Ein position in CmCLC is naturally occupied by a threonine residue rather than glutamate, yet Cl--driven H+ transport still occurs. CmCLC served as a key model system for studying the role of the glutamate gate (Egate) and the Ein residue in the CLC Cl-/H+ exchange mechanism. Structural and functional studies of CmCLC demonstrated that aspartate at the Egate position is insufficient for efficient H+ transport because its shorter side chain cannot easily reach the central Cl- binding site, and that the Ein position modulates H+ transport kinetics but is not universally essential across all CLC transporters.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1194640 | 3ORG | 3.5 |  | CmCLC from Cyanidioschyzon merolae, expressed in Hi5 insect cells |  |

## Expression and Purification

- **Expression system**: Hi5 insect cells (Trichoplusia ni.)
- **Construct**: CmCLC wild-type and mutants expressed in Hi5 insect cells

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Baculovirus expression in Hi5 insect cells | -- | -- + -- | CmCLC WT and mutants expressed in Hi5 (Trichoplusia ni.) insect cells and purified as previously described (Feng et al., 2010, Science) |


## Crystallization

### doi/10.1126##science.1194640

| Parameter | Value |
|---|---|
| Method | Not specified in this paper |
| Protein sample | Purified CmCLC |
| Reservoir | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | X-ray structure determined at 3.5 A resolution. Refer to Feng et al., 2010, Science for detailed crystallization conditions. |


## Biological / Functional Insights

### Ein position in CmCLC is threonine, not glutamate

In CmCLC, the Ein position (homologous to E203 in EcCLC) is naturally occupied by threonine rather than glutamate. Despite this difference, a Cl- gradient drives H+ transport in vesicle flux experiments. Cl--driven H+ transport persists even when the threonine is mutated to valine. Mutation of threonine to glutamate in CmCLC promotes H+ transport that is more rapid than wild-type, more similar to EcCLC kinetics.

### Aspartate at the Egate position cannot efficiently replace glutamate

In the atomic model of CmCLC, when Egate is modeled as aspartate and the possible orientations of the side chain are explored, the carboxylate can adopt the external and outer Cl- site conformations easily, but the shorter side chain suggests an energetic penalty to reaching all the way to the central Cl- site. With aspartate at the Egate position, H+ transport is measurable compared to alanine but extremely slow compared to glutamate in both CmCLC and EcCLC.

### Ein modulates H+ transport kinetics but is not universally essential

The presence of threonine (rather than glutamate) at the Ein position in CmCLC demonstrates that this residue does not play the same uniformly necessary role in CLC transporters as Egate. While mutation of Ein in EcCLC (E203) abolishes H+ transport, CmCLC with its native threonine at this position still supports Cl--driven H+ transport, though at reduced rates compared to EcCLC.


## Cross-References

- [CLC-ec1 Cl-/H+ Antiporter](/xray-mp-wiki/proteins/slc-transporters/clc-ec1/) — E. coli homolog used for comparative structural and functional studies of the CLC exchange mechanism
- [CLC Cl-/H+ Exchange Transport Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/clc-proton-transport-mechanism/) — CmCLC provided key evidence for the glutamate gate shuttle mechanism and the role of the Ein residue
- [Gluex Conformational States in CLC Proteins](/xray-mp-wiki/concepts/transport-mechanisms/gluex-conformational-states-clc/) — CmCLC structures contributed to understanding the multiple conformations of the glutamate gate
