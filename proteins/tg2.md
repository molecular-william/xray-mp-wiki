---
title: "Human Transglutaminase 2 (TG2)"
created: 2026-06-26
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.020128199]
verified: false
---

# Human Transglutaminase 2 (TG2)

## Overview

Transglutaminase 2 (TG2) is a multifunctional enzyme that catalyzes Ca2+-dependent crosslinking of proteins by forming isopeptide bonds between glutamine and lysine residues. TG2 is ubiquitously expressed and plays diverse roles in cell adhesion, apoptosis, extracellular matrix organization, and signal transduction. It has been implicated in various diseases including Celiac disease, neurodegenerative disorders, and cancer. TG2 undergoes large conformational changes between a closed (inactive) and open (active) state regulated by calcium and GTP binding.

## Publications

### doi/10.1073##pnas.020128199

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1kv3">1KV3</a></td>
      <td>2.8 A</td>
      <td>P212121</td>
      <td>Full-length human transglutaminase 2 (residues 1-687)</td>
      <td>GTP (bound in the GTP-binding pocket, inactive conformation)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2q3z">2Q3Z</a></td>
      <td>2.0 A</td>
      <td>P212121</td>
      <td>Full-length human transglutaminase 2 (active conformation)</td>
      <td>Calcium (activating ion)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length human TG2 (residues 1-687) with [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) [6xHis](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag

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
      <td>Cell lysis</td>
      <td>French press</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.5, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> + --</td>
      <td>Lysate clarified by centrifugation at 30,000g for 30 min</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> agarose resin</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.5, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (wash), 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (elution) + --</td>
      <td>His-tagged TG2 eluted and dialyzed against low-imidazole buffer</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion exchange chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion exchange chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/q-sepharose/">Q-Sepharose</a> column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.5, 50 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, eluted with gradient to 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + --</td>
      <td>Peak fractions analyzed by <a href="/xray-mp-wiki/methods/quality-assessment/sds-page/">SDS-PAGE</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> + --</td>
      <td>Monomeric TG2 concentrated to 10-15 mg/mL</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-drop</a> <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>TG2 at 10-15 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 1.5 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">ammonium sulfate</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>5-10 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> 25% v/v in reservoir solution</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown by streak seeding. Phased by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using the erythrocyte transglutaminase (band 4.2) as search model. GTP-bound (inactive) and Ca2+-bound (active) conformations both solved.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### GTP-dependent conformational regulation

TG2 adopts a compact closed conformation when bound to GTP, which inhibits its transamidase activity. Calcium binding induces a large conformational change to an open active state, exposing the catalytic core.


## Cross-References

- <a href="/xray-mp-wiki/concepts/structural-mechanisms/enzyme-regulation/">Enzyme Regulation</a> — TG2 activity is regulated by calcium and GTP binding
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> — Affinity resin for His-tag purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography (SEC)</a> — Final purification step
- <a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion Exchange Chromatography</a> — Intermediate purification step using Q-Sepharose
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Reducing agent used in purification and crystallization buffers
