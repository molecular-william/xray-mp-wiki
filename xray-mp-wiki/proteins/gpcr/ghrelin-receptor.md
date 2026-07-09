---
title: "Human Ghrelin Receptor (GHSR)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-17554-1]
verified: agent
uniprot_id: Q92847
---

# Human Ghrelin Receptor (GHSR)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q92847">UniProt: Q92847</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The human ghrelin receptor (GHSR, growth hormone secretagogue receptor) is a class A [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) that mediates the physiological effects of ghrelin, a gastric peptide hormone with important roles in appetite stimulation, growth hormone secretion, adiposity, energy homeostasis, and hippocampal neurogenesis. Ghrelin is uniquely modified by O-acyl-modification at Ser3, which is essential for its activity. The first high-resolution crystal structure of the ghrelin receptor bound to the neutral antagonist Compound 21 revealed a bifurcated ligand-binding pocket divided by a salt bridge between E124^3.33 and R283^6.55, and a hydrophobic gap (crevasse) between TM6 and TM7 rich in phenylalanine residues (F279^6.51, F286^6.58, F290^6.62, F309^7.39, F312^7.42). This gap is proposed to accommodate the acyl modification of ghrelin, explaining why acyl modification is essential for receptor activation.

## Publications

### doi/10.1038##s41467-020-17554-1

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ko5">6KO5</a></td>
      <td></td>
      <td></td>
      <td>Engineered construct: N-terminal 28 residues replaced with thermostabilized apocytochrome b562RIL (bRIL), C-terminal 20 residues deleted. Mutations: T130K (thermostability), N188Q (glycosylation site removal). Fab 7881 fragment antibody added to facilitate crystallization.</td>
      <td>Compound 21 (synthesized from YIL-781)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Baculovirus/Sf9 insect cells
- **Construct**: HA signal sequence + FLAG tag at N-terminus; HRV 3C protease site followed by eGFP and 8xHis tag at C-terminus. N-terminal 28 residues replaced with bRIL. C-terminal 20 residues deleted. Mutations: T130K, N188Q.

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
      <td>Cell harvest</td>
      <td>Sf9 insect cells infected with baculovirus at MOI 1; harvested 48 h post-infection</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Dounce homogenization in hypotonic buffer, ultracentrifugation, high salt wash</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> with <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Nickel IMAC for His-tag capture</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC for purification of receptor-Fab-Compound 21 complex</td>
      <td>—</td>
      <td></td>
      <td></td>
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
      <td>Ghrelin receptor-Fab 7881-Compound 21 complex</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein:cholesterol (10:1)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Up to 2 weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at SPring-8 BL32XU. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using orexin receptor (PDB 4S0V), <a href="/xray-mp-wiki/reagents/protein-tags/bril/">bRIL</a> (PDB 1M6T), and Fab 7881 (PDB 6KS2) as search models.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ko5">6KO5</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">A</span><span class="topo-inside">DLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKY</span><span class="topo-unknown">LSLGDELLQLF</span><span class="topo-inside">PAP</span><span class="topo-membrane">L</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">LAGVTATCVALFVVGIAGNLLTML</span><span class="topo-outside">VVSRFRELRTTTNLYL</span><span class="topo-membrane">SSMAFSDLLIFLCMPLDLVRLW</span><span class="topo-inside">QYRPWNFG</span><span class="topo-membrane">DLLCKLFQFVSESCTYAKVLTIT</span><span class="topo-outside">ALSVERYFAICFPLRAKVVVTKGRVKL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VI</span><span class="topo-membrane">FVIWAVAFCSAGPIFVLVG</span><span class="topo-inside">VEHEQGTDPWDTNECRPTEF</span><span class="topo-membrane">AVRSGLLTVMVWVSSIFFFLPVFCLT</span><span class="topo-outside">VLYSLIGRKLWRRRRGDAVVGASLRDQNHKQTVKMLAV</span><span class="topo-membrane">VVFAFILCWLPFHVG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420    </span>
<span class="topo-line"><span class="topo-membrane">RYLFSKSFE</span><span class="topo-inside">P</span><span class="topo-unknown">GSLEIAQI</span><span class="topo-inside">S</span><span class="topo-membrane">QYCNLVSFVLFYLSAAINPIL</span><span class="topo-outside">YNIMS</span><span class="topo-unknown">KKYRVAVFRLL</span><span class="topo-outside">G</span><span class="topo-unknown">FEPFSQR</span></span>
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
      <td>2</td>
      <td>105</td>
      <td>1002</td>
      <td>1105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>106</td>
      <td>1106</td>
      <td>1106</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>117</td>
      <td>119</td>
      <td>39</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>144</td>
      <td>42</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>160</td>
      <td>67</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>182</td>
      <td>83</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>190</td>
      <td>105</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>213</td>
      <td>113</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>242</td>
      <td>136</td>
      <td>164</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>261</td>
      <td>165</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>262</td>
      <td>281</td>
      <td>184</td>
      <td>203</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>307</td>
      <td>204</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>345</td>
      <td>230</td>
      <td>267</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>369</td>
      <td>268</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>370</td>
      <td>370</td>
      <td>292</td>
      <td>292</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>379</td>
      <td>301</td>
      <td>301</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>400</td>
      <td>302</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>401</td>
      <td>405</td>
      <td>323</td>
      <td>327</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>416</td>
      <td>328</td>
      <td>338</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>417</td>
      <td>417</td>
      <td>339</td>
      <td>339</td>
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

### Bifurcated ligand-binding pocket

The ghrelin receptor has a bifurcated ligand-binding pocket divided into two cavities (cavity I and cavity II) by a salt bridge between E124^3.33 and R283^6.55. This bifurcated pocket has not been observed in other solved beta-branch class A peptide hormone GPCRs. Mutagenesis of E124 or R283 completely abolished ghrelin-induced receptor function.

### Hydrophobic crevasse for acyl-modification recognition

A wide hydrophobic gap (crevasse) between TM6 and TM7 is formed by five phenylalanine residues (F279^6.51, F286^6.58, F290^6.62, F309^7.39, F312^7.42) and G282^6.54. The F279A and F312A mutations decreased Compound 21 binding and basal receptor activity. This crevasse is proposed to accommodate the acyl modification of ghrelin, explaining why acyl-modification at Ser3 is essential for receptor activation.

### Constitutive activity basis

The ghrelin receptor exhibits high constitutive (ligand-independent) activity. The aromatic amino acid cluster on TM6 and TM7, particularly the phenylalanine residues forming the crevasse, is thought to contribute to this high basal activity. The structure suggests the ghrelin receptor has properties of both peptide hormone GPCRs and lipid GPCRs.


## Cross-References

- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr/">GPCR</a> — Ghrelin receptor is a class A GPCR
