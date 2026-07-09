---
title: "E. coli YebT Tube-like MCE Protein"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.03.019]
verified: regex
uniprot_id: P64605
---

# E. coli YebT Tube-like MCE Protein

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P64605">UniProt: P64605</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

YebT (also known as MAM7) is a periplasm-spanning MCE (mammalian cell entry) protein from Escherichia coli that forms an elongated tube-like hexameric barrel. YebT consists of seven tandem MCE domains that stack into seven hexameric rings, forming a ~570 kDa complex approximately 230 A long and 90 A in diameter. The structure spans the periplasmic space between the inner and outer membranes of Gram-negative bacteria, creating a continuous channel of sufficient length to directly transport lipids without the need for a periplasmic shuttle protein. YebT is anchored in the inner membrane via six transmembrane helices, with its C terminus extending up to 230 A away from the membrane.

## Publications

### doi/10.1016##j.cell.2017.03.019

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5uw8">5UW8</a></td>
      <td>~20 A (EMDB: EMD-8611)</td>
      <td>not applicable</td>
      <td>Full-length YebT (residues 1-440 approximately), with N-terminal transmembrane helices</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli Rosetta2 DE3
- **Construct**: yebST operon cloned into pBAD-His for bicistronic YebS-YebT co-expression with C-terminal 6xHis tag on YebT

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
      <td>Emulsiflex-C3 cell disruptor</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0, 300 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + --</td>
      <td>Membrane fraction prepared by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane solubilization with detergent</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0, 300 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + n-Dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>)</td>
      <td>YebT solubilized from membrane fraction</td>
    </tr>
    <tr>
      <td>His-tag affinity purification</td>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA Agarose Resin</a> agarose</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0, 300 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> (wash), 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> (elution) + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Full-length YebT purified; YebS co-expression construct but only YebT obtained in significant amounts</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex 200</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> pH 8.0, 150 mM NaCl + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Hexameric YebT tube-like complex</td>
    </tr>
  </tbody>
</table>


## Biological / Functional Insights

### Seven-ringed tube architecture spanning the periplasm

YebT forms a ~570 kDa hexameric assembly of six copies of the YebT polypeptide,
each containing seven tandem MCE domains. The seven MCE domains stack into seven
hexameric rings, forming an elongated tube approximately 230 A long and 90 A in
diameter. The tube resembles other macromolecular barrels such as the proteasome,
ClpXP, and GroEL. A fuzzy density at one end likely corresponds to a detergent
micelle and the N-terminal transmembrane helices from each YebT chain. The C terminus
of YebT can extend up to 230 A from the inner membrane, spanning the ~225 A distance
between the inner and outer membranes in E. coli.

### Hexameric ring stacking determined by tandem MCE domains

Each ring of density in the YebT reconstruction exhibits apparent 6-fold symmetry
and is similar in overall size and shape to the hexameric ring formed by [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/mlaD).
Polyalanine MCE models derived from the [E. coli MlaD MCE Protein](/xray-mp-wiki/proteins/mlaD) hexamer fit well into each density
ring. The number of stacked rings corresponds directly to the number of tandem
MCE domains in the primary sequence: YebT has seven MCE domains yielding seven
rings. This suggests a modular assembly principle where the domain architecture
of an MCE protein determines the architecture of its hexameric assembly.

### Lipid transport without periplasmic shuttle

Unlike the Mla system which uses [E. coli MlaC Periplasmic Lipid-Binding Protein](/xray-mp-wiki/proteins/mlaC) as a soluble periplasmic lipid shuttle, YebT
creates a continuous channel directly spanning the periplasm. This allows YebT
to potentially transport lipids or other hydrophobic molecules directly between
the inner and outer membranes without requiring a separate carrier protein. YebT
may associate with the inner membrane protein YebS as part of a larger transport
complex.


## Cross-References

- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaD/">E. coli MlaD MCE Protein</a> — YebT shares the same MCE domain fold; MlaD hexameric ring serves as structural template
- <a href="/xray-mp-wiki/proteins/structural-adhesion/pqiB/">E. coli PqiB Syringe-like MCE Protein</a> — PqiB shares the same modular stacking principle but with only three MCE domains
- <a href="/xray-mp-wiki/proteins/structural-adhesion/mlaC/">E. coli MlaC Lipid-Binding Protein</a> — MlaC shuttles lipids in the Mla system; YebT bypasses the need for a shuttle by direct spanning
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for YebT solubilization from membranes
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used for Ni-NTA affinity chromatography
- <a href="/xray-mp-wiki/concepts/protein-families/mce-protein-family/">MCE Protein Family</a> — YebT is a seven-domain MCE protein with unique tube-like architecture
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA Agarose Resin</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/tris">TRIS</a> — Entity mentioned in text
