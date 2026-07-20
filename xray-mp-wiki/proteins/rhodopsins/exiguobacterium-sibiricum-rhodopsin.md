---
title: "Exiguobacterium sibiricum Rhodopsin (ESR)"
created: 2026-06-21
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1221629110]
verified: pdb
uniprot_id: Q81BL7
---

# Exiguobacterium sibiricum Rhodopsin (ESR)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q81BL7">UniProt: Q81BL7</a>

<span class="expr-badge">Bacillus cereus</span>

## Overview

Exiguobacterium sibiricum rhodopsin (ESR) is a light-driven proton pump
from the permafrost bacterium Exiguobacterium sibiricum. ESR belongs to
the proteorhodopsin family and exhibits three unique features compared to
[Bacteriorhodopsin (bR) from Halobacterium salinarum](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) and [Xanthorhodopsin](/xray-mp-wiki/proteins/rhodopsins/xanthorhodopsin/): (i) the proton donor is a lysine
residue (Lys-96) situated close to the bulk solvent, (ii) the alpha-helical
structure in the middle of helix F is replaced by 3_10- and pi-helix-like
elements stabilized by Trp-154 and Asn-224, and (iii) the proton release
region is connected to the bulk solvent by a chain of water molecules
already in the ground state. The 2.3 A crystal structure (PDB 4RYJ) reveals
a conserved Schiff base environment despite these unusual features. ESR
represents the first high-resolution structure of a proteorhodopsin.


## Publications

### doi/10.1073##pnas.1221629110

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ryj">4RYJ</a></td>
      <td>2.3</td>
      <td>P321</td>
      <td>Full-length ESR with C-terminal hexahistidine tag; residues Met1 to Ala...</td>
      <td>All-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> (chromophore)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli Rosetta2(DE3)pLysS
- **Construct**: Full-length ESR with C-terminal hexahistidine tag
- **Notes**: Fermenter for 3 days at 30 C in 2x ZYM5052 autoinduction medium with 100 ug/mL [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) and 34 ug/mL [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/)

**Purification:**

- **Expression system**: E. coli Rosetta2(DE3)pLysS
- **Expression construct**: Full-length ESR with C-terminal hexahistidine tag
- **Tag info**: C-terminal hexahistidine tag

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
      <td>Membrane fraction isolation</td>
      <td>Centrifugation</td>
      <td>—</td>
      <td></td>
      <td>Obtained membrane fraction after cell lysis</td>
    </tr>
    <tr>
      <td>Extraction</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM Tris, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, pH 8.0 + 1% n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Overnight at 4 C</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-Sepharose 6 Fast Flow (GE Healthcare)</td>
      <td>Buffer 1: 50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a>, 500 mM NaCl, 2 M <a href="/xray-mp-wiki/reagents/substrates/urea/">UREA</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, pH 8.0; Buffer 2: 50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a>, 200 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, pH 8.0</td>
      <td>Wash with buffer 1 and buffer 2; eluted with 50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a>, 200 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% Na azide, 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, pH 7.4</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> removal and concentration</td>
      <td>Ultrafiltration</td>
      <td>Amicon regenerated cellulose membrane, 10 kDa MWCO</td>
      <td></td>
      <td>Final concentration up to 2 mg/mL</td>
    </tr>
  </tbody>
</table>
**Final sample**: ESR at up to 2 mg/mL in 50 mM [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/), 200 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 0.01% Na azide, pH 7.4

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (in meso) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified ESR at 35 mg/mL in crystallization buffer</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (Nu-Chek Prep)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>Not specified</td>
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
      <td>Notes</td>
      <td>Crystals grown using the in meso approach. Best crystals obtained at protein concentration of 35 mg/mL.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ryj">4RYJ</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKHHHHHHHHHHENLYFQSYVMF</span><span class="topo-outside">MKKSSIIV</span><span class="topo-membrane">FFLTYGLFYVSSVLFPI</span><span class="topo-inside">DRTWYDALEKPSWTP</span><span class="topo-membrane">PGMTIGMIWAVLFGLIALSVA</span><span class="topo-outside">IIYNNYGFKPK</span><span class="topo-membrane">TFWFLFLLNYIFNQAFSY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180 </span>
