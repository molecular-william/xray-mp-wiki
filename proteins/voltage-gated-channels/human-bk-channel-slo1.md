---
title: Human BK Channel (Slo1)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1190414, doi/10.1073##pnas.1908183117, doi/10.1038##nature09252]
verified: false
---

# Human BK Channel (Slo1)

## Overview

The BK (Slo1) channel is a high-conductance voltage- and Ca2+-activated K+ channel that provides negative feedback regulation of membrane voltage and Ca2+ signaling, playing central roles in neuronal excitability, smooth muscle contractility, and hair cell tuning. It is dually regulated by membrane voltage and intracellular Ca2+. Depolarization and increased intracellular Ca2+ both cause BK channels to open, hyperpolarizing the membrane and reducing Ca2+ influx.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1190414 | 3MT5 | 3.0 |  | Human BK channel CTD (gating ring, residues 343-1061) | None |
| doi/10.1073##pnas.1908183117 | 6V5A | 2.0 |  | Human BK channel CTD L390P mutant | None |
| doi/10.1038##nature09252 | 3NAF | 3.10 | I422 | Human BK channel intracellular domain residues 329-1113, N-terminal GCN4_LI leucine zipper fusion | None (Ca2+-free state) |

## Expression and Purification

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: Human BK CTD L390P mutant (residues 343-1061)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression and purification | Standard E. coli expression and chromatography | — |  | Structure determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using PDB 3MT5 as search model with alphaB helix deleted to avoid model bias. Final model Rwork/Rfree = 20.3%/22.5% at 2.0 A. |


## Crystallization

### doi/10.1073##pnas.1908183117

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Human BK CTD L390P mutant |
| Notes | Crystal structure refined to 2.0 A resolution. L390P mutation flattens the first turn of the alphaB helix compared to wild-type, with no other notable structural changes in the CTD. |


## Biological / Functional Insights

### Tandem RCK domains form a gating ring

The C-terminal domain (CTD) contains two tandem RCK (Regulator of K+ Conductance) domains per subunit, forming a 350 kDa gating ring at the intracellular membrane surface with fourfold symmetry.

### Ca2+ bowl binding sites at the assembly interface

The Ca2+ bowl, a sequence of aspartic amino acids within RCK2, creates four Ca2+ binding sites on the outer perimeter of the gating ring at the assembly interface between RCK domains.

### Three mutation clusters define functional regions

Functionally important mutations cluster near the Ca2+ bowl, near the flexible interface (alphaF-alphaG/alphaS-alphaT) between RCK domains, and on the gating ring surface facing the voltage sensors.

### Gating ring modulates voltage sensors

The structure suggests the Ca2+ gating ring, in addition to regulating the pore directly, may also modulate the voltage sensor.

### Ca2+ bowl is an integral RCK2 element

The Ca2+ bowl is an integral structural element of the RCK2 Rossmann fold, located between beta strands betaO and betaP.

### Conserved salt bridge K448-D481

A conserved salt bridge identified in E. coli RCK domains (K448-D481) is confirmed in the BK structure, with distances of 2.7 and 3.3 Angstroms.

### Unstructured segments contain SH3 binding motifs

Two unstructured segments in the CTD contain consensus sequences for SH3 domain binding, suggesting roles in higher-level channel regulation through protein-protein interactions.

### alphaB helix/VSD interface couples Ca2+ and voltage activation

The alphaB helix at the top of each RCK1 N-lobe forms a critical interface with the S4-S5 linker and VSD of an adjacent subunit in a swapped configuration. In Ca2+-free closed channels ([Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) PDB 6V3G), the interface area per subunit is 117 A2 between alphaB and S4-S5 linker. In Ca2+-bound open channels ([Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) PDB 6V38), the interface expands to 360 A2 with S4-S5 linker plus an additional VSD interface (combined 724 A2 per subunit). The L390P proline mutation flattens the first turn of the alphaB helix (PDB 6V5A), reducing interface effectiveness.

### L390P disrupts voltage sensor-to-pore coupling

Proline mutations in the alphaB helix caused ~66 mV right shifts in G-V curves with negligible effects on gating currents. HCA model analysis showed L390P increased L0 12.8-fold and decreased coupling factor D 4.94-fold, reducing effective coupling at positive potentials by 596-fold. This demonstrates the alphaB helix is required for effective voltage sensor-to-pore coupling.

### L390P reduces Ca2+ and Mg2+ sensitivity

L390P reduced Ca2+ sensitivity by 49% (DeltaV1/2 0->100 uM Ca2+). Both Ca2+ bowl and RCK1 Ca2+ site pathways were affected. Increasing Ca2+ 100-fold did not restore sensitivity, confirming disrupted transduction rather than reduced binding. Mg2+ activation was reduced by 29%. These results indicate a shared transduction pathway for voltage, Ca2+, and Mg2+ activation through the alphaB helix/VSD interface.

### Ca2+ bowl and gating ring architecture from Nature 2010 structure

The Nature 2010 structure (PDB 3NAF) at 3.1 A revealed the full BK channel gating ring architecture in a Ca2+-free (apo) state. The cytoplasmic domain forms a tetrameric gating ring with four-fold symmetry, each subunit comprising two tandem RCK domains (RCK1 and RCK2). The Ca2+ bowl within RCK2 forms an EF-hand-like motif (alphaE, acidic loop, alphaEF helix) that is disordered in the apo state. Three Ca2+ binding sites were mapped: the Ca2+ bowl, Asp367, and Glu374/Glu399. The gating ring has a diagonal distance of ~82 A and a 20 A central hole.


## Cross-References

- [BK Channel Gating Mechanism](/xray-mp-wiki/concepts/bk-channel-gating/) — The alphaB helix/VSD interface is a key element in BK channel allosteric gating
- [Allosteric Coupling](/xray-mp-wiki/concepts/allosteric-coupling/) — HCA model analysis reveals allosteric coupling between voltage sensors and pore gate
- [RCK Domain Gating Ring](/xray-mp-wiki/concepts/rck-domain-gating-ring/) — The CTD gating ring houses Ca2+ sensors and transduces Ca2+ binding to pore opening
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
