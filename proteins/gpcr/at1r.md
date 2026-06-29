---
title: "Angiotensin II Type 1 Receptor"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1074##jbc.M115.689000, doi/10.1016##j.cell.2015.04.011, doi/10.1016##j.cell.2018.12.006, doi/10.1126##science.aay9813]
verified: false
---

# Angiotensin II Type 1 Receptor

## Overview

The [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) type 1 receptor (AT1R) is a class A G protein-coupled receptor that serves as the primary regulator of blood pressure maintenance. AT1R mediates most of the physiological effects of [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/), the endogenous agonist, including vasoconstriction, aldosterone secretion, and sodium retention. The first crystal structure of AT1R was determined in complex with the inverse agonist [olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) (Benicar) at 2.8 A resolution by conventional synchrotron cryo-crystallography (Zhang et al., 2015, JBC), revealing the molecular basis for ligand recognition and functional selectivity. A room temperature structure in complex with the antagonist [ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/) was subsequently solved at 2.9 A using serial femtosecond crystallography. Dysregulation of AT1R signaling contributes to hypertension, cardiac hypertrophy, heart failure, and renal disease. AT1R is a major therapeutic target, with angiotensin receptor blockers (ARBs, or sartans) being among the most widely prescribed anti-hypertensive drugs worldwide.


## Publications

### doi/10.1074##jbc.M115.689000

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4zud">4ZUD</a></td>
      <td>2.8</td>
      <td>P32</td>
      <td>BRIL-AT1R fusion; N-terminal truncations: Met1, Thr7-Asp16; C-terminal truncation: residues 320-359 (4 residues shorter than construct used for 4YAY); HA signal sequence, <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>, 10x <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His Tag</a> (cleaved), TEV cleavage site</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/olmesartan/">Olmesartan</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (Bac-to-Bac [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system)
