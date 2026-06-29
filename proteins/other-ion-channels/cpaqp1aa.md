---
title: "cpAQP1aa (Climbing Perch Aquaporin 1aa)"
created: 2026-06-11
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.26508##lsa.202201491]
verified: false
---

# cpAQP1aa (Climbing Perch Aquaporin 1aa)

## Overview

cpAQP1aa is a water-specific [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) from the climbing perch (Anabas testudineus),
a euryhaline fish species capable of acclimating from freshwater to seawater and
surviving on land. It is the first structurally and functionally characterized fish
[Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) and a homolog of mammalian [AQP1](/xray-mp-wiki/proteins/other-ion-channels/aqp1/). The 1.9 A crystal structure reveals the
conserved [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) homotetrameric fold with six transmembrane helices and two
half-helices per monomer, but with a unique extracellular fold in loop C that creates
a constriction region on the extracellular side—a feature not seen in other [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/)
structures. The channel is water-specific, does not transport [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) or ammonia,
and is proposed to be regulated by phosphorylation at Thr38 (loop A) and Tyr107
(loop C), which may control gating from the extracellular side. Molecular dynamics
simulations suggest phosphorylation of Tyr107 causes structural perturbations
that narrow the pore, while mutation of Thr38 increases water permeability to levels
comparable to human AQP4.


## Publications

### doi/10.26508##lsa.202201491

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7w7s">7W7S</a></td>
      <td>1.9</td>
      <td>P42₁2</td>
      <td>C-terminally truncated cpAQP1aa (residues 1-243, untagged), expressed in Pichia pastoris</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7w7s">7W7S</a></td>
      <td>3.5</td>
      <td>C222₁</td>
      <td>C-terminally truncated cpAQP1aa (residues 1-243), expressed in Pichia pastoris</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (methylotrophic yeast)
- **Construct**: Full-length cpAQP1aa (residues 1-261) with C-terminal 8xHis tag; truncated cpAQP1aa-243 (residues 1-243) both with and without C-terminal 8xHis tag
- **Notes**: Codon-optimized for P. pastoris. GCT added after start codon for Kozak consensus. Gene subcloned into pPICZA vector, transformed into aquaporin-deficient Delta33 strain by electroporation. Large-scale production in 3L fermentors with [Methanol](/xray-mp-wiki/reagents/additives/methanol/) fed-batch induction. Yield >250 g wet cells/L culture; 63 mg purified protein/L culture.

**Purification:**

- **Expression system**: P. pastoris
- **Expression construct**: cpAQP1aa-243 (untagged)
- **Tag info**: Untagged

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
      <td>X-press or French press</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 8, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 4% NG, 2 mM beta-MeOH (solubilization)</td>
      <td></td>
    </tr>
    <tr>
      <td>Ion exchange chromatography</td>
      <td>Resource S cation exchange</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6, 37.5 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.4% NG, 2 mM beta-MeOH</td>
      <td>Elution with NaCl gradient (0-40% buffer B with 1 M NaCl)</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Superdex 200 Increase</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 8, 100 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.4% NG, 2 mM beta-MeOH</td>
      <td>Monodisperse peak; protein concentrated to ~18 mg/ml</td>
    </tr>
  </tbody>
</table>

