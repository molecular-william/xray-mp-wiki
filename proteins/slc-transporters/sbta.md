---
title: SbtA (High-Affinity Sodium-Dependent Bicarbonate Transporter, Synechocystis sp. PCC 6803)
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, transporter, xray-crystallography]
sources: [doi/10.1073##pnas.2101632118]
verified: false
---

# SbtA (High-Affinity Sodium-Dependent Bicarbonate Transporter, Synechocystis sp. PCC 6803)

## Overview

SbtA is a high-affinity, sodium-dependent bicarbonate (HCO3-) transporter found in the cyanobacterial CO2-concentrating mechanism ([CCM](/xray-mp-wiki/concepts/miscellaneous/co2-concentrating-mechanism/)). It forms a homotrimer in the membrane, with each protomer comprising 10 transmembrane helices organized into a scaffold domain (TMs 1-2, 6-7) and a core domain (TMs 3-5, 8-10). The core domain contains the HCO3-/Na+ binding site formed by a TM cross (TM4a/b and TM9a/b). SbtA uses an [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) for bicarbonate transport, where the core domain undergoes rigid-body movement to translocate HCO3- across the membrane. SbtA is allosterically inhibited by [SBTB](/xray-mp-wiki/proteins/slc-transporters/sbtb/), a PII-like regulatory protein, which binds to the cytoplasmic surface and locks SbtA in an inward-facing state.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.2101632118 | (not deposited) | 2.7 | Not applicable (cryo-EM) | Full-length SbtA (Synechocystis sp. PCC 6803) with C-terminal His-tag, co-expressed with [SBTB](/xray-mp-wiki/proteins/slc-transporters/sbtb/) | HCO3-, Na+, AMP |
| doi/10.1073##pnas.2101632118 | (not deposited) | 3.2 | (not specified) | Full-length SbtA (Synechocystis sp. PCC 6803) with C-terminal His-tag, co-expressed with [SBTB](/xray-mp-wiki/proteins/slc-transporters/sbtb/) | HCO3-, Na+ |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and expression | E. coli C43(DE3) heterologous expression | — | LB medium with 50 ug/mL [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin/) | Co-expression of SbtA (C-terminal His-tag) and [SBTB](/xray-mp-wiki/proteins/slc-transporters/sbtb/) from pRSFDuet plasmid; induced with 0.25 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600=1.2; 14 h growth at 37C |
| Membrane preparation | French press and ultracentrifugation | — | 100 mM NaCl, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 mM AMP | Cells homogenized by French press; membrane fraction collected at 150,000 x g for 1 h |
| Solubilization | Detergent solubilization | — | 100 mM NaCl, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 2 mM AMP + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (n-dodecyl-beta-D-maltopyranoside) | Solubilized for 2 h at 4C; insoluble material removed at 20,000 x g for 45 min |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni2+-NTA agarose (Qiagen) | Wash: 100 mM NaCl, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 0.018% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 2 mM AMP, 25 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); Elution: same buffer with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.018% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |  |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | SEC ([Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/)) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) | 100 mM NaCl, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 0.18% DM, 2 mM AMP + 0.18% DM ([n-Decyl-β-D-maltoside](/xray-mp-wiki/reagents/detergents/dm/)) | Peak fractions concentrated to ~5 mg/mL for crystallization |


## Crystallization

### doi/10.1073##pnas.2101632118

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (not explicitly specified) |
| Protein sample | Purified SbtA-[SBTB](/xray-mp-wiki/proteins/slc-transporters/sbtb/) complex at ~5 mg/mL in 0.18% DM |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystal structure solved at 3.2 A by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using the [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) map as template |


## Biological / Functional Insights

### Bicarbonate and sodium binding site

The substrate-binding site is formed by a TM cross where broken helices TM4a/b and TM9a/b cross over. HCO3- is coordinated by residues from TM4 and TM9. Na+ is coordinated by nearby residues. The binding site is located in the core domain, accessible from the cytoplasm in the inward-facing state.

### Elevator transport mechanism

SbtA adopts an [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) for bicarbonate transport. The core domain (TMs 3-5, 8-10) undergoes rigid-body movement relative to the scaffold domain (TMs 1-2, 6-7) to translocate HCO3- across the membrane. This mechanism is shared with structurally homologous SLC family transporters including [NHAA](/xray-mp-wiki/proteins/slc-transporters/nhaa/), NhaP, NapA, and ASBT_NM, which share similar overall topology despite low sequence identity.

### Trimeric functional unit

SbtA forms a homotrimer that is the functional unit. The scaffold domain mediates inter-subunit interactions along the trimer interface. Each [SBTB](/xray-mp-wiki/proteins/slc-transporters/sbtb/) protomer binds to the cytoplasmic surface of one SbtA protomer to form a 1:1 heterodimer within the overall 3:3 complex.


## Cross-References

- [SbtB (PII-Like Regulatory Protein, Synechocystis sp. PCC 6803)](/xray-mp-wiki/proteins/slc-transporters/sbtb/) — SbtB is the allosteric regulatory protein that binds to SbtA and inhibits bicarbonate transport
- [CO2-Concentrating Mechanism](/xray-mp-wiki/concepts/miscellaneous/co2-concentrating-mechanism/) — SbtA is one of five dissolved inorganic carbon uptake systems in the cyanobacterial CCM
- [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) — SbtA uses an elevator mechanism for bicarbonate transport
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — SbtA is allosterically inhibited by SbtB through T-loop insertion
- [NhaA Sodium/Proton Antiporter](/xray-mp-wiki/proteins/slc-transporters/nhaa/) — Structural homologue sharing similar TM topology and transport mechanism
- [Na+/H+ Antiporter NapA from Thermus thermophilus](/xray-mp-wiki/proteins/slc-transporters/nap-a/) — Structural homologue sharing similar elevator transport mechanism
- [ASBT-NM (Bacterial Homologue of the Bile Acid Sodium Symporter ASBT)](/xray-mp-wiki/proteins/slc-transporters/asbt-nm/) — Structural homologue sharing similar 10 TM topology and elevator-like transport mechanism
- [Ammonium Transporter AmtB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/e-coli-amtb/) — Analogous regulatory system where PII protein GlnK allosterically inhibits AmtB
- [GlnK PII Signal Transduction Protein (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/glnk/) — SbtB is functionally analogous to GlnK, both being PII-family regulators
- [PII Signal Transduction Protein Family](/xray-mp-wiki/concepts/signaling-receptors/pii-protein-family/) — SbtB is a member of the PII protein family
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Main structural method used (2.7 A cryo-EM structure)
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Complementary crystal structure at 3.2 A resolution
- [Nanodisc Reconstitution](/xray-mp-wiki/methods/nanodisc-reconstitution/) — SbtA-SbtB was reconstituted into POPG nanodiscs for cryo-EM
