---
title: "Engineered Paddle-Chimera Voltage-Gated Potassium Channel"
created: 2026-06-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2005.12.035]
verified: none
uniprot_id: P62483
---

# Engineered Paddle-Chimera Voltage-Gated Potassium Channel

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P62483">UniProt: P62483</a>

<span class="expr-badge">Rattus norvegicus</span>

## Overview

The Paddle-Chimera (PTR) is an engineered voltage-gated potassium channel created by replacing the S3b-S4 paddle motif of the KvAP voltage sensor with the corresponding paddle motif from the Kv1.2 channel. This chimera was designed to capture the voltage-sensing mechanism in an activated conformation. The structure reveals how the paddle motif moves across the membrane electric field to couple voltage sensing to pore opening.

## Publications

### doi/10.1016##j.cell.2005.12.035

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
      <td>2.8</td>
      <td>P212121</td>
      <td>KvAP paddle-chimera with S3b-S4 motif from Kv1.2, residues 1-261</td>
      <td>Not specified</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length paddle-chimera channel cloned into pET vector with [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) [6xHis](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag

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
      <td><a href="/xray-mp-wiki/methods/purification/microfluidizer/">Microfluidizer</a> cell disruptor</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> + --</td>
      <td>Lysate clarified by centrifugation at 40,000g</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) agarose resin</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (wash), 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (elution) + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>His-tagged protein eluted and pooled</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Monodisperse peak fractions concentrated to 10 mg/mL</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-drop</a> <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PTR channel at 10 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">ammonium sulfate</a>, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 30% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>7-14 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td><a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene glycol</a> 25% v/v in reservoir solution</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Phased by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using KvAP structure (PDB 1ORQ) as search model. Crystals diffracted to 2.8 Angstrom resolution.</td>
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

### Paddle motif voltage-sensing mechanism

The paddle-chimera structure captures the voltage sensor paddle (S3b-S4 helix-turn-helix) in an activated conformation, demonstrating that the paddle motif moves across the membrane electric field to couple voltage sensing to pore opening.


## Cross-References

- <a href="/xray-mp-wiki/proteins/kvap/">KvAP Voltage-Gated Potassium Channel</a> — Parent voltage-gated potassium channel used as backbone for chimera construction
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/voltage-sensing/">Voltage Sensing Mechanism</a> — PTR structure reveals voltage sensor paddle movement
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Primary detergent used in purification and crystallization
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> — Affinity resin for His-tag purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography (SEC)</a> — Final purification step using Superdex 200
