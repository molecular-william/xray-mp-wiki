---
title: "Human GPR4 Proton-Sensing Receptor"
created: 2026-06-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [receptor, gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2020.01.008]
verified: regex
uniprot_id: P12277
---

# Human GPR4 Proton-Sensing Receptor

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P12277">UniProt: P12277</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

GPR4 is a proton-sensing G protein-coupled receptor (GPCR) that responds to extracellular acidification by activating Gs and Gq signaling pathways. It plays important roles in inflammatory responses, vascular biology, and tumor biology. The receptor contains multiple histidine residues that act as pH sensors, detecting proton concentrations in the physiological pH range of 6.0-7.5.

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7tun">7TUN</a></td>
      <td>2.9 A</td>
      <td>I222</td>
      <td>Human GPR4 with N-terminal BRIL fusion, thermostabilizing mutations, and T4 lysozyme insertion in ICL3</td>
      <td>Not specified (ligand-free active-state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Construct**: Full-length human GPR4 with N-terminal [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion, [T4 lysozyme](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) insertion in ICL3, and C-terminal [6xHis](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag, expressed using [baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) system

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
      <td>Sf9 cell pellets lysed by osmotic shock, membranes collected by centrifugation at 100,000g</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Solubilized for 2 h at 4 C, centrifuged at 100,000g for 30 min</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (wash), 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (elution)</td>
      <td>Protein eluted in buffer with 200 mM imidazole</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">FLAG affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/m2-anti-flag/">M2 Anti-FLAG</a> antibody resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> peptide elution</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Monomeric peak concentrated to 30 mg/mL for crystallization</td>
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
      <td>GPR4-BRIL fusion at 30 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
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
      <td>Crystals harvested and flash-frozen in liquid nitrogen. Data collected at beamline 12-2 at SSRL. Phased by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using BRIL search model. Diffraction to 2.9 Angstrom resolution.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Proton sensing by histidine residues

GPR4 contains multiple histidine residues that act as pH sensors, with protonation of specific histidines triggering conformational changes that activate G protein signaling.


## Cross-References

- <a href="/xray-mp-wiki/proteins/human-gpr65/">Human GPR65 (TDAG8)</a> — Related proton-sensing GPCR with similar pH-sensing mechanism
- <a href="/xray-mp-wiki/proteins/human-gpr68/">Human GPR68 (OGR1)</a> — Related proton-sensing GPCR in the same receptor family
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> — Primary detergent used in purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Stabilizing additive used with LMNG in purification
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> — Fusion protein used to facilitate crystallization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — Method used for crystallization
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> — Affinity resin for initial purification step
