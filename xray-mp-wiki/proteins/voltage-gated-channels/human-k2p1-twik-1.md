---
title: "Human K2P1 (TWIK-1) Potassium Channel"
created: 2026-06-21
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1213274]
verified: agent
uniprot_id: O00180
---

# Human K2P1 (TWIK-1) Potassium Channel

<div class="expr-badges"><span class="expr-badge expr-p-pastoris">P. pastoris</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O00180">UniProt: O00180</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Human K2P1 (also known as TWIK-1, encoded by KCNK1) is a two-pore domain potassium (K2P) channel that generates background leak K+ currents and contributes to the resting membrane potential. K2P1 is unusual among K2P channels in that it can conduct Na+ when extracellular K+ is below approximately 3 mM (hypokalemia), depolarizing cardiomyocytes and potentially contributing to cardiac arrhythmia. The crystal structure of human K2P1 was determined at 3.4 A resolution, revealing a dimeric channel with a distinctive extracellular cap domain, an interfacial C helix, and subunit interface openings that expose the central cavity to the lipid membrane.

## Publications

### doi/10.1126##science.1213274

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ukm">3UKM</a></td>
      <td>3.4</td>
      <td>P2(1)</td>
      <td>Human K2P1 residues 19-288 (removed N-terminal 18 residues and C-terminal 48 residues), C22S, N95Q mutations</td>
      <td>K+ ions at selectivity filter sites S1-S4; Tl+ ions (surrogate for K+) at selectivity filter</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: Human K2P1 residues 19-288, C22S, N95Q mutations
- **Notes**: Protein confirmed functional by flux assay when reconstituted into lipid vesicles (fig. S2)

**Purification:**

- **Expression system**: Pichia pastoris
- **Expression construct**: Human K2P1 residues 19-288, C22S, N95Q

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
      <td>Expression and purification</td>
      <td>Standard Pichia pastoris expression and purification</td>
      <td>—</td>
      <td></td>
      <td>Purified protein was functional, forming K+ channels when reconstituted into lipid vesicles as confirmed by flux assay</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified human K2P1</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>150 mM K+</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in presence of 150 mM K+. Soaked in Tl+ solutions for anomalous phasing. Space group P2(1) with four copies per asymmetric unit forming two channels. Experimental SAD/MAD phasing using Hg, Au, and Tl derivatives.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ukm">3UKM</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPSREAS</span><span class="topo-inside">NSAT</span><span class="topo-membrane">MFGFLVLGYLLYLVFGAVVFSSV</span><span class="topo-outside">ELPYEDLLRQELRKLKRRFLEEHECLSEQQLEQFLGRVLEASNYGVSVL</span><span class="topo-unknown">SQASGN</span><span class="topo-outside">WNWDF</span><span class="topo-unknown">TSALFFASTVLSTTGYG</span><span class="topo-outside">HTVPLSD</span><span class="topo-membrane">GG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KAFCIIYSVIGIPFTLLFLTAVVQRIT</span><span class="topo-inside">VHVTRRPVLYF</span><span class="topo-unknown">HIRWGF</span><span class="topo-inside">SKQVVAIV</span><span class="topo-membrane">HAVLLGFVTVSCFFFIPAAVFSVL</span><span class="topo-outside">EDDWNF</span><span class="topo-unknown">LESFYFCFISLSTIGLG</span><span class="topo-outside">DYVPGEGYNQKFRE</span><span class="topo-membrane">LYKIGIT</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-membrane">CYLLLGLIAMLVVLETFC</span><span class="topo-inside">EL</span><span class="topo-unknown">HELKKFRK</span><span class="topo-inside">MFY</span><span class="topo-unknown">VKKDKDEVD</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>11</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>11</td>
      <td>18</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>34</td>
      <td>22</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>83</td>
      <td>45</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>89</td>
      <td>94</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>100</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>105</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>118</td>
      <td>122</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>147</td>
      <td>129</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>158</td>
      <td>158</td>
      <td>168</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>164</td>
      <td>169</td>
      <td>174</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>165</td>
      <td>172</td>
      <td>175</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>196</td>
      <td>183</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>202</td>
      <td>207</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>219</td>
      <td>213</td>
      <td>229</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>220</td>
      <td>233</td>
      <td>230</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>258</td>
      <td>244</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>259</td>
      <td>260</td>
      <td>269</td>
      <td>270</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>268</td>
      <td>271</td>
      <td>278</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>269</td>
      <td>271</td>
      <td>279</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>280</td>
      <td>282</td>
      <td>290</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ukm">3UKM</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPSREAS</span><span class="topo-inside">NSAT</span><span class="topo-membrane">MFGFLVLGYLLYLVFGAVVFSSV</span><span class="topo-outside">ELPYEDLLRQELRKLKRRFLEEHECLSEQQLEQFLGRVLEASNYGVSVL</span><span class="topo-unknown">SQASGN</span><span class="topo-outside">WNWDF</span><span class="topo-unknown">TSALFFASTVLSTTGYG</span><span class="topo-outside">HTVPLSD</span><span class="topo-membrane">GG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KAFCIIYSVIGIPFTLLFLTAVVQRIT</span><span class="topo-inside">VHVTRRPVLYF</span><span class="topo-unknown">HIRWGF</span><span class="topo-inside">SKQVVAIV</span><span class="topo-membrane">HAVLLGFVTVSCFFFIPAAVFSVL</span><span class="topo-outside">EDDWNF</span><span class="topo-unknown">LESFYFCFISLSTIGLG</span><span class="topo-outside">DYVPGEGYNQKFRE</span><span class="topo-membrane">LYKIGIT</span></span>
