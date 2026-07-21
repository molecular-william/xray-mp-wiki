---
title: "MurJ (Lipid II Flippase from E. coli and T. africanus)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-09658-0, doi/10.1016##j.str.2022.05.008, doi/10.1073##pnas.1802192115]
verified: agent
uniprot_id: ['A0A979HMS2', 'B7IE18', 'P0AF16']
---

# MurJ (Lipid II Flippase from E. coli and T. africanus)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A979HMS2">UniProt: A0A979HMS2</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/B7IE18">UniProt: B7IE18</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0AF16">UniProt: P0AF16</a>

<span class="expr-badge">Arsenophonus endosymbiont of nilaparvata lugens</span>

## Overview

MurJ is an essential integral membrane protein in Gram-negative bacteria that flips the cell wall building block Lipid II across the cytoplasmic membrane for peptidoglycan biosynthesis. MurJ is a member of the MOP (Multidrug/Oligosaccharidyl-lipid/Polysaccharide) flippase superfamily. Crystal structures have revealed V-shaped inward- and outward-facing forms with a central cavity for substrate binding. A novel "squeezed" form of E. coli MurJ (EcMurJ) was discovered, representing an intermediate conformation after substrate release that lacks an internal cavity. Structures from Arsenophonus endosymbiont MurJ (AeMurJ) show inward closed and occluded conformations. The MurJ from Thermosiphon africanus (MurJ_TA) was captured in multiple conformations — inward-closed, inward-open, inward-occluded, and outward-facing — revealing the complete conformational landscape of the Lipid II flipping cycle, including a sodium binding site and a conserved Arg24-Asp25-Arg255 substrate-binding triad.

## Publications

### doi/10.1038##s41467-019-09658-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5t77">5T77</a></td>
      <td>2.0</td>
      <td>Not specified</td>
      <td>MurJ_TA (Thermosiphon africanus)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6nc6">6NC6</a></td>
      <td>3.2</td>
      <td>Not specified</td>
      <td>MurJ_TA inward-closed</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6nc6">6NC6</a></td>
      <td>3.0</td>
      <td>Not specified</td>
      <td>MurJ_TA inward-open</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6nc6">6NC6</a></td>
      <td>2.6</td>
      <td>Not specified</td>
      <td>MurJ_TA inward-occluded</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6nc6">6NC6</a></td>
      <td>1.8</td>
      <td>Not specified</td>
      <td>MurJ_TA outward-facing</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41(DE3)
