---
title: "Opsin (Retinal-Free Rhodopsin Apoprotein)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature07063, doi/10.1038##nature07330, doi/10.1002##anie.201302374, doi/10.1016##j.str.2015.09.015, doi/10.1038##ncomms5801]
verified: agent
uniprot_id: P02699
---

# Opsin (Retinal-Free Rhodopsin Apoprotein)


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P02699">UniProt: P02699</a>

<span class="expr-badge">Bos taurus</span>

## Overview

Opsin is the apoprotein form of rhodopsin, the G-protein-coupled receptor responsible for vision in vertebrate retinal rod cells. The first crystal structure of ligand-free native opsin (PDB 3CAP, 2.9 A resolution, 2008) revealed the conformational changes associated with GPCR activation in the absence of an inactivating ligand. Compared to the dark-state rhodopsin structure, opsin shows prominent structural changes in the conserved E(D)RY and NPxxY(x)5,6F regions and in TM5-TM7, including a 6-7 A outward tilt of cytoplasmic TM6, breakage of the ionic lock between Arg135 and Glu247, and reorganization of the empty retinal-binding pocket with two openings that may serve retinal entry and exit. Later higher-resolution structures (PDB 4GZM at 2.65 A, PDB 4X1H at 2.3 A) resolved the active Ops* conformation in complex with synthetic G-protein peptides, revealing an extensive solvent-mediated hydrogen-bonding network connecting the chromophore binding site to the G protein binding site through conserved GPCR activation motifs (CWxP, NPxxY, and (D/E)RY). The opsin structure serves as the best available structural template for homology modeling of olfactory receptors (ORs), which comprise over half of all GPCRs.

## Publications

### doi/10.1038##nature07063

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3cap">3CAP</a></td>
      <td>2.9 A</td>
      <td>H3</td>
      <td>Native opsin apoprotein from bovine retinal rod cells (retinal-free rhodopsin, residues 1-348)</td>
      <td>None (retinal-free; empty binding pocket)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Vertebrate retinal rod cells (disc membrane)
