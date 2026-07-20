---
title: "CD9 (Tetraspanin)"
created: 2026-06-09
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-15459-7]
verified: pdb
uniprot_id: P21926
---

# CD9 (Tetraspanin)

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P21926">UniProt: P21926</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

CD9 is a member of the tetraspanin family, a class of four-transmembrane domain proteins that play critical roles in cell adhesion, migration, fertilization, and viral infection. The crystal structure of human CD9 was determined at 2.7 A resolution using the SIRAS method from crystals grown in [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/). The structure reveals a reversed cone-like molecular shape with four transmembrane helices arranged in a teepee-like configuration, creating a large central cavity in the intramembranous region. A [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of CD9 in complex with its partner protein EWI-2 at 7.3 A resolution reveals a 2:2 hetero-tetrameric stoichiometry, with the TM3-4 region of CD9 interacting with the membrane-spanning helix of EWI-2 through small residue contacts (Gly/Ala zipper motif). MD simulations show spontaneous transitions between open and closed conformations of the extracellular loops. The asymmetric molecular shape generates membrane curvature, explaining CD9 localization in microvilli and exosomes. Fertilization assays demonstrate that the large extracellular loop (LEL) is critical for sperm-egg fusion.

## Publications

### doi/10.1038##s41467-020-15459-7

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6k4j">6K4J</a></td>
      <td>2.7 A</td>
      <td>—</td>
      <td>Human CD9 with partial LEL deletion (Thr175-Lys179) and C-terminal tail deletion (Glu226-Val228)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6k4j">6K4J</a></td>
      <td>7.3 A</td>
      <td>—</td>
      <td>Full-length CD9 + EWI-2 + anti-CD9 Fab</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S GnTI- (BacMam)
- **Construct**: Human wild-type CD9 with N-terminal His6-GFP tag and TEV cleavage site

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
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.0, 150 mM NaCl + 1.5% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.3% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Membrane fractions solubilized for 1 h, insoluble material removed by ultracentrifugation</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> Metal Affinity Resin</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.0, 150 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (wash), 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (elution)</td>
      <td>His6-GFP tag cleaved by <a href="/xray-mp-wiki/reagents/enzymes/tev-protease">TEV</a> protease during dialysis</td>
    </tr>
    <tr>
      <td>Reverse <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> subtractive step</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> Superflow</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.0, 150 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Removes His6-GFP tag and <a href="/xray-mp-wiki/reagents/enzymes/tev-protease">TEV</a> protease</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200</a> Increase 10/300 GL</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.0, 150 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Concentrated to ~15 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified CD9 at ~15 mg/ml mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (2:3 protein:lipid ratio)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Up to 3 weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury (HgCl2) - Aquaporin Inhibitor</a> derivative co-crystallized with 2 mM CH3HgCl for SIRAS phasing. Crystals collected and flash-cooled in liquid nitrogen.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6k4j">6K4J</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSREF</span><span class="topo-inside">MPVKGGTKC</span><span class="topo-membrane">IKYLLFGFNFIFWLAGIAVLAIGLWLRFDSQTK</span><span class="topo-outside">SIFEQETNNNNSSFY</span><span class="topo-membrane">TGVYILIGAGALMMLVGFLGCCGAV</span><span class="topo-inside">QESQ</span><span class="topo-membrane">CMLGLFFGFLLVIFAIEIAAAIWG</span><span class="topo-outside">YSH</span><span class="topo-unknown">KD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220        </span>
<span class="topo-line"><span class="topo-unknown">EVIKEVQEFYKDTYNKLK</span><span class="topo-outside">TKD</span><span class="topo-unknown">EPQRETLKAIHYAL</span><span class="topo-outside">NCCGLAGGVEQFISDICPKKDVLES</span><span class="topo-unknown">CPDAIKEVFDN</span><span class="topo-outside">KFH</span><span class="topo-membrane">IIGAVGIGIAVVMIFGMIFSMILC</span><span class="topo-inside">CAIRRNR</span><span class="topo-unknown">EMV</span></span>
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
      <td>6</td>
      <td>14</td>
      <td>1</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>47</td>
      <td>10</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>62</td>
      <td>43</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>87</td>
      <td>58</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>91</td>
      <td>83</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>115</td>
      <td>87</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>118</td>
      <td>111</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>138</td>
      <td>114</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>139</td>
      <td>141</td>
      <td>134</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>155</td>
      <td>137</td>
      <td>150</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>180</td>
      <td>151</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>191</td>
      <td>181</td>
      <td>191</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>194</td>
      <td>192</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>218</td>
      <td>195</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>225</td>
      <td>219</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6k4j">6K4J</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSREF</span><span class="topo-inside">MPVKGGTKC</span><span class="topo-membrane">IKYLLFGFNFIFWLAGIAVLAIGLWLRFDSQTK</span><span class="topo-outside">SIFEQETNNNNSSFY</span><span class="topo-membrane">TGVYILIGAGALMMLVGFLGCCGAV</span><span class="topo-inside">QESQ</span><span class="topo-membrane">CMLGLFFGFLLVIFAIEIAAAIWG</span><span class="topo-outside">YSH</span><span class="topo-unknown">KD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220        </span>
<span class="topo-line"><span class="topo-unknown">EVIKEVQEFYKDTYNKLK</span><span class="topo-outside">TKD</span><span class="topo-unknown">EPQRETLKAIHYAL</span><span class="topo-outside">NCCGLAGGVEQFISDICPKKDVLES</span><span class="topo-unknown">CPDAIKEVFDN</span><span class="topo-outside">KFH</span><span class="topo-membrane">IIGAVGIGIAVVMIFGMIFSMILC</span><span class="topo-inside">CAIRRNR</span><span class="topo-unknown">EMV</span></span>
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
      <td>6</td>
      <td>14</td>
      <td>1</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>47</td>
      <td>10</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>62</td>
      <td>43</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>87</td>
      <td>58</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>91</td>
      <td>83</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>115</td>
      <td>87</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>118</td>
      <td>111</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>138</td>
      <td>114</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>139</td>
      <td>141</td>
      <td>134</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>155</td>
      <td>137</td>
      <td>150</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>180</td>
      <td>151</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>191</td>
      <td>181</td>
      <td>191</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>194</td>
      <td>192</td>
      <td>194</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>218</td>
      <td>195</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>225</td>
      <td>219</td>
      <td>225</td>
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

### Reversed cone-like molecular shape generates membrane curvature

CD9 adopts a reversed cone-like shape with the four TM helices bundled tightly at the intracellular side and loosely packed at the extracellular side, creating a large central cavity. This asymmetric shape generates membrane curvature in crystalline lipid layers of [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/), explaining CD9 localization in regions of high membrane curvature such as microvilli tips and exosomes.

### TM region and LEL provide multi-platform binding interface

The CD9-EWI-2 complex reveals that CD9 associates with partner proteins through two distinct interfaces: the TM3-4 region interacting with the EWI-2 membrane-spanning helix via small residue (Gly/Ala) contacts, and the large extracellular loop (LEL) which adopts an open conformation to contact the juxta-membrane Ig-like domain of EWI-2. Fertilization assays show that the LEL is critical for sperm-egg fusion, while the TM region is sufficient for EWI-2 association, demonstrating different functional dependencies for different partner proteins.

### Dynamic SEL-LEL gating

MD simulations (100 microsecond reconstructed trajectory) reveal spontaneous transitions between closed, semi-open, and open conformations of the short extracellular loop (SEL) and large extracellular loop (LEL). Unlike [Human CD81 Tetraspanin](/xray-mp-wiki/proteins/structural-adhesion/cd81/), CD9 transitions between conformations even in the absence of [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) binding, suggesting a more dynamic extracellular interface.

### Central cavity accommodates lipid molecules

The central cavity in the intramembranous region is rendered hydrophilic by conserved residues Asn18 and Glu103. An unassigned electron density within the cavity likely corresponds to [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) or endogenous lipid molecules, suggesting regulatory roles of lipids in CD9 function. The [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/)-binding residue Glu219 found in [Human CD81 Tetraspanin](/xray-mp-wiki/proteins/structural-adhesion/cd81/) is replaced by Gly210 in CD9.


## Cross-References

- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) method used for CD9 crystal structure determination
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Used for [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization of CD9
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM (n-Dodecyl-beta-D-Maltopyranoside)</a> — Primary solubilization and purification detergent
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — Used as additive during purification for stability
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Used throughout purification and crystallization
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/elic/">ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/structural-adhesion/cd81/">Human CD81 Tetraspanin</a> — Related protein structure
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a> — Purification method used in protein preparation
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a> — Purification method used in protein preparation
