---
title: "AtTIP2;1 - Arabidopsis thaliana Tonoplast Intrinsic Protein 2;1"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein]
sources: [doi/10.1371##journal.pbio.1002411]
verified: regex
uniprot_id: Q41951
---

# AtTIP2;1 - Arabidopsis thaliana Tonoplast Intrinsic Protein 2;1

<div class="expr-badges"><span class="expr-badge expr-p-pastoris">P. pastoris</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q41951">UniProt: Q41951</a>

<span class="expr-badge">Arabidopsis thaliana</span>

## Overview

AtTIP2;1 is an ammonia-permeable [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) (aquaammoniaporin) from the TIP
(Tonoplast Intrinsic Protein) subfamily of Arabidopsis thaliana. It facilitates
permeation of both water and ammonia across the vacuolar membrane. The
structure reveals an extended selectivity filter with five positions,
including a histidine (His 131) in loop C that directly participates in
substrate interactions, a unique feature among [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/). A water-filled side
pore beneath loop C is speculated to participate in deprotonating ammonium
ions, potentially increasing net ammonia permeation.


## Publications

### doi/10.1371##journal.pbio.1002411

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5i32">5I32</a></td>
      <td>1.18</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: Full-length AtTIP2;1 with N-terminal deca-His-tag and TEV cleavage site
- **Notes**: Up to 1.1 mg purified protein per g wet cells

**Purification:**

- **Expression system**: Pichia pastoris
- **Expression construct**: Full-length AtTIP2;1 with N-terminal deca-His-tag and TEV cleavage site

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
      <td>Urea wash of membranes</td>
      <td>Wash</td>
      <td>—</td>
      <td></td>
      <td>Membranes washed with <a href="/xray-mp-wiki/reagents/substrates/urea/">Urea</a> to remove peripheral proteins</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>10% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> (<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>)</td>
      <td>Membranes solubilized with <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
    </tr>
    <tr>
      <td>Nickel <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> wash + 0.05% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>—</td>
      <td>0.05% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging drop vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM magnesium/sodium <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate</a> pH 5.0, 28% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at Swiss Light Source beamline X06SA (PXI), wavelength 1.0 A</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5i32">5I32</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSHHHHHHHHHHDSNGIPTENLYFQ</span><span class="topo-inside">GAGVAFGSFDDSFSLASLRA</span><span class="topo-membrane">YLAEFISTLLFVFAGVGS</span><span class="topo-outside">AIAYAKLTSDAALDTPGLV</span><span class="topo-membrane">AIAVCHGFALFVAVAIGA</span><span class="topo-inside">NIS</span><span class="topo-unknown">GGHVNPAVTFGLAV</span><span class="topo-inside">GGQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ITV</span><span class="topo-membrane">ITGVFYWIAQLLGSTAACFLLKYV</span><span class="topo-outside">TGGLAVPTHSVAAGLGSI</span><span class="topo-membrane">EGVVMEIIITFALVYTVYATA</span><span class="topo-inside">ADPKKGSLGTI</span><span class="topo-membrane">APLAIGLIVGANILAAG</span><span class="topo-outside">PFS</span><span class="topo-unknown">GGSMNPARSFGPAVA</span><span class="topo-outside">AGDFSGH</span><span class="topo-membrane">W</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-membrane">VYWVGPLIGGGLAGLIY</span><span class="topo-inside">GNVFMG</span><span class="topo-unknown">SSEHVPLASADF</span></span>
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
      <td>26</td>
      <td>45</td>
      <td>1</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>21</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>82</td>
      <td>39</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>100</td>
      <td>58</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>103</td>
      <td>76</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>117</td>
      <td>79</td>
      <td>92</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>118</td>
      <td>123</td>
      <td>93</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>147</td>
      <td>99</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>165</td>
      <td>123</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>186</td>
      <td>141</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>197</td>
      <td>162</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>214</td>
      <td>173</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>217</td>
      <td>190</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>232</td>
      <td>193</td>
      <td>207</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>233</td>
      <td>239</td>
      <td>208</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>257</td>
      <td>215</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>263</td>
      <td>233</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5i32">5I32</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSHHHHHHHHHHDSNGIPTENLYFQ</span><span class="topo-inside">GAGVAFGSFDDSFSLASLRA</span><span class="topo-membrane">YLAEFISTLLFVFAGVGS</span><span class="topo-outside">AIAYAKLTSDAALDTPGLV</span><span class="topo-membrane">AIAVCHGFALFVAVAIGA</span><span class="topo-inside">NIS</span><span class="topo-unknown">GGHVNPAVTFGLAV</span><span class="topo-inside">GGQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ITV</span><span class="topo-membrane">ITGVFYWIAQLLGSTAACFLLKYV</span><span class="topo-outside">TGGLAVPTHSVAAGLGSI</span><span class="topo-membrane">EGVVMEIIITFALVYTVYATA</span><span class="topo-inside">ADPKKGSLGTI</span><span class="topo-membrane">APLAIGLIVGANILAAG</span><span class="topo-outside">PFS</span><span class="topo-unknown">GGSMNPARSFGPAVA</span><span class="topo-outside">AGDFSGH</span><span class="topo-membrane">W</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-membrane">VYWVGPLIGGGLAGLIY</span><span class="topo-inside">GNVFMG</span><span class="topo-unknown">SSEHVPLASADF</span></span>
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
      <td>26</td>
      <td>45</td>
      <td>1</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>21</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>82</td>
      <td>39</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>100</td>
      <td>58</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>103</td>
      <td>76</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>117</td>
      <td>79</td>
      <td>92</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>118</td>
      <td>123</td>
      <td>93</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>147</td>
      <td>99</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>165</td>
      <td>123</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>186</td>
      <td>141</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>197</td>
      <td>162</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>214</td>
      <td>173</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>217</td>
      <td>190</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>232</td>
      <td>193</td>
      <td>207</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>233</td>
      <td>239</td>
      <td>208</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>257</td>
      <td>215</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>263</td>
      <td>233</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5i32">5I32</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSHHHHHHHHHHDSNGIPTENLYFQ</span><span class="topo-inside">GAGVAFGSFDDSFSLASLRA</span><span class="topo-membrane">YLAEFISTLLFVFAGVGS</span><span class="topo-outside">AIAYAKLTSDAALDTPGLV</span><span class="topo-membrane">AIAVCHGFALFVAVAIGA</span><span class="topo-inside">NIS</span><span class="topo-unknown">GGHVNPAVTFGLAV</span><span class="topo-inside">GGQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ITV</span><span class="topo-membrane">ITGVFYWIAQLLGSTAACFLLKYV</span><span class="topo-outside">TGGLAVPTHSVAAGLGSI</span><span class="topo-membrane">EGVVMEIIITFALVYTVYATA</span><span class="topo-inside">ADPKKGSLGTI</span><span class="topo-membrane">APLAIGLIVGANILAAG</span><span class="topo-outside">PFS</span><span class="topo-unknown">GGSMNPARSFGPAVA</span><span class="topo-outside">AGDFSGH</span><span class="topo-membrane">W</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-membrane">VYWVGPLIGGGLAGLIY</span><span class="topo-inside">GNVFMG</span><span class="topo-unknown">SSEHVPLASADF</span></span>
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
      <td>26</td>
      <td>45</td>
      <td>1</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>21</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>82</td>
      <td>39</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>100</td>
      <td>58</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>103</td>
      <td>76</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>117</td>
      <td>79</td>
      <td>92</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>118</td>
      <td>123</td>
      <td>93</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>147</td>
      <td>99</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>165</td>
      <td>123</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>186</td>
      <td>141</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>197</td>
      <td>162</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>214</td>
      <td>173</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>217</td>
      <td>190</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>232</td>
      <td>193</td>
      <td>207</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>233</td>
      <td>239</td>
      <td>208</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>257</td>
      <td>215</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>263</td>
      <td>233</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5i32">5I32</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSHHHHHHHHHHDSNGIPTENLYFQ</span><span class="topo-inside">GAGVAFGSFDDSFSLASLRA</span><span class="topo-membrane">YLAEFISTLLFVFAGVGS</span><span class="topo-outside">AIAYAKLTSDAALDTPGLV</span><span class="topo-membrane">AIAVCHGFALFVAVAIGA</span><span class="topo-inside">NIS</span><span class="topo-unknown">GGHVNPAVTFGLAV</span><span class="topo-inside">GGQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ITV</span><span class="topo-membrane">ITGVFYWIAQLLGSTAACFLLKYV</span><span class="topo-outside">TGGLAVPTHSVAAGLGSI</span><span class="topo-membrane">EGVVMEIIITFALVYTVYATA</span><span class="topo-inside">ADPKKGSLGTI</span><span class="topo-membrane">APLAIGLIVGANILAAG</span><span class="topo-outside">PFS</span><span class="topo-unknown">GGSMNPARSFGPAVA</span><span class="topo-outside">AGDFSGH</span><span class="topo-membrane">W</span></span>
<span class="topo-ruler">       250       260       270     </span>
<span class="topo-line"><span class="topo-membrane">VYWVGPLIGGGLAGLIY</span><span class="topo-inside">GNVFMG</span><span class="topo-unknown">SSEHVPLASADF</span></span>
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
      <td>26</td>
      <td>45</td>
      <td>1</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>21</td>
      <td>38</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>82</td>
      <td>39</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>100</td>
      <td>58</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>103</td>
      <td>76</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>117</td>
      <td>79</td>
      <td>92</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>118</td>
      <td>123</td>
      <td>93</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>147</td>
      <td>99</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>165</td>
      <td>123</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>186</td>
      <td>141</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>197</td>
      <td>162</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>214</td>
      <td>173</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>217</td>
      <td>190</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>232</td>
      <td>193</td>
      <td>207</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>233</td>
      <td>239</td>
      <td>208</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>257</td>
      <td>215</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>263</td>
      <td>233</td>
      <td>238</td>
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

### Extended selectivity filter

AtTIP2;1 reveals an extended selectivity filter with five positions
(H2P, LCP, H5P, LEP, HEP) rather than the classical four-position
aromatic/arginine filter of water-specific [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/). The conserved
arginine (Arg 200) adopts a unique unpredicted position, stabilized by
interactions with His 63 (H2P) and His 131 (LCP).

### Ammonia permeability determinants

The relatively wide pore and polar nature of the selectivity filter
explain ammonia permeability. A histidine at position LCP in loop C
(His 131) directly participates in substrate interactions, extending
the selectivity filter.

### Water-filled side pore

A water-filled side pore beneath loop C is speculated to facilitate
deprotonation of ammonium ions via a Grotthuss-type proton shuttle
mechanism involving His 131, potentially increasing net ammonia
permeation.

### Gain-of-function in human AQP1

Mutation of the four deviating selectivity filter residues in
water-specific human [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/) to corresponding TIP2 residues (F56H,
N127H, H180I, C189G) converted it into an AtTIP2;1-like ammonia
channel, demonstrating the sufficiency of the extended selectivity
filter determinants.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin Family</a> — AtTIP2;1 is a member of the aquaporin superfamily, specifically the TIP subfamily
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/extended-selectivity-filter/">Extended Selectivity Filter</a> — AtTIP2;1 defines the five-position extended selectivity filter in aquaporins
- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl-beta-D-glucoside (OG)</a> — OG used for solubilization of AtTIP2;1 from P. pastoris membranes
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">Polyethylene Glycol 400 (PEG400)</a> — PEG 400 used as crystallization precipitant at 28% (v/v)
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Imidazole used at 100 mM in Ni-NTA wash step
- <a href="/xray-mp-wiki/reagents/substrates/urea/">Urea</a> — Referenced in the context of Urea
- <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> — Referenced in the context of OG
- <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate</a> — Referenced in the context of Acetate
- <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> — Referenced in the context of Peg
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp1/">AQP1</a> — Referenced in the context of AQP1
