---
title: "RibU (ECF-Type Riboflavin Transporter S Component from Staphylococcus aureus)"
created: 2026-06-02
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature09488]
verified: true
---

# RibU (ECF-Type Riboflavin Transporter S Component from Staphylococcus aureus)

## Overview

RibU is the S component (substrate-binding protein) of the energy-coupling factor (ECF) type [Riboflavin (Vitamin B2)](/xray-mp-wiki/reagents/cofactors/riboflavin/) transporter from Staphylococcus aureus. ECF transporters are a unique family of membrane transporters responsible for vitamin uptake in prokaryotes. RibU comprises six transmembrane segments, adopts a previously unreported transporter fold, and binds [Riboflavin (Vitamin B2)](/xray-mp-wiki/reagents/cofactors/riboflavin/) on the periplasmic side.

## Publications

### doi/10.1038##nature09488

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3p5n">3P5N</a></td>
      <td>3.6</td>
      <td>P212121</td>
      <td>residues 10-141, 153-188</td>
      <td><a href="/xray-mp-wiki/reagents/cofactors/riboflavin/">Riboflavin (Vitamin B2)</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Induction**: 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at A600 0.8, 14 h at 37 C

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
      <td>French press (2 passes at 15-20,000 psi)</td>
      <td>N/A</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a>, pH 8.0, 100 mM NaCl</td>
      <td>Cell debris removed by centrifugation</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Ultracentrifugation (150,000g, 1 h)</td>
      <td>N/A</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a>, pH 8.0, 100 mM NaCl</td>
      <td>Membrane fraction collected</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>N/A</td>
      <td>2% beta-NG in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a>, pH 8.0, 100 mM NaCl</td>
      <td>2 h at 4 C, followed by ultracentrifugation (150,000g, 30 min)</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA agarose (Qiagen)</td>
      <td>20 mM Tris, pH 8.0, 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.4% beta-NG</td>
      <td>Elution with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (GE Healthcare)</td>
      <td>20 mM Tris, pH 8.0, 100 mM NaCl, 0.4% beta-NG</td>
      <td>Peak fraction concentrated to 8 mg/ml for crystallization</td>
    </tr>
  </tbody>
</table>
**Final sample**: 8 mg/ml in 20 mM Tris, pH 8.0, 100 mM NaCl, 0.4% beta-NG

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>N/A</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3p5n">3P5N</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNGRRKLNM</span><span class="topo-outside">QQNKRLIT</span><span class="topo-membrane">ISMLSAIAFVLTFIKF</span><span class="topo-inside">PIPFLPPYL</span><span class="topo-membrane">TLDFSDVPSLLATF</span><span class="topo-outside">TFGP</span><span class="topo-membrane">VAGIIVALVKNLLNYLFSM</span><span class="topo-inside">GDP</span><span class="topo-membrane">VGPFANFLAGASFLLTAYAIY</span><span class="topo-outside">KNKRSTK</span><span class="topo-membrane">SLITGLIIAT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180         </span>
<span class="topo-line"><span class="topo-membrane">IVMTIVLSILN</span><span class="topo-inside">YFVLLPLYGM</span><span class="topo-unknown">IFNLADIANNL</span><span class="topo-inside">KVIIVSGII</span><span class="topo-membrane">PFNIIKGIVISIVFILLYRR</span><span class="topo-outside">LANFLKR</span><span class="topo-unknown">I</span></span>
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
      <td>9</td>
      <td>1</td>
      <td>9</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>17</td>
      <td>10</td>
      <td>17</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>33</td>
      <td>18</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>42</td>
      <td>34</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>56</td>
      <td>43</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>60</td>
      <td>57</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>79</td>
      <td>61</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>82</td>
      <td>80</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>103</td>
      <td>83</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>110</td>
      <td>104</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>131</td>
      <td>111</td>
      <td>131</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>141</td>
      <td>132</td>
      <td>141</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>152</td>
      <td>142</td>
      <td>152</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>153</td>
      <td>161</td>
      <td>153</td>
      <td>161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>181</td>
      <td>162</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>188</td>
      <td>182</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>189</td>
      <td>189</td>
      <td>189</td>
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

### Riboflavin binding site

[Riboflavin (Vitamin B2)](/xray-mp-wiki/reagents/cofactors/riboflavin/) is bound on the periplasmic side, approximately 5 A into the predicted membrane surface. The ligand is nestled in a hydrophobic pocket formed by 13 conserved amino acids. Multiple hydrogen bonds stabilize [Riboflavin (Vitamin B2)](/xray-mp-wiki/reagents/cofactors/riboflavin/) binding, including interactions from invariant residues around the substrate-binding pocket. Thr 43 and Lys 167, both from conserved positions, are within hydrogen-bonding distance of [Riboflavin (Vitamin B2)](/xray-mp-wiki/reagents/cofactors/riboflavin/). The binding affinity is approximately 0.6 nM, consistent with extensive protein-ligand interactions. Flavin mononucleotide binds with moderate affinity (36 nM), while flavin adenine dinucleotide shows no measurable binding.

### Novel transporter fold

RibU comprises six transmembrane segments with a unique fold not previously reported for any membrane transporter. A DALI search of the Protein Data Bank found no structurally homologous entry. The structure resembles a cylinder with rugged ends, positioned roughly perpendicular to the lipid membrane. The outer surface is predominantly hydrophobic, while cytoplasmic and periplasmic faces are enriched with charged amino acids.

### Conserved residues and transport mechanism

Most highly conserved residues cluster in the interior of the cylinder-shaped RibU molecule, with four invariant amino acids located around the substrate-binding pocket. The L1 loop (17 residues between TM1 and TM2, with 9 highly conserved) hovers above the substrate-binding site and is thought to serve as a gate. Upon [Riboflavin (Vitamin B2)](/xray-mp-wiki/reagents/cofactors/riboflavin/) binding, the L1 loop may close down to interact with the substrate. Facilitated by the T-A-A' components through ATP hydrolysis, the TM1-3 module may move away from TM4-6, allowing the protein to adopt a transient inward-open conformation for substrate release into the cytoplasm.

### Structural similarity to particulate methane monooxygenase

While no full transporter structure is homologous to RibU, transmembrane segments 1-5 of RibU can be superimposed with chain F of particulate methane monooxygenase with an RMSD of 3.3 A over 124 aligned C-alpha atoms, suggesting limited structural similarity.

### ECF transporter conservation

Sequence alignment of RibU with representatives from eight bacterial species shows a high degree of pairwise sequence identity. This, combined with alignment with transporters for folate, thiamine precursor, and [Cobalamin (Vitamin B12)](/xray-mp-wiki/reagents/ligands/cobalamin/) precursor, suggests that S components of at least some ECF transporters contain six transmembrane segments, have a similar structure, and adopt the same membrane topology.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/nonylglucoside/">Nonylglucoside (NG)</a> — Related nonionic glucoside detergent
- <a href="/xray-mp-wiki/reagents/detergents/nonylmaltoside/">Nonylmaltoside</a> — Related nonionic maltoside detergent
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Eluent for Ni-NTA affinity chromatography
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Buffer component throughout purification
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase SEC Resin</a> — Size-exclusion chromatography resin
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Agarose Resin</a> — Affinity chromatography resin
- <a href="/xray-mp-wiki/methods/structure-determination/multi-wavelength-anomalous-diffraction/">Multi-Wavelength Anomalous Diffraction</a> — Phasing method used for structure determination
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Crystallization method used
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
