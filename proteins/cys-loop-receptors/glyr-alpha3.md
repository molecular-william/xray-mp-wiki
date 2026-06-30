---
title: "Human Glycine Receptor Alpha 3 (GlyRα3)"
created: 2026-05-28
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.04.007]
verified: false
---

# Human Glycine Receptor Alpha 3 (GlyRα3)

## Overview

Human [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) receptor alpha 3 (GlyRα3) is a [Pentameric Ligand-Gated Ion Channel (pLGIC)](/xray-mp-wiki/concepts/signaling-receptors/cys-loop-receptor-family/) belonging to the [Cys-Loop Receptor Family](/xray-mp-wiki/concepts/signaling-receptors/cys-loop-receptor-family/) family. It mediates fast inhibitory neurotransmission in the central nervous system by allowing chloride ions to flow through its transmembrane pore upon [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) binding. GlyRα3 is the primary isoform responsible for the analgesic effects of delta-9-tetrahydrocannabinol, making it a therapeutic target for neuropathic pain. Crystal structures of GlyRα3 in complex with [Glycine](/xray-mp-wiki/reagents/buffers/glycine/), the potentiator [AM-3607](/xray-mp-wiki/reagents/ligands/am-3607), and [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) have revealed the molecular basis of channel gating and [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) in vertebrate Cys-loop receptors.


## Publications

### doi/10.1016##j.str.2017.04.007

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5vdh">5VDH</a></td>
      <td>2.85 A</td>
      <td>P43212</td>
      <td>GlyRα3 crystallization construct</td>
      <td>AM-3607, glycine, ivermectin</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5vdi">5VDI</a></td>
      <td>3.08 A</td>
      <td>P2121</td>
      <td>GlyRα3 crystallization construct with N38Q mutation</td>
      <td>AM-3607, glycine, ivermectin</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Not specified in this paper
- **Construct**: GlyRα3 crystallization construct and N38Q mutant. Construct details from Huang et al., 2016.


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
      <td>Protein expression</td>
      <td>As described in Huang et al., 2016</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Construct details from Huang et al., 2016</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>As described in Huang et al., 2016</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Purification protocol from Huang et al., 2016</td>
    </tr>
  </tbody>
