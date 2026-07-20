---
title: "OsNIP2;1 (Silicon Transporter Lsi1 from Oryza sativa)"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2021.167226]
verified: agent
uniprot_id: Q6Z2T3
---

# OsNIP2;1 (Silicon Transporter Lsi1 from Oryza sativa)

<div class="expr-badges"><span class="expr-badge expr-s-cerevisiae">S. cerevisiae</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q6Z2T3">UniProt: Q6Z2T3</a>

<span class="expr-badge">Oryza sativa subsp. japonica</span>

## Overview

OsNIP2;1 (Nodulin26-like Intrinsic Protein 2;1) is a silicon transporter from the rice plant Oryza sativa, also known as Lsi1 (low silicon rice 1). It belongs to the NIP (Nodulin26-like Intrinsic Protein) subfamily of aquaporins, also termed metalloid porins. OsNIP2;1 mediates the uptake of silicic acid across root cell plasma membranes, a critical step for silicon accumulation in rice and other grasses. The protein forms a tetrameric assembly with each protomer containing six transmembrane helices and two half-helices forming NPA motifs. The structure reveals a novel five-residue selectivity filter (TGSGR) and a channel gating mechanism involving cytoplasmic loop D.


## Publications

### doi/10.1016##j.jmb.2021.167226

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7nl4">7NL4</a></td>
      <td>2.6 A</td>
      <td>P1</td>
      <td>Truncated OsNIP2;1, residues 38-264, N4Q/N13Q/N26Q glycosylation mutants, C-terminal 6xHis-tag</td>
      <td>None (apo)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7nl4">7NL4</a></td>
      <td>3.8 A</td>
      <td>C2</td>
      <td>Full-length OsNIP2;1, N4Q/N13Q/N26Q glycosylation mutants, C-terminal 6xHis-tag</td>
      <td>None (apo)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae W303 delta pep4 strain
- **Construct**: Synthetic gene optimized for yeast expression; hexa-histidine tag at C terminus; N-terminal glycosylation sites removed (N4Q/N13Q/N26Q); cloned via BamHI and XhoI into 83v vector; expressed by galactose induction (YP medium with 1.5% galactose) at 30 C for 16-20 hours

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
      <td>Cell disruption (cell disrupter at 35-37 kpsi)</td>
      <td>--</td>
      <td>TSB buffer (20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a>, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, pH 8) with 5 mM <a href="/xray-mp-wiki/reagents/additives/edta">EDTA</a> + --</td>
      <td>Cells resuspended in TSB buffer with <a href="/xray-mp-wiki/reagents/additives/edta">EDTA</a>; lysed by 1-2 passes through cell disrupter; membranes collected by centrifugation at 200,000g for 90 min</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane solubilization</td>
      <td>--</td>
      <td>TSB buffer (20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a>, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, pH 8) with Complete <a href="/xray-mp-wiki/reagents/additives/edta">EDTA</a>-free protease inhibitor + 1:1 (w/w) mixture of <a href="/xray-mp-wiki/reagents/detergents/ddm">dodecyl-beta-D-maltoside ([DDM</a>)] and <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (total 1% w/v detergent)</td>
      <td>Homogenization in TSB with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> mixture; stirred at 4 C for 1 hr or overnight; 1 g total detergent per 2 liters of cells</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>--</td>
      <td>TSB buffer with <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> + <a href="/xray-mp-wiki/reagents/detergents/dm">'[DM</a>']</td>
      <td>Centrifuged membrane extract loaded onto <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) resin</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Truncated OsNIP2;1 (residues 38-264) at ~5 mg/ml in <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>MemGold H11 hit condition: 1 mM <a href="/xray-mp-wiki/reagents/additives/cadmium-chloride/">cadmium chloride</a>, 30 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">magnesium chloride</a>, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/mes">MES</a> (pH 6.5), 30% <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> 400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Block-shaped crystals in space group P1. Data collected at beamline I24 at Diamond Light Source. Solved by molecular replacement using AqpM from Methanothermobacter marburgensis (PDB 2EVU) as search model. Two tetramers per asymmetric unit. Cadmium ions bridge tetramers via cytoplasmic faces.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7nl4">7NL4</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AIADFFP</span><span class="topo-inside">PHLLKK</span><span class="topo-membrane">VVSEVVATFLLVFMTCGA</span><span class="topo-outside">AGISGSDLSRISQL</span><span class="topo-membrane">GQSIAGGLIVTVMIYAVG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHMNPAVTLAFAV</span><span class="topo-inside">FRHFPWIQV</span><span class="topo-membrane">PFYWAAQFTGAICASFVL</span><span class="topo-outside">KAVIHPVDVIGTT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       </span>
