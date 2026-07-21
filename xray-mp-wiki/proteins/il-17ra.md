---
title: "Interleukin-17 Receptor A (IL-17RA)"
created: 2026-05-27
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.immuni.2020.02.004]
verified: agent
uniprot_id: Q96F46
---

# Interleukin-17 Receptor A (IL-17RA)

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span> <span class="expr-badge expr-mammalian">Mammalian</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q96F46">UniProt: Q96F46</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

IL-17RA is the founding and best-known member of the interleukin-17 receptor (IL-17R) family. It is a single-pass type I transmembrane glycoprotein that serves as the shared receptor for several members of the IL-17 cytokine family, including [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/), [IL-17F](/xray-mp-wiki/proteins/receptors-signaling/il-17f/), and [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/)/F. IL-17RA was traditionally believed to operate in concert with [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) to mediate IL-17 signaling. However, structural analysis revealed that [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) and IL-17RA compete for the same binding surface on [IL-17F](/xray-mp-wiki/proteins/receptors-signaling/il-17f/). IL-17RA has a shorter extracellular domain compared to [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) and is classified as a "short receptor." It contains a cytoplasmic SEFIR domain for intracellular signaling.


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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3jvf">3JVF</a></td>
      <td>not specified</td>
      <td>not specified</td>
      <td>Human IL-17RA extracellular domain (referenced structure from Ely et al., 2009; the numbering in the PDB differs from UniProt Q96F46 by +31)
</td>
      <td><a href="/xray-mp-wiki/proteins/receptors-signaling/il-17f/">IL-17F</a></td>
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
      <td>Protein expression</td>
      <td>Transient expression in HEK293S cells</td>
      <td>--</td>
      <td>V3 medium (Novartis medium, patent WO 2011/134920 A1) + --</td>
      <td>Full-length IL-17RA ECD (residues 33-320 of UniProt entry Q96F46) fused to CD33 signal peptide and C-terminal APP4-tag, cloned into pRS5-derived vector
</td>
    </tr>
    <tr>
      <td>SEC purification</td>
      <td>Size-exclusion chromatography</td>
      <td>--</td>
      <td>-- + --</td>
      <td>IL-17RA purified by SEC; used for <a href="/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/">ITC</a> and <a href="/xray-mp-wiki/methods/quality-assessment/sec-mals/">SEC-MALS</a> experiments
</td>
    </tr>
  </tbody>
</table>


## Biological / Functional Insights

### IL-17RA competes with IL-17RC for IL-17F binding

IL-17RA forms an asymmetric 1:1 complex with [IL-17F](/xray-mp-wiki/proteins/receptors-signaling/il-17f/) (one IL-17RA chain per [IL-17F](/xray-mp-wiki/proteins/receptors-signaling/il-17f/) homodimer), while [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) binds symmetrically on both sides forming a 2:1 complex. The footprints of [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) and IL-17RA on [IL-17F](/xray-mp-wiki/proteins/receptors-signaling/il-17f/) overlap extensively, with both receptors interacting with the same three binding sub-sites (S1-S3). [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) blocks the IL-17RA binding site, paradoxically competing with its co-receptor for cytokine binding.

### IL-17RA induces conformational changes in IL-17F

Upon binding IL-17RA, the cytokine undergoes large conformational changes that break the two-fold symmetry of the [IL-17F](/xray-mp-wiki/proteins/receptors-signaling/il-17f/) homodimer. The first beta-hairpin shifts outward by approximately 3 A, and the second beta-hairpin of the same [IL-17F](/xray-mp-wiki/proteins/receptors-signaling/il-17f/) subunit is pushed up to approximately 13 A outward by the IL-17RA R1 motif. In contrast, [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) binding preserves the symmetry of the cytokine.

### IL-17RA is a short receptor

IL-17RA has a short extracellular domain compared to [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/). The last 17 amino acid residues of the IL-17RA ECD before the predicted transmembrane segment (304-PEMPDTPEPIPDYMPPLW-320) were disordered in all published X-ray analyses. In contrast, [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/) is classified as a tall receptor with extended D3-D4 stalk domains.

### IL-17A drives heteromeric complex formation more efficiently than IL-17F

In the presence of both IL-17RA and [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/), [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) readily drives formation of the heteromeric [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/):IL-17RA:[IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) complex. [IL-17F](/xray-mp-wiki/proteins/receptors-signaling/il-17f/) preferentially forms a symmetrical complex with [IL-17RC](/xray-mp-wiki/proteins/receptors-signaling/il-17rc/), requiring approximately 250-fold higher concentrations than [IL-17A](/xray-mp-wiki/proteins/receptors-signaling/il-17a/) in [TR-FRET](/xray-mp-wiki/methods/quality-assessment/tr-fret/) assays to achieve a similar signal.


## Cross-References

- <a href="/xray-mp-wiki/proteins/receptors-signaling/il-17rc/">Interleukin-17 Receptor C (IL-17RC)</a> — Co-receptor that competes with IL-17RA for cytokine binding
- <a href="/xray-mp-wiki/proteins/receptors-signaling/il-17f/">Interleukin-17F (IL-17F)</a> — Cytokine that forms asymmetric 1:1 complex with IL-17RA
- <a href="/xray-mp-wiki/proteins/receptors-signaling/il-17a/">Interleukin-17A (IL-17A)</a> — Cytokine that efficiently drives heteromeric IL-17RC:IL-17RA:IL-17A complex
- <a href="/xray-mp-wiki/concepts/tall-receptor/">Tall Receptor</a> — IL-17RA classified as a short receptor, contrasting with tall IL-17RC
- <a href="/xray-mp-wiki/concepts/competitive-receptor-binding/">Competitive Receptor Binding</a> — IL-17RA and IL-17RC compete for the same binding surface on IL-17F
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> — Related precipitant used in crystallization
- <a href="/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/">ITC</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/quality-assessment/sec-mals/">SEC-MALS</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/quality-assessment/tr-fret/">TR-FRET</a> — Method used in structure determination or purification
