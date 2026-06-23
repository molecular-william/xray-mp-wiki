---
title: "Human Naᵥ1.4 C-Terminal Domain in Complex with Calmodulin"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-09570-7]
verified: false
---

# Human Naᵥ1.4 C-Terminal Domain in Complex with Calmodulin

## Overview

Voltage-gated sodium channels Naᵥ1.4 (skeletal muscle) and Naᵥ1.5 (cardiac) are regulated by [calmodulin (CaM)](/xray-mp-wiki/reagents/ligands/calmodulin/) in an isoform-specific manner. The crystal structures of the Naᵥ1.4 C-terminal domain (CTerm) in complex with apo CaM at 1.79 Å resolution (PDB 6MBA) and with (Ca²⁺)₄-CaM at 3.3 Å resolution (PDB 6MC9) reveal the structural basis for Ca²⁺-dependent inactivation (CDI) differences between isoforms. The Naᵥ1.5 CTerm contains a Ca²⁺-dependent N-lobe binding motif (NLBM) in the post-IQ region that prevents CDI, while Naᵥ1.4 lacks this motif, allowing the N-lobe to interact elsewhere in the channel and mediate CDI. Deletion of the post-IQ NLBM in Naᵥ1.5 unveils robust CDI.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-019-09570-7 | 6MBA | 1.79 | C 1 2 1 | Naᵥ1.4 CTerm Short (1599–1754) + apo CaM |  |
| doi/10.1038##s41467-019-09570-7 | 6MC9 | 3.3 | P 4₃ 2₁ 2 | Naᵥ1.4 CTerm Short (1599–1754) + (Ca²⁺)₄-CaM |  |

## Expression and Purification

- **Expression system**: Escherichia coli BL21-CodonPlus RIL
- **Construct**: H. sapiens Naᵥ1.4 CTerm Long (residues 1599–1764) and Short (residues 1599–1754) with N-terminal GST tag; R. norvegicus CaM (CALM2)

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Affinity chromatography | Glutathione Sepharose 4 Fast Flow | — | PBS | Co-expressed Naᵥ1.4 CTerm–GST and CaM complex purified together |
| Tag cleavage | PreScission protease | — | 20 mM Tris, 50 mM NaCl, 1 mM DTT, pH 7.4 | Dialysis overnight at 4 °C |
| Ion exchange chromatography | Source Q anion exchange | — | 20 mM Tris, 1 mM DTT, 50–500 mM NaCl gradient |  |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Isoform-specific Ca²⁺-dependent inactivation

Naᵥ1.4 exhibits robust CDI while Naᵥ1.5 does not. The difference is controlled by the post-IQ motif: Naᵥ1.5 contains a Ca²⁺-dependent N-lobe binding motif (NLBM) that sequesters the CaM N-lobe, preventing CDI. Naᵥ1.4 lacks this motif, allowing the CaM N-lobe to interact with other channel regions to mediate CDI.

### CaM C-lobe anchoring

The CaM C-lobe remains bound to the IQ motif of Naᵥ helix αVI in both apo and Ca²⁺-saturated states, maintaining a semi-open configuration. This anchoring allows the N-lobe to switch binding targets depending on Ca²⁺ concentration.


## Cross-References

- [Sodium Channel Gating](/xray-mp-wiki/concepts/transport-mechanisms/sodium-channel-gating/) — CaM regulates Naᵥ channel gating via Ca²⁺-dependent inactivation
- [Sodium Channel Inactivation](/xray-mp-wiki/concepts/transport-mechanisms/sodium-channel-inactivation-gating/) — CDI is controlled by the post-IQ motif and N-lobe binding
- [Sodium Allosteric Modulation](/xray-mp-wiki/concepts/signaling-receptors/sodium-allosteric-modulation/) — Ca²⁺-CaM binding allosterically modulates Naᵥ channel activity
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component in purification
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Reducing agent in purification buffers
- [Ion Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) — Source Q anion exchange used for final purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Used for structure determination of both Naᵥ1.4 CTerm complexes
