---
title: "Kv1.2-2.1-3m Chimeric Channel (C-type Inactivated State)"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.abm8804]
verified: false
---

# Kv1.2-2.1-3m Chimeric Channel (C-type Inactivated State)

## Overview

The Kv1.2-2.1-3m channel is a triple mutant (W362F, S367T, V377T) of the Kv1.2-2.1 chimeric voltage-gated K+ channel that exhibits a ~2000-fold increase in the rate of C-type inactivation at high (100 mM) external K+. The crystal structure was determined at 3.35 A resolution (PDB 7SIT) and reveals the selectivity filter in a C-type inactivated state. The structure shows dilation of the selectivity filter at the S1 and S2 ion binding sites, caused by reorientation of the conserved Tyr373 and Asp375 side chains, which creates a widened vestibule. The S3 and S4 sites remain intact. Structural changes propagate to the extracellular mouth and turret regions. The structure supports the dilation model for C-type inactivation and provides a mechanism for the effect of extracellular K+ on inactivation.

## Publications

### doi/10.1126##sciadv.abm8804

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7sit">7SIT</a></td>
      <td>3.35</td>
      <td>P4 2_1 2</td>
      <td>Kv1.2-2.1 chimera with W362F, S367T, V377T mutations, co-expressed with rat Kv beta2 subunit</td>
      <td>K+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (co-expression with rat Kv beta2 subunit)
- **Construct**: Kv1.2-2.1 chimera with W362F, S367T, V377T mutations, N207Q, co-expressed with rat Kv beta2 subunit
- **Notes**: The Kv1.2-2.1 chimera substitutes residues 267-302 in the S3-S4 loop of Kv1.2 with residues 274-305 of Kv2.1 for improved crystallographic properties.

**Purification:**

- **Expression system**: Pichia pastoris
- **Expression construct**: Kv1.2-2.1-3m (W362F/S367T/V377T) with beta2 subunit, cloned into pPicZ-C vector

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
      <td>Cryogenic milling</td>
      <td>--</td>
      <td>50 mM Tris-HCl pH 7.5, 150 mM KCl, 2 mM TCEP, 10 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, DNase I, protease inhibitors + --</td>
      <td>Six cycles of milling at 25 Hz for 3 min; cells kept cold with liquid nitrogen between cycles</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM Tris-HCl pH 7.5, 150 mM KCl, 2 mM TCEP, 10 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> + 1.5% (w/v) n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Solubilized for 3 h at room temperature; unsolubilized material removed by ultracentrifugation (100,000g, 50 min)</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt affinity</td>
      <td>Cobalt resin</td>
      <td>50 mM Tris-HCl pH 7.5, 150 mM KCl, 2 mM TCEP, 10 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, 5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Incubated overnight at 4°C with gentle rotation; washed with 20 volumes of column buffer containing lipids (0.1 mg/ml <a href="/xray-mp-wiki/reagents/lipids/popc/">POPC</a>:<a href="/xray-mp-wiki/reagents/lipids/pope/">POPE</a>:<a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a> 3:1:1) and 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; eluted with 400 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>Superdex S200</td>
      <td>20 mM Tris-HCl pH 7.5, 150 mM KCl, 2 mM TCEP, 10 mM DTT, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, lipids (0.1 mg/ml) (3:1:1 <a href="/xray-mp-wiki/reagents/lipids/popc/">POPC</a>:<a href="/xray-mp-wiki/reagents/lipids/pope/">POPE</a>:<a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a>) + 3 mM <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a>, 3 mM Cymal-7</td>
      <td>Eluted protein supplemented with 10 mM DTT, concentrated using Millipore Amicon Ultra 100K device</td>
    </tr>
  </tbody>
