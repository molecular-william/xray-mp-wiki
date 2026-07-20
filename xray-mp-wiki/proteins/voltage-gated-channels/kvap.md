---
title: "KvAP Voltage-Dependent Potassium Channel"
created: 2026-06-10
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature01580, doi/10.1073##pnas.1314356110]
verified: agent
uniprot_id: Q9YDF8
---

# KvAP Voltage-Dependent Potassium Channel

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9YDF8">UniProt: Q9YDF8</a>

<span class="expr-badge">Aeropyrum pernix</span>

## Overview

KvAP is a voltage-dependent potassium channel from the thermophilic archaebacterium Aeropyrum pernix. It serves as a model system for understanding voltage-gated potassium channel structure and gating mechanisms. The channel forms a homotetramer with a central ion-conduction pore lined by the conserved TVGYG selectivity filter motif, surrounded by four voltage-sensor domains. The structure revealed the voltage-sensor paddle architecture and provided the first high-resolution view of a full-length voltage-gated potassium channel.


## Publications

### doi/10.1038##nature01580

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1orq">1ORQ</a></td>
      <td>3.2</td>
      <td>I422</td>
      <td>Full-length KvAP from A. pernix (residues 18-240) with Fab 6E1</td>
      <td>K+, Cd2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1orq">1ORQ</a></td>
      <td>1.9</td>
      <td>C2</td>
      <td>Isolated voltage-sensor domain (Met 1 to Lys 147) with Fab 33H1</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli XL1-Blue
- **Construct**: KvAP full-length (residues 18-240) and isolated voltage-sensor domain (Met 1 to Lys 147) from Aeropyrum pernix, cloned into pQE69 with thrombin cleavage site and C-terminal hexahistidine tag
- **Notes**: Cells grown at 37 C to OD600 ~1.0, induced with 0.4 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 4 hours. Also expressed in E. coli for in vivo nonsense suppression of Y199-ester mutant.

**Purification:**

- **Expression system**: E. coli XL1-Blue
- **Expression construct**: KvAP full-length (residues 18-240) with C-terminal hexahistidine tag
- **Tag info**: C-terminal hexahistidine, thrombin cleavable

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
      <td>Chemical lysis with protease inhibitors</td>
      <td>—</td>
      <td>50 mM Tris pH 8.0, 100 mM KCl, leupeptin, pepstatin, aprotinin, PMSF</td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane extraction</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM Tris pH 8.0, 100 mM KCl + 40 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (DM)</td>
      <td>3 hour extraction at room temperature</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> Co2+ <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> Co2+ affinity resin (Clontech)</td>
      <td>20 mM Tris pH 8.0, 100 mM KCl + 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Eluted with 300-400 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/thrombin-protease/">Thrombin Protease</a> cleavage</td>
      <td>—</td>
      <td>20 mM Tris pH 8.0, 100 mM KCl + 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Overnight at room temperature (21 C), 1 unit thrombin per 2 mg protein</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (10/30) (Pharmacia)</td>
      <td>30 mM n-octyl glucoside</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Co-crystallization with Fab</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Full-length KvAP in DM + Fab 6E1</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Full-length KvAP-Fab 6E1 complex in I422. Also isolated VSD-Fab 33H1 in C2.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1orq">1ORQ</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">IGD</span><span class="topo-membrane">VMEHPLVELGVSYAALLSVIVVVVECTMQLSG</span><span class="topo-inside">EYLVRLYLVDLILVIILWADYAYRAYKSGDPAGYVKKTLYEIP</span><span class="topo-unknown">ALVPAGLLALIEGHLA</span><span class="topo-inside">GLGLFRLVRLLRFLRILLIISRGSKF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220   </span>
