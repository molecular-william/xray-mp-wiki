---
title: "C. elegans TRIC-B2 Channel"
created: 2026-06-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature19767]
verified: false
---

# C. elegans TRIC-B2 Channel

## Overview

TRIC-B2 is an intracellular cation channel from Caenorhabditis elegans belonging to the Trimeric Intracellular Cation (TRIC) channel family. It forms a symmetrical homotrimeric complex with endogenous phosphatidylinositol-4,5-biphosphate ([PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/)) lipid molecules. Each monomer contains seven transmembrane helices (M1-7) with a 3+3+1 organization pattern and an hourglass-shaped hydrophilic pore. TRIC-B2 shares 57% sequence identity with [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/) and 34% identity with human TRIC-B. It was solved in the Ca2+-free state at 2.3 A resolution, providing a structural basis for understanding Ca2+-induced conformational changes when compared with the Ca2+-bound [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/) structure.


## Publications

### doi/10.1038##nature19767

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5eik">5EIK</a></td>
      <td>2.3 A</td>
      <td>R32</td>
      <td>CeTRIC-B2 (residues 1-252), C. elegans, Myc and 6His tags removed</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a> (phosphatidylinositol-4,5-biphosphate), Ca2+-free state</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5eik">5EIK</a></td>
      <td>2.3 A</td>
      <td>R32</td>
      <td>CeTRIC-B2 (residues 1-252), C. elegans</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> crystallization condition</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: Gene encoding TRIC-B2 from C. elegans (UniProt: Q9NA73) was synthesized with optimized codon usage for expression in Pichia pastoris. Target cDNA was inserted between EcoRI/XhoI sites of pPICZ-C vector with C-terminal fusion of c-Myc epitope and 6His tag. For crystallization, 61 amino acid residues at the flexible C-terminal region plus the Myc epitope were truncated, yielding residues 1-252 covering the transmembrane domain. Expression vectors linearized with PmeI and transformed into P. pastoris GS115 strain by electroporation.


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
      <td>High-pressure homogenization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> (pH 8.0), 150 mM KCl + --</td>
      <td>Frozen cell pellets suspended 1:10 (m:v), homogenized with T10 basic homogenizer, passed through high-pressure homogenizer at 1300 bar, 4 times</td>
    </tr>
    <tr>
      <td>Membrane collection and solubilization</td>
      <td>Centrifugation and detergent solubilization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> (pH 8.0), 150 mM KCl + Triton X-100 (1.5% v/v final concentration)</td>
      <td>Cell lysate stirred at room temperature for 2 h, insoluble debris removed by centrifugation at 37044g for 1 h</td>
    </tr>
    <tr>
      <td>Cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> cobalt affinity beads (BD Science), 1 ml resin/30 g cell pellet</td>
      <td>150 mM KCl, 25 mM HEPES (pH 7.5), 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.5% beta-DM + 0.5% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (beta-DM, Anatrace)</td>
      <td>Pre-equilibrated resin, 1-h incubation at room temperature, washed with 5 column volumes of buffer A (150 mM KCl, 25 mM HEPES pH 7.5)</td>
    </tr>
    <tr>
      <td>Elution</td>
      <td>Affinity elution</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> beads</td>
      <td>150 mM KCl, 25 mM HEPES (pH 7.5), <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient + 0.5% beta-DM</td>
      <td>Elution via <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient</td>
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
      <td>CeTRIC-B2 (residues 1-252) in beta-DM with endogenous <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Ca2+-free state (no CaCl2 added)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Space group R32, cell dimensions a=b=126.34 A, c=135.57 A. Wavelength 1.5306 A, resolution 43-2.3 A (shell 2.38-2.3), Rmerge 11.6% (73.0%), Rpim 5.9% (36.6%), I/sigmaI 8.6 (2.0), completeness 99.2% (99.4%), redundancy 5.4. The structure was solved in the Ca2+-free state, providing a structural baseline for comparison with the Ca2+-bound <a href="/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/">C. elegans TRIC-B1 Channel</a> structure. Mass spectrometry confirmed the presence of multiple <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/">PIP2</a> species (34:0, 34:1, 34:2, 34:3, 36:1, 36:2, 36:3, 36:8) in the purified protein sample.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5eik">5EIK</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGWVPDEWS</span><span class="topo-outside">I</span><span class="topo-unknown">DHDTLIDAGGYVQK</span><span class="topo-outside">LKLYP</span><span class="topo-membrane">YFDAAHYVLTCLSVRHDL</span><span class="topo-inside">GPDAISF</span><span class="topo-membrane">SRKHPF</span></span>
