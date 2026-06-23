---
title: AaWzmWzt (O Antigen ABC Transporter from Aquifex aeolicus)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-08646-8, doi/10.1016##j.str.2019.11.020]
verified: false
---

# AaWzmWzt (O Antigen ABC Transporter from Aquifex aeolicus)

## Overview

AaWzmWzt is an [ABC Transporter](/xray-mp-wiki/concepts/abc-transporter-family/) from Aquifex aeolicus responsible for translocating O antigen polysaccharides across the inner membrane in Gram-negative bacteria. The ATP-bound crystal structure (EQ mutant) reveals a continuous transmembrane channel with lateral openings toward the periplasm. The structure shows large structural changes in NBDs and TMDs upon ATP binding, pushing conserved hydrophobic residues at the substrate entry site toward the periplasm. The channel's periplasmic exit is sealed by lipid molecules in a proposed lipid gating mechanism that maintains the membrane permeability barrier. The isolated carbohydrate-binding domain (CBD) of Wzt was determined at 2.65 A resolution, revealing a jelly-roll fold with beta strand exchange between protomers in the dimer. The CBD interacts with the O antigen polysaccharide and may regulate the transporter's ATPase activity.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-019-08646-8 | unknown | 2.7 | — | AaWzmWzt EQ mutant (E164Q) | [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) |
| doi/10.1016##j.str.2019.11.020 | 6O14 | 2.65 | Not specified | Aa Wzt CBD (short construct, residues 245-395) |  |

## Expression and Purification

- **Expression system**: Escherichia coli C43(DE3)
- **Construct**: EQ mutant (Walker B E164Q in Wzt)

### Purification Workflow

*Source: doi/10.1038##s41467-019-08646-8*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Microfluidizer lysis, ultracentrifugation at 200,000 x g | — | 20 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 100 mM NaCl, 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) |  |
| Solubilization | Detergent extraction | — | 50 mM [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) pH 7.2, 100 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 5 mM [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) + 2% (w/v) [Octaethylene Glycol Monododecyl Ether (C12E8)](/xray-mp-wiki/reagents/detergents/c12e8/) | 60 min at 4 C |
| Ni-NTA affinity chromatography | Immobilized metal-affinity chromatography | Ni-NTA agarose | Sequential washes with 22 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 5 mM LDAO, 40 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 5 mM LDAO, 1.5 M NaCl + 22 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 5 mM LDAO | Eluted with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 5 mM LDAO |
| Size-exclusion chromatography | Gel filtration | S200 gel filtration column (GE Healthcare) | 20 mM [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 100 mM NaCl, 5 mM [Magnesium Chloride (MgCl₂)](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 0.5 mM [Tris(2-carboxyethyl)phosphine (TCEP)](/xray-mp-wiki/reagents/additives/tcep/), 5 mM LDAO |  |

### Purification Workflow

*Source: doi/10.1016##j.str.2019.11.020*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Affinity purification | Ni-NTA affinity chromatography | Ni-NTA agarose | 25 mM Tris HCl pH 8.5, 0.5 M NaCl, 30 mM imidazole, 5 mM beta-ME (wash 1); 25 mM Tris HCl pH 8.5, 50 mM NaCl, 50 mM imidazole, 5 mM beta-ME (wash 2) | CBD construct (residues 235-395) with C-terminal hexahistidine tag |
| Size-exclusion chromatography | Gel filtration | Superdex-200 | 25 mM Tris HCl pH 8.5, 50 mM NaCl, 5 mM beta-ME |  |


## Crystallization

### doi/10.1038##s41467-019-08646-8

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | 7.5 mg/ml AaWzmWzt_EQ + 2 mM [Adenosine Triphosphate (ATP)](/xray-mp-wiki/reagents/ligands/atp/) + 5 mM [Magnesium Chloride (MgCl₂)](/xray-mp-wiki/reagents/additives/magnesium-chloride/) |
| Temperature | 20 C |
| Notes | Crystals grown with ATP and magnesium. C12E8 and LDAO were used as detergents throughout purification. |

### doi/10.1016##j.str.2019.11.020

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, sitting drop |
| Protein sample | 7.6 mg/ml Aa CBD (long construct, residues 235-395) or 3.7 mg/ml Aa CBD (short construct, residues 245-395) |
| Reservoir | 0.1 M citric acid pH 5.5, 0.5 M tri-sodium citrate (long construct); 0.1 M MOPS pH 7, 1.5 M sodium acetate (short construct) |
| Temperature | 27-30 C |
| Growth time | 3 days to 3 weeks |
| Cryoprotection | 25% glycerol (long construct); 3 M sodium acetate (short construct) |
| Notes | Long construct crystallized as needle-shaped crystals diffracting to 3.6 A. Truncated construct (lacking 8 N-terminal residues) diffracted to 2.65 A and was used for refinement. Structure determined by molecular replacement using E. coli O9a CBD (PDB 2R5O) as search model. |


## Biological / Functional Insights

### CBD structure reveals dimeric jelly-roll fold

The Aa CBD forms a partially SDS-resistant dimer with each protomer adopting a jelly-roll fold. The dimer is stabilized by beta strand exchange between protomers: C-terminal residues of one protomer complete the jelly-roll fold of the other. The domain contains a conserved flat surface and a variable twisted jelly-roll surface.

### CBD interacts with O antigen via glycan array

Microbial glycan array binding studies with 313 LPS/O antigen structures identified selective binding to Pseudomonas aeruginosa 7a,7d O antigen. The CBD discriminates between 4-acetylated and unmodified FucNAc, suggesting specificity toward the natural O antigen cap structure.

### CBD-NBD interaction may regulate ATPase activity

The CBD likely contacts the NBD at a short alpha helix following the conserved H-loop. CBD binding could perturb the H-loop (containing His199), affecting the transporter's hydrolytic activity. The CBD may function to increase local O antigen concentration near the ABC transporter.


## Cross-References

- [ABC Transporter Family](/xray-mp-wiki/concepts/abc-transporter-family/) — WzmWzt is a type II ABC transporter for O antigen export
- [Type II ABC Transporter Family](/xray-mp-wiki/concepts/type-ii-abc-transporter-family/) — WzmWzt is a member of the type II ABC transporter family
- [Outward-Facing Conformation](/xray-mp-wiki/concepts/outward-facing-conformation/) — The ATP-bound structure represents the outward-facing state
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-NTA affinity chromatography was used for purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC was used as a final purification step
- [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) — Detergent used for solubilization at 2% (w/v)
- [TCEP](/xray-mp-wiki/reagents/additives/tcep/) — Reducing agent in SEC buffer
- [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/) — Reducing agent in purification buffers
- [MgCl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/) — Used in crystallization and SEC buffers
- [ATP](/xray-mp-wiki/reagents/ligands/atp/) — Added for ATP-bound crystallization and structure determination
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer component
- [Sodium Phosphate](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) — Buffer used during solubilization step
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used in Ni-NTA affinity chromatography buffers
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used for structure determination of the ATP-bound state