</table>
**Final sample**: Kv1.2-2.1-3m-beta2 complex in lipid/detergent mixture with reducing agents

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Kv1.2-2.1-3m-beta2 complex in buffer with 8 mM CHAPS, 150 mM K+</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM Tris-HCl pH 8.2-8.8, 26-36% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>4-5 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td><a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400 concentration increased to 35% in well solution for 24 h, then frozen in liquid N2</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein-to-reservoir ratio 1:1. Rod-shaped crystals. Data collected at APS (beamlines 23ID-B and 23ID-D). Multiple crystals combined for complete dataset.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7sit">7SIT</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">LQFYRNLGKSGLRVSCLGLGTWVTFGGQITDEMAEHLMTLAYDNGINLFDTAEVYAAGKAEVVLGNIIKKKGWRRSSLVITTKIFWGGKAETERGLSRKHIIEGLKASLERLQLEYVDV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VFANRPDPNTPMEETVRAMTHVINQGMAMYWGTSRWSSMEIMEAYSVARQFNLIPPICEQAEYHMFQREKVEVQLPELFHKIGVGAMTWSPLACGIVSGKYDSGIPPYSRASLKGYQWLK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-inside">DKILSEEGRRQQAKLKELQAIAERLGCTLPQLAIAWCLRNEGVSSVLLGASNAEQLMENIGAIQVLPKLSSSIVHEIDSILGNKPYS</span><span class="topo-unknown">KKDYRS</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>35</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>327</td>
      <td>36</td>
      <td>361</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>333</td>
      <td>362</td>
      <td>367</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7sit">7SIT</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAHHHHHHHHHHGLVPRGSMTVATGDPVDEAAAHPGHPQDTYDPEADHES</span><span class="topo-inside">SERVVINISGLRFETQLKTLAQFPETLLGDPKKRMRYFDPLRNEYFFDRNRPSFDAILYYYQSGGRLRRP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VNVPLDIFSEEIRFYELGEEAMEMFREDEGYI</span><span class="topo-unknown">KEEERPLPEN</span><span class="topo-inside">EFQRQVWLLFEYPESSGPAR</span><span class="topo-membrane">IIAIVSVMVILISIVSFCLE</span><span class="topo-outside">TLPIFR</span><span class="topo-unknown">DENEDMHGGGVTFHTYSQSTIGYQQSTS</span><span class="topo-outside">FTDP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-membrane">FIVETLCIIWFSFEFLVRFF</span><span class="topo-inside">ACPSK</span><span class="topo-unknown">AG</span><span class="topo-inside">FFTN</span><span class="topo-membrane">IMNIIDIVAIIPY</span><span class="topo-unknown">YVTIFLTESNKSVLQFQNVRR</span><span class="topo-outside">V</span><span class="topo-membrane">VQIFRIMRILRIFKLSRHSK</span><span class="topo-inside">GLQILGQTLKASM</span><span class="topo-membrane">RELGLLIFFLFIGVILFSSA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VYFA</span><span class="topo-outside">EADERDSQFPSI</span><span class="topo-unknown">PDAFFWAVVTMTTVGYG</span><span class="topo-outside">DMTPTTI</span><span class="topo-membrane">GGKIVGSLCAIAGVLTIALPV</span><span class="topo-inside">PVIVSNFNYFYHRET</span><span class="topo-unknown">EGEEQAQYLQVTSSPKIPSSPDLKKSRSASTISKSDYMEIQEGV</span></span>
