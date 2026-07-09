---
title: "M3 Muscarinic Acetylcholine Receptor"
created: 2026-05-28
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10867, doi/10.1016##j.str.2014.08.022]
verified: regex
uniprot_id: P08483
---

# M3 Muscarinic Acetylcholine Receptor

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P08483">UniProt: P08483</a>

<span class="expr-badge">Rattus norvegicus</span>

## Overview

The M3 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine) receptor (M3 mAChR) is a class A G protein-coupled receptor that mediates smooth muscle contraction, glandular secretion, and neuronal signaling through Gq/11-coupled pathways. It is a major therapeutic target for conditions including overactive bladder, chronic obstructive pulmonary disease, and hyperhidrosis. Multiple crystal structures of the rat M3 receptor have been solved using T4 lysozyme (T4L) fusion constructs in the third intracellular loop, revealing the binding modes of antagonists including [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium) and [NMS](/xray-mp-wiki/reagents/ligands/n-methylscopolamine) at resolutions up to 2.8 A.


## Publications

### doi/10.1038##nature10867

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4daj">4DAJ</a></td>
      <td>3.4 A</td>
      <td>P 1</td>
      <td>Rat M3 muscarinic receptor, N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG tag</a>, N-glycosylation mutants (4 asparagine to glutamine at positions N6, N15, N41, N48), <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease site at residues 50-56, ICL3 replaced by T4 lysozyme (residues 259-482), C-terminal His tag (6His)
</td>
      <td>Tiotropium</td>
    </tr>
  </tbody>
</table>
 - R-work 25.1%, R-free 30.3%; Data collection: 76 crystals merged. Cell dimensions: a=54.8, b=61.3, c=176.9 A, alpha=85.9, beta=89.9, gamma=84.9 degrees. Anisotropic diffraction with superior quality along a* and b* axes compared to c*. Completeness decreases with resolution from 90.6% overall to 85.9% in highest shell.


**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: Rat M3 muscarinic receptor with N-terminal [FLAG tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) epitope tag, cleavable signal sequence, four N-glycosylation site asparagine mutations (to glutamine), [TEV](/xray-mp-wiki/reagents/additives/tev-protease/) protease site at residues 50-56, ICL3 replaced by T4 lysozyme variant (dsT4L or mT4L) between residues 259 and 482, C-terminal truncation at residue 569, His tag (6 or 8 histidines depending on construct)


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
      <td>Sf9 cell expression</td>
      <td>Baculovirus expression in Sf9 insect cells</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Membranes prepared from transfected COS-7 cells for binding assays; Sf9 cells for purification</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane solubilization</td>
      <td>--</td>
      <td>-- + --</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Nickel NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Nickel NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Nickel NTA</a> resin</td>
      <td>-- + --</td>
      <td>First affinity purification step via C-terminal His tag</td>
    </tr>
    <tr>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG tag</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG tag</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG tag</a> resin</td>
      <td>-- + --</td>
      <td>Second affinity purification step via N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG tag</a> epitope tag</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease cleavage</td>
      <td>--</td>
      <td>-- + --</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease cleaved N-terminal extracellular tail; cleaved constructs retained similar ligand binding affinity</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size exclusion chromatography</a></td>
      <td>Size exclusion column</td>
      <td>-- + --</td>
      <td>Final purification step; monodispersity confirmed by analytical <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4daj">4DAJ</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GDPLGGHT</span><span class="topo-outside">IWQ</span><span class="topo-membrane">VVFIAFLTGFLALVTIIGNILVIV</span><span class="topo-inside">AFKVNKQLKTVNNYF</span><span class="topo-membrane">LLSLACADLIIGVISMNLFTTYII</span><span class="topo-outside">MNRWALGNLA</span><span class="topo-membrane">CDLWLSIDYVASNASVMNLLVISF</span><span class="topo-inside">DRYFSITRPLTY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RAKRTTKRAG</span><span class="topo-membrane">VMIGLAWVISFVLWAPAILFW</span><span class="topo-outside">QYFVGKRTVPPGECFIQFLSEP</span><span class="topo-membrane">TITFGTAIAAFYMPVTIMTIL</span><span class="topo-inside">YWRIYKETEKMNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">PSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470         </span>
