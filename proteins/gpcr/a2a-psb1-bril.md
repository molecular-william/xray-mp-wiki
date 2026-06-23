---
title: "Human Adenosine A2A Receptor A2A-PSB1-bRIL Complex"
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1002##anie.202115545]
verified: false
---

# Human Adenosine A2A Receptor A2A-PSB1-bRIL Complex

## Overview

The [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar) (A2AAR) is a class A GPCR and an important drug target for immuno-oncology and neurodegenerative diseases. A novel thermostabilized mutant construct, A2A-PSB1-bRIL, was engineered with a single S91K mutation that confers superior stability compared to the previously used A2A-StaR2 construct with nine mutations. This enabled the first high-resolution co-crystal structures of a GPCR in complex with PEGylated and fluorophore-labeled antagonist derivatives.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1002##anie.202115545 | 7PX4 | 2.25 A | P212121 | A2AAR with single S91K mutation, C-terminus truncated, ICL3 replaced by [bRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion protein | PSB-2113 (PEGylated [Preladenant](/xray-mp-wiki/reagents/ligands/preladenant)) |
| doi/10.1002##anie.202115545 | 7PYR | 2.6 A | P212121 | A2AAR with single S91K mutation, C-terminus truncated, ICL3 replaced by [bRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion protein | PSB-2115 (BODIPY-labeled [Preladenant](/xray-mp-wiki/reagents/ligands/preladenant) derivative) |

## Expression and Purification

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/sf9-insect-cells)
- **Construct**: A2AAR with S91K mutation (S91K in position 3,30), C-terminal truncation, ICL3 replaced by [bRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion protein

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | Sf9 insect cell expression | -- | -- + -- | Receptor expressed in [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/sf9-insect-cells); membranes harvested for binding assays and purification |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | Ni-NTA [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) | -- | [His Tag](/xray-mp-wiki/reagents/protein-tags/his-tag) on bRIL fusion partner used for affinity capture |
| [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [Size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) column | -- | Analytical SEC confirmed presence of fluorophore in A2A-PSB1-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril)-PSB-2115 complex at 495 nm absorption maximum |


## Crystallization

### doi/10.1002##anie.202115545

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | A2A-PSB1-bRIL co-crystallized with [PSB-2113 (PEGylated Preladenant)](/xray-mp-wiki/reagents/ligands/psb-2113) or PSB-2115 |
| Reservoir | not specified in main text |
| Temperature | not specified in main text |
| Growth time | not specified in main text |
| Cryoprotection | not specified in main text |
| Notes | Crystals diffracted to 2.25 A (PDB: 7PX4) and 2.6 A (PDB: 7PYR). Data deposited in the Protein Data Bank under accession codes 7PX4 and 7PYR. |


## Biological / Functional Insights

### Single S91K mutation confers superior thermostability

The A2A-PSB1-bRIL construct harbors only a single point mutation (S91K in position 3,30) in the transmembrane domain, compared to the previously optimized A2A-StaR2 construct with nine mutations. Despite the marked reduction in mutated residues, the stability of A2A-PSB1-bRIL is even greater than that of any other [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar) mutant reported to date. The S91K mutation introduces a basic lysine residue that occupies the well-known allosteric sodium binding site, stabilizing the same inactive state as sodium ions. The A2A-PSB1-bRIL receptor construct is proposed to become the new gold standard for determining A2AAR structures in its inactive state.

### S91K mutation locks the receptor in inactive conformation

The S91K mutation restrains key activation switches in the inactive conformation, preventing movements of W246(6,48), H250(6,52), and helix III required to accommodate the ribose moiety of agonists such as NECA in the ligand binding pocket. No agonist binding to A2A-PSB1-bRIL could be detected (pKi < 4.0), while high-affinity antagonist binding was preserved. The S91K-mutated [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar) was also unable to activate Gs proteins in HEK293 cells, confirming the locked inactive state.

### First GPCR structures with PEGylated and fluorophore-conjugated ligands

The obtained crystal structures represent the first crystal structures of a GPCR in complex with PEG- and fluorophore-conjugated ligands. PSB-2113 is a [PEG](/xray-mp-wiki/reagents/additives/peg) (PEG)-conjugated Preladenant derivative, and PSB-2115 is a BODIPY fluorophore-labeled derivative. No unambiguous electron density could be observed for the flexible PEG linker or the BODIPY fluorophore, which clearly sticks out of the binding pocket. The binding pocket accommodating the Preladenant scaffold is virtually identical in both structures, proving that the attached fluorophore does not interfere with A2AAR binding.

### Preladenant derivative binding mode and water displacement

The [Preladenant](/xray-mp-wiki/reagents/ligands/preladenant) derivative PSB-2113 binds to the A2AAR in the same orientation as the standard antagonist ZM241385, with key hydrogen bond interactions to N253(6,55) and E169(ECL2) by the furan oxygen atom and the 5-amino group of the heterocyclic core. The tricyclic aromatic system is stabilized by pi-pi stacking to F168(ECL2) and by hydrophobic contacts to L249(6,51) and I274(7,39). The tricyclic core extends further towards helix II, leading to the displacement of one structural water molecule from the ligand binding pocket — water molecules previously termed "unhappy waters" that would prefer to be in bulk solvent. This displacement is expected to be energetically favorable and likely contributes to the compound's high affinity.

### High A2AAR selectivity of Preladenant derivatives

[Preladenant](/xray-mp-wiki/reagents/ligands/preladenant) and its derivatives exhibit exceptional selectivity towards the other adenosine receptor subtypes of several hundred- to more than 1000-fold. The A2AAR exhibits direct hydrophobic contacts to the tricyclic Preladenant structure, including an L249(6,51) residue whose exchange to valine in the A2BAR may contribute to the observed high A2AAR selectivity. The additional pyrazole ring in Preladenant determines the direction of the elongated N7-substituent, restricting its conformation and fixing the exit vector sterically. This restricted conformation is consistent with the predominant A2AAR binding mode, whereas the analogous residue in the non-selective bicyclic antagonist ZM241385 is much more flexible.


## Cross-References

- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) — A2A-PSB1-bRIL is a thermostabilized mutant of the human [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar)
- [bRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — [BRIL](/xray-mp-wiki/reagents/protein-tags/bril) (thermostabilized apocytochrome b562 RIL) replaces ICL3 for crystallization
- [Preladenant](/xray-mp-wiki/reagents/ligands/preladenant/) — Parent compound of co-crystallized ligands [PSB-2113 (PEGylated Preladenant)](/xray-mp-wiki/reagents/ligands/psb-2113) and PSB-2115
- [PSB-2113 (PEGylated Preladenant)](/xray-mp-wiki/reagents/ligands/psb-2113/) — Co-crystallized ligand for PDB 7PX4
- [BODIPY Fluorophore](/xray-mp-wiki/reagents/additives/bodipy/) — Attached to PSB-2115 as fluorescent probe
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — PEG linker used in [PSB-2113 (PEGylated Preladenant)](/xray-mp-wiki/reagents/ligands/psb-2113) conjugate
- [ZM241385](/xray-mp-wiki/reagents/ligands/zm241385/) — Structurally related [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar) antagonist used as binding reference
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) affinity purification used for His-tagged bRIL fusion construct
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) used to confirm complex formation and monodispersity
- [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) — Crystallization method used for structure determination
