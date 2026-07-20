---
title: "Aquaporin-2 (AQP2)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41598-023-41616-1, doi/10.1073##pnas.1321406111]
verified: agent
uniprot_id: P41181
---

# Aquaporin-2 (AQP2)

<div class="expr-badges"><span class="expr-badge expr-p-pastoris">P. pastoris</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P41181">UniProt: P41181</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Aquaporin-2 (AQP2) is a water-selective channel expressed in the kidney
collecting duct principal cells, where it plays a critical role in urine
concentration and body water homeostasis. AQP2 functions as a homo-tetramer,
with each monomer containing six transmembrane helices and two membrane-inserted
non-membrane-spanning helices that form the water pore. The water permeability
of AQP2 is regulated by arginine vasopressin (AVP)-dependent trafficking
between subapical storage vesicles and the apical plasma membrane.
Phosphorylation of Ser-256, Ser-264, and Thr-269 in the C-terminus promotes
apical membrane accumulation, while dephosphorylation of Ser-261 and
ubiquitination stimulate endocytosis. Mutations in the AQP2 gene cause
nephrogenic diabetes insipidus (NDI), with recessive mutants typically
retained in the endoplasmic reticulum due to misfolding.

The 2.75 Å X-ray structure of wild-type human AQP2 (C-terminally truncated at
Pro242) reveals the conserved [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) fold with the C terminus displaying
multiple conformations. Two Cd²⁺-binding sites are observed, with Ca²⁺
proposed as the physiological ligand. The structure provides insights into
NDI-causing mutations and [AQP2](/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-2/) trafficking interactions including LIP5 binding.

## Publications

### doi/10.1038##s41598-023-41616-1

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8ghj">8GHJ</a></td>
      <td>3.90</td>
      <td>P4_2</td>
      <td>Human AQP2 T125M mutant, N-terminal 8xHis-tag, TEV-cleavable, C-terminally truncated at residue 242</td>
      <td>Cd2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8oee">8OEE</a></td>
      <td>3.15</td>
      <td>P4_2</td>
      <td>Human AQP2 T126M mutant, N-terminal 8xHis-tag, TEV-cleavable, C-terminally truncated at residue 242</td>
      <td>Cd2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris X33 strain
