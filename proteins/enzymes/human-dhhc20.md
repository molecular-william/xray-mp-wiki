---
title: Human DHHC20 Palmitoyltransferase
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aao6326]
verified: false
---

# Human DHHC20 Palmitoyltransferase

## Overview

Human DHHC20 (hDHHC20) is an integral membrane S-acyltransferase of the DHHC
family that catalyzes protein palmitoylation — the attachment of a palmitoyl
group to cysteine residues via a thioester linkage. It is a Golgi-resident
enzyme with four transmembrane helices adopting a tepee-like organization.
The active site, containing the signature Asp-His-His-Cys (DHHC) motif,
resides at the membrane-cytosol interface, explaining why membrane-proximal
cysteines are preferred substrates. The 2.44 A crystal structure of hDHHC20
and a 2.54 A structure of the zfDHHS15 mutant revealed the acyl-chain binding
cavity formed by the transmembrane domain, providing insights into acyl-CoA
recognition and chain-length selectivity. DHHC20 overexpression causes
cellular transformation and has been proposed as a therapeutic target for
cancers resistant to EGFR-targeted therapy.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.aao6326 |  | 2.44 | — | hDHHC20 (residues 5-299), reductively methylated, hexagonal P63 form |  |
| doi/10.1126##science.aao6326 |  | 2.44 | — | hDHHC20 C263A mutant with 2-bromopalmitate (2-BP) covalent inhibitor |  |

## Expression and Purification

- **Expression system**: Pichia pastoris (yeast)
- **Construct**: N-terminal His10-GFP-PreScission-tagged hDHHC20
- **Notes**: Codon-optimized hDHHC20 cloned into pPICZ-C vector; expressed in Pichia pastoris SDM1163 cells

### Purification Workflow

- **Expression system**: Pichia pastoris
- **Expression construct**: N-terminal His10-GFP tag with PreScission cleavage site
- **Tag info**: His10-GFP, removed by [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) resin (cobalt affinity) | — | 50 mM HEPES pH 7.5, 150 mM NaCl, 2 mM beta-ME, 2 mM TCEP + 1 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Wash with 25 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), elute with 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); gravity flow at ambient temperature |
| SEC / Tag removal | PreScission cleavage overnight at 4C, then [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) Increase SEC | — | 50 mM HEPES pH 7.5, 150 mM NaCl, 2 mM TCEP + 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | GFP tag and [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) removed by SEC; fractions pooled and concentrated using 50 kDa MWCO Amicon |
| Reductive methylation (for crystallization) | Formaldehyde and DMAB complex treatment | — | 50 mM HEPES pH 7.5, 250 mM NaCl, 2 mM TCEP, 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Methylation quenched with Tris HCl pH 8.0 and [DTT](/xray-mp-wiki/reagents/additives/dtt/); then SEC on [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) Increase |

**Final sample**: Concentrated in SEC buffer containing 0.05 mg/mL [POPC](/xray-mp-wiki/reagents/lipids/popc/):[POPG](/xray-mp-wiki/reagents/lipids/popg/):POPA (3:1:1) lipids and 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/)


## Crystallization

### doi/10.1126##science.aao6326

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | 1:1 (v/v) |
| Temperature | 20°C |
| Growth time | 3.5 months |
| Cryoprotection | Directly frozen in liquid N2 |
| Notes | Hexagonal crystals; data collected at APS NE-CAT 24ID-C; microbatch format with 100 nl LCP bolus and ~3.6 ul crystallization solution |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | 1:1 (v/v) |
| Temperature | 20°C |
| Growth time | 1.5 months |
| Notes | 2-BP modified C263A hDHHC20 crystals; data collected at APS GM/CA-CAT 23ID-D |

| Parameter | Value |
|---|---|
| Method | [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) |
| Protein sample | zfDHHS15 (zebrafish DHHC15 C153S mutant) |
| Reservoir | 50 mM MES pH 6.5, 50 mM NaH2PO4, 30.3% [PEG](/xray-mp-wiki/reagents/additives/peg/) 300, 50 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/), 2.5% 2,5-Hexanediol |
| Temperature | 20°C |
| Growth time | 3 months |
| Notes | P21 crystal form; data collected at APS GM/CA-CAT 23ID-B |


## Biological / Functional Insights

### Active site at membrane-cytosol interface enables thioester-exchange chemistry

The DHHC active site is positioned at the membrane-aqueous interface, with
the catalytic cysteine (Cys156) protruding toward the membrane. The aspartic
acid (Asp154) and the first histidine (His154) of the DHHC motif form a
catalytic triad-like arrangement that activates the nucleophilic cysteine for
attack on the acyl-CoA thioester. The second histidine (His155) coordinates
a Zn2+ ion and positions the catalytic cysteine. This organization explains
why substrate cysteines must be membrane-proximal for palmitoylation.

### Acyl chain binding cavity and chain-length selectivity

The transmembrane domain forms a hydrophobic cavity where the acyl chain of
acyl-CoA inserts. Residues from all four TM helices line the cavity, with
Trp28, Trp158, Phe171, Phe174, and Leu227 making critical contacts. Mutation
of Tyr181 to alanine shifts preference from C16 (palmitoyl) toward C18
(stearoyl)-CoA, while S29F mutation increases short-chain preference. The
Tyr181-Ser29 pair closes off the cavity; breaking this interaction allows
longer acyl chains. This enabled engineering of mutants with altered
acyl-CoA selectivity.

### C-terminal domain with amphipathic helix and hydrophobic loop

The C-terminal domain contains a conserved amphipathic helix (alpha'2)
that contacts TM3 and TM4, providing local stability. A conserved TTXE
motif (Thr240, Thr241, Glu243) forms critical interactions with the active
site. The PaCCT motif, with highly conserved Phe259 and Asn266, forms a
packing core. A hydrophobic loop inserts into the lipid bilayer and forms
contacts with TM3 and TM2. Deletion of Trp267 (homologous to a residue
causing depilation in mice when deleted in DHHC21) results in negligible
catalytic activity.


## Cross-References

- [DHHC Palmitoyltransferase Family](/xray-mp-wiki/concepts/protein-families/dhhc-palmitoyltransferase-family/) — hDHHC20 is a member of the DHHC family of S-acyltransferases
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Used for purification and stabilization of hDHHC20 (1 mM in affinity, 0.5 mM in SEC)
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Used as LCP host lipid for crystallization of hDHHC20
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Method used in structure determination or purification
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Additive used in purification or crystallization buffers
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/) — Additive used in purification or crystallization buffers
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — Additive used in purification or crystallization buffers