- **Expression system**: P. pastoris
- **Expression construct**: His-tagged cpAQP1aa-243
- **Tag info**: C-terminal 8xHis tag

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
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM KH2PO4 pH 7.5, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 4% NG</td>
      <td></td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Ni-NTA</td>
      <td>—</td>
      <td>pH 8.0 for His-tagged constructs</td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Superdex 200 Increase</td>
      <td>—</td>
      <td></td>
      <td>Protein concentrated to ~18 mg/ml, stored at -80 C</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Untagged cpAQP1aa-243 at ~18 mg/ml</td>
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
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>High pH crystals (pH 7.8) in space group P42₁2 diffracted to 1.9 A. Low pH crystals (pH 6.5) in space group C222₁ diffracted to 3.5 A. Data collected at PETRA III (DESY, Hamburg) beamline P13 and ESRF beamline ID30B.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7w7s">7W7S</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">AREFKSKNFWKAV</span><span class="topo-membrane">LAELVGMTLFIFLSLSAA</span><span class="topo-inside">IGN</span><span class="topo-unknown">KNS</span><span class="topo-inside">TNPDQEV</span><span class="topo-membrane">KVSLAFGLAIATLAQ</span></span>
<span class="topo-line"><span class="topo-membrane">SLG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHLNPAVTLGMLA</span><span class="topo-outside">SCQISVLKA</span><span class="topo-membrane">VMYIVAQMLGSALASGIV</span><span class="topo-inside">YG</span><span class="topo-unknown">TRPNG</span><span class="topo-inside">NANLGL</span></span>
<span class="topo-line"><span class="topo-inside">NALSGVTPS</span><span class="topo-membrane">QGVGIELLATFQLVLCVIAV</span><span class="topo-outside">TDKRRRDVTGS</span><span class="topo-membrane">APLAIGLSVCLGHLAAI</span><span class="topo-inside">SYT</span></span>
<span class="topo-line"><span class="topo-unknown">GCGINPARSFGPALI</span><span class="topo-inside">LNNFENH</span><span class="topo-membrane">WVYWVGPMCGGVAAALIY</span><span class="topo-outside">DFLLAPK</span><span class="topo-unknown">FDDFPERIKVLVS</span></span>
<span class="topo-line"><span class="topo-unknown">GPVG</span></span>
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
      <td>0</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>14</td>
      <td>1</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>14</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>35</td>
      <td>32</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>38</td>
      <td>35</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>45</td>
      <td>38</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>67</td>
      <td>63</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>80</td>
      <td>67</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>80</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>107</td>
      <td>89</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>109</td>
      <td>107</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>109</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>114</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>149</td>
      <td>129</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>160</td>
      <td>149</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>177</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>180</td>
      <td>177</td>
      <td>179</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>195</td>
      <td>180</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>202</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>227</td>
      <td>220</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>227</td>
      <td>243</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7w7s">7W7S</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">AREFKSKNFWKAV</span><span class="topo-membrane">LAELVGMTLFIFLSLSAA</span><span class="topo-inside">IGN</span><span class="topo-unknown">KNS</span><span class="topo-inside">TNPDQEV</span><span class="topo-membrane">KVSLAFGLAIATLAQ</span></span>
<span class="topo-line"><span class="topo-membrane">SLG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHLNPAVTLGMLA</span><span class="topo-outside">SCQISVLKA</span><span class="topo-membrane">VMYIVAQMLGSALASGIV</span><span class="topo-inside">YG</span><span class="topo-unknown">TRPNG</span><span class="topo-inside">NANLGL</span></span>
<span class="topo-line"><span class="topo-inside">NALSGVTPS</span><span class="topo-membrane">QGVGIELLATFQLVLCVIAV</span><span class="topo-outside">TDKRRRDVTGS</span><span class="topo-membrane">APLAIGLSVCLGHLAAI</span><span class="topo-inside">SYT</span></span>
<span class="topo-line"><span class="topo-unknown">GCGINPARSFGPALI</span><span class="topo-inside">LNNFENH</span><span class="topo-membrane">WVYWVGPMCGGVAAALIY</span><span class="topo-outside">DFLLAPK</span><span class="topo-unknown">FDDFPERIKVLVS</span></span>
<span class="topo-line"><span class="topo-unknown">GPVG</span></span>
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
      <td>0</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>14</td>
      <td>1</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>14</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>35</td>
      <td>32</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>38</td>
      <td>35</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>45</td>
      <td>38</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>67</td>
      <td>63</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>80</td>
      <td>67</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>80</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>107</td>
      <td>89</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>109</td>
      <td>107</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>109</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>114</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>149</td>
      <td>129</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>160</td>
      <td>149</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>177</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>180</td>
      <td>177</td>
      <td>179</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>195</td>
      <td>180</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>202</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>227</td>
      <td>220</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>227</td>
      <td>243</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7w7s">7W7S</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">AREFKSKNFWKAV</span><span class="topo-membrane">LAELVGMTLFIFLSLSAA</span><span class="topo-inside">IGN</span><span class="topo-unknown">KNS</span><span class="topo-inside">TNPDQEV</span><span class="topo-membrane">KVSLAFGLAIATLAQ</span></span>
