---
title: "Heliorhodopsin (TaHeR) from Thermoplasmatales archaeon SG8-52-1"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-019-1604-6, doi/10.1038##s41598-022-17716-9]
verified: agent
uniprot_id: A0A151EDA9
---

# Heliorhodopsin (TaHeR) from Thermoplasmatales archaeon SG8-52-1

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A151EDA9">UniProt: A0A151EDA9</a>

<span class="expr-badge">Thermoplasmatales archaeon SG8-52-1</span>

## Overview

Heliorhodopsin (HeR) from an uncultured Thermoplasmatales archaeon SG8-52-1 (TaHeR) is a member of the heliorhodopsin family, a distinct class of microbial rhodopsins discovered through functional metagenomics. HeRs have seven predicted transmembrane helices and bind an all-trans retinal chromophore as in type-1 microbial rhodopsins, but exhibit less than 15% sequence identity with type-1 and type-2 rhodopsins and display the reverse orientation in the membrane. TaHeR does not function as a proton pump or ion channel; instead it exhibits a long-lived photoactivated state and is thought to function as a signalling photoreceptor. The 2.4 A crystal structure reveals an overall fold similar to bacteriorhodopsin, with a linear hydrophobic pocket for retinal binding, a unique polar-interaction network around the Schiff base, and an unexpected lateral fenestration above the beta-ionone ring that facilitates retinal uptake from the environment. A 1.97 A structure at pH 4.5 revealed a chloride anion in the Schiff base cavity (SBC) that substitutes for the neutralized Glu-108 counterion, and identified an intramolecular signaling pathway connecting the SBC to the extracellular A-B loop via conserved residues including His-23, Gln-26, and Trp-243.

## Publications

### doi/10.1038##s41586-019-1604-6

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6is6">6IS6</a></td>
      <td>2.4</td>
      <td>P212121</td>
      <td>Full-length TaHeR with N-terminal 6x His tag, expressed in E. coli C41(Rosetta)</td>
      <td>all-trans retinal (covalently bound via Schiff base to Lys238)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C41(Rosetta)
- **Construct**: Full-length TaHeR with N-terminal 6x His tag, codon-optimized for E. coli
- **Induction**: 1 mM IPTG for 20 h at 25 C
- **Media**: 10 uM all-trans retinal supplemented in culture

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
      <td>Cell disruption</td>
      <td>Sonication</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a>-HCl pH 7.5, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol">glycerol</a></td>
      <td>Cells were disrupted by sonication</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td><a href="/xray-mp-wiki/methods/purification/ultracentrifugation">Ultracentrifugation</a></td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a>-HCl pH 7.5, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol">glycerol</a></td>
      <td>Crude membrane fraction collected at 180,000g for 1 h</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a>-HCl pH 7.5, 150 mM NaCl, 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membrane fraction solubilized in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>-containing buffer</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose</td>
      <td>0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His-tag</a>ged TaHeR purified by <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">affinity chromatography</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> crystallization (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">in meso</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified TaHeR in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> solution, reconstituted into <a href="/xray-mp-wiki/reagents/lipids/monoolein/">monoolein</a>-based <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase)</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested directly and flash frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained by <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">in meso</a> crystallization. Data collected to 2.4 A resolution. Space group P212121. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">molecular replacement</a> using <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">bacteriorhodopsin</a> (PDB 1M0L) as search model after trimming side chains to alanine.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6is6">6IS6</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHTE</span><span class="topo-outside">NEEINFRKF</span><span class="topo-membrane">RIFNGIMGVIHLIQVFLVLYLS</span><span class="topo-inside">NNFSLPITVNKPVYNEITNSISPVAETLFSI</span><span class="topo-membrane">EIGPLVAMFLFISATAHILIATVLY</span><span class="topo-unknown">YRYVQNLK</span><span class="topo-outside">NHM</span><span class="topo-membrane">NPYRWFEYSISAS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FMIVIIAMLT</span><span class="topo-inside">TIYD</span><span class="topo-membrane">LGTLLALFTLTAVMNLMGLMMEL</span><span class="topo-outside">HNQTTQNTNW</span><span class="topo-membrane">TSYIIGCIAGFVPWIVIFI</span><span class="topo-inside">PLISAESVPDF</span><span class="topo-membrane">VIYIFISIAIFFNCFAINMYLQ</span><span class="topo-outside">YKKIGKWKNYLH</span><span class="topo-membrane">GEKVYIILS</span></span>
