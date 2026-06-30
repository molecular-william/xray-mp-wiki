---
title: "PspR (DTG Rhodopsin from Pseudomonas putida)"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jbc.2022.101722]
verified: false
---

# PspR (DTG Rhodopsin from Pseudomonas putida)

## Overview

PspR is a light-driven outward proton-pumping microbial rhodopsin from Pseudomonas putida, belonging to the DTG/DTS rhodopsin family. Unlike other light-driven proton pumps, PspR lacks a cytoplasmic proton donor residue (Asp/Glu homologous to BR Asp96), instead using a DTG motif. The protein comprises seven transmembrane helices and is covalently bound to [retinal](/xray-mp-wiki/reagents/ligands/retinal/) via a protonated Schiff base. The 2.84 A structure reveals large hydrophilic cytoplasmic cavities that enable direct proton uptake from the cytoplasmic solvent without a specialized donor residue.

## Publications

### doi/10.1016##j.jbc.2022.101722

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7w74">7W74</a></td>
      <td>2.84 A</td>
      <td>Not specified in paper</td>
      <td>PspR (DTG rhodopsin) from Pseudomonas putida, full-length, seven transmembrane helices</td>
      <td>all-trans retinal (covalently bound via protonated Schiff base to Lys210)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli (heterologous expression)
- **Construct**: PspR from Pseudomonas putida, full-length, seven transmembrane helices, with His-tag for affinity purification

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
      <td>Cell disruption</td>
      <td>Sonication</td>
      <td>--</td>
      <td>50 mM Tris-HCl pH 8.0, 5 mM MgCl2 + --</td>
      <td>Harvested cells sonicated with Ultrasonic Homogenizer VP-300N; membrane fraction collected by ultracentrifugation at 142,000g for 1 h</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM MES-NaOH pH 6.5, 300 mM NaCl, 5 mM imidazole, 5 mM MgCl2 + 3% n-dodecyl-beta-D-maltopyranoside (DDM)</td>
      <td>Insoluble fractions removed by ultracentrifugation at 142,000g for 1 h</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Co-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>HiTrap TALON crude</td>
      <td>50 mM Tris-HCl pH 7.0, 300 mM NaCl, 300 mM imidazole, 5 mM MgCl2, 0.1% DDM + 0.1% DDM</td>
      <td>Wash with 50 mM MES-NaOH pH 6.5, 300 mM NaCl, 50 mM imidazole, 0.1% DDM; elution with 300 mM imidazole</td>
    </tr>
    <tr>
      <td>Dialysis</td>
      <td>Dialysis</td>
      <td>--</td>
      <td>20 mM Hepes-NaOH pH 7.0, 100 mM NaCl, 0.05% DDM + 0.05% DDM</td>
      <td>Dialysis to remove imidazole; final concentration 34 mg/ml protein for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>34 mg/ml PspR mixed with monoolein at 2:3 protein-to-lipid ratio (v/v)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>23 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash-cooled and stored in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Sample dispensed using Mosquito LCP robot (TTP Labtech); crystals harvested directly from LCP bolus</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7w74">7W74</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MIQT</span><span class="topo-membrane">PLLIGFIVMALASLAIYIKGAH</span><span class="topo-inside">YGPL</span><span class="topo-membrane">LGHTLIHAAVPFIAATAYLCMYL</span><span class="topo-outside">GVGNLIKVDGSVT</span><span class="topo-membrane">YLARYVDWAFTTPLLLAGVVSS</span><span class="topo-inside">AYYGTRDLYGK</span><span class="topo-membrane">SGYITAIVTLDVIMIVTGLIA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230        </span>
<span class="topo-line"><span class="topo-membrane">SL</span><span class="topo-outside">APYGV</span><span class="topo-membrane">IKWVFFAWSCAAFAGVLYLLWKPVA</span><span class="topo-inside">SIASQQPGVSPA</span><span class="topo-membrane">YRRNVGFLTVLWLIYPVVFAVG</span><span class="topo-outside">PEGFWAVSDAT</span><span class="topo-membrane">TVWVFLVLDVLAKVVYAFTSERNL</span><span class="topo-inside">RAVPV</span><span class="topo-unknown">GRGYLEHHHHHH</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>26</td>
      <td>5</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>30</td>
      <td>27</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>53</td>
      <td>31</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>66</td>
      <td>54</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>88</td>
      <td>67</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>99</td>
      <td>89</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>122</td>
      <td>100</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>127</td>
      <td>123</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>152</td>
      <td>128</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>164</td>
      <td>153</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>186</td>
      <td>165</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>197</td>
      <td>187</td>
      <td>197</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>221</td>
      <td>198</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>226</td>
      <td>222</td>
      <td>226</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>238</td>
      <td>227</td>
      <td>238</td>
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

### Absence of cytoplasmic proton donor residue

PspR lacks a cytoplasmic proton donor residue homologous to BR Asp96 (position 96 in BR corresponds to Gly84 in PspR). Instead, it has a DTG/DTS motif (Asp-Thr-Gly or Asp-Thr-Ser) important for its function. Proton directly binds from the cytoplasmic solvent to the retinal Schiff base (RSB) without a specialized donor residue. This represents a fundamentally different proton uptake mechanism compared to other light-driven proton pumps.

### Large cytoplasmic cavities enable direct proton uptake

The cytoplasmic side of TM7 (Ala212-Arg222) moves away from TM1, creating large hydrophilic cytoplasmic cavities not present in BR. These cavities increase water accessibility from the cytoplasmic milieu to the RSB region. The cytoplasmic region of the interhelical pathway consists of hydrophilic residues (His33, His37, Tyr91, Tyr213, Ser217), in contrast to the more tightly packed hydrophobic cytoplasmic region of BR. This structural rearrangement enables direct H+ transfer from cytoplasmic solvent to RSB.

### Extracellular proton release mechanism differs from BR

In BR, Glu194 and Glu204 form the proton-release group (PRG) with water molecules. In PspR, Glu204 is substituted with Thr198, and the homologous Glu188 forms a different hydrogen bond network with Arg70, Tyr71, and a water molecule. The E188A and E188Q mutants retained only 35-40% of WT pumping activity, confirming Glu188 significance in the proton release process.

### Photocycle intermediates and mutation effects

The PspR L81A mutant showed 1.9-fold higher activity than WT due to accumulation of a long-lived O-like intermediate that shortcuts the photocycle via photo-induced conversion. The Y213F mutant had similar decay of the M2 intermediate but significantly slower M2 decay, suggesting Tyr213 contributes to accelerating H+ uptake. The G84E mutant showed less pH-dependent photocycle with faster turnover at pH >= 7, as the introduced Glu partially functions as a proton donor.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — Comparison reference; archetypal proton-pumping rhodopsin with cytoplasmic donor
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid component of LCP crystallization matrix
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent for membrane solubilization and purification
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> — Chromophore covalently bound to Lys210 via protonated Schiff base
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — PspR crystallized by LCP method at 2.84 A resolution
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/">Rhodopsin Photocycle</a> — PspR photocycle intermediates (M, O, L) characterized by laser flash photolysis
