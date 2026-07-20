---
title: "K2P 2.1 (TREK-1) Potassium Channel"
created: 2026-06-10
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature22988, doi/10.1126##sciadv.abc9174]
verified: agent
uniprot_id: P97438
---

# K2P 2.1 (TREK-1) Potassium Channel

<div class="expr-badges"><span class="expr-badge expr-p-pastoris">P. pastoris</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P97438">UniProt: P97438</a>

<span class="expr-badge">Mus musculus</span>

## Overview

K2P 2.1 (also known as TREK-1, encoded by KCNK2) is a polymodal thermo- and mechanosensitive two-pore domain potassium channel of the TREK subfamily. It generates leak currents that regulate neuronal excitability and responds to lipids, temperature, and mechanical stretch. Unlike other potassium channels, K2P channels use a selectivity filter C-type gate as the principal gating site. Structural studies have revealed a cryptic binding pocket at the P1-M4 intrasubunit interface behind the selectivity filter and have uncovered unprecedented asymmetric, potassium-dependent conformational changes that underlie K2P C-type gating. These include order-disorder transitions in the selectivity filter that encompass SF1 pinching and SF2 dilation, disrupting the S1 and S2 ion binding sites.


## Publications

### doi/10.1038##nature22988

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5vk5">5VK5</a></td>
      <td>3.1 A</td>
      <td>P212121</td>
      <td>K2P 2.1cryst (residues 21-322) with surface mutations K84R, Q85E, T86K, I88L, A89R, Q90A, A92P, N95S, S96D, D797Q, N119A, S300A, E306A; domain-swapped M1 helix, extracellular CAP domain, C-terminal tail (residues 307-321), unimpeded aqueous path between intracellular side and selectivity filter. C-terminal TEV cleavage site and GFP for <a href="/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/">FSEC</a> screening.</td>
      <td>K+ ions at selectivity filter sites S1-S4</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5vkn">5VKN</a></td>
      <td>3.0 A</td>
      <td>P212121</td>
      <td>K2P 2.1cryst same construct as 5VK5, co-crystallized with <a href="/xray-mp-wiki/reagents/ligands/ml335/">ML335 (N-aryl-sulfonamide K2P activator)</a> activator</td>
      <td>K+ ions, <a href="/xray-mp-wiki/reagents/ligands/ml335/">ML335 (N-aryl-sulfonamide K2P activator)</a> (2 molecules per channel)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5vkp">5VKP</a></td>
      <td>2.8 A</td>
      <td>P212121</td>
      <td>K2P 2.1cryst same construct as 5VK5, co-crystallized with <a href="/xray-mp-wiki/reagents/ligands/ml402/">ML402 (thiophene-carboxamide K2P activator)</a> activator</td>
      <td>K+ ions, <a href="/xray-mp-wiki/reagents/ligands/ml402/">ML402 (thiophene-carboxamide K2P activator)</a> (2 molecules per channel)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: K2P 2.1cryst (residues 21-322) with additional C-terminal GFP and His10 tag. Cloned into pPICZ vector. Plasmids linearized with PmeI and transformed into P. pastoris SMD1163H by electroporation. Multi-integration recombinants selected on zeocin plates (1-4 mg/ml).
- **Notes**: Construct K2P 2.1cryst identified through [FSEC](/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/) screening of mutants and deletion constructs expressed in HEK293 cells.

**Purification:**

