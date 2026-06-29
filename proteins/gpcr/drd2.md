---
title: "Human D2 Dopamine Receptor (DRD2)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature25758, doi/10.1038##s41467-020-20221-0, doi/10.1038##s41467-020-14884-y]
verified: false
---

# Human D2 Dopamine Receptor (DRD2)

## Overview

The human D2 dopamine receptor (DRD2) is a class A G protein-coupled receptor that serves as the primary target for both typical and atypical antipsychotic drugs. DRD2 mediates dopamine actions in reward, addiction, coordinated movement, metabolism, and hormonal secretion. Multiple inactive-state structures of DRD2 have been solved in complex with different antipsychotics including [RISPERIDONE](/xray-mp-wiki/reagents/ligands/risperidone) (6C38), haloperidol, and spiperone (7DFP). The spiperone-bound structure (7DFP, 3.1 A) revealed a dynamic extracellular loop 2 (ECL2) conformation and an extended binding pocket that accommodates spiperone phenyl ring, contributing to its selectivity for D2R and 5-HT2AR. The haloperidol-bound structure (2020) revealed a second extended binding pocket (SEBP) formed by TM2, TM3, EL1, and EL2 that is critical for DRD2 activation and subtype selectivity.

## Publications

### doi/10.1038##nature25758

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6c38">6C38</a></td>
      <td>2.9 A</td>
      <td>P212121</td>
      <td>Human DRD2 long variant with N-terminal <a href="/xray-mp-wiki/concepts/truncation">TRUNCATION</a>, T4L fused into ICL3, thermostabilizing mutations I122A, L375A, L379A</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/risperidone">RISPERIDONE</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: DRD2-mbIIIG S121K/L123W with C-terminal TEV protease site, GFP, and octa-histidine tag

### doi/10.1038##s41467-020-20221-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7dfp">7DFP</a></td>
      <td>3.1 A</td>
      <td>C2</td>
      <td>Human DRD2-mbIIIG S121K/L123W with N-terminal <a href="/xray-mp-wiki/concepts/truncation">TRUNCATION</a> (residues 1-34), ICL3 replaced by loop-modified cytochrome b562 (mbIIIG), Fab3089 bound</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/spiperone">SPIPERONE</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: DRD2-mbIIIG S121K/L123W with C-terminal TEV protease site, GFP, and octa-histidine tag

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
      <td>Baculovirus expression in Sf9 cells</td>
      <td>--</td>
      <td>Not specified + --</td>
      <td>Sf9 cells infected at 1.5 x 10^6 cells/ml, MOI 0.05, harvested 84 h later</td>
    </tr>
    <tr>
      <td>Cell lysis and membrane preparation</td>
      <td>Cell lysis in hypotonic buffer followed by membrane collection</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.4, 1 mM EDTA + --</td>
      <td>Membranes resuspended in lysis buffer</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> solubilization</td>
      <td>—</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.4, 150 mM NaCl, 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Solubilized for 2 h at 4 C</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/ni-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/ni-nta/">Ni-NTA</a></td>
      <td>10 mM HEPES pH 7.4, 150 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">IMIDAZOLE</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Eluted with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">IMIDAZOLE</a></td>
    </tr>
    <tr>
      <td>Tag cleavage and SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> cleavage followed by size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL column</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.4, 150 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Purified DRD2-mbIIIG complexed with <a href="/xray-mp-wiki/reagents/ligands/spiperone">SPIPERONE</a> and Fab3089</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a>) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>DRD2-mbIIIG-S121K/L123W complexed with <a href="/xray-mp-wiki/reagents/ligands/spiperone">SPIPERONE</a> and Fab3089 at ~30 mg/ml</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Microcrystals appeared after 2 days, grew to 20 x 2 x 2 um within a week</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein-laden <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a> prepared by mixing protein with monoolein and 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol">CHOLESTEROL</a> at 2:3 volume ratio. Data collected by serial femtosecond crystallography at SACLA XFEL.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7dfp">7DFP</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">NYY</span><span class="topo-membrane">ATLLTLLIAVIVFGNVLVCM</span><span class="topo-outside">AVSREKALQTTTNYL</span><span class="topo-membrane">IVSLAVADLLVATLVMPWVV</span><span class="topo-inside">Y</span></span>
