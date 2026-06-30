---
title: "ScaDMT Divalent Metal-Ion Transporter"
created: 2026-06-05
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2904]
verified: false
---

# ScaDMT Divalent Metal-Ion Transporter

## Overview

ScaDMT is a divalent metal-ion transporter from Staphylococcus capitis belonging to the [SLC11 (NRAMP) Family](/xray-mp-wiki/concepts/protein-families/slc11-nramp-family/). It catalyzes the proton-coupled transport of transition-metal ions including Mn2+, Fe2+, Cd2+, Co2+, Ni2+, and Pb2+ across cellular membranes. The protein adopts an inward-facing conformation with a LeuT-fold architecture and a substrate-binding site at the center of the transporter. ScaDMT is highly homologous to human DMT1 (SLC11A2), sharing 37% identical and 59% homologous residues. It contains 448 amino acids and is monomeric in detergent solution as determined by multiangle light scattering.


## Publications

### doi/10.1038##nsmb.2904

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5m94">5M94</a></td>
      <td>3.6 A</td>
      <td>P3_1 2 1</td>
      <td>Selenomethionine-labeled ScaDMT^tru-<a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> complex</td>
      <td>SeMet (for structural determination by X-ray crystallography)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: ScaDMT from S. capitis DSM 20326 (448 aa), C-terminal His10 tag separated by [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/) cleavage site, cloned into pBXC3H vector

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
      <td>Cell lysis and membrane preparation</td>
      <td>Cell disruption with custom-made cell disruptor; ultracentrifugation to harvest membranes</td>
      <td>--</td>
      <td>50 mM potassium phosphate pH 7.5, 150 mM NaCl + DM (1-2% w/v)</td>
      <td>Membrane vesicles extracted with 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> and 1-2% DM</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (IMAC)</td>
      <td>Ni-NTA</td>
      <td>DM-containing buffer + DM</td>
      <td>His10-tagged protein purified; <a href="/xray-mp-wiki/reagents/additives/hrv-3c-protease/">HRV 3C Protease</a> cleavage during dialysis</td>
    </tr>
    <tr>
      <td>Tag cleavage and SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/hrv-3c-protease/">HRV 3C Protease</a> cleavage followed by size-exclusion chromatography</td>
      <td>Superdex S200</td>
      <td>10 mM HEPES pH 7.5, 150 mM NaCl, 0.25% DM + DM</td>
      <td>Cleaved protein concentrated and pooled for experiments</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> co-crystallization, vapor diffusion</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Full-length ScaDMT crystals grew to 6.5 A resolution in P3_2 2 1. ScaDMT^tru co-crystallized with <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> in <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a>/650 precipitants yielding 3.1 A structures in P3_1 2 1. Mn2+ complexes obtained by soaking. SeMet-labeled crystals used for structural determination.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5m94">5M94</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAVA</span><span class="topo-outside">VGYMDPGNWITSMQGGAQYGYTLLF</span><span class="topo-membrane">VILISSLAAMLLQSMTV</span><span class="topo-inside">RLGIATGKDLAQMTRHFLSKPVAI</span><span class="topo-membrane">IFWIIAELAIIATDIAE</span><span class="topo-outside">VIGSAIALDLIFGIPLIVGALITVFDVFLLLFI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">MRFGFRKIEAIVGTLIFTVLAIFVFEVFISSPQLTDILNGFVPHKEIVTNQGILYIA</span><span class="topo-membrane">LGIIGATIMPHNLYLHSSIV</span><span class="topo-inside">QSRKYDRHDNEEKAQAI</span><span class="topo-membrane">KYATIDSNLQLSIAFV</span><span class="topo-outside">VNCLLLTLGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ALFFGTKTNDLGGFYDLYHALKTEPVLGATLGGVMSTLFAVALLASGQ</span><span class="topo-membrane">NSTITGTLAGQIVME</span><span class="topo-inside">GFLRL</span><span class="topo-membrane">SIPNWLRRLITRSLAVIP</span><span class="topo-outside">VIICLIIFKGNSEKIEQLLVF</span><span class="topo-membrane">SQVFLSIALPFSL</span></span>
