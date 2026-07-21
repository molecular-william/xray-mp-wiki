---
title: "Cytochrome b5"
created: 2026-05-27
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2020.05.017]
verified: agent
uniprot_id: P00167
---

# Cytochrome b5

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P00167">UniProt: P00167</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Cytochrome b5 is a membrane-embedded electron transfer protein consisting of a soluble cytosolic domain and a single C-terminal transmembrane helix. The soluble domain contains a b-type heme group ligated by two axial histidine residues. In the endoplasmic reticulum, cytochrome b5 serves as the intermediate electron carrier between cytochrome b5 reductase and various downstream enzymes including [STEAROYL-COA](/xray-mp-wiki/reagents/ligands/stearoyl-coa) desaturase 1 (SCD1). This paper reports the expression and purification of the soluble domain of mouse cytochrome b5 for in vitro electron transfer studies.


## Publications

### doi/10.1016##j.jmb.2020.05.017

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2i96">2I96</a></td>
      <td>not specified in this paper</td>
      <td>not specified</td>
      <td>Soluble cytosolic domain of mouse cytochrome b5</td>
      <td>B-type heme (protoporphyrin IX with <a href="/xray-mp-wiki/reagents/additives/iron">IRON</a>)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli (pET vector)
- **Construct**: Mouse cytochrome b5 soluble domain, C-terminally tagged with polyhistidine tag and TEV protease site

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
      <td>Cell expression and lysis</td>
      <td>E. coli expression in pET vector with sonication</td>
      <td>--</td>
      <td>Buffer A (composition not fully specified) + --</td>
      <td>Cells supplemented with 0.5 mM delta-aminolevulinic acid, 5 uM FeCl3, and 1 uM hemin chloride for <a href="/xray-mp-wiki/reagents/ligands/heme">HEME</a> biosynthesis</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> cobalt-based affinity resin</td>
      <td>-- + --</td>
      <td>Polyhistidine tag captured on <a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> resin</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> resin</td>
      <td>-- + --</td>
      <td><a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease cleaved His tag</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Concentration</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Concentrated using 10 kDa cutoff concentrators</td>
    </tr>
  </tbody>
</table>


## Biological / Functional Insights

### Electron transfer to SCD1

In the SCD1 electron transfer chain, reduced ferrous cytochrome b5 donates
electrons to SCD1, becoming oxidized. The oxidation of cyt b5 by SCD1 exhibits
a biphasic time course with rate constants k1 = 1.86 min-1 and k2 = 0.246 min-1,
as monitored by the decrease of the Soret peak at 423 nm. This interaction is
the rate-limiting step in the assembled electron transfer chain. The reaction
must be performed anaerobically to prevent auto-oxidation by molecular oxygen.

### Spectroscopic characterization

The soluble domain of cytochrome b5 exhibits characteristic spectroscopic
features confirming the presence of the b-type heme cofactor. The oxidized form
shows a Soret peak at 413 nm, which shifts to 423 nm upon reduction. Reduction
is achieved by cytochrome b5 reductase in the presence of [NADH](/xray-mp-wiki/reagents/cofactors/nadh). The heme is
ligated by two axial histidine residues, characteristic of b-type cytochromes.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/mouse-scd1/">Mouse Stearoyl-CoA Desaturase 1 (mSCD1)</a> — Direct electron acceptor; cyt b5 oxidized by SCD1
- <a href="/xray-mp-wiki/proteins/enzymes/cytochrome-b5-reductase/">Cytochrome b5 Reductase</a> — Reduces cytochrome b5 using NADH as electron donor
- <a href="/xray-mp-wiki/reagents/cofactors/nadh/">NADH</a> — Electron donor for cytochrome b5 reduction by b5R
- <a href="/xray-mp-wiki/reagents/cofactors/nadh">NADH</a> — Reagent used in this study
- <a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> — Reagent used in this study
- <a href="/xray-mp-wiki/reagents/ligands/heme">HEME</a> — Reagent used in this study
- <a href="/xray-mp-wiki/reagents/ligands/stearoyl-coa">STEAROYL-COA</a> — Reagent used in this study
- <a href="/xray-mp-wiki/reagents/additives/iron">IRON</a> — Reagent used in this study