<span class="topo-line"><span class="topo-inside">LSAIADAADKIRF</span><span class="topo-membrane">YHLFGAVMLTVLYGAFAIYIV</span><span class="topo-outside">EYPDPNSSIKSV</span><span class="topo-unknown">FDALWWAVVTATTVGYG</span><span class="topo-outside">DVVPATPI</span><span class="topo-membrane">GKVIGIAVMLTGISALTLLIGTVSNMFQ</span><span class="topo-inside">KILV</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>35</td>
      <td>21</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>78</td>
      <td>53</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>94</td>
      <td>96</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>133</td>
      <td>112</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>151</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>166</td>
      <td>172</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>184</td>
      <td>200</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>191</td>
      <td>201</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>219</td>
      <td>209</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>223</td>
      <td>237</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1orq">1ORQ</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">IGD</span><span class="topo-membrane">VMEHPLVELGVSYAALLSVIVVVVECTMQLSG</span><span class="topo-inside">EYLVRLYLVDLILVIILWADYAYRAYKSGDPAGYVKKTLYEIP</span><span class="topo-unknown">ALVPAGLLALIEGHLA</span><span class="topo-inside">GLGLFRLVRLLRFLRILLIISRGSKF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220   </span>
<span class="topo-line"><span class="topo-inside">LSAIADAADKIRF</span><span class="topo-membrane">YHLFGAVMLTVLYGAFAIYIV</span><span class="topo-outside">EYPDPNSSIKSV</span><span class="topo-unknown">FDALWWAVVTATTVGYG</span><span class="topo-outside">DVVPATPI</span><span class="topo-membrane">GKVIGIAVMLTGISALTLLIGTVSNMFQ</span><span class="topo-inside">KILV</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>35</td>
      <td>21</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>78</td>
      <td>53</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>94</td>
      <td>96</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>133</td>
      <td>112</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>151</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>166</td>
      <td>172</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>184</td>
      <td>200</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>191</td>
      <td>201</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>219</td>
      <td>209</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>223</td>
      <td>237</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1orq">1ORQ</a> — Chain E (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">IGD</span><span class="topo-membrane">VMEHPLVELGVSYAALLSVIVVVVECTMQLSG</span><span class="topo-inside">EYLVRLYLVDLILVIILWADYAYRAYKSGDPAGYVKKTLYEIP</span><span class="topo-unknown">ALVPAGLLALIEGHLA</span><span class="topo-inside">GLGLFRLVRLLRFLRILLIISRGSKF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220   </span>
<span class="topo-line"><span class="topo-inside">LSAIADAADKIRF</span><span class="topo-membrane">YHLFGAVMLTVLYGAFAIYIV</span><span class="topo-outside">EYPDPNSSIKSV</span><span class="topo-unknown">FDALWWAVVTATTVGYG</span><span class="topo-outside">DVVPATPI</span><span class="topo-membrane">GKVIGIAVMLTGISALTLLIGTVSNMFQ</span><span class="topo-inside">KILV</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>35</td>
      <td>21</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>78</td>
      <td>53</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>94</td>
      <td>96</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>133</td>
      <td>112</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>151</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>166</td>
      <td>172</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>184</td>
      <td>200</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>191</td>
      <td>201</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>219</td>
      <td>209</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>223</td>
      <td>237</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1orq">1ORQ</a> — Chain F (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">IGD</span><span class="topo-membrane">VMEHPLVELGVSYAALLSVIVVVVECTMQLSG</span><span class="topo-inside">EYLVRLYLVDLILVIILWADYAYRAYKSGDPAGYVKKTLYEIP</span><span class="topo-unknown">ALVPAGLLALIEGHLA</span><span class="topo-inside">GLGLFRLVRLLRFLRILLIISRGSKF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220   </span>
<span class="topo-line"><span class="topo-inside">LSAIADAADKIRF</span><span class="topo-membrane">YHLFGAVMLTVLYGAFAIYIV</span><span class="topo-outside">EYPDPNSSIKSV</span><span class="topo-unknown">FDALWWAVVTATTVGYG</span><span class="topo-outside">DVVPATPI</span><span class="topo-membrane">GKVIGIAVMLTGISALTLLIGTVSNMFQ</span><span class="topo-inside">KILV</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>35</td>
      <td>21</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>78</td>
      <td>53</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>94</td>
      <td>96</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>133</td>
      <td>112</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>151</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>166</td>
      <td>172</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>184</td>
      <td>200</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>191</td>
      <td>201</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>219</td>
      <td>209</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>223</td>
      <td>237</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1orq">1ORQ</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">IGD</span><span class="topo-membrane">VMEHPLVELGVSYAALLSVIVVVVECTMQLSG</span><span class="topo-inside">EYLVRLYLVDLILVIILWADYAYRAYKSGDPAGYVKKTLYEIP</span><span class="topo-unknown">ALVPAGLLALIEGHLA</span><span class="topo-inside">GLGLFRLVRLLRFLRILLIISRGSKF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220   </span>
