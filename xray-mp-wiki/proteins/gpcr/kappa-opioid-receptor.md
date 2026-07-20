---
title: "Kappa Opioid Receptor"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10939, doi/10.1016##j.cell.2017.12.011, doi/10.1038##s41467-023-37041-7]
verified: agent
uniprot_id: ['P0ABE7', 'P41145']
---

# Kappa Opioid Receptor

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0ABE7">UniProt: P0ABE7</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P41145">UniProt: P41145</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The human kappa opioid receptor (KOP) is a class A G-protein coupled receptor (GPCR) that mediates the actions of opioids with hallucinogenic, dysphoric, and analgesic activities. Multiple crystal structures have been solved: the inactive-state structure with JDTic alone (PDB 4DJH, 2.9 A), the active-state structure with MP1104 and Nb39 (PDB 6B73, 3.1 A), the Nb6-stabilized inactive-state with JDTic, and the nalfurafine-bound structure with Nb39 (3.3 A).


## Publications

### doi/10.1038##nature10939

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4djh">4DJH</a></td>
      <td>2.9</td>
      <td>C2</td>
      <td>Kappa-OR-T4L fusion (T4L inserted at ICL3 between Gly261 and Arg263), N-terminal deletion Delta Glu2-Ala42, C-terminal deletion Delta Arg359-Val380, I135L point mutation</td>
      <td>JDTic</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 insect cells
- **Construct**: Kappa-OR with N-terminal HA signal sequence, Flag tag, 10xHis tag, and TEV protease recognition site; T4L fused in ICL3; N-terminal Delta Glu2-Ala42 and C-terminal Delta Arg359-Val380 truncations; I135L mutation
- **Notes**: Baculovirus expression system used. 25 uM naltrexone (NTX) and 5% Protein Boost Additive added during expression.

**Purification:**

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: Kappa-OR-T4L with N-terminal HA-Flag-10xHis-TEV tag, N/C-terminal truncations, I135L mutation
- **Tag info**: N-terminal HA-Flag-10xHis tag, cleavable by TEV protease

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
      <td>Centrifugation</td>
      <td>—</td>
      <td>Hypotonic buffer (10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitors); high osmotic buffer (1.0 M NaCl, 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitors) + —</td>
      <td>Thawed in hypotonic buffer, washed 2-3x in hypotonic buffer, then 3-4x in high osmotic buffer</td>
    </tr>
    <tr>
      <td>Alkylation and ligand incubation</td>
      <td>Pre-incubation</td>
      <td>—</td>
      <td>40 uM NTX, 2 mg/ml iodoacetamide, 150 mM NaCl, protease inhibitors + —</td>
      <td>1 h at 4 °C before solubilization</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 150 mM NaCl + 1% (w/v) detergent (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) likely)</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Kappa-OR-T4L-JDTic complex</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized using <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> method as described in Caffrey & Cherezov (2009). Data collected at APS.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4djh">4DJH</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGTTMGSEDAQLEPAHI</span><span class="topo-outside">SPA</span><span class="topo-membrane">IPVIITAVYSVVFVVGLVGNSLVMFVIIR</span><span class="topo-inside">YTKMKTA</span><span class="topo-membrane">TNIYIFNLALADALVTTTMPFQS</span><span class="topo-outside">TVYLMNSWPFGDVLCK</span><span class="topo-membrane">IVLSIDYYNMFTSIFTLTMMSVDRY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">I</span><span class="topo-inside">AVCHPVKALDFRTPL</span><span class="topo-membrane">KAKIINICIWLLSSSVGISAI</span><span class="topo-outside">VLGGTKVREDVDVIECSLQFPDDDYSWWDLFMKI</span><span class="topo-membrane">CVFIFAFVIPVLIIIVCYTLMIL</span><span class="topo-inside">RLKSVRLLSGNIFEMLRIDEGLRLKI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">YKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">WYNQTPNRAKRVITTFRTGTWDAYREKDRNLRRI</span><span class="topo-membrane">TRLVLVVVAVFVVCWTPIHI</span><span class="topo-outside">FILVEALGS</span><span class="topo-unknown">TSHST</span><span class="topo-outside">AALSSYY</span><span class="topo-membrane">FCIALGYTNSSLNPILYAFLD</span><span class="topo-unknown">ENFKRCFRDFC</span><span class="topo-inside">FP</span><span class="topo-unknown">LKMRMERQSTS</span></span>
