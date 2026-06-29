---
title: "dsT4L (Disulfide-Stabilized T4 Lysozyme)"
created: 2026-05-28
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, xray-crystallography, membrane-protein]
sources: [doi/10.1016##j.str.2014.08.022]
verified: false
---

# dsT4L (Disulfide-Stabilized T4 Lysozyme)

## Overview

dsT4L is a disulfide-stabilized variant of T4 lysozyme engineered for use as a fusion partner in GPCR crystallography. It contains two engineered disulfide bridges (Cys3-Cys97 and Cys21-Cys142) that restrict the flexible hinge region between the N- and C-terminal lobes of T4 lysozyme, stabilizing a more closed conformation. When fused to the M3 muscarinic receptor in the third intracellular loop, dsT4L eliminated epitaxial twinning observed with wild-type T4L and enabled crystallization in a higher symmetry space group (P41212). The M3-dsT4L structure was solved at 3.6 A resolution (PDB 4U14).


## Publications

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
      <td>dsT4L fused to M3 muscarinic receptor ICL3 (residues 259-482). Two disulfide bridges: Cys3-Cys97 and Cys21-Cys142.
</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/tiotropium">TIOTROPIUM</a> (bound to M3 receptor)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: dsT4L fused to M3 muscarinic receptor. Four cysteines introduced at positions 3, 21, 97, and 142 to form two disulfide bridges. The third bridge described by Matsumura et al. (Cys9-Cys164) was omitted because residue 164 is truncated for compactness. [IODOACETAMIDE](/xray-mp-wiki/reagents/additives/iodoacetamide) treatment deferred until after Ni-NTA purification to allow disulfide bond formation.


**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>M3-dsT4L bound to <a href="/xray-mp-wiki/reagents/ligands/tiotropium">TIOTROPIUM</a></td>
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
      <td>Crystals in higher symmetry space group P41212 compared to P1 for M3-wtT4L (4DAJ). Not twinned. One molecule per asymmetric unit. Resolution 3.6 A. Solved by molecular replacement using wtT4L (PDB 4LZM) as search model.
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
<span class="topo-line"><span class="topo-unknown">GDPLGGH</span><span class="topo-inside">TIWQ</span><span class="topo-membrane">VVFIAFLTGFLALVTIIGNIL</span><span class="topo-outside">VIVAFKVNKQLKTVNNYFLLS</span><span class="topo-membrane">LACADLI</span></span>
<span class="topo-line"><span class="topo-membrane">IGVISMNLFTTYII</span><span class="topo-inside">MNRWALGNL</span><span class="topo-membrane">ACDLWLSIDYVASNASVMNLL</span><span class="topo-outside">VISFDRYFSITRPLTY</span></span>
<span class="topo-line"><span class="topo-outside">RAKRTTKRAGVMIG</span><span class="topo-membrane">LAWVISFVLWAPAILFWQYFV</span><span class="topo-inside">GKRTVPPGEC</span><span class="topo-membrane">FIQFLSEPTITFGTA</span></span>
<span class="topo-line"><span class="topo-membrane">IAAFYMPVTI</span><span class="topo-outside">MTILYWRIYKETEKMNCFEMLRIDEGLRLKIYKDCEGYYTIGIGHLLTKS</span></span>
<span class="topo-line"><span class="topo-outside">PSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRR</span></span>
<span class="topo-line"><span class="topo-outside">CALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQCPNRAKRVITTFRTG</span></span>
<span class="topo-line"><span class="topo-outside">TWDAYLIKEKKAAQTLSAI</span><span class="topo-membrane">LLAFIITWTPYNIMVLVNTFC</span><span class="topo-inside">DSC</span><span class="topo-membrane">IPKTYWNLGYWLCYINS</span></span>
<span class="topo-line"><span class="topo-membrane">TVNPVC</span><span class="topo-outside">YALCN</span><span class="topo-unknown">KTFRTTFKT</span><span class="topo-outside">LLL</span><span class="topo-unknown">CQCDKRKRRKHHHHHHH</span></span>
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
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Disulfide stabilization restricts T4L lobe flexibility

The Cys21-Cys142 disulfide bridge stabilizes a more closed conformation of dsT4L compared to wtT4L, while the Cys3-Cys97 distance remains nearly the same as in wtT4L. This selective stabilization reduces the flexibility between the N- and C-terminal lobes of T4 lysozyme, which otherwise can vary by as much as 11.8 A in GPCR fusion protein structures. The reduced flexibility leads to more ordered crystal packing.

### Elimination of epitaxial twinning in GPCR crystals

M3-wtT4L crystals exhibit epitaxial twinning due to two different T4L packing arrangements that alternate in successive layers. Replacing wtT4L with dsT4L results in only one T4L packing arrangement, eliminating twinning. The dsT4L variant has a more rigid structure that promotes a single crystal contact interface, yielding crystals in higher symmetry space group P41212.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/m3-muscarinic-acetylcholine-receptor/">M3 Muscarinic Acetylcholine Receptor</a> — dsT4L fusion partner; PDB 4U14
- <a href="/xray-mp-wiki/proteins/gpcr/mt4l-lysozyme/">mT4L (Minimal T4 Lysozyme)</a> — Alternative T4L variant used in same study
- <a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a> — Co-crystallized ligand bound to M3-dsT4L
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method used
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — LCP lipid matrix
- <a href="/xray-mp-wiki/reagents/additives/iodoacetamide">IODOACETAMIDE</a> — Reagent used in this study
- <a href="/xray-mp-wiki/reagents/buffers/citrate">CITRATE</a> — Reagent used in this study