- **Construct**: MurJ_TA (T. africanus): His10-MBP-PPX-MurJ_TA-PPX-His10; EcMurJ (E. coli) residues 12-511; AeMurJ (Arsenophonus) full-length with [TEV](/xray-mp-wiki/reagents/additives/tev-protease/)-cleavable C-terminal GFP-His8
- **Notes**: Sources: doi/10.1038##s41467-019-09658-0 (MurJ_TA); doi/10.1016##j.str.2022.05.008 (EcMurJ, AeMurJ)

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
      <td>Microfluidizer disruption</td>
      <td>—</td>
      <td>50 mM HEPES-NaOH pH 8.0, 150 mM Na acetate, 10 mM beta-ME, protease inhibitors</td>
      <td>Chloride-free buffers used throughout</td>
    </tr>
    <tr>
      <td>Membrane protein extraction</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM HEPES-NaOH pH 8.0, 150 mM Na acetate + 30 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (n-dodecyl-beta-D-maltopyranoside)</td>
      <td>60 min at 4 C</td>
    </tr>
    <tr>
      <td>Immobilized metal-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> cobalt affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> Cobalt resin</td>
      <td>50 mM HEPES-NaOH pH 8.0, 150 mM Na acetate, 15 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted with 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>. PreScission protease cleavage overnight at 4 C to remove tags.</td>
    </tr>
    <tr>
      <td>Buffer exchange and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300</td>
      <td>20 mM HEPES-NaOH pH 8.0, 150 mM Na acetate, 2 mM DTT, 0.3 mM decyl maltose neopentyl glycol (<a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a>)</td>
      <td>Exchanged into <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a> by 15-fold dilution prior to <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>20-25 mg/mL MurJ_TA in <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a> buffer mixed with Lipid II-doped <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (2:3 w/w water:lipid ratio)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in 96-well glass sandwich plates. Salt composition of precipitant determined crystal form. Inward-closed: 1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 50 mM Na acetate pH 4.6, 40% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>. Inward-open: 200 mM (NH4)2SO4, 50 mM Tris-HCl pH 8.5 or 100 mM Na citrate pH 5.5, 20-40% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>. Inward-occluded: 100 mM Na citrate pH 5.0, 40% <a href="/xray-mp-wiki/reagents/additives/peg200/">PEG200</a>. Outward: 1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a>-NaOH pH 7.5, 20% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, or MgCl2/NaCl conditions. Crystals grew to full size in 4 weeks.</td>
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
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5t77">5T77</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSI</span><span class="topo-outside">LFSSILFSIA</span><span class="topo-membrane">TFFSRILGLFRDV</span><span class="topo-inside">LFAKYFGVSYELDAYF</span><span class="topo-membrane">IAIMFPFFLRKVFG</span><span class="topo-outside">EGAMSSAFVPLYSEKSGEEKDKFLSSVIN</span><span class="topo-membrane">GFSLIILALVILSY</span><span class="topo-inside">FFP</span><span class="topo-unknown">ELIINLFG</span><span class="topo-inside">AGSSHETKIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AKKLL</span><span class="topo-membrane">LITSPSIYFIFLWA</span><span class="topo-outside">ISYSILNTNNKFFWPAL</span><span class="topo-membrane">TPSISNITIIIG</span><span class="topo-inside">TFLSTKYGIISP</span><span class="topo-membrane">TIGFLIGSILMFFS</span><span class="topo-outside">IIKSIIKHKYYFTIKH</span><span class="topo-unknown">FPHFLKLFFPTF</span><span class="topo-membrane">MTMVVSQINTVVDMN</span><span class="topo-inside">VVS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">FYDKGSISYL</span><span class="topo-membrane">QYASRFYLLPYGLFA</span><span class="topo-outside">VSVSTVVLSKISNDRKNFNYHLNDALKTTLFF</span><span class="topo-membrane">TIPSMVGLIFLS</span><span class="topo-unknown">TPIIRFFY</span><span class="topo-inside">EHGAFTSKDTLITSKI</span><span class="topo-membrane">LIAYTLGLPFYG</span><span class="topo-outside">IYSTISRSYHAIKNT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470     </span>
<span class="topo-line"><span class="topo-outside">KTPFIA</span><span class="topo-membrane">ATIVSLSNIILDII</span><span class="topo-inside">FGLKYGPIG</span><span class="topo-membrane">VALATSIAGIIGVLY</span><span class="topo-outside">LLFSVKTFPIKDFLKI</span><span class="topo-membrane">SLNSLIMLFVIYLTD</span><span class="topo-inside">FTDNEF</span><span class="topo-membrane">WFLIQILIGILVYLIF</span><span class="topo-outside">SSIFYRDLIRRFL</span><span class="topo-unknown">YARKK</span></span>
<details class="topo-details"><summary>Topology coordinates (33 regions)</summary>
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
      <td>4</td>
      <td>13</td>
      <td>4</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>26</td>
      <td>14</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>42</td>
      <td>27</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>56</td>
      <td>43</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>85</td>
      <td>57</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>99</td>
      <td>86</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>102</td>
      <td>100</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>110</td>
      <td>103</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>111</td>
      <td>125</td>
      <td>111</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>139</td>
      <td>126</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>156</td>
      <td>140</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>168</td>
      <td>157</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>180</td>
      <td>169</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>194</td>
      <td>181</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>210</td>
      <td>195</td>
      <td>210</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>222</td>
      <td>211</td>
      <td>222</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>223</td>
      <td>237</td>
      <td>223</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>250</td>
      <td>238</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>265</td>
      <td>251</td>
      <td>265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>297</td>
      <td>266</td>
      <td>297</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>309</td>
      <td>298</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>317</td>
      <td>310</td>
      <td>317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>318</td>
      <td>333</td>
      <td>318</td>
      <td>333</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>345</td>
      <td>334</td>
      <td>345</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>346</td>
      <td>366</td>
      <td>346</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>380</td>
      <td>367</td>
      <td>380</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>381</td>
      <td>389</td>
      <td>381</td>
      <td>389</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>404</td>
      <td>390</td>
      <td>404</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>405</td>
      <td>420</td>
      <td>405</td>
      <td>420</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>421</td>
      <td>435</td>
      <td>421</td>
      <td>435</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>436</td>
      <td>441</td>
      <td>436</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>457</td>
      <td>442</td>
      <td>457</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>458</td>
      <td>470</td>
      <td>458</td>
      <td>470</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1016##j.str.2022.05.008

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wag">7WAG</a></td>
      <td>2.6</td>
      <td>Not specified</td>
      <td>EcMurJ, residues 12-511</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7waw">7WAW</a></td>
      <td>2.8</td>
      <td>Not specified</td>
      <td>AeMurJ, inward closed form (AeMurJ-N)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wax">7WAX</a></td>
      <td>2.4</td>
      <td>Not specified</td>
      <td>AeMurJ, inward occluded form (AeMurJ-L)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41(DE3)
