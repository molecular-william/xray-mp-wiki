---
title: F-Type Na+-ATPase c11 Rotor Ring from Ilyobacter tartaricus
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein]
sources: [doi/10.1126##science.1111199]
verified: false
---

# F-Type Na+-ATPase c11 Rotor Ring from Ilyobacter tartaricus

## Overview

The crystal structure of the membrane-embedded rotor ring of the sodium ion-translocating ATP synthase (F-type Na+-ATPase) from Ilyobacter tartaricus was determined at 2.4 A resolution. Eleven c subunits are assembled into an hourglass-shaped cylinder with 11-fold symmetry. Each c subunit consists of two transmembrane alpha helices connected by a cytoplasmic loop. Sodium ions are bound in a locked conformation close to the outer surface of the cylinder near the middle of the membrane. The coordination sphere involves Gln-32, Glu-65, Ser-66, and Val-63 from neighboring subunits. The structure supports an ion-translocation mechanism in which the binding site converts from the locked conformation into one that opens toward subunit a as the rotor ring moves through the subunit a/c interface.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1111199 | 1YCE | 2.4 |  | c11 rotor ring (11 c subunits) | Na+ |

## Expression and Purification

- **Expression system**: Ilyobacter tartaricus (native)
- **Construct**: Native c11 ring
- **Notes**: c rings were isolated from I. tartaricus membranes

### Purification Workflow

- **Expression system**: Ilyobacter tartaricus (native)
- **Expression construct**: Native c11 ring

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane isolation | Cell lysis and membrane fractionation |  |  | I. tartaricus membranes isolated |
| c ring purification | Chromatography |  | [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | c11 ring purified in detergent solution |


## Crystallization

### doi/10.1126##science.1111199

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified c11 ring in detergent |
| Reservoir | 100 mM [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) |
| Notes | Crystallized in buffer containing 100 mM [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) to promote Na+ binding |


## Biological / Functional Insights

### Sodium ion binding site and locked conformation

Each Na+ ion is coordinated by side-chain oxygens of Gln-32 (O-epsilon-1) and Glu-65 (O-epsilon-2) of one subunit and the hydroxyl oxygen of Ser-66 and backbone carbonyl oxygen of Val-63 of the neighboring subunit. The liganding distance is 2.37 +/- 0.14 A. The bound ion is surrounded by a hydrogen-bond network: O-epsilon-1 of Glu-65 accepts hydrogen bonds from Ser-66 and Tyr-70 hydroxyl groups, while N-epsilon-2 of Gln-32 donates a hydrogen bond to O-epsilon-2 of Glu-65. These interactions keep Glu-65 deprotonated at physiological pH and lock the Na+ in its binding conformation.

### Ion translocation mechanism

The Na+ binding site is located near the surface of the c ring between two C-terminal helices, allowing ion transfer to and from subunit a after side-chain movements without large backbone rearrangements. The locked conformation must convert to an open one during passage through the subunit a/c interface. This interconversion may be enabled by electrostatic interaction with the universally conserved Arg-227 of subunit a. The structure does not support the previously proposed 140-degree swiveling of the C-terminal helix model for E. coli F-ATPase.

### Comparison with NtpK structure

The overall fold of helices H3 and H4 of E. hirae NtpK is very similar to the c subunit fold, but the essential carboxylate (Glu-139 in NtpK, Asp-61 in E. coli c) differs by almost half an alpha-helical turn, corresponding to a rotation of approximately 150 degrees around the helix axis. A model of the I. tartaricus c ring based on the NtpK structure shows no intrinsic ion channel in the ring, supporting the two-half-channel model for both F- and V-ATPases.


## Cross-References

- [V-Type Na+-ATPase Rotor Ring (NtpK10) from Enterococcus hirae](/xray-mp-wiki/proteins/pumps-atpases/ehirae-v-atpase-k-ring/) — V-ATPase rotor ring with related structure and function
- [Bovine F1-ATPase (Mitochondrial ATP Synthase Catalytic Domain)](/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/) — F1 catalytic domain of the same ATP synthase class
- [F1-ATPase Rotary Catalytic Mechanism](/xray-mp-wiki/concepts/f1-atpase-rotary-mechanism/) — Rotary mechanism of F-ATPases
- [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) — Buffer component in purification or crystallization
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
