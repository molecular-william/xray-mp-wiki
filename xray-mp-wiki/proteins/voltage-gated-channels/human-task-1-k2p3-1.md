---
title: "Human TASK-1 (K2P 3.1) Potassium Channel"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-020-2250-8]
verified: agent
uniprot_id: O14649
---

# Human TASK-1 (K2P 3.1) Potassium Channel

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O14649">UniProt: O14649</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

TWIK-related acid-sensitive potassium (TASK) channels (K2P 3.1/KCNK3) are
members of the two-pore domain potassium (K2P) channel family, found in
neurons, cardiomyocytes, and vascular smooth muscle cells, where they regulate
the resting membrane potential and are involved in heart rate, pulmonary artery
tone, sleep/wake cycles, and responses to volatile anaesthetics. Unlike other
K2P channels, TASK channels bind inhibitors with high affinity, exceptional
selectivity, and very slow washout rates, making them attractive drug targets
for obstructive sleep apnoea and atrial fibrillation. The X-ray crystal
structure of human TASK-1 (construct Met1-Glu259) was determined at 3.0 A
resolution, revealing a domain-swapped homodimer with a pseudo-tetrameric
selectivity filter, four transmembrane helices (M1-M4), and an extracellular
cap. Notably, TASK-1 contains a novel lower gate termed the 'X-gate', formed by
the crossed C-terminal M4 transmembrane helices at the vestibule entrance. This
structure is created by six residues (243VLRFMT248) that are essential for
responses to volatile anaesthetics, neurotransmitters, and GPCRs. Structures
of TASK-1 bound to two high-affinity inhibitors (BAY1000493 and BAY2341237)
show both compounds bind below the selectivity filter and are trapped in the
vestibule by the X-gate, explaining their exceptionally low washout rates.

## Publications

### doi/10.1038##s41586-020-2250-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6rv2">6RV2</a></td>
      <td>3.0</td>
      <td>Not specified</td>
      <td>Human TASK-1 Met1-Glu259 (C-terminally truncated), C-terminal TEV cleavage site, decahistidine and Flag tags</td>
      <td>K+ ions at selectivity filter sites</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6rv3">6RV3</a></td>
      <td>3.0</td>
      <td>Not specified</td>
      <td>Human TASK-1 Met1-Glu259 plus BAY1000493 (inhibitor)</td>
      <td>BAY1000493 (4-[[2-(4-bromophenyl)imidazo[1,2-a]pyridin-3-yl]methyl]piperazin-1-yl)(2-fluorophenyl)methanone), K+ ions</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6rv4">6RV4</a></td>
      <td>3.0</td>
      <td>Not specified</td>
      <td>Human TASK-1 Met1-Glu259 plus BAY2341237 (inhibitor)</td>
      <td>BAY2341237 (4-[[2-(4-chlorophenyl)imidazo[1,2-a]pyridin-3-yl]methyl]piperazin-1-yl]6-(trifluoromethoxy)pyridin-2-yl]methanone), K+ ions</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) cells, Bac-to-Bac baculovirus system
