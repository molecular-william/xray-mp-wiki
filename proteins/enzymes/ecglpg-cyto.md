---
title: "Cytoplasmic Domain of Escherichia coli Rhomboid Protease GlpG"
created: 2026-05-26
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2013.01.019]
verified: false
---

# Cytoplasmic Domain of Escherichia coli Rhomboid Protease GlpG

## Overview

Crystal structure of the soluble cytoplasmic domain of the Escherichia coli rhomboid protease GlpG (ecGlpG) was determined at 1.35 A resolution, revealing a domain-swapped dimer structure. Steady-state kinetic analysis demonstrated that removal of the cytoplasmic domain does not significantly alter the catalytic parameters of the enzyme, indicating that this domain does not modulate the active site conformation, stability, or accessibility.

## Publications

### doi/10.1016##j.jmb.2013.01.019

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4hdd">4HDD</a></td>
      <td>1.35 A</td>
      <td>I422</td>
      <td>ecGlpG(1-74)</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21
- **Construct**: ecGlpG residues 1-74 (cytoplasmic domain only)

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
      <td>Protein expression and cell lysis</td>
      <td>Expression in E. coli BL21 cells followed by detergent solubilization</td>
      <td>--</td>
      <td>not specified in main text (see Supplementary Data) + not specified in main text (see Supplementary Data)</td>
      <td>Se-Met substituted ecGlpG(1-74) produced in BL21 cells; purification protocol based on previously described method</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (hanging drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Se-Met ecGlpG(1-74) at 20 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.49 M sodium phosphate monobasic monohydrate and 0.91 M potassium phosphate dibasic, pH 6.9</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
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
      <td>Crystals diffracted to 2.3 A; structure solved by MAD; selenium sites found by HYSS; phases calculated with Phaser and improved by RESOLVE; automated model building with RESOLVE fitted 63 out of 74 residues</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (hanging drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Native ecGlpG(1-74) at 20 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM sodium acetate trihydrate, pH 4.6, 0.2 M ammonium sulfate, 25% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000</td>
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
      <td>Crystals diffracted to 1.35 A; data collected at Canadian Light Source beamline 08ID-1</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Domain-swapped dimer structure

The 1.35 A-resolution crystal structure reveals that the ecGlpG cytoplasmic domain exists as a domain-swapped dimer with extensive exchange between the two monomers. The extended beta-strand is split into two parts (beta2-A and beta2-B), corresponding to two distinct beta-strands in the globular monomeric form. The hinge region (residues 32-34) mediates the domain swap through hydrogen bond networks involving Q34, H32, and N33.

### Cytoplasmic domain does not affect catalytic activity

Steady-state kinetic analysis using both a water-soluble fluorescently labeled [casein](/xray-mp-wiki/reagents/additives/bodipy/) substrate ([BODIPY FL casein](/xray-mp-wiki/reagents/additives/bodipy/)) and the membrane protein psTatA from Providencia stuartii showed that removal of the cytoplasmic domain does not significantly alter the catalytic parameters (Km, Vmax, kcat) for detergent-solubilized rhomboid. This contradicts previous studies and is attributed to improved steady-state kinetic assay conditions in this work.

### Temperature and mutation promote dimer formation

The ecGlpG cytoplasmic domain exists predominantly as monomers in solution at 4 C, with a very slow conversion to the dimeric form. Increasing temperature to 55 C shifted the equilibrium toward dimers (27% after 2 h, 52% after 14 h). The N33P mutation in the hinge region increased dimer fraction to 44%, confirming that the hinge loop conformation controls the monomer-dimer equilibrium.

### Domain swapping occurs in full-length protein

When the cytoplasmic domain was cleaved from full-length ecGlpG using immobilized [alpha-chymotrypsin](/xray-mp-wiki/reagents/additives/thermolysin/), gel filtration showed that 20% of the released cytoplasmic domain existed as dimers, compared to only 5% for purified cytoplasmic domain alone. This suggests that domain swapping occurs in the full-length protein and is not an artifact of crystallization.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/glpg/">GlpG Protease</a> — ecGlpG-cyto is the cytoplasmic domain of the full-length ecGlpG protein
- <a href="/xray-mp-wiki/proteins/enzymes/hiGlpG/">hiGlpG</a> — Related prokaryotic rhomboid protease from Haemophilus influenzae, the first rhomboid structure solved
- <a href="/xray-mp-wiki/concepts/protein-families/rhomboid-protease/">Rhomboid Protease Family</a> — ecGlpG is the archetypal prokaryotic rhomboid intramembrane protease
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-proteolysis/">Intramembrane Proteolysis</a> — ecGlpG catalyzes substrate cleavage within the lipid bilayer via its Ser-His catalytic dyad
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/domain-swapping/">Domain Swapping</a> — The cytoplasmic domain adopts a domain-swapped dimer structure, a key finding of this study
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — DDM is used for detergent solubilization of rhomboid proteases in related studies (Sampathkumar et al., 2012)
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (Se-Met)</a> — Se-Met substituted protein used for MAD phasing in structure determination
