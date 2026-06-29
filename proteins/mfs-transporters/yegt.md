---
title: "YegT Nucleoside Proton Symporter from Escherichia coli"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jbc.2025.108357]
verified: false
---

# YegT Nucleoside Proton Symporter from Escherichia coli

## Overview

YegT is a member of the nucleoside proton symporter (NHS) family within the [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/mfs-transporter/). Despite only 27% sequence identity with [NupG](/xray-mp-wiki/proteins/mfs-transporters/nupg/), YegT shares high structural conservation and a conserved GXXXD motif in TM10 that mediates proton-coupled substrate translocation.

## Publications

### doi/10.1016##j.jbc.2025.108357

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8zoj">8ZOJ</a></td>
      <td>3.1</td>
      <td>unknown</td>
      <td>YegT K267A mutant from E. coli</td>
      <td>none (apo state)</td>
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
      <td>Cell lysis and membrane preparation</td>
      <td>Cell lysis and membrane fractionation</td>
      <td>—</td>
      <td>25 mM MES pH 6.0, 150 mM NaCl + 2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>High-pressure homogenization at 800 bar</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> affinity resin (Qiagen)</td>
      <td>25 mM MES pH 6.0, 150 mM NaCl, 25-300 mM imidazole + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Wash with 25 mM imidazole, eluted with 300 mM imidazole</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 Increase (GE Healthcare)</td>
      <td>25 mM MES pH 6.0, 150 mM NaCl + 0.4% NG (n-octyl beta-D-glucoside)</td>
      <td>Buffer exchanged to 0.4% NG for crystallization; concentrated to 30 mg/ml</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>, in meso)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>YegT K267A at 30 mg/ml, mixed with monoolein at 1:1.5 (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared within ~3 days; solved by molecular replacement at 3.1 Å</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Conserved GXXXD motif for proton coupling

YegT contains a conserved GXXXD motif (Gly311–Asp315) in TM10, equivalent to NupG's Gly319–Asp323. The Asp315 serves as the protonation site with a calculated pKa of 7.96 (at crystallization pH 5.8, Asp315 is protonated). MD simulations showed deprotonation of Asp315 triggers TM10 helix destabilization and TM8 outward shift.

### Different substrate specificity from NupG

YegT shares only 27% sequence identity with NupG. The substrate-binding cavity residues differ significantly — residues Phe143, Tyr318, Phe322, and Asn228 in NupG (involved in uridine binding) are not conserved in YegT. ITC experiments showed no significant binding of uridine, adenosine, cytidine, or guanosine to YegT, suggesting a different physiological substrate.

### Structural conservation despite low sequence identity

Despite 27% sequence identity, YegT and NupG share a high structural similarity (RMSD 1.57 Å over 316 Cα atoms). The overall MFS fold, the GXXXD motif, and the protonation site architecture are fully conserved, indicating a shared proton-coupled release mechanism.


## Cross-References

- <a href="/xray-mp-wiki/proteins/mfs-transporters/nupg/">NupG Nucleoside Proton Symporter</a> — Paralogs sharing the NHS family, conserved GXXXD motif, and proton-coupled mechanism
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — YegT belongs to the MFS family as an NHS member
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — YegT crystallized by [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) method with monoolein
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent for membrane solubilization of YegT
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid component of [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization matrix
- <a href="/xray-mp-wiki/reagents/buffers/mes/">2-(N-Morpholino)ethanesulfonic Acid (MES)</a> — Buffer used throughout YegT purification
- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl-beta-D-glucopyranoside (OG)</a> — Detergent used in [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) for crystallization
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — Core transport mechanism shared by MFS transporters