- **Construct**: Human KCNK3 (GenBank ID 4504849), residues Met1-Glu259, subcloned in pFB-CT10HF-LIC with C-terminal TEV protease site, decahistidine and Flag tags

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
      <td>Emulsiflex-C3/C5 high-pressure homogenizer</td>
      <td>--</td>
      <td>50 mM HEPES pH 7.5, 200 mM KCl, 5% v/v <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + --</td>
      <td>40 ml breaking buffer per litre of culture</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM HEPES pH 7.5, 200 mM KCl, 5% v/v <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1% w/v <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (DM), 0.1% w/v <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a> salt</td>
      <td>Rotated at 4 C for 1 h</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin (0.5 ml resin per litre culture)</td>
      <td>Wash buffer (50 mM HEPES pH 7.5, 200 mM KCl, 5% v/v <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> pH 8.0, 0.24% w/v <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 0.024% w/v <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)); Elution buffer (same + 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>) + 0.24% w/v <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 0.024% w/v <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>30 column volumes wash; 5 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> added before loading</td>
    </tr>
    <tr>
      <td>Tag cleavage and deglycosylation</td>
      <td><a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease + PNGaseF digestion</td>
      <td>--</td>
      <td>Desalting buffer (50 mM HEPES pH 7.5, 200 mM KCl, 5% v/v <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.24% w/v <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 0.024% w/v <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)) + 0.24% w/v <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 0.024% w/v <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>1:3 w/w <a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease, 1:10 w/w PNGaseF, 12-16 h at 4 C</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>Superose 6 Increase 10/300 GL</td>
      <td>20 mM HEPES pH 7.5, 200 mM KCl, 0.12% w/v <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 0.012% w/v <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.12% w/v <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 0.012% w/v <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Concentrated to 12-30 mg/ml with 50 kDa MWCO spin concentrator</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion">Sitting-drop vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified TASK-1 at 8-12 mg/ml in <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">gel filtration</a> buffer</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in raw paper</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained with CHOL-<a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> mix and trigalactoside additives; data processed with STARANISO for anisotropic <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>. Three structures: apo TASK-1 (6RV2), TASK-1-BAY1000493 complex (6RV3, 50% occupancy in two orientations), and TASK-1-BAY2341237 complex (6RV4, 100% occupancy, single orientation). Ramachandran statistics: 97.56% allowed, 2.44% preferred (6RV3); 97.54% allowed, 2.46% preferred (6RV4). BAY1000493 was synthesized in-house; BAY2341237 was synthesized as described in ref 31.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>sitting-drop</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6rv2">6RV2</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MKRQNVR</span><span class="topo-membrane">TLALIVCTFTYLLVGAAV</span><span class="topo-inside">FDALESEPELIERQRLELRQQELRARYNLSQGGYEELERVVLRLKPHKAGVQWRFAGSF</span><span class="topo-unknown">YFAITVITTIG</span><span class="topo-inside">YGHAAPSTDGGKV</span><span class="topo-membrane">FCMFYALLGIPL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TLVMFQSLGERIN</span><span class="topo-outside">TLVRYLLHRAKKGLG</span><span class="topo-unknown">MRR</span><span class="topo-outside">ADVSMAN</span><span class="topo-membrane">MVLIGFFSCISTLCIGAAA</span><span class="topo-inside">FSHYEHWTFFQAY</span><span class="topo-unknown">YYCFITLTTIG</span><span class="topo-inside">FGDYVALQKDQALQTQPQYVA</span><span class="topo-membrane">FSFVYILTGLTVIGAFLN</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-membrane">LVVL</span><span class="topo-outside">RFMTMNAEDEKRD</span><span class="topo-unknown">AENLYFQ</span></span>
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
      <td>1</td>
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>8</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>84</td>
      <td>26</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>95</td>
      <td>85</td>
      <td>95</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>96</td>
      <td>108</td>
      <td>96</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>133</td>
      <td>109</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>148</td>
      <td>134</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>151</td>
      <td>149</td>
      <td>151</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>152</td>
      <td>158</td>
      <td>152</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>177</td>
      <td>159</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>190</td>
      <td>178</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>201</td>
      <td>191</td>
      <td>201</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>202</td>
      <td>222</td>
      <td>202</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>257</td>
      <td>245</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>264</td>
      <td>258</td>
      <td>264</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6rv2">6RV2</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MKRQNV</span><span class="topo-membrane">RTLALIVCTFTYLLVGAAV</span><span class="topo-inside">FDALESEPELIERQRLELRQQELRARYNLSQGGYEELERVVLRLKPHKAGVQWRFAGSF</span><span class="topo-unknown">YFAITVITTIG</span><span class="topo-inside">YGHAAPSTDGGKV</span><span class="topo-membrane">FCMFYALLGIPL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TLVMFQSLGERIN</span><span class="topo-outside">TLVRYLLHRAKKGLG</span><span class="topo-unknown">MRR</span><span class="topo-outside">ADVSMANM</span><span class="topo-membrane">VLIGFFSCISTLCIGAAA</span><span class="topo-inside">FSHYEHWTFFQAY</span><span class="topo-unknown">YYCFITLTTIG</span><span class="topo-inside">FGDYVALQKDQALQTQPQYVA</span><span class="topo-membrane">FSFVYILTGLTVIGAFLN</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-membrane">LVVL</span><span class="topo-outside">RFMTMNAEDEKRDAENL</span><span class="topo-unknown">YFQ</span></span>
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
      <td>1</td>
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>25</td>
      <td>7</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>84</td>
      <td>26</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>95</td>
      <td>85</td>
      <td>95</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>96</td>
      <td>108</td>
      <td>96</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>133</td>
      <td>109</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>148</td>
      <td>134</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>151</td>
      <td>149</td>
      <td>151</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>152</td>
      <td>159</td>
      <td>152</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>177</td>
      <td>160</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>190</td>
      <td>178</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>201</td>
      <td>191</td>
      <td>201</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>202</td>
      <td>222</td>
      <td>202</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>223</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>261</td>
      <td>245</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>264</td>
      <td>262</td>
      <td>264</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6rv3">6RV3</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MKRQ</span><span class="topo-membrane">NVRTLALIVCTFTYLLVGAAV</span><span class="topo-inside">FDALESEPELIERQRLELRQQELRARYNLSQGGYEELERVVLRLKPHKAGVQWRFAGSF</span><span class="topo-unknown">YFAITVITTIG</span><span class="topo-inside">YGHAAPSTDGGKV</span><span class="topo-membrane">FCMFYALLGIPL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TLVMFQSLGERINTLVRYLL</span><span class="topo-unknown">HRAKKGL</span><span class="topo-outside">G</span><span class="topo-unknown">MRR</span><span class="topo-outside">ADVSM</span><span class="topo-membrane">ANMVLIGFFSCISTLCIGAAA</span><span class="topo-inside">FSHYEHWTFFQAY</span><span class="topo-unknown">YYCFITLTTIG</span><span class="topo-inside">FGDYVALQKDQALQTQPQYVA</span><span class="topo-membrane">FSFVYILTGLTVIGAFLN</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-membrane">LVVLRFMTMN</span><span class="topo-outside">AEDEKRDAENL</span><span class="topo-unknown">YFQ</span></span>
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
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>5</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>84</td>
      <td>26</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>95</td>
      <td>85</td>
      <td>95</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>96</td>
      <td>108</td>
      <td>96</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>140</td>
      <td>109</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>147</td>
      <td>141</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>148</td>
      <td>148</td>
      <td>148</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>156</td>
      <td>152</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>177</td>
      <td>157</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>190</td>
      <td>178</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>201</td>
      <td>191</td>
      <td>201</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>202</td>
      <td>222</td>
      <td>202</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>250</td>
      <td>223</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>261</td>
      <td>251</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6rv3">6RV3</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MKRQ</span><span class="topo-membrane">NVRTLALIVCTFTYLLVGAAV</span><span class="topo-inside">FDALESEPELIERQRLELRQQELRARYNLSQGGYEELERVVLRLKPHKAGVQWRFAGSF</span><span class="topo-unknown">YFAITVITTIG</span><span class="topo-inside">YGHAAPSTDGGKV</span><span class="topo-membrane">FCMFYALLGIPL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TLVMFQSLGERINTLVRYLL</span><span class="topo-unknown">HRAKKGL</span><span class="topo-outside">GM</span><span class="topo-unknown">RR</span><span class="topo-outside">ADVSM</span><span class="topo-membrane">ANMVLIGFFSCISTLCIGAAA</span><span class="topo-inside">FSHYEHWTFFQAY</span><span class="topo-unknown">YYCFITLTTIG</span><span class="topo-inside">FGDYVALQKDQALQTQPQYVA</span><span class="topo-membrane">FSFVYILTGLTVIGAFLN</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-membrane">LVVLRFMTMN</span><span class="topo-outside">AEDEKRDAENL</span><span class="topo-unknown">YFQ</span></span>
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
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>5</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>84</td>
      <td>26</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>95</td>
      <td>85</td>
      <td>95</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>96</td>
      <td>108</td>
      <td>96</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>140</td>
      <td>109</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>147</td>
      <td>141</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>148</td>
      <td>149</td>
      <td>148</td>
      <td>149</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>156</td>
      <td>152</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>177</td>
      <td>157</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>190</td>
      <td>178</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>201</td>
      <td>191</td>
      <td>201</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>202</td>
      <td>222</td>
      <td>202</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>250</td>
      <td>223</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>261</td>
      <td>251</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6rv4">6RV4</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MKRQ</span><span class="topo-membrane">NVRTLALIVCTFTYLLVGAAVF</span><span class="topo-inside">DALESEPELIERQRLELRQQELRARYNLSQGGYEELERVVLRLKPHKAGVQWRFAGS</span><span class="topo-unknown">FYFAITVITTIGY</span><span class="topo-inside">GHAAPSTDGGK</span><span class="topo-membrane">VFCMFYALLGIPL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TLVMFQSLGERINTLVRYLL</span><span class="topo-unknown">HRAKKGL</span><span class="topo-outside">G</span><span class="topo-unknown">MRR</span><span class="topo-outside">ADVSM</span><span class="topo-membrane">ANMVLIGFFSCISTLCIGAAA</span><span class="topo-inside">FSHYEHWTFFQAY</span><span class="topo-unknown">YYCFITLTTIGF</span><span class="topo-inside">GDYVALQKDQALQTQPQYV</span><span class="topo-membrane">AFSFVYILTGLTVIGAFLN</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-membrane">LVVLRFMTMNA</span><span class="topo-outside">EDEKRDA</span><span class="topo-unknown">ENLYFQ</span></span>
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
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>26</td>
      <td>5</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>83</td>
      <td>27</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>96</td>
      <td>84</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>97</td>
      <td>107</td>
      <td>97</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>140</td>
      <td>108</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>147</td>
      <td>141</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>148</td>
      <td>148</td>
      <td>148</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>156</td>
      <td>152</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>177</td>
      <td>157</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>190</td>
      <td>178</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>202</td>
      <td>191</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>203</td>
      <td>221</td>
      <td>203</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>251</td>
      <td>222</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>252</td>
      <td>258</td>
      <td>252</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6rv4">6RV4</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MKRQ</span><span class="topo-membrane">NVRTLALIVCTFTYLLVGAAVF</span><span class="topo-inside">DALESEPELIERQRLELRQQELRARYNLSQGGYEELERVVLRLKPHKAGVQWRFAGSF</span><span class="topo-unknown">YFAITVITTIGY</span><span class="topo-inside">GHAAPSTDGGK</span><span class="topo-membrane">VFCMFYALLGIPL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TLVMFQSLGERINTLVRYLL</span><span class="topo-unknown">HRAKKGL</span><span class="topo-outside">G</span><span class="topo-unknown">MRR</span><span class="topo-outside">ADVSM</span><span class="topo-membrane">ANMVLIGFFSCISTLCIGAAA</span><span class="topo-inside">FSHYEHWTFFQAY</span><span class="topo-unknown">YYCFITLTTIGF</span><span class="topo-inside">GDYVALQKDQALQTQPQYV</span><span class="topo-membrane">AFSFVYILTGLTVIGAFLN</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-membrane">LVVLRFMTMN</span><span class="topo-outside">AEDEKRDAENL</span><span class="topo-unknown">YFQ</span></span>
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
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>26</td>
      <td>5</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>84</td>
      <td>27</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>96</td>
      <td>85</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>97</td>
      <td>107</td>
      <td>97</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>140</td>
      <td>108</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>147</td>
      <td>141</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>148</td>
      <td>148</td>
      <td>148</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>156</td>
      <td>152</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>177</td>
      <td>157</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>190</td>
      <td>178</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>202</td>
      <td>191</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>203</td>
      <td>221</td>
      <td>203</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>250</td>
      <td>222</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>261</td>
      <td>251</td>
      <td>261</td>
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

