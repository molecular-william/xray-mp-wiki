---
title: "PsbS from Spinach (Spinacia oleracea)"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3068]
verified: false
---

# PsbS from Spinach (Spinacia oleracea)

## Overview

PsbS is a photosystem II protein essential for qE-type non-photochemical quenching (NPQ) in plants. It protects plants from photodamage under excess light conditions by sensing lumenal acidification and triggering thermal dissipation of excess absorbed light energy. The low-pH crystal structures of PsbS from spinach (Spinacia oleracea) revealed that PsbS adopts a unique folding pattern within the light-harvesting-complex (LHC) superfamily and is a noncanonical pigment-binding protein. Unlike other LHCs, PsbS has four transmembrane helices (TM1-TM4) with a compact structure that leaves no internal void space for pigment binding. Both active (low pH) and inactive (neutral pH) PsbS form homodimers in the thylakoid membrane, with activation involving a conformational change associated with altered lumenal intermolecular interactions rather than a dimer-to-monomer transition. The pH-sensing residues are two lumen-exposed glutamates (Glu69 and Glu173 in spinach), and DCCD binding to these residues disrupts lumenal intermolecular hydrogen bonds, inhibiting qE.


## Publications

### doi/10.1038##nsmb.3068

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/not yet assigned (native 1)">NOT YET ASSIGNED (NATIVE 1)</a></td>
      <td>3.10</td>
      <td>P2(1)2(1)2(1)</td>
      <td>PsbS from spinach (residues after limited proteolysis removing N-terminal LFKSK)</td>
      <td>Hg (derivative), Chl a</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/not yet assigned (native 2)">NOT YET ASSIGNED (NATIVE 2)</a></td>
      <td>2.35</td>
      <td>P2(1)2(1)2(1)</td>
      <td>PsbS from spinach (residues after limited proteolysis)</td>
      <td>Chl a</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/not yet assigned (dccd-modified)">NOT YET ASSIGNED (DCCD-MODIFIED)</a></td>
      <td>2.70</td>
      <td>P2(1)2(1)2(1)</td>
      <td>PsbS from spinach, DCCD-soaked crystal</td>
      <td>DCCD, Chl a</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Native purification from fresh market spinach
- **Construct**: PsbS selectively precipitated from BBY membranes (photosystem II-enriched thylakoid fragments)
- **Notes**: BBY membranes were solubilized with 0.4% [n-octyl-β-D-thioglucopyranoside](/xray-mp-wiki/reagents/detergents/otg/) (OTG) at pH 6.0. PsbS was selectively precipitated, then solubilized with 2% [n-octyl-β-D-glucopyranoside](/xray-mp-wiki/reagents/detergents/og/) (OG) overnight at 4 °C. The solubilized PsbS was purified by Resource S cation-exchange chromatography in buffer containing 0.4% [n-nonyl-β-D-glucopyranoside](/xray-mp-wiki/reagents/detergents/ng/) (NG), followed by limited proteolysis with subtilisin and [size-exclusion chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) on a Superdex 200 column. The first five residues (LFKSK) were removed by subtilisin treatment.

**Purification:**

- **Expression system**: Native (spinach)
- **Expression construct**: PsbS from BBY membranes

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
      <td>BBY membrane preparation</td>
      <td>Differential centrifugation</td>
      <td>—</td>
      <td>20 mM MES pH 6.0, 15 mM NaCl, 0.4 M sucrose</td>
      <td>From fresh market spinach</td>
    </tr>
    <tr>
      <td>Selective precipitation</td>
      <td>Detergent solubilization and precipitation</td>
      <td>—</td>
      <td>20 mM MES pH 6.0, 15 mM NaCl, 0.4 M sucrose + 0.4% OTG</td>
      <td>Solubilization on ice for 10 min, then centrifugation at 40,000g for 40 min</td>
    </tr>
    <tr>
      <td>Resolubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>20 mM sodium acetate pH 5.0, 20 mM NaCl + 2% OG</td>
      <td>Overnight incubation at 4 °C, then centrifugation at 40,000g for 30 min</td>
    </tr>
    <tr>
      <td>Cation-exchange chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-exchange chromatography</a></td>
      <td>Resource S (GE Healthcare)</td>
      <td>20 mM sodium acetate pH 5.0, 20 mM NaCl + 0.4% NG</td>
      <td>Eluted by NaCl gradient</td>
    </tr>
    <tr>
      <td>Limited proteolysis</td>
      <td><a href="/xray-mp-wiki/methods/purification/limited-proteolysis/">Limited proteolysis</a></td>
      <td>—</td>
      <td></td>
      <td>Incubation with subtilisin (0.01 mg/ml) at 20 °C for 2 h; removes N-terminal LFKSK</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td>Superdex 200 (GE Healthcare)</td>
      <td>20 mM sodium acetate pH 5.0, 100 mM NaCl + 0.4% NG</td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: PsbS at 10 mg/ml in 20 mM sodium acetate pH 5.0, 100 mM NaCl, 0.4% NG

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-drop vapor-diffusion</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM sodium acetate pH 5.0, 25-28% PEG 300, 1% ethyl acetate</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir solution plus 0.5% NG and 18% glycerol</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of maximal size obtained after 10 d. DCCD-modified crystals obtained by soaking native crystals in 10 mM DCCD for 3 d. Heavy atom derivative by soaking in 10 mM mercury nitrate for 1 d.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### PsbS is a noncanonical LHC protein without internal pigment binding

PsbS is a noncanonical LHC protein that does not bind internal pigments like other LHCs. TM2 (equivalent to LHCII helix C) and TM4 (unique to PsbS) are positioned too close to the central supercoil to accommodate chlorophylls, neoxanthin, or lutein molecules. The compact structure is stabilized by close interactions of TM2 and TM4 with the central TM1-TM3 supercoil, serving a similar structural role as lutein molecules in LHCII.

### Active and inactive PsbS both form homodimers

Both active (pH 5.0) and inactive (neutral pH) PsbS form homodimers in thylakoid membranes. The dimer interface involves TM2 and TM3 in the transmembrane region, 13 hydrogen bonds plus one salt bridge at the stromal side, and four hydrogen bonds at the lumenal side mediated by Glu173. The dimer has a large interfacial area of over 1,600 A2.

### Activation involves conformational change while maintaining dimeric state

Activation of PsbS by low pH involves a conformational change while maintaining dimeric state. The pH-sensing Glu173 residue is protonated at low pH (active) and deprotonated at neutral pH (inactive), altering lumenal intermolecular hydrogen bonds. DCCD binding to Glu173 induces a rotameric switch that disrupts lumenal hydrogen bonds, producing a looser dimer conformation similar to the neutral pH state.


## Cross-References

- <a href="/xray-mp-wiki/concepts/miscellaneous/non-photochemical-quenching/">Non-photochemical Quenching (NPQ) in LHC-II</a> — PsbS is essential for qE-type NPQ in plants
- <a href="/xray-mp-wiki/proteins/photosynthesis/spinach-light-harvesting-complex-ii/">Spinach Light-Harvesting Complex II (LHC-II)</a> — PsbS belongs to the LHC superfamily; structural comparison with LHCII
- <a href="/xray-mp-wiki/proteins/photosynthesis/cp29-spinach/">CP29 Light-Harvesting Complex from Spinach</a> — Structural comparison with other LHC proteins; gel-filtration standard
- <a href="/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/">Photosystem II</a> — PsbS is a photosystem II protein