</table>
**Final sample**: --

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion Crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GlyRα3cryst or GlyRα3crystN38Q pre-equilibrated with <a href="/xray-mp-wiki/reagents/ligands/am-3607">AM-3607</a>, <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a>, and <a href="/xray-mp-wiki/reagents/ligands/ivermectin/">Ivermectin</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES Buffer</a> pH 6.5, 50 mM CaCl2</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1 protein to reservoir</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td><a href="/xray-mp-wiki/reagents/additives/peg">PEG (Polyethylene Glycol)</a>350MME</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Two crystal forms solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> with Phaser. 5VDH in space group P43212 at 2.85 A resolution. 5VDI in space group P2121 at 3.08 A resolution.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vdh">5VDH</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ARSRSAP</span><span class="topo-outside">MSPSDFLDKLMGRTSGYDARIRPNFKGPPVNVTCNIFINSFGSIAETTMDYRVNIFLRQKWNDPRLAYSEYPDDSLDLDPSMLDSIWKPDLFFANEKGANFHEVTTDNKLLRI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FKNGNVLYSIRLTLTLSCPMDLKNFPMDVQTCIMQLESFGYTMNDLIFEWQDEAPVQVAEGLTLPQFLLKEEKDLRYCTKHYNTGKFTCIEVRFHLERQMGYYLIQM</span><span class="topo-membrane">YIPSLLIVILSWV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SFWI</span><span class="topo-inside">NMDA</span><span class="topo-membrane">APARVALGITTVLTMTTQSS</span><span class="topo-outside">GSRASLPKVSYVKAID</span><span class="topo-membrane">IWMAVCLLFVFSALLEYAAVN</span><span class="topo-inside">FVSRAGTKVFIDRAKKI</span><span class="topo-membrane">DTISRACFPLAFLIFNIFYWVI</span><span class="topo-outside">Y</span><span class="topo-unknown">KILRHEDIHWSHPQF</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EK</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>8</td>
      <td>227</td>
      <td>8</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>228</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>248</td>
      <td>245</td>
      <td>248</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>268</td>
      <td>249</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>284</td>
      <td>269</td>
      <td>284</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>305</td>
      <td>285</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>306</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>344</td>
      <td>323</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>345</td>
      <td>345</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vdh">5VDH</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ARSRS</span><span class="topo-outside">APMSPSDFLDKLMGRTSGYDARIRPNFKGPPVNVTCNIFINSFGSIAETTMDYRVNIFLRQKWNDPRLAYSEYPDDSLDLDPSMLDSIWKPDLFFANEKGANFHEVTTDNKLLRI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FKNGNVLYSIRLTLTLSCPMDLKNFPMDVQTCIMQLESFGYTMNDLIFEWQDEAPVQVAEGLTLPQFLLKEEKDLRYCTKHYNTGKFTCIEVRFHLERQMGYYLIQM</span><span class="topo-membrane">YIPSLLIVILSWV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SFWI</span><span class="topo-inside">NMDA</span><span class="topo-membrane">APARVALGITTVLTMTTQSS</span><span class="topo-outside">GSRASLPKVSYVKAID</span><span class="topo-membrane">IWMAVCLLFVFSALLEYAAVN</span><span class="topo-inside">FVSRAGTKVFIDRAKKI</span><span class="topo-membrane">DTISRACFPLAFLIFNIFYWVI</span><span class="topo-outside">YKIL</span><span class="topo-unknown">RHEDIHWSHPQF</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EK</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>6</td>
      <td>227</td>
      <td>6</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>228</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>248</td>
      <td>245</td>
      <td>248</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>268</td>
      <td>249</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>284</td>
      <td>269</td>
      <td>284</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>305</td>
      <td>285</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>306</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>344</td>
      <td>323</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>348</td>
      <td>345</td>
      <td>348</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vdh">5VDH</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ARSRSAP</span><span class="topo-outside">MSPSDFLDKLMGRTSGYDARIRPNFKGPPVNVTCNIFINSFGSIAETTMDYRVNIFLRQKWNDPRLAYSEYPDDSLDLDPSMLDSIWKPDLFFANEKGANFHEVTTDNKLLRI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FKNGNVLYSIRLTLTLSCPMDLKNFPMDVQTCIMQLESFGYTMNDLIFEWQDEAPVQVAEGLTLPQFLLKEEKDLRYCTKHYNTGKFTCIEVRFHLERQMGYYLIQM</span><span class="topo-membrane">YIPSLLIVILSWV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SFWI</span><span class="topo-inside">NMDA</span><span class="topo-membrane">APARVALGITTVLTMTTQSS</span><span class="topo-outside">GSRASLPKVSYVKAID</span><span class="topo-membrane">IWMAVCLLFVFSALLEYAAVN</span><span class="topo-inside">FVSRAGTKVFIDRAKKI</span><span class="topo-membrane">DTISRACFPLAFLIFNIFYWVI</span><span class="topo-outside">Y</span><span class="topo-unknown">KILRHEDIHWSHPQF</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EK</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>8</td>
      <td>227</td>
      <td>8</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>228</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>248</td>
      <td>245</td>
      <td>248</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>268</td>
      <td>249</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>284</td>
      <td>269</td>
      <td>284</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>305</td>
      <td>285</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>306</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>344</td>
      <td>323</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>345</td>
      <td>345</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vdh">5VDH</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AR</span><span class="topo-outside">SRSAPMSPSDFLDKLMGRTSGYDARIRPNFKGPPVNVTCNIFINSFGSIAETTMDYRVNIFLRQKWNDPRLAYSEYPDDSLDLDPSMLDSIWKPDLFFANEKGANFHEVTTDNKLLRI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FKNGNVLYSIRLTLTLSCPMDLKNFPMDVQTCIMQLESFGYTMNDLIFEWQDEAPVQVAEGLTLPQFLLKEEKDLRYCTKHYNTGKFTCIEVRFHLERQMGYYLIQM</span><span class="topo-membrane">YIPSLLIVILSWV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SFWI</span><span class="topo-inside">NMDA</span><span class="topo-membrane">APARVALGITTVLTMTTQSS</span><span class="topo-outside">GSRASLPKVSYVKAID</span><span class="topo-membrane">IWMAVCLLFVFSALLEYAAVN</span><span class="topo-inside">FVSRAGTKVFIDRAKKI</span><span class="topo-membrane">DTISRACFPLAFLIFNIFYWVI</span><span class="topo-outside">Y</span><span class="topo-unknown">KILRHEDIHWSHPQF</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EK</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>3</td>
      <td>227</td>
      <td>3</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>228</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>248</td>
      <td>245</td>
      <td>248</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>268</td>
      <td>249</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>284</td>
      <td>269</td>
      <td>284</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>305</td>
      <td>285</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>306</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>344</td>
      <td>323</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>345</td>
      <td>345</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vdh">5VDH</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ARSRSAP</span><span class="topo-outside">MSPSDFLDKLMGRTSGYDARIRPNFKGPPVNVTCNIFINSFGSIAETTMDYRVNIFLRQKWNDPRLAYSEYPDDSLDLDPSMLDSIWKPDLFFANEKGANFHEVTTDNKLLRI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FKNGNVLYSIRLTLTLSCPMDLKNFPMDVQTCIMQLESFGYTMNDLIFEWQDEAPVQVAEGLTLPQFLLKEEKDLRYCTKHYNTGKFTCIEVRFHLERQMGYYLIQM</span><span class="topo-membrane">YIPSLLIVILSWV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SFWI</span><span class="topo-inside">NMDA</span><span class="topo-membrane">APARVALGITTVLTMTTQSS</span><span class="topo-outside">GSRASLPKVSYVKAID</span><span class="topo-membrane">IWMAVCLLFVFSALLEYAAVN</span><span class="topo-inside">FVSRAGTKVFIDRAKKI</span><span class="topo-membrane">DTISRACFPLAFLIFNIFYWVI</span><span class="topo-outside">Y</span><span class="topo-unknown">KILRHEDIHWSHPQF</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EK</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>8</td>
      <td>227</td>
      <td>8</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>228</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>248</td>
      <td>245</td>
      <td>248</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>268</td>
      <td>249</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>284</td>
      <td>269</td>
      <td>284</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>305</td>
      <td>285</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>306</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>344</td>
      <td>323</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>345</td>
      <td>345</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vdi">5VDI</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ARSRSAP</span><span class="topo-inside">MSPSDFLDKLMGRTSGYDARIRPNFKGPPVQVTCNIFINSFGSIAETTMDYRVNIFLRQKWNDPRLAYSEYPDDSLDLDPSMLDSIWKPDLFFANEKGANFHEVTTDNKLLRI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FKNGNVLYSIRLTLTLSCPMDLKNFPMDVQTCIMQLESFGYTMNDLIFEWQDEAPVQVAEGLTLPQFLLKEEKDLRYCTKHYNTGKFTCIEVRFHLERQMGYYL</span><span class="topo-membrane">IQMYIPSLLIVILSWV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SFWI</span><span class="topo-outside">NMDA</span><span class="topo-membrane">APARVALGITTVLTMTTQSSG</span><span class="topo-inside">SRASLPKVSYVKAI</span><span class="topo-membrane">DIWMAVCLLFVFSALLEYAAVN</span><span class="topo-outside">FVSRAGTKVFIDRAKKI</span><span class="topo-membrane">DTISRACFPLAFLIFNIFYWVI</span><span class="topo-inside">Y</span><span class="topo-unknown">KILRHEDIHWSHPQF</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EK</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>8</td>
      <td>224</td>
      <td>8</td>
      <td>224</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>244</td>
      <td>225</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>248</td>
      <td>245</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>269</td>
      <td>249</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>283</td>
      <td>270</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>305</td>
      <td>284</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>306</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>344</td>
      <td>323</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>345</td>
      <td>345</td>
      <td>345</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vdi">5VDI</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ARSRS</span><span class="topo-inside">APMSPSDFLDKLMGRTSGYDARIRPNFKGPPVQVTCNIFINSFGSIAETTMDYRVNIFLRQKWNDPRLAYSEYPDDSLDLDPSMLDSIWKPDLFFANEKGANFHEVTTDNKLLRI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FKNGNVLYSIRLTLTLSCPMDLKNFPMDVQTCIMQLESFGYTMNDLIFEWQDEAPVQVAEGLTLPQFLLKEEKDLRYCTKHYNTGKFTCIEVRFHLERQMGYYL</span><span class="topo-membrane">IQMYIPSLLIVILSWV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SFWI</span><span class="topo-outside">NMDA</span><span class="topo-membrane">APARVALGITTVLTMTTQSSG</span><span class="topo-inside">SRASLPKVSYVKAI</span><span class="topo-membrane">DIWMAVCLLFVFSALLEYAAVN</span><span class="topo-outside">FVSRAGTKVFIDRAKKI</span><span class="topo-membrane">DTISRACFPLAFLIFNIFYWVI</span><span class="topo-inside">YKIL</span><span class="topo-unknown">RHEDIHWSHPQF</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EK</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>6</td>
      <td>224</td>
      <td>6</td>
      <td>224</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>244</td>
      <td>225</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>248</td>
      <td>245</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>269</td>
      <td>249</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>283</td>
      <td>270</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>305</td>
      <td>284</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>306</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>344</td>
      <td>323</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>348</td>
      <td>345</td>
      <td>348</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vdi">5VDI</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ARSRSAP</span><span class="topo-inside">MSPSDFLDKLMGRTSGYDARIRPNFKGPPVQVTCNIFINSFGSIAETTMDYRVNIFLRQKWNDPRLAYSEYPDDSLDLDPSMLDSIWKPDLFFANEKGANFHEVTTDNKLLRI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FKNGNVLYSIRLTLTLSCPMDLKNFPMDVQTCIMQLESFGYTMNDLIFEWQDEAPVQVAEGLTLPQFLLKEEKDLRYCTKHYNTGKFTCIEVRFHLERQMGYYL</span><span class="topo-membrane">IQMYIPSLLIVILSWV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SFWI</span><span class="topo-outside">NMDA</span><span class="topo-membrane">APARVALGITTVLTMTTQSSG</span><span class="topo-inside">SRASLPKVSYVKAI</span><span class="topo-membrane">DIWMAVCLLFVFSALLEYAAVN</span><span class="topo-outside">FVSRAGTKVFIDRAKKI</span><span class="topo-membrane">DTISRACFPLAFLIFNIFYWVI</span><span class="topo-inside">Y</span><span class="topo-unknown">KILRHEDIHWSHPQF</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EK</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>8</td>
      <td>224</td>
      <td>8</td>
      <td>224</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>244</td>
      <td>225</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>248</td>
      <td>245</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>269</td>
      <td>249</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>283</td>
      <td>270</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>305</td>
      <td>284</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>306</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>344</td>
      <td>323</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>345</td>
      <td>345</td>
      <td>345</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vdi">5VDI</a> — Chain D (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ARSRSA</span><span class="topo-inside">PMSPSDFLDKLMGRTSGYDARIRPNFKGPPVQVTCNIFINSFGSIAETTMDYRVNIFLRQKWNDPRLAYSEYPDDSLDLDPSMLDSIWKPDLFFANEKGANFHEVTTDNKLLRI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FKNGNVLYSIRLTLTLSCPMDLKNFPMDVQTCIMQLESFGYTMNDLIFEWQDEAPVQVAEGLTLPQFLLKEEKDLRYCTKHYNTGKFTCIEVRFHLERQMGYYL</span><span class="topo-membrane">IQMYIPSLLIVILSWV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SFWI</span><span class="topo-outside">NMDA</span><span class="topo-membrane">APARVALGITTVLTMTTQSSG</span><span class="topo-inside">SRASLPKVSYVKAI</span><span class="topo-membrane">DIWMAVCLLFVFSALLEYAAVN</span><span class="topo-outside">FVSRAGTKVFIDRAKKI</span><span class="topo-membrane">DTISRACFPLAFLIFNIFYWVI</span><span class="topo-inside">YKI</span><span class="topo-unknown">LRHEDIHWSHPQF</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EK</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>7</td>
      <td>224</td>
      <td>7</td>
      <td>224</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>244</td>
      <td>225</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>248</td>
      <td>245</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>269</td>
      <td>249</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>283</td>
      <td>270</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>305</td>
      <td>284</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>306</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>344</td>
      <td>323</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>347</td>
      <td>345</td>
      <td>347</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5vdi">5VDI</a> — Chain E (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ARSRSAP</span><span class="topo-inside">MSPSDFLDKLMGRTSGYDARIRPNFKGPPVQVTCNIFINSFGSIAETTMDYRVNIFLRQKWNDPRLAYSEYPDDSLDLDPSMLDSIWKPDLFFANEKGANFHEVTTDNKLLRI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FKNGNVLYSIRLTLTLSCPMDLKNFPMDVQTCIMQLESFGYTMNDLIFEWQDEAPVQVAEGLTLPQFLLKEEKDLRYCTKHYNTGKFTCIEVRFHLERQMGYYL</span><span class="topo-membrane">IQMYIPSLLIVILSWV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SFWI</span><span class="topo-outside">NMDA</span><span class="topo-membrane">APARVALGITTVLTMTTQSSG</span><span class="topo-inside">SRASLPKVSYVKAI</span><span class="topo-membrane">DIWMAVCLLFVFSALLEYAAVN</span><span class="topo-outside">FVSRAGTKVFIDRAKKI</span><span class="topo-membrane">DTISRACFPLAFLIFNIFYWVI</span><span class="topo-inside">Y</span><span class="topo-unknown">KILRHEDIHWSHPQF</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EK</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>8</td>
      <td>224</td>
      <td>8</td>
      <td>224</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>244</td>
      <td>225</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>248</td>
      <td>245</td>
      <td>248</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>269</td>
      <td>249</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>283</td>
      <td>270</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>305</td>
      <td>284</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>306</td>
      <td>322</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>344</td>
      <td>323</td>
      <td>344</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>345</td>
      <td>345</td>
      <td>345</td>
      <td>345</td>
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

