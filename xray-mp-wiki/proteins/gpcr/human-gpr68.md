---
title: "Human GPR68 Proton-Sensing Receptor (OGR1)"
created: 2026-06-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [receptor, gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2020.01.008]
verified: agent
uniprot_id: Q96RU2
---

# Human GPR68 Proton-Sensing Receptor (OGR1)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q96RU2">UniProt: Q96RU2</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

GPR68 (also known as OGR1, Ovarian Cancer G Protein-coupled Receptor 1) is a proton-sensing GPCR that responds to extracellular acidification by activating Gq and Gs signaling pathways. It is widely expressed in various tissues including bone, kidney, and the nervous system. GPR68 plays critical roles in physiological processes such as bone remodeling, pH homeostasis, and inflammation. The receptor contains multiple histidine residues that serve as pH sensors.

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6kpc">6KPC</a></td>
      <td>2.8 A</td>
      <td>P212121</td>
      <td>Human GPR68 with N-terminal BRIL fusion and thermostabilizing mutations</td>
      <td>Not specified (ligand-free active-state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Construct**: Full-length human GPR68 with N-terminal [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion, C-terminal [6xHis](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag, expressed using [baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) system

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
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Solubilized for 2 h at 4 C, cleared by ultracentrifugation</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (wash), 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (elution)</td>
      <td>Eluted with 200 mM imidazole</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Monomeric fractions pooled and concentrated to 30-40 mg/mL</td>
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
      <td>GPR68-BRIL fusion at 30-40 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
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
      <td>Crystals harvested and flash-frozen. Data collected at SSRL beamline 12-2. Phased by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using BRIL search model. Diffraction to 2.8 Angstrom resolution.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Proton-sensing mechanism via histidine protonation

GPR68 contains multiple histidine residues in extracellular loop 2 (ECL2) that become protonated at acidic pH, triggering conformational changes that activate Gq-mediated signaling.


## Cross-References

- <a href="/xray-mp-wiki/proteins/human-gpr4/">Human GPR4</a> — Related proton-sensing GPCR with similar structure
- <a href="/xray-mp-wiki/proteins/human-gpr65/">Human GPR65 (TDAG8)</a> — Related proton-sensing GPCR in the same receptor family
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> — Primary detergent used in purification and crystallization
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Stabilizing additive used in all purification buffers
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> — Fusion protein used to facilitate crystallization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — Method used to grow crystals for X-ray diffraction
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> — Affinity resin for His-tag purification step
