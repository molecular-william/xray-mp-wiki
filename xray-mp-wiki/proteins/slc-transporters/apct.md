---
title: "ApcT Amino Acid Transporter from Methanocaldococcus jannaschii"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1176088]
verified: regex
---

# ApcT Amino Acid Transporter from Methanocaldococcus jannaschii


## Overview

ApcT is a 435-amino acid amino acid transporter from the archaeon Methanocaldococcus jannaschii, belonging to the APC (Amino Acid-Polyamine-Organocation) superfamily. It functions as a sodium-independent, proton-coupled amino acid symporter with broad specificity for L-amino acids. The crystal structure was determined at 2.35 Å resolution using [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) SAD phasing, revealing an inward-facing occluded conformation with a [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/)-like fold consisting of 10 transmembrane helices arranged in an inverted repeat.


## Publications

### doi/10.1126##science.1176088

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/— (see supporting material)">— (SEE SUPPORTING MATERIAL)</a></td>
      <td>2.35</td>
      <td>—</td>
      <td>Full-length ApcT (residues 1-435)</td>
      <td>—</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/— (see supporting material)">— (SEE SUPPORTING MATERIAL)</a></td>
      <td>2.35</td>
      <td>—</td>
      <td>Full-length ApcT K158A mutant</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Screening of thermophilic orthologs by FSEC; ApcT from M. jannaschii selected for sharp symmetrical elution profile
- **Construct**: Full-length ApcT (435 residues)
- **Notes**: Expressed with anti-ApcT Fab fragment for stabilization

**Purification:**

- **Expression system**: [E. coli](/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/) (expression screening)
- **Expression construct**: Full-length ApcT
- **Tag info**: [His-tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (see supporting material)

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
      <td>Fluorescence detection <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">size exclusion chromatography</a> (FSEC)</td>
      <td>Screening of thermophilic orthologs</td>
      <td>—</td>
      <td>— + —</td>
      <td>Identified ApcT as promising candidate based on sharp symmetrical elution profile</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>— + n-octyl-beta-D-thioglucoside</td>
      <td>ApcT solubilized in n-octyl-beta-D-thioglucoside (OTG)</td>
    </tr>
    <tr>
      <td>Complex formation</td>
      <td>Fab fragment binding</td>
      <td>—</td>
      <td>— + —</td>
      <td>Complexed with anti-ApcT 7F11 Fab fragment for crystallization</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified ApcT in n-octyl-beta-D-thioglucoside
**Yield**: —
**Purity**: —

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a> (see supporting material)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>ApcT in n-octyl-beta-D-thioglucoside</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown at pH 9; ApcT alone diffracted to higher resolution than Fab complex</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Sodium-Independent Proton-Coupled Amino Acid Transport

ApcT is a sodium-independent, broad-specificity amino acid transporter active at acidic pH. Transport is coupled to a proton gradient, as shown by inhibition of transport when the pH gradient is collapsed by proton/potassium ionophores. Substrate uptake does not require sodium or a sodium gradient.

### Substrate Specificity and Binding Pocket

ApcT transports a wide range of L-amino acids (L-Glu, L-Ala, L-Ser, L-Gln, L-Phe) but transports Gly and Trp very slowly. The substrate binding pocket (~195 Å³) is large enough to accommodate phenylalanine but not tryptophan. The pocket is lined by polar, aromatic, and aliphatic residues from TMs 1, 3, 6, and 8, with hydrogen bonding interactions between substrate amino/carboxyl groups and main-chain carbonyl/amide moieties.

### Lys158 as Proton Sensor

Lys158 (TM5) is situated between TMs 1 and 8, forming hydrogen bonds to the main-chain carbonyl of Gly19 (TM1) and hydroxyl of Ser283 (TM8). Based on structural alignment with [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/), the amine of Lys158 superimposes on the Na2 ion of [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/). The K158A mutant showed no measurable transport activity, supporting the hypothesis that Lys158 undergoes reversible protonation/deprotonation during the transport cycle, acting as a proton sensor that modulates the conformation of TM1 and the opening/closing of extracellular and intracellular gates.

### Inward-Facing Occluded Conformation

The ApcT structure represents a substrate-free, inward-facing yet occluded conformation. Three lines of evidence support this: (1) a solvent-accessible path from the cytoplasmic side to Lys158; (2) TM1 conformation that occludes access to the outside but partially opens to the inside; (3) a belt of water molecules at the extracellular face with a solvent-free swath separating it from the putative substrate binding pocket. This apo conformation resembles the substrate-bound occluded state of [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/), demonstrating that occluded state formation does not require bound substrate.

### Structural Comparison with LeuT and AdiC

ApcT adopts the [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/)-like fold with two inverted repeats of five transmembrane helices. Structural superposition shows that ApcT aligns well with [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/), but less well with [V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)](/xray-mp-wiki/proteins/slc-transporters/vsglt/), [Mhp1 Benzyl-Hydantoin Transporter from Microbacterium liquefaciens](/xray-mp-wiki/proteins/slc-transporters/mhp1/), and [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/). Comparison with the [AdiC Arginine/Agmatine Antiporter](/xray-mp-wiki/proteins/slc-transporters/adic/) structure (PDB 3H5M) revealed significant discrepancies in TMs 6-8, suggesting the [AdiC Arginine/Agmatine Antiporter](/xray-mp-wiki/proteins/slc-transporters/adic/) sequence is off-register by ~4 residues in these regions.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/apc-superfamily/">APC Superfamily (Amino Acid-Polyamine-Organocation Transporter Family)</a> — ApcT is a member of the APC superfamily
- <a href="/xray-mp-wiki/proteins/enzymes/leut/">LeuT Amino Acid Transporter from Aquifex aeolicus</a> — LeuT shares the same structural fold and was used for structural comparison
- <a href="/xray-mp-wiki/proteins/slc-transporters/adic/">AdiC Arginine/Agmatine Antiporter</a> — AdiC is an APC superfamily member compared structurally to ApcT
- <a href="/xray-mp-wiki/proteins/slc-transporters/vsglt/">V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)</a> — vSGLT shares the LeuT-like fold and was compared in the structural analysis
- <a href="/xray-mp-wiki/proteins/slc-transporters/betp/">BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)</a> — BetP occluded conformation was compared to ApcT inward-facing occluded state
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — ApcT structure supports the alternating access model for secondary transporters
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocking-bundle-mechanism/">Rocking-Bundle Mechanism</a> — ApcT structural transitions are consistent with the rocking-bundle model
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Method used in the study
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/apc-superfamily/">APC Superfamily (Amino Acid-Polyamine-Organocation Transporter Family)</a> — Key concept related to this protein
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocking-bundle-mechanism/">Rocking-Bundle Mechanism</a> — Key concept related to this protein
