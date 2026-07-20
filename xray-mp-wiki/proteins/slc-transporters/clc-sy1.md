---
title: "CLC-sy1 (CLC Cl-/H+ Antiporter from Synechocystis sp. PCC6803)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1021##bi1019258]
verified: agent
uniprot_id: P73745
---

# CLC-sy1 (CLC Cl-/H+ Antiporter from Synechocystis sp. PCC6803)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P73745">UniProt: P73745</a>

<span class="expr-badge">Synechocystis sp.</span>

## Overview

CLC-sy1 (SY) is a CLC Cl-/H+ exchange transporter from the cyanobacterium Synechocystis sp. PCC6803. Its X-ray crystal structure was determined at 3.2 Angstrom resolution, revealing a homodimeric architecture nearly identical to that of the E. coli CLC-ec1 (EC) homologue (39% sequence identity, C-alpha rmsd 1.3 Angstrom). All key residues involved in Cl- binding and proton coupling are structurally conserved. SY actively pumps protons into liposomes against a gradient and moves Cl- at approximately 20 s-1 per subunit, roughly 100-fold slower than EC. Electrostatic calculations identified two residues (F143 and D309) flanking the external binding site that are destabilizing for Cl- binding in SY; mutating these to their EC counterparts (F143R/D309F) accelerates transport to approximately 150 s-1, allowing measurement of the Cl-/H+ stoichiometry at 2:1. SY provides a comparative structural model for understanding the determinants of CLC transport rates.

## Publications

### doi/10.1021##bi1019258

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3nco">3NCO</a></td>
      <td>3.2</td>
      <td>unknown</td>
      <td>CLC-sy1 residues 26-450 from Synechocystis sp. PCC6803, expressed in E. coli, treated with lysine-C endoproteinase to remove first 14 N-terminal residues</td>
      <td>Cl- (central binding site)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3q17">3Q17</a></td>
      <td>3.2</td>
      <td>unknown</td>
      <td>Same construct as 3NCO, crystallized with Br-</td>
      <td>Br- (anomalous difference data)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: CLC-sy1 from Synechocystis sp. PCC6803. For crystallization, the preparation was treated with lysine-C endoproteinase to remove the first 14 N-terminal residues. Purified on Superdex 200 gel filtration column in 100 mM NaCl, 20 mM Tris-HCl, pH 7.5, and 5 mM DM.

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
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> (pH 7.5) + 5 mM DM (<a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside</a>)</td>
      <td>Lysine-C endoproteinase treatment (1 h, 0.01 unit/mg, 25 C) before <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> step to remove first 14 N-terminal residues</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified CLC-sy1 at 18-25 mg/mL with 40 mM DM</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>30-32% PEG 400, 200 mM <a href="/xray-mp-wiki/reagents/additives/calcium-chloride/">CaCl2</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> (pH 8.0-8.2)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-12 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Additives introduced to final concentrations: C-Hega-11 (14 mM), SrCl2 (12 mM), PEG 400 (6.2%), and in some cases Hega-10 (9 mM) and decanoyl sucrose (3 mM). Only crystals larger than 200 um diffracted well. Structure solved by molecular replacement with PHASER using EC homodimer (PDB 1OTS) as search model. Anisotropic diffraction with high mosaicity. High solvent content (80%).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3q17">3Q17</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAADFETSNRRWLDKLPRNLTDSAR</span><span class="topo-inside">SLHPRTL</span><span class="topo-membrane">VAAIVVGLITGVLGAGFKSAVN</span><span class="topo-outside">NMLQWRSQLAQILAPIPPLAWL</span><span class="topo-membrane">VTALISGGMVALSFWL</span><span class="topo-inside">MKRFAPDTSGSGIPQIEGHLEGKLPLVW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QRVL</span><span class="topo-membrane">PIKLVGGFLSLGAG</span><span class="topo-outside">M</span><span class="topo-membrane">LAGFEGPTIQMGG</span><span class="topo-inside">SIGQMTGGWFKATQENQRILIAV</span><span class="topo-unknown">GAGAGLATAFNAPLAGVALIGEE</span><span class="topo-inside">MHPRFRSQTLAY</span><span class="topo-membrane">HSLLFGCVMATIILRMI</span><span class="topo-outside">RGQSAIISLTEFK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">RVPLDSL</span><span class="topo-membrane">WMFIILGILFGVMGYTFNRGL</span><span class="topo-inside">FKVLDWFDRLPPLATK</span><span class="topo-membrane">WKGFLLGSIIGIL</span><span class="topo-outside">SLFPLPLTDGGDNAVLWAFNSQSHFSTLILVF</span><span class="topo-membrane">CGRFLLTLICYGSG</span><span class="topo-inside">A</span><span class="topo-membrane">IGGIFAPMLGIAS</span><span class="topo-outside">IVS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460      </span>
