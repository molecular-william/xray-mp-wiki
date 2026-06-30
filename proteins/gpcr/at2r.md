---
title: "Angiotensin II Type 2 Receptor"
created: 2026-05-29
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2019.12.003, doi/10.1038##nature22035, doi/10.1038##s41594-018-0079-8]
verified: false
---

# Angiotensin II Type 2 Receptor

## Overview

The [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) type 2 receptor (AT2R) is a class A [G Protein](/xray-mp-wiki/concepts/signaling-receptors/g-protein/)-coupled receptor that counteracts many of the physiological effects of [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) mediated by [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/). AT2R is involved in blood pressure regulation, vasodilation, sodium excretion, and anti-proliferative signaling. Unlike [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/), AT2R does not signal through G proteins or [Beta-Arrestin](/xray-mp-wiki/concepts/signaling-receptors/beta-arrestin/) in a conventional manner and requires additional effector proteins such as ATIP and SHP-1 for signal transduction. Crystal structures of AT2R reveal an active-like conformation of the 7TM bundle with a non-canonical helix VIII position that sterically blocks G protein/beta-arrestin recruitment.


## Publications

### doi/10.1016##j.str.2019.12.003

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6jod">6JOD</a></td>
      <td>3.2</td>
      <td>C2221</td>
      <td>AT2R-mbIIGN-term; C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> at residue 368; N-terminal HA signal sequence, FLAG tag, TEV cleavage site; C-terminal His8 tag; complex with G-protein mbIIGN-term fragment and Fab4A03 antibody fragment</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/angiotensin-ii/">Angiotensin II</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) ([Bac-to-Bac System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system)
- **Construct**: BRIL-AT2R chimera; AT2R residues 1-34 and 336-363 truncated; N-terminal BRIL (apocytochrome b562RIL, Met7Trp, His102Ile, Arg106L) fused via 4-residue linker (Gly-Ser-Gly-Ser); N-terminal HA signal sequence, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10x His tag, TEV cleavage site
- **Notes**: AT2R gene sequence (UNIPROT P50052) codon-optimized for insect cell expression, cloned into [pFastBac1](/xray-mp-wiki/reagents/vectors/pfastbac1/) vector. [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) infected with [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/), membranes prepared by hypotonic lysis and high osmotic wash.


**Purification:**

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)
- **Expression construct**: AT2R-mbIIGN-term; N-terminal HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) site; C-terminal [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) site, His8 tag; C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) at residue 368
- **Tag info**: [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), His8 (C-terminal, cleaved by [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/))

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
      <td>Membrane preparation</td>
      <td>Cell lysis and membrane isolation</td>
      <td></td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (HEPES Buffer)</a> pH 7.5, 20 mM KCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a>, protease inhibitor cocktail</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Sf9 Insect Cells</a> harvested by centrifugation, flash-frozen at -80 C, lysed under hypotonic conditions, membranes collected by ultracentrifugation at 100,000 x g, washed twice with high osmotic buffer (5 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (HEPES Buffer)</a> pH 7.5, 0.5 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 10 mM KCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a>)</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 800 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1.0% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Membranes solubilized with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> and <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> supplemented with <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> (100 mg/ml) and excess <a href="/xray-mp-wiki/reagents/ligands/angiotensin-ii/">Angiotensin II</a>; 1 hour at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> Cobalt Affinity Resin</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, <a href="/xray-mp-wiki/reagents/ligands/angiotensin-ii/">Angiotensin II</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> resin pre-equilibrated with solubilization buffer; incubation 12-16 hours at 4 C; washed with 10 column volumes of wash buffer, 3 CVs of elution buffer containing AngII</td>
    </tr>
    <tr>
      <td>Elution</td>
      <td>Metal affinity elution</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> Cobalt Affinity Resin</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, <a href="/xray-mp-wiki/reagents/ligands/angiotensin-ii/">Angiotensin II</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Elution with buffer containing excess AngII to maintain receptor-ligand complex</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase SEC Resin</a></td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Monodisperse <a href="/xray-mp-wiki/proteins/gpcr/at2r/">Angiotensin II Type 2 Receptor</a>-mbIIGN-term/Fab4A03 complex isolated for crystallization</td>
    </tr>
  </tbody>
