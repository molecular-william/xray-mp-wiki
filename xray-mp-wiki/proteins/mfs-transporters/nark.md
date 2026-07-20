---
title: "NarK Nitrate/Nitrite Antiporter from Escherichia coli"
created: 2026-06-05
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12139, doi/10.1038##ncomms8097]
verified: agent
uniprot_id: P10903
---

# NarK Nitrate/Nitrite Antiporter from Escherichia coli

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P10903">UniProt: P10903</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

NarK is a nitrate/nitrite antiporter from the nitrate/nitrite porter (NNP) family in the major facilitator superfamily (MFS). The first crystal structure of NarK (Zheng, Wisedchaisri & Gonen, 2013, Nature) was determined at 2.6 A resolution in complex with a Fab antibody fragment, revealing an inward-facing conformation with a positively charged substrate-translocation pathway lacking protonatable residues, providing the first evidence that NarK functions as a nitrate/nitrite exchanger without proton co-transport. Two conserved arginine residues (R89, R305) form the substrate-binding pocket, capped by phenylalanines (F147, F267). Nitrite-bound structures at 2.8 A showed conformational changes in R305 upon substrate binding. Later higher-resolution structures (Coudray et al., 2016) captured inward-open, occluded, and outward-open conformations, revealing the complete alternating access transport cycle.
NarK plays a central role in nitrate uptake and nitrite extrusion in Escherichia coli, functioning as a nitrate/nitrite antiporter that couples substrate recognition to the transport cycle through concomitant
movement of transmembrane helices and key residues in the substrate-binding site. NarK comprises 12 transmembrane helices with pseudo twofold symmetry and adopts inward-open, occluded, and outward-open conformations during the alternating access transport cycle.


## Publications

### doi/10.1038##nature12139

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4jr9">4JR9</a></td>
      <td>2.60</td>
      <td>not specified</td>
      <td>Full-length E. coli NarK (strain K12) co-crystallized with Fab antibody fragment (hybridoma line 4G5, IgG2a, kappa)</td>
      <td>none (apo, inward-facing conformation)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4jr9">4JR9</a></td>
      <td>2.80</td>
      <td>not specified</td>
      <td>NarK-Fab complex crystal soaked in buffer containing 50 mM sodium nitrite</td>
      <td>nitrite (NO2-)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3) C41 (for nature12139) or E. coli C41(DE3) Delta ACRB (for ncomms8097)
