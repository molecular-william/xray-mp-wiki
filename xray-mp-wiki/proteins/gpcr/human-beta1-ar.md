---
title: "Human Beta-1 Adrenergic Receptor (beta1 AR)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41422-020-00424-2]
verified: agent
uniprot_id: P08588
---

# Human Beta-1 Adrenergic Receptor (beta1 AR)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P08588">UniProt: P08588</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The beta-1 adrenergic receptor (beta1 AR) is a G protein-coupled receptor (GPCR) that mediates physiologic responses to the catecholamines [Epinephrine](/xray-mp-wiki/reagents/ligands/epinephrine/) and [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/) released by the sympathetic nervous system. It is highly expressed in the heart, where it plays a key role in regulating cardiac function. While beta1 AR and beta2 AR share identical catecholamine-binding pockets, beta1 AR has approximately tenfold higher affinity for [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/), contributing to distinct physiologic roles. This receptor activates Gs leading to adenyl cyclase activation and increased cAMP. Crystal structures of human beta1 AR in inactive (carazolol-bound) and active (BI-167107-, epinephrine-, and norepinephrine-bound) conformations were determined, revealing that the extracellular vestibule shape and electrostatic properties determine ligand association rates and selectivity.


## Publications

### doi/10.1038##s41422-020-00424-2

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7bvq">7BVQ</a></td>
      <td>2.5</td>
      <td>Not specified in paper</td>
      <td>T4L-beta1AR (T4 lysozyme fused to S54 with two alanine linkers, truncated at position 399, ICL3 removed, FLAG-tagged)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/carazolol/">Carazolol</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7bu7">7BU7</a></td>
      <td>2.8</td>
      <td>Not specified in paper</td>
      <td>T4L-beta1AR + Nb6B9 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7bu6">7BU6</a></td>
      <td>3.1</td>
      <td>Not specified in paper</td>
      <td>T4L-beta1AR + Nb6B9 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/norepinephrine/">Norepinephrine</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7bts">7BTS</a></td>
      <td>2.8</td>
      <td>Not specified in paper</td>
      <td>T4L-beta1AR + Nb6B9 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/epinephrine/">Epinephrine</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: T4L-beta1AR with FLAG epitope at N-terminus, truncated at position 399, ICL3 (C261-L314) removed
- **Notes**: Expressed with recombinant baculovirus (Bac-to-Bac system) for 48 h at 27 C

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
      <td>Solubilization</td>
      <td>Membrane solubilization</td>
      <td></td>
      <td>20 mM HEPES pH 7.5, 100 mM NaCl, 1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>For inactive-state beta1 AR (carazolol-bound)</td>
    </tr>
    <tr>
      <td>M1 Flag <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>M1 <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> affinity resin (Sigma)</td>
      <td>20 mM HEPES pH 7.5, 100 mM NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.0002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.0002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Purified with 10 uM <a href="/xray-mp-wiki/reagents/ligands/carazolol/">Carazolol</a> for inactive state</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) column</td>
      <td>20 mM HEPES pH 7.5, 100 mM NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.0002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.0002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Final buffer with 10 uM <a href="/xray-mp-wiki/reagents/ligands/carazolol/">Carazolol</a> for inactive state</td>
    </tr>
  </tbody>
</table>

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
      <td>Solubilization and M1 Flag affinity</td>
      <td>Same as inactive but with agonists</td>
      <td>M1 <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> affinity resin</td>
      <td>20 mM HEPES pH 7.5, 100 mM NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.0002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.0002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Purified with target agonists (100 nM <a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a>, 1 mM <a href="/xray-mp-wiki/reagents/ligands/epinephrine/">Epinephrine</a>, or 1 mM <a href="/xray-mp-wiki/reagents/ligands/norepinephrine/">Norepinephrine</a>)</td>
    </tr>
    <tr>
      <td>Nb6B9 incubation</td>
      <td>Complex formation</td>
      <td></td>
      <td>Same as above + 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.0002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Mixed with 1.2-fold molar excess of Nb6B9 overnight at 4 C</td>
    </tr>
    <tr>
      <td>Nickel <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (pull-down)</td>
      <td>Nickel affinity resin</td>
      <td>Same as above + 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.0002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Pull-down of functional receptor-Nb6B9 complex via His-tagged Nb6B9</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) column</td>
      <td>20 mM HEPES pH 7.5, 100 mM NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.0002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.0002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Excess Nb6B9 removed; agonists maintained in buffer</td>
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
      <td>T4L-beta1AR-<a href="/xray-mp-wiki/reagents/ligands/carazolol/">Carazolol</a> complex reconstituted in <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> with 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Inactive state crystals; protein:lipid ratio 2:3</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Citrate: 100 mM [buffer]  
