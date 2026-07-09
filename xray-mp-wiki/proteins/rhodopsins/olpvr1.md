---
title: "OLPVR1"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-19457-7]
verified: regex
uniprot_id: F2Y337
---

# OLPVR1

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/F2Y337">UniProt: F2Y337</a>

<span class="expr-badge">Organic lake phycodnavirus</span>

## Overview

OLPVR1 is a viral channelrhodopsin from the VR1 group, encoded by the Organic Lake phycodnavirus (OLPV), a nucleocytoplasmic large DNA virus that infects marine phytoplankton. It is a light-gated Na+/K+-selective cation channel that is uniquely impermeable to Ca2+ ions. The 1.4 A resolution crystal structure reveals remarkable differences from known channelrhodopsins, including a unique ion-conducting pathway with intracellular pore formation and absence of prominent extracellular cavities. OLPVR1 represents a distinct group of light-gated channels with potential optogenetic applications due to its lack of Ca2+ permeability.

## Publications

### doi/10.1038##s41467-020-19457-7

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7akx">7AKX</a></td>
      <td>1.4 A</td>
      <td>P1</td>
      <td>OLPVR1 from Organic Lake phycodnavirus, full-length viral channelrhodopsin</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal">Retinal</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7akw">7AKW</a></td>
      <td>1.4 A</td>
      <td>P21212</td>
      <td>OLPVR1 from Organic Lake phycodnavirus, full-length viral channelrhodopsin</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal">Retinal</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7aky">7AKY</a></td>
      <td>1.6 A</td>
      <td>not specified</td>
      <td>OLPVR1 O1O2 mutant</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal">Retinal</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Human embryonic kidney (HEK) cells
- **Construct**: Human codon-optimized OLPVR1 gene cloned into pcDNA3.1(-) vector with P2A self-cleavage peptide and fluorescent tag

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
      <td>Protein expression</td>
      <td>Transfection of HEK cells with codon-optimized OLPVR1 plasmid</td>
      <td>--</td>
      <td>Not specified + --</td>
      <td>Codon-optimized OLPVR1 synthesized commercially (Eurofins), cloned into pcDNA3.1(-) vector with P2A self-cleavage peptide and Katushka fluorescent protein at C-terminus</td>
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
      <td>OLPVR1 at 20 mg/ml with 10 mM CaCl2, 10 mM <a href="/xray-mp-wiki/reagents/additives/mgcl2">MGCL2</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1 to 4 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals incubated in precipitant solution for 5 min before data collection</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Best crystals obtained with 20 mg/ml protein. Data collected at ESRF beamlines ID30b and ID23-1 using PILATUS 6M detector. Structures solved by molecular replacement using 6SQG structure as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7akx">7AKX</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DNI</span><span class="topo-membrane">IMTAYISIFVQIITAIISVYG</span><span class="topo-inside">LFIPLNFKDIILREI</span><span class="topo-membrane">LILELIVQIIEFIFYIWLII</span><span class="topo-outside">TLQSINEDIT</span><span class="topo-membrane">YVRYFDWVLTTPVMLLTTV</span><span class="topo-inside">YFFEYMNSDDGIRKKEINDRDYV</span><span class="topo-membrane">YLFYICLS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230 </span>
<span class="topo-line"><span class="topo-membrane">NFFMLLIGYLGE</span><span class="topo-outside">TKQINKM</span><span class="topo-membrane">LTLFGGSFFLFLTFYLLYVK</span><span class="topo-inside">YTKENW</span><span class="topo-membrane">MNYIVFYFMFLVWFLYGFAFM</span><span class="topo-outside">FPFSIK</span><span class="topo-membrane">NQMYNILDIVSKNIYSIFIFI</span><span class="topo-inside">VILNQSYKLLLE</span><span class="topo-unknown">HHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>5</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>40</td>
      <td>26</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>60</td>
      <td>41</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>70</td>
      <td>61</td>
      <td>70</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>89</td>
      <td>71</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>112</td>
      <td>90</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>132</td>
      <td>113</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>139</td>
      <td>133</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>159</td>
      <td>140</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>165</td>
      <td>160</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>186</td>
      <td>166</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>192</td>
      <td>187</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>213</td>
      <td>193</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>225</td>
      <td>214</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>226</td>
      <td>231</td>
      <td>226</td>
      <td>231</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7akw">7AKW</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MDNIIMT</span><span class="topo-membrane">AYISIFVQIITAIISVYGLFI</span><span class="topo-outside">PLNFKDIIL</span><span class="topo-membrane">REILILELIVQIIEFIFYIWL</span><span class="topo-inside">IITLQSINEDIT</span><span class="topo-membrane">YVRYFDWVLTTPVMLLTTVYF</span><span class="topo-outside">FEYMNSDDGIRKKEINDRDYV</span><span class="topo-membrane">YLFYICLS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220   </span>
<span class="topo-line"><span class="topo-membrane">NFFMLLIGYLGE</span><span class="topo-inside">TKQINK</span><span class="topo-membrane">MLTLFGGSFFLFLTFYLLYV</span><span class="topo-outside">KYTKENWM</span><span class="topo-membrane">NYLVFGAMFLLWALYGFAFM</span><span class="topo-inside">FPFSIK</span><span class="topo-membrane">NQMYNILDIFSKNFVSIFFFIVILN</span><span class="topo-outside">QSYKLL</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>28</td>
      <td>8</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>37</td>
      <td>29</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>58</td>
      <td>38</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>70</td>
      <td>59</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>91</td>
      <td>71</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>112</td>
      <td>92</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>132</td>
      <td>113</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>138</td>
      <td>133</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>158</td>
      <td>139</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>166</td>
      <td>159</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>186</td>
      <td>167</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>192</td>
      <td>187</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>217</td>
      <td>193</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>223</td>
      <td>218</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7akw">7AKW</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">DNIIM</span><span class="topo-membrane">TAYISIFVQIITAIISVYGL</span><span class="topo-outside">FIPLNFKDIILREI</span><span class="topo-membrane">LILELIVQIIEFIFYIWLII</span><span class="topo-inside">TLQSINEDIT</span><span class="topo-membrane">YVRYFDWVLTTPVMLLTTVYFF</span><span class="topo-outside">EYMNSDDGIRKKEINDRDY</span><span class="topo-membrane">VYLFYICLS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220   </span>
