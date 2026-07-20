---
title: "AqpM (Aquaporin from Methanothermobacter marburgensis)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0509469102]
verified: agent
uniprot_id: Q9C4Z5
---

# AqpM (Aquaporin from Methanothermobacter marburgensis)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9C4Z5">UniProt: Q9C4Z5</a>

<span class="expr-badge">Methanothermobacter marburgensis str. marburg</span>

## Overview

AqpM is the aquaporin from the methanogenic archaeon Methanothermobacter marburgensis, the first structurally characterized archaeal aquaporin. The structure was determined to 1.68-Å resolution by X-ray crystallography, revealing AqpM as a member of a unique subdivision between water-selective aquaporins and water-plus-glycerol-conducting aquaglyceroporins. In AqpM, isoleucine (Ile187) replaces a key histidine residue found in the lumen of water channels (which becomes glycine in aquaglyceroporins). The selectivity filter, formed by R202, F62, I187, and the carbonyl oxygen of S196, has a diameter of 2.54 Å — intermediate between Aqp1 (1.86 Å) and GlpF (3.14 Å). The channel is occupied by water molecules with a single glycerol at the NPA region. Notably, AqpM exhibits extreme stability, maintaining activity after exposure to pH < 4.2, temperatures > 80°C, and resistance to SDS-PAGE dissociation, attributed to a larger monomer-monomer interface (3,629 Å²) than other aquaporins. The histidine-to-isoleucine substitution suggests possible adaptation for conducting larger, less polar permeants such as H₂S or CO₂, in addition to water.



## Publications

### doi/10.1073##pnas.0509469102

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2f2b">2F2B</a></td>
      <td>1.68 A</td>
      <td>P4₁2₁2</td>
      <td>Full-length AqpM from Methanothermobacter marburgensis with N-terminal 10-His tag removed by Factor Xa digestion</td>
      <td>Water and glycerol molecules in the channel; two octyl-β-D-glucoside (OG) detergent molecules (low-resolution structure only)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli, recombinant expression
- **Construct**: Full-length AqpM with N-terminal 10-His tag and Factor Xa cleavage site

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
      <td><a href="/xray-mp-wiki/methods/cell-lysis/french-press/">Microfluidizer</a> (3 cycles, 15,000–18,000 psi at 4°C)</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 300 mM NaCl, 1 mM PMSF</td>
      <td>Cells lysed in solubilization buffer</td>
    </tr>
    <tr>
      <td>Membrane recovery</td>
      <td><a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">Ultracentrifugation</a></td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 300 mM NaCl, 1 mM PMSF</td>
      <td>138,000 × g for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Solubilization in octyl-β-D-glucoside (<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>)</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 300 mM NaCl, 1 mM PMSF, 5.0% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
      <td>Incubated at 4°C for 3 h with stirring</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Immobilized metal affinity chromatography</a> (Co²⁺-Sepharose)</td>
      <td>Co²⁺-Sepharose</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 300 mM NaCl, 1.2% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 50 mM (wash) / 300 mM (elution) <a href="/xray-mp-wiki/reagents/buffers/imidazole/">imidazole</a></td>
      <td>Batch binding overnight at 4°C; elution with <a href="/xray-mp-wiki/reagents/buffers/imidazole/">imidazole</a> gradient</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td>Size-exclusion column</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.4, 100 mM NaCl, 1.2% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
      <td>After tag cleavage by Factor Xa, another <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) step was performed</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a> (<a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> screen)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified AqpM at ~10 mg/ml in 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.4, 100 mM NaCl, 1.2% OG</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 9.0, 100 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 4000</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22 °C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-3 days to appear, ~2 weeks to full size (200-300 μm along c axis)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> in reservoir</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Best crystals grew from protein samples dialyzed to avoid phase separation. Crystal form is tetragonal. Highest diffracting crystal grew in <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.5, 200 mM MgCl₂, 23% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 4000</a>. Data collected at ALS Beamline 8.3.1. Two structures determined: low-resolution (2.3 Å) from a crystal in the detergent-rich phase, and high-resolution (1.68 Å) from a dialyzed sample with no phase separation.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2f2b">2F2B</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MVSLTKR</span><span class="topo-membrane">CIAEFIGTFILVFFGAGS</span><span class="topo-inside">AAVTLMIASGGTSPNPFNIGIGLLGGLGDW</span><span class="topo-membrane">VAIGLAFGFAIAASIYALG</span><span class="topo-outside">NISG</span><span class="topo-unknown">CHINPAVTIGLWS</span><span class="topo-outside">VKKFPGREV</span><span class="topo-membrane">VPYIIAQLLGAAFGSFIF</span><span class="topo-inside">LQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CAGIGAATVGGLGATAPFPGISYWQA</span><span class="topo-membrane">MLAEVVGTFLLMITIMGI</span><span class="topo-outside">AVDERAPKGF</span><span class="topo-membrane">AGIIIGLTVAGIITTLG</span><span class="topo-inside">NIS</span><span class="topo-unknown">GSSLNPARTFGPYLN</span><span class="topo-inside">DMIFAGTDLWNYY</span><span class="topo-membrane">SIYVIGPIVGAVLAALTY</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-outside">QYLTS</span><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>8</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>55</td>
      <td>26</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>74</td>
      <td>56</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>78</td>
      <td>75</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>91</td>
      <td>79</td>
      <td>91</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>92</td>
      <td>100</td>
      <td>92</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>118</td>
      <td>101</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>146</td>
      <td>119</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>164</td>
      <td>147</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>174</td>
      <td>165</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>191</td>
      <td>175</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>194</td>
      <td>192</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>209</td>
      <td>195</td>
      <td>209</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>210</td>
      <td>222</td>
      <td>210</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>240</td>
      <td>223</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>245</td>
      <td>241</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>246</td>
      <td>246</td>
      <td>246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2f2b">2F2B</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MVSLTKR</span><span class="topo-membrane">CIAEFIGTFILVFFGAGS</span><span class="topo-inside">AAVTLMIASGGTSPNPFNIGIGLLGGLGDW</span><span class="topo-membrane">VAIGLAFGFAIAASIYALG</span><span class="topo-outside">NISG</span><span class="topo-unknown">CHINPAVTIGLWS</span><span class="topo-outside">VKKFPGREV</span><span class="topo-membrane">VPYIIAQLLGAAFGSFIF</span><span class="topo-inside">LQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CAGIGAATVGGLGATAPFPGISYWQA</span><span class="topo-membrane">MLAEVVGTFLLMITIMGI</span><span class="topo-outside">AVDERAPKGF</span><span class="topo-membrane">AGIIIGLTVAGIITTLG</span><span class="topo-inside">NIS</span><span class="topo-unknown">GSSLNPARTFGPYLN</span><span class="topo-inside">DMIFAGTDLWNYY</span><span class="topo-membrane">SIYVIGPIVGAVLAALTY</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-outside">QYLTS</span><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>8</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>55</td>
      <td>26</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>74</td>
      <td>56</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>78</td>
      <td>75</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>91</td>
      <td>79</td>
      <td>91</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>92</td>
      <td>100</td>
      <td>92</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>118</td>
      <td>101</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>146</td>
      <td>119</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>164</td>
      <td>147</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>174</td>
      <td>165</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>191</td>
      <td>175</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>194</td>
      <td>192</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>209</td>
      <td>195</td>
      <td>209</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>210</td>
      <td>222</td>
      <td>210</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>240</td>
      <td>223</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>245</td>
      <td>241</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>246</td>
      <td>246</td>
      <td>246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2f2b">2F2B</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MVSLTKR</span><span class="topo-membrane">CIAEFIGTFILVFFGAGS</span><span class="topo-inside">AAVTLMIASGGTSPNPFNIGIGLLGGLGDW</span><span class="topo-membrane">VAIGLAFGFAIAASIYALG</span><span class="topo-outside">NISG</span><span class="topo-unknown">CHINPAVTIGLWS</span><span class="topo-outside">VKKFPGREV</span><span class="topo-membrane">VPYIIAQLLGAAFGSFIF</span><span class="topo-inside">LQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CAGIGAATVGGLGATAPFPGISYWQA</span><span class="topo-membrane">MLAEVVGTFLLMITIMGI</span><span class="topo-outside">AVDERAPKGF</span><span class="topo-membrane">AGIIIGLTVAGIITTLG</span><span class="topo-inside">NIS</span><span class="topo-unknown">GSSLNPARTFGPYLN</span><span class="topo-inside">DMIFAGTDLWNYY</span><span class="topo-membrane">SIYVIGPIVGAVLAALTY</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-outside">QYLTS</span><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>8</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>55</td>
      <td>26</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>74</td>
      <td>56</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>78</td>
      <td>75</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>91</td>
      <td>79</td>
      <td>91</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>92</td>
      <td>100</td>
      <td>92</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>118</td>
      <td>101</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>146</td>
      <td>119</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>164</td>
      <td>147</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>174</td>
      <td>165</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>191</td>
      <td>175</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>194</td>
      <td>192</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>209</td>
      <td>195</td>
      <td>209</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>210</td>
      <td>222</td>
      <td>210</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>240</td>
      <td>223</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>245</td>
      <td>241</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>246</td>
      <td>246</td>
      <td>246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2f2b">2F2B</a> — Chain D (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MVSLTKR</span><span class="topo-membrane">CIAEFIGTFILVFFGAGS</span><span class="topo-inside">AAVTLMIASGGTSPNPFNIGIGLLGGLGDW</span><span class="topo-membrane">VAIGLAFGFAIAASIYALG</span><span class="topo-outside">NISG</span><span class="topo-unknown">CHINPAVTIGLWS</span><span class="topo-outside">VKKFPGREV</span><span class="topo-membrane">VPYIIAQLLGAAFGSFIF</span><span class="topo-inside">LQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CAGIGAATVGGLGATAPFPGISYWQA</span><span class="topo-membrane">MLAEVVGTFLLMITIMGI</span><span class="topo-outside">AVDERAPKGF</span><span class="topo-membrane">AGIIIGLTVAGIITTLG</span><span class="topo-inside">NIS</span><span class="topo-unknown">GSSLNPARTFGPYLN</span><span class="topo-inside">DMIFAGTDLWNYY</span><span class="topo-membrane">SIYVIGPIVGAVLAALTY</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-outside">QYLTS</span><span class="topo-unknown">E</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>8</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>55</td>
      <td>26</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>74</td>
      <td>56</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>78</td>
      <td>75</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>91</td>
      <td>79</td>
      <td>91</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>92</td>
      <td>100</td>
      <td>92</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>118</td>
      <td>101</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>146</td>
      <td>119</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>164</td>
      <td>147</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>174</td>
      <td>165</td>
      <td>174</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>191</td>
      <td>175</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>194</td>
      <td>192</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>209</td>
      <td>195</td>
      <td>209</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>210</td>
      <td>222</td>
      <td>210</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>240</td>
      <td>223</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>245</td>
      <td>241</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>246</td>
      <td>246</td>
      <td>246</td>
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

### Unique selectivity filter with Ile187 replaces conserved His in water channels

AqpM's selectivity filter is formed by R202, F62, I187, and the carbonyl oxygen of S196. The critical distinction is I187 replacing the highly conserved His residue found in all water-selective aquaporins (corresponding to H182 in Aqp1). This Ile substitution makes the filter wider (2.54 Å vs. 1.86 Å in Aqp1) and more hydrophobic, creating a channel that is intermediate between water-selective aquaporins and aquaglyceroporins. The hydrophobic nature of I187 reduces water conductance efficiency compared with Aqp1 while enabling possible conductance of less polar permeants.

### Archaeal aquaporins as a distinct subfamily within the aquaporin superfamily

AqpM establishes a unique subdivision between water-selective aquaporins and aquaglyceroporins. Like other archaeal aquaporins (AfAqp from A. fulgidus, MbAqp from M. barkeri), AqpM possesses aliphatic residues at the His/Gly position of the selectivity filter rather than the canonical His of water channels or Gly of glycerol channels. This suggests archaeal aquaporins form a distinct subfamily adapted to the unique lipid environments and physiological needs of archaea.

### Extreme thermostability from large monomer-monomer interface

AqpM exhibits remarkable stability, maintaining tetrameric integrity and activity after exposure to extreme pH (<4.2) and high temperature (>80°C), and resists dissociation in 14% SDS-PAGE. This stability correlates with the largest monomer-monomer interface among structurally characterized aquaporins (3,629 Å² vs. GlpF 3,060 Å², Aqp1 3,180 Å², AqpZ 3,340 Å²). The extended helix M1 and loop A (residues 33–51) make major contributions to this interface.

### Possible gas conductance: H₂S or CO₂ as additional permeants

The substitution of the polar His with hydrophobic Ile187 at the selectivity filter suggests adaptation for less polar permeants. M. marburgensis uses CO₂ as its sole carbon source and H₂S as the terminal electron acceptor, making these molecules candidates for AqpM conductance. The structural similarity of H₂S to H₂O and the intermediate channel diameter (2.54 Å) support the hypothesis that AqpM may function as a multifunctional channel for water and gas molecules, potentially representing a novel subclass of gas-conducting aquaporins.

### Architecture of the conserved NPA motifs and carbonyl ladder

AqpM contains the canonical aquaporin NPA (Asn-Pro-Ala) motifs (N82-P83-A84 from loop B and N199-P200-A201 from loop E). Each loop provides a ladder of four carbonyl oxygens from successive amino acids into the channel lumen, spaced ~2.8 Å apart, forming a helical set of hydrogen-bond acceptors. This carbonyl ladder, together with the NPA motifs and helix dipoles, establishes the electrostatic environment for water coordination and proton exclusion characteristic of the aquaporin family.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/">Aquaporin Family</a> — AqpM is a member of the aquaporin superfamily; first structurally characterized archaeal aquaporin
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aqp1/">Aquaporin-1</a> — Water-selective aquaporin used as comparison for selectivity filter dimensions and conductance
- <a href="/xray-mp-wiki/proteins/other-ion-channels/aquaporin-z/">Aquaporin Z (AqpZ)</a> — Bacterial water-specific aquaporin used for comparison of monomer-monomer interface
- <a href="/xray-mp-wiki/proteins/other-ion-channels/glpf/">GlpF (Glycerol Facilitator from E. coli)</a> — Aquaglyceroporin used as comparison for selectivity filter dimensions and tetramer stability
