---
title: "Thermotoga maritima CorA Mg2+ Transporter"
created: 2026-06-10
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature04642, doi/10.1126##science.1127121, doi/10.1038##sj.emboj.7601269]
verified: false
---

# Thermotoga maritima CorA Mg2+ Transporter

## Overview

The [CorA Magnesium Transporter from Thermotoga maritima](/xray-mp-wiki/proteins/slc-transporters/thermotoga-maritima-cora/) is the founding structural model for the CorA/MRS2 family of Mg2+ transporters, which constitute the primary Mg2+ uptake system in most prokaryotes and functional homologues of the eukaryotic mitochondrial magnesium transporter. The structure was determined as a full-length protein in an apparent closed state at 3.9 A resolution (Nature 2006) and subsequently at 2.9 A resolution (Science 2006). The transporter is a funnel-shaped homopentamer with two transmembrane helices per monomer. The channel pore is formed by five inner helices and putatively gated by bulky hydrophobic residues. The cytoplasmic domain forms a large funnel with metal-binding regulatory sites (M1, M2) that sense intracellular Mg2+ concentration.


## Publications

### doi/10.1038##nature04642

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2bbj">2BBJ</a></td>
      <td>1.85</td>
      <td>Not specified</td>
      <td>N-terminal soluble domain of T. maritima CorA (residues 1-266)</td>
      <td>Mg2+, Na+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length Thermotoga maritima CorA

**Purification:**

- **Expression system**: Escherichia coli
- **Expression construct**: Full-length T. maritima CorA and N-terminal domain (residues 1-266) as fusions to N-terminal six-histidine tag in modified T7 polymerase expression vector

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
      <td>Cell lysis and membrane isolation</td>
      <td>Centrifugation</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 1% n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Protease inhibitors added to lysis buffer</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Nickel <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA</td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
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
      <td>Full-length T. maritima CorA</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a>, 0.3 M Mg(NO3)2, 0.1 M Tris pH 8.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of full-length CorA diffracted to 3.9 A</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Soluble N-terminal domain (residues 1-266)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>35% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350, 0.2 M MgCl2, 0.1 M Tris pH 8.5</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Soluble domain crystallized to 1.85 A</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2bbj">2BBJ</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GSHMEEKRLSA</span><span class="topo-inside">KKGLPPGTLVYTGKYREDFEIEVMNYSIEEFREFKTTDVESVLPFRDSS</span></span>
<span class="topo-line"><span class="topo-inside">TPTWINITGIHRTDVVQRVGEFFGIHPLVLEDILNVHQRPKVEFFENYVFIVLKMFTYDK</span></span>
<span class="topo-line"><span class="topo-inside">NLHELESEQVSLILTKNCVLMFQEKIGDVFDPVRERIRYNRGIIRKKRADYLLYSLIDAL</span></span>
<span class="topo-line"><span class="topo-inside">VDDYFVLLEKIDDEIDVLEEEVLERPEKETVQRTHQLKRNLVELRKTIWPLREVLSSLYR</span></span>
<span class="topo-line"><span class="topo-inside">DVPPLIEKETVPYFRDVYDHTIQIADTVETFRDIVSGLLDVYLSSVSNKTNEVM</span><span class="topo-membrane">KVLTII</span></span>
<span class="topo-line"><span class="topo-membrane">ATIFMPLTFIAGIYGM</span><span class="topo-outside">NF</span><span class="topo-unknown">EYMPELR</span><span class="topo-outside">WKWG</span><span class="topo-membrane">YPVVLAVMGVIAVIMVVYFKK</span><span class="topo-inside">KK</span><span class="topo-unknown">WL</span></span>
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
      <td>11</td>
      <td>-2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>294</td>
      <td>9</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>316</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>318</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>325</td>
      <td>316</td>
      <td>322</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>326</td>
      <td>329</td>
      <td>323</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>350</td>
      <td>327</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>352</td>
      <td>348</td>
      <td>349</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>354</td>
      <td>350</td>
      <td>351</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2bbj">2BBJ</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GSHMEEKRLSA</span><span class="topo-inside">KKGLPPGTLVYTGKYREDFEIEVMNYSIEEFREFKTTDVESVLPFRDSS</span></span>