<span class="topo-line"><span class="topo-membrane">SCWLSCMLMSFAGSFLS</span><span class="topo-outside">CFLLGEPIISPLKQHADI</span><span class="topo-membrane">LLGSIVWYLVFYSPFD</span><span class="topo-inside">V</span><span class="topo-membrane">VFRLATWF</span></span>
<span class="topo-line"><span class="topo-membrane">PVKLGLSVLKEVQRT</span><span class="topo-outside">HKIAAGVKHAVRIYPESYLVQI</span><span class="topo-membrane">LVGVAKGAGSGVVKIVEQLARG</span><span class="topo-inside">T</span></span>
<span class="topo-line"><span class="topo-inside">WHPTNHEILRP</span><span class="topo-membrane">SFTTKACVIASIV</span><span class="topo-outside">FTLERHSMYVTAPHDLVYL</span><span class="topo-membrane">CVVGFFIYFKLASL</span><span class="topo-inside">CLS</span></span>
<span class="topo-line"><span class="topo-inside">VHD</span><span class="topo-unknown">VLMPIENVLHHHHHH</span></span>
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
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>11</td>
      <td>24</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>47</td>
      <td>30</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>54</td>
      <td>48</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>77</td>
      <td>55</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>95</td>
      <td>78</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>111</td>
      <td>96</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>135</td>
      <td>113</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>157</td>
      <td>136</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>179</td>
      <td>158</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>191</td>
      <td>180</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>204</td>
      <td>192</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>223</td>
      <td>205</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>237</td>
      <td>224</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>243</td>
      <td>238</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5eik">5EIK</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGWVPDEWS</span><span class="topo-outside">I</span><span class="topo-unknown">DHDTLIDAGGYVQK</span><span class="topo-outside">LKLYP</span><span class="topo-membrane">YFDAAHYVLTCLSVRHDL</span><span class="topo-inside">GPDAISF</span><span class="topo-membrane">SRKHPF</span></span>
<span class="topo-line"><span class="topo-membrane">SCWLSCMLMSFAGSFLS</span><span class="topo-outside">CFLLGEPIISPLKQHADI</span><span class="topo-membrane">LLGSIVWYLVFYSPFD</span><span class="topo-inside">V</span><span class="topo-membrane">VFRLATWF</span></span>
<span class="topo-line"><span class="topo-membrane">PVKLGLSVLKEVQRT</span><span class="topo-outside">HKIAAGVKHAVRIYPESYLVQI</span><span class="topo-membrane">LVGVAKGAGSGVVKIVEQLARG</span><span class="topo-inside">T</span></span>
<span class="topo-line"><span class="topo-inside">WHPTNHEILRP</span><span class="topo-membrane">SFTTKACVIASIV</span><span class="topo-outside">FTLERHSMYVTAPHDLVYL</span><span class="topo-membrane">CVVGFFIYFKLASL</span><span class="topo-inside">CLS</span></span>
<span class="topo-line"><span class="topo-inside">VHD</span><span class="topo-unknown">VLMPIENVLHHHHHH</span></span>
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
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>11</td>
      <td>24</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>47</td>
      <td>30</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>54</td>
      <td>48</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>77</td>
      <td>55</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>95</td>
      <td>78</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>111</td>
      <td>96</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>135</td>
      <td>113</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>157</td>
      <td>136</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>179</td>
      <td>158</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>191</td>
      <td>180</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>204</td>
      <td>192</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>223</td>
      <td>205</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>237</td>
      <td>224</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>243</td>
      <td>238</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5eik">5EIK</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGWVPDEWS</span><span class="topo-outside">I</span><span class="topo-unknown">DHDTLIDAGGYVQK</span><span class="topo-outside">LKLYP</span><span class="topo-membrane">YFDAAHYVLTCLSVRHDL</span><span class="topo-inside">GPDAISF</span><span class="topo-membrane">SRKHPF</span></span>
<span class="topo-line"><span class="topo-membrane">SCWLSCMLMSFAGSFLS</span><span class="topo-outside">CFLLGEPIISPLKQHADI</span><span class="topo-membrane">LLGSIVWYLVFYSPFD</span><span class="topo-inside">V</span><span class="topo-membrane">VFRLATWF</span></span>
<span class="topo-line"><span class="topo-membrane">PVKLGLSVLKEVQRT</span><span class="topo-outside">HKIAAGVKHAVRIYPESYLVQI</span><span class="topo-membrane">LVGVAKGAGSGVVKIVEQLARG</span><span class="topo-inside">T</span></span>
<span class="topo-line"><span class="topo-inside">WHPTNHEILRP</span><span class="topo-membrane">SFTTKACVIASIV</span><span class="topo-outside">FTLERHSMYVTAPHDLVYL</span><span class="topo-membrane">CVVGFFIYFKLASL</span><span class="topo-inside">CLS</span></span>
<span class="topo-line"><span class="topo-inside">VHD</span><span class="topo-unknown">VLMPIENVLHHHHHH</span></span>
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
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>11</td>
      <td>24</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>47</td>
      <td>30</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>54</td>
      <td>48</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>77</td>
      <td>55</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>95</td>
      <td>78</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>111</td>
      <td>96</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>135</td>
      <td>113</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>157</td>
      <td>136</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>179</td>
      <td>158</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>191</td>
      <td>180</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>204</td>
      <td>192</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>223</td>
      <td>205</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>237</td>
      <td>224</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>243</td>
      <td>238</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5eik">5EIK</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGWVPDEWS</span><span class="topo-outside">I</span><span class="topo-unknown">DHDTLIDAGGYVQK</span><span class="topo-outside">LKLYP</span><span class="topo-membrane">YFDAAHYVLTCLSVRHDL</span><span class="topo-inside">GPDAISF</span><span class="topo-membrane">SRKHPF</span></span>
