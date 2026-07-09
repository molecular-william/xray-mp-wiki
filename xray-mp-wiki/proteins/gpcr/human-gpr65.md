---
title: "Human GPR65 Proton-Sensing Receptor (TDAG8)"
created: 2026-06-26
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [receptor, gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2020.01.008]
verified: regex
---

# Human GPR65 Proton-Sensing Receptor (TDAG8)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


## Overview

GPR65 (also known as TDAG8) is a proton-sensing G protein-coupled receptor predominantly expressed in immune cells. It responds to extracellular acidosis by activating the Gs signaling pathway, leading to cAMP accumulation. GPR65 plays important roles in inflammatory diseases, asthma, and cancer immunity. The receptor contains conserved histidine residues in its extracellular loops that function as pH sensors.

## Publications

### doi/10.1016##j.cell.2020.01.008

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7tup">7TUP</a></td>
      <td>3.1 A</td>
      <td>P212121</td>
      <td>Human GPR65 with N-terminal BRIL fusion and thermostabilizing mutations</td>
      <td>Not specified (ligand-free active-state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Construct**: Full-length human GPR65 with N-terminal [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion, C-terminal [6xHis](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag, expressed using [baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) system

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
      <td>Osmotic shock and Dounce homogenization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 2 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a> + --</td>
      <td>Sf9 cell pellets lysed by osmotic shock, membranes isolated by ultracentrifugation at 100,000g</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Solubilized for 2 h at 4 C, clarified by centrifugation</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (wash), 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (elution)</td>
      <td>Eluted in buffer containing 200 mM imidazole</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Monomeric peak fractions concentrated to 25 mg/mL</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GPR65-BRIL fusion at 25 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
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
      <td><a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene glycol</a> 25% v/v</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals harvested and flash-frozen. Data collected at SSRL beamline 12-2. Phased by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using BRIL as search model. Diffraction to 3.1 Angstrom resolution.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### pH-dependent Gs activation

GPR65 activates Gs signaling in response to acidic pH, with maximal activation at pH 6.0-6.5. Histidine residues in extracellular loops act as proton sensors that trigger receptor activation.


## Cross-References

- <a href="/xray-mp-wiki/proteins/human-gpr4/">Human GPR4</a> — Related proton-sensing GPCR with similar structure and mechanism
- <a href="/xray-mp-wiki/proteins/human-gpr68/">Human GPR68 (OGR1)</a> — Related proton-sensing GPCR in the same receptor family
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> — Primary detergent used in purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Stabilizing additive used in purification buffers
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> — Fusion protein used for crystallization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — Crystallization method used for structure determination
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> — Affinity resin for His-tag purification
