---
title: TmYidC (Thermotoga maritima YidC Insertase)
created: 2026-06-08
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.bbamem.2021.183825, doi/10.1096##fj.201700893RR]
verified: false
---

# TmYidC (Thermotoga maritima YidC Insertase)

## Overview

TmYidC is the YidC insertase/chaperone from the thermophilic bacterium Thermotoga maritima. YidC is a member of the evolutionarily conserved YidC/Alb3/Oxa1 membrane protein family that plays essential roles in the insertion and folding of membrane proteins. The crystal structure of TmYidC at 3.4 A resolution (PDB 6Y86) revealed the N-terminal amphipathic helix (N-AH) for the first time, which acts as a membrane recognition helix. The structure shows an active insertase conformation. Molecular dynamics simulations showed that N-AH lies on the periplasmic side of the membrane forming an angle of about 15 deg with the membrane surface. The C1 region exhibits high flexibility, enabling switching between insertase and chaperone conformations.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.bbamem.2021.183825 | 6Y86 | 3.4 | P 41 21 2 | Full-length TmYidC, residues 1-425 |  |
| doi/10.1096##fj.201700893RR | 5Y82 | 2.5 | P4(1) | TmPD (Thermotoga maritima YidC periplasmic domain, residues 24-222) |  |
| doi/10.1096##fj.201700893RR | 5Y83 | 3.8 | P2(1)2(1)2(1) | Full-length TmYidC, residues 1-445 |  |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length TmYidC with C-terminal hexahistidine tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Affinity purification | Immobilized metal affinity chromatography | Ni-NTA | n-dodecyl-beta-D-maltopyranoside (DDM) | TmYidC expressed in E. coli and purified in DDM |
| Size-exclusion chromatography | Gel filtration | — |  | Final polishing step. TmYidC exists as a monomer in DDM solution. |


## Crystallization

### doi/10.1016##j.bbamem.2021.183825

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Notes | Crystallized using vapor diffusion method in presence of DDM. Structure solved by molecular replacement using P1 domain of TmYidC as search model. |


## Biological / Functional Insights

### N-terminal amphipathic helix as membrane recognition helix

The N-AH (residues 1-19) is tilted on the membrane surface at approximately 15 deg, as confirmed by MD simulations in POPE:POPG (3:1) bilayers. The N-terminus is embedded in the membrane, acting as a recognition helix to localize YidC to the lipid bilayer.

### Dual insertase and chaperone conformations

YidC functions both as an insertase (independent membrane protein insertion) and as a chaperone (in complex with SecYEG translocon). The C1 region (residues 282-308) exhibits high flexibility with deviations up to 2.5 nm from the crystal structure, enabling functional switching between conformations. The EH1 helix (residues 226-244) acts as a mechanical lever coordinating domain movements.

### Species-specific SecY interaction

Complementation assays showed that TmYidC cannot rescue E. coli YidC depletion, but a chimera with EcYidC's N-AH (YidC61) partially rescues growth. Crosslinking experiments identified N-AH as a major contact site with SecY, suggesting species-specific interaction with the Sec translocon.


## Cross-References

- [YidC/Oxa1/Alb3 Insertase Family](/xray-mp-wiki/concepts/yidc-oxa1-alb3-insertase-family/) — YidC is the founding member of this conserved membrane protein family
- [N-Dodecyl-beta-D-maltopyranoside (beta-DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for purification of TmYidC
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-NTA IMAC used for purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC used as polishing step
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Structure solved by MR using P1 domain as search model
