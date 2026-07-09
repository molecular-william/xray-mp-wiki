---
title: "SNAP-25A (Rat Neuronal Qbc-SNARE Protein)"
created: 2026-06-02
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature08156]
verified: regex
---

# SNAP-25A (Rat Neuronal Qbc-SNARE Protein)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

SNAP-25A (Synaptosomal-Associated Protein of 25 kDa, isoform A) is a neuronal Qbc-SNARE protein from rat that anchors to the plasma membrane via palmitoyl chains bound to cysteine residues in a loop region connecting its two SNARE motifs. SNAP-25A provides two of the four helices in the neuronal SNARE complex: one from each of its two SNARE motifs. It plays an essential role in synaptic vesicle fusion by assembling with [Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)](/xray-mp-wiki/proteins/syntaxin-1a) and [Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)](/xray-mp-wiki/proteins/synaptobrevin-2) into a stable four-helix bundle that drives membrane merger during neurotransmitter release.


## Publications

### doi/10.1038##nature08156

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/tba">TBA</a></td>
      <td>3.4 A</td>
      <td>C2</td>
      <td>Rat SNAP-25A (residues 7-83, 141-204; all cysteines replaced by serines) in complex with syntaxin-1A and synaptobrevin-2, including linkers and TMRs</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BI21 (DE3)
- **Construct**: Rat SNAP-25A (residues 7-83, 141-204) with all cysteines replaced by serines, expressed from pET28a. Full-length version with C-to-S mutations also used for circular dichroism experiments.

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
      <td>Protein expression</td>
      <td>Expression in E. coli BI21 (DE3) from pET28a</td>
      <td>--</td>
      <td>-- + --</td>
      <td>His-tagged SNAP-25A expressed separately</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Ni-NTA agarose</td>
      <td>-- + --</td>
      <td>Initial purification of His-tagged SNAP-25A</td>
    </tr>
    <tr>
      <td>Complex assembly</td>
      <td>In vitro complex assembly</td>
      <td>--</td>
      <td>Assembled by overnight incubation of monomers at 4 C + --</td>
      <td>SNAP-25A (C-to-S mutant) assembled with <a href="/xray-mp-wiki/proteins/syntaxin-1a">Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)</a> and <a href="/xray-mp-wiki/proteins/synaptobrevin-2">Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)</a> monomers for CD and crystallization experiments</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion in n-nonyl beta-D-glucopyranoside</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Syntaxin-1A/SNAP-25A/synaptobrevin-2 complex with SNAP-25A (residues 7-83, 141-204, C-to-S mutant), linkers and TMRs</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in main text</td>
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
      <td>SNAP-25A provides two helices to the four-helix bundle SNARE complex. All cysteines replaced by serines to prevent aberrant disulfide formation.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Two-SNARE-motif architecture

SNAP-25A uniquely provides two of the four alpha-helices in the neuronal SNARE complex, with each SNARE motif contributing one helix. The two SNARE motifs are connected by a loop region containing palmitoylation sites (cysteine residues) that anchor the protein to the plasma membrane.

### Palmitoyl membrane anchoring

SNAP-25A is anchored to the plasma membrane by palmitoyl chains bound to cysteine residues in the loop connecting its two SNARE motifs. This dual membrane anchoring (via palmitoyl chains rather than a transmembrane domain) positions SNAP-25A to participate in the SNARE complex at the plasma membrane.

### Cysteine-to-serine mutations for structural studies

All cysteine residues in SNAP-25A were replaced by serines to prevent aberrant disulfide bond formation during structural studies. This mutation did not affect the protein's ability to assemble into the SNARE complex for CD and crystallization experiments.


## Cross-References

- <a href="/xray-mp-wiki/proteins/structural-adhesion/syntaxin-1a/">Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)</a> — Qa-SNARE partner; assembles with SNAP-25A and synaptobrevin-2 into four-helix bundle
- <a href="/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/">Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein)</a> — Qc-SNARE partner; assembles with SNAP-25A and syntaxin-1A into four-helix bundle
- <a href="/xray-mp-wiki/reagents/detergents/nonylglucoside/">Nonylglucoside (NG)</a> — n-nonyl beta-D-glucopyranoside used as detergent for crystallization
- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl beta-D-glucopyranoside (OG)</a> — n-octyl beta-D-glucopyranoside used in purification buffer for SNARE complex assembly
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/snare-complex/">SNARE Complex</a> — SNAP-25A provides two helices to the four-helix bundle SNARE complex