<span class="topo-line"><span class="topo-membrane">FQFS</span><span class="topo-inside">QKNLFL</span><span class="topo-membrane">ATVDCLLVAITTLLLIMFSS</span><span class="topo-outside">NLSK</span><span class="topo-membrane">VSAWLLIPYFLWSAFATYLS</span><span class="topo-inside">WTIYSIN</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>31</td>
      <td>38</td>
      <td>3</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>55</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>70</td>
      <td>28</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>91</td>
      <td>43</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>102</td>
      <td>64</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>124</td>
      <td>75</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>130</td>
      <td>97</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>150</td>
      <td>103</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>154</td>
      <td>123</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>174</td>
      <td>127</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>181</td>
      <td>147</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ryj">4RYJ</a> — Chain B (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKHHHHHHHHHHENLYFQSYVMF</span><span class="topo-outside">MKKSSII</span><span class="topo-membrane">VFFLTYGLFYVSSVLFPI</span><span class="topo-inside">D</span><span class="topo-unknown">RTWYDA</span><span class="topo-inside">LEKPSWTP</span><span class="topo-membrane">PGMTIGMIWAVLFGLIALSVA</span><span class="topo-outside">IIYNNYGFKPK</span><span class="topo-membrane">TFWFLFLLNYIFNQAFSY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180 </span>
<span class="topo-line"><span class="topo-membrane">FQFS</span><span class="topo-inside">QKNLFL</span><span class="topo-membrane">ATVDCLLVAITTLLLIMFSS</span><span class="topo-outside">NLSK</span><span class="topo-membrane">VSAWLLIPYFLWSAFATYLS</span><span class="topo-inside">WTIYSIN</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>31</td>
      <td>37</td>
      <td>3</td>
      <td>9</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>55</td>
      <td>10</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>56</td>
      <td>56</td>
      <td>28</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>62</td>
      <td>29</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>63</td>
      <td>70</td>
      <td>35</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>91</td>
      <td>43</td>
      <td>63</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>102</td>
      <td>64</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>124</td>
      <td>75</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>130</td>
      <td>97</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>131</td>
      <td>150</td>
      <td>103</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>154</td>
      <td>123</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>174</td>
      <td>127</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>181</td>
      <td>147</td>
      <td>153</td>
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

### Lysine as proton donor in proteorhodopsins

ESR's proton donor is Lys-96, a lysine side chain situated very close to
the bulk solvent. This contrasts with BR (Asp-96) and XR (Glu-107),
where the proton donor is a carboxylic acid far from the bulk. Lys-96
is immersed in a mostly hydrophobic cavity and may have a pKa as low
as 5.3, allowing it to function as a proton donor. The cavity is
separated from the bulk solvent only by Thr-43, providing easy direct
access of protons from the cytoplasm.

### Helix F structural disruption in proteorhodopsins

The alpha-helical structure in the middle of helix F is replaced by
3_10- and pi-helix-like elements stabilized by Trp-154 and Asn-224 side
chains. This feature is characteristic of the proteorhodopsin family of
proteins and distinguishes them from other [Microbial Rhodopsins](/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/). The
structural disruption is unique to ESR among known retinylidene protein
structures.

### Proton release region with continuous water chain

The proton release region is connected to the bulk solvent by a chain
of water molecules already in the ground state. In ESR, the histidine
residue (His-57) of the putative proton release group (Asp-221/His-57)
is immersed in a cavity of sufficient size for a water molecule from
the bulk to contact it. This continuous cavity contains ordered water
molecules and transitions into the bulk.

### Broad pH range proton pumping

ESR functions across a broad pH range (4.5-8.5). The Asp-85/His-57 pair
allows stabilization of Asp-85 in the unprotonated state across this
wide pH range. Lys-96 with its reduced pKa may serve as a key element
of stabilization of proton pumping under varying environmental
conditions, consistent with E. sibiricum's permafrost habitat
characterized by pH 5.6-7.8.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin (bR) from Halobacterium salinarum</a> — Archetypal light-driven proton pump; ESR shares the seven-helix retinylidene protein fold but with unique structural features
- <a href="/xray-mp-wiki/proteins/rhodopsins/xanthorhodopsin/">Xanthorhodopsin</a> — Eubacterial proton pump with dual chromophore; comparison of proton uptake regions reveals ESR's unique lysine proton donor
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/">Microbial Rhodopsins</a> — ESR is the first high-resolution proteorhodopsin structure within the microbial rhodopsin family
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/proton-pump-mechanism/">Proton Pump Mechanism</a> — ESR reveals unusual proton pumping features including lysine as proton donor and continuous water chain to bulk solvent
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-Maltopyranoside (DDM)</a> — Detergent used for solubilization and purification of ESR
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/sodium-malonate/">Sodium Malonate</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> — Antibiotic used in selection
