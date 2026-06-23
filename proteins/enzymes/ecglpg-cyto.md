---
title: Cytoplasmic Domain of Escherichia coli Rhomboid Protease GlpG
created: 2026-05-26
updated: 2026-05-26
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

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2013.01.019 | 4HDD | 1.35 A | I422 | ecGlpG(1-74) | None |

## Expression and Purification

- **Expression system**: E. coli BL21
- **Construct**: ecGlpG residues 1-74 (cytoplasmic domain only)

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression and cell lysis | Expression in E. coli BL21 cells followed by detergent solubilization | -- | not specified in main text (see Supplementary Data) + not specified in main text (see Supplementary Data) | Se-Met substituted ecGlpG(1-74) produced in BL21 cells; purification protocol based on previously described method |


## Crystallization

### doi/10.1016##j.jmb.2013.01.019

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | Se-Met ecGlpG(1-74) at 20 mg/ml |
| Reservoir | 0.49 M sodium phosphate monobasic monohydrate and 0.91 M potassium phosphate dibasic, pH 6.9 |
| Temperature | Room temperature |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals diffracted to 2.3 A; structure solved by MAD; selenium sites found by HYSS; phases calculated with Phaser and improved by RESOLVE; automated model building with RESOLVE fitted 63 out of 74 residues |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | Native ecGlpG(1-74) at 20 mg/ml |
| Reservoir | 100 mM sodium acetate trihydrate, pH 4.6, 0.2 M ammonium sulfate, 25% [PEG](/xray-mp-wiki/reagents/additives/peg/) 4000 |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals diffracted to 1.35 A; data collected at Canadian Light Source beamline 08ID-1 |


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

- [GlpG Protease](/xray-mp-wiki/proteins/enzymes/glpg/) — ecGlpG-cyto is the cytoplasmic domain of the full-length ecGlpG protein
- [hiGlpG](/xray-mp-wiki/proteins/enzymes/hiGlpG/) — Related prokaryotic rhomboid protease from Haemophilus influenzae, the first rhomboid structure solved
- [Rhomboid Protease Family](/xray-mp-wiki/concepts/protein-families/rhomboid-protease/) — ecGlpG is the archetypal prokaryotic rhomboid intramembrane protease
- [Intramembrane Proteolysis](/xray-mp-wiki/concepts/membrane-mimetics/membrane-mimetics/membrane-mimetics/intramembrane-proteolysis/) — ecGlpG catalyzes substrate cleavage within the lipid bilayer via its Ser-His catalytic dyad
- [Domain Swapping](/xray-mp-wiki/concepts/structural-mechanisms/domain-swapping/) — The cytoplasmic domain adopts a domain-swapped dimer structure, a key finding of this study
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM is used for detergent solubilization of rhomboid proteases in related studies (Sampathkumar et al., 2012)
- [Selenomethionine (Se-Met)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Se-Met substituted protein used for MAD phasing in structure determination