- Lithium Sulfate: 150-175 mM [additive]  
- Peg: 38-42 % [precipitant] (PEG300)</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>T4L-beta1AR-Nb6B9-agonist complexes reconstituted in <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> with 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Active state crystals (<a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a>, <a href="/xray-mp-wiki/reagents/ligands/norepinephrine/">Norepinephrine</a>, and <a href="/xray-mp-wiki/reagents/ligands/epinephrine/">Epinephrine</a> complexes); protein:lipid ratio 2:3</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>7.5</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Hepes: 100 mM [buffer]  
- Ammonium Sulfate: 100-175 mM [salt]  
- Peg 400: 38-43 % [precipitant] (PEG400)  
- Glycine: 0.15-0.2 M [buffer]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7bvq">7BVQ</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">DYKDDDDANIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYAASQQWT</span><span class="topo-membrane">AGMGLLMALIVLLIVAGNVLVI</span><span class="topo-outside">VAIAKTPRLQTLTNLFI</span><span class="topo-membrane">MSLASADLVMGLLVVPFGATIVV</span><span class="topo-inside">WGR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">W</span><span class="topo-membrane">EYGSFFCELWTSVDVLCVTASIETLCV</span><span class="topo-outside">IALDRYLAITSPFRYQSLLTRARARGLV</span><span class="topo-membrane">CTVWAISALVSFLPILMHWWR</span><span class="topo-inside">AES</span><span class="topo-unknown">DEARRCY</span><span class="topo-inside">NDPKCC</span><span class="topo-membrane">DFVTNRAYAIASSVVSFYVPLCIMAFV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460  </span>
<span class="topo-line"><span class="topo-membrane">YL</span><span class="topo-outside">RVFREAQKQVKKIDSVALREQKALKTL</span><span class="topo-membrane">GIIMGVFTLCWLPFFLANVVKAF</span><span class="topo-inside">HRELVPDR</span><span class="topo-membrane">LFVFFNWLGYANSAFNPIIYC</span><span class="topo-outside">RS</span><span class="topo-unknown">PDFRKAFQGLL</span><span class="topo-outside">C</span><span class="topo-unknown">CARRAAR</span></span>
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
      <td>175</td>
      <td>884</td>
      <td>1058</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>197</td>
      <td>1059</td>
      <td>1080</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>214</td>
      <td>1081</td>
      <td>1097</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>237</td>
      <td>1098</td>
      <td>1120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>241</td>
      <td>1121</td>
      <td>1124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>268</td>
      <td>1125</td>
      <td>1151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>296</td>
      <td>1152</td>
      <td>1179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>317</td>
      <td>1180</td>
      <td>1200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>320</td>
      <td>1201</td>
      <td>1203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>327</td>
      <td>1204</td>
      <td>1210</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>328</td>
      <td>333</td>
      <td>1211</td>
      <td>1216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>362</td>
      <td>1217</td>
      <td>1245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>363</td>
      <td>389</td>
      <td>1246</td>
      <td>1326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>412</td>
      <td>1327</td>
      <td>1349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>420</td>
      <td>1350</td>
      <td>1357</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>421</td>
      <td>441</td>
      <td>1358</td>
      <td>1378</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>442</td>
      <td>443</td>
      <td>1379</td>
      <td>1380</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>454</td>
      <td>1381</td>
      <td>1391</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>455</td>
      <td>455</td>
      <td>1392</td>
      <td>1392</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7bu7">7BU7</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">DYKDDDDANIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">FTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYAASQQWTA</span><span class="topo-membrane">GMGLLMALIVLLIVAGNVLVI</span><span class="topo-outside">VAIAKTPRLQTLTNLFIM</span><span class="topo-membrane">SLASADLVMGLLVVPFGATIVV</span><span class="topo-inside">WGR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">WEY</span><span class="topo-membrane">GSFFCELWTSVDVLCVTASIETLCV</span><span class="topo-outside">IALDRYLAITSPFRYQSLLTRARARGLV</span><span class="topo-membrane">CTVWAISALVSFLPILMHWWRA</span><span class="topo-inside">ES</span><span class="topo-unknown">DEARRCYN</span><span class="topo-inside">DPKCC</span><span class="topo-membrane">DFVTNRAYAIASSVVSFYVPLCIMAF</span><span class="topo-outside">V</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">YLRVFREAQKQVK</span><span class="topo-unknown">KIDSCERRFLGGPARPPSPSPSPVPAPAPPPGPPRPAAAAATAPLANGRAGKRRPSRLVALR</span><span class="topo-outside">EQKALKTL</span><span class="topo-membrane">GIIMGVFTLCWLPFFLANVVKAFHR</span><span class="topo-inside">EL</span><span class="topo-membrane">VPDRLFVFFN</span></span>
