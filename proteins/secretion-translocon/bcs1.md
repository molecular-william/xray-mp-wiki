---
title: "Mouse Bcs1 (AAA Protein Translocase)"
created: 2026-06-17
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##s41594-020-0373-0]
verified: false
---

# Mouse Bcs1 (AAA Protein Translocase)

## Overview

Bcs1 is a mitochondrial membrane-bound [AAA](/xray-mp-wiki/reagents/ligands/aaa/)+ ATPase that translocates folded proteins across the mitochondrial inner membrane. Its primary substrate is the Rieske iron-sulfur protein (ISP), a subunit of respiratory Complex III. Unlike canonical [AAA](/xray-mp-wiki/reagents/ligands/aaa/) unfoldases that thread unfolded polypeptides through a narrow central pore, Bcs1 forms a homo-heptamer that creates a large substrate-binding cavity (~35 A diameter, ~28,000 A^3 volume) sufficient to accommodate folded protein domains. [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structures of mouse Bcs1 (mBcs1) in apo, ATPgS-bound, and ADP-bound states reveal a nucleotide-dependent conformational cycle. In the apo/ADP-bound state, the cavity is open and accessible to the mitochondrial matrix, allowing substrate entry. ATP binding drives a concerted contraction of the [AAA](/xray-mp-wiki/reagents/ligands/aaa/) domains, pushing the substrate across the membrane. This mechanism represents a departure from the threading mechanism of hexameric [AAA](/xray-mp-wiki/reagents/ligands/aaa/) proteins, making Bcs1 a prototype for a class of [AAA](/xray-mp-wiki/reagents/ligands/aaa/) translocases that transport folded protein substrates. mBcs1 shares 94% sequence identity with human BCS1L, whose mutations cause GRACILE syndrome and Bjoernstad syndrome.

## Publications

### doi/10.1038##s41594-020-0373-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ukp">6UKP</a></td>
      <td>3.81</td>
      <td></td>
      <td>Full-length mouse Bcs1 (residues 1-418), apo form</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6uks">6UKS</a></td>
      <td>3.2</td>
      <td></td>
      <td>Full-length mouse Bcs1 (residues 1-418) with ATPgS and Mg2+</td>
      <td>ATPgS, Mg2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6u1y">6U1Y</a></td>
      <td>2.2</td>
      <td></td>
      <td>N-terminally truncated mouse Bcs1 (DeltaN mBcs1, residues 151-418) with <a href="/xray-mp-wiki/reagents/ligands/amp-pnp/">AMP-PNP</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/amp-pnp/">AMP-PNP</a>, Mg2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6uko">6UKO</a></td>
      <td>4.4</td>
      <td></td>
      <td>Full-length mouse Bcs1 (residues 1-418) with ADP</td>
      <td>ADP</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (yeast expression system)
- **Construct**: Full-length mouse Bcs1 (residues 1-418) with N-terminal or C-terminal hexahistidine tag in pPICZ A vector

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
      <td>Expression and membrane preparation</td>
      <td>Pichia pastoris expression with <a href="/xray-mp-wiki/reagents/additives/methanol/">Methanol</a> induction for 4 days</td>
      <td></td>
      <td>100 mM Tris, pH 8, 100 mM <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 2 mM PMSF</td>
      <td>Cells disrupted by Microfluidizer at 2,500 bar for three passages. Crude membranes collected by ultracentrifugation at 125,000g for 1 h.</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>CHAPS detergent solubilization</td>
      <td></td>
      <td>25 mM potassium phosphate, pH 7.4, 200 mM NaCl, 0.5% CHAPS</td>
      <td>20% CHAPS solution added slowly to 0.5% final concentration with 5 mg/ml final protein concentration at 4 C for 30 min. Insoluble material removed by centrifugation at 125,000g for 30 min.</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Nickel-nitrilotriacetic acid (Ni-NTA) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA resin (Qiagen)</td>
      <td>25 mM Tris, pH 8, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.1% CHAPS</td>
      <td>Bound protein washed and eluted with <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient.</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>25 mM Tris, pH 8, 150 mM NaCl, 0.1% CHAPS</td>
      <td>Purification yielded homogeneous heptameric mBcs1 as confirmed by BN-PAGE and <a href="/xray-mp-wiki/methods/quality-assessment/sec-mals/">SEC-MALS</a>.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> single-particle analysis</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Full-length mouse Bcs1, purified in detergent (CHAPS), with or without ATPgS.Mg2+</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> grids prepared using self-assembled monolayer supports. Data collected on a Titan Krios at 300 kV with Gatan K2 Summit detector. Two structures determined: apo (3.81 A) and ATPgS-bound (3.2 A). Data processing with MotionCor2, gCTF, and RELION.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>DeltaN mBcs1 (residues 151-418, C-terminal His6 tag) with <a href="/xray-mp-wiki/reagents/ligands/amp-pnp/">AMP-PNP</a>.Mg2+</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>X-ray crystallography of truncated mBcs1 lacking the N-terminal Bcs1-specific domain. Diffracted to 2.2 A resolution. Seven-fold symmetry confirmed by self-rotation function. <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> was unsuccessful with known <a href="/xray-mp-wiki/reagents/ligands/aaa/">AAA</a> domains; phased using <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> derived model.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Full-length mBcs1 with ATPgS.Mg2+</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>X-ray crystallography of full-length mBcs1. Crystals only obtained in the presence of ATPgS.Mg2+. Diffracted to 4.4 A resolution. <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> failed with known <a href="/xray-mp-wiki/reagents/ligands/aaa/">AAA</a> structures; phased using the apo mBcs1 <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> model. Bound ADP detected in the nucleotide-binding pocket despite ATPgS in the crystallization condition.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Homo-heptameric assembly enables folded protein translocation

Bcs1 forms a homo-heptamer (~324 kDa) rather than the canonical hexamer found in most [AAA](/xray-mp-wiki/reagents/ligands/aaa/) proteins. The heptameric architecture creates a larger entrance and binding cavity (~35 A average diameter, ~28,000 A^3 volume) sufficient to accommodate folded protein substrates like the 126-residue ISP extrinsic domain (~25 A effective diameter).

### Nucleotide-dependent conformational changes drive substrate translocation

ATP binding to Bcs1 induces a concerted contraction of the [AAA](/xray-mp-wiki/reagents/ligands/aaa/) domains, reducing the substrate-binding cavity volume. In the apo/ADP-bound state, the cavity is open and accessible to the mitochondrial matrix. ATP binding causes inter-subunit sliding movements that constrict the cavity, potentially pushing the substrate across the mitochondrial inner membrane. The Arg-finger residue R343 moves ~19 A in the apo state to interact with the gamma-phosphate in the ATPgS-bound state.

### Unique seven-stranded beta-sheet in the AAA domain

Unlike most [AAA](/xray-mp-wiki/reagents/ligands/aaa/) proteins that have a five-stranded beta-sheet in the RecA-like domain, Bcs1 has a seven-stranded beta-sheet with two extra beta-strands at the N terminus of the [AAA](/xray-mp-wiki/reagents/ligands/aaa/) domain. This unique structural feature places Bcs1 in a separate phylogenetic group of its own.

### Bcs1 lacks pore-loop and sensor-II motifs

Bcs1 lacks the conserved substrate-contact pore loop found in canonical [AAA](/xray-mp-wiki/reagents/ligands/aaa/) unfoldases that use a hand-over-hand threading mechanism. Additionally, the sensor-II region in the small helical domain involved in ATP binding is missing. This suggests Bcs1 uses a fundamentally different translocation mechanism compared to other [AAA](/xray-mp-wiki/reagents/ligands/aaa/) proteins.

### Distinct TM domain behavior in different nucleotide states

In the apo structure, the TM helices (L29-I49) were partially traced, suggesting close association of TM helices. In the ATPgS-bound structure, the TM region is entirely disordered, with the first confidently modeled residue being I49. This indicates nucleotide-dependent reorganization of the transmembrane domain.

### Human disease mutations mapped to Bcs1 structure

mBcs1 shares 94% sequence identity with human BCS1L. Mapping of disease-causing mutations onto the mBcs1 structure reveals that mutations associated with the severe GRACILE syndrome cluster at the Bcs1-specific domain and [AAA](/xray-mp-wiki/reagents/ligands/aaa/) domain interface, while those causing the milder Bjoernstad syndrome are distributed throughout. 14 out of 21 missense mutations involve positively charged arginine residues, underscoring the importance of electrostatic interactions in Bcs1 function.

### Putative substrate-binding cavity electrostatic properties

The cap of the putative substrate-binding cavity, made of the Bcs1-specific domain, is intensely negatively charged. The interior surface of the cavity in the apo state is negatively charged, complementary to the positively charged surface of the ISP substrate. This electrostatic complementarity likely guides substrate recognition and binding.


## Cross-References

- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/quality-assessment/sec-mals/">SEC-MALS</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/methanol/">Methanol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/ligands/aaa/">AAA</a> — Related ligand or cofactor
