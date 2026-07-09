---
title: "Stearoyl-CoA Desaturase-1 (hSCD1)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3049]
verified: regex
uniprot_id: O00767
---

# Stearoyl-CoA Desaturase-1 (hSCD1)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O00767">UniProt: O00767</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

[Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) desaturase-1 (SCD1) is an integral membrane enzyme in the endoplasmic reticulum that catalyzes the delta-9 desaturation of saturated fatty acyl-CoA substrates ([Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) and palmitoyl-CoA) to produce monounsaturated fatty acids ([Oleoyl-CoA](/xray-mp-wiki/reagents/ligands/oleoyl-coa/) and palmitoleoyl-CoA). SCD1 belongs to the di-iron-containing desaturase family but uses a unique histidine-coordinated dimetal center rather than the carboxylate-bridged [IRON](/xray-mp-wiki/reagents/additives/iron/) center found in soluble forms. SCD1 maintains the cellular balance of saturated and monounsaturated lipids and is implicated in metabolic diseases including diabetes, obesity, and cancer. Inhibitors of SCD1 are under active investigation as therapeutic agents.


## Publications

### doi/10.1038##nsmb.3049

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4zyo">4ZYO</a></td>
      <td>3.25</td>
      <td>P3_121</td>
      <td>N-terminal 45 residues truncated; K60A, K62A, E63A surface mutations; residues 53-350 in final model</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/stearoyl-coa/">Stearoyl-CoA</a>, 2 Zn2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: N-terminal hexahistidine tag with TEV protease cleavage site; N-term 45 truncated; K60A, K62A, E63A mutations
- **Notes**: SeMet labeling achieved by growing Sf9 cells in methionine-free medium with 70 mg/L SeMet before infection

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
      <td>solubilization</td>
      <td>membrane solubilization</td>
      <td>none</td>
      <td>25 mM Tris pH 7.6, 800 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.25 mM TCEP, 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes extracted from Sf9 cell pellets; solubilized with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA Superflow (Qiagen)</td>
      <td>25 mM Tris pH 7.6, 200 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.025% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.25 mM TCEP, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (elution)</td>
      <td>Eluted with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>tag cleavage</td>
      <td>TEV protease cleavage</td>
      <td>none</td>
      <td>25 mM Tris pH 7.6, 200 mM NaCl, 0.025% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.25 mM TCEP</td>
      <td>Hexahistidine tag cleaved by TEV protease</td>
    </tr>
    <tr>
      <td>flow-through purification</td>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (flow-through)</td>
      <td>Ni-NTA Superflow (Qiagen)</td>
      <td>25 mM Tris pH 7.2, 200 mM NaCl, 1 mM TCEP, 0.02% <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a></td>
      <td>Tag-free hSCD1 collected in flow-through after TEV cleavage</td>
    </tr>
    <tr>
      <td>desalting</td>
      <td>PD-10 column</td>
      <td>none</td>
      <td>25 mM Tris pH 7.2, 200 mM NaCl, 1 mM TCEP, 0.02% <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a></td>
      <td>Desalted using PD-10 column (GE Healthcare)</td>
    </tr>
    <tr>
      <td>size-exclusion chromatography</td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL (GE Healthcare)</td>
      <td>25 mM Tris pH 7.2, 200 mM NaCl, 1 mM TCEP, 0.02% <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a></td>
      <td>Final polishing step; peak fractions concentrated to 8.5 mg/ml</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>8.5 mg/ml hSCD1 in 25 mM Tris pH 7.2, 200 mM NaCl, 1 mM TCEP, 0.02% <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.5, 30-35% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 220 mM sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Both native and SeMet-labeled crystals; native crystals soaked in 1 mM Ta6Br12 overnight for phasing</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4zyo">4ZYO</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGSDIRPDIKD</span><span class="topo-outside">DIYDPTYADAAGPSPKVEYVWRNIIL</span><span class="topo-membrane">MSLLHLGALYGITLIP</span><span class="topo-inside">TCKF</span><span class="topo-membrane">YTWLWGVFYYFVSAL</span><span class="topo-outside">GITAGAHRLWSHRSYKAR</span><span class="topo-unknown">LPLRLFLIIANTM</span><span class="topo-outside">AFQNDVYEWARDHRAHH</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">KFSETHADPHNSRRGFFFSHVGWLLVRKHPAVKEKGSTLDLSDLEAE</span><span class="topo-unknown">KLVMFQRR</span><span class="topo-outside">YYKP</span><span class="topo-membrane">GLLMMCFILPTLVPWYF</span><span class="topo-inside">WGE</span><span class="topo-membrane">TFQNSVFVATFLRYAVVLNA</span><span class="topo-outside">TWLVNSAAHLFGYRPYDKNIS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310        </span>
<span class="topo-line"><span class="topo-outside">PREN</span><span class="topo-unknown">ILVSLG</span><span class="topo-outside">AVGEGFHNYHHSFPYDYSASEYRWHIN</span><span class="topo-unknown">FTTFFIDCMAA</span><span class="topo-outside">LGLAYDRKKVSKAAILARIKR</span><span class="topo-unknown">TGDGNYKSG</span></span>
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
      <td>12</td>
      <td>37</td>
      <td>53</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>53</td>
      <td>79</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>57</td>
      <td>95</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>72</td>
      <td>99</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>90</td>
      <td>114</td>
      <td>131</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>103</td>
      <td>132</td>
      <td>144</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>104</td>
      <td>167</td>
      <td>145</td>
      <td>208</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>175</td>
      <td>209</td>
      <td>216</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>176</td>
      <td>179</td>
      <td>217</td>
      <td>220</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>196</td>
      <td>221</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>199</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>219</td>
      <td>241</td>
      <td>260</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>244</td>
      <td>261</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>250</td>
      <td>286</td>
      <td>291</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>251</td>
      <td>277</td>
      <td>292</td>
      <td>318</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>288</td>
      <td>319</td>
      <td>329</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>289</td>
      <td>309</td>
      <td>330</td>
      <td>350</td>
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

### Mushroom-like architecture with transmembrane anchor

hSCD1 folds into a mushroom-like architecture consisting of a stem of four transmembrane
alpha-helices (TM stem) and a cytoplasmic domain (cap). The four transmembrane helices
form a tight hydrophobic core that presumably functions as an anchor spanning the
endoplasmic reticulum membrane. The cytoplasmic cap domain contains the catalytic center
and substrate binding site.

### Unique histidine-coordinated dimetal catalytic center

The hSCD1 structure reveals a new dimetal catalytic center coordinated by histidine
residues in histidine-box motifs (HXXXXH, HXXHH, HXXHH), rather than the carboxylate-
bridged di-[IRON](/xray-mp-wiki/reagents/additives/iron/) center found in soluble desaturases. Zn1 is coordinated by five
histidine residues, while Zn2 is coordinated by four histidine residues and a water
molecule. The dimetal center is buried among TM2, CH2, TM4, and CH8.

### Substrate binding site with hydrophobic tunnel

The [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) binding site is located at the surface of the cytoplasmic cap domain
with a prominent internal hydrophobic tunnel extending from the CoA-binding site toward
the dimetal center. The CoA head group interacts with polar residues via hydrogen bonds
and electrostatic interactions, while the acyl chain extends into the hydrophobic tunnel.
The tunnel geometry determines the regioselective cis dehydrogenation at the delta-9
position of the fatty acid chain.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent for membrane solubilization (1%) and Ni-NTA elution (0.025%)
- <a href="/xray-mp-wiki/reagents/detergents/c12e8/">Octaethylene Glycol Monododecyl Ether (C12E8)</a> — Final SEC detergent (0.02%) replacing DDM for improved resolution
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Primary buffer throughout purification (25 mM) and crystallization (100 mM)
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Ni-NTA affinity elution at 20 mM (solubilization) and 250 mM (elution)
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Included in Ni-NTA elution buffer (5%) for protein stabilization
- <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> — Cleaved N-terminal hexahistidine tag after affinity purification
- <a href="/xray-mp-wiki/reagents/additives/tcep/">Tris(2-carboxyethyl)phosphine (TCEP)</a> — Reducing agent (0.25-1 mM) in all purification buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase SEC Resin</a> — Final SEC polishing step using Superdex 200 10/300 GL column
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/iron/">IRON</a> — Additive used in purification or crystallization buffers