<span class="topo-ruler">       490       500       510    </span>
<span class="topo-line"><span class="topo-unknown">NNSNEDFREENLKTANSTLANTNYVNITKMLTDV</span></span>
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
      <td>50</td>
      <td>-18</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>152</td>
      <td>32</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>162</td>
      <td>134</td>
      <td>143</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>163</td>
      <td>182</td>
      <td>144</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>202</td>
      <td>164</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>208</td>
      <td>184</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>236</td>
      <td>190</td>
      <td>217</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>237</td>
      <td>241</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>223</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>266</td>
      <td>243</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>268</td>
      <td>248</td>
      <td>249</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>269</td>
      <td>272</td>
      <td>250</td>
      <td>253</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>285</td>
      <td>254</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>267</td>
      <td>287</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>307</td>
      <td>307</td>
      <td>288</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>327</td>
      <td>289</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>328</td>
      <td>340</td>
      <td>309</td>
      <td>321</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>364</td>
      <td>322</td>
      <td>345</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>376</td>
      <td>346</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>393</td>
      <td>358</td>
      <td>374</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>394</td>
      <td>400</td>
      <td>375</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>421</td>
      <td>382</td>
      <td>402</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>436</td>
      <td>403</td>
      <td>417</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>437</td>
      <td>514</td>
      <td>418</td>
      <td>495</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7sit">7SIT</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">LQFYRNLGKSGLRVSCLGLGTWVTFGGQITDEMAEHLMTLAYDNGINLFDTAEVYAAGKAEVVLGNIIKKKGWRRSSLVITTKIFWGGKAETERGLSRKHIIEGLKASLERLQLEYVDV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VFANRPDPNTPMEETVRAMTHVINQGMAMYWGTSRWSSMEIMEAYSVARQFNLIPPICEQAEYHMFQREKVEVQLPELFHKIGVGAMTWSPLACGIVSGKYDSGIPPYSRASLKGYQWLK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-inside">DKILSEEGRRQQAKLKELQAIAERLGCTLPQLAIAWCLRNEGVSSVLLGASNAEQLMENIGAIQVLPKLSSSIVHEIDSILGNKPYS</span><span class="topo-unknown">KKDYRS</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>35</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>327</td>
      <td>36</td>
      <td>361</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>333</td>
      <td>362</td>
      <td>367</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7sit">7SIT</a> — Chain F (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAHHHHHHHHHHGLVPRGSMTVATGDPVDEAAAHPGHPQDTYDPEADHES</span><span class="topo-inside">SERVVINISGLRFETQLKTLAQFPETLLGDPKKRMRYFDPLRNEYFFDRNRPSFDAILYYYQSGGRLRRP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VNVPLDIFSEEIRFYELGEEAMEMFREDEGYI</span><span class="topo-unknown">KEEERPLPEN</span><span class="topo-inside">EFQRQVWLLFEYPESSGPAR</span><span class="topo-membrane">IIAIVSVMVILISIVSFCLE</span><span class="topo-outside">TLPIFR</span><span class="topo-unknown">DENEDMHGGGVTFHTYSQSTIGYQQSTS</span><span class="topo-outside">FTDP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-membrane">FIVETLCIIWFSFEFLVRFF</span><span class="topo-inside">ACPSK</span><span class="topo-unknown">AG</span><span class="topo-inside">FFTN</span><span class="topo-membrane">IMNIIDIVAIIPY</span><span class="topo-unknown">YVTIFLTESNKSVLQFQNVRR</span><span class="topo-outside">V</span><span class="topo-membrane">VQIFRIMRILRIFKLSRHSK</span><span class="topo-inside">GLQILGQTLKASM</span><span class="topo-membrane">RELGLLIFFLFIGVILFSSA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VYFA</span><span class="topo-outside">EADERDSQFPSI</span><span class="topo-unknown">PDAFFWAVVTMTTVGYG</span><span class="topo-outside">DMTPTTI</span><span class="topo-membrane">GGKIVGSLCAIAGVLTIALPV</span><span class="topo-inside">PVIVSNFNYFYHRET</span><span class="topo-unknown">EGEEQAQYLQVTSSPKIPSSPDLKKSRSASTISKSDYMEIQEGV</span></span>
