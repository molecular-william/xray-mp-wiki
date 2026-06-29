---
title: "PPE41"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jsb.2015.06.003]
verified: false
---

# PPE41

## Overview

PPE41 is the conserved N-terminal domain of the PPE (Pro-Pro-Glu) protein family from Mycobacterium tuberculosis. PPE41 forms a heterodimer with [PE25](/xray-mp-wiki/proteins/secretion-translocon/pe25/) through a four-helix bundle interface, creating an elongated all-helical structure characteristic of ESX-secreted substrates. The PPE41 protein contains a characteristic hh motif (residues D121-T129) that serves as the binding site for EspG chaperones. PPE41 is secreted by the ESX-1 type VII secretion system as part of the PE25-PPE41 heterodimer and is essential for mycobacterial virulence.


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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2g38">2G38</a></td>
      <td>2.0 A</td>
      <td>Not specified</td>
      <td>PE25-PPE41 heterodimer (N-terminal domains only, lacking C-terminal regions)</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4kxr">4KXR</a></td>
      <td>Not specified</td>
      <td>Not specified</td>
      <td>PE25-PPE41-EspG5 complex</td>
      <td>EspG5 chaperone</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4w4l">4W4L</a></td>
      <td>Not specified</td>
      <td>Not specified</td>
      <td>PE25-PPE41-EspG5 complex</td>
      <td>EspG5 chaperone</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Not specified in this paper
- **Construct**: PPE41 N-terminal domain as part of PE25-PPE41 heterodimer

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
      <td>Not specified</td>
      <td>Not specified</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Purification details not described in this paper; original structure determined by Strong et al. (2006) PNAS 103:8060-8065</td>
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
      <td>PE25-PPE41 heterodimer</td>
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
      <td>Original crystallization described in Strong et al. (2006) PNAS 103:8060-8065</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### PPE41 contains the EspG chaperone-binding site

PPE41 contains a characteristic hh motif (residues D121-T129) that mediates binding to EspG chaperones. The EspG chaperone binds specifically to this conserved motif on PPE41, protecting the hydrophobic regions of the PE-PPE heterodimer from self-polymerization. EspG chaperones are essential for PE-PPE heterodimer folding, stability, and targeting to the cognate ESX secretion machinery. The alpha4-alpha5 loop of PPE proteins, which contains the hh motif, is highly conserved in length and sequence among PPE family members.

### PPE41 contributes helices to the PE-PPE heterodimer bundle

In the PE25-PPE41 heterodimer, PPE41 contributes two alpha-helices to the four-helix bundle interface. Helix alpha1 of PPE41 corresponds to helix alpha3 of the related [EspB](/xray-mp-wiki/proteins/secretion-translocon/espB/) protein. The conserved Trp56 (W56) of PPE41 makes van der Waals contacts with Y87 of [PE25](/xray-mp-wiki/proteins/secretion-translocon/pe25/) in the heterodimer interface. The length and sequence of the alpha4-alpha5 loop of PPE proteins are highly conserved, distinguishing them from the variable corresponding region in [EspB](/xray-mp-wiki/proteins/secretion-translocon/espB/) homologs.

### YxxxD/E secretion motif in PE25-PPE41 complex

The YxxxD/E secretion motif is present in [PE25](/xray-mp-wiki/proteins/secretion-translocon/pe25/) (part of the PE-PPE heterodimer). In the isolated heterodimer structures (PDB 2G38, 4W4K), the motif is partially disordered. However, in the PE25-PPE41-EspG5 complex structures (PDB 4KXR, 4W4L), the motif adopts a helical conformation, suggesting that chaperone binding stabilizes the secretion-competent conformation.


## Cross-References

- <a href="/xray-mp-wiki/proteins/secretion-translocon/pe25/">PE25</a> — PPE41 forms the heterodimer partner of PE25 in the canonical PE-PPE complex
- <a href="/xray-mp-wiki/proteins/secretion-translocon/espB/">EspB</a> — EspB structure structurally resembles the PE25-PPE41 heterodimer despite being a single-chain fusion
- <a href="/xray-mp-wiki/concepts/construct-design/pe-ppe-fusion-proteins/">PE-PPE Fusion Proteins</a> — PPE41 is the PPE domain component of the canonical PE-PPE heterodimer architecture
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/esx-1-secretion-system/">ESX-1 Secretion System</a> — PPE41 is a secreted substrate of the ESX-1 type VII secretion system as part of PE25-PPE41
- <a href="/xray-mp-wiki/proteins/secretion-translocon/espg1/">EspG1</a> — EspG chaperones bind the hh motif on PPE41 for heterodimer folding and secretion
