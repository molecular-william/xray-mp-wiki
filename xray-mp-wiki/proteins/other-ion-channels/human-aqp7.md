---
title: "Human Aquaporin 7 (AQP7)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2019.11.011]
verified: regex
uniprot_id: O14520
---

# Human Aquaporin 7 (AQP7)

<div class="expr-badges"><span class="expr-badge expr-p-pastoris">P. pastoris</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O14520">UniProt: O14520</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) 7 (AQP7) is an aquaglyceroporin highly expressed in adipocytes that facilitates [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) efflux and is crucial for lipid metabolism. Two X-ray structures of human AQP7 were determined at 1.9 A (PDB 6QZI) and 2.2 A (PDB 6QZJ) resolution. The structures reveal a tetrameric channel with five [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) molecules (G1-G5) in the conducting pore spanning the ar/R selectivity filter, NPA motifs, and cytoplasmic vestibule. Combined with molecular dynamics simulations, the study shows that AQP7 is highly permeable to water (Pf = 4.8 x 10^-14 cm^3/s) but [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) binding reduces water permeability by a factor of 2-4. [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) is conducted via a partly rotating movement, with the NPA region serving as a transition point.

## Publications

### doi/10.1016##j.str.2019.11.011

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6qzi">6QZI</a></td>
      <td>1.9 A</td>
      <td>I4</td>
      <td>Human AQP7 (residues 33-279) with N-terminal 6xHis-tag, expressed in Pichia pastoris</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> (5 molecules per monomer, G1-G5)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6qzj">6QZJ</a></td>
      <td>2.2 A</td>
      <td>I4</td>
      <td>Human AQP7 (residues 33-279) with N-terminal 6xHis-tag, expressed in Pichia pastoris</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> (5 molecules per monomer)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (yeast expression system)
- **Construct**: Human AQP7 residues 33-279 (full-length excluding N-terminal cytoplasmic domain) with N-terminal 6xHis-tag

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
      <td>Cell lysis and membrane preparation</td>
      <td>High-pressure homogenization and ultracentrifugation</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> pH 8.0, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> + --</td>
      <td>Cells disrupted by high-pressure homogenization; membranes isolated by centrifugation at 145,000g for 90 min at 4 C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> pH 8.0, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> + 1% n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membranes solubilized for 2 h at 4 C under gentle stirring</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA agarose</td>
      <td>Buffer A: 20 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> pH 8.0, 300 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.07% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a>. Wash: 10 mM then 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>. Elution: 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.07% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a> (octyl <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> neopentyl glycol)</td>
      <td>Protein loaded overnight in presence of 5 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> pH 7.5, 100 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.07% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a> + 0.07% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a></td>
      <td>Final polishing step; purity assessed by SDS-PAGE</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified AQP7 at 9 mg/mL in 0.07% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>85 mM Tris pH 8.0, 37% v/v <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 200, 0.80% v/v n-octyl-beta-D-glucopyranoside</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystal 1 (1.9 A): gradient increase of <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> to 20% in 5% increments before plunge freezing. Crystal 2 (2.2 A): 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> in mother liquor before plunge freezing</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Two crystals from the same drop were used for data collection at the P13 beamline at PETRA III, EMBL Hamburg. Crystal 1 was subjected to crude dehydration via <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> gradient. Both structures solved by molecular replacement. <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> molecules were modeled in the conducting pore, with G4 occupying two alternative positions (G4a, G4b) at the NPA region.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qzi">6QZI</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MVREF</span><span class="topo-membrane">LAEFMSTYVMMVFGLGSV</span><span class="topo-outside">AHMVLNKKYGSYL</span><span class="topo-membrane">GVNLGFGFGVTMGVHVAG</span><span class="topo-inside">RISG</span><span class="topo-unknown">AHMNAAVTFANCAL</span><span class="topo-inside">GRVPWRKF</span><span class="topo-membrane">PVYVLGQFLGSFLAAATIYSL</span><span class="topo-outside">FYTAILHFSGGQLMVTGPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ATAGIFATYLPDHMTLWRG</span><span class="topo-membrane">FLNEAWLTGMLQLCLFAI</span><span class="topo-inside">TDQENNPALPGT</span><span class="topo-membrane">EALVIGILVVIIGVSLG</span><span class="topo-outside">MNTG</span><span class="topo-unknown">YAINPSRDLPPRIF</span><span class="topo-outside">TFIAGWGKQVFSNGENWW</span><span class="topo-membrane">WVPVVAPLLGAYLGGIIY</span></span>
