---
title: "E. coli Methionine ABC Transporter MetNI"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1157987]
verified: false
---

# E. coli Methionine ABC Transporter MetNI

## Overview

The MetNI complex is the high-affinity methionine ABC transporter from *Escherichia coli*, consisting of the transmembrane domain MetI and the nucleotide-binding domain MetN. The structure reveals an inward-facing, ATPase-inactive conformation and provides the first crystallographic analysis of a member of the methionine uptake transporter family. MetI contains an odd number of five transmembrane helices per subunit (with N and C termini on opposite sides of the membrane), in contrast to other structurally characterized ABC transporters. MetN features a C-terminal C2 (ACT) domain that mediates allosteric regulation through methionine binding, providing a molecular mechanism for transinhibition of methionine transport.


## Publications

### doi/10.1126##science.1157987

**Expression:**

- **Expression system**: E. coli
- **Notes**: Detergent-solubilized transporter

**Purification:**

- **Expression system**: E. coli

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
      <td>Solubilization and purification</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td></td>
      <td>MetNI complex purified in detergent-solubilized form</td>
    </tr>
  </tbody>
</table>
**Final sample**: Detergent-solubilized MetNI transporter

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Soaking</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals soaked in 1 mM L-<a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> for 2 hours; diffraction data collected to 5.2 Å resolution at the selenium edge</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Minimal Core of Five Transmembrane Helices

Each MetI subunit is organized around a core of five transmembrane helices that correspond to a subset of helices in larger ABC transporter membrane-spanning subunits (ModB, [MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malF/), [MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)](/xray-mp-wiki/proteins/abc-transporters/malG/)). The region of highest sequence and structural similarity includes the coupling helix and two surrounding transmembrane helices (TM3 and TM4), which form the core of the translocation pathway.

### Asymmetric Inward-Facing Conformation

The MetNI transporter crystallizes in an inward-facing, ATPase-inactive conformation with NBDs separated by 26-30 Å (compared to 11-16 Å in active ABC transporters). The NBDs and C2 domains are related by twofold axes that differ in orientation by ~20°, creating pronounced asymmetry accommodated by different linker conformations.

### Allosteric Regulation by Transinhibition

Methionine binds to the C2 (ACT) domain dimer interface near residues Met301 and Met312, stabilizing the inward-facing, ATPase-inactive conformation. [L-Methionine](/xray-mp-wiki/reagents/ligands/l-methionine/) inhibits ATPase activity with half-maximal inhibition at ~30 µM; L-[Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) is more potent (~10 µM). [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) of the C2 domain eliminates methionine inhibition. This provides a molecular mechanism for Kadner's observation that increasing internal methionine inhibits transport.


## Cross-References

- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/proteins/abc-transporters/malF/">MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/abc-transporters/malG/">MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/ligands/l-methionine/">L-Methionine</a> — Related ligand or cofactor