<span class="topo-line"><span class="topo-membrane">NFFMLLIGYLGE</span><span class="topo-inside">TKQINKML</span><span class="topo-membrane">TLFGGSFFLFLTFYLLYVKYT</span><span class="topo-outside">KENW</span><span class="topo-membrane">MNYLVFGAMFLLWALYGFAF</span><span class="topo-inside">MFPFSIKN</span><span class="topo-membrane">QMYNILDIFSKNFVSIFFFIV</span><span class="topo-outside">ILNQSYKL</span><span class="topo-unknown">L</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>6</td>
      <td>2</td>
      <td>6</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>26</td>
      <td>7</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>40</td>
      <td>27</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>60</td>
      <td>41</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>70</td>
      <td>61</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>92</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>111</td>
      <td>93</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>132</td>
      <td>112</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>140</td>
      <td>133</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>161</td>
      <td>141</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>165</td>
      <td>162</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>185</td>
      <td>166</td>
      <td>185</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>193</td>
      <td>186</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>214</td>
      <td>194</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>222</td>
      <td>215</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>223</td>
      <td>223</td>
      <td>223</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7aky">7AKY</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">DNI</span><span class="topo-membrane">IMTAYISIFVQIITAIISVYG</span><span class="topo-outside">LFIPLNFKDIILREI</span><span class="topo-membrane">LILELIVQIIEFIFYIWLII</span><span class="topo-inside">TLQSINEDIT</span><span class="topo-membrane">YVRYFDWVLTTPVMLLTTV</span><span class="topo-outside">YFFEYMNSDDGIRKKEINDRDY</span><span class="topo-membrane">VYLFYICLS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230 </span>
<span class="topo-line"><span class="topo-membrane">NFFMLLIGYLGE</span><span class="topo-inside">TKQINKM</span><span class="topo-membrane">LTLFGGSFFLFLTFYLLYVK</span><span class="topo-outside">YTKENW</span><span class="topo-membrane">MNYIVFYFMFLVWFLYGFAFM</span><span class="topo-inside">FPFSIK</span><span class="topo-membrane">NQMYNILDIVSKNIYSIFIFI</span><span class="topo-outside">VILNQSYKLLL</span><span class="topo-unknown">EHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>5</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>40</td>
      <td>26</td>
      <td>40</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>41</td>
      <td>60</td>
      <td>41</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>70</td>
      <td>61</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>89</td>
      <td>71</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>111</td>
      <td>90</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>132</td>
      <td>112</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>139</td>
      <td>133</td>
      <td>139</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>159</td>
      <td>140</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>165</td>
      <td>160</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>186</td>
      <td>166</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>192</td>
      <td>187</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>213</td>
      <td>193</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>224</td>
      <td>214</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>225</td>
      <td>231</td>
      <td>225</td>
      <td>231</td>
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

### Unique ion-conducting pathway with intracellular pore

Unlike other channelrhodopsins, OLPVR1 lacks prominent cavities in the extracellular part. Instead, it has a pore in the intracellular part that ends with a relatively large hydrophilic cavity near the [Retinal](/xray-mp-wiki/reagents/ligands/retinal). The cavity is filled with four water molecules and surrounded by polar residues E44, T87, T88, and W178. Three constriction sites form the putative ion-conductive pathway: intracellular (E44), central (S-E-N triad at E51), and extracellular (R73, E132, K192, N193, N197).

### Ca2+ impermeability distinguishes viral channelrhodopsins

VirChR1 (61% sequence similarity to OLPVR1) is completely impermeable to Ca2+ cations, in contrast to the high Ca2+ conductivity of CrChR2. This Ca2+ impermeability is an important feature that separates VirChR1s from direct competition with chlorophyte channelrhodopsins in optogenetic applications, as it avoids Ca2+-induced noxious side effects.

### Photocycle intermediates lack detectable M-state

Transient absorption measurements revealed three distinct intermediate states: an early decaying K-like state (540 nm), followed by major accumulation of L-like (460 nm) and N-like (560 nm) states lasting about 1.5 s. Unlike other channelrhodopsins, OLPVR1 lacks a detectable M-state that is generally associated with the ion-conducting state. The equilibrium between L-like and N-like states is the major candidate for the ion-conducting state.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/">Channelrhodopsin C1C2</a> — Reference channelrhodopsin structure for comparison of ion-conducting pathway and constriction sites
- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — Archetypal microbial rhodopsin; OLPVR1 architecture resembles PR family with different ion pathway
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">All-trans retinal</a> — Chromophore covalently bound to conserved Lys204 via Schiff base linkage
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid component of the lipidic cubic phase crystallization matrix
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl buffer)</a> — Buffer (100 mM, pH 8.2) used in crystallization reservoir
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> — Salt used in electrophysiology experiments to measure Na+ conductivity
- <a href="/xray-mp-wiki/reagents/additives/calcium-chloride/">Calcium Chloride (CaCl2)</a> — Used in crystallization (10 mM) and to test Ca2+ impermeability in electrophysiology
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used to grow OLPVR1 crystals at 22 C
- <a href="/xray-mp-wiki/reagents/ligands/retinal">Retinal</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> — Entity mentioned in text