<span class="topo-line"><span class="topo-membrane">SCWLSCMLMSFAGSFLS</span><span class="topo-outside">CFLLGEPIISPLKQHADI</span><span class="topo-membrane">LLGSIVWYLVFYSPFD</span><span class="topo-inside">V</span><span class="topo-membrane">VFRLATWF</span></span>
<span class="topo-line"><span class="topo-membrane">PVKLGLSVLKEVQRT</span><span class="topo-outside">HKIAAGVKHAVRIYPESYLVQI</span><span class="topo-membrane">LVGVAKGAGSGVVKIVEQLARG</span><span class="topo-inside">T</span></span>
<span class="topo-line"><span class="topo-inside">WHPTNHEILRP</span><span class="topo-membrane">SFTTKACVIASIV</span><span class="topo-outside">FTLERHSMYVTAPHDLVYL</span><span class="topo-membrane">CVVGFFIYFKLASL</span><span class="topo-inside">CLS</span></span>
<span class="topo-line"><span class="topo-inside">VHD</span><span class="topo-unknown">VLMPIENVLHHHHHH</span></span>
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
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>11</td>
      <td>24</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>47</td>
      <td>30</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>54</td>
      <td>48</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>77</td>
      <td>55</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>95</td>
      <td>78</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>111</td>
      <td>96</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>135</td>
      <td>113</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>157</td>
      <td>136</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>179</td>
      <td>158</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>191</td>
      <td>180</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>204</td>
      <td>192</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>223</td>
      <td>205</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>237</td>
      <td>224</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>243</td>
      <td>238</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5eik">5EIK</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGWVPDEWS</span><span class="topo-outside">I</span><span class="topo-unknown">DHDTLIDAGGYVQK</span><span class="topo-outside">LKLYP</span><span class="topo-membrane">YFDAAHYVLTCLSVRHDL</span><span class="topo-inside">GPDAISF</span><span class="topo-membrane">SRKHPF</span></span>
<span class="topo-line"><span class="topo-membrane">SCWLSCMLMSFAGSFLS</span><span class="topo-outside">CFLLGEPIISPLKQHADI</span><span class="topo-membrane">LLGSIVWYLVFYSPFD</span><span class="topo-inside">V</span><span class="topo-membrane">VFRLATWF</span></span>
<span class="topo-line"><span class="topo-membrane">PVKLGLSVLKEVQRT</span><span class="topo-outside">HKIAAGVKHAVRIYPESYLVQI</span><span class="topo-membrane">LVGVAKGAGSGVVKIVEQLARG</span><span class="topo-inside">T</span></span>
<span class="topo-line"><span class="topo-inside">WHPTNHEILRP</span><span class="topo-membrane">SFTTKACVIASIV</span><span class="topo-outside">FTLERHSMYVTAPHDLVYL</span><span class="topo-membrane">CVVGFFIYFKLASL</span><span class="topo-inside">CLS</span></span>
<span class="topo-line"><span class="topo-inside">VHD</span><span class="topo-unknown">VLMPIENVLHHHHHH</span></span>
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
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>11</td>
      <td>24</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>47</td>
      <td>30</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>54</td>
      <td>48</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>77</td>
      <td>55</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>95</td>
      <td>78</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>111</td>
      <td>96</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>135</td>
      <td>113</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>157</td>
      <td>136</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>179</td>
      <td>158</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>191</td>
      <td>180</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>204</td>
      <td>192</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>223</td>
      <td>205</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>237</td>
      <td>224</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>243</td>
      <td>238</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5eik">5EIK</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGWVPDEWS</span><span class="topo-outside">I</span><span class="topo-unknown">DHDTLIDAGGYVQK</span><span class="topo-outside">LKLYP</span><span class="topo-membrane">YFDAAHYVLTCLSVRHDL</span><span class="topo-inside">GPDAISF</span><span class="topo-membrane">SRKHPF</span></span>
