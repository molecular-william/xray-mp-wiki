---
title: "Phosphatidylglycerol Phosphate Synthase PgsA from Staphylococcus aureus"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.crstbi.2021.11.005]
verified: regex
uniprot_id: P63756
---

# Phosphatidylglycerol Phosphate Synthase PgsA from Staphylococcus aureus

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P63756">UniProt: P63756</a>

<span class="expr-badge">Staphylococcus aureus</span>

## Overview

[Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol) phosphate synthase (PgsA) from Staphylococcus aureus (SaPgsA) is a membrane-embedded enzyme that catalyzes the conversion of cytidine diphosphate-diacylglycerol (CDP-DAG) and [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) 3-phosphate (G3P) into [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol) phosphate (PGP) and cytidine monophosphate (CMP). PgsA forms a homodimer and is essential for [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol) biosynthesis in bacteria. Mutations in pgsA are frequently associated with [Daptomycin](/xray-mp-wiki/reagents/ligands/daptomycin) resistance in pathogenic Gram-positive bacteria, making SaPgsA a potential antibacterial target.

## Publications

### doi/10.1016##j.crstbi.2021.11.005

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7drj">7DRJ</a></td>
      <td>2.5 A</td>
      <td>not specified</td>
      <td>Full-length SaPgsA, homodimer, 6 transmembrane helices per protomer</td>
      <td>phosphatidylglycerol phosphate (PGP)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7drk">7DRK</a></td>
      <td>3.0 A</td>
      <td>not specified</td>
      <td>Full-length SaPgsA, homodimer, 6 transmembrane helices per protomer</td>
      <td>cytidine diphosphate-diacylglycerol (CDP-DAG)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C41(DE3) or C43(DE3)
- **Construct**: Full-length SaPgsA with N-terminal His-tag, codon-optimized for E. coli expression

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
      <td>Cell culture and membrane preparation</td>
      <td>E. coli expression in Terrific Broth, <a href="/xray-mp-wiki/reagents/additives/iptg">IPTG</a> induction</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 200 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + --</td>
      <td>Induction at 37 C for 2-3 h or 16 C for 12-15 h; cells harvested by centrifugation</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>French press at 900-1000 bar, 4-5 passes</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 200 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + --</td>
      <td>Membrane fraction pelleted at 160,000xg for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 200 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + 1.5% beta-<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Solubilization for 2-3 h at 4 C</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Ni-NTA</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.5, 300 mM NaCl, 10% glycerin, 0.1% beta-<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> (wash); 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 0.05% beta-<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> (elution) + beta-<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Protein eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex 200</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 0.05% beta-<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> + beta-<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>SaPgsA eluted as dimer confirmed by <a href="/xray-mp-wiki/methods/quality-assessment/sec-mals">SEC-MALS</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SaPgsA reconstituted in <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a> LCP</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified in main text</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified in main text</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified in main text</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>SaPgsA-PGP complex (7DRJ) at 2.5 A resolution; SaPgsA-CDP-DAG complex (7DRK) at 3.0 A resolution. Initial phases solved by ab initio phasing with ARCIMBOLDO-LITE.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7drj">7DRJ</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSH</span><span class="topo-outside">MNI</span><span class="topo-membrane">PNQITVFRVVLIPVFILFAL</span><span class="topo-inside">VDFGFGNVSFLGGYEIRIELLI</span><span class="topo-membrane">SGFIFILASLSDFVDGYL</span><span class="topo-outside">ARKWNLVTNMGKFL</span><span class="topo-membrane">DPLADKLLVASALIVLVQ</span><span class="topo-inside">LGLT</span><span class="topo-membrane">N</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210  </span>
<span class="topo-line"><span class="topo-membrane">SVVAIIIIAREFAVTG</span><span class="topo-outside">LRLLQIEQGFVSAA</span><span class="topo-membrane">GQLGKIKTAVTMVAITWLLL</span><span class="topo-inside">GDPLATLIGLSL</span><span class="topo-membrane">GQILLYIGVIFTILSGIEYF</span><span class="topo-outside">YKGRDVFK</span><span class="topo-unknown">QK</span></span>
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
      <td>20</td>
      <td>-19</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>23</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>43</td>
      <td>4</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>65</td>
      <td>24</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>83</td>
      <td>46</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>97</td>
      <td>64</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>115</td>
      <td>78</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>119</td>
      <td>96</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>136</td>
      <td>100</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>150</td>
      <td>117</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>170</td>
      <td>131</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>182</td>
      <td>151</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>202</td>
      <td>163</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>210</td>
      <td>183</td>
      <td>190</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>212</td>
      <td>191</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7drj">7DRJ</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSH</span><span class="topo-outside">MNI</span><span class="topo-membrane">PNQITVFRVVLIPVFILFAL</span><span class="topo-inside">VDFGFGNVSFLGGYEIRIELLI</span><span class="topo-membrane">SGFIFILASLSDFVDGYL</span><span class="topo-outside">ARKWNLVTNMGKFL</span><span class="topo-membrane">DPLADKLLVASALIVLVQ</span><span class="topo-inside">LGLT</span><span class="topo-membrane">N</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210  </span>
