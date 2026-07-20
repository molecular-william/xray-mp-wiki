---
title: "TonB (E. coli)"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature19757]
verified: agent
uniprot_id: P02929
---

# TonB (E. coli)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P02929">UniProt: P02929</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

TonB is an integral polytopic membrane protein from Escherichia coli that serves as the energy transducer connecting the inner membrane [Ton Complex](/xray-mp-wiki/concepts/miscellaneous/ton-complex/) (ExbB-[ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/)) to TonB-dependent transporters (TBDTs) at the outer membrane. TonB contains a single N-terminal transmembrane helix that anchors a large C-terminal periplasmic domain. The periplasmic domain contains a conserved 5-7 residue TonB box that interacts with TBDTs upon ligand binding. TonB exchanges for one [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) monomer during energy transduction, and its interaction with [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) triggers conformational changes that lead to ligand uptake by TBDTs at the outer membrane.


## Publications

### doi/10.1038##nature19757

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5sv0">5SV0</a></td>
      <td>2.6 A</td>
      <td>P63</td>
      <td>ExbB-ExbD-TonB fully assembled complex</td>
      <td>calcium ion</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5sv0">5SV0</a></td>
      <td>3.5 A</td>
      <td>P212121</td>
      <td>ExbB-ExbD-TonB fully assembled complex</td>
      <td>calcium ion</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli K-12 BL21(DE3) cells
- **Construct**: TonB cloned into pACYCDUET-1 vector with N-terminal 10xHis tag followed by TEV protease site; TonB C18A mutant also prepared

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
      <td>Emulsiflex-C3 high-pressure homogenization</td>
      <td>--</td>
      <td>TBS + --</td>
      <td>Cells resuspended with 100 uM AEBSF, 100 uM DNase, 50 ug/ml lysozyme; disrupted at ~15,000 p.s.i.</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Ultracentrifugation</td>
      <td>--</td>
      <td>TBS + --</td>
      <td>Pelleted at 200,000g for 1 h at 4 C; membranes resuspended with dounce homogenizer</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane solubilization</td>
      <td>--</td>
      <td>TBS + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Solubilized by addition of <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> to 1% final concentration</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>His-tag <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>--</td>
      <td>TBS + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purified using N-terminal 10xHis tag on TonB; co-expression with <a href="/xray-mp-wiki/proteins/other-ion-channels/exbB/">ExbB (E. coli)</a> and <a href="/xray-mp-wiki/proteins/other-ion-channels/exbD/">ExbD (E. coli)</a> for <a href="/xray-mp-wiki/concepts/miscellaneous/ton-complex/">Ton Complex</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>ExbB-ExbD-TonB fully assembled complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in paper</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
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
      <td>The fully assembled <a href="/xray-mp-wiki/concepts/miscellaneous/ton-complex/">Ton Complex</a> was characterized by electron microscopy, crosslinking, and DEER spectroscopy. Only a single TMH of TonB can fit within the <a href="/xray-mp-wiki/proteins/other-ion-channels/exbB/">ExbB (E. coli)</a> pentamer pore. DEER on the fully assembled complex (TonB C18A-<a href="/xray-mp-wiki/proteins/other-ion-channels/exbB/">ExbB (E. coli)</a> C25S-<a href="/xray-mp-wiki/proteins/other-ion-channels/exbD/">ExbD (E. coli)</a> N78C) showed distance distributions nearly identical to the subcomplex, confirming <a href="/xray-mp-wiki/proteins/other-ion-channels/exbD/">ExbD (E. coli)</a> remains dimeric in the presence of TonB.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Stoichiometry of the fully assembled Ton complex

The fully assembled [Ton Complex](/xray-mp-wiki/concepts/miscellaneous/ton-complex/) consists of a pentamer of [ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/), a dimer of [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/), and at least one TonB. Association of TonB does not notably affect the structure or stoichiometry of [ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/) or [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/). The interaction of TonB with [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) leads to a functional [Ton Complex](/xray-mp-wiki/concepts/miscellaneous/ton-complex/) that triggers energy production and transduction in the form of conformational changes in TonB, which lead to ligand uptake by the TBDT at the outer membrane.

### TonB-ExbD interaction and energy transduction

Previous studies indicated that TonB may exchange for one of the [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) monomers during energy transduction. The second [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) copy is located outside the [ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/) pentamer, hypothesized to be mediated by its periplasmic domain. The interaction of TonB with [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) leads to a functional [Ton Complex](/xray-mp-wiki/concepts/miscellaneous/ton-complex/), triggering energy production and transduction. This mechanism couples the proton motive force at the inner membrane to ligand transport across the outer membrane.

### DEER validation of complex assembly

DEER spectroscopy on the fully assembled [Ton Complex](/xray-mp-wiki/concepts/miscellaneous/ton-complex/) (TonB C18A-[ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/) C25S-[ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) N78C, labeled with MTSL) showed distance distributions for the labels on [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) nearly identical to those of the subcomplex, confirming that [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/) remains a dimer in both the absence and presence of TonB. This confirms the proposed model of a pentamer of [ExbB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbB/), dimer of [ExbD (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/exbD/), and at least one TonB.


## Cross-References

- <a href="/xray-mp-wiki/proteins/other-ion-channels/exbB/">ExbB (E. coli)</a> — TonB interacts with the ExbB pentamer as part of the fully assembled Ton complex
- <a href="/xray-mp-wiki/proteins/other-ion-channels/exbD/">ExbD (E. coli)</a> — TonB interacts directly with ExbD; TonB may exchange for one ExbD monomer during energy transduction
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for solubilization of the fully assembled Ton complex (1% DDM)
- <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6 Tag</a> — N-terminal 10xHis tag used for TonB purification
- <a href="/xray-mp-wiki/methods/quality-assessment/deer-spectroscopy/">DEER Spectroscopy</a> — DEER performed on the fully assembled Ton complex (TonB C18A-ExbB C25S-ExbD N78C) to validate stoichiometry
- <a href="/xray-mp-wiki/methods/quality-assessment/circular-dichroism-spectroscopy/">Circular Dichroism Spectroscopy</a> — Circular dichroism used to assess secondary structure and thermal stability of the Ton subcomplex
- <a href="/xray-mp-wiki/concepts/miscellaneous/ton-complex/">Ton Complex</a> — TonB is a core component of the Ton complex; the concept page describes the functional complex and energy transduction mechanism
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