<span class="topo-ruler">       490       500       510    </span>
<span class="topo-line"><span class="topo-unknown">NNSNEDFREENLKTANSTLANTNYVNITKMLTDV</span></span>
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
      <td>50</td>
      <td>-18</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>152</td>
      <td>32</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>162</td>
      <td>134</td>
      <td>143</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>163</td>
      <td>182</td>
      <td>144</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>202</td>
      <td>164</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>208</td>
      <td>184</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>236</td>
      <td>190</td>
      <td>217</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>237</td>
      <td>241</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>223</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>266</td>
      <td>243</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>268</td>
      <td>248</td>
      <td>249</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>269</td>
      <td>272</td>
      <td>250</td>
      <td>253</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>285</td>
      <td>254</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>267</td>
      <td>287</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>307</td>
      <td>307</td>
      <td>288</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>327</td>
      <td>289</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>328</td>
      <td>340</td>
      <td>309</td>
      <td>321</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>364</td>
      <td>322</td>
      <td>345</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>376</td>
      <td>346</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>393</td>
      <td>358</td>
      <td>374</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>394</td>
      <td>400</td>
      <td>375</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>421</td>
      <td>382</td>
      <td>402</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>436</td>
      <td>403</td>
      <td>417</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>437</td>
      <td>514</td>
      <td>418</td>
      <td>495</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7sit">7SIT</a> — Chain G (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">LQFYRNLGKSGLRVSCLGLGTWVTFGGQITDEMAEHLMTLAYDNGINLFDTAEVYAAGKAEVVLGNIIKKKGWRRSSLVITTKIFWGGKAETERGLSRKHIIEGLKASLERLQLEYVDV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VFANRPDPNTPMEETVRAMTHVINQGMAMYWGTSRWSSMEIMEAYSVARQFNLIPPICEQAEYHMFQREKVEVQLPELFHKIGVGAMTWSPLACGIVSGKYDSGIPPYSRASLKGYQWLK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-inside">DKILSEEGRRQQAKLKELQAIAERLGCTLPQLAIAWCLRNEGVSSVLLGASNAEQLMENIGAIQVLPKLSSSIVHEIDSILGNKPYS</span><span class="topo-unknown">KKDYRS</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>35</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>327</td>
      <td>36</td>
      <td>361</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>333</td>
      <td>362</td>
      <td>367</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7sit">7SIT</a> — Chain H (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAHHHHHHHHHHGLVPRGSMTVATGDPVDEAAAHPGHPQDTYDPEADHES</span><span class="topo-inside">SERVVINISGLRFETQLKTLAQFPETLLGDPKKRMRYFDPLRNEYFFDRNRPSFDAILYYYQSGGRLRRP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VNVPLDIFSEEIRFYELGEEAMEMFREDEGYI</span><span class="topo-unknown">KEEERPLPEN</span><span class="topo-inside">EFQRQVWLLFEYPESSGPAR</span><span class="topo-membrane">IIAIVSVMVILISIVSFCLE</span><span class="topo-outside">TLPIFR</span><span class="topo-unknown">DENEDMHGGGVTFHTYSQSTIGYQQSTS</span><span class="topo-outside">FTDP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-membrane">FIVETLCIIWFSFEFLVRFF</span><span class="topo-inside">ACPSK</span><span class="topo-unknown">AG</span><span class="topo-inside">FFTN</span><span class="topo-membrane">IMNIIDIVAIIPY</span><span class="topo-unknown">YVTIFLTESNKSVLQFQNVRR</span><span class="topo-outside">V</span><span class="topo-membrane">VQIFRIMRILRIFKLSRHSK</span><span class="topo-inside">GLQILGQTLKASM</span><span class="topo-membrane">RELGLLIFFLFIGVILFSSA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VYFA</span><span class="topo-outside">EADERDSQFPSI</span><span class="topo-unknown">PDAFFWAVVTMTTVGYG</span><span class="topo-outside">DMTPTTI</span><span class="topo-membrane">GGKIVGSLCAIAGVLTIALPV</span><span class="topo-inside">PVIVSNFNYFYHRET</span><span class="topo-unknown">EGEEQAQYLQVTSSPKIPSSPDLKKSRSASTISKSDYMEIQEGV</span></span>
