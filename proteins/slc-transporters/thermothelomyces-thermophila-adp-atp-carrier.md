---
title: "Thermothelomyces thermophila ADP/ATP Carrier"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2018.11.025]
verified: false
---

# Thermothelomyces thermophila ADP/ATP Carrier

## Overview

The Thermothelomyces thermophila ADP/ATP carrier (TtAac) is a mitochondrial inner membrane transporter. The thermostabilized Q302K mutant was crystallized in the matrix-open state locked by [Bongkrekic Acid](/xray-mp-wiki/reagents/ligands/bongkrekic-acid/), revealing the transport mechanism involving rotation of three domains about a central substrate-binding site.

## Publications

### doi/10.1016##j.cell.2018.11.025

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6gj2">6GJ2</a></td>
      <td>3.3 A</td>
      <td>P3221</td>
      <td>TtAac residues 4-315 with Q302K mutation, N-terminal MetSer tag, complex with <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/bongkrekic-acid/">Bongkrekic Acid</a> (BKA); tetraoleoyl <a href="/xray-mp-wiki/reagents/lipids/cardiolipin/">Cardiolipin</a>; <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6gj3">6GJ3</a></td>
      <td>3.6 A</td>
      <td>P212121</td>
      <td>TtAac residues 8-311 with Q302K mutation, N-terminal His8 tag with Factor Xa cleavage site</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/bongkrekic-acid/">Bongkrekic Acid</a> (BKA); tetraoleoyl <a href="/xray-mp-wiki/reagents/lipids/cardiolipin/">Cardiolipin</a></td>
    </tr>
  </tbody>
</table>

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
      <td>Mitochondria isolation</td>
      <td>Cell disruption and differential centrifugation</td>
      <td>--</td>
      <td>0.1 M MES pH 6.5, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
      <td>Saccharomyces cerevisiae WB-12 strain, grown in YEPG at 30 C for 72 h</td>
    </tr>
    <tr>
      <td>BKA inhibition</td>
      <td>Inhibitor pre-incubation</td>
      <td>--</td>
      <td>100 mM Tris pH 7.4, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 2 umol BKA per mg mitochondrial protein, 250 uM ADP</td>
      <td>Inhibited at room temperature for 30 min before solubilization</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>2% 10-MNG, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 150 mM NaCl, 5 uM BKA</td>
      <td>Solubilized for 1 h at 4 C, clarified by ultracentrifugation at 200,000g</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity purification</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni Sepharose High Performance</td>
      <td>100 mM Tris pH 7.4, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 150 mM NaCl, 5 uM BKA</td>
      <td>Washed with buffer containing 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> complex formation</td>
      <td>Complex incubation</td>
      <td>Ni Sepharose High Performance</td>
      <td>Buffer C with <a href="/xray-mp-wiki/reagents/lipids/cardiolipin/">Cardiolipin</a>, <a href="/xray-mp-wiki/reagents/detergents/hega-10/">HEGA-10</a>, BKA</td>
      <td>His-tagged <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> added, incubated 30 min at 4 C, then overnight with Ni Sepharose</td>
    </tr>
    <tr>
      <td>Factor Xa cleavage</td>
      <td>Protease cleavage</td>
      <td>--</td>
      <td>Buffer D with CaCl2, <a href="/xray-mp-wiki/reagents/detergents/hega-10/">HEGA-10</a>, BKA</td>
      <td>Slurry supplemented with 30 ug Factor Xa protease, incubated at 10 C for 2 h</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>Gel filtration</td>
      <td>Sephadex G75</td>
      <td>10 mM Tris pH 7.4, 50 mM NaCl, 0.35% <a href="/xray-mp-wiki/reagents/detergents/hega-10/">HEGA-10</a>, 10 uM BKA</td>
      <td>TtAac-Nb complex eluted in volume fractions 0.5-1.5 mL</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>TtAac-Nb complex at A280 8-10</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M HEPES pH 7.5, 3% 3-methyl-3-pentanol, 18% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> OR 0.1 M MES pH 6.5, 1% 3-methyl-3-pentanol, 22% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>PFO cryo oil or LV cryo oil, flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown at 4 C, appeared within 3 days. Also solved without <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> (6GJ3, P212121, 3.6 A) confirming structure not affected by <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a>.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Matrix-open state structure reveals transport mechanism

The BKA-inhibited m-state structure shows the carrier with a central cavity open to the mitochondrial matrix side, with matrix helices rotated outward. The cytoplasmic side is closed by conserved hydrophobic residues and a salt bridge network braced by tyrosines. The carrier switches between states by rotation of its three domains about a fulcrum provided by the substrate-binding site, a mechanism likely applicable to the whole mitochondrial carrier family.

### Bongkrekic acid as conformation-specific competitive inhibitor

BKA binds deeply and asymmetrically within the central cavity, mimicking the dicarboxylate end of ATP phosphate groups and the polyunsaturated backbone mimicking the adenine ring. BKA forms electrostatic interactions with K30, R88, R197, hydrogen bonds to Y196, N96, and Y89. The steric bulk of BKA polyunsaturated backbone prevents substrate binding, locking the carrier in an abortive m-state.

### Cytoplasmic gate and salt bridge networks

The cytoplasmic gate is formed by hydrophobic residues (F97, F201, L295), the cytoplasmic salt bridge network (D101, K104, D205, K208, D299, K302), and tyrosine braces (Y100, Y204, Y298). These elements are highly conserved across the mitochondrial carrier family. Mutations of the strongest network links (R100, K104, K208) have the greatest effect on transport and thermal stability.

### Alternating access mechanism with domain rotation

The transport mechanism involves rigid-body rotation of core elements with approximately 15 degree rocking motion coupled with inward movement of gate elements. The substrate-binding site acts as a fulcrum. Core elements comprise odd-numbered helices, matrix helices, linkers, and one-third of even-numbered helices. Gate elements are the C-terminal portions of even-numbered helices beyond the contact points (R88, G192, R287).


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/bongkrekic-acid/">Bongkrekic Acid</a> — BKA inhibitor co-crystallized with TtAac, locks m-state conformation
- <a href="/xray-mp-wiki/reagents/lipids/cardiolipin/">Cardiolipin</a> — Tetraoleoyl cardiolipin binds at inter-domain interfaces via helix dipole interactions
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Decyl Maltose Neopentyl Glycol (10-MNG)</a> — Primary solubilization detergent at 2% for mitochondrial carrier extraction
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — PEG400 and PEG600 used as crystallization precipitants
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> — Crystallization buffer at 0.1 M pH 7.5
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> — Alternative crystallization buffer at 0.1 M pH 6.5
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Elution agent for Ni-NTA affinity purification
- <a href="/xray-mp-wiki/proteins/slc-transporters/bovine-adp-atp-carrier/">Bovine ADP/ATP Carrier</a> — Homologous mitochondrial carrier; ScAac2 CATR-inhibited c-state used for comparison
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