<details class="topo-details"><summary>Topology coordinates (22 regions)</summary>
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
      <td>17</td>
      <td>38</td>
      <td>54</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>20</td>
      <td>55</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>49</td>
      <td>58</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>56</td>
      <td>87</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>79</td>
      <td>94</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>95</td>
      <td>117</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>121</td>
      <td>133</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>136</td>
      <td>159</td>
      <td>173</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>157</td>
      <td>174</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>191</td>
      <td>195</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>214</td>
      <td>229</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>224</td>
      <td>252</td>
      <td>261</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>384</td>
      <td>1002</td>
      <td>1161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>394</td>
      <td>263</td>
      <td>272</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>414</td>
      <td>273</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>415</td>
      <td>423</td>
      <td>293</td>
      <td>301</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>424</td>
      <td>428</td>
      <td>302</td>
      <td>306</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>429</td>
      <td>435</td>
      <td>307</td>
      <td>313</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>436</td>
      <td>456</td>
      <td>314</td>
      <td>334</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>467</td>
      <td>335</td>
      <td>345</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>468</td>
      <td>469</td>
      <td>346</td>
      <td>347</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>470</td>
      <td>480</td>
      <td>348</td>
      <td>358</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4djh">4DJH</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGTTMGSEDAQLEPAHI</span><span class="topo-outside">SPA</span><span class="topo-membrane">IPVIITAVYSVVFVVGLVGNSLVMFVII</span><span class="topo-inside">RYTKMKTAT</span><span class="topo-membrane">NIYIFNLALADALVTTTMPFQS</span><span class="topo-outside">TVYLMNSWPFGDVLCK</span><span class="topo-membrane">IVLSIDYYNMFTSIFTLTMMSVD</span><span class="topo-inside">RY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IAVCH</span><span class="topo-unknown">PVKALDF</span><span class="topo-inside">RTPLK</span><span class="topo-membrane">AKIINICIWLLSSSVGISAIV</span><span class="topo-outside">LGGTKVREDVDVIECSLQFPDDDYSWWDLF</span><span class="topo-membrane">MKICVFIFAFVIPVLIIIVCYT</span><span class="topo-inside">LMILRLKSVRLLSGNIFEMLRIDEGLRLKI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">YKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">WYNQTPNRAKRVITTFRTGTWDAYREKDRNLRRITRL</span><span class="topo-membrane">VLVVVAVFVVCWTPIHIFILV</span><span class="topo-outside">EALG</span><span class="topo-unknown">STSH</span><span class="topo-outside">STAALSS</span><span class="topo-membrane">YYFCIALGYTNSSLNPILYAFL</span><span class="topo-inside">D</span><span class="topo-unknown">ENFKRCFRDFC</span><span class="topo-inside">FP</span><span class="topo-unknown">LKMRMERQSTS</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>17</td>
      <td>38</td>
      <td>54</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>20</td>
      <td>55</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>48</td>
      <td>58</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>86</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>95</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>95</td>
      <td>117</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>118</td>
      <td>133</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>125</td>
      <td>156</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>132</td>
      <td>163</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>133</td>
      <td>137</td>
      <td>170</td>
      <td>174</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>158</td>
      <td>175</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>188</td>
      <td>196</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>210</td>
      <td>226</td>
      <td>247</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>224</td>
      <td>248</td>
      <td>261</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>384</td>
      <td>1002</td>
      <td>1161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>397</td>
      <td>263</td>
      <td>275</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>418</td>
      <td>276</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>419</td>
      <td>422</td>
      <td>297</td>
      <td>300</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>426</td>
      <td>301</td>
      <td>304</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>427</td>
      <td>433</td>
      <td>305</td>
      <td>311</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>434</td>
      <td>455</td>
      <td>312</td>
      <td>333</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>456</td>
      <td>334</td>
      <td>334</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>457</td>
      <td>467</td>
      <td>335</td>
      <td>345</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>468</td>
      <td>469</td>
      <td>346</td>
      <td>347</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>470</td>
      <td>480</td>
      <td>348</td>
      <td>358</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1016##j.cell.2017.12.011

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6b73">6B73</a></td>
      <td>3.1</td>
      <td>P21</td>
      <td>BRIL-fused KOP (truncated 7TM)</td>
      <td>MP1104, Nb39</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 insect cells