<span class="topo-line"><span class="topo-outside">VAMARHFHLLFPSQIPEPAVMAIA</span><span class="topo-unknown">GMGALVAATVRAPLTAILLTIEM</span><span class="topo-outside">TDNYFVI</span><span class="topo-membrane">LPLLVTCLVASVVAEAL</span><span class="topo-inside">GGKPIYTVLLERTLAKQNR</span><span class="topo-unknown">GSLVPRGSGGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>25</td>
      <td>1</td>
      <td>25</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>32</td>
      <td>26</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>54</td>
      <td>33</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>76</td>
      <td>55</td>
      <td>76</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>92</td>
      <td>77</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>124</td>
      <td>93</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>138</td>
      <td>125</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>139</td>
      <td>139</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>152</td>
      <td>140</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>175</td>
      <td>153</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>198</td>
      <td>176</td>
      <td>198</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>210</td>
      <td>199</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>227</td>
      <td>211</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>247</td>
      <td>228</td>
      <td>247</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>268</td>
      <td>248</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>284</td>
      <td>269</td>
      <td>284</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>297</td>
      <td>285</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>329</td>
      <td>298</td>
      <td>329</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>343</td>
      <td>330</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>357</td>
      <td>345</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>384</td>
      <td>358</td>
      <td>384</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>407</td>
      <td>385</td>
      <td>407</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>408</td>
      <td>414</td>
      <td>408</td>
      <td>414</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>415</td>
      <td>431</td>
      <td>415</td>
      <td>431</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>450</td>
      <td>432</td>
      <td>450</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>451</td>
      <td>466</td>
      <td>451</td>
      <td>466</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3q17">3Q17</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAADFETSNRRWLDKLPRNLTDSAR</span><span class="topo-inside">SLHPRTL</span><span class="topo-membrane">VAAIVVGLITGVLGAGFKSAVN</span><span class="topo-outside">NMLQWRSQLAQILAPIPPLAWL</span><span class="topo-membrane">VTALISGGMVALSFWL</span><span class="topo-inside">MKRFAPDTSGSGIPQIEGHLEGKLPLVW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QRVL</span><span class="topo-membrane">PIKLVGGFLSLGAG</span><span class="topo-outside">M</span><span class="topo-membrane">LAGFEGPTIQMGG</span><span class="topo-inside">SIGQMTGGWFKATQENQRILIAV</span><span class="topo-unknown">GAGAGLATAFNAPLAGVALIGEE</span><span class="topo-inside">MHPRFRSQTLAY</span><span class="topo-membrane">HSLLFGCVMATIILRMI</span><span class="topo-outside">RGQSAIISLTEFK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">RVPLDSL</span><span class="topo-membrane">WMFIILGILFGVMGYTFNRGL</span><span class="topo-inside">FKVLDWFDRLPPLATK</span><span class="topo-membrane">WKGFLLGSIIGIL</span><span class="topo-outside">SLFPLPLTDGGDNAVLWAFNSQSHFSTLILVF</span><span class="topo-membrane">CGRFLLTLICYGSG</span><span class="topo-inside">A</span><span class="topo-membrane">IGGIFAPMLGIAS</span><span class="topo-outside">IVS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460      </span>
<span class="topo-line"><span class="topo-outside">VAMARHFHLLFPSQIPEPAVMAIA</span><span class="topo-unknown">GMGALVAATVRAPLTAILLTIEM</span><span class="topo-outside">TDNYFVI</span><span class="topo-membrane">LPLLVTCLVASVVAEAL</span><span class="topo-inside">GGKPIYTVLLERTLAKQNR</span><span class="topo-unknown">GSLVPRGSGGHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>25</td>
      <td>1</td>
      <td>25</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>32</td>
      <td>26</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>54</td>
      <td>33</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>76</td>
      <td>55</td>
      <td>76</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>92</td>
      <td>77</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>124</td>
      <td>93</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>138</td>
      <td>125</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>139</td>
      <td>139</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>152</td>
      <td>140</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>175</td>
      <td>153</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>198</td>
      <td>176</td>
      <td>198</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>199</td>
      <td>210</td>
      <td>199</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>227</td>
      <td>211</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>247</td>
      <td>228</td>
      <td>247</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>268</td>
      <td>248</td>
      <td>268</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>269</td>
      <td>284</td>
      <td>269</td>
      <td>284</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>297</td>
      <td>285</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>329</td>
      <td>298</td>
      <td>329</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>343</td>
      <td>330</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>357</td>
      <td>345</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>384</td>
      <td>358</td>
      <td>384</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>407</td>
      <td>385</td>
      <td>407</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>408</td>
      <td>414</td>
      <td>408</td>
      <td>414</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>415</td>
      <td>431</td>
      <td>415</td>
      <td>431</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>432</td>
      <td>450</td>
      <td>432</td>
      <td>450</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>451</td>
      <td>466</td>
      <td>451</td>
      <td>466</td>
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

### Slow transport rate compared to E. coli homologue

CLC-sy1 transports Cl- at ~20 s-1, approximately 100-fold slower than CLC-ec1 (2000-3000 s-1). This refutes the idea that CLC transport mechanisms intrinsically produce high rates. Despite nearly identical structures and shared 2:1 Cl-/H+ antiport stoichiometry, subtle sequence differences produce dramatically different turnover rates.

### Electrostatic determinants of transport rate

Electrostatic calculations identified residues F143 and D309 as key determinants of transport rate. Positioned at the N-terminal ends of helices pointed at the external Cl- site and adjacent to the external glutamate gate (E144), these residues are destabilizing for Cl- binding in SY and stabilizing in EC. The double mutant F143R/D309F increases SY turnover to ~150 s-1 (8% of EC rate).

### Gate removal does not speed transport in SY

In EC, removal of both external and internal gates (E148A/Y445A) produces a continuous pore and increases Cl- transport to ~20000 s-1. However, the equivalent mutation in SY (E144A/Y437A) produces no change in the slow Cl- transport rate, a surprising result that remains unexplained without a crystal structure of the double mutant.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Primary solubilization and purification detergent (5 mM DM)
- <a href="/xray-mp-wiki/reagents/additives/calcium-chloride/">Calcium Chloride (CaCl2)</a> — Component in crystallization reservoir (200 mM CaCl2)
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> — Buffer component in purification (100 mM NaCl)
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> — Buffer used in purification and crystallization