- **Expression system**: Pichia pastoris SMD1163H
- **Expression construct**: K2P 2.1cryst (residues 21-322), C-terminal GFP-His10 tag
- **Tag info**: C-terminal His10 tag via GFP fusion

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
      <td>Construct screening</td>
      <td><a href="/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/">FSEC</a> (fluorescence-detection size-exclusion chromatography)</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Set of mutants and deletion constructs expressed in HEK293 cells screened for expression level and peak quality using <a href="/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/">FSEC</a>. Construct K2P 2.1cryst identified as optimal.</td>
    </tr>
    <tr>
      <td>Large-scale expression</td>
      <td>Pichia pastoris fermentation in 7L Bioreactor</td>
      <td>--</td>
      <td>Minimal medium (4% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.93 g/l CaSO4·2H2O, 18.2 g/l K2SO4, 14.9 g/l MgSO4·7H2O, 9 g/l (NH4)2SO4, 25 g/l sodium hexametaphosphate, PTM1 trace metals) + --</td>
      <td>Fed-batch phase at 15-30% pump speed until wet cell mass reached ~250 g/l. pH maintained at 5.0 by 30% ammonium hydroxide. pO2 kept at minimum 30%.</td>
    </tr>
    <tr>
      <td>Cell harvesting and membrane preparation</td>
      <td>Centrifugation</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Cells pelleted by centrifugation (3,000g, 10 min, 20C). Membranes prepared for solubilization.</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes solubilized in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> detergent.</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>His10-tag purification.</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM Tris (pH 8.0), 150 mM NaCl + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final sample buffer: 20 mM Tris (pH 8.0), 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>.</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified in 20 mM Tris (pH 8.0), 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified K2P 2.1cryst in 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 20 mM Tris (pH 8.0), 150 mM NaCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>All three structures (unliganded, <a href="/xray-mp-wiki/reagents/ligands/ml335/">ML335 (N-aryl-sulfonamide K2P activator)</a>, <a href="/xray-mp-wiki/reagents/ligands/ml402/">ML402 (thiophene-carboxamide K2P activator)</a>) crystallized in space group P212121 with similar unit cell dimensions. Crystal lattice contacts involve C-terminal tails from adjacent symmetry mates, stabilized by cadmium ions coordinated between His313 residues of adjacent channels. Structures solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a>.</td>
    </tr>
  </tbody>
</table>
### doi/10.1126##sciadv.abc9174

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6w7b">6W7B</a></td>
      <td>3.3-3.9 A</td>
      <td></td>
      <td>K2P 2.1cryst (same construct as 5VK5) crystallized at seven potassium concentrations (0, 1, 10, 30, 50, 100, 200 mM [K+]) and in complex with <a href="/xray-mp-wiki/reagents/ligands/ml335/">ML335 (N-aryl-sulfonamide K2P activator)</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: K2P 2.1cryst (residues 21-322) with additional C-terminal GFP and His10 tag. Cloned into pPICZ vector. Plasmids linearized with PmeI and transformed into P. pastoris SMD1163H by electroporation. Multi-integration recombinants selected on zeocin plates (1-4 mg/ml).
