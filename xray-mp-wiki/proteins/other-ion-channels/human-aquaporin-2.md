---
title: "Human Aquaporin 2 (AQP2)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein]
sources: [doi/10.1073##pnas.1321406111, doi/10.1107##s2052252519007395]
verified: agent
uniprot_id: P41181
---

# Human Aquaporin 2 (AQP2)

<div class="expr-badges"><span class="expr-badge expr-p-pastoris">P. pastoris</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P41181">UniProt: P41181</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) 2 ([AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/)) is a water channel found in the kidney collecting duct, where it plays a key role in concentrating urine through regulated water reabsorption. [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) trafficking between intracellular storage vesicles and the apical membrane is tightly controlled by the pituitary hormone arginine vasopressin (AVP). The 2.75 A X-ray structure reveals the conserved [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) fold with six transmembrane helices and two half-membrane spanning helices, assembled as a tetramer. The C terminus displays multiple conformations, with a C-terminal alpha-helix potentially involved in protein-protein interactions governing cellular sorting. Two Cd2+-binding sites are observed within the tetramer, and Ca2+ is proposed as the physiological ligand. Defective trafficking of [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) results in [Nephrogenic Diabetes Insipidus](/xray-mp-wiki/concepts/miscellaneous/nephrogenic-diabetes-insipidus/) (NDI). An additional room-temperature SFX structure was determined at 3.7 A resolution from on-chip crystallized crystals using the Roadrunner II fixed-target system at LCLS (PDB 6qf5), demonstrating the feasibility of on-chip crystallization for membrane protein serial crystallography.


## Publications

### doi/10.1073##pnas.1321406111

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4nef">4NEF</a></td>
      <td>2.75</td>
      <td>P4_2</td>
      <td>C-terminally truncated at Pro242, expressed in Pichia pastoris</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: C-terminally truncated [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) (residues 1-242) expressed in Pichia pastoris

- **Construct**: [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) truncated at Pro242
- **Notes**: Full-length [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) produced in insect cells failed to yield well-diffracting 3D crystals. [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) at Pro242 (last visible residue in [AQP5](/xray-mp-wiki/proteins/other-ion-channels/human-aqp5/) structure) significantly improved diffraction quality.


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
      <td>Protein expression and purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>Details in SI Materials and Methods</td>
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
      <td>Truncated <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp2/">AQP2</a> (1-242)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>100 K (data collection)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Frozen crystal</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>CdCl2 used as an additive during crystallization. Complete data collected at ESRF (Grenoble, France) from a single frozen crystal. Crystals belonged to space group P42 with one tetramer in the asymmetric unit (a=119.11 A, b=119.11 A, c=90.48 A).
</td>
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
      <td>100 K</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nef">4NEF</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SELRSIAFSRA</span><span class="topo-membrane">VFAEFLATLLFVFFGLGS</span><span class="topo-outside">ALNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHINPAVTVACLV</span><span class="topo-inside">GCHVSVLRA</span><span class="topo-membrane">AFYVAAQLLGAVAGAALL</span><span class="topo-outside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LSNSTTAGQA</span><span class="topo-membrane">VTVELFLTLQLVLCIFAS</span><span class="topo-inside">TDERRGENPG</span><span class="topo-membrane">TPALSIGFSVALGHLLG</span><span class="topo-outside">IHYTGC</span><span class="topo-unknown">SMNPARSLAP</span><span class="topo-outside">AVVTGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLY</span><span class="topo-inside">NYVLFPPAKSLSERLAVLKGL</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EP</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>30</td>
      <td>13</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>42</td>
      <td>31</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>63</td>
      <td>61</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>77</td>
      <td>64</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>86</td>
      <td>78</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>130</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>131</td>
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
      <td>175</td>
      <td>159</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>181</td>
      <td>176</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>191</td>
      <td>182</td>
      <td>191</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>201</td>
      <td>192</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>240</td>
      <td>220</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>242</td>
      <td>241</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nef">4NEF</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSELR</span><span class="topo-inside">SIAFSRAV</span><span class="topo-membrane">FAEFLATLLFVFFGLGS</span><span class="topo-outside">ALNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALG</span><span class="topo-inside">HISG</span><span class="topo-unknown">AHINPAVTVACL</span><span class="topo-inside">VGCHVSVLRA</span><span class="topo-membrane">AFYVAAQLLGAVAGAALL</span><span class="topo-outside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LSNSTTAG</span><span class="topo-membrane">QAVTVELFLTLQLVLCIF</span><span class="topo-inside">ASTDERRGENPGT</span><span class="topo-membrane">PALSIGFSVALGHLLGI</span><span class="topo-outside">HYTGC</span><span class="topo-unknown">SMNPARSLAPAVV</span><span class="topo-outside">TGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLY</span><span class="topo-inside">NYVLFPPAKSLSERLAVLK</span><span class="topo-unknown">GL</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EP</span></span>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>13</td>
      <td>6</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>30</td>
      <td>14</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>42</td>
      <td>31</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>64</td>
      <td>61</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>76</td>
      <td>65</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>77</td>
      <td>86</td>
      <td>77</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>128</td>
      <td>105</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>146</td>
      <td>129</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>159</td>
      <td>147</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>176</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>181</td>
      <td>177</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>194</td>
      <td>182</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>238</td>
      <td>220</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>242</td>
      <td>239</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nef">4NEF</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSELR</span><span class="topo-inside">SIAFSRAV</span><span class="topo-membrane">FAEFLATLLFVFFGLGS</span><span class="topo-outside">ALNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALG</span><span class="topo-inside">HISG</span><span class="topo-unknown">AHINPAVTVACL</span><span class="topo-inside">VGCHVSVLRA</span><span class="topo-membrane">AFYVAAQLLGAVAGAALL</span><span class="topo-outside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LSNSTTAGQA</span><span class="topo-membrane">VTVELFLTLQLVLCIFAS</span><span class="topo-inside">TDERRGENPGTP</span><span class="topo-membrane">ALSIGFSVALGHLLGI</span><span class="topo-outside">HYTGC</span><span class="topo-unknown">SMNPARSLAPAVV</span><span class="topo-outside">TGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLY</span><span class="topo-inside">NYVLFPPAKSLSERLAVLKGL</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-inside">E</span><span class="topo-unknown">P</span></span>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>13</td>
      <td>6</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>30</td>
      <td>14</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>42</td>
      <td>31</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>64</td>
      <td>61</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>76</td>
      <td>65</td>
      <td>76</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>77</td>
      <td>86</td>
      <td>77</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>130</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>131</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>160</td>
      <td>149</td>
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
      <td>181</td>
      <td>177</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>194</td>
      <td>182</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>241</td>
      <td>220</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>242</td>
      <td>242</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4nef">4NEF</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-inside">SELRSIAFSRA</span><span class="topo-membrane">VFAEFLATLLFVFFGLGS</span><span class="topo-outside">ALNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALG</span><span class="topo-inside">HIS</span><span class="topo-unknown">GAHINPAVTVACLV</span><span class="topo-inside">GCHVSVLRA</span><span class="topo-membrane">AFYVAAQLLGAVAGAALL</span><span class="topo-outside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LSNSTTAGQA</span><span class="topo-membrane">VTVELFLTLQLVLCIFAS</span><span class="topo-inside">TDERRGENPGT</span><span class="topo-membrane">PALSIGFSVALGHLLG</span><span class="topo-outside">IHYTGC</span><span class="topo-unknown">SMNPARSLAP</span><span class="topo-outside">AVVTGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLY</span><span class="topo-inside">NYVLFPPAKSLSER</span><span class="topo-unknown">LAVLKGL</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EP</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>30</td>
      <td>13</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>42</td>
      <td>31</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>63</td>
      <td>61</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>77</td>
      <td>64</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>86</td>
      <td>78</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>130</td>
      <td>105</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>148</td>
      <td>131</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>159</td>
      <td>149</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>175</td>
      <td>160</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>181</td>
      <td>176</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>191</td>
      <td>182</td>
      <td>191</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>201</td>
      <td>192</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>233</td>
      <td>220</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>242</td>
      <td>234</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1107##s2052252519007395

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6qf5">6QF5</a></td>
      <td>3.70</td>
      <td>P4_2</td>
      <td>Full-length hAQP2 expressed in Pichia pastoris</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: C-terminally truncated [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) (residues 1-242) expressed in Pichia pastoris

- **Construct**: [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) truncated at Pro242
- **Notes**: Full-length [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) produced in insect cells failed to yield well-diffracting 3D crystals. [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) at Pro242 (last visible residue in [AQP5](/xray-mp-wiki/proteins/other-ion-channels/human-aqp5/) structure) significantly improved diffraction quality.


**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>On-chip crystallization by sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Full-length hAQP2 at 9 mg/ml in 20 mM Tris pH 8.0, 0.3 M NaCl, 0.2% OGNPG</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M Tris pH 8.5, 0.1 M NaCl, 0.1 M MgCl2, 22-25% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400 with 0.1 M CdCl2</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>298 K (room-temperature data collection)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>15 min to a few hours</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>On-chip crystallization on Roadrunner II chip. 100 ul protein-precipitant mix applied to chip, equilibrated against 5-7 ml reservoir. Excess mother liquor removed by blotting. Room-temperature SFX data collected at LCLS MFX beamline using fast-scanning goniometer at 120 images/s, 50 um step size, 25-degree tilt angle. Humidified helium stream used during data collection.
</td>
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
      <td>Variant</td>
      <td>sitting-drop</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>8.5</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>298 K</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Tris: 0.1 M [buffer]  
- Sodium Chloride: 0.1 M [salt]  
- Magnesium Chloride: 0.1 M [salt]  
- Peg 400: 22-25 % [precipitant] (PEG 400 with 0.1 M CdCl2)</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qf5">6QF5</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSEL</span><span class="topo-outside">RSIAFS</span><span class="topo-membrane">RAVFAEFLATLLFVFFGLGSA</span><span class="topo-inside">LNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALGHIS</span><span class="topo-outside">G</span><span class="topo-unknown">AHINPAVTVACLVG</span><span class="topo-outside">CHVSVL</span><span class="topo-membrane">RAAFYVAAQLLGAVAGAALL</span><span class="topo-inside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LSNSTTAG</span><span class="topo-membrane">QAVTVELFLTLQLVLCIFAST</span><span class="topo-outside">DERRGENPG</span><span class="topo-membrane">TPALSIGFSVALGHLLGI</span><span class="topo-inside">HYTG</span><span class="topo-unknown">CSMNPARSLAP</span><span class="topo-inside">AVVTGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLYNYVL</span><span class="topo-outside">FPPAKSLSE</span><span class="topo-unknown">RLAVLKGL</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EP</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>10</td>
      <td>5</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>31</td>
      <td>11</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>42</td>
      <td>32</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>63</td>
      <td>43</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>64</td>
      <td>64</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>78</td>
      <td>65</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>84</td>
      <td>79</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>104</td>
      <td>85</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>128</td>
      <td>105</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>149</td>
      <td>129</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>158</td>
      <td>150</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>176</td>
      <td>159</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>180</td>
      <td>177</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>191</td>
      <td>181</td>
      <td>191</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>201</td>
      <td>192</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>223</td>
      <td>202</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>232</td>
      <td>224</td>
      <td>232</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>242</td>
      <td>233</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qf5">6QF5</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSEL</span><span class="topo-outside">RSIAFSR</span><span class="topo-membrane">AVFAEFLATLLFVFFGLGSA</span><span class="topo-inside">LNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALGHIS</span><span class="topo-outside">G</span><span class="topo-unknown">AHINPAVTVACLV</span><span class="topo-outside">GCHVSVLR</span><span class="topo-membrane">AAFYVAAQLLGAVAGAALLHEI</span><span class="topo-inside">TPA</span><span class="topo-unknown">DIRG</span><span class="topo-inside">DLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LSNSTTAG</span><span class="topo-membrane">QAVTVELFLTLQLVLCIFAS</span><span class="topo-outside">TDERRGENPGT</span><span class="topo-membrane">PALSIGFSVALGHLLGI</span><span class="topo-inside">HYT</span><span class="topo-unknown">GCSMNPARSLAPAVV</span><span class="topo-inside">TGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLYN</span><span class="topo-outside">YVLFPPAKSLSERLAVLK</span><span class="topo-unknown">GL</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EP</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>11</td>
      <td>5</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>31</td>
      <td>12</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>42</td>
      <td>32</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>63</td>
      <td>43</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>64</td>
      <td>64</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>77</td>
      <td>65</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>85</td>
      <td>78</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>107</td>
      <td>86</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>110</td>
      <td>108</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>114</td>
      <td>111</td>
      <td>114</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>128</td>
      <td>115</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>148</td>
      <td>129</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>159</td>
      <td>149</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>176</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>179</td>
      <td>177</td>
      <td>179</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>194</td>
      <td>180</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>220</td>
      <td>202</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>238</td>
      <td>221</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>242</td>
      <td>239</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qf5">6QF5</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSEL</span><span class="topo-outside">RSIAFS</span><span class="topo-membrane">RAVFAEFLATLLFVFFGLGSA</span><span class="topo-inside">LNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALGHIS</span><span class="topo-outside">G</span><span class="topo-unknown">AHINPAVTVACLV</span><span class="topo-outside">GCHVSV</span><span class="topo-membrane">LRAAFYVAAQLLGAVAGAALL</span><span class="topo-inside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LSNSTTAG</span><span class="topo-membrane">QAVTVELFLTLQLVLCIFAST</span><span class="topo-outside">DERRGENP</span><span class="topo-membrane">GTPALSIGFSVALGHLLGI</span><span class="topo-inside">HYTG</span><span class="topo-unknown">CSMNPARSLAPAVV</span><span class="topo-inside">TGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLYNYVL</span><span class="topo-outside">FPP</span><span class="topo-unknown">AKSLSERLAVLKGL</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EP</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>10</td>
      <td>5</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>31</td>
      <td>11</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>42</td>
      <td>32</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>63</td>
      <td>43</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>64</td>
      <td>64</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>77</td>
      <td>65</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>83</td>
      <td>78</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>104</td>
      <td>84</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>128</td>
      <td>105</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>149</td>
      <td>129</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>157</td>
      <td>150</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>176</td>
      <td>158</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>180</td>
      <td>177</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>194</td>
      <td>181</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>223</td>
      <td>202</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>226</td>
      <td>224</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>242</td>
      <td>227</td>
      <td>242</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qf5">6QF5</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSELRS</span><span class="topo-outside">IAFS</span><span class="topo-membrane">RAVFAEFLATLLFVFFGLGSA</span><span class="topo-inside">LNWPQALPSVL</span><span class="topo-membrane">QIAMAFGLGIGTLVQALGHIS</span><span class="topo-outside">G</span><span class="topo-unknown">AHINPAVTVACLV</span><span class="topo-outside">GCHVSV</span><span class="topo-membrane">LRAAFYVAAQLLGAVAGAALL</span><span class="topo-inside">HEITPADIRGDLAVNA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LSNSTTAG</span><span class="topo-membrane">QAVTVELFLTLQLVLCIFAST</span><span class="topo-outside">DERRGENPG</span><span class="topo-membrane">TPALSIGFSVALGHLLGI</span><span class="topo-inside">HYTG</span><span class="topo-unknown">CSMNPARSLAPAVV</span><span class="topo-inside">TGKFDDH</span><span class="topo-membrane">WVFWIGPLVGAILGSLLY</span><span class="topo-outside">NYVLFPP</span><span class="topo-unknown">AKSLSERLAVLKGL</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">EP</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>10</td>
      <td>7</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>31</td>
      <td>11</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>42</td>
      <td>32</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>63</td>
      <td>43</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>64</td>
      <td>64</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>77</td>
      <td>65</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>83</td>
      <td>78</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>104</td>
      <td>84</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>128</td>
      <td>105</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>149</td>
      <td>129</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>158</td>
      <td>150</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>176</td>
      <td>159</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>180</td>
      <td>177</td>
      <td>180</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>194</td>
      <td>181</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>201</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>226</td>
      <td>220</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>242</td>
      <td>227</td>
      <td>242</td>
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

### C-terminal conformational variability

The C-terminal helix of [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) shows significant conformational variability
across the four protomers of the tetramer, with one protomer (D) being
highly disordered. This flexibility likely explains why full-length [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/)
failed to yield well-diffracting crystals. In protomer C, the C-terminal
helix interacts with a symmetry-related [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) molecule via leucine residues
(Leu230, 234, 237, 240), suggesting a role in protein-protein interactions
relevant to cellular sorting and LIP5-mediated trafficking.

### Cd2+ and Ca2+ binding

Two Cd2+ binding sites (Cd1 and Cd2) were identified per [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) tetramer.
Cd1 has full occupancy at the membrane interface between protomers A and D,
ligated by GluA155 and GlnD57. Cd2 has partial (65%) occupancy between loop
B and the C-terminal tail. Binding of Cd2+ influences loop D conformation
and stabilizes crystal contacts. Radioactive Ca2+ binding assays demonstrate
that AQP2-expressing oocytes bind significantly more Ca2+ than controls,
suggesting Ca2+ is the physiological ligand for these sites.

### NDI-causing mutations

The [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) structure reveals locations of mutations causing nephrogenic
diabetes insipidus (NDI). Most mutations are in transmembrane domains and
cause misfolding and ER retention. Key mutation sites include: Gln57 (Cd1
ligand), Ser148 (casein kinase II consensus site, hydrogen bonds to Gln57),
Thr125/Thr126 in loop C near the N-glycosylation site Asn123, and Asp150
in loop D which mediates interactions between loop D and the C-terminal
tail via Arg152.

### LIP5 interaction site

The LIP5 binding site on [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) has been mapped to residues 230-243 within
the C-terminal helix. Leucines 230, 234, 237, and 240 align on the same
side of the helix, creating a leucine-rich region. This is similar to the
AQP0-Calmodulin interaction motif, suggesting exposed hydrophobic residues
on [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) C-terminal helices may be a recurring motif for protein-
protein interactions involved in trafficking.


## Cross-References

- <a href="/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-4/">Human Aquaporin 4 (hAQP4)</a> — Related mammalian aquaporin for structural comparison
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aquaporin-z/">Aquaporin Z (AqpZ)</a> — Bacterial aquaporin homolog for comparative analysis
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp0/">Aquaporin 0 (AQP0)</a> — AQP0-Calmodulin interaction provides comparative model for C-terminal helix interactions
- <a href="/xray-mp-wiki/methods/crystallization/on-chip-crystallization/">On-Chip Crystallization</a> — Method used to obtain the 3.7 A room-temperature SFX structure (PDB 6qf5)
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin Family</a> — Related biological concept
- <a href="/xray-mp-wiki/concepts/miscellaneous/nephrogenic-diabetes-insipidus/">Nephrogenic Diabetes Insipidus</a> — Related biological concept
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp2/">AQP2</a> — Related protein structure