<span class="topo-line"><span class="topo-inside">TWDAYLIKE</span><span class="topo-unknown">KKA</span><span class="topo-inside">AQTL</span><span class="topo-membrane">SAILLAFIITWTPYNIMVLVNTFC</span><span class="topo-outside">DSCIPK</span><span class="topo-membrane">TYWNLGYWLCYINSTVNPVCY</span><span class="topo-inside">ALCN</span><span class="topo-unknown">KTFRTTFK</span><span class="topo-inside">T</span><span class="topo-unknown">LLLCQCDKRKRRKQQYQQRQSVIFHKRVPEQALHHHHHH</span></span>
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
      <td>8</td>
      <td>56</td>
      <td>63</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>11</td>
      <td>64</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>35</td>
      <td>67</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>50</td>
      <td>91</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>74</td>
      <td>106</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>84</td>
      <td>130</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>108</td>
      <td>140</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>130</td>
      <td>164</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>151</td>
      <td>186</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>173</td>
      <td>207</td>
      <td>228</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>194</td>
      <td>229</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>204</td>
      <td>250</td>
      <td>259</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>365</td>
      <td>1001</td>
      <td>1161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>369</td>
      <td>482</td>
      <td>485</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>370</td>
      <td>372</td>
      <td>486</td>
      <td>488</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>373</td>
      <td>376</td>
      <td>489</td>
      <td>492</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>400</td>
      <td>493</td>
      <td>516</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>401</td>
      <td>406</td>
      <td>517</td>
      <td>522</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>427</td>
      <td>523</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>431</td>
      <td>544</td>
      <td>547</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>432</td>
      <td>439</td>
      <td>548</td>
      <td>555</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>440</td>
      <td>440</td>
      <td>556</td>
      <td>556</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>479</td>
      <td>557</td>
      <td>595</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1016##j.str.2014.08.022

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u14">4U14</a></td>
      <td>3.6 A</td>
      <td>P41212</td>
      <td>Rat M3 muscarinic receptor, N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG tag</a>, N-glycosylation mutants (4 asparagine to glutamine), <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease site at residues 50-56, ICL3 replaced by T4 lysozyme (residues 259-482), C-terminal His tag
</td>
      <td>Tiotropium</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u15">4U15</a></td>
      <td>2.8 A</td>
      <td>C2</td>
      <td>Rat M3 muscarinic receptor, N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG tag</a>, N-glycosylation mutants, <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease site at residues 50-56, ICL3 replaced by mT4L (minimal T4 lysozyme with GGSGG linker), C-terminal truncation at residue 569, His tag
</td>
      <td>Tiotropium</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u16">4U16</a></td>
      <td>3.7 A</td>
      <td>C2</td>
      <td>Rat M3 muscarinic receptor, N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG tag</a>, N-glycosylation mutants, <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease site at residues 50-56, ICL3 replaced by mT4L (minimal T4 lysozyme with GGSGG linker), C-terminal truncation at residue 569, His tag
</td>
      <td>N-methylscopolamine</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: Rat M3 muscarinic receptor with N-terminal [FLAG tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) epitope tag, cleavable signal sequence, four N-glycosylation site asparagine mutations (to glutamine), [TEV](/xray-mp-wiki/reagents/additives/tev-protease/) protease site at residues 50-56, ICL3 replaced by T4 lysozyme variant (dsT4L or mT4L) between residues 259 and 482, C-terminal truncation at residue 569, His tag (6 or 8 histidines depending on construct)


