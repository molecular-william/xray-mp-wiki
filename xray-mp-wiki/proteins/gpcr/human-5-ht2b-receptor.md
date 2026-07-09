---
title: "Human 5-HT2B Serotonin Receptor Bound to Ergotamine"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein]
sources: [doi/10.1126##science.1232808]
verified: regex
---

# Human 5-HT2B Serotonin Receptor Bound to Ergotamine

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


## Overview

The 5-HT2B receptor is a class A G protein-coupled receptor (GPCR) for [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands/serotonin/) (5-hydroxytryptamine) involved in cardiovascular function, CNS signaling, and valvular heart disease pathogenesis. This crystal structure captures the receptor bound to [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) ([ERG](/xray-mp-wiki/reagents/ligands/ergotamine/)) in an active-like conformation, revealing structural features that govern functional selectivity (biased agonism) between G protein and beta-arrestin signaling pathways. The structure was solved at 2.7 Å resolution using lipidic cubic phase (LCP) crystallization and data merged from 17 crystals.


## Publications

### doi/10.1126##science.1232808

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Construct**: Delta N(1-35)-5-HT2B-BRIL-Delta C(406-481); HA signal + [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/) N-terminal; PreScission site + 10xHis C-terminal
- **Notes**: Bac-to-Bac baculovirus system, MOI 5, harvested 48h post-infection at 27C

**Purification:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Expression construct**: Delta N-5-HT2B-BRIL-Delta C with N-terminal HA-FLAG and C-terminal PreScission-10xHis
- **Tag info**: C-terminal 10xHis tag removed by [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/)

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
      <td>Membrane preparation</td>
      <td>Hypotonic lysis and high-salt wash</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl; high-salt wash: 1.0 M NaCl, 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl</td>
      <td>EDTA-free protease inhibitors; washed 2x hypotonic, 4-5x high-salt</td>
    </tr>
    <tr>
      <td>Ligand incubation</td>
      <td>Incubation</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, 150 mM NaCl</td>
      <td>100 uM <a href="/xray-mp-wiki/reagents/ligands/ergotamine/">ERG</a> for 1h at RT; 2 mg/ml <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> for 30 min at 4C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.5, 150 mM NaCl, 50 uM <a href="/xray-mp-wiki/reagents/ligands/ergotamine/">ERG</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>2h at 4C; unsolubilized material removed at 150,000xg for 30 min</td>
    </tr>
    <tr>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC resin (Clontech)</td>
      <td>Wash I: 50 mM HEPES pH 7.5, 800 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 50 uM <a href="/xray-mp-wiki/reagents/ligands/ergotamine/">ERG</a>; Wash II: 50 mM HEPES pH 7.5, 150 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 50 uM <a href="/xray-mp-wiki/reagents/ligands/ergotamine/">ERG</a></td>
      <td>Elution in Wash II + 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> removed via PD MiniTrap G-25</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> digestion</td>
      <td>—</td>
      <td></td>
      <td>His-tagged PreScission; overnight; protease and uncleaved protein removed by second <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Centrifugal concentration</td>
      <td>—</td>
      <td></td>
      <td>100 kDa MWCO Vivaspin; concentrated to ~50 mg/ml; purity >95% by SDS-PAGE</td>
    </tr>
  </tbody>
</table>
**Final sample**: ~50 mg/ml in Wash Buffer II (without [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/))
**Purity**: >95% by SDS-PAGE; monodisperse by aSEC

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/))</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>/cholesterol mixture (40%:54%:6%)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>40% protein : 60% lipid</td>
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
      <td>Flash-frozen directly from LCP matrix</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in 96-well glass sandwich plates; NT8-<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) robot; 40 nl <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">lcp</a> drops + 800 nl precipitant; crystals up to 100x30x20 um</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Functional Selectivity at 5-HT2B

The 5-HT2B/ERG complex reveals that [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) induces beta-arrestin-biased signaling at the 5-HT2B receptor but not at the 5-HT1B receptor. The structural basis involves a unique kink in helix V of 5-HT2B that engages helix VI through S2225.43-N3446.45 hydrogen bonding and hydrophobic contacts mediated by the [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) phenyl moiety. This interaction selectively impairs G protein signaling while preserving beta-arrestin recruitment, providing a structural mechanism for biased agonism.

### Active-State Conformation

The 5-HT2B/ERG complex adopts an active-state conformation intermediate between inactive (Rho-R, A2AAR-R) and fully active (Ops-R*, A2AAR-R*) states. Helix VI shows outward displacement characteristic of active GPCRs, while helix VII adopts an intermediate active-state position. The D(E)/RY and NPxxY motifs show distinct activation features compared to both inactive and fully active receptors.

### Extended Ligand Binding Site

[ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) occupies the orthosteric binding pocket with its ergoline core, while its tripeptide moiety extends into an extended binding site that differs between 5-HT1B and 5-HT2B receptors. This differential engagement contributes to the functional selectivity profiles of [ERG](/xray-mp-wiki/reagents/ligands/ergotamine/) and related ergolines.


## Cross-References

- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/ligands/ergotamine/">ERG</a> — Related ligand or cofactor
