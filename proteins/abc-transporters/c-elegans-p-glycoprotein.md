---
title: "C. elegans P-glycoprotein (P-gp)"
created: 2026-06-02
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11448]
verified: false
---

# C. elegans P-glycoprotein (P-gp)

## Overview

P-glycoprotein (P-gp) from Caenorhabditis elegans is an [ATP](/xray-mp-wiki/reagents/ligands/atp/)-binding cassette (ABC) transporter that functions as a multidrug efflux pump. It belongs to the P-gp/MDR subfamily of ABC transporters and confers cellular resistance to a wide range of cytotoxic drugs including actinomycin D, [Paclitaxel](/xray-mp-wiki/reagents/ligands/paclitaxel/), and [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/). P-gp is a primary active transporter that uses [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis to extrude hydrophobic compounds from cells, playing a critical role in multidrug resistance. The C. elegans P-gp structure was solved by X-ray crystallography at 3.4 A resolution, providing the first high-resolution view of an ABC transporter in a nucleotide-free conformation. The protein is N-glycosylated at residue N125 and expresses as a functional full-length protein when produced in Sf9 insect cells.


## Publications

### doi/10.1038##nature11448

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4mq1">4MQ1</a></td>
      <td>3.4</td>
      <td>P212121</td>
      <td>C. elegans P-glycoprotein, full-length, N125 glycosylated</td>
      <td>None (nucleotide-free)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Baculovirus expression in Sf9 insect cells
- **Construct**: Full-length C. elegans P-glycoprotein with GFP tag on C-terminus for expression monitoring

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
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus expression</a> in <a href="/xray-mp-wiki/methods/expression-systems/sf9-expression-system/">Sf9</a> cells</td>
      <td>--</td>
      <td>Not specified + Not specified</td>
      <td>P-gp expression monitored by <a href="/xray-mp-wiki/reagents/protein-tags/gfp/">GFP</a> fluorescence fused to C-terminus</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>Not specified + Not specified</td>
      <td>Not specified in supplementary information</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/gfp/">GFP</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/gfp-trap/">GFP-Trap</a></td>
      <td>Not specified + Not specified</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/gfp/">GFP</a>-tagged P-gp purified using <a href="/xray-mp-wiki/reagents/protein-tags/gfp-trap/">GFP-Trap beads</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a> (<a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a>)</td>
      <td>--</td>
      <td>Not specified + Not specified</td>
      <td>Final polishing step; <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> used for sample homogeneity assessment</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>C. elegans P-glycoprotein, nucleotide-free</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
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
      <td>Notes</td>
      <td>Space group P212121, unit cell a=96.8, b=155.3, c=162.4 Angstroms. Structure determined by <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">SeMet</a> SAD and Hg anomalous diffraction. Resolution 3.4 A, Rwork/Rfree 24.9/28.2.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Drug resistance function

C. elegans P-gp confers cellular resistance to cytotoxic drugs. Sf9 cells expressing P-gp show protection from drug-induced cytotoxicity by actinomycin D (12 hours exposure) and [Paclitaxel](/xray-mp-wiki/reagents/ligands/paclitaxel/) (48 hours exposure), correlated with P-gp membrane expression monitored by GFP fluorescence. The protein functions as a broad-spectrum multidrug efflux pump.

### ATPase activity and drug stimulation

P-gp exhibits basal ATPase activity that is stimulated by drug substrates. Multiple compounds including [Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/), [Valinomycin](/xray-mp-wiki/reagents/ligands/valinomycin/), and trifluoperazine stimulate ATPase activity in detergent-solubilized P-gp, confirming their role as P-gp substrates. The drug concentration dependence of ATPase stimulation provides functional evidence for drug transport activity.

### N-glycosylation site resolved by anomalous diffraction

The N-glycosylation site at residue N125 was resolved using anomalous difference Fourier maps. [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) and [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) anomalous diffraction data (contoured at 4 sigma) enabled direct visualization of the attached oligosaccharide, confirming the glycosylation state of the crystallized protein.

### Transmembrane register shifts vs. mouse P-gp

Comparison with mouse P-gp (PDB 3G5U) reveals register shifts in transmembrane helices TM3, TM4, and TM5. Region of TM3 (residues 184-200) shifted by one amino acid, entire TM4 helix (residues 217-251) shifted by four amino acids, and TM5 shifted by three amino acids. These shifts highlight sequence divergence between C. elegans and mouse P-gp despite structural conservation.

### N-terminal truncation mutant

A [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) mutant lacking the N-terminal 56 residues (Delta56) confers cellular resistance to actinomycin D and [Paclitaxel](/xray-mp-wiki/reagents/ligands/paclitaxel/) similarly to full-length P-gp, indicating the N-terminus is not essential for drug transport function. However, the [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) mutant shows reduced maximum drug-stimulated ATPase activity in detergent, suggesting the N-terminus modulates the enzymatic activity of the transporter.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/abcg2/">ABCG2</a> — ABC transporter G subfamily; multidrug efflux pump with similar drug resistance function
- <a href="/xray-mp-wiki/proteins/abc-transporters/abcg1/">ABCG1</a> — ABC transporter G subfamily member; lipid transporter with structural similarities
- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">AcrB multidrug efflux pump</a> — Multidrug efflux pump from E. coli; functional comparison with P-gp
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — P-gp is a member of the ABC (ATP-binding cassette) superfamily of transporters
- <a href="/xray-mp-wiki/reagents/antibiotics/actinomycin-d/">Actinomycin D</a> — P-gp substrate; tested for cellular resistance in P-gp-expressing cells
- <a href="/xray-mp-wiki/reagents/ligands/paclitaxel/">Paclitaxel</a> — P-gp substrate; antimitotic drug whose cellular toxicity is reversed by P-gp
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">AcrB multidrug efflux pump</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/abc-transporters/abcg2/">ABCG2</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/elic/">ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)</a> — Related protein structure