</table>
**Final sample**: 10 mg/ml in 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 200 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)
**Purity**: Monodisperse peak by [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/proteins/gpcr/at2r/">Angiotensin II Type 2 Receptor</a>-mbIIGN-term/Fab4A03 complex + AngII, 10 mg/ml</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>1:1 <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>:<a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at 100 K at SPring-8 BL32XU micro-focus beamline. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> with MOLREP. 470 datasets collected with KAMO system and merged.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jod">6JOD</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">CSQKPSDKHLDA</span><span class="topo-membrane">IPILYYIIFVIGFLVNIVVVTLFC</span><span class="topo-inside">CQKGPKKVSSI</span><span class="topo-membrane">YIFNLAVADLLLLATLPLWATYYS</span><span class="topo-outside">YRYDWL</span><span class="topo-membrane">FGPVMCKVFGSFLTLNMFASIFFITCMSV</span><span class="topo-inside">DRYQSVIYPFLSQR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RNPWQASY</span><span class="topo-membrane">IVPLVWCMACLSSLPTFYFRDV</span><span class="topo-outside">RTIEYLGVNACIMAFPPEKYAQ</span><span class="topo-membrane">WAAGIALMKNILGFIIPLIFIATCYFG</span><span class="topo-inside">IRKHLLKTNSYGKNRITRDQVL</span><span class="topo-membrane">KMAAAVVLAFIICWLPFHV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310  </span>
<span class="topo-line"><span class="topo-membrane">LTFLDAL</span><span class="topo-outside">AWMGVINSCEVIAVIDLA</span><span class="topo-membrane">LPFAILLGFTNSCVNPFLYCFV</span><span class="topo-inside">G</span><span class="topo-unknown">NRFQQKLRSVF</span><span class="topo-inside">RVPITWL</span><span class="topo-unknown">QGKRES</span></span>
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
      <td>12</td>
      <td>35</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>36</td>
      <td>47</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>47</td>
      <td>71</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>71</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>77</td>
      <td>106</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>106</td>
      <td>112</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>128</td>
      <td>141</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>150</td>
      <td>163</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>172</td>
      <td>185</td>
      <td>206</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>199</td>
      <td>207</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>221</td>
      <td>234</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>247</td>
      <td>256</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>248</td>
      <td>265</td>
      <td>282</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>266</td>
      <td>287</td>
      <td>300</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>288</td>
      <td>288</td>
      <td>322</td>
      <td>322</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>299</td>
      <td>323</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>300</td>
      <td>306</td>
      <td>334</td>
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
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6jod">6JOD</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80      </span>
<span class="topo-line"><span class="topo-unknown">ADLEDNW</span><span class="topo-outside">ETLNDNLKVIEKADNAAQVKDALTKMRAAALD</span><span class="topo-unknown">AGSGSGD</span><span class="topo-outside">ILVGQIDDALKLANEGKVKEAQAAAEQ</span><span class="topo-unknown">LKTTINAYIQKYG</span></span>
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
      <td>8</td>
      <td>39</td>
      <td>1008</td>
      <td>1039</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>73</td>
      <td>1067</td>
      <td>1093</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nature22035

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5unf">5UNF</a></td>
      <td>2.8</td>
      <td>P212121</td>
      <td>BRIL-AT2R fusion; N-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>: residues 1-34; C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>: residues 336-363; N-terminal BRIL (apocytochrome b562RIL) fused via 4-residue linker (Gly-Ser-Gly-Ser); N-terminal HA signal sequence, FLAG tag, 10x His tag (cleaved), TEV cleavage site; complex with Cpd 1</td>
      <td>Cpd 1 (<a href="/xray-mp-wiki/proteins/gpcr/at2r/">Angiotensin II Type 2 Receptor</a>-selective ligand)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5ung">5UNG</a></td>
      <td>2.8</td>
      <td>C2</td>
      <td>BRIL-AT2R fusion; N-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>: residues 1-34; C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>: residues 336-363; N-terminal BRIL (apocytochrome b562RIL) fused via 4-residue linker (Gly-Ser-Gly-Ser); N-terminal HA signal sequence, FLAG tag, 10x His tag (cleaved), TEV cleavage site; complex with Cpd 1</td>
      <td>Cpd 1 (<a href="/xray-mp-wiki/proteins/gpcr/at2r/">Angiotensin II Type 2 Receptor</a>-selective ligand)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5unh">5UNH</a></td>
      <td>2.9</td>
      <td>P21</td>
      <td>BRIL-AT2R fusion; N-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>: residues 1-34; C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>: residues 336-363; N-terminal BRIL (apocytochrome b562RIL) fused via 4-residue linker (Gly-Ser-Gly-Ser); N-terminal HA signal sequence, FLAG tag, 10x His tag (cleaved), TEV cleavage site; complex with Cpd 2 (AT1R/AT2R dual ligand)</td>
      <td>Cpd 2 (AT1R/AT2R dual ligand)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) ([Bac-to-Bac System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system)
- **Construct**: BRIL-AT2R chimera; AT2R residues 1-34 and 336-363 truncated; N-terminal BRIL (apocytochrome b562RIL, Met7Trp, His102Ile, Arg106L) fused via 4-residue linker (Gly-Ser-Gly-Ser); N-terminal HA signal sequence, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10x His tag, TEV cleavage site
- **Notes**: AT2R gene sequence (UNIPROT P50052) codon-optimized for insect cell expression, cloned into [pFastBac1](/xray-mp-wiki/reagents/vectors/pfastbac1/) vector. [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) infected with [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/), membranes prepared by hypotonic lysis and high osmotic wash.


**Purification:**

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)
- **Expression construct**: [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/)-AT2R chimera; AT2R residues 1-34 and 336-363 truncated; N-terminal [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (apocytochrome b562RIL, Met7Trp, His102Ile, Arg106L) fused via 4-residue linker (Gly-Ser-Gly-Ser); N-terminal HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10x [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/), [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) cleavage site
- **Tag info**: [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10x His (N-terminal, cleaved by [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/))

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
      <td>Membrane preparation</td>
      <td>Cell lysis and membrane isolation</td>
      <td></td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (HEPES Buffer)</a> pH 7.5, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a>, 20 mM KCl, <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>-free protease inhibitor cocktail</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Sf9 Insect Cells</a> lysed by repeated washing and centrifugation with hypotonic and high osmotic buffers; membranes treated with <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> (2 mg/ml) for 30 min at 4 C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 800 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Solubilized for 4 hours at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a> resin</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 400 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (wash I); 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (wash II) + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> (wash I); 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> (wash II)</td>
      <td>Bound overnight to <a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> resin; washed with 10 column volumes each of wash buffers I and II</td>
    </tr>
    <tr>
      <td>Elution and tag cleavage</td>
      <td>Metal affinity elution followed by protease cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a> resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.004% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (elution); then <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> overnight + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.004% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Eluted with 3 CV elution buffer, incubated with 100 uM ligand (Cpd 1 or 2), treated overnight with <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> to remove N-terminal tags, concentrated to 15 mg/ml</td>
    </tr>
  </tbody>
</table>
**Final sample**: 15 mg/ml in 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 100 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.004% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)
**Purity**: Tested by analytical [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) - SFX at XFEL</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>-AT2R + Cpd 1, 15 mg/ml, reconstituted in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase</a> with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> + 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> at 2:3 protein:lipid ratio</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> + 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (v/v)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>5 days</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Microcrystals (5x2x2 um) grown in syringe, injected into <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> injector at LCLS XFEL. Two lattices observed. Data merged using CrystFEL with Cheetah hit finding. Orthorhombic structure used for description.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) - Synchrotron radiation</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>-AT2R + Cpd 2, reconstituted in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase</a> with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> + 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> at 2:3 protein:lipid ratio</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> + 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (v/v)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>21 days</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals (70x40x20 um) harvested with micromounts and flash-frozen in liquid nitrogen. Data collected at 23ID-D beamline (GM/CA) at Advanced Photon Source, Argonne National Laboratory. Integrated and scaled with XDS.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5unf">5UNF</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">ADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGK</span><span class="topo-unknown">VKEAQAAA</span><span class="topo-outside">EQLKTTRN</span><span class="topo-unknown">AYIQKYLGSGSCSQKPSDK</span><span class="topo-outside">HL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">D</span><span class="topo-membrane">AIPILYYIIFVIGFLVNIVVVTL</span><span class="topo-inside">FCCQKGPKKVSSI</span><span class="topo-membrane">YIFNLAVADLLLLATLPLWATYYS</span><span class="topo-outside">YRYDW</span><span class="topo-membrane">LFGPVMCKVFGSFLTLNMFASIFFITCMSV</span><span class="topo-inside">DRYQSVIYPF</span><span class="topo-unknown">LSQRRN</span><span class="topo-inside">PWQASY</span><span class="topo-membrane">IV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">PLVWCMACLSSLPTFYFRD</span><span class="topo-outside">VRTIEYLGVNACIMAFPPEKYAQ</span><span class="topo-membrane">WSAGIALMKNILGFIIPLIFIATCYFG</span><span class="topo-inside">IRKHLLKTNSYGKNRITRDQVL</span><span class="topo-membrane">KMAAAVVLAFIICWLPFHVLTFLDAL</span><span class="topo-outside">AWM</span></span>
<span class="topo-ruler">       370       380       390       400       410 </span>
<span class="topo-line"><span class="topo-outside">GVINSCEVIAVIDLA</span><span class="topo-membrane">LPFAILLGFTNSCVNPFLYCFVG</span><span class="topo-inside">NRFQQKLRSVFR</span><span class="topo-unknown">V</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>83</td>
      <td>1001</td>
      <td>1083</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>91</td>
      <td>1084</td>
      <td>1091</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>92</td>
      <td>99</td>
      <td>1092</td>
      <td>1099</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>100</td>
      <td>1100</td>
      <td>1100</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>119</td>
      <td>121</td>
      <td>43</td>
      <td>45</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>144</td>
      <td>46</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>157</td>
      <td>69</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>181</td>
      <td>82</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>186</td>
      <td>106</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>216</td>
      <td>111</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>226</td>
      <td>141</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>238</td>
      <td>157</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>259</td>
      <td>163</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>282</td>
      <td>184</td>
      <td>206</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>309</td>
      <td>207</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>331</td>
      <td>234</td>
      <td>255</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>357</td>
      <td>256</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>375</td>
      <td>282</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>376</td>
      <td>398</td>
      <td>300</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>399</td>
      <td>410</td>
      <td>323</td>
      <td>334</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5ung">5UNG</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">ADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLGSGSCSQKPSDKHL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">DAIPILYYIIFVIGFLVNIVVVTL</span><span class="topo-inside">FCCQKGPKKVSSIY</span><span class="topo-membrane">IFNLAVADLLLLATLPLWATYYS</span><span class="topo-outside">YRYDW</span><span class="topo-membrane">LFGPVMCKVFGSFLTLNMFASIFFITCMSV</span><span class="topo-inside">DRYQSVIYPFLSQRRNPWQASY</span><span class="topo-membrane">IV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">PLVWCMACLSSLPTFYFRD</span><span class="topo-outside">VRTIEYLGVNACIMAFPPEKYAQ</span><span class="topo-membrane">WSAGIALMKNILGFIIPLIFIATCYF</span><span class="topo-inside">GIRKHLLKTNSYGKNRITRDQVLK</span><span class="topo-membrane">MAAAVVLAFIICWLPFHVLTFLDAL</span><span class="topo-outside">AWM</span></span>
