---
title: "Ci-VSD Voltage-Sensing Domain"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2768]
verified: agent
uniprot_id: F6XHE4
---

# Ci-VSD Voltage-Sensing Domain

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/F6XHE4">UniProt: F6XHE4</a>

<span class="expr-badge">Ciona intestinalis</span>

## Overview

Ci-VSD is the isolated voltage-sensing domain from the Ciona intestinalis voltage-sensing phosphatase (Ci-VSP). It contains the S1-S4 transmembrane segments that form the voltage-sensing module responsible for detecting changes in membrane potential. Crystal structures of both wild-type Ci-VSD (3.6 A) and the R217E mutant (2.5 A) reveal the structural basis of voltage-dependent gating, including the rotameric reorientation of gating arginine residues. The structures were refined using extended Molecular Dynamics Flexible Fitting (xMDFF), a method that integrates X-ray crystallography with molecular dynamics simulations to improve low-resolution structures. Ci-VSD was co-crystallized with Fab fragments and contains [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) detergent molecules at the S3-S4 loop region.


## Publications

### doi/10.1038##nsmb.2768

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4g7v">4G7V</a></td>
      <td>2.5</td>
      <td>P6_5 2 2</td>
      <td>Ci-VSD R217E mutant in complex with Fab fragment 33F12_4, 12 complexes (6 homodimers) in unit cell</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> (3 molecules), succinic acid (1 molecule)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4g7v">4G7V</a></td>
      <td>3.6</td>
      <td>P1</td>
      <td>Ci-VSD wild-type (residues 1-260) in complex with Fab fragment 39D10_18, 4 complexes (2 dimers) per asymmetric unit</td>
      <td>none (apo structure)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Ci-VSD (residues 1-260) from Ciona intestinalis, expressed with Fab co-expression for crystallization

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
      <td>Complex purification</td>
      <td>Co-purification with Fab fragments</td>
      <td>Not specified</td>
      <td>Not specified + <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
      <td>Ci-VSD co-expressed and co-purified with Fab fragments 33F12_4 (R217E) or 39D10_18 (WT)</td>
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
      <td>Notes</td>
      <td>Ci-VSD R217E+33F12_4 complex crystallized in space group P6_5 2 2 at 2.5 A resolution. Ci-VSD WT+39D10_18 complex crystallized in space group P1 at 3.6 A resolution with 4 complexes per asymmetric unit. <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> detergent molecules and succinic acid resolved around the S3-S4 loop region of the R217E structure.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4g7v">4G7V</a> — Chain S (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGVDDGRMEIPTT</span><span class="topo-outside">GVGR</span><span class="topo-unknown">VQFRVRAVI</span><span class="topo-outside">DHLGMRV</span><span class="topo-membrane">FGVFLIFLDIILMIIDLS</span><span class="topo-inside">LPGKSESSQS</span><span class="topo-membrane">FYDGMALALSCYFMLDLGL</span><span class="topo-outside">RIFAYGPKNFFTNPW</span><span class="topo-membrane">EVADGLIIVVTFVVTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180     </span>
<span class="topo-line"><span class="topo-membrane">FYTVLD</span><span class="topo-inside">EYVQE</span><span class="topo-membrane">TGADGLGELVVLARLLRVVRLARIF</span><span class="topo-outside">YS</span><span class="topo-unknown">HQQMKASSRRTISQNKRRYRKDGFKLN</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>22</td>
      <td>79</td>
      <td>100</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>26</td>
      <td>101</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>35</td>
      <td>105</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>42</td>
      <td>114</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>70</td>
      <td>139</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>89</td>
      <td>149</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>104</td>
      <td>168</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>126</td>
      <td>183</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>131</td>
      <td>205</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>156</td>
      <td>210</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>157</td>
      <td>158</td>
      <td>235</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>185</td>
      <td>237</td>
      <td>263</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4g7v">4G7V</a> — Chain S (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHGVDDGRMEIPTT</span><span class="topo-outside">GVGR</span><span class="topo-unknown">VQFRVRAVI</span><span class="topo-outside">DHLGMRV</span><span class="topo-membrane">FGVFLIFLDIILMIIDLS</span><span class="topo-inside">LPGKSESSQS</span><span class="topo-membrane">FYDGMALALSCYFMLDLGL</span><span class="topo-outside">RIFAYGPKNFFTNPW</span><span class="topo-membrane">EVADGLIIVVTFVVTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180     </span>
