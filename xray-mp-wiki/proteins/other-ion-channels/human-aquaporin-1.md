---
title: "Human Aquaporin 1 (hAQP1)"
created: 2026-06-11
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1107##s2053230x14024558]
verified: agent
uniprot_id: P29972
---

# Human Aquaporin 1 (hAQP1)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P29972">UniProt: P29972</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) 1 (hAQP1) is the archetypal water-selective channel from the
[Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/), originally discovered in red blood cells and renal proximal
tubules. It forms homotetrameric channels that transport water bidirectionally
in response to osmotic gradients, strictly excluding ions including protons.
hAQP1 is a key factor in cell migration and angiogenesis and constitutes a
possible target for anticancer compounds and glaucoma treatment. A
preliminary crystallographic analysis at 3.28 A resolution was obtained from
protein expressed in Sf9 insect cells (the first recombinant hAQP1
structure). Crystals belong to the tetragonal space group I422 with
unit-cell parameters a = b = 89.28, c = 174.9 A and one monomer per
asymmetric unit; the biological tetramer is generated via the
crystallographic fourfold axis. This extends previous electron
crystallographic studies of hAQP1 from human red blood cells which were
limited to approximately 3.8 A resolution. A 2.2 A crystal structure of the
closely related bovine [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) 1 (bAQP1, PDB 1j4n) had previously been
solved from bovine red blood cells.


## Publications

### doi/10.1107/S2053230X14024558

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4csk">4CSK</a></td>
      <td>3.28</td>
      <td>I422</td>
      <td>Full-length human <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp1/">AQP1</a> (residues 1-269) with N-terminal 6xHis tag and TEV cleavage site, expressed in Sf9 insect cells</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 insect cells (baculovirus expression system)
- **Construct**: hAQP1 gene cloned into pFB-Lic-Bse vector with N-terminal 6xHis tag and TEV protease cleavage site
- **Notes**: Early passage virus (P0 amplified to P2). MOI 2-3, 27 C, 56 h, 140 rpm. 21 log-phase culture (3x10^6 cells/mL).

**Purification:**