- **Construct**: Native opsin apoprotein (retinal-free rhodopsin)

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
      <td>Disc membrane preparation</td>
      <td>Opsin solubilization from rod outer-segment disc membranes</td>
      <td>--</td>
      <td>20 mM BTP (pH 7.5), 130 mM NaCl, 1 mM MgCl2, 10% sucrose + <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> (beta-D-octylglucopyranoside, 1% w/v)</td>
      <td>Rod outer-segment disc membranes prepared from bovine eyes. Opsin solubilized using 1% beta-D-octylglucopyranoside. Solubilized opsin with A280/A362 ratios greater than 4 used without further purification.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Opsin apoprotein (5 mg/ml, epsilon280 = 81,200 M-1 cm-1) solubilized in <a href="/xray-mp-wiki/reagents/detergents/og/">og</a> detergent</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>2.8-3.2 M ammonium sulphate in 0.1 M MES or 0.1 M sodium acetate buffer, pH 5.6</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>277 K (4 C)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>7 days (crystals appeared within 2-3 days, grew further for 5 days)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>10% (w/v) trehalose in reservoir solution; crystals flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown using hanging-drop vapor diffusion at 277 K in 24-well Linbro plates. Each drop contained 2 ul protein + 2 ul reservoir. Colourless opsin crystals had dimensions of 0.1 x 0.1 x 0.2 mm3. On addition of 11-cis-retinal to the crystal, a colour change to red was observed, indicating rhodopsin could be regenerated. Data collected at 100 K at synchrotron beamline BL 14.2, BESSY (Berlin) with MAR-165CCD detector at 210 mm distance. Space group H3 (a = 242.92 A, b = 242.92 A, c = 110.42 A, alpha = beta = 90 degrees, gamma = 120 degrees). Two monomers in asymmetric unit arranged as a dimer with TM1 and H8 as interface.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3cap">3CAP</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTV</span><span class="topo-inside">QHKKLRTPLNY</span><span class="topo-membrane">ILLNLAVADLFMVFGGFTTTL</span><span class="topo-outside">YTSLHGYFVFGPTGCNL</span><span class="topo-membrane">EGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAI</span><span class="topo-inside">ERYVVVCKPMSNFRFGENHAI</span><span class="topo-membrane">MGVAFTWVMALACAAPPL</span><span class="topo-outside">VGWSRYIPEGMQCSCGIDYYTPHEETNNE</span><span class="topo-membrane">SFVIYMFVVHFIIPLIVIFF</span><span class="topo-inside">CYGQLVFTVKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-inside">ATTQKAEKEVTRMVI</span><span class="topo-membrane">IMVIAFLICWLPYAGVAFYIFT</span><span class="topo-outside">HQGSDFGPIFMT</span><span class="topo-membrane">IPAFFAKTSAVYNPVIYIMM</span><span class="topo-inside">NKQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>39</td>
      <td>1</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>63</td>
      <td>40</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>74</td>
      <td>64</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>95</td>
      <td>75</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>96</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>133</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>172</td>
      <td>155</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>201</td>
      <td>173</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>221</td>
      <td>202</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>255</td>
      <td>222</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>277</td>
      <td>256</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>289</td>
      <td>278</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>309</td>
      <td>290</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>326</td>
      <td>310</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>348</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3cap">3CAP</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTV</span><span class="topo-inside">QHKKLRTPLNY</span><span class="topo-membrane">ILLNLAVADLFMVFGGFTTTL</span><span class="topo-outside">YTSLHGYFVFGPTGCNL</span><span class="topo-membrane">EGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAI</span><span class="topo-inside">ERYVVVCKPMSNFRFGENHAI</span><span class="topo-membrane">MGVAFTWVMALACAAPPL</span><span class="topo-outside">VGWSRYIPEGMQCSCGIDYYTPHEETNNE</span><span class="topo-membrane">SFVIYMFVVHFIIPLIVIFF</span><span class="topo-inside">CYGQLVFTVKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-inside">ATTQKAEKEVTRMVI</span><span class="topo-membrane">IMVIAFLICWLPYAGVAFYIFT</span><span class="topo-outside">HQGSDFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMM</span><span class="topo-inside">NKQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>39</td>
      <td>1</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>63</td>
      <td>40</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>74</td>
      <td>64</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>95</td>
      <td>75</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>96</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>133</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>172</td>
      <td>155</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>201</td>
      <td>173</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>221</td>
      <td>202</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>255</td>
      <td>222</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>277</td>
      <td>256</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>288</td>
      <td>278</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>309</td>
      <td>289</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>326</td>
      <td>310</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>348</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nature07330

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3dqb">3DQB</a></td>
      <td>3.2 A</td>
      <td>H32</td>
      <td>Ops* (bovine rhodopsin apoprotein, residues 1-326) in complex with synthetic GalphaCT peptide (Galpha_t(340-350)K341L; ILENLKDCGLF)</td>
      <td>beta-D-Octylglucoside (OG); Palmitoyl chains; N-Acetyl-D-Glucosamine; GalphaCT peptide</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Vertebrate retinal rod cells (disc membrane)