### Ivermectin binding site and pore expansion mechanism

[Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) binds in the transmembrane domain of GlyRα3 at the interface between adjacent subunits, acting as a positive [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/). The binding pocket is formed by the M2, M3, and M4 helices at the plus subunit interface. Key residues include Ser267 on M2 and Ala288 on M3. Binding of [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) causes the M2 helices to tilt outward at the extracellular end while tapering inward at the intracellular end, rotating the 9' Leu261 residues out of the pore and expanding the extracellular portion of the channel. The expanded extracellular pore is stabilized by inter-subunit hydrogen bonds between Arg271 (M2+) and Gln226 (M1-). The direct binding of [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) wedges apart M3(+) and M1(-) by about 3 Angstroms and drags M2 away from the pore axis, opening the ion channel.

### Desensitized state of GlyRα3

The crystal structures of AM-3607/glycine/ivermectin-bound GlyRα3 delineate a partially open or desensitized state. While the M2 helices tilt outward and the 9' Leu261 residues rotate out of the pore, the radius at the intracellular end defined by the -2' Pro250 is only 1.4 A, too narrow to permit chloride passage. Thus -2' Pro250 serves as the desensitization gate. The desensitized state is essentially identical to the desensitized GlyRα1 structure, with the intracellular half of the TMD tilting away from the pore in both open and desensitized states.

