---
title: "TySemiSWEET from Thermotoga yellowstonii"
created: 2026-06-02
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##cr.2014.144]
verified: regex
uniprot_id: B5YGD6
---

# TySemiSWEET from Thermotoga yellowstonii

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/B5YGD6">UniProt: B5YGD6</a>

<span class="expr-badge">Thermodesulfovibrio yellowstonii</span>

## Overview

TySemiSWEET is a bacterial sugar transporter from the [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/semisweet/) family found in Thermotoga yellowstonii. It is a dimeric three-helix bundle transporter that selectively transports disaccharides such as [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/). The structure reveals an elongated central pocket that accommodates a disaccharide ligand, providing structural insight into substrate selectivity within the [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/semisweet/) family.


## Publications

### doi/10.1038##cr.2014.144

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4rng">4RNG</a></td>
      <td>2.4</td>
      <td>P212121</td>
      <td>TySemiSWEET full-length</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> (tentative)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: TySemiSWEET full-length

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
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purified in detergent micelles; crystals in hanging-drop diffusion did not diffract beyond 10 A</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>TySemiSWEET</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted beyond 2.4 A at BL32XU, SPring-8; structure determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using <a href="/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/">LbSemiSWEET from Leptospira biflexa</a> as search model</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4rng">4RNG</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90    </span>
<span class="topo-line"><span class="topo-unknown">MEFSI</span><span class="topo-outside">DLNN</span><span class="topo-membrane">LIGIIAGAITTSALIPQALKIY</span><span class="topo-inside">KTKSARDV</span><span class="topo-membrane">SLAMFIFMAIGITLWFFYG</span><span class="topo-outside">VLIKEI</span><span class="topo-membrane">PVILANLISLILIFLIIFMKIR</span><span class="topo-inside">Y</span><span class="topo-unknown">GHHHHHH</span></span>
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
      <td>6</td>
      <td>9</td>
      <td>6</td>
      <td>9</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>31</td>
      <td>10</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>39</td>
      <td>32</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>58</td>
      <td>40</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>64</td>
      <td>59</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>86</td>
      <td>65</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4rng">4RNG</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90    </span>
<span class="topo-line"><span class="topo-unknown">MEFSI</span><span class="topo-outside">DLNNLI</span><span class="topo-membrane">GIIAGAITTSALIPQALKIY</span><span class="topo-inside">KTKSARDV</span><span class="topo-membrane">SLAMFIFMAIGITLWFFYGV</span><span class="topo-outside">LIKEI</span><span class="topo-membrane">PVILANLISLILIFLIIFMKI</span><span class="topo-inside">RYG</span><span class="topo-unknown">HHHHHH</span></span>
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
      <td>6</td>
      <td>11</td>
      <td>6</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>31</td>
      <td>12</td>
      <td>31</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>32</td>
      <td>39</td>
      <td>32</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>59</td>
      <td>40</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>64</td>
      <td>60</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>85</td>
      <td>65</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>88</td>
      <td>86</td>
      <td>88</td>
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

### Dimeric assembly and interface

Six TySemiSWEET molecules arranged into three dimers in the asymmetric unit. Two dimers are arranged in parallel fashion, while the third is positioned in opposite orientation. Within each dimer, the two parallel protomers are related by 180-degree rotation around an axis perpendicular to the membrane plane. The dimer interface involves hydrogen bonds between Tyr57 of one protomer and Glu63 of the other, and between Trp54 and Thr19. An extensive H-bond network exists between the L1-2 linkers on the cytosolic side.

### Central pocket and substrate selectivity

The central pocket of TySemiSWEET is 18 A long with surface area of 463 A squared and volume of 613 A cubed. This elongated pocket can accommodate a disaccharide molecule such as [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/). The pocket size is determined by Met47, which leaves enough space compared to the corresponding Phe41 in [LbSemiSWEET from Leptospira biflexa](/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/) that closes the pocket midway. All 16 residues in each protomer constituting the central pocket are highly conserved between TySemiSWEET and BjSemiSWEET1 (10 invariants), indicating similar pocket architecture in the [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) transporter BjSemiSWEET1. In contrast, [LbSemiSWEET from Leptospira biflexa](/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/) has a smaller pocket (11 A long, 424 A cubed volume) consistent with its function as a [Glucose](/xray-mp-wiki/reagents/additives/glucose/) transporter.

### Topology and transport mechanism

Each protomer contains three transmembrane helices (TM1, TM2, TM3) with TM3 positioned between TM1 and TM2. TM1 and TM2 are connected by an extended linker L1-2 enriched with positively charged residues. According to the positive-inside rule, L1-2 is located on the cytoplasmic side, leaving the N-terminus on the periplasmic side. The structure supports the alternating access mechanism, with the outward-open and occluded states captured. The inward-open structure remains to be determined.


## Cross-References

- <a href="/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/">LbSemiSWEET from Leptospira biflexa</a> — Close homologue used as molecular replacement search model; structural comparison reveals pocket size differences
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/sweet-transporter/">SWEET Transporter Family</a> — TySemiSWEET is a member of the SemiSWEET subfamily of sugar transporters
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — TySemiSWEET operates via alternating access with outward-open and occluded conformations captured
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — TySemiSWEET crystals obtained by LCP diffracted to 2.4 A at SPring-8
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/semisweet/">SemiSWEET Transporter Family</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> — Related ligand or cofactor