<span class="topo-ruler">       250       260       270       280</span>
<span class="topo-line"><span class="topo-membrane">CYLLLGLIAMLVVLETFC</span><span class="topo-inside">EL</span><span class="topo-unknown">HELKKFRK</span><span class="topo-inside">MFY</span><span class="topo-unknown">VKKDKDEVD</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>11</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>11</td>
      <td>18</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>34</td>
      <td>22</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>83</td>
      <td>45</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>89</td>
      <td>94</td>
      <td>99</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>100</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>105</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>112</td>
      <td>118</td>
      <td>122</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>147</td>
      <td>129</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>158</td>
      <td>158</td>
      <td>168</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>164</td>
      <td>169</td>
      <td>174</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>165</td>
      <td>172</td>
      <td>175</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>196</td>
      <td>183</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>202</td>
      <td>207</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>219</td>
      <td>213</td>
      <td>229</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>220</td>
      <td>233</td>
      <td>230</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>258</td>
      <td>244</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>259</td>
      <td>260</td>
      <td>269</td>
      <td>270</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>268</td>
      <td>271</td>
      <td>278</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>269</td>
      <td>271</td>
      <td>279</td>
      <td>281</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>280</td>
      <td>282</td>
      <td>290</td>
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

### Extracellular cap domain

K2P1 has a ~55-amino acid extracellular region between M1 and pore helix 1 forming a structured cap domain extending approximately 35 A above the membrane. The cap is an A-frame structure with E1 and E2 helices from each subunit, positioned directly above the selectivity filter. Pro47 (conserved among K2P channels) creates a ~30 degree bend between M1 and E1. Cys69 (conserved in most K2P channels) forms a disulfide bond covalently linking the two subunits at the cap apex. The C-terminal ends of E2 helices are positioned above the selectivity filter, with helix dipole moments concentrating cations near the filter.

### Interfacial C helix and inner helix gating

A conserved amphipathic C helix located at the membrane/cytosol interface runs along the inner surface of the M2 and M4 inner helices. The C helix contacts the M2-M3 loop and the M4 helix of the adjacent subunit, appearing structurally poised to affect inner helix gating. Conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues Gly141 and Gly256 in the inner helices serve as gating hinges. This region in TREK-1 is known to respond to phospholipids, intracellular acidification, and membrane stretch.

### Dimeric K2P architecture and selectivity filter

K2P channels assemble as dimers with each protomer containing two P domain sequences arranged in tandem. The selectivity filter sequences differ between P domain 1 (TTGYGH) and P domain 2 (TIGLGD), deviating from the canonical K+ channel filter sequence TXGYGD. Despite this, the filter adopts a conductive, four-fold symmetric configuration for K+ ion coordination. Thr118 (the second T in TTGYGH) is associated with the ability of K2P1 to conduct Na+ in low extracellular K+.

### Subunit interface fenestrations

K2P1 has openings between subunits (between M2 of one subunit and M4 of the other) that expose the central cavity to the hydrophobic core of the lipid membrane. These openings span much of the inner leaflet. Electron density maps revealed alkyl chains of approximately 11 carbons within these openings, likely from bound lipids or detergent. Pro143 (conserved in most K2P channels) creates a bend in M2 that contributes to these openings, which may allow lipophilic compounds like tetrahexylammonium (THA) to access the central cavity via the membrane.

### Extracellular ion pathway

The extracellular cap restricts access to the selectivity filter to two side portals (funnel-shaped, approximately 6 A van der Waals opening at the narrow end). The portals are lined by negatively charged residues (Glu84, Ser86, Asn87, Ser91, Glu235) and the C-terminal ends of E2 helices, creating an electrostatic gradient that concentrates cations near the filter. An external K+ binding site coordinated by two water molecules was observed above the filter. Sequence variation in portal-lining residues among K2P channels may account for electrophysiological differences.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/k2p-2-1-trek-1/">K2P 2.1 (TREK-1) Potassium Channel</a> — Fellow K2P channel member; both are two-pore domain potassium channels
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/human-task-1-k2p3-1/">Human TASK-1 (K2P 3.1)</a> — Fellow K2P channel member; structural and functional comparisons
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/traak/">Human TRAAK Potassium Channel (K2P 4.1)</a> — K2P channel family comparison
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/">Ion Channel Selectivity Filter</a> — K2P1 has a pseudo-tetrameric selectivity filter with two different P domain sequences (TTGYGH and TIGLGD)
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/">C-type Inactivation</a> — K2P channels use a selectivity filter C-type gate as the principal gating site
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/">NCS</a> — Related biological concept
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> — Buffer component used in purification or crystallization