<span class="topo-line"><span class="topo-inside">TPTWINITGIHRTDVVQRVGEFFGIHPLVLEDILNVHQRPKVEFFENYVFIVLKMFTYDK</span></span>
<span class="topo-line"><span class="topo-inside">NLHELESEQVSLILTKNCVLMFQEKIGDVFDPVRERIRYNRGIIRKKRADYLLYSLIDAL</span></span>
<span class="topo-line"><span class="topo-inside">VDDYFVLLEKIDDEIDVLEEEVLERPEKETVQRTHQLKRNLVELRKTIWPLREVLSSLYR</span></span>
<span class="topo-line"><span class="topo-inside">DVPPLIEKETVPYFRDVYDHTIQIADTVETFRDIVSGLLDVYLSSVSNKTNEVMK</span><span class="topo-membrane">VLTII</span></span>
<span class="topo-line"><span class="topo-membrane">ATIFMPLTFIAGIYGM</span><span class="topo-outside">NF</span><span class="topo-unknown">EYMPELR</span><span class="topo-outside">WKWG</span><span class="topo-membrane">YPVVLAVMGVIAVIMVVYFKK</span><span class="topo-inside">KK</span><span class="topo-unknown">WL</span></span>
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
      <td>11</td>
      <td>-2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>295</td>
      <td>9</td>
      <td>292</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>316</td>
      <td>293</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>318</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>325</td>
      <td>316</td>
      <td>322</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>326</td>
      <td>329</td>
      <td>323</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>350</td>
      <td>327</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>352</td>
      <td>348</td>
      <td>349</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>354</td>
      <td>350</td>
      <td>351</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2bbj">2BBJ</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GSHMEEKRLSA</span><span class="topo-inside">KKGLPPGTLVYTGKYREDFEIEVMNYSIEEFREFKTTDVESVLPFRDSS</span></span>
<span class="topo-line"><span class="topo-inside">TPTWINITGIHRTDVVQRVGEFFGIHPLVLEDILNVHQRPKVEFFENYVFIVLKMFTYDK</span></span>
<span class="topo-line"><span class="topo-inside">NLHELESEQVSLILTKNCVLMFQEKIGDVFDPVRERIRYNRGIIRKKRADYLLYSLIDAL</span></span>
<span class="topo-line"><span class="topo-inside">VDDYFVLLEKIDDEIDVLEEEVLERPEKETVQRTHQLKRNLVELRKTIWPLREVLSSLYR</span></span>
<span class="topo-line"><span class="topo-inside">DVPPLIEKETVPYFRDVYDHTIQIADTVETFRDIVSGLLDVYLSSVSNKTNEVM</span><span class="topo-membrane">KVLTII</span></span>
<span class="topo-line"><span class="topo-membrane">ATIFMPLTFIAGIYGM</span><span class="topo-outside">NF</span><span class="topo-unknown">EYMPELR</span><span class="topo-outside">WKWG</span><span class="topo-membrane">YPVVLAVMGVIAVIMVVYFKK</span><span class="topo-inside">KK</span><span class="topo-unknown">WL</span></span>
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
      <td>11</td>
      <td>-2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>294</td>
      <td>9</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>316</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>318</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>325</td>
      <td>316</td>
      <td>322</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>326</td>
      <td>329</td>
      <td>323</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>350</td>
      <td>327</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>352</td>
      <td>348</td>
      <td>349</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>354</td>
      <td>350</td>
      <td>351</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2bbj">2BBJ</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GSHMEEKRLSA</span><span class="topo-inside">KKGLPPGTLVYTGKYREDFEIEVMNYSIEEFREFKTTDVESVLPFRDSS</span></span>
