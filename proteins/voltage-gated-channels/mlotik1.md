---
title: MlotiK1 (Mesorhizobium loti Cyclic Nucleotide-Regulated Potassium Channel)
created: 2026-06-17
updated: 2026-06-17
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0711533105]
verified: false
---

# MlotiK1 (Mesorhizobium loti Cyclic Nucleotide-Regulated Potassium Channel)

## Overview

MlotiK1 is a bacterial cyclic nucleotide-regulated potassium channel from Mesorhizobium loti, a member of the six-transmembrane helix (6 TM) tetrameric cation channel superfamily. It is a non-voltage-gated 6 TM channel, meaning its S1-S4 domain does not function as a voltage sensor. The crystal structure of MlotiK1 (Clayton et al., PNAS 2008, 3.1 A resolution, space group R3) was determined in the presence of 200 uM cAMP, with the C-terminal cyclic nucleotide-binding (CNB) domains disordered and not resolved. This was the first structure of a non-voltage-gated 6 TM channel, revealing how the S1-S4 domain and its associated S4-S5 linker serve as a clamp constraining the gate of the pore. The structure revealed a compact S1-S4 domain with a 3_10 helical conformation in S4 that buries positively charged residues within the protein core, distinct from the voltage-sensor paddle architecture of voltage-gated channels. A prominent feature is that Phe-203 side chains fill the central cavity, suggesting a cavity-based gating mechanism closer to the selectivity filter than the canonical helix bundle crossing gate. Mutagenesis (F203A, Y215A) increased rubidium uptake rates approximately 6-fold, supporting a gating role for these residues.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0711533105 |  | 3.1 | R3 | MlotiK1 channel from Mesorhizobium loti, full-length transmembrane regions (CNB domains disordered) | 200 uM cAMP (present during crystallization; K+ in pore) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length MlotiK1 from Mesorhizobium loti, expressed and purified as described in Nimigean et al. (2004) and Nimigean & Pagel (2007)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Expression in E. coli |  |  | Protein expressed and purified according to variations of protocols described in Nimigean et al. (2004) and Nimigean & Pagel (2007) |
| Purification | Size-exclusion chromatography |  | 150 mM KCl | Purified protein in buffer with 150 mM KCl |


## Crystallization

### doi/10.1073##pnas.0711533105

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | MlotiK1 at 10 mg/ml in 200 uM cAMP, 5 mM lauryl dimethylamide oxide (LDAO), 150 mM KCl |
| Reservoir | 10% PEG 2000, 100 mM trisodium citrate pH 5.6 |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Crystals grown in the presence of substoichiometric amounts of cAMP (200 uM). KCl replaced by RbCl or CsCl by size exclusion for heavy-atom derivatives. Best diffracting crystals grew with 200 uM cAMP present. C-terminal CNB domains disordered. Data collected from native, RbCl co-crystal, and CsCl co-crystal forms. |


## Biological / Functional Insights

### First structure of a non-voltage-gated 6 TM channel

MlotiK1 is the first reported structure of a non-voltage-gated 6 TM tetrameric cation channel. The structure defines the transmembrane regions (pore and S1-S4 domains) at 3.1 A resolution, revealing overall architecture similar to voltage-gated channels but with key differences in the S1-S4 domain. The CNB domains are not resolved in the structure.

### S1-S4 domain as a structural clamp on the pore gate

In MlotiK1, the S1-S4 domain and its S4-S5 linker form a cuff around the C-terminal ends of the S6 inner helices, constraining the gate in a closed conformation. Superposition with the open Kv1.2 channel shows the Kv1.2 S6 helices would clash with the MlotiK1 S4-S5 linkers. To open to the same extent as Kv1.2, the S4-S5 linkers would need to shift outward (~5 A) and upward (~5 A). This structural arrangement provides a mechanism by which the S1-S4 domain serves as a clamp to regulate pore opening.

### Compact S1-S4 domain distinct from voltage sensors

The MlotiK1 S1-S4 domain forms a compact arrangement of four transmembrane helices with interdigitated side chains forming a solid protein core. This contrasts with the voltage sensor of Kv1.2 where the S3b-S4 paddle motif is tilted away from S1 and S2, creating a water-accessible crevice. The MlotiK1 S1-S4 domain also interacts more extensively with the pore (~1200 A2 buried surface area) than in Kv1.2, and the entire domain is rotated relative to Kv1.2, paralleling the closed conformation of the gate.

### 3_10 helix in S4 buries positively charged residues

The S4 helix in MlotiK1 adopts a 3_10 helical conformation over a segment, which is more tightly wound than an alpha-helix (i to i+3 hydrogen bonding instead of i to i+4). This conformation causes every third residue to fall on the same helical face, burying positively charged residues (equivalent to R2, R3, R4, K5, R6 in Kv channels) within the core of the S1-S4 domain, shielded from the lipid environment. This is distinct from Kv1.2 where these residues are exposed to lipid. A reversible transition between 3_10 and alpha-helix could provide the structural basis for S4 rotational movements upon stimulation.

### Cavity gating by Phe-203 in the central cavity

A prominent feature of the MlotiK1 pore is that the side chains of Phe-203 fill the central cavity, which is a water-filled cavity in other potassium channels like KcsA. This occludes the ion conduction pathway at a position closer to the selectivity filter than the canonical helix bundle crossing gate. The F203A mutation increased rubidium uptake rate ~6-fold (time constant 17 min vs 94 min for wild-type), and Y215A also accelerated uptake (25 min). This suggests a novel gating mechanism where the cavity can be occluded by hydrophobic side chains, representing a gate that could operate independently of the bundle crossing gate.

### S4-S5 linker in a closed 6 TM channel

The MlotiK1 structure provides the first opportunity to inspect the S4-S5 linker in the context of a closed 6 TM channel. In voltage-gated channels, the S4-S5 linker interacts with the S6 gate region during gating. In MlotiK1 (closed), the linkers form a cuff around the gate regions, restricting S6 movement. Superposition with open Kv1.2 reveals that the Kv1.2 linker is shifted outward (~5 A) and upward (~5 A) relative to MlotiK1, consistent with the role of the linker as a gating element.

### Absence of voltage-sensing machinery

MlotiK1 lacks the conserved negatively charged residues in S2 and S3 (E283 and E293 in Shaker) that are essential for voltage sensing in voltage-gated potassium channels. The compact S1-S4 domain architecture, absence of a water-accessible crevice, and burial of positively charged S4 residues within the protein core indicate MlotiK1 does not function as a voltage sensor. The S1-S4 domain instead serves a structural role as a clamp regulating the pore gate in concert with the C-terminal CNB domain.


## Cross-References

- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — KcsA was used as the molecular replacement search model for MlotiK1 structure determination; both are tetrameric potassium channels with conserved pore architecture
- [S4-S5 Linker Interaction Motif](/xray-mp-wiki/concepts/s4-s5-linker-interaction-motif/) — The MlotiK1 structure reveals the S4-S5 linker conformation in a closed 6 TM channel, providing a structural template for understanding linker function in both voltage-gated and non-voltage-gated channels
- [Channel Gating](/xray-mp-wiki/concepts/channel-gating/) — MlotiK1 reveals a novel cavity gating mechanism where Phe-203 side chains occlude the central cavity, representing a gate closer to the selectivity filter than the helix bundle crossing
