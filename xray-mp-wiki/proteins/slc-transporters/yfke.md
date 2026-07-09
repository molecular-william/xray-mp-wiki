---
title: "YfkE Ca2+/H+ Antiporter from Bacillus subtilis"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1073##pnas.1302515110]
verified: regex
---

# YfkE Ca2+/H+ Antiporter from Bacillus subtilis

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

YfkE is a Ca2+/H+ antiporter from *Bacillus subtilis* belonging to the [Ca2+:Cation Antiporter (CaCA) Superfamily](/xray-mp-wiki/concepts/transport-mechanisms/caca-superfamily/). The structure was determined by X-ray crystallography at 3.1-Å resolution, revealing a homotrimeric assembly with an inward-facing conformation. Each protomer contains 11 transmembrane helices (TMs 0-10) arranged in two antiparallel helical bundles with a pseudo twofold symmetry. The structure provides insights into the Ca2+/H+ exchange mechanism and pH regulation of CAX family proteins.


## Publications

### doi/10.1073##pnas.1302515110

**Expression:**

- **Expression system**: E. coli
- **Construct**: Polyhistidine tag inserted within the cytoplasmic loop between TMs 5 and 6; K116A and L77M mutations

**Purification:**

- **Expression system**: E. coli
- **Tag info**: Polyhistidine tag

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
      <td>Solubilization and extraction</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>n-dodecyl-beta-D-maltoside</td>
      <td></td>
    </tr>
    <tr>
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA</td>
      <td>n-dodecyl-beta-D-maltoside</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (hanging drop)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained at pH 4 for both native and Se-Met proteins</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Inward-Facing Conformation and pH Regulation

The YfkE structure captured in a protonated state at pH 4 reveals an inward-facing conformation with a large hydrophilic cavity opening to the cytoplasm. A hydrophobic seal closes the periplasmic exit. This acid-locked conformation suggests that H+ influx resets the protein to a state ready for cytoplasmic Ca2+ access, providing a mechanism for pH-dependent regulation of Ca2+/H+ exchange.

### Ca2+/H+ Exchange Mechanism and Alternating Access

Comparison of the inward-facing YfkE structure with the outward-facing NCX_Mj structure supports an [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) for CaCA proteins. Conformational transitions are triggered by rotation of kink angles in TMs 2 and 7, coupled with large movements in adjacent TMs 1 and 6. Two conserved glutamate residues (E72 and E255) play key roles in Ca2+ binding and H+ coupling.

### Evolutionary Adaptation of Energy Coupling

Sequence differences between YfkE and NCX_Mj reveal how Na+-binding sites in NCXs are replaced by amino acid substitutions in YfkE, creating a more compact Ca2+-binding site. These adaptations reflect evolutionary divergence between H+-driven CAX proteins and Na+-driven NCX/NCKX proteins within the CaCA superfamily.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/caca-superfamily/">Ca2+:Cation Antiporter (CaCA) Superfamily</a> — YfkE is a member of the CAX family within the CaCA superfamily
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — Structural comparison of inward-facing YfkE and outward-facing NCX_Mj demonstrates alternating access
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