- **Construct**: Human AQP2 (residues 1–242 with N-terminal 8xHis-tag and TEV-protease cleavage site, truncated at P242 for crystallization

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
      <td>Membrane preparation</td>
      <td>Cell lysis and <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a></td>
      <td>--</td>
      <td>20 mM Tris-HCl pH 8.0, 300 mM NaCl, 0.2% OGNG + n-Octyl-β-D-glucopyranoside (OGNG)</td>
      <td>Cells lysed, membranes harvested by centrifugation, solubilized in 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 0.2% OGNG</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Immobilized metal affinity chromatography</a> (<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a></td>
      <td>HisTrap HP column, stepwise <a href="/xray-mp-wiki/reagents/buffers/imidazole/">imidazole</a> elution</td>
      <td>HisTrap HP (<a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td>20 mM Tris-HCl Propane-HCl pH 8.0, 300 mM NaCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a> + OGNG</td>
      <td>Wash with 10 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">imidazole</a> (2 CV, then 75 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">imidazole</a> (5 CV, elution with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Desalting</td>
      <td>Sephadex G-25 PD-10 column</td>
      <td>Sephadex G-25</td>
      <td>20 mM Tris-HCl Propane-HCl pH 8.0, 300 mM NaCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a> + OGNG</td>
      <td>Concentrated to 2.5 ml before desalting</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV protease</a> cleavage</td>
      <td>His-tagged <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV protease</a>, overnight at 4 °C</td>
      <td>--</td>
      <td>0.5 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a>, 20 mM TrisPs Hclray-mp-wiki/reagents/buffers/tes/fer Trisfer Bis <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> Propane-HCl pH 9.5 + OGNG</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV protease</a> added at 2:1 ratio (</td>
    </tr>
    <tr>
      <td>Reverse <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a></td>
      <td>Second HisTrap HP column, flowthrough collection</td>
      <td>HisTrap HP</td>
      <td>20 mM Tris-HCl Propane-HCl pH 8.0, 300 mM NaCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + OGNG</td>
      <td>Cleaved</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase</td>
      <td>20 mM Tris-HCl Propane-HCl pH 8.0, 300 mM NaCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a> + OGNG</td>
      <td>Concentrated to <500 μl before</td>
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
      <td>AQP2 constructs at 10 mg/ml in 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 0.2% OGNG, 5% glycerol</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20–30% PEG400, 20 mM Tris-HCl pH 8.5, 0.1 M MgCl2, 0.1 M NaCl, 0.1 M CdCl2 (added 1:4 ratio)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 °C or room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2–3 days (crystals formed within 15 min at highest PEG concentrations)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals grown at <24% PEG400 soaked in reservoir + 30% PEG400; otherwise no additional cryoprotection</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>T125M best in 20% PEG400 at 6 °C, T126M best in 24% PEG400 at room temperature, A147T in 22% PEG400 at 6 °C.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8ghj">8GHJ</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-outside">SELRSIAFSRA</span><span class="topo-membrane">VFAEFLATLLFVFFGLGS</span><span class="topo-inside">ALNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHINPAVTVACLV</span><span class="topo-outside">GCHVSVLRA</span><span class="topo-membrane">AFYVAAQLLGAVAGAALL</span><span class="topo-inside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LSNSMTAGQA</span><span class="topo-membrane">VTVELFLTLQLVLCIFAS</span><span class="topo-outside">TDERRGENPG</span><span class="topo-membrane">TPALSIGFSVALGHLLG</span><span class="topo-inside">IHYTGC</span><span class="topo-unknown">SMNPARSLAP</span><span class="topo-inside">AVVTGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLY</span><span class="topo-outside">NYVLFPPAKSLSERLAVLK</span><span class="topo-unknown">GL</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>30</td>
      <td>13</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>42</td>
      <td>31</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>64</td>
      <td>61</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>77</td>
      <td>65</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>86</td>
      <td>78</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>130</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>131</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>158</td>
      <td>149</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>175</td>
      <td>159</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>181</td>
      <td>176</td>
      <td>181</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>191</td>
      <td>182</td>
      <td>191</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>201</td>
      <td>192</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>238</td>
      <td>220</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>239</td>
      <td>241</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8ghj">8GHJ</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSELR</span><span class="topo-outside">SIAFSRAV</span><span class="topo-membrane">FAEFLATLLFVFFGLGS</span><span class="topo-inside">ALNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHINPAVTVACL</span><span class="topo-outside">VGCHVSVLRA</span><span class="topo-membrane">AFYVAAQLLGAVAGAALL</span><span class="topo-inside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LSNSMTAG</span><span class="topo-membrane">QAVTVELFLTLQLVLCIFAS</span><span class="topo-outside">TDERRGENPGT</span><span class="topo-membrane">PALSIGFSVALGHLLGI</span><span class="topo-inside">HYTG</span><span class="topo-unknown">CSMNPARSLAPAVV</span><span class="topo-inside">TGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLY</span><span class="topo-outside">NYVLFPPAKSL</span><span class="topo-unknown">SERLAVLKGL</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>13</td>
      <td>6</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>30</td>
      <td>14</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>42</td>
      <td>31</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>64</td>
      <td>61</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>76</td>
      <td>65</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>77</td>
      <td>86</td>
      <td>77</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>128</td>
      <td>105</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>148</td>
      <td>129</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>159</td>
      <td>149</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>176</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>180</td>
      <td>177</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>194</td>
      <td>181</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>230</td>
      <td>220</td>
      <td>230</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>241</td>
      <td>231</td>
      <td>241</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8ghj">8GHJ</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSELR</span><span class="topo-outside">SIAFSRAV</span><span class="topo-membrane">FAEFLATLLFVFFGLGS</span><span class="topo-inside">ALNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHINPAVTVACL</span><span class="topo-outside">VGCHVSVLRA</span><span class="topo-membrane">AFYVAAQLLGAVAGAALL</span><span class="topo-inside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LSNSMTAGQA</span><span class="topo-membrane">VTVELFLTLQLVLCIFAS</span><span class="topo-outside">TDERRGENPGTP</span><span class="topo-membrane">ALSIGFSVALGHLLGI</span><span class="topo-inside">HYTG</span><span class="topo-unknown">CSMNPARSLAPAVV</span><span class="topo-inside">TGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLY</span><span class="topo-outside">NYVLFPPAKSLSERLAVLKGL</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-outside">E</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>13</td>
      <td>6</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>30</td>
      <td>14</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>42</td>
      <td>31</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>64</td>
      <td>61</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>76</td>
      <td>65</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>77</td>
      <td>86</td>
      <td>77</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>130</td>
      <td>105</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>131</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>160</td>
      <td>149</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>176</td>
      <td>161</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>180</td>
      <td>177</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>194</td>
      <td>181</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>241</td>
      <td>220</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8ghj">8GHJ</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-outside">SELRSIAFSRA</span><span class="topo-membrane">VFAEFLATLLFVFFGLGS</span><span class="topo-inside">ALNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALG</span><span class="topo-outside">HIS</span><span class="topo-unknown">GAHINPAVTVACLV</span><span class="topo-outside">GCHVSVLRA</span><span class="topo-membrane">AFYVAAQLLGAVAGAALL</span><span class="topo-inside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LSNSMTAG</span><span class="topo-membrane">QAVTVELFLTLQLVLCIFAS</span><span class="topo-outside">TDERRGENPGT</span><span class="topo-membrane">PALSIGFSVALGHLLGI</span><span class="topo-inside">HYTG</span><span class="topo-unknown">CSMNPARSLAP</span><span class="topo-inside">AVVTGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLY</span><span class="topo-outside">NYVLFPPAKSLSE</span><span class="topo-unknown">RLAVLKGL</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>30</td>
      <td>13</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>42</td>
      <td>31</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>63</td>
      <td>61</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>77</td>
      <td>64</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>86</td>
      <td>78</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>128</td>
      <td>105</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>148</td>
      <td>129</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>159</td>
      <td>149</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>176</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>180</td>
      <td>177</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>191</td>
      <td>181</td>
      <td>191</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>201</td>
      <td>192</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>232</td>
      <td>220</td>
      <td>232</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>241</td>
      <td>233</td>
      <td>241</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8oee">8OEE</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SELRSIAFS</span><span class="topo-membrane">RAVFAEFLATLLFVFFGLGSA</span><span class="topo-outside">LNWPQALPSV</span><span class="topo-membrane">LQIAMAFGLGIGTLVQALGHIS</span><span class="topo-unknown">GAHINPAVTVACLVG</span><span class="topo-inside">CHVSV</span><span class="topo-membrane">LRAAFYVAAQLLGAVAGAALLHEI</span><span class="topo-outside">TPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LSNSTMAG</span><span class="topo-membrane">QAVTVELFLTLQLVLCIFAST</span><span class="topo-inside">DERRGEN</span><span class="topo-membrane">PGTPALSIGFSVALGHLLGI</span><span class="topo-outside">HY</span><span class="topo-unknown">TGCSMNPARSLAPAVV</span><span class="topo-outside">TGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLYNYVL</span><span class="topo-inside">FPPAKSLSERLAVLKGL</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>10</td>
      <td>2</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>31</td>
      <td>11</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>41</td>
      <td>32</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>78</td>
      <td>65</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>83</td>
      <td>79</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>107</td>
      <td>84</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>128</td>
      <td>108</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>149</td>
      <td>129</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>156</td>
      <td>150</td>
      <td>156</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>176</td>
      <td>157</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>178</td>
      <td>177</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>194</td>
      <td>179</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>223</td>
      <td>202</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>240</td>
      <td>224</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8oee">8OEE</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSELR</span><span class="topo-inside">SIAFS</span><span class="topo-membrane">RAVFAEFLATLLFVFFGLGSA</span><span class="topo-outside">LNWPQALPSV</span><span class="topo-membrane">LQIAMAFGLGIGTLVQALG</span><span class="topo-inside">HI</span><span class="topo-unknown">SGAHINPAVTVACLVG</span><span class="topo-inside">CHVSV</span><span class="topo-membrane">LRAAFYVAAQLLGAVAGAALLHEI</span><span class="topo-outside">TPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LSNSTMA</span><span class="topo-membrane">GQAVTVELFLTLQLVLCIFAST</span><span class="topo-inside">DERRGENP</span><span class="topo-membrane">GTPALSIGFSVALGHLLGI</span><span class="topo-outside">HY</span><span class="topo-unknown">TGCSMNPARSLAPAVV</span><span class="topo-outside">TGKFDD</span><span class="topo-membrane">HWVFWIGPLVGAILGSLLYN</span><span class="topo-inside">YVLFPPAKSLSERLAVLK</span><span class="topo-unknown">GL</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>10</td>
      <td>6</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>31</td>
      <td>11</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>41</td>
      <td>32</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>60</td>
      <td>42</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>62</td>
      <td>61</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>78</td>
      <td>63</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>83</td>
      <td>79</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>107</td>
      <td>84</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>127</td>
      <td>108</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>149</td>
      <td>128</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>157</td>
      <td>150</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>176</td>
      <td>158</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>178</td>
      <td>177</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>194</td>
      <td>179</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>200</td>
      <td>195</td>
      <td>200</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>220</td>
      <td>201</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>239</td>
      <td>241</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8oee">8OEE</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSELR</span><span class="topo-inside">SIAFS</span><span class="topo-membrane">RAVFAEFLATLLFVFFGLGSA</span><span class="topo-outside">LNWPQALPSV</span><span class="topo-membrane">LQIAMAFGLGIGTLVQALG</span><span class="topo-inside">HI</span><span class="topo-unknown">SGAHINPAVTVACLV</span><span class="topo-inside">GCHVSV</span><span class="topo-membrane">LRAAFYVAAQLLGAVAGAALLHEI</span><span class="topo-outside">TPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LSNSTMA</span><span class="topo-membrane">GQAVTVELFLTLQLVLCIFAST</span><span class="topo-inside">DERRGENPGT</span><span class="topo-membrane">PALSIGFSVALGHLLGI</span><span class="topo-outside">HY</span><span class="topo-unknown">TGCSMNPARSLAPAVV</span><span class="topo-outside">TGKFDD</span><span class="topo-membrane">HWVFWIGPLVGAILGSLLYNYVL</span><span class="topo-inside">FPPAKSLSERLAVLKGL</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-inside">E</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>10</td>
      <td>6</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>31</td>
      <td>11</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>41</td>
      <td>32</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>60</td>
      <td>42</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>62</td>
      <td>61</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>77</td>
      <td>63</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>83</td>
      <td>78</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>107</td>
      <td>84</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>127</td>
      <td>108</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>149</td>
      <td>128</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>159</td>
      <td>150</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>176</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>178</td>
      <td>177</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>194</td>
      <td>179</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>200</td>
      <td>195</td>
      <td>200</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>223</td>
      <td>201</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>241</td>
      <td>224</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8oee">8OEE</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SELRSIAFS</span><span class="topo-membrane">RAVFAEFLATLLFVFFGLGSA</span><span class="topo-outside">LNWPQALPSV</span><span class="topo-membrane">LQIAMAFGLGIGTLVQALGHIS</span><span class="topo-unknown">GAHINPAVTVACLVG</span><span class="topo-inside">CHVSV</span><span class="topo-membrane">LRAAFYVAAQLLGAVAGAALLHEI</span><span class="topo-outside">TPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LSNSTMA</span><span class="topo-membrane">GQAVTVELFLTLQLVLCIFAST</span><span class="topo-inside">DERRGENPG</span><span class="topo-membrane">TPALSIGFSVALGHLLGI</span><span class="topo-outside">HY</span><span class="topo-unknown">TGCSMNPARSLAPAVV</span><span class="topo-outside">TGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLYNYVL</span><span class="topo-inside">FPPAKSLSER</span><span class="topo-unknown">LAVLKGL</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>10</td>
      <td>2</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>31</td>
      <td>11</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>41</td>
      <td>32</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>78</td>
      <td>65</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>83</td>
      <td>79</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>107</td>
      <td>84</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>127</td>
      <td>108</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>149</td>
      <td>128</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>158</td>
      <td>150</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>176</td>
      <td>159</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>178</td>
      <td>177</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>194</td>
      <td>179</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>223</td>
      <td>202</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>233</td>
      <td>224</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>241</td>
      <td>234</td>
      <td>241</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.1321406111

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4nef">4NEF</a></td>
      <td>2.75</td>
      <td>P4₂</td>
      <td>Wild-type human AQP2, C-terminally truncated at Pro242, expressed in Pichia pastoris</td>
      <td>Cd²⁺, Zn²⁺</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris X33 strain
- **Construct**: Human AQP2 (residues 1–242 with N-terminal 8xHis-tag and TEV-protease cleavage site, truncated at P242 for crystallization

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>C-terminally truncated AQP2 (residues 1-242) at Pro242</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>100 K (data collection)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Frozen crystal</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>CdCl₂ used as an additive during crystallization. Complete data collected at ESRF (Grenoble, France) from a single frozen crystal. Belonged to space group P4₂ with one tetramer in the asymmetric unit (a=119.11 Å, b=119.11 Å, c=90.48 Å).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nef">4NEF</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SELRSIAFSRA</span><span class="topo-membrane">VFAEFLATLLFVFFGLGS</span><span class="topo-outside">ALNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHINPAVTVACLV</span><span class="topo-inside">GCHVSVLRA</span><span class="topo-membrane">AFYVAAQLLGAVAGAALL</span><span class="topo-outside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LSNSTTAGQA</span><span class="topo-membrane">VTVELFLTLQLVLCIFAS</span><span class="topo-inside">TDERRGENPG</span><span class="topo-membrane">TPALSIGFSVALGHLLG</span><span class="topo-outside">IHYTGC</span><span class="topo-unknown">SMNPARSLAP</span><span class="topo-outside">AVVTGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLY</span><span class="topo-inside">NYVLFPPAKSLSERLAVLKGL</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EP</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>30</td>
      <td>13</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>42</td>
      <td>31</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>63</td>
      <td>61</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>77</td>
      <td>64</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>86</td>
      <td>78</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>130</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>131</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>158</td>
      <td>149</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>175</td>
      <td>159</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>181</td>
      <td>176</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>191</td>
      <td>182</td>
      <td>191</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>201</td>
      <td>192</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>240</td>
      <td>220</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>242</td>
      <td>241</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nef">4NEF</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSELR</span><span class="topo-inside">SIAFSRAV</span><span class="topo-membrane">FAEFLATLLFVFFGLGS</span><span class="topo-outside">ALNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALG</span><span class="topo-inside">HISG</span><span class="topo-unknown">AHINPAVTVACL</span><span class="topo-inside">VGCHVSVLRA</span><span class="topo-membrane">AFYVAAQLLGAVAGAALL</span><span class="topo-outside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LSNSTTAG</span><span class="topo-membrane">QAVTVELFLTLQLVLCIF</span><span class="topo-inside">ASTDERRGENPGT</span><span class="topo-membrane">PALSIGFSVALGHLLGI</span><span class="topo-outside">HYTGC</span><span class="topo-unknown">SMNPARSLAPAVV</span><span class="topo-outside">TGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLY</span><span class="topo-inside">NYVLFPPAKSLSERLAVLK</span><span class="topo-unknown">GL</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EP</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>13</td>
      <td>6</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>30</td>
      <td>14</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>42</td>
      <td>31</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>64</td>
      <td>61</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>76</td>
      <td>65</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>77</td>
      <td>86</td>
      <td>77</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>128</td>
      <td>105</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>146</td>
      <td>129</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>159</td>
      <td>147</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>176</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>181</td>
      <td>177</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>194</td>
      <td>182</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>238</td>
      <td>220</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>242</td>
      <td>239</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nef">4NEF</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSELR</span><span class="topo-inside">SIAFSRAV</span><span class="topo-membrane">FAEFLATLLFVFFGLGS</span><span class="topo-outside">ALNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALG</span><span class="topo-inside">HISG</span><span class="topo-unknown">AHINPAVTVACL</span><span class="topo-inside">VGCHVSVLRA</span><span class="topo-membrane">AFYVAAQLLGAVAGAALL</span><span class="topo-outside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LSNSTTAGQA</span><span class="topo-membrane">VTVELFLTLQLVLCIFAS</span><span class="topo-inside">TDERRGENPGTP</span><span class="topo-membrane">ALSIGFSVALGHLLGI</span><span class="topo-outside">HYTGC</span><span class="topo-unknown">SMNPARSLAPAVV</span><span class="topo-outside">TGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLY</span><span class="topo-inside">NYVLFPPAKSLSERLAVLKGL</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-inside">E</span><span class="topo-unknown">P</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>13</td>
      <td>6</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>30</td>
      <td>14</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>42</td>
      <td>31</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>64</td>
      <td>61</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>76</td>
      <td>65</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>77</td>
      <td>86</td>
      <td>77</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>130</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>131</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>160</td>
      <td>149</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>176</td>
      <td>161</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>181</td>
      <td>177</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>194</td>
      <td>182</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>241</td>
      <td>220</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>242</td>
      <td>242</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nef">4NEF</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SELRSIAFSRA</span><span class="topo-membrane">VFAEFLATLLFVFFGLGS</span><span class="topo-outside">ALNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHINPAVTVACLV</span><span class="topo-inside">GCHVSVLRA</span><span class="topo-membrane">AFYVAAQLLGAVAGAALL</span><span class="topo-outside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LSNSTTAGQA</span><span class="topo-membrane">VTVELFLTLQLVLCIFAS</span><span class="topo-inside">TDERRGENPGT</span><span class="topo-membrane">PALSIGFSVALGHLLG</span><span class="topo-outside">IHYTGC</span><span class="topo-unknown">SMNPARSLAP</span><span class="topo-outside">AVVTGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLY</span><span class="topo-inside">NYVLFPPAKSLSER</span><span class="topo-unknown">LAVLKGL</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EP</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>30</td>
      <td>13</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>42</td>
      <td>31</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>63</td>
      <td>61</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>77</td>
      <td>64</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>86</td>
      <td>78</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>130</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>131</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>159</td>
      <td>149</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>175</td>
      <td>160</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>181</td>
      <td>176</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>191</td>
      <td>182</td>
      <td>191</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>201</td>
      <td>192</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>233</td>
      <td>220</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>242</td>
      <td>234</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Minor misfolding recognized by ER quality control



### A147T destabilizes the AQP2 tetramer



### Therapeutic implications of functional NDI mutants



### C-terminal conformational variability

The C-terminal helix of AQP2 shows significant conformational variability across the four protomers of the tetramer. In protomer C, the C-terminal helix interacts with a symmetry-related AQP2 molecule via leucine residues (Leu230, 234, 237, 240), suggesting a role in protein-protein interactions relevant to AQP2 trafficking and LIP5 binding.

### Cd²⁺ and Ca²⁺ binding sites

Two Cd²⁺ binding sites (Cd1 and Cd2) identified per AQP2 tetramer. Cd1 is at the interface between protomers A and D, ligated by GluA155 and GlnD57. Cd2 is located between loop B and the C-terminal tail in protomer C. Radioactive Ca²⁺ assays demonstrate that AQP2-expressing oocytes bind significantly more Ca²⁺ than controls, suggesting Ca²⁺ is the physiological ligand for these sites.

### NDI-causing mutations in the wild-type structure

The wild-type AQP2 structure reveals locations of mutations causing NDI. Key sites include: Gln57 (Cd1 ligand), Ser148 (casein kinase II site), Thr125/Thr126 in loop C near the N-glycosylation site at Asn123, and Asp150 in loop D which mediates interactions with the C-terminal tail via Arg152. Most NDI-causing mutations are in transmembrane domains and cause misfolding and ER retention.


## Cross-References

- <a href="/xray-mp-wiki/proteins/other-ion-channels/human-aqp7/">Human Aquaporin 7 (AQP7)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/other-ion-channels/human-aqp5/">Human Aquaporin 5 (AQP5)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/abc-transporters/malG/">MalG (Escherichia coli Maltose Transporter Transmembrane Subunit)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/other-ion-channels/kpbest/">KpBest Bestrophin Ion Channel</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/abc-transporters/malF/">MalF (Escherichia coli Maltose Transporter Transmembrane Subunit)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-2/">Human Aquaporin 2 (AQP2)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/n-glycosylation-sequon/">N-Glycosylation Sequon</a> — Related concept; referenced in text
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin Family</a> — Related concept; referenced in text
- <a href="/xray-mp-wiki/concepts/protein-families/pq-loop-family/">PQ-Loop Family</a> — Related concept; referenced in text
- <a href="/xray-mp-wiki/concepts/methods-techniques/steered-molecular-dynamics/">Steered Molecular Dynamics (SMD)</a> — Related concept; referenced in text