<span class="topo-ruler">       370       380       390       400       410     </span>
<span class="topo-line"><span class="topo-membrane">IPLQ</span><span class="topo-inside">LATSNKKLMGPFINKTW</span><span class="topo-membrane">VNIISWTLIVILSGLNVYLIIQTF</span><span class="topo-unknown">QELALEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>41</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>45</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>70</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>70</td>
      <td>87</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>87</td>
      <td>111</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>177</td>
      <td>128</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>197</td>
      <td>218</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>214</td>
      <td>238</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>230</td>
      <td>255</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>288</td>
      <td>271</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>303</td>
      <td>329</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>308</td>
      <td>344</td>
      <td>348</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>309</td>
      <td>326</td>
      <td>349</td>
      <td>366</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>347</td>
      <td>367</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>364</td>
      <td>388</td>
      <td>404</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>381</td>
      <td>405</td>
      <td>421</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>405</td>
      <td>422</td>
      <td>445</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>406</td>
      <td>415</td>
      <td>446</td>
      <td>455</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5m94">5M94</a> — Chain C (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAVA</span><span class="topo-outside">VGYMDPGNWITSMQGGAQYGYTLLF</span><span class="topo-membrane">VILISSLAAMLLQSMTV</span><span class="topo-inside">RLGIATGKDLAQMTRHFLSKPVAI</span><span class="topo-membrane">IFWIIAELAIIATDIAE</span><span class="topo-outside">VIGSAIALDLIFGIPLIVGALITVFDVFLLLFI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">MRFGFRKIEAIVGTLIFTVLAIFVFEVFISSPQLTDILNGFVPHKEIVTNQGILYIA</span><span class="topo-membrane">LGIIGATIMPHNLYLHSSIV</span><span class="topo-inside">QSRKYDRHDNEEKAQAI</span><span class="topo-membrane">KYATIDSNLQLSIAFV</span><span class="topo-outside">VNCLLLTLGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ALFFGTKTNDLGGFYDLYHALKTEPVLGATLGGVMSTLFAVALLASG</span><span class="topo-membrane">QNSTITGTLAGQIVME</span><span class="topo-inside">GFLRLS</span><span class="topo-membrane">IPNWLRRLITRSLAVIP</span><span class="topo-outside">VIICLIIFKGNSEKIEQLLVF</span><span class="topo-membrane">SQVFLSIALPFSL</span></span>
<span class="topo-ruler">       370       380       390       400       410     </span>
<span class="topo-line"><span class="topo-membrane">IPLQ</span><span class="topo-inside">LATSNKKLMGPFINKTW</span><span class="topo-membrane">VNIISWTLIVILSGLNVYLIIQTF</span><span class="topo-unknown">QELALEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>41</td>
      <td>44</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>45</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>70</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>70</td>
      <td>87</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>87</td>
      <td>111</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>177</td>
      <td>128</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>197</td>
      <td>218</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>214</td>
      <td>238</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>230</td>
      <td>255</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>287</td>
      <td>271</td>
      <td>327</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>303</td>
      <td>328</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>304</td>
      <td>309</td>
      <td>344</td>
      <td>349</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>326</td>
      <td>350</td>
      <td>366</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>327</td>
      <td>347</td>
      <td>367</td>
      <td>387</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>348</td>
      <td>364</td>
      <td>388</td>
      <td>404</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>365</td>
      <td>381</td>
      <td>405</td>
      <td>421</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>405</td>
      <td>422</td>
      <td>445</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>406</td>
      <td>415</td>
      <td>446</td>
      <td>455</td>
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

### Conserved transition-metal ion binding site

The ion-binding site is located at the center of the transporter and is composed of
conserved residues Asp49 and Asn52 from the unwound region of alpha-helix 1, and
Met226 from alpha-helix 6a. The coordinating atoms form an approximately planar
geometry with predominantly hard oxygen ligands and a soft thioether sulfur ligand
from Met226. This binding mode is conserved across the SLC11 family including human
DMT1, as demonstrated by equivalent mutations (D86A, N89A, M265A) in human DMT1
showing similar loss of ion binding and transport activity.

### Ion selectivity mechanism

ScaDMT selectively transports transition-metal ions (Mn2+, Fe2+, Cd2+, Co2+, Ni2+,
Pb2+) while excluding alkaline earth metal ions (Ca2+, Mg2+, Sr2+, Ba2+). The binding
site chemistry reflects this selectivity: the planar coordination geometry with
oxygen and sulfur ligands favors transition metals over alkaline earth metals. The
conserved DPGN motif in the unwound region of alpha-helix 1 serves as a family
signature. Cu2+ binds at the same site with shifted position, while Zn2+ binds in
the aqueous vestibule interacting with His233.

### Alternating-access transport mechanism

ScaDMT operates via an alternating-access mechanism. Binding of a proton and a
transition-metal ion to the extracellular-accessible site triggers conformational
changes in alpha-helices 1 and 6 around a hinge at the ion-binding region. This
closes the extracellular pathway and opens the intracellular pathway, releasing
both substrates into the cytoplasm. The empty transporter returns to its
outward-facing state.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/slc11-nramp-family/">SLC11 (NRAMP) Family</a> — ScaDMT is a member of the SLC11/NRAMP family of divalent metal-ion transporters
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — ScaDMT transports ions via the alternating-access mechanism
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/inward-facing-conformation/">Inward-Facing Conformation</a> — ScaDMT structures adopt inward-facing conformation
- <a href="/xray-mp-wiki/concepts/miscellaneous/leut-return-state-mechanism/">LeuT Return-State Mechanism</a> — ScaDMT shares the LeuT-fold architecture with amino acid permeases
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside</a> — DM used for solubilization and purification of ScaDMT
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/hrv-3c-protease/">HRV 3C Protease</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> — Fusion tag for crystallization or purification
- <a href="/xray-mp-wiki/proteins/slc-transporters/sca-dmt/">ScaDMT Divalent Metal-Ion Transporter</a> — ScaDMT^tru is a truncated N-terminal variant of full-length ScaDMT
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/dmt-superfamily/">DMT Superfamily (Drug/Metabolite Transporter Superfamily)</a> — ScaDMT^tru is a member of the SLC11 family
- <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/protein-tags/nanobody">Nanobody</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/concepts/truncation">Protein Truncation for Crystallization</a> — Entity mentioned in text
