---
title: "HiGlpG (Haemophilus influenzae Rhomboid Protease)"
created: 2026-05-26
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0609981104, doi/10.1016##j.jmb.2011.01.046]
verified: false
---

# HiGlpG (Haemophilus influenzae Rhomboid Protease)

## Overview

HiGlpG is the rhomboid intramembrane protease from Haemophilus influenzae, a member of the serine protease family that cleaves transmembrane substrates within the lipid bilayer. The original 2.2-A resolution crystal structure (Lemieux et al., 2007) revealed the catalytic architecture of hiGlpG, including the nucleophilic Ser-116, general base His-169, and a distinctive oxyanion hole comprising His-65 and the main-chain NH of Ser-116. The structure identified three lipids (phosphatidic acid) bound to the protein and highlighted the roles of the L1, L3, and L5 loops in substrate gating. A later high-resolution study (PDB 3ODJ, 2.85 A) revealed persistent disorder in loop 4, helix 5, and loop 5, which together form the substrate gate. Mutagenesis combined with functional assays demonstrates that flexibility in helix 5 and loop 5 is essential for substrate access to the buried active site, while loop 4 requires structural rigidity. The studies also predict that rhomboid cleavage occurs on the si-face of the scissile peptide bond.

## Publications

### doi/10.1073##pnas.0609981104

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2nr9">2NR9</a></td>
      <td>2.2 A</td>
      <td>C2 / P2(1)2(1)2(1)</td>
      <td>Full-length hiGlpG from Haemophilus influenzae (residues 1-276)</td>
      <td>Three phosphatidic acid (PA) molecules; two C12E8 detergent molecules</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli Top10 cells (Invitrogen) transformed with pBAD-Myc-HisA expression vector
- **Construct**: HiGlpG with N-terminal Myc epitope tag and His6 tag. Grown in LB media supplemented with [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/), induced with 0.002% arabinose at 24 C for 5 h.

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
      <td>Cell culture and induction</td>
      <td>Expression</td>
      <td>—</td>
      <td>LB medium supplemented with <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> + —</td>
      <td>Cells grown to OD600 0.4, induced with 0.0002% arabinose at 24 C for 16 h</td>
    </tr>
    <tr>
      <td>Membrane fraction isolation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>TBS supplemented with EDTA-free peptidase-inhibitor mixture, 1 mM PMSF, 0.1 mg/ml DNase + —</td>
      <td>Cells lysed by EmulsiFlex-C3 homogenizer; membranes pelleted at 100,000 x g in 45Ti rotor</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM Tris, 300 mM NaCl, 30 mM imidazole, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1% DDM</td>
      <td>Membrane fractions homogenized, stirred 30 min, then ultracentrifuged at 110,000 x g</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA resin (Qiagen)</td>
      <td>50 mM Tris, 300 mM NaCl, 30 mM imidazole, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>; elution with 250-1000 mM imidazole step gradient + 0.1% DDM</td>
      <td>Protein eluted in stepwise manner with 3 x 2 CV of 250, 500, and 1000 mM imidazole</td>
    </tr>
    <tr>
      <td>Detergent exchange and gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex200 (16/60) column (Amersham)</td>
      <td>50 mM Tris (pH 8.0), 20 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.05% C12E8</td>
      <td>Protein concentrated by 30K centrifugal filter and subjected to detergent exchange on Superdex200 column</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, hanging drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>HiGlpG at 5 mg/ml in 50 mM Tris (pH 8.0), 0.05% C12E8, 20 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>25% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000, 0.1 M citrate (pH 6.0), 1 M NaCl, 3% ethanol, 15% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified (room temperature)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1-2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals directly flash-cooled in liquid nitrogen (reservoir already contained 15% glycerol)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew to 100 x 50 x 20 micrometers. Two space groups obtained: monoclinic C2 and orthorhombic P2(1)2(1)2(1). Monoclinic data diffracted to higher resolution (2.2 A) with one molecule in the AU. Molecular replacement with MolRep using ecGlpG coordinates (2IC8.pdb). Refinement with Refmac5. Data collected at ALS beamline 8.3.1.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2nr9">2NR9</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MEN</span><span class="topo-outside">FLAQQGK</span><span class="topo-membrane">ITLILTALCVLIYI</span><span class="topo-inside">AQQLGF</span><span class="topo-unknown">EDDIMYLM</span><span class="topo-inside">HYPAYEEQDSEV</span><span class="topo-unknown">WRYISHTLVH</span></span>
<span class="topo-line"><span class="topo-inside">LSN</span><span class="topo-membrane">LHILFNLSWFFIFGG</span><span class="topo-outside">MIERTFGSV</span><span class="topo-membrane">KLLMLYVVASAITGYVQ</span><span class="topo-inside">NYVSGPAFFG</span><span class="topo-membrane">LSGVVY</span></span>
<span class="topo-line"><span class="topo-membrane">AVLGY</span><span class="topo-outside">VFIRDKLNHHLFDLPEGF</span><span class="topo-membrane">FTMLLVGIALGFIS</span><span class="topo-inside">PLFGVEMGN</span><span class="topo-membrane">AAHISGLIVGLIW</span><span class="topo-outside">G</span></span>
<span class="topo-line"><span class="topo-outside">FIDSKLRKNSLELVP</span><span class="topo-unknown">R</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>10</td>
      <td>4</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>11</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>30</td>
      <td>25</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>38</td>
      <td>31</td>
      <td>38</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>50</td>
      <td>39</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>60</td>
      <td>51</td>
      <td>60</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>61</td>
      <td>63</td>
      <td>61</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>78</td>
      <td>64</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>87</td>
      <td>79</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>104</td>
      <td>88</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>114</td>
      <td>105</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>125</td>
      <td>115</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>126</td>
      <td>143</td>
      <td>126</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>157</td>
      <td>144</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>166</td>
      <td>158</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>179</td>
      <td>167</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>195</td>
      <td>180</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>196</td>
      <td>196</td>
      <td>196</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1016##j.jmb.2011.01.046

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3odj">3ODJ</a></td>
      <td>2.85 A</td>
      <td>C2</td>
      <td>HiGlpG from H. influenzae (residues 1-133 and 165-164, with residues 134-164 disordered and not modeled; loop 4, helix 5, and loop 5 lack electron density)</td>
      <td>None (no inhibitor or ligand bound; detergent molecules present from purification)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli Top10 cells (Invitrogen) transformed with pBAD-Myc-HisA expression vector
- **Construct**: HiGlpG with N-terminal Myc epitope tag and His6 tag. Grown in LB media supplemented with [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/), induced with 0.002% arabinose at 24 C for 5 h.

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
      <td>Cell culture and induction</td>
      <td>Expression</td>
      <td>--</td>
      <td>LB media supplemented with <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> + --</td>
      <td>Cells grown at 24 C and induced with 0.002% arabinose for 5 h</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Ultracentrifugation</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Crude membrane fraction isolated by high-speed ultracentrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>-- + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membranes solubilized in buffer containing 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (Anatrace, USA)</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA resin</td>
      <td>Buffer containing <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> for elution + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>His-tag affinity purification of HiGlpG</td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td>Protease digestion</td>
      <td>--</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Thrombin cleavage at 30 U/mg <a href="/xray-mp-wiki/proteins/enzymes/glpg/">GLPG</a> for 1 h at room temperature to remove N-terminal Myc-His tag</td>
    </tr>
    <tr>
      <td>Concentration and dialysis</td>
      <td>Ultrafiltration and dialysis</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Protein dialyzed to remove <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> and concentrated using Millipore Amicon ultracentrifugal concentrators (30,000 MWCO) to 10-15 mg/ml</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column</td>
      <td>50 mM Tris, 200 mM NaCl, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> (pH 8.0) + 0.005% AnaPOE <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a></td>
      <td>Final purification and detergent exchange. Buffer contained 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>. Gel filtration carried out using <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column with detergent exchange (Anatrace).</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (hanging drop or sitting drop, as previously described)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>HiGlpG at 10-15 mg/ml in 50 mM Tris, 200 mM NaCl, 0.005% AnaPOE <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a>, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> (pH 8.0)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in this paper (prepared as previously described in reference 24)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted to 2.85 A resolution, space group C2. Disorder in residues 134-164 (loop 4, helix 5, loop 5) was observed across 6 different data sets collected around 2.8 A. Approximately 150 crystals were searched for covalent inhibitors and heavy-atom derivatives. X-ray diffraction data collected on beamline 8.3.1 at the Advanced Light Source (ALS), Lawrence Berkeley Laboratory.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3odj">3ODJ</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MENFLAQ</span><span class="topo-inside">QG</span><span class="topo-membrane">KITLILTALCVLIYIAQQL</span><span class="topo-outside">GF</span><span class="topo-unknown">EDDIMYLM</span><span class="topo-outside">HYPAYEEQDSEVW</span><span class="topo-unknown">RYISHTL</span><span class="topo-outside">VH</span></span>
<span class="topo-line"><span class="topo-outside">L</span><span class="topo-membrane">SNLHILFNLSWFFIFGG</span><span class="topo-inside">MIERTFGS</span><span class="topo-membrane">VKLLMLYVVASAITGYVQNY</span><span class="topo-outside">VSGPAF</span><span class="topo-membrane">FGLSGVVY</span></span>
<span class="topo-line"><span class="topo-membrane">AVLGYVFI</span><span class="topo-inside">RDKLNH</span><span class="topo-unknown">HLFDLPEGFFTMLLVGIALGFISPLFGVEMG</span><span class="topo-outside">N</span><span class="topo-membrane">AAHISGLIVGLIWG</span></span>
<span class="topo-line"><span class="topo-membrane">FI</span><span class="topo-inside">DSKLRKNSLELVP</span><span class="topo-unknown">R</span></span>
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
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td>8</td>
      <td>9</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>28</td>
      <td>10</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>30</td>
      <td>29</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>38</td>
      <td>31</td>
      <td>38</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>39</td>
      <td>51</td>
      <td>39</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>58</td>
      <td>52</td>
      <td>58</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>59</td>
      <td>61</td>
      <td>59</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>78</td>
      <td>62</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>106</td>
      <td>87</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>112</td>
      <td>107</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>128</td>
      <td>113</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>129</td>
      <td>134</td>
      <td>129</td>
      <td>134</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>165</td>
      <td>135</td>
      <td>165</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>166</td>
      <td>166</td>
      <td>166</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>182</td>
      <td>167</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>195</td>
      <td>183</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>196</td>
      <td>196</td>
      <td>196</td>
      <td>196</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Catalytic dyad and oxyanion hole in hiGlpG

The 2.2-A crystal structure of hiGlpG revealed the complete active-site architecture of a rhomboid intramembrane protease. The catalytic dyad consists of Ser-116 (nucleophile) and His-169 (general base), with a hydrogen bond already established between Ser116O-gamma and His169N-epsilon2 in the native unbound form. Unlike classical serine proteases, rhomboid lacks an aspartate equivalent for the third member of the catalytic triad. Instead, Tyr-120 packs against the imidazole ring of His-169 to stabilize the general base. The oxyanion hole is formed by the main-chain NH of Ser-116 and the protonated N-epsilon2 of His-65. A distinctive water molecule (W40) occupies the oxyanion hole in the resting state, bridging Ser116NH and His65N-epsilon2 and forming H-bonds to Phe113O and Val162O. This water would be displaced by the carbonyl oxygen of the P1 residue upon substrate binding. Additional stabilization of the tetrahedral intermediate comes from the helix dipole of helix H4 (Ser-116 is at the N-terminus of H4), analogous to the peptide dipole stabilization in subtilisin.

### Substrate gating by the L1, L3, and L5 loops

In the resting state, the active site of hiGlpG is buried and inaccessible to solvent. Three loops - L1 (Gly-29 to Ser-55), L3 (Gly-109 to Gly-114), and L5 (Gly-161 to Gly-165) - must move substantially to allow substrate access. These loops exhibit elevated B-factors (60-70 A^2 for L1, 50 A^2 for L3, 60 A^2 for L5) compared to the overall B-factor of 35.5 A^2, supporting their conformational flexibility. The loops are demarcated by glycine residues that confer conformational flexibility. A hypothetical sequence of events includes: (1) the destabilized transmembrane helix of the substrate docks to rhomboid, displacing the L1 gate; (2) L3 and L5 loops are displaced; (3) the substrate enters the active site. A model of the Drosophila spitz substrate (Ala-Ser-Gly-Ala) docked into the active site showed the P1 carbonyl positioned ideally for nucleophilic attack by Ser-116, with small side chains (Ala, Gly) accommodated in the active site.

### Bound lipids and membrane-mimetic environment

Three phosphatidic acid (PA) molecules were observed bound to hiGlpG in the crystal structure. Two PA molecules flank the L1 loop, and one is located near helix H6. The lipids may play a structural role, acting as chaperones, or may play a role in rhomboid function. Two additional C12E8 detergent molecules were also visible. The bound lipids may alternatively be cardiolipin (CL), phosphatidylserine (PS), or phosphatidylethanolamine (PE), the main lipids found in the E. coli lipid bilayer.

### Substrate gating by loop 4, helix 5, and loop 5 flexibility

The new hiGlpG crystal structure (3ODJ) reveals persistent disorder in loop 4 (residues 134-137), helix 5 (residues 138-144), and loop 5 (residues 145-164) across multiple crystal forms, confirming that these regions are conformationally mobile. Mutagenesis of loop 5 residues F160A and M164A retained 46-60% of wild-type peptidase activity, indicating that loop 5 flexibility is tolerated. Mutations in helix 5 F144A reduced activity by 40%. In contrast, loop 4 mutations L136A, F137A, and F84A dramatically reduced activity to 5-22%, suggesting loop 4 requires structural rigidity. Disrupting hydrophobic interactions between helix 2 and helix 5 (triple mutants W72A/F76A/F144A and W72V/F76V/F144V) actually increased substrate cleavage 2.5- and 2-fold, respectively, indicating the gate opens more readily when these contacts are weakened.

### si-face cleavage mechanism in rhomboid proteases

The structural evidence for substrate gating via helix 5 movements, combined with the active-site geometry, predicts that rhomboid cleavage occurs on the si-face of the scissile peptide bond (rather than the re-face typical of soluble serine proteases such as [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/)). The oxyanion hole is composed of the main-chain NH from Ser116 and the protonated N-epsilon from His65. This si-face attack mechanism is shared with other serine peptidases having a Ser-Lys catalytic dyad, including signal peptidase (SPase), Lon protease, LexA peptidase, and VP4 protease. A cocrystal of SPase with a beta-lactam inhibitor confirmed this stereochemistry.

### Comparison with ecGlpG gating reveals conserved rhomboid dynamics

HiGlpG differs from the E. coli rhomboid [GLPG](/xray-mp-wiki/proteins/enzymes/glpg/) (ecGlpG) in the intramolecular connections between helix 5 and helix 2: in hiGlpG, helix 5 is partially unwound and tilted away from the helical bundle, while in ecGlpG, helix 5 runs parallel to helix 2. Despite these structural differences, both rhomboids show comparable gating mechanisms with subtle variations. The disorder in loop 4, helix 5, and loop 5 observed in hiGlpG is a common feature of the rhomboid family, indicating conserved substrate access dynamics. Both gating hypotheses (loop 5 cap movement and helix 5 lateral movement) may apply, with substrate recognition possibly involving an exosite on the enzyme surface in the lipid bilayer.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/rhomboid-protease/">Rhomboid Protease Family</a> — HiGlpG is a member of the rhomboid intramembrane protease family
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-proteolysis/">Intramembrane Proteolysis</a> — HiGlpG cleaves transmembrane substrates within the lipid bilayer
- <a href="/xray-mp-wiki/proteins/enzymes/glpg/">GlpG (E. coli Rhomboid Protease)</a> — Homologous rhomboid protease from E. coli with comparable gating mechanism
- <a href="/xray-mp-wiki/proteins/enzymes/ecglpg-cyto/">Cytoplasmic Domain of E. coli Rhomboid Protease GlpG (EcGlpG-Cyto)</a> — Related structural entity representing the soluble cytoplasmic domain of the GlpG homolog
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM (N-Dodecyl-beta-D-maltoside)</a> — Primary solubilization detergent (1%) for HiGlpG membrane extraction
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Used at 20% in the final purification buffer for HiGlpG stability
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> — Primary buffer component (50 mM, pH 8.0) for purification and crystallization
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Agarose Resin</a> — Used for His-tag affinity purification of HiGlpG
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Superdex 200 gel filtration used for final purification and detergent exchange
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