<span class="topo-ruler">       </span>
<span class="topo-line"><span class="topo-inside">LVFIGST</span></span>
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
      <td>5</td>
      <td>33</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>23</td>
      <td>38</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>36</td>
      <td>56</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>54</td>
      <td>69</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>58</td>
      <td>87</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>72</td>
      <td>91</td>
      <td>104</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>73</td>
      <td>80</td>
      <td>105</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>101</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>139</td>
      <td>134</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>157</td>
      <td>172</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>169</td>
      <td>190</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>186</td>
      <td>202</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>190</td>
      <td>219</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>204</td>
      <td>223</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>205</td>
      <td>222</td>
      <td>237</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>240</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>247</td>
      <td>273</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qzi">6QZI</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MVREF</span><span class="topo-membrane">LAEFMSTYVMMVFGLGSV</span><span class="topo-outside">AHMVLNKKYGSYL</span><span class="topo-membrane">GVNLGFGFGVTMGVHVAG</span><span class="topo-inside">RISG</span><span class="topo-unknown">AHMNAAVTFANCAL</span><span class="topo-inside">GRVPWRKF</span><span class="topo-membrane">PVYVLGQFLGSFLAAATIYSL</span><span class="topo-outside">FYTAILHFSGGQLMVTGPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ATAGIFATYLPDHMTLWRG</span><span class="topo-membrane">FLNEAWLTGMLQLCLFAI</span><span class="topo-inside">TDQENNPALPGT</span><span class="topo-membrane">EALVIGILVVIIGVSLG</span><span class="topo-outside">MNTG</span><span class="topo-unknown">YAINPSRDLPPRIF</span><span class="topo-outside">TFIAGWGKQVFSNGENWW</span><span class="topo-membrane">WVPVVAPLLGAYLGGIIY</span></span>
<span class="topo-ruler">       </span>
<span class="topo-line"><span class="topo-inside">LVFIGST</span></span>
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
      <td>5</td>
      <td>33</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>23</td>
      <td>38</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>36</td>
      <td>56</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>54</td>
      <td>69</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>58</td>
      <td>87</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>72</td>
      <td>91</td>
      <td>104</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>73</td>
      <td>80</td>
      <td>105</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>101</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>139</td>
      <td>134</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>157</td>
      <td>172</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>169</td>
      <td>190</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>186</td>
      <td>202</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>190</td>
      <td>219</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>204</td>
      <td>223</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>205</td>
      <td>222</td>
      <td>237</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>240</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>247</td>
      <td>273</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qzi">6QZI</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MVREF</span><span class="topo-membrane">LAEFMSTYVMMVFGLGSV</span><span class="topo-outside">AHMVLNKKYGSYL</span><span class="topo-membrane">GVNLGFGFGVTMGVHVAG</span><span class="topo-inside">RISG</span><span class="topo-unknown">AHMNAAVTFANCAL</span><span class="topo-inside">GRVPWRKF</span><span class="topo-membrane">PVYVLGQFLGSFLAAATIYSL</span><span class="topo-outside">FYTAILHFSGGQLMVTGPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ATAGIFATYLPDHMTLWRG</span><span class="topo-membrane">FLNEAWLTGMLQLCLFAI</span><span class="topo-inside">TDQENNPALPGT</span><span class="topo-membrane">EALVIGILVVIIGVSLG</span><span class="topo-outside">MNTG</span><span class="topo-unknown">YAINPSRDLPPRIF</span><span class="topo-outside">TFIAGWGKQVFSNGENWW</span><span class="topo-membrane">WVPVVAPLLGAYLGGIIY</span></span>
