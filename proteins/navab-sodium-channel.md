---
title: NaVAb Sodium Channel
created: 2026-04-27
updated: 2026-04-27
type: protein
tags: [ion-channel, channel]
sources: [doi/10.1016##j.cell.2019.06.031]

category: proteins
layout: default
---



# NaVAb Voltage-Gated Sodium Channel

## Overview

NaVAb is an ancestral bacterial voltage-gated sodium channel from *Anabaema bradleyi*. It is composed of a homotetramer of identical subunits, each containing a voltage-sensing module (VS: S0–S4), an S4-S5 helical linker, and a pore module (PM: S5-P-S6). NaVAb is the likely evolutionary ancestor of both eukaryotic NaV and CaV channels.

## Structural States

### Activated-State Structures ([xray-crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/))

Multiple activated-state structures of NaVAb have been solved by [xray-crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) (Payandeh et al., 2011, 2012; Lenaeus et al., 2017), showing outward-positioned S4 helices and open activation gates.

### Resting-State Structure (Cryo-EM, 4.0 Å)

The resting-state structure was solved by [cryoem](/xray-mp-wiki/methods/structure-determination/cryoem/) at 4.0 Å resolution (Wisedchaisri et al., 2019, Cell), revealing the complete voltage-dependent gating mechanism:

- **Construct**: MBP-NaVAb/KAV/G94C/Q150C — voltage-shifting mutations (N49K, L109A, M116V → KAV) + disulfide crosslink (G94C-Q150C) to lock the resting state
- **Expression**: [sf9-cells](/xray-mp-wiki/methods/expression-systems/sf9-cells/) (baculovirus system)
- **Detergent**: [digitonin](/xray-mp-wiki/reagents/detergents/digitonin/) (high purity) for solubilization and [cryoem](/xray-mp-wiki/methods/structure-determination/cryoem/) sample preparation
- **Resolution**: 4.0 Å overall; 3.0–3.9 Å in pore module; 4–5 Å in VS (S0–S2)
- **Key findings**: S4 drawn intracellularly with three gating charges passing through the transmembrane electric field; elbow bend in S4-S5 linker tightens collar around S6 activation gate; supports classical "sliding helix" mechanism
- **Voltage-sensing domain conformational changes**:
  - **New S3-S4 loop fold**: Extracellular end of S4 segment adopts novel fold in resting state
  - **Striking S4 inward movement**: S4 helix moves intracellularly by ~11.5 Å compared to activated state
  - **S4-S5 linker elbow bend**: Sharply angled bend at linker junction tightens collar around S6 gate
  - **Extracellular aqueous cleft**: Formed between S1-S2 and S3-S4 helical hairpins in resting state
  - **S3 tilt**: S3 helix tilts slightly toward S4; S3-S4 loop is shorter in resting vs activated state
- **Electrophysiology**: KAV mutations shift V₁/₂ from -21.8 mV (N49K) to 59.1 mV (full KAV), enabling resting-state capture at 0 mV

## Expression and Purification

- **Expression system**: [sf9-cells](/xray-mp-wiki/methods/expression-systems/sf9-cells/) (baculovirus [baculovirus-expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression/))
- **Construct design**:
  - MBP (maltose-binding protein) fusion tag at N-terminus
  - KAV voltage-shifting mutations (N49K, L109A, M116V)
  - C-terminal Δ28 truncation
  - G94C/Q150C disulfide crosslink for resting-state stabilization
- **Detergent**: [ddm](/xray-mp-wiki/reagents/detergents/ddm/) (n-dodecyl-β-D-maltopyranoside) for membrane solubilization
- **Purification**: Anti-FLAG [affinity-chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (N-terminal FLAG tag), [affinity-chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (His-tag), followed by [size-exclusion-chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)
- **SEC buffer**: 20 mM [hepes-buffer](/xray-mp-wiki/reagents/buffers/hepes-buffer/) pH 7.5, 150 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 0.02% [digitonin](/xray-mp-wiki/reagents/detergents/digitonin/)
- **Cryo-EM grid preparation**: MBP-NaVAb/KAV/G94C/Q150C in [digitonin](/xray-mp-wiki/reagents/detergents/digitonin/) detergent

## Crystallization (Activated State)

- **Method**: [xray-crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) (activated state structures)
- **Detergent**: [ddm](/xray-mp-wiki/reagents/detergents/ddm/) for solubilization
- **Disulfide-locked constructs**: V100C-Q150C (activated state), G94C-Q150C (resting state)

## Gating Mechanism

The resting-state structure completes the picture of NaVAb voltage gating:

1. **Resting state**: S4 drawn intracellularly; elbow at S4-S4-S5 linker junction tightens S4-S5 linker collar around S6 gate; activation gate tightly closed (I217)
2. **Activation**: S4 moves outward by ~11.5 Å (sliding helix); elbow angle opens to ~90°; collar loosens; S6 segments bend and rotate to open gate to 10.5 Å diameter
3. **Key coupling**: Hydrophobic residues (I119, L123, V126) in S4-S5 linker interact with S6 (N211, I216) to maintain closed state; outward S4 movement exchanges these interactions to allow opening

## Pharmacological Implications

The resting-state structure reveals fenestrations providing hydrophobic drug access to the central cavity, with implications for sodium channel pharmacology and drug design.

## Related Entities

- [digitonin](/xray-mp-wiki/reagents/detergents/digitonin/) — Detergent used for [cryoem](/xray-mp-wiki/methods/structure-determination/cryoem/) sample preparation
- [cryoem](/xray-mp-wiki/methods/structure-determination/cryoem/) — Cryo-EM structure determination method
- [ion-channels](/xray-mp-wiki/concepts/ion-channels/) — Voltage-gated ion channel class
- [kirbac](/xray-mp-wiki/proteins/kirbac/) — Prokaryotic inwardly rectifying K⁺ channel; structural model for eukaryotic Kir channels