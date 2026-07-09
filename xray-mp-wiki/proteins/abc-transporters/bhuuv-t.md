---
title: "Burkholderia cenocepacia Haem Importer Complex BhuUV-T"
created: 2026-06-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms13411]
verified: regex
---

# Burkholderia cenocepacia Haem Importer Complex BhuUV-T

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

The BhuUV-T complex is a type II ATP-binding cassette (ABC) haem importer from the Gram-negative pathogen Burkholderia cenocepacia. It consists of the transmembrane domain dimer BhuU, the nucleotide-binding domain dimer BhuV, and the periplasmic haem-binding protein BhuT. The crystal structure reveals an inward-facing conformation in the nucleotide-free form, representing the post-translocation state of the haem transport cycle. The periplasmic gate is closed and the cytoplasmic gate is open. This structure provides mechanistic insights into the conformational transitions of type II ABC haem importers.

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
      <td>3.2</td>
      <td>P2₁2₁2₁</td>
      <td>BhuU (TMD) dimer + BhuV (NBD) dimer + BhuT (PBP)</td>
      <td>none (haem- and nucleotide-free)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: BhuU and BhuV co-expressed from a single plasmid with N-terminal 8 His-tag and enterokinase cleavage site on BhuU. BhuT (residues 40-311, signal sequence removed) expressed separately with N-terminal GST tag and PreScission protease cleavage site.
- **Induction**: 0.3 mM IPTG at OD600 0.6-0.8, further growth 20 h at 16°C
- **Media**: LB medium with ampicillin (50 µg/mL) and chloramphenicol (34 µg/mL)

**Purification:**

- **Expression system**: E. coli c41 (DE3) for BhuUV, E. coli Rosetta2 (DE3) for BhuT
- **Expression construct**: BhuU with N-terminal 8 His-tag + enterokinase site; BhuV; BhuT residues 40-311 with N-terminal GST tag + PreScission site

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
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Ni-NTA agarose</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.5, 150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>His-tagged <a href="/xray-mp-wiki/proteins/abc-transporters/bhuuv/">Bhuuv</a> captured; GST-BhuT co-purified</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.5, 150 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>BhuUV-T complex co-purified</td>
    </tr>
  </tbody>
</table>
**Final sample**: BhuUV-T complex in 50 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.02% DM

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>BhuUV-T complex</td>
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
      <td>Nucleotide-free form; BhuT exhibits poor electron density with high temperature factors, possibly due to alternative orientation</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Inward-facing conformation of BhuUV-T

The BhuUV-T crystal structure reveals an inward-facing conformation in the nucleotide-free, haem-free form. The cytoplasmic gate is completely open, formed by separation of hydrophobic residues (L177, L178, I181) of TM5 from the other monomer. The periplasmic gate is tightly sealed by R204-D200 salt bridges and hydrophobic interaction (L203-L203') in helix H5a. This represents the post-translocation state of the haem transport cycle, previously uncharacterized for type II ABC transporters.

### BhuT-BhuU interaction interface

BhuT interacts with the periplasmic surface of BhuU. The α3-α4 helices of the N-terminal domain and α9-α10 helices and β-strands of the C-terminal domain of BhuT are bound into a shallow pocket on the BhuU dimer periplasmic surface. Binding is mediated by van der Waals contacts and salt bridges between E94 or E231 of BhuT with R84 of BhuU. These residues are highly conserved in type II ABC haem importers.

### Haem translocation channel

The haem translocation channel extends from below H5a to the cytoplasmic solvent region via the BhuU-BhuU and BhuV-BhuV dimerization interface. The channel wall is formed by TM3, TM5, TM8, and TM10. Per BhuU monomer, 28 hydrophobic residues, 9 polar residues (N108, S119, S120, T127, N184, T195, T207, S210, T319), and only 1 charged residue (D112) are found. No stable ligand binding site for haem [Iron](/xray-mp-wiki/reagents/additives/iron/) is present, suggesting hydrophobic residues transiently interact with haem during translocation.

### ATP-binding triggers BhuT dissociation

Pull-down assays demonstrate that [ATP](/xray-mp-wiki/reagents/ligands/atp/) or non-hydrolysable [ATP](/xray-mp-wiki/reagents/ligands/atp/) analogue ([Amp Pnp](/xray-mp-wiki/reagents/ligands/amp-pnp/)) causes dissociation of GFP-BhuT from [Bhuuv](/xray-mp-wiki/proteins/abc-transporters/bhuuv/), while [ADP](/xray-mp-wiki/reagents/ligands/adp/) does not. This indicates that ATP-binding (not hydrolysis) is sufficient to reduce [Bhuuv](/xray-mp-wiki/proteins/abc-transporters/bhuuv/) affinity for BhuT, facilitating the conformational reset from inward- to outward-facing state after haem translocation.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — BhuUV-T is a type II ABC transporter
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — Inward/outward-facing conformations illustrate alternating access
- <a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French Press Cell Lysis</a> — Used for cell lysis in BhuUV-T purification
- <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-β-D-Maltopyranoside (DM)</a> — Detergent used for membrane solubilization
- <a href="/xray-mp-wiki/reagents/ligands/amp-pnp/">AMP-PNP</a> — ATP analog used in pull-down assays
- <a href="/xray-mp-wiki/proteins/abc-transporters/bhuuv/">BhuUV Complex</a> — BhuUV-T contains BhuUV as core complex
- <a href="/xray-mp-wiki/proteins/abc-transporters/hmuuv/">Yersinia pestis Heme Transporter HmuUV</a> — Orthologous type II ABC haem importer; HmuUV outward-facing vs BhuUV-T inward-facing
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> — Referenced in the context of Tris Hcl
- <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> — Referenced in the context of DM
- <a href="/xray-mp-wiki/reagents/additives/iron/">Iron</a> — Referenced in the context of Iron
