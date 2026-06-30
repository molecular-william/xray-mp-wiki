---
title: "Coccomyxa subellipsoidea Rhodopsin (CsR)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1126##scisignal.aav4203]
verified: false
---

# Coccomyxa subellipsoidea Rhodopsin (CsR)

## Overview

Coccomyxa subellipsoidea rhodopsin (CsR) is a light-driven proton pump from the polar freshwater alga C. subellipsoidea (Trebouxiophyceae). The crystal structure of wild-type CsR (CsR-WT) was determined at 2.0-Å resolution, revealing seven transmembrane helices (TM1-TM7) with an all-trans-retinal chromophore covalently bound to Lys215 via a protonated Schiff base. A specific hydrogen bond between the highly conserved Arg83 and a nonconserved Tyr14 guided the structure-based transformation of CsR into an operational light-gated proton channel (CySeR, Y14E mutant) designed for potential optogenetic applications. CsR exhibits a BR-like pentameric counterion complex involving Asp86, Asp211, and three well-ordered water molecules, with a proton release complex including Glu193 and Glu203.


## Publications

### doi/10.1126##scisignal.aav4203

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6gyh">6GYH</a></td>
      <td>2.0</td>
      <td>H3</td>
      <td>Wild-type CsR (residues 2-226) from Coccomyxa subellipsoidea expressed in Pichia pastoris, with C-terminal 8xHis tag
</td>
      <td>all-trans-retinal (covalently bound via Schiff base to Lys215)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: CsR gene (residues 2-226) with C-terminal 8xHis tag, codon-optimized for P. pastoris expression

- **Notes**: Expressed in P. pastoris under control of AOX1 promoter. Cells disrupted by bead milling, membranes collected by ultracentrifugation, solubilized in 1% n-dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)).


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
      <td>Bead milling and ultracentrifugation</td>
      <td>—</td>
      <td>Lysis buffer (not specified in paper)</td>
      <td>P. pastoris cells disrupted by bead milling, membranes collected by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>Buffer containing 150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.0 + 1% n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membranes solubilized at 4°C for 1 h with rotation</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Ni-NTA agarose</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.0, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>C-terminal 8xHis tag used for purification</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>HiLoad 16/600 Superdex 200 pg</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.0, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purified CsR concentrated to 35 mg/ml for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>35 mg/ml CsR in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.0, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>
</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>10-14 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals picked from mesophase and flash-frozen in liquid nitrogen without additional cryoprotectant
</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>CsR mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> containing 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> in 1:1 (w/w) ratio. Rhombohedral crystals (space group H3) with one monomer per asymmetric unit. >100 crystals screened at ESRF (ID23-2) and BESSY II. Cell dimensions: a=b=78.08, c=143.97 A.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6gyh">6GYH</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AVHQIGEGG</span><span class="topo-membrane">LVMYWVTFGLMAFSALAFAVMTF</span><span class="topo-outside">TRPLNKRSH</span><span class="topo-membrane">GYITLAIVTIAAIAYYAMAAS</span><span class="topo-inside">GGKALVSNPDGNLRDI</span><span class="topo-membrane">YYARYIDWFFTTPLLLLDII</span><span class="topo-outside">LLTGIPIGV</span><span class="topo-membrane">TLWIVLADVAMI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230      </span>
<span class="topo-line"><span class="topo-membrane">MLGLFGALS</span><span class="topo-inside">TNSY</span><span class="topo-membrane">RWGYYGVSCAFFFVVLWGLFF</span><span class="topo-outside">PGAKGARARGGQVPGLY</span><span class="topo-membrane">FGLAGYLALLWFGYPIVWGLAEG</span><span class="topo-inside">SDYISVTA</span><span class="topo-membrane">EAASYAGLDIAAKVVFGWAVML</span><span class="topo-outside">SH</span><span class="topo-unknown">PLIAHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>33</td>
      <td>11</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>42</td>
      <td>34</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>63</td>
      <td>43</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>79</td>
      <td>64</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>99</td>
      <td>80</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>108</td>
      <td>100</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>129</td>
      <td>109</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>133</td>
      <td>130</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>171</td>
      <td>155</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>194</td>
      <td>172</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>202</td>
      <td>195</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>224</td>
      <td>203</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>226</td>
      <td>225</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6gyh">6GYH</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AVHQIGEGG</span><span class="topo-membrane">LVMYWVTFGLMAFSALAFAVMTF</span><span class="topo-outside">TRPLNKRSH</span><span class="topo-membrane">GYITLAIVTIAAIAYYAMAAS</span><span class="topo-inside">GGKALVSNPDGNLRDI</span><span class="topo-membrane">YYARYIDWFFTTPLLLLDII</span><span class="topo-outside">LLTGIPIGV</span><span class="topo-membrane">TLWIVLADVAMI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230      </span>