- **Construct**: Kappa-OR with N-terminal HA signal sequence, Flag tag, 10xHis tag, and TEV protease recognition site; T4L fused in ICL3; N-terminal Delta Glu2-Ala42 and C-terminal Delta Arg359-Val380 truncations; I135L mutation
- **Notes**: Baculovirus expression system used. 25 uM naltrexone (NTX) and 5% Protein Boost Additive added during expression.

**Purification:**

- **Expression system**: Sf9 cells (baculovirus)
- **Expression construct**: BRIL-fused KOP with C-terminal His-tag
- **Tag info**: C-terminal hexa-His tag on BRIL

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
      <td>— + —</td>
      <td>Sf9 cells harvested 48 h post-infection, washed in 1x PBS, stored at -80 C. 10 uM naltrexone added to help receptor trafficking.</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Repeated centrifugation</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, 500 uM AEBSF, 1 uM E-64, 1 uM leupeptin, 150 nM Aprotinin (low-salt); 1.0 M NaCl, 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl (high osmolarity) + —</td>
      <td>4 repeated centrifugations in high osmolarity buffer to remove soluble and membrane-associated proteins.</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.5, 100 mM NaCl + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2 mg/mL <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Membranes resuspended and solubilized by gentle stirring.</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC resin (Clontech)</td>
      <td>10 mM HEPES pH 7.5, 100 mM NaCl, 20 mM imidazole (wash); 250 mM imidazole (elution) + 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Supernatant incubated with <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin, washed, eluted with imidazole.</td>
    </tr>
    <tr>
      <td>TEV protease cleavage</td>
      <td>Proteolytic cleavage</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.5, 100 mM NaCl + 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease added overnight at 4 C to cleave His-tag from <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>.</td>
    </tr>
    <tr>
      <td>Reverse TALON purification</td>
      <td>Pass-through chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC resin</td>
      <td>10 mM HEPES pH 7.5, 100 mM NaCl + 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Flow-through collected containing cleaved <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>-KOP complex.</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td>10 mM HEPES pH 7.5, 100 mM NaCl + 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final purification step to isolate monodisperse complex.</td>
    </tr>
  </tbody>
</table>
**Final sample**: [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/)-KOP-MP1104-Nb39 complex, 10-15 mg/mL in 10 mM HEPES pH 7.5, 100 mM NaCl, 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), stored at -80 C with 10% glycerol

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>-KOP-MP1104-Nb39 complex at 10-15 mg/mL</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>. Data collected at APS GM/CA CAT 23ID-B/D.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6b73">6B73</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGTTMADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKY</span><span class="topo-inside">LGSISPAI</span><span class="topo-membrane">PV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IITAVYSVVFVVGLVGNSLVMFVIIR</span><span class="topo-outside">YTKMKTAT</span><span class="topo-membrane">NIYIFNLALADALVTTTMPFQST</span><span class="topo-inside">VYLMNSWPFGDVL</span><span class="topo-membrane">CKIVLSIDYYNMFTSIFTLTMMSVD</span><span class="topo-outside">RYIAVCH</span><span class="topo-unknown">PVKALDF</span><span class="topo-outside">RTPL</span><span class="topo-membrane">KAKIINI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">CIWLLSSSVGISAIVLG</span><span class="topo-inside">GTKVR</span><span class="topo-unknown">EDV</span><span class="topo-inside">DVIECSLQFPDDDYSWW</span><span class="topo-membrane">DLFMKICVFIFAFVIPVLIIIVCYT</span><span class="topo-outside">LMILRLKSVR</span><span class="topo-unknown">LLSG</span><span class="topo-outside">SREKDRNLRRIT</span><span class="topo-membrane">RLVLVVVAVFVVCWTPIHIFILVEAL</span><span class="topo-inside">G</span></span>
<span class="topo-ruler">       370       380       390       400       410        </span>
<span class="topo-line"><span class="topo-unknown">S</span><span class="topo-inside">TSHSTAALS</span><span class="topo-membrane">SYYFCIALGYTNSSLNPILYAFLD</span><span class="topo-outside">ENFKR</span><span class="topo-unknown">CFRDFCFPLKMRMERQSTS</span></span>
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
      <td>111</td>
      <td>118</td>
      <td>51</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>146</td>
      <td>59</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>154</td>
      <td>87</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>177</td>
      <td>95</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>190</td>
      <td>118</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>215</td>
      <td>131</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>222</td>
      <td>156</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>229</td>
      <td>163</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>230</td>
      <td>233</td>
      <td>170</td>
      <td>173</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>257</td>
      <td>174</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>258</td>
      <td>262</td>
      <td>198</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>282</td>
      <td>206</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>307</td>
      <td>223</td>
      <td>247</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>317</td>
      <td>248</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>333</td>
      <td>262</td>
      <td>273</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>359</td>
      <td>274</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>360</td>
      <td>300</td>
      <td>300</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>362</td>
      <td>370</td>
      <td>302</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>394</td>
      <td>311</td>
      <td>334</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>395</td>
      <td>399</td>
      <td>335</td>
      <td>339</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41467-023-37041-7

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7yit">7YIT</a></td>
      <td>3.3</td>
      <td>—</td>
      <td>BRIL-fused KOP (truncated 7TM) with S324C thermostabilizing mutation</td>
      <td>Nalfurafine, Nb39</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 insect cells
