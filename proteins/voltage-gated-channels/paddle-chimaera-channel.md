---
title: "Paddle-Chimaera Voltage-Dependent Potassium Channel"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein]
sources: [doi/10.1038##nature06265]
verified: false
---

# Paddle-Chimaera Voltage-Dependent Potassium Channel

## Overview

The paddle-chimaera channel is a chimeric voltage-dependent K+ (Kv) channel constructed by replacing the voltage-sensor paddle (S3b-S4 helix-turn-helix) of rat Kv1.2 with the corresponding region from rat Kv2.1. The structure was determined at 2.4 A resolution in a lipid membrane-like environment, with the pore and voltage sensors embedded in a bilayer-like arrangement of lipid molecules. This high-resolution structure revealed detailed atomic interactions of voltage sensors within a membrane environment, including charge stabilization by external and internal negative clusters, a phenylalanine gap separating the clusters, and the conformation of gating charges in the open state.

## Publications

### doi/10.1038##nature06265

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2r9r">2R9R</a></td>
      <td>2.4</td>
      <td>P42(1)2</td>
      <td>Paddle-chimaera channel (Kv1.2 backbone with Kv2.1 paddle residues VAIIPYYVTIFLTESNKSVLQFQNVRRVVQIFRIMRILRIFK), co-expressed with rat beta2.1 subunit in Pichia pastoris</td>
      <td>K+, NADP+</td>
    </tr>
  </tbody>
</table>

**Purification:**

- **Expression system**: Pichia pastoris
- **Expression construct**: Paddle-chimaera channel with N-terminal His10 tag and thrombin cleavage site, co-expressed with rat beta2.1 subunit (residues 36-367)
- **Tag info**: N-terminal His10 tag

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
      <td>Yeast transformation and expression</td>
      <td>Pichia pastoris fermentation</td>
      <td>—</td>
      <td></td>
      <td>Co-expression of paddle-chimaera channel and beta2.1 subunit</td>
    </tr>
    <tr>
      <td>Cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt affinity column</td>
      <td>not specified</td>
      <td>Protein concentrated to ~20 mg/ml after elution</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>150 mM KCl, 20 mM Tris-HCl pH 7.5, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 2 mM TCEP, 10 mM DTT + 3 mM <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a>, 3 mM Cymal-7</td>
      <td>Lipids (3:1:1 <a href="/xray-mp-wiki/reagents/lipids/popc/">POPC</a>:<a href="/xray-mp-wiki/reagents/lipids/pope/">POPE</a>:<a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a> at 0.1 mg/ml) included in gel filtration buffer. Elution between 11-12 ml showed correct Kv1.2:beta2.1 ratio.</td>
    </tr>
  </tbody>
</table>
**Final sample**: ~10 mg/ml in gel filtration buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Paddle-chimaera channel at 10 mg/ml in gel filtration buffer</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>28-36% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 50 mM Tris-HCl pH 8.5</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>5 days</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals approximately 200 um in each dimension. Detergents <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a>, Cymal-7, and CHAPS present. Lipids <a href="/xray-mp-wiki/reagents/lipids/popc/">POPC</a>, <a href="/xray-mp-wiki/reagents/lipids/pope/">POPE</a>, <a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a> present. Space group P42(1)2. Data collected to 2.4 A at NSLS beamline X29. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using Kv1.2 structure (PDB 2A79) as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2r9r">2R9R</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAHHHHHHHHHHGLVPRGSMTVATGDPVDEAAALPGHPQDTYDPEADHES</span><span class="topo-inside">SERVVINISGLRFETQLKTLAQFPETLLGDPKKRMRYFDPLRNEYFFDRNRPSFDAILYYYQSGGRLRRP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VNVPLDIFSEEIRFYELGEEAMEMFREDEGYIKEEERPLPENEFQRQVWLLFEYPESSGPAR</span><span class="topo-membrane">IIAIVSVMVILISIVSFCL</span><span class="topo-outside">ETLPIFRDENEDMHGGGVTFHTYSQSTIGYQQSTSFTDP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-membrane">FIVETLCIIWFSFEFLVRFF</span><span class="topo-inside">ACPSKAGFF</span><span class="topo-membrane">TNIMNIIDIVAIIPYYVTIFL</span><span class="topo-outside">TESNKSVLQFQNVRRV</span><span class="topo-membrane">VQIFRIMRILRIFKLSRHS</span><span class="topo-unknown">KGLQILGQTLKA</span><span class="topo-inside">SM</span><span class="topo-membrane">RELGLLIFFLFIGVILFSSA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VYFA</span><span class="topo-outside">EADERDSQFPSI</span><span class="topo-unknown">PDAFWWAVVSMTTVGY</span><span class="topo-outside">GDMVPTTI</span><span class="topo-membrane">GGKIVGSLCAIAGVLTIALPV</span><span class="topo-unknown">PVIVSNFNYFYHRE</span><span class="topo-inside">T</span><span class="topo-unknown">EGEEQAQYLQVTSSPKIPSSPDLKKSRSASTISKSDYMEIQEGV</span></span>
<span class="topo-ruler">       490       500       510    </span>
<span class="topo-line"><span class="topo-unknown">NNSNEDFREENLKTANSTLANTNYVNITKMLTDV</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>182</td>
      <td>32</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>201</td>
      <td>164</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>241</td>
      <td>183</td>
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
      <td>270</td>
      <td>243</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>291</td>
      <td>252</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>307</td>
      <td>273</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>326</td>
      <td>289</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>338</td>
      <td>308</td>
      <td>319</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>339</td>
      <td>340</td>
      <td>320</td>
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
      <td>392</td>
      <td>358</td>
      <td>373</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>374</td>
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
      <td>435</td>
      <td>403</td>
      <td>416</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>436</td>
      <td>436</td>
      <td>417</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2r9r">2R9R</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAHHHHHHHHHHGLVPRGSMTVATGDPVDEAAALPGHPQDTYDPEADHES</span><span class="topo-inside">SERVVINISGLRFETQLKTLAQFPETLLGDPKKRMRYFDPLRNEYFFDRNRPSFDAILYYYQSGGRLRRP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VNVPLDIFSEEIRFYELGEEAMEMFREDEGYIKEEERPLPENEFQRQVWLLFEYPESSGPAR</span><span class="topo-membrane">IIAIVSVMVILISIVSFCL</span><span class="topo-outside">ETLPIFRDENEDMHGGGVTFHTYSQSTIGYQQSTSFTDP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-membrane">FIVETLCIIWFSFEFLVRFF</span><span class="topo-inside">ACPSKAGFF</span><span class="topo-membrane">TNIMNIIDIVAIIPYYVTIFL</span><span class="topo-outside">TESNKSVLQFQNVRRV</span><span class="topo-membrane">VQIFRIMRILRIFKLSRHS</span><span class="topo-unknown">KGLQILGQTLKA</span><span class="topo-inside">SM</span><span class="topo-membrane">RELGLLIFFLFIGVILFSSA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VYFA</span><span class="topo-outside">EADERDSQFPSI</span><span class="topo-unknown">PDAFWWAVVSMTTVGY</span><span class="topo-outside">GDMVPTTI</span><span class="topo-membrane">GGKIVGSLCAIAGVLTIALPV</span><span class="topo-unknown">PVIVSNFNYFYHRE</span><span class="topo-inside">T</span><span class="topo-unknown">EGEEQAQYLQVTSSPKIPSSPDLKKSRSASTISKSDYMEIQEGV</span></span>
<span class="topo-ruler">       490       500       510    </span>
<span class="topo-line"><span class="topo-unknown">NNSNEDFREENLKTANSTLANTNYVNITKMLTDV</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>182</td>
      <td>32</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>201</td>
      <td>164</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>241</td>
      <td>183</td>
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
      <td>270</td>
      <td>243</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>291</td>
      <td>252</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>307</td>
      <td>273</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>326</td>
      <td>289</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>338</td>
      <td>308</td>
      <td>319</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>339</td>
      <td>340</td>
      <td>320</td>
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
      <td>392</td>
      <td>358</td>
      <td>373</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>374</td>
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
      <td>435</td>
      <td>403</td>
      <td>416</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>436</td>
      <td>436</td>
      <td>417</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2r9r">2R9R</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAHHHHHHHHHHGLVPRGSMTVATGDPVDEAAALPGHPQDTYDPEADHES</span><span class="topo-inside">SERVVINISGLRFETQLKTLAQFPETLLGDPKKRMRYFDPLRNEYFFDRNRPSFDAILYYYQSGGRLRRP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VNVPLDIFSEEIRFYELGEEAMEMFREDEGYIKEEERPLPENEFQRQVWLLFEYPESSGPAR</span><span class="topo-membrane">IIAIVSVMVILISIVSFCL</span><span class="topo-outside">ETLPIFRDENEDMHGGGVTFHTYSQSTIGYQQSTSFTDP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-membrane">FIVETLCIIWFSFEFLVRFF</span><span class="topo-inside">ACPSKAGFF</span><span class="topo-membrane">TNIMNIIDIVAIIPYYVTIFL</span><span class="topo-outside">TESNKSVLQFQNVRRV</span><span class="topo-membrane">VQIFRIMRILRIFKLSRHS</span><span class="topo-unknown">KGLQILGQTLKA</span><span class="topo-inside">SM</span><span class="topo-membrane">RELGLLIFFLFIGVILFSSA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VYFA</span><span class="topo-outside">EADERDSQFPSI</span><span class="topo-unknown">PDAFWWAVVSMTTVGY</span><span class="topo-outside">GDMVPTTI</span><span class="topo-membrane">GGKIVGSLCAIAGVLTIALPV</span><span class="topo-unknown">PVIVSNFNYFYHRE</span><span class="topo-inside">T</span><span class="topo-unknown">EGEEQAQYLQVTSSPKIPSSPDLKKSRSASTISKSDYMEIQEGV</span></span>
<span class="topo-ruler">       490       500       510    </span>
<span class="topo-line"><span class="topo-unknown">NNSNEDFREENLKTANSTLANTNYVNITKMLTDV</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>182</td>
      <td>32</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>201</td>
      <td>164</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>241</td>
      <td>183</td>
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
      <td>270</td>
      <td>243</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>291</td>
      <td>252</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>307</td>
      <td>273</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>326</td>
      <td>289</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>338</td>
      <td>308</td>
      <td>319</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>339</td>
      <td>340</td>
      <td>320</td>
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
      <td>392</td>
      <td>358</td>
      <td>373</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>374</td>
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
      <td>435</td>
      <td>403</td>
      <td>416</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>436</td>
      <td>436</td>
      <td>417</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2r9r">2R9R</a> — Chain E (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAHHHHHHHHHHGLVPRGSMTVATGDPVDEAAALPGHPQDTYDPEADHES</span><span class="topo-inside">SERVVINISGLRFETQLKTLAQFPETLLGDPKKRMRYFDPLRNEYFFDRNRPSFDAILYYYQSGGRLRRP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VNVPLDIFSEEIRFYELGEEAMEMFREDEGYIKEEERPLPENEFQRQVWLLFEYPESSGPAR</span><span class="topo-membrane">IIAIVSVMVILISIVSFCL</span><span class="topo-outside">ETLPIFRDENEDMHGGGVTFHTYSQSTIGYQQSTSFTDP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">F</span><span class="topo-membrane">FIVETLCIIWFSFEFLVRFF</span><span class="topo-inside">ACPSKAGFF</span><span class="topo-membrane">TNIMNIIDIVAIIPYYVTIFL</span><span class="topo-outside">TESNKSVLQFQNVRRV</span><span class="topo-membrane">VQIFRIMRILRIFKLSRHS</span><span class="topo-unknown">KGLQILGQTLKA</span><span class="topo-inside">SM</span><span class="topo-membrane">RELGLLIFFLFIGVILFSSA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VYFA</span><span class="topo-outside">EADERDSQFPSI</span><span class="topo-unknown">PDAFWWAVVSMTTVGY</span><span class="topo-outside">GDMVPTTI</span><span class="topo-membrane">GGKIVGSLCAIAGVLTIALPV</span><span class="topo-unknown">PVIVSNFNYFYHRE</span><span class="topo-inside">T</span><span class="topo-unknown">EGEEQAQYLQVTSSPKIPSSPDLKKSRSASTISKSDYMEIQEGV</span></span>
<span class="topo-ruler">       490       500       510    </span>
<span class="topo-line"><span class="topo-unknown">NNSNEDFREENLKTANSTLANTNYVNITKMLTDV</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>182</td>
      <td>32</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>201</td>
      <td>164</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>202</td>
      <td>241</td>
      <td>183</td>
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
      <td>270</td>
      <td>243</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>291</td>
      <td>252</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>307</td>
      <td>273</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>326</td>
      <td>289</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>338</td>
      <td>308</td>
      <td>319</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>339</td>
      <td>340</td>
      <td>320</td>
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
      <td>392</td>
      <td>358</td>
      <td>373</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>393</td>
      <td>400</td>
      <td>374</td>
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
      <td>435</td>
      <td>403</td>
      <td>416</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>436</td>
      <td>436</td>
      <td>417</td>
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

### Voltage-sensor architecture in a membrane-like environment

The 2.4 A structure reveals the voltage sensor in atomic detail within a membrane-like arrangement of lipids. The voltage-sensor paddle (S3b-S4) is tilted away from the central axis of the voltage sensor, towards the lipid membrane, making minimal contact with the remainder of the channel. One entire face of the voltage-sensor paddle is exposed to the lipid membrane.

### Negative clusters and the phenylalanine gap

Negatively charged amino acids form two clusters: an external negative cluster (Glu183 in S1, Glu226 in S2) and an internal negative cluster (Glu154 in S0, Glu236 in S2, Asp259 in S3a), separated by approximately 15 A. Phe233, the single most conserved amino acid in Kv channels outside the selectivity filter, separates the two clusters in a 'phenylalanine gap' - a hydrophobic zone of roughly 10 A that may create an energy barrier for arginine side chains, preventing proton transfer and favoring a switch-like transition between closed and open conformations.

### Gating charge disposition in the open state

In the open conformation, positively charged residues on S4 are positioned such that R0, R1, and R2 are in or close to the extracellular solution. R3 and R4 form ionized hydrogen bonds with the external negative cluster. K5 and R6 form ionized hydrogen bonds with the internal negative cluster. The S4 helix adopts a 3_10-helix hydrogen-bonding pattern below position 296 (R3), stretching the helix and allowing the voltage-sensor paddle to reside closer to the extracellular side.

### Lipid interactions and bilayer-like arrangement

Multiple complete and/or partial lipid molecules surround the channel, with a bilayer-like arrangement near the protein surface. Lipids are most dense in the concave hemi-circles between voltage sensors. A displaced phospholipid molecule is wedged between the voltage sensor and the S4-S5 linker, a region that couples voltage-sensor motions to pore gating.

### Gating mechanism inferred from structure

The structure suggests that during closure, the voltage-sensor paddle moves relative to S1 and S2, translating S4 gating charges ~15 A towards the intracellular side. The 3_10-helical region may shift as a moving segment along S4 in a wave-like 'concertina effect', turning arginine residues away from the lipid membrane as they cross the hydrophobic core.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/shaker-kv1-2/">Shaker Kv1.2 Potassium Channel</a> — Parent channel backbone for the paddle-chimaera construct
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kvap/">KvAP Voltage-Dependent Potassium Channel</a> — Prokaryotic Kv channel used for structural comparison
- <a href="/xray-mp-wiki/concepts/construct-design/voltage-sensor-paddle/">Voltage-Sensor Paddle</a> — The voltage-sensor paddle concept characterized by this structure
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/lipids/popc/">POPC</a> — Additive used in purification or crystallization buffers