<span class="topo-line"><span class="topo-outside">TPVGPHWHS</span><span class="topo-membrane">LVVEVIVTFNMMFVTLAV</span><span class="topo-inside">ATDTRAVGE</span><span class="topo-membrane">LAGLAVGSAVCITSIFAG</span><span class="topo-outside">AISGG</span><span class="topo-unknown">SMNPARTLGP</span><span class="topo-outside">ALASNKFDGL</span><span class="topo-membrane">WIYFLGPVMGTLSGAWTY</span><span class="topo-inside">TFIRFE</span><span class="topo-unknown">DTPK</span></span>
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
      <td>8</td>
      <td>13</td>
      <td>45</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>31</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>45</td>
      <td>69</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>83</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>66</td>
      <td>101</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>80</td>
      <td>104</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>118</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>107</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>129</td>
      <td>145</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>147</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>156</td>
      <td>185</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>174</td>
      <td>194</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>179</td>
      <td>212</td>
      <td>216</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>189</td>
      <td>217</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>190</td>
      <td>199</td>
      <td>227</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>217</td>
      <td>237</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>223</td>
      <td>255</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7nl4">7NL4</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AIADFFP</span><span class="topo-inside">PHLLKK</span><span class="topo-membrane">VVSEVVATFLLVFMTCGA</span><span class="topo-outside">AGISGSDLSRISQL</span><span class="topo-membrane">GQSIAGGLIVTVMIYAVG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHMNPAVTLAFAV</span><span class="topo-inside">FRHFPWIQV</span><span class="topo-membrane">PFYWAAQFTGAICASFVL</span><span class="topo-outside">KAVIHPVDVIGTT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       </span>
<span class="topo-line"><span class="topo-outside">TPVGPHWHS</span><span class="topo-membrane">LVVEVIVTFNMMFVTLAV</span><span class="topo-inside">ATDTRAVGE</span><span class="topo-membrane">LAGLAVGSAVCITSIFAG</span><span class="topo-outside">AISGG</span><span class="topo-unknown">SMNPARTLGP</span><span class="topo-outside">ALASNKFDGL</span><span class="topo-membrane">WIYFLGPVMGTLSGAWTY</span><span class="topo-inside">TFIRFE</span><span class="topo-unknown">DTPK</span></span>
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
      <td>8</td>
      <td>13</td>
      <td>45</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>31</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>45</td>
      <td>69</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>83</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>66</td>
      <td>101</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>80</td>
      <td>104</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>118</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>107</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>129</td>
      <td>145</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>147</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>156</td>
      <td>185</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>174</td>
      <td>194</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>179</td>
      <td>212</td>
      <td>216</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>189</td>
      <td>217</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>190</td>
      <td>199</td>
      <td>227</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>217</td>
      <td>237</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>223</td>
      <td>255</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7nl4">7NL4</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AIADFFP</span><span class="topo-inside">PHLLKK</span><span class="topo-membrane">VVSEVVATFLLVFMTCGA</span><span class="topo-outside">AGISGSDLSRISQL</span><span class="topo-membrane">GQSIAGGLIVTVMIYAVG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHMNPAVTLAFAV</span><span class="topo-inside">FRHFPWIQ</span><span class="topo-membrane">VPFYWAAQFTGAICASFVL</span><span class="topo-outside">KAVIHPVDVIGTT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       </span>
