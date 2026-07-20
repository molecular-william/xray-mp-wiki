---
title: "AtPIP2;4 (Arabidopsis thaliana Plasma Membrane Intrinsic Protein 2;4)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.bbamem.2019.183065]
verified: agent
uniprot_id: Q9FF53
---

# AtPIP2;4 (Arabidopsis thaliana Plasma Membrane Intrinsic Protein 2;4)

<div class="expr-badges"><span class="expr-badge expr-p-pastoris">P. pastoris</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9FF53">UniProt: Q9FF53</a>

<span class="expr-badge">Arabidopsis thaliana</span>

## Overview

AtPIP2;4 is a plasma membrane intrinsic protein (PIP) [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) from Arabidopsis thaliana. It belongs to the PIP2 subfamily of plant [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/), which form homotetramers at the plasma membrane and function as water and hydrogen peroxide (H2O2) channels. AtPIP2;4 shares the conserved [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) hourglass architecture with six transmembrane helices and two half-helices containing NPA motifs. The structure was determined at 3.7 Å resolution (PDB: 6QIM), revealing high structural similarity to SoPIP2;1 from spinach (75% sequence identity). Unlike SoPIP2;1, Cd2+ cation is not required to retain the closed conformation. AtPIP2;4 is an efficient transporter of both water and H2O2, with H2O2 transport capacity comparable to SoPIP2;1 and significantly higher than human [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/).


## Publications

### doi/10.1016##j.bbamem.2019.183065

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6qim">6QIM</a></td>
      <td>3.7</td>
      <td>P 63 22</td>
      <td>Truncated AtPIP2;4(28-279) with 8xHis-tag, expressed in Pichia pastoris, purified in LDAO/OG micelles</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (X-33Δ strain, aquaporin-deficient)
