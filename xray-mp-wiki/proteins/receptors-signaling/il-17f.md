---
title: "Interleukin-17F (IL-17F)"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.immuni.2020.02.004]
verified: regex
uniprot_id: Q96PD4
---

# Interleukin-17F (IL-17F)

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span> <span class="expr-badge expr-mammalian">Mammalian</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q96PD4">UniProt: Q96PD4</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

IL-17F is a secreted cytokine and a member of the IL-17 cytokine family. It forms homodimers and plays a key role in innate and adaptive immune responses, contributing to chronic inflammatory and autoimmune disorders. IL-17F shares structural homology with [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) but has distinct receptor binding properties. Unlike [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/), IL-17F forms a symmetrical 2:1 complex with [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) (two receptor chains per cytokine homodimer), competing with the shared co-receptor [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) for cytokine binding. IL-17F can also form heterodimers with [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) ([IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/)/F). The crystal structure of IL-17F in complex with [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) revealed that [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) binding preserves the two-fold symmetry of the cytokine, while [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) binding induces large conformational changes that break symmetry.


## Publications

### doi/10.1016##j.immuni.2020.02.004

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hgo">6HGO</a></td>
      <td>not specified</td>
      <td>not specified</td>
      <td>Human IL-17F, residues 31-163 of UniProt entry Q96PD4, fused to the Myeloid cell surface antigen CD33 signal peptide, with C-terminal APP6-tag (synthetic peptide EFRHDS derived from human Amyloid Precursor Protein) for crystallization
</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hg4">6HG4</a></td>
      <td>3.3 A</td>
      <td>P321</td>
      <td>Human IL-17F homodimer in complex with <a href="/xray-mp-wiki/proteins/receptors-signaling/il-17rc/">IL-17RC</a> ECD (residues 21-467)
</td>
      <td><a href="/xray-mp-wiki/proteins/receptors-signaling/il-17rc/">IL-17RC</a> (2 chains)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hg9">6HG9</a></td>
      <td>not specified</td>
      <td>R32</td>
      <td>Human IL-17F homodimer in complex with <a href="/xray-mp-wiki/proteins/receptors-signaling/il-17rc/">IL-17RC</a> ECD (residues 21-467)
</td>
      <td><a href="/xray-mp-wiki/proteins/receptors-signaling/il-17rc/">IL-17RC</a> (2 chains)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S cells (human embryonic kidney cells deficient in N-acetylglucosaminyl-transferase I)

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
      <td>Co-expression</td>
      <td>Transient co-expression in HEK293S cells</td>
      <td>--</td>
      <td>V3 medium (Novartis medium, patent WO 2011/134920 A1) + --</td>
      <td>Co-expression of <a href="/xray-mp-wiki/proteins/receptors-signaling/il-17a/">IL-17A</a> and IL-17F led to production of <a href="/xray-mp-wiki/proteins/receptors-signaling/il-17a/">IL-17A</a>, IL-17F, and <a href="/xray-mp-wiki/proteins/receptors-signaling/il-17a/">IL-17A</a>/F heterodimer; cells grown to 3 x 10^6 cells/mL
</td>
    </tr>
    <tr>
      <td>Supernatant collection</td>
      <td>Supernatant harvesting</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Supernatant collected from transfected HEK293S cells; IL-17F expressed as secreted protein with CD33 signal peptide and APP6-tag
</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> and SEC</td>
      <td>--</td>
      <td>-- + --</td>
      <td>IL-17F purified from supernatant; concentrated to 16.5 mg/mL in PBS pH 7.3 for crystallization
</td>
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
      <td>Unliganded IL-17F at 16.5 mg/mL in PBS pH 7.3