<span class="topo-line"><span class="topo-outside">TPVGPHWHS</span><span class="topo-membrane">LVVEVIVTFNMMFVTLAV</span><span class="topo-inside">ATDTRAVGE</span><span class="topo-membrane">LAGLAVGSAVCITSIFAG</span><span class="topo-outside">AIS</span><span class="topo-unknown">GGSMNPARTLGP</span><span class="topo-outside">ALASNKFDGL</span><span class="topo-membrane">WIYFLGPVMGTLSGAWTY</span><span class="topo-inside">TFIR</span><span class="topo-unknown">FEDTPK</span></span>
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
      <td>8</td>
      <td>13</td>
      <td>45</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>31</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>45</td>
      <td>69</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>83</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>66</td>
      <td>101</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>80</td>
      <td>104</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>88</td>
      <td>118</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>107</td>
      <td>126</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>129</td>
      <td>145</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>147</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>156</td>
      <td>185</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>174</td>
      <td>194</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>177</td>
      <td>212</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>189</td>
      <td>215</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>190</td>
      <td>199</td>
      <td>227</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>217</td>
      <td>237</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>221</td>
      <td>255</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7nl4">7NL4</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AIADFFP</span><span class="topo-inside">PHLLKKV</span><span class="topo-membrane">VSEVVATFLLVFMTCGA</span><span class="topo-outside">AGISGSDLSRISQL</span><span class="topo-membrane">GQSIAGGLIVTVMIYAVG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHMNPAVTLAFAV</span><span class="topo-inside">FRHFPWIQ</span><span class="topo-membrane">VPFYWAAQFTGAICASFVL</span><span class="topo-outside">KAVIHPVDVIGTT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       </span>
<span class="topo-line"><span class="topo-outside">TPVGPHWHS</span><span class="topo-membrane">LVVEVIVTFNMMFVTLAV</span><span class="topo-inside">ATDTRAVGE</span><span class="topo-membrane">LAGLAVGSAVCITSIFAG</span><span class="topo-outside">AIS</span><span class="topo-unknown">GGSMNPARTLGPAL</span><span class="topo-outside">ASNKFDGL</span><span class="topo-membrane">WIYFLGPVMGTLSGAWTY</span><span class="topo-inside">TFIRFE</span><span class="topo-unknown">DTPK</span></span>
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
      <td>8</td>
      <td>14</td>
      <td>45</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>31</td>
      <td>52</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>45</td>
      <td>69</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>83</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>66</td>
      <td>101</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>80</td>
      <td>104</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>88</td>
      <td>118</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>107</td>
      <td>126</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>129</td>
      <td>145</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>147</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>156</td>
      <td>185</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>174</td>
      <td>194</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>177</td>
      <td>212</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>191</td>
      <td>215</td>
      <td>228</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>199</td>
      <td>229</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>217</td>
      <td>237</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>223</td>
      <td>255</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7nl4">7NL4</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AIADFFP</span><span class="topo-inside">PHLLKK</span><span class="topo-membrane">VVSEVVATFLLVFMTCGA</span><span class="topo-outside">AGISGSDLSRISQL</span><span class="topo-membrane">GQSIAGGLIVTVMIYAVG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHMNPAVTLAFAV</span><span class="topo-inside">FRHFPWIQV</span><span class="topo-membrane">PFYWAAQFTGAICASFVL</span><span class="topo-outside">KAVIHPVDVIGTT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       </span>
<span class="topo-line"><span class="topo-outside">TPVGPHWHS</span><span class="topo-membrane">LVVEVIVTFNMMFVTLAV</span><span class="topo-inside">ATDTRAVGE</span><span class="topo-membrane">LAGLAVGSAVCITSIFAG</span><span class="topo-outside">AISGG</span><span class="topo-unknown">SMNPARTLGP</span><span class="topo-outside">ALASNKFDGL</span><span class="topo-membrane">WIYFLGPVMGTLSGAWTY</span><span class="topo-inside">TFIRFE</span><span class="topo-unknown">DTPK</span></span>
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
      <td>8</td>
      <td>13</td>
      <td>45</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>31</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>45</td>
      <td>69</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>83</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>66</td>
      <td>101</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>80</td>
      <td>104</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>118</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>107</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>129</td>
      <td>145</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>147</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>156</td>
      <td>185</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>174</td>
      <td>194</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>179</td>
      <td>212</td>
      <td>216</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>189</td>
      <td>217</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>190</td>
      <td>199</td>
      <td>227</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>217</td>
      <td>237</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>223</td>
      <td>255</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7nl4">7NL4</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AIADFFP</span><span class="topo-inside">PHLLKK</span><span class="topo-membrane">VVSEVVATFLLVFMTCGA</span><span class="topo-outside">AGISGSDLSRISQL</span><span class="topo-membrane">GQSIAGGLIVTVMIYAVG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHMNPAVTLAFAV</span><span class="topo-inside">FRHFPWIQV</span><span class="topo-membrane">PFYWAAQFTGAICASFVL</span><span class="topo-outside">KAVIHPVDVIGTT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       </span>
