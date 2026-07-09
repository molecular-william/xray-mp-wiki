---
title: "Human GPR132 (G2A) Receptor"
created: 2026-06-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [receptor, gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2020.01.008]
verified: regex
uniprot_id: O60885
---

# Human GPR132 (G2A) Receptor

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O60885">UniProt: O60885</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

GPR132 (also known as G2A) is a proton-sensing G protein-coupled receptor that responds to extracellular acidification. It is predominantly expressed in immune cells and plays roles in inflammation, immune regulation, and cancer biology. GPR132 activates multiple G protein signaling pathways including Gs and Gq in a pH-dependent manner. The receptor contains characteristic histidine residues in its extracellular domains that function as pH sensors.

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7tuq">7TUQ</a></td>
      <td>3.0 A</td>
      <td>P212121</td>
      <td>Human GPR132 with N-terminal BRIL fusion and thermostabilizing mutations</td>
      <td>Not specified (ligand-free active-state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Construct**: Full-length human GPR132 with N-terminal [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion, C-terminal [6xHis](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag, expressed using [baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) system

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
      <td>Sf9 cell pellets lysed, membranes isolated by ultracentrifugation</td>
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
      <td>Eluted with 200 mM imidazole</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Monomeric fractions pooled and concentrated to 20-25 mg/mL</td>
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
      <td>GPR132-BRIL fusion at 20-25 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-7 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td><a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene glycol</a> 25% v/v</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals flash-frozen in liquid nitrogen. Data collected at SSRL beamline 12-2. Phased by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using BRIL as search model. Diffraction to 3.0 Angstrom resolution.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### pH sensing in immune regulation

GPR132 acts as a proton sensor in immune cells, where acidic microenvironments at sites of inflammation trigger G protein signaling that modulates immune cell function.


## Cross-References

- <a href="/xray-mp-wiki/proteins/human-gpr4/">Human GPR4</a> — Related proton-sensing GPCR with similar structural mechanism
- <a href="/xray-mp-wiki/proteins/human-gpr65/">Human GPR65 (TDAG8)</a> — Related proton-sensing GPCR in the same receptor family
- <a href="/xray-mp-wiki/proteins/human-gpr68/">Human GPR68 (OGR1)</a> — Related proton-sensing GPCR in the same receptor family
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> — Primary detergent for membrane protein solubilization
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Stabilizing additive in purification buffers
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> — Fusion protein for crystallization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — Method used to grow diffraction-quality crystals
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> — Affinity resin for initial purification step
