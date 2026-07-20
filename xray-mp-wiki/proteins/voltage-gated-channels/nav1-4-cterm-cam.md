---
title: "Human Naᵥ1.4 C-Terminal Domain in Complex with Calmodulin"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-09570-7]
verified: agent
uniprot_id: P35499
---

# Human Naᵥ1.4 C-Terminal Domain in Complex with Calmodulin

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P35499">UniProt: P35499</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Voltage-gated sodium channels Naᵥ1.4 (skeletal muscle) and Naᵥ1.5 (cardiac) are regulated by [calmodulin (CaM)](/xray-mp-wiki/reagents/ligands/calmodulin/) in an isoform-specific manner. The crystal structures of the Naᵥ1.4 C-terminal domain (CTerm) in complex with apo CaM at 1.79 Å resolution (PDB 6MBA) and with (Ca²⁺)₄-CaM at 3.3 Å resolution (PDB 6MC9) reveal the structural basis for Ca²⁺-dependent inactivation (CDI) differences between isoforms. The Naᵥ1.5 CTerm contains a Ca²⁺-dependent N-lobe binding motif (NLBM) in the post-IQ region that prevents CDI, while Naᵥ1.4 lacks this motif, allowing the N-lobe to interact elsewhere in the channel and mediate CDI. Deletion of the post-IQ NLBM in Naᵥ1.5 unveils robust CDI.


## Publications

### doi/10.1038##s41467-019-09570-7

**Structures:**

<table class="wiki-table">
  <thead><tr>
    <th>PDB ID</th>
    <th>Resolution</th>
    <th>Space Group</th>
    <th>Construct</th>
    <th>Ligand/Co-factor</th>
  </tr></thead>
  <tbody>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6mba">6MBA</a></td>
      <td>1.79</td>
      <td>C 1 2 1</td>
      <td>Naᵥ1.4 CTerm Short (1599–1754) + apo CaM</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6mc9">6MC9</a></td>
      <td>3.3</td>
      <td>P 4₃ 2₁ 2</td>
      <td>Naᵥ1.4 CTerm Short (1599–1754) + (Ca²⁺)₄-CaM</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-CodonPlus RIL
- **Construct**: H. sapiens Naᵥ1.4 CTerm Long (residues 1599–1764) and Short (residues 1599–1754) with N-terminal GST tag; R. norvegicus CaM (CALM2)

**Purification:**

<table class="wiki-table">
  <thead><tr>
    <th>Step</th>
    <th>Method</th>
    <th>Resin / Column</th>
    <th>Buffer + Detergent</th>
    <th>Notes</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>Affinity chromatography</td>
      <td>Glutathione Sepharose 4 Fast Flow</td>
      <td>—</td>
      <td>PBS</td>
      <td>Co-expressed Naᵥ1.4 CTerm–GST and CaM complex purified together</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>PreScission protease</td>
      <td>—</td>
      <td>20 mM Tris, 50 mM NaCl, 1 mM DTT, pH 7.4</td>
      <td>Dialysis overnight at 4 °C</td>
    </tr>
    <tr>
      <td>Ion exchange chromatography</td>
      <td>Source Q anion exchange</td>
      <td>—</td>
      <td>20 mM Tris, 1 mM DTT, 50–500 mM NaCl gradient</td>
      <td></td>
    </tr>
  </tbody>
</table>


## Biological / Functional Insights

### Isoform-specific Ca²⁺-dependent inactivation

Naᵥ1.4 exhibits robust CDI while Naᵥ1.5 does not. The difference is controlled by the post-IQ motif: Naᵥ1.5 contains a Ca²⁺-dependent N-lobe binding motif (NLBM) that sequesters the CaM N-lobe, preventing CDI. Naᵥ1.4 lacks this motif, allowing the CaM N-lobe to interact with other channel regions to mediate CDI.

### CaM C-lobe anchoring

The CaM C-lobe remains bound to the IQ motif of Naᵥ helix αVI in both apo and Ca²⁺-saturated states, maintaining a semi-open configuration. This anchoring allows the N-lobe to switch binding targets depending on Ca²⁺ concentration.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/sodium-channel-gating/">Sodium Channel Gating</a> — CaM regulates Naᵥ channel gating via Ca²⁺-dependent inactivation
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/sodium-channel-inactivation-gating/">Sodium Channel Inactivation</a> — CDI is controlled by the post-IQ motif and N-lobe binding
- <a href="/xray-mp-wiki/concepts/signaling-receptors/sodium-allosteric-modulation/">Sodium Allosteric Modulation</a> — Ca²⁺-CaM binding allosterically modulates Naᵥ channel activity
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Buffer component in purification
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Reducing agent in purification buffers
- <a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion Exchange Chromatography</a> — Source Q anion exchange used for final purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Used for structure determination of both Naᵥ1.4 CTerm complexes