### Structural basis for ivermectin selectivity between GlyR and GluCl

Comparison with the [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/)-bound [GluCl (GABA-Gated Chloride Channel from C. elegans)](/xray-mp-wiki/proteins/glucl) structure reveals why [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) activates GlyRs less potently than invertebrate glutamate-gated chloride channels. Ala288 in the M3 helix of GlyRα3 at the mouth of the [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) binding cleft is replaced by a smaller Gly281 in [GluCl (GABA-Gated Chloride Channel from C. elegans)](/xray-mp-wiki/proteins/glucl). As a result, [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) is buried about 1 A deeper in the cleft of [GluCl (GABA-Gated Chloride Channel from C. elegans)](/xray-mp-wiki/proteins/glucl) than in GlyRα3, leading to higher [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) potency for [GluCl (GABA-Gated Chloride Channel from C. elegans)](/xray-mp-wiki/proteins/glucl). C10 of [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) is 4.7 A from the C-alpha of Ala288 in GlyRα3 but only 3.5 A from the C-alpha of Gly281 in [GluCl (GABA-Gated Chloride Channel from C. elegans)](/xray-mp-wiki/proteins/glucl). This is consistent with functional data where wild-type [GluCl (GABA-Gated Chloride Channel from C. elegans)](/xray-mp-wiki/proteins/glucl) and the Ala288Gly mutant of GlyRα1 show an [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) EC50 of around 40 nM, while wild-type GlyRα1 has an EC50 of 1.2 uM.

