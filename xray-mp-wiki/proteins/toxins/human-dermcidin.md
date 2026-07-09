---
title: "Human Dermcidin (DCD) Antimicrobial Channel"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein]
sources: [doi/10.1073##pnas.1214739110]
verified: regex
---

# Human Dermcidin (DCD) Antimicrobial Channel


## Overview

Dermcidin (DCD) is a human antimicrobial host-defense peptide that forms transmembrane channels to disrupt bacterial membranes. Its X-ray crystal structure reveals a hexameric channel architecture composed of zinc-connected trimers of antiparallel helix pairs. The channel has a unique barrel-stave-like architecture with six lateral openings (eyelets) that allow ions to enter sideways. DCD channels exhibit a conductance of ~80-110 pS and are anion-selective. The structure and functional mechanism were elucidated through a combination of X-ray crystallography, solid-state NMR spectroscopy, electrophysiology, and molecular dynamics simulations, providing a foundation for structure-based design of peptide antibiotics.


## Publications

### doi/10.1073##pnas.1214739110

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/not in raw text">NOT IN RAW TEXT</a></td>
      <td>not specified</td>
      <td>—</td>
      <td>Full-length DCD peptide (synthetic)</td>
      <td>Zn2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Chemically synthesized peptide (>97% purity, Peptide2.0)


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
      <td>Peptide synthesis</td>
      <td>Chemical synthesis</td>
      <td>—</td>
      <td></td>
      <td>DCD peptide synthesized by Peptide2.0 at >97% purity</td>
    </tr>
    <tr>
      <td>Preparation for crystallization</td>
      <td>Dissolved in buffer</td>
      <td>—</td>
      <td>10 mM HEPES</td>
      <td>50 mg/mL (~10 mM) peptide in 10 mM HEPES</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>DCD peptide at 50 mg/mL in 10 mM HEPES</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M Zn(ac)2, 0.1 M Na-<a href="/xray-mp-wiki/reagents/buffers/cacodylate/">Cacodylate (Sodium Dimethylarsenate)</a>, 18% PEG8000, pH 6.5</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1 (400 nL peptide + 400 nL reservoir)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>100 K (cryo)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>None (flash-frozen from mother liquor)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized in absence of detergents or lipids; crystals flash-frozen in liquid nitrogen without cryoprotectant</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Zn2+-dependent channel formation

Zinc ions are essential for DCD channel formation. The structure
reveals Zn2+ ions coordinated by Glu5, Glu9, His38', and Asp42' at
the dimer interfaces. Zn2+ neutralizes the anionic charge of DCD
peptides (from -12e to neutral) and stabilizes the hexameric
assembly. MD simulations show that removal of Zn2+ compromises the
membrane-channel character. Electrophysiology confirms that H38A
mutation abolishes channel formation.

### Unique ion permeation pathway through lateral eyelets

DCD exhibits an unusual ion-permeation pathway. Through channel tilt
(~30° from membrane normal), ions enter sideways through six lateral
openings (eyelets, ~1 nm diameter) at the trimeric interfaces. This
shortens the ion pathway across the channel and exploits increased
ion concentration at lipid head groups. Anion traversal involves
single-ion "hopping" in the inner pore and multi-ion "knock-on"
effects at channel termini, expelling clusters of 3-4 anions.

### Barrel-stave mechanism for antimicrobial action

DCD represents a structurally characterized barrel-stave-like
antimicrobial channel. Unlike the carpet or toroidal pore models
proposed for many AMPs, DCD forms a defined hexameric channel with
high conductance (~80-110 pS). A single channel can dissipate the
bacterial transmembrane potential on a time scale of ~10^-4 s.
The structure provides the first comprehensive atomic-level
mechanism for membrane perturbation by a human antimicrobial peptide.

### DCD adopts multiple states depending on environment

DCD exists in a complex equilibrium of states: monomers and
oligomers in solution, monomers or small oligomers lying parallel to
the membrane surface, and transmembrane channels. Transmembrane
voltage and Zn2+ favor the membrane-spanning oligomeric state.
Solid-state NMR shows that the majority of DCD aligns in-plane with
the membrane in the absence of voltage, while electrophysiology
captures the minor but functionally relevant channel-forming
population.


## Cross-References

- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Used for DCD peptide preparation (10 mM HEPES)
- <a href="/xray-mp-wiki/reagents/buffers/cacodylate/">Cacodylate (Sodium Dimethylarsenate)</a> — Used in crystallization reservoir (0.1 M Na-cacodylate, pH 6.5)