- **Notes**: Construct K2P 2.1cryst identified through [FSEC](/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/) screening of mutants and deletion constructs expressed in HEK293 cells.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified K2P 2.1cryst concentrated to 6 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20-25% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 200 mM KCl, 1 mM CdCl2, 100 mM HEPES (pH 8.0)</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>0.2 ul protein + 0.1 ul precipitant over 100 ul reservoir</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>12 hours to full size (200-300 um) in ~1 week</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Buffer D (200 mM KCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a>, 15 mM HTG, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 1 mM CdCl2, 100 mM HEPES pH 8.0) with 5% step increases of <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> up to 38%. After cryoprotection, crystals incubated for 8 hours in buffer E (38% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a>, 15 mM HTG, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 1 mM CdCl2, 100 mM HEPES pH 8.0) containing appropriate [K+] before freezing.</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structures determined at seven potassium concentrations (0, 1, 10, 30, 50, 100, 200 mM [K+]) and in the presence of <a href="/xray-mp-wiki/reagents/ligands/ml335/">ML335 (N-aryl-sulfonamide K2P activator)</a> activator.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w7b">6W7B</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSFSSKPTVLASRVESDSAINVM</span><span class="topo-inside">KWKTV</span><span class="topo-membrane">STIFLVVVLYLIIGATVFKAL</span><span class="topo-outside">EQPQEISQRTTIVIQREKFLRAHPCVSDQELDELIQQIVAAINAGIIPLGASSNQVSHWDL</span><span class="topo-unknown">GSSFFFAGTV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">ITTIGFG</span><span class="topo-outside">NISPRTE</span><span class="topo-membrane">GGKIFCIIYALLGIPLFGFLLAGVG</span><span class="topo-inside">DQLGTIFGKGIAKVED</span><span class="topo-unknown">TFIKWNVSQT</span><span class="topo-inside">KIRIIST</span><span class="topo-membrane">IIFILFGCVLFVALPAVIF</span><span class="topo-unknown">KHIE</span><span class="topo-outside">GWSA</span><span class="topo-unknown">LDAIYFVVITLTTIGFG</span><span class="topo-outside">DYVA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310  </span>
<span class="topo-line"><span class="topo-outside">GGS</span><span class="topo-unknown">DIEYLDFY</span><span class="topo-outside">K</span><span class="topo-membrane">PVVWFWILVGLAYFAAVLSMIGDWL</span><span class="topo-inside">RVIAKKTKEAVGEFRAHAAEWTANVTS</span><span class="topo-unknown">NSLEVLFQ</span></span>
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
      <td>23</td>
      <td>20</td>
      <td>42</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>28</td>
      <td>43</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>49</td>
      <td>48</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>110</td>
      <td>69</td>
      <td>129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>127</td>
      <td>130</td>
      <td>146</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>128</td>
      <td>134</td>
      <td>147</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>159</td>
      <td>154</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>175</td>
      <td>179</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>185</td>
      <td>195</td>
      <td>204</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>186</td>
      <td>192</td>
      <td>205</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>211</td>
      <td>212</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>215</td>
      <td>231</td>
      <td>234</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>216</td>
      <td>219</td>
      <td>235</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>236</td>
      <td>239</td>
      <td>255</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>237</td>
      <td>243</td>
      <td>256</td>
      <td>262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>251</td>
      <td>263</td>
      <td>270</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>252</td>
      <td>252</td>
      <td>271</td>
      <td>271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>277</td>
      <td>272</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>304</td>
      <td>297</td>
      <td>323</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>312</td>
      <td>324</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6w7b">6W7B</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSFSSKPTVLASRVE</span><span class="topo-inside">SDSAINVMKWKTV</span><span class="topo-membrane">STIFLVVVLYLIIGATVFKA</span><span class="topo-outside">LEQPQEISQRTTIVIQREKFLRAHPCVSDQELDELIQQIVAAINAGIIPLGASSNQVSHWDL</span><span class="topo-unknown">GSSFFFAGTV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">ITTIG</span><span class="topo-outside">F</span><span class="topo-unknown">G</span><span class="topo-outside">NISPRTE</span><span class="topo-membrane">GGKIFCIIYALLGIPLFGFLLAGVG</span><span class="topo-inside">DQLGTIFGKGIAKVEDTFIKWNVSQTKIRIIST</span><span class="topo-membrane">IIFILFGCVLFVALPAVIFKH</span><span class="topo-outside">IEGWSA</span><span class="topo-unknown">LDAIYFVVITLTTIG</span><span class="topo-outside">F</span><span class="topo-unknown">GDY</span><span class="topo-outside">VA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310  </span>
<span class="topo-line"><span class="topo-outside">GGSD</span><span class="topo-unknown">IEYL</span><span class="topo-outside">D</span><span class="topo-membrane">FYKPVVWFWILVGLAYFAAVLSMIGDWL</span><span class="topo-inside">RVIAKKTKEAVGEFRAHA</span><span class="topo-unknown">AEWTANVTSNSLEVLFQ</span></span>
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
      <td>15</td>
      <td>20</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>16</td>
      <td>28</td>
      <td>35</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>48</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>110</td>
      <td>68</td>
      <td>129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>125</td>
      <td>130</td>
      <td>144</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>126</td>
      <td>126</td>
      <td>145</td>
      <td>145</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>127</td>
      <td>146</td>
      <td>146</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>128</td>
      <td>134</td>
      <td>147</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>159</td>
      <td>154</td>
      <td>178</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>192</td>
      <td>179</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>213</td>
      <td>212</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>219</td>
      <td>233</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>234</td>
      <td>239</td>
      <td>253</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>235</td>
      <td>235</td>
      <td>254</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>238</td>
      <td>255</td>
      <td>257</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>239</td>
      <td>244</td>
      <td>258</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>248</td>
      <td>264</td>
      <td>267</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>249</td>
      <td>249</td>
      <td>268</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>277</td>
      <td>269</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>295</td>
      <td>297</td>
      <td>314</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>312</td>
      <td>315</td>
      <td>331</td>
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

