---
title: "ClpP Protease"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2006.05.063, doi/10.1016##j.jmb.2007.11.080]
verified: agent
uniprot_id: P0A6G7
---

# ClpP Protease

<div class="expr-badges"><span class="expr-badge expr-native-tissue">Native tissue</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0A6G7">UniProt: P0A6G7</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

ClpP is an ATP-dependent, general protease from bacterial cytoplasm that works with chaperones ClpA and ClpX to recognize, unfold, and cleave misfolded and transient proteins. ClpP forms a large circular assembly with an axial pore hole and contains 14 catalytic active sites utilizing a Ser/His/Asp catalytic triad mechanism. The structure shows a surprising fold similarity to the periplasmic Ser/Lys protease [SppA_EC](/xray-mp-wiki/proteins/enzymes/sppa-ec/) despite different catalytic mechanisms and oligomeric arrangements.

## Publications

### doi/10.1016##j.jmb.2006.05.063

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2clp">2CLP</a></td>
      <td>1.9</td>
      <td>--</td>
      <td>E. coli ClpP with peptide covalently bound</td>
      <td>peptide inhibitor</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Not specified in source papers; ClpP is a native cytoplasmic protease
- **Construct**: Native E. coli ClpP; the structure in PDB 2CLP includes ClpP with a peptide covalently bound at the active site

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
      <td>ClpP purification</td>
      <td>Not specified in detail; ClpP was purified for structural studies with covalently bound peptide inhibitor</td>
      <td>--</td>
      <td>-- + --</td>
      <td>ClpP was crystallized with a peptide covalently bound at the active site.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>ClpP with peptide covalently bound at active site</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structure solved at 1.9 A resolution; ClpP forms a 14-mer spherical assembly (two 7-mer oligomers). The axial hole is ~13.5 A in diameter.</td>
    </tr>
  </tbody>
</table>
### doi/10.1016##j.jmb.2007.11.080

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3bf0">3BF0</a></td>
      <td>--</td>
      <td>--</td>
      <td>E. coli ClpP (structural comparison model)</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Not specified in source papers; ClpP is a native cytoplasmic protease
- **Construct**: Native E. coli ClpP; the structure in PDB 2CLP includes ClpP with a peptide covalently bound at the active site


## Biological / Functional Insights

### 14-mer spherical assembly with axial pore

ClpP forms a large circular assembly composed of two heptameric rings (14-mer) creating a barrel-shaped structure with an axial pore hole of approximately 13.5 A in diameter. The major globular domain of each monomer forms the axial hole, with an internal sequence extension (the "handle") creating intercalating interactions between the two 7-mer halves. This is distinct from the bowl-shaped tetrameric assembly of SppA, where the extension domain forms the axial hole.

### Ser/His/Asp catalytic triad

Each ClpP monomer encodes a complete active site involving a Ser/His/Asp catalytic triad. This differs from SppA, which utilizes residues at the interface of its tandemly repeated domains to create a Ser/Lys catalytic dyad. Remarkably, when a ClpP monomer is superimposed on the C-terminal half of SppA, the catalytic atoms of the Ser/His/Asp triad superimpose with the catalytic atoms of the Ser/Lys dyad.

### ATP-dependent chaperone/protease complex

ClpP works with ATP-dependent chaperones ClpA and ClpX to form the ClpAP and ClpXP complexes. These chaperones recognize, unfold, and deliver misfolded and transient proteins from the bacterial cytoplasm to the ClpP protease chamber for degradation. This is analogous to how SppA may function in quality control of periplasmic and membrane-bound proteins.

### Structural similarity to SppA despite different mechanisms

Despite limited sequence identity (15.6-25% identity for 147-155 aligned residues), the N- and C-terminal regions of SppA monomers are similar in fold to ClpP monomers, with rmsd of 3.0 A and 1.8 A respectively. The oxyanion holes in both SppA and ClpP are unique among serine proteases in that they use a main-chain amide NH from the residue following the nucleophile. The internal surface of the ClpP complex is much more polar than the hydrophobic interior of the SppA bowl.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/sppa-ec/">Signal Peptide Peptidase A from Escherichia coli (SppA_EC)</a> — Primary structural comparison protein; SppA shows surprising fold similarity to ClpP despite different catalytic mechanisms; both are Ser proteases with similar oxyanion hole architecture