- **Construct**: Kappa-OR with N-terminal HA signal sequence, Flag tag, 10xHis tag, and TEV protease recognition site; T4L fused in ICL3; N-terminal Delta Glu2-Ala42 and C-terminal Delta Arg359-Val380 truncations; I135L mutation
- **Notes**: Baculovirus expression system used. 25 uM naltrexone (NTX) and 5% Protein Boost Additive added during expression.

**Purification:**

- **Expression system**: Sf9 cells (baculovirus)
- **Expression construct**: BRIL-fused KOP (truncated 7TM) with S324C mutation, C-terminal His-tag
- **Tag info**: C-terminal hexa-His tag on BRIL

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
      <td>Cell culture and membrane preparation</td>
      <td>Baculovirus infection of Sf9 cells</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, protease inhibitors; high-salt wash (1.0 M NaCl, 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl) + —</td>
      <td>Cells harvested 48 h post-infection; membranes washed 4x in high-salt buffer.</td>
    </tr>
    <tr>
      <td>Ligand incubation and alkylation</td>
      <td>Pre-incubation with ligand</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, 150 mM NaCl, 50 uM nalfurafine, protease inhibitors + —</td>
      <td>Incubated 1 h RT, then 30 min at 4 C; 2 mg/mL iodoacetamide added for 30 min alkylation.</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.5, 150 mM NaCl, protease inhibitors + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>2 h at 4 C; clarified at 150,000 x g for 30 min.</td>
    </tr>
    <tr>
      <td>TALON IMAC affinity</td>
      <td>Cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC resin (Clontech)</td>
      <td>Wash I: 50 mM HEPES pH 7.5, 800 mM NaCl, 20 mM imidazole, 10% glycerol, 25 uM nalfurafine; Wash II: 25 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol, 25 uM nalfurafine + Wash I: 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/); Wash II: 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Resin incubated with supernatant overnight at 4 C; washed with 10 CV Wash I then 10 CV Wash II; eluted with 250 mM imidazole.</td>
    </tr>
    <tr>
      <td>TEV protease cleavage</td>
      <td>Proteolytic cleavage</td>
      <td>—</td>
      <td>25 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>His-tagged <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease added overnight at 4 C to remove N-terminal 10x His-tag.</td>
    </tr>
    <tr>
      <td>Reverse TALON purification</td>
      <td>Pass-through chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC resin</td>
      <td>25 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Flow-through collected to remove <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease, cleaved His-tag, and uncleaved protein.</td>
    </tr>
    <tr>
      <td>Nb39 complex formation</td>
      <td>Complex formation</td>
      <td>—</td>
      <td>25 mM HEPES pH 7.5, 150 mM NaCl, 10% glycerol + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Incubated with excess Nb39 (KOR/Nb39 1:2 molar ratio) for 3 h; concentrated to ~30 mg/mL using 100 kDa MWCO concentrator.</td>
    </tr>
  </tbody>
