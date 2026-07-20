---
title: "GtACR1 Anion Channelrhodopsin from Guillardia theta"
created: 2026-06-09
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.41741, doi/10.7554##eLife.65903]
verified: agent
uniprot_id: L1J207
---

# GtACR1 Anion Channelrhodopsin from Guillardia theta

<div class="expr-badges"><span class="expr-badge expr-p-pastoris">P. pastoris</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/L1J207">UniProt: L1J207</a>

<span class="expr-badge">Guillardia theta CCMP2712</span>

## Overview

GtACR1 is a natural light-gated anion channelrhodopsin from the cryptophyte alga Guillardia theta. It is the most potent neuron-silencing optogenetic tool available, exhibiting 25-fold higher unitary conductance than the cation channelrhodopsin CrChR2. The X-ray crystal structure of the dark (closed) state was determined at 2.9 A resolution (Li et al., 2019, PDB 6EDQ). The structure reveals a continuous intramolecular tunnel traversing the protein from the extracellular surface to a large cytoplasmic cavity, lined primarily by small polar and aliphatic residues essential for anion conductance. A disulfide-immobilized extracellular cap facilitates channel closing, and the ion path is blocked mid-membrane by the photoactive retinylidene chromophore. The structure also reveals a novel photoactive site configuration that maintains the retinylidene Schiff base protonated in the open-channel state, in contrast to cation channelrhodopsins where Schiff base deprotonation precedes channel opening. GtACR1 forms a disulfide-crosslinked homodimer stabilized by TM3 and TM4 interactions and an intermolecular C6-C6 disulfide bridge. The bromide-bound structure at 3.2 A resolution (Li et al., 2021, PDB 7L1E) revealed structural changes that relax the C1 and C3 tunnel constrictions, including a novel salt-bridge switch mechanism involving Arg94, providing direct evidence that the tunnel is the closed form of the channel and shedding light on the light-gated channel activation mechanism.


## Publications