<span class="topo-line"><span class="topo-inside">TPTWINITGIHRTDVVQRVGEFFGIHPLVLEDILNVHQRPKVEFFENYVFIVLKMFTYDK</span></span>
<span class="topo-line"><span class="topo-inside">NLHELESEQVSLILTKNCVLMFQEKIGDVFDPVRERIRYNRGIIRKKRADYLLYSLIDAL</span></span>
<span class="topo-line"><span class="topo-inside">VDDYFVLLEKIDDEIDVLEEEVLERPEKETVQRTHQLKRNLVELRKTIWPLREVLSSLYR</span></span>
<span class="topo-line"><span class="topo-inside">DVPPLIEKETVPYFRDVYDHTIQIADTVETFRDIVSGLLDVYLSSVSNKTNEVM</span><span class="topo-membrane">KVLTII</span></span>
<span class="topo-line"><span class="topo-membrane">ATIFMPLTFIAGIYGM</span><span class="topo-outside">NF</span><span class="topo-unknown">EYMPELR</span><span class="topo-outside">WKWG</span><span class="topo-membrane">YPVVLAVMGVIAVIMVVYFKK</span><span class="topo-inside">KK</span><span class="topo-unknown">WL</span></span>
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
      <td>11</td>
      <td>-2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>294</td>
      <td>9</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>316</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>318</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>325</td>
      <td>316</td>
      <td>322</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>326</td>
      <td>329</td>
      <td>323</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>350</td>
      <td>327</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>352</td>
      <td>348</td>
      <td>349</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>354</td>
      <td>350</td>
      <td>351</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2bbj">2BBJ</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GSHMEEKRLSA</span><span class="topo-inside">KKGLPPGTLVYTGKYREDFEIEVMNYSIEEFREFKTTDVESVLPFRDSS</span></span>
<span class="topo-line"><span class="topo-inside">TPTWINITGIHRTDVVQRVGEFFGIHPLVLEDILNVHQRPKVEFFENYVFIVLKMFTYDK</span></span>
<span class="topo-line"><span class="topo-inside">NLHELESEQVSLILTKNCVLMFQEKIGDVFDPVRERIRYNRGIIRKKRADYLLYSLIDAL</span></span>
<span class="topo-line"><span class="topo-inside">VDDYFVLLEKIDDEIDVLEEEVLERPEKETVQRTHQLKRNLVELRKTIWPLREVLSSLYR</span></span>
<span class="topo-line"><span class="topo-inside">DVPPLIEKETVPYFRDVYDHTIQIADTVETFRDIVSGLLDVYLSSVSNKTNEVMK</span><span class="topo-membrane">VLTII</span></span>
<span class="topo-line"><span class="topo-membrane">ATIFMPLTFIAGIYGM</span><span class="topo-outside">NF</span><span class="topo-unknown">EYMPELR</span><span class="topo-outside">WKWG</span><span class="topo-membrane">YPVVLAVMGVIAVIMVVYFKK</span><span class="topo-inside">KK</span><span class="topo-unknown">WL</span></span>
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
      <td>11</td>
      <td>-2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>295</td>
      <td>9</td>
      <td>292</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>316</td>
      <td>293</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>318</td>
      <td>314</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>325</td>
      <td>316</td>
      <td>322</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>326</td>
      <td>329</td>
      <td>323</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>350</td>
      <td>327</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>352</td>
      <td>348</td>
      <td>349</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>354</td>
      <td>350</td>
      <td>351</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1126##science.1127121

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2iub">2IUB</a></td>
      <td>2.9</td>
      <td>Not specified</td>
      <td>Full-length T. maritima CorA</td>
      <td>Mg2+, Co2+ (soak), Cl-</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length Thermotoga maritima CorA

**Purification:**

- **Expression system**: Escherichia coli
- **Expression construct**: Full-length T. maritima CorA

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
      <td>E. coli expression</td>
      <td>—</td>
      <td></td>
      <td>Expression and purification of full-length TmCorA</td>
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
      <td>Full-length T. maritima CorA</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>100 mM MgCl2 present during crystallization. Crystals diffracted to 2.9 A resolution.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2iub">2IUB</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSDKIHHHHHHMEEK</span><span class="topo-outside">RLSAKKGLPPGTLVYTGKYREDFEIEVMNYSIEEFREFKTTDVE</span></span>