<span class="topo-ruler">       490       500       510    </span>
<span class="topo-line"><span class="topo-unknown">NNSNEDFREENLKTANSTLANTNYVNITKMLTDV</span></span>
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
      <td>50</td>
      <td>-18</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>152</td>
      <td>32</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>162</td>
      <td>134</td>
      <td>143</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>163</td>
      <td>182</td>
      <td>144</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>202</td>
      <td>164</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>208</td>
      <td>184</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>236</td>
      <td>190</td>
      <td>217</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>237</td>
      <td>241</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>223</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>266</td>
      <td>243</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>268</td>
      <td>248</td>
      <td>249</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>269</td>
      <td>272</td>
      <td>250</td>
      <td>253</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>285</td>
      <td>254</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>267</td>
      <td>287</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>307</td>
      <td>307</td>
      <td>288</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>327</td>
      <td>289</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>328</td>
      <td>340</td>
      <td>309</td>
      <td>321</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>364</td>
      <td>322</td>
      <td>345</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>376</td>
      <td>346</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>393</td>
      <td>358</td>
      <td>374</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>394</td>
      <td>400</td>
      <td>375</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>421</td>
      <td>382</td>
      <td>402</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>436</td>
      <td>403</td>
      <td>417</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>437</td>
      <td>514</td>
      <td>418</td>
      <td>495</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7sit">7SIT</a> — Chain I (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">LQFYRNLGKSGLRVSCLGLGTWVTFGGQITDEMAEHLMTLAYDNGINLFDTAEVYAAGKAEVVLGNIIKKKGWRRSSLVITTKIFWGGKAETERGLSRKHIIEGLKASLERLQLEYVDV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VFANRPDPNTPMEETVRAMTHVINQGMAMYWGTSRWSSMEIMEAYSVARQFNLIPPICEQAEYHMFQREKVEVQLPELFHKIGVGAMTWSPLACGIVSGKYDSGIPPYSRASLKGYQWLK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330   </span>
<span class="topo-line"><span class="topo-inside">DKILSEEGRRQQAKLKELQAIAERLGCTLPQLAIAWCLRNEGVSSVLLGASNAEQLMENIGAIQVLPKLSSSIVHEIDSILGNKPYS</span><span class="topo-unknown">KKDYRS</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>35</td>
      <td>35</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>327</td>
      <td>36</td>
      <td>361</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>333</td>
      <td>362</td>
      <td>367</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7sit">7SIT</a> — Chain J (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAHHHHHHHHHHGLVPRGSMTVATGDPVDEAAAHPGHPQDTYDPEADHES</span><span class="topo-inside">SERVVINISGLRFETQLKTLAQFPETLLGDPKKRMRYFDPLRNEYFFDRNRPSFDAILYYYQSGGRLRRP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VNVPLDIFSEEIRFYELGEEAMEMFREDEGYI</span><span class="topo-unknown">KEEERPLPEN</span><span class="topo-inside">EFQRQVWLLFEYPESSGPAR</span><span class="topo-membrane">IIAIVSVMVILISIVSFCLE</span><span class="topo-outside">TLPIFR</span><span class="topo-unknown">DENEDMHGGGVTFHTYSQSTIGYQQSTS</span><span class="topo-outside">FTDP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-membrane">FIVETLCIIWFSFEFLVRFF</span><span class="topo-inside">ACPSK</span><span class="topo-unknown">AG</span><span class="topo-inside">FFTN</span><span class="topo-membrane">IMNIIDIVAIIPY</span><span class="topo-unknown">YVTIFLTESNKSVLQFQNVRR</span><span class="topo-outside">V</span><span class="topo-membrane">VQIFRIMRILRIFKLSRHSK</span><span class="topo-inside">GLQILGQTLKASM</span><span class="topo-membrane">RELGLLIFFLFIGVILFSSA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VYFA</span><span class="topo-outside">EADERDSQFPSI</span><span class="topo-unknown">PDAFFWAVVTMTTVGYG</span><span class="topo-outside">DMTPTTI</span><span class="topo-membrane">GGKIVGSLCAIAGVLTIALPV</span><span class="topo-inside">PVIVSNFNYFYHRET</span><span class="topo-unknown">EGEEQAQYLQVTSSPKIPSSPDLKKSRSASTISKSDYMEIQEGV</span></span>
