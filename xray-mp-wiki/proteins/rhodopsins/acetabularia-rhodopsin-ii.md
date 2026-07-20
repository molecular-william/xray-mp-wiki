---
title: "Acetabularia Rhodopsin II"
created: 2026-05-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2011.06.028]
verified: agent
uniprot_id: G1K3Q0
---

# Acetabularia Rhodopsin II

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span> <span class="expr-badge expr-mammalian">Mammalian</span> <span class="expr-badge expr-cell-free">Cell-free</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/G1K3Q0">UniProt: G1K3Q0</a>

<span class="expr-badge">Acetabularia acetabulum</span>

## Overview

Acetabularia rhodopsin II (ARII) is a light-driven proton pump from the marine alga Acetabularia acetabulum, representing the first crystal structure of a eukaryotic member of the microbial rhodopsin family. The protein was expressed using an E. coli cell-free protein synthesis system and crystallized by the lipidic mesophase (in meso) method at 3.2 A resolution. ARII shares structural similarity with [bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) but exhibits a reversed proton uptake/release sequence and lacks dark-light adaptation.

## Publications

### doi/10.1016##j.jmb.2011.06.028

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3am6">3AM6</a></td>
      <td>3.2 A</td>
      <td>P212121</td>
      <td>ARII opsin, 247 amino acid residues, N11-tag at N-terminus (not removed)</td>
      <td>Retinal (all-trans), Cholesterol (8 molecules in asymmetric unit)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli cell-free protein synthesis system (supplemented with 0.4% digitonin and 6.7 mg/ml phosphatidylcholine)