- **Construct**: Native opsin apoprotein (retinal-free rhodopsin)

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3dqb">3DQB</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQF</span><span class="topo-membrane">SMLAAYMFLLIMLGFPINFLTLYVTV</span><span class="topo-inside">QHKKLRTPLN</span><span class="topo-membrane">YILLNLAVADLFMVFGGFTTTLYTSL</span><span class="topo-outside">HGYFVFGPT</span><span class="topo-membrane">GCNLEGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIE</span><span class="topo-inside">RYVVVCKPMSNFRFGENHA</span><span class="topo-membrane">IMGVAFTWVMALACAAPPLVGWS</span><span class="topo-outside">RYIPEGMQCSCGIDYYTPHEET</span><span class="topo-membrane">NNESFVIYMFVVHFIIPLIVIFFCYG</span><span class="topo-inside">QLVFTVKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-inside">ATTQKAEKEVT</span><span class="topo-membrane">RMVIIMVIAFLICWLPYAGVAFYIFT</span><span class="topo-outside">HQGSDFGPI</span><span class="topo-membrane">FMTIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-inside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>37</td>
      <td>1</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>63</td>
      <td>38</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>73</td>
      <td>64</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>99</td>
      <td>74</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>108</td>
      <td>100</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>134</td>
      <td>109</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>153</td>
      <td>135</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>176</td>
      <td>154</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>198</td>
      <td>177</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>224</td>
      <td>199</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>251</td>
      <td>225</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>277</td>
      <td>252</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>286</td>
      <td>278</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>310</td>
      <td>287</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>326</td>
      <td>311</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>348</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1002##anie.201302374

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4j4q">4J4Q</a></td>
      <td>2.65 A</td>
      <td>not specified</td>
      <td>Ops* conformation (retinal-free rhodopsin apoprotein) in complex with synthetic G protein peptide GalphaCT2</td>
      <td>Octyl glucoside (OG) in retinal-binding pocket; synthetic G protein peptide GalphaCT2</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Vertebrate retinal rod cells (disc membrane)
- **Construct**: Native opsin apoprotein (retinal-free rhodopsin)

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
      <td>Disc membrane solubilization</td>
      <td>Solubilization in <a href="/xray-mp-wiki/reagents/detergents/og/">og</a> detergent</td>
      <td>--</td>
      <td>not specified + <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
      <td>Opsin was solubilized from disc membranes of vertebrate retinal rod cells using <a href="/xray-mp-wiki/reagents/detergents/og/">og</a>, which favors the active Ops* conformation</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>X-ray crystallography</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Ops* in complex with synthetic G protein peptide GalphaCT2 and <a href="/xray-mp-wiki/reagents/detergents/og/">og</a> in <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> detergent</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>pH 5.6 crystallization conditions</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallization at low pH (5.6) in <a href="/xray-mp-wiki/reagents/detergents/og/">og</a> detergent promotes formation of the active Ops* conformation. The well-defined hydrogen-bond network holds <a href="/xray-mp-wiki/reagents/detergents/og/">og</a> in the retinal-binding pocket. Active Ops* conformation stabilized by <a href="/xray-mp-wiki/reagents/detergents/og/">og</a> in the ligand-binding pocket.</td>
    </tr>
  </tbody>
</table>
### doi/10.1016##j.str.2015.09.015

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4x1h">4X1H</a></td>
      <td>2.3 A</td>
      <td>not specified</td>
      <td>Activated opsin (bovine rhodopsin, residues 1-326) stabilized with nonyl-glucoside in chromophore binding site, in complex with Galpha-CT peptide (VLEDLKSCGLF)</td>
      <td>nonyl-glucoside (C9G) in chromophore binding pocket; Galpha-CT peptide (G alpha C-terminus mimetic)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Vertebrate retinal rod cells (disc membrane)