<span class="topo-line"><span class="topo-membrane">SLG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHLNPAVTLGMLA</span><span class="topo-outside">SCQISVLKA</span><span class="topo-membrane">VMYIVAQMLGSALASGIV</span><span class="topo-inside">YG</span><span class="topo-unknown">TRPNG</span><span class="topo-inside">NANLGL</span></span>
<span class="topo-line"><span class="topo-inside">NALSGVTPS</span><span class="topo-membrane">QGVGIELLATFQLVLCVIAV</span><span class="topo-outside">TDKRRRDVTGS</span><span class="topo-membrane">APLAIGLSVCLGHLAAI</span><span class="topo-inside">SYT</span></span>
<span class="topo-line"><span class="topo-unknown">GCGINPARSFGPALI</span><span class="topo-inside">LNNFENH</span><span class="topo-membrane">WVYWVGPMCGGVAAALIY</span><span class="topo-outside">DFLLAPK</span><span class="topo-unknown">FDDFPERIKVLVS</span></span>
<span class="topo-line"><span class="topo-unknown">GPVG</span></span>
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
      <td>0</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>14</td>
      <td>1</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>14</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>35</td>
      <td>32</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>38</td>
      <td>35</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>45</td>
      <td>38</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>67</td>
      <td>63</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>80</td>
      <td>67</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>80</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>107</td>
      <td>89</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>109</td>
      <td>107</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>109</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>114</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>149</td>
      <td>129</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>160</td>
      <td>149</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>177</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>180</td>
      <td>177</td>
      <td>179</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>195</td>
      <td>180</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>202</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>227</td>
      <td>220</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>227</td>
      <td>243</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7w7s">7W7S</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">AREFKSKNFWKAV</span><span class="topo-membrane">LAELVGMTLFIFLSLSAA</span><span class="topo-inside">IGN</span><span class="topo-unknown">KNS</span><span class="topo-inside">TNPDQEV</span><span class="topo-membrane">KVSLAFGLAIATLAQ</span></span>
<span class="topo-line"><span class="topo-membrane">SLG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHLNPAVTLGMLA</span><span class="topo-outside">SCQISVLKA</span><span class="topo-membrane">VMYIVAQMLGSALASGIV</span><span class="topo-inside">YG</span><span class="topo-unknown">TRPNG</span><span class="topo-inside">NANLGL</span></span>
<span class="topo-line"><span class="topo-inside">NALSGVTPS</span><span class="topo-membrane">QGVGIELLATFQLVLCVIAV</span><span class="topo-outside">TDKRRRDVTGS</span><span class="topo-membrane">APLAIGLSVCLGHLAAI</span><span class="topo-inside">SYT</span></span>
<span class="topo-line"><span class="topo-unknown">GCGINPARSFGPALI</span><span class="topo-inside">LNNFENH</span><span class="topo-membrane">WVYWVGPMCGGVAAALIY</span><span class="topo-outside">DFLLAPK</span><span class="topo-unknown">FDDFPERIKVLVS</span></span>
<span class="topo-line"><span class="topo-unknown">GPVG</span></span>
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
      <td>0</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>14</td>
      <td>1</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>14</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>35</td>
      <td>32</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>38</td>
      <td>35</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>45</td>
      <td>38</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>67</td>
      <td>63</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>80</td>
      <td>67</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>80</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>107</td>
      <td>89</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>109</td>
      <td>107</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>109</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>114</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>149</td>
      <td>129</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>160</td>
      <td>149</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>177</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>180</td>
      <td>177</td>
      <td>179</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>195</td>
      <td>180</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>202</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>227</td>
      <td>220</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>227</td>
      <td>243</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7w7s">7W7S</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">AREFKSKNFWKAV</span><span class="topo-membrane">LAELVGMTLFIFLSLSAA</span><span class="topo-inside">IGN</span><span class="topo-unknown">KNS</span><span class="topo-inside">TNPDQEV</span><span class="topo-membrane">KVSLAFGLAIATLAQ</span></span>