<span class="topo-line"><span class="topo-outside">SVLPFRDSSTPTWINITGIHRTDVVQRVGEFFGIHPLVLEDILNVHQRPKVEFFENYVFI</span></span>
<span class="topo-line"><span class="topo-outside">VLKMFTYDKNLHELESEQVSLILTKNCVLMFQEKIGDVFDPVRERIRYNRGIIRKKRADY</span></span>
<span class="topo-line"><span class="topo-outside">LLYSLIDALVDDYFVLLEKIDDEIDVLEEEVLERPEKETVQRTHQLKRNLVELRKTIWPL</span></span>
<span class="topo-line"><span class="topo-outside">REVLSSLYRDVPPLIEKETVPYFRDVYDHTIQIADTVETFRDIVSGLLDVYLSSVSNKTN</span></span>
<span class="topo-line"><span class="topo-outside">EVMKV</span><span class="topo-membrane">LTIIATIFMPLTFIAGI</span><span class="topo-inside">YG</span><span class="topo-unknown">MNFEYMPELRWKWG</span><span class="topo-inside">YPVV</span><span class="topo-membrane">LAVMGVIAVIMVVYFK</span><span class="topo-outside">KK</span></span>
<span class="topo-line"><span class="topo-outside">K</span><span class="topo-unknown">WL</span></span>
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
      <td>16</td>
      <td>-11</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>305</td>
      <td>5</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>294</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>324</td>
      <td>311</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>338</td>
      <td>313</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>339</td>
      <td>342</td>
      <td>327</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>358</td>
      <td>331</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>361</td>
      <td>347</td>
      <td>349</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>362</td>
      <td>363</td>
      <td>350</td>
      <td>351</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2iub">2IUB</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSDKIHHHHHHMEEK</span><span class="topo-outside">RLSAKKGLPPGTLVYTGKYREDFEIEVMNYSIEEFREFKTTDVE</span></span>
<span class="topo-line"><span class="topo-outside">SVLPFRDSSTPTWINITGIHRTDVVQRVGEFFGIHPLVLEDILNVHQRPKVEFFENYVFI</span></span>
<span class="topo-line"><span class="topo-outside">VLKMFTYDKNLHELESEQVSLILTKNCVLMFQEKIGDVFDPVRERIRYNRGIIRKKRADY</span></span>
<span class="topo-line"><span class="topo-outside">LLYSLIDALVDDYFVLLEKIDDEIDVLEEEVLERPEKETVQRTHQLKRNLVELRKTIWPL</span></span>
<span class="topo-line"><span class="topo-outside">REVLSSLYRDVPPLIEKETVPYFRDVYDHTIQIADTVETFRDIVSGLLDVYLSSVSNKTN</span></span>
<span class="topo-line"><span class="topo-outside">EVMKV</span><span class="topo-membrane">LTIIATIFMPLTFIAGI</span><span class="topo-inside">YG</span><span class="topo-unknown">MNFEYMPELRWKWG</span><span class="topo-inside">YPVV</span><span class="topo-membrane">LAVMGVIAVIMVVYFK</span><span class="topo-outside">KK</span></span>
<span class="topo-line"><span class="topo-outside">K</span><span class="topo-unknown">WL</span></span>
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
      <td>16</td>
      <td>-11</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>305</td>
      <td>5</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>294</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>324</td>
      <td>311</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>338</td>
      <td>313</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>339</td>
      <td>342</td>
      <td>327</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>358</td>
      <td>331</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>361</td>
      <td>347</td>
      <td>349</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>362</td>
      <td>363</td>
      <td>350</td>
      <td>351</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2iub">2IUB</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSDKIHHHHHHMEEKR</span><span class="topo-outside">LSAKKGLPPGTLVYTGKYREDFEIEVMNYSIEEFREFKTTDVE</span></span>
