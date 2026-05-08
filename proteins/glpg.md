---
title: GlpG Rhomboid Intramembrane Protease (E. coli)
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [intramembrane-protease, rhomboid, serine-protease, membrane-protein, tm-helices]
sources: [doi/10.1016##j.jmb.2007.10.014]
---

# GlpG Rhomboid Intramembrane Protease (E. coli)

## Overview

The crystal structure of Escherichia coli GlpG, a rhomboid family serine intramembrane protease, refined at 1.7 A resolution. GlpG consists of seven transmembrane helices with an internal water-filled cavity harboring the Ser-His catalytic dyad. A novel L1 loop lies partially embedded in the membrane at the side of the TM helices bundle. The L1 loop contains a conserved WR motif (Trp136-Arg137) critical for optimal proteolytic activity. A 20-A-wide hydrophobic belt surrounds the protease, thinner than the typical 30-A lipid bilayer core, suggesting membrane compression around the protein.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2007.10.014 | 3B44 | 1.7 A | not specified | E. coli GlpG wild type | -- |
| doi/10.1016##j.jmb.2007.10.014 | 3B45 | 1.7 A | not specified | GlpG W136A mutant | -- |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: GlpG with His6-Myc tag

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Detergent solubilization | -- | -- | Cells expressing GlpG-His6-Myc |
| Purification | [Ni-NTA affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | -- | Standard purification protocol for GlpG |


## Crystallization

### doi/10.1016##j.jmb.2007.10.014

| Parameter | Value |
|---|---|
| Method | Detergent-based crystallization |
| Protein sample | Wild-type GlpG |
| Reservoir | -- |
| Temperature | -- |
| Notes | Crystallized from similar conditions as previously reported; refined at 1.7 A |


## Biological / Functional Insights

### L1 loop half-inserted in membrane

The L1 loop is partially embedded in the lipid bilayer, as demonstrated by AMS (2-acetamido-3-(maleimido)propanesulfonic acid) modification of cysteine mutants in intact cells. Four of 11 cysteine mutants (D116C, F127C, L131C, R137C) were modifiable by membrane-impermeable AMS in spheroplasts, while others were protected. Upon detergent addition, all became modifiable. This confirms lateral insertion of L1 into the hydrocarbon region of the lipid bilayer.

### WR motif (Trp136-Arg137) essential for activity

The conserved WR sequence at the distal tip of L1 is critical for optimal activity. W136A and R137A mutants retained some activity but showed significant reduction under low-expression or suboptimal substrate conditions. Deletion of both residues (Delta WR) further reduced activity. Complete L1 deletion (Delta L1, residues 116-142) abolished activity entirely. The W136A mutation attracted 6 water molecules into the void left by the indole ring, changing the local polarity.

### 20-A hydrophobic belt and substrate entry model

The hydrophobic belt around GlpG is only 20 A wide, thinner than the typical 30 A lipid bilayer core. This membrane compression forces substrate TM helix ends to partition out of the hydrophobic core before bending into the protease active site. The active site (Ser-His catalytic dyad) and the L5 cap must be positioned within a few angstroms of the membrane surface for catalysis. Substrate cleavage occurs primarily from the interfacial region rather than from within the hydrophobic core.

### Catalytic mechanism

GlpG employs a Ser-His catalytic dyad housed in an internal water-filled cavity. The L5 cap blocks a side portal that leads to the active site, and conformational plasticity of L5 may allow substrate entry. The L1 loop is structurally rigid, unlike the flexible L5 cap and TM helix S5, suggesting substrate access occurs from the side opposite L1.


## Cross-References

- [Detergents](/xray-mp-wiki/reagents/detergents/) — Detergent solubilization required for purification and crystallization
- [Intramembrane Proteolysis](/xray-mp-wiki/concepts/intramembrane-proteolysis/) — GlpG is the archetypal rhomboid intramembrane protease
