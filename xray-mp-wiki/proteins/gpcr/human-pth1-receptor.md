---
title: "Human Parathyroid Hormone 1 Receptor (PTH1R)"
created: 2026-06-16
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41594-018-0151-4]
verified: agent
uniprot_id: Q37979
---

# Human Parathyroid Hormone 1 Receptor (PTH1R)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span> <span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q37979">UniProt: Q37979</a>

<span class="expr-badge">Listeria phage A500</span>

## Overview

The human parathyroid hormone 1 receptor (PTH1R) is a class B G-protein-coupled receptor that mediates the actions of parathyroid hormone (PTH) and parathyroid hormone-related protein (PTHrP), playing a central role in calcium homeostasis and bone metabolism. PTH1R is a major drug target for osteoporosis and hypoparathyroidism. The high-resolution crystal structure of the engineered PTH1R (PTH1R_XTAL) in complex with an engineered peptide agonist (ePTH) was determined, revealing the detailed interactions between the receptor and its ligand. The construct included deletions in the extracellular domain (ECD) and C-terminus, a PGS fusion replacing ICL3, and 10 thermostabilizing mutations from directed yeast evolution.


## Publications

### doi/10.1038##s41594-018-0151-4

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6fj3">6FJ3</a></td>
      <td>3.00</td>
      <td>P 2_1 2_1 2_1</td>
      <td>PTH1R_XTAL (ECD-PTH1R_S-PGS fusion) with N-terminal HA signal, FLAG tag, His10 tag, 3C cleavage site; ECD deletion (61-104), C-term deletion (481-593), ICL3 (389-397) replaced by PGS fusion; 10 thermostabilising mutations from yeast evolution</td>
      <td>ePTH (engineered PTH peptide agonist)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda Sf9 insect cells (baculovirus) and HEK293T cells
- **Construct**: PTH1R_XTAL — melittin signal peptide, FLAG epitope, His10 tag, 3C protease cleavage site, ECD-PTH1R_S-PGS with ECD deletion (61-104), C-term deletion (481-593), ICL3 (389-397) replaced by PGS
- **Notes**: Directed evolution in S. cerevisiae followed by additional thermostabilising mutations

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
      <td>Cell culture</td>
      <td>Baculovirus infection of Sf9 cells</td>
      <td>—</td>
      <td></td>
      <td>Receptor expressed in Sf9 insect cells</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Homogenization and ultracentrifugation</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)](/xray-mp-wiki/reagents/additives/nickel-nta/) / <a href="/xray-mp-wiki/reagents/additives/talon/">talon</a> immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity-chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>His10 tag purification</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td>—</td>
      <td></td>
      <td>Final polishing step in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)-compatible buffer</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (lipid cubic phase)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PTH1R_XTAL-ePTH complex in buffer</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-7 days</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (monoolein-based); P2_1_2_1_2_1 space group; diffraction to ~3.0 A resolution</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### ePTH binding mode and peptide-receptor interactions

The crystal structure reveals that ePTH binds to PTH1R in a two-domain mode typical of class B GPCRs: the C-terminal helical region of ePTH (residues 15-34) interacts with the N-terminal extracellular domain (ECD), while the N-terminal region of ePTH (residues 1-14) inserts into the transmembrane helical bundle. Key interactions include hydrogen bonds between ePTH residues (Ac5c1, Aib3, E4, Hrg11, N16) and PTH1R residues (Q364^5.40, Y429^ECL3, M441^7.39, E444^7.42, Y195^1.47, R233^2.60, F288^3.36, N448^7.46), as well as hydrophobic contacts mediated by I5, L7, M8, W14, and V21. The engineered substitutions in ePTH (Ac5c1, Aib3, Q10, Hrg11, A12, W14, Nle18, Y34) increase peptide stability and binding affinity.

### Conserved W352 in ECL2 adopts distinct orientation

In the PTH1R-ePTH complex, the conserved tryptophan W352 in extracellular loop 2 (ECL2) adopts a distinct orientation compared to other class B GPCR structures (GCGR, GLP1R). Instead of positioning between TM3 and TM4, W352 packs against the peptide ligand, contributing to the orthosteric binding pocket. This unique orientation is defined by clear side chain electron density and contributes to ligand binding specificity.

### R440 stabilising mutation reduces receptor activation

The stabilising mutation R440^7.38 (Q440 in wild-type PTH1R) forms an extended hydrogen bonding network that includes E444^7.42 and the backbone oxygen of F424^6.56 at the extracellular end of helix VI. This additional hydrogen bond stabilises the top of helix VI in an inactive-like state, explaining why the Q440R mutation strongly reduces receptor activation while largely retaining ligand binding. This provides structural insight into the activation mechanism requiring conformational rearrangements at the extracellular end of helix VI.

### Jansen Metaphyseal Chondrodysplasia mutations affect HETX motif

Jansen's metaphyseal chondrodysplasia is caused by constitutively activating mutations in PTH1R. The conserved class B HETX motif (H409^6.41, E410^6.42, T411^6.43, X412^6.44) is located at the cytoplasmic end of helix VI. In the active state, T^6.42 is removed from the network due to rearrangements in TM6. The thermostabilising mutation I458^7.56A together with disease-associated I458^7.56R face toward S409^6.41 near the HETX motif. The bulky arginine sidechain of I458R clashes with helix VI in the inactive state, providing a structural rationale for constitutive activation.

### Glycosylation at N161 near the peptide binding site

The crystal structure resolved glycosylation (GlcNAc and fucose) at residue N161 of the PTH1R ECD, located in close proximity to the ePTH C-terminus. The amidated C-terminus of Y34 forms hydrogen bonds with T163 of PTH1R, rationalizing the increased binding affinity of C-terminally amidated PTH peptides. The N161D mutation showed similar binding to wild-type PTH1R (IC50 11.0 vs 13.0 nM), indicating that glycosylation at this site is not essential for ligand binding.


## Cross-References

- <a href="/xray-mp-wiki/concepts/signaling-receptors/polar-network-gpcr-activation/">Polar Network in GPCR Activation</a> — The HETX motif is a conserved polar network in class B GPCRs critical for activation
- <a href="/xray-mp-wiki/concepts/signaling-receptors/constitutive-active-gpcr-mutations/">Constitutive Active GPCR Mutations</a> — Jansen metaphyseal chondrodysplasia mutations cause constitutive PTH1R activation
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/">GPCR Active Conformation</a> — PTH1R-ePTH complex represents an active-state class B GPCR
- <a href="/xray-mp-wiki/concepts/construct-design/thermostabilization/">Thermostabilization</a> — Directed yeast evolution and additional mutations stabilized PTH1R for crystallization