<span class="topo-line"><span class="topo-outside">SVLPFRDSSTPTWINITGIHRTDVVQRVGEFFGIHPLVLEDILNVHQRPKVEFFENYVFI</span></span>
<span class="topo-line"><span class="topo-outside">VLKMFTYDKNLHELESEQVSLILTKNCVLMFQEKIGDVFDPVRERIRYNRGIIRKKRADY</span></span>
<span class="topo-line"><span class="topo-outside">LLYSLIDALVDDYFVLLEKIDDEIDVLEEEVLERPEKETVQRTHQLKRNLVELRKTIWPL</span></span>
<span class="topo-line"><span class="topo-outside">REVLSSLYRDVPPLIEKETVPYFRDVYDHTIQIADTVETFRDIVSGLLDVYLSSVSNKTN</span></span>
<span class="topo-line"><span class="topo-outside">EVMKV</span><span class="topo-membrane">LTIIATIFMPLTFIAGI</span><span class="topo-inside">YG</span><span class="topo-unknown">MNFEYMPELRWKW</span><span class="topo-inside">GYPVV</span><span class="topo-membrane">LAVMGVIAVIMVVYFK</span><span class="topo-outside">KK</span></span>
<span class="topo-line"><span class="topo-outside">K</span><span class="topo-unknown">WL</span></span>
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
      <td>-11</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>305</td>
      <td>6</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>294</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>324</td>
      <td>311</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>337</td>
      <td>313</td>
      <td>325</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>338</td>
      <td>342</td>
      <td>326</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>358</td>
      <td>331</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>361</td>
      <td>347</td>
      <td>349</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>362</td>
      <td>363</td>
      <td>350</td>
      <td>351</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2iub">2IUB</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSDKIHHHHHHMEEK</span><span class="topo-outside">RLSAKKGLPPGTLVYTGKYREDFEIEVMNYSIEEFREFKTTDVE</span></span>
<span class="topo-line"><span class="topo-outside">SVLPFRDSSTPTWINITGIHRTDVVQRVGEFFGIHPLVLEDILNVHQRPKVEFFENYVFI</span></span>
<span class="topo-line"><span class="topo-outside">VLKMFTYDKNLHELESEQVSLILTKNCVLMFQEKIGDVFDPVRERIRYNRGIIRKKRADY</span></span>
<span class="topo-line"><span class="topo-outside">LLYSLIDALVDDYFVLLEKIDDEIDVLEEEVLERPEKETVQRTHQLKRNLVELRKTIWPL</span></span>
<span class="topo-line"><span class="topo-outside">REVLSSLYRDVPPLIEKETVPYFRDVYDHTIQIADTVETFRDIVSGLLDVYLSSVSNKTN</span></span>
<span class="topo-line"><span class="topo-outside">EVMKV</span><span class="topo-membrane">LTIIATIFMPLTFIAGI</span><span class="topo-inside">YG</span><span class="topo-unknown">MNFEYMPELRWKWG</span><span class="topo-inside">YPVVL</span><span class="topo-membrane">AVMGVIAVIMVVYFK</span><span class="topo-outside">KK</span></span>
<span class="topo-line"><span class="topo-outside">K</span><span class="topo-unknown">WL</span></span>
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
      <td>16</td>
      <td>-11</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>305</td>
      <td>5</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>294</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>324</td>
      <td>311</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>338</td>
      <td>313</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>339</td>
      <td>343</td>
      <td>327</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>358</td>
      <td>332</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>359</td>
      <td>361</td>
      <td>347</td>
      <td>349</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>362</td>
      <td>363</td>
      <td>350</td>
      <td>351</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2iub">2IUB</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSDKIHHHHHHMEEK</span><span class="topo-outside">RLSAKKGLPPGTLVYTGKYREDFEIEVMNYSIEEFREFKTTDVE</span></span>