<span class="topo-ruler">       250         </span>
<span class="topo-line"><span class="topo-membrane">LVAKSALAWQVFA</span><span class="topo-inside">GTLRPM</span></span>
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
      <td>10</td>
      <td>18</td>
      <td>4</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>40</td>
      <td>13</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>41</td>
      <td>71</td>
      <td>35</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>96</td>
      <td>66</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>104</td>
      <td>91</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>105</td>
      <td>107</td>
      <td>99</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>130</td>
      <td>102</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>134</td>
      <td>125</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>157</td>
      <td>129</td>
      <td>151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>167</td>
      <td>152</td>
      <td>161</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>186</td>
      <td>162</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>197</td>
      <td>181</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>219</td>
      <td>192</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>231</td>
      <td>214</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>253</td>
      <td>226</td>
      <td>247</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>254</td>
      <td>259</td>
      <td>248</td>
      <td>253</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6is6">6IS6</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHTE</span><span class="topo-outside">NEEINFRKF</span><span class="topo-membrane">RIFNGIMGVIHLIQVFLVLYLS</span><span class="topo-inside">NNFSLPITVNKPVYNEITNSISPVAETLFSI</span><span class="topo-membrane">EIGPLVAMFLFISATAHILIATVLY</span><span class="topo-unknown">YRYVQNLK</span><span class="topo-outside">NHM</span><span class="topo-membrane">NPYRWFEYSISAS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FMIVIIAMLT</span><span class="topo-inside">TIYD</span><span class="topo-membrane">LGTLLALFTLTAVMNLMGLMMEL</span><span class="topo-outside">HNQTTQNTNW</span><span class="topo-membrane">TSYIIGCIAGFVPWIVIFI</span><span class="topo-inside">PLISAESVPDF</span><span class="topo-membrane">VIYIFISIAIFFNCFAINMYLQ</span><span class="topo-outside">YKKIGKWKNYLH</span><span class="topo-membrane">GEKVYIILS</span></span>
<span class="topo-ruler">       250         </span>
<span class="topo-line"><span class="topo-membrane">LVAKSALAWQVFA</span><span class="topo-inside">GTLRPM</span></span>
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
      <td>10</td>
      <td>18</td>
      <td>4</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>40</td>
      <td>13</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>41</td>
      <td>71</td>
      <td>35</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>96</td>
      <td>66</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>104</td>
      <td>91</td>
      <td>98</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>105</td>
      <td>107</td>
      <td>99</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>130</td>
      <td>102</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>134</td>
      <td>125</td>
      <td>128</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>157</td>
      <td>129</td>
      <td>151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>167</td>
      <td>152</td>
      <td>161</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>186</td>
      <td>162</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>197</td>
      <td>181</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>219</td>
      <td>192</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>231</td>
      <td>214</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>253</td>
      <td>226</td>
      <td>247</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>254</td>
      <td>259</td>
      <td>248</td>
      <td>253</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41598-022-17716-9

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7u55">7U55</a></td>
      <td>1.97</td>
      <td>P21212</td>
      <td>Full-length TaHeR with N-terminal 6x His tag</td>
      <td>all-trans retinal, chloride ion</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C41(Rosetta)
- **Construct**: Full-length TaHeR with N-terminal 6x His tag, codon-optimized for E. coli
- **Induction**: 1 mM IPTG for 20 h at 25 C
- **Media**: 10 uM all-trans retinal supplemented in culture

**Purification:**

- **Expression system**: [E. coli](/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/) C41(Rosetta)
- **Expression construct**: TaHeR-I51C mutant for EPR studies
- **Tag info**: N-terminal 6x His tag

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
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 300 mM NaCl, 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> (octylglucoside)</td>
      <td>Purification carried out in <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> detergent</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td>HisTrap 1 mL <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) column (GE Healthcare)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 300 mM NaCl, 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">imidazole</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
      <td>Elution with 20-500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">imidazole</a> gradient over 30 CV</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200</a> 10/300 GL (Cytiva)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 300 mM NaCl, 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a></td>
      <td>Fractions with A550/A280 > 0.7 combined for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">Bicelle crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified TaHeR at 7.5 mg/ml in OG, combined with <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a>s (2:1 ratio, final 5 mg/ml protein, 8% bicelle)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>26% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 3350</a>, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate">sodium phosphate</a> monobasic pH 4.5, 0.28 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate">ammonium sulfate</a>, 0.18 M <a href="/xray-mp-wiki/reagents/additives/1-6-hexanediol">1,6-hexanediol</a></td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>4 ul protein-<a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a> + 1.5 ul reservoir</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>307 K (34 C)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Several months</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>None - crystals flash frozen directly in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>First HeR crystallized via <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">bicelle</a>s. Large 50-100 um diamond-shaped crystals. <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion">Hanging drop vapor diffusion</a>. Data collected at APS beamline 23-ID-B. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">molecular replacement</a> using basic TaHeR (PDB 6IS6) at 1.97 A. Space group P21212.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7u55">7U55</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHTENEEI</span><span class="topo-outside">NFRK</span><span class="topo-membrane">FRIFNGIMGVIHLIQVFLVLYLS</span><span class="topo-inside">NNFSLPITVNKPVYNEITNSISPVAETLFSIEI</span><span class="topo-membrane">GPLVAMFLFISATAHILIATVLY</span><span class="topo-outside">YRYVQNLKNHM</span><span class="topo-membrane">NPYRWFEYSISAS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FMIVIIAML</span><span class="topo-inside">TTIYDL</span><span class="topo-membrane">GTLLALFTLTAVMNLMGLMMELH</span><span class="topo-outside">NQTTQNTN</span><span class="topo-membrane">WTSYIIGCIAGFVPWIVIFI</span><span class="topo-inside">PLISAESVPDF</span><span class="topo-membrane">VIYIFISIAIFFNCFAINMYLQYK</span><span class="topo-outside">KIGKWKNYLH</span><span class="topo-membrane">GEKVYIILS</span></span>