- **Expression system**: S. frugiperda Sf9
- **Expression construct**: 6xHis-tagged hAQP1 with TEV cleavage site
- **Tag info**: N-terminal 6xHis tag

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
      <td>Cell harvest</td>
      <td>Centrifugation</td>
      <td>—</td>
      <td></td>
      <td>1500g for 30 min; pellet washed twice with PBS</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Sonication</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8, 300 mM NaCl, 2 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, cOmplete protease inhibitor cocktail, benzonase, 2% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
      <td>10 min sonication</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Solubilization</td>
      <td>—</td>
      <td>2% n-octyl-beta-D-glucopyranoside (<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>)</td>
      <td>Insoluble material removed by centrifugation</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>His-tagged hAQP1 purified by <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>—</td>
      <td></td>
      <td>hAQP1 elutes at 72 mL corresponding to homotetramer</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified tetrameric hAQP1 in OG

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (hanging drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified hAQP1 tetramer in OG</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K (room temperature)</td>
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
      <td>Tetragonal-shaped crystals. Anisotropic diffraction - strong to 3.3 A along c*, weak beyond 6 A in perpendicular directions. Significant diffuse scattering observed. Space group I422. Data collected at PXIII, SLS-PSI, PILATUS 2M detector, 110 K, 410 mm crystal-to-detector distance. 120 total rotation, 1 per image, 4 s exposure per image.</td>
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
      <td>hanging-drop</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>293 K</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4csk">4CSK</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHSSGVDLGTENLYFQSMA</span><span class="topo-inside">SEFKKKLFWRA</span><span class="topo-membrane">VVAEFLATTLFVFISIGSA</span><span class="topo-outside">LGFKYPVGNNQTAVQDN</span><span class="topo-membrane">VKVSLAFGLSIATLAQSVG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHLNPAVTLGLLL</span><span class="topo-inside">SCQISIF</span><span class="topo-membrane">RALMY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IIAQCVGAIVATAIL</span><span class="topo-outside">SGITSSLTGNSLGRNDLADGVNSGQ</span><span class="topo-membrane">GLGIEIIGTLQLVLCVLAT</span><span class="topo-inside">TDRRRRDLGG</span><span class="topo-membrane">SAPLAIGLSVALGHLLAI</span><span class="topo-outside">DYTG</span><span class="topo-unknown">CGINPARSFGSAVI</span><span class="topo-outside">THNFSNH</span><span class="topo-membrane">WIFWVGPF</span></span>
<span class="topo-ruler">       250       260       270       280       290  </span>
<span class="topo-line"><span class="topo-membrane">IGGALAVLIY</span><span class="topo-inside">DFILAPRS</span><span class="topo-unknown">SDLTDRVKVWTSGQVEEYDLDADDINSRVEMKPK</span></span>
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
      <td>36</td>
      <td>3</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>55</td>
      <td>14</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>72</td>
      <td>33</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>91</td>
      <td>50</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>94</td>
      <td>69</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>108</td>
      <td>72</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>109</td>
      <td>115</td>
      <td>86</td>
      <td>92</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>135</td>
      <td>93</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>160</td>
      <td>113</td>
      <td>137</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>179</td>
      <td>138</td>
      <td>156</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>189</td>
      <td>157</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>207</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>185</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>225</td>
      <td>189</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>232</td>
      <td>203</td>
      <td>209</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>250</td>
      <td>210</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>258</td>
      <td>228</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4csk">4CSK</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHSSGVDLGTENLYFQSMA</span><span class="topo-inside">SEFKKKLFWRA</span><span class="topo-membrane">VVAEFLATTLFVFISIGSA</span><span class="topo-outside">LGFKYPVGNNQTAVQDN</span><span class="topo-membrane">VKVSLAFGLSIATLAQSVG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHLNPAVTLGLLL</span><span class="topo-inside">SCQISIF</span><span class="topo-membrane">RALMY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IIAQCVGAIVATAIL</span><span class="topo-outside">SGITSSLTGNSLGRNDLADGVNSGQ</span><span class="topo-membrane">GLGIEIIGTLQLVLCVLAT</span><span class="topo-inside">TDRRRRDLGG</span><span class="topo-membrane">SAPLAIGLSVALGHLLAI</span><span class="topo-outside">DYTG</span><span class="topo-unknown">CGINPARSFGSAVI</span><span class="topo-outside">THNFSNH</span><span class="topo-membrane">WIFWVGPF</span></span>
<span class="topo-ruler">       250       260       270       280       290  </span>
<span class="topo-line"><span class="topo-membrane">IGGALAVLIY</span><span class="topo-inside">DFILAPRS</span><span class="topo-unknown">SDLTDRVKVWTSGQVEEYDLDADDINSRVEMKPK</span></span>
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
      <td>36</td>
      <td>3</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>55</td>
      <td>14</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>72</td>
      <td>33</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>91</td>
      <td>50</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>94</td>
      <td>69</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>108</td>
      <td>72</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>109</td>
      <td>115</td>
      <td>86</td>
      <td>92</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>135</td>
      <td>93</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>160</td>
      <td>113</td>
      <td>137</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>179</td>
      <td>138</td>
      <td>156</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>189</td>
      <td>157</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>207</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>185</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>225</td>
      <td>189</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>232</td>
      <td>203</td>
      <td>209</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>250</td>
      <td>210</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>258</td>
      <td>228</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4csk">4CSK</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHSSGVDLGTENLYFQSMA</span><span class="topo-inside">SEFKKKLFWRA</span><span class="topo-membrane">VVAEFLATTLFVFISIGSA</span><span class="topo-outside">LGFKYPVGNNQTAVQDN</span><span class="topo-membrane">VKVSLAFGLSIATLAQSVG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHLNPAVTLGLLL</span><span class="topo-inside">SCQISIF</span><span class="topo-membrane">RALMY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IIAQCVGAIVATAIL</span><span class="topo-outside">SGITSSLTGNSLGRNDLADGVNSGQ</span><span class="topo-membrane">GLGIEIIGTLQLVLCVLAT</span><span class="topo-inside">TDRRRRDLGG</span><span class="topo-membrane">SAPLAIGLSVALGHLLAI</span><span class="topo-outside">DYTG</span><span class="topo-unknown">CGINPARSFGSAVI</span><span class="topo-outside">THNFSNH</span><span class="topo-membrane">WIFWVGPF</span></span>
<span class="topo-ruler">       250       260       270       280       290  </span>
<span class="topo-line"><span class="topo-membrane">IGGALAVLIY</span><span class="topo-inside">DFILAPRS</span><span class="topo-unknown">SDLTDRVKVWTSGQVEEYDLDADDINSRVEMKPK</span></span>
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
      <td>36</td>
      <td>3</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>55</td>
      <td>14</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>72</td>
      <td>33</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>91</td>
      <td>50</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>94</td>
      <td>69</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>108</td>
      <td>72</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>109</td>
      <td>115</td>
      <td>86</td>
      <td>92</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>135</td>
      <td>93</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>160</td>
      <td>113</td>
      <td>137</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>179</td>
      <td>138</td>
      <td>156</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>189</td>
      <td>157</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>207</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>185</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>225</td>
      <td>189</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>232</td>
      <td>203</td>
      <td>209</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>250</td>
      <td>210</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>258</td>
      <td>228</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4csk">4CSK</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGHHHHHHSSGVDLGTENLYFQSMA</span><span class="topo-inside">SEFKKKLFWRA</span><span class="topo-membrane">VVAEFLATTLFVFISIGSA</span><span class="topo-outside">LGFKYPVGNNQTAVQDN</span><span class="topo-membrane">VKVSLAFGLSIATLAQSVG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHLNPAVTLGLLL</span><span class="topo-inside">SCQISIF</span><span class="topo-membrane">RALMY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IIAQCVGAIVATAIL</span><span class="topo-outside">SGITSSLTGNSLGRNDLADGVNSGQ</span><span class="topo-membrane">GLGIEIIGTLQLVLCVLAT</span><span class="topo-inside">TDRRRRDLGG</span><span class="topo-membrane">SAPLAIGLSVALGHLLAI</span><span class="topo-outside">DYTG</span><span class="topo-unknown">CGINPARSFGSAVI</span><span class="topo-outside">THNFSNH</span><span class="topo-membrane">WIFWVGPF</span></span>
<span class="topo-ruler">       250       260       270       280       290  </span>
<span class="topo-line"><span class="topo-membrane">IGGALAVLIY</span><span class="topo-inside">DFILAPRS</span><span class="topo-unknown">SDLTDRVKVWTSGQVEEYDLDADDINSRVEMKPK</span></span>
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
      <td>36</td>
      <td>3</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>55</td>
      <td>14</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>72</td>
      <td>33</td>
      <td>49</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>91</td>
      <td>50</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>94</td>
      <td>69</td>
      <td>71</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>108</td>
      <td>72</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>109</td>
      <td>115</td>
      <td>86</td>
      <td>92</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>135</td>
      <td>93</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>160</td>
      <td>113</td>
      <td>137</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>179</td>
      <td>138</td>
      <td>156</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>189</td>
      <td>157</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>207</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>211</td>
      <td>185</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>225</td>
      <td>189</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>226</td>
      <td>232</td>
      <td>203</td>
      <td>209</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>250</td>
      <td>210</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>258</td>
      <td>228</td>
      <td>235</td>
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

### First recombinant hAQP1 crystal structure

This work reports the first crystal structure of human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) 1 obtained from recombinant protein expressed in Sf9 insect cells, extending previous electron crystallographic studies (limited to ~3.8 A) that used native hAQP1 extracted from human red blood cells. The recombinant expression system enables mutagenesis studies and structure-based drug discovery targeting hAQP1.

### Comparison of hAQP1 and bAQP1 crystal packing

The crucial difference between hAQP1 and bAQP1 (bovine [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/), PDB 1j4n) lattices is the presence of an additional ~400 A2 packing interface in bAQP1 established between the N-terminal region of one tetramer and the C-terminal region of a dyad-related tetramer, stabilized by six hydrogen bonds. This interface is absent in hAQP1 due to disorder of the C-terminal polypeptide chain, leading to a slight tilt of the hAQP1 tetramer compared to bAQP1. The hAQP1 tetramer is formed via crystallographic fourfold axis. Contacts between head-to-tail tetramers are limited to arginine-rich loops 158-162 brought into proximity via a crystallographic dyad.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin Family</a> — hAQP1 is the founding member of the aquaporin water channel family
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aquaporin-z/">Aquaporin Z (AqpZ)</a> — Bacterial homolog of hAQP1; structural comparison for water selectivity
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp1/">AQP1</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
