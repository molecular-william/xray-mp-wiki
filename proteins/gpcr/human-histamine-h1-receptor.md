---
title: "Human Histamine H1 Receptor (H1R)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10236]
verified: false
---

# Human Histamine H1 Receptor (H1R)

## Overview

The human histamine H1 receptor (H1R) is a [G Protein](/xray-mp-wiki/concepts/signaling-receptors/g-protein/)-coupled receptor ([GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/)) belonging to the aminergic receptor subfamily of class A GPCRs. H1R is expressed in various human tissues including airway, intestinal, and vascular smooth muscle and brain, where it mediates the effects of histamine in type I hypersensitivity allergic reactions and inflammation. The first X-ray crystal structure of H1R was determined at 3.1 A resolution in complex with the first-generation antagonist [Doxepin](/xray-mp-wiki/reagents/ligands/doxepin) (Shimamura et al., 2011, PDB 3RZE). The structure reveals that doxepin sits deep in the ligand-binding pocket, directly interacting with Trp428^6.48, a highly conserved key residue in GPCR activation. A unique anion-binding region occupied by a phosphate ion was observed at the entrance to the binding pocket, coordinated by Lys179^ECL2, Lys191^5.39, Tyr431^6.51, and His450^7.35. H1R is structurally most similar to the beta2-adrenergic receptor, beta1-adrenergic receptor, and dopamine D3 receptor among known GPCR structures. The structure provides a molecular basis for understanding H1R antagonist specificity.


## Publications

### doi/10.1038##nature10236

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3rze">3RZE</a></td>
      <td>3.1</td>
      <td>I 4 2 2</td>
      <td>Human H1R with N-terminal 19-residue deletion, T4 lysozyme inserted into ICL3 (C54T, C97A), C-terminal TEV cleavage site, yeast-enhanced GFP, and octa-histidine tag</td>
      <td>Doxepin (E isomer), phosphate ion</td>
    </tr>
  </tbody>
</table>
 - R-work 0.2145%, R-free 0.2486%; Data collection: Complete data set to 3.1 A resolution

**Expression:**