<span class="topo-ruler">       </span>
<span class="topo-line"><span class="topo-inside">LVFIGST</span></span>
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
      <td>5</td>
      <td>33</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>23</td>
      <td>38</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>36</td>
      <td>56</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>54</td>
      <td>69</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>58</td>
      <td>87</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>72</td>
      <td>91</td>
      <td>104</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>73</td>
      <td>80</td>
      <td>105</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>101</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>139</td>
      <td>134</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>157</td>
      <td>172</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>169</td>
      <td>190</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>186</td>
      <td>202</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>190</td>
      <td>219</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>204</td>
      <td>223</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>205</td>
      <td>222</td>
      <td>237</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>240</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>247</td>
      <td>273</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qzi">6QZI</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MVREF</span><span class="topo-membrane">LAEFMSTYVMMVFGLGSV</span><span class="topo-outside">AHMVLNKKYGSYL</span><span class="topo-membrane">GVNLGFGFGVTMGVHVAG</span><span class="topo-inside">RISG</span><span class="topo-unknown">AHMNAAVTFANCAL</span><span class="topo-inside">GRVPWRKF</span><span class="topo-membrane">PVYVLGQFLGSFLAAATIYSL</span><span class="topo-outside">FYTAILHFSGGQLMVTGPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ATAGIFATYLPDHMTLWRG</span><span class="topo-membrane">FLNEAWLTGMLQLCLFAI</span><span class="topo-inside">TDQENNPALPGT</span><span class="topo-membrane">EALVIGILVVIIGVSLG</span><span class="topo-outside">MNTG</span><span class="topo-unknown">YAINPSRDLPPRIF</span><span class="topo-outside">TFIAGWGKQVFSNGENWW</span><span class="topo-membrane">WVPVVAPLLGAYLGGIIY</span></span>
<span class="topo-ruler">       </span>
<span class="topo-line"><span class="topo-inside">LVFIGST</span></span>
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
      <td>5</td>
      <td>33</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>23</td>
      <td>38</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>36</td>
      <td>56</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>54</td>
      <td>69</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>58</td>
      <td>87</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>72</td>
      <td>91</td>
      <td>104</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>73</td>
      <td>80</td>
      <td>105</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>101</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>139</td>
      <td>134</td>
      <td>171</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>157</td>
      <td>172</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>169</td>
      <td>190</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>186</td>
      <td>202</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>190</td>
      <td>219</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>204</td>
      <td>223</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>205</td>
      <td>222</td>
      <td>237</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>240</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>247</td>
      <td>273</td>
      <td>279</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qzj">6QZJ</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">VREF</span><span class="topo-membrane">LAEFMSTYVMMVFGLGSV</span><span class="topo-inside">AHMVLNKKYGSYL</span><span class="topo-membrane">GVNLGFGFGVTMGVHVA</span><span class="topo-outside">GRISGA</span><span class="topo-unknown">HMNAAVTFANCA</span><span class="topo-outside">LGRVPWRKF</span><span class="topo-membrane">PVYVLGQFLGSFLAAATIYSL</span><span class="topo-inside">FYTAILHFSGGQLMVTGPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ATAGIFATYLPDHMTLWRG</span><span class="topo-membrane">FLNEAWLTGMLQLCLFAI</span><span class="topo-outside">TDQENNPALPGT</span><span class="topo-membrane">EALVIGILVVIIGVSLG</span><span class="topo-inside">MNT</span><span class="topo-unknown">GYAINPSRDLPPRIF</span><span class="topo-inside">TFIAGWGKQVFSNGENWW</span><span class="topo-membrane">WVPVVAPLLGAYLGGIIY</span></span>
