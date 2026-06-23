---
title: "Yeast ATP Synthase c10 Ring (Oligomycin-Bound)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, channel, membrane-protein]
sources: [doi/10.1073##pnas.1207912109]
verified: false
---

# Yeast ATP Synthase c10 Ring (Oligomycin-Bound)

## Overview

The c10 ring of the yeast mitochondrial F1Fo ATP synthase is a homomeric ring of 10 subunit-c molecules that forms the proton turbine of the ATP synthase. Each subunit-c is a hairpin of two transmembrane helices that spans the inner mitochondrial membrane. The essential carboxylate residue Glu59 in helix 2 is required for proton translocation. This entry covers the 1.9 A resolution crystal structure of the c10 ring bound to the inhibitor [Oligomycin](/xray-mp-wiki/reagents/ligands/oligomycin/), which binds at the interface between two adjacent subunit-c molecules and blocks proton access to Glu59.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1207912109 | 4F4S | 1.90 | — | c10 ring from Saccharomyces cerevisiae ATP synthase, oligomycin-soaked crystals | oligomycin |

## Expression and Purification

- **Expression system**: Purified from Saccharomyces cerevisiae mitochondrial membranes


### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| ATP synthase purification | Native purification from yeast mitochondria | — |  | As described in reference (8) |
| c10 ring crystallization | Vapor diffusion | — | 50 mM Na citrate pH 5.5, 100 mM Na malonate pH 7.0 | Crystals soaked with 0.5 mg/mL oligomycin mixture (A, B, C) |


## Crystallization

### doi/10.1073##pnas.1207912109

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Yeast c10 ring purified from mitochondrial membranes |
| Reservoir | 50 mM Na citrate pH 5.5, 100 mM Na malonate pH 7.0 |
| Temperature | not specified |
| Cryoprotection | not specified |
| Notes | Crystals were soaked in solution containing 0.5 mg/mL oligomycin (60% oligomycin A, mixture of A/B/C) to reduce MPD concentration to 5% |


## Biological / Functional Insights

### Oligomycin binds at the subunit-c interface and blocks proton translocation

Oligomycin binds to helix 2 of two adjacent subunit-c molecules, making contact with both chains. The carboxyl side chain of Glu59, essential for proton translocation, forms an H-bond with oligomycin via a bridging water molecule. The hydrophobic face of oligomycin covers the hydrophobic surface of subunit-c, burying 345 A2 of hydrophobic surface. Oligomycin locks Glu59 in a semiclosed conformation, shielding it from the aqueous environment of the proton half-channel.

### Common drug-binding site on the c-ring

The oligomycin-binding site overlaps with the binding site of other antibiotics including ossamycin, venturicidin, and the anti-tuberculosis drug R207910 (TMC207). Mutations conferring resistance to these drugs map to residues in or near the oligomycin-binding site. The binding site residues are 100% conserved between human and yeast but differ in bacteria, explaining differential sensitivity.


## Cross-References

- [Oligomycin](/xray-mp-wiki/reagents/ligands/oligomycin/) — Inhibitor bound to the c10 ring; defines the drug-binding site