<span class="topo-ruler">       490       500       510    </span>
<span class="topo-line"><span class="topo-unknown">NNSNEDFREENLKTANSTLANTNYVNITKMLTDV</span></span>
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
      <td>50</td>
      <td>-18</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>51</td>
      <td>152</td>
      <td>32</td>
      <td>133</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>162</td>
      <td>134</td>
      <td>143</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>163</td>
      <td>182</td>
      <td>144</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>202</td>
      <td>164</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>208</td>
      <td>184</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>236</td>
      <td>190</td>
      <td>217</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>237</td>
      <td>241</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>261</td>
      <td>223</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>266</td>
      <td>243</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>268</td>
      <td>248</td>
      <td>249</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>269</td>
      <td>272</td>
      <td>250</td>
      <td>253</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>285</td>
      <td>254</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>267</td>
      <td>287</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>307</td>
      <td>307</td>
      <td>288</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>327</td>
      <td>289</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>328</td>
      <td>340</td>
      <td>309</td>
      <td>321</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>364</td>
      <td>322</td>
      <td>345</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>376</td>
      <td>346</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>393</td>
      <td>358</td>
      <td>374</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>394</td>
      <td>400</td>
      <td>375</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>421</td>
      <td>382</td>
      <td>402</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>436</td>
      <td>403</td>
      <td>417</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>437</td>
      <td>514</td>
      <td>418</td>
      <td>495</td>
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

### Selectivity filter dilation in C-type inactivated state

The structure reveals that C-type inactivation involves a dilation of the selectivity filter at the S1 and S2 ion binding sites. The conserved Tyr373 reorients from facing the channel interior to facing the extracellular solution. Asp375 undergoes a corresponding conformational change. Together these changes widen the selectivity filter, disrupting the S1 and S2 K+ binding sites. The S3 and S4 sites remain intact with K+ bound. This is consistent with the dilation model for C-type inactivation proposed by Hoshi and Armstrong.

### Mechanism for external K+ effect on inactivation

The disruption of S1 and S2 sites provides a mechanism for the effect of extracellular K+ on C-type inactivation. When external K+ is high, occupancy of S1 and S2 sites increases, which slows the structural changes at these sites and thereby slows inactivation. This explains why elevated external K+ slows C-type inactivation.

### Propagation of structural changes to extracellular mouth

Changes at the selectivity filter propagate to the loop region linking the filter to TM6. The repositioning of Asp375 leads to increased surface exposure of residues 376-378 (equivalent to Shaker positions 448-450), consistent with previous studies showing enhanced modification rates of Cys substitutions at these positions in the inactivated state.

### Intersubunit Asp375-Thr377 interaction stabilizes inactivated state

The V377T substitution creates a new intersubunit hydrogen bond between Asp375 and Thr377 that stabilizes the selectivity filter in the C-type inactivated conformation. The Kv1.2-2.1-2m construct (W362F, S367T without V377T) shows slow inactivation similar to wild type, and its crystal structure (PDB 7SIZ) shows a conductive selectivity filter, confirming the importance of the Asp375-Thr377 interaction.

### E346-S6 loop coupling

The V377T substitution also affects the interaction of E346 in the S4-S5 linker with the pore-S6 loop region. In the inactivated structure, E346 forms a new H-bond with the protein backbone of Thr379, breaking previous H-bond interactions with Thr379 backbone and Thr380 side chain.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/shaker-kv1-2/">Shaker Kv1.2 Potassium Channel</a> — Parent channel; wild-type Kv1.2-2.1 structure (PDB 2R9R) used as molecular replacement model
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kv1-2-2-1-v406w/">Kv1.2-2.1 V406W Mutant Channel</a> — Previously proposed C-type inactivated state structure; comparison of filter dilation magnitude
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/">C-type Inactivation</a> — Primary structural evidence for selectivity filter dilation in C-type inactivation
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA Potassium Channel</a> — KcsA inactivation mechanism shares similarity with C-type inactivation in Kv channels
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
