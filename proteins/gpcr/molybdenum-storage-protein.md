---
title: "Molybdenum Storage Protein (MOSTO)"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-017-00630-4]
verified: false
---

# Molybdenum Storage Protein (MOSTO)

## Overview

Molybdenum storage protein (MOSTO) is a heterohexameric (αβ)₃ cage-like protein complex from Azotobacter vinelandii that stores molybdenum in the form of polyoxomolybdate clusters bound inside the cage. It is highly sensitive to X-ray radiation damage under conventional cryo-crystallographic conditions, making it an ideal test case for serial millisecond crystallography (SMX) at room temperature. The SMX structure was determined at 1.3 Å resolution using data collected in a single 6-hour synchrotron shift, demonstrating that SMX effectively mitigates radiation damage in metalloproteins.


## Publications

### doi/10.1038##s41467-017-00630-4

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5njm">5NJM</a></td>
      <td>1.3</td>
      <td>Not specified</td>
      <td>Heterologously produced in E. coli BL21 (DE3) with molecular chaperones, purified via Strep-tag affinity chromatography, ion exchange, and size exclusion chromatography. Crystallized from 0.1 M sodium citrate pH 5.6, 1.4 M NH₄H₂PO₄, 20% glycerol.</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/polyoxomolybdate/">Polyoxomolybdate Cluster</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21 (DE3)
- **Construct**: Full-length MOSTO with molecular chaperone coexpression; Strep-tag for affinity purification
- **Notes**: Protein purified via Strep-tag affinity, ion exchange (IEX), and size exclusion chromatography (SEC). Buffer: 50 mM MOPS, 50 mM NaCl pH 6.5.
- **Induction**: Not specified
- **Media**: Not specified

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
      <td>Strep-tag affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>StrepTactin</td>
      <td>50 mM MOPS, 50 mM NaCl pH 6.5 + None</td>
      <td>First capture step</td>
    </tr>
    <tr>
      <td>Ion exchange chromatography</td>
      <td>Ion exchange chromatography</td>
      <td>Not specified</td>
      <td>50 mM MOPS, 50 mM NaCl pH 6.5</td>
      <td>Intermediate purification step</td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a></td>
      <td>Not specified</td>
      <td>50 mM MOPS, 50 mM NaCl pH 6.5</td>
      <td>Final polishing step. Prior to crystallization, 1 mM ATP, 1 mM MgSO₄, and 1 mM Na₂MoO₄ were added.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified MOSTO at 25 mg/mL with 1 mM ATP, 1 mM MgSO₄, 1 mM Na₂MoO₄</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M sodium citrate pH 5.6, 1.4 M NH₄H₂PO₄, 20% glycerol</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18 °C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallization conditions were modified to produce sub-50 µm crystals suitable for SMX: 1.1–1.7 M NH₄H₂PO₄ gradient screen. Optimal: 1.4 M NH₄H₂PO₄. Drops: 2+2 µL. Crystals harvested by pooling hanging drops and mixing with ~70% monoolein through a 400 µm LCP coupler.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### SMX overcomes radiation damage in metalloprotein crystallography

MOSTO is highly radiation-sensitive due to its polyoxomolybdate clusters. Conventional cryo-crystallography causes severe radiation damage before complete data can be collected. SMX distributes the dose over approximately 240,000 crystals, yielding a 1.3 Å room-temperature structure with minimal radiation damage. This demonstrates SMX as a general method for radiation-sensitive metalloproteins.


## Cross-References

- <a href="/xray-mp-wiki/concepts/methods-techniques/serial-millisecond-crystallography/">Serial Millisecond Crystallography (SMX)</a> — SMX was essential for the MOSTO structure determination, overcoming radiation damage in this metalloprotein.