<span class="topo-line"><span class="topo-membrane">SCWLSCMLMSFAGSFLS</span><span class="topo-outside">CFLLGEPIISPLKQHADI</span><span class="topo-membrane">LLGSIVWYLVFYSPFD</span><span class="topo-inside">V</span><span class="topo-membrane">VFRLATWF</span></span>
<span class="topo-line"><span class="topo-membrane">PVKLGLSVLKEVQRT</span><span class="topo-outside">HKIAAGVKHAVRIYPESYLVQI</span><span class="topo-membrane">LVGVAKGAGSGVVKIVEQLARG</span><span class="topo-inside">T</span></span>
<span class="topo-line"><span class="topo-inside">WHPTNHEILRP</span><span class="topo-membrane">SFTTKACVIASIV</span><span class="topo-outside">FTLERHSMYVTAPHDLVYL</span><span class="topo-membrane">CVVGFFIYFKLASL</span><span class="topo-inside">CLS</span></span>
<span class="topo-line"><span class="topo-inside">VHD</span><span class="topo-unknown">VLMPIENVLHHHHHH</span></span>
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
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>11</td>
      <td>24</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>47</td>
      <td>30</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>54</td>
      <td>48</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>77</td>
      <td>55</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>95</td>
      <td>78</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>111</td>
      <td>96</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>135</td>
      <td>113</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>157</td>
      <td>136</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>179</td>
      <td>158</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>191</td>
      <td>180</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>204</td>
      <td>192</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>223</td>
      <td>205</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>237</td>
      <td>224</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>243</td>
      <td>238</td>
      <td>243</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Ca2+-free structure reveals open cytoplasmic vestibule

The Ca2+-free TRIC-B2 structure (2.3 A) reveals the conformation of the cytoplasmic vestibule and M5-6 loop in the absence of calcium binding. The M5-6 loop in TRIC-B2 adopts a different conformation compared to the Ca2+-bound [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/) structure, with the His186-Asp50 pair (TRIC-B2) versus Asn185-Ala49 pair ([C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/)) at the monomer interface. Superposition of TRIC-B2 on [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/) reveals dramatic conformational differences, particularly in the M5-6 loop region which swings towards the pore upon Ca2+ binding. The [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) head group is more accessible in the Ca2+-free state.

### Structural comparison with TRIC-B1 reveals gating mechanism

[C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/) and TRIC-B2 share similar overall structures with RMSD of C-alpha atoms at 1.1 A. However, key differences in the M5-6 loop and cytoplasmic vestibule regions reveal the Ca2+-dependent gating mechanism. In TRIC-B2, the Ca2+ binding site at the trimeric center is unoccupied, and the Trp180 residues (Ser70 at the M5 kink position) adopt a different conformation. The Ca2+-free structure provides the baseline conformation for the proposed three-state gating model.

### PIP2 binding in the Ca2+-free state

Mass spectrometry analysis confirmed that the TRIC-B2 protein sample contains multiple [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) species (34:0, 34:1, 34:2, 34:3, 36:1, 36:2, 36:3, 36:8). In the Ca2+-free state, [PIP2](/xray-mp-wiki/reagents/lipids/phosphatidylinositol-4-5-bisphosphate/) binds to the same site as in [C. elegans TRIC-B1 Channel](/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/), with its head group located on the surface of the cytoplasmic vestibule of the pore. The PIP2-binding residues are highly conserved among TRIC-A and TRIC-B homologues from various species including Homo sapiens, Mus musculus, Gallus gallus, Danio rerio, Xenopus tropicalis, and Caenorhabditis elegans.


## Cross-References

- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol/">Phosphatidylinositol</a> — PIP2 is a phosphorylated derivative of phosphatidylinositol; mass spectrometry confirmed multiple PIP2 species in TRIC-B2 sample
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Primary detergent (beta-DM, 0.5%) used throughout purification and crystallization of TRIC-B2
- <a href="/xray-mp-wiki/reagents/detergents/triton-x-100/">Triton X-100</a> — Used at 1.5% for solubilization of membrane proteins from P. pastoris cell lysate
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> — Buffer component (25 mM, pH 7.5) used in purification buffers
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/tric-b1/">C. elegans TRIC-B1 Channel</a> — Ca2+-bound counterpart (3.3 A); structural superposition reveals Ca2+-induced gating mechanism
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA Potassium Channel</a> — Structural comparison with canonical tetrameric K+ channel (KcsA, PDB 1BL8) highlights unique TRIC architecture
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kirbac-potassium-channels/">KirBac Potassium Channels</a> — Homologous prokaryotic potassium channel; PIP2 binding compared with Kir2.2 channel
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> — Buffer component (50 mM, pH 8.0) used in cell lysis buffer
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/">Allosteric Regulation in Membrane Proteins</a> — Ca2+-induced conformational change in M5-6 loop allosterically affects pore gating via PIP2 interaction
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
