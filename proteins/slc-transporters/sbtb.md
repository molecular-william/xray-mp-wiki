---
title: SbtB (PII-Like Regulatory Protein, Synechocystis sp. PCC 6803)
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [xray-crystallography, transporter]
sources: [doi/10.1073##pnas.2101632118]
verified: false
---

# SbtB (PII-Like Regulatory Protein, Synechocystis sp. PCC 6803)

## Overview

SbtB is a PII-like signal transduction protein from the cyanobacterium Synechocystis sp. PCC 6803 that allosterically regulates the bicarbonate transporter [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/). SbtB forms a homotrimer in the cytoplasm, with each protomer adopting a classic PII fold characterized by four antiparallel beta-strands and flanking alpha-helices. SbtB binds adenyl nucleotides (AMP, ADP, ATP, cAMP) at the trimer interfaces, and the identity of the bound nucleotide dictates the conformation of its T-loop, which controls [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) binding. AMP binding stabilizes the T-loop in an extended conformation that inserts into the cytoplasmic cavity of [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/), locking the transporter in an inward-facing state and inhibiting bicarbonate transport. cAMP binding disrupts the T-loop conformation, relieving inhibition.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.2101632118 | (not deposited) | 2.7 | Not applicable (cryo-EM) | Full-length SbtB (Synechocystis sp. PCC 6803) in complex with [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) | AMP |
| doi/10.1073##pnas.2101632118 | (not deposited) | 3.2 | (not specified) | Full-length SbtB (Synechocystis sp. PCC 6803) in complex with [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) | None (no AMP in crystal structure) |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Co-expression | E. coli C43(DE3) with pRSFDuet-SbtA-SbtB | — |  | [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) with C-terminal His-tag; SbtB untagged. Co-purification with [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) via pull-down. |
| Co-purification | Ni-NTA affinity + SEC | — | 100 mM NaCl, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 2 mM AMP; 0.018% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) or 0.18% DM | AMP (2 mM) in purification buffer essential for stable 1:1 SbtA-SbtB complex. ADP also supports complex; cAMP and ATP do not. |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### AMP-dependent T-loop stabilization

The T-loop of SbtB (residues ~37-54) adopts a defined conformation when AMP is bound at the trimer interface. AMP forms hydrogen bonds with residues Ser42 and Arg43 from the T-loop and Gly89 from beta4. Arg43 also hydrogen bonds with Asp86 from the alpha2-beta4 loop. These interactions collectively stabilize the T-loop in an extended conformation capable of [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) binding.

### Allosteric inhibition of SbtA

The T-loop inserts into the cytoplasmic cavity of [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) formed between its scaffold domain (TMs 1-2, 6-7) and core domain (TMs 3-5, 8-10). This locks [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) in an inward-facing state, preventing the conformational changes required for bicarbonate transport. The mechanism is analogous to AmtB regulation by [GLNK](/xray-mp-wiki/proteins/other-ion-channels/glnk/) in bacteria.

### Nucleotide selectivity

AMP and ADP stabilize the T-loop and promote SbtA-SbtB complex formation, while cAMP and ATP do not. cAMP binding to SbtB would cause steric clash with Arg46 and lose key hydrogen bonds from Ser42 and Arg43, distorting the T-loop and preventing [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) interaction. This creates a regulatory switch responsive to cellular energy and carbon status.

### PII family conservation

SbtB belongs to the PII family of signal transduction proteins, which regulate nitrogen assimilation and carbon homeostasis in bacteria and archaea. The regulation of [SBTA](/xray-mp-wiki/proteins/slc-transporters/sbta/) by SbtB closely parallels the regulation of ammonium transporter AmtB by [GLNK](/xray-mp-wiki/proteins/other-ion-channels/glnk/) in E. coli, where [GLNK](/xray-mp-wiki/proteins/other-ion-channels/glnk/) also forms a trimer with ADP at the dimer interface and inserts its T-loop to block the AmtB channel.


## Cross-References

- [SbtA (High-Affinity Sodium-Dependent Bicarbonate Transporter)](/xray-mp-wiki/proteins/slc-transporters/sbta/) — SbtB is the allosteric regulator of SbtA bicarbonate transporter
- [PII Signal Transduction Protein Family](/xray-mp-wiki/concepts/signaling-receptors/pii-protein-family/) — SbtB is a member of the PII protein family
- [GlnK PII Signal Transduction Protein (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/glnk/) — SbtB is functionally and structurally analogous to GlnK
- [Ammonium Transporter AmtB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/e-coli-amtb/) — AmtB-GlnK is the paradigmatic system of PII-mediated transporter regulation
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — SbtB allosterically inhibits SbtA through T-loop insertion
- [CO2-Concentrating Mechanism](/xray-mp-wiki/concepts/miscellaneous/co2-concentrating-mechanism/) — SbtA-SbtB system regulates bicarbonate uptake in the cyanobacterial CCM
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Main structural method used
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Complementary crystal structure
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Method used in structure determination or purification
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification or crystallization