<span class="topo-ruler">       </span>
<span class="topo-line"><span class="topo-outside">LVFIGS</span><span class="topo-unknown">T</span></span>
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
      <td>2</td>
      <td>5</td>
      <td>34</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>23</td>
      <td>38</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>36</td>
      <td>56</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>53</td>
      <td>69</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>59</td>
      <td>86</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>71</td>
      <td>92</td>
      <td>103</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>72</td>
      <td>80</td>
      <td>104</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>101</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>139</td>
      <td>134</td>
      <td>171</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>157</td>
      <td>172</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>169</td>
      <td>190</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>186</td>
      <td>202</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>189</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>204</td>
      <td>222</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>205</td>
      <td>222</td>
      <td>237</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>240</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>246</td>
      <td>273</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qzj">6QZJ</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">VREF</span><span class="topo-membrane">LAEFMSTYVMMVFGLGSV</span><span class="topo-inside">AHMVLNKKYGSYL</span><span class="topo-membrane">GVNLGFGFGVTMGVHVA</span><span class="topo-outside">GRISGA</span><span class="topo-unknown">HMNAAVTFANCA</span><span class="topo-outside">LGRVPWRKF</span><span class="topo-membrane">PVYVLGQFLGSFLAAATIYSL</span><span class="topo-inside">FYTAILHFSGGQLMVTGPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ATAGIFATYLPDHMTLWRG</span><span class="topo-membrane">FLNEAWLTGMLQLCLFAI</span><span class="topo-outside">TDQENNPALPGT</span><span class="topo-membrane">EALVIGILVVIIGVSLG</span><span class="topo-inside">MNT</span><span class="topo-unknown">GYAINPSRDLPPRIF</span><span class="topo-inside">TFIAGWGKQVFSNGENWW</span><span class="topo-membrane">WVPVVAPLLGAYLGGIIY</span></span>
<span class="topo-ruler">       </span>
<span class="topo-line"><span class="topo-outside">LVFIGS</span><span class="topo-unknown">T</span></span>
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
      <td>2</td>
      <td>5</td>
      <td>34</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>23</td>
      <td>38</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>36</td>
      <td>56</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>53</td>
      <td>69</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>59</td>
      <td>86</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>71</td>
      <td>92</td>
      <td>103</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>72</td>
      <td>80</td>
      <td>104</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>101</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>139</td>
      <td>134</td>
      <td>171</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>157</td>
      <td>172</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>169</td>
      <td>190</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>186</td>
      <td>202</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>189</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>204</td>
      <td>222</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>205</td>
      <td>222</td>
      <td>237</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>240</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>246</td>
      <td>273</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qzj">6QZJ</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">VREF</span><span class="topo-membrane">LAEFMSTYVMMVFGLGSV</span><span class="topo-inside">AHMVLNKKYGSYL</span><span class="topo-membrane">GVNLGFGFGVTMGVHVA</span><span class="topo-outside">GRISGA</span><span class="topo-unknown">HMNAAVTFANCA</span><span class="topo-outside">LGRVPWRKF</span><span class="topo-membrane">PVYVLGQFLGSFLAAATIYSL</span><span class="topo-inside">FYTAILHFSGGQLMVTGPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ATAGIFATYLPDHMTLWRG</span><span class="topo-membrane">FLNEAWLTGMLQLCLFAI</span><span class="topo-outside">TDQENNPALPGT</span><span class="topo-membrane">EALVIGILVVIIGVSLG</span><span class="topo-inside">MNT</span><span class="topo-unknown">GYAINPSRDLPPRIF</span><span class="topo-inside">TFIAGWGKQVFSNGENWW</span><span class="topo-membrane">WVPVVAPLLGAYLGGIIY</span></span>
<span class="topo-ruler">       </span>
<span class="topo-line"><span class="topo-outside">LVFIGS</span><span class="topo-unknown">T</span></span>
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
      <td>2</td>
      <td>5</td>
      <td>34</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>23</td>
      <td>38</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>36</td>
      <td>56</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>53</td>
      <td>69</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>59</td>
      <td>86</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>71</td>
      <td>92</td>
      <td>103</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>72</td>
      <td>80</td>
      <td>104</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>101</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>139</td>
      <td>134</td>
      <td>171</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>157</td>
      <td>172</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>169</td>
      <td>190</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>186</td>
      <td>202</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>189</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>204</td>
      <td>222</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>205</td>
      <td>222</td>
      <td>237</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>240</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>246</td>
      <td>273</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6qzj">6QZJ</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">VREF</span><span class="topo-membrane">LAEFMSTYVMMVFGLGSV</span><span class="topo-inside">AHMVLNKKYGSYL</span><span class="topo-membrane">GVNLGFGFGVTMGVHVA</span><span class="topo-outside">GRISGA</span><span class="topo-unknown">HMNAAVTFANCA</span><span class="topo-outside">LGRVPWRKF</span><span class="topo-membrane">PVYVLGQFLGSFLAAATIYSL</span><span class="topo-inside">FYTAILHFSGGQLMVTGPV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ATAGIFATYLPDHMTLWRG</span><span class="topo-membrane">FLNEAWLTGMLQLCLFAI</span><span class="topo-outside">TDQENNPALPGT</span><span class="topo-membrane">EALVIGILVVIIGVSLG</span><span class="topo-inside">MNT</span><span class="topo-unknown">GYAINPSRDLPPRIF</span><span class="topo-inside">TFIAGWGKQVFSNGENWW</span><span class="topo-membrane">WVPVVAPLLGAYLGGIIY</span></span>
