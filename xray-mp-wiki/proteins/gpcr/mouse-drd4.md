---
title: "Mouse Dopamine Receptor D4 (DRD4)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.48822]
verified: regex
uniprot_id: P51436
---

# Mouse Dopamine Receptor D4 (DRD4)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P51436">UniProt: P51436</a>

<span class="expr-badge">Mus musculus</span>

## Overview

Mouse [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor D4 ([DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/)) is a G-protein-coupled receptor (GPCR) belonging to the D2-like subfamily of [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptors. It is expressed in the frontal cortex and amygdala and plays roles in cognition and emotions. [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) is coupled to Gi/o proteins and downregulates adenylyl cyclase activity. The 3.5-angstrom crystal structure of mouse [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) complexed with the subtype-selective antagonist [L745870](/xray-mp-wiki/reagents/ligands/l745870/) reveals an extended ligand-binding pocket specific for [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/), located between transmembrane helices 2 and 3.


## Publications

### doi/10.7554##eLife.48822

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6iql">6IQL</a></td>
      <td>3.5</td>
      <td>P1</td>
      <td>Mouse <a href="/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/">DRD4</a> (N22 <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, ICL3 replaced with <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a>, F121W/P201I/P317A/C181R) with <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG Tag</a>, complexed with <a href="/xray-mp-wiki/reagents/ligands/l745870/">L745870</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/l745870/">L745870</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Bac-to-Bac Baculovirus Expression System in High5 (Spodoptera frugiperda) cells
- **Construct**: Mouse [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) (GenBank BC051421.1) with N22 [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/), HA signal sequence and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) at N-terminus, [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (residues A1-L106 with M7W/H102I/R106L) replacing ICL3 (A220-A302), [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) site, C-terminal EGFP-10xHis tag. Mutations: F121W, P201I, P317A, C181R
- **Notes**: Expressed for 48 hr. Cells flash-frozen in liquid nitrogen and stored at -80 C

**Purification:**

- **Expression system**: High5 insect cells via Bac-to-Bac Baculovirus
- **Expression construct**: Mouse DRD4-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) chimera with [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), EGFP-His10, mutations F121W/P201I/P317A/C181R
- **Tag info**: N-terminal [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), C-terminal 10xHis-tag, PreScission-cleavable EGFP

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
      <td>Dounce homogenization</td>
      <td>—</td>
      <td>25 mM HEPES pH 7.4, 150 mM NaCl</td>
      <td>Cells homogenized, membranes collected and washed</td>
    </tr>
    <tr>
      <td>Membrane incubation</td>
      <td>Ligand stabilization</td>
      <td>—</td>
      <td>25 mM HEPES pH 7.4, 150 mM NaCl, 30 uM <a href="/xray-mp-wiki/reagents/ligands/l745870/">L745870</a>, 0.2% w/v <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a></td>
      <td>Membranes incubated at 4 C for 1 hr with <a href="/xray-mp-wiki/reagents/ligands/l745870/">L745870</a> antagonist</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Membranes solubilized in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> for membrane protein extraction</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>IMAC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> cobalt resin</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>His10-tag purification</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> digestion</td>
      <td>—</td>
      <td></td>
      <td>EGFP-His10 tag removed by <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>25 mM HEPES pH 7.4, 150 mM NaCl + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.015% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Purified protein concentrated for crystallization</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified DRD4-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) in 25 mM HEPES pH 7.4, 150 mM NaCl, 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.015% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) with [L745870](/xray-mp-wiki/reagents/ligands/l745870/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified DRD4-<a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> with <a href="/xray-mp-wiki/reagents/ligands/l745870/">L745870</a> in buffer containing 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.015% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew within one week. Harvested from <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a> matrix using 50 um micromounts and flash-frozen in liquid nitrogen. Data collected at SPring-8 beamline 41XU</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6iql">6IQL</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDKEFTGAGLGGA</span><span class="topo-outside">GAA</span><span class="topo-membrane">ALVGGVLLIGLVLAGNSLVCVSVAS</span><span class="topo-inside">ERTLQTP</span><span class="topo-membrane">TNYFIVSLAAADLLLAVLVLPLFV</span><span class="topo-outside">YSEVQGGVWLLSPRLCDT</span><span class="topo-membrane">LMAMDVMLCTASIWNLCAISVDRF</span><span class="topo-inside">V</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AVT</span><span class="topo-unknown">VPLRYNQQ</span><span class="topo-inside">GQC</span><span class="topo-membrane">QLLLIAATWLLSAAVASP</span><span class="topo-outside">VVCGLNDVPGRDP</span><span class="topo-unknown">AVCRL</span><span class="topo-outside">ENRDY</span><span class="topo-membrane">VVYSSVCSFFLPCILMLLLYWATFR</span><span class="topo-inside">GLRRWEADLEDNWETLNDNLKVIEKADNAAQVKDALTKMR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">AAALDAQKA</span><span class="topo-unknown">TPPKLEDKSPDSPEM</span><span class="topo-inside">KDFRHGFDILVGQIDDALKLANEGKVKEAQAAAEQLKTTRNAYIQKYLKITGRERKAM</span><span class="topo-membrane">RVLAVVVGAFLVCWTPFFVVHIT</span><span class="topo-outside">RALCPACFVSPRL</span><span class="topo-membrane">VS</span></span>
<span class="topo-ruler">       370       380       390      </span>
<span class="topo-line"><span class="topo-membrane">AVTWLGYVNSALNPIIYTIFN</span><span class="topo-inside">AEFRSV</span><span class="topo-unknown">FRKTLRLRC</span></span>
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
      <td>18</td>
      <td>13</td>
      <td>30</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>21</td>
      <td>31</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>22</td>
      <td>46</td>
      <td>34</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>53</td>
      <td>59</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>77</td>
      <td>66</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>95</td>
      <td>90</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>119</td>
      <td>108</td>
      <td>131</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>123</td>
      <td>132</td>
      <td>135</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>131</td>
      <td>136</td>
      <td>143</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>132</td>
      <td>134</td>
      <td>144</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>152</td>
      <td>147</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>165</td>
      <td>165</td>
      <td>177</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>170</td>
      <td>178</td>
      <td>182</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>171</td>
      <td>175</td>
      <td>183</td>
      <td>187</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>200</td>
      <td>188</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>201</td>
      <td>206</td>
      <td>213</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>249</td>
      <td>1001</td>
      <td>1043</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>264</td>
      <td>1044</td>
      <td>1058</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>265</td>
      <td>312</td>
      <td>1059</td>
      <td>1106</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>313</td>
      <td>322</td>
      <td>304</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>323</td>
      <td>345</td>
      <td>314</td>
      <td>336</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>346</td>
      <td>358</td>
      <td>337</td>
      <td>349</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>381</td>
      <td>350</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>382</td>
      <td>387</td>
      <td>373</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>388</td>
      <td>396</td>
      <td>379</td>
      <td>387</td>
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

### Extended binding pocket (EBP) for subtype selectivity

The crystal structure reveals a secondary binding pocket extending from
the orthosteric binding pocket to a DRD4-specific crevice located between
transmembrane helices 2 and 3. This extended pocket is formed by residues
S91(2.64), L94(2.67), L108(3.28), and G110(3.30) that are unique to
[DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) within the D2-like subfamily. [L745870](/xray-mp-wiki/reagents/ligands/l745870/) inserts a bulky 4-chlorophenyl
group into this crevice, providing the structural basis for its
DRD4-selective antagonism.

### Antagonist mechanism through TM2-TM3 immobilization

[L745870](/xray-mp-wiki/reagents/ligands/l745870/) blocks [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) activation by reducing the moving freedom of
transmembrane helix 3 (TM3). The bulky chemical group inserted into the
TM2-TM3 crevice prevents the relative movement between these helices
required for full activation of class-A GPCRs. Mutagenesis studies showed
that small-to-large mutations S91L and L108F dramatically reduced the
inhibitory effects of [L745870](/xray-mp-wiki/reagents/ligands/l745870/), and S91F abolished dopamine-induced
activity entirely.

### Non-symmetric homodimer

The crystal structure revealed a non-symmetrical homodimer interface
between TM1-3 of Mol-A and TM5-6 of Mol-B, burying 1600 square angstroms
of solvent-accessible surface. This is stabilized by hydrogen bonds and
hydrophobic packing, including polar interactions between S101(A3.21) and
D186(B5.37) extracellularly, and intracellular hydrogen bonds between
A57(1.58)/T135(3.55) and S58(1.59)/G213(5.64). Cross-linking experiments
confirmed [DRD4](/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/) dimerization also occurs in solution.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/drd2/">Human D2 Dopamine Receptor (DRD2)</a> — Related D2-like dopamine receptor; comparison of extended binding pocket determinants
- <a href="/xray-mp-wiki/reagents/ligands/l745870/">L745870</a> — Subtype-selective DRD4 antagonist bound in the 6IQL structure
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — Primary detergent used for purification and crystallization
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (HEPES-KOH Buffer)</a> — 25 mM HEPES pH 7.4 used throughout purification
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Used in cross-linking and SEC buffers
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/gpcr/d4-dopamine-receptor/">DRD4</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> — Additive used in purification or crystallization buffers
