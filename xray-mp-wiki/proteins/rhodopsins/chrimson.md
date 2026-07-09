---
title: "Chrimson Channelrhodopsin"
created: 2018-09-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-018-06421-9]
verified: regex
uniprot_id: Q8L435
---

# Chrimson Channelrhodopsin

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8L435">UniProt: Q8L435</a>

<span class="expr-badge">Chlamydomonas noctigama</span>

## Overview

Chrimson is a red light-activated channelrhodopsin from the algae *Chlamydomonas noctigama* that represents the most red-shifted channelrhodopsin identified to date, with a peak absorption at 590 nm. The crystal structure was determined at 2.6 A resolution (PDB 5ZIH) (Oda et al., 2018), revealing a unique counterion configuration with protonated Glu165, polar residue distribution biased toward the beta-ionone ring, and tight retinal binding pocket packing. Chrimson resembles prokaryotic proton pumps in the retinal binding pocket while sharing similarity with other channelrhodopsins in the ion-conducting pore. Based on the structural insights, the ChrimsonSA mutant (S169A) was engineered with further red-shifted absorption beyond 605 nm, reduced blue-light sensitivity, and accelerated closing kinetics, making it a useful tool for dual-color optogenetic applications.

## Publications

### doi/10.1038##s41467-018-06421-9

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5zih">5ZIH</a></td>
      <td>2.6 A</td>
      <td>C 1 2 1</td>
      <td>C1Chrimson (Chlamydomonas noctigama Chrimson with N-terminal 79 residues replaced by CrChR1 residues 1-76), C-terminal TEV-EGFP-FLAG tag, expressed in Sf9 insect cells</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal">Retinal</a> (covalently bound via Schiff base to Lys283)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Sf9](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) insect cells ([Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system)
- **Construct**: C1Chrimson (N-terminal 1-79 swapped with CrChR1 1-76), C-terminal TEV-EGFP-FLAG tag

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
      <td>Expression</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus</a> infection of <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Sf9</a> cells (Sf900II medium, 27 C, 48 h); 100 uM all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">retinal</a> added at 24 h post-infection</td>
      <td>--</td>
      <td>150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.0, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a> + --</td>
      <td>Cells harvested 48 h post-infection; pellets disrupted by sonication; cell debris cleared at 10,000 x g; crude membrane collected by ultracentrifugation at 215,000 x g</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.0, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a> + 2.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.5% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Insoluble material removed by ultracentrifugation at 208,000 x g</td>
    </tr>
    <tr>
      <td>FLAG affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">ANTI-FLAG M2 Agarose</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>ANTI-FLAG M2 Agarose Affinity Gel (Sigma)</td>
      <td>150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.0, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Binding for 1.5 h; EGFP-FLAG tag cleaved by <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV protease</a> (homemade) on resin</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td>Not specified</td>
      <td>150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.0, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Peak fractions pooled and concentrated to 7.0 mg/ml for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>C1Chrimson at 7.0 mg/ml in 150 mM NaCl, 50 mM HEPES pH 7.0, 5% glycerol, 0.05% DDM, 0.01% CHS</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>4 weeks in the dark</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>No additional cryoprotectant needed (high PEG concentration); flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> at 2:3 protein-to-lipid ratio (w/w). 50 nl protein-LCP mixture per well, overlaid with 800 ul precipitant solution. Crystals harvested using microworms. Data collected at SPring-8 BL32XU; merged from multiple crystals using KAMO.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5zih">5ZIH</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSRRPWLLALALAVALAAGSAGASTGSDATVPVATQDGPDYVFHRAHERMLFQT</span><span class="topo-outside">SYTLENNGSVICIPNNGQCFCLAWLHSRGTPGEKIG</span><span class="topo-membrane">AQVCQWIAFSIAIALLTFYGF</span><span class="topo-unknown">SAWKA</span><span class="topo-inside">TCGW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">E</span><span class="topo-membrane">EVYVCCVEVLFVTLEIFKE</span><span class="topo-outside">FSSPATVYLSTGNHA</span><span class="topo-membrane">YCLRYFEWLLSCPVIL</span><span class="topo-inside">IKLSNLSGLKNDYSKRTMG</span><span class="topo-membrane">LIVSCVGMIVFGMAAGLA</span><span class="topo-outside">TDWL</span><span class="topo-membrane">KWLLYIVSCIYGGYMYF</span><span class="topo-inside">QAAKCYVEANH</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       </span>