<span class="topo-line"><span class="topo-membrane">SLG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHLNPAVTLGMLA</span><span class="topo-outside">SCQISVLKA</span><span class="topo-membrane">VMYIVAQMLGSALASGIV</span><span class="topo-inside">YG</span><span class="topo-unknown">TRPNG</span><span class="topo-inside">NANLGL</span></span>
<span class="topo-line"><span class="topo-inside">NALSGVTPS</span><span class="topo-membrane">QGVGIELLATFQLVLCVIAV</span><span class="topo-outside">TDKRRRDVTGS</span><span class="topo-membrane">APLAIGLSVCLGHLAAI</span><span class="topo-inside">SYT</span></span>
<span class="topo-line"><span class="topo-unknown">GCGINPARSFGPALI</span><span class="topo-inside">LNNFENH</span><span class="topo-membrane">WVYWVGPMCGGVAAALIY</span><span class="topo-outside">DFLLAPK</span><span class="topo-unknown">FDDFPERIKVLVS</span></span>
<span class="topo-line"><span class="topo-unknown">GPVG</span></span>
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
      <td>0</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>14</td>
      <td>1</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>14</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>35</td>
      <td>32</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>38</td>
      <td>35</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>45</td>
      <td>38</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>67</td>
      <td>63</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>80</td>
      <td>67</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>80</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>107</td>
      <td>89</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>109</td>
      <td>107</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>109</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>114</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>149</td>
      <td>129</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>160</td>
      <td>149</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>177</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>180</td>
      <td>177</td>
      <td>179</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>195</td>
      <td>180</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>202</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>227</td>
      <td>220</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>227</td>
      <td>243</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7w7s">7W7S</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">AREFKSKNFWKAV</span><span class="topo-membrane">LAELVGMTLFIFLSLSAA</span><span class="topo-inside">IGN</span><span class="topo-unknown">KNS</span><span class="topo-inside">TNPDQEV</span><span class="topo-membrane">KVSLAFGLAIATLAQ</span></span>
<span class="topo-line"><span class="topo-membrane">SLG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHLNPAVTLGMLA</span><span class="topo-outside">SCQISVLKA</span><span class="topo-membrane">VMYIVAQMLGSALASGIV</span><span class="topo-inside">YG</span><span class="topo-unknown">TRPNG</span><span class="topo-inside">NANLGL</span></span>
<span class="topo-line"><span class="topo-inside">NALSGVTPS</span><span class="topo-membrane">QGVGIELLATFQLVLCVIAV</span><span class="topo-outside">TDKRRRDVTGS</span><span class="topo-membrane">APLAIGLSVCLGHLAAI</span><span class="topo-inside">SYT</span></span>
<span class="topo-line"><span class="topo-unknown">GCGINPARSFGPALI</span><span class="topo-inside">LNNFENH</span><span class="topo-membrane">WVYWVGPMCGGVAAALIY</span><span class="topo-outside">DFLLAPK</span><span class="topo-unknown">FDDFPERIKVLVS</span></span>
<span class="topo-line"><span class="topo-unknown">GPVG</span></span>
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
      <td>0</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>14</td>
      <td>1</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>14</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>35</td>
      <td>32</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>38</td>
      <td>35</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>45</td>
      <td>38</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>67</td>
      <td>63</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>80</td>
      <td>67</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>80</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>107</td>
      <td>89</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>109</td>
      <td>107</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>109</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>114</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>149</td>
      <td>129</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>160</td>
      <td>149</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>177</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>180</td>
      <td>177</td>
      <td>179</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>195</td>
      <td>180</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>202</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>227</td>
      <td>220</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>227</td>
      <td>243</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7w7s">7W7S</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">AREFKSKNFWKAV</span><span class="topo-membrane">LAELVGMTLFIFLSLSAA</span><span class="topo-inside">IGN</span><span class="topo-unknown">KNS</span><span class="topo-inside">TNPDQEV</span><span class="topo-membrane">KVSLAFGLAIATLAQ</span></span>