### Discovery of the X-gate in TASK channels

TASK-1 contains a novel lower gate (the 'X-gate') formed by the crossed
C-terminal M4 transmembrane helices. This is created by six residues
(243VLRFMT248) that adopt an extended two-turn-helical structure lacking
standard alpha/3-10 hydrogen bonding. The gate narrows the vestibule
entrance to only 0.8 A radius (measured by CHAP), compared to 7.5 A in
[KCNK10](/xray-mp-wiki/proteins/voltage-gated-channels/trek-2/) (PDB 4XDJ). TASK-3 and TASK-5 likely form similar X-gates based on
sequence conservation. This is the first example of a lower gate in K2P
channels, breaking the paradigm that K2P channels lack lower gates.

### X-gate mutations increase channel activity

Alanine scanning mutagenesis across the distal M4 helix (Thr230-Thr248)
showed that disruption of the X-gate increases the low basal activity of
TASK-1. Mutation of any X-gate residue except Val243 led to increased
currents without increased surface expression. Leu244Ala showed the largest
effect, with a sixfold increase in channel-open probability (from 0.7% to
4.0%) and increased open times. The X-gate is also essential for activation
by volatile anaesthetics (sevoflurane, halothane) - mutations in the X-gate
reduce anaesthetic activation.

### Latch region stabilizes the X-gate

