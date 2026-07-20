---
title: "Burkholderia cenocepacia Haem Importer Complex BhuUV"
created: 2026-06-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms13411]
verified: agent
---

# Burkholderia cenocepacia Haem Importer Complex BhuUV

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

The BhuUV complex is the transmembrane and nucleotide-binding domain core of the type II ATP-binding cassette (ABC) haem importer from the Gram-negative pathogen Burkholderia cenocepacia. It consists of the transmembrane domain dimer BhuU and the nucleotide-binding domain dimer BhuV. The crystal structure in the nucleotide-free form reveals an inward-facing conformation where the cytoplasmic gate is open and the periplasmic gate is closed. This represents the post-translocation state of the haem transport cycle. BhuUV is a close ortholog of [Hmuuv](/xray-mp-wiki/proteins/abc-transporters/hmuuv/) from Yersinia pestis.

## Publications

### doi/10.1038##ncomms13411

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/unspecified">UNSPECIFIED</a></td>
      <td>2.8</td>
      <td>P2₁2₁2₁</td>
      <td>BhuU (TMD) dimer + BhuV (NBD) dimer (without BhuT)</td>
      <td>none (nucleotide-free)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: BhuU and BhuV co-expressed from a single plasmid with N-terminal 8 His-tag and enterokinase cleavage site on BhuU.
- **Induction**: 0.3 mM IPTG at OD600 0.6-0.8, further growth 20 h at 16°C
- **Media**: LB medium with ampicillin (50 µg/mL)

**Purification:**

- **Expression system**: E. coli c41 (DE3)
- **Expression construct**: BhuU with N-terminal 8 His-tag + enterokinase site + BhuV

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
      <td>French press</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.5, 150 mM NaCl, 2 mM MgCl₂, 10 µg/mL DNase, 0.2 mg/mL lysozyme + --</td>
      <td>Cell debris removed by centrifugation; membrane fraction obtained by ultracentrifugation at 66,000g for 1 h</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.5, 150 mM NaCl + 2% (w/v) n-decyl-β-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Solubilized for 1 h at 4°C</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> agarose</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.5, 150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>His-tagged BhuUV captured</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.5, 150 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>BhuUV complex purified</td>
    </tr>
  </tbody>
</table>
**Final sample**: BhuUV complex in 50 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.02% DM

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>BhuUV complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>unspecified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4°C or 20°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>unspecified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Nucleotide-free form; 76 ligands and 22 water molecules resolved in refinement</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Inward-facing conformation of BhuUV

The BhuUV structure (2.8 Å) reveals an inward-facing conformation in the nucleotide-free form, in sharp contrast to the outward-facing conformation of the orthologous [Hmuuv](/xray-mp-wiki/proteins/abc-transporters/hmuuv/) from Yersinia pestis. The cytoplasmic gate is completely open, with hydrophobic residues L177, L178, and I181 of TM5 separated from the other monomer. The periplasmic gate is sealed by R204-D200 salt bridges and hydrophobic interaction in helix H5a. This structure represents the post-translocation state of the type II ABC haem importer.

### Haem translocation channel architecture

The transmembrane channel extends from below H5a to the cytoplasmic solvent region. The channel wall is formed by TM3, TM5, TM8, and TM10. Per BhuU monomer, 28 hydrophobic residues, 9 polar residues (N108, S119, S120, T127, N184, T195, T207, S210, T319), and only 1 charged residue (D112) are found. D112 is the only charged residue in the BhuU dimer channel and is critical for haem transport activity, as the D112R mutant showed reduced [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis and was unstable during purification.

### Structural comparison with HmuUV

Structural alignment of BhuU and HmuU monomers (r.m.s.d. 0.8 Å for 135 Cα atoms in core TM helices) reveals that while TM1, TM2, TM6, TM7, TM8, and TM9 orientations are similar, TM3-5 and H5a show large deviations. The core TM helices of the dimers can rotate as a unit by 6°. The inward-facing BhuU has an open cytoplasmic gate while HmuU has a sealed cytoplasmic gate, consistent with their respective inward- and outward-facing conformations.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — BhuUV is a type II ABC transporter
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — Inward/outward-facing conformations illustrate alternating access
- <a href="/xray-mp-wiki/proteins/abc-transporters/bhuuv-t/">BhuUV-T Complex</a> — BhuUV is the core complex of BhuUV-T
- <a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French Press Cell Lysis</a> — Used for cell lysis in BhuUV purification
- <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-β-D-Maltopyranoside (DM)</a> — Detergent used for membrane solubilization
- <a href="/xray-mp-wiki/proteins/abc-transporters/hmuuv/">Yersinia pestis Heme Transporter HmuUV</a> — Orthologous type II ABC haem importer; HmuUV is outward-facing vs BhuUV inward-facing
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> — Referenced in the context of Tris Hcl
- <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> — Referenced in the context of DM
- <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> — Referenced in the context of ATP
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in the context of Imidazole