<span class="topo-line"><span class="topo-inside">SVPKGHCRMVVKLM</span><span class="topo-membrane">AYAYFASWGSYPILWAVG</span><span class="topo-outside">PEGLLKLSPYA</span><span class="topo-membrane">NSIGHSICDIIA?EFWTF</span><span class="topo-inside">LAHHLRIKIHEHILIHGDIRKTTKMEIGGEEVEVEEF</span><span class="topo-unknown">VEEEDEDTV</span></span>
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
      <td>55</td>
      <td>90</td>
      <td>58</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>111</td>
      <td>94</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>121</td>
      <td>120</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>140</td>
      <td>125</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>155</td>
      <td>144</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>171</td>
      <td>159</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>190</td>
      <td>175</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>208</td>
      <td>194</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>212</td>
      <td>212</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>229</td>
      <td>216</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>254</td>
      <td>233</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>258</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>283</td>
      <td>276</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>301</td>
      <td>287</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>338</td>
      <td>305</td>
      <td>341</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5zih">5ZIH</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSRRPWLLALALAVALAAGSAGASTGSDATVPVATQDGPDYVFHRAHERM</span><span class="topo-outside">LFQTSYTLENNGSVICIPNNGQCFCLAWLHSRGTPGEKIG</span><span class="topo-membrane">AQVCQWIAFSIAIALLTFYGF</span><span class="topo-inside">S</span><span class="topo-unknown">AWK</span><span class="topo-inside">ATCGW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">E</span><span class="topo-membrane">EVYVCCVEVLFVTLEIFKE</span><span class="topo-outside">FSSPATVYLSTGNHA</span><span class="topo-membrane">YCLRYFEWLLSCPVIL</span><span class="topo-inside">IKLSNLSGLKNDYSKRTMG</span><span class="topo-membrane">LIVSCVGMIVFGMAAGLA</span><span class="topo-outside">TDW</span><span class="topo-membrane">LKWLLYIVSCIYGGYMYF</span><span class="topo-inside">QAAKCYVEANH</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       </span>
<span class="topo-line"><span class="topo-inside">SVPKGHCRMVVKLM</span><span class="topo-membrane">AYAYFASWGSYPILWAVG</span><span class="topo-outside">PEGLLKLSPYA</span><span class="topo-membrane">NSIGHSICDIIA?EFWTF</span><span class="topo-inside">LAHHLRIKIHEHILIHGDIRKTTKMEIGGEEVEVEEF</span><span class="topo-unknown">VEEEDEDTV</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>51</td>
      <td>90</td>
      <td>54</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>111</td>
      <td>94</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>112</td>
      <td>115</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>119</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>140</td>
      <td>125</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>155</td>
      <td>144</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>171</td>
      <td>159</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>190</td>
      <td>175</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>208</td>
      <td>194</td>
      <td>211</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>211</td>
      <td>212</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>229</td>
      <td>215</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>254</td>
      <td>233</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>272</td>
      <td>258</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>283</td>
      <td>276</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>301</td>
      <td>287</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>302</td>
      <td>338</td>
      <td>305</td>
      <td>341</td>
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

### Unique counterion configuration enables red-shifted absorption

