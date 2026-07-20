---
title: "MjCorA — CorA Mg2+ Transporter from Methanocaldococcus jannaschii"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, channel, membrane-protein]
sources: [doi/10.1073##pnas.1210076109]
verified: agent
---

# MjCorA — CorA Mg2+ Transporter from Methanocaldococcus jannaschii

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

CorA is the primary Mg2+ transport system in most prokaryotes and is conserved throughout the CorA family including eukaryotic homologs. The structure of MjCorA from Methanocaldococcus jannaschii was determined at 3.2 Å resolution, revealing the complete architecture including the conserved extraplasmic loop containing the signature GMN motif that functions as a selectivity filter. The structure shows a pentameric arrangement with two transmembrane helices per monomer. Polar residues facing the channel coordinate a partially hydrated Mg2+ during transport. A unique gating mechanism is proposed involving a helical turn upon Mg2+ binding to regulatory intracellular binding sites, converting a polar ion passage into a narrow hydrophobic pore.


## Publications

### doi/10.1073##pnas.1210076109

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ev6">4EV6</a></td>
      <td>3.20</td>
      <td>—</td>
      <td>Full-length MjCorA</td>
      <td>Mg2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Heterologous expression in Escherichia coli (strain not specified)


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
      <td>Protein purification</td>
      <td>Standard purification (details in SI)</td>
      <td>—</td>
      <td>HEPES-NaOH buffer with MgCl2 + Dodecyl-maltoside</td>
      <td>Full-length MjCorA purified in solubilization buffer containing dodecyl-maltoside</td>
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
      <td>Full-length MjCorA in solubilization buffer</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>30% PEG8000, HEPES-NaOH, 60 mM MgCl2</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized in 30% PEG8000, HEPES-NaOH, 60 mM MgCl2</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### GMN motif as selectivity filter

The conserved GMN (Gly-Met-Asn) motif in the extraplasmic loop forms
the selectivity filter of CorA. The Asn280 ring (N280-ring) creates a
narrow entry that allows only partially hydrated Mg2+ to pass. The
carbonyl groups of Gly278 attract ions, while Met279 anchors the
filter in a hydrophobic environment. The YGMNF and LPLA motifs create
a rigid scaffold maintaining the Asn-ring position. This arrangement
explains the strict conservation of the GMN motif across all CorA
family members including eukaryotic homologs.

### Helical turn gating mechanism

A unique gating mechanism is proposed where Mg2+ binding to
intracellular regulatory sites (the Mg2+-binding grooves at monomer
interfaces) induces a clockwise helical turn of helix 6. This
rotation moves polar residues away from the pore and replaces them
with hydrophobic residues, blocking the passage. In the open state,
the pore is polar and allows partially hydrated Mg2+ passage. The
gating converts a polar ion passage into a narrow hydrophobic pore
rather than using the iris-like sideways movement previously proposed
for TmCorA.

### Mg2+ transport as partially hydrated ion

The structure reveals that Mg2+ is taken up and transported as a
partially hydrated ion. The Asn280-ring replaces water molecules in
the second hydration shell. A wide internal cavity (~23 Å long)
allows the ion to potentially return to fully hydrated state after
passing the selectivity filter. The filter discriminates against
Ca2+ and Mn2+ based on differences in first hydration shell radii,
while allowing Mg2+, Co2+, and Ni2+ which have similar radii
(~2.05-2.1 Å).


## Cross-References

- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
