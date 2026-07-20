---
title: "Fucoxanthin Chlorophyll a/c-Binding Protein (FCP) from Phaeodactylum tricornutum"
created: 2026-06-10
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aav0365]
verified: pdb
uniprot_id: B7FRW2
---

# Fucoxanthin Chlorophyll a/c-Binding Protein (FCP) from Phaeodactylum tricornutum

<div class="expr-badges"><span class="expr-badge expr-native-tissue">Native tissue</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/B7FRW2">UniProt: B7FRW2</a>

<span class="expr-badge">Phaeodactylum tricornutum CCAP 1055/1</span>

## Overview

 chlorophyll a/c-binding protein (FCP) is a light-harvesting antenna protein from the marine diatom *Phaeodactylum tricornutum*. FCPs belong to the superfamily of transmembrane light-harvesting complex (LHC) proteins and contain the pigments Chl a, Chl c, and  (Fx), enabling them to absorb light in the blue-green region that penetrates underwater. The structure of Lhcf4 was solved as a homodimer at 1.8-Å resolution, revealing a unique pigment arrangement with nine Chls (seven Chl a, two Chl c), seven Fxs, and one diadinoxanthin (Ddx) per monomer. Unlike the trimeric LHCII of green plants, FCP forms a dimer stabilized by interactions between transmembrane C helices. FCPs display robust [Non-photochemical Quenching (NPQ) in LHC-II](/xray-mp-wiki/concepts/miscellaneous/non-photochemical-quenching/) (NPQ) via the Ddx-Dtx xanthophyll cycle, providing photoprotection under fluctuating light conditions in the ocean surface layer.


## Publications

### doi/10.1126##science.aav0365

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6a2w">6A2W</a></td>
      <td>1.8</td>
      <td>TBD</td>
      <td>Lhcf4 (residues 1-166 of 167 total); native FCP dimer from Phaeodactylum tricornutum</td>
      <td>Chl a (x7), Chl c (x2), Fx (x7), Ddx (x1), phosphatidyl- (x1),  (x1), <a href="/xray-mp-wiki/reagents/detergents/og/">OTG</a>, a-, Ca2+ (x2)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Native Phaeodactylum tricornutum cells
- **Construct**: Native Lhcf4 (product of lhcf3/lhcf4 genes, 167 residues)

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
      <td>Cell culture and harvest</td>
      <td>Glass bead disruption</td>
      <td>—</td>
      <td>20 mM tricine, 10 mM , 20 mM KCl, 5% , pH 7.8 (TMKS buffer)</td>
      <td></td>
    </tr>
    <tr>
      <td>Thylakoid membrane isolation</td>
      <td>Centrifugation</td>
      <td>—</td>
      <td>TMKS buffer</td>
      <td>100,000 x g for 20 min at 4 C</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>1% (w/v) n-dodecyl-alpha-D-maltopyranoside (alpha-)</td>
      <td>0.5 mg Chl a/ml for 30 min on ice</td>
    </tr>
    <tr>
      <td>Anion exchange chromatography (1st column)</td>
      <td><a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a></td>
      <td>Q-Sepharose HP</td>
      <td>TMKS buffer with 0.03% alpha-</td>
      <td>Wash with 0.25 M NaCl; elute with 0.25-0.42 M NaCl gradient; Lhcf4 elutes at 0.35-0.38 M NaCl</td>
    </tr>
    <tr>
      <td>Anion exchange chromatography (2nd column)</td>
      <td><a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a></td>
      <td>Q-Sepharose HP</td>
      <td>TMKS buffer with 0.03% alpha-</td>
      <td>Same conditions as first column to increase purity</td>
    </tr>
    <tr>
      <td> gradient centrifugation</td>
      <td>Density gradient centrifugation</td>
      <td>—</td>
      <td>TMK buffer with 0.03% alpha-</td>
      <td>5-20% linear  gradient, 303,800 x g for 16 h</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified FCP dimer in TMK buffer with 0.03% alpha-</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted to 1.8 A resolution. Phasing by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using PHASER with an LHCII search model, followed by extension to 1.8 A.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6a2w">6A2W</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">AFEDELGAQPPLGFFDPLGLVADGDQEKFDRLRYVE</span><span class="topo-membrane">IKHGRISMLAVVGYLVQ</span><span class="topo-outside">EAGVRLPGTIDYSGKTFAEIPNGFAAFKEIPA</span><span class="topo-membrane">GGLVQLLFFIGVLES</span><span class="topo-inside">SVMRDLTGEAEFVGDFRNGA</span></span>