Chrimson's red-shifted absorption is partly due to protonation of the counterion residue Glu165, which weakens the stabilization of the protonated retinal Schiff base (PSB). Glu165 is in 3.0 A proximity to the PSB, while Asp295 is at 3.6 A. The two counterion residues are only 3.3 A apart, suggesting the Glu165 proton may be partly shared by both residues via hydrogen bond interactions. This configuration is similar to the acidic form of bacteriorhodopsin (BR605).

### Chrimson resembles prokaryotic proton pumps in the retinal binding pocket

About half of the residues constituting the retinal binding pocket are substituted in Chrimson compared to C1C2. Chrimson resembles bacteriorhodopsin rather than C1C2 in the residues surrounding the polyene chain and beta-ionone ring. Polar residues (Ser223, Tyr231) near the beta-ionone ring create biased polarity distribution, stabilizing the light-excited intermediate and contributing to the red-shifted absorption.

### Tight retinal packing by Met201 controls kinetics and absorption

The bulky side chain of Met201 tightly packs against the polyene chain of retinal. The M201T mutation causes a large blue-shift (50-80 nm) and extremely slow closing kinetics with photocurrents sustained for minutes, indicating that structural rigidity around the beta-ionone ring is crucial for proper photocycle kinetics. This is reminiscent of the step-function opsin (SFO) mutants in CrChRs.

### Outer gate and proton selectivity

The extracellular ion pore of Chrimson is occluded by an outer gate formed by Arg162 and Asn287, which separates a buried cluster of carboxylate residues (Glu132, Glu139, Glu300) from the extracellular solvent. Mutations destabilizing the outer gate (R162H, N287E, E139Q) cause largely blue-shifted activation spectra and altered ion permeability. The R162H mutant becomes permeable to guanidinium, suggesting Arg162 is part of the ion selectivity filter.

### Three constriction sites form the ion pore gates

Chrimson's ion-conducting pore is formed by TM2, TM3, TM6, and TM7, lined by five glutamic acid residues (Glu124-E5). Three constriction sites restrict ion permeation in the dark state: the inner gate (Lys176, Arg310), the central gate adjacent to the retinal Schiff base (Ser102, Glu129, Glu132), and the outer gate (Arg162, Asn287). The inner gate lacks the histidine-mediated ionic interaction seen in C1C2 and CrChR2.

### ChrimsonSA (S169A) engineered for dual-color optogenetics

Based on structural insights, the ChrimsonSA mutant (S169A) was engineered with peak absorption shifted beyond 605 nm, significantly reduced blue-light sensitivity, and accelerated closing kinetics. ChrimsonSA expressed well in hippocampal neurons and allowed spiking with red light while reducing blue-light-evoked action potentials, making it a useful tool for dual-color optogenetic applications.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent (2.5% solubilization, 0.05% purification) for membrane protein isolation
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — Stabilizing additive (0.5% solubilization, 0.01% purification) used with DDM
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> — Buffer (50 mM, pH 7.0) used throughout purification and crystallization
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> — Salt (150 mM) included in purification and SEC buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Stabilizer (5%) used in purification buffers
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used for LCP crystallization matrix (2:3 protein-to-lipid ratio)
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">All-trans Retinal</a> — Chromophore covalently bound to Lys283 via Schiff base
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — LCP method used for Chrimson crystallization
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> — Protein expressed in Sf9 cells using baculovirus system
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Sf9 Insect Cells</a> — Expression host for recombinant Chrimson production
- <a href="/xray-mp-wiki/proteins/rhodopsins/channelrhodopsin-c1c2/">Channelrhodopsin C1C2</a> — Chimeric channelrhodopsin used for structural comparison with Chrimson
- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — Chrimson resembles BR in retinal binding pocket architecture
- <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> — FLAG tag used for affinity purification via ANTI-FLAG M2 Agarose
- <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> — Used to cleave EGFP-FLAG tag during purification
- <a href="/xray-mp-wiki/reagents/additives/pmsf/">Phenylmethylsulfonyl Fluoride (PMSF)</a> — Protease inhibitor (0.1 mM) included in purification buffers
