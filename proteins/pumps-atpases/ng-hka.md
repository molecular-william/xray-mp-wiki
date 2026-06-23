---
title: Non-Gastric H+/K+-ATPase (ngHKA)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-022-32793-0]
verified: false
---

# Non-Gastric H+/K+-ATPase (ngHKA)

## Overview

The non-gastric H+/K+-ATPase (ngHKA, [ATP](/xray-mp-wiki/reagents/ligands/atp)12A) is a P-type 2C ATPase that participates in K+ reabsorption by the colon and kidney and contributes to acidification of the airways, a process promoting chronic respiratory infections in cystic fibrosis. This paper presents the first crystal structure of ngHKA in the K+-occluded E2-Pi state at 3.3 A resolution, revealing mechanistic differences between ngHKA and the gastric proton pump (gHKA). The structure shows that ngHKA exchanges 1 H+ and 1 K+ per cycle in an electroneutral fashion. The paper also demonstrates that four simultaneous residue substitutions (Ser794, Trp943, Cys949, Ala797Pro - SPWC mutant) convert ngHKA into a bona fide Na+/K+ pump with 3Na+:2K+ stoichiometry.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-022-32793-0 | Not specified (deposited, PDB code in supplementary) | 3.3 | Not specified | Rat ngHKA alpha subunit co-expressed with rat NKA beta1 subunit in HEK293S GnT1 cells; Asp315Gly correction applied | K+ ([ALF4](/xray-mp-wiki/reagents/ligands/alf4)- inhibited, K+-occluded E2-Pi state) |

## Expression and Purification

- **Expression system**: HEK293S GnT1 cells (baculovirus-mediated transduction, BacMam)
- **Construct**: Rat ngHKA alpha subunit with N-terminal His6-EGFP-TEV tag; rat NKA beta1 subunit with N-terminal Flag-TEV tag; Asp315Gly correction applied
- **Induction**: Baculovirus transduction of mammalian cells

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure emulsifier | — | Not specified | Harvested cells broken up, membrane fractions sedimented |
| Solubilization | [C12E8](/xray-mp-wiki/reagents/detergents/c12e8) (1% octaethylene glycol monododecyl ether) | — | 40 mM MES/Tris pH 6.5, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 5 mM [DTT](/xray-mp-wiki/reagents/additives/dtt), 0.06% GDN | Solubilized for crystallization or [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em) |
| Affinity chromatography | Ni-NTA resin | Ni-NTA (Qiagen) | 20 mM MES/Tris pH 6.5, 1% GDN, 5 mM [MGCL2](/xray-mp-wiki/reagents/additives/mgcl2) | Anti-GFP [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody) added; digested fragments removed by Ni-NTA passage |
| Size-exclusion chromatography | Superose 6 Increase column | — | 20 mM MES/Tris pH 6.5, 1% GDN, 5 mM [MGCL2](/xray-mp-wiki/reagents/additives/mgcl2), 100 mM KCl or 200-300 mM NaCl |  |


## Crystallization

### doi/10.1038##s41467-022-32793-0

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | 5 mg/mL purified, lipidated protein |
| Reservoir | 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 33% [PEG300](/xray-mp-wiki/reagents/additives/peg300), 50 mM [Glycine](/xray-mp-wiki/reagents/buffers/glycine)-NaOH pH 9.5, 100 mM NaCl, 200 mM KCl, 0.1 mM AlCl3, 0.4 mM NaF |
| Temperature | 20 C |
| Notes | Crystals flash-frozen in liquid nitrogen; RbCl substituted KCl for anomalous diffraction experiments |


## Biological / Functional Insights

### Electroneutral 1H+:1K+ exchange mechanism

The ngHKA structure reveals a single K+ occluded at a site overlapping with NKA's site II, coordinated by Glu346, Asn795, Glu798, Asp823 and main-chain oxygens from Val341, Ala342, and Val344. Unlike the gastric HKA which has Glu936 on TM8 that interacts with Lys791, ngHKA has Met939, and Asp827 forms a salt bridge with Lys794, explaining the distinct cation-binding-site structure and evolved function for K+ reabsorption rather than building H+ gradients.

### Ion selectivity switching via four mutations

The SPWC quadruple mutant (Lys794Ser, Ile943Trp, Arg949Cys, Ala797Pro) converts the electroneutral ngHKA into a bona fide Na+/K+ pump with 3Na+:2K+ stoichiometry. The mutations create a third Na+-binding site (site III) and enable the concerted mechanism leading to Na+/K+ pump phosphorylation, providing a prototype for studying ion-selectivity evolution in P-type ATPases.


## Cross-References

- [Glycine](/xray-mp-wiki/reagents/buffers/glycine) — Entity mentioned in text
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em) — Entity mentioned in text
- [ATP](/xray-mp-wiki/reagents/ligands/atp) — Entity mentioned in text
- [PEG300](/xray-mp-wiki/reagents/additives/peg300) — Entity mentioned in text
- [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody) — Entity mentioned in text
- [MGCL2](/xray-mp-wiki/reagents/additives/mgcl2) — Entity mentioned in text
- [C12E8](/xray-mp-wiki/reagents/detergents/c12e8) — Entity mentioned in text
- [ALF4](/xray-mp-wiki/reagents/ligands/alf4) — Entity mentioned in text
- [DTT](/xray-mp-wiki/reagents/additives/dtt) — Entity mentioned in text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) — Entity mentioned in text