- **Construct**: MurJ_TA (T. africanus): His10-MBP-PPX-MurJ_TA-PPX-His10; EcMurJ (E. coli) residues 12-511; AeMurJ (Arsenophonus) full-length with [TEV](/xray-mp-wiki/reagents/additives/tev-protease/)-cleavable C-terminal GFP-His8
- **Notes**: Sources: doi/10.1038##s41467-019-09658-0 (MurJ_TA); doi/10.1016##j.str.2022.05.008 (EcMurJ, AeMurJ)

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
      <td>Membrane preparation</td>
      <td>Microfluidizer lysis, ultracentrifugation</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-ME</a>, 0.1 mM PMSF</td>
      <td></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-ME</a>, 0.1 mM PMSF + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (n-dodecyl-beta-D-maltopyranoside)</td>
      <td>60 min at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Immobilized metal-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 5% glycerol, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-ME</a></td>
      <td>Eluted with 100-300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient. GFP-His8 tag cleaved by <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease at 4 C for 16 h.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase</a> 10/30 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> pH 8.0, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-ME</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Approximately 20 mg/ml EcMurJ or AeMurJ in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>EcMurJ crystallized in long thin plate-like crystals. AeMurJ produced two crystal forms (AeMurJ-N and AeMurJ-L). Structures determined by Se-Met SAD (AeMurJ) and molecular replacement using EcMurJ (PDB 6CC4) as search model.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wag">7WAG</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">NLLKSLAAGR</span><span class="topo-membrane">CSMTMFSRVLGFARDAIVAR</span><span class="topo-outside">IFGAGMAT</span><span class="topo-membrane">DAFFVAFKLPNLLRRIFAEGAFS</span><span class="topo-inside">QAFVPILAEYKSKQGEDATRVFVSYVS</span><span class="topo-membrane">GLLTLALAVVTVAGMLAAPWVI</span><span class="topo-outside">MVTAPGFADT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ADKFALT</span><span class="topo-membrane">SQLLKITFPYILLISLASLVG</span><span class="topo-inside">AILNTWNRFS</span><span class="topo-membrane">IPAFAPTLLNISMIGFALFAA</span><span class="topo-outside">PYFNPPV</span><span class="topo-membrane">LALAWAVTVGGVLQLVYQLP</span><span class="topo-inside">HLKKIGMLVLPRINFHDAGAMRVV</span><span class="topo-membrane">KQMGPAILGV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SVSQISLIINTIFA</span><span class="topo-outside">SFLASGSV</span><span class="topo-membrane">SWMYYADRLMEFPSGVLGVALG</span><span class="topo-inside">TILLPSLSKSFASGNHDEYNRLMDWGL</span><span class="topo-membrane">RLCFLLALPSAVALGILSGPLTVSLF</span><span class="topo-outside">QYGKFTAFDALMT</span><span class="topo-membrane">QRALIAYSVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LIGLIVVKVLA</span><span class="topo-inside">PGFYSRQDI</span><span class="topo-membrane">KTPVKIAIVTLILTQLMNLAFI</span><span class="topo-outside">GPLKH</span><span class="topo-membrane">AGLSLSIGLAACLNASLLYWQ</span><span class="topo-inside">LRKQKIFTPQPGW</span><span class="topo-membrane">MAFLLRLVVAVLVMSGVLLGMLHIM</span><span class="topo-outside">PEWSLGT</span><span class="topo-membrane">MPWRLLR</span></span>