- **Construct**: BRIL-AT1R chimera with N-terminal HA signal, FLAG, [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tags, TEV site
- **Notes**: AT1R gene sequence optimized for insect cell expression. [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (apocytochrome b562RIL, M7W, H102I, R106L) fused to N-terminus. Truncations: Met1, Thr7-Asp16, residues 320-359 after helix VIII. Full glycosylation retained (no PNGase F treatment).


**Purification:**

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)
- **Expression construct**: [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/)-AT1R chimera with HA/FLAG/His tags (olmesartan-bound)
- **Tag info**: [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (N-terminal, cleaved by TEV)

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
      <td>Cell infection</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> infection</td>
      <td></td>
      <td></td>
      <td>2-3 x 10^6 cells/mL infected with <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> at 27C, harvested at 48 hr</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Hypotonic and high osmotic buffer washes</td>
      <td></td>
      <td>Hypotonic: 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 10 mM MgCl2, 20 mM KCl; High osmotic: 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 1.0 M NaCl, 10 mM MgCl2, 20 mM KCl</td>
      <td>Added EDTA-free protease inhibitor cocktail; membranes incubated with 100 uM <a href="/xray-mp-wiki/reagents/ligands/olmesartan/">Olmesartan</a> for 1 h at 4C before solubilization</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 500 mM NaCl + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>-AT1R in complex with <a href="/xray-mp-wiki/reagents/ligands/olmesartan/">Olmesartan</a> solubilized from membranes; buffer contained 20 uM <a href="/xray-mp-wiki/reagents/ligands/olmesartan/">Olmesartan</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> <a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography/">IMAC</a></td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 500 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His Tag</a> capture; buffer contained <a href="/xray-mp-wiki/reagents/ligands/olmesartan/">Olmesartan</a> 100 uM; wash with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, elute with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage and deglycosylation</td>
      <td>Protease and glycosidase treatment</td>
      <td></td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.004% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> + 0.004% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Overnight treatment with <a href="/xray-mp-wiki/reagents/protein-tags/his-tag">His-tag</a>ged <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> and PNGase F to cleave N-terminal tags and glycosylation sites</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Centrifugal concentration</td>
      <td></td>
      <td></td>
      <td>Concentrated to 30 mg/ml with <a href="/xray-mp-wiki/reagents/additives/vivaspin/">Vivaspin</a> 100 kDa cutoff concentrator; monodispersity tested by analytical <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: 30 mg/ml
**Purity**: Tested by analytical [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>-AT1R + <a href="/xray-mp-wiki/reagents/ligands/olmesartan/">Olmesartan</a>, 30 mg/ml</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> supplemented with 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>1:1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Crystals appeared and grew over several weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals harvested from <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> using micromounts; cryo-cooled at 100K. Data collected at GM/CA@APS (23ID-D), Advanced Photon Source, using 10 um minibeam at 1.0330 A wavelength, 1 s exposure, 1.0 oscillation. Detector: Pilatus3 6M. Space group P32, merohedral twinning (twin law h,k,l and k,h,-l) refined with phenix.xtriage and Refmac5. Single crystal of 70x70x15 um3, 4 non-overlapping spots used.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4zud">4ZUD</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">A</span><span class="topo-inside">DLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKD</span></span>
<span class="topo-line"><span class="topo-inside">FRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLILNSSDCPKAGRHN</span></span>
<span class="topo-line"><span class="topo-inside">YIFV</span><span class="topo-membrane">MIPTLYSIIFVVGIFGNSLVVIVIYF</span><span class="topo-outside">YMKLKTV</span><span class="topo-membrane">ASVFLLNLALADLCFLLTLPLWA</span></span>
<span class="topo-line"><span class="topo-membrane">V</span><span class="topo-inside">YTAMEYRWPFGNYLCK</span><span class="topo-membrane">IASASVSFNLYASVFLLTCLSIDRY</span><span class="topo-outside">LAIVHP</span><span class="topo-unknown">MKSRLRR</span><span class="topo-outside">TM</span><span class="topo-membrane">LVA</span></span>
<span class="topo-line"><span class="topo-membrane">KVTCIIIWLLAGLASLPAI</span><span class="topo-inside">IHRNVFFIENTNITVCAFHYE</span><span class="topo-unknown">SQN</span><span class="topo-inside">STLPIG</span><span class="topo-membrane">LGLTKNILGFL</span></span>
<span class="topo-line"><span class="topo-membrane">FPFLIILTSYTL</span><span class="topo-outside">IWKAL</span><span class="topo-unknown">KKAYEIQKNKPR</span><span class="topo-outside">NDDI</span><span class="topo-membrane">FKIIMAIVLFFFFSWIPHQIFTFL</span><span class="topo-inside">DVL</span></span>
<span class="topo-line"><span class="topo-inside">IQLGIIRDCRIADIVDTA</span><span class="topo-membrane">MPITICIAYFNNCLNPLFYGF</span><span class="topo-unknown">LGKKFKRYFLQ</span></span>
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
      <td>124</td>
      <td>1002</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>150</td>
      <td>30</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>157</td>
      <td>56</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>181</td>
      <td>63</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>197</td>
      <td>87</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>222</td>
      <td>103</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>228</td>
      <td>128</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>237</td>
      <td>141</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>238</td>
      <td>259</td>
      <td>143</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>280</td>
      <td>165</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>289</td>
      <td>189</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>312</td>
      <td>195</td>
      <td>217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>317</td>
      <td>218</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>333</td>
      <td>235</td>
      <td>238</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>357</td>
      <td>239</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>378</td>
      <td>263</td>
      <td>283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>399</td>
      <td>284</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1016##j.cell.2015.04.011

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4yay">4YAY</a></td>
      <td>2.9</td>
      <td></td>
      <td>BRIL-AT1R fusion; N-terminal truncations: residue 1, residues 7-16; C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallography</a>: residues 320-359; HA signal sequence, FLAG tag, 10x His tag (cleaved), TEV cleavage site</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/zd7155/">ZD7155</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (Bac-to-Bac [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system)
- **Construct**: BRIL-AT1R chimera with N-terminal HA signal, FLAG, [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tags, TEV site
- **Notes**: AT1R gene sequence optimized for insect cell expression. [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (apocytochrome b562RIL, M7W, H102I, R106L) fused to N-terminus. Truncations: Met1, Thr7-Asp16, residues 320-359 after helix VIII. Full glycosylation retained (no PNGase F treatment).


**Purification:**

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)
- **Expression construct**: [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/)-AT1R chimera with HA/FLAG/His tags
- **Tag info**: FLAG, [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (N-terminal, cleaved by TEV)

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
      <td>Cell infection</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> infection</td>
      <td></td>
      <td></td>
      <td>2-3 x 10^6 cells/mL infected with <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> at 27C, harvested at 48 hr</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Cell lysis and membrane preparation</td>
      <td></td>
      <td></td>
      <td>Isolated membranes from <a href="/xray-mp-wiki/methods/expression-systems/sf9-expression-system/">Sf9</a> cells</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>-AT1R in complex with <a href="/xray-mp-wiki/reagents/ligands/zd7155/">ZD7155</a> solubilized from membranes</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> <a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography/">IMAC</a></td>
      <td>1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His Tag</a> capture</td>
    </tr>
    <tr>
      <td>Desalting</td>
      <td>Size exclusion (column)</td>
      <td>PD MiniTrap G-25</td>
      <td></td>
      <td>Remove <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Protease cleavage</td>
      <td></td>
      <td></td>
      <td>Overnight treatment with <a href="/xray-mp-wiki/reagents/protein-tags/his-tag">His-tag</a>ged <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> to cleave N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a>/His</td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Immobilized Metal Affinity Chromatography</a> flow-through</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> <a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography/">IMAC</a></td>
      <td></td>
      <td>Cleaved <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a>/<a href="/xray-mp-wiki/reagents/protein-tags/his-tag">His tag</a>s and <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> removed by <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin</td>
    </tr>
  </tbody>
</table>
**Final sample**: 30 mg/ml
**Purity**: Tested by analytical [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>-AT1R + <a href="/xray-mp-wiki/reagents/ligands/zd7155/">ZD7155</a>, 30 mg/ml</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>1:1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-4 weeks</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yay">4YAY</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">A</span><span class="topo-inside">DLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKD</span></span>
<span class="topo-line"><span class="topo-inside">FRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLILNSSDCPKAGRHN</span></span>
<span class="topo-line"><span class="topo-inside">YIFVMI</span><span class="topo-membrane">PTLYSIIFVVGIFGNSLVVIVIYFYM</span><span class="topo-outside">KLKTV</span><span class="topo-membrane">ASVFLLNLALADLCFLLTLPLWA</span></span>
<span class="topo-line"><span class="topo-inside">VYTAMEYRWPFGNYLCK</span><span class="topo-membrane">IASASVSFNLYASVFLLTCLSIDRY</span><span class="topo-outside">LAIVHPMKSRLRRTML</span><span class="topo-membrane">VA</span></span>
<span class="topo-line"><span class="topo-membrane">KVTCIIIWLLAGLASLPAII</span><span class="topo-inside">HRNVFFI</span><span class="topo-unknown">ENTN</span><span class="topo-inside">ITVCAFHYE</span><span class="topo-unknown">SQNS</span><span class="topo-inside">TLPI</span><span class="topo-membrane">GLGLTKNILGFL</span></span>
<span class="topo-line"><span class="topo-membrane">FPFLIILTSYTLIWK</span><span class="topo-outside">ALKK</span><span class="topo-unknown">AYEIQKNKPR</span><span class="topo-outside">NDD</span><span class="topo-membrane">IFKIIMAIVLFFFFSWIPHQIFTF</span><span class="topo-inside">LDVL</span></span>
<span class="topo-line"><span class="topo-inside">IQLGIIRDCRIADIVDTAMP</span><span class="topo-membrane">ITICIAYFNNCLNPLFYGFLGK</span><span class="topo-unknown">KFKRYFLQL</span><span class="topo-outside">L</span><span class="topo-unknown">KY</span></span>
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
      <td>126</td>
      <td>1002</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>152</td>
      <td>32</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>157</td>
      <td>58</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>180</td>
      <td>63</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>197</td>
      <td>86</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>222</td>
      <td>103</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>238</td>
      <td>128</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>260</td>
      <td>144</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>261</td>
      <td>267</td>
      <td>166</td>
      <td>172</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>280</td>
      <td>177</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>288</td>
      <td>190</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>315</td>
      <td>194</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>316</td>
      <td>319</td>
      <td>221</td>
      <td>224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>332</td>
      <td>235</td>
      <td>237</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>356</td>
      <td>238</td>
      <td>261</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>357</td>
      <td>380</td>
      <td>262</td>
      <td>285</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>402</td>
      <td>286</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>403</td>
      <td>411</td>
      <td>308</td>
      <td>316</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>412</td>
      <td>412</td>
      <td>317</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1016##j.cell.2018.12.006

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6do1">6DO1</a></td>
      <td>2.9</td>
      <td>P21212</td>
      <td>AT1R with BRIL inserted into ICL3 (residues 226-227); I320 stop codon; N-terminal HA signal sequence, <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>; no N-terminal deletion</td>
      <td>S1I8 (Sarcosine1,Isoleucine8-<a href="/xray-mp-wiki/reagents/ligands/angiotensin-ii/">Angiotensin II</a>)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (Bac-to-Bac [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system)
- **Construct**: BRIL-AT1R chimera with N-terminal HA signal, FLAG, [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tags, TEV site
- **Notes**: AT1R gene sequence optimized for insect cell expression. [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (apocytochrome b562RIL, M7W, H102I, R106L) fused to N-terminus. Truncations: Met1, Thr7-Asp16, residues 320-359 after helix VIII. Full glycosylation retained (no PNGase F treatment).


**Purification:**

- **Expression system**: Expi293F mammalian cells (tetracycline-inducible)
- **Expression construct**: AT1R with N-terminal HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), BRIL inserted into ICL3 (residues 226-227), I320 stop codon
- **Tag info**: N-terminal HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/)

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
      <td>Cell culture</td>
      <td>Mammalian transient expression</td>
      <td></td>
      <td>Expi293F expression media</td>
      <td>Tetracycline-inducible Expi293F cells; induced with 4 mg/mL doxycycline, 5 mM <a href="/xray-mp-wiki/reagents/additives/sodium-butyrate/">Sodium Butyrate</a>, 1 uM losartan</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Hypotonic lysis</td>
      <td></td>
      <td>10 mM Tris pH 7.4, 2 mM EDTA, 10 mM MgCl2, benzonase, <a href="/xray-mp-wiki/reagents/ligands/benzamidine/">Benzamidine</a>, leupeptin, 5 uM losartan</td>
      <td>Frozen cell pellets lysed under hypotonic conditions at room temperature</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Centrifugation</td>
      <td></td>
      <td></td>
      <td>30,000 x g for 15 min</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.4, 500 mM NaCl, 10 mM MgCl2, benzonase, <a href="/xray-mp-wiki/reagents/ligands/benzamidine/">Benzamidine</a>, leupeptin, 5 uM losartan + 0.5% MNG + 0.05% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hydrogen Succinate (CHS)</a></td>
      <td>2 h stirring at room temperature then 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> affinity</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/m1-flag-resin/">M1 FLAG Affinity Resin</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (HEPES Buffer)</a> pH 7.4, 500 mM NaCl, 0.01% MNG, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 2 mM CaCl2 + 0.01% MNG + 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hydrogen Succinate (CHS)</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a>-tagged AT1R captured on <a href="/xray-mp-wiki/reagents/protein-tags/m1-flag-resin/">M1 FLAG Affinity Resin</a></td>
    </tr>
    <tr>
      <td>Elution</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> peptide elution</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/m1-flag-resin/">M1 FLAG Affinity Resin</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (HEPES Buffer)</a> pH 7.4, 500 mM NaCl, 0.01% MNG, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 0.2 mg/mL <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> peptide, 5 mM EDTA + 0.01% MNG + 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hydrogen Succinate (CHS)</a></td>
      <td>AT1R eluted with <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> peptide</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase SEC Resin</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (HEPES Buffer)</a> pH 7.4, 100 mM NaCl, 0.01% MNG, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> (HNM buffer) + 0.01% MNG + 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hydrogen Succinate (CHS)</a></td>
      <td>Monomeric <a href="/xray-mp-wiki/proteins/gpcr/at1r/">Angiotensin II Type 1 Receptor</a> isolated; for crystallography, treated with EndoH for 90 min prior to <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: 30 uM
**Purity**: Monomeric peak by [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>AT1R-<a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>(ICL3) + S1I8 + Nb.AT110i1, 30 uM</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>10:1 <a href="/xray-mp-wiki/reagents/lipids/monoolein/">monoolein</a>:<a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>1.5:1 by mass</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>6-11 days</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6do1">6DO1</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">DYKDDDDKILNSSTE</span><span class="topo-inside">DGIKRIQDDCPKAGRHNY</span><span class="topo-membrane">IFVMIPTLYSIIFVVGIFGNSLVV</span><span class="topo-outside">IVI</span></span>
<span class="topo-line"><span class="topo-outside">YFYMKLKTVASVF</span><span class="topo-membrane">LLNLALADLCFLLTLPLWAVYTA</span><span class="topo-inside">MEYRWPF</span><span class="topo-membrane">GNYLCKIASASVSFNLY</span></span>
<span class="topo-line"><span class="topo-membrane">ASVFLLTCLSI</span><span class="topo-outside">DRYLAIVHPMKSRLRRTMLVAK</span><span class="topo-membrane">VTCIIIWLLAGLASLPAIIHR</span><span class="topo-inside">NVFFIE</span></span>
<span class="topo-line"><span class="topo-inside">NTNITVCAFHYE</span><span class="topo-unknown">SQN</span><span class="topo-inside">STLP</span><span class="topo-membrane">IGLGLTKNILGFLFPFLIILTSYT</span><span class="topo-outside">LIWKALKKAYDLEDN</span><span class="topo-unknown">WE</span></span>
<span class="topo-line"><span class="topo-unknown">TLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDIL</span></span>
<span class="topo-line"><span class="topo-unknown">VGQIDDALKLANEGKVKEAQAAAEQLKTTRNAEIQKNKP</span><span class="topo-outside">RNDDIFKII</span><span class="topo-membrane">MAIVLFFFFSWI</span></span>
<span class="topo-line"><span class="topo-membrane">PHQIFTFLDV</span><span class="topo-inside">LIQLGIIRDCRIADIV</span><span class="topo-membrane">DTAMPITICIAYFNNCLNPLFY</span><span class="topo-outside">GFLG</span><span class="topo-unknown">KKFKRYFL</span></span>
<span class="topo-line"><span class="topo-unknown">Q</span><span class="topo-outside">LL</span><span class="topo-unknown">KY</span></span>
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
      <td>16</td>
      <td>33</td>
      <td>9</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>57</td>
      <td>27</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>73</td>
      <td>51</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>96</td>
      <td>67</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>103</td>
      <td>90</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>131</td>
      <td>97</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>153</td>
      <td>125</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>147</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>192</td>
      <td>168</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>199</td>
      <td>189</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>223</td>
      <td>193</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>238</td>
      <td>217</td>
      <td>231</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>348</td>
      <td>333</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>349</td>
      <td>370</td>
      <td>342</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>371</td>
      <td>386</td>
      <td>364</td>
      <td>379</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>408</td>
      <td>380</td>
      <td>401</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>412</td>
      <td>402</td>
      <td>405</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>413</td>
      <td>421</td>
      <td>406</td>
      <td>414</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>422</td>
      <td>423</td>
      <td>415</td>
      <td>416</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6do1">6DO1</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">DYKDDDDKILNSSTE</span><span class="topo-inside">DGIKRIQDDCPKAGRHNY</span><span class="topo-membrane">IFVMIPTLYSIIFVVGIFGNSLVVI</span><span class="topo-outside">VI</span></span>
<span class="topo-line"><span class="topo-outside">YFYMKLKTVASVF</span><span class="topo-membrane">LLNLALADLCFLLTLPLWAVYTA</span><span class="topo-inside">MEYRWPF</span><span class="topo-membrane">GNYLCKIASASVSFNLY</span></span>
<span class="topo-line"><span class="topo-membrane">ASVFLLTCLSI</span><span class="topo-outside">DRYLAIVHPMKSRLRRTMLVAK</span><span class="topo-membrane">VTCIIIWLLAGLASLPAIIHR</span><span class="topo-inside">NVFFIE</span></span>
<span class="topo-line"><span class="topo-inside">NTNITVCAFHYE</span><span class="topo-unknown">SQN</span><span class="topo-inside">STLP</span><span class="topo-membrane">IGLGLTKNILGFLFPFLIILTSYT</span><span class="topo-outside">LIWKALKKAYDLEDN</span><span class="topo-unknown">WE</span></span>
<span class="topo-line"><span class="topo-unknown">TLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDIL</span></span>
<span class="topo-line"><span class="topo-unknown">VGQIDDALKLANEGKVKEAQAAAEQLKTTRNAEIQKNKP</span><span class="topo-outside">RNDDIFKII</span><span class="topo-membrane">MAIVLFFFFSWI</span></span>
<span class="topo-line"><span class="topo-membrane">PHQIFTFLDV</span><span class="topo-inside">LIQLGIIRDCRIADIV</span><span class="topo-membrane">DTAMPITICIAYFNNCLNPLFY</span><span class="topo-outside">GFLG</span><span class="topo-unknown">KKFKRYFL</span></span>
<span class="topo-line"><span class="topo-unknown">Q</span><span class="topo-outside">LL</span><span class="topo-unknown">KY</span></span>
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
      <td>16</td>
      <td>33</td>
      <td>9</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>58</td>
      <td>27</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>73</td>
      <td>52</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>96</td>
      <td>67</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>103</td>
      <td>90</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>131</td>
      <td>97</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>153</td>
      <td>125</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>147</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>192</td>
      <td>168</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>199</td>
      <td>189</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>223</td>
      <td>193</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>238</td>
      <td>217</td>
      <td>231</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>348</td>
      <td>333</td>
      <td>341</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>349</td>
      <td>370</td>
      <td>342</td>
      <td>363</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>371</td>
      <td>386</td>
      <td>364</td>
      <td>379</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>408</td>
      <td>380</td>
      <td>401</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>412</td>
      <td>402</td>
      <td>405</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>413</td>
      <td>421</td>
      <td>406</td>
      <td>414</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>422</td>
      <td>423</td>
      <td>415</td>
      <td>416</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1126##science.aay9813

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6os0">6OS0</a></td>
      <td>2.9</td>
      <td></td>
      <td>AT1R-AT110i1 nanobody complex</td>
      <td>Angiotensin II (AngII)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6os1">6OS1</a></td>
      <td>2.9</td>
      <td></td>
      <td>AT1R-AT110i1 nanobody complex</td>
      <td>TRV023</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6os2">6OS2</a></td>
      <td>2.9</td>
      <td></td>
      <td>AT1R-AT110i1 nanobody complex</td>
      <td>TRV026</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (Bac-to-Bac [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system)
- **Construct**: BRIL-AT1R chimera with N-terminal HA signal, FLAG, [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tags, TEV site
- **Notes**: AT1R gene sequence optimized for insect cell expression. [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (apocytochrome b562RIL, M7W, H102I, R106L) fused to N-terminus. Truncations: Met1, Thr7-Asp16, residues 320-359 after helix VIII. Full glycosylation retained (no PNGase F treatment).


**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>AT1R-AT110i1 <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">nanobody</a> complex + AngII, TRV023, or TRV026</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal structures of AT1R bound to three ligands with divergent bias profiles. Data collected at APS GM/CA beamlines. Structures deposited as PDB 6OS0 (AngII), 6OS1 (TRV023), 6OS2 (TRV026).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6os0">6OS0</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">DYKDDDDKILNSSTE</span><span class="topo-inside">DGIKRIQDDCPKAGRHNYIFV</span><span class="topo-membrane">MIPTLYSIIFVVGIFGNSLVVIVI</span></span>
<span class="topo-line"><span class="topo-membrane">YF</span><span class="topo-outside">YMKLKTV</span><span class="topo-membrane">ASVFLLNLALADLCFLLTLPLWAV</span><span class="topo-inside">YTAMEYRWPFGNY</span><span class="topo-membrane">LCKIASASVSFNLY</span></span>
<span class="topo-line"><span class="topo-membrane">ASVFLLTCLSIDRYL</span><span class="topo-outside">AIVH</span><span class="topo-unknown">PMKSRLR</span><span class="topo-outside">RTM</span><span class="topo-membrane">LVAKVTCIIIWLLAGLASLPAII</span><span class="topo-inside">HRNVFFIE</span></span>
<span class="topo-line"><span class="topo-inside">NTNITVCAFHYESQN</span><span class="topo-unknown">ST</span><span class="topo-inside">LPIG</span><span class="topo-membrane">LGLTKNILGFLFPFLIILTSYTLIWK</span><span class="topo-outside">ALKKAYDLEDNWE</span></span>
<span class="topo-line"><span class="topo-outside">TLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPP</span><span class="topo-unknown">KLEDKSPDS</span><span class="topo-outside">PEMKDFRHGFDIL</span></span>
<span class="topo-line"><span class="topo-outside">VGQIDDALKLANEGKVKEAQAAAEQLKTTR</span><span class="topo-unknown">N</span><span class="topo-outside">AEIQKNKPRNDDIF</span><span class="topo-membrane">KIIMAIVLFFFFSWI</span></span>
<span class="topo-line"><span class="topo-membrane">PHQIFTFL</span><span class="topo-inside">DVLIQLGIIRDCRIADIVDTA</span><span class="topo-membrane">MPITICIAYFNNCLNPLFYGFL</span><span class="topo-outside">G</span><span class="topo-unknown">KKFKRYFL</span></span>
<span class="topo-line"><span class="topo-unknown">Q</span><span class="topo-outside">L</span><span class="topo-unknown">LKY</span></span>
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
      <td>16</td>
      <td>36</td>
      <td>9</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>62</td>
      <td>30</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>63</td>
      <td>69</td>
      <td>56</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>93</td>
      <td>63</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>106</td>
      <td>87</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>135</td>
      <td>100</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>139</td>
      <td>129</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>146</td>
      <td>133</td>
      <td>139</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>147</td>
      <td>149</td>
      <td>140</td>
      <td>142</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>172</td>
      <td>143</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>195</td>
      <td>166</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>201</td>
      <td>191</td>
      <td>194</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>227</td>
      <td>195</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>278</td>
      <td>221</td>
      <td>271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>330</td>
      <td>281</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>345</td>
      <td>1226</td>
      <td>1239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>368</td>
      <td>1240</td>
      <td>1262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>369</td>
      <td>389</td>
      <td>1263</td>
      <td>1283</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>390</td>
      <td>411</td>
      <td>1284</td>
      <td>1305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>412</td>
      <td>412</td>
      <td>1306</td>
      <td>1306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>413</td>
      <td>421</td>
      <td>1307</td>
      <td>1315</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>422</td>
      <td>422</td>
      <td>1316</td>
      <td>1316</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6os1">6OS1</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">DYKDDDDKILNSSTEDG</span><span class="topo-inside">IKRIQDDCPKAGRHNY</span><span class="topo-membrane">IFVMIPTLYSIIFVVGIFGNSLVVIVI</span></span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-outside">FYMKLKTVASV</span><span class="topo-membrane">FLLNLALADLCFLLTLPLWAVYTA</span><span class="topo-inside">MEYRWPFGNY</span><span class="topo-membrane">LCKIASASVSFNLY</span></span>
<span class="topo-line"><span class="topo-membrane">ASVFLLTCLSI</span><span class="topo-outside">DRYLAIVHPMKSRLRRTMLV</span><span class="topo-membrane">AKVTCIIIWLLAGLASLPAIIHR</span><span class="topo-inside">NVFFIE</span></span>
<span class="topo-line"><span class="topo-inside">NTNITVCAFHYESQNSTL</span><span class="topo-membrane">PIGLGLTKNILGFLFPFLIILTSYT</span><span class="topo-outside">LIWKALKKAYDLEDNWE</span></span>
<span class="topo-line"><span class="topo-outside">TLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKA</span><span class="topo-unknown">TPPKLEDKSPDSPEMKDF</span><span class="topo-outside">RHGFDIL</span></span>
<span class="topo-line"><span class="topo-outside">VGQIDDALKLANEGKVKEAQAAAEQLK</span><span class="topo-unknown">TTRNAEIQ</span><span class="topo-outside">KNKPRNDDIFKII</span><span class="topo-membrane">MAIVLFFFFSWI</span></span>
<span class="topo-line"><span class="topo-membrane">PHQIFTFLDVL</span><span class="topo-inside">IQLGIIRDCRIADI</span><span class="topo-membrane">VDTAMPITICIAYFNNCLNPLFYG</span><span class="topo-outside">FLG</span><span class="topo-unknown">KKFKRYFL</span></span>
<span class="topo-line"><span class="topo-unknown">QLL</span><span class="topo-outside">K</span><span class="topo-unknown">Y</span></span>
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
      <td>18</td>
      <td>33</td>
      <td>11</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>61</td>
      <td>27</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>72</td>
      <td>55</td>
      <td>65</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>96</td>
      <td>66</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>106</td>
      <td>90</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>131</td>
      <td>100</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>151</td>
      <td>125</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>174</td>
      <td>145</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>198</td>
      <td>168</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>223</td>
      <td>192</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>275</td>
      <td>217</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>327</td>
      <td>287</td>
      <td>320</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>348</td>
      <td>1230</td>
      <td>1242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>349</td>
      <td>371</td>
      <td>1243</td>
      <td>1265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>385</td>
      <td>1266</td>
      <td>1279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>409</td>
      <td>1280</td>
      <td>1303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>412</td>
      <td>1304</td>
      <td>1306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>413</td>
      <td>423</td>
      <td>1307</td>
      <td>1317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>424</td>
      <td>424</td>
      <td>1318</td>
      <td>1318</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6os2">6OS2</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">DYKDDDDKILNSSTEDG</span><span class="topo-inside">IKRIQDDCPKAGRHNY</span><span class="topo-membrane">IFVMIPTLYSIIFVVGIFGNSLVVIVI</span></span>
<span class="topo-line"><span class="topo-membrane">Y</span><span class="topo-outside">FYMKLKTVAS</span><span class="topo-membrane">VFLLNLALADLCFLLTLPLWAVYTA</span><span class="topo-inside">MEYRWPFGNY</span><span class="topo-membrane">LCKIASASVSFNLY</span></span>
<span class="topo-line"><span class="topo-membrane">ASVFLLTCLSI</span><span class="topo-outside">DRYLAIVHPMKSRLRRTML</span><span class="topo-membrane">VAKVTCIIIWLLAGLASLPAIIHR</span><span class="topo-inside">NVFFIE</span></span>
<span class="topo-line"><span class="topo-inside">NTNITVCAFHYESQNSTL</span><span class="topo-membrane">PIGLGLTKNILGFLFPFLIILTSYT</span><span class="topo-outside">LIWKALKKAYDLEDNWE</span></span>
<span class="topo-line"><span class="topo-outside">TLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKA</span><span class="topo-unknown">TPPKLEDKSPDSPEMKDFR</span><span class="topo-outside">HGFDIL</span></span>
<span class="topo-line"><span class="topo-outside">VGQIDDALKLANEGKVKEAQAAAEQLK</span><span class="topo-unknown">TTRNAEIQ</span><span class="topo-outside">KNKPRNDDIFKII</span><span class="topo-membrane">MAIVLFFFFSWI</span></span>
<span class="topo-line"><span class="topo-membrane">PHQIFTFLDVL</span><span class="topo-inside">IQLGIIRDCRIADI</span><span class="topo-membrane">VDTAMPITICIAYFNNCLNPLFYG</span><span class="topo-outside">FLG</span><span class="topo-unknown">KKFKRYFL</span></span>
<span class="topo-line"><span class="topo-unknown">QLL</span><span class="topo-outside">K</span><span class="topo-unknown">Y</span></span>
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
      <td>18</td>
      <td>33</td>
      <td>11</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>61</td>
      <td>27</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>71</td>
      <td>55</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>96</td>
      <td>65</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>106</td>
      <td>90</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>131</td>
      <td>100</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>150</td>
      <td>125</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>174</td>
      <td>144</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>198</td>
      <td>168</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>223</td>
      <td>192</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>275</td>
      <td>217</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>327</td>
      <td>288</td>
      <td>320</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>348</td>
      <td>1230</td>
      <td>1242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>349</td>
      <td>371</td>
      <td>1243</td>
      <td>1265</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>385</td>
      <td>1266</td>
      <td>1279</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>409</td>
      <td>1280</td>
      <td>1303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>412</td>
      <td>1304</td>
      <td>1306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>413</td>
      <td>423</td>
      <td>1307</td>
      <td>1317</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>424</td>
      <td>424</td>
      <td>1318</td>
      <td>1318</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Olmesartan binding mode and conserved ARB recognition

The AT1R-[Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) structure (PDB 4ZUD, 2.8 A) confirmed the binding mode of ARBs. [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) is anchored by three critical residues: Tyr35^1.39, Trp84^2.60, and Arg167^ECL2, which form hydrogen bonds, salt bridges, and pi-pi interactions with the biphenyl-tetrazole scaffold. Comparison with the [ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/)-bound structure (PDB 4YAY) showed RMSD of 0.85 A over 92% of Calpha atoms, supporting a conserved binding mode for different ARBs. The Lys199^5.42 side chain was ordered in the cryo-cooled structure but did not directly contact [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/).

### ZD7155 binding pocket architecture

[ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/) binds in a prominent ligand-binding pocket formed by residues from helices
I, II, III, VII, and ECL2. Key interactions: Arg167^ECL2 forms an extensive network
with the acidic tetrazole and naphthyridin-2-one moieties; Tyr35^1.39 hydrogen-bonds
with the naphthyridin-2-one; Trp84^2.60 forms a pi-pi interaction with the
naphthyridin-2-one. Mutagenesis confirmed that Arg167^ECL2A, Tyr35^1.39A, and
Trp84^2.60A all abolish peptide and non-peptide ligand binding.

### Functional selectivity of olmesartan derivatives

Modifications of the [Olmesartan](/xray-mp-wiki/reagents/ligands/olmesartan/) scaffold yield ligands with distinct pharmacological properties. R781253 (additional 4-hydroxybenzyl group) retains inverse agonism. R239470 (carbamoyl group replacing carboxyl) is a neutral antagonist. R794847 (both modifications) is a weak partial agonist. Docking simulations predicted that the 4-hydroxybenzyl groups of R781253 and R794847 extend to a sub-pocket formed by Leu112^3.36, Lys199^5.42, Asn200^5.43, Trp253^6.48, His256^6.51, Gln257^6.52, and Thr260^6.55. Trp253^6.48 (toggle switch) was identified as a key determinant of functional selectivity.

### Sodium binding site

A conserved allosteric sodium-binding site is observed in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/), structurally
superimposable with the sodium pocket in the delta-opioid receptor (PDB 4N6H).
The pocket includes Asp74^2.50, Asn111^3.35, Asn295^7.46, Trp253^6.48, and
Asn298^7.49. Asn111^3.35 and Asn295^7.46 form two intramolecular hydrogen bonds
stabilizing the inactive conformation.

### Allosteric sodium modulation of peptide ligand binding

The Asn111^3.35Ala sodium pocket mutant showed ~300-fold higher affinity for [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) in the absence of sodium ions compared to physiological Na+ concentration. This effect was absent for the beta-arrestin biased agonist TRV120027, suggesting different mechanisms for AT1R modulation by its natural ligand and biased ligands. The sodium ion may allosterically stabilize the inactive conformation of AT1R.

### ECL2 as autoantibody epitope

ECL2 of [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) serves as an epitope for harmful agonistic autoantibodies in
preeclampsia and malignant hypertension. The atomic details of ECL2 and the
extracellular ligand-binding region provide guidance for designing antigens against
these autoantibodies.

### Activation mechanism

The inactive conformation is stabilized by the Asn111^3.35-Asn295^7.46 hydrogen
bond network. Binding of [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) disrupts this interaction, allowing
Asn295^7.46 to interact with Asp74^2.50. The conserved D(E)RY motif (helix III)
and NPxxY motif (helix VII) are present. The ionic lock between Arg^3.50 and
Asp/Glu^6.30 is not possible in AT1R due to lack of acidic residue at 6.30.
Helix VIII angles away from the membrane, resembling CCR5 orientation.

### Beta-arrestin signaling

G protein-independent [Beta-Arrestin](/xray-mp-wiki/concepts/signaling-receptors/beta-arrestin/) mediated signaling by AT1R confers
cardio-protective benefits. Thr336Pro and Pro341His (in the C-terminal tail not
included in the crystallized construct) affect GPCR kinase-dependent phosphorylation,
necessary for [Beta-Arrestin](/xray-mp-wiki/concepts/signaling-receptors/beta-arrestin/) recruitment.

### Active-state conformational changes

The active-state AT1R (PDB 6DO1) shows an 11 angstrom outward displacement of TM6,
rotation of TM5 away from the transducer binding pocket, and inward rotation of TM7.
ICL2 reorganizes to form a short alpha helix. Helix 8 repositions from a bent
conformation away from the membrane to a conventional position parallel to the
membrane near the TM1-TM7 interface. Y302^7.53 of the [NPxxY Motif](/xray-mp-wiki/concepts/structural-mechanisms/npxxy-motif/) rotates 10
angstroms inward to hydrogen bond with Y215^5.58 in TM5.

### Peptide binding mode

[S1I8 Peptide](/xray-mp-wiki/reagents/ligands/s1i8/) binds in an extended conformation with N terminus facing the solvent and C
terminus buried deep in the receptor core. The peptide forms a half-beta-barrel
with the receptor N terminus and ECL2 beta-hairpin. Key interactions: H183^ECL2
hydrogen bonds with the peptide N terminus; W84^2.60, V108^3.32, L112^3.36, and
I288^7.38 interact with P7 and I8 of [S1I8 Peptide](/xray-mp-wiki/reagents/ligands/s1i8/); R2 of the peptide engages D281^7.32
and D263^6.58; the terminal carboxylate interacts with K199^5.42.

### Phenylalanine ratchet mechanism

[Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) activation involves a phenylalanine ratchet between TMs 5 and 6: I8 of S1I8
forces W253^6.48 and Y292^7.43 downward, causing F249^6.44 and F250^6.45 to ratchet
past F208^5.51. This creates a void filled by N295^7.46 moving inward, breaking the
N111^3.35-N295^7.46 hydrogen bond present in the inactive structure. This mechanism
diverges from other GPCRs and explains the diversity of allosteric mechanisms among
GPCRs.

### Biased agonism and C-terminal residue 8

The C-terminal residue 8 of AngII determines signaling bias. Ile8 (S1I8) produces
partial Gq agonism; Phe8 (AngII) produces full Gq agonism but the phenyl ring
slightly exceeds the cavity size shaped by TM3. Smaller residues or deletions at
position 8 produce [Beta-Arrestin](/xray-mp-wiki/concepts/signaling-receptors/beta-arrestin/)-biased ligands. The I8 side chain fits closely
into a TM3-shaped cavity, and the cavity size relative to residue 8 side chain
determines the conformational changes propagated through the receptor.

### Molecular recognition paradigm for ARBs

Docking simulations and mutagenesis of multiple ARBs (candesartan, telmisartan, valsartan, losartan, eprosartan) revealed a molecular recognition paradigm: the biphenyl-tetrazole scaffold employs three critical residues Arg167^ECL2, Trp84^2.60, and Tyr35^1.39, but relative binding energy contributions vary per ARB. Derivative moieties extend to additional sub-pockets, allowing wobbling of the core structure. Naturally occurring SNPs in the AGTR1 gene (Leu48^1.52Val, Ala163^4.60Thr, Leu222^5.65Val, Ala244^6.39Ser, Thr282^7.33Met, Cys289^7.40Trp) near the orthosteric pocket may affect ARB binding and efficacy in humans.

### AngII induces distinct active conformations of AT1R

Crystal structures of AT1R bound to angiotensin II (AngII), TRV023, and TRV026 reveal that AngII promotes more substantial rearrangements at the bottom of the ligand-binding pocket and in a key polar network in the receptor core. The AngII F8 residue is conformationally heterogeneous with high B-factors, while TRV026 and TRV023 show clear density for all residues. TM3 rotates in the AngII-bound structure, moving L112^3.36 past W253^6.48 and repositioning N111^3.35 outside the receptor core.

### Bipartite activation mechanism for biased signaling

The AT1R contains a divergent sodium-binding site polar core. Substitution of the highly conserved S^7.46 with N295^7.46 disrupts the sodium coordination sphere, replacing sodium with a hydrogen bond between N295^7.46 and N111^3.35. This creates a bipartite activation mechanism: N295^7.46 rearrangement is sufficient for beta-arrestin coupling, while N111^3.35 flipping is essential for Gq signaling. This predisposes AT1R to biased signaling.

### Structural basis of beta-arrestin-biased agonism

Beta-arrestin-biased ligands (TRV023, TRV026) trigger TM6 outward rotation and N295^7.46 conformational changes, which are sufficient for beta-arrestin coupling. However, they fail to induce the N111^3.35 outward movement that is essential for Gq signaling. This provides a structural mechanism for biased agonism at AT1R, where the partial or beta-arrestin-biased peptide agonists activate only a subset of the full conformational changes induced by AngII.

### Divergent sodium-binding motif in GPCRs and biased signaling

Deviations from the conserved sodium-binding motif are enriched in peptide- and protein-binding family A GPCRs related to AT1R. Only 3 out of 22 chemokine receptors possess all conserved residues for tight sodium binding. The chemokine receptor family contains atypical receptors that signal through beta-arrestins without G proteins, and endogenous chemokines function as biased ligands at many chemokine receptors. Substitutions in and around the sodium-binding site can bias receptor signaling.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/zd7155/">ZD7155</a> — Primary ligand bound in PDB 4YAY structure
- <a href="/xray-mp-wiki/reagents/ligands/angiotensin-ii/">Angiotensin II</a> — Endogenous agonist of [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- <a href="/xray-mp-wiki/reagents/ligands/s1i8/">S1I8</a> — Partial agonist peptide used in active-state PDB 6DO1 crystallization
- <a href="/xray-mp-wiki/reagents/antibodies/nb-at110i1/">Nb.AT110i1 Synthetic Nanobody</a> — Conformation-specific [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) stabilizing active-state AT1R (PDB 6DO1)
- <a href="/xray-mp-wiki/reagents/detergents/mng/">Lauryl Maltose Neopentyl Glycol (MNG)</a> — Detergent used for [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) solubilization and purification in PDB 6DO1
- <a href="/xray-mp-wiki/reagents/ligands/losartan/">Losartan</a> — ARB used for [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) expression stabilization and comparison with peptide ligands
- <a href="/xray-mp-wiki/reagents/ligands/olmesartan/">Olmesartan</a> — Inverse agonist ARB bound in PDB 4ZUD structure; used for functional selectivity studies
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> — Thermostabilization fusion partner inserted into [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) ICL3 for PDB 6DO1
- <a href="/xray-mp-wiki/proteins/gpcr/at2r/">Angiotensin II Type 2 Receptor</a> — Close homolog with distinct signaling; AT2R structure reveals helix 8 canonical conformation upon [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) binding
- <a href="/xray-mp-wiki/concepts/signaling-receptors/beta-arrestin/">Beta-Arrestin</a> — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/npxxy-motif/">NPxxY Motif</a> — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Immobilized Metal Affinity Chromatography</a> — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a> — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- <a href="/xray-mp-wiki/proteins/gpcr/at1r/">Angiotensin II Type 1 Receptor</a> — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- <a href="/xray-mp-wiki/reagents/protein-tags/m1-flag-resin/">M1 FLAG Affinity Resin</a> — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- <a href="/xray-mp-wiki/reagents/additives/peg-300/">PEG 300</a> — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Sf9 Insect Cells</a> — Referenced in [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/)