<span class="topo-ruler">       250         </span>
<span class="topo-line"><span class="topo-membrane">LVAKSALAWQVFA</span><span class="topo-inside">GTLRP</span><span class="topo-unknown">M</span></span>
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
      <td>13</td>
      <td>-5</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>17</td>
      <td>8</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>40</td>
      <td>12</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>41</td>
      <td>73</td>
      <td>35</td>
      <td>67</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>96</td>
      <td>68</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>107</td>
      <td>91</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>129</td>
      <td>102</td>
      <td>123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>135</td>
      <td>124</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>158</td>
      <td>130</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>166</td>
      <td>153</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>186</td>
      <td>161</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>197</td>
      <td>181</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>221</td>
      <td>192</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>231</td>
      <td>216</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>253</td>
      <td>226</td>
      <td>247</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>254</td>
      <td>258</td>
      <td>248</td>
      <td>252</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>259</td>
      <td>253</td>
      <td>253</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7u55">7U55</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHTENEEI</span><span class="topo-outside">NFRK</span><span class="topo-membrane">FRIFNGIMGVIHLIQVFLVLYLS</span><span class="topo-inside">NNFSLPITVNKPVYNEITNSISPVAETLFSIEI</span><span class="topo-membrane">GPLVAMFLFISATAHILIATVLY</span><span class="topo-outside">YRYVQNLKNHM</span><span class="topo-membrane">NPYRWFEYSISAS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FMIVIIAML</span><span class="topo-inside">TTIYDL</span><span class="topo-membrane">GTLLALFTLTAVMNLMGLMMELH</span><span class="topo-outside">NQTTQNTN</span><span class="topo-membrane">WTSYIIGCIAGFVPWIVIFI</span><span class="topo-inside">PLISAESVPDF</span><span class="topo-membrane">VIYIFISIAIFFNCFAINMYLQYK</span><span class="topo-outside">KIGKWKNYLH</span><span class="topo-membrane">GEKVYIILS</span></span>
<span class="topo-ruler">       250         </span>
<span class="topo-line"><span class="topo-membrane">LVAKSALAWQVFA</span><span class="topo-inside">GTLRP</span><span class="topo-unknown">M</span></span>
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
      <td>13</td>
      <td>-5</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>17</td>
      <td>8</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>40</td>
      <td>12</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>41</td>
      <td>73</td>
      <td>35</td>
      <td>67</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>96</td>
      <td>68</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>107</td>
      <td>91</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>129</td>
      <td>102</td>
      <td>123</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>135</td>
      <td>124</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>158</td>
      <td>130</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>166</td>
      <td>153</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>186</td>
      <td>161</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>197</td>
      <td>181</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>221</td>
      <td>192</td>
      <td>215</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>231</td>
      <td>216</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>253</td>
      <td>226</td>
      <td>247</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>254</td>
      <td>258</td>
      <td>248</td>
      <td>252</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>259</td>
      <td>253</td>
      <td>253</td>
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

### Overall fold similarity to bacteriorhodopsin