<span class="topo-ruler">       490       500       510       520  </span>
<span class="topo-line"><span class="topo-membrane">LMAVVLAGIAAYFAALAVLGF</span><span class="topo-inside">KVKEFARRTVLESSGENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>30</td>
      <td>11</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>38</td>
      <td>31</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>61</td>
      <td>39</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>88</td>
      <td>62</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>110</td>
      <td>89</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>127</td>
      <td>111</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>148</td>
      <td>128</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>158</td>
      <td>149</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>179</td>
      <td>159</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>186</td>
      <td>180</td>
      <td>186</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>206</td>
      <td>187</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>230</td>
      <td>207</td>
      <td>230</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>254</td>
      <td>231</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>262</td>
      <td>255</td>
      <td>262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>263</td>
      <td>284</td>
      <td>263</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>285</td>
      <td>311</td>
      <td>285</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>337</td>
      <td>312</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>338</td>
      <td>350</td>
      <td>338</td>
      <td>350</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>351</td>
      <td>371</td>
      <td>351</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>380</td>
      <td>372</td>
      <td>380</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>402</td>
      <td>381</td>
      <td>402</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>403</td>
      <td>407</td>
      <td>403</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>428</td>
      <td>408</td>
      <td>428</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>429</td>
      <td>441</td>
      <td>429</td>
      <td>441</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>442</td>
      <td>466</td>
      <td>442</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>467</td>
      <td>473</td>
      <td>467</td>
      <td>473</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>474</td>
      <td>501</td>
      <td>474</td>
      <td>501</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>502</td>
      <td>522</td>
      <td>502</td>
      <td>522</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7waw">7WAW</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNLLKSLA</span><span class="topo-inside">AISS</span><span class="topo-membrane">MTMFSRILGFIRDAII</span><span class="topo-outside">ARFFGAGAATDAF</span><span class="topo-membrane">FVAFRLPNLLRRIFAE</span><span class="topo-inside">GAFSQAFVPILAEYKNQQGDEATRTFIAYVSGLL</span><span class="topo-membrane">TLILAIVTLAGILAAPWI</span><span class="topo-outside">IYITAPGFTDT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">PDKFDLT</span><span class="topo-membrane">VRLLRITFPYILLISLAS</span><span class="topo-inside">LAGAILNTWNRFSVP</span><span class="topo-membrane">AFAPTLLNISMIISVL</span><span class="topo-outside">LLAPYCEPPIIA</span><span class="topo-membrane">LGWGVFAGGILQLLYQ</span><span class="topo-inside">LPYLQKIGMLVLPRISFRNSGVWRVLKLMGPAII</span><span class="topo-membrane">GV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SVSQISLIINTIFAS</span><span class="topo-outside">FLQSGSV</span><span class="topo-membrane">SWMYYADRLMELPTGVLG</span><span class="topo-inside">VALGTILLPSLAKSFSTGDHKEYQRLMDWGLRLCF</span><span class="topo-membrane">LLALPCAIALAILAEPLT</span><span class="topo-outside">VSLFQYGNFTAYDAVMT</span><span class="topo-membrane">QRALIAYCVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMGLIVV</span><span class="topo-inside">KVLAPGFYSRQDIKTPVKI</span><span class="topo-membrane">AIITLILTQLMNLAFI</span><span class="topo-outside">GSLKH</span><span class="topo-membrane">AGLALSISLAACFNAL</span><span class="topo-inside">MLYWQLRRQAIFSPLVGWGKFL</span><span class="topo-membrane">LKLIAALIVMVAVLLLLL</span><span class="topo-outside">NFMPPWEQGNM</span><span class="topo-membrane">LVRITR</span></span>