<span class="topo-line"><span class="topo-inside">LEVVGEWKFSRIHCDI</span><span class="topo-membrane">FVTLDVMMCTAKIWNLCAIS</span><span class="topo-outside">IDRYTAVAMPM</span><span class="topo-unknown">LYNTRYS</span><span class="topo-outside">SKRRVT</span></span>
<span class="topo-line"><span class="topo-membrane">VMISIVWVLSFTISCPLLF</span><span class="topo-inside">GLNNADQNECIIANPA</span><span class="topo-membrane">FVVYSSIVSFYVPFIVTLLV</span><span class="topo-outside">YIKIY</span></span>
<span class="topo-line"><span class="topo-outside">IVL</span><span class="topo-unknown">RRRRAD</span><span class="topo-outside">LEDNWETLNDNLKVIEKADNAAQVKDALTKMRAAALDAGS</span><span class="topo-unknown">GSG</span><span class="topo-outside">DILVGQID</span></span>
<span class="topo-line"><span class="topo-outside">DALKLANEGKVKEAQAAAEQLKTTINAYIQKYGSQQKEKKATQML</span><span class="topo-membrane">AIVLGVFIICWLPFF</span></span>
<span class="topo-line"><span class="topo-membrane">ITHILNIH</span><span class="topo-inside">CDCNIPPVL</span><span class="topo-membrane">YSAFTWLGYVNSAVNPIIY</span><span class="topo-outside">TTFN</span><span class="topo-unknown">IEFRKAFLKI</span><span class="topo-outside">LH</span><span class="topo-unknown">CGENLYFQ</span></span>
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
      <td>4</td>
      <td>35</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>24</td>
      <td>38</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>39</td>
      <td>58</td>
      <td>72</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>59</td>
      <td>73</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>76</td>
      <td>93</td>
      <td>109</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>96</td>
      <td>110</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>107</td>
      <td>130</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>120</td>
      <td>148</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>139</td>
      <td>154</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>155</td>
      <td>173</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>175</td>
      <td>189</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>183</td>
      <td>209</td>
      <td>216</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>229</td>
      <td>1003</td>
      <td>1042</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>285</td>
      <td>1066</td>
      <td>375</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>308</td>
      <td>376</td>
      <td>398</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>309</td>
      <td>317</td>
      <td>399</td>
      <td>407</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>318</td>
      <td>336</td>
      <td>408</td>
      <td>426</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>337</td>
      <td>340</td>
      <td>427</td>
      <td>430</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>350</td>
      <td>431</td>
      <td>440</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>351</td>
      <td>352</td>
      <td>441</td>
      <td>442</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##s41467-020-14884-y

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6luq">6LUQ</a></td>
      <td></td>
      <td></td>
      <td>Human DRD2 long variant with N-terminal truncation, engineered with thermostabilizing mutations, crystallized with <a href="/xray-mp-wiki/reagents/ligands/haloperidol">HALOPERIDOL</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/haloperidol">HALOPERIDOL</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: DRD2-mbIIIG S121K/L123W with C-terminal TEV protease site, GFP, and octa-histidine tag

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6luq">6LUQ</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">NYY</span><span class="topo-membrane">ATLLTLLIAVIVFGNVLVC</span><span class="topo-outside">MAVSREKALQTTTNYLI</span><span class="topo-membrane">VSLAVADLLVATLVMPWVV</span><span class="topo-inside">YL</span></span>
<span class="topo-line"><span class="topo-inside">EVVGEWKFSRIH</span><span class="topo-membrane">CDIFVTLDVMMCTASALNLC</span><span class="topo-outside">AISIDRYTAVAMP</span><span class="topo-unknown">MLYN</span><span class="topo-outside">TRYSSKRRVTV</span></span>
<span class="topo-line"><span class="topo-outside">MI</span><span class="topo-membrane">SIVWVLSFTISCPLLFGLN</span><span class="topo-inside">NADQNECIIANPA</span><span class="topo-membrane">FVVYSSIVSFYVPFIVTLL</span><span class="topo-outside">VYIKIYI</span></span>
<span class="topo-line"><span class="topo-outside">VLRRRRKRNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRN</span></span>
<span class="topo-line"><span class="topo-outside">TNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAG</span></span>
<span class="topo-line"><span class="topo-outside">FTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAY</span><span class="topo-unknown">KLSQ</span><span class="topo-outside">QKEKKATQ</span></span>
<span class="topo-line"><span class="topo-outside">MAAI</span><span class="topo-membrane">VAGVFIICWLPFFITHILNIH</span><span class="topo-inside">CDCNIPPVL</span><span class="topo-membrane">YSAFTWLGYVNSAVNPII</span><span class="topo-outside">YTTFN</span><span class="topo-unknown">IEF</span></span>
<span class="topo-line"><span class="topo-unknown">RKAFLKIL</span><span class="topo-outside">H</span><span class="topo-unknown">C</span></span>
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
      <td>3</td>
      <td>35</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>22</td>
      <td>38</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>39</td>
      <td>57</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>58</td>
      <td>74</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>72</td>
      <td>93</td>
      <td>106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>92</td>
      <td>107</td>
      <td>126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>105</td>
      <td>127</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>122</td>
      <td>144</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>123</td>
      <td>141</td>
      <td>157</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>154</td>
      <td>176</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>173</td>
      <td>189</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>348</td>
      <td>208</td>
      <td>382</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>364</td>
      <td>387</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>385</td>
      <td>399</td>
      <td>419</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>394</td>
      <td>420</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>412</td>
      <td>429</td>
      <td>446</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>417</td>
      <td>447</td>
      <td>451</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>418</td>
      <td>428</td>
      <td>452</td>
      <td>462</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>429</td>
      <td>429</td>
      <td>463</td>
      <td>463</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Dynamic ECL2 conformation in DRD2

