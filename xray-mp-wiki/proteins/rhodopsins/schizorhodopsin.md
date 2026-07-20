---
title: "Schizorhodopsin SzR4 (AM_5_00977)"
created: 2026-06-11
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.2016328118]
verified: agent
---

# Schizorhodopsin SzR4 (AM_5_00977)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

Schizorhodopsins (SzRs) are a family of light-driven inward H+ pumps identified
in Asgard archaea, phylogenetically located at an intermediate position between
type-1 [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/) and heliorhodopsins. SzR4 (AM_5_00977, GenBank
TFG21677.1) is a full-length schizorhodopsin whose structure was determined at
2.1 A resolution by X-ray crystallography using [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) with
[Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) as the search model. The structure reveals that SzRs belong
to the type-1 rhodopsin family, with a seven-transmembrane helix architecture
forming a trimer in the crystal. Key structural features include a single
counterion (D184) to the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base, absence of the strongly
hydrogen-bonded water molecule (water402) characteristic of other H+ pumping
rhodopsins, and uniquely short cytoplasmic ends of TM2, TM6, and TM7 that
position E81 near the cytosol. This close proximity of E81 to the solvent
enables an "untrapped inward H+ release" mechanism: H+ is released from the
[Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base through a water-mediated transport network to the cytosol
without being metastably trapped at E81, unlike other proton pumps.


## Publications

### doi/10.1073##pnas.2016328118

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7e4g">7E4G</a></td>
      <td>2.1</td>
      <td></td>
      <td>Full-length SzR4 (AM_5_00977)</td>
      <td>all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41(Rosetta)
- **Construct**: SzR4 with C-terminal TEV cleavage site followed by GFP-His10 tag in pET21a(+)

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
      <td>Cell growth and membrane preparation</td>
      <td>E. coli C41(Rosetta) transformed with pET21a(+)-SzR4, grown at 25 C for 20 h with 1 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> induction and 10 uM all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> supplementation. Cells disrupted by sonication in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>. Crude membrane fraction collected by ultracentrifugation at 180,000g for 1 h.</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + --</td>
      <td>Cells harvested and disrupted by sonication</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane fraction solubilized for 1 h at 4 C in buffer containing detergent</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Solubilized for 1 h at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Eluate from affinity step treated with <a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease and dialyzed overnight. Cleaved GFP and protease removed with Co2+-NTA resin.</td>
      <td>Co2+-NTA</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> cleavage removed GFP-His10 tag</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Flow-through concentrated and loaded onto Superdex200 10/300 Increase column</td>
      <td>Superdex200 10/300 Increase</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Peak fractions pooled and concentrated to 30 mg/mL</td>
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
      <td>30 mg/mL SzR4 in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (protein:lipid ratio 1:1.5)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested directly from LCP and frozen in liquid nitrogen without added cryoprotectant</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in LCP using Gryphon robot. 30 nL protein-laden mesophase drops overlaid with 800 nL precipitant solution in 96-well glass plates. Data collected at SPring-8 BL32XU with EIGER X 9M detector at 1.0 A wavelength. 148 small-wedge datasets (10 deg/crystal) processed with KAMO, XDS, and XSCALE. Structure determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> with PHASER using BR structure (PDB 1M0K).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7e4g">7E4G</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MEQI</span><span class="topo-membrane">IFYLGIGMFILSTIMFFF</span><span class="topo-outside">LKKKNAKLAS</span><span class="topo-membrane">INIIVSFVTIVSYILML</span><span class="topo-inside">SGLFTLSATSGDTIY</span><span class="topo-membrane">WTRWAFYAVSCSFLMV</span><span class="topo-outside">EISYLLRIDNTTRL</span><span class="topo-membrane">EILVFNSMVMITGLFAS</span><span class="topo-inside">ISEDLY</span><span class="topo-membrane">KWL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210</span>
<span class="topo-line"><span class="topo-membrane">FFIISSVAYLNVLFL</span><span class="topo-outside">IAKNRSEKKAII</span><span class="topo-membrane">LFVAIFWSGFPIVWILS</span><span class="topo-inside">PAGLMVLNAFW</span><span class="topo-membrane">TALFYLVLDFITKIYFGF</span><span class="topo-outside">HTTFKH</span><span class="topo-unknown">IEQLEHHHHHH</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>22</td>
      <td>5</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>32</td>
      <td>23</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>33</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>64</td>
      <td>50</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>80</td>
      <td>65</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>94</td>
      <td>81</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>95</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>117</td>
      <td>112</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>135</td>
      <td>118</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>147</td>
      <td>136</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>164</td>
      <td>148</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>175</td>
      <td>165</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>193</td>
      <td>176</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>194</td>
      <td>199</td>
      <td>194</td>
      <td>199</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7e4g">7E4G</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MEQI</span><span class="topo-membrane">IFYLGIGMFILSTIMFFF</span><span class="topo-outside">LKKKNAKLAS</span><span class="topo-membrane">INIIVSFVTIVSYILML</span><span class="topo-inside">SGLFTLSATSGDTIY</span><span class="topo-membrane">WTRWAFYAVSCSFLMV</span><span class="topo-outside">EISYLLRIDNTTRL</span><span class="topo-membrane">EILVFNSMVMITGLFAS</span><span class="topo-inside">ISEDLY</span><span class="topo-membrane">KWL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210</span>
<span class="topo-line"><span class="topo-membrane">FFIISSVAYLNVLFL</span><span class="topo-outside">IAKNR</span><span class="topo-unknown">SEK</span><span class="topo-outside">KAII</span><span class="topo-membrane">LFVAIFWSGFPIVWILS</span><span class="topo-inside">PAGLMVLNAFW</span><span class="topo-membrane">TALFYLVLDFITKIYFGFH</span><span class="topo-outside">TTFKH</span><span class="topo-unknown">IEQLEHHHHHH</span></span>
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
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>22</td>
      <td>5</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>32</td>
      <td>23</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>33</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>64</td>
      <td>50</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>80</td>
      <td>65</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>94</td>
      <td>81</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>95</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>117</td>
      <td>112</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>135</td>
      <td>118</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>140</td>
      <td>136</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>147</td>
      <td>144</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>164</td>
      <td>148</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>175</td>
      <td>165</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>194</td>
      <td>176</td>
      <td>194</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>199</td>
      <td>195</td>
      <td>199</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7e4g">7E4G</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MEQI</span><span class="topo-membrane">IFYLGIGMFILSTIMFFF</span><span class="topo-outside">LKKKNAKLAS</span><span class="topo-membrane">INIIVSFVTIVSYILML</span><span class="topo-inside">SGLFTLSATSGDTIY</span><span class="topo-membrane">WTRWAFYAVSCSFLMV</span><span class="topo-outside">EISYLLRIDNTTRL</span><span class="topo-membrane">EILVFNSMVMITGLFAS</span><span class="topo-inside">ISEDLY</span><span class="topo-membrane">KWL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210</span>
<span class="topo-line"><span class="topo-membrane">FFIISSVAYLNVLFL</span><span class="topo-outside">IAK</span><span class="topo-unknown">NRSE</span><span class="topo-outside">KKAII</span><span class="topo-membrane">LFVAIFWSGFPIVWILS</span><span class="topo-inside">PAGLMVLNAFW</span><span class="topo-membrane">TALFYLVLDFITKIYFGF</span><span class="topo-outside">HTTF</span><span class="topo-unknown">KHIEQLEHHHHHH</span></span>
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
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>22</td>
      <td>5</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>32</td>
      <td>23</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>49</td>
      <td>33</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>64</td>
      <td>50</td>
      <td>64</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>80</td>
      <td>65</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>94</td>
      <td>81</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>111</td>
      <td>95</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>117</td>
      <td>112</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>135</td>
      <td>118</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>138</td>
      <td>136</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>147</td>
      <td>143</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>164</td>
      <td>148</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>175</td>
      <td>165</td>
      <td>175</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>193</td>
      <td>176</td>
      <td>193</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>194</td>
      <td>197</td>
      <td>194</td>
      <td>197</td>
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

### SzR4 structure establishes schizorhodopsins as type-1 rhodopsins

The SzR4 structure superimposes well on [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (BR, RMSD 1.27 A for
C-alpha atoms) rather than heliorhodopsin (TaHeR, RMSD 1.96 A). SzR4 and BR
similarly form trimers in the crystal, with TM1 and TM2 of one monomer creating
a binding interface with TM4' and TM5' of the adjacent monomer, in contrast to
heliorhodopsins which form dimers. The membrane orientation is the same as type-1
rhodopsins (N terminus extracellular, C terminus cytoplasmic), opposite to HeRs.
This classifies SzRs within the type-1 rhodopsin family despite their intermediate
phylogenetic position.

### Single counterion D184 and absence of strongly hydrogen-bonded water

Unlike BR which has a double counterion system (D85, D212) bridged by a strongly
hydrogen-bonded water molecule (water402), SzR4 employs D184 as a single counterion
forming a direct salt bridge with the [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) Schiff base (RSB). No electron
density corresponds to water402. Three water molecules exist in the space opened
by F70 side-chain flipping, but the RSB complex does not form hydrogen bonds with
them. This absence of the strongly hydrogen-bonded water molecule is a unique
structural feature of SzR4 among H+ pumping rhodopsins and may be associated
with its inward pumping function.

### Short cytoplasmic helices position E81 near the cytosol

The cytoplasmic parts of TM2, TM6, and TM7 in SzR4 are shorter than in other
[Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/). TM6 of SzR4 has only 13 residues between the conserved
Pro and the cytoplasmic end, compared to ~21 residues in other type-1 rhodopsins,
making it the shortest among [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/). This places E81 (the putative
H+ acceptor, homologous to BR D96) very close to the cytoplasmic surface,
separated from the solvent by only two leucine residues (L30, L85). This
structural feature enables the "untrapped inward H+ release" mechanism.

### Color-tuning mechanism via residues around the beta-ionone ring

SzR4 shows lambda_max at 557 nm, identical to SzR1. SzR2 and SzR3 show
blue-shifted absorptions at 542 and 540 nm, respectively. Residues N100 and
V103 around the beta-ionone ring were identified as primary determinants of
color tuning. The N100M mutation (SzR4 to SzR2 type) and N100T mutation (SzR4
to SzR3 type) each produced 11 nm blue shifts. In BR, the homologous position
(D115) also affects absorption wavelength, suggesting a conserved color-tuning
mechanism at this position across rhodopsins.

### L78 hydrophobic gate regulates solvent access to E81

L78 in SzR4 (homologous to L93 in BR) forms a hydrophobic barrier between the
RSB and E81. The L78A mutant completely abolished H+ transport activity. The
RSB in SzR4 L78A was accessible to hydroxylamine even in the dark, indicating
that L78 normally gates solvent access to the cytoplasmic side. Light-induced
rotation of L78 likely opens a water-mediated transport network from the RSB to
the cytosol, enabling H+ release attracted by the negative charge of E81.

### Untrapped inward H+ release mechanism

SzR4 employs a unique "untrapped inward H+ release" mechanism distinct from
other proton pumps. During the M-intermediate rise, light-induced structural
changes (including TM3 movement) disrupt the hydrogen-bonding network around
E81 and the two hydrophobic barriers above and below it. A water-mediated
transport network forms between the RSB and the cytosol. The RSB deprotonates,
and the H+ is released to the solvent through this network, attracted by the
negative charge of E81. Unlike BR where H+ is metastably trapped at D96, the
H+ in SzR is not trapped at E81 because the rate of H+ release to the bulk
is faster than H+ transfer from RSB to E81. This model explains the different
kinetic behaviors of SzR compared to xenorhodopsins and [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/).


## Cross-References

- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/">Microbial Rhodopsins</a> — SzR is a newly identified family of microbial rhodopsins from Asgard archaea
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/evolution-of-rhodopsins/">Evolution of Rhodopsins</a> — SzRs are phylogenetically intermediate between type-1 rhodopsins and heliorhodopsins
- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — SzR4 structure was solved by molecular replacement using BR model and shows structural similarity to BR
- <a href="/xray-mp-wiki/proteins/rhodopsins/bcxer/">BcXeR (Xenorhodopsin from Bacillus coahuilensis)</a> — SzR and XeR both function as inward H+ pumps but with different mechanisms
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/proton-wire/">Proton Wire</a> — SzR uses a water-mediated transport network (proton wire) for inward H+ release
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — SzR4 was crystallized using LCP with monoolein
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Monoolein was the lipid used for LCP crystallization
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> — All-trans retinal is covalently bound to K188 via Schiff base
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/retinal-chromophore-conformation/">Retinal Chromophore Conformation</a> — All-trans to 13-cis isomerization drives the photocycle
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/">Rhodopsin Photocycle</a> — SzR exhibits a photocycle with M-intermediate formation