### Asymmetric order-disorder transitions in K2P C-type gating

Low potassium concentrations evoke asymmetric conformational changes in the K2P 2.1 selectivity filter. SF1 undergoes pinching at its extracellular side, exposing Asn147 side chains. SF2 and the SF2-M4 loop undergo unwinding and dilation. These changes destroy the S1 and S2 ion binding sites while S3 and S4 sites persist. The two classes of C-type gating (SF1 pinching and SF2 dilation) operate simultaneously in one channel, leveraging the fundamentally heterodimeric K2P architecture.

### M3 glutamate network supports SF2-M4 loop stability

A conserved hydrogen bond network centered on Glu234 (M3 helix), Gly260 (SF2-M4 loop backbone amide), and Tyr270 (M4) supports the SF2-M4 loop structure. Disruption of this network (E234Q, Y270F mutants) enhances C-type gating and blunts responses to temperature, pressure, and [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/) activation. The network is conserved across K2P subfamilies including K2P 3.1 (TASK-1).

### ML335 stabilizes the C-type gate by rigidifying the P1-M4 interface

The K2P activator [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/) binds to the P1-M4 intrasubunit interface ([K2P Modulator Pocket](/xray-mp-wiki/concepts/miscellaneous/k2p-modulator-pocket/)) and stabilizes the SF2-M4 loop. ML335-bound structures show canonical selectivity filter conformations with ions at all four sites (S1-S4) at all potassium concentrations tested. [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/) increases the strength of the Glu234 hydrogen bonding network and suppresses potassium-dependent loop dynamics. Single-channel recordings show [ML335 (N-aryl-sulfonamide K2P activator)](/xray-mp-wiki/reagents/ligands/ml335/) increases open probability.

### SF2-M4 loop integrates diverse gating cues

The uniquely long K2P SF2-M4 loop (6-8 residues longer than canonical potassium channel loops) transduces gating signals from temperature, pressure, and intracellular C-terminal tail to the selectivity filter C-type gate. Shortening the SF2-M4 loop (Loop2sym6 mutant) or disrupting the Glu234 network blunts responses to these stimuli. The loop is a central element of K2P gating and a target for modulator development.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/ml335/">ML335 (N-aryl-sulfonamide K2P activator)</a> — K2P 2.1 activator co-crystallized (PDB 5VKN, this paper); stabilizes C-type gate by rigidifying P1-M4 interface
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/">C-type Inactivation</a> — K2P channels use C-type gate as principal gating site; this paper reveals asymmetric SF1 pinching and SF2 dilation mechanisms
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA Potassium Channel</a> — Homotetrameric model system; SF1 pinching mechanism of C-type gating shared with K2P channels
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/traak/">Human TRAAK Potassium Channel (K2P 4.1)</a> — K2P family member; SF2-M4 loop length comparison across K2P subtypes
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/k2p2-1/">Human K2P2.1 (TREK-1) Potassium Channel I110D Mutant</a> — Alternative K2P2.1 construct; RuR inhibition independent of C-type gate activation
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/human-task-1-k2p3-1/">Human TASK-1 (K2P 3.1)</a> — K2P subfamily; M3 glutamate network conserved (Glu182, Tyr220); Y220F mutation destabilizes C-type gate
- <a href="/xray-mp-wiki/concepts/miscellaneous/k2p-modulator-pocket/">K2P Modulator Pocket</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/quality-assessment/fluorescence-size-exclusion-chromatography/">FSEC</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
