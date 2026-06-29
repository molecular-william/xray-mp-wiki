---
title: "sCtr1 (High-Affinity Copper Transporter from Salmo salar)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-09376-7]
verified: false
---

# sCtr1 (High-Affinity Copper Transporter from Salmo salar)

## Overview

Ctr1 is the evolutionarily conserved high-affinity Cu⁺ transporter crucial for dietary copper uptake and peripheral distribution. The X-ray crystal structures of Salmo salar Ctr1 (sCtr1) were determined in both Cu⁺-free and Cu⁺-bound states, revealing a homo-trimeric Cu⁺-selective ion channel-like architecture. Two layers of methionine triads (M146 and M150 in TM2) form a selectivity filter at the extracellular entrance, coordinating two bound Cu⁺ ions. A Zn²⁺ binding site comprised of E80 (TM1) and H135 (TM2) was also identified, with mutations at these positions increasing Cu⁺ transport rate. The C-terminal HCH motif potentially forms an intracellular gate.


## Publications

### doi/10.1038##s41467-019-09376-7

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6m97">6M97</a></td>
      <td>3.0</td>
      <td>H32</td>
      <td>sCtr1_cryst (ΔN40, BRIL insertion)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6m97">6M97</a></td>
      <td>3.2</td>
      <td>H32</td>
      <td>sCtr1_cryst</td>
      <td>Cu⁺</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Pichia pastoris](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/) SMD1163H