<span class="topo-ruler">       490       500       510 </span>
<span class="topo-line"><span class="topo-membrane">LLLVVFAGAMSYFAAL</span><span class="topo-inside">FIFGFRLR</span><span class="topo-unknown">DFSQRAI</span></span>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>12</td>
      <td>9</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>28</td>
      <td>13</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>41</td>
      <td>29</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>57</td>
      <td>42</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>91</td>
      <td>58</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>109</td>
      <td>92</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>127</td>
      <td>110</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>145</td>
      <td>128</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>160</td>
      <td>146</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>176</td>
      <td>161</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>188</td>
      <td>177</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>204</td>
      <td>189</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>238</td>
      <td>205</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>255</td>
      <td>239</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>262</td>
      <td>256</td>
      <td>262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>263</td>
      <td>280</td>
      <td>263</td>
      <td>280</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>281</td>
      <td>315</td>
      <td>281</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>333</td>
      <td>316</td>
      <td>333</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>350</td>
      <td>334</td>
      <td>350</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>351</td>
      <td>367</td>
      <td>351</td>
      <td>367</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>386</td>
      <td>368</td>
      <td>386</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>402</td>
      <td>387</td>
      <td>402</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>403</td>
      <td>407</td>
      <td>403</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>423</td>
      <td>408</td>
      <td>423</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>445</td>
      <td>424</td>
      <td>445</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>446</td>
      <td>463</td>
      <td>446</td>
      <td>463</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>464</td>
      <td>474</td>
      <td>464</td>
      <td>474</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>475</td>
      <td>496</td>
      <td>475</td>
      <td>496</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>497</td>
      <td>504</td>
      <td>497</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>505</td>
      <td>511</td>
      <td>505</td>
      <td>511</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7wax">7WAX</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">NLLKSL</span><span class="topo-membrane">AAISSMTMFSRILGFIRDAIIA</span><span class="topo-outside">RFFGAGAAT</span><span class="topo-membrane">DAFFVAFRLPNLLRRIFAEGAFS</span><span class="topo-inside">QAFVPILAEYKNQQGDEATRTFIAYVS</span><span class="topo-membrane">GLLTLILAIVTLAGILAAPWII</span><span class="topo-outside">YITAPGFTDT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">PDKFDLT</span><span class="topo-membrane">VRLLRITFPYILLISLASLAGA</span><span class="topo-inside">ILNTWNRF</span><span class="topo-membrane">SVPAFAPTLLNISMIISVLL</span><span class="topo-outside">LAPYCEPPIIA</span><span class="topo-membrane">LGWGVFAGGILQLLYQLPY</span><span class="topo-inside">LQKIGMLVLPRISFRNSGVWRVLKLMGPA</span><span class="topo-membrane">IIGV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">SVSQISLIINTIFAS</span><span class="topo-outside">FLQSGSV</span><span class="topo-membrane">SWMYYADRLMELPTGVLGVALG</span><span class="topo-inside">TILLPSLAKSFSTGDHKEYQRLMDWGL</span><span class="topo-membrane">RLCFLLALPCAIALAILAEPLTVSLF</span><span class="topo-outside">QYGNFTAYDAVMT</span><span class="topo-membrane">QRALIAYCVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">LMGLIVVKVLA</span><span class="topo-inside">PGFYSRQDIKTP</span><span class="topo-membrane">VKIAIITLILTQLMNLAFI</span><span class="topo-outside">GSLKH</span><span class="topo-membrane">AGLALSISLAACFNALMLYW</span><span class="topo-inside">QLRRQAIFSPLVGWGKF</span><span class="topo-membrane">LLKLIAALIVMVAVLLLLLNFM</span><span class="topo-outside">PPWEQGNM</span><span class="topo-membrane">LVRITR</span></span>