- **Construct**: Native opsin apoprotein (retinal-free rhodopsin)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, sitting drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Photoactivated rhodopsin (opsin) with 12-fold molar excess of Galpha-CT peptide (VLEDLKSCGLF), in nonyl-glucoside (C9G) detergent</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>3-3.4 M ammonium sulfate, 100 mM citrate (pH 5-6.5)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-12 months</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested from mother liquor, blotted, and flash frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in complete darkness at 4 C. Crystals appeared after 3-4 months and reached maximum dimensions of 300 x 300 x 600 um at 6-12 months. Data collected from a crystal over 16 months old at NE-CAT 23-ID-C using shutterless mode. Nonyl-glucoside (C9G) detergent was found occupying the chromophore binding site instead of retinal.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4x1h">4X1H</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTVQH</span><span class="topo-outside">KKL</span><span class="topo-membrane">RTPLNYILLNLAVADLFMVFGGFTTTLY</span><span class="topo-inside">TSLHGYFVFGPTGCNL</span><span class="topo-membrane">EGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAIERYV</span><span class="topo-outside">VVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAPPL</span><span class="topo-inside">VGWSRYIPEGMQCSCGIDYYTPHEETNNES</span><span class="topo-membrane">FVIYMFVVHFIIPLIVIFFCYGQLV</span><span class="topo-outside">FTVKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-outside">ATTQKAEKEVT</span><span class="topo-membrane">RMVIIMVIAFLICWLPYAGVAFY</span><span class="topo-inside">IFTHQGSDFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMMN</span><span class="topo-outside">KQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>39</td>
      <td>1</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>65</td>
      <td>40</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>68</td>
      <td>66</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>96</td>
      <td>69</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>112</td>
      <td>97</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>137</td>
      <td>113</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>150</td>
      <td>138</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>172</td>
      <td>151</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>202</td>
      <td>173</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>227</td>
      <td>203</td>
      <td>227</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>251</td>
      <td>228</td>
      <td>251</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>274</td>
      <td>252</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>288</td>
      <td>275</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>310</td>
      <td>289</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>326</td>
      <td>311</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>348</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##ncomms5801

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4pxf">4PXF</a></td>
      <td>2.75 A</td>
      <td>H32</td>
      <td>Ops* (bovine rhodopsin apoprotein, residues 1-326) in complex with ArrFL-1 peptide (residues 71-77 of rod photoreceptor arrestin: DVMGLLL)</td>
      <td>beta-D-Octylglucopyranoside (OG) in retinal-binding pocket; ArrFL-1 peptide (arrestin finger loop mimic); Palmitoyl chains; N-Acetyl-D-Glucosamine (oligosaccharides)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Vertebrate retinal rod cells (disc membrane)
- **Construct**: Native opsin apoprotein (retinal-free rhodopsin)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Ops* (150 uM in 20 mM BTP pH 7.5, 130 mM NaCl, 1 mM MgCl2, 1.25% n-octyl-beta-D-glucopyranoside) mixed with ArrFL-1 peptide (12:1 molar ratio, peptide:protein), light-activated (530 nm for 60 s)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>3.2-3.5 M (NH4)2SO4 in 0.1 M MES or sodium acetate, pH 6.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>277 K (4 C)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>12 days (crystals appeared within 7 days, grew further for 5 days)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>10-15% trehalose in crystallization buffer; crystals flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Best results obtained with ArrFL-1 peptide derived from rod photoreceptor arrestin (residues 67-77: YGQEDIDVMGLLL). Space group H32 with cell dimensions a=b=242.62 A, c=110.22 A, alpha=beta=90 degrees, gamma=120 degrees. One monomer per asymmetric unit. Data collected at ESRF ID29. Resolution 2.75 A with Rwork/Rfree = 21.7/25.1%. Over 500 crystals screened. Phases obtained by molecular replacement using Ops*-GalphaCT structure (3DQB) as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4pxf">4PXF</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">NGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTV</span><span class="topo-outside">QHKKLRTPLNY</span><span class="topo-membrane">ILLNLAVADLFMVFGGFTTTL</span><span class="topo-inside">YTSLHGYFVFGPTGCNL</span><span class="topo-membrane">EGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAI</span><span class="topo-outside">ERYVVVCKPMSNFRFGENHAI</span><span class="topo-membrane">MGVAFTWVMALACAAPPL</span><span class="topo-inside">VGWSRYIPEGMQCSCGIDYYTPHEETNNE</span><span class="topo-membrane">SFVIYMFVVHFIIPLIVIFF</span><span class="topo-outside">CYGQLVFTVKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-outside">ATTQKAEKEVTRMVI</span><span class="topo-membrane">IMVIAFLICWLPYAGVAFYIFT</span><span class="topo-inside">HQGSDFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMM</span><span class="topo-outside">NKQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>2</td>
      <td>39</td>
      <td>2</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>63</td>
      <td>40</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>74</td>
      <td>64</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>95</td>
      <td>75</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>96</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>133</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>172</td>
      <td>155</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>201</td>
      <td>173</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>221</td>
      <td>202</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>255</td>
      <td>222</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>277</td>
      <td>256</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>288</td>
      <td>278</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>309</td>
      <td>289</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>326</td>
      <td>310</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>348</td>
      <td>327</td>
      <td>348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4pxf">4PXF</a> — Chain E (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">NGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIMLGFPINFLTLYVTV</span><span class="topo-outside">QHKKLRTPLNY</span><span class="topo-membrane">ILLNLAVADLFMVFGGFTTTL</span><span class="topo-inside">YTSLHGYFVFGPTGCNL</span><span class="topo-membrane">EGFFATLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEIALWSLVVLAI</span><span class="topo-outside">ERYVVVCKPMSNFRFGENHAI</span><span class="topo-membrane">MGVAFTWVMALACAAPPL</span><span class="topo-inside">VGWSRYIPEGMQCSCGIDYYTPHEETNNE</span><span class="topo-membrane">SFVIYMFVVHFIIPLIVIFF</span><span class="topo-outside">CYGQLVFTVKEAAAQQQES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340        </span>