**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>M3-dsT4L bound to <a href="/xray-mp-wiki/reagents/ligands/tiotropium">Tiotropium</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>M3-dsT4L crystallized in higher symmetry space group P41212 compared to P1 for original M3-wtT4L (4DAJ). Crystals were not twinned. Resolution 3.6 A, lower than original P1 structure (3.4 A). Solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using wtT4L (PDB 4LZM) as search model.
</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>M3-mT4L bound to <a href="/xray-mp-wiki/reagents/ligands/tiotropium">Tiotropium</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals in space group C2 with block-like morphology, strongly birefringent. Data collected to 2.8 A resolution. 37 crystals used. Rwork/Rfree 23.0/26.1%. Solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using M3 structure from 4DAJ and wtT4L (PDB 4LZM) or triple cysteine <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> (PDB 152L) as search models.
</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>M3-mT4L bound to <a href="/xray-mp-wiki/reagents/ligands/n-methylscopolamine">NMS</a> (<a href="/xray-mp-wiki/reagents/n-methylscopolamine/">NMS</a>)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Same crystallization condition as <a href="/xray-mp-wiki/reagents/ligands/tiotropium">Tiotropium</a>-bound M3-mT4L. 12 crystals used. Resolution 3.7 A (space group C2). Rwork/Rfree 23.9/28.5%. Binding pocket interactions nearly identical to <a href="/xray-mp-wiki/reagents/ligands/tiotropium">Tiotropium</a>-bound structure.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u14">4U14</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GDPLGGH</span><span class="topo-inside">TIWQ</span><span class="topo-membrane">VVFIAFLTGFLALVTIIGNIL</span><span class="topo-outside">VIVAFKVNKQLKTVNNYFLLS</span><span class="topo-membrane">LACADLIIGVISMNLFTTYII</span><span class="topo-inside">MNRWALGNL</span><span class="topo-membrane">ACDLWLSIDYVASNASVMNLL</span><span class="topo-outside">VISFDRYFSITRPLTY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">RAKRTTKRAGVMIG</span><span class="topo-membrane">LAWVISFVLWAPAILFWQYFV</span><span class="topo-inside">GKRTVPPGEC</span><span class="topo-membrane">FIQFLSEPTITFGTAIAAFYMPVTI</span><span class="topo-outside">MTILYWRIYKETEKMNCFEMLRIDEGLRLKIYKDCEGYYTIGIGHLLTKS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">PSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRCALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQCPNRAKRVITTFRTG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460</span>
<span class="topo-line"><span class="topo-outside">TWDAYLIKEKKAAQTLSAI</span><span class="topo-membrane">LLAFIITWTPYNIMVLVNTFC</span><span class="topo-inside">DSC</span><span class="topo-membrane">IPKTYWNLGYWLCYINSTVNPVC</span><span class="topo-outside">YALCN</span><span class="topo-unknown">KTFRTTFKT</span><span class="topo-outside">LLL</span><span class="topo-unknown">CQCDKRKRRKHHHHHHH</span></span>
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
      <td>8</td>
      <td>11</td>
      <td>63</td>
      <td>66</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>32</td>
      <td>67</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>53</td>
      <td>88</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>74</td>
      <td>109</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>83</td>
      <td>130</td>
      <td>138</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>104</td>
      <td>139</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>134</td>
      <td>160</td>
      <td>189</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>155</td>
      <td>190</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>165</td>
      <td>211</td>
      <td>220</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>221</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>379</td>
      <td>246</td>
      <td>495</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>380</td>
      <td>400</td>
      <td>496</td>
      <td>516</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>401</td>
      <td>403</td>
      <td>517</td>
      <td>519</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>426</td>
      <td>520</td>
      <td>542</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>427</td>
      <td>431</td>
      <td>543</td>
      <td>547</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>432</td>
      <td>440</td>
      <td>548</td>
      <td>556</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>441</td>
      <td>443</td>
      <td>557</td>
      <td>559</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u15">4U15</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GDPLGGH</span><span class="topo-outside">TIWQVVFIAF</span><span class="topo-membrane">LTGFLALVTIIGNILVIV</span><span class="topo-inside">AFKVNKQLKTVNNYF</span><span class="topo-membrane">LLSLACADLIIGVISMN</span><span class="topo-outside">LFTTYIIMNRWALGNLACD</span><span class="topo-membrane">LWLSIDYVASNASVMNLL</span><span class="topo-inside">VISFDRYFSITRPLTY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RAKRTTKRAGVM</span><span class="topo-membrane">IGLAWVISFVLWAPAILF</span><span class="topo-outside">WQYFVGKRTVPPGECFIQFLSEPT</span><span class="topo-membrane">ITFGTAIAAFYMPVTIMTI</span><span class="topo-inside">LYWRIYKETEKMNIFEMLRIDEGGGSGGDEAEKLFNQDVDAAVRGIL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">RNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYLIKEKKAAQTL</span><span class="topo-membrane">SAILLAFIITWTPYNIMVL</span><span class="topo-outside">VNTFCDSC</span></span>