<span class="topo-line"><span class="topo-inside">LSAIADAADKIRF</span><span class="topo-membrane">YHLFGAVMLTVLYGAFAIYIV</span><span class="topo-outside">EYPDPNSSIKSV</span><span class="topo-unknown">FDALWWAVVTATTVGYG</span><span class="topo-outside">DVVPATPI</span><span class="topo-membrane">GKVIGIAVMLTGISALTLLIGTVSNMFQ</span><span class="topo-inside">KILV</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>35</td>
      <td>21</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>78</td>
      <td>53</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>94</td>
      <td>96</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>133</td>
      <td>112</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>151</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>166</td>
      <td>172</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>184</td>
      <td>200</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>191</td>
      <td>201</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>219</td>
      <td>209</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>223</td>
      <td>237</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1orq">1ORQ</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">IGD</span><span class="topo-membrane">VMEHPLVELGVSYAALLSVIVVVVECTMQLSG</span><span class="topo-inside">EYLVRLYLVDLILVIILWADYAYRAYKSGDPAGYVKKTLYEIP</span><span class="topo-unknown">ALVPAGLLALIEGHLA</span><span class="topo-inside">GLGLFRLVRLLRFLRILLIISRGSKF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220   </span>
<span class="topo-line"><span class="topo-inside">LSAIADAADKIRF</span><span class="topo-membrane">YHLFGAVMLTVLYGAFAIYIV</span><span class="topo-outside">EYPDPNSSIKSV</span><span class="topo-unknown">FDALWWAVVTATTVGYG</span><span class="topo-outside">DVVPATPI</span><span class="topo-membrane">GKVIGIAVMLTGISALTLLIGTVSNMFQ</span><span class="topo-inside">KILV</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>35</td>
      <td>21</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>78</td>
      <td>53</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>94</td>
      <td>96</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>133</td>
      <td>112</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>151</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>166</td>
      <td>172</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>184</td>
      <td>200</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>191</td>
      <td>201</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>219</td>
      <td>209</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>223</td>
      <td>237</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1orq">1ORQ</a> — Chain E (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">IGD</span><span class="topo-membrane">VMEHPLVELGVSYAALLSVIVVVVECTMQLSG</span><span class="topo-inside">EYLVRLYLVDLILVIILWADYAYRAYKSGDPAGYVKKTLYEIP</span><span class="topo-unknown">ALVPAGLLALIEGHLA</span><span class="topo-inside">GLGLFRLVRLLRFLRILLIISRGSKF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220   </span>
<span class="topo-line"><span class="topo-inside">LSAIADAADKIRF</span><span class="topo-membrane">YHLFGAVMLTVLYGAFAIYIV</span><span class="topo-outside">EYPDPNSSIKSV</span><span class="topo-unknown">FDALWWAVVTATTVGYG</span><span class="topo-outside">DVVPATPI</span><span class="topo-membrane">GKVIGIAVMLTGISALTLLIGTVSNMFQ</span><span class="topo-inside">KILV</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>35</td>
      <td>21</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>78</td>
      <td>53</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>94</td>
      <td>96</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>133</td>
      <td>112</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>151</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>166</td>
      <td>172</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>184</td>
      <td>200</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>191</td>
      <td>201</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>219</td>
      <td>209</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>223</td>
      <td>237</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1orq">1ORQ</a> — Chain F (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">IGD</span><span class="topo-membrane">VMEHPLVELGVSYAALLSVIVVVVECTMQLSG</span><span class="topo-inside">EYLVRLYLVDLILVIILWADYAYRAYKSGDPAGYVKKTLYEIP</span><span class="topo-unknown">ALVPAGLLALIEGHLA</span><span class="topo-inside">GLGLFRLVRLLRFLRILLIISRGSKF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220   </span>
