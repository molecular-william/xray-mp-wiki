---
title: "CD47 BRIL-B6H12 complex from Homo sapiens"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-25475-w]
verified: pdb
uniprot_id: Q08722
---

# CD47 BRIL-B6H12 complex from Homo sapiens

<div class="expr-badges"><span class="expr-badge expr-mammalian">Mammalian</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q08722">UniProt: Q08722</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

CD47 is the only 5-transmembrane (5-TM) spanning receptor of the immune system. Its extracellular domain (ECD) is a heavily glycosylated cell surface marker of self that binds signal regulatory protein alpha (SIRPalpha) and inhibits macrophage phagocytosis, delivering a 'don't eat me' signal. This structural characterization presents the crystal structure of full-length human CD47 in complex with the function-blocking antibody B6H12, which can inhibit the binding of two endogenous partners, SIRPalpha and thrombospondin-1. The structure reveals a unique extracellular loop region (ECLR) architecture, comprised of two extracellular loops and a six-residue linker (RVVSWF) that forms an extended SWF loop. The hydrophobic aromatic side chains of W118 and F119 from the SWF loop are buried deep in the ECLR core, providing an anchor point for tethering the ECD to the transmembrane domain. Molecular dynamics simulations revealed ECD motion between two macrostates (s1 and s2), with a ~22 degree tilt transition mediated by the conformational switch of Tyr184 on ECL1. CD47 is a validated drug target in cancer immuno-therapy, with multiple clinical trials focused on blocking CD47-SIRPalpha interaction.


## Publications

### doi/10.1038##s41467-021-25475-w

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7myz">7MYZ</a></td>
      <td>2.85</td>
      <td>P 21 21 21</td>
      <td>Full-length CD47 (residues 1-278) with <a href="/xray-mp-wiki/reagents/protein-tags/bril">BRIL</a> fusion on helix IV, in complex with B6H12 Fab</td>
      <td>B6H12 Fab</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: CHO cells
- **Construct**: CD47 (residues 1-278) with [BRIL](/xray-mp-wiki/reagents/protein-tags/bril) fusion on helix IV, expressed transiently in ExpiCHO-S cells
- **Notes**: B6H12 mAb expressed in ExpiCHO-S cells. Fab prepared from IgG1 using Pierce Fab Preparation kit.

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
      <td>1</td>
      <td>Cell lysis by sonication</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">NaCl</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Membrane fraction collected by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation">ultracentrifugation</a></td>
    </tr>
    <tr>
      <td>2</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity chromatography</a> (Protein-A for Fab, <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> for CD47)</td>
      <td>Protein-A affinity resin / <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> Superflow</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">NaCl</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>B6H12 Fab eluted with 100 mM sodium <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate</a> pH 3.3, neutralized</td>
    </tr>
    <tr>
      <td>3</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-exclusion chromatography</a></td>
      <td>—</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 250 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">NaCl</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Final purification step for complex formation and crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor diffusion</a>, <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion">sitting drop</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>CD47-<a href="/xray-mp-wiki/reagents/protein-tags/bril">BRIL</a>-B6H12 complex at ~10 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>25% <a href="/xray-mp-wiki/reagents/additives/peg400">PEG400</a>, 0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate</a> pH 5.5, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/mes">MES</a> pH 6.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Full-length CD47-B6H12 complex crystals diffracted to 2.85 Angstrom</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7myz">7MYZ</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">QLLFNKTKSVEFTFCNDTVVIPCFVTNMEAQNTTEVYVKWKFKGRDIYTFDGALNKSTVPTDFSSAKIEVSQLLKGDASLKMDKSDAVSHTGNYTCEVTELTREGETIIELKYRVVSWFS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">P</span><span class="topo-membrane">NENILIVIFPIFAILLFWGQFG</span><span class="topo-inside">IKT</span><span class="topo-unknown">LKYRSGADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">AAAEQLKTTRNAYIQKYLGMDEK</span><span class="topo-inside">TIA</span><span class="topo-membrane">LLVAGLVITVIVIVGAILFVP</span><span class="topo-outside">GEYS</span><span class="topo-membrane">LKNATGLGLIVTSTGILILLHYYV</span><span class="topo-inside">F</span><span class="topo-unknown">STAIG</span><span class="topo-inside">LTS</span><span class="topo-membrane">FVIAILVIQVIAYILAVVGLSLCI</span><span class="topo-outside">AACIPMH</span><span class="topo-membrane">GPLLI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420 </span>
