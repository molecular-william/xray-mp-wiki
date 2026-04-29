---

title: CD81 Tetraspanin
created: 2026-04-26
updated: 2026-04-27
type: protein
tags: [membrane-protein, receptor]
sources: [doi/10.1016##j.cell.2016.09.056]

category: proteins
---
layout: default


# CD81 Tetraspanin

## Overview

CD81 (also known as TAPA-1, tspan28) is a four-pass transmembrane protein of the tetraspanin family. Tetraspanins form "signaling hubs" by associating with other membrane proteins. CD81 plays essential roles in B-cell biology, forming the CD19/CD21/CD225 complex to regulate B-cell receptor function. It is also a host factor for Hepatitis C virus entry.

## Structure Determination

- **PDB ID**: 5TCX
- **Resolution**: 2.95 Å along b* and c* axes, 5.5 Å along a* (anisotropic)
- **Method**: [xray-crystallography](//xray-mp-wiki/methods/structure-determination/xray-crystallography/), [lipidic-cubic-phase](//xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) crystallization
- **Phasing**: Fragment-based iterative [molecular-replacement](//xray-mp-wiki/methods/structure-determination/molecular-replacement/) (CD81 EC2 region PDB 1IV5 + poly-Ala helix model)
- **Expression**: [sf9-cells](//xray-mp-wiki/methods/expression-systems/sf9-cells/) (baculovirus [baculovirus-expression](//xray-mp-wiki/methods/expression-systems/baculovirus-expression/))
- **Construct**: Full-length human CD81 with N-terminal His-tag and C-terminal Strep-tag II

## Expression and Purification

- **Expression system**: [sf9-cells](//xray-mp-wiki/methods/expression-systems/sf9-cells/) via [baculovirus-expression](//xray-mp-wiki/methods/expression-systems/baculovirus-expression/)
- **Detergent**: [ddm](//xray-mp-wiki/reagents/detergents/ddm/) (n-dodecyl-β-D-maltopyranoside) for membrane solubilization
- **Purification**: [affinity-chromatography](//xray-mp-wiki/methods/purification/affinity-chromatography/) (N-terminal His-tag), followed by [size-exclusion-chromatography](//xray-mp-wiki/methods/purification/size-exclusion-chromatography/) ([superdex-columns](//xray-mp-wiki/methods/purification/superdex-columns/))
- **SEC buffer**: 20 mM [hepes-buffer](//xray-mp-wiki/reagents/buffers/hepes-buffer/) pH 7.5, 150 mM [sodium-chloride](//xray-mp-wiki/reagents/additives/sodium-chloride/), 0.05% [ddm](//xray-mp-wiki/reagents/detergents/ddm/)

## Crystallization

- **Method**: [lipidic-cubic-phase](//xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP) — [monoolein](//xray-mp-wiki/methods/crystallization/monoolein/)-based mesophase
- **Lipid**: [monoolein](//xray-mp-wiki/methods/crystallization/monoolein/) (Nu-Chek Prep)
- **Protein-to-lipid ratio**: 1:1.5 (w/w)
- **Reservoir**: 0.1 M [sodium-acetate](//xray-mp-wiki/reagents/additives/sodium-acetate/) pH 4.5, 18–22% [peg-400](//xray-mp-wiki/reagents/additives/peg-400/), 0.2 M [sodium-chloride](//xray-mp-wiki/reagents/additives/sodium-chloride/)
- **Temperature**: 20 °C
- **Crystal growth**: 1–3 weeks
- **Space group**: P2₁2₁2₁

## Key Structural Feature: Intramembrane Cholesterol Pocket

The most striking feature is a large hydrophobic pocket (3300 Å³) bounded by the four transmembrane helices and the EC2 cap. A **[cholesterol-lipid](//xray-mp-wiki/reagents/lipids/cholesterol-lipid/) molecule** was resolved in this pocket:

- **Contact residues**: F21 (TM1), I64/V68/V71/M72/V75 (TM2), F94/L98/L101 (TM3), V212/M216 (TM4)
- **Polar contacts**: N18 (TM1) and E219 (TM4) hydrogen-bond to [cholesterol-lipid](//xray-mp-wiki/reagents/lipids/cholesterol-lipid/) hydroxyl group
- **Conservation**: 13 amino acids nearly 100% conserved across 37 homologs; E219 only in CD81 and tspan10

## Molecular Dynamics Simulations

- **EC2 open/closed conformations**: MD simulations in hydrated lipid bilayer (with and without cholesterol) revealed two states
  - **Closed state** (cholesterol-bound): EC2 remains in contact with TM1 and TM2, similar to crystal structure
  - **Open state** (cholesterol-free): EC2 disengages from TM1 and TM2 in 3 of 9 simulations; fully open conformation persists
  - **Opening mechanism**: Salt bridge D196(EC2)-K201(TM4) breaks → TM3 straightens → TM4 extends → new K116-D117 interaction stabilizes extended TM3
  - **Cholesterol dissociation**: In 2 of 9 simulations with cholesterol, cholesterol dissociated into membrane, followed by EC2 opening
- **TM1/TM2 motion**: Intracellular end of TM1 stays close to TM4 in apoprotein (N18-E219 H-bond); when cholesterol bound, cholesterol competes for E219 interaction, causing TM1 to separate from TM4
- **Functional consequence**: Cholesterol-bound (closed) state disfavors partner protein binding; open state (cholesterol-free) binds partners more tightly

## Functional Evidence

- CD81 immunoprecipitates 15-fold more [cholesterol-lipid](//xray-mp-wiki/reagents/lipids/cholesterol-lipid/) than controls
- E219A and E219Q mutants recover 50% less [cholesterol-lipid](//xray-mp-wiki/reagents/lipids/cholesterol-lipid/)
- [cholesterol-lipid](//xray-mp-wiki/reagents/lipids/cholesterol-lipid/) binding regulates CD81-dependent CD19 surface export
- Molecular dynamics: [cholesterol-lipid](//xray-mp-wiki/reagents/lipids/cholesterol-lipid/) stabilizes "closed" EC2 conformation; absence leads to "open" state

## Tetraspanin Fold

- Transmembrane region: two largely separated pairs of antiparallel helices (TM1/TM2 and TM3/TM4)
- Not a four-helix bundle as previously modeled
- EC2 domain caps the intramembrane cavity
- Monomeric in crystals (vs. dimeric in isolated EC2 fragment — likely non-native)

## Related Membrane Proteins

- [a2a-adenosine-receptor](//xray-mp-wiki/proteins/a2a-adenosine-receptor/) — GPCR with [cholesterol-lipid](//xray-mp-wiki/reagents/lipids/cholesterol-lipid/) binding implications
- [lpa1-receptor](//xray-mp-wiki/proteins/lpa1-receptor/) — GPCR with spherical binding pocket
- [angiotensin-ii-type-1-receptor](//xray-mp-wiki/proteins/angiotensin-ii-type-1-receptor/) — GPCR with [cholesterol-hydrogen-succinate](//xray-mp-wiki/reagents/lipids/cholesterol-hydrogen-succinate/) stabilization