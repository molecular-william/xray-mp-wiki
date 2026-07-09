---
title: "DltB (Membrane-Bound O-Acyltransferase)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-018-0568-2]
verified: regex
uniprot_id: ['Q5M4V3', 'Q5M4V4']
---

# DltB (Membrane-Bound O-Acyltransferase)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5M4V3">UniProt: Q5M4V3</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5M4V4">UniProt: Q5M4V4</a>

<span class="expr-badge">Streptococcus thermophilus</span>

## Overview

DltB is a membrane-bound O-acyltransferase (MBOAT) from Streptococcus thermophilus responsible for the D-alanylation of cell-wall teichoic acid in Gram-positive bacteria. Crystal structures of DltB were determined in the apo state (PDB 6BUG, 3.30 Å; PDB 6BUI, 3.30 Å) and in complex with the D-alanyl carrier protein DltC-Ppant (PDB 6BUH, 3.15 Å). DltB contains a ring of 11 peripheral transmembrane helices that shield a highly conserved extracellular structural funnel extending into the middle of the lipid bilayer. The conserved catalytic histidine residue (His336) is located at the bottom of this funnel and is connected to the intracellular DltC through a narrow tunnel. Mutation of either the catalytic histidine or the DltC-binding site abolishes D-alanylation of lipoteichoic acid and sensitizes Bacillus subtilis to cell-wall stress, suggesting cross-membrane catalysis involving the tunnel. Structure-guided sequence comparison reveals a conserved structural core among MBOATs from different organisms, providing a template for understanding structure-function relationships and for developing therapeutic MBOAT inhibitors targeting proteins such as PORCN, HHAT, and DGAT1.

## Publications