<span class="topo-ruler">       490       500       510 </span>
<span class="topo-line"><span class="topo-membrane">LLLVVFAGAMSYFAALFIF</span><span class="topo-inside">GFRLRDFSQRAI</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>29</td>
      <td>8</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>38</td>
      <td>30</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>61</td>
      <td>39</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>88</td>
      <td>62</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>110</td>
      <td>89</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>127</td>
      <td>111</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>149</td>
      <td>128</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>157</td>
      <td>150</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>177</td>
      <td>158</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>188</td>
      <td>178</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>207</td>
      <td>189</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>236</td>
      <td>208</td>
      <td>236</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>255</td>
      <td>237</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>262</td>
      <td>256</td>
      <td>262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>263</td>
      <td>284</td>
      <td>263</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>285</td>
      <td>311</td>
      <td>285</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>337</td>
      <td>312</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>338</td>
      <td>350</td>
      <td>338</td>
      <td>350</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>351</td>
      <td>371</td>
      <td>351</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>383</td>
      <td>372</td>
      <td>383</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>402</td>
      <td>384</td>
      <td>402</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>403</td>
      <td>407</td>
      <td>403</td>
      <td>407</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>408</td>
      <td>427</td>
      <td>408</td>
      <td>427</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>444</td>
      <td>428</td>
      <td>444</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>466</td>
      <td>445</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>467</td>
      <td>474</td>
      <td>467</td>
      <td>474</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>475</td>
      <td>499</td>
      <td>475</td>
      <td>499</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>500</td>
      <td>511</td>
      <td>500</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.1802192115

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6cc4">6CC4</a></td>
      <td>3.5</td>
      <td>Not specified</td>
      <td>E. coli MurJ (residues 5-507) with N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> fusion</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41(DE3)