<span class="topo-line"><span class="topo-membrane">MLGLFGALS</span><span class="topo-inside">TNSY</span><span class="topo-membrane">RWGYYGVSCAFFFVVLWGLFF</span><span class="topo-outside">PGAKGARARGGQVPGLY</span><span class="topo-membrane">FGLAGYLALLWFGYPIVWGLAEG</span><span class="topo-inside">SDYISVTA</span><span class="topo-membrane">EAASYAGLDIAAKVVFGWAVML</span><span class="topo-outside">SH</span><span class="topo-unknown">PLIAHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>33</td>
      <td>11</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>42</td>
      <td>34</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>63</td>
      <td>43</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>79</td>
      <td>64</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>99</td>
      <td>80</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>108</td>
      <td>100</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>129</td>
      <td>109</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>133</td>
      <td>130</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>171</td>
      <td>155</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>194</td>
      <td>172</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>202</td>
      <td>195</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>224</td>
      <td>203</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>226</td>
      <td>225</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6gyh">6GYH</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AVHQIGEGG</span><span class="topo-membrane">LVMYWVTFGLMAFSALAFAVMTF</span><span class="topo-outside">TRPLNKRSH</span><span class="topo-membrane">GYITLAIVTIAAIAYYAMAAS</span><span class="topo-inside">GGKALVSNPDGNLRDI</span><span class="topo-membrane">YYARYIDWFFTTPLLLLDII</span><span class="topo-outside">LLTGIPIGV</span><span class="topo-membrane">TLWIVLADVAMI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230      </span>
<span class="topo-line"><span class="topo-membrane">MLGLFGALS</span><span class="topo-inside">TNSY</span><span class="topo-membrane">RWGYYGVSCAFFFVVLWGLFF</span><span class="topo-outside">PGAKGARARGGQVPGLY</span><span class="topo-membrane">FGLAGYLALLWFGYPIVWGLAEG</span><span class="topo-inside">SDYISVTA</span><span class="topo-membrane">EAASYAGLDIAAKVVFGWAVML</span><span class="topo-outside">SH</span><span class="topo-unknown">PLIAHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>33</td>
      <td>11</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>42</td>
      <td>34</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>63</td>
      <td>43</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>79</td>
      <td>64</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>99</td>
      <td>80</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>108</td>
      <td>100</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>129</td>
      <td>109</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>133</td>
      <td>130</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>171</td>
      <td>155</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>194</td>
      <td>172</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>202</td>
      <td>195</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>224</td>
      <td>203</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>226</td>
      <td>225</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Proton pump architecture and extracellular half-channel

CsR shares the canonical seven-transmembrane fold of microbial rhodopsins. The extracellular half-channel features a BR-like pentameric counterion complex (Asp86, Asp211, three water molecules) and a hydrogen-bond network connecting the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base to the extracellular side via Arg83 and six water molecules. A unique feature is the hydrogen bond between Arg83 and Tyr14 (TM1), stabilized by a hydrophobic cage formed by Tyr57, Met60, Ala204, Tyr80, and Ile6.

### Conversion of pump to light-gated proton channel (CySeR)

Substitution of Tyr14 with glutamate (Y14E) transformed CsR from a unidirectional proton pump into a light-gated proton channel (CySeR). The Glu14-Arg83 interaction reshapes the extracellular half-channel, creating a more open configuration that permits passive proton conductance. CySeR shows symmetric photocurrents at neutral pH, with residual pump activity under acidic conditions due to pH-dependent protonation of Glu14.

### Distinguishing pump vs channel currents

Time-resolved electrophysiological and spectroscopic measurements showed that pump and channel currents can coexist in a single protein. Arg83 mobility is essential as a dynamic extracellular barrier to prevent passive conductance. The findings demonstrate that molecular constraints distinguishing active and passive ion transport are structurally more confined than previously expected, located in the extracellular half-channel near the Arg83-Tyr14 interaction.

### Photocycle kinetics

CsR-WT exhibits a BR-like photocycle with K, M, and O intermediates. Deprotonation of the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base occurs within ~1.8 microseconds. CySeR retains similar early photocycle kinetics at neutral pH but shows impaired K-to-M transition at pH 9.0. Late photocycle steps coincide with passive conductance, suggesting structural rearrangements open a transient water channel on the cytoplasmic side.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/acetabularia-rhodopsin-ii/">Acetabularia Rhodopsin II</a> — ARII used as molecular replacement search model (PDB 3AM6)
- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — Reference proton pump for structural and mechanistic comparison
- <a href="/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-3/">Archaerhodopsin-3</a> — Compared pump-channel dichotomy with CsR findings
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/">Rhodopsin Photocycle</a> — CsR follows BR-type photocycle with K, M, O intermediates
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — CsR crystallized in monoolein LCP with cholesterol
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Matrix lipid for LCP crystallization of CsR
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for CsR solubilization and purification
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> — Chromophore covalently bound to Lys215 via Schiff base
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/proton-release-complex/">Proton Release Complex</a> — CsR features Glu193-Glu203 proton release complex
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channel-gating/">Channel Gating</a> — CySeR engineering demonstrates pump-channel conversion mechanism