### doi/10.1038##s41586-018-0568-2

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bug">6BUG</a></td>
      <td>3.30 A</td>
      <td>P2_1</td>
      <td>Full-length DltB from Streptococcus thermophilus</td>
      <td>None (apo state)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6buh">6BUH</a></td>
      <td>3.15 A</td>
      <td>P2_1</td>
      <td>DltB in complex with DltC-Ppant (4'-phosphopantetheine-modified DltC)</td>
      <td>4'-phosphopantetheine (Ppant) on DltC Ser35</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bui">6BUI</a></td>
      <td>3.30 A</td>
      <td>P2_1_2_1_2</td>
      <td>Full-length DltB from Streptococcus thermophilus</td>
      <td>None (apo state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C43 (DE3)
- **Construct**: Full-length S. thermophilus DltB subcloned into pET21b. Expression induced with 0.4 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/) at OD600 = 1.0, 37°C for 5 h. DltC subcloned into pQLink with N-terminal GST-tag for complex studies.

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
      <td>Cell lysis and membrane preparation</td>
      <td>Sonication and ultracentrifugation</td>
      <td>--</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 8.0, 150 mM NaCl + --</td>
      <td>Cells disrupted by sonication, debris removed at 20,000g for 10 min, membranes collected at 100,000g for 1.5 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 8.0, 150 mM NaCl + 1.5% (w/v) n-decyl-β-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Incubated for 2 h at 4°C, then ultracentrifuged at 100,000g for 30 min</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Ni-NTA affinity</td>
      <td>Ni-NTA (Qiagen)</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 8.0, 500 mM NaCl, 25 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Wash buffer; eluted with 400 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/30 (GE Healthcare)</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 8.0, 150 mM NaCl + 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (or other detergents from Anatrace)</td>
      <td>Concentrated to 10 mg/ml before SEC; peak fractions collected</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>DltB purified in n-nonyl-β-D-glucopyranoside (Anatrace) at ~10 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>21% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.5, 100 mM NaCl, 100 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C (room temperature)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal form I (P2₁, 3.30 Å): native DltB apo. Crystal form II (P2₁, 3.15 Å): DltB-DltC-Ppant complex, DltB and DltC mixed at 1:2 molar ratio. Crystal form III (P2₁2₁2, 3.30 Å): DltB apo. Au-SAD phasing used for structure determination (Au derivative for crystal form I).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bug">6BUG</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-unknown">GSH</span><span class="topo-inside">MDVKAEVIEIIDELFMEDVSDMMDEDLFDAGVLDSMGTVELIVELESRFDIRVPVSEFGRDDWNTANKIVEGVTELRNA</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>4</td>
      <td>82</td>
      <td>1</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bug">6BUG</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">IDFLKQ</span><span class="topo-outside">LPH</span><span class="topo-membrane">LEPYGNPFYFIYLGIALLPIFI</span><span class="topo-inside">GLFFKKRF</span><span class="topo-membrane">AIYECLVSITFIVLALT</span><span class="topo-outside">GTHA</span><span class="topo-membrane">SQILALLFYIVWQIIW</span><span class="topo-inside">VYSYKRYRSQRDNKWVFYL</span><span class="topo-membrane">HSFLVVLPLILVKVEPTI</span><span class="topo-outside">NGTQ</span><span class="topo-membrane">SL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LNFLGISYLTFRAV</span><span class="topo-inside">GMIIEMRDGVLKEFTLGEFL</span><span class="topo-unknown">RFMLFMPTFTSGPI</span><span class="topo-inside">DR</span><span class="topo-unknown">FKRFNEDYQ</span><span class="topo-inside">SIPNRDELLNML</span><span class="topo-membrane">EQAVKYIMLGFLYKFVLAQIFG</span><span class="topo-outside">SML</span><span class="topo-unknown">LPPLKAQALSQ</span><span class="topo-outside">GGIFNLPT</span><span class="topo-membrane">LGVMY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">VYGFDLFFDFAGYSMFALAVSNLM</span><span class="topo-inside">GIKSPINFDKPFISRDMKEFWNRWHMSLSFWFRDFVFMRLVIVLMRNKVFKNRNTTSNVAYI</span><span class="topo-membrane">INMMVMGFWHGITW</span><span class="topo-outside">Y</span><span class="topo-membrane">YIAYGIFHGIGL</span><span class="topo-inside">VINDAWL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420     </span>
<span class="topo-line"><span class="topo-inside">RKKKTINKDRKKAGLKPLPENKWTKA</span><span class="topo-membrane">LGIFITFNTVMLSFLIFSGFL</span><span class="topo-outside">NDLWFTK</span><span class="topo-unknown">KLEHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>10</td>
      <td>8</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>32</td>
      <td>11</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>40</td>
      <td>33</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>57</td>
      <td>41</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>61</td>
      <td>58</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>77</td>
      <td>62</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>96</td>
      <td>78</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>114</td>
      <td>97</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>118</td>
      <td>115</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>134</td>
      <td>119</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>154</td>
      <td>135</td>
      <td>154</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>168</td>
      <td>155</td>
      <td>168</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>169</td>
      <td>170</td>
      <td>169</td>
      <td>170</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>179</td>
      <td>171</td>
      <td>179</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>180</td>
      <td>191</td>
      <td>180</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>213</td>
      <td>192</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>216</td>
      <td>214</td>
      <td>216</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>227</td>
      <td>217</td>
      <td>227</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>228</td>
      <td>235</td>
      <td>228</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>264</td>
      <td>236</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>326</td>
      <td>265</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>340</td>
      <td>327</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>341</td>
      <td>341</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>353</td>
      <td>342</td>
      <td>353</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>354</td>
      <td>386</td>
      <td>354</td>
      <td>386</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>407</td>
      <td>387</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>408</td>
      <td>414</td>
      <td>408</td>
      <td>414</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6buh">6BUH</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80  </span>
<span class="topo-line"><span class="topo-unknown">GSH</span><span class="topo-inside">MDVKAEVIEIIDELFMEDVSDMMDEDLFDAGVLDSMGTVELIVELESRFDIRVPVSEFGRDDWNTANKIVEGVTELRNA</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>4</td>
      <td>82</td>
      <td>1</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6buh">6BUH</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">IDFLKQ</span><span class="topo-outside">L</span><span class="topo-membrane">PHLEPYGNPFYFIYLGIALLPI</span><span class="topo-inside">FIGLFFKKRFAI</span><span class="topo-membrane">YECLVSITFIVLALT</span><span class="topo-outside">GTHASQ</span><span class="topo-membrane">ILALLFYIVWQIIWVYSY</span><span class="topo-inside">KRYRSQRDNK</span><span class="topo-membrane">WVFYLHSFLVVLPLILVKV</span><span class="topo-outside">EPTINGTQSL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">L</span><span class="topo-membrane">NFLGISYLTFRAVGMI</span><span class="topo-inside">IEMRDGVLKEFTLGEF</span><span class="topo-unknown">LRFMLFMPTFTSGPID</span><span class="topo-inside">R</span><span class="topo-unknown">FKRFNEDYQ</span><span class="topo-inside">SIPNRDELLNMLEQA</span><span class="topo-membrane">VKYIMLGFLYKFVLAQIFG</span><span class="topo-outside">SMLLPPLKAQALSQGGIFNLPTLGVM</span><span class="topo-membrane">Y</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">VYGFDLFFDFAGYSMFALAVSNLM</span><span class="topo-inside">GIKSPINFDKPFISRDMKEFWNRWHMSLSFWFRDFV</span><span class="topo-unknown">FMRLVIVLMR</span><span class="topo-inside">NKVFKNRN</span><span class="topo-membrane">TTSNVAYIINMMVMGFWHGI</span><span class="topo-outside">TWY</span><span class="topo-membrane">YIAYGIFHGIGLVINDAWL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420     </span>
<span class="topo-line"><span class="topo-inside">RKKKTINKDRKKAGLKPLPENK</span><span class="topo-membrane">WTKALGIFITFNTVMLSFLIFS</span><span class="topo-outside">GFLNDLWFTK</span><span class="topo-unknown">KLEHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>30</td>
      <td>9</td>
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
      <td>57</td>
      <td>43</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>63</td>
      <td>58</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>81</td>
      <td>64</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>91</td>
      <td>82</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>110</td>
      <td>92</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>121</td>
      <td>111</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>137</td>
      <td>122</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>153</td>
      <td>138</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>169</td>
      <td>154</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>170</td>
      <td>170</td>
      <td>170</td>
      <td>170</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>179</td>
      <td>171</td>
      <td>179</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>180</td>
      <td>194</td>
      <td>180</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>213</td>
      <td>195</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>239</td>
      <td>214</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>264</td>
      <td>240</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>300</td>
      <td>265</td>
      <td>300</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>301</td>
      <td>310</td>
      <td>301</td>
      <td>310</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>311</td>
      <td>318</td>
      <td>311</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>338</td>
      <td>319</td>
      <td>338</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>339</td>
      <td>341</td>
      <td>339</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>360</td>
      <td>342</td>
      <td>360</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>361</td>
      <td>382</td>
      <td>361</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>404</td>
      <td>383</td>
      <td>404</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>414</td>
      <td>405</td>
      <td>414</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bui">6BUI</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIDFLKQLPHL</span><span class="topo-membrane">EPYGNPFYFIYLGIALLPIFIG</span><span class="topo-outside">LFFKKR</span><span class="topo-membrane">FAIYECLVSITFIVLAL</span><span class="topo-inside">TGTHASQ</span><span class="topo-membrane">ILALLFYIVWQIIW</span><span class="topo-outside">VYSYKRYRSQRDNKWVFYLHSF</span><span class="topo-membrane">LVVLPLILVKVEPTI</span><span class="topo-inside">NGTQ</span><span class="topo-membrane">SL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LNFLGISYLTFRAV</span><span class="topo-outside">GMIIEMRDGVLKEFTLGEFL</span><span class="topo-unknown">RFMLFMPTFTSGPI</span><span class="topo-outside">DR</span><span class="topo-unknown">FKRFNEDYQ</span><span class="topo-outside">SIPNRDELLNML</span><span class="topo-membrane">EQAVKYIMLGFLYKFVLAQIFG</span><span class="topo-inside">SML</span><span class="topo-unknown">LPPLKAQALSQ</span><span class="topo-inside">GGIFNLPT</span><span class="topo-membrane">LGVMY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">VYGFDLFFDFAGYSMFALAVSNLM</span><span class="topo-outside">GIKSPINFDKPFISRDMKEFWNRWHMSLSFWFRDFVFMRLVIVLMRNKVFKNRNTTSNVAYIINM</span><span class="topo-membrane">MVMGFWHGIT</span><span class="topo-inside">W</span><span class="topo-membrane">YYIAYGIFHGIG</span><span class="topo-outside">LVINDAWL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420     </span>
<span class="topo-line"><span class="topo-outside">RKKKTINKDRKKAGLKPLPENKWTKALGI</span><span class="topo-membrane">FITFNTVMLSFLIFSGFLN</span><span class="topo-inside">DLWFTK</span><span class="topo-unknown">KLEHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>33</td>
      <td>12</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>39</td>
      <td>34</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>56</td>
      <td>40</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>63</td>
      <td>57</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>77</td>
      <td>64</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>99</td>
      <td>78</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>114</td>
      <td>100</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>118</td>
      <td>115</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>134</td>
      <td>119</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>154</td>
      <td>135</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>168</td>
      <td>155</td>
      <td>168</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>169</td>
      <td>170</td>
      <td>169</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>179</td>
      <td>171</td>
      <td>179</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>180</td>
      <td>191</td>
      <td>180</td>
      <td>191</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>213</td>
      <td>192</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>216</td>
      <td>214</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>227</td>
      <td>217</td>
      <td>227</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>228</td>
      <td>235</td>
      <td>228</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>264</td>
      <td>236</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>329</td>
      <td>265</td>
      <td>329</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>339</td>
      <td>330</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>340</td>
      <td>340</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>352</td>
      <td>341</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>389</td>
      <td>353</td>
      <td>389</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>408</td>
      <td>390</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>414</td>
      <td>409</td>
      <td>414</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Novel MBOAT fold with ring of peripheral helices

DltB contains 17 helices arranged with 11 peripheral transmembrane helices forming an external ring-shaped ridge that shields a central basin thinner than the lipid bilayer. The structure can be divided into three parts: the N-terminal helical ridge (N-ridge), the central core, and the C-terminal helical ridge (C-ridge). A Dali search found no similar structures, revealing a novel protein fold for the MBOAT superfamily.

### Conserved extracellular funnel and catalytic histidine

A deep extracellular structural funnel extends from the extracellular surface into the middle of the lipid bilayer. The completely conserved catalytic histidine (His336) is located at the bottom of this funnel. The funnel surface is highly conserved among MBOATs, suggesting it serves as the substrate-binding site for the acyl-group acceptor (e.g., LTA for DltB).

### Cross-membrane catalysis via a narrow tunnel

A narrow tunnel connects the extracellular funnel to the intracellular side where DltC-Ppant binds. The distance between the Ser35-Ppant phosphate group and His336 is approximately 21 Å — the length of the Ppant-D-Ala chain (~20 Å). This suggests a cross-membrane catalytic mechanism where the Ppant chain delivers D-Ala from DltC through the tunnel to His336 for transfer to LTA in the extracellular funnel.

### DltC binding interface

DltC-Ppant binds to the cytoplasmic side of DltB primarily through a mostly hydrophobic interface formed by DltB residues Met302, Val305, Ile306, and Met309 on the C-terminal half of helix H13, and DltC residues Met36, Val39, Val43, and Val55 on helix α3 and the α3-α4 loop. Arg317 forms charged hydrogen bonds with DltC Glu40, and the Ppant phosphate group forms a salt bridge with DltB Lys282.

### Conserved MBOAT core across species

Despite low overall sequence homology, the MBOAT central core (funnel, tunnel, His336, and key helices H6, H10, H12) is conserved among vertebrate MBOATs including PORCN (Wnt acyltransferase), HHAT (hedgehog acyltransferase), GOAT (ghrelin O-acyltransferase), DGAT1, and ACAT. The peripheral ridges are non-conserved and likely mediate distinct substrate recognition, enabling targeted drug development against individual MBOAT family members.

### Functional validation of catalytic mechanism

Mutation of His336 (catalytic His) or the DltC-binding interface residues (V305D/I306D) completely abolished LTA D-alanylation and reduced B. subtilis viability under lysozyme stress. The DltB-specific inhibitor m-AMSA also blocked D-alanylation, confirming the functional importance of the observed structural features for DltB activity.


## Cross-References

- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — DltB was crystallized using hanging-drop vapor diffusion
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Ni-NTA affinity chromatography used for DltB purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — SEC (Superdex-200) used for final purification step
- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction (SAD)</a> — Au-SAD phasing used for experimental structure determination
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> — Purification and crystallization buffer (Tris-HCl pH 7.5-8.0)
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a> — Crystallization additive (100 mM MgCl2)
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> — Crystallization precipitant (21% PEG400)
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used for elution in Ni-NTA affinity chromatography
- <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> — Referenced in context related to Iptg
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> — Referenced in context related to Tris Hcl