<span class="topo-ruler">       370       380       390       400       410        </span>
<span class="topo-line"><span class="topo-outside">IPKTYWNL</span><span class="topo-membrane">GYWLCYINSTVNPVCYAL</span><span class="topo-inside">CNKTFRTTFKTL</span><span class="topo-unknown">LLCQCDKRKRRKHHHHHHHH</span></span>
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
      <td>7</td>
      <td>56</td>
      <td>62</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>17</td>
      <td>63</td>
      <td>72</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>35</td>
      <td>73</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>50</td>
      <td>91</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>67</td>
      <td>106</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>86</td>
      <td>123</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>142</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>132</td>
      <td>160</td>
      <td>187</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>150</td>
      <td>188</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>174</td>
      <td>206</td>
      <td>229</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>193</td>
      <td>230</td>
      <td>248</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>194</td>
      <td>333</td>
      <td>249</td>
      <td>492</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>334</td>
      <td>352</td>
      <td>493</td>
      <td>511</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>368</td>
      <td>512</td>
      <td>527</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>386</td>
      <td>528</td>
      <td>545</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>398</td>
      <td>546</td>
      <td>557</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>418</td>
      <td>558</td>
      <td>577</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u16">4U16</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GDPLGGH</span><span class="topo-outside">TIWQ</span><span class="topo-membrane">VVFIAFLTGFLALVTIIGNILVIVAFK</span><span class="topo-inside">VNKQLKTVNNY</span><span class="topo-membrane">FLLSLACADLIIGVISMNLFTTYII</span><span class="topo-outside">MNRWALGNL</span><span class="topo-membrane">ACDLWLSIDYVASNASVMNLLVISF</span><span class="topo-inside">DRYFSITRPLTY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RAKRTTKRA</span><span class="topo-membrane">GVMIGLAWVISFVLWAPAILFW</span><span class="topo-outside">QYFVGKRTVPPGEC</span><span class="topo-membrane">FIQFLSEPTITFGTAIAAFYMPVTIMTILYW</span><span class="topo-inside">RIYKETEKMNIFEMLRIDEGGGSGGDEAEKLFNQDVDAAVRGIL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">RNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYLIKEKKAAQT</span><span class="topo-membrane">LSAILLAFIITWTPYNIMVLVNTFC</span><span class="topo-outside">DSC</span></span>
<span class="topo-ruler">       370       380       390       400       410        </span>
<span class="topo-line"><span class="topo-outside">IPK</span><span class="topo-membrane">TYWNLGYWLCYINSTVNPVCYAL</span><span class="topo-inside">CN</span><span class="topo-unknown">KTFRTTFKTLLLCQCDKRKRRKHHHHHHHH</span></span>
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
      <td>8</td>
      <td>11</td>
      <td>63</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>38</td>
      <td>67</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>49</td>
      <td>94</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>74</td>
      <td>105</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>83</td>
      <td>130</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>108</td>
      <td>139</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>129</td>
      <td>164</td>
      <td>184</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>151</td>
      <td>185</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>165</td>
      <td>207</td>
      <td>220</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>196</td>
      <td>221</td>
      <td>251</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>332</td>
      <td>252</td>
      <td>491</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>357</td>
      <td>492</td>
      <td>516</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>363</td>
      <td>517</td>
      <td>522</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>364</td>
      <td>386</td>
      <td>523</td>
      <td>545</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>387</td>
      <td>388</td>
      <td>546</td>
      <td>547</td>
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

### T4L fusion variant optimization for GPCR crystallization

