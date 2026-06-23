---
title: Amt-1 ammonium transporter from Archaeoglobus fulgidus
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0506254102]
verified: false
---

# Amt-1 ammonium transporter from Archaeoglobus fulgidus

## Overview

Amt-1 is one of three ammonium transporters (Amts) encoded in the genome of the hyperthermophilic archaeon Archaeoglobus fulgidus. The crystal structure was determined at 1.72 A resolution, revealing a compact trimer with 11 transmembrane helices per monomer and a central substrate channel in each monomer, similar to E. coli AmtB. Xenon derivatization identified 15 binding sites per monomer, mapping hydrophobic regions including the substrate channel and extensive internal cavities. The well-ordered cytoplasmic C terminus enabled construction of a docking model with the PII regulatory protein GlnB-1, which binds to the cytoplasmic face and blocks all three substrate channels. The histidine pair (H157 and H305) in the pore are nearly coplanar, forming a more stable hydrogen bond than observed in E. coli AmtB.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0506254102 | 2B2F | 1.72 A | P6$_2$22 (hexagonal) | Full-length A. fulgidus Amt-1 (residues 1-391) | None (apo structure) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Full-length Amt-1

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression and purification | Standard recombinant expression and membrane protein purification | -- | -- + n-Octyl-beta-D-glucopyranoside (beta-OG) | Amt-1 was expressed in E. coli and purified in n-octyl-beta-D-glucopyranoside (beta-OG) detergent |


## Crystallization

### doi/10.1073##pnas.0506254102

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified Amt-1 in beta-[OG](/xray-mp-wiki/reagents/detergents/og/) |
| Reservoir | -- |
| Mixing ratio | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Crystals grown in hexagonal space group P6_2_22. Substrate soaks performed with 20 mM (NH4)2SO4 and 80 mM CH3NH3+. Xenon derivatives prepared for phase determination and hydrophobic cavity mapping. |


## Biological / Functional Insights

### Archaeal ammonium transporter structure

Amt-1 is the first archaeal ammonium transporter structure. It shows a compact trimer with 11 TM helices per monomer, conserved pseudo-twofold symmetry, and a central hydrophobic substrate channel in each monomer. The architecture is very similar to E. coli AmtB despite only 41.6% sequence identity, demonstrating structural conservation across domains of life.

### Xenon mapping of hydrophobic cavities

Xenon derivatization revealed 15 binding sites per monomer, including four strong sites on the central threefold axis, three strong and one weak site in the transport channel, and sites in extensive internal cavities. The xenon binding confirmed the hydrophobic nature of the substrate channel. The internal cavities may allow for structural flexibility, particularly around helix V which has a conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/)-rich region (G152, G153) that may serve as a pivot point for conformational changes.

### Coplanar histidine pair in the pore

In Amt-1, the two conserved histidine residues H157 and H305 have nearly coplanar [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) rings, forming a 3.0 A hydrogen bond between their N_delta atoms. This is more optimally aligned than in E. coli AmtB, suggesting a more stable arrangement in the thermostable archaeal protein. F204 shows elevated B factors indicating conformational flexibility that may be important for substrate passage.

### GlnB-1 docking model for regulation

Amt-1 has a well-ordered cytoplasmic C terminus that enabled construction of a docking model with the PII regulatory protein GlnB-1. In the model, GlnB-1 binds tightly to the cytoplasmic face of the transporter, with its T-loops inserting deeply into the substrate channels, effectively blocking conduction. This provides a structural basis for the known regulatory interaction between Amt proteins and [GlnK PII Signal Transduction Protein (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/glnk/)/GlnB family members.

### Substrate transport mechanism debate

The structure supports a hydrophobic channel consistent with NH3 transport, but the authors note that uniport of NH3 poses a bioenergetic problem: it would effectively result in NH4+/H+ antiport, with protons moving against their gradient. A mechanism involving NH3 transport coupled to parallel proton transport in the same direction (net NH4+ uniport) may resolve this apparent contradiction.


## Cross-References

- [AmtB ammonium transporter / ammonia channel from Escherichia coli](/xray-mp-wiki/proteins/other-ion-channels/e-coli-amtb/) — Amt-1 is the archaeal homolog of E. coli AmtB, with conserved structure and mechanism
- [Ammonia Channel Mechanism](/xray-mp-wiki/concepts/ammonia-channel-mechanism/) — Amt-1 is an ammonium transporter/ammonia channel from the same Mep/Amt/Rh family
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [GR (Halobacterium sp. GR Bacteriorhodopsin)](/xray-mp-wiki/proteins/rhodopsins/gr/) — Related protein mentioned in the study
- [GlnK PII Signal Transduction Protein (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/glnk/) — Related protein mentioned in the study
- [AdiC Arginine/Agmatine Antiporter](/xray-mp-wiki/proteins/slc-transporters/adic/) — Related protein mentioned in the study
- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — Related protein mentioned in the study
- [AmtB ammonium transporter / ammonia channel from Escherichia coli](/xray-mp-wiki/proteins/other-ion-channels/e-coli-amtb/) — Related protein mentioned in the study
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used in purification
- [TES Buffer (N-Tris(hydroxymethyl)methyl-2-aminoethanesulfonic acid)](/xray-mp-wiki/reagents/buffers/tes/) — Reagent used in the study