- **Construct**: MurJ_TA (T. africanus): His10-MBP-PPX-MurJ_TA-PPX-His10; EcMurJ (E. coli) residues 12-511; AeMurJ (Arsenophonus) full-length with [TEV](/xray-mp-wiki/reagents/additives/tev-protease/)-cleavable C-terminal GFP-His8
- **Notes**: Sources: doi/10.1038##s41467-019-09658-0 (MurJ_TA); doi/10.1016##j.str.2022.05.008 (EcMurJ, AeMurJ)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6cc4">6CC4</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MA</span><span class="topo-outside">DLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLKSLA</span><span class="topo-membrane">AVSSMTMFS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">RVLGFARDA</span><span class="topo-inside">IVARIFGAGMATDAFF</span><span class="topo-membrane">VAFKLPNLLRRIFAEGAFS</span><span class="topo-outside">QAFVPILAEYKSKQGEDATRVFV</span><span class="topo-membrane">SYVSGLLTLALAVVTVAGM</span><span class="topo-inside">LA</span><span class="topo-unknown">APWVIMVT</span><span class="topo-inside">APGFADTADKFALTSQLLKIT</span><span class="topo-membrane">FPY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">ILLISLASLVGAIL</span><span class="topo-outside">NTWNRF</span><span class="topo-membrane">SIPAFAPTLLNISMI</span><span class="topo-inside">GFALFAAPYFNPPVLALAWA</span><span class="topo-membrane">VTVGGVLQLVYQLPHLKK</span><span class="topo-outside">IGMLVLPRINFHD</span><span class="topo-unknown">AGAMRVVKQM</span><span class="topo-membrane">GPAILGVSVSQISLIINTIF</span><span class="topo-inside">ASFL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">ASGSVSWM</span><span class="topo-membrane">YYADRLMEFPSGVLGVAL</span><span class="topo-outside">GTILLPSLSKSFASGNHDEYNRLMDWGLRLC</span><span class="topo-membrane">FLLALPSAVALGILSGPLT</span><span class="topo-inside">VSLFQYGKFTAFDALMTQ</span><span class="topo-membrane">RALIAYSVGLIGLIVVK</span><span class="topo-outside">VLAPGFYSR</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">QDIKTP</span><span class="topo-membrane">VKIAIVTLILTQLMNLAFI</span><span class="topo-inside">GPLKHA</span><span class="topo-membrane">GLSLSIGLAACLNASLL</span><span class="topo-outside">YWQLRKQKIFTPQPGWMAFL</span><span class="topo-membrane">LRLVVAVLVMSGVLLGMLHIM</span><span class="topo-inside">PEWSLGTMPWRL</span><span class="topo-membrane">LRLMAVVLAGIAAYFAALA</span></span>
<span class="topo-ruler">       610    </span>
<span class="topo-line"><span class="topo-membrane">VL</span><span class="topo-outside">GFKVKEFA</span><span class="topo-unknown">RRTV</span></span>
<details class="topo-details"><summary>Topology coordinates (32 regions)</summary>
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
      <td>111</td>
      <td>-100</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>129</td>
      <td>9</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>145</td>
      <td>27</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>164</td>
      <td>43</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>187</td>
      <td>62</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>206</td>
      <td>85</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>208</td>
      <td>104</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>216</td>
      <td>106</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>217</td>
      <td>237</td>
      <td>114</td>
      <td>134</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>254</td>
      <td>135</td>
      <td>151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>260</td>
      <td>152</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>275</td>
      <td>158</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>295</td>
      <td>173</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>313</td>
      <td>193</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>326</td>
      <td>211</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>336</td>
      <td>224</td>
      <td>233</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>337</td>
      <td>356</td>
      <td>234</td>
      <td>253</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>368</td>
      <td>254</td>
      <td>265</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>386</td>
      <td>266</td>
      <td>283</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>417</td>
      <td>284</td>
      <td>314</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>418</td>
      <td>436</td>
      <td>315</td>
      <td>333</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>437</td>
      <td>454</td>
      <td>334</td>
      <td>351</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>471</td>
      <td>352</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>472</td>
      <td>486</td>
      <td>369</td>
      <td>383</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>505</td>
      <td>384</td>
      <td>402</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>506</td>
      <td>511</td>
      <td>403</td>
      <td>408</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>528</td>
      <td>409</td>
      <td>425</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>529</td>
      <td>548</td>
      <td>426</td>
      <td>445</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>549</td>
      <td>569</td>
      <td>446</td>
      <td>466</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>570</td>
      <td>581</td>
      <td>467</td>
      <td>478</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>582</td>
      <td>602</td>
      <td>479</td>
      <td>499</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>603</td>
      <td>610</td>
      <td>500</td>
      <td>507</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Complete conformational landscape of MurJ

The paper captured MurJ_TA in four conformations (inward-closed, inward-open, inward-occluded, outward-facing), revealing the complete transport cycle. The ordered trajectory proceeds through lateral gating at the membrane portal, asymmetric thin gate formation, and outward transition driven by TM7 straightening.

### Lateral membrane portal controls substrate entry

The lateral membrane portal between TM1 and TM8 dilates from 8.0 A to 17.4 A during the inward-closed to inward-open transition, controlled by TM4-5 loop rearrangement and TM1 bending. The conserved TM4-5 loop (Leu145, Asn146, Phe151, Pro158) distinguishes MurJ from MATE drug pumps and is a specific adaptation for flippase function.

### Thin gate occludes Lipid II headgroup

An asymmetric inward-occluded state features a thin gate formed by Glu57 (TM2) and Arg352 (TM10) that likely occludes the Lipid II headgroup in the cavity above the gate. The conserved (G/A)-E-G-A motif on TM2 enables S-shaped bending for thin gate formation.

### Arg352 as a multifunctional switch

Arg352 participates in both the thin gate (with Glu57 in inward-occluded) and the cytoplasmic gate (with Ser61, Ser62, Gly58 backbone in outward-facing), suggesting it plays a key role in conformational transitions during the transport cycle.

### Sodium binding site in the C-lobe