<span class="topo-line"><span class="topo-outside">TPVGPHWHS</span><span class="topo-membrane">LVVEVIVTFNMMFVTLAV</span><span class="topo-inside">ATDTRAVGE</span><span class="topo-membrane">LAGLAVGSAVCITSIFAG</span><span class="topo-outside">AISGG</span><span class="topo-unknown">SMNPARTLGP</span><span class="topo-outside">ALASNKFDGL</span><span class="topo-membrane">WIYFLGPVMGTLSGAWTY</span><span class="topo-inside">TFIRFE</span><span class="topo-unknown">DTPK</span></span>
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
      <td>8</td>
      <td>13</td>
      <td>45</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>31</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>45</td>
      <td>69</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>83</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>66</td>
      <td>101</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>80</td>
      <td>104</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>118</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>107</td>
      <td>127</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>129</td>
      <td>145</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>147</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>156</td>
      <td>185</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>174</td>
      <td>194</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>179</td>
      <td>212</td>
      <td>216</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>189</td>
      <td>217</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>190</td>
      <td>199</td>
      <td>227</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>217</td>
      <td>237</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>223</td>
      <td>255</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7nl4">7NL4</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AIADFFP</span><span class="topo-inside">PHLLKK</span><span class="topo-membrane">VVSEVVATFLLVFMTCGA</span><span class="topo-outside">AGISGSDLSRISQL</span><span class="topo-membrane">GQSIAGGLIVTVMIYAVG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHMNPAVTLAFAV</span><span class="topo-inside">FRHFPWIQ</span><span class="topo-membrane">VPFYWAAQFTGAICASFVL</span><span class="topo-outside">KAVIHPVDVIGTT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       </span>
<span class="topo-line"><span class="topo-outside">TPVGPHWHS</span><span class="topo-membrane">LVVEVIVTFNMMFVTLAV</span><span class="topo-inside">ATDTRAVGE</span><span class="topo-membrane">LAGLAVGSAVCITSIFAG</span><span class="topo-outside">AIS</span><span class="topo-unknown">GGSMNPARTLGP</span><span class="topo-outside">ALASNKFDGL</span><span class="topo-membrane">WIYFLGPVMGTLSGAWTY</span><span class="topo-inside">TFIR</span><span class="topo-unknown">FEDTPK</span></span>
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
      <td>8</td>
      <td>13</td>
      <td>45</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>31</td>
      <td>51</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>45</td>
      <td>69</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>83</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>66</td>
      <td>101</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>80</td>
      <td>104</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>88</td>
      <td>118</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>107</td>
      <td>126</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>129</td>
      <td>145</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>147</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>156</td>
      <td>185</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>174</td>
      <td>194</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>177</td>
      <td>212</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>189</td>
      <td>215</td>
      <td>226</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>190</td>
      <td>199</td>
      <td>227</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>217</td>
      <td>237</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>221</td>
      <td>255</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7nl4">7NL4</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AIADFFP</span><span class="topo-inside">PHLLKKV</span><span class="topo-membrane">VSEVVATFLLVFMTCGA</span><span class="topo-outside">AGISGSDLSRISQL</span><span class="topo-membrane">GQSIAGGLIVTVMIYAVG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHMNPAVTLAFAV</span><span class="topo-inside">FRHFPWIQ</span><span class="topo-membrane">VPFYWAAQFTGAICASFVL</span><span class="topo-outside">KAVIHPVDVIGTT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       </span>