<span class="topo-line"><span class="topo-outside">ATTQKAEKEVTRMVI</span><span class="topo-membrane">IMVIAFLICWLPYAGVAFYIFT</span><span class="topo-inside">HQGSDFGPIFM</span><span class="topo-membrane">TIPAFFAKTSAVYNPVIYIMM</span><span class="topo-outside">NKQFRNCMVTTLCCGKN</span><span class="topo-unknown">PLGDDEASTTVSKTETSQVAPA</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>2</td>
      <td>39</td>
      <td>2</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>63</td>
      <td>40</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>74</td>
      <td>64</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>95</td>
      <td>75</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>96</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>133</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>154</td>
      <td>134</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>172</td>
      <td>155</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>201</td>
      <td>173</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>221</td>
      <td>202</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>255</td>
      <td>222</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>277</td>
      <td>256</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>288</td>
      <td>278</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>309</td>
      <td>289</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>326</td>
      <td>310</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>348</td>
      <td>327</td>
      <td>348</td>
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

### Crystal structure of Ops*–GalphaCT complex reveals G protein binding surface

The 3.2 A crystal structure of the Ops*–GalphaCT complex (PDB 3DQB) revealed how the C-terminal alpha5 helix of Galpha_t (transducin) binds to the cytoplasmic pocket of active opsin. The GalphaCT peptide (residues 340-350, sequence ILENLKDCGLF) forms an alpha_L-type C-cap motif upon receptor binding. Key interactions include hydrogen bonds between main-chain atoms of the peptide and residues in TM3, TM5, TM6, and Helix 8 of Ops*, as well as van der Waals contacts with Val230, Ala233, Thr242, Thr243, Ala246, Val138, Val139, Ala246, Val250, Leu72, Asn310, and other residues. Arg135 of the conserved E(D)RY motif interacts with the C-terminal region of the peptide. The structure shows that GalphaCT binding stabilizes the active Ops* conformation, with the nucleotide-free G protein coupled receptor state providing a crevice for Galpha binding that is absent in dark-state rhodopsin.

### First crystal structure of ligand-free opsin reveals GPCR activation mechanism

The 2.9 A structure of native opsin (PDB 3CAP) was the first crystal structure of a ligand-free GPCR, revealing the conformational changes that occur upon release of the inactivating ligand 11-cis-retinal. Key changes include: (1) breakage of the ionic lock (Arg135-Glu247 salt bridge), (2) 6-7 A outward tilt of the cytoplasmic end of TM6 with Trp265 as a pivot point, (3) elongation of TM5 by 1.5-2.5 helical turns at the cytoplasmic side, (4) rotation of Tyr306 (NPxxY motif) to face into the helix bundle, blocking TM6 from returning to the rhodopsin conformation, and (5) formation of two openings in the retinal-binding pocket between TM5-TM6 and TM1-TM7, proposed as entry and exit routes for retinal.