<span class="topo-ruler">       370       380       390       400       410 </span>
<span class="topo-line"><span class="topo-outside">GVINSCEVIAV</span><span class="topo-membrane">IDLALPFAILLGFTNSCVNPFLYCFV</span><span class="topo-inside">GNRFQQKLRSVFR</span><span class="topo-unknown">V</span></span>
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
      <td>120</td>
      <td>1001</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>144</td>
      <td>45</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>158</td>
      <td>69</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>181</td>
      <td>83</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>186</td>
      <td>106</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>216</td>
      <td>111</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>238</td>
      <td>141</td>
      <td>162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>259</td>
      <td>163</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>282</td>
      <td>184</td>
      <td>206</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>308</td>
      <td>207</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>309</td>
      <td>332</td>
      <td>233</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>357</td>
      <td>257</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>371</td>
      <td>282</td>
      <td>295</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>397</td>
      <td>296</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>410</td>
      <td>322</td>
      <td>334</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5unh">5UNH</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ADLEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAQKATPPKLEDKSPDSPEMKDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKY</span><span class="topo-unknown">LGSGSCSQK</span><span class="topo-inside">PSDKHL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">D</span><span class="topo-membrane">AIPILYYIIFVIGFLVNIVVVTL</span><span class="topo-outside">FCCQK</span><span class="topo-unknown">GPK</span><span class="topo-outside">KVSSIY</span><span class="topo-membrane">IFNLAVADLLLLATLPLWATYY</span><span class="topo-inside">SYRYDW</span><span class="topo-membrane">LFGPVMCKVFGSFLTLNMFASIFFITCMSV</span><span class="topo-outside">DRYQSVIY</span><span class="topo-unknown">PFLSQRRNPWQ</span><span class="topo-outside">ASY</span><span class="topo-membrane">IV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">PLVWCMACLSSLPTFYFRD</span><span class="topo-inside">VRTIEYLGVNACIMAFPPEKYAQW</span><span class="topo-membrane">SAGIALMKNILGFIIPLIFIATCYFG</span><span class="topo-outside">IRKHLLKT</span><span class="topo-unknown">NS</span><span class="topo-outside">YGKNRITRDQVL</span><span class="topo-membrane">KMAAAVVLAFIICWLPFHVLTFLDAL</span><span class="topo-inside">AWM</span></span>