<span class="topo-line"><span class="topo-membrane">FYTVLD</span><span class="topo-inside">EYVQE</span><span class="topo-membrane">TGADGLGELVVLARLLRVVRLARIF</span><span class="topo-outside">YS</span><span class="topo-unknown">HQQMKASSRRTISQNKRRYRKDGFKLN</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>22</td>
      <td>79</td>
      <td>100</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>26</td>
      <td>101</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>35</td>
      <td>105</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>42</td>
      <td>114</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>70</td>
      <td>139</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>89</td>
      <td>149</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>104</td>
      <td>168</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>126</td>
      <td>183</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>131</td>
      <td>205</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>156</td>
      <td>210</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>157</td>
      <td>158</td>
      <td>235</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>185</td>
      <td>237</td>
      <td>263</td>
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

### Gating arginine rotameric reorientation

The four gating arginine residues (R223, R226, R229, R232) in Ci-VSD show a distinct span of rotamer orientations. R229 lies horizontally inside the hydrophobic gasket, separating the intracellular and extracellular sides electrically. R223 and R226 point straight up above the electric field, while R232 points down below the electrical field. This rotameric reorientation mechanism is also observed in other VSDs ([KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/), Kv1.2-2.1 chimera, NavAb) and may be an additional contributor to total gating charge translocation in VSDs.

### xMDFF refinement methodology

Extended Molecular Dynamics Flexible Fitting (xMDFF) was developed as a method to iteratively refine atomic models into low-resolution electron density maps. The method cycles between X-ray crystallography refinement (using PHENIX) and MDFF fitting, using steering forces derived from the X-ray electron density. xMDFF was benchmarked on six low-resolution X-ray structures (4-4.5 A resolution: 1AV1, 1YE1, 1JL4, 1AOS, 1XDV, 1Y15) and showed significant improvements in R-free values, MolProbity scores, and Ramachandran favored conformations.

### S4 helix conformation and gating model

The S4 helix in the Ci-VSD WT structure is well resolved, including the gating arginines and the S4-phosphatase linker. The electron density supports the conformation observed rather than a hypothetical "two-click down" model (shifting S4 3 residues downward) or an "up-conformation" model (shifting S4 upward). The S3-S4 loop length and linker density are consistent with the resting/down conformation of the voltage sensor.

### Hydrophobic gasket and counter-charge interactions

The hydrophobic gasket residues and counter-charge residues (E205, F199) form a conserved interaction network around the gating arginines. F199 and Y200 are part of the hydrophobic constriction site that separates intracellular and extracellular compartments in the voltage sensor.


## Cross-References

- <a href="/xray-mp-wiki/concepts/construct-design/voltage-sensor-paddle/">Voltage-Sensor Paddle</a> — Ci-VSD contains the conserved voltage-sensor paddle motif (S3b-S4)
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kvap/">KvAP Voltage-Dependent Potassium Channel</a> — KvAP voltage sensor compared to Ci-VSD for rotamer analysis
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/navab/">NavAb Bacterial Voltage-Gated Sodium Channel</a> — NavAb structure compared to Ci-VSD for gating charge translocation
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kvap/">KvAP Voltage-Dependent Potassium Channel</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/navab/">NavAb Bacterial Voltage-Gated Sodium Channel</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/pumps-atpases/ribu/">RibU (ECF-Type Riboflavin Transporter S Component from Staphylococcus aureus)</a> — Related protein structure
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Method used in the study
- <a href="/xray-mp-wiki/concepts/construct-design/voltage-sensor-paddle/">Voltage-Sensor Paddle</a> — Related concept
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">Lauryldimethylamine N-oxide (LDAO)</a> — Reagent used in the study