<span class="topo-ruler">       490       500       510      </span>
<span class="topo-line"><span class="topo-membrane">WLGYANSAFNPIIY</span><span class="topo-outside">CRS</span><span class="topo-unknown">PDFRKAFQGL</span><span class="topo-outside">LC</span><span class="topo-unknown">CARRAAR</span></span>
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
      <td>176</td>
      <td>884</td>
      <td>1059</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>197</td>
      <td>1060</td>
      <td>1080</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>215</td>
      <td>1081</td>
      <td>1098</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>237</td>
      <td>1099</td>
      <td>1120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>243</td>
      <td>1121</td>
      <td>1126</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>268</td>
      <td>1127</td>
      <td>1151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>296</td>
      <td>1152</td>
      <td>1179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>318</td>
      <td>1180</td>
      <td>1201</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>320</td>
      <td>1202</td>
      <td>1203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>328</td>
      <td>1204</td>
      <td>1211</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>329</td>
      <td>333</td>
      <td>1212</td>
      <td>1216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>359</td>
      <td>1217</td>
      <td>1242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>373</td>
      <td>1243</td>
      <td>1256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>436</td>
      <td>443</td>
      <td>1319</td>
      <td>1326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>468</td>
      <td>1327</td>
      <td>1351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>469</td>
      <td>470</td>
      <td>1352</td>
      <td>1353</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>494</td>
      <td>1354</td>
      <td>1377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>495</td>
      <td>497</td>
      <td>1378</td>
      <td>1380</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>498</td>
      <td>507</td>
      <td>1381</td>
      <td>1390</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>508</td>
      <td>509</td>
      <td>1391</td>
      <td>1392</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7bu6">7BU6</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">DYKDDDDANIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYAASQQWT</span><span class="topo-membrane">AGMGLLMALIVLLIVAGNVLVIV</span><span class="topo-inside">AIAKTPRLQTLTNLF</span><span class="topo-membrane">IMSLASADLVMGLLVVPFGATIVV</span><span class="topo-outside">WGR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">WEYGSF</span><span class="topo-membrane">FCELWTSVDVLCVTASIETLCV</span><span class="topo-inside">IALDRYLAITSPFRYQSLLTRARARG</span><span class="topo-membrane">LVCTVWAISALVSFLPILMHWWR</span><span class="topo-outside">AES</span><span class="topo-unknown">DEARRCYN</span><span class="topo-outside">DPKCC</span><span class="topo-membrane">DFVTNRAYAIASSVVSFYVPLCIMAF</span><span class="topo-inside">V</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">YLRVFREAQKQV</span><span class="topo-unknown">KKIDSCERRFLGGPARPPSPSPSPVPAPAPPPGPPRPAAAAATAPLANGRAGKRRPSRLV</span><span class="topo-inside">ALREQKALKTLG</span><span class="topo-membrane">IIMGVFTLCWLPFFLANVVKAFH</span><span class="topo-outside">REL</span><span class="topo-membrane">VPDRLFVFFN</span></span>
<span class="topo-ruler">       490       500       510      </span>
<span class="topo-line"><span class="topo-membrane">WLGYANSAFNPIIY</span><span class="topo-inside">CRS</span><span class="topo-unknown">PDFRKAFQGLL</span><span class="topo-inside">C</span><span class="topo-unknown">CARRAAR</span></span>
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
      <td>175</td>
      <td>884</td>
      <td>1058</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>198</td>
      <td>1059</td>
      <td>1081</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>213</td>
      <td>1082</td>
      <td>1096</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>237</td>
      <td>1097</td>
      <td>1120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>246</td>
      <td>1121</td>
      <td>1129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>268</td>
      <td>1130</td>
      <td>1151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>294</td>
      <td>1152</td>
      <td>1177</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>317</td>
      <td>1178</td>
      <td>1200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>320</td>
      <td>1201</td>
      <td>1203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>328</td>
      <td>1204</td>
      <td>1211</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>329</td>
      <td>333</td>
      <td>1212</td>
      <td>1216</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>359</td>
      <td>1217</td>
      <td>1242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>372</td>
      <td>1243</td>
      <td>1255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>433</td>
      <td>444</td>
      <td>1316</td>
      <td>1327</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>467</td>
      <td>1328</td>
      <td>1350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>468</td>
      <td>470</td>
      <td>1351</td>
      <td>1353</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>471</td>
      <td>494</td>
      <td>1354</td>
      <td>1377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>495</td>
      <td>497</td>
      <td>1378</td>
      <td>1380</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>498</td>
      <td>508</td>
      <td>1381</td>
      <td>1391</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>509</td>
      <td>509</td>
      <td>1392</td>
      <td>1392</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7bts">7BTS</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">DYKDDDDANIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYAASQQW</span><span class="topo-membrane">TAGMGLLMALIVLLIVAGNVLVIV</span><span class="topo-inside">AIAKTPRLQTLTNLF</span><span class="topo-membrane">IMSLASADLVMGLLVVPFGATIVV</span><span class="topo-outside">WGR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">WEYGSF</span><span class="topo-membrane">FCELWTSVDVLCVTASIETLCVIA</span><span class="topo-inside">LDRYLAITSPFRYQSLLTRARARG</span><span class="topo-membrane">LVCTVWAISALVSFLPILMHWWR</span><span class="topo-outside">AES</span><span class="topo-unknown">DEARRCYN</span><span class="topo-outside">DPKCC</span><span class="topo-membrane">DFVTNRAYAIASSVVSFYVPLCIMAF</span><span class="topo-inside">V</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460  </span>
