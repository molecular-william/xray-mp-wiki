---
title: "EspG1"
created: 2026-05-27
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jsb.2015.06.003]
verified: agent
uniprot_id: I6X486
---

# EspG1


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/I6X486">UniProt: I6X486</a>

<span class="expr-badge">Mycobacterium tuberculosis</span>

## Overview

EspG1 is the ESX-1-specific chaperone from Mycobacterium tuberculosis that belongs to the EspG chaperone family. EspG chaperones mediate the secretion of PE-PPE proteins and other ESX substrates by binding to a conserved motif on the PPE domain and protecting the heterodimer from self-polymerization. EspG1 is specific to the ESX-1 secretion system, while other EspG paralogs (EspG3, EspG5) are specific to ESX-3 and ESX-5 respectively. EspG1 does not bind [EspB](/xray-mp-wiki/proteins/espB), distinguishing EspB from canonical PE-PPE heterodimers that require EspG chaperones for folding and stability.


## Publications

### doi/10.1016##j.jsb.2015.06.003

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4kxr">4KXR</a></td>
      <td>Not specified</td>
      <td>Not specified</td>
      <td>EspG5 in complex with PE25-<a href="/xray-mp-wiki/proteins/ppe41">PPE41</a> heterodimer</td>
      <td>PE25-<a href="/xray-mp-wiki/proteins/ppe41">PPE41</a> heterodimer</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4w4l">4W4L</a></td>
      <td>Not specified</td>
      <td>Not specified</td>
      <td>EspG5 in complex with PE25-<a href="/xray-mp-wiki/proteins/ppe41">PPE41</a> heterodimer</td>
      <td>PE25-<a href="/xray-mp-wiki/proteins/ppe41">PPE41</a> heterodimer</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Not specified in this paper
- **Construct**: EspG1 expressed in E. coli for pull-down experiments with [EspB](/xray-mp-wiki/proteins/espB)

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
      <td>Expression and purification</td>
      <td>Not specified</td>
      <td>--</td>
      <td>-- + --</td>
      <td>EspG1 expressed in E. coli for pull-down experiments with <a href="/xray-mp-wiki/proteins/espB">EspB</a>; detailed purification described in Korotkova et al. (2014) Mol Microbiol</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Not specified in this paper</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>EspG5-PE25-<a href="/xray-mp-wiki/proteins/ppe41">PPE41</a> complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
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
      <td>Structures of EspG5-PE25-<a href="/xray-mp-wiki/proteins/ppe41">PPE41</a> complex described in Korotkova et al. (2014) Mol Microbiol and Ekiert and Cox (2014) PNAS 111:14758-14763</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### EspG1 does not bind EspB

Pull-down experiments using EspG1 expressed in E. coli showed no binding to either full-length or mature isoforms of [EspB](/xray-mp-wiki/proteins/espB). This is consistent with the structural observation that EspB lacks the hh motif (residues D121-T129) on the PPE domain that mediates EspG binding. Unlike canonical PE-PPE heterodimers, EspB has evolved as a PE-PPE fusion that no longer requires EspG chaperones for folding or stability.

### EspG chaperones protect PE-PPE heterodimers from self-polymerization

EspG chaperones bind to a conserved motif on the PPE domain, protecting the hydrophobic regions of PE-PPE heterodimers from self-polymerization. EspG chaperones are implicated in the folding, stability, and targeting of PE-PPE heterodimers to their cognate ESX secretion machinery. The EspG5-PE25-[PPE41](/xray-mp-wiki/proteins/ppe41) complex structure revealed that EspG binds specifically to the hh motif on PPE41, with the chaperone interacting with a relatively conserved motif on the PPE protein.

### EspG chaperone specificity is ESX-system-specific

Different EspG chaperones are specific to different ESX systems: EspG1 for ESX-1, EspG3 for ESX-3, and EspG5 for ESX-5. This specificity ensures that PE-PPE heterodimers are targeted to the correct secretion machinery. EspG chaperones have been implicated in the folding and stability of PE-PPE heterodimers and in targeting them to the cognate ESX machinery.


## Cross-References

- <a href="/xray-mp-wiki/proteins/secretion-translocon/pe25/">PE25</a> — EspG chaperones bind the PE25-[PPE41](/xray-mp-wiki/proteins/ppe41) heterodimer to protect it from self-polymerization
- <a href="/xray-mp-wiki/proteins/secretion-translocon/ppe41/">PPE41</a> — EspG chaperones bind the hh motif on [PPE41](/xray-mp-wiki/proteins/ppe41) for heterodimer folding and secretion
- <a href="/xray-mp-wiki/proteins/secretion-translocon/espB/">EspB</a> — [EspB](/xray-mp-wiki/proteins/espB) does not bind EspG1, unlike canonical PE-PPE heterodimers
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/esx-1-secretion-system/">ESX-1 Secretion System</a> — EspG1 is the ESX-1-specific chaperone for PE-PPE protein secretion
- <a href="/xray-mp-wiki/concepts/construct-design/pe-ppe-fusion-proteins/">PE-PPE Fusion Proteins</a> — EspG1 chaperones are not required for PE-PPE fusion proteins like [EspB](/xray-mp-wiki/proteins/espB)