- **Construct**: Two constructs produced: Full-length AtPIP2;4-FL (1-291) and truncated AtPIP2;4(28-279), both with C-terminal TEV-8xHis tag. Codon-optimized gene, cloned into pPICZB vector.

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
      <td>Bead beating (12×30s with cooling)</td>
      <td>--</td>
      <td>Breaking buffer (50 mM potassium phosphate pH 7.5, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 2 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">Pmsf</a>) + --</td>
      <td>Glass beads (0.5 mm) used. Cell debris removed at 10,000g.</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td><a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">Ultracentrifugation</a> and <a href="/xray-mp-wiki/reagents/substrates/urea/">Urea</a> wash</td>
      <td>--</td>
      <td><a href="/xray-mp-wiki/reagents/substrates/urea/">Urea</a> buffer (4 M <a href="/xray-mp-wiki/reagents/substrates/urea/">Urea</a>, 5 mM Tris·HCl pH 9.5, 2 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 2 mM <a href="/xray-mp-wiki/reagents/additives/egta/">Egta</a>); Membrane wash buffer (20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8, 20 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 2 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">Pmsf</a>) + --</td>
      <td>Membranes collected at 200,000g for 90 min at 4°C.</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization screen</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8, 200 mM NaCl + 2% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> (n-Dodecyl-N,N-Dimethylamine-N-Oxide)</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> selected as most efficient detergent after screening CHAPS, <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, FC12, <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, MNG, NG, β-<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Immobilized metal affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose (Qiagen)</td>
      <td>Wash: 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 8.0, 200 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.4% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>, 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; Elution: 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.4% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> added before loading. 50 mg of AtPIP2;4-FL obtained from 90 g cells.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) for buffer exchange and polishing</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex200</a> Increase 10/300 GL (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 8.0, 200 mM NaCl + 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> (n-Octyl-β-D-Glucopyranoside) or 0.145% OGNPG (Octyl <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> Neopentyl Glycol)</td>
      <td>For crystallization, β-<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> and OGNPG gave monodisperse peaks for FL. For truncated variant, β-OG, <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> and <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> gave monodisperse peaks.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>AtPIP2;4(28-279) at 20 mg/mL in 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>1.5 M sodium formate, 0.05 M sodium <a href="/xray-mp-wiki/reagents/buffers/cacodylate/">Cacodylate</a> pH 5.5, 30% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 3% w/v 6-Aminohexanoic acid, 0.01 M Calcium chloride dihydrate</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Few days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Flash frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared after a few days. The tetramer shows a typical <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin</a> oligomer with four individual water pores. Two molecules in asymmetric unit. Data collected at ESRF beamline MASSIF-1 (ID30A-1). <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular replacement</a> with SoPIP2;1 (PDB: 4jc6).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qim">6QIM</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEE</span><span class="topo-inside">LRKWPLYRA</span><span class="topo-membrane">VIAEFVATLLFLYVSILTV</span><span class="topo-outside">IGYKAQTDATAGGVDCGGVGIL</span><span class="topo-membrane">GIAWAFGGMIFVLVYCTA</span><span class="topo-inside">GIS</span><span class="topo-unknown">GGHINPAVTVGLFL</span><span class="topo-inside">ARKVSLV</span><span class="topo-membrane">RTVLYIVAQCLGAICGCGFV</span><span class="topo-outside">KAFQS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SYYTRYGGGANELADGYNKG</span><span class="topo-membrane">TGLGAEIIGTFVLVYTVFSA</span><span class="topo-inside">TDPKRNARDSHVPVL</span><span class="topo-membrane">APLPIGFAVFMVHLATI</span><span class="topo-outside">PIT</span><span class="topo-unknown">GTGINPARSFGAAVI</span><span class="topo-outside">YNNEKAWDDQ</span><span class="topo-membrane">WIFWVGPMIGAAAAAFYH</span><span class="topo-inside">QF</span></span>
<span class="topo-ruler">       250         </span>
<span class="topo-line"><span class="topo-inside">ILRAAA</span><span class="topo-unknown">IKALGHHHHHHHH</span></span>
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
      <td>4</td>
      <td>12</td>
      <td>32</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>31</td>
      <td>41</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>53</td>
      <td>60</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>71</td>
      <td>82</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>74</td>
      <td>100</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>88</td>
      <td>103</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>89</td>
      <td>95</td>
      <td>117</td>
      <td>123</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>115</td>
      <td>124</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>140</td>
      <td>144</td>
      <td>168</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>160</td>
      <td>169</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>175</td>
      <td>189</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>192</td>
      <td>204</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>195</td>
      <td>221</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>210</td>
      <td>224</td>
      <td>238</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>220</td>
      <td>239</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>249</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>246</td>
      <td>267</td>
      <td>274</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qim">6QIM</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEE</span><span class="topo-inside">LRKWPLYRA</span><span class="topo-membrane">VIAEFVATLLFLYVSILT</span><span class="topo-outside">VIGYKAQTDATAGGVDCGGVGIL</span><span class="topo-membrane">GIAWAFGGMIFVLVYCTA</span><span class="topo-inside">GIS</span><span class="topo-unknown">GGHINPAVTVGLFL</span><span class="topo-inside">ARKVSLVRT</span><span class="topo-membrane">VLYIVAQCLGAICGCGFV</span><span class="topo-outside">KAFQS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SYYTRYGGGANELADGYNKG</span><span class="topo-membrane">TGLGAEIIGTFVLVYTVFSA</span><span class="topo-inside">TDPKRNARDSHVPVLA</span><span class="topo-membrane">PLPIGFAVFMVHLATI</span><span class="topo-outside">PIT</span><span class="topo-unknown">GTGINPARSFGAAVI</span><span class="topo-outside">YNNEKAWDDQ</span><span class="topo-membrane">WIFWVGPMIGAAAAAFYH</span><span class="topo-inside">QF</span></span>
<span class="topo-ruler">       250         </span>
<span class="topo-line"><span class="topo-inside">ILRAAAI</span><span class="topo-unknown">KALGHHHHHHHH</span></span>
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
      <td>4</td>
      <td>12</td>
      <td>32</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>30</td>
      <td>41</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>53</td>
      <td>59</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>71</td>
      <td>82</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>74</td>
      <td>100</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>88</td>
      <td>103</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>89</td>
      <td>97</td>
      <td>117</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>115</td>
      <td>126</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>140</td>
      <td>144</td>
      <td>168</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>160</td>
      <td>169</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>176</td>
      <td>189</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>192</td>
      <td>205</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>195</td>
      <td>221</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>210</td>
      <td>224</td>
      <td>238</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>220</td>
      <td>239</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>249</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>247</td>
      <td>267</td>
      <td>275</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qim">6QIM</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEE</span><span class="topo-inside">LRKWPLYRA</span><span class="topo-membrane">VIAEFVATLLFLYVSILTV</span><span class="topo-outside">IGYKAQTDATAGGVDCGGVGIL</span><span class="topo-membrane">GIAWAFGGMIFVLVYCTA</span><span class="topo-inside">GIS</span><span class="topo-unknown">GGHINPAVTVGLFL</span><span class="topo-inside">ARKVSLV</span><span class="topo-membrane">RTVLYIVAQCLGAICGCGFV</span><span class="topo-outside">KAFQS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SYYTRYGGGANELADGYNKG</span><span class="topo-membrane">TGLGAEIIGTFVLVYTVFSA</span><span class="topo-inside">TDPKRNARDSHVPVL</span><span class="topo-membrane">APLPIGFAVFMVHLATI</span><span class="topo-outside">PIT</span><span class="topo-unknown">GTGINPARSFGAAVI</span><span class="topo-outside">YNNEKAWDDQ</span><span class="topo-membrane">WIFWVGPMIGAAAAAFYH</span><span class="topo-inside">QF</span></span>
<span class="topo-ruler">       250         </span>
<span class="topo-line"><span class="topo-inside">ILRAAA</span><span class="topo-unknown">IKALGHHHHHHHH</span></span>
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
      <td>4</td>
      <td>12</td>
      <td>32</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>31</td>
      <td>41</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>53</td>
      <td>60</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>71</td>
      <td>82</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>74</td>
      <td>100</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>88</td>
      <td>103</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>89</td>
      <td>95</td>
      <td>117</td>
      <td>123</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>115</td>
      <td>124</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>140</td>
      <td>144</td>
      <td>168</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>160</td>
      <td>169</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>175</td>
      <td>189</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>192</td>
      <td>204</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>195</td>
      <td>221</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>210</td>
      <td>224</td>
      <td>238</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>220</td>
      <td>239</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>249</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>246</td>
      <td>267</td>
      <td>274</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qim">6QIM</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEE</span><span class="topo-inside">LRKWPLYRA</span><span class="topo-membrane">VIAEFVATLLFLYVSILT</span><span class="topo-outside">VIGYKAQTDATAGGVDCGGVGIL</span><span class="topo-membrane">GIAWAFGGMIFVLVYCTA</span><span class="topo-inside">GIS</span><span class="topo-unknown">GGHINPAVTVGLFL</span><span class="topo-inside">ARKVSLVRT</span><span class="topo-membrane">VLYIVAQCLGAICGCGFV</span><span class="topo-outside">KAFQS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SYYTRYGGGANELADGYNKG</span><span class="topo-membrane">TGLGAEIIGTFVLVYTVFSA</span><span class="topo-inside">TDPKRNARDSHVPVLA</span><span class="topo-membrane">PLPIGFAVFMVHLATI</span><span class="topo-outside">PIT</span><span class="topo-unknown">GTGINPARSFGAAVI</span><span class="topo-outside">YNNEKAWDDQ</span><span class="topo-membrane">WIFWVGPMIGAAAAAFYH</span><span class="topo-inside">QF</span></span>
<span class="topo-ruler">       250         </span>
<span class="topo-line"><span class="topo-inside">ILRAAAI</span><span class="topo-unknown">KALGHHHHHHHH</span></span>
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
      <td>4</td>
      <td>12</td>
      <td>32</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>30</td>
      <td>41</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>53</td>
      <td>59</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>71</td>
      <td>82</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>74</td>
      <td>100</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>88</td>
      <td>103</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>89</td>
      <td>97</td>
      <td>117</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>115</td>
      <td>126</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>140</td>
      <td>144</td>
      <td>168</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>160</td>
      <td>169</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>176</td>
      <td>189</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>192</td>
      <td>205</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>195</td>
      <td>221</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>210</td>
      <td>224</td>
      <td>238</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>220</td>
      <td>239</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>249</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>247</td>
      <td>267</td>
      <td>275</td>
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

### AtPIP2;4 is an efficient H2O2 transporter

AtPIP2;4 transports hydrogen peroxide efficiently, as demonstrated by yeast growth assay (most significant growth defect among 12 AtPIP homologues at 3 mM H2O2), DCF fluorescence assay, and a novel proteoliposome assay. The plant [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) (AtPIP2;4 and SoPIP2;1) are significantly more efficient at H2O2 transport than human [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/), despite comparable water transport efficiencies. The H2O2 transport is protein-specific and can be inhibited by [Mercury](/xray-mp-wiki/reagents/additives/mercury/) (tested for hAQP1, which has Cys189 in the selectivity filter; plant [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) have Thr at the corresponding position and are mercury-insensitive).

### Loop D conformation in AtPIP2;4 without divalent cation

The AtPIP2;4 structure reveals loop D in a conformation very similar to the closed conformation of SoPIP2;1, despite the absence of a Cd2+ cation. In SoPIP2;1, a divalent cation (Cd2+ in crystals, possibly Ca2+ in vivo) was critical for defining the closed structure by anchoring loop D. The observation that AtPIP2;4 adopts a similar closed conformation without the cation suggests variations in the molecular mechanisms for plant [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) regulation, with possible additional fine-tuning involving loop regions.

### Comparison of transport specificities across aquaporin homologues

The pore-lining residues of hAQP1, SoPIP2;1 and AtPIP2;4 are almost identical. The selectivity filter residues (F87, H216, T225, R231 in AtPIP2;4) show no obvious difference in pore diameter despite T225 being a cysteine in hAQP1. Differences in H2O2 transport efficiency between plant and human [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) cannot be explained by differences in the monomeric pore architecture. The structural determinants likely reside in the flexible loop regions outside the membrane core. Loop D, which is four residues shorter in hAQP1 and lacks the conserved Leu197 involved in PIP channel regulation, is a candidate for contributing to transport specificity differences.


## Cross-References

- <a href="/xray-mp-wiki/proteins/other-ion-channels/so-pip2-1/">SoPIP2;1 (Spinach Plasma Membrane Aquaporin)</a> — Highly homologous plant aquaporin (75% sequence identity) used as molecular replacement model and for comparative functional analysis
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aquaporin-z/">Aquaporin Z</a> — Related bacterial aquaporin for comparative structural analysis
- <a href="/xray-mp-wiki/methods/expression-systems/pichia-pastoris/">Pichia pastoris Expression System</a> — Expression system used for recombinant AtPIP2;4 production
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Method used for crystallization of AtPIP2;4
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO (n-Dodecyl-N,N-Dimethylamine-N-Oxide)</a> — Primary detergent for solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl-beta-D-glucopyranoside (OG)</a> — Detergent used for crystallization and final SEC buffer
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin Family</a> — AtPIP2;4 is a member of the aquaporin family
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp1/">AQP1</a> — Referenced in the context of AQP1
- <a href="/xray-mp-wiki/reagents/substrates/urea/">Urea</a> — Referenced in the context of Urea
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Referenced in the context of Tris
