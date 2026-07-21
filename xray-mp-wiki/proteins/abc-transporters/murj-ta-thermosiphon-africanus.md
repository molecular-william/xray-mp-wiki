---
title: "MurJ from Thermosiphon africanus (MurJ_TA) — Lipid II Flippase"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, enzyme]
sources: [doi/10.1038##nsmb.3346]
verified: agent
uniprot_id: B7IE18
---

# MurJ from Thermosiphon africanus (MurJ_TA) — Lipid II Flippase

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/B7IE18">UniProt: B7IE18</a>

<span class="expr-badge">Thermosipho africanus (strain TCF52B)</span>

## Overview

[MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/) from Thermosiphon africanus (MurJ_TA) is a lipid II flippase belonging to the multidrug/oligosaccharidyl-lipid/polysaccharide (MOP) transporter superfamily. [MURJ](/xray-mp-wiki/proteins/abc-transporters/murj/) flips the peptidoglycan precursor lipid II from the cytoplasmic leaflet to the periplasmic leaflet of the bacterial inner membrane, a critical step in peptidoglycan biogenesis. The crystal structure of MurJ_TA was solved at 2.0 A resolution in an inward-facing conformation, revealing a large central cavity divided into a cationic proximal site and a distal site, connected to a hydrophobic groove formed by two C-terminal transmembrane helices (TMs 13-14) that accommodates the undecaprenyl tail of lipid II.


## Publications

### doi/10.1038##nsmb.3346

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
      <td>C2</td>
      <td>Full-length <a href="/xray-mp-wiki/proteins/abc-transporters/murj/">MURJ</a> (residues 1-475) from Thermosiphon africanus with N-terminal His10-MBP tag removed by <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a></td>
      <td>Chloride ion, <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41(DE3)
- **Construct**: His10-MBP-PPX-MurJ-PPX-His10 (N-terminal His10-MBP tag and C-terminal His10 tag, both cleavable by [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/))
- **Notes**: SeMet-labeled protein expressed in B834(DE3) by autoinduction with 125 mg/L L-[Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/)
- **Induction**: 0.4 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600 0.8
- **Media**: Terrific broth (LB for autoinduction with [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/))

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
      <td>Microfluidizer</td>
      <td>Not specified</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl</td>
      <td>Including 10 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, 1 ug/mL leupeptin, 1 ug/mL pepstatin, 5 uU/mL aprotinin, 20 ug/mL DNase I, 2.5 mM PMSF</td>
    </tr>
    <tr>
      <td>Membrane extraction</td>
      <td>Detergent solubilization</td>
      <td>Not specified</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl + 30 mM n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Stirring for 1 h at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (IMAC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> Cobalt resin</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 500 mM NaCl, 15 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Wash buffer: 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 15 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>. Eluted with 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>. Incubated overnight with 40 ug/mL <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> and 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>.</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 2 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> + 0.3 mM decyl <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> neopentyl glycol (<a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a>)</td>
      <td>Final purification step; detergent exchanged from <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> to <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>MurJ_TA at 15 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 2 mM TCEP, 0.3 mM <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein mixed with molten <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> in 2:3 (w/w) protein:lipid ratio. 150 nL LCP drops overlaid with 1 uL precipitant. Crystals grew to full size in 4 weeks. Native crystals supplemented with 1.5 mM lipid II in <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>.</td>
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
      <td>6.5</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Peg 400: 30-45 % [precipitant] (PEG400)  
- Calcium Chloride: 200-400 mM [salt]</td>
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

## Biological / Functional Insights

### Inward-facing conformation of a MOP transporter

The structure of MurJ_TA represents the first structure of a MOP transporter captured in an inward-facing conformation, contrasting with the outward-facing V-shape observed in MATE transporters. The N-lobe (TMs 1-6) and C-lobe (TMs 7-14) are arranged in an inward-facing N-shape. TM7 is bent by approximately 45 degrees about Ser228, which likely acts as a hinge for the rocker-switch motion between inward- and outward-facing states.

### Substrate recognition and binding

A hydrophobic groove formed by C-terminal TMs 13-14 binds the undecaprenyl tail of lipid II. The groove connects via a membrane portal (between TMs 1 and 8) to a large central cavity. The proximal site of the cavity is highly cationic (Arg18, Arg24, Arg52, Arg255), serving to recognize the diphosphate and sugar moieties of lipid II. A chloride ion was observed in the proximal site. The distal site accommodates the pentapeptide moiety.

### Alternating-access rocker-switch mechanism

Based on the inward-facing structure, MTSES accessibility data, and an outward-facing homology model, a rocker-switch mechanism was proposed for lipid II flipping. The N-lobe and C-lobe rotate about a TM7 hinge (Ser228), translocating lipid II across the membrane. The hydrophobic groove retains the undecaprenyl tail during the transition. This mechanism differs from the [PGLK](/xray-mp-wiki/proteins/abc-transporters/pglk/) flippase which operates via only an outward-facing state.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/mop-transporter-superfamily/">MOP Transporter Superfamily</a> — MurJ is a member of the MOP superfamily, specifically the MVF family
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Used for membrane extraction of MurJ_TA
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Host lipid for LCP crystallization
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Used throughout purification and crystallization buffers
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/abc-transporters/murj/">MURJ</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/abc-transporters/pglk/">PGLK</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