- **Construct**: Full-length NarK from E. coli K12, pET15b with N-terminal 8x His-tag and thrombin cleavage site (nature12139) or pET-modified with N-terminal His8-GFP tag (ncomms8097)
- **Induction**: 0.3 mM IPTG at 37 C for 4-5 h (nature12139); 0.5 mM IPTG at 20 C for 24 h (ncomms8097)

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
      <td>1. Membrane preparation</td>
      <td><a href="/xray-mp-wiki/methods/purification/ultracentrifugation">Ultracentrifugation</a></td>
      <td>not applicable</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a>-HCl pH 8, 150 mM NaCl, 1 mM PMSF</td>
      <td>30 min at 15,000g to remove debris, then 1 h at 130,000g to pellet membranes. Pellets resuspended and frozen at -80 C until use.</td>
    </tr>
    <tr>
      <td>2. Solubilization</td>
      <td>Detergent solubilization</td>
      <td>not applicable</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a>-HCl pH 8, 150 mM NaCl + 1% n-decyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>4 C for 2 h. After addition of 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">imidazole</a>, clarified by centrifugation.</td>
    </tr>
    <tr>
      <td>3. <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a>-HCl pH 8, 150 mM NaCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Wash with 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">imidazole</a>, elution with 250 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">imidazole</a> in same buffer.</td>
    </tr>
    <tr>
      <td>4. Thrombin cleavage and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>Thrombin digestion + <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">gel filtration</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a>-HCl pH 8, 150 mM NaCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His-tag</a> removed by thrombin digestion at 1:1000 enzyme:protein molar ratio, 4 C overnight. Final <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">gel filtration</a> in <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a>.</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified NarK in 0.2% DM buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion">Hanging-drop vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>NarK-Fab complex at 5.8 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a>-HCl pH 8, 150 mM NaCl, 0.2% DM</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M citric acid pH 3.5, 0.1 M NaCl, 0.1 M Li2SO4, 28% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a>400</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>not specified</td>
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
      <td>30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a>400 in reservoir solution for 5 min before flash freezing</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Fab antibody fragment produced from mouse monoclonal IgG (hybridoma line 4G5, IgG2a, kappa). Initial NarK crystals gave anisotropic diffraction to 4-6 A. Only NarK-Fab complex gave high-quality crystals diffracting to ~2.5 A. Data collected at ALS beamline 8.2.2. Nitrite-bound crystals obtained by soaking in 50 mM sodium nitrite overnight before freezing. Nitrate soaking deteriorated crystal packing.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4jr9">4JR9</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSHMSHSSAPERAT</span><span class="topo-outside">GAVITDWRPEDPAFWQQRGQRIASRNLWI</span><span class="topo-membrane">SVPCLLLAFCVWMLFSA</span><span class="topo-inside">VAVNLPKVGFNFTTDQLFM</span><span class="topo-membrane">LTALPSVSGALLRVPYS</span><span class="topo-outside">FMVPIFGGRRW</span><span class="topo-membrane">TAFSTGILIIPCV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">WLG</span><span class="topo-inside">FAVQDTSTPYSVFI</span><span class="topo-membrane">IISLLCGFAGANFASS</span><span class="topo-outside">MANISFFFPKQKQGGALGL</span><span class="topo-membrane">NGGLGNMGVSVMQLVAPLV</span><span class="topo-inside">VS</span><span class="topo-unknown">LSIFAVFGSQGVKQPDGTELY</span><span class="topo-inside">LAN</span><span class="topo-membrane">ASWIWVPFLAIFTIAAW</span><span class="topo-outside">FGMNDL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">A</span><span class="topo-unknown">TSKASIKEQLPVLKRGH</span><span class="topo-outside">LW</span><span class="topo-membrane">IMSLLYLATFGSFIGFSAGF</span><span class="topo-inside">AMLSKTQFPDVQILQ</span><span class="topo-membrane">YAFFGPFIGALARSAGG</span><span class="topo-outside">ALSDRLGGT</span><span class="topo-membrane">RVTLVNFILMAIFSGLL</span><span class="topo-inside">FLTLPTDGQGGSFMAFF</span><span class="topo-membrane">AVFLA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460      </span>
