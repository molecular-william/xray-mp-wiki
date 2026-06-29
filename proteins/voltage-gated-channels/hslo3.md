---
title: "Human SLO3 (hSLO3) pH- and Voltage-Gated Potassium Channel"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein]
sources: [doi/10.1073##pnas.1215078109]
verified: false
---

# Human SLO3 (hSLO3) pH- and Voltage-Gated Potassium Channel

## Overview

hSLO3 (KCNU1) is a pH- and voltage-gated potassium channel from the SLO family, exclusively expressed in mammalian sperm. It is activated by intracellular alkalization and plays a critical role in male fertility. The channel features a transmembrane voltage sensor and a large cytoplasmic gating ring composed of tandem RCK (regulator of K+ conductance) domains. The gating ring acts as an intracellular pH sensor, and its crystal structure suggests an open conformation similar to the Ca2+-bound open state of the homologous SLO1 channel.


## Publications

### doi/10.1073##pnas.1215078109

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4hpf">4HPF</a></td>
      <td>3.30</td>
      <td>I222</td>
      <td>hSLO3 CTD residues 330-1062 with loop deletion (residues 831-851) - gating ring only</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus); CTD construct (residues 330-1062, loop deletion 831-851) fused to C-terminal PreScission-GFP-His10 tag


**Purification:**

- **Expression system**: Sf9 insect cells
- **Expression construct**: hSLO3 CTD (330-1062, loop del 831-851) with C-terminal PreScission-GFP-His10
- **Tag info**: C-terminal GFP-His10, removed by [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) (1:40 wt/wt, overnight)

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
      <td>Cell disruption</td>
      <td>Sonication</td>
      <td>—</td>
      <td>500 mM KCl, 50 mM K-phosphate, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, pH 8.0 (K-OH)</td>
      <td>Supplements: DNase and protease inhibitors</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Co2+ affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> (Clontech)</td>
      <td>500 mM KCl, 50 mM K-phosphate, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, pH 8.0</td>
      <td>Supplemented with 10 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>; incubated overnight with <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> to remove GFP-His10</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>Superose 6 (GE Life Sciences)</td>
      <td>500 mM KCl, 20 mM K-phosphate, 20 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>, 1.5 mM TCEP, pH 8.5 (K-OH)</td>
      <td>Protein concentrated to ~5 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>
**Final sample**: ~5 mg/mL in 500 mM KCl, 20 mM K-phosphate, 20 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/), 1.5 mM TCEP, pH 8.5
**Yield**: not specified
**Purity**: not specified

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (hanging drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>hSLO3 CTD (330-1062, loop deletion 831-851) at ~5 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM K-phosphate, 3% (wt/vol) PEG12000, 1 M <a href="/xray-mp-wiki/reagents/additives/ammonium-formate/">Ammonium Formate</a>, pH 6.3 (K-OH)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td><a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a> gradient (5%, 10%, 20%, 30% vol/vol) in cryoprotective solution (500 mM KCl, 70 mM K-phosphate, 4% PEG12000, 1 M <a href="/xray-mp-wiki/reagents/additives/ammonium-formate/">Ammonium Formate</a>, pH 6.4)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Final pH of mixed drop measured at 6.8. Crystals grew to 0.4 x 0.15 x 0.05 mm. Space group I222.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### pH gating of SLO3 channels

hSLO3 is activated by intracellular pH increase with pH50 of 7.7 at +180 mV (Hill coefficient 1.5). The channel shows lower expression levels compared to mouse SLO3 when expressed in Xenopus oocytes. Coexpression with the testis-specific accessory subunit LRRC52 increases functional expression, slows activation kinetics, and shifts pH dependence such that significant opening occurs even at low pH.

### Gating ring structure reveals potential open conformation

The crystal structure of the hSLO3 gating ring (3.3-3.8 A resolution) shows the tetrameric assembly of RCK1-RCK2 domains. Comparison with SLO1 gating ring structures (PDB 3U6N open, 3NAF closed) reveals that the hSLO3 RCK1 N-lobe layer closely matches the open SLO1 conformation (RMSD 2.7 A for N-lobe layer), while the closed SLO1 conformation aligns poorly. The hSLO3 gating ring diameter (94 A) matches the open SLO1 ring (93 A) rather than the closed ring (81 A), suggesting the crystallized hSLO3 gating ring represents an open state.

### Conservation of gating ring conformational change

The structural conservation of the RCK1 N-lobe layer between hSLO3 and SLO1 open states suggests that the conformational change in this region during gating ring opening is conserved across SLO family channels, despite the different activating signals (pH vs Ca2+). This implies a conserved mechanism where the RCK1 N-lobe layer acts as a mechanical transducer that pulls open the transmembrane pore.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slo1/">SLO1 BK Channel</a> — Homologous Ca2+-activated K+ channel; structural comparator for gating ring conformations
- <a href="/xray-mp-wiki/proteins/mslo3/">Mouse SLO3 (mSLO3)</a> — Mouse orthologue with similar pH sensitivity but higher functional expression
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/ammonium-formate/">Ammonium Formate</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Additive used in purification or crystallization buffers