The overall fold of TaHeR is similar to [bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (BR), with seven transmembrane helices. However, there are notable differences: TM3 is kinked by a hydrogen bond between Ser114 and the carbonyl oxygen of Ser111 (instead of the Pro91 kink in BR), and TM7 is not kinked at Lys238 (contrast with the conserved kink in type-1 rhodopsins). Sequence identity between HeR and BR is less than 15%.

### Dimer interface

TaHeR forms a dimer in the crystal structure with an extensive interface of approximately 1800 A^2 per protomer. The dimer is stabilized by hydrogen bonds involving Glu186-Tyr48, Thr125-Asn44, and Thr131-Thr131' and Thr155-Thr155' interactions. HS-AFM analysis confirmed that HeR typically functions as a dimer in the lipid membrane.

### Lateral fenestration for retinal capture

An unexpected lateral fenestration between TM5 and TM6, located above the beta-ionone ring of the retinal chromophore, provides a direct pathway for retinal from the lipid environment to the binding pocket. This fenestration is critical for capturing exogenous retinal, since HeR-expressing organisms lack retinal biosynthetic pathways. The G171W mutant, which blocks the fenestration, showed no retinal regeneration, confirming the functional role of this feature.

### Unique retinal binding pocket

The retinal-binding pocket is a linear hydrophobic cavity lined by residues including Tyr109, Asn143, Phe203, Phe206, Ala113, and Met116. Despite the low sequence identity with type-1 rhodopsins, the residues accommodating the C11-C12 bond (Tyr109, Phe203, Phe206) similarly contribute to 13-cis isomerization. A conserved glycine (Gly146) near the beta-ionone ring increases planarity for red-shifted absorption, as in type-1 rhodopsins.

### Schiff base environment and polar-interaction network

The Schiff base (Lys238) forms a hydrogen bond with the counterion Glu108, which is surrounded by polar residues Ser112 and Ser234. A unique polar network includes His23, His82, Glu108, and Ser234 with a four-coordinated water molecule, providing a hydrophilic environment around the Schiff base. This is distinct from BR, where the equivalent region has hydrophobic/aromatic residues. The proton-accepting group (PAG) for M intermediate formation appears to be formed by the hydrogen-bonding network including water molecules, rather than a specific carboxylate or histidine residue.

### Functional characterization as signalling photoreceptor

TaHeR exhibits a photocycle with K, M, and O intermediates and a long-lived photoactivated state (tau approximately 1 s). No proton release from the protein is observed, and the protein does not function as a proton pump or ion channel. The long O intermediate lifetime is conserved across HeRs from bacteria, archaea, eukaryotes, and giant viruses, suggesting a conserved signalling photoreceptor function.

### Chloride binding at low pH in Schiff base cavity

The 1.97 A TaHeR structure at pH 4.5 revealed a chloride anion in the Schiff base cavity (SBC) that serves as a surrogate counterion to stabilize the protonated retinal Schiff base (RSBH+) when the primary counterion Glu-108 is neutralized by protonation at low pH. This is analogous to HeR 48C12, which accommodates acetate at pH 4.3. The chloride ion is hydrogen bonded to the RSBH+ through a water-mediated network. Under basic conditions (pH 8.0), the SBC contains only water molecules and the Glu-108 counterion. Most HeRs are predicted to accommodate exogenous anions as surrogate counterions under acidic conditions or when the counterion is mutated.

### Intramolecular signal transduction pathway

Comparison of TaHeR structures at pH 8.0 and pH 4.5 reveals a conserved intramolecular signaling pathway: (1) chloride/acetate binding in the SBC at low pH, (2) reorientation of His-23, (3) displacement of a water molecule adjacent to Ser-78, (4) disordering of Gln-26 and Trp-243 into two conformations. This pathway connects the SBC to the extracellular A-B loop, which shows a ~6 A shift at residue Ile-51 between the two structures. Similar changes are observed in HeR 48C12 between its pH 8.8 and pH 4.3 structures, suggesting a conserved signaling mechanism among HeRs.

### DEER spectroscopy reveals dimer-of-dimer assemblies

DEER (double electron-electron resonance) spectroscopy on spin-labelled TaHeR (I51C mutant with MTSL or IAP labels) revealed distance distributions indicating transient dimer-of-dimer assemblies. Two distance populations were observed at ~4.7 nm (dimer) and ~6.6 nm (dimer-of-dimers). Light irradiation and acidification increase the population of the 6.6 nm long-distance peak, suggesting pH- and light-dependent oligomerization. These dimer-of-dimer assemblies may be relevant for transducer protein binding in a sensory function, consistent with HS-AFM observations.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — Structural homolog with similar overall fold despite less than 15% sequence identity
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> — All-trans retinal chromophore covalently bound via Schiff base to Lys238
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/retinal-chromophore-conformation/">Retinal Chromophore Conformation</a> — Retinal configuration and isomerization in HeR compared to type-1 rhodopsins
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Structure solved by in meso crystallization in monoolein
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used in the lipidic cubic phase crystallization matrix
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used for solubilization and purification
- <a href="/xray-mp-wiki/methods/crystallization/bicelle-crystallization/">Bicelle Crystallization</a> — Low pH structure (1.97 A) solved using bicelle crystallization method
- <a href="/xray-mp-wiki/methods/quality-assessment/deer-spectroscopy/">DEER Spectroscopy</a> — DEER revealed pH- and light-dependent dimer-of-dimer assemblies of TaHeR
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/">Rhodopsin Photocycle</a> — TaHeR photocycle with K, M, and O intermediates characteristic of microbial rhodopsins
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> — MES buffer used in purification and crystallization at pH 6.5