<span class="topo-line"><span class="topo-inside">YLRVFREAQKQV</span><span class="topo-unknown">KKIDSV</span><span class="topo-inside">ALREQKALKTLG</span><span class="topo-membrane">IIMGVFTLCWLPFFLANVVKAFH</span><span class="topo-outside">REL</span><span class="topo-membrane">VPDRLFVFFNWLGYANSAFNPIIY</span><span class="topo-inside">CRS</span><span class="topo-unknown">PDFRKAFQGLL</span><span class="topo-inside">C</span><span class="topo-unknown">CARRAAR</span></span>
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
      <td>174</td>
      <td>884</td>
      <td>1057</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>198</td>
      <td>1058</td>
      <td>1081</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>213</td>
      <td>1082</td>
      <td>1096</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>237</td>
      <td>1097</td>
      <td>1120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>246</td>
      <td>1121</td>
      <td>1129</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>270</td>
      <td>1130</td>
      <td>1153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>271</td>
      <td>294</td>
      <td>1154</td>
      <td>1177</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>317</td>
      <td>1178</td>
      <td>1200</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>320</td>
      <td>1201</td>
      <td>1203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>328</td>
      <td>1204</td>
      <td>1211</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>329</td>
      <td>333</td>
      <td>1212</td>
      <td>1216</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>359</td>
      <td>1217</td>
      <td>1242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>372</td>
      <td>1243</td>
      <td>1255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>390</td>
      <td>1316</td>
      <td>1327</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>391</td>
      <td>413</td>
      <td>1328</td>
      <td>1350</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>416</td>
      <td>1351</td>
      <td>1353</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>440</td>
      <td>1354</td>
      <td>1377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>441</td>
      <td>443</td>
      <td>1378</td>
      <td>1380</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>454</td>
      <td>1381</td>
      <td>1391</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>455</td>
      <td>455</td>
      <td>1392</td>
      <td>1392</td>
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

### Norepinephrine selectivity for beta1 AR is determined by the extracellular vestibule

Despite identical orthosteric catecholamine-binding pockets in beta1 AR and beta2 AR, [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/) is tenfold selective for beta1 AR. The selectivity arises from different association rates (on-rates), not dissociation rates. Metadynamics simulations revealed that [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/) takes different pathways to the orthosteric pocket in the two receptors, determined by differences in extracellular vestibule shape, electrostatic properties, and key residues including negatively charged pairs (D217/D356 in beta1 AR vs E180/D300 in beta2 AR) and aromatic gates (F218/F359 in beta1 AR vs F193/Y308 in beta2 AR).

### Active and inactive conformations of human beta1 AR

The inactive (carazolol-bound) and active (BI-167107-, norepinephrine-, and epinephrine-bound) beta1 AR structures display classical GPCR activation features including outward movement of TM5 and TM6 and inward displacement of TM3 and TM7 on the cytoplasmic side. The conserved PIF motif rearrangement (P236, I246, F333) and water-mediated hydrogen bonds characteristic of active-state stabilization were observed.

### Electrostatic differences distinguish norepinephrine and epinephrine binding

Although both catecholamines follow similar binding pathways in their respective receptors, [Epinephrine](/xray-mp-wiki/reagents/ligands/epinephrine/) has an additional methyl group on the primary amine that modifies the electron distribution, making the protonated nitrogen less positively charged than in [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/). This makes [Epinephrine](/xray-mp-wiki/reagents/ligands/epinephrine/) less sensitive to the electrostatic differences between the beta1 AR and beta2 AR extracellular vestibules, explaining why [Epinephrine](/xray-mp-wiki/reagents/ligands/epinephrine/) binds both receptors with equal affinity.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/carazolol/">Carazolol</a> — Inverse agonist used for inactive state structure determination
- <a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a> — High-affinity agonist used for active state structure
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Lauryl Maltose Neopentyl Glycol (LMNG)</a> — Primary detergent for solubilization and purification
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Buffer used in all purification steps
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used for LCP crystallization
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — Stabilizing additive used with LMNG
- <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4 Lysozyme (T4L)</a> — Fusion partner for crystallization construct
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> — Additive used in purification or crystallization buffers