### Therapeutic implications for neuropathic pain

The analgesic effects of delta-9-tetrahydrocannabinol are mediated through potentiation of GlyRα3, particularly via binding in the transmembrane domain with Ser296 of M3 being critical for THC potentiation. Ser296 is only about 7 A from the [Ivermectin](/xray-mp-wiki/reagents/ligands/ivermectin/) binding site in the GlyRα3 crystal structures. These structures provide a valuable structural basis for screening and designing novel pain therapeutics that act on the transmembrane domain of GlyRα3.


## Cross-References

- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/glic/">GLIC (Gloeobacter violaceus Ion Channel)</a> — Prokaryotic Cys-loop receptor homolog; model system for anesthetic action on pLGICs
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/glic-ecd/">GLIC ECD</a> — Isolated extracellular domain of GLIC; related Cys-loop receptor structure
- <a href="/xray-mp-wiki/reagents/ligands/ketamine/">Ketamine</a> — Anesthetic ligand binding to Cys-loop receptors; related allosteric modulation
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/">Allosteric Regulation in Membrane Proteins</a> — Ivermectin acts as a positive allosteric modulator of GlyR
- <a href="/xray-mp-wiki/reagents/ligands/ivermectin/">Ivermectin</a> — Positive allosteric modulator binding to transmembrane domain of GlyRα3
- <a href="/xray-mp-wiki/reagents/ligands/am-3607/">AM-3607</a> — Novel analgesic potentiator binding to GlyRα3 transmembrane domain
- <a href="/xray-mp-wiki/reagents/buffers/mes/">2-(N-Morpholino)ethanesulfonic Acid (MES)</a> — Crystallization buffer at pH 6.5 used for GlyRα3 crystal forms 5VDH and 5VDI
- <a href="/xray-mp-wiki/reagents/additives/calcium-chloride/">Calcium Chloride (CaCl₂)</a> — Crystallization additive (50 mM) used for GlyRα3 crystal forms 5VDH and 5VDI
- <a href="/xray-mp-wiki/concepts/signaling-receptors/cys-loop-receptor-family/">Pentameric Ligand-Gated Ion Channel (pLGIC)</a> — Referenced in glyr-alpha3
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion Crystallization</a> — Referenced in glyr-alpha3
