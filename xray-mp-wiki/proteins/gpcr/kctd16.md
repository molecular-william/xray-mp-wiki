---
title: "KCTD16 (Potassium Channel Tetramerization Domain-Containing Protein 16)"
created: 2026-06-11
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1903024116]
verified: pdb-pass
uniprot_id: Q68DU8
---

# KCTD16 (Potassium Channel Tetramerization Domain-Containing Protein 16)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q68DU8">UniProt: Q68DU8</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

KCTD16 is a potassium channel tetramerization domain-containing protein that functions
as an auxiliary subunit of metabotropic GABA_B receptors. It belongs to the KCTD family
(group D) along with KCTD8, KCTD12, and KCTD12b, which modulate GABA_B receptor
signaling. KCTD16 contains an N-terminal T1 oligomerization domain (broad-complex,
tramtrack, and bric a brac fold) and two C-terminal homology domains (H1 and H2).
The T1 domain forms an open pentamer that binds to the C-terminal tail of the GABA_B2
subunit. The crystal structure of the KCTD16 T1 domain in complex with a GABA_B2-derived
peptide (residues 895-909) was solved at 2.4 A resolution, revealing that a single
GABA_B2 peptide binds to the interior of the open pentamer formed by five KCTD16
subunits. Key interfacial residues include F80 (conserved across all four KCTD subunits)
and E102, which form hydrophobic and hydrogen bonding interactions with the GABA_B2
peptide.


## Publications

### doi/10.1073##pnas.1903024116

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ocp">6OCP</a></td>
      <td>2.4</td>
      <td>P1</td>
      <td>KCTD16 T1 domain (residues 22-134) in complex with GABA_B2(895-909) peptide</td>
      <td>GABA_B2 peptide</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: KCTD16 T1 domain (residues 22-134), L89M mutant for SeMet

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
      <td>Homogenization</td>
      <td>—</td>
      <td>50 mM Tris pH 8.0, 500 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
      <td>Lysate clarified by centrifugation</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)</td>
      <td>50 mM Tris pH 8.0, 500 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
      <td>Eluted with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">tev</a> protease cleavage</td>
      <td>—</td>
      <td></td>
      <td>His6-SUMO tag removed overnight at 4 C</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex 75</td>
      <td>10 mM HEPES pH 7.5, 150 mM NaCl</td>
      <td></td>
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
      <td>KCTD16 T1 domain with GABA_B2(895-909) peptide at 1.5:5 molar ratio</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>2% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 6000, 2% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 8% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/sodium-cacodylate/">Sodium Cacodylate</a> trihydrate pH 5.6</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals belong to P1 space group with 15 molecules per asymmetric unit. Data collected at APS 24ID-C beamline.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### KCTD16 T1 forms an open pentamer

KCTD16 T1 assembles into an open pentameric ring structure (inner diameter ~25 A)
with a gap of ~16 A between subunits I and V. The pentamer is stabilized by extensive
salt bridge interactions mediated by the alpha-3 helix of each subunit. A D76R mutation
disrupts pentamer formation, converting KCTD16 T1 to a monomer in solution and
abolishing its ability to accelerate GIRK channel activation.

### Single GABA_B2 peptide binds to four KCTD16 subunits

The GABA_B2 C-terminal peptide (residues 895-909) forms a loop inside the KCTD16
pentamer ring, contacting four of the five subunits (I-IV). The binding involves
three regions: (1) N-terminal anchor via Q34/L896/L899 interactions with F80 from
subunits I-II; (2) a 3_10 helix (H900-Y903) sandwiched between F80 of subunits II-III
with key hydrogen bonds involving E102-Y903 and Q34-H901; (3) C-terminal contacts
with F80 of subunits III-IV. The interfacial residue F80 is conserved across all
GABA_B-associated KCTDs.

### Conserved binding mode across KCTD family

The GABA_B2-binding residues in KCTD16 (particularly F80, Q34, and E102) are
highly conserved in KCTD8, KCTD12, and KCTD12b, suggesting a universal binding
mode for all GABA_B-associated KCTD proteins. Co-immunoprecipitation experiments
confirmed that mutations at the interface (F80A, E102A in KCTD16; I898A, Y903A,
L904A in GABA_B2) disrupt both biochemical association and functional modulation
of GABA_B receptors.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/human-gabab-receptor/">Human GABA_B Receptor</a> — KCTD16 binds to the C-terminal tail of the GABA_B2 subunit as an auxiliary regulatory subunit
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-g-protein-coupling/">GPCR-G Protein Coupling Mechanism</a> — KCTD16 modulates GABA_B receptor coupling to GIRK channels
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/sodium-cacodylate/">Sodium Cacodylate</a> — Buffer component in purification or crystallization