- **Construct**: N11-tag (modified histidine tag) at N-terminus, not removed after purification; 247 amino acid residues (gene truncated at position 229)

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
      <td>Cell-free synthesis</td>
      <td>Cell-free protein synthesis</td>
      <td>--</td>
      <td>Cell-free reaction mixture with 0.4% <a href="/xray-mp-wiki/reagents/detergents/digitonin/">digitonin</a> and 6.7 mg/ml <a href="/xray-mp-wiki/reagents/lipids/phosphatidylcholine/">phosphatidylcholine</a> + 0.4% <a href="/xray-mp-wiki/reagents/digitonin/">digitonin</a></td>
      <td>Yield of 4.5 mg from a 27-ml reaction. Synthesis performed in presence of both lipid and detergent, enabling high target protein content in liposomes.</td>
    </tr>
    <tr>
      <td>Ni2+ chelating <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td>Ni2+ chelating resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>-HCl (pH 7.0), 400 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">sodium chloride</a></td>
      <td>Modified N11-tag at N-terminus used for purification; tag not removed.</td>
    </tr>
    <tr>
      <td>Gel filtration chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td>Gel filtration column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>-HCl (pH 7.0), 400 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">sodium chloride</a>, 1 mM dithiothreitol, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final fractions concentrated to 45.4 mg/ml with a filter unit for crystallization. Absorption ratio at 280/532 <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a> was 1.34.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase crystallization</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">in meso</a> using <a href="/xray-mp-wiki/reagents/lipids/monoolein/">monoolein</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>45.4 mg/ml ARII in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> (pH 7.0), 400 mM NaCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 °C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals cryocooled for X-ray data collection at SPring-8 BL41XU beamline (10-µm microbeam, Mar MX-225HE detector)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Reddish-purple plate-like crystals grew to 100 µm × 100 µm × 10 µm. Crystals were very unstable under open-air conditions and easily damaged during handling. Four ARII monomers with eight <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">cholesterol</a> molecules in the asymmetric unit. Cholesterol molecules located between helices A and G, stabilizing overlaid planar layers. No obvious electron densities for loops between helices A-B and E-F.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3am6">3AM6</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MADVETETGMIA</span><span class="topo-membrane">QWIVFAIMAAAAIAFGVAVHFR</span><span class="topo-outside">P</span><span class="topo-unknown">SE</span><span class="topo-outside">LK</span><span class="topo-membrane">SAYYINIAICTIAATAYYAMA</span><span class="topo-inside">VNYQDLTMNGERQVVY</span><span class="topo-membrane">ARYIDWVLTTPLLLLDLIVM</span><span class="topo-outside">TKM</span><span class="topo-membrane">GGVMISWVIGADIFMIVFGIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-membrane">GA</span><span class="topo-inside">FEDEHKFKW</span><span class="topo-membrane">VYFIAGCVMQAVLTYGMYNATW</span><span class="topo-outside">KDD</span><span class="topo-unknown">LK</span><span class="topo-outside">KSPEYHS</span><span class="topo-membrane">SYVSLLVFLSILWVFYPVVWA</span><span class="topo-inside">FGSGSGVLSVDNE</span><span class="topo-membrane">AILMGILDVLAKPLFGMGCLIAHE</span><span class="topo-outside">TIFKK</span><span class="topo-unknown">M</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>12</td>
      <td>1</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>34</td>
      <td>13</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>37</td>
      <td>36</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>38</td>
      <td>39</td>
      <td>38</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>60</td>
      <td>40</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>76</td>
      <td>61</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>96</td>
      <td>77</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>99</td>
      <td>97</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>122</td>
      <td>100</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>131</td>
      <td>123</td>
      <td>131</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>153</td>
      <td>132</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>156</td>
      <td>154</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>158</td>
      <td>157</td>
      <td>158</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>159</td>
      <td>165</td>
      <td>159</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>186</td>
      <td>166</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>199</td>
      <td>187</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>223</td>
      <td>200</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>228</td>
      <td>224</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>229</td>
      <td>229</td>
      <td>229</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3am6">3AM6</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MADVETETGMI</span><span class="topo-membrane">AQWIVFAIMAAAAIAFGVAVHFR</span><span class="topo-outside">P</span><span class="topo-unknown">SE</span><span class="topo-outside">LK</span><span class="topo-membrane">SAYYINIAICTIAATAYYAMA</span><span class="topo-inside">VNYQDLTMNGERQVV</span><span class="topo-membrane">YARYIDWVLTTPLLLLDLIV</span><span class="topo-outside">MTKMGG</span><span class="topo-membrane">VMISWVIGADIFMIVFGIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-membrane">GAFE</span><span class="topo-inside">DEHK</span><span class="topo-membrane">FKWVYFIAGCVMQAVLTYGMY</span><span class="topo-outside">NATWKDD</span><span class="topo-unknown">LK</span><span class="topo-outside">KSPEYHSSY</span><span class="topo-membrane">VSLLVFLSILWVFYPVVWAFGSGS</span><span class="topo-inside">GVLSVDN</span><span class="topo-membrane">EAILMGILDVLAKPLFGMGCLIA</span><span class="topo-outside">HETIFKK</span><span class="topo-unknown">M</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>34</td>
      <td>12</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>37</td>
      <td>36</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>38</td>
      <td>39</td>
      <td>38</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>60</td>
      <td>40</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>75</td>
      <td>61</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>95</td>
      <td>76</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>101</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>124</td>
      <td>102</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>128</td>
      <td>125</td>
      <td>128</td>
      <td>Inside</td>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>158</td>
      <td>157</td>
      <td>158</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>159</td>
      <td>167</td>
      <td>159</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>191</td>
      <td>168</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>198</td>
      <td>192</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>221</td>
      <td>199</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>228</td>
      <td>222</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>229</td>
      <td>229</td>
      <td>229</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3am6">3AM6</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MADVETETGMI</span><span class="topo-membrane">AQWIVFAIMAAAAIAFGVAVHFR</span><span class="topo-outside">P</span><span class="topo-unknown">SE</span><span class="topo-outside">LK</span><span class="topo-membrane">SAYYINIAICTIAATAYYAMA</span><span class="topo-inside">VNYQDLTMNGERQVV</span><span class="topo-membrane">YARYIDWVLTTPLLLLDLIV</span><span class="topo-outside">MTKMGG</span><span class="topo-membrane">VMISWVIGADIFMIVFGIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-membrane">GAFE</span><span class="topo-inside">DEHK</span><span class="topo-membrane">FKWVYFIAGCVMQAVLTYGMY</span><span class="topo-outside">NATWKDD</span><span class="topo-unknown">LK</span><span class="topo-outside">KSPEYHSSY</span><span class="topo-membrane">VSLLVFLSILWVFYPVVWAFGSGS</span><span class="topo-inside">GVLSVDN</span><span class="topo-membrane">EAILMGILDVLAKPLFGMGCLIA</span><span class="topo-outside">HETIFKK</span><span class="topo-unknown">M</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>34</td>
      <td>12</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>37</td>
      <td>36</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>38</td>
      <td>39</td>
      <td>38</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>60</td>
      <td>40</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>75</td>
      <td>61</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>95</td>
      <td>76</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>101</td>
      <td>96</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>124</td>
      <td>102</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>128</td>
      <td>125</td>
      <td>128</td>
      <td>Inside</td>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>158</td>
      <td>157</td>
      <td>158</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>159</td>
      <td>167</td>
      <td>159</td>
      <td>167</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>191</td>
      <td>168</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>198</td>
      <td>192</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>221</td>
      <td>199</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>228</td>
      <td>222</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>229</td>
      <td>229</td>
      <td>229</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3am6">3AM6</a> — Chain D (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MADVETETGMIA</span><span class="topo-membrane">QWIVFAIMAAAAIAFGVAVHF</span><span class="topo-outside">RP</span><span class="topo-unknown">SE</span><span class="topo-outside">LK</span><span class="topo-membrane">SAYYINIAICTIAATAYYAMA</span><span class="topo-inside">VNYQDLTMNGERQVVY</span><span class="topo-membrane">ARYIDWVLTTPLLLLDLIVM</span><span class="topo-outside">TKMGG</span><span class="topo-membrane">VMISWVIGADIFMIVFGIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220         </span>