A latch region involving Arg7 on the N terminus and Arg131 on the M2-M3
loop stabilizes the X-gate by electrostatic interactions with the distal
M4 region. Mutations to acidic residues (Arg7Asp, Arg131Asp) result in
5-10 fold increases in currents without increased surface expression,
confirming the latch's role in stabilizing the closed X-gate. X-gate
opening and pH sensing (via His98) appear not to be strictly coupled.

### High-affinity inhibitors are trapped by the X-gate

BAY1000493 and BAY2341237 bind to the closed TASK-1 conformation below
the selectivity filter without perturbing the X-gate structure. Both
compounds fit precisely on the vestibule surface, with Leu122 projecting
below the compounds. The binding site is created by the closed X-gate,
which traps inhibitors within the vestibule, explaining their exceptionally
slow washout rates. Mutation of binding-site residues (Thr93Cys, Ile118Ala,
Leu122Ala, Thr199Cys, Leu239Ala, Asn240Ala) substantially reduced
inhibition. Once trapped, the inhibitor remains bound for extended periods,
with important implications for drug development and clinical trials.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/traak/">Human TRAAK Potassium Channel (K2P 4.1)</a> — K2P channel family comparison; TREK-2 (4XDJ) used as comparison for vestibule size measurements
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/k2p2-1/">Human K2P2.1 (TREK-1) I110D Mutant</a> — Fellow K2P channel member; both are two-pore domain potassium channels
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/">C-type Inactivation</a> — K2P channels use C-type gate as principal gating site; X-gate is an additional lower gate unique to TASK
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/">Ion Channel Selectivity Filter</a> — TASK-1 has a pseudo-tetrameric selectivity filter with K+ binding sites S1-S4
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/">KirBac Potassium Channels</a> — Inward rectifier potassium channels discussed as comparison for lower gate architecture
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/trek-2/">KCNK10</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