<span class="topo-ruler">       370       380       390       400       410 </span>
<span class="topo-line"><span class="topo-inside">GVINSCEVIAVIDLA</span><span class="topo-membrane">LPFAILLGFTNSCVNPFLYCFV</span><span class="topo-outside">GNRFQQKLRSVF</span><span class="topo-unknown">RV</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>105</td>
      <td>1001</td>
      <td>1105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>106</td>
      <td>1106</td>
      <td>1106</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>115</td>
      <td>121</td>
      <td>39</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>144</td>
      <td>46</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>149</td>
      <td>69</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>158</td>
      <td>77</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>180</td>
      <td>83</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>186</td>
      <td>105</td>
      <td>110</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>216</td>
      <td>111</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>224</td>
      <td>141</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>238</td>
      <td>160</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>239</td>
      <td>259</td>
      <td>163</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>283</td>
      <td>184</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>309</td>
      <td>208</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>317</td>
      <td>234</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>320</td>
      <td>331</td>
      <td>244</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>357</td>
      <td>256</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>375</td>
      <td>282</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>376</td>
      <td>397</td>
      <td>300</td>
      <td>321</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>409</td>
      <td>322</td>
      <td>333</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41594-018-0079-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5xjm">5XJM</a></td>
      <td>3.2</td>
      <td>P2(1)2(1)2</td>
      <td>BRIL-AT2R fusion; BRIL replaces ICL3; N-terminal HA signal sequence, FLAG tag, TEV cleavage site; C-terminal His6 tag; complex with <a href="/xray-mp-wiki/reagents/ligands/s1i8/">S1I8</a> and <a href="/xray-mp-wiki/reagents/antibodies/fab4a03/">Fab4A03</a> antibody fragment</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/s1i8/">S1I8</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) ([Bac-to-Bac System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression system)