The spiperone-bound DRD2 structure (7DFP) revealed that ECL2 adopts an extended conformation distinct from the helical conformation seen in the [RISPERIDONE](/xray-mp-wiki/reagents/ligands/risperidone)-bound structure (6C38). In the spiperone structure, ECL2 does not form a hydrophobic patch with Trp100, Leu94, and Ile184, making the binding pocket more exposed. MD simulations suggested the extended ECL2 conformation represents a lower energy state, while the helical conformation in 6C38 is higher energy.

### Extended binding pocket in spiperone-bound DRD2

The spiperone-bound structure reveals an extended binding pocket (EBP) formed by a flipped Phe110 side chain that stacks with Trp90. This EBP accommodates spiperone's phenyl ring and extends from subsite B to subsite C. The EBP is unique among the inactive state DRD2 structures and may contribute to spiperone's high selectivity for D2R over other aminergic receptors. The bottom hydrophobic cleft in the spiperone structure is stabilized by steric contact between TM5 and ECL2, preventing the TM5 shift observed in [RISPERIDONE](/xray-mp-wiki/reagents/ligands/risperidone) and haloperidol structures.

### Second Extended Binding Pocket (SEBP) in DRD2-haloperidol structure

The DRD2-haloperidol complex structure revealed an unexpected second extended binding pocket (SEBP) formed by TM2, TM3, EL1, and EL2. The SEBP partially overlaps with the previously identified DRD3 EBP but is distinct. The outward movement of EL2 makes additional space for the SEBP at DRD2 compared to DRD3. Phe110^3.28 is a key residue: the F110A mutation enhances haloperidol binding 15.33-fold and L-741626 binding 144.18-fold, while F110W or F110Y mutations greatly reduce binding. The SEBP plays a critical role in both DRD2 antagonist binding and agonist activation. Using the SEBP and OBP structures, highly subtype-selective DRD2 agonists (O4SE6 and O8LE6) were discovered that show no activity at DRD3 or DRD4.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/5ht2a-receptor/">Serotonin 5-HT2A Receptor</a> — Spiperone binds with high affinity to both D2R and 5-HT2AR; structural comparison reveals shared binding features
- <a href="/xray-mp-wiki/reagents/ligands/spiperone/">Spiperone</a> — Typical antipsychotic ligand co-crystallized with DRD2 in 7DFP structure
- <a href="/xray-mp-wiki/reagents/ligands/risperidone/">Risperidone</a> — Atypical antipsychotic; risperidone-bound DRD2 (6C38) used for structural comparison
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid component of the lipidic cubic phase crystallization matrix
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl buffer)</a> — Buffer (0.1 M, pH 8.0) used in crystallization reservoir
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">Polyethylene glycol 400 (PEG400)</a> — Precipitant (28-32%) used in crystallization reservoir
- <a href="/xray-mp-wiki/reagents/additives/dimethyl-sulfoxide/">Dimethyl sulfoxide (DMSO)</a> — Additive (5%) used in crystallization reservoir
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used to crystallize DRD2-Fab3089-spiperone complex
- <a href="/xray-mp-wiki/reagents/additives/imidazole">IMIDAZOLE</a> — Reagent used in this study
- <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> — Reagent used in this study