<span class="topo-line"><span class="topo-outside">TPVGPHWHS</span><span class="topo-membrane">LVVEVIVTFNMMFVTLAV</span><span class="topo-inside">ATDTRAVGE</span><span class="topo-membrane">LAGLAVGSAVCITSIFAG</span><span class="topo-outside">AIS</span><span class="topo-unknown">GGSMNPARTLGPAL</span><span class="topo-outside">ASNKFDGL</span><span class="topo-membrane">WIYFLGPVMGTLSGAWTY</span><span class="topo-inside">TFIRFE</span><span class="topo-unknown">DTPK</span></span>
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
      <td>8</td>
      <td>14</td>
      <td>45</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>31</td>
      <td>52</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>45</td>
      <td>69</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>83</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>66</td>
      <td>101</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>80</td>
      <td>104</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>88</td>
      <td>118</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>107</td>
      <td>126</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>129</td>
      <td>145</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>147</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>156</td>
      <td>185</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>174</td>
      <td>194</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>177</td>
      <td>212</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>191</td>
      <td>215</td>
      <td>228</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>199</td>
      <td>229</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>217</td>
      <td>237</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>223</td>
      <td>255</td>
      <td>260</td>
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

### Novel five-residue selectivity filter (TGSGR)

The extracellular mouth of OsNIP2;1 contains a five-residue selectivity filter TGSGR, which is wider than the canonical four-residue SF of conventional aquaporins. The fifth residue, Thr65, is located at the extracellular end and is occluded in most other AQP/AQGP structures by an aromatic residue. The SF contains four oxygen atoms lining the channel, providing multiple hydrogen bond donor and acceptor groups for the four hydroxyl groups of translocating silicic acid. The Arg residue in the SF forms a hydrogen bond with Gly155 in extracellular loop C, constraining the Arg sidechain in a substrate-permissive position. A precise spacing of 108 residues between the NPA motifs is crucial for Si selectivity, as it positions Gly155 to maintain this critical Arg-loop C interaction.

### Channel gating by cytoplasmic loop D

The OsNIP2;1 channel is closed in the crystal structure by cytoplasmic loop D (residues 185-ATDTRA-191). Equilibrium MD simulations in a [POPC](/xray-mp-wiki/reagents/lipids/popc) bilayer show that the channel opens in solution: three independent 0.5 microsecond simulations show a pronounced shift of up to 15 A for the Arg189 side chain, opening the channel. 10 out of 12 monomers showed partial or complete channel opening, suggesting the closed conformation was selected by crystallization. The closed channels in MD simulations are still more open than the crystal structure per HOLE analysis. Channel opening may require phosphorylation of residues such as Thr186 or Thr188 in loop D, though no phosphorylation was detected by mass spectrometry.

### Silicic acid translocation mechanism

MD simulations reveal spontaneous silicic acid uptake and export through OsNIP2;1. Translocating silicic acid molecules form hydrogen bonds with all SF residues including Thr65, with Ser207 appearing especially important. The SF region combined with NPA1 motif provides the largest permeation barrier. Residence times in SF, NPA1, and NPA2 regions were 16.0 ns, 9.9 ns, and 8.4 ns from steered MD, respectively. Silicic acid (diameter 6 +/- 0.5 A) is larger than most of the channel per HOLE analysis, but non-spherical geometry allows permeation without hydration waters. The molecule rotates during passage, with hydroxyl hydrogens pointing away from NPA asparagine side chains at the NPA region. Transport appears bidirectional in the absence of a gradient.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin Family</a> — OsNIP2;1 is a member of the NIP subfamily of aquaporins (metalloid porins)
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Detergent used for membrane solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-Maltopyranoside (DDM)</a> — Detergent used in solubilization mixture with DM (1:1 w/w)
- <a href="/xray-mp-wiki/reagents/detergents/dmng/">Decyl Maltose Neopentyl Glycol (DMng)</a> — Detergent in which OsNIP2;1 behaves well for crystallization
- <a href="/xray-mp-wiki/reagents/additives/cadmium-chloride/">Cadmium Chloride</a> — Used in crystallization reservoir; bridges tetramers via cytoplasmic faces
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES Buffer</a> — Buffer in crystallization reservoir (0.1 M, pH 6.5)
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol) 400</a> — Crystallization precipitant (30% w/v)
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a> — Crystallization additive (30 mM)
- <a href="/xray-mp-wiki/reagents/additives/edta">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a> — Buffer component in purification or crystallization
