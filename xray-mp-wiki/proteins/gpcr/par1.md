---
title: "Human Protease-Activated Receptor 1 (PAR1)"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11701]
verified: agent
uniprot_id: B6YXQ1
---

# Human Protease-Activated Receptor 1 (PAR1)


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/B6YXQ1">UniProt: B6YXQ1</a>

<span class="expr-badge">Thermococcus onnurineus</span>

## Overview

Human Protease-Activated Receptor 1 (PAR1) is a class A G protein-coupled receptor that serves as the primary signaling receptor for thrombin, a key protease in hemostasis and thrombosis. PAR1 activation by thrombin initiates platelet aggregation and promotes inflammatory responses. The crystal structure of human PAR1 in complex with the functionally irreversible antagonist [Vorapaxar](/xray-mp-wiki/reagents/ligands/vorapaxar/) was solved at 2.20 A resolution, revealing a closed ligand-binding pocket with the extracellular loop 2 (ECL2) forming a lid over the binding site. This structure provided the first high-resolution view of a thrombin-activated GPCR and enabled structure-based design of selective PAR1 antagonists for cardiovascular therapy.


## Publications

### doi/10.1038##nature11701

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3vw7">3VW7</a></td>
      <td>2.20</td>
      <td>P212121</td>
      <td>Human PAR1 with N-terminal FLAG epitope, TEV cleavage site between P85 and A86 (N-terminus before P85 removed), T4 lysozyme inserted between A301 and A303 in ICL3, 10xHis tag after S395, glycosylation mutations N250G and N259S in ECL2. Truncated at residue 395.
</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/vorapaxar/">Vorapaxar</a></td>
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
      <td>Notes</td>
      <td>18 crystals merged. Space group P212121. Cell dimensions: 44.0, 71.5, 172.2 A. Resolution 30.0 - 2.20 A (2.25 - 2.20 in highest shell). R_merge 13.5% (57.5% in highest shell). Completeness 95.6% (85.7% in highest shell). Multiplicity 4.8 (3.3 in highest shell). R_work/R_free 21.8/23.5. Average B-factors: PAR1 40.6 A^2, T4 lysozyme 53.5 A^2, <a href="/xray-mp-wiki/reagents/ligands/vorapaxar/">Vorapaxar</a> 30.5 A^2, water 46.4 A^2, lipids 69.1 A^2. Ramachandran favored 97.5%, allowed 2.5%, outliers 0.
</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Vorapaxar binding pocket architecture

The ligand-binding pocket of PAR1 is closed with only small openings to the extracellular solvent and the lipid bilayer. Four aromatic residues form strong interactions with [Vorapaxar](/xray-mp-wiki/reagents/ligands/vorapaxar/): Y183^3.33, F271^5.39, Y337^6.59, and Y353^7.35. A crystallographic sodium ion is present near D148^2.50, consistent with the conserved sodium-binding site in class A GPCRs. ECL2 forms a lid over the [Vorapaxar](/xray-mp-wiki/reagents/ligands/vorapaxar/) binding pocket, stabilized by hydrogen bonds between H255 and N242, Y353^7.35, and between D256 and Y95 in the amino terminus.

### Ligand-induced structural stability

Molecular dynamics simulations demonstrate that the PAR1 binding pocket collapses upon removal of [Vorapaxar](/xray-mp-wiki/reagents/ligands/vorapaxar/). In unliganded simulations, the extracellular end of TM6 moves inward toward TM4, and ECL3 comes into contact with ECL2. This collapse does not occur in simulations of PAR1 with [Vorapaxar](/xray-mp-wiki/reagents/ligands/vorapaxar/) bound, or in simulations of the unliganded mu-opioid receptor. The observation that [Vorapaxar](/xray-mp-wiki/reagents/ligands/vorapaxar/) inhibition is poorly reversible in platelets and requires protein synthesis for recovery in Cos7 cells is consistent with an off-rate that is slow compared to the duration of the experiment.

### PAR1 selectivity determinants

[Vorapaxar](/xray-mp-wiki/reagents/ligands/vorapaxar/) is selective for human PAR1 over human [Human Protease-Activated Receptor 2 (PAR2) - Stabilized T4L Fusion](/xray-mp-wiki/proteins/gpcr/par2/), PAR4, and mouse PAR1. Sequence alignment of ECL3 reveals that Y337 and Y353 are conserved in human PAR1 but differ in [Human Protease-Activated Receptor 2 (PAR2) - Stabilized T4L Fusion](/xray-mp-wiki/proteins/gpcr/par2/) and PAR4. Different conformations of ECL3 may affect the positions of Y337 and Y353 residues and thus compromise [Vorapaxar](/xray-mp-wiki/reagents/ligands/vorapaxar/) binding, explaining the species and subtype selectivity of this antagonist.

### Structural comparison with other GPCRs

The PAR1 ligand-binding site is closer to the extracellular surface than in beta2-adrenergic receptor (PDB 2RH1) and M2 muscarinic receptor (PDB 3UON). The [S1P1](/xray-mp-wiki/proteins/gpcr/s1p1/) structure (PDB 3V2Y) shows a lipid-embedded ligand with a wide opening to the lipid bilayer, contrasting with the closed, spherical pocket of PAR1. The mu-opioid receptor (PDB 4DKL) has a well solvent-exposed ligand-binding pocket. These comparisons highlight the diversity of ligand access mechanisms among class A GPCRs.


## Cross-References

- <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4 Lysozyme (T4L)</a> — T4L fusion inserted into ICL3 (between A301 and A303) for PAR1 crystallization
- <a href="/xray-mp-wiki/reagents/ligands/vorapaxar/">Vorapaxar</a> — Co-crystallized functionally irreversible antagonist in PDB 4MB0
- <a href="/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/">Human Beta2-Adrenergic Receptor (beta2 AR)</a> — Structural comparison; ligand-binding site position differs from PAR1
- <a href="/xray-mp-wiki/proteins/gpcr/s1p1/">Sphingosine-1-Phosphate Receptor 1 (S1P1)</a> — Structural comparison; S1P1 has lipid-embedded ligand with wide membrane access
- <a href="/xray-mp-wiki/proteins/gpcr/m2-muscarinic-acetylcholine-receptor/">Human M2 Muscarinic Acetylcholine Receptor</a> — Structural comparison; M2R ligand-binding site position differs from PAR1
- <a href="/xray-mp-wiki/proteins/gpcr/m3-muscarinic-acetylcholine-receptor/">M3 Muscarinic Acetylcholine Receptor</a> — GPCR crystallized using T4L fusion into ICL3 for structure determination
- <a href="/xray-mp-wiki/proteins/gpcr/par2/">Human Protease-Activated Receptor 2 (PAR2) - Stabilized T4L Fusion</a> — PAR2 shares 36% sequence identity with PAR1; structural comparison in Cheng et al. 2017