</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a>, 20% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew in sitting drops; nearly isomorphous to published structure (Hymowitz et al., 2001); structure determined by rigid-body refinement using PDB entry 1JPY
</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>IL-17F:<a href="/xray-mp-wiki/proteins/receptors-signaling/il-17rc/">IL-17RC</a>(21-467) complex at 5.1-5.7 mg/mL in PBS pH 7.4, 10 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>
</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350, 0.2 M ammonium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> tribasic pH 7.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Stepwise transfer to mother solution containing 40% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 1500, flash-cooling in liquid nitrogen
</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal form I, space group P321, diffracted to 3.3 A resolution
</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>IL-17F:<a href="/xray-mp-wiki/proteins/receptors-signaling/il-17rc/">IL-17RC</a>(21-467) complex at 5.1-5.7 mg/mL in PBS pH 7.4, 10 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>
</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350, 0.2 M <a href="/xray-mp-wiki/reagents/additives/ammonium-formate/">Ammonium Formate</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Stepwise transfer to mother solution containing 40% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 1500, flash-cooling in liquid nitrogen
</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal form II, space group R32
</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### IL-17F forms a symmetrical 2:1 complex with IL-17RC

IL-17F binds symmetrically to two [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) receptor chains, forming a 2:1 complex. This contrasts with the expected 1:1 asymmetric complex with [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/). [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) binding preserves the two-fold symmetry of the cytokine and does not shift the beta-hairpins, while [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) binding induces large conformational changes that break the symmetry of the IL-17F homodimer.

### IL-17F has three binding sub-sites (S1-S3)

Three main binding sub-sites on IL-17F (S1-S3) are exploited by both [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) and [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/). S1 is a hydrophobic site bound by Leu47 and Leu49 of [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) (or Leu58 and Trp62 of [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/)). S2 involves interactions with Tyr132 of [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) R2. S3 includes a buried salt-bridge between Asp281 of [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) and Arg77F. The binding sites overlap extensively between [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) and [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/).

### IL-17F can signal through IL-17RC independently of IL-17RA

The symmetrical [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/):IL-17F complex provides a structural basis for IL-17RA-independent signaling. IL-17F signaling through [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) induced il33 gene expression in mouse lung epithelial cells in vivo under conditions of [IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) disruption, suggesting homodimeric [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) signaling complexes can function independently.

### IL-17F has lower biological activity than IL-17A

The much lower biological activity of IL-17F compared to [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) may be a consequence of its poor ability to drive formation of significant amounts of the heteromeric [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/):[IL-17RA](/xray-mp-wiki/proteins/receptors-signaling/il-17ra/) complex. [TR-FRET](/xray-mp-wiki/methods/quality-assessment/tr-fret/) assays showed IL-17F requires approximately 250-fold higher concentrations than [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) to achieve a similar [TR-FRET](/xray-mp-wiki/methods/quality-assessment/tr-fret/) signal.


## Cross-References

- <a href="/xray-mp-wiki/proteins/receptors-signaling/il-17rc/">Interleukin-17 Receptor C (IL-17RC)</a> — Primary receptor forming symmetrical 2:1 complex with IL-17F
- <a href="/xray-mp-wiki/proteins/receptors-signaling/il-17ra/">Interleukin-17 Receptor A (IL-17RA)</a> — Shared co-receptor that forms asymmetric 1:1 complex with IL-17F
- <a href="/xray-mp-wiki/proteins/receptors-signaling/il-17a/">Interleukin-17A (IL-17A)</a> — Related cytokine in the IL-17 family; can form heterodimer with IL-17F
- <a href="/xray-mp-wiki/concepts/homodimeric-signaling/">Homodimeric Signaling</a> — IL-17F drives homodimeric IL-17RC signaling complex
- <a href="/xray-mp-wiki/concepts/competitive-receptor-binding/">Competitive Receptor Binding</a> — IL-17F binding to IL-17RC competes with IL-17RA binding
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> — PEG 3350 used as precipitant in crystallization
- <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate/">Ammonium Sulfate</a> — Precipitant used for unliganded IL-17F crystallization
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/quality-assessment/tr-fret/">TR-FRET</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/ammonium-formate/">Ammonium Formate</a> — Additive used in purification or crystallization buffers