The M3 receptor was used to demonstrate that modified T4 lysozyme variants can improve crystal quality compared to wild-type T4L. The original M3-wtT4L fusion produced twinned crystals (P1 space group) requiring 70 crystals to yield a 3.4 A structure. Replacing wtT4L with dsT4L (disulfide-stabilized) yielded untwinned crystals in higher symmetry P41212 space group at 3.6 A. Replacing wtT4L with mT4L (minimal, N-terminal lobe deleted) yielded untwinned C2 crystals at 2.8 A resolution, an improvement over the wtT4L construct. The mT4L variant eliminated epitaxial twinning by providing only one T4L packing arrangement instead of two.

### Tiotropium binding mode at M3 receptor

[Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium) binds to the orthosteric pocket of the M3 muscarinic receptor with nearly identical binding mode across all three crystal structures (M3-wtT4L, M3-dsT4L, M3-mT4L). The tropane moiety occupies the central binding pocket while the tropic acid ester extends toward the extracellular side. The binding mode is conserved between [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium) and [NMS](/xray-mp-wiki/reagents/ligands/n-methylscopolamine) bound structures, confirming the orthosteric binding site.

### Crystal packing and twinning mechanism

M3-wtT4L crystals exhibit epitaxial twinning due to two different T4L packing arrangements that alternate in successive layers. The M3 receptor forms antiparallel dimers in all three constructs. In M3-wtT4L, four molecules occupy the asymmetric unit with two distinct T4L orientations. M3-dsT4L has one molecule per asymmetric unit with single T4L packing. M3-mT4L has two molecules per asymmetric unit with the receptor forming two oligomerization interfaces, positioning receptors in a linear arrangement. The smaller interface is mediated by helices 1 and 2, while a second antiparallel interface forms between helices 4 and 5.

### Molecular dynamics reveals receptor-specific dynamics

Molecular dynamics simulations comparing M2 and M3 receptors bound to [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium) revealed several key differences. Extracellular loop 2 (ECL2) is significantly more mobile in the M2 receptor than in M3, as shown by broader RMSD distributions in M2. This difference may contribute to [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium)'s slower off-rate from the M3 receptor. TM5 is more mobile in the M3 simulation, fluctuating between conformations similar to both the M3 and M2 crystal structures. [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium) loses approximately half of its hydration shell as it enters the extracellular vestibule, with similar behavior observed in both M2 and M3 simulations.

### G protein coupling interface residues

Mutagenesis studies identified key residues involved in M3-Gq coupling. S493 (6.38) is conserved in M1, M3, and M5 but not M2/M4, and forms a hydrogen bond with Y250 (5.58) in TM5. Mutation of S493 to arginine or [Glycine](/xray-mp-wiki/reagents/buffers/glycine) severely interfered with G protein signaling without affecting ligand binding. L173 in ICL2 was identified as a critical M3/Gq contact site. Homology modeling of the M3-Gq complex using the beta2AR-Gs structure as template suggests L173 binds a hydrophobic pocket on Gqalpha similar to the F139-Galphas interaction in the beta2AR complex.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a> — Co-crystallized antagonist in PDB 4U14 and 4U15
- <a href="/xray-mp-wiki/reagents/ligands/n-methylscopolamine/">N-methylscopolamine (NMS)</a> — Co-crystallized antagonist in PDB 4U16
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) lipid matrix used for all M3 structures
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method for all M3-T4L structures
- <a href="/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/">M1 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor GPCR; M1 and M4 structures solved in same study (Thal et al., 2016)
- <a href="/xray-mp-wiki/proteins/gpcr/m2-muscarinic-acetylcholine-receptor/">Human M2 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor GPCR; compared via MD simulations
- <a href="/xray-mp-wiki/proteins/gpcr/m4-muscarinic-acetylcholine-receptor/">Human M4 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor subtype; M4 structure solved in same study as M1 (Thal et al., 2016)
- <a href="/xray-mp-wiki/reagents/ligands/acetylcholine/">Acetylcholine</a> — Endogenous agonist tested in competition binding assays
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component used in purification
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> — Buffer component used in purification