</table>
**Final sample**: KOR-nalfurafine-Nb39 complex at ~30 mg/mL in 25 mM HEPES pH 7.5, 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 10% glycerol

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>KOR-nalfurafine-Nb39 complex at ~30 mg/mL</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yit">7YIT</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">I</span><span class="topo-inside">SPAIPV</span><span class="topo-membrane">IITAVYSVVFVVGLVGNSLVMFVIIRYTK</span><span class="topo-unknown">M</span><span class="topo-outside">KTA</span><span class="topo-membrane">TNIYIFNLALADALVTTTMPFQS</span><span class="topo-inside">TVYLMNSWPFGDVL</span><span class="topo-membrane">CKIVLSIDYYNMFTSIFTLTMMSVDRY</span><span class="topo-outside">IAVCHPVKALDFRTPL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">KAKIINICIWLLSSSVGISAIVLG</span><span class="topo-inside">GTKVRE</span><span class="topo-unknown">DV</span><span class="topo-inside">DVIECSLQFPDDDYSWWDL</span><span class="topo-membrane">FMKICVFIFAFVIPVLIIIVCYTL</span><span class="topo-outside">MILRLKSVR</span><span class="topo-unknown">LLSG</span><span class="topo-outside">SREKDRNLRRIT</span><span class="topo-membrane">RLVLVVVAVFVVCWTPIHIF</span></span>
<span class="topo-ruler">       250       260       270       280       290       300     </span>
<span class="topo-line"><span class="topo-membrane">ILV</span><span class="topo-inside">EALGS</span><span class="topo-unknown">TSH</span><span class="topo-inside">STAALSS</span><span class="topo-membrane">YYFCIALGYTNSCLNPILYAFLD</span><span class="topo-outside">ENFKRCFRDFCFP</span><span class="topo-unknown">LKMRMERQSTS</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>54</td>
      <td>54</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>55</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>36</td>
      <td>61</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>37</td>
      <td>90</td>
      <td>90</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>38</td>
      <td>40</td>
      <td>91</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>63</td>
      <td>94</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>77</td>
      <td>117</td>
      <td>130</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>104</td>
      <td>131</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>120</td>
      <td>158</td>
      <td>173</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>144</td>
      <td>174</td>
      <td>197</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>150</td>
      <td>198</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>152</td>
      <td>204</td>
      <td>205</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>153</td>
      <td>171</td>
      <td>206</td>
      <td>224</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>195</td>
      <td>225</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>204</td>
      <td>249</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>208</td>
      <td>258</td>
      <td>261</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>209</td>
      <td>220</td>
      <td>262</td>
      <td>273</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>243</td>
      <td>274</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>248</td>
      <td>297</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>251</td>
      <td>302</td>
      <td>304</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>252</td>
      <td>258</td>
      <td>305</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>281</td>
      <td>312</td>
      <td>334</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>282</td>
      <td>294</td>
      <td>335</td>
      <td>347</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>305</td>
      <td>348</td>
      <td>358</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7yit">7YIT</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100         </span>
<span class="topo-line"><span class="topo-unknown">MA</span><span class="topo-inside">DLEDNWETLNDNLKVIEK</span><span class="topo-unknown">ADNAA</span><span class="topo-inside">QVKDALTKMRAAALDA</span><span class="topo-unknown">QKATPPKLEDKSPDSPE</span><span class="topo-inside">MKDFRHGFDILVGQIDDALKLANE</span><span class="topo-unknown">GKE</span><span class="topo-inside">KEAQAAAEQLKTTRNAYIQKYLGS</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>2</td>
      <td>1000</td>
      <td>1001</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>20</td>
      <td>1002</td>
      <td>1019</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>25</td>
      <td>1020</td>
      <td>1024</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>41</td>
      <td>1025</td>
      <td>1040</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>58</td>
      <td>1041</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>82</td>
      <td>1058</td>
      <td>1081</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>85</td>
      <td>1082</td>
      <td>1084</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>86</td>
      <td>109</td>
      <td>1085</td>
      <td>1108</td>
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

