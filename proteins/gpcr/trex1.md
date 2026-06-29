---
title: "Mouse TREX1 (Three Prime Repair Exonuclease 1)"
created: 2026-06-11
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1093##nar##gkad910]
verified: false
---

# Mouse TREX1 (Three Prime Repair Exonuclease 1)

## Overview

TREX1 (Three prime repair exonuclease 1) is a crucial mammalian enzyme consisting of an N-terminal nuclease domain and a C-terminal transmembrane domain. It acts as a 3'-to-5' exonuclease in the cytoplasm and nucleus, anchored at the endoplasmic reticulum (ER) membrane under normal conditions, where it degrades endogenous DNA to prevent nucleic acid-mediated immune activation. Dysfunction of TREX1 leads to accumulation of cytosolic nucleic acids and autoimmune diseases including Aicardi-Goutieres syndrome (AGS), systemic lupus erythematosus (SLE), and familial chilblain lupus (FCL). TREX1 is a member of the [DEDDh Exonuclease Family](/xray-mp-wiki/concepts/protein-families/deddh-exonuclease-family/) and adopts a general two-metal ion mechanism for catalysis. This paper establishes that TREX1 can digest single-stranded RNA (ssRNA) and DNA/RNA hybrids but not double-stranded RNA (dsRNA), through a combination of nuclease activity assays, X-ray crystallography, and all-atom molecular dynamics simulations.

## Publications

### doi/10.1093##nar##gkad910

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8hcc">8HCC</a></td>
      <td>2.0</td>
      <td>P12(1)1</td>
      <td>mTREX1 (amino acids 11-242) with RNA product (AMP)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8hcd">8HCD</a></td>
      <td>2.0</td>
      <td>P12(1)1</td>
      <td>mTREX1 (amino acids 11-242) with DNA product (dGMP)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8hce">8HCE</a></td>
      <td>1.5</td>
      <td>P2(1)2(1)2(1)</td>
      <td>mTREX1 (amino acids 11-242) with CMP</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8hcf">8HCF</a></td>
      <td>1.6</td>
      <td>P2(1)2(1)2(1)</td>
      <td>mTREX1 (amino acids 11-242) with UMP</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8hcg">8HCG</a></td>
      <td>1.8</td>
      <td>P3(2)21</td>
      <td>mTREX1 (amino acids 11-242) with dAMP</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8hch">8HCH</a></td>
      <td>2.0</td>
      <td>P12(1)1</td>
      <td>mTREX1 (amino acids 11-242) with uridine</td>
      <td></td>
    </tr>
  </tbody>
</table>


## Biological / Functional Insights

### TREX1 functions as an RNase with approximately half the activity of its DNase activity

Nuclease activity assays established that mTREX1 digests ssRNA at approximately half the rate of ssDNA. TREX1 can also process the RNA strand in DNA/RNA hybrids, but with lower activity than ssRNA degradation. No activity is observed against dsRNA even at 25-fold excess enzyme concentration.

### 2'-OH does not impose steric hindrance in the active site

Crystal structures of mTREX1 complexed with ribonucleotides (AMP, CMP, UMP) and deoxyribonucleotides (dGMP, dAMP) show that the 2'-OH group in RNA interacts with Gly23, Ala21, and Tyr129 through hydrogen bonds without causing steric hindrance. The binding positions of deoxyribonucleotides and ribonucleotides are nearly identical.

### Intra-chain hydrogen bonding in RNA reduces TREX1 binding affinity

All-atom MD simulations (2 microsecond production runs) revealed that 2'-OH-mediated intra-chain hydrogen bonding in RNA increases conformational rigidity, reducing the strength of TREX1-RNA interactions. Fluorescence anisotropy measurements confirmed that ssDNA has higher binding affinity (Kd = 77.7 nM) than ssRNA (Kd ~58,973 nM) for TREX1.

### TREX1 processes DNA/RNA hybrids with efficiency similar to dsDNA

DNA/RNA hybrids are processed by TREX1 with efficiency comparable to dsDNA digestion. HMGB-2 enhances TREX1 activity against dsDNA and DNA/RNA hybrids but does not enable dsRNA digestion. This suggests that DNA/RNA hybrids are natural substrates of TREX1 in cellular contexts.


## Cross-References

- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/trex1-rnase-activity/">TREX1 RNase Activity</a> — This paper establishes the molecular basis of TREX1's RNase activity
- <a href="/xray-mp-wiki/concepts/protein-families/deddh-exonuclease-family/">DEDDh Exonuclease Family</a> — TREX1 is a member of the DEDDh family
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
