---
title: "LspA from Staphylococcus aureus (Lipoprotein Signal Peptidase II)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-13724-y, doi/10.1126##science.aad3747]
verified: false
---

# LspA from Staphylococcus aureus (Lipoprotein Signal Peptidase II)

## Overview

LspA (lipoprotein signal peptidase II) is an integral membrane aspartyl protease responsible for processing bacterial lipoproteins by cleaving the signal peptide after diacylglyceryl modification. The enzyme is essential in Gram-negative bacteria and required for full virulence in Gram-positive bacteria, making it an attractive drug target. The first crystal structure of LspA from Pseudomonas aeruginosa (strain PAO1) was solved at 2.8 A resolution in complex with the natural antibiotic [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) using in meso crystallization and Se-Met SAD phasing, identifying LspA as an aspartyl peptidase with catalytic dyad Asp124 and Asp143 (Science 2016). Subsequently, crystal structures of LspA from methicillin-resistant Staphylococcus aureus (MRSA) in complex with [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) and myxovirescin revealed both antibiotics inhibit the enzyme as non-cleavable tetrahedral intermediate analogs, sharing a common 19-atom spine motif (Nature Communications 2019).


## Publications

### doi/10.1038##s41467-019-13724-y

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ryo">6RYO</a></td>
      <td>1.92 A</td>
      <td>P3_2 21</td>
      <td>LspA from S. aureus MRSA (LspMrs) in complex with <a href="/xray-mp-wiki/reagents/ligands/globomycin/">Globomycin</a>, residues approximately 1-163, crystallized using lipidic cubic phase (LCP)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/globomycin/">Globomycin</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ryp">6RYP</a></td>
      <td>2.30 A</td>
      <td>P6_1 22</td>
      <td>LspA from S. aureus MRSA (LspMrs) in complex with myxovirescin A1, residues approximately 1-162, crystallized using lipidic cubic phase (LCP)</td>
      <td>myxovirescin A1</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length LspMrs with N-terminal MGSS-hexahistidine tag, TEV protease cleavage site, expressed in E. coli

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
      <td>Cell lysis and membrane preparation</td>
      <td>Cell disruption and ultracentrifugation</td>
      <td></td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM TCEP</td>
      <td>Cells resuspended and lysed; membranes collected by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM TCEP + n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membranes solubilized with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (IMAC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM TCEP, <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Histidine-tagged LspMrs purified on <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> column</td>
    </tr>
    <tr>
      <td>TEV protease cleavage</td>
      <td>Tag removal by <a href="/xray-mp-wiki/reagents/enzymes/tev-protease">TEV</a> protease</td>
      <td></td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM TCEP + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>N-terminal His-tag cleaved by <a href="/xray-mp-wiki/reagents/enzymes/tev-protease">TEV</a> protease; cleaved protein used for crystallization</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> (SEC)</td>
      <td>Size exclusion column</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM TCEP + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final purification step; protein concentrated to 14-16 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>
**Final sample**: 14-16 mg/ml in 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 1 mM TCEP
**Purity**: High purity by SDS-PAGE

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>LspMrs in buffer D (50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 mM TCEP) at 14-16 mg/mL, with 5-fold molar excess of <a href="/xray-mp-wiki/reagents/ligands/globomycin/">Globomycin</a> or myxovirescin in DMSO</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/globomycin/">Globomycin</a> complex: 15-20 days; Myxovirescin complex: 21 days</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallization was performed using the in meso method. Protein solution mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> in a 2:3 ratio (v/v) to form the <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>. Boluses of protein-laden mesophase (50 nL) were covered with 800 nL precipitant solution. LspMrs-<a href="/xray-mp-wiki/reagents/ligands/globomycin/">Globomycin</a> crystals: bipyramid-shaped, 50x50x50 um, appeared after 4 days. LspMrs-myxovirescin crystals: thin hexagon-shaped, 80 um longest dimension, appeared after 2-3 days. Data collected at SLS beamline X06SA-PXI.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ryo">6RYO</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGHHHHHHDYDIPTTENLYFQGA</span><span class="topo-inside">HMHKKY</span><span class="topo-membrane">FIGTSILIAVFVVIFDQVTK</span><span class="topo-outside">YIIATTMKIGD</span></span>
<span class="topo-line"><span class="topo-outside">SFEVIPHFLNITSHRNNGAAWGILSGK</span><span class="topo-membrane">MTFFFIITIIILIALVYFFIKDA</span><span class="topo-inside">QYNL</span><span class="topo-membrane">FMQVAI</span></span>
<span class="topo-line"><span class="topo-membrane">SLLFAGALGNFIDRVL</span><span class="topo-outside">TGEVVDFIDTNIFGYDFPIF</span><span class="topo-membrane">NIADSSLTIGVILIIIALLK</span><span class="topo-inside">DT</span><span class="topo-unknown">SN</span></span>
<span class="topo-line"><span class="topo-unknown">KKEKEVK</span></span>
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
      <td>23</td>
      <td>-23</td>
      <td>-1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>29</td>
      <td>0</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>49</td>
      <td>6</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>87</td>
      <td>26</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>110</td>
      <td>64</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>114</td>
      <td>87</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>136</td>
      <td>91</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>156</td>
      <td>113</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>176</td>
      <td>133</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>178</td>
      <td>153</td>
      <td>154</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>187</td>
      <td>155</td>
      <td>163</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ryp">6RYP</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGHHHHHHDYDIPTTENLYFQGA</span><span class="topo-inside">HMHKKY</span><span class="topo-membrane">FIGTSILIAVFVVIFDQVT</span><span class="topo-outside">KYIIATTMKIGD</span></span>
<span class="topo-line"><span class="topo-outside">SFEVIPHFLNITSHRNNGAAWGILSGKMT</span><span class="topo-membrane">FFFIITIIILIALVYFFIKDA</span><span class="topo-inside">QYNL</span><span class="topo-membrane">FMQVAI</span></span>
<span class="topo-line"><span class="topo-membrane">SLLFAGALGNFI</span><span class="topo-outside">DRVLTGEVVDFIDTNIFGYDFPIF</span><span class="topo-membrane">NIADSSLTIGVILIIIALLK</span><span class="topo-inside">DTSN</span></span>
<span class="topo-line"><span class="topo-inside">KKEKEVK</span></span>
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
      <td>24</td>
      <td>29</td>
      <td>-1</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>48</td>
      <td>6</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>89</td>
      <td>25</td>
      <td>65</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>110</td>
      <td>66</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>114</td>
      <td>87</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>132</td>
      <td>91</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>156</td>
      <td>109</td>
      <td>132</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>176</td>
      <td>133</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>187</td>
      <td>153</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1126##science.aad3747

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5dir">5DIR</a></td>
      <td>2.8 A</td>
      <td></td>
      <td>LspA from P. aeruginosa PAO1 in complex with <a href="/xray-mp-wiki/reagents/ligands/globomycin/">Globomycin</a>, 169 amino acids</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/globomycin/">Globomycin</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length LspMrs with N-terminal MGSS-hexahistidine tag, TEV protease cleavage site, expressed in E. coli

**Purification:**

- **Expression system**: Escherichia coli (P. aeruginosa PAO1 LspA)

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
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>Provided material of high purity (fig. S2)</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>—</td>
      <td></td>
      <td>Provided material of high purity (fig. S2)</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified LspA-[Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) complex for in meso crystallization
**Purity**: High purity by SDS-PAGE (fig. S2)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>In meso (lipid cubic phase) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>LspA from P. aeruginosa PAO1 in complex with <a href="/xray-mp-wiki/reagents/ligands/globomycin/">Globomycin</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>LspA from P. aeruginosa was crystallized using the in meso (lipid cubic phase) method in the presence of <a href="/xray-mp-wiki/reagents/ligands/globomycin/">Globomycin</a>. The structure of the complex was obtained at 2.8 A resolution by using seleno-methionine, single-wavelength anomalous diffraction (SAD) phasing.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5dir">5DIR</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GSSHHHHHHSSGLVPRGSHM</span><span class="topo-inside">PDVDRFGRL</span><span class="topo-membrane">PWLWITVLVFVLDQVS</span><span class="topo-outside">KAFFQAELSMYQQIV</span></span>
<span class="topo-line"><span class="topo-outside">VIPDLFSWTLAYNTGAAFSFLADSSGWQ</span><span class="topo-membrane">RWLFALIAIVVSASLVVWL</span><span class="topo-inside">KRLKKGETWL</span><span class="topo-membrane">AIA</span></span>
<span class="topo-line"><span class="topo-membrane">LALVLGGALGNLYDRM</span><span class="topo-outside">VLGHVVDFILVHWQNRWYFPAF</span><span class="topo-membrane">NLADSAITVGAVMLAL</span><span class="topo-inside">DMF</span><span class="topo-unknown">RSK</span></span>
<span class="topo-line"><span class="topo-unknown">KSGEAAHG</span></span>
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
      <td>20</td>
      <td>-18</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>29</td>
      <td>2</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>45</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>88</td>
      <td>27</td>
      <td>69</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>107</td>
      <td>70</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>117</td>
      <td>89</td>
      <td>98</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>136</td>
      <td>99</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>158</td>
      <td>118</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>174</td>
      <td>140</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>177</td>
      <td>156</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>188</td>
      <td>159</td>
      <td>169</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Convergent evolution of two natural antibiotics targeting LspA

[Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) (a cyclic depsipeptide) and myxovirescin (a macrolactam) have completely different molecular structures and biosynthetic origins. Yet both inhibit LspA by the same mechanism: they position a hydroxyl group between the catalytic aspartate dyad (Asp118 and Asp136) as non-cleavable tetrahedral intermediate analogs. The two antibiotics superpose along 19 contiguous atoms (the "spine") that interact similarly with LspA, demonstrating a remarkable instance of convergent evolution towards the same molecular target.

### Structural basis for antibiotic binding

[Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) approaches the substrate-binding pocket from one side while myxovirescin approaches from the other, yet both block the catalytic dyad. The 19-atom spine motif recapitulates a part of the natural lipoprotein substrate in its proposed binding mode. All 14 highly conserved residues in LspA are similarly poised in both complex structures. The extracellular loop (EL) between the beta-cradle and H2 exhibits flexibility that is key to effective binding of both antibiotics, enabled by Gly54 as a flexible hinge.

### LspA as a therapeutic target

LspA is essential in Gram-negative bacteria and required for full virulence in Gram-positive bacteria, including MRSA. The lspA mutant showed reduced ability to survive in whole human blood, confirming LspA is important for MRSA survival under physiologically relevant conditions. Both antibiotics interact with highly conserved residues, making resistance development difficult - mutations that weaken antibiotic binding would also compromise LspA function, providing no competitive advantage.

### Mechanism of globomycin and myxovirescin inhibition

Both antibiotics act as non-cleavable tetrahedral intermediate analogs of the aspartyl protease reaction. The beta-hydroxyl of [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/)'s Ser residue and the 6-OH of myxovirescin lodge between the catalytic aspartates (Asp118, Asp136). The blocking hydroxyl oxygens superpose to within 0.8 A in the two complex structures. The 19-atom spine of overlapping atoms provides a natural pharmacophore framework for drug design.

### Substrate specificity and EL flexibility

The extracellular loop (EL, residues Asn53-Lys63) shows remarkable flexibility between the two complex structures. In the [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) complex, the loop includes a half-turn helix with Trp57 reaching over the antibiotic. In the myxovirescin complex, the loop unfolds fully, allowing Trp57 to contact the macrocycle from the opposite side. This EL flexibility likely reflects substrate promiscuity, as LspA must process many different lipoprotein substrates (67 in S. aureus, 175 in P. aeruginosa).

### LspA is an aspartyl peptidase with catalytic dyad Asp124 and Asp143

Mutagenesis studies confirmed LspA is an aspartyl peptidase. The catalytic dyad consists of Asp124 and Asp143, both strictly conserved in 485 organisms. Asp124Asn and Asp143Asn mutants were devoid of activity, while Asp115Ala retained partial activity, confirming Asp115 is functionally important but not catalytic.

### Globomycin inhibits via non-cleavable transition-state mimicry

[Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) acts as a competitive inhibitor of LspA by molecular mimicry. The beta-hydroxyl of g-Ser nests between the two catalytic aspartates (Asp124, Asp143), acting as a non-cleavable tetrahedral intermediate analog. [Globomycin](/xray-mp-wiki/reagents/ligands/globomycin/) also mimics the P-3, P-2, P-1 residues of the lipobox consensus sequence (LAGC). The hydroxyethylamide of g-Ser incorporates elements of a noncleavable transition-state isostere, similar to inhibitors designed for other aspartyl proteases (renin, HIV protease).

### Substrate recognition via shape complementarity

LspA processes 175 different lipoproteins in P. aeruginosa. The structure has grooves and clefts radiating about the active site with remarkable shape complementarity to the trigonal feature of the prolipoprotein substrate (signal peptide, lipoprotein, and [DAG](/xray-mp-wiki/reagents/lipids/dag/) modification converging at the lipobox cysteine). The scissile Gly-Cys* bond is positioned between the catalytic aspartates. This shape complementarity explains how LspA can accommodate diverse lipoprotein substrates while maintaining specificity for the lipobox.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/globomycin/">Globomycin</a> — Natural cyclic depsipeptide antibiotic that inhibits LspA
- <a href="/xray-mp-wiki/reagents/ligands/myxovirescin/">Myxovirescin A1</a> — Natural macrolactam antibiotic that inhibits LspA
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-Maltopyranoside (DDM)</a> — Detergent used for membrane solubilization and purification of LspMrs
- <a href="/xray-mp-wiki/methods/crystallization/lcp/">Lipidic Cubic Phase (LCP) Crystallization</a> — Crystallization method used to obtain LspMrs-antibiotic complex structures
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-proteolysis/">Intramembrane Proteolysis</a> — LspA catalyzes signal peptide cleavage at the membrane interface
- <a href="/xray-mp-wiki/methods/structure-determination/semet-sad-phasing/">SeMet SAD Phasing</a> — Phasing method used for the 2.8 A P. aeruginosa LspA structure
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
