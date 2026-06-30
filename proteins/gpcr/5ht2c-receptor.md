---
title: "Human 5-HT2C Serotonin Receptor"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2018.01.001]
verified: false
---

# Human 5-HT2C Serotonin Receptor

## Overview

The 5-HT2C [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) receptor is a class A G protein-coupled receptor (GPCR) and a validated therapeutic target for anti-obesity medications (e.g., lorcaserin/Belviq), as well as a potential target for depression, schizophrenia, and drug addiction. The 5-HT2C receptor exhibits several RNA-edited isoforms, where the non-edited INI isoform displays high constitutive activity. Crystal structures of the 5-HT2C INI isoform were determined in complex with the polypharmacological agonist [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) (ERG) at 2.7 Å (PDB: 6BQG) and the selective inverse agonist ritanserin (RIT) at 2.8 Å (PDB: 6BQH), revealing the structural basis of GPCR polypharmacology. The structures reveal key differences in ligand binding modes, activation states, and microswitch conformations between the agonist-bound active-like state and the inverse agonist-bound inactive state.


## Publications

### doi/10.1016##j.cell.2018.01.001

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bqg">6BQG</a></td>
      <td>2.7</td>
      <td>unknown</td>
      <td>Human 5-HT2C INI isoform with thermostabilizing mutations, expressed in Sf9 insect cells, purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/CHS, crystallized in LCP, complexed with <a href="/xray-mp-wiki/reagents/ligands/ergotamine/">ERG</a> (ERG)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/ergotamine/">ERG</a> (ERG) — polypharmacological agonist</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bqh">6BQH</a></td>
      <td>2.8</td>
      <td>unknown</td>
      <td>Human 5-HT2C INI isoform with thermostabilizing mutations, expressed in Sf9 insect cells, purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/CHS, crystallized in LCP, complexed with ritanserin (RIT)</td>
      <td>Ritanserin (RIT) — selective inverse agonist</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: Human 5-HT2C INI isoform with thermostabilizing mutations. N-terminal HA signal sequence followed by [FLAG tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10xHis tag, and [TEV protease](/xray-mp-wiki/reagents/additives/tev-protease/) site.

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
      <td>Baculovirus infection of Sf9 insect cells</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Cells harvested 48 h post-infection</td>
    </tr>
    <tr>
      <td>Membrane preparation and solubilization</td>
      <td>Dounce homogenization and <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a></td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.5, 50 mM NaCl, 2 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, protease inhibitors + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (n-dodecyl-β-D-maltopyranoside) + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a> (<a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> hemisuccinate)</td>
      <td>Membranes solubilized for 2 h at 4°C</td>
    </tr>
    <tr>
      <td>TALON IMAC affinity purification</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">IMAC</a> resin (Clontech)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.5, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; elution with 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a></td>
      <td>Receptor eluted and concentrated</td>
    </tr>
    <tr>
      <td>TEV protease cleavage and FLAG purification</td>
      <td><a href="/xray-mp-wiki/reagents/enzymes/tev-protease">TEV</a> cleavage followed by <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag">FLAG</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">affinity chromatography</a></td>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag">FLAG</a> M1 agarose resin (Sigma)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.5, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag">FLAG</a> tag cleaved, receptor concentrated to ~30 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified 5-HT2C at ~30 mg/mL in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a>, reconstituted into <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>/<a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> (9:1) <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
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
      <td>Crystals harvested and flash-cooled in liquid nitrogen. Data collected at SSRF beamline BL17U1 (Shanghai) or APS GM/CA-CAT. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using 5-HT2B receptor (PDB: 4IB4) as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bqg">6BQG</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDGAPTSD</span><span class="topo-outside">GGRFKFPDGVQNWP</span><span class="topo-membrane">ALSIVIIIIMTIGGNILVIMAVSM</span><span class="topo-inside">EKKLHNAT</span><span class="topo-membrane">NYFLMSLAIADMLVGLLVMPLSLL</span><span class="topo-outside">AILYDYVWPLPRYLC</span><span class="topo-membrane">PVWISL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">DVLFSTASIMHLCAISLD</span><span class="topo-inside">RYVAIRNPIEH</span><span class="topo-unknown">SRF</span><span class="topo-inside">NSRT</span><span class="topo-membrane">KAIMKIAIVWAISIGVSVPIPVI</span><span class="topo-outside">GLRDEEKVFVNNTTCVLND</span><span class="topo-membrane">PNFVLIGSFVAFFIPLTIMVITYC</span><span class="topo-inside">LTIYVLRRQAADLEDNWE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">TLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKA</span><span class="topo-unknown">TPPKLEDKSPDSPE</span><span class="topo-inside">MKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLQAINNERKASKV</span><span class="topo-membrane">LGIVFFVFLI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450  </span>
<span class="topo-line"><span class="topo-membrane">MWCPFFITNILSVLC</span><span class="topo-outside">EKSCNQKL</span><span class="topo-membrane">MEKLLNVFVWIGYVNSGINPLVYTLF</span><span class="topo-inside">NKIYRRAFSNYLRCN</span><span class="topo-unknown">YKVEKKPGRPLEVLFQGPHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>14</td>
      <td>42</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>43</td>
      <td>43</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>67</td>
      <td>57</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>75</td>
      <td>81</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>99</td>
      <td>89</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>114</td>
      <td>113</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>138</td>
      <td>128</td>
      <td>151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>149</td>
      <td>152</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>152</td>
      <td>163</td>
      <td>165</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>153</td>
      <td>156</td>
      <td>166</td>
      <td>169</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>179</td>
      <td>170</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>198</td>
      <td>193</td>
      <td>211</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>222</td>
      <td>212</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>232</td>
      <td>236</td>
      <td>245</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>275</td>
      <td>1001</td>
      <td>1043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>289</td>
      <td>1044</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>290</td>
      <td>338</td>
      <td>1058</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>339</td>
      <td>350</td>
      <td>301</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>351</td>
      <td>375</td>
      <td>313</td>
      <td>337</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>376</td>
      <td>383</td>
      <td>338</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>409</td>
      <td>346</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>424</td>
      <td>372</td>
      <td>386</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>425</td>
      <td>452</td>
      <td>387</td>
      <td>414</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bqh">6BQH</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDGAPTSDGGR</span><span class="topo-outside">FKFPDGVQNW</span><span class="topo-membrane">PALSIVIIIIMTIGGNILVIMA</span><span class="topo-inside">VSMEKKLHNATNY</span><span class="topo-membrane">FLMSLAIADMLVGLLVMPLSLLAIL</span><span class="topo-outside">YDYVWPLPRY</span><span class="topo-membrane">LCPVWISL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">DVLFSTASIMHLCAISL</span><span class="topo-inside">DRYVAIRNPIEHSRFNSRTKAI</span><span class="topo-membrane">MKIAIVWAISIGVSVPIPVIGLR</span><span class="topo-outside">DEEKVFVNNTTC</span><span class="topo-membrane">VLNDPNFVLIGSFVAFFIPLTIMVITYC</span><span class="topo-inside">LTIYVLRRQAADLEDNWE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">TLNDNLKVIEKA</span><span class="topo-unknown">DNAAQ</span><span class="topo-inside">VKDALTKMRAAALDAQKAT</span><span class="topo-unknown">PPKLEDKSPDSPE</span><span class="topo-inside">MKDFRHGFDIL</span><span class="topo-unknown">VGQIDDALKLANEGKVKEAQAAAE</span><span class="topo-inside">QLKTTRNAYIQKYLQAINNERKASKV</span><span class="topo-membrane">LGIVFFVFLI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450  </span>
<span class="topo-line"><span class="topo-membrane">MWCPFFITNILSVLCE</span><span class="topo-outside">KSCNQKL</span><span class="topo-membrane">MEKLLNVFVWIGYVNSGINPLVYTL</span><span class="topo-inside">FNKIYRRAFSNYLRCNY</span><span class="topo-unknown">KVEKKPGRPLEVLFQGPHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>32</td>
      <td>14</td>
      <td>45</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>33</td>
      <td>42</td>
      <td>46</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>64</td>
      <td>56</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>65</td>
      <td>77</td>
      <td>78</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>91</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>112</td>
      <td>116</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>137</td>
      <td>126</td>
      <td>150</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>159</td>
      <td>151</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>182</td>
      <td>173</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>194</td>
      <td>196</td>
      <td>207</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>222</td>
      <td>208</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>232</td>
      <td>236</td>
      <td>245</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>252</td>
      <td>1001</td>
      <td>1020</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>253</td>
      <td>257</td>
      <td>1021</td>
      <td>1025</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>258</td>
      <td>276</td>
      <td>1026</td>
      <td>1044</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>289</td>
      <td>1045</td>
      <td>1057</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>290</td>
      <td>300</td>
      <td>1058</td>
      <td>1068</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>301</td>
      <td>324</td>
      <td>1069</td>
      <td>1092</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>325</td>
      <td>338</td>
      <td>1093</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>339</td>
      <td>350</td>
      <td>301</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>351</td>
      <td>376</td>
      <td>313</td>
      <td>338</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>377</td>
      <td>383</td>
      <td>339</td>
      <td>345</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>408</td>
      <td>346</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>425</td>
      <td>371</td>
      <td>387</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>426</td>
      <td>452</td>
      <td>388</td>
      <td>414</td>
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

### Distinct binding modes of ergotamine and ritanserin

[ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) (ERG) and ritanserin (RIT) bind to 5-HT2C with fundamentally different poses. ERG adopts a shallower binding pose within the TM helical bundle with its ergoline core sandwiched between helices III and VI, forming a salt bridge with D134^3.32. Its terminal benzyl moiety extends toward the extracellular loops. In contrast, RIT binds deeper in the receptor, with one of its 4-fluorophenyl groups forming tight π-π stacking interactions with W324^6.48 (the 'toggle switch'), I142^3.40, and F320^6.44 of the P-I-F motif. RIT's thiazolopyrimidine group extends toward helices II and VII. The deeper binding pose of RIT effectively prevents the conformational changes of key activation microswitches, stabilizing the inactive state and producing inverse agonism.

### Structural basis for RIT's 5-HT2 selectivity

Ritanserin shows selectivity for 5-HT2 receptors over other aminergic GPCRs. Key determinants include G218^5.42 and V354^7.39, which are exclusive to 5-HT2 receptors. The second 4-fluorophenyl group of RIT 'pushes' against the backbone of helix V at G218^5.42. Mutation G218A^5.42 attenuates RIT binding affinity more than 10-fold but only has modest effect on ERG affinity. W324^6.48 is a major determinant of RIT's binding mode, and mutations W324F^6.48 and W324Y^6.48 (preserving aromatic character) had substantially less effect on RIT binding compared to alanine substitution.

### P-I-F motif and toggle switch in inverse agonism

The P-I-F motif (P^5.50-I^3.40-F^6.44) and W^6.48 toggle switch are critical for RIT's inverse agonist activity. Mutations of W324^6.48 and F320^6.44 selectively abolish RIT's Gαq inverse agonism without affecting β-arrestin2 inverse agonist activity. The I142A^3.40 mutation also selectively abolishes RIT's Gαq inverse agonism, and I142F^3.40 transforms RIT into a Gαq partial agonist. These results support a model whereby RIT's 4-fluorophenyl moiety stabilizes an inactive state via interference with the toggle switch and trigger motif, and that these microswitch residues are critical for the Gαq activation process at 5-HT2C.

### Ergotamine polypharmacology across the aminergic GPCRome

ERG shows appreciable affinity (Ki < 10 µM) for nearly 70% of all human aminergic GPCRs with low or sub-nanomolar affinity for 15 receptors. The ergoline core is recognized by nine key residues across helices III, V, VI, and VII, eight of which have specific conserved amino acid properties. The cyclic tripeptide and benzyl substituents display only non-specific side-chain van der Waals contacts, tolerating high amino acid diversity. The conservation of a small aliphatic residue at the EL2 position (L209 in 5-HT2C) is critical for ERG binding across all receptors showing high ERG affinity.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/5ht2a-receptor/">Human 5-HT2A Receptor</a> — Closely related 5-HT2 family member; off-target for 5-HT2C agonists causing hallucinations
- <a href="/xray-mp-wiki/proteins/gpcr/5ht2b-receptor/">Human 5-HT2B Receptor</a> — Closely related 5-HT2 family member; ERG co-crystal structure (PDB: 4IB4) used as MR model
- <a href="/xray-mp-wiki/reagents/ligands/ergotamine/">Ergotamine</a> — Polypharmacological agonist co-crystallized with 5-HT2C (PDB: 6BQG)
- <a href="/xray-mp-wiki/reagents/ligands/ritanserin/">Ritanserin</a> — Selective inverse agonist co-crystallized with 5-HT2C (PDB: 6BQH)
- <a href="/xray-mp-wiki/reagents/ligands/serotonin/">Serotonin (5-Hydroxytryptamine)</a> — Endogenous ligand for 5-HT2C receptor
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent for membrane solubilization and purification
- <a href="/xray-mp-wiki/reagents/lipids/chs/">Cholesterol Hemisuccinate (CHS)</a> — Lipid additive for receptor stabilization during purification
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipidic cubic phase (LCP) host lipid for crystallization
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Method used in the study
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein mentioned in the study