<span class="topo-line"><span class="topo-membrane">SGLSILALAQLLGLVYMK</span><span class="topo-inside">FVASNQ</span><span class="topo-unknown">KTIQPPRKAVEEPLNAFKESKGMMNDEHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>121</td>
      <td>1</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>143</td>
      <td>122</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>146</td>
      <td>144</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>147</td>
      <td>147</td>
      <td>147</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>264</td>
      <td>266</td>
      <td>158</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>287</td>
      <td>161</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>288</td>
      <td>291</td>
      <td>182</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>315</td>
      <td>186</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>316</td>
      <td>210</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>324</td>
      <td>216</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>348</td>
      <td>219</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>349</td>
      <td>355</td>
      <td>243</td>
      <td>249</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>378</td>
      <td>250</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>379</td>
      <td>384</td>
      <td>273</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7myz">7MYZ</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">QLLFNKTKSVEFTFCNDTVVIPCFVTNMEAQNTTEVYVKWKFKGRDIYTFDGALNKSTVPTDFSSAKIEVSQLLKGDASLKMDKSDAVSHTGNYTCEVTELTREGETIIELKYRVVS</span><span class="topo-unknown">WFS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">PNENILIVIFPIFAILLFWGQFGIKTLKYRSGADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">AAAEQLKTTRNAYIQKYLGMDEKTIALLVAGLVITVIVIVGAILFVPGEYSLKNATGLGLIVTSTGILILLHYYVFSTAIGLTSFVIAILVIQVIAYILAVVGLSLCIAACIPMHGPLLI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420 </span>
<span class="topo-line"><span class="topo-unknown">SGLSILALAQLLGLVYMKFVASNQKTIQPPRKAVEEPLNAFKESKGMMNDEHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>117</td>
      <td>1</td>
      <td>117</td>
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

### Unique 5-TM receptor architecture

CD47 is the only known 5-TM receptor of the immune system and the human genome (together with the distantly related prominin family). The TMD forms a pentagon-like helical bundle spanning ~32 Angstrom across the lipid membrane. Helix II is nearly perpendicular to the membrane, while helices I, III, IV, and V span at shallower angles. A proline-induced kink at P131 in helix I allows helical tilt away from the receptor core. An intracellular hydrogen bond network centered on H206 (involving Q141, Q227, and Q264) contributes to local stability of the 5-TM bundle at the intracellular side.

### ECD motion and immune recognition

The relative orientation of the ECD with respect to the TMD is dynamic. Molecular dynamics simulations revealed two macrostates (s1 and s2) separated by a ~22 degree ECD tilt. The transition is mediated by the conformational switch of Tyr184 on ECL1, which hydrogen bonds to ECL2 residues I242 and A244 in the s1 state. Departure of Y184 from the ECLR pocket triggers ECD rigid body shifts. The ECD transition from s1 to s2 is accompanied by shortening of the RVVSWF linker, allowing R114 to dock into a negatively charged ECLR pocket between helix I and V. This dynamic ECD positioning may be relevant for recognition by different endogenous protein partners including SIRPalpha, integrins, and thrombospondin-1.


## Cross-References

- <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> — Entity mentioned in overview or biological insights
- <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> — Entity mentioned in overview or biological insights
- <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a> — Entity mentioned in overview or biological insights
- <a href="/xray-mp-wiki/reagents/protein-tags/bril">BRIL</a> — Entity mentioned in overview or biological insights
- <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> — Entity mentioned in overview or biological insights
- <a href="/xray-mp-wiki/reagents/buffers/mes">MES</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/peg400">PEG400</a> — Entity mentioned in text