A sodium ion was identified in the C-lobe (TMs 7, 11, 12) coordinated by Asp235, Asn374, Asp378, Val390 (CO), and Thr394 in trigonal bipyramidal geometry. The DNDXT motif and coordination geometry are conserved with MATE transporters. Sodium binding at Asp235 may propagate conformational changes down TM7.

### Arg24-Asp25-Arg255 substrate-binding triad

Three conserved residues (Arg24, Asp25, Arg255) undergo coordinated rearrangement across conformational states. In the inward-occluded state, Arg24 and Arg255 are brought to 2.9 A proximity, stabilized by electrostatic interactions with Asp25 and the Lipid II diphosphate moiety. Mutations at these positions cause Lipid II accumulation and loss of complementation.

### Squeezed form represents post-release intermediate

The EcMurJ squeezed form lacks an internal cavity. The distance between TM2 and TM8 at the middle and periplasmic pairs is less than 9 A, considerably closer than in inward or outward forms. This conformation is proposed to occur after Lipid II release to the periplasm, preventing substrate re-binding and reverse flip.

### TM7 acts as conformational switch

TM7 is the most structurally variable helix, connecting N- and C-lobes. The bend angle at G239 in the squeezed form (76 deg) is larger than in the outward form. C-lobe rotates about 35 deg in conjunction with TM7 bend angle changes, leading to cavity closure.

### Coevolution supports squeezed form existence

EVcouplings server predicted coevolution of residues R53 and E273, whose side chains are adjacent only in the squeezed form. The cluster of residues R52, R53, E57, R270, and E273 appears to stabilize the squeezed form.

### Rocker switch transport model

MurJ transports Lipid II via alternating access. Inward closed/open form captures Lipid II. Inward occluded form holds substrate with a narrow gate between E57(TM2) and V281(TM8). Outward form releases Lipid II to periplasm. After release, MurJ adopts the squeezed form before transitioning back to inward forms.

### High-throughput mutagenesis (mut-seq) mapping of E. coli MurJ

High-throughput mutagenesis with next-generation sequencing (mut-seq) was performed on E. coli MurJ, scoring complementation of more than 1,500 individual point mutants covering all 521 codons. A total of 61 severely deleterious missense mutations were identified and mapped into four functional groups: (i) buried hydrophobic residues affecting folding; (ii) extracellular gate residues (D39, S263) at the interface between N-lobe and C-lobe; (iii) intracellular gate residues (V65, P66, A69 interacting with L288, P289, S292) that stabilize the outward-open conformation; and (iv) solvent-exposed residues in the central cavity and extended groove involved in substrate binding. Mutations altering the central cavity charge were particularly common, highlighting the importance of electrostatic interactions for substrate recognition and transport.

### Rocker-switch alternating-access model supported by evolutionary coupling

Evolutionary coupling analysis using 15,972 MurJ sequences identified 470 significant coevolving pairs. A subset of coevolved residue pairs are distant in the inward-open structure but become close in an outward-open homology model (based on MATE transporter PDB 3VVN). These pairs are located on opposite lobes at the cytosolic face, demonstrating that both inward-open and outward-open states are under evolutionary selection and supporting a rocker-switch alternating-access model for lipid II flipping.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — MurJ uses alternating access to flip Lipid II across the membrane
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-beta-D-maltopyranoside (beta-DDM)</a> — Detergent used for purification and crystallization
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used in [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) [affinity chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) buffers
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Primary buffer component throughout purification
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> — Reducing agent in purification buffers
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta/) IMAC and [TALON](/xray-mp-wiki/reagents/additives/talon/) cobalt affinity used for initial purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) used as final polishing step
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — EcMurJ and AeMurJ-L and MurJ_TA structures solved by MR
- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction (SAD)</a> — AeMurJ-N structure solved by Se-Met SAD phasing
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP)</a> — MurJ_TA was crystallized by LCP method
- <a href="/xray-mp-wiki/reagents/detergents/dmng/">Decyl Maltose Neopentyl Glycol (DMNG)</a> — Used in final purification buffer for MurJ_TA
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Used as LCP host lipid for MurJ_TA crystallization
