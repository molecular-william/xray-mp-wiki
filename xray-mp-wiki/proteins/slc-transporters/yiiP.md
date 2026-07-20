---
title: "Escherichia coli Zinc Transporter YiiP"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1143748]
verified: agent
---

# Escherichia coli Zinc Transporter YiiP

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

YiiP is a Zn²⁺/H⁺ antiporter from the [Cation Diffusion Facilitator (CDF) Family](/xray-mp-wiki/concepts/protein-families/cation-diffusion-facilitator-family/)
that catalyzes zinc efflux across the inner membrane of Escherichia coli. It
forms a homodimer with a Y-shaped architecture: the two cytoplasmic domains
form the dimer interface through four Zn²⁺ ions, while the two transmembrane
domains swing outward. Each protomer contains six transmembrane helices and a
C-terminal cytoplasmic domain (CTD) with a metallochaperone-like fold. Mammalian
homologs (ZnT-3, ZnT-8) play critical roles in zinc homeostasis, neurotransmission,
and insulin secretion, and ZnT-8 is linked to type 2 diabetes pathogenesis.


## Publications

### doi/10.1126##science.1143748

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length YiiP with C-terminal His6 tag
- **Notes**: Endogenous expression inducible by Zn²⁺ and Fe²⁺. Transcription of yiiP gene is inducible by both metals.

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: Full-length YiiP

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
      <td>—</td>
      <td></td>
      <td>Native membrane vesicles used for transport measurement</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Multiple isomorphous replacement with anomalous scattering (<a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a>)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Zn²⁺ improved stability of YiiP in detergent micelles. 12 heavy-atom derivative crystals used for phasing. Resolution: 3.8 Å.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Y-shaped homodimer architecture

YiiP crystallizes as a homodimer with a distinctive Y-shaped structure.
The two CTDs form the dimer interface through four Zn²⁺ ions (Z2-Z4 sites)
at the cytoplasmic domain interface, while the TMDs swing outward. This
architecture is consistent with a YiiP projection map obtained in native
E. coli lipid bilayers.

### Transmembrane domain topology

Each protomer contains six transmembrane helices (TM1-TM6) arranged as
a compact six-helix bundle. Helix cross-interactions follow the
"knobs-into-holes" packing pattern. TM5 is conspicuously short (3.5 turns,
V147-M159), creating extracellular and intracellular cavities on either side
of the membrane. The extracellular cavity is accessible to bulk solvent and
anchors a Zn²⁺ ion (site Z1) near the bottom in tetrahedral coordination by
D45, D49, H153, and D157.

### Metallochaperone-like CTD fold

The C-terminal domain (residues 212-300) folds into an open αβ-domain with
two α-helices (H1, H2) and a three-stranded mixed β-sheet (S1-S3). This
fold superimposes onto the copper metallochaperone Hah1 with RMSD 1.8 Å
for 42 Cα positions, despite no sequence homology. The structural similarity
suggests the CTD may function as a Zn²⁺-receiving domain.

### Binuclear Zn²⁺ cluster at CTD dimer interface

Two Zn²⁺ ions (Z3, Z4) are coordinated within a cleft between CTDs through
a bidentate interaction with the highly conserved D285. The binuclear cluster
involves H232 (S1), H283, D285 (S3), and H261 (H2 of the neighboring subunit).
These clusters stabilize the dimer interface and are resistant to [EDTA](/xray-mp-wiki/reagents/additives/edta/) chelation.

### Zinc binding sites and transport mechanism

Four Zn²⁺-populated sites (Z1-Z4) per protomer were identified by anomalous
difference Fourier maps at the zinc edge. Site Z1 is the transport site with
tetrahedral coordination (D45, D49, H153, D157). Site Z2 (D68, H75) in IL1
contributes to subunit dimerization. Sites Z3-Z4 form binuclear clusters at
the CTD interface. The tetrahedral coordination geometry is selective for
Zn²⁺ and Cd²⁺ over Ca²⁺, Mg²⁺, Ni²⁺, Co²⁺, and Mn²⁺.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/cation-diffusion-facilitator-family/">Cation Diffusion Facilitator (CDF) Family</a> — YiiP is the founding structurally characterized CDF family member
- <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