- **Expression system**: [Pichia pastoris](/xray-mp-wiki/methods/expression-systems/pichia-pastoris)
- **Construct**: Codon-optimized human H1R with N-terminal 19-residue deletion, T4L in ICL3, TEV cleavage site, yeast-enhanced GFP, octa-histidine tag; cloned into pPIC9K vector
- **Notes**: Expressed in P. pastoris SMD1163 under methanol-inducible AOX1 promoter; induced with 0.5% methanol + 2.5% v/v DMSO at 30 C for 20-24 h

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
      <td>Cell lysis</td>
      <td>Glass bead disruption</td>
      <td>not specified</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 120 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">NaCl</a>, 5% v/v <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 2 mM <a href="/xray-mp-wiki/reagents/additives/edta">EDTA</a>, protease inhibitor cocktail + not specified</td>
      <td>Yeast cells disrupted with 0.5 mm glass beads; membranes collected by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 100,000g; washed with high-salt buffer (1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride">NaCl</a>)</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>not specified</td>
      <td>not specified + 1% w/v <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 0.2% w/v <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a></td>
      <td>Solubilized from P. pastoris membranes</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography">IMAC</a> purification</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography">IMAC</a></td>
      <td>not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a></td>
      <td>C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/gfp">GFP</a> tag cleaved by <a href="/xray-mp-wiki/reagents/protein-tags/tev-protease">TEV Protease</a>; reverse <a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography">IMAC</a> to remove cleaved His-tagged <a href="/xray-mp-wiki/reagents/protein-tags/gfp">GFP</a> and <a href="/xray-mp-wiki/reagents/protein-tags/tev-protease">TEV Protease</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>H1R-<a href="/xray-mp-wiki/reagents/ligands/doxepin">doxepin</a> complex in <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate">CHS</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a></td>
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
      <td>Crystals collected and flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein-LCP mixture: 40% w/w receptor solution, 54% w/w <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a>, 6% w/w <a href="/xray-mp-wiki/reagents/lipids/cholesterol">Cholesterol</a>. The phosphate ion in the reservoir (300 mM ammonium phosphate) was found bound at the entrance to the ligand-binding pocket and acts as a positive modulator of ligand binding.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3rze">3RZE</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">TTMASPQL</span><span class="topo-inside">MPLVV</span><span class="topo-membrane">VLSTICLVTVGLNLLVLY</span><span class="topo-outside">AVRSERKLHTVGNLYIV</span><span class="topo-membrane">SLSVADLIVGAV</span></span>
<span class="topo-line"><span class="topo-membrane">VMPMN</span><span class="topo-inside">ILYLLMSKWSLGRPLCL</span><span class="topo-membrane">FWLSMDYVASTASIFSVFI</span><span class="topo-outside">LCIDRYRSVQQPLRYLKYR</span></span>
<span class="topo-line"><span class="topo-outside">TKTRASATI</span><span class="topo-membrane">LGAWFLSFLWVIPILG</span><span class="topo-inside">WNH</span><span class="topo-unknown">FMQQTSV</span><span class="topo-inside">RREDKCETDFYDVTW</span><span class="topo-membrane">FKVMTAIINF</span></span>
<span class="topo-line"><span class="topo-membrane">YLPTLLMLW</span><span class="topo-outside">FYAKIYKAVRQHCNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSL</span></span>
<span class="topo-line"><span class="topo-outside">NAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAAL</span></span>
<span class="topo-line"><span class="topo-outside">INMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWD</span></span>
<span class="topo-line"><span class="topo-outside">AYLHMNRERKAAKQLGF</span><span class="topo-membrane">IMAAFILCWIPYFIFFM</span><span class="topo-inside">VIAFCKNCCNEHLHMF</span><span class="topo-membrane">TIWLGYINST</span></span>
<span class="topo-line"><span class="topo-membrane">LNPLI</span><span class="topo-outside">YPLCN</span><span class="topo-unknown">ENFKKTFKRIL</span><span class="topo-outside">HI</span><span class="topo-unknown">RSGENLYFQ</span></span>
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
      <td>20</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>13</td>
      <td>28</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>31</td>
      <td>33</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>48</td>
      <td>51</td>
      <td>67</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>68</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>82</td>
      <td>85</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>101</td>
      <td>102</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>129</td>
      <td>121</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>145</td>
      <td>149</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>148</td>
      <td>165</td>
      <td>167</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>155</td>
      <td>168</td>
      <td>174</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>170</td>
      <td>175</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>189</td>
      <td>190</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>377</td>
      <td>209</td>
      <td>419</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>378</td>
      <td>394</td>
      <td>420</td>
      <td>436</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>395</td>
      <td>410</td>
      <td>437</td>
      <td>452</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>425</td>
      <td>453</td>
      <td>467</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>426</td>
      <td>430</td>
      <td>468</td>
      <td>472</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>431</td>
      <td>441</td>
      <td>473</td>
      <td>483</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>442</td>
      <td>443</td>
      <td>484</td>
      <td>485</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>452</td>
      <td>486</td>
      <td>494</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Deep Ligand Binding and Trp428^6.48 Interaction

Doxepin sits approximately 5 A deeper in the binding pocket than ligands in other non-rhodopsin GPCR structures. The tricyclic dibenzo[b,e]oxepin ring makes extensive hydrophobic interactions with Trp428^6.48 (the conserved CWxP motif), which is unique among known non-rhodopsin GPCR structures. This interaction likely stabilizes the hydrophobic packing around helix VI and contributes to the inverse agonist activity of doxepin by locking H1R in an inactive conformation. The highly conserved binding pocket, composed mainly of residues including Ile115^3.40, Phe424^6.44, Trp428^6.48, and Phe432^6.52, explains the low selectivity of first-generation H1R antagonists.

### Anion-Binding Region at Pocket Entrance

A phosphate ion from the crystallization buffer (300 mM ammonium phosphate) was observed coordinated by Lys179^ECL2, Lys191^5.39, Tyr431^6.51, and His450^7.35 at the entrance to the ligand-binding pocket. Except for Tyr431^6.51, these residues are unique to H1R among aminergic receptors. The phosphate ion may act as a positive modulator of ligand binding, as thermostability and ligand affinity increased in the presence of phosphate. The second-generation zwitterionic H1R antagonists (cetirizine, acrivastine, fexofenadine) interact with Lys191^5.39 and/or Lys179^ECL2, providing a structural basis for their enhanced H1R selectivity.

### ECL2 Structure and Ligand Specificity

ECL2 of H1R contains 7 amino acids between the conserved disulfide bridge (Cys100^3.25-Cys180) and helix V, compared to 5 in beta2-AR and 4 in D3R. The extra length is accommodated by increased distance between the extracellular ends of helices III and V (1.5 A vs beta2-AR, 3.1 A vs D3R), creating more space in the ligand-binding pocket for larger second-generation antagonists. Seven residues (Phe168-Val174) before the disulfide were disordered. Doxepin does not interact with ECL2, contributing to its low selectivity.

### H1R Inactivation Mechanism

H1R antagonists act as highly effective inverse agonists, reducing basal receptor activity by up to 78%. The mechanism involves blocking both (1) the activation-related contraction of the extracellular binding pocket (histamine is much smaller than bulky H1R antagonists) and (2) the Trp428^6.48 switch, which in rhodopsin and A2AAR participates in activation-related conformational changes. The extensive interaction between doxepin and Trp428^6.48 is a key feature of H1R inactivation.


## Cross-References

- <a href="/xray-mp-wiki/concepts/signaling-receptors/g-protein/">G Protein</a> — Related entity
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr/">GPCR</a> — H1R is a class A GPCR
- <a href="/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/">Human Beta2-Adrenergic Receptor</a> — Comparative structural analysis with aminergic GPCR
- <a href="/xray-mp-wiki/proteins/gpcr/human-beta-2-adrenergic-receptor/">Human Beta-2 Adrenergic Receptor</a> — Comparative structural analysis
- <a href="/xray-mp-wiki/proteins/gpcr/human-histamine-h3-receptor/">Human Histamine H3 Receptor</a> — Related histamine receptor subtype
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method
- <a href="/xray-mp-wiki/methods/expression-systems/pichia-pastoris/">Pichia Pastoris</a> — Expression host
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Purification method
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Immobilized Metal Affinity Chromatography</a> — Purification method
- <a href="/xray-mp-wiki/reagents/ligands/doxepin/">Doxepin</a> — Co-crystallized antagonist in H1R structure
