---
title: "Yersinia pestis Heme Transporter HmuUV"
created: 2026-06-05
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2417]
verified: false
---

# Yersinia pestis Heme Transporter HmuUV

## Overview

The HmuUV complex is the transmembrane and nucleotide-binding domain core of the type II [ATP](/xray-mp-wiki/reagents/ligands/atp/)-binding cassette (ABC) haem importer from the Gram-negative pathogen Yersinia pestis. It consists of the transmembrane domain dimer HmuU and the nucleotide-binding domain dimer HmuV. The crystal structure in the nucleotide-free form reveals an outward-facing conformation where the periplasmic gate is open and the cytoplasmic gate is closed. This represents the substrate-receptive state of the haem transport cycle, poised to accept a haem molecule from the cognate periplasmic binding protein HmuT. The structure also provides mechanistic insights into the coupling mechanism of type II ABC importers.

## Publications

### doi/10.1038##nsmb.2417

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
      <td>3.0</td>
      <td>P2₁</td>
      <td>HmuU (TMD) dimer + HmuV (NBD) dimer (nucleotide-free)</td>
      <td>none (nucleotide-free; outward-facing conformation)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: HmuU and HmuV co-expressed from a single plasmid with N-terminal His10 (decahistidine) tag on HmuU. HmuT expressed separately with C-terminal hexahistidine tag.
- **Induction**: unspecified
- **Media**: unspecified

**Purification:**

- **Expression system**: E. coli BL21 Gold (DE3)
- **Expression construct**: HmuU with N-terminal His10 tag + HmuV

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
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>unspecified + n-dodecyl-β-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Solubilized from membranes using <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (Anatrace)</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> Superflow (Qiagen)</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>-NaOH pH 8.0, 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>His10-tagged HmuUV captured</td>
    </tr>
  </tbody>
</table>
**Final sample**: HmuUV in 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM [NaCl](/xray-mp-wiki/reagents/additives/sodium-chloride/), 0.5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/)-NaOH pH 8.0, 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion in detergent solution</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>HmuUV complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>unspecified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>unspecified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>unspecified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>3D crystals grown in detergent solution. Phased using two <a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury (HgCl2) - Aquaporin Inhibitor</a> derivatives (EMP and EMTS) by single-wavelength anomalous diffraction (SIRAS). Diffraction data anisotropic: 3.0 A best, 3.2 A worst direction.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Outward-facing conformation of HmuUV

The HmuUV structure (3.0 A) reveals an outward-facing conformation in the nucleotide-free form. A cavity mainly formed by transmembrane helix 5 (TM5) and helix 5a (H5a) is accessible from the periplasm but closed to the cytoplasm, representing the haem translocation pathway. This is in contrast to the inward-facing conformation of the orthologous [Burkholderia cenocepacia Haem Importer Complex BhuUV](/xray-mp-wiki/proteins/abc-transporters/bhuuv/) from Burkholderia cenocepacia, suggesting that type II ABC importers sample outward-facing states even without nucleotide binding — a coupling mechanism distinct from other ABC transporters.

### Haem translocation pathway architecture

The haem translocation pathway is a cavity at the TMD dimer interface formed mainly by TM5 and H5a. The surface bears no resemblance to reported binding pockets of haem-dependent enzymes, and HmuUV showed no detectable affinity for haeme in detergent solution. A haemin molecule can be modeled into the cavity without steric clashes. The pathway is adapted for the smaller haeme substrate (652 Da) compared to the vitamin B12 transporter BtuCD (cobalamin, 1355 Da), with a smaller periplasmic entrance due to different spacer residues in TM10 and TM5.

### Conserved residues Gly164 and Arg176

Among the many conserved HmuU residues facing the translocation pathway, only Gly164 and Arg176 are uniquely conserved in functionally characterized haeme transporters. Arg176 is located at the periplasmic entrance to the translocation pathway. Gly164 marks the narrowing point in the entrance funnel. Mutations G164Y and R176Q impaired haeme transport and ATPase stimulation by HmuT, with G164Y resulting in almost complete uncoupling of [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis and transport by plugging the translocation pathway entrance.

### Comparison with BtuCD vitamin B12 transporter

HmuU and BtuC share 37% identity (57% similarity); HmuV and BtuD share 28% identity (45% similarity). Despite similar architecture and overall conformation, structural superposition revealed differences in the translocation pathways. The periplasmic entrance is smaller in HmuUV, correlating with the smaller substrate (haeme 652 Da vs cobalamin 1355 Da). In TM5, BtuCD contains Trp162 (conserved in BtuC homologs) whereas functionally characterized haeme transporters contain a smaller side chain. In TM10, HmuUV has Tyr320 (tyrosine or phenylalanine in haeme transporters) vs valine in BtuC.

### In vitro haeme transport assay

In vitro haeme transport rate of reconstituted HmuUV was determined to be 1.0 ± 0.1 nmol haeme min⁻¹ mg⁻¹ HmuUV at 37 °C, strictly dependent on [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis and cognate binding protein HmuT. The transport rate was lower than BtuCD (4.3 nmol vitamin B12 min⁻¹ mg⁻¹), attributed to lower assay concentrations required by the narrow linear detection range of the HRP-based haeme-quantification method. The apparent [ATP](/xray-mp-wiki/reagents/ligands/atp/) stoichiometry was ~300 [ATP](/xray-mp-wiki/reagents/ligands/atp/) per transported haeme, likely reflecting high basal ATPase rate in vitro rather than physiological stoichiometry.

### Coupling mechanism in type II ABC importers

The outward-facing conformation of HmuUV in the nucleotide-free state has implications for the coupling mechanism of type II ABC importers. Type I ABC importers (e.g., MalFGK) and ABC exporters (e.g., Sav1866) adopt outward-facing conformations in the [ATP](/xray-mp-wiki/reagents/ligands/atp/)-bound state but inward-facing in the absence of nucleotide. In contrast, both HmuUV and BtuCD adopt outward-facing conformations in their apo states, suggesting that type II ABC importers have a coupling mechanism distinct from other ABC transporters.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/type-ii-abc-transporter-family/">Type II ABC Transporter Family</a> — HmuUV is a type II ABC transporter
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — HmuUV is an ABC transporter
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — Outward/inward-facing conformations illustrate alternating access
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/inward-facing-conformation/">Inward-Facing Conformation of ABC Transporters</a> — HmuUV outward-facing conformation contrasts with inward-facing BhuUV
- <a href="/xray-mp-wiki/proteins/abc-transporters/bhuuv/">BhuUV Complex</a> — Orthologous haem transporter from Burkholderia cenocepacia
- <a href="/xray-mp-wiki/proteins/abc-transporters/bhuuv-t/">BhuUV-T Complex</a> — Orthologous haem importer complex from Burkholderia cenocepacia
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-β-D-Maltopyranoside (DDM)</a> — Detergent used for membrane solubilization of HmuUV
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer used in HmuUV purification and crystallization
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> — Affinity resin used for His-tag purification of HmuUV
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Related protein
