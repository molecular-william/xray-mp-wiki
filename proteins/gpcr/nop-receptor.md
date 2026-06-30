---
title: "Nociceptin/Orphanin FQ Peptide Receptor (NOP)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11085, doi/10.1016##j.str.2015.07.024]
verified: false
---

# Nociceptin/Orphanin FQ Peptide Receptor (NOP)

## Overview

The nociceptin/orphanin FQ peptide receptor (NOP), also known as ORL-1, is a member of the opioid receptor subfamily of GPCRs. NOP is a key drug target due to its roles in pain transmission, drug addiction, anxiety, and locomotor and mood disorders. The first X-ray crystal structure of the human NOP receptor was determined at 3.0 A resolution in complex with the peptide mimetic antagonist C-24 (Thompson et al., Nature 2012, PDB 4EA3), revealing an antagonist-bound inactive conformation with a large solvent-exposed orthosteric binding pocket. The receptor was subsequently crystallized in complex with antagonists SB-612111 and C-35 using lipidic cubic phase (LCP) crystallization, also to 3.0 A resolution. A strong correlation between antagonist potency (pKB) and receptor thermostability (Tm) was demonstrated, providing a high-throughput strategy for identifying GPCR ligands for crystallization. Docking studies revealed that potent, stabilizing antagonists like SB-612111 favor a single binding orientation, while less potent ligands can adopt multiple binding modes, contributing to reduced receptor stabilization.

## Publications

### doi/10.1038##nature11085

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ea3">4EA3</a></td>
      <td>3.0</td>
      <td>P21</td>
      <td>BRIL-ΔN-NOP-ΔC fusion with N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> (apocytochrome b562 RIL), N-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> (ΔN), C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> (ΔC); expressed in Sf9 insect cells</td>
      <td>C-24 (peptide mimetic antagonist; Banyu Compound-24)</td>
    </tr>
  </tbody>
