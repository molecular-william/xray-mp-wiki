---
title: "Yeast Mitochondrial F1 ATPase from Saccharomyces cerevisiae"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##sj.emboj.7601410, doi/10.1098##rsob.120164]
verified: false
---

# Yeast Mitochondrial F1 ATPase from Saccharomyces cerevisiae

## Overview

Yeast mitochondrial F1 ATPase is the water-soluble catalytic domain of the F1F0 ATP synthase (EC 3.6.3.14), the molecular motor responsible for ATP synthesis in mitochondria. The F1 complex has an α3β3γδε subunit stoichiometry, with three catalytic sites at the α/β interfaces. This 2.8 Å crystal structure reveals three independent copies of the complex with different conformational states, providing new insights into the rotary catalytic mechanism, including the binding of phosphate to the empty (βE) catalytic site.


## Publications

### doi/10.1038##sj.emboj.7601410

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2hld">2HLD</a></td>
      <td>2.8</td>
      <td>P21</td>
      <td>Yeast F1 ATPase (alpha3beta3gammadeltaepsilon)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/amp-pnp/">AMP-PNP (Adenylyl Imidodiphosphate)</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in monoclinic space group P21 with three F1 complexes per asymmetric unit; 0.25 mM NiSO4 present in crystallization medium</td>
    </tr>
  </tbody>
</table>
### doi/10.1098##rsob.120164

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3zia">3ZIA</a></td>
      <td>2.5</td>
      <td>P21</td>
      <td>Yeast F1 ATPase (alpha3beta3gammadeltaepsilon) inhibited by yI1-53 (IF1 residues 1-53, E21A mutation)</td>
      <td>ADP</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Microbatch under oil</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Yeast F1-ATPase (10 mg/ml) inhibited with yI1-53 (E21A), in 100 mM Bis-Tris propane pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a>, 1 mM ADP, 10 mM magnesium sulphate, 100 mM sodium-potassium tartrate</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Filtered paraffin oil (as sealant)</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>NA (microbatch)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>23</td>
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
      <td>Enzyme inhibited with 4-fold molar excess of yI1-53 before crystallization. Crystals grown in D2O-based crystallization buffer under paraffin oil in 72-well micro-batch plates.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Phosphate Binding to the βE Subunit

A strong electron density peak (8 sigma) found in the nucleotide-binding
site of the βE subunit of yF1II was modeled as inorganic phosphate (Pi).
The Pi-binding site is formed by residues αArg375, βLys163, βArg190,
βAsp256, βAsn257, and βArg260. This represents the first clear Pi-bound
state in F1 ATPase, providing a snapshot of phosphate binding during
ATP synthesis. The Pi-binding site is accessible from the internal
solvent-filled cavity of F1, consistent with random-order binding of
ADP and Pi.

### Central Stalk Rotation and Catalytic States

Comparison of yF1I and yF1II reveals a 16 degree rotation of the
γ-subunit (clockwise, in the direction of ATP synthesis) between the
two complexes. yF1II has Pi bound to βE with a rotated γ-subunit,
while yF1I has a 12 degree rotation in the opposite direction
(counterclockwise, toward ATP hydrolysis). These rotations are
associated with Pi binding (16 degrees) and the partial opening of
the αDP/βDP catalytic interface (12 degrees), providing a structural
framework for the rotary catalytic cycle.

### Comparison with Bovine F1 ATPase

The yeast F1 shows the same asymmetric features as the bovine enzyme
despite completely different crystal packing, confirming that the
asymmetry is an essential feature of F1 structure. The βDP active site
in yeast binds [AMP-PNP (Adenylyl Imidodiphosphate)](/xray-mp-wiki/reagents/ligands/amp-pnp/) (ATP analog) rather than ADP as in the bovine
enzyme, indicating this is not the ADP-inhibited form. The αDP/βDP
interface is more open in yF1I than in yF1II, with a relative rotation
of 5.5 degrees.

### IF1 Inhibition of Yeast F1-ATPase at 2.5 A Resolution

The structure of yeast F1-ATPase inhibited by its regulatory protein
IF1 (yI1-53, residues 1-53 with E21A mutation) was determined at
2.5 A resolution (space group P2_1, unit cell 118.2 x 187.8 x 181.8 A,
beta = 90.0 degrees). The inhibitory region (residues 1-36) is
entrapped between the C-terminal domains of the alpha_DP- and
beta_DP-subunits. The yeast inhibitor differs significantly from
bovine IF1: residues 6-16 form a loop held by a salt bridge between
R9 and D15 and a hydrogen-bonding network, whereas the bovine
inhibitor has an alpha-helical turn. From residue 17, the yeast
inhibitor forms an alpha-helix extending to residue 36, occupying
the same cleft as the bovine inhibitor but following a steeper path
(~7 degree angle difference) due to altered conformation of beta_DP
residues 391-398. Mutagenesis of R9 significantly impaired binding
(Ki increased ~3.5-fold), while L40A also increased Ki (~3.3-fold),
suggesting these residues play important roles in inhibition.

### Sequential Product Release Captured in the beta_E Subunit

The most significant difference from the bovine-inhibited complex is
the nucleotide occupancy of the catalytic beta_E-subunit. In the
yeast IF1-inhibited complex, the beta_E-subunit contains an ADP
molecule without an accompanying magnesium ion, whereas it is
unoccupied in the bovine complex. This provides structural evidence
for sequential product release during ATP hydrolysis: the phosphate
and magnesium ion are released before the ADP molecule. The structure
represents a post-hydrolysis, pre-nucleotide release intermediate in
the catalytic cycle. The adenosine binding pocket remains intact
(beta_E-Y345 and beta_E-F424 still form the pocket), and the
magnesium coordination sphere has been disrupted, releasing the
metal ion before ADP.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/">Bovine F1 ATPase</a> — Homologous ATP synthase catalytic domain used for comparison
- <a href="/xray-mp-wiki/proteins/pumps-atpases/yeast-mitochondrial-atp-synthase-c10-ring/">Yeast Mitochondrial ATP Synthase c10 Ring</a> — The membrane rotor component of the same ATP synthase complex
- <a href="/xray-mp-wiki/reagents/ligands/amp-pnp/">AMP-PNP</a> — ATP analog bound in the catalytic sites
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/f1-atpase-rotary-mechanism/">F1-ATPase Rotary Catalytic Mechanism</a> — The IF1-inhibited structure captures a post-hydrolysis intermediate providing evidence for sequential product release in the rotary mechanism
- <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> — Related ligand or cofactor
