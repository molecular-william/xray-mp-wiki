---
title: "GltTk — substrate-free aspartate transporter"
created: 2026-06-11
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2663]
verified: agent
uniprot_id: Q9I5Q5
---

# GltTk — substrate-free aspartate transporter

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9I5Q5">UniProt: Q9I5Q5</a>

<span class="expr-badge">Pseudomonas aeruginosa</span>

## Overview

GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
a member of the glutamate transporter (SLC1/EAAT) family. The crystal structure
of substrate-free (apo) GltTk was determined at 3.0 A resolution, revealing the
transporter in an outward-open conformation with the two helical hairpin domains
(HP1 and HP2) occluding the binding site. The structure highlights the
conformational changes that occur upon substrate binding and provides insight
into the alternating-access mechanism of glutamate transporter homologs.


## Publications

### doi/10.1038##nsmb.2663

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ky0">4KY0</a></td>
      <td>3.0</td>
      <td>P3221</td>
      <td>Full-length GltTk</td>
      <td></td>
    </tr>
  </tbody>
</table>
 - R-work 21.2%, R-free 26.6%; Atoms: 9308

**Expression:**

- **Expression system**: Escherichia coli


## Biological / Functional Insights

### Substrate-free conformation of an aspartate transporter

The crystal structure of GltTk in the absence of aspartate reveals an
outward-open conformation. The two helical hairpin domains (HP1 and HP2)
occlude the central substrate-binding site, protecting it from the
extracellular and intracellular environments. Comparison with the
aspartate-bound structure of the homologous [Gltph](/xray-mp-wiki/proteins/slc-transporters/glt-ph/) (PDB 2NWL) shows that
substrate binding induces conformational changes, particularly in the
HP2 region, which closes over the binding pocket.

Key structural features include Arg401, which interacts with Asp398 in
transmembrane segment 8 (TMS8) and Val358 in HP2. These interactions are
important for stabilizing the substrate-free conformation. The B-factors
of the Arg401 side chain are elevated relative to the average side chain
B-factors, suggesting conformational flexibility.

### Sodium dependence of aspartate transport

Transport of [L Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) by GltTk is strictly dependent on sodium ions.
Isothermal titration calorimetry showed that aspartate binds only in the
presence of Na+. The transport rate is not dependent on a proton gradient,
confirming a sodium-coupled electrogenic mechanism. Purified GltTk is
devoid of both Na+ and aspartate, as demonstrated by ITC experiments.

### Trimeric architecture

Like other glutamate transporter homologs, GltTk forms a trimer. The
space group P3221 with cell dimensions a=b=117.57 A, c=309.51 A is
consistent with a trimeric assembly in the asymmetric unit. Each protomer
consists of eight transmembrane segments (TMS1-TMS8) and two helical
hairpin domains (HP1 and HP2).


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/glt-ph/">Gltph</a> — Referenced in glttk text
- <a href="/xray-mp-wiki/reagents/substrates/l-aspartate/">L Aspartate</a> — Referenced in glttk text
