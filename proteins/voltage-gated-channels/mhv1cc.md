---
title: "mHv1cc Mouse Voltage-Gated Proton Channel"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2783]
verified: false
---

# mHv1cc Mouse Voltage-Gated Proton Channel

## Overview

mHv1cc is a crystallizable construct of the mouse voltage-gated proton channel (mHv1, also known as VSOP) that includes the coiled-coil (CC) cytoplasmic domain fused to the transmembrane core. Voltage-gated proton channels play critical roles in regulating intracellular pH, facilitating the respiratory burst in phagocytes, and controlling sperm capacitation. The crystal structure of mHv1cc at 3.45 A resolution reveals a dimeric arrangement mediated by a coiled-coil interaction in the cytoplasmic C-terminal domain. The structure features a long S4 helix that extends from the transmembrane region into the cytoplasm, and double hydrophobic layers that may prevent proton leakage in the resting state while allowing proton conduction upon S4 movement.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.2783 | 3WKV | 3.45 | P6_3 | mHv1cc (S76-mHv1cc construct), Se-Met labeled for MAD phasing | none (apo structure; Zn2+ binding analyzed by anomalous signals) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: mHv1cc (S76-mHv1cc construct) with [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) labeling for MAD phasing

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression and purification | Standard E. coli expression and purification | Not specified | Not specified + Not specified | Selenomethionine-labeled protein expressed in E. coli for MAD phasing; multiple crystal forms grown (Cryst-A, Cryst-B, Se-Met1-3 variants) |


## Crystallization

### doi/10.1038##nsmb.2783

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Notes | Multiple crystal forms obtained: native Cryst-B (S76-mHv1cc) at 3.45 A resolution; [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) derivatives Se-Met1 (L107M L118M), Se-Met2, and Se-Met3 (L182M) for MAD phasing; and zinc-bound crystals (Cryst-Z1, Cryst-Z2). All crystals in space group P6_3. Initial phasing by Se-MAD at 4.3 A resolution. Native data collected to 3.45 A.
 |


## Biological / Functional Insights

### Zn2+ binding and S4 position

Zinc ions bind to the voltage-gated proton channel and modulate its activity. Bijvoet anomalous difference maps of Zn2+ were calculated at 5.0 sigma contoured level, confirming the position of S4 within the channel. The S4 helix consists of a 3_10 helix (Arg201-Arg204) and an alpha helix (Arg204-Arg207), with three arginine residues (Arg201, Arg204, Arg207) serving as gating charges.

### Double hydrophobic layers for proton conduction

The presence of two hydrophobic layers in the channel may have implications for proton permeation. Minimum S4 motion upon activation could allow protons to be conducted by recruiting water molecules into a continuous water-wire across the channel, while proton leakage is prevented in the resting state. This resembles the case of the M2 proton channel of influenza A virus, which also shows two barriers built by His37 and Trp41.

### Coiled-coil dimer interface

The cytoplasmic domain of mHv1cc forms a coiled-coil dimer interface. Sequence alignment using the 'abcdefg' heptad repeat convention shows that the dimer-interface residues (positions a and d) are conserved. Superimposition of the mHv1cc coiled-coil region (Ile225-Leu242) with the mouse Hv1 cytoplasmic coiled-coil (Ile224-Gly266) shows an RMSD of 0.670 A. The trimer observed in crystal packing is distinct from the functional dimeric assembly.

### Sequence conservation of gating-associated residues

Alignment of mHv1cc with related voltage-gated proton channels from multiple species (mouse, human, Ciona, zebrafish, etc.) shows conserved S1-S4 transmembrane segments. The gating arginine residues and the coiled-coil dimer interface are highly conserved. A table of accessibility by MTS reagent or Zn2+ maps the up-state (activated) and down-state (resting) conformations of the S4 helix.


## Cross-References

- [Channel Gating](/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/) — mHv1cc is a voltage-gated proton channel with S4-based gating mechanism
- [Influenza A M2 Proton Channel](/xray-mp-wiki/proteins/other-ion-channels/influenza-a-m2-proton-channel/) — M2 proton channel also uses double hydrophobic barrier mechanism for proton conduction
- [Voltage-Sensor Paddle](/xray-mp-wiki/concepts/construct-design/voltage-sensor-paddle/) — mHv1cc contains a voltage-sensing S4 helix with gating arginines
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Additive used in purification or crystallization buffers