<span class="topo-line"><span class="topo-membrane">LFLTAGLGSGSTF</span><span class="topo-outside">QMISVIFRKLTMDRVKAEGGSDERAMREAATDTAAALG</span><span class="topo-membrane">FISAIGAIGGFFIPKA</span><span class="topo-inside">FGSSLALTGSPVGA</span><span class="topo-membrane">MKVFLIFYIACVVITWAV</span><span class="topo-outside">YG</span><span class="topo-unknown">RHSKK</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>14</td>
      <td>-2</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>43</td>
      <td>12</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>60</td>
      <td>41</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>79</td>
      <td>58</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>96</td>
      <td>77</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>107</td>
      <td>94</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>123</td>
      <td>105</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>124</td>
      <td>137</td>
      <td>121</td>
      <td>134</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>153</td>
      <td>135</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>172</td>
      <td>151</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>191</td>
      <td>170</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>193</td>
      <td>189</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>214</td>
      <td>191</td>
      <td>211</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>215</td>
      <td>217</td>
      <td>212</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>215</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>241</td>
      <td>232</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>258</td>
      <td>239</td>
      <td>255</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>259</td>
      <td>260</td>
      <td>256</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>280</td>
      <td>258</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>295</td>
      <td>278</td>
      <td>292</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>312</td>
      <td>293</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>321</td>
      <td>310</td>
      <td>318</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>338</td>
      <td>319</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>339</td>
      <td>355</td>
      <td>336</td>
      <td>352</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>373</td>
      <td>353</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>411</td>
      <td>371</td>
      <td>408</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>427</td>
      <td>409</td>
      <td>424</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>441</td>
      <td>425</td>
      <td>438</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>459</td>
      <td>439</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>460</td>
      <td>461</td>
      <td>457</td>
      <td>458</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>462</td>
      <td>466</td>
      <td>459</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4jr9">4JR9</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSHMSHSSAPERAT</span><span class="topo-outside">GAVITDWRPEDPAFWQQRGQRIASRNLWI</span><span class="topo-membrane">SVPCLLLAFCVWMLFSA</span><span class="topo-inside">VAVNLPKVGFNFTTDQLFM</span><span class="topo-membrane">LTALPSVSGALLRVPYS</span><span class="topo-outside">FMVPIFGGRRW</span><span class="topo-membrane">TAFSTGILIIPCV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">WLG</span><span class="topo-inside">FAVQDTSTPYSVFI</span><span class="topo-membrane">IISLLCGFAGANFASS</span><span class="topo-outside">MANISFFFPKQKQGGALGL</span><span class="topo-membrane">NGGLGNMGVSVMQLVAPLV</span><span class="topo-inside">VS</span><span class="topo-unknown">LSIFAVFGSQGVKQPDGTELY</span><span class="topo-inside">LAN</span><span class="topo-membrane">ASWIWVPFLAIFTIAAW</span><span class="topo-outside">FGMNDL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">A</span><span class="topo-unknown">TSKASIKEQLPVLKRGH</span><span class="topo-outside">LW</span><span class="topo-membrane">IMSLLYLATFGSFIGFSAGF</span><span class="topo-inside">AMLSKTQFPDVQILQ</span><span class="topo-membrane">YAFFGPFIGALARSAGG</span><span class="topo-outside">ALSDRLGGT</span><span class="topo-membrane">RVTLVNFILMAIFSGLL</span><span class="topo-inside">FLTLPTDGQGGSFMAFF</span><span class="topo-membrane">AVFLA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460      </span>
<span class="topo-line"><span class="topo-membrane">LFLTAGLGSGSTF</span><span class="topo-outside">QMISVIFRKLTMDRVKAEGGSDERAMREAATDTAAALG</span><span class="topo-membrane">FISAIGAIGGFFIPKA</span><span class="topo-inside">FGSSLALTGSPVGA</span><span class="topo-membrane">MKVFLIFYIACVVITWAV</span><span class="topo-outside">YG</span><span class="topo-unknown">RHSKK</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>14</td>
      <td>-2</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>43</td>
      <td>12</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>60</td>
      <td>41</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>79</td>
      <td>58</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>96</td>
      <td>77</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>107</td>
      <td>94</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>123</td>
      <td>105</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>124</td>
      <td>137</td>
      <td>121</td>
      <td>134</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>153</td>
      <td>135</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>172</td>
      <td>151</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>191</td>
      <td>170</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>193</td>
      <td>189</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>214</td>
      <td>191</td>
      <td>211</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>215</td>
      <td>217</td>
      <td>212</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>215</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>241</td>
      <td>232</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>258</td>
      <td>239</td>
      <td>255</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>259</td>
      <td>260</td>
      <td>256</td>
      <td>257</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>280</td>
      <td>258</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>295</td>
      <td>278</td>
      <td>292</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>312</td>
      <td>293</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>321</td>
      <td>310</td>
      <td>318</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>338</td>
      <td>319</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>339</td>
      <td>355</td>
      <td>336</td>
      <td>352</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>373</td>
      <td>353</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>374</td>
      <td>411</td>
      <td>371</td>
      <td>408</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>412</td>
      <td>427</td>
      <td>409</td>
      <td>424</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>441</td>
      <td>425</td>
      <td>438</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>459</td>
      <td>439</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>460</td>
      <td>461</td>
      <td>457</td>
      <td>458</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>462</td>
      <td>466</td>
      <td>459</td>
      <td>463</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##ncomms8097

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u4v">4U4V</a></td>
      <td>\'2.35\'</td>
      <td>P2_12_12_1</td>
      <td>Full-length E. coli NarK (GI: 945783, residues 1-427) from strain K-12 MG1655, N-terminal His8-GFP tag cleaved</td>
      <td>none (apo inward-open state)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u4v">4U4V</a></td>
      <td>\'2.4\'</td>
      <td>P2_12_12_1</td>
      <td>Full-length E. coli NarK with nitrate bound</td>
      <td>nitrate ion (NO3-)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u4v">4U4V</a></td>
      <td>\'2.4\'</td>
      <td>P2_12_12_1</td>
      <td>Full-length E. coli NarK with nitrate bound</td>
      <td>nitrate ion (NO3-)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3) C41 (for nature12139) or E. coli C41(DE3) Delta ACRB (for ncomms8097)