- **Construct**: BRIL-AT2R chimera; AT2R residues 1-34 and 336-363 truncated; N-terminal BRIL (apocytochrome b562RIL, Met7Trp, His102Ile, Arg106L) fused via 4-residue linker (Gly-Ser-Gly-Ser); N-terminal HA signal sequence, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10x His tag, TEV cleavage site
- **Notes**: AT2R gene sequence (UNIPROT P50052) codon-optimized for insect cell expression, cloned into [pFastBac1](/xray-mp-wiki/reagents/vectors/pfastbac1/) vector. [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) infected with [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/), membranes prepared by hypotonic lysis and high osmotic wash.


**Purification:**

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/)
- **Expression construct**: BRIL-AT2R (BRIL replaces ICL3); N-terminal HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) site; C-terminal His6 tag
- **Tag info**: [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), His6 (C-terminal)

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
      <td>Membrane preparation</td>
      <td>Cell lysis and membrane isolation</td>
      <td></td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (HEPES Buffer)</a> pH 7.5, 20 mM KCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a>, protease inhibitor cocktail</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Sf9 Insect Cells</a> harvested by centrifugation (7,000g, 10 min, 4 C), flash-frozen at -80 C, resuspended and lysed under hypotonic conditions</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 800 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1.0% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Membranes solubilized with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> and <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> supplemented with <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> (100 mg/ml) and excess s-AngII; 1 hour at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a></td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, s-AngII + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> resin pre-equilibrated; incubation 12-16 hours at 4 C; washed with 10 column volumes of wash buffer, 3 CVs of elution buffer containing s-AngII</td>
    </tr>
    <tr>
      <td>Elution</td>
      <td>Metal affinity elution</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a></td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, s-AngII + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Elution with buffer containing excess s-AngII to maintain receptor-ligand complex</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase SEC Resin</a></td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Monodisperse <a href="/xray-mp-wiki/proteins/gpcr/at2r/">Angiotensin II Type 2 Receptor</a>-<a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>/Fab4A03 complex isolated for crystallization</td>
    </tr>
  </tbody>