<span class="topo-line"><span class="topo-membrane">SLG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHLNPAVTLGMLA</span><span class="topo-outside">SCQISVLKA</span><span class="topo-membrane">VMYIVAQMLGSALASGIV</span><span class="topo-inside">YG</span><span class="topo-unknown">TRPNG</span><span class="topo-inside">NANLGL</span></span>
<span class="topo-line"><span class="topo-inside">NALSGVTPS</span><span class="topo-membrane">QGVGIELLATFQLVLCVIAV</span><span class="topo-outside">TDKRRRDVTGS</span><span class="topo-membrane">APLAIGLSVCLGHLAAI</span><span class="topo-inside">SYT</span></span>
<span class="topo-line"><span class="topo-unknown">GCGINPARSFGPALI</span><span class="topo-inside">LNNFENH</span><span class="topo-membrane">WVYWVGPMCGGVAAALIY</span><span class="topo-outside">DFLLAPK</span><span class="topo-unknown">FDDFPERIKVLVS</span></span>
<span class="topo-line"><span class="topo-unknown">GPVG</span></span>
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
      <td>0</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>14</td>
      <td>1</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>14</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>35</td>
      <td>32</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>38</td>
      <td>35</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>45</td>
      <td>38</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>67</td>
      <td>63</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>80</td>
      <td>67</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>80</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>107</td>
      <td>89</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>109</td>
      <td>107</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>109</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>114</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>149</td>
      <td>129</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>160</td>
      <td>149</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>177</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>180</td>
      <td>177</td>
      <td>179</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>195</td>
      <td>180</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>202</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>227</td>
      <td>220</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>227</td>
      <td>243</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7w7s">7W7S</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">AREFKSKNFWKAV</span><span class="topo-membrane">LAELVGMTLFIFLSLSAA</span><span class="topo-inside">IGN</span><span class="topo-unknown">KNS</span><span class="topo-inside">TNPDQEV</span><span class="topo-membrane">KVSLAFGLAIATLAQ</span></span>
<span class="topo-line"><span class="topo-membrane">SLG</span><span class="topo-outside">HISG</span><span class="topo-unknown">AHLNPAVTLGMLA</span><span class="topo-outside">SCQISVLKA</span><span class="topo-membrane">VMYIVAQMLGSALASGIV</span><span class="topo-inside">YG</span><span class="topo-unknown">TRPNG</span><span class="topo-inside">NANLGL</span></span>
<span class="topo-line"><span class="topo-inside">NALSGVTPS</span><span class="topo-membrane">QGVGIELLATFQLVLCVIAV</span><span class="topo-outside">TDKRRRDVTGS</span><span class="topo-membrane">APLAIGLSVCLGHLAAI</span><span class="topo-inside">SYT</span></span>
<span class="topo-line"><span class="topo-unknown">GCGINPARSFGPALI</span><span class="topo-inside">LNNFENH</span><span class="topo-membrane">WVYWVGPMCGGVAAALIY</span><span class="topo-outside">DFLLAPK</span><span class="topo-unknown">FDDFPERIKVLVS</span></span>
<span class="topo-line"><span class="topo-unknown">GPVG</span></span>
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
      <td>0</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>14</td>
      <td>1</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>32</td>
      <td>14</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>35</td>
      <td>32</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>38</td>
      <td>35</td>
      <td>37</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>45</td>
      <td>38</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>45</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>67</td>
      <td>63</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>80</td>
      <td>67</td>
      <td>79</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>80</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>107</td>
      <td>89</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>109</td>
      <td>107</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>114</td>
      <td>109</td>
      <td>113</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>129</td>
      <td>114</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>149</td>
      <td>129</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>160</td>
      <td>149</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>177</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>180</td>
      <td>177</td>
      <td>179</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>195</td>
      <td>180</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>196</td>
      <td>202</td>
      <td>195</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>220</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>227</td>
      <td>220</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>244</td>
      <td>227</td>
      <td>243</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### First structural characterization of a fish aquaporin