- **Construct**: Full-length NarK from E. coli K12, pET15b with N-terminal 8x His-tag and thrombin cleavage site (nature12139) or pET-modified with N-terminal His8-GFP tag (ncomms8097)
- **Induction**: 0.3 mM IPTG at 37 C for 4-5 h (nature12139); 0.5 mM IPTG at 20 C for 24 h (ncomms8097)

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
      <td><a href="/xray-mp-wiki/methods/cell-lysis/french-press/">Microfluidizer</a> processor (Microfluidics) at 15,000 p.s.i., three passages</td>
      <td>not applicable</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 20 mM NaNO3, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf">PMSF</a>, 4 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a></td>
      <td>Centrifugation at 12,000g, 30 min, 4 C to remove debris</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td><a href="/xray-mp-wiki/methods/purification/ultracentrifugation">Ultracentrifugation</a></td>
      <td>not applicable</td>
      <td>Same as lysis buffer</td>
      <td>138,000g, 1 h, 4 C to pellet membranes</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>not applicable</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 20 mM NaNO3, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf">PMSF</a>, 4 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a> + 2% n-dodecyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>), 0.4% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">cholesteryl hemisuccinate</a> (<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>)</td>
      <td>30 min at 4 C, <a href="/xray-mp-wiki/methods/purification/ultracentrifugation">ultracentrifugation</a> at 138,000g, 30 min</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a> Superflow](/xray-mp-wiki/reagents/additives/nickel-nta/) (Qiagen), 10 ml</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 25 mM NaNO3, 4 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Binding 2 h; wash with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>; elution with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> at 4 C</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Protease cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) column (10 ml)</td>
      <td></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His-tag</a>ged tobacco etch virus protease (produced in-house) cleaved <a href="/xray-mp-wiki/reagents/protein-tags/gfp/">GFP</a>-His8 tag; protease retained on column</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td>HiLoad 16/600 <a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200</a> pg column (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 25 mM NaNO3, 4 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Final sample concentrated to 15-20 mg/ml</td>
    </tr>
  </tbody>
</table>
**Final sample**: 15-20 mg/ml

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion">Sitting-drop vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified NarK, 15-20 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>not specified in paper</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>not specified</td>
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
      <td>Notes</td>
      <td>Three crystal structures determined (apo inward-open, nitrate-bound inward-open, nitrate-bound occluded); all in P212121 space group; X-ray source: SPring-8 BL32XU</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u4v">4U4V</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSHSSAPERATG</span><span class="topo-inside">AVITDWRPEDPAFWQQRGQRIASRNLW</span><span class="topo-membrane">ISVPCLLLAFCVWMLFS</span><span class="topo-outside">AVAVNLPKVGFNFTTDQLFML</span><span class="topo-membrane">TALPSVSGALLRVPY</span><span class="topo-inside">SFMVPIFGGRRW</span><span class="topo-membrane">TAFSTGILIIPCVWL</span><span class="topo-outside">G</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FAVQDTSTPYSVF</span><span class="topo-membrane">IIISLLCGFAGANFASS</span><span class="topo-inside">MANISFFFPKQKQGGAL</span><span class="topo-membrane">GLNGGLGNMGVSVMQLVA</span><span class="topo-outside">PLVVSLSIFAVFGSQGVKQPDGTELYLANA</span><span class="topo-membrane">SWIWVPFLAIFTIAA</span><span class="topo-inside">WFGMNDLAT</span><span class="topo-unknown">S</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">KASIKEQ</span><span class="topo-inside">LPVLKRGHL</span><span class="topo-membrane">WIMSLLYLATFGSFIGFSA</span><span class="topo-outside">GFAMLSKTQFPDVQILQYA</span><span class="topo-membrane">FFGPFIGALARSAGGALS</span><span class="topo-inside">DRLG</span><span class="topo-membrane">GTRVTLVNFILMAIFS</span><span class="topo-outside">GLLFLTLPTD</span><span class="topo-unknown">G</span><span class="topo-outside">QGGSFMAFFAV</span><span class="topo-membrane">FLALFL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470     </span>
<span class="topo-line"><span class="topo-membrane">TAGLGSGSTF</span><span class="topo-inside">QMISVIFRKLTMDRVKAEGGSDERAMREAATDTAAALG</span><span class="topo-membrane">FISAIGAIGGFFIP</span><span class="topo-outside">KAFGSSLALTGSPVGAMK</span><span class="topo-membrane">VFLIFYIACVVITWAVY</span><span class="topo-inside">GRHSKK</span><span class="topo-unknown">LESSGENLYFQG</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>39</td>
      <td>13</td>
      <td>39</td>
      <td>Inside</td>
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
      <td>77</td>
      <td>57</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>92</td>
      <td>78</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>104</td>
      <td>93</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>119</td>
      <td>105</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>133</td>
      <td>120</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>150</td>
      <td>134</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>167</td>
      <td>151</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>185</td>
      <td>168</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>215</td>
      <td>186</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>230</td>
      <td>216</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>239</td>
      <td>231</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>247</td>
      <td>240</td>
      <td>247</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>248</td>
      <td>256</td>
      <td>248</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>275</td>
      <td>257</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>312</td>
      <td>295</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>316</td>
      <td>313</td>
      <td>316</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>332</td>
      <td>317</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>342</td>
      <td>333</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>343</td>
      <td>343</td>
      <td>343</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>344</td>
      <td>354</td>
      <td>344</td>
      <td>354</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>355</td>
      <td>370</td>
      <td>355</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>371</td>
      <td>408</td>
      <td>371</td>
      <td>408</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>422</td>
      <td>409</td>
      <td>422</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>440</td>
      <td>423</td>
      <td>440</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>457</td>
      <td>441</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>458</td>
      <td>463</td>
      <td>458</td>
      <td>463</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>464</td>
      <td>475</td>
      <td>464</td>
      <td>475</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u4v">4U4V</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSHSSAPERATG</span><span class="topo-inside">AVITDWRPEDPAFWQQRGQRIASRNLW</span><span class="topo-membrane">ISVPCLLLAFCVWMLFS</span><span class="topo-outside">AVAVNLPKVGFNFTTDQLFML</span><span class="topo-membrane">TALPSVSGALLRVPY</span><span class="topo-inside">SFMVPIFGGRRW</span><span class="topo-membrane">TAFSTGILIIPCVWL</span><span class="topo-outside">G</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FAVQDTSTPYSVF</span><span class="topo-membrane">IIISLLCGFAGANFASS</span><span class="topo-inside">MANISFFFPKQKQGGAL</span><span class="topo-membrane">GLNGGLGNMGVSVMQLVA</span><span class="topo-outside">PLVVSLSIFAVFGSQGVKQPDGTELYLANA</span><span class="topo-membrane">SWIWVPFLAIFTIAA</span><span class="topo-inside">WFGMNDLAT</span><span class="topo-unknown">S</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">KASIKEQ</span><span class="topo-inside">LPVLKRGHL</span><span class="topo-membrane">WIMSLLYLATFGSFIGFSA</span><span class="topo-outside">GFAMLSKTQFPDVQILQYA</span><span class="topo-membrane">FFGPFIGALARSAGGALS</span><span class="topo-inside">DRLG</span><span class="topo-membrane">GTRVTLVNFILMAIFS</span><span class="topo-outside">GLLFLTLPTD</span><span class="topo-unknown">G</span><span class="topo-outside">QGGSFMAFFAV</span><span class="topo-membrane">FLALFL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470     </span>
<span class="topo-line"><span class="topo-membrane">TAGLGSGSTF</span><span class="topo-inside">QMISVIFRKLTMDRVKAEGGSDERAMREAATDTAAALG</span><span class="topo-membrane">FISAIGAIGGFFIP</span><span class="topo-outside">KAFGSSLALTGSPVGAMK</span><span class="topo-membrane">VFLIFYIACVVITWAVY</span><span class="topo-inside">GRHSKK</span><span class="topo-unknown">LESSGENLYFQG</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>39</td>
      <td>13</td>
      <td>39</td>
      <td>Inside</td>
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
      <td>77</td>
      <td>57</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>92</td>
      <td>78</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>104</td>
      <td>93</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>119</td>
      <td>105</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>133</td>
      <td>120</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>150</td>
      <td>134</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>167</td>
      <td>151</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>185</td>
      <td>168</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>215</td>
      <td>186</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>230</td>
      <td>216</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>239</td>
      <td>231</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>247</td>
      <td>240</td>
      <td>247</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>248</td>
      <td>256</td>
      <td>248</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>275</td>
      <td>257</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>312</td>
      <td>295</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>316</td>
      <td>313</td>
      <td>316</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>332</td>
      <td>317</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>342</td>
      <td>333</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>343</td>
      <td>343</td>
      <td>343</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>344</td>
      <td>354</td>
      <td>344</td>
      <td>354</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>355</td>
      <td>370</td>
      <td>355</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>371</td>
      <td>408</td>
      <td>371</td>
      <td>408</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>422</td>
      <td>409</td>
      <td>422</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>440</td>
      <td>423</td>
      <td>440</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>457</td>
      <td>441</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>458</td>
      <td>463</td>
      <td>458</td>
      <td>463</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>464</td>
      <td>475</td>
      <td>464</td>
      <td>475</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u4v">4U4V</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSHSSAPERATG</span><span class="topo-inside">AVITDWRPEDPAFWQQRGQRIASRNLW</span><span class="topo-membrane">ISVPCLLLAFCVWMLFS</span><span class="topo-outside">AVAVNLPKVGFNFTTDQLFML</span><span class="topo-membrane">TALPSVSGALLRVPY</span><span class="topo-inside">SFMVPIFGGRRW</span><span class="topo-membrane">TAFSTGILIIPCVWL</span><span class="topo-outside">G</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FAVQDTSTPYSVF</span><span class="topo-membrane">IIISLLCGFAGANFASS</span><span class="topo-inside">MANISFFFPKQKQGGAL</span><span class="topo-membrane">GLNGGLGNMGVSVMQLVA</span><span class="topo-outside">PLVVSLSIFAVFGSQGVKQPDGTELYLANA</span><span class="topo-membrane">SWIWVPFLAIFTIAA</span><span class="topo-inside">WFGMNDLAT</span><span class="topo-unknown">S</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">KASIKEQ</span><span class="topo-inside">LPVLKRGHL</span><span class="topo-membrane">WIMSLLYLATFGSFIGFSA</span><span class="topo-outside">GFAMLSKTQFPDVQILQYA</span><span class="topo-membrane">FFGPFIGALARSAGGALS</span><span class="topo-inside">DRLG</span><span class="topo-membrane">GTRVTLVNFILMAIFS</span><span class="topo-outside">GLLFLTLPTD</span><span class="topo-unknown">G</span><span class="topo-outside">QGGSFMAFFAV</span><span class="topo-membrane">FLALFL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470     </span>
<span class="topo-line"><span class="topo-membrane">TAGLGSGSTF</span><span class="topo-inside">QMISVIFRKLTMDRVKAEGGSDERAMREAATDTAAALG</span><span class="topo-membrane">FISAIGAIGGFFIP</span><span class="topo-outside">KAFGSSLALTGSPVGAMK</span><span class="topo-membrane">VFLIFYIACVVITWAVY</span><span class="topo-inside">GRHSKK</span><span class="topo-unknown">LESSGENLYFQG</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>39</td>
      <td>13</td>
      <td>39</td>
      <td>Inside</td>
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
      <td>77</td>
      <td>57</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>92</td>
      <td>78</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>104</td>
      <td>93</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>119</td>
      <td>105</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>133</td>
      <td>120</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>150</td>
      <td>134</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>167</td>
      <td>151</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>185</td>
      <td>168</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>215</td>
      <td>186</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>230</td>
      <td>216</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>239</td>
      <td>231</td>
      <td>239</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>247</td>
      <td>240</td>
      <td>247</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>248</td>
      <td>256</td>
      <td>248</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>275</td>
      <td>257</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>294</td>
      <td>276</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>312</td>
      <td>295</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>316</td>
      <td>313</td>
      <td>316</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>332</td>
      <td>317</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>342</td>
      <td>333</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>343</td>
      <td>343</td>
      <td>343</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>344</td>
      <td>354</td>
      <td>344</td>
      <td>354</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>355</td>
      <td>370</td>
      <td>355</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>371</td>
      <td>408</td>
      <td>371</td>
      <td>408</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>422</td>
      <td>409</td>
      <td>422</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>440</td>
      <td>423</td>
      <td>440</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>457</td>
      <td>441</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>458</td>
      <td>463</td>
      <td>458</td>
      <td>463</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>464</td>
      <td>475</td>
      <td>464</td>
      <td>475</td>
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

### First structure of a nitrate/nitrite transport protein

The 2013 NarK structure (Zheng, Wisedchaisri & Gonen) was the first crystal structure of any nitrate transport protein. The structure revealed a positively charged substrate-translocation pathway with no protonatable residues (glutamates, aspartates, histidines) on transmembrane helices, providing the first structural evidence that NarK functions as a nitrate/nitrite exchanger without proton co-transport. Surface electrostatic potential calculations showed the pathway is highly positively charged, attracting anions while forming a formidable barrier for proton translocation. This contrasts with other MFS members (LacY, GlpT, FucP) that use acidic residues for proton coupling. (DOI: 10.1038/nature12139)

### Substrate-binding pocket defined by conserved arginines

The substrate-binding pocket is formed by two absolutely conserved arginine residues R89 (TM2) and R305 (TM8) positioned at the center of NarK, capped by F147 and F267. In the nitrite-bound structure (2.8 A), nitrite binds in-plane with both arginines, stabilized by pi-electron delocalization among arginine and phenylalanine side chains. R305 undergoes a conformational change upon substrate binding, disrupting the inter-domain hydrogen bond network involving Y263 and G171. Key residues are stabilized by inter-domain hydrogen bonds: Y263 (C-domain) and G171 (N-domain) bond with R305; G144 (N-domain) and S411 (C-domain) bond with R89. (DOI: 10.1038/nature12139)

### Rocker switch mechanism without proton coupling

The proposed mechanism for nitrate/nitrite exchange is based on the rocker switch model. NarK cycles through outward-facing, occluded, and inward-facing conformations. Substrate binding and release are coupled to breaking and reforming of inter-domain hydrogen bonds involving R89 and R305. Unlike other MFS members, NarK contains no acidic residues in its pore, so salt bridges form only between protein and substrate, not between protein residues. The rocking motion is driven by inter-domain hydrogen bond networks at the substrate-binding pocket. This is consistent with the conserved nitrate signature (NS) motifs: NS1 (164-GGALGLNGGLGN-175 on TM5) and NS2 (408-GFISAIGAIGGFF-420 on TM11). (DOI: 10.1038/nature12139)

### NarK is a nitrate/nitrite antiporter

In vitro reconstituted liposome-based nitrite-flux assay demonstrated that NarK functions as a nitrate/nitrite antiporter. Nitrite influx was driven by a nitrate concentration gradient across the membrane at pH 7 with membrane potential present. Substrate specificity showed nitrate and nitrite transport but not chloride, carbonate, formate, [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate), or propionate as counteranions, indicating tight coupling without transport in absence of counteranions.

### Nitrate recognition in the substrate-binding site

The substrate-binding site is formed by F49, R89, F147, N175, Y263, F267, and R305. Nitrate is sandwiched between F147 and F267 forming pi-pi stacking interactions. R89 forms a bidentate salt bridge with nitrate oxygen atoms. Y263 forms a bifurcated hydrogen bond with nitrate oxygen atoms. R305 guanidinium group is oriented perpendicularly to the substrate. These residues are highly conserved among NNP family transporters.

### Alternating access via TM helix bending

The transport cycle involves conformational changes between inward-open, occluded, and outward-open states. TM7, TM10, and TM11 in the C bundle bend at conserved Gly residues (G268 in TM7; G363, G365, G367, G408, G414, G417, [G418](/xray-mp-wiki/reagents/additives/g418) in TM10/11) during the transition from occluded to inward-open state. TM10 and TM11 cytosolic halves rotate 31 and 26 degrees away from the transporter center. TM7 rotates 18 degrees toward the periphery. These Gly residues are strictly conserved in NNP family transporters.

### Coupling mechanism between substrate recognition and conformational change

In the nitrate-bound occluded state, the negative charge of nitrate relaxes the electrostatic repulsion between R89 and R305. Transition to inward-open state induces TM bending, enlarging the substrate-binding site volume from 37.6 A^3 to 50.5 A^3, decreasing nitrate affinity and facilitating release. Y263 and R305 are the key coupling residues; Y263F and R305K mutants completely abolish transport activity. The electrostatic repulsion between R89 and R305 prevents premature closure of the transport pathway.

### Structural basis for tight coupling

[Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate) and propionate ions do not facilitate nitrate uptake, likely because their bulky methyl and ethyl groups prevent interaction with the narrow substrate binding site. This confirms NarK is a tightly coupled antiporter that does not transport substrates in the absence of counteranions. MD simulations showed the apo occluded state spontaneously transitions toward inward-open conformation within 10 ns when nitrate is absent, confirming the coupling mechanism.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/nnp-family/">Nitrate/Nitrite Porter (NNP) Family</a> — NarK belongs to the NNP family of the major facilitator superfamily
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — NarK is a member of the MFS superfamily
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — NarK operates via alternating access between inward-open, occluded, and outward-open states
- <a href="/xray-mp-wiki/proteins/mfs-transporters/naru/">NarU Nitrate/Nitrite Antiporter from Escherichia coli</a> — Related NNP family member with 75% sequence similarity to NarK
- <a href="/xray-mp-wiki/reagents/detergents/n-dodecyl-beta-d-maltopyranoside/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for NarK membrane solubilization
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — Lipid stabilizer used with DDM for NarK solubilization
- <a href="/xray-mp-wiki/reagents/additives/iptg">IPTG</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/g418">G418</a> — Entity mentioned in text