<span class="topo-line"><span class="topo-membrane">SVVAIIIIAREFAVTGL</span><span class="topo-outside">RLLQIEQGFVSAA</span><span class="topo-membrane">GQLGKIKTAVTMVAITWLLL</span><span class="topo-inside">GDPLATLIGLSL</span><span class="topo-membrane">GQILLYIGVIFTILSGIEYF</span><span class="topo-outside">YKGR</span><span class="topo-unknown">DVFKQK</span></span>
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
      <td>20</td>
      <td>-19</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>23</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>43</td>
      <td>4</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>65</td>
      <td>24</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>83</td>
      <td>46</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>97</td>
      <td>64</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>115</td>
      <td>78</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>119</td>
      <td>96</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>137</td>
      <td>100</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>150</td>
      <td>118</td>
      <td>130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>170</td>
      <td>131</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>182</td>
      <td>151</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>202</td>
      <td>163</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>206</td>
      <td>183</td>
      <td>186</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>212</td>
      <td>187</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7drk">7DRK</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHM</span><span class="topo-outside">NIPNQ</span><span class="topo-membrane">ITVFRVVLIPVFILFAL</span><span class="topo-inside">VDFGFGNVSFLGGYEIRIELL</span><span class="topo-membrane">ISGFIFILASLSDFVDGYL</span><span class="topo-outside">ARKWNLVTNMGKFL</span><span class="topo-membrane">DPLADKLLVASALIVLVQ</span><span class="topo-inside">LGLT</span><span class="topo-membrane">N</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210  </span>
<span class="topo-line"><span class="topo-membrane">SVVAIIIIAREFAVT</span><span class="topo-outside">GLRLLQIEQGFVSAAGQ</span><span class="topo-membrane">LGKIKTAVTMVAITWLLL</span><span class="topo-inside">GDPLATLIGLSL</span><span class="topo-membrane">GQILLYIGVIFTILSGIE</span><span class="topo-outside">YFYKG</span><span class="topo-unknown">RDVFKQK</span></span>
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
      <td>21</td>
      <td>-19</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>26</td>
      <td>2</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>43</td>
      <td>7</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>64</td>
      <td>24</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>83</td>
      <td>45</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>97</td>
      <td>64</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>115</td>
      <td>78</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>119</td>
      <td>96</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>135</td>
      <td>100</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>152</td>
      <td>116</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>170</td>
      <td>133</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>182</td>
      <td>151</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>163</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>205</td>
      <td>181</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>212</td>
      <td>186</td>
      <td>192</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7drk">7DRK</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSH</span><span class="topo-outside">MNIPNQ</span><span class="topo-membrane">ITVFRVVLIPVFILFAL</span><span class="topo-inside">VDFGFGNVSFLGGYEIRIELL</span><span class="topo-membrane">ISGFIFILASLSDFVDGYL</span><span class="topo-outside">ARKWNLVTNMGKFL</span><span class="topo-membrane">DPLADKLLVASALIVLVQ</span><span class="topo-inside">LGLT</span><span class="topo-membrane">N</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210  </span>
<span class="topo-line"><span class="topo-membrane">SVVAIIIIAREFAVT</span><span class="topo-outside">GLRLLQIEQGFVSAAGQ</span><span class="topo-membrane">LGKIKTAVTMVAITWLLL</span><span class="topo-inside">GDPLATLIGLSL</span><span class="topo-membrane">GQILLYIGVIFTILSGIE</span><span class="topo-outside">YFYKG</span><span class="topo-unknown">RDVFKQK</span></span>
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
      <td>20</td>
      <td>-19</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>26</td>
      <td>1</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>43</td>
      <td>7</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>64</td>
      <td>24</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>83</td>
      <td>45</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>97</td>
      <td>64</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>98</td>
      <td>115</td>
      <td>78</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>119</td>
      <td>96</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>135</td>
      <td>100</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>152</td>
      <td>116</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>170</td>
      <td>133</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>171</td>
      <td>182</td>
      <td>151</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>200</td>
      <td>163</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>205</td>
      <td>181</td>
      <td>185</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>206</td>
      <td>212</td>
      <td>186</td>
      <td>192</td>
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

