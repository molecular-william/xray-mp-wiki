---
title: "Human Alpha-1B Adrenergic Receptor (alpha1B AR)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-27911-3]
verified: agent
---

# Human Alpha-1B Adrenergic Receptor (alpha1B AR)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

The human alpha-1B adrenergic receptor (alpha1B AR, ADRA1B) is a class A G protein-coupled receptor that mediates physiological responses to the endogenous catecholamines [Epinephrine](/xray-mp-wiki/reagents/ligands/epinephrine/) and [Norepinephrine](/xray-mp-wiki/reagents/ligands/norepinephrine/). It plays key roles in cardiovascular function, CNS signaling, and immune regulation. The crystal structure of alpha1B AR bound to the inverse agonist (+)-cyclazosin was determined at 2.87 A resolution (anisotropy-corrected, PDB 7B6W), enabled by CHESS-based directed evolution for stabilization and a [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 crystallization chaperone. The structure revealed a canonical GPCR fold with two unique secondary binding pockets. Structural comparison with alpha2 ARs and construction of alpha1B-alpha2C chimeras identified residues 3.29 and 6.55 as key determinants of ligand selectivity. The structure provides a template for rational design of alpha1B AR-selective ligands and for understanding off-target binding of aminergic drugs.


## Publications

### doi/10.1038##s41467-021-27911-3

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7b6w">7B6W</a></td>
      <td>2.87 A (anisotropy-corrected from 3.1 A)</td>
      <td>Not specified in paper</td>
      <td>Human alpha1B AR with 12 stabilizing mutations from CHESS directed evolution, N-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> (residues 1-34 deleted), ICL3 deletion (residues K249-L283 deleted), and C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/darpin/">Designed Ankyrin Repeat Protein (DARPin)</a> D12 crystallization chaperone fused via AEDLVEDWE linker; expressed in E. coli
</td>
      <td>(+)-Cyclazosin (inverse agonist)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli (inner membranes)
- **Construct**: alpha1B AR_XTAL: N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) M1-N34 deleted, ICL3 K249-L283 deleted, 12 stabilizing mutations from directed evolution, [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 fused at C-terminus via AEDLVEDWE linker


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
      <td>Membrane preparation</td>
      <td>Cell lysis and membrane isolation</td>
      <td>--</td>
      <td>Hypotonic buffer with protease inhibitors + --</td>
      <td>Cells harvested and lysed; membranes isolated by centrifugation</td>
    </tr>
    <tr>
      <td>Solubilization and purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity-chromatography</a></td>
      <td>Ligand-affinity column (cleavable prazosin analog)</td>
      <td>PBS-E (1.8 mM KH2PO4, 137 mM NaCl, 2.7 mM KCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, pH 7.4) + <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (<a href="/xray-mp-wiki/reagents/detergents/dm/">dm</a>) / CHAPS / <a href="/xray-mp-wiki/reagents/detergents/dhpc/">DHPC</a></td>
      <td>Receptor solubilized in <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>/CHAPS, incubated with QAPB fluorescent ligand, purified using cleavable ligand column strategy. Further details in Schuster et al. BBA Biomembr. 2020.
</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) (inferred - standard for GPCR crystallography)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified alpha1B AR_XTAL in complex with (+)-cyclazosin</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified in paper</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified in paper</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified in paper</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structure determined at 3.1 A (processed to 2.87 A with STARANISO anisotropy correction). Data collected at synchrotron. Molecular replacement using turkey beta1 AR (PDB 6IBL) and <a href="/xray-mp-wiki/reagents/protein-tags/darpin/">Designed Ankyrin Repeat Protein (DARPin)</a> D12 (PDB 5LW2) as search models.
</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Two unique secondary binding pockets identified

The (+)-cyclazosin ligand adopts an inverted L-shaped binding mode. The dimethoxyquinazoline moiety occupies the orthosteric binding site (OBS). The cis-decahydroquinoxaline moiety sits at the boundary between OBS and a secondary pocket defined by TM3 and ECL2. The furan-2-yl-methanone moiety is accommodated in secondary binding pockets proximal to the extracellular surface, making (+)-cyclazosin a bitopic ligand.

### Residues 3.29 and 6.55 as key determinants of ligand selectivity

Using structural comparison of alpha1B AR with alpha2 ARs and construction of alpha1B-alpha2C chimeras, residues A122(3.29) and L314(6.55) were identified as key determinants of ligand selectivity. The quadruple mutant alpha1B-alpha2C(YLLY) (W121Y, A122L, V197L, L314Y) showed nearly three orders of magnitude improved affinity for the alpha2-selective antagonist RS79948. Position 3.29 (Ala in alpha1, Leu in alpha2) modulates the distinct selectivity profiles of yohimbine and corynanthine. ECL2 in alpha2 ARs is postulated to sterically hinder binding of bulky piperazinyl quinazoline ligands.

### DARPin crystallization chaperone strategy

The receptor was stabilized using CHESS-based directed evolution in E. coli and fused to a [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 crystallization chaperone at the C-terminus replacing helix 8. This same strategy was previously used for NTSR1 structures. The [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) was modified with N-terminal deletions and point mutations for optimized crystal packing. [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) D12-mediated crystal contacts enabled structure determination of this previously recalcitrant GPCR.


## Cross-References

- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Method used in the study
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Key concept related to this protein
- <a href="/xray-mp-wiki/reagents/protein-tags/darpin/">Designed Ankyrin Repeat Protein (DARPin)</a> — Key concept related to this protein
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/reagents/detergents/dhpc/">1,2-Dihexanoyl-sn-glycero-3-phosphocholine (DHPC)</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl beta-D-glucopyranoside (OG)</a> — Detergent used in purification
- <a href="/xray-mp-wiki/reagents/detergents/dm/">n-Decyl-beta-D-Maltoside (DM)</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/buffers/tes/">TES Buffer (N-Tris(hydroxymethyl)methyl-2-aminoethanesulfonic acid)</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/additives/edta/">Ethylenediaminetetraacetic Acid (EDTA)</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/ligands/epinephrine/">Epinephrine</a> — Reagent used in the study