cpAQP1aa is the first fish [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) to be structurally and functionally
characterized. The 1.9 A crystal structure reveals the conserved [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/)
homotetrameric architecture with a unique extracellular fold not seen in
other [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) structures. This provides the first molecular insights into
water homeostasis mechanisms in fish.

### Novel extracellular constriction region formed by loop C

The cpAQP1aa structure features a unique extracellular fold in loop C that
creates a constriction region on the extracellular side, narrowing the channel
to ~1.1 A radius at Leu117 (~16 A from the NPA region). This constriction
is stabilized by a hydrogen-bonding network involving Tyr107, Arg187, and
residues 114-119 of loop C. The main structural differences compared to human
AQP4 and AQP7 are found in loops A and C.

### Water-specific channel lacking glycerol and ammonia permeability

Functional studies using stopped-flow spectroscopy on proteoliposomes showed
cpAQP1aa is water-permeable (rate constants 37.6-40.0 s^-1, compared to 95.1
s^-1 for hAQP4) but does not transport [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) or ammonia. The water
permeability is lower than hAQP4 due to the extracellular constriction region.
Structural comparison with AtTIP2;1 confirmed the pore does not support
ammonia passage.

### Phosphorylation-dependent extracellular gating mechanism

Two putative phosphorylation sites were identified: Thr38 in loop A and Tyr107
in loop C. Mutational analysis combined with 100-ns MD simulations suggests
that phosphorylation of Tyr107 causes structural perturbations that narrow the
pore (to ~1.2 A radius at the constriction) and widen the ar/R region, while
phosphorylation of Thr38 (Y107A and T38A/T38E mutants) increases water
permeability to levels comparable to hAQP4. The crystal structure likely
represents a semi-open state, with loop C acting as a gate modulated by
extracellular phosphorylation. Secreted kinases VLK (tyrosine kinase) and
DIA1/FAM69 (Ser/Thr kinase) are proposed as candidates for extracellular
phosphorylation.

### pH-independent loop C conformation

Structures determined at both pH 7.8 (1.9 A, space group P42₁2) and pH 6.5
(3.5 A, space group C222₁) show that the loop C constriction region occupies
a similar position regardless of pH, suggesting the extracellular hydrophobic
constriction is unaffected by pH changes.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin Family</a> — cpAQP1aa is a water-specific aquaporin from fish, expanding the diversity of characterized aquaporin family members
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp1/">Aquaporin-1 (AQP1)</a> — cpAQP1aa is a homolog of mammalian AQP1; bovine AQP1 structure (1J4N) used as molecular replacement model
- <a href="/xray-mp-wiki/proteins/other-ion-channels/so-pip2-1/">SoPIP2;1 (Spinach Plasma Membrane Aquaporin)</a> — Similar phosphorylation-dependent gating mechanism proposed for cpAQP1aa; loop D gating in SoPIP2;1 provides comparative model
- <a href="/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-4/">Human Aquaporin 4</a> — Used as functional comparison for water permeability measurements; hAQP4 has a fully open pore with higher water transport rate
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in the context of Glycerol
- <a href="/xray-mp-wiki/reagents/additives/methanol/">Methanol</a> — Referenced in the context of Methanol
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> — Referenced in the context of Tris Hcl
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> — Referenced in the context of MES