<span class="topo-ruler">       </span>
<span class="topo-line"><span class="topo-outside">LVFIGS</span><span class="topo-unknown">T</span></span>
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
      <td>2</td>
      <td>5</td>
      <td>34</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>23</td>
      <td>38</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>36</td>
      <td>56</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>53</td>
      <td>69</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>59</td>
      <td>86</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>71</td>
      <td>92</td>
      <td>103</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>72</td>
      <td>80</td>
      <td>104</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>101</td>
      <td>113</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>139</td>
      <td>134</td>
      <td>171</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>157</td>
      <td>172</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>169</td>
      <td>190</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>186</td>
      <td>202</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>189</td>
      <td>219</td>
      <td>221</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>204</td>
      <td>222</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>205</td>
      <td>222</td>
      <td>237</td>
      <td>254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>240</td>
      <td>255</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>246</td>
      <td>273</td>
      <td>278</td>
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

### Glycerol conduction via rotating movement

The high-resolution AQP7 structures reveal five [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) molecules (G1-G5) in the pore. At the NPA region, [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) G4 adopts two alternative positions (G4a and G4b, refined to 45% and 55% occupancy), suggesting the NPA area serves as a transition point. The rotation of [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) molecules facilitates breaking of hydrogen bonds to allow movement along the pore, indicating a partly rotating conducting mechanism.

### Glycerol reduces water permeability

MD simulations showed that water permeability (Pf) of AQP7 is 4.8 x 10^-14 cm3/s in the absence of [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), similar to orthodox aquaporins. In the presence of [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), water permeability is reduced 2-4 fold (1.3-2.4 x 10^-14 cm3/s) due to competition for hydrogen-bonding sites. This explains the lower water permeability of AQP7 observed in cellular assays where [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) is present.

### AQP7 selectivity filter architecture

The ar/R selectivity filter of AQP7 has a diameter of 3.3 A, formed by Phe74, Tyr223, Gly222, and His92. Unlike other aquaglyceroporins ([GLPF](/xray-mp-wiki/proteins/other-ion-channels/glpf/), PfAQP), the Tyr223 hydroxyl group provides a hydrogen bond donor that orientates [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) uniquely. This structural feature contributes to AQP7 specificity for [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) over water. The PMF for [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) shows a maximum barrier of ~8 kJ/mol, lower than [GLPF](/xray-mp-wiki/proteins/other-ion-channels/glpf/), consistent with efficient permeation.

### Structural differences between AQP7 and AQP10

Comparison of AQP7 (pore diameter 3.3 A at selectivity filter) with AQP10 (pore diameter ~5 A at selectivity filter) reveals significant differences. AQP10 has a narrowing on the intracellular side that blocks [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) but permits water, and is regulated by pH-dependent gating via His80. In contrast, AQP7 has a narrower selectivity filter but constitutively open intracellular vestibule, explaining their different [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) transport activities.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary solubilization detergent for AQP7
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Substrate of AQP7; used as cryoprotectant and present in crystallization
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin</a> — AQP7 belongs to the aquaglyceroporin subfamily
- <a href="/xray-mp-wiki/methods/expression-systems/pichia-pastoris-expression/">Pichia pastoris Expression System</a> — AQP7 expressed in Pichia pastoris
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/">Molecular Dynamics Simulation</a> — MD simulations used to study water and glycerol permeation
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/other-ion-channels/glpf/">GLPF</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
