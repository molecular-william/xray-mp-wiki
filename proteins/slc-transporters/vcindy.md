---
title: "VcINDY Sodium-Dependent Dicarboxylate Transporter"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11542, doi/10.1038##ncomms15009]
verified: false
---

# VcINDY Sodium-Dependent Dicarboxylate Transporter

## Overview

VcINDY is a sodium-dependent dicarboxylate transporter from Vibrio cholerae, belonging to the [Divalent Anion/Na+ Symporter (DASS) Family](/xray-mp-wiki/concepts/transport-mechanisms/dass-family/). It is a homologue of the mammalian SLC13 transporters (NaCT, NaDC1, NaDC3) and the Drosophila INDY (I'm Not Dead Yet) protein. VcINDY catalyzes the Na+-coupled uptake of di- and tricarboxylates such as [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) and [Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/). The 3.2 A crystal structure of VcINDY revealed an inward-facing conformation with one [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) molecule and one sodium ion bound per protomer. Higher resolution 2.8 A structures of succinate- and citrate-bound VcINDY later identified a second Na+-binding site (Na2) and elucidated how DASS proteins recognize and distinguish between C4-dicarboxylate and C6-tricarboxylate substrates.


## Publications

### doi/10.1038##nature11542

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4f35">4F35</a></td>
      <td>3.2 A</td>
      <td>C2</td>
      <td>N-terminal 10X His-tagged VcINDY</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-AI
- **Construct**: N-terminal 10X His-tagged VcINDY in modified pET vector
- **Notes**: Seleno-[L-Methionine](/xray-mp-wiki/reagents/ligands/l-methionine/) (SeMet) protein produced in E. coli B834DE3 cells grown in minimal media containing SeMet. For ncomms15009, proteins expressed with N-terminal cleavable deca-histidine tag in modified pET28b vector; site-directed mutagenesis by QuikChange method.

**Purification:**

- **Expression system**: E. coli BL21-AI
- **Expression construct**: N-terminal 10X His-tagged VcINDY

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
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>1.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-β-D-maltoside</a> (DM)</td>
      <td>Membranes solubilized in 1.2% DM</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt affinity (IMAC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> (Clontech)</td>
      <td>50 mM Tris pH 7.5, 100 mM NaCl, 50 mM <a href="/xray-mp-wiki/reagents/additives/lithium-citrate/">Lithium Citrate</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.15% DM</td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td>Shodex KW804 (HPLC)</td>
      <td>50 mM Tris pH 7.5, 100 mM NaCl, 50 mM <a href="/xray-mp-wiki/reagents/additives/lithium-citrate/">Lithium Citrate</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.15% DM</td>
      <td>Preparative SEC in same buffer</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Size-exclusion purified VcINDY in 50 mM Tris pH 7.5, 100 mM NaCl, 50 mM <a href="/xray-mp-wiki/reagents/additives/lithium-citrate/">Lithium Citrate</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.15% DM</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>29% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 1000, 50 mM <a href="/xray-mp-wiki/reagents/additives/lithium-citrate/">Lithium Citrate</a>, 50 mM MOPS pH 6.5</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown at 18 C. SeMet crystals used for structure determination by multi-crystal SAD at 0.9792 A wavelength.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4f35">4F35</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">REWFL</span><span class="topo-inside">HRNS</span><span class="topo-membrane">LIVLADVALFLAL</span><span class="topo-outside">YHFLPFEHNVVLGIS</span><span class="topo-membrane">MLAFIAVLWLTEAL</span><span class="topo-inside">H</span><span class="topo-membrane">VTVTAILV</span></span>
<span class="topo-line"><span class="topo-membrane">PVM</span><span class="topo-outside">AVFFGIFETQAAL</span><span class="topo-membrane">NNFANSIIFLFLGGFAL</span><span class="topo-inside">AAAMHHQGLDKVIADKVLAM</span><span class="topo-unknown">AQGKMS</span><span class="topo-inside">V</span></span>
<span class="topo-line"><span class="topo-inside">AVFMLFGVTALLSMWISNTATAAMMLPLVLGVLSKV</span><span class="topo-unknown">DADKQ</span><span class="topo-inside">RSTYVFVLLGVAYSASI</span><span class="topo-membrane">GG</span></span>
<span class="topo-line"><span class="topo-membrane">IATLVGSPPNAIAAAE</span><span class="topo-outside">VGL</span><span class="topo-membrane">SFTDWMKFGLPTAMMM</span><span class="topo-inside">LPMAIAILYFLLK</span><span class="topo-unknown">PTLNGMFELDRA</span></span>
<span class="topo-line"><span class="topo-unknown">PVNWD</span><span class="topo-inside">KGKVVTLG</span><span class="topo-membrane">IFGLTVFLWIFSS</span><span class="topo-outside">PINAALGGFKS</span><span class="topo-membrane">FDTLVALGAILMLSFA</span><span class="topo-inside">RVVH</span><span class="topo-unknown">WKE</span></span>
<span class="topo-line"><span class="topo-unknown">IQKT</span><span class="topo-inside">A</span><span class="topo-membrane">DWGVLLLFGGGLCLS</span><span class="topo-outside">NVLKQTG</span><span class="topo-unknown">TSVFLANALSDMVSHM</span><span class="topo-outside">GIF</span><span class="topo-membrane">VVILVVATFVVFLT</span></span>
<span class="topo-line"><span class="topo-membrane">EF</span><span class="topo-inside">A</span><span class="topo-membrane">SNTASAALLIPVF</span><span class="topo-outside">ATVAEAFGMSPVL</span><span class="topo-membrane">LSVLIAVAASCA</span><span class="topo-inside">FMLPVATPPNAIVFASG</span><span class="topo-unknown">HI</span></span>
<span class="topo-line"><span class="topo-inside">KQSEMMRVGLYL</span><span class="topo-membrane">NIACIGLLTAIAMLF</span><span class="topo-outside">WQ</span></span>
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
      <td>5</td>
      <td>14</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>9</td>
      <td>19</td>
      <td>22</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>22</td>
      <td>23</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>36</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>51</td>
      <td>51</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>52</td>
      <td>65</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>63</td>
      <td>66</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>76</td>
      <td>77</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>93</td>
      <td>90</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>113</td>
      <td>107</td>
      <td>126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>119</td>
      <td>127</td>
      <td>132</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>120</td>
      <td>156</td>
      <td>133</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>161</td>
      <td>170</td>
      <td>174</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>162</td>
      <td>178</td>
      <td>175</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>196</td>
      <td>192</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>199</td>
      <td>210</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>215</td>
      <td>213</td>
      <td>228</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>228</td>
      <td>229</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>245</td>
      <td>242</td>
      <td>258</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>246</td>
      <td>253</td>
      <td>259</td>
      <td>266</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>266</td>
      <td>267</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>277</td>
      <td>280</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>293</td>
      <td>291</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>297</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>304</td>
      <td>311</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>305</td>
      <td>305</td>
      <td>318</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>320</td>
      <td>319</td>
      <td>333</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>321</td>
      <td>327</td>
      <td>334</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>343</td>
      <td>341</td>
      <td>356</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>344</td>
      <td>346</td>
      <td>357</td>
      <td>359</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>362</td>
      <td>360</td>
      <td>375</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>363</td>
      <td>363</td>
      <td>376</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>364</td>
      <td>376</td>
      <td>377</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>377</td>
      <td>389</td>
      <td>390</td>
      <td>402</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>401</td>
      <td>403</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>402</td>
      <td>418</td>
      <td>415</td>
      <td>431</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>420</td>
      <td>432</td>
      <td>433</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>421</td>
      <td>432</td>
      <td>434</td>
      <td>445</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>433</td>
      <td>447</td>
      <td>446</td>
      <td>460</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>448</td>
      <td>449</td>
      <td>461</td>
      <td>462</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4f35">4F35</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">REWFL</span><span class="topo-inside">HRNS</span><span class="topo-membrane">LIVLADVALFLAL</span><span class="topo-outside">YHFLPFEHNVVLGIS</span><span class="topo-membrane">MLAFIAVLWLTEAL</span><span class="topo-inside">H</span><span class="topo-membrane">VTVTAILV</span></span>
<span class="topo-line"><span class="topo-membrane">PVM</span><span class="topo-outside">AVFFGIFETQAAL</span><span class="topo-membrane">NNFANSIIFLFLGGFAL</span><span class="topo-inside">AAAMHHQGLDKVIADKVLAMAQGKMSV</span></span>
<span class="topo-line"><span class="topo-inside">AVFMLFGVTALLSMWISNTATAAMMLPLVLGVLSKVDADKQRSTYVFVLLGVAYSAS</span><span class="topo-membrane">IGG</span></span>
<span class="topo-line"><span class="topo-membrane">IATLVGSPPNAIAAAE</span><span class="topo-outside">VGL</span><span class="topo-membrane">SFTDWMKFGLPTAMMML</span><span class="topo-inside">PMAIAILYFLLKP</span><span class="topo-unknown">TLNGMFELDR</span><span class="topo-inside">A</span></span>
<span class="topo-line"><span class="topo-inside">PVNWDKGKVVTLG</span><span class="topo-membrane">IFGLTVFLWIFSS</span><span class="topo-outside">PINAALGGFKS</span><span class="topo-membrane">FDTLVALGAILMLSFA</span><span class="topo-inside">RVVH</span><span class="topo-unknown">WKE</span></span>
<span class="topo-line"><span class="topo-unknown">IQKT</span><span class="topo-inside">A</span><span class="topo-membrane">DWGVLLLFGGGLCL</span><span class="topo-outside">SNVLKQTG</span><span class="topo-unknown">TSVFLANALSDMVS</span><span class="topo-outside">HMGIF</span><span class="topo-membrane">VVILVVATFVVFLT</span></span>
<span class="topo-line"><span class="topo-membrane">EF</span><span class="topo-inside">A</span><span class="topo-membrane">SNTASAALLIPVF</span><span class="topo-outside">ATVAEAFGMSPVL</span><span class="topo-membrane">LSVLIAVAASCA</span><span class="topo-inside">FMLPVATPPNAIVFASGHI</span></span>
<span class="topo-line"><span class="topo-inside">KQSEMMRVGLYLN</span><span class="topo-membrane">IACIGLLTAIAMLF</span><span class="topo-outside">WQ</span></span>
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
      <td>5</td>
      <td>14</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>9</td>
      <td>19</td>
      <td>22</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>22</td>
      <td>23</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>36</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>51</td>
      <td>51</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>52</td>
      <td>65</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>63</td>
      <td>66</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>76</td>
      <td>77</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>93</td>
      <td>90</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>177</td>
      <td>107</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>196</td>
      <td>191</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>199</td>
      <td>210</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>216</td>
      <td>213</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>229</td>
      <td>230</td>
      <td>242</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>239</td>
      <td>243</td>
      <td>252</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>240</td>
      <td>253</td>
      <td>253</td>
      <td>266</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>266</td>
      <td>267</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>277</td>
      <td>280</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>293</td>
      <td>291</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>297</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>304</td>
      <td>311</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>305</td>
      <td>305</td>
      <td>318</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>319</td>
      <td>319</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>320</td>
      <td>327</td>
      <td>333</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>341</td>
      <td>341</td>
      <td>354</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>342</td>
      <td>346</td>
      <td>355</td>
      <td>359</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>362</td>
      <td>360</td>
      <td>375</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>363</td>
      <td>363</td>
      <td>376</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>364</td>
      <td>376</td>
      <td>377</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>377</td>
      <td>389</td>
      <td>390</td>
      <td>402</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>401</td>
      <td>403</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>402</td>
      <td>433</td>
      <td>415</td>
      <td>446</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>434</td>
      <td>447</td>
      <td>447</td>
      <td>460</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>448</td>
      <td>449</td>
      <td>461</td>
      <td>462</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##ncomms15009

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ul7">5UL7</a></td>
      <td>2.8 A</td>
      <td>not specified</td>
      <td>Full-length VcINDY (462 residues), N-terminal deca-histidine tag cleaved</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/succinate/">Succinate (Succinic Acid)</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ul7">5UL7</a></td>
      <td>2.8 A</td>
      <td>not specified</td>
      <td>Full-length VcINDY (462 residues), N-terminal deca-histidine tag cleaved</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ul7">5UL7</a></td>
      <td>2.8 A</td>
      <td>not specified</td>
      <td>MT5 (humanized VcINDY octuple mutant)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/succinate/">Succinate (Succinic Acid)</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ul7">5UL7</a></td>
      <td>2.8 A</td>
      <td>not specified</td>
      <td>MT5 (humanized VcINDY octuple mutant)</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-AI
- **Construct**: N-terminal 10X His-tagged VcINDY in modified pET vector
- **Notes**: Seleno-[L-Methionine](/xray-mp-wiki/reagents/ligands/l-methionine/) (SeMet) protein produced in E. coli B834DE3 cells grown in minimal media containing SeMet. For ncomms15009, proteins expressed with N-terminal cleavable deca-histidine tag in modified pET28b vector; site-directed mutagenesis by QuikChange method.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified VcINDY or MT5 in crystallization buffer</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in paper body</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structures determined by combining <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> and multiple isomorphous replacement and anomalous scattering (<a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a>) phasing. <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a> phases allowed modelling of 445 out of 462 residues.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ul7">5UL7</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">LHRN</span><span class="topo-membrane">SLIVLADVALFLAL</span><span class="topo-outside">YHFLPFEHNVVLGIS</span><span class="topo-membrane">MLAFIAVLWLTEAL</span><span class="topo-inside">H</span><span class="topo-membrane">VTVTAILVPVM</span><span class="topo-outside">A</span></span>
<span class="topo-line"><span class="topo-outside">VFFGIFETQAALNN</span><span class="topo-membrane">FANSIIFLFLGGFALA</span><span class="topo-inside">AAMHHQGLDKVIADKVLAMAQGKMSVAVFM</span></span>
<span class="topo-line"><span class="topo-inside">LFGVTALLSMWISNTATAAMMLPLVLGVLSKVDADKQRSTYVFVLLGVAYSAS</span><span class="topo-membrane">IGGIATL</span></span>
<span class="topo-line"><span class="topo-membrane">VGSPPNAIAAAE</span><span class="topo-outside">VGL</span><span class="topo-membrane">SFTDWMKFGLPTAMMMLPM</span><span class="topo-inside">AIAILYFLLKPTLNGMFELDRAPVNW</span></span>
<span class="topo-line"><span class="topo-inside">DKGKVVTLG</span><span class="topo-membrane">IFGLTVFLWIFS</span><span class="topo-outside">SPINAALGGFKSF</span><span class="topo-membrane">DTLVALGAILMLSFA</span><span class="topo-inside">RVVH</span><span class="topo-unknown">WKEIQKT</span></span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">DWGVLLLFGGGLCL</span><span class="topo-outside">SNVLKQTG</span><span class="topo-unknown">TSVFLANAL</span><span class="topo-outside">SDMVSHMGIFVVI</span><span class="topo-membrane">LVVATFVVFLTEFA</span><span class="topo-inside">S</span></span>
<span class="topo-line"><span class="topo-membrane">NTASAALLIPV</span><span class="topo-outside">FATVAEAFGMSPVLL</span><span class="topo-membrane">SVLIAVAASCA</span><span class="topo-inside">FMLPVATPPNAIVFASGHIKQSE</span></span>
<span class="topo-line"><span class="topo-inside">MMRVGL</span><span class="topo-membrane">YLNIACIGLLTAIAMLF</span><span class="topo-outside">WQ</span></span>
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
      <td>4</td>
      <td>18</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>36</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>47</td>
      <td>51</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>48</td>
      <td>65</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>59</td>
      <td>66</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>74</td>
      <td>77</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>90</td>
      <td>92</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>173</td>
      <td>108</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>192</td>
      <td>191</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>195</td>
      <td>210</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>214</td>
      <td>213</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>249</td>
      <td>232</td>
      <td>266</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>261</td>
      <td>267</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>274</td>
      <td>279</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>289</td>
      <td>292</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>293</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>300</td>
      <td>311</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>301</td>
      <td>301</td>
      <td>318</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>315</td>
      <td>319</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>323</td>
      <td>333</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>332</td>
      <td>341</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>333</td>
      <td>345</td>
      <td>350</td>
      <td>362</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>359</td>
      <td>363</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>360</td>
      <td>377</td>
      <td>377</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>371</td>
      <td>378</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>386</td>
      <td>389</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>397</td>
      <td>404</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>426</td>
      <td>415</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>443</td>
      <td>444</td>
      <td>460</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>445</td>
      <td>461</td>
      <td>462</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ul7">5UL7</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">LHRN</span><span class="topo-membrane">SLIVLADVALFLAL</span><span class="topo-outside">YHFLPFEHNVVLGIS</span><span class="topo-membrane">MLAFIAVLWLTEAL</span><span class="topo-inside">H</span><span class="topo-membrane">VTVTAILVPVM</span><span class="topo-outside">A</span></span>
<span class="topo-line"><span class="topo-outside">VFFGIFETQAALNN</span><span class="topo-membrane">FANSIIFLFLGGFALA</span><span class="topo-inside">AAMHHQGLDKVIADKVLAMAQGKMSVAVFM</span></span>
<span class="topo-line"><span class="topo-inside">LFGVTALLSMWISNTATAAMMLPLVLGVLSKVDADKQRSTYVFVLLGVAYSAS</span><span class="topo-membrane">IGGIATL</span></span>
<span class="topo-line"><span class="topo-membrane">VGSPPNAIAAAE</span><span class="topo-outside">VGL</span><span class="topo-membrane">SFTDWMKFGLPTAMMMLPM</span><span class="topo-inside">AIAILYFLLKPTLNGMFELDRAPVNW</span></span>
<span class="topo-line"><span class="topo-inside">DKGKVVTLG</span><span class="topo-membrane">IFGLTVFLWIFS</span><span class="topo-outside">SPINAALGGFKSF</span><span class="topo-membrane">DTLVALGAILMLSFA</span><span class="topo-inside">RVVH</span><span class="topo-unknown">WKEIQKT</span></span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">DWGVLLLFGGGLCL</span><span class="topo-outside">SNVLKQTG</span><span class="topo-unknown">TSVFLANAL</span><span class="topo-outside">SDMVSHMGIFVVI</span><span class="topo-membrane">LVVATFVVFLTEFA</span><span class="topo-inside">S</span></span>
<span class="topo-line"><span class="topo-membrane">NTASAALLIPV</span><span class="topo-outside">FATVAEAFGMSPVLL</span><span class="topo-membrane">SVLIAVAASCA</span><span class="topo-inside">FMLPVATPPNAIVFASGHIKQSE</span></span>
<span class="topo-line"><span class="topo-inside">MMRVGL</span><span class="topo-membrane">YLNIACIGLLTAIAMLF</span><span class="topo-outside">WQ</span></span>
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
      <td>4</td>
      <td>18</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>36</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>47</td>
      <td>51</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>48</td>
      <td>65</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>59</td>
      <td>66</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>74</td>
      <td>77</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>90</td>
      <td>92</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>173</td>
      <td>108</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>192</td>
      <td>191</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>195</td>
      <td>210</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>214</td>
      <td>213</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>249</td>
      <td>232</td>
      <td>266</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>261</td>
      <td>267</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>274</td>
      <td>279</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>289</td>
      <td>292</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>293</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>300</td>
      <td>311</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>301</td>
      <td>301</td>
      <td>318</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>315</td>
      <td>319</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>323</td>
      <td>333</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>332</td>
      <td>341</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>333</td>
      <td>345</td>
      <td>350</td>
      <td>362</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>359</td>
      <td>363</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>360</td>
      <td>377</td>
      <td>377</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>371</td>
      <td>378</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>386</td>
      <td>389</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>397</td>
      <td>404</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>426</td>
      <td>415</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>443</td>
      <td>444</td>
      <td>460</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>445</td>
      <td>461</td>
      <td>462</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ul7">5UL7</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">LHRN</span><span class="topo-membrane">SLIVLADVALFLAL</span><span class="topo-outside">YHFLPFEHNVVLGIS</span><span class="topo-membrane">MLAFIAVLWLTEAL</span><span class="topo-inside">H</span><span class="topo-membrane">VTVTAILVPVM</span><span class="topo-outside">A</span></span>
<span class="topo-line"><span class="topo-outside">VFFGIFETQAALNN</span><span class="topo-membrane">FANSIIFLFLGGFALA</span><span class="topo-inside">AAMHHQGLDKVIADKVLAMAQGKMSVAVFM</span></span>
<span class="topo-line"><span class="topo-inside">LFGVTALLSMWISNTATAAMMLPLVLGVLSKVDADKQRSTYVFVLLGVAYSAS</span><span class="topo-membrane">IGGIATL</span></span>
<span class="topo-line"><span class="topo-membrane">VGSPPNAIAAAE</span><span class="topo-outside">VGL</span><span class="topo-membrane">SFTDWMKFGLPTAMMMLPM</span><span class="topo-inside">AIAILYFLLKPTLNGMFELDRAPVNW</span></span>
<span class="topo-line"><span class="topo-inside">DKGKVVTLG</span><span class="topo-membrane">IFGLTVFLWIFS</span><span class="topo-outside">SPINAALGGFKSF</span><span class="topo-membrane">DTLVALGAILMLSFA</span><span class="topo-inside">RVVH</span><span class="topo-unknown">WKEIQKT</span></span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">DWGVLLLFGGGLCL</span><span class="topo-outside">SNVLKQTG</span><span class="topo-unknown">TSVFLANAL</span><span class="topo-outside">SDMVSHMGIFVVI</span><span class="topo-membrane">LVVATFVVFLTEFA</span><span class="topo-inside">S</span></span>
<span class="topo-line"><span class="topo-membrane">NTASAALLIPV</span><span class="topo-outside">FATVAEAFGMSPVLL</span><span class="topo-membrane">SVLIAVAASCA</span><span class="topo-inside">FMLPVATPPNAIVFASGHIKQSE</span></span>
<span class="topo-line"><span class="topo-inside">MMRVGL</span><span class="topo-membrane">YLNIACIGLLTAIAMLF</span><span class="topo-outside">WQ</span></span>
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
      <td>4</td>
      <td>18</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>36</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>47</td>
      <td>51</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>48</td>
      <td>65</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>59</td>
      <td>66</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>74</td>
      <td>77</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>90</td>
      <td>92</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>173</td>
      <td>108</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>192</td>
      <td>191</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>195</td>
      <td>210</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>214</td>
      <td>213</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>249</td>
      <td>232</td>
      <td>266</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>261</td>
      <td>267</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>274</td>
      <td>279</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>289</td>
      <td>292</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>293</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>300</td>
      <td>311</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>301</td>
      <td>301</td>
      <td>318</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>315</td>
      <td>319</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>323</td>
      <td>333</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>332</td>
      <td>341</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>333</td>
      <td>345</td>
      <td>350</td>
      <td>362</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>359</td>
      <td>363</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>360</td>
      <td>377</td>
      <td>377</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>371</td>
      <td>378</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>386</td>
      <td>389</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>397</td>
      <td>404</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>426</td>
      <td>415</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>443</td>
      <td>444</td>
      <td>460</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>445</td>
      <td>461</td>
      <td>462</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ul7">5UL7</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">LHRN</span><span class="topo-membrane">SLIVLADVALFLAL</span><span class="topo-outside">YHFLPFEHNVVLGIS</span><span class="topo-membrane">MLAFIAVLWLTEAL</span><span class="topo-inside">H</span><span class="topo-membrane">VTVTAILVPVM</span><span class="topo-outside">A</span></span>
<span class="topo-line"><span class="topo-outside">VFFGIFETQAALNN</span><span class="topo-membrane">FANSIIFLFLGGFALA</span><span class="topo-inside">AAMHHQGLDKVIADKVLAMAQGKMSVAVFM</span></span>
<span class="topo-line"><span class="topo-inside">LFGVTALLSMWISNTATAAMMLPLVLGVLSKVDADKQRSTYVFVLLGVAYSAS</span><span class="topo-membrane">IGGIATL</span></span>
<span class="topo-line"><span class="topo-membrane">VGSPPNAIAAAE</span><span class="topo-outside">VGL</span><span class="topo-membrane">SFTDWMKFGLPTAMMMLPM</span><span class="topo-inside">AIAILYFLLKPTLNGMFELDRAPVNW</span></span>
<span class="topo-line"><span class="topo-inside">DKGKVVTLG</span><span class="topo-membrane">IFGLTVFLWIFS</span><span class="topo-outside">SPINAALGGFKSF</span><span class="topo-membrane">DTLVALGAILMLSFA</span><span class="topo-inside">RVVH</span><span class="topo-unknown">WKEIQKT</span></span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">DWGVLLLFGGGLCL</span><span class="topo-outside">SNVLKQTG</span><span class="topo-unknown">TSVFLANAL</span><span class="topo-outside">SDMVSHMGIFVVI</span><span class="topo-membrane">LVVATFVVFLTEFA</span><span class="topo-inside">S</span></span>
<span class="topo-line"><span class="topo-membrane">NTASAALLIPV</span><span class="topo-outside">FATVAEAFGMSPVLL</span><span class="topo-membrane">SVLIAVAASCA</span><span class="topo-inside">FMLPVATPPNAIVFASGHIKQSE</span></span>
<span class="topo-line"><span class="topo-inside">MMRVGL</span><span class="topo-membrane">YLNIACIGLLTAIAMLF</span><span class="topo-outside">WQ</span></span>
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
      <td>4</td>
      <td>18</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>36</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>47</td>
      <td>51</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>48</td>
      <td>65</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>59</td>
      <td>66</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>74</td>
      <td>77</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>90</td>
      <td>92</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>173</td>
      <td>108</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>192</td>
      <td>191</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>195</td>
      <td>210</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>214</td>
      <td>213</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>249</td>
      <td>232</td>
      <td>266</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>261</td>
      <td>267</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>274</td>
      <td>279</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>289</td>
      <td>292</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>293</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>300</td>
      <td>311</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>301</td>
      <td>301</td>
      <td>318</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>315</td>
      <td>319</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>323</td>
      <td>333</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>332</td>
      <td>341</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>333</td>
      <td>345</td>
      <td>350</td>
      <td>362</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>359</td>
      <td>363</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>360</td>
      <td>377</td>
      <td>377</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>371</td>
      <td>378</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>386</td>
      <td>389</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>397</td>
      <td>404</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>426</td>
      <td>415</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>443</td>
      <td>444</td>
      <td>460</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>445</td>
      <td>461</td>
      <td>462</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ul7">5UL7</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">LHRN</span><span class="topo-membrane">SLIVLADVALFLAL</span><span class="topo-outside">YHFLPFEHNVVLGIS</span><span class="topo-membrane">MLAFIAVLWLTEAL</span><span class="topo-inside">H</span><span class="topo-membrane">VTVTAILVPVM</span><span class="topo-outside">A</span></span>
<span class="topo-line"><span class="topo-outside">VFFGIFETQAALNN</span><span class="topo-membrane">FANSIIFLFLGGFALA</span><span class="topo-inside">AAMHHQGLDKVIADKVLAMAQGKMSVAVFM</span></span>
<span class="topo-line"><span class="topo-inside">LFGVTALLSMWISNTATAAMMLPLVLGVLSKVDADKQRSTYVFVLLGVAYSAS</span><span class="topo-membrane">IGGIATL</span></span>
<span class="topo-line"><span class="topo-membrane">VGSPPNAIAAAE</span><span class="topo-outside">VGL</span><span class="topo-membrane">SFTDWMKFGLPTAMMMLPM</span><span class="topo-inside">AIAILYFLLKPTLNGMFELDRAPVNW</span></span>
<span class="topo-line"><span class="topo-inside">DKGKVVTLG</span><span class="topo-membrane">IFGLTVFLWIFS</span><span class="topo-outside">SPINAALGGFKSF</span><span class="topo-membrane">DTLVALGAILMLSFA</span><span class="topo-inside">RVVH</span><span class="topo-unknown">WKEIQKT</span></span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">DWGVLLLFGGGLCL</span><span class="topo-outside">SNVLKQTG</span><span class="topo-unknown">TSVFLANAL</span><span class="topo-outside">SDMVSHMGIFVVI</span><span class="topo-membrane">LVVATFVVFLTEFA</span><span class="topo-inside">S</span></span>
<span class="topo-line"><span class="topo-membrane">NTASAALLIPV</span><span class="topo-outside">FATVAEAFGMSPVLL</span><span class="topo-membrane">SVLIAVAASCA</span><span class="topo-inside">FMLPVATPPNAIVFASGHIKQSE</span></span>
<span class="topo-line"><span class="topo-inside">MMRVGL</span><span class="topo-membrane">YLNIACIGLLTAIAMLF</span><span class="topo-outside">WQ</span></span>
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
      <td>4</td>
      <td>18</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>36</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>47</td>
      <td>51</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>48</td>
      <td>65</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>59</td>
      <td>66</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>74</td>
      <td>77</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>90</td>
      <td>92</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>173</td>
      <td>108</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>192</td>
      <td>191</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>195</td>
      <td>210</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>214</td>
      <td>213</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>249</td>
      <td>232</td>
      <td>266</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>261</td>
      <td>267</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>274</td>
      <td>279</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>289</td>
      <td>292</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>293</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>300</td>
      <td>311</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>301</td>
      <td>301</td>
      <td>318</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>315</td>
      <td>319</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>323</td>
      <td>333</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>332</td>
      <td>341</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>333</td>
      <td>345</td>
      <td>350</td>
      <td>362</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>359</td>
      <td>363</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>360</td>
      <td>377</td>
      <td>377</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>371</td>
      <td>378</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>386</td>
      <td>389</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>397</td>
      <td>404</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>426</td>
      <td>415</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>443</td>
      <td>444</td>
      <td>460</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>445</td>
      <td>461</td>
      <td>462</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ul7">5UL7</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">LHRN</span><span class="topo-membrane">SLIVLADVALFLAL</span><span class="topo-outside">YHFLPFEHNVVLGIS</span><span class="topo-membrane">MLAFIAVLWLTEAL</span><span class="topo-inside">H</span><span class="topo-membrane">VTVTAILVPVM</span><span class="topo-outside">A</span></span>
<span class="topo-line"><span class="topo-outside">VFFGIFETQAALNN</span><span class="topo-membrane">FANSIIFLFLGGFALA</span><span class="topo-inside">AAMHHQGLDKVIADKVLAMAQGKMSVAVFM</span></span>
<span class="topo-line"><span class="topo-inside">LFGVTALLSMWISNTATAAMMLPLVLGVLSKVDADKQRSTYVFVLLGVAYSAS</span><span class="topo-membrane">IGGIATL</span></span>
<span class="topo-line"><span class="topo-membrane">VGSPPNAIAAAE</span><span class="topo-outside">VGL</span><span class="topo-membrane">SFTDWMKFGLPTAMMMLPM</span><span class="topo-inside">AIAILYFLLKPTLNGMFELDRAPVNW</span></span>
<span class="topo-line"><span class="topo-inside">DKGKVVTLG</span><span class="topo-membrane">IFGLTVFLWIFS</span><span class="topo-outside">SPINAALGGFKSF</span><span class="topo-membrane">DTLVALGAILMLSFA</span><span class="topo-inside">RVVH</span><span class="topo-unknown">WKEIQKT</span></span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">DWGVLLLFGGGLCL</span><span class="topo-outside">SNVLKQTG</span><span class="topo-unknown">TSVFLANAL</span><span class="topo-outside">SDMVSHMGIFVVI</span><span class="topo-membrane">LVVATFVVFLTEFA</span><span class="topo-inside">S</span></span>
<span class="topo-line"><span class="topo-membrane">NTASAALLIPV</span><span class="topo-outside">FATVAEAFGMSPVLL</span><span class="topo-membrane">SVLIAVAASCA</span><span class="topo-inside">FMLPVATPPNAIVFASGHIKQSE</span></span>
<span class="topo-line"><span class="topo-inside">MMRVGL</span><span class="topo-membrane">YLNIACIGLLTAIAMLF</span><span class="topo-outside">WQ</span></span>
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
      <td>4</td>
      <td>18</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>36</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>47</td>
      <td>51</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>48</td>
      <td>65</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>59</td>
      <td>66</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>74</td>
      <td>77</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>90</td>
      <td>92</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>173</td>
      <td>108</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>192</td>
      <td>191</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>195</td>
      <td>210</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>214</td>
      <td>213</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>249</td>
      <td>232</td>
      <td>266</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>261</td>
      <td>267</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>274</td>
      <td>279</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>289</td>
      <td>292</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>293</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>300</td>
      <td>311</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>301</td>
      <td>301</td>
      <td>318</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>315</td>
      <td>319</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>323</td>
      <td>333</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>332</td>
      <td>341</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>333</td>
      <td>345</td>
      <td>350</td>
      <td>362</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>359</td>
      <td>363</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>360</td>
      <td>377</td>
      <td>377</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>371</td>
      <td>378</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>386</td>
      <td>389</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>397</td>
      <td>404</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>426</td>
      <td>415</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>443</td>
      <td>444</td>
      <td>460</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>445</td>
      <td>461</td>
      <td>462</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ul7">5UL7</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">LHRN</span><span class="topo-membrane">SLIVLADVALFLAL</span><span class="topo-outside">YHFLPFEHNVVLGIS</span><span class="topo-membrane">MLAFIAVLWLTEAL</span><span class="topo-inside">H</span><span class="topo-membrane">VTVTAILVPVM</span><span class="topo-outside">A</span></span>
<span class="topo-line"><span class="topo-outside">VFFGIFETQAALNN</span><span class="topo-membrane">FANSIIFLFLGGFALA</span><span class="topo-inside">AAMHHQGLDKVIADKVLAMAQGKMSVAVFM</span></span>
<span class="topo-line"><span class="topo-inside">LFGVTALLSMWISNTATAAMMLPLVLGVLSKVDADKQRSTYVFVLLGVAYSAS</span><span class="topo-membrane">IGGIATL</span></span>
<span class="topo-line"><span class="topo-membrane">VGSPPNAIAAAE</span><span class="topo-outside">VGL</span><span class="topo-membrane">SFTDWMKFGLPTAMMMLPM</span><span class="topo-inside">AIAILYFLLKPTLNGMFELDRAPVNW</span></span>
<span class="topo-line"><span class="topo-inside">DKGKVVTLG</span><span class="topo-membrane">IFGLTVFLWIFS</span><span class="topo-outside">SPINAALGGFKSF</span><span class="topo-membrane">DTLVALGAILMLSFA</span><span class="topo-inside">RVVH</span><span class="topo-unknown">WKEIQKT</span></span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">DWGVLLLFGGGLCL</span><span class="topo-outside">SNVLKQTG</span><span class="topo-unknown">TSVFLANAL</span><span class="topo-outside">SDMVSHMGIFVVI</span><span class="topo-membrane">LVVATFVVFLTEFA</span><span class="topo-inside">S</span></span>
<span class="topo-line"><span class="topo-membrane">NTASAALLIPV</span><span class="topo-outside">FATVAEAFGMSPVLL</span><span class="topo-membrane">SVLIAVAASCA</span><span class="topo-inside">FMLPVATPPNAIVFASGHIKQSE</span></span>
<span class="topo-line"><span class="topo-inside">MMRVGL</span><span class="topo-membrane">YLNIACIGLLTAIAMLF</span><span class="topo-outside">WQ</span></span>
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
      <td>4</td>
      <td>18</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>36</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>47</td>
      <td>51</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>48</td>
      <td>65</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>59</td>
      <td>66</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>74</td>
      <td>77</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>90</td>
      <td>92</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>173</td>
      <td>108</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>192</td>
      <td>191</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>195</td>
      <td>210</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>214</td>
      <td>213</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>249</td>
      <td>232</td>
      <td>266</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>261</td>
      <td>267</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>274</td>
      <td>279</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>289</td>
      <td>292</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>293</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>300</td>
      <td>311</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>301</td>
      <td>301</td>
      <td>318</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>315</td>
      <td>319</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>323</td>
      <td>333</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>332</td>
      <td>341</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>333</td>
      <td>345</td>
      <td>350</td>
      <td>362</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>359</td>
      <td>363</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>360</td>
      <td>377</td>
      <td>377</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>371</td>
      <td>378</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>386</td>
      <td>389</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>397</td>
      <td>404</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>426</td>
      <td>415</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>443</td>
      <td>444</td>
      <td>460</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>445</td>
      <td>461</td>
      <td>462</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ul7">5UL7</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">LHRN</span><span class="topo-membrane">SLIVLADVALFLAL</span><span class="topo-outside">YHFLPFEHNVVLGIS</span><span class="topo-membrane">MLAFIAVLWLTEAL</span><span class="topo-inside">H</span><span class="topo-membrane">VTVTAILVPVM</span><span class="topo-outside">A</span></span>
<span class="topo-line"><span class="topo-outside">VFFGIFETQAALNN</span><span class="topo-membrane">FANSIIFLFLGGFALA</span><span class="topo-inside">AAMHHQGLDKVIADKVLAMAQGKMSVAVFM</span></span>
<span class="topo-line"><span class="topo-inside">LFGVTALLSMWISNTATAAMMLPLVLGVLSKVDADKQRSTYVFVLLGVAYSAS</span><span class="topo-membrane">IGGIATL</span></span>
<span class="topo-line"><span class="topo-membrane">VGSPPNAIAAAE</span><span class="topo-outside">VGL</span><span class="topo-membrane">SFTDWMKFGLPTAMMMLPM</span><span class="topo-inside">AIAILYFLLKPTLNGMFELDRAPVNW</span></span>
<span class="topo-line"><span class="topo-inside">DKGKVVTLG</span><span class="topo-membrane">IFGLTVFLWIFS</span><span class="topo-outside">SPINAALGGFKSF</span><span class="topo-membrane">DTLVALGAILMLSFA</span><span class="topo-inside">RVVH</span><span class="topo-unknown">WKEIQKT</span></span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">DWGVLLLFGGGLCL</span><span class="topo-outside">SNVLKQTG</span><span class="topo-unknown">TSVFLANAL</span><span class="topo-outside">SDMVSHMGIFVVI</span><span class="topo-membrane">LVVATFVVFLTEFA</span><span class="topo-inside">S</span></span>
<span class="topo-line"><span class="topo-membrane">NTASAALLIPV</span><span class="topo-outside">FATVAEAFGMSPVLL</span><span class="topo-membrane">SVLIAVAASCA</span><span class="topo-inside">FMLPVATPPNAIVFASGHIKQSE</span></span>
<span class="topo-line"><span class="topo-inside">MMRVGL</span><span class="topo-membrane">YLNIACIGLLTAIAMLF</span><span class="topo-outside">WQ</span></span>
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
      <td>4</td>
      <td>18</td>
      <td>21</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>18</td>
      <td>22</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>36</td>
      <td>50</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>47</td>
      <td>51</td>
      <td>64</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>48</td>
      <td>65</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>59</td>
      <td>66</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>74</td>
      <td>77</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>90</td>
      <td>92</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>173</td>
      <td>108</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>192</td>
      <td>191</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>195</td>
      <td>210</td>
      <td>212</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>214</td>
      <td>213</td>
      <td>231</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>249</td>
      <td>232</td>
      <td>266</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>261</td>
      <td>267</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>274</td>
      <td>279</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>289</td>
      <td>292</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>290</td>
      <td>293</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>300</td>
      <td>311</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>301</td>
      <td>301</td>
      <td>318</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>315</td>
      <td>319</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>323</td>
      <td>333</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>332</td>
      <td>341</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>333</td>
      <td>345</td>
      <td>350</td>
      <td>362</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>359</td>
      <td>363</td>
      <td>376</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>360</td>
      <td>377</td>
      <td>377</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>371</td>
      <td>378</td>
      <td>388</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>386</td>
      <td>389</td>
      <td>403</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>397</td>
      <td>404</td>
      <td>414</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>426</td>
      <td>415</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>443</td>
      <td>444</td>
      <td>460</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>444</td>
      <td>445</td>
      <td>461</td>
      <td>462</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Inward-facing conformation and inverted two-fold symmetry

VcINDY consists of 11 transmembrane helices (TM1-TM11) arranged in two
inverted symmetry-related halves. The N-terminal half (TM2-TM6) and
C-terminal half (TM7-TM11) each form a hand-shaped structure related by
an inverted two-fold symmetry axis parallel to the membrane plane. The
N-terminal hand adopts a V-shape while the C-terminal hand adopts a
U-shape. Each hand contains a helical hairpin (HP_in and HP_out,
respectively) that inserts into the membrane from opposite sides.

### Two sodium-binding sites (Na1 and Na2)

Two Na+ binding sites were identified in 2.8 A structures. Na1 is coordinated by
Ser146 (side chain and backbone carbonyl), Ser150 (backbone carbonyl), Asn151
(side chain carbonyl), and Gly199 (backbone carbonyl). Na2 is coordinated by
Thr373 (side chain hydroxyl and backbone carbonyl), Asn378 (side chain carbonyl),
Ala376 (backbone carbonyl), and Ala420 (backbone carbonyl). Both Na+ ions are
penta-coordinated and separated by >13 A. Na2 is functionally more important
than Na1; T373A mutation caused more severe transport defects than S146A.

### Succinate recognition without positively charged residues

Unlike many anion transporters that use Arg or Lys residues, VcINDY binds
[Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/) without any positively charged amino acids in the binding site.
Instead, the two negative charges of [Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/) are stabilized by positive
helix dipoles from four short helices (HP_in, HP_out, TM5b, TM10b) and by
the two bound Na+ ions. This suggests a general mechanism for achieving
anion selectivity within the lipid bilayer by membrane proteins.

### Substrate discrimination between C4 and C6 carboxylates

VcINDY discriminates between [Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/) (C4) and [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/) (C6) through
steric and electrostatic mechanisms. Pro201 and Thr379 pack against [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/)'s
pro-S carboxylate, steering it away from the transporter. In the MT5
humanized variant (P201G, T379V), the pro-S carboxylate forms additional
hydrogen bonds with the protein, explaining why MT5/NaCT transport [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/)
more effectively.

### Relationship to mammalian SLC13 transporters

VcINDY shares 26-33% sequence identity with human SLC13 transporters
(NaCT/SLC13A5, NaDC1/SLC13A2, NaDC3/SLC13A3). The SNT motifs identified
in VcINDY are conserved across the DASS family and serve as signature
sequences for Na+-dependent tri- and dicarboxylate transporters. The
structural framework provides direct insight into the transport mechanism
of human NaCT, a potential drug target for obesity, diabetes, and
cardiovascular diseases.

### Structural similarity to AbgT transporters

VcINDY exhibits striking structural resemblance to dimeric AbgT transporters
(r.m.s.d. 3.1-3.5 A for ~300 C-alpha atoms), despite only 13-18% sequence
identity. A Na+-binding site similar to Na2 in VcINDY was found in an AbgT
transporter, suggesting that at least one functionally important Na+-binding
site is conserved between the DASS and AbgT protein families.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/dass-family/">Divalent Anion/Na+ Symporter (DASS) Family</a> — VcINDY is a member of the DASS family of transporters
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/inward-facing-conformation/">Inward-Facing Conformation</a> — The VcINDY structure represents an inward-facing conformation
- <a href="/xray-mp-wiki/reagents/detergents/dm/">N-Decyl-beta-D-maltopyranoside (DM)</a> — Primary detergent used for VcINDY purification
- <a href="/xray-mp-wiki/reagents/buffers/mops/">MOPS Buffer</a> — Used in crystallization reservoir (50 mM, pH 6.5)
- <a href="/xray-mp-wiki/reagents/additives/lithium-citrate/">Lithium Citrate</a> — Used in purification buffer and crystallization reservoir
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate</a> — Primary substrate and bound ligand in the crystal structure
- <a href="/xray-mp-wiki/reagents/ligands/succinate/">Succinate</a> — Alternative dicarboxylate substrate of VcINDY
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine</a> — Used for SeMet SAD phasing
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