<span class="topo-line"><span class="topo-outside">SVLPFRDSSTPTWINITGIHRTDVVQRVGEFFGIHPLVLEDILNVHQRPKVEFFENYVFI</span></span>
<span class="topo-line"><span class="topo-outside">VLKMFTYDKNLHELESEQVSLILTKNCVLMFQEKIGDVFDPVRERIRYNRGIIRKKRADY</span></span>
<span class="topo-line"><span class="topo-outside">LLYSLIDALVDDYFVLLEKIDDEIDVLEEEVLERPEKETVQRTHQLKRNLVELRKTIWPL</span></span>
<span class="topo-line"><span class="topo-outside">REVLSSLYRDVPPLIEKETVPYFRDVYDHTIQIADTVETFRDIVSGLLDVYLSSVSNKTN</span></span>
<span class="topo-line"><span class="topo-outside">EVMKV</span><span class="topo-membrane">LTIIATIFMPLTFIAGI</span><span class="topo-inside">YG</span><span class="topo-unknown">MNFEYMPELRWKWG</span><span class="topo-inside">YPVVL</span><span class="topo-membrane">AVMGVIAVIMVVYFKK</span><span class="topo-outside">K</span></span>
<span class="topo-line"><span class="topo-outside">K</span><span class="topo-unknown">WL</span></span>
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
      <td>16</td>
      <td>-11</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>305</td>
      <td>5</td>
      <td>293</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>322</td>
      <td>294</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>324</td>
      <td>311</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>338</td>
      <td>313</td>
      <td>326</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>339</td>
      <td>343</td>
      <td>327</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>359</td>
      <td>332</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>361</td>
      <td>348</td>
      <td>349</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>362</td>
      <td>363</td>
      <td>350</td>
      <td>351</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##sj.emboj.7601269

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2bbh">2BBH</a></td>
      <td>1.85</td>
      <td>P41212</td>
      <td>TmCorA_SGC-266</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length Thermotoga maritima CorA


## Biological / Functional Insights

### Funnel-shaped homopentameric architecture

The CorA transporter is a homopentamer with five-fold symmetry about a central pore. The pore is narrowest at three rings formed by Met291, Leu294, and Met302. At the cytosolic side, the pore diameter rapidly increases around Asp277, leading to a funnel-shaped cavity formed by the N-terminal domain. The conserved GMN sequence (residues 312-314) occurs just after the first TM segment on the periplasmic side.

### Two regulatory metal-binding sites (M1 and M2)

Two metal-binding sites were identified at 2.9 A resolution using anomalous scattering from Co2+ soaks. M1 is directly coordinated by Asp89 and Asp253 (distances ~2.2 A), with a second coordination sphere of hydrogen-bonding residues (Asn92, Gln95, Glu100, Asp256, His257). M2 is located ~7 A from M1, surrounded by Leu12, Glu88, Asp175, and Asp253, likely binding a hydrated metal ion with water-mediated coordination. These metal-binding sites are conserved in class II CorAs and likely regulate transport activity.

### Aspartate ring at the pore entrance

A ring formed by five symmetry-related Asp277 residues at the entrance of the pore shows significant residual density (~4.5 sigma in Fo-Fc maps), attributed to bound Mg2+ ions. This aspartate ring is highly conserved among class II CorAs and may determine selectivity or form a binding site for inhibitory cations, analogous to the aspartate ring in the TolC transport system.

### Unique pore architecture

The CorA pore differs from other cation channels, with extensive hydrophobic interactions in the interior and few polar groups (Ser284, Thr287, Thr305). The pore has several narrow regions lacking appropriate polar groups for cation interactions along more than two-thirds of its ~60 A length, suggesting that gating and transport mechanisms may differ from previously studied cation-transport systems.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kvap/">KvAP Voltage-Dependent Potassium Channel</a> — Both are prokaryotic membrane protein structures solved at similar resolutions
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/slc-transporters/thermotoga-maritima-cora/">CorA Magnesium Transporter from Thermotoga maritima</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/proteins/abc-transporters/ec-cor-a/">Escherichia coli CorA Mg2+ Channel (Cytoplasmic Domain)</a> — Homologous CorA protein from E. coli
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Buffer component in purification
- <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> — Reducing agent in purification buffer
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> — Salt component in purification buffer