### JDTic Binding and Subtype Selectivity

The crystal structure of KOR in complex with the selective antagonist JDTic (PDB 4DJH, 2.9 A) reveals the structural basis for high affinity and subtype selectivity. JDTic adopts a V-shaped conformation, anchoring via two amino groups to Asp1383.32. Four residues differing among opioid receptor subtypes contribute to selectivity: Val1082.53, Val1182.63, Ile2946.55, and Tyr3127.35. JDTic achieves >1000-fold selectivity for KOR via these residue differences, without requiring the 'address' interaction with Glu2976.58 utilized by morphinan-based antagonists.

### Salvinorin A Binding

Docking studies of the diterpene agonist salvinorin A analogue RB-64 into the KOR structure reveal that the thiocyanate group of RB-64 can react with Cys3157.38 to form covalent adducts, consistent with SCAM and SAR studies. SalA is unique among KOR ligands in lacking a charged nitrogen atom.

### MP1104 Binding Pocket and Hydrophobic Interactions

MP1104 binds in the orthosteric pocket of active-state KOP with its cyclopropylmethyl group extending into a hydrophobic pocket formed by W2876.48, G3197.42, and Y3207.43. The iodobenzamide moiety forms a water-mediated hydrogen bond with Y3127.35. Mutations W2876.48L, G3197.42L, and Y3207.43L strongly reduce MP1104 potency for both G protein activation and beta-arrestin2 recruitment.

### KOP Activation Mechanism and Signal Propagation

Activation-related conformational changes propagate from the orthosteric site: (1) The D3.32YYNM3.36 anchoring motif in TM3 rearranges. (2) The CWxP motif residue W2876.48 couples to the P5.50-I3.40-F6.44 toggle switch, promoting F2836.44 rotation. (3) TM6 outward displacement of ~10 A opens the intracellular surface. (4) The sodium pocket between TM2/TM3/TM7 collapses. (5) The NPxxY motif and DRY motif undergo characteristic rearrangements.

### Nb6 Stabilizes a Distinct Inactive State

The KOR-JDTic-Nb6 complex structure revealed Nb6 binds at the intracellular interface between TM5 and TM6. R102 in Nb6 forms ionic interactions with D2666.27 and R2706.31. Unlike beta2AR-Nb60, KOR uses R3.50 forming two H-bonds with T2.39 and T6.34 to stabilize the inactive conformation.

### Nalfurafine-Bound KOR Structure and Biased Signaling

The nalfurafine-bound KOR structure (3.3 A) revealed nalfurafine adopts a reversed V-shaped conformation. The furan ring extends into a crevice between TM1 and TM2. The S3247.47C mutation increased receptor stability. MD simulations identified three active-state conformations, including an occluded state that explains G protein bias.

### Ligand-Specific Determinants of Signaling Bias

Nalfurafine destabilizes the K2275.39-E2976.58 salt bridge. W2876.48A selectively reduces nalfurafine-mediated arrestin recruitment. TRUPATH profiling showed KOR activates multiple G protein subtypes (Gi1, Gi2, Gi3, GoA, GoB, Gz, Gustducin).


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/jdtc/">JDTic</a> — Selective antagonist co-crystallized with KOR in PDB 4DJH
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> — Fusion partner used in crystallization constructs
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Primary detergent for solubilization and crystallization
- <a href="/xray-mp-wiki/reagents/ligands/mp1104/">MP1104</a> — Co-crystallized agonist in PDB 6B73
- <a href="/xray-mp-wiki/reagents/ligands/nalfurafine/">Nalfurafine</a> — G protein-biased KOR agonist co-crystallized in the 2023 structure
- <a href="/xray-mp-wiki/concepts/gpcr-biased-signaling/">GPCR Biased Signaling</a> — The occluded state mechanism explains G protein bias at KOR
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/npxxy-motif/">NPxxY Motif</a> — Important functional motif in KOR activation
- <a href="/xray-mp-wiki/concepts/signaling-receptors/beta-arrestin/">Beta-Arrestin</a> — Key signaling pathway for KOR
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> — Expression system used for KOR production
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Purification method used for KOR