<span class="topo-line"><span class="topo-inside">LSAIADAADKIRF</span><span class="topo-membrane">YHLFGAVMLTVLYGAFAIYIV</span><span class="topo-outside">EYPDPNSSIKSV</span><span class="topo-unknown">FDALWWAVVTATTVGYG</span><span class="topo-outside">DVVPATPI</span><span class="topo-membrane">GKVIGIAVMLTGISALTLLIGTVSNMFQ</span><span class="topo-inside">KILV</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>3</td>
      <td>18</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>35</td>
      <td>21</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>78</td>
      <td>53</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>94</td>
      <td>96</td>
      <td>111</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>133</td>
      <td>112</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>151</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>155</td>
      <td>166</td>
      <td>172</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>184</td>
      <td>200</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>191</td>
      <td>201</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>219</td>
      <td>209</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>223</td>
      <td>237</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.1314356110

**Expression:**

- **Expression system**: E. coli XL1-Blue
- **Construct**: KvAP full-length (residues 18-240) and isolated voltage-sensor domain (Met 1 to Lys 147) from Aeropyrum pernix, cloned into pQE69 with thrombin cleavage site and C-terminal hexahistidine tag
- **Notes**: Cells grown at 37 C to OD600 ~1.0, induced with 0.4 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 4 hours. Also expressed in E. coli for in vivo nonsense suppression of Y199-ester mutant.

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: KvAP with Y199-ester substitution (amber suppression at position 199)
- **Tag info**: Unnatural amino acid (HPLA) incorporated at Y199 via orthogonal tRNA/tRNA synthetase pair

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
      <td>Expression</td>
      <td>In vivo nonsense suppression</td>
      <td>—</td>
      <td></td>
      <td>Y199 in KvAP selectivity filter (equivalent to Y78 in <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KCSA</a>, Y445 in Shaker B) replaced with HPLA using amber suppression</td>
    </tr>
    <tr>
      <td>Purification and reconstitution</td>
      <td>Planar lipid bilayer reconstitution</td>
      <td>—</td>
      <td></td>
      <td>KvAP Y199-ester mutant incorporated into planar lipid bilayers for single-channel and macroscopic current recordings</td>
    </tr>
  </tbody>
</table>


## Biological / Functional Insights

### Voltage-sensor paddle architecture

The voltage sensor features a novel helix-turn-helix structure called the voltage-sensor paddle, composed of S3b and N-terminal half of S4. The paddle is located at the protein-lipid interface. Conserved S4 arginines carry most of the gating charge.

### S2 site occupancy regulates C-type inactivation

An ester substitution at the 2' amide bond in the KvAP selectivity filter (Y199-ester, equivalent to Y78 in [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/)) dramatically slows C-type inactivation, similar to the effect in [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/). Single-channel conductance is reduced from 136 pS (WT) to 18 pS (Y199-ester) in 150 mM K+ at +100 mV. Recovery from inactivation is also affected. These results demonstrate that the S2-dependent inactivation mechanism is conserved across K+ channels.

### S4-S5 linker as flexible coupling element

The S4-S5 linker connects the voltage-sensor paddle to the pore-lining S5 helix. It is poorly conserved with many hydrophilic residues and [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) break points.

### Glycine-gating hinge mechanism

The S6 inner helices contain a conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) that acts as a gating hinge, allowing the inner helices to open like a camera aperture.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA Potassium Channel</a> — Selectivity filter structure essentially identical; glycine-gating hinge mechanism first identified in KcsA-MthK comparison
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Primary detergent (40 mM) for membrane extraction and 5 mM for purification
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Main buffer component (50 mM, pH 8.0) throughout purification
- <a href="/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/">Potassium Chloride (KCl)</a> — 100 mM KCl in lysis buffer; 6 K+ ions in selectivity filter
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/">C-type Inactivation</a> — Y199-ester mutation slows C-type inactivation in KvAP, linking S2 occupancy to inactivation
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Elution agent (300-400 mM) for TALON Co2+ affinity chromatography
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Additive used in purification or crystallization buffers
