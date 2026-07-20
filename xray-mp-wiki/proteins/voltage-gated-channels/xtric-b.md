---
title: "XTRIC-B (Xenopus TRIC-B Channel)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1817271116]
verified: agent
---

# XTRIC-B (Xenopus TRIC-B Channel)

<div class="expr-badges"><span class="expr-badge expr-s-cerevisiae">S. cerevisiae</span></div>


## Overview

XTRIC-B is the Xenopus tropicalis ortholog of the TRIC-B subtype of trimeric intracellular cation (TRIC) channels. TRIC-B synchronizes with inositol 1,4,5-trisphosphate receptors (IP3Rs) to mediate Ca2+ release from intracellular stores. XTRIC-B shares 48% sequence identity with [GgTRIC-A (Chicken Trimeric Intracellular Cation Channel A)](/xray-mp-wiki/proteins/voltage-gated-channels/ggtric-a/), 46% with human HsTRIC-A, and 54% with human HsTRIC-B. The structure was determined at 3.1 A resolution by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using the [GgTRIC-A (Chicken Trimeric Intracellular Cation Channel A)](/xray-mp-wiki/proteins/voltage-gated-channels/ggtric-a/) structure.


## Publications

### doi/10.1073##pnas.1817271116

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6iyu">6IYU</a></td>
      <td>3.1</td>
      <td></td>
      <td>Xenopus XTRIC-B, full-length</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6iyu">6IYU</a></td>
      <td></td>
      <td></td>
      <td>Xenopus XTRIC-B, Ca2+-free state</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Schizosaccharomyces pombe (yeast)
- **Construct**: Full-length XTRIC-B with codon optimization
- **Notes**: Gene synthesized with codon optimization for S. pombe expression; identified as stable candidate for structural and functional characterization

**Purification:**

- **Expression system**: Schizosaccharomyces pombe
- **Expression construct**: Full-length XTRIC-B

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
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td>20 mM HEPES pH 7.5, 150 mM KCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.06% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a></td>
      <td>Solubilized in octyl glucose-neopentyl glycol (<a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a>) amphiphiles; purification similar to <a href="/xray-mp-wiki/proteins/voltage-gated-channels/ggtric-a/">GgTRIC-A (Chicken Trimeric Intracellular Cation Channel A)</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified XTRIC-B in 20 mM HEPES pH 7.5, 150 mM KCl, 0.06% <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Multiple conditions (see SI Appendix Table S2)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized in multiple lattices. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using <a href="/xray-mp-wiki/proteins/voltage-gated-channels/ggtric-a/">GgTRIC-A (Chicken Trimeric Intracellular Cation Channel A)</a> as search model. Structures determined in both Ca2+-bound and Ca2+-free states at resolutions down to 3.1 A.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Conserved TRIC architecture across subtypes

XTRIC-B adopts the same overall fold as [GgTRIC-A (Chicken Trimeric Intracellular Cation Channel A)](/xray-mp-wiki/proteins/voltage-gated-channels/ggtric-a/), with an rmsd of 0.92 A for 221 superimposed C-alpha atoms of the protomer and 1.14 A for 665 superimposed C-alpha atoms of the trimer. Both share similar topological organization, trimeric assembly architecture, and surface electrostatic characteristics with prokaryotic TRICs and invertebrate TRICs from C. elegans. The transmembrane helices are more inclined within the membrane compared to prokaryotic TRICs and adopt a more expanded conformation.

### TRIC-B as a counter-ion channel for IP3R-mediated Ca2+ release

TRIC-B functionally couples with IP3Rs (rather than RyRs) to mediate intracellular Ca2+ release. Purified XTRIC-B reconstituted into planar lipid bilayers conducts K+ currents with characteristics similar to those of mammalian TRIC-B, validating the structural studies as representative of functional TRIC-B channels.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/ggtric-a/">GgTRIC-A (Chicken TRIC-A)</a> — Vertebrate TRIC-A subtype used as molecular replacement model; high sequence identity (48%) and conserved architecture
- <a href="/xray-mp-wiki/reagents/lipids/dag/">Diacylglycerol (DAG)</a> — Lipid identified at protomer interfaces in TRIC channels; DAG binds at lateral fenestrations
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ogng/">OGNG</a> — Detergent used in purification or crystallization