</table>
 - R-work 24.8%, R-free 28.8%; Atoms: 3946 protein atoms (molecule A: 2113, molecule B: 2081), 64 ligand atoms (32 per molecule), 59 lipid/water atoms; Data collection: Merged from 23 crystals at 3.0 A resolution; space group P21 with two molecules in asymmetric unit

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells; baculovirus expression system
- **Construct**: Human NOP receptor with N-terminal [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion; N-terminal and C-terminal truncations for crystallogenesis

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
      <td>Protein expression</td>
      <td>Baculovirus infection of Sf9 insect cells</td>
      <td></td>
      <td></td>
      <td>BRIL-ΔN-NOP-ΔC construct expressed in Sf9 cells; harvested 48 h post-infection</td>
    </tr>
    <tr>
      <td>Membrane preparation and solubilization</td>
      <td>Homogenization and solubilization in detergent</td>
      <td></td>
      <td>20 mM HEPES pH 7.5, 500 mM NaCl, 30% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1.0% lauryl <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> neopentyl glycol (MNG), 0.3% <a href="/xray-mp-wiki/reagents/detergents/sodium-cholate/">Sodium Cholate</a>, 0.03% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> hemisuccinate (<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> present during solubilization; <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> used for cysteine blocking</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC resin</td>
      <td>20 mM HEPES pH 7.5, 500 mM NaCl, 0.1% MNG, 0.03% <a href="/xray-mp-wiki/reagents/detergents/sodium-cholate/">Sodium Cholate</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.1% MNG, 0.03% <a href="/xray-mp-wiki/reagents/detergents/sodium-cholate/">Sodium Cholate</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
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
      <td>Purified BRIL-NOP-ΔC construct in complex with C-24</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in LCP using <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>/cholesterol mix. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a>. 23 crystals merged for final dataset. Data collected at wavelength 1.0330 A. Two NOP molecules per asymmetric unit (antiparallel) with one <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> domain forming crystal lattice contacts with receptors from an adjacent layer.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ea3">4EA3</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDGAPADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLGAFL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PLGL</span><span class="topo-membrane">KVTIVGLYLAVCVGGLLGNCLVMY</span><span class="topo-outside">VILRHTKMKTATNIY</span><span class="topo-membrane">IFNLALADTLVLLTLPFQGTDI</span><span class="topo-inside">LLGFWPF</span><span class="topo-membrane">GNALCKTVIAIDYYNMFTSTFTLTA</span><span class="topo-outside">MSVDRYVAICHP</span><span class="topo-unknown">IRALDVR</span><span class="topo-outside">TSSK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">AQAV</span><span class="topo-membrane">NVAIWALASVVGVPVAIMGS</span><span class="topo-inside">AQVEDEEIECLVEIPTPQ</span><span class="topo-membrane">DYWGPVFAICIFLFSFIVPVLVIS</span><span class="topo-outside">VCYSLMIRRLRGVRLLSGSREKDRNLRRITRLVL</span><span class="topo-membrane">VVVAVFVGCWTPVQVFVLAQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430    </span>
<span class="topo-line"><span class="topo-membrane">GLGVQP</span><span class="topo-inside">SSET</span><span class="topo-membrane">AVAILRFCTALGYVNSCLNPILYA</span><span class="topo-outside">FLD</span><span class="topo-unknown">ENFKACF</span><span class="topo-outside">R</span><span class="topo-unknown">KFCCASALGRPLEVLFQGPHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>120</td>
      <td>-73</td>
      <td>46</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>121</td>
      <td>124</td>
      <td>47</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>148</td>
      <td>51</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>163</td>
      <td>75</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>185</td>
      <td>90</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>186</td>
      <td>192</td>
      <td>112</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>217</td>
      <td>119</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>229</td>
      <td>144</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>236</td>
      <td>156</td>
      <td>162</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>237</td>
      <td>244</td>
      <td>163</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>264</td>
      <td>171</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>282</td>
      <td>191</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>306</td>
      <td>209</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>340</td>
      <td>233</td>
      <td>266</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>366</td>
      <td>267</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>367</td>
      <td>370</td>
      <td>293</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>394</td>
      <td>297</td>
      <td>320</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>395</td>
      <td>397</td>
      <td>321</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>404</td>
      <td>324</td>
      <td>330</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>405</td>
      <td>405</td>
      <td>331</td>
      <td>331</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>434</td>
      <td>332</td>
      <td>360</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1016##j.str.2015.07.024

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5dhh">5DHH</a></td>
      <td>3.0</td>
      <td>P21</td>
      <td>Human NOP receptor with <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> fusion, in complex with SB-612111</td>
      <td>SB-612111 (piperidine-based antagonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5dhg">5DHG</a></td>
      <td>3.0</td>
      <td>P21</td>
      <td>Human NOP receptor with <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> fusion, in complex with C-35</td>
      <td>C-35 (dichlorophenyl-N-benzyl D-Pro antagonist)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells; baculovirus expression system
- **Construct**: Human NOP receptor with N-terminal [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion; N-terminal and C-terminal truncations for crystallogenesis

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
      <td>Protein expression</td>
      <td>Baculovirus infection of Sf9 insect cells</td>
      <td></td>
      <td>Not specified</td>
      <td>Expressed from 5 L Sf9 insect cell biomass, concentrated to 40 mg/ml for crystallization</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td></td>
      <td>Not specified</td>
      <td>Receptor purity and monodispersity monitored via SDS-PAGE and analytic SEC throughout purification</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified NOP receptor at 40 mg/ml, reconstituted into LCP (40% protein, 54% <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>, 6% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a>)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~20 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash frozen directly from LCP in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>LCP drops: 40 nl protein-containing LCP + 0.8 ul precipitant. Crystals harvested using 50 um MiTeGen micromounts. Data collected at APS GM/CA CAT beamline 23ID-B/D using 10 um minibeam at 1.0330 A wavelength. Due to radiation damage, 10-20 degree wedges collected per crystal. 19-22 crystals used per dataset. <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> with Phaser-MR using NOP-C24 structure (PDB 4EA3) as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5dhh">5DHH</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDGAPADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLGA</span><span class="topo-inside">FL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PLG</span><span class="topo-membrane">LKVTIVGLYLAVCVGGLLGNCLVMYV</span><span class="topo-outside">ILRHTKMKTATNI</span><span class="topo-membrane">YIFNLALADTLVLLTLPFQGTDIL</span><span class="topo-inside">LGFWPF</span><span class="topo-membrane">GNALCKTVIAIDYYNMFTSTFTLTAMS</span><span class="topo-outside">VDRYVAICHP</span><span class="topo-unknown">IRALDV</span><span class="topo-outside">RTSSK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">AQ</span><span class="topo-membrane">AVNVAIWALASVVGVPVAIMGSA</span><span class="topo-inside">QVEDEEIECLVEIPTPQ</span><span class="topo-membrane">DYWGPVFAICIFLFSFIVPVLVISV</span><span class="topo-outside">CYSLMIRRLRGVRLLSGSREKDRNLRRITRLV</span><span class="topo-membrane">LVVVAVFVGCWTPVQVFVLAQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420    </span>
<span class="topo-line"><span class="topo-membrane">GLGVQP</span><span class="topo-inside">SSET</span><span class="topo-membrane">AVAILRFCTALGYVNSCLNPILYAF</span><span class="topo-outside">LD</span><span class="topo-unknown">ENFKACFR</span><span class="topo-outside">K</span><span class="topo-unknown">FCCASALGRPLEVLFQGP</span></span>
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
      <td>119</td>
      <td>123</td>
      <td>45</td>
      <td>49</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>149</td>
      <td>50</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>162</td>
      <td>76</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>186</td>
      <td>89</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>192</td>
      <td>113</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>219</td>
      <td>119</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>229</td>
      <td>146</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>242</td>
      <td>162</td>
      <td>168</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>265</td>
      <td>169</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>282</td>
      <td>192</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>307</td>
      <td>209</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>339</td>
      <td>234</td>
      <td>265</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>366</td>
      <td>266</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>367</td>
      <td>370</td>
      <td>293</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>395</td>
      <td>297</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>396</td>
      <td>397</td>
      <td>322</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>405</td>
      <td>324</td>
      <td>331</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>406</td>
      <td>406</td>
      <td>332</td>
      <td>332</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5dhg">5DHG</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDGAPADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLGAFL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PLGL</span><span class="topo-membrane">KVTIVGLYLAVCVGGLLGNCLVMY</span><span class="topo-outside">VILRHTKMKTATNIY</span><span class="topo-membrane">IFNLALADTLVLLTLPFQGTDIL</span><span class="topo-inside">LGFWPF</span><span class="topo-membrane">GNALCKTVIAIDYYNMFTSTFTLTA</span><span class="topo-outside">MSVDRYVAICHPI</span><span class="topo-unknown">RALD</span><span class="topo-outside">VRTSSK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">AQAV</span><span class="topo-membrane">NVAIWALASVVGVPVAIMGSA</span><span class="topo-inside">QVEDEEIECLVEIPTPQ</span><span class="topo-membrane">DYWGPVFAICIFLFSFIVPVLVISV</span><span class="topo-outside">CYSLMIRRLRGVRLLSGSREKDRNLRRITRLVL</span><span class="topo-membrane">VVVAVFVGCWTPVQVFVLAQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420    </span>
<span class="topo-line"><span class="topo-membrane">GLGVQ</span><span class="topo-inside">PSSET</span><span class="topo-membrane">AVAILRFCTALGYVNSCLNPILYAF</span><span class="topo-outside">LD</span><span class="topo-unknown">ENFKACF</span><span class="topo-outside">R</span><span class="topo-unknown">KFCCASALGRPLEVLFQGP</span></span>
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
      <td>121</td>
      <td>124</td>
      <td>47</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>148</td>
      <td>51</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>163</td>
      <td>75</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>186</td>
      <td>90</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>192</td>
      <td>113</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>217</td>
      <td>119</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>230</td>
      <td>144</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>244</td>
      <td>161</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>265</td>
      <td>171</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>266</td>
      <td>282</td>
      <td>192</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>307</td>
      <td>209</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>340</td>
      <td>234</td>
      <td>266</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>365</td>
      <td>267</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>366</td>
      <td>370</td>
      <td>292</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>371</td>
      <td>395</td>
      <td>297</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>396</td>
      <td>397</td>
      <td>322</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>404</td>
      <td>324</td>
      <td>330</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>405</td>
      <td>405</td>
      <td>331</td>
      <td>331</td>
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

### First NOP receptor structure and antagonist binding

The first X-ray crystal structure of the NOP receptor (Thompson et al., Nature 2012) was determined at 3.0 A resolution in complex with the peptide mimetic antagonist C-24 (Banyu Compound-24). The structure reveals a canonical seven-transmembrane GPCR fold with a large, solvent-exposed orthosteric binding pocket characteristic of peptide-binding GPCRs. C-24 binds in the pocket with its piperidine nitrogen forming a salt bridge with D130(3.32), similar to the binding mode of morphinan antagonists in other opioid receptors.

### Correlation between antagonist potency and receptor thermostability

A strong positive correlation was found between antagonist potency (pKB, measured by BRET assay) and receptor thermal stability (Tm, measured by CPM assay) for the NOP receptor (linear regression r^2 = 0.97, P < 0.001). This correlation provides a high-throughput strategy for identifying GPCR ligands for crystallization using BRET assays on crude membrane preparations, which is more amenable to automation than purified protein Tm measurements.

### Single binding mode correlates with high Tm and successful crystallization

Docking studies showed that potent, stabilizing antagonists (SB-612111, C-35, C-24) strongly favor a single binding orientation, with a salt bridge between the piperidine nitrogen and D130(3.32) anchoring the ligand. Less potent ligands (J-113397, Trap-101, JTC-801) that lowered thermostability could adopt multiple binding modes. This suggests that degenerate ligand binding orientations divide the receptor population into sub-conformations, reducing the probability of isolating a single receptor-ligand pair via crystallization.

### Structural basis of antagonist binding to NOP

The NOP structures with SB-612111 and C-35 are highly similar to the previously determined NOP-C24 structure (RMSD 0.37 A and 0.45 A over C-alpha atoms, respectively). All three antagonists use a piperidine group whose protonated nitrogen forms a salt bridge with D130(3.32). The dichlorophenyl head group of both SB-612111 and C-35 is buried deep in a hydrophobic sub-pocket outlined by M134(3.36), F135(3.37), I219(5.42), and V283(6.55). A sodium ion and water cluster was observed in the NOP-SB-612111 structure near residues D97(2.50), N133(3.35), S137(3.39), and N311(7.45).

### Structural basis of opioid receptor subtype selectivity

The NOP receptor has low affinity for classical opioid alkaloids despite sharing ~67% transmembrane sequence identity with mu-, delta-, and kappa-opioid receptors. Comparison of the NOP-C24 structure with kappa-opioid receptor (PDB 4DJH) and [Human CXCR4 Chemokine Receptor](/xray-mp-wiki/proteins/gpcr/cxcr4/) (PDB 3ODU) reveals differences in extracellular loop conformations, particularly in the region around helices V, VI, and VII, which contribute to ligand selectivity. The NOP receptor shows a more constrained extracellular binding pocket entrance compared to classical opioid receptors.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/delta-opioid-receptor/">Delta Opioid Receptor</a> — Homologous opioid receptor subfamily member; shares conserved sodium binding pocket architecture
- <a href="/xray-mp-wiki/proteins/gpcr/mu-opioid-receptor/">Mu Opioid Receptor</a> — Homologous opioid receptor subfamily member; NOP antagonists show >300-1000 fold selectivity over mu opioid receptor
- <a href="/xray-mp-wiki/proteins/gpcr/kappa-opioid-receptor/">Kappa Opioid Receptor</a> — Homologous opioid receptor subfamily member; used for structural comparison of extracellular region conformations
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Major component of LCP (54% w/w) for NOP crystallization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — Method used for all NOP crystal structures
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/gpcr/cxcr4/">Human CXCR4 Chemokine Receptor</a> — Related protein structure