<span class="topo-line"><span class="topo-membrane">GA</span><span class="topo-inside">FEDEHKFKW</span><span class="topo-membrane">VYFIAGCVMQAVLTYGMYNATW</span><span class="topo-outside">KDD</span><span class="topo-unknown">LK</span><span class="topo-outside">KSPEYHS</span><span class="topo-membrane">SYVSLLVFLSILWVFYPVVWA</span><span class="topo-inside">FGSGSGVLSVDNE</span><span class="topo-membrane">AILMGILDVLAKPLFGMGCLIAH</span><span class="topo-outside">ETIFKK</span><span class="topo-unknown">M</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>12</td>
      <td>1</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>33</td>
      <td>13</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>35</td>
      <td>34</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>37</td>
      <td>36</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>38</td>
      <td>39</td>
      <td>38</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>60</td>
      <td>40</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>76</td>
      <td>61</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>96</td>
      <td>77</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>101</td>
      <td>97</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>122</td>
      <td>102</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>131</td>
      <td>123</td>
      <td>131</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>153</td>
      <td>132</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>156</td>
      <td>154</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>158</td>
      <td>157</td>
      <td>158</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>159</td>
      <td>165</td>
      <td>159</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>186</td>
      <td>166</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>199</td>
      <td>187</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>222</td>
      <td>200</td>
      <td>222</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>228</td>
      <td>223</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>229</td>
      <td>229</td>
      <td>229</td>
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

### First eukaryotic microbial rhodopsin structure

ARII is the first crystal structure of a eukaryotic member of the microbial rhodopsin family, determined at 3.2 A resolution (PDB: 3AM6). The structure reveals seven transmembrane helices (A-G) and a retinal chromophore, with four monomers and eight cholesterol molecules in the asymmetric unit. The structure is highly similar to bacteriorhodopsin (Z score=28.9), N. pharaonis SRII (Z score=29.3), and Anabaena sensory rhodopsin (Z score=27.8).

### Reversed proton uptake/release sequence compared to bacteriorhodopsin

During the ARII photocycle, proton uptake from the cytoplasm occurs first, followed by release to the extracellular side. This is reversed relative to bacteriorhodopsin, where proton release precedes uptake at pH 7.0. The reversed sequence is attributed to the lack of Ser189 (corresponding to Glu194BR, the proton-releasing group in BR) and the different pKa of Glu199 (corresponding to Glu204BR) in ARII.

### Conserved proton transfer pathway residues

The cytoplasmic-to-extracellular proton transfer pathway in ARII consists of: Asp92 (corresponding to Asp96BR, proton donor), Schiff base at Lys211, Asp207 (Asp212BR), Asp81 (Asp85BR, proton acceptor), Arg78 (Arg82BR), Glu199 (Glu204BR), and Ser189 (Glu194BR). The Arg78 side chain orientation is opposite to Arg82 in BR but same as Arg72 in NpSRII, which is capable of proton transfer.

### Cys218 involvement in proton uptake from cytoplasm

The side chain of Cys218 in ARII (corresponding to Leu223 in BR) is positioned 3.0 A from the δ2 oxygen of Asp92, suggesting a low-barrier hydrogen bond that may promote proton uptake. ARII and NpSRII both contain a non-dissociable residue at this position and show late proton release, unlike BR which has a dissociable residue and shows fast proton release.

### Retinal isomer composition and lack of dark adaptation

Unlike BR which contains both all-trans and 13-cis retinal in the dark, ARII contains 95.5% all-trans and 4.5% 13-cis retinal in the dark, with no dark adaptation observed. This is similar to NpSRII, which also has only all-trans retinal. The relative positions of the protonated Schiff base and counterion are important for light-dark adaptation.

### Photocycle kinetics and intermediates

The ARII photocycle proceeds on a millisecond timescale, similar to a typical light-driven proton pump. M intermediate formation occurs earlier than in BR. The K intermediate decay almost immediately leads to M formation, and the L intermediate is difficult to observe. Both M and O intermediates are confirmed.

### Cholesterol-mediated crystal stabilization

Eight cholesterol molecules were observed in the asymmetric unit, located between helices A and G of one ARII molecule and helix A of the neighboring ARII molecule. These intermolecular contacts play important roles in stabilizing the overlaid planar layers of ARII in the thin plate-like crystal.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — ARII structure compared to BR; conserved proton transfer pathway residues; reversed proton release/uptake sequence
- <a href="/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-2/">Archaerhodopsin-2</a> — Another microbial rhodopsin with late proton release behavior
- <a href="/xray-mp-wiki/methods/expression-systems/cell-free-protein-synthesis/">Cell-free Protein Synthesis</a> — ARII expressed using E. coli cell-free synthesis system supplemented with detergent and lipid
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — ARII crystallized by in meso method using monoolein
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Ni2+ chelating affinity chromatography used for N11-tagged ARII purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Gel filtration chromatography used for final purification step
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-β-D-maltoside (DDM)</a> — 0.01% DDM used in gel filtration buffer for ARII purification
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Primary lipid used for in meso crystallization of ARII
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — 10% glycerol used in purification buffer
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl buffer)</a> — 20 mM Tris-HCl (pH 7.0) used in purification buffer
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/">Rhodopsin Photocycle</a> — ARII follows the BR-type photocycle with K, M, and O intermediates
- <a href="/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/">Channelrhodopsin C1C2</a> — Related microbial rhodopsin; ARII used in opto-neurophysiology applications