### Ionic lock breakage and new stabilizing interactions in opsin

In rhodopsin, a salt bridge between Arg135 (TM3, part of the E(D)RY motif) and Glu247 (TM6) together with Glu134 and Thr251 forms the ionic lock that stabilizes TM6 within the helical bundle. In opsin, this ionic lock is broken: Arg135 is released from Glu134 and Glu247 and instead engages with Tyr223 to tether TM5. Glu247 flips over to interact with Lys231 (TM5) and Thr251 (TM6) in an extended hydrogen-bonded network, stabilizing the TM5-TM6 pair at the cytoplasmic side. Glu134 repositions toward TM2 and TM4 without specific interactions.

### Retinal-binding pocket openings for ligand exchange

The ligand-free opsin structure reveals two openings in the retinal-binding pocket that are absent in rhodopsin. The first opening between TM5 and TM6 is formed by Ile205, Phe208 (TM5) and Phe273, Phe276 (TM6), resulting from small backbone movements and side-chain reorientations. This hydrophobic hole is proposed as the entry route for 11-cis-retinal during rhodopsin regeneration. The second opening between TM1 and TM7 arises from backbone alteration in TM7 and a 120-degree clockwise rotation of Phe293, with a small hole that can be sealed by rotamers of the Lys296 side chain. This opening is proposed as the exit route for all-trans-retinal after photobleaching.

### Conserved Trp265 as pivot for TM6 movement

The highly conserved Trp265 (Trp6.48) acts as a pivot point for the outward tilt of the cytoplasmic end of TM6. In the ligand-free opsin structure, Trp265 is in van der Waals contact with the space previously occupied by the beta-ionone ring of retinal, with Phe261 moving toward TM5. The indole side chain of Trp265 fills part of the space vacated by retinal. Coupled changes in the rotamer states of Trp6.48 and Phe6.52 were predicted to enable the activating outward movement of TM6. In opsin, the empty retinal-binding pocket means no rotamer change is observed for Trp265 relative to rhodopsin, but the cytoplasmic end of TM6 is already displaced outward.

### Ops* conformation stabilized by OG in ligand-binding pocket

A molecule of [OG](/xray-mp-wiki/reagents/detergents/og/) was identified in the retinal-binding pocket of the active Ops* conformation, replacing retinal and stabilizing the G-protein-interacting state. This was confirmed by the crystal structure of Ops* in complex with the synthetic G protein peptide GalphaCT2, derived from the key GPCR binding site on the C-terminal region of the G-alpha subunit.

### Structural homology between opsin and olfactory receptors

Opsin shares key features expected for olfactory receptors (ORs): a deep hydrophobic ligand-binding pocket accessible from the lipid bilayer, a hydrogen-bond network for ligand recognition, and conformational flexibility between active and inactive states. The hydrogen-bond pattern holding OG in the pocket is reminiscent of the dynamic hydrogen-bond pattern proposed for OR-odorant interactions, in which the receptor offers changing side chains for bonding.

### Detergent chain-length-dependent pocket occupancy

Various detergents ([DM](/xray-mp-wiki/reagents/detergents/dm/), OG, [NG](/xray-mp-wiki/reagents/detergents/nonylglucoside/), and [HpG](/xray-mp-wiki/reagents/detergents/heptylglucoside/)) can occupy the binding pocket in a chain-length-dependent manner, providing a model for how hydrophobic odorants enter ORs. The neopentyl glycol detergents ([LMNG](/xray-mp-wiki/reagents/detergents/lmng/), octyl glucose neopentyl glycol) showed only small inhibitory effects, suggesting they block the openings rather than entering the pocket.

### Opsin as structural template for OR homology modeling

