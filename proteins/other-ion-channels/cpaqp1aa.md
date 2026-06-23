---
title: "cpAQP1aa (Climbing Perch Aquaporin 1aa)"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.26508##lsa.202201491]
verified: false
---

# cpAQP1aa (Climbing Perch Aquaporin 1aa)

## Overview

cpAQP1aa is a water-specific [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) from the climbing perch (Anabas testudineus),
a euryhaline fish species capable of acclimating from freshwater to seawater and
surviving on land. It is the first structurally and functionally characterized fish
[Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) and a homolog of mammalian [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/). The 1.9 A crystal structure reveals the
conserved [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) homotetrameric fold with six transmembrane helices and two
half-helices per monomer, but with a unique extracellular fold in loop C that creates
a constriction region on the extracellular side—a feature not seen in other [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/)
structures. The channel is water-specific, does not transport [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) or ammonia,
and is proposed to be regulated by phosphorylation at Thr38 (loop A) and Tyr107
(loop C), which may control gating from the extracellular side. Molecular dynamics
simulations suggest phosphorylation of Tyr107 causes structural perturbations
that narrow the pore, while mutation of Thr38 increases water permeability to levels
comparable to human AQP4.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.26508##lsa.202201491 | 7W7S | 1.9 | P42₁2 | C-terminally truncated cpAQP1aa (residues 1-243, untagged), expressed in Pichia pastoris |  |
| doi/10.26508##lsa.202201491 | 7W7S | 3.5 | C222₁ | C-terminally truncated cpAQP1aa (residues 1-243), expressed in Pichia pastoris |  |

## Expression and Purification

- **Expression system**: Pichia pastoris (methylotrophic yeast)
- **Construct**: Full-length cpAQP1aa (residues 1-261) with C-terminal 8xHis tag; truncated cpAQP1aa-243 (residues 1-243) both with and without C-terminal 8xHis tag
- **Notes**: Codon-optimized for P. pastoris. GCT added after start codon for Kozak consensus. Gene subcloned into pPICZA vector, transformed into aquaporin-deficient Delta33 strain by electroporation. Large-scale production in 3L fermentors with [Methanol](/xray-mp-wiki/reagents/additives/methanol/) fed-batch induction. Yield >250 g wet cells/L culture; 63 mg purified protein/L culture.

### Purification Workflow

- **Expression system**: P. pastoris
- **Expression construct**: cpAQP1aa-243 (untagged)
- **Tag info**: Untagged

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | X-press or French press | — | 20 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 4% NG, 2 mM beta-MeOH (solubilization) |  |
| Ion exchange chromatography | Resource S cation exchange | — | 20 mM [MES](/xray-mp-wiki/reagents/buffers/mes/) pH 6, 37.5 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.4% NG, 2 mM beta-MeOH | Elution with NaCl gradient (0-40% buffer B with 1 M NaCl) |
| Size-exclusion chromatography | Superdex 200 Increase | — | 20 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8, 100 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.4% NG, 2 mM beta-MeOH | Monodisperse peak; protein concentrated to ~18 mg/ml |

- **Expression system**: P. pastoris
- **Expression construct**: His-tagged cpAQP1aa-243
- **Tag info**: C-terminal 8xHis tag

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | Detergent solubilization | — | 50 mM KH2PO4 pH 7.5, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 4% NG |  |
| Affinity chromatography | Ni-NTA | — | pH 8.0 for His-tagged constructs |  |
| Size-exclusion chromatography | Superdex 200 Increase | — |  | Protein concentrated to ~18 mg/ml, stored at -80 C |


## Crystallization

### doi/10.26508##lsa.202201491

| Parameter | Value |
|---|---|
| Method | Not specified |
| Protein sample | Untagged cpAQP1aa-243 at ~18 mg/ml |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | High pH crystals (pH 7.8) in space group P42₁2 diffracted to 1.9 A. Low pH crystals (pH 6.5) in space group C222₁ diffracted to 3.5 A. Data collected at PETRA III (DESY, Hamburg) beamline P13 and ESRF beamline ID30B. |


## Biological / Functional Insights

### First structural characterization of a fish aquaporin

cpAQP1aa is the first fish [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) to be structurally and functionally
characterized. The 1.9 A crystal structure reveals the conserved [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/)
homotetrameric architecture with a unique extracellular fold not seen in
other [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) structures. This provides the first molecular insights into
water homeostasis mechanisms in fish.

### Novel extracellular constriction region formed by loop C

The cpAQP1aa structure features a unique extracellular fold in loop C that
creates a constriction region on the extracellular side, narrowing the channel
to ~1.1 A radius at Leu117 (~16 A from the NPA region). This constriction
is stabilized by a hydrogen-bonding network involving Tyr107, Arg187, and
residues 114-119 of loop C. The main structural differences compared to human
AQP4 and AQP7 are found in loops A and C.

### Water-specific channel lacking glycerol and ammonia permeability

Functional studies using stopped-flow spectroscopy on proteoliposomes showed
cpAQP1aa is water-permeable (rate constants 37.6-40.0 s^-1, compared to 95.1
s^-1 for hAQP4) but does not transport [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) or ammonia. The water
permeability is lower than hAQP4 due to the extracellular constriction region.
Structural comparison with AtTIP2;1 confirmed the pore does not support
ammonia passage.

### Phosphorylation-dependent extracellular gating mechanism

Two putative phosphorylation sites were identified: Thr38 in loop A and Tyr107
in loop C. Mutational analysis combined with 100-ns MD simulations suggests
that phosphorylation of Tyr107 causes structural perturbations that narrow the
pore (to ~1.2 A radius at the constriction) and widen the ar/R region, while
phosphorylation of Thr38 (Y107A and T38A/T38E mutants) increases water
permeability to levels comparable to hAQP4. The crystal structure likely
represents a semi-open state, with loop C acting as a gate modulated by
extracellular phosphorylation. Secreted kinases VLK (tyrosine kinase) and
DIA1/FAM69 (Ser/Thr kinase) are proposed as candidates for extracellular
phosphorylation.

### pH-independent loop C conformation

Structures determined at both pH 7.8 (1.9 A, space group P42₁2) and pH 6.5
(3.5 A, space group C222₁) show that the loop C constriction region occupies
a similar position regardless of pH, suggesting the extracellular hydrophobic
constriction is unaffected by pH changes.


## Cross-References

- [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — cpAQP1aa is a water-specific aquaporin from fish, expanding the diversity of characterized aquaporin family members
- [Aquaporin-1 (AQP1)](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) — cpAQP1aa is a homolog of mammalian AQP1; bovine AQP1 structure (1J4N) used as molecular replacement model
- [SoPIP2;1 (Spinach Plasma Membrane Aquaporin)](/xray-mp-wiki/proteins/other-ion-channels/so-pip2-1/) — Similar phosphorylation-dependent gating mechanism proposed for cpAQP1aa; loop D gating in SoPIP2;1 provides comparative model
- [Human Aquaporin 4](/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-4/) — Used as functional comparison for water permeability measurements; hAQP4 has a fully open pore with higher water transport rate
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in the context of Glycerol
- [Methanol](/xray-mp-wiki/reagents/additives/methanol/) — Referenced in the context of Methanol
- [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in the context of Tris Hcl
- [MES](/xray-mp-wiki/reagents/buffers/mes/) — Referenced in the context of MES