### Homodimeric structure with 6 transmembrane helices

SaPgsA forms a homodimer with two protomers related by a central pseudo two-fold symmetry axis. Each monomer contains six transmembrane alpha-helices (TM1-TM6) forming a compact fold. The dimer interface is stable in both detergent micelles (confirmed by [SEC-MALS](/xray-mp-wiki/methods/quality-assessment/sec-mals)) and the crystal lattice.

### Trifurcated amphipathic cavity for catalysis

The active site is embedded in a large intracellular trifurcated amphipathic cavity. The hydrophilic head groups of substrate/product occupy distinct pockets while the fatty acyl chains extend into membrane-exposed grooves. An elongated membrane-exposed surface groove accommodates the fatty acyl chains and opens a lateral portal for lipid entry and release.

### Bimetal zinc-binding catalytic center

A conserved DxxD motif (D57xxD60G61xxA64R65...G74xxxD78xxxD82) coordinates two zinc ions at the active site center. Zn1 is coordinated by Asp57, Asp78, Asp82 and the beta-phosphoryl moiety of CDP-DAG, while Zn2 is coordinated by Asp57, Asp60, Asp78 and the alpha-phosphoryl moiety. This bimetal center increases the pKa of surrounding residues, creating an acidic microenvironment to facilitate bond formation. The zinc binding mode closely resembles the physiologically relevant magnesium binding.

### Substrate-dependent conformational changes

The PGP-bound and CDP-DAG-bound structures reveal substrate-dependent conformational changes. In the PGP-bound state, the TM4-5 loop shifts toward TM6 by 1-3 A, expanding the CMP release channel (Channel 1) while diminishing the G3P entrance channel (Channel 2). In the CDP-DAG-bound state, the reverse occurs: Channel 1 closes while Channel 2 opens. This reversible seesaw-like movement facilitates the substrate entry and product release cycle during catalysis.

### Daptomycin resistance mutations cluster around active site

Eight [Daptomycin](/xray-mp-wiki/reagents/ligands/daptomycin) resistance-related mutations from clinical S. aureus, Streptococcus oralis, and Staphylococcus capitis strains were mapped onto the SaPgsA structure. Seven of eight tested mutants (V59D, V59N, G61S, A64V, K75N, K135E, S177F, D187E) exhibited reduced enzymatic activity compared to wild type, except A64V and D187E. Mutations V59, G61, and A64 are located on TM2 near the conserved helix kink essential for catalysis, within the DxxD motif. The clustering of resistance mutations around the active site suggests a trade-off mechanism where reduced PgsA activity lowers membrane anionic lipid content, conferring [Daptomycin](/xray-mp-wiki/reagents/ligands/daptomycin) resistance at the cost of reduced enzymatic function.

### Key catalytic residues identified

The 3-phosphoryl moiety of PGP is sandwiched between TM3 and TM5, interacting with Lys83, Arg110, Arg118, Lys137, and Tyr181. Mutations K83A, R110A, R118A, and K137A exhibited reduced activity. Tyr181A mutation increased activity by facilitating G3P entry. Thr138 on TM5 hydrogen bonds to the 2-hydroxyl of PGP; T138A showed slightly higher activity. For CDP-DAG binding, Asn5, Phe58, Arg65, and Lys135 directly interact with the substrate. N5A and R65A showed much lower activity in LCP but near wild-type activity in detergent, indicating their role in attracting CDP-DAG head group in the membrane environment.


## Cross-References

- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylglycerol-phosphate/">Phosphatidylglycerol Phosphate</a> — Product of SaPgsA enzymatic reaction
- <a href="/xray-mp-wiki/reagents/lipids/cytidine-diphosphate-diacylglycerol/">Cytidine Diphosphate Diacylglycerol</a> — Substrate of SaPgsA enzymatic reaction
- <a href="/xray-mp-wiki/reagents/additives/glycerol-3-phosphate/">Glycerol 3-Phosphate</a> — Second substrate of SaPgsA enzymatic reaction
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/">Phosphatidylglycerol</a> — Downstream product of PG biosynthesis pathway catalyzed by PgsA
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method used for SaPgsA structures
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (beta-DDM)</a> — Detergent used for SaPgsA solubilization and purification
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid component of LCP crystallization matrix
- <a href="/xray-mp-wiki/methods/quality-assessment/sec-mals">SEC-MALS</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> — Entity mentioned in text
