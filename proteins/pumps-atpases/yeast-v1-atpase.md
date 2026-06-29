---
title: "Yeast V1-ATPase from Saccharomyces cerevisiae"
created: 2026-06-09
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.15252##embj.201593447]
verified: false
---

# Yeast V1-ATPase from Saccharomyces cerevisiae

## Overview

V-type ATPase (V-ATPase) is a rotary ATPase complex that couples ATP hydrolysis to proton
pumping across cellular membranes. In Saccharomyces cerevisiae, the ~640 kDa V1 domain
(A3B3CDE3FG3H) catalyzes ATP hydrolysis and undergoes reversible dissociation from the
membrane-embedded Vo domain as a regulatory mechanism. Dissociated V1 is autoinhibited
to prevent wasteful ATP consumption. The X-ray crystal structure of the autoinhibited
yeast V1-ATPase was determined at 6.2-6.5 Å resolution, revealing the molecular mechanism
by which subunit H acts as a molecular brake. The structure shows that the C-terminal
domain of subunit H (HCT) undergoes a ~150° rotation from its position in the holoenzyme
to dock at the bottom of the catalytic hexamer, where it contacts the D subunit and the
open catalytic site, stabilizing an ADP-inhibited state.


## Publications

### doi/10.15252##embj.201593447

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5bw9">5BW9</a></td>
      <td>6.5 A</td>
      <td>Not stated in raw paper</td>
      <td>Yeast V1-ATPase (A3B3CDE3FG3H) from S. cerevisiae, C subunit deleted for homogeneity</td>
      <td>ADP (inhibitory nucleotide, ~1.3 mol/mol V1)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5d80">5D80</a></td>
      <td>6.2 A</td>
      <td>Not stated in raw paper</td>
      <td>Yeast V1-ATPase (A3B3CDE3FG3H) from S. cerevisiae, C subunit deleted for homogeneity</td>
      <td>ADP (inhibitory nucleotide)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae (native yeast strain)
- **Construct**: V1-ATPase complex consisting of A3B3CDE3FG3H subunits; C subunit (VMA5) deleted for homogeneous preparation

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
      <td>Expression</td>
      <td>Native expression in Saccharomyces cerevisiae</td>
      <td>—</td>
      <td>Not specified</td>
      <td>V1-ATPase purified from yeast strain deleted for the C subunit (VMA5) to ensure homogeneity; B subunit (VMA2) C-terminally tagged for affinity purification</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Capture</a> via tagged B subunit</td>
      <td>—</td>
      <td>Standard V-ATPase purification buffer</td>
      <td>Purified V1 from yeast cytoplasm; <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> precipitation and <a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography (SEC)</a></td>
      <td>—</td>
      <td>SEC buffer</td>
      <td>Final polishing step; V1 elutes as monodisperse ~600 kDa complex</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> / <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Variable (multiple datasets collected)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structure determined from multiple datasets. Initial 7 Å dataset from one crystal
used for <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> with EhA3B3 (Enterococcus hirae A3B3) as search model.
Higher resolution 6.2-6.5 Å datasets collected at APS and NSLS beamlines. Two
independent structures deposited: 5BW9 and 5D80. <a href="/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/">NCS</a> averaging and density modification
were essential for interpretable maps at this resolution.
</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Subunit H as a molecular brake

The C-terminal domain of subunit H (HCT) undergoes a ~150° rotation from its position
in the holo V1Vo complex to dock at the bottom of the V1 catalytic hexamer. In its
inhibitory position, HCT binds simultaneously to the D subunit (central rotor) and the
B subunit of the open catalytic site (AB)1, preventing rotation of the central stalk
and stabilizing an open conformation that traps inhibitory ADP at an adjacent closed site.

### Asymmetric peripheral stalk conformations

The three peripheral stalks (EG1, EG2, EG3) adopt different conformations in the
autoinhibited state. EG1 binds to the N-terminal domain of subunit H (HNT), while EG3
contacts the C-terminal domain of the A subunit at the (AB)2 closed catalytic site.
The EG3 stalk shows a partially disordered "bulge" region in subunit G that provides
flexibility for conformational changes during disassembly. The EG3 N-terminus,
which binds subunit C in the holoenzyme, moves to contact the A subunit C-terminal
domain in the autoinhibited V1.

### Subunit C deletion and purification strategy

Subunit C is released into the cytoplasm during V-ATPase disassembly but variably
co-purifies with V1 (from substoichiometric to significant amounts). Deletion of
subunit C (VMA5) was essential for a homogeneous preparation suitable for crystallization.
The resulting V1 shows no detectable MgATPase activity, confirming that subunit C is
not required for autoinhibition by subunit H.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/v1-atpase-t-thermophilus/">V1-ATPase from Thermus thermophilus</a> — Related bacterial V1-ATPase structure used for comparison of catalytic core and rotary mechanism
- <a href="/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/">Bovine F1-ATPase</a> — Related rotary ATPase; comparison of central rotor and catalytic mechanism
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/">NCS</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> — Additive used in purification or crystallization buffers
