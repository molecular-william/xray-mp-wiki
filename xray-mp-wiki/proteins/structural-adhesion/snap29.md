---
title: "SNAP29 (Synaptosomal-Associated Protein 29)"
created: 2026-06-11
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, receptor]
sources: [doi/10.1073##pnas.2006997117]
verified: regex
uniprot_id: O95721
---

# SNAP29 (Synaptosomal-Associated Protein 29)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O95721">UniProt: O95721</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

SNAP29 is a Qbc-SNARE protein that provides both Qb- and Qc-SNARE motifs for the autophagic
SNARE core complex. Together with the Qa-SNARE [STX17](/xray-mp-wiki/proteins/structural-adhesion/syntaxin17/) and the R-SNARE [VAMP8 (Vesicle-Associated Membrane Protein 8)](/xray-mp-wiki/proteins/structural-adhesion/vamp8/), SNAP29 forms
the four-helix bundle that mediates autophagosome-lysosome fusion. SNAP29 contributes two
helices to the bundle (Qb residues 40-126, Qc residues 191-258) and the conserved glutamine
residues Q84 (Qb) and Q230 (Qc) that participate in the hydrophilic 0-layer.


## Publications

### doi/10.1073##pnas.2006997117

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7bv6">7BV6</a></td>
      <td></td>
      <td></td>
      <td>SNAP29 Qb-SNARE (40-126) and Qc-SNARE (191-258) in complex with <a href="/xray-mp-wiki/proteins/structural-adhesion/syntaxin17/">STX17</a> and <a href="/xray-mp-wiki/proteins/structural-adhesion/vamp8/">VAMP8 (Vesicle-Associated Membrane Protein 8)</a></td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Human SNAP29 Qb (40-126) and Qc (191-258) fragments
- **Notes**: Expressed with MBP or GB1 tags using in-house modified pET32a vectors. Induced with 100 uM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 16 C.


## Biological / Functional Insights

### SNAP29 provides Qb and Qc SNARE motifs for autophagic fusion

SNAP29 contributes two helices (Qb and Qc) to the four-helix SNARE bundle. The conserved
glutamine at the 0-layer differs between the two: Q84 in the Qb motif and Q230 in the Qc
motif. Mutagenesis of L213Q (layer -5 in Qc) and Q230L (0-layer in Qc) essentially abolished
SNARE core complex formation.


## Cross-References

- <a href="/xray-mp-wiki/proteins/structural-adhesion/syntaxin17/">Syntaxin17 (STX17)</a> — SNAP29 assembles with STX17 and VAMP8 to form the autophagic SNARE complex
- <a href="/xray-mp-wiki/proteins/structural-adhesion/vamp8/">VAMP8</a> — VAMP8 is the R-SNARE partner in the autophagic SNARE complex
- <a href="/xray-mp-wiki/concepts/construct-design/autophagic-snare-fusion-mechanism/">Autophagic SNARE Fusion Mechanism</a> — SNAP29 provides two of the four helices in the autophagic SNARE complex
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