- **Construct**: sCtr1_cryst (N-terminal 40 residues deleted, intracellular loop 94–120 replaced by BRIL)

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
      <td>Ball milling (Retsch MM400)</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 8.0, 150 mM NaCl, protease inhibitors</td>
      <td></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 8.0, 150 mM NaCl + 2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a></td>
      <td>3 h at 4 °C</td>
    </tr>
    <tr>
      <td>Cobalt affinity chromatography</td>
      <td>Immobilized metal-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Cobalt resin (Clontech)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 8.0, 150 mM NaCl, 30 mM imidazole, 4 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a></td>
      <td>C-terminal GFP tag removed by PreScission protease overnight at 4 °C</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td>Superose 6 (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 8.0, 150 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">Dithiothreitol (DTT)</a>, 5 mM CYMAL-5</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, hanging drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>~7 mg/ml sCtr1_cryst</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>26% <a href="/xray-mp-wiki/reagents/additives/peg-400/">Polyethylene Glycol 400 (PEG 400)</a>, 50 mM Zn(OAc)₂, 50 mM <a href="/xray-mp-wiki/reagents/buffers/cacodylate/">Sodium Cacodylate</a> pH 5.9</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 °C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared in 2 days, grew to full size within 2 weeks. Space group H32.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6m97">6M97</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MTFYFGYTNVELLFASLVINTPGEMV</span><span class="topo-membrane">AACFGCFLLAVLYEGLKIGREFLLR</span><span class="topo-inside">RN</span><span class="topo-unknown">A</span><span class="topo-inside">DLEDNW</span></span>
<span class="topo-line"><span class="topo-inside">ETLNDNLKVIE</span><span class="topo-unknown">KADN</span><span class="topo-inside">AAQVKDALTKMRAAALDAQKATPPK</span><span class="topo-unknown">LEDKSPD</span><span class="topo-inside">SPEMKDFRHGFDI</span></span>
<span class="topo-line"><span class="topo-inside">LVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQK</span><span class="topo-unknown">YL</span><span class="topo-inside">QRMLS</span><span class="topo-membrane">MAHLLQTVLHVIQVVV</span></span>
<span class="topo-line"><span class="topo-membrane">SYFLMLVFM</span><span class="topo-outside">TYNA</span><span class="topo-membrane">YLCMAVAAGAGLGYFLFSWKKAV</span><span class="topo-inside">VVDIT</span><span class="topo-unknown">EHCHSNSLEVLFQ</span></span>
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
      <td>26</td>
      <td>41</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>51</td>
      <td>67</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>53</td>
      <td>92</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>71</td>
      <td>1002</td>
      <td>1018</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>100</td>
      <td>1023</td>
      <td>1047</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>157</td>
      <td>1055</td>
      <td>1104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>158</td>
      <td>1105</td>
      <td>1105</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>160</td>
      <td>164</td>
      <td>121</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>126</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>193</td>
      <td>151</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>216</td>
      <td>155</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>221</td>
      <td>178</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6m97">6M97</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MTFYFGYTNVELLFASLVINTPGEMV</span><span class="topo-membrane">AACFGCFLLAVLYEGLKIGREFLLR</span><span class="topo-inside">RN</span><span class="topo-unknown">A</span><span class="topo-inside">DLEDNW</span></span>
<span class="topo-line"><span class="topo-inside">ETLNDNLKVIE</span><span class="topo-unknown">KADN</span><span class="topo-inside">AAQVKDALTKMRAAALDAQKATPPK</span><span class="topo-unknown">LEDKSPD</span><span class="topo-inside">SPEMKDFRHGFDI</span></span>
<span class="topo-line"><span class="topo-inside">LVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQK</span><span class="topo-unknown">YL</span><span class="topo-inside">QRMLS</span><span class="topo-membrane">MAHLLQTVLHVIQVVV</span></span>
<span class="topo-line"><span class="topo-membrane">SYFLMLVFM</span><span class="topo-outside">TYNA</span><span class="topo-membrane">YLCMAVAAGAGLGYFLFSWKKAV</span><span class="topo-inside">VVDIT</span><span class="topo-unknown">EHCHSNSLEVLFQ</span></span>
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
      <td>26</td>
      <td>41</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>51</td>
      <td>67</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>53</td>
      <td>92</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>71</td>
      <td>1002</td>
      <td>1018</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>100</td>
      <td>1023</td>
      <td>1047</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>157</td>
      <td>1055</td>
      <td>1104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>158</td>
      <td>1105</td>
      <td>1105</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>160</td>
      <td>164</td>
      <td>121</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>126</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>193</td>
      <td>151</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>216</td>
      <td>155</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>221</td>
      <td>178</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6m97">6M97</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MTFYFGYTNVELLFASLVINTPGEMV</span><span class="topo-membrane">AACFGCFLLAVLYEGLKIGREFLLR</span><span class="topo-inside">RN</span><span class="topo-unknown">A</span><span class="topo-inside">DLEDNW</span></span>
<span class="topo-line"><span class="topo-inside">ETLNDNLKVIE</span><span class="topo-unknown">KADN</span><span class="topo-inside">AAQVKDALTKMRAAALDAQKATPPK</span><span class="topo-unknown">LEDKSPD</span><span class="topo-inside">SPEMKDFRHGFDI</span></span>
<span class="topo-line"><span class="topo-inside">LVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQK</span><span class="topo-unknown">YL</span><span class="topo-inside">QRMLS</span><span class="topo-membrane">MAHLLQTVLHVIQVVV</span></span>
<span class="topo-line"><span class="topo-membrane">SYFLMLVFM</span><span class="topo-outside">TYNA</span><span class="topo-membrane">YLCMAVAAGAGLGYFLFSWKKAV</span><span class="topo-inside">VVDIT</span><span class="topo-unknown">EHCHSNSLEVLFQ</span></span>
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
      <td>26</td>
      <td>41</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>51</td>
      <td>67</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>53</td>
      <td>92</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>71</td>
      <td>1002</td>
      <td>1018</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>100</td>
      <td>1023</td>
      <td>1047</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>157</td>
      <td>1055</td>
      <td>1104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>158</td>
      <td>1105</td>
      <td>1105</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>160</td>
      <td>164</td>
      <td>121</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>126</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>193</td>
      <td>151</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>216</td>
      <td>155</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>221</td>
      <td>178</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6m97">6M97</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MTFYFGYTNVELLFASLVINTPGEMV</span><span class="topo-membrane">AACFGCFLLAVLYEGLKIGREFLLR</span><span class="topo-inside">RN</span><span class="topo-unknown">A</span><span class="topo-inside">DLEDNW</span></span>
<span class="topo-line"><span class="topo-inside">ETLNDNLKVIE</span><span class="topo-unknown">KADN</span><span class="topo-inside">AAQVKDALTKMRAAALDAQKATPPK</span><span class="topo-unknown">LEDKSPD</span><span class="topo-inside">SPEMKDFRHGFDI</span></span>
<span class="topo-line"><span class="topo-inside">LVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQK</span><span class="topo-unknown">YL</span><span class="topo-inside">QRMLS</span><span class="topo-membrane">MAHLLQTVLHVIQVVV</span></span>
<span class="topo-line"><span class="topo-membrane">SYFLMLVFM</span><span class="topo-outside">TYNA</span><span class="topo-membrane">YLCMAVAAGAGLGYFLFSWKKAV</span><span class="topo-inside">VVDIT</span><span class="topo-unknown">EHCHSNSLEVLFQ</span></span>
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
      <td>26</td>
      <td>41</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>51</td>
      <td>67</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>53</td>
      <td>92</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>71</td>
      <td>1002</td>
      <td>1018</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>100</td>
      <td>1023</td>
      <td>1047</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>157</td>
      <td>1055</td>
      <td>1104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>158</td>
      <td>1105</td>
      <td>1105</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>160</td>
      <td>164</td>
      <td>121</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>126</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>193</td>
      <td>151</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>216</td>
      <td>155</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>221</td>
      <td>178</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6m97">6M97</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MTFYFGYTNVELLFASLVINTPGEMV</span><span class="topo-membrane">AACFGCFLLAVLYEGLKIGREFLLR</span><span class="topo-inside">RN</span><span class="topo-unknown">A</span><span class="topo-inside">DLEDNW</span></span>
<span class="topo-line"><span class="topo-inside">ETLNDNLKVIE</span><span class="topo-unknown">KADN</span><span class="topo-inside">AAQVKDALTKMRAAALDAQKATPPK</span><span class="topo-unknown">LEDKSPD</span><span class="topo-inside">SPEMKDFRHGFDI</span></span>
<span class="topo-line"><span class="topo-inside">LVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQK</span><span class="topo-unknown">YL</span><span class="topo-inside">QRMLS</span><span class="topo-membrane">MAHLLQTVLHVIQVVV</span></span>
<span class="topo-line"><span class="topo-membrane">SYFLMLVFM</span><span class="topo-outside">TYNA</span><span class="topo-membrane">YLCMAVAAGAGLGYFLFSWKKAV</span><span class="topo-inside">VVDIT</span><span class="topo-unknown">EHCHSNSLEVLFQ</span></span>
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
      <td>26</td>
      <td>41</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>51</td>
      <td>67</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>53</td>
      <td>92</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>71</td>
      <td>1002</td>
      <td>1018</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>100</td>
      <td>1023</td>
      <td>1047</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>157</td>
      <td>1055</td>
      <td>1104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>158</td>
      <td>1105</td>
      <td>1105</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>160</td>
      <td>164</td>
      <td>121</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>126</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>193</td>
      <td>151</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>216</td>
      <td>155</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>221</td>
      <td>178</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6m97">6M97</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MTFYFGYTNVELLFASLVINTPGEMV</span><span class="topo-membrane">AACFGCFLLAVLYEGLKIGREFLLR</span><span class="topo-inside">RN</span><span class="topo-unknown">A</span><span class="topo-inside">DLEDNW</span></span>
<span class="topo-line"><span class="topo-inside">ETLNDNLKVIE</span><span class="topo-unknown">KADN</span><span class="topo-inside">AAQVKDALTKMRAAALDAQKATPPK</span><span class="topo-unknown">LEDKSPD</span><span class="topo-inside">SPEMKDFRHGFDI</span></span>
<span class="topo-line"><span class="topo-inside">LVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQK</span><span class="topo-unknown">YL</span><span class="topo-inside">QRMLS</span><span class="topo-membrane">MAHLLQTVLHVIQVVV</span></span>
<span class="topo-line"><span class="topo-membrane">SYFLMLVFM</span><span class="topo-outside">TYNA</span><span class="topo-membrane">YLCMAVAAGAGLGYFLFSWKKAV</span><span class="topo-inside">VVDIT</span><span class="topo-unknown">EHCHSNSLEVLFQ</span></span>
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
      <td>26</td>
      <td>41</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>51</td>
      <td>67</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>53</td>
      <td>92</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>71</td>
      <td>1002</td>
      <td>1018</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>100</td>
      <td>1023</td>
      <td>1047</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>157</td>
      <td>1055</td>
      <td>1104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>158</td>
      <td>1105</td>
      <td>1105</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>160</td>
      <td>164</td>
      <td>121</td>
      <td>125</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>126</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>193</td>
      <td>151</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>216</td>
      <td>155</td>
      <td>177</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>221</td>
      <td>178</td>
      <td>182</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Selectivity filter

Two strictly conserved [methionine triads](/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/) (M146 and M150 in TM2, MX₃M motif) form a Cu⁺ selectivity filter near the extracellular entrance. Each triad coordinates a single Cu⁺ ion through trigonal planar Cu-S coordination, conferring selectivity for Cu⁺ over Cu²⁺.

### Zinc binding and regulation

A Zn²⁺ binding site is formed by E80 (TM1) and H135 (TM2) from adjacent subunits. Mutations at corresponding positions in human Ctr1 (E84Q, H139R) increase Cu⁺ transport rate, suggesting Zn²⁺ negatively regulates Cu⁺ transport.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/selectivity-filter/">Selectivity Filter</a> — Two methionine triads form a Cu⁺ selectivity filter
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channel-like-mechanism/">Channel-Like Mechanism</a> — Ctr1 functions like an ion channel for Cu⁺ conduction
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-ion-coordination/">Intramembrane Ion Coordination</a> — Cu⁺ is coordinated by methionine S atoms in the selectivity filter
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — SEC was used as a final purification step
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging Drop Vapor Diffusion</a> — Crystals were grown by hanging drop vapor diffusion
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used for solubilization at 2% (w/v)
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Primary buffer component throughout purification
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Reducing agent in SEC buffer
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400</a> — Precipitant in crystallization conditions
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> — Fusion protein used in crystallization construct
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used in cobalt affinity wash buffer
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Used as cryoprotectant
- <a href="/xray-mp-wiki/methods/expression-systems/pichia-pastoris/">Pichia pastoris Expression System</a> — Used for recombinant expression of sCtr1
- <a href="/xray-mp-wiki/reagents/buffers/cacodylate/">Sodium Cacodylate</a> — Buffer component in crystallization reservoir solution
