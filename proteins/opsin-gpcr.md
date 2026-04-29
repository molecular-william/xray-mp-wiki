---
title: Opsin (Rhodopsin Apoprotein)
created: 2026-04-26
updated: 2026-04-28
type: protein
tags: [gpcr, membrane-protein, receptor]
sources: [doi/10.1002##anie.201302374, doi/10.1016##J.JMB.2004.08.090, doi/10.1016##J.JMB.2007.03.007]
category: proteins
---
layout: default

# Opsin — Rhodopsin Apoprotein

## Overview

Opsin is the retinal-free apoprotein of rhodopsin, the G-protein-coupled receptor (GPCR) responsible for vision in vertebrate rod cells. The crystallized opsin structure represents the active Ops* conformation, making it a valuable structural model for olfactory receptors (ORs) which belong to the rhodopsin-like GPCR family.

## Structure Determination

- **PDB ID**: 3LZ8 (Ops*-GαCT2-OG complex)
- **Resolution**: 2.65 Å
- **Method**: X-ray crystallography, vapor diffusion
- **Crystal form**: Active state (Ops*)
- **pH**: 5.6
- **Complex**: Ops* bound to GαCT2 peptide (synthetic G-protein peptide from C-terminal region of Gα subunit)

## Expression

- **Source**: Native bovine retinal disc membranes (rhodopsin from vertebrate rod cells)
- **Construct**: Opsin (retinal-free rhodopsin), no genetic fusion or mutation
- **Note**: Opsin was solubilized from native membranes rather than heterologously expressed

## Solubilization Reagents

- **OG** (n-octyl β-D-glucopyranoside) — primary detergent for solubilization and crystallization
- OG concentration: below critical micellar concentration during crystallization

## Purification

- Native solubilization from bovine retinal disc membranes using OG
- No affinity chromatography or SEC described — direct crystallization from OG-solubilized membrane fraction
- GαCT2 peptide added to stabilize active conformation

## Crystallization

- **Method**: Vapor diffusion
- **Condition**: pH 5.6 (acidic pH favors active Ops* conformation)
- **Key finding**: A molecule of **OG** was found occupying the retinal-binding pocket, replacing retinal and stabilizing the active receptor conformation
- The OG binding provides hydrogen-bonding interactions analogous to odorant-receptor interactions in olfactory receptors

## Detergent Binding Pocket Study

Various detergents were tested for their ability to occupy the retinal-binding pocket (reconstitution inhibition assay with 11-cis-retinal):

| Detergent | Effect on Reconstitution | Interpretation |
|-----------|--------------------------|----------------|
| **OG** | Strong inhibition | Enters binding pocket |
| **NG** (nonylglucoside) | Concentration-dependent inhibition | Enters binding pocket |
| **HpG** (heptylglucoside) | Weak inhibition | Partial pocket access |
| **DM** (decylmaltoside) | Strong inhibition | Best steric fit |
| **DDM** (dodecylmaltoside) | Weak inhibition | Moderate fit |
| **TDM** (tridecylmaltoside) | Minimal inhibition | Too bulky |
| **HxM** (hexylmaltoside) | Weak inhibition | Short chain |
| **LMNG** | Minimal inhibition | Too bulky (neopentyl glycol) |
| **OGNG** | Minimal inhibition | Too bulky (neopentyl glycol) |

**Conclusion**: Alkylmaltosides and alkylglucosides can enter the retinal-binding pocket when concentration is above CMC. DM fits best sterically. Neopentyl glycol detergents are too bulky to penetrate the pocket.

## Key Findings

- OG binds deep in the orthosteric ligand-binding pocket, mimicking odorant binding to ORs
- The hydrogen-bond pattern holding OG in the pocket is reminiscent of dynamic hydrogen-bonding proposed for OR-ligand interactions
- Opsin serves as the best available structural template for olfactory receptor homology modeling
- Demonstrates how hydrophobic odorants can enter ORs from the lipid bilayer into the 7TM scaffold

## Related GPCRs

- [bovine-rhodopsin](//xray-mp-wiki/proteins/bovine-rhodopsin/) — Dark state rhodopsin (11-cis-retinal-bound) in trigonal crystal form; native bovine source and recombinant N2C/D282C mutant (first recombinant GPCR structure)
- [a2a-adenosine-receptor](//xray-mp-wiki/proteins/a2a-adenosine-receptor/) — Class A GPCR with extensive structural biology
- [5ht2b-receptor](//xray-mp-wiki/proteins/5ht2b-receptor/) — Serotonin GPCR with BRIL fusion
- [etb-receptor](//xray-mp-wiki/proteins/etb-receptor/) — Endothelin GPCR with thermostabilization
- [kappa-opioid-receptor](//xray-mp-wiki/proteins/kappa-opioid-receptor/) — Opioid GPCR with nanobody stabilization
- [lpa1-receptor](//xray-mp-wiki/proteins/lpa1-receptor/) — GPCR with spherical binding pocket
- [p2y12-receptor](//xray-mp-wiki/proteins/p2y12-receptor/) — Platelet GPCR with LCP crystallization

## Cross-References

- [og](//xray-mp-wiki/reagents/detergents/og/) — Octyl glucoside detergent (solubilization + binding pocket)
- [lDAO](//xray-mp-wiki/reagents/detergents/lDAO/) — Zwitterionic detergent (0.05% in bovine rhodopsin crystallization)
- [ddm](//xray-mp-wiki/reagents/detergents/ddm/) — DDM tested in reconstitution
- [dm](//xray-mp-wiki/reagents/detergents/dm/) — Decylmaltoside (best steric fit in pocket)
- [lmng](//xray-mp-wiki/reagents/detergents/lmng/) — LMNG (too bulky for pocket)
- [ogng](//xray-mp-wiki/reagents/detergents/ogng/) — OGNG (too bulky for pocket)
- [vapor-diffusion](//xray-mp-wiki/methods/crystallization/vapor-diffusion/) — Crystallization method
- [xray-crystallography](//xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Structure determination method