---
title: "Orphan GPR52 (G Protein-Coupled Receptor 52)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-020-2019-0]
verified: false
---

# Orphan GPR52 (G Protein-Coupled Receptor 52)

## Overview

GPR52 is a class-A orphan G-protein-coupled receptor (GPCR) highly expressed in the brain, representing a promising therapeutic target for Huntington’s disease and psychiatric disorders. Unlike most GPCRs, GPR52 exhibits intrinsically high constitutive activity through a unique self-activation mechanism where extracellular loop 2 (ECL2) occupies the orthosteric binding pocket and operates as a built-in agonist. This study presents high-resolution structures of human GPR52 in three states: ligand-free (apo), Gs-coupled (fully active), and bound to the allosteric surrogate agonist c17. The receptor features a novel side pocket for ligand binding.

## Publications

### doi/10.1038##s41586-020-2019-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6lii">6LII</a></td>
      <td>2.90 A</td>
      <td>P 21 21 21</td>
      <td>GPR52-Rub-apo (<a href="/xray-mp-wiki/reagents/protein-tags/rubredoxin/">Rubredoxin</a> fusion in ICL3, residues 17-340, 7 stabilizing mutations)</td>
      <td>none (apo)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6li2">6LI2</a></td>
      <td>3.20 A</td>
      <td>I 41</td>
      <td>GPR52-Fla-apo (flavodoxin fusion in ICL3, residues 17-340, 7 stabilizing mutations)</td>
      <td>none (apo)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6li0">6LI0</a></td>
      <td>2.80 A</td>
      <td>P 21 21 21</td>
      <td>GPR52-c17 (<a href="/xray-mp-wiki/reagents/protein-tags/rubredoxin/">Rubredoxin</a> fusion, ligand-bound)</td>
      <td>c17 (allosteric surrogate agonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6li3">6LI3</a></td>
      <td>3.30 A</td>
      <td>none (cryo-EM)</td>
      <td>GPR52-mini-Gs-<a href="/xray-mp-wiki/reagents/antibodies/nb35/">Nb35</a> complex</td>
      <td>mini-Gs heterotrimer, <a href="/xray-mp-wiki/reagents/antibodies/nb35/">Nb35</a> <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Baculovirus/Sf9 insect cells (Bac-to-Bac system, Invitrogen)
- **Construct**: Human GPR52 residues 17-340. N-terminal HA signal peptide + Flag tag + [Bril](/xray-mp-wiki/reagents/protein-tags/bril/), TEV site, C-terminal 10xHis tag (3C-protease-removable). ICL3 replaced with [Rubredoxin](/xray-mp-wiki/reagents/protein-tags/rubredoxin/) (residues 235-263) or flavodoxin (residues 236-261). 7 stabilizing mutations: A130W, A264L, W278Q, C314P, S318A, N321D, V323T.

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
      <td>Cell culture and infection</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/sf9-expression-system/">Sf9</a> cells infected with baculovirus at 2x10^6 cells/ml, grown at 27C, harvested 48 h post-infection</td>
      <td>—</td>
      <td></td>
      <td>Used <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Bac-to-Bac</a> system</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Low-salt wash (10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 20 mM KCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a>, <a href="/xray-mp-wiki/reagents/additives/protease-inhibitor-cocktail/">protease inhibitors</a>) followed by high-salt wash (10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 20 mM KCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a>, <a href="/xray-mp-wiki/reagents/additives/protease-inhibitor-cocktail/">protease inhibitors</a>)</td>
      <td>—</td>
      <td></td>
      <td>For c17 cocrystallization, membranes incubated with 20 uM c17 for 3 h, then 2 mg/ml <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a>, 800 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 1.0% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, stirred 2.5 h at 4C</td>
      <td>—</td>
      <td></td>
      <td>c17 (20 uM) added for ligand-bound sample</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a> resin (Clontech), overnight batch binding at 4C</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a> resin</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 800 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 20 uM c17</td>
      <td>Washed with 15 CV buffer I, eluted with buffer II (40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>)</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC for complex formation and final purification using <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 10/300</a> column</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 10/300</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 1 uM <a href="/xray-mp-wiki/reagents/ligands/gdp/">GDP</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a></td>
      <td>GPR52 mixed with 1.2x mini-Gs and 1.5x <a href="/xray-mp-wiki/reagents/antibodies/nb35/">Nb35</a>; peak fractions pooled and concentrated</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase (LCP)</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified GPR52 (apo or with c17 ligand), ~30 mg/ml</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>GPR52-Rub-apo, GPR52-Fla-apo, and GPR52-c17 crystals grown in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a></td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo Em</a> single-particle analysis</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GPR52-mini-Gs-<a href="/xray-mp-wiki/reagents/antibodies/nb35/">Nb35</a> complex, ~2.5 mg/ml</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C (blotting)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected on FEI Titan Krios at 300 kV with Falcon III detector. 7,287 movies; 651,456 particles; nominal global resolution 3.3 A. Processed with RELION-3.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6li2">6LI2</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGIVNVS</span><span class="topo-inside">ERHSCPLGFGHYSVVDVCI</span><span class="topo-membrane">FETVVIVLLTFLIIAGNLTVIF</span><span class="topo-outside">VFHC</span><span class="topo-unknown">APL</span><span class="topo-outside">LHHYTTSY</span><span class="topo-membrane">FIQTMAYADLFVGVSCLVPTLSLL</span><span class="topo-inside">HYSTGVHESLTCQV</span><span class="topo-membrane">FGYIISVLKSVSMWCLACI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">SVDRYL</span><span class="topo-outside">AITKPLSYNQLVTPC</span><span class="topo-membrane">RLRICIILIWIYSCLIFL</span><span class="topo-inside">PSFFGWGKPGYHGDIFEWCATSWLTSAYFTG</span><span class="topo-membrane">FIVCLLYAPAAFVVCFTYFHIFK</span><span class="topo-outside">ICRQHTKMKKYTCTVCGYIYNPEDGDP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">DNGVNPGTDFKDIPDDWVCPLCGVGKDQFEEVEEYLM</span><span class="topo-membrane">VLFRITSVFYMLQLPYIIYF</span><span class="topo-inside">LLESSRVLDNPTLSF</span><span class="topo-membrane">LTTWLAISNSFCNPVIYAL</span><span class="topo-outside">SD</span><span class="topo-unknown">STFRLGLRRLSETMCTSCMEF</span><span class="topo-outside">LEV</span><span class="topo-unknown">LFQ</span></span>
<span class="topo-ruler">       370  </span>
<span class="topo-line"><span class="topo-unknown">GPHHHHHHHHHH</span></span>
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
      <td>8</td>
      <td>26</td>
      <td>23</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>48</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>52</td>
      <td>64</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>63</td>
      <td>71</td>
      <td>78</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>87</td>
      <td>79</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>101</td>
      <td>103</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>126</td>
      <td>117</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>141</td>
      <td>142</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>159</td>
      <td>157</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>190</td>
      <td>175</td>
      <td>205</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>213</td>
      <td>206</td>
      <td>228</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>277</td>
      <td>229</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>278</td>
      <td>297</td>
      <td>266</td>
      <td>285</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>312</td>
      <td>286</td>
      <td>300</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>313</td>
      <td>331</td>
      <td>301</td>
      <td>319</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>332</td>
      <td>333</td>
      <td>320</td>
      <td>321</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>354</td>
      <td>322</td>
      <td>602</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>355</td>
      <td>357</td>
      <td>603</td>
      <td>605</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6li0">6LI0</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GGIVN</span><span class="topo-inside">VSERHSCPLGFGHYSVVDVC</span><span class="topo-membrane">IFETVVIVLLTFLIIAGNLTVI</span><span class="topo-outside">FVFHCAPLLHHYTTSYF</span><span class="topo-membrane">IQTMAYADLFVGVSCLVPTLSLLHY</span><span class="topo-inside">STGVHE</span><span class="topo-membrane">SLTCQVFGYIISVLKSVSMWCLACI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">SV</span><span class="topo-outside">DRYLAITKPLSYNQLVTPCRLR</span><span class="topo-membrane">ICIILIWIYSCLIFLPSFFGWG</span><span class="topo-inside">KPGYHGDIF</span><span class="topo-unknown">EWCATS</span><span class="topo-inside">WLT</span><span class="topo-membrane">SAYFTGFIVCLLYAPAAFVVCFTYF</span><span class="topo-outside">HIFKICRQHTKEAKALIVYGSTTGNTEYTAE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TIARELADAGYEVDSRDAASVEAGGLFEGFDLVLLGCSTWGDDSIELQDDFIPLFDSLEETGAQGRKVACFGCGDSSWEYFCGAVDAIEEKLKNLGAEIVQDGLRIDGDPRAARDDIVGW</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460        </span>
<span class="topo-line"><span class="topo-outside">AHDVRGAIRRYLMVL</span><span class="topo-membrane">FRITSVFYMLQLPYIIYFLLESS</span><span class="topo-inside">RVLDNP</span><span class="topo-membrane">TLSFLTTWLAISNSFCNPVIYA</span><span class="topo-outside">LSD</span><span class="topo-unknown">STFRLGLRRLSETMCT</span><span class="topo-outside">S</span><span class="topo-unknown">CMEFLEVLFQGPHHHHHHHHHH</span></span>
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
      <td>6</td>
      <td>25</td>
      <td>21</td>
      <td>40</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>47</td>
      <td>41</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>64</td>
      <td>63</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>89</td>
      <td>80</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>95</td>
      <td>105</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>122</td>
      <td>111</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>144</td>
      <td>138</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>166</td>
      <td>160</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>175</td>
      <td>182</td>
      <td>190</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>181</td>
      <td>191</td>
      <td>196</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>182</td>
      <td>184</td>
      <td>197</td>
      <td>199</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>209</td>
      <td>200</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>210</td>
      <td>375</td>
      <td>225</td>
      <td>267</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>376</td>
      <td>398</td>
      <td>268</td>
      <td>290</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>399</td>
      <td>404</td>
      <td>291</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>405</td>
      <td>426</td>
      <td>297</td>
      <td>318</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>429</td>
      <td>319</td>
      <td>321</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>445</td>
      <td>322</td>
      <td>337</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>446</td>
      <td>446</td>
      <td>338</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6li3">6LI3</a> — Chain R (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNESRWTEWRILNMSSGIVNVSERHSCPLGFGHYSV</span><span class="topo-outside">VDVCI</span><span class="topo-membrane">FETVVIVLLTFLIIAGNLTVIF</span><span class="topo-inside">VFHCAPLLHHYTTSYF</span><span class="topo-membrane">IQTMAYADLFVGVSCLVPTLS</span><span class="topo-outside">LLHYSTGVHESL</span><span class="topo-membrane">TCQVFGYI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ISVLKSVSMWCLAC</span><span class="topo-inside">ISVDRYLAITKPLSYNQLVTPCRLRI</span><span class="topo-membrane">CIILIWIYSCLIFLPSFFGWG</span><span class="topo-outside">KPGYHGDIFEWCATSWLT</span><span class="topo-membrane">SAYFTGFIVCLLYAPAAFVVC</span><span class="topo-inside">FTYFHIFKICRQHTKEINDR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340</span>
<span class="topo-line"><span class="topo-inside">RARFPSH</span><span class="topo-unknown">EVDSSRETGHSPDRRYA</span><span class="topo-inside">MVLF</span><span class="topo-membrane">RITSVFYMLWLPYIIYFLLESS</span><span class="topo-outside">RVLDNP</span><span class="topo-membrane">TLSFLTTWLAISNSFCNPVIY</span><span class="topo-inside">SLSN</span><span class="topo-unknown">SVFRLGLRRLSETMC</span><span class="topo-inside">T</span><span class="topo-unknown">SCM</span></span>
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
      <td>37</td>
      <td>41</td>
      <td>37</td>
      <td>41</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>63</td>
      <td>42</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>79</td>
      <td>64</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>100</td>
      <td>80</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>112</td>
      <td>101</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>134</td>
      <td>113</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>160</td>
      <td>135</td>
      <td>160</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>181</td>
      <td>161</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>199</td>
      <td>182</td>
      <td>199</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>220</td>
      <td>200</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>247</td>
      <td>221</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>268</td>
      <td>265</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>290</td>
      <td>269</td>
      <td>290</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>291</td>
      <td>296</td>
      <td>291</td>
      <td>296</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>317</td>
      <td>297</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>321</td>
      <td>318</td>
      <td>321</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>336</td>
      <td>322</td>
      <td>336</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>337</td>
      <td>337</td>
      <td>337</td>
      <td>337</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6li3">6LI3</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">NSK</span><span class="topo-inside">TEDQRNEEKAQREANKKIEKQLQKDKQVYRATHRLLLLGADNSGKSTIVKQMRILH</span><span class="topo-unknown">GGSGG</span><span class="topo-inside">SGGTSGIFETKFQVDKVNFHMFDVGGQRDERRKWIQCFNDVTAIIFVVDSSDYNRL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QEALNLFKSIWNNRWLRTISVILFLNKQDLLAEKVLAGKSKIEDYFPEFARYTTPEDATPEPGEDPRVTRAKYFIRDEFLRISTASGDGRHYCYPHFTCAVDTENARRIFNDCRDIIQRM</span></span>
<span class="topo-ruler">        </span>
<span class="topo-line"><span class="topo-inside">HLRQYELL</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>4</td>
      <td>59</td>
      <td>9</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>248</td>
      <td>201</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6li3">6LI3</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MS</span><span class="topo-inside">ELDQLRQEAEQLKNQIRDARKACADATLSQITNNIDPVGRIQMRTRRTLRGHLAKIYAMHWGTDSRLLVSASQDGKLIIWDSYTTNKVHAIPLRSSWVMTCAYAPSGNYVACGGLDNI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CSIYNLKTREGNVRVSRELAGHTGYLSCCRFLDDNQIVTSSGDTTCALWDIETGQQTTTFTGHTGDVMSLSLAPDTRLFVSGACDASAKLWDVREGMCRQTFTGHESDINAICFFPNGNA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340</span>
<span class="topo-line"><span class="topo-inside">FATGSDDATCRLFDLRADQELMTYSHDNIICGITSVSFSKSGRLLLAGYDDFNCNVWDALKADRAGVLAGHDNRVSCLGVTDDGMAVATGSWDSFLKIWN</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>340</td>
      <td>3</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6li3">6LI3</a> — Chain G (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70 </span>
<span class="topo-line"><span class="topo-unknown">MASNN</span><span class="topo-inside">TASIAQARKLVEQLKMEANIDRIKVSKAAADLMAYCEAHAKEDPLLTPVPASENPFR</span><span class="topo-unknown">EKKFFSAIL</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>62</td>
      <td>6</td>
      <td>62</td>
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

### ECL2 functions as a built-in agonist (self-activation mechanism)

GPR52s 22-residue ECL2 folds into a small module occupying the orthosteric binding pocket, functioning as a built-in agonist. The second segment (residues 182-190) adopts an extended conformation with a short 3_10 helix that fits into the large hydrophobic cavity. Tyr185 packs against an aromatic cluster (Tyr281, Tyr284, Phe285 of TM6). A salt bridge between Lys182 and Asp188 stabilizes this conformation. This confers intrinsically high basal activity (~90% of maximal) without an external agonist.

### Gs-coupled active state and G-protein coupling interface

The [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of GPR52-mini-Gs-Nb35 at 3.3 A reveals the fully active state. TM6 moves outward by ~6 A vs the apo structure. The interface involves TM3, TM5-TM7 and the Ras-like domain of G-alpha-s. The DRY motif (Asp138-Arg139-Tyr317) rearranges: Arg139 stacks with Tyr391 of G-alpha-s, and Tyr317 rotates to lock TM6 in the active position.

### Novel allosteric ligand-binding side pocket

GPR52s orthosteric site is occupied by ECL2. The surrogate agonist c17 binds in a newly identified side pocket between ECL2 and TM1, TM2, and TM7, closer to TM4-TM6. This side pocket is less conserved than the orthosteric pocket. The unique position of Pro214(5.50) in TM5 prevents use of the consensus PIF motif for activation.

### Structural basis for orphan receptor understanding

GPR52 is the closest homologue of GPR21 (71% sequence identity). ECL2 is highly conserved between them, suggesting GPR21 may also self-activate. The structures enable modeling of other orphan receptors and provide a foundation for drug discovery targeting GPR52 for Huntingtons disease and psychiatric disorders.


## Cross-References

- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr/">G Protein-Coupled Receptor (GPCR)</a> — GPR52 is a class-A orphan GPCR
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-Maltopyranoside (DDM)</a> — Primary detergent for membrane protein solubilization
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — LCP matrix lipid for crystallization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — LCP method used for GPR52 crystallization
- <a href="/xray-mp-wiki/reagents/protein-tags/rubredoxin/">Rubredoxin</a> — Referenced in gpr52 text
- <a href="/xray-mp-wiki/reagents/antibodies/nb35/">Nb35</a> — Referenced in gpr52 text
- <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> — Referenced in gpr52 text
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">Bril</a> — Referenced in gpr52 text
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a> — Referenced in gpr52 text
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> — Referenced in gpr52 text
