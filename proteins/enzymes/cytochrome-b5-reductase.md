---
title: "Cytochrome b5 Reductase"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2020.05.017]
verified: false
---

# Cytochrome b5 Reductase

## Overview

Cytochrome b5 reductase (b5R) is a membrane-embedded flavoprotein that catalyzes the transfer of electrons from [NADH](/xray-mp-wiki/reagents/cofactors/nadh) or NADPH to cytochrome b5. It consists of a single N-terminal transmembrane helix anchoring it to the endoplasmic reticulum membrane and a large soluble cytosolic domain composed of an N-terminal FAD-binding half and a C-terminal NAD(P)H-binding half. This paper reports the expression and purification of the soluble domain of mouse b5R for reconstitution of the SCD1 electron transfer chain in vitro.


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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1umk">1UMK</a></td>
      <td>not specified in this paper</td>
      <td>not specified</td>
      <td>Soluble cytosolic domain of mouse cytochrome b5 reductase</td>
      <td>FAD (flavin adenine dinucleotide)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli (pET vector)
- **Construct**: Mouse cytochrome b5 reductase soluble domain, N-terminally tagged with polyhistidine tag and TEV protease site

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
      <td>Cells supplemented with 100 uM FAD in media for flavin cofactor incorporation</td>
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
      <td>TEV protease cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> resin</td>
      <td>-- + --</td>
      <td>TEV protease cleaved His tag</td>
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

### Electron donor to cytochrome b5

Cytochrome b5 reductase reduces the heme group of cytochrome b5 using [NADH](/xray-mp-wiki/reagents/cofactors/nadh) or
NADPH as the electron donor. The NAD(P)H binds to the C-terminal half of the
soluble domain while FAD binds to the N-terminal half. Electron flow proceeds
from NAD(P)H to FAD to the b-type heme of cytochrome b5. In the SCD1 electron
transfer chain, b5R reduces cyt b5, which then donates electrons to SCD1 for
the desaturation reaction.

### In vitro reconstituted electron transfer chain

The soluble domains of b5R and cyt b5, together with SCD1 and NADH, form a
complete in vitro electron transfer chain capable of catalyzing the conversion
of [STEAROYL-COA](/xray-mp-wiki/reagents/ligands/stearoyl-coa) to oleoyl-CoA. The initial rate of oleoyl-CoA production yielded
Km = 6.3 +/- 1.2 uM and kcat = 2.78 +/- 0.59 min-1 for stearoyl-CoA. The rate
limiting step is the interaction between cyt b5 and SCD1.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/mouse-scd1/">Mouse Stearoyl-CoA Desaturase 1 (mSCD1)</a> — Terminal electron acceptor in the reconstituted electron transfer chain
- <a href="/xray-mp-wiki/proteins/enzymes/cytochrome-b5/">Cytochrome b5</a> — Direct electron acceptor from b5R; intermediate carrier to SCD1
- <a href="/xray-mp-wiki/reagents/cofactors/nadh/">NADH</a> — Primary electron donor for b5R
- <a href="/xray-mp-wiki/reagents/ligands/stearoyl-coa">STEAROYL-COA</a> — Reagent used in this study
- <a href="/xray-mp-wiki/reagents/cofactors/nadh">NADH</a> — Reagent used in this study
- <a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> — Reagent used in this study