</table>
**Final sample**: 10 mg/ml in 25 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 200 mM [Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)
**Purity**: Monodisperse peak by [Size Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/proteins/gpcr/at2r/">Angiotensin II Type 2 Receptor</a>-<a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>/Fab4A03 complex + s-AngII, 10 mg/ml</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at 100 K at SPring-8 BL32XU micro-focus beamline. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> with MOLREP. 470 datasets collected with KAMO system and merged. High Rmerge due to large variety of crystals, not poor datasets.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5xjm">5XJM</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">G</span><span class="topo-outside">CSQKPSDKHLDA</span><span class="topo-membrane">IPILYYIIFVIGFLVNIVVVT</span><span class="topo-inside">LFCCQKGPKKVSSIYIF</span><span class="topo-membrane">NLAVADLLLLATLPLWATYY</span><span class="topo-outside">SYRYDWLF</span><span class="topo-membrane">GPVMCKVFGSFLTLNMFASIFFIT</span><span class="topo-inside">CMSVDRYQSVIYPFLSQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RRNPWQASYIV</span><span class="topo-membrane">PLVWCMACLSSLPTFYFRD</span><span class="topo-outside">VRTIEYLGVNACIMAFPPEKYA</span><span class="topo-membrane">QWSAGIALMKNILGFIIPLIFIA</span><span class="topo-inside">TCYFGIRKHLLKTNADLEDNWETLNDNLKVIEKADNAAQVKDALT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KMRAAALDAQKATP</span><span class="topo-unknown">PKLEDKSPDSPEMK</span><span class="topo-inside">DFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLKNRITRDQVLKMAAA</span><span class="topo-membrane">VVLAFIICWLPFHVLTFLDALAWM</span><span class="topo-outside">GVINSC</span></span>
<span class="topo-ruler">       370       380       390       400       410       420  </span>
<span class="topo-line"><span class="topo-outside">EVIAV</span><span class="topo-membrane">IDLALPFAILLGFTNSCVNPFL</span><span class="topo-inside">YCF</span><span class="topo-unknown">VGNRFQQKLRSVFRVPITWLQGKRESENLYFQ</span></span>
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
      <td>1</td>
      <td>34</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>13</td>
      <td>35</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>34</td>
      <td>47</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>51</td>
      <td>68</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>71</td>
      <td>85</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>79</td>
      <td>105</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>103</td>
      <td>113</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>131</td>
      <td>137</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>150</td>
      <td>165</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>172</td>
      <td>184</td>
      <td>205</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>173</td>
      <td>195</td>
      <td>206</td>
      <td>228</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>209</td>
      <td>229</td>
      <td>242</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>254</td>
      <td>1001</td>
      <td>1045</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>268</td>
      <td>1046</td>
      <td>1059</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>269</td>
      <td>315</td>
      <td>1060</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>330</td>
      <td>246</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>354</td>
      <td>261</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>365</td>
      <td>285</td>
      <td>295</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>387</td>
      <td>296</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>388</td>
      <td>390</td>
      <td>318</td>
      <td>320</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>391</td>
      <td>422</td>
      <td>321</td>
      <td>352</td>
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

### Helix 8 conformational change upon AngII binding

In the AngII-bound AT2R structure, helix 8 shifts from a non-canonical bent
conformation (observed in the partial agonist [Sar1,Ile8]-AngII-bound AT2R structure,
PDB 5XJM) to a canonical [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) helix 8 conformation parallel to the membrane. This
shift is caused by pi-pi interactions between Phe325^8.50 in helix 8 and Phe316^7.51
and Phe320^7.55 in TM7. These pi-pi interactions are not visible in the compound
1/2-bound AT2R structure (PDB 5UNF). The canonical helix 8 conformation suggests
that AT2R can engage G proteins and [Beta-Arrestin](/xray-mp-wiki/concepts/signaling-receptors/beta-arrestin/), although downstream signaling
is not transmitted by steric blocking.

### Deep ligand-binding pocket and Met128^3.36 rearrangement

Met128^3.36, located at the deep end of the AT2R ligand-binding pocket, moves away
toward Phe308^7.43 upon AngII binding to accommodate the Phe8 side chain of
[Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/). The equivalent residues in [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/) (Leu112^3.36 and Phe308^7.43) form
a hydrophobic core that must rearrange to accommodate Phe8, leading to rotation of
helix 7. This rearrangement at the bottom of the ligand-binding pocket is a key
feature distinguishing full agonist (AngII) from partial agonist ([Sar1,Ile8]-AngII)
binding.

### Asn111^3.35-Asn295^7.46 internal lock

The internal lock between Asn111^3.35 and Asn295^7.46 (equivalent to Asn127^3.35
and Ser311^7.46 in AT2R numbering) is disrupted upon AngII binding. In the
[Sar1,Ile8]-AngII-[Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) complex (PDB 6DO1), one hydrogen bond is maintained at this
internal lock, whereas two bonds are observed in the antagonist-bound inactive
conformation (PDB 4YAY). The complete disruption of this internal lock by full
agonist AngII binding may lead to full active conformation of AT2R. This internal
lock state differs from [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/) and could provide a molecular basis for the high basal
activity of AT2R.

### Activation mechanism comparison with AT1R

The AT2R-AngII structure reveals activation features that can be compared with [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/)
structures. In the active [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/) (PDB 6DO1) bound to partial agonist [S1I8](/xray-mp-wiki/reagents/ligands/s1i8/), one
hydrogen bond is maintained at the Asn111^3.35-Asn295^7.46 internal lock, while
in the inactive [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/) (PDB 4YAY) bound to antagonist [ZD7155](/xray-mp-wiki/reagents/ligands/zd7155/), two bonds are observed.
The full agonist AngII binding to AT2R appears to completely disrupt this internal
lock, similar to AngII binding to [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/). Both AT2R and [AT1R](/xray-mp-wiki/proteins/gpcr/at1r/) share conserved
activation motifs including PIF, [NPxxY Motif](/xray-mp-wiki/concepts/structural-mechanisms/npxxy-motif/), and DRY motifs, but the deep ligand-binding
pocket rearrangement differs between the two receptors.

### Non-canonical helix VIII blocks G protein/beta-arrestin binding

In the Cpd 1- and Cpd 2-bound [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) structures (PDB 5UNF, 5UNG, 5UNH), helix VIII
adopts a non-canonical conformation by flipping over to interact with the intracellular
ends of helices III, V, and VI. This conformation is stabilized by hydrophobic
interactions from Phe325^8.50, Leu329^8.54, Val332^8.57, and Phe333^8.58, as well
as polar interactions from Arg324^8.49, Gln326^8.51, and Lys328^8.53. Molecular
dynamics simulations (4 us total, 8 independent runs) confirm the stability of this
conformation. Helix VIII sterically blocks the G protein/beta-arrestin binding site,
explaining the lack of signaling responses in standard cellular assays. When
experimentally relocated to the canonical position, helix VIII relaxes into a
membrane-bound conformation accompanied by inward shift of helix VI toward the
inactive state.

### Active-like conformation of the 7TM bundle

All three AT2R structures (PDB 5UNF, 5UNG, 5UNH) display an active-like conformation
of the 7TM bundle despite being bound to antagonists. Helix VI shows an ~11.5 A
outward displacement at its intracellular end, while helix VII exhibits a ~4.9 A
inward displacement. Helix V shifts ~4.8 A toward the ligand-binding pocket at its
extracellular end. Conserved activation micro-switches are rearranged: the [PIF Motif](/xray-mp-wiki/concepts/pif-motif/)
(Pro223^5.50-Ile132^3.40-Phe265^6.44), [DRY Motif](/xray-mp-wiki/concepts/dry-motif/) (Arg142^3.50 rotated ~90 degrees),
and [NPxxY Motif](/xray-mp-wiki/concepts/structural-mechanisms/npxxy-motif/) (Tyr318^7.53 shifted ~6.5 A and rotated ~45 degrees). The putative
sodium-binding pocket is collapsed due to helix VII inward shift. AT2R has a rare
alanine at position 6.37 (vs. hydrophobic residue in ~97% of class A GPCRs), which
facilitates activation-related conformational changes.

### Fab4A03 antibody fragment as positive allosteric modulator

The [Fab4A03](/xray-mp-wiki/reagents/antibodies/fab4a03/) antibody fragment binds to the extracellular vestibule of AT2R and acts as a positive allosteric modulator, increasing the binding affinity of both s-AngII (Kd: 2.76 nM without Fab4A03, 0.56 nM with Fab4A03) and [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) for the receptor. No direct interaction between s-AngII and Fab4A03 was observed (distance > 7 A). The Fab4A03 binding site overlaps with the positive allosteric modulator binding site of the M2 muscarinic acetylcholine receptor (PDB 4MQT). The Fab also functioned as a crystallization chaperone, enabling the 3.2 A structure determination of the AT2R-s-AngII complex. 


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/at1r/">Angiotensin II Type 1 Receptor</a> — Close homolog (34% identity); AT2R and [Angiotensin II Type 1 Receptor](/xray-mp-wiki/proteins/gpcr/at1r/) have distinct signaling properties and structural differences in ligand-binding pocket and helix VIII conformation
- <a href="/xray-mp-wiki/reagents/ligands/angiotensin-ii/">Angiotensin II</a> — Endogenous full agonist peptide ligand of [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/reagents/ligands/s1i8/">S1I8 Peptide</a> — Partial agonist analog used in previous [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) structure (PDB 5XJM) for comparison
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hydrogen Succinate (CHS)</a> — Membrane protein stabilizer used during [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) purification
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used as LCP crystallization matrix for [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) crystallized by LCP method (both synchrotron and XFEL)
- <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> — Cysteine alkylating agent used during [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/) solubilization to prevent disulfide formation
- <a href="/xray-mp-wiki/concepts/signaling-receptors/beta-arrestin/">Beta-Arrestin</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus Expression System</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/reagents/additives/16-hexanediol/">1,6-Hexanediol</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/reagents/additives/potassium-formate/">Potassium Formate</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size Exclusion Chromatography</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase SEC Resin</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Sf9 Insect Cells</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/npxxy-motif/">NPxxY Motif</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/reagents/ligands/zd7155/">ZD7155</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (HEPES Buffer)</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
- <a href="/xray-mp-wiki/proteins/gpcr/at2r/">Angiotensin II Type 2 Receptor</a> — Referenced in [Angiotensin II Type 2 Receptor](/xray-mp-wiki/proteins/gpcr/at2r/)