<span class="topo-ruler">       130       140       150       160       </span>
<span class="topo-line"><span class="topo-inside">IDFGWDTFDEETQFKKRAI</span><span class="topo-membrane">ELNQGRAAQMGILALMVH</span><span class="topo-outside">EQLGVSLLP</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>36</td>
      <td>1</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>53</td>
      <td>37</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>85</td>
      <td>54</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>100</td>
      <td>86</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>139</td>
      <td>101</td>
      <td>139</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>157</td>
      <td>140</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>166</td>
      <td>158</td>
      <td>166</td>
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

### FCP forms a homodimer via C-helix interactions

Unlike the trimeric LHCII from green plants, FCP from P. tricornutum forms a homodimer. Two monomers are held together by hydrophobic interactions between their transmembrane C helices. The N-terminal "WYGPDR" motif and C-terminal Trp residue crucial for LHCII trimer formation are absent in Lhcf4, explaining the dimeric assembly. The N- and C-termini and loop regions are shorter in FCP compared to LHCII, and helix D found at the lumenal surface in LHCII is absent.

### Unique pigment composition enables blue-green light harvesting

Each FCP monomer binds nine Chls (seven Chl a, two Chl c) and seven Fxs, giving a much higher Fx/Chl ratio than LHCI and LHCII. The two Chl c molecules are located at opposing sides of transmembrane helices A and B, in close interaction with nearby Chls a and Fxs. Each Fx is surrounded by one or more Chls, with pi-pi distances of 4.0 A or less, enabling fast and efficient excitation energy transfer (as fast as 75 fs, >90% efficiency).

### Chl c enables efficient harvesting of the green gap

Chl c absorbs blue-green and even yellow light, which is the "green gap" where Chls a and b absorb weakly. The energy absorbed by Chls c is transferred efficiently to coupled Chls a. The close coupling of Chl c with Chl a and Fx allows Chl c to serve as an efficient harvester of the blue-green light available underwater.

### Diadinoxanthin cycle in energy dissipation

One Ddx molecule is located near the monomer-monomer interface. Its weak electron density suggests easy dissociation and involvement in the Ddx-Dtx de-epoxidation cycle that functions in energy dissipation (NPQ). Luminal acidic residues (Glu54, Asp64, Glu72, Glu82, Glu158) may be involved in pH-induced conformational changes during photoprotection. Two calcium cations coordinated at the lumenal surface may modulate this pH response.


## Cross-References

- <a href="/xray-mp-wiki/proteins/photosynthesis/pea-light-harvesting-complex-ii/">Pea Light-Harvesting Complex II (LHC-II)</a> — FCP is structurally homologous to LHCII but has unique pigment composition and dimeric assembly
- <a href="/xray-mp-wiki/proteins/photosynthesis/spinach-light-harvesting-complex-ii/">Spinach Light-Harvesting Complex II (LHC-II)</a> — Comparison of FCP with LHCII reveals differences in pigment binding and oligomeric state
- <a href="/xray-mp-wiki/concepts/miscellaneous/non-photochemical-quenching/">Non-photochemical Quenching (NPQ)</a> — FCPs exhibit robust NPQ via the Ddx-Dtx xanthophyll cycle for photoprotection under high light
- <a href="/xray-mp-wiki/reagents/ligands/lutein/">Lutein</a> — Lutein-binding sites in LHCII correspond to Fx303 and Fx305 positions in FCP
- <a href="/xray-mp-wiki/reagents/ligands/fucoxanthin/">Fucoxanthin</a> — Referenced in fcp-phaeodactylum-tricornutum text
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in fcp-phaeodactylum-tricornutum text
- <a href="/xray-mp-wiki/reagents/lipids/digalactosyl-diacylglycerol/">Digalactosyl Diacylglycerol</a> — Referenced in fcp-phaeodactylum-tricornutum text
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in fcp-phaeodactylum-tricornutum text
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a> — Referenced in fcp-phaeodactylum-tricornutum text
- <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> — Referenced in fcp-phaeodactylum-tricornutum text