Opsin can host various artificial hydrophobic retinal analogues, naturally occurring hydroxy analogues, and chemically distinct molecules like detergents containing multiple hydroxy groups. The Ops* structure illustrates how hydrophobic odorants, after partitioning into the membrane, can enter from the lipid bilayer into the 7TM scaffold. Ops* may serve as the best currently available structural template for homology modeling of ORs.

### Conserved solvent network in activated opsin links GPCR activation motifs

The 2.3-A resolution structure of activated opsin (PDB 4X1H) revealed an extensive water-mediated hydrogen-bonding network connecting the chromophore binding site to the G protein binding site over 35 A away. This continuous solvent network links three conserved GPCR activation motifs: the CWxP motif at the base of the chromophore binding site, the NPxxY motif at the end of Helix VII, and the (D/E)RY ionic lock motif. Three subsets of ordered solvent molecules were identified: (1) waters present in both active and ground states (structural role), (2) remodeled solvent retaining hydrogen bonding despite protein rearrangement, and (3) activation-state-specific solvent. Nonyl-glucoside (C9G) detergent molecules occupied the chromophore binding site in place of retinal, stabilizing an activated-state-like conformation.

### Ops*-ArrFL-1 structure reveals arrestin finger loop binding to active GPCR

The 2.75 A crystal structure of Ops* in complex with the ArrFL-1 peptide (PDB 4PXF, doi/10.1038##ncomms5801) reveals the structural basis for arrestin recognition of active GPCRs. The ArrFL-1 peptide (derived from residues 71-77 of rod photoreceptor arrestin finger loop, sequence DVMGLLL) binds in the same cytoplasmic crevice of the active receptor as the Gα C-terminus (GαCT), using the conserved consensus motif (E/D)x(I/L)xxxGL. The peptide adopts a reverse turn-like structure (C-cap) similar to GαCT upon binding. However, structural differences at the rim of the binding crevice reflect their divergent biological functions: G protein undergoes GDP/GTP exchange while arrestin blocks G protein access and scaffolds signaling proteins. Arg135 (E(D)RY motif) and Lys311 (NPxxY motif) form key interactions with the ArrFL-1 peptide.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/">Bovine Rhodopsin (Dark State)</a> — Same protein in dark state with 11-cis-retinal bound (PDB 1GZM); structural basis for comparison to active Ops* state
- <a href="/xray-mp-wiki/proteins/gpcr/metarhodopsin-ii/">Metarhodopsin II (Active Photointermediate)</a> — Active photointermediate of rhodopsin; opsin represents the decay product after all-trans-retinal is released
- <a href="/xray-mp-wiki/reagents/detergents/og/">Octyl Glucoside (OG)</a> — Detergent found bound in orthosteric ligand-binding pocket of Ops*, stabilizing active conformation
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent tested for reconstitution compatibility with opsin
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Lauryl Maltose Neopentyl Glycol (LMNG)</a> — Neopentyl glycol detergent family, tested for pocket access in reconstitution experiments
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Shows strong concentration-dependent inhibition of rhodopsin reconstitution, fitting best into retinal-binding pocket
- <a href="/xray-mp-wiki/reagents/detergents/nonylglucoside/">Nonylglucoside (NG)</a> — Tested for reconstitution inhibition, shows chain-length-dependent pocket occupancy; C9G occupied chromophore site in 4X1H structure
- <a href="/xray-mp-wiki/reagents/detergents/heptylglucoside/">Heptylglucoside (HpG)</a> — Tested for reconstitution inhibition, shows chain-length-dependent pocket occupancy
- <a href="/xray-mp-wiki/reagents/ligands/11-cis-retinal/">11-cis-Retinal</a> — Natural chromophore ligand of rhodopsin; replaced by OG in the Ops* crystal structure
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-g-protein-arrestin-common-interface/">GPCR G Protein-Arrestin Common Interface</a> — Ops*-ArrFL-1 structure (PDB 4PXF) reveals the common GPCR-binding interface shared by G proteins and arrestins