### doi/10.7554##eLife.41741

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6edq">6EDQ</a></td>
      <td>2.9 A</td>
      <td>P2(1)2(1)2</td>
      <td>GtACR1 from G. theta, residues 1-295, dark (closed) state</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> lipids</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: GtACR1 (GenBank KP171708, residues 1-295) with C-terminal His8 tag in pPIC9K

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
      <td>Cell culture and harvesting</td>
      <td>Baculovirus expression in Sf9 cells</td>
      <td>not applicable</td>
      <td>350 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 20 mM HEPES pH 7.5 (Buffer A) with 0.1 mM PMSF + not specified</td>
      <td>Sf9 cells infected at ~2x10^6 cells/ml with GtACR1-encoding baculovirus at 15:1 (v/v); 5 uM all-trans-<a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> added; 3 days in spinner flasks at 27 C. Pink-colored cells harvested by centrifugation.</td>
    </tr>
    <tr>
      <td>Cell lysis and membrane isolation</td>
      <td>High-pressure homogenization and ultracentrifugation</td>
      <td>not applicable</td>
      <td>Buffer A (350 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 20 mM HEPES pH 7.5) with 0.1 mM PMSF + not specified</td>
      <td>Cells ruptured by 3 passes through EmulsiFlex-C3 homogenizer; low-speed spin at 5000 rpm for 10 min to remove debris; membranes pelleted at 40,000 rpm for 1 hr in Ti45 rotor.</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>not applicable</td>
      <td>Buffer A + 1% n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membranes suspended in Buffer A and solubilized with 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for 1 hr at 4 C with shaking; undissolved material removed by ultracentrifugation at 45,000 rpm for 1 hr.</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td>Immobilized metal ion <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin (Qiagen)</td>
      <td>Buffer A with 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>; 15 mM and 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> for washes; 400 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> for elution + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Supernatant supplemented with 15 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> incubated with Ni resin for 1 hr at 4 C; step-wise washes with 15 mM and 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; eluted with 400 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in Buffer A + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>.</td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>Superdex Increase 10/300 GL column (GE Healthcare)</td>
      <td>Buffer B (350 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>) + not specified</td>
      <td>Eluted protein further purified on Superdex Increase 10/300 GL column equilibrated with Buffer B.</td>
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
      <td>GtACR1 in buffer, ~unknown concentration</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>100 K (data collection)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (LCP). Continuous grid-scan method used for X-ray data collection at SLS X06SA-PXI beamline (Swiss Light Source). Four partial datasets merged to 2.9 A. Space group P2(1)2(1)2, cell dimensions a=77.79 A, b=149.55 A, c=62.41 A, alpha=beta=gamma=90 degrees. Data processed with XDS/XSCALE. Structure solved by molecular replacement using CrChR2 (PDB 6EID) as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6edq">6EDQ</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSSIT</span><span class="topo-outside">CDPAIYGEWSRENQFCVEKSLITLDG</span><span class="topo-membrane">IKYVQLVMAVVSACQVFFMV</span><span class="topo-inside">TRAPKVPW</span><span class="topo-membrane">EAIYLPTTEMITYSLAFT</span><span class="topo-outside">GNGYIRVANGKYL</span><span class="topo-membrane">PWARMASWLCTCPIMLG</span><span class="topo-inside">LVSNMALVKYKSI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PLNP</span><span class="topo-membrane">MMIAASSICTVFGITAS</span><span class="topo-outside">VVLDPLH</span><span class="topo-membrane">VWLYCFISSIFFIFEMVVAF</span><span class="topo-inside">AIFAITIHDFQTIGSPMSLKVVERLKL</span><span class="topo-membrane">MRIVFYVSWMAYPILWSFS</span><span class="topo-outside">STGACIMSE</span><span class="topo-membrane">NTSSVLYLLGDALCKNT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-membrane">YGI</span><span class="topo-inside">LLWATTWGLLNGKWDRDYVKGRNVDGTLM</span><span class="topo-unknown">PEYEQDLEKGNTERYEDARAGETHHHHHHHH</span></span>
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
      <td>6</td>
      <td>31</td>
      <td>6</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>51</td>
      <td>32</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>59</td>
      <td>52</td>
      <td>59</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>77</td>
      <td>60</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>90</td>
      <td>78</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>107</td>
      <td>91</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>124</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>141</td>
      <td>125</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>148</td>
      <td>142</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>168</td>
      <td>149</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>195</td>
      <td>169</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>214</td>
      <td>196</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>223</td>
      <td>215</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>243</td>
      <td>224</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>272</td>
      <td>244</td>
      <td>272</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6edq">6EDQ</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSSI</span><span class="topo-outside">TCDPAIYGEWSRENQFCVEKSLITLDG</span><span class="topo-membrane">IKYVQLVMAVVSACQVFFMV</span><span class="topo-inside">TRAPKVPW</span><span class="topo-membrane">EAIYLPTTEMITYSLAFT</span><span class="topo-outside">GNGYIRVANGKYL</span><span class="topo-membrane">PWARMASWLCTCPIMLG</span><span class="topo-inside">LVSNMALVKYKSI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PLNP</span><span class="topo-membrane">MMIAASSICTVFGITAS</span><span class="topo-outside">VVLDPLH</span><span class="topo-membrane">VWLYCFISSIFFIFEMVVAF</span><span class="topo-inside">AIFAITIHDFQTIGSPMSLKVVERLKLM</span><span class="topo-membrane">RIVFYVSWMAYPILWSFS</span><span class="topo-outside">STGACIMSE</span><span class="topo-membrane">NTSSVLYLLGDALCKNT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-membrane">YGI</span><span class="topo-inside">LLWATTWGLLNGKWDRDYVKGRNVDGTLMPEYEQDL</span><span class="topo-unknown">EKGNTERYEDARAGETHHHHHHHH</span></span>
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
      <td>5</td>
      <td>31</td>
      <td>5</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>51</td>
      <td>32</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>59</td>
      <td>52</td>
      <td>59</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>77</td>
      <td>60</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>90</td>
      <td>78</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>107</td>
      <td>91</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>124</td>
      <td>108</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>141</td>
      <td>125</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>148</td>
      <td>142</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>168</td>
      <td>149</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>196</td>
      <td>169</td>
      <td>196</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>214</td>
      <td>197</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>223</td>
      <td>215</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>224</td>
      <td>243</td>
      <td>224</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>279</td>
      <td>244</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.7554##eLife.65903

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7l1e">7L1E</a></td>
      <td>3.2 A</td>
      <td>P 2(1)</td>
      <td>GtACR1 from G. theta, residues 1-295, bromide-bound pre-activated state</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>, bromide ion</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris
- **Construct**: GtACR1 (GenBank KP171708, residues 1-295) with C-terminal His8 tag in pPIC9K

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
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization in IMISX plates</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GtACR1 in purification buffer (350 mM NaBr, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>100 K (data collection)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1 month</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>LCP crystallization set up in IMISX glass plates to facilitate high-throughput data collection. Crystals harvested using micromesh loops and 3D-printed holders. Data collected by serial synchrotron crystallography at SLS X06SA-PXI beamline. 217 datasets collected using EIGER 16M detector; 31 IMISX and 5 loop-mounted datasets merged to 3.2 A. Space group P 2(1). Structure solved by molecular replacement using 6EDQ as search model. Rwork/Rfree = 0.24/0.29.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7l1e">7L1E</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">IT</span><span class="topo-outside">CDPAIYGEWSRENQFCVEKSLITLDG</span><span class="topo-membrane">IKYVQLVMAVVSACQVFFMVTR</span><span class="topo-inside">APKV</span><span class="topo-membrane">PWEAIYLPTTEMITYSLAFTGNGY</span><span class="topo-outside">IRVANGKYL</span><span class="topo-membrane">PWARMASWLCTCPIMLGLVSN</span><span class="topo-inside">MALVKYKSIP</span><span class="topo-membrane">LN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">PMMIAASSICTVFGITAS</span><span class="topo-outside">VVLDPLH</span><span class="topo-membrane">VWLYCFISSIFFIFEMVVAFAIFA</span><span class="topo-inside">ITIHDFQTIGSPMSLKVVER</span><span class="topo-membrane">LKLMRIVFYVSWMAYPILWSFS</span><span class="topo-outside">STGACIMSE</span><span class="topo-membrane">NTSSVLYLLGDALCKNTYGI</span></span>
<span class="topo-ruler">       250       260         </span>
<span class="topo-line"><span class="topo-membrane">LLWA</span><span class="topo-inside">TTWGLLNGKWDRDYVKGRNVDGT</span><span class="topo-unknown">LM</span></span>
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
      <td>3</td>
      <td>28</td>
      <td>6</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>50</td>
      <td>32</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>54</td>
      <td>54</td>
      <td>57</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>78</td>
      <td>58</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>87</td>
      <td>82</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>108</td>
      <td>91</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>118</td>
      <td>112</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>138</td>
      <td>122</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>145</td>
      <td>142</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>169</td>
      <td>149</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>189</td>
      <td>173</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>211</td>
      <td>193</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>220</td>
      <td>215</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>244</td>
      <td>224</td>
      <td>247</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>267</td>
      <td>248</td>
      <td>270</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7l1e">7L1E</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">ITCDPAIYGEWSRENQFCVEKSLITLDGI</span><span class="topo-membrane">KYVQLVMAVVSACQVFFMVTR</span><span class="topo-inside">APKV</span><span class="topo-membrane">PWEAIYLPTTEMITYSLAFT</span><span class="topo-outside">GNGYIRVANGKYL</span><span class="topo-membrane">PWARMASWLCTCPIMLGLVSN</span><span class="topo-inside">MALVKYKSIP</span><span class="topo-membrane">LN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">PMMIAASSICTVFGITAS</span><span class="topo-outside">VVLDPL</span><span class="topo-membrane">HVWLYCFISSIFFIFEMVVAFAIF</span><span class="topo-inside">AITIHDFQTIGSPMSLKVVER</span><span class="topo-membrane">LKLMRIVFYVSWMAYPILWSFS</span><span class="topo-outside">STGACIMSE</span><span class="topo-membrane">NTSSVLYLLGDALCKNTYGI</span></span>
<span class="topo-ruler">       250       260         </span>
<span class="topo-line"><span class="topo-membrane">LLWA</span><span class="topo-inside">TTWGLLNGKWDRDYVKGRNVDGTLM</span></span>
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
      <td>29</td>
      <td>4</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>50</td>
      <td>33</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>54</td>
      <td>54</td>
      <td>57</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>74</td>
      <td>58</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>87</td>
      <td>78</td>
      <td>90</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>108</td>
      <td>91</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>118</td>
      <td>112</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>138</td>
      <td>122</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>144</td>
      <td>142</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>168</td>
      <td>148</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>189</td>
      <td>172</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>211</td>
      <td>193</td>
      <td>214</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>220</td>
      <td>215</td>
      <td>223</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>244</td>
      <td>224</td>
      <td>247</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>269</td>
      <td>248</td>
      <td>272</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Anion conductance pathway architecture

The GtACR1 structure reveals a continuous tunnel traversing the protein from extracellular to cytoplasmic surface, assembled by TM1-3 and TM7. The tunnel is lined by small polar and aliphatic residues (A75, T71, S97) in contrast to charged residues at corresponding positions in cation channelrhodopsins C1C2 and CrChR2. Three constrictions (C1 at extracellular port, C2 near the Schiff base, C3 at cytoplasmic side) regulate anion flux. The C1 constriction is stabilized by an H-bond network involving Y81, R94 and E223.

### Disulfide-immobilized extracellular cap

An intramolecular disulfide bridge between C21 (N-terminal loop) and C219 (TM6-7 loop) immobilizes the extracellular cap domain, encapsulating a hydrophobic segment on the tunnel entry port. This disulfide is conserved in ACRs but absent in CCRs. Disruption by [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) (Delta1-25) or C21S/C219S mutations results in slowed channel closing, establishing the cap's role in gating kinetics.

### Protonated Schiff base in open-channel state

In GtACR1, the retinylidene Schiff base remains protonated throughout the lifetime of the open-channel state, with deprotonation correlated with the initial phase of channel closing (~20 ms). This is fundamentally different from cation channelrhodopsins where Schiff base deprotonation precedes channel opening. A triad of residues (E68, N259, S263, ENS) forms a hydrogen bond network that stabilizes the protonated Schiff base.

### Anion selectivity mechanism

Anion selectivity in GtACR1 is governed by pore-surface electrostatics. The tunnel is lined by small polar and aliphatic residues with sparse positive charges, creating an electropositive pathway that favors anion conduction. The R94A mutation nearly abolishes Cl- conductance. The retinylidene Schiff base itself serves not only as a gate but also as a direct mediator for anion flux.

### Dimeric architecture and cytoplasmic cavity

GtACR1 forms a disulfide-crosslinked homodimer stabilized by TM3 and TM4 interactions and a C6-C6 intermolecular disulfide bridge. The TM5-7 helices are longer than TM1-4, creating a large funnel-shaped cytoplasmic cavity (~18 A deep and ~28 A wide). Each protomer contains 7 transmembrane helices (TM1-7), an extracellular cap domain, and a C-terminal cytoplasmic loop.

### Conserved 7-TM scaffold of channelrhodopsins

Despite only ~24% sequence identity, each GtACR1 protomer superposes well with C1C2 and CrChR2 (RMSD ~0.9 A), indicating that functionally distinct channelrhodopsins share a common TM helical scaffold in their closed states. This conserved scaffold was used for molecular replacement phasing.

### Bromide binding reveals pre-activated state at C3 constriction

The bromide-bound GtACR1 structure (PDB 7L1E, 3.2 A) reveals a bromide ion bound at the cytoplasmic port of the transmembrane tunnel, stabilized by H-bond interactions with Trp250 and Pro58. Bromide binding pushes Pro58 outward by ~1.8 A, widening the C3 constriction by ~1 A in diameter. This demonstrates that substrate binding induces a transition from an inactivated state to a pre-activated state in the dark that facilitates channel opening by reducing free energy in the tunnel constrictions. The data provide direct evidence that the tunnel is the closed form of the channel.

### Salt-bridge switch mechanism at C1 constriction

In chain A of the bromide-bound structure, Arg94 at the C1 constriction undergoes a ~180 degree side-chain rotation, switching from a salt-bridge with Glu223 (apo form conformation) to an alternative salt-bridge with Asp234 near the photoactive site. This rotation widens the C1 constriction by ~1 A and creates a conformation similar to the chloride-binding site of the CIR chloride pump (PDB 5G2A, Arg95). Chain B retains the apo-form Arg94 conformation, demonstrating intrinsic flexibility of the C1 constriction between protomers.

### Larger bromide conductance explained by tunnel widening

The conformational changes induced by bromide binding expand the tunnel in both C1 and C3 constrictions, while C2 remains the narrowest constriction due to the trans-configured [Retinal](/xray-mp-wiki/reagents/ligands/retinal/). This pre-activating conformational change reduces the free energy barrier for channel opening, consistent with GtACR1 exhibiting larger conductance for bromide than chloride. FTIR data confirm that bromide binding alters the electron conjugation of the retinylidene polyene chain in the dark state without perturbing the all-trans to 13-cis photoisomerization.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/">Channelrhodopsin C1C2 Chimera</a> — Closely related cation channelrhodopsin chimera used for structural comparison
- <a href="/xray-mp-wiki/proteins/rhodopsins/ic-plus-plus/">iC++ Designed Anion Channelrhodopsin</a> — Designed ACR created by structure-guided engineering for comparison with natural ACR GtACR1
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channelrhodopsin-photocycle/">Channelrhodopsin Photocycle</a> — GtACR1 exhibits a distinct photocycle mechanism with protonated Schiff base in open state
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — GtACR1 structure determined by LCP crystallization method
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for GtACR1 purification and solubilization
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> — Referenced in gtacr1 text
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Referenced in gtacr1 text
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in gtacr1 text
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in gtacr1 text
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in gtacr1 text
