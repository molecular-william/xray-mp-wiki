---
title: "O. sativa SWEET2b (OsSWEET2b)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature15391]
verified: false
---

# O. sativa SWEET2b (OsSWEET2b)

## Overview

OsSWEET2b is a vacuolar glucose transporter from the SWEET family found in rice (Oryza sativa). It is a seven-transmembrane-helix protein composed of two triple-helix bundles (THBs) connected by an inversion linker helix (TM4), forming an asymmetrical transport pathway in an inward-open conformation. OsSWEET2b assembles as a homo-trimer in the membrane, with each protomer containing its own transport route. The structure reveals a conserved proline tetrad that functions as hinges for gating and an asymmetrical substrate-binding pocket that diverges from the symmetrical architecture of ancestral bacterial SemiSWEETs.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature15391 | 5CTG | 3.1 | P2_1 | OsSWEET2b(deltaC15)-3C-EGFP-His; reductive methylation | -- |
| doi/10.1038##nature15391 | 5CTH | 3.7 | P2_1_2_1 | OsSWEET2b(deltaC15)-3C-EGFP-His; reductive methylation | -- |

## Expression and Purification

- **Expression system**: Pichia pastoris (native); sf9 insect cells (SeMet)
- **Construct**: OsSWEET2b(deltaC15)-3C-EGFP-His; C-terminal 15 disordered residues removed
- **Induction**: OD600 10 at 27 C for native; 48 h at 27 C for sf9

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane extraction | Detergent extraction | -- | 3% [DDM](/xray-mp-wiki/reagents/detergents/ddm) with protease inhibitor cocktail | 4 C for 2 h |
| Centrifugation | Centrifugation | -- | -- | 16,000 rpm for 45 min to remove insoluble |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [Cobalt](/xray-mp-wiki/reagents/affinity-resins/cobalt-resin) resin | 0.3% [DM (n-decyl-beta-D-maltoside)](/xray-mp-wiki/reagents/detergents/dm), 20 mM imidazole | 4 C for 2 h; cleaved with 3C protease |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [Gel Filtration](/xray-mp-wiki/methods/purification/gel-filtration) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200) | 10 mM Tris-HCl pH 8.0, 150 mM NaCl, 0.5% [NG (n-nonyl-beta-D-glucopyranoside)](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-maltopyranoside) | Protein concentrated to 10 mg/mL for crystallization |


## Crystallization

### doi/10.1038##nature15391

| Parameter | Value |
|---|---|
| Method | [Hanging Drop](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion) [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | OsSWEET2b(deltaC15) in 0.5% NG |
| Reservoir | 30% PEG 400, 0.1 M MES pH 6.5, 10 mM MnCl2, 5% ethanol |
| Temperature | 22 |
| Growth time | -- |
| Notes | Form I (P2_1) plate-like crystals; directly flash-frozen without cryoprotectant |

| Parameter | Value |
|---|---|
| Method | [Hanging Drop](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion) [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | OsSWEET2b(deltaC15) in 0.5% NG |
| Reservoir | 27% PEG 400, 0.1 M MES pH 6.0 |
| Temperature | 22 |
| Growth time | -- |
| Notes | Form II (P2_1_2_1) cubic crystals; cryo-protected by gradual PEG400 concentration increase to 44% |


## Biological / Functional Insights

### Asymmetrical THB architecture

OsSWEET2b consists of two triple-helix bundles (THBs) connected by an inversion linker helix (TM4). Unlike symmetric bacterial SemiSWEET homodimers, the two THBs in eukaryotic SWEETs have diverged to create an asymmetrical binding pocket. THB1 (TM1-3) and THB2 (TM5-7) are structurally divergent, with THB1 bending to accommodate TM4. The TM4 inversion linker connects the two THBs in opposite orientation, enabling covalent fusion of the ancestral dimer into a single polypeptide chain.

### Homo-trimeric assembly

OsSWEET2b forms a homo-trimer with each protomer containing an independent transport pathway. The trimer interface involves TM4 of one protomer interacting with TM5 and TM7 of the neighboring protomer, burying ~1700 A2 between protomers. Trimer formation was confirmed by glutaraldehyde cross-linking, site-directed disulfide cross-linking in both detergent and membranes, and co-immunoprecipitation. The quaternary structure was observed in two distinct crystal forms.

### Proline tetrad gating mechanism

Four conserved proline residues (one in each of TM1, TM2, TM5, and TM6) line the transport pathway at the intrafacial (cytosolic) side. These prolines terminate or kink the respective helices and face the transport route at a similar membrane depth. Mutagenesis of all four prolines in AtSWEET1 (P23A, P43A, P145A, P162A) abolished transport activity, suggesting they function as molecular hinges enabling concerted structural rearrangements during the transport cycle.

### Extrafacial gate and asymmetrical binding pocket

The extrafacial (luminal) gate is formed by Tyr61, Asp190, Gln132, and Ile193 in OsSWEET2b. Tyr61 hydrogen-bonds with Asp190 and interacts with Gln132 to seal the cavity from the luminal side. In the binding pocket, two conserved asparagines (Asn77 and Asn197) are essential for transport, while only one aromatic residue (Phe181 in THB2, corresponding to Trp176 in AtSWEET1) is required — contrasting with the paired tryptophans in symmetric SemiSWEETs. This confirms the asymmetrical nature of the eukaryotic SWEET binding pocket.

### Dominant-negative gate mutations

Mutations in the extrafacial gate (V188A) and intrafacial gate (P23T) of AtSWEET1 cause dominant-negative inhibition of co-expressed wild-type transporter, indicating allosteric coupling between protomers in the trimer. This suggests that conformational states are coupled among SWEET protomers, similar to cooperative transport observed in GLUT1 tetramers and AMT transporters.


## Cross-References

- [E. coli SemiSWEET (EcSemiSWEET)](/xray-mp-wiki/proteins/miscellaneous/ec-semisweet/) — Bacterial homolog with inward-open and outward-open structures; shares conserved binding pocket residues and PQ-loop hinge
- [A. thaliana SWEET1](/xray-mp-wiki/proteins/miscellaneous/a-thaliana-sweet1/) — Closely related plant SWEET used for structure-function mutagenesis studies
- [TySemiSWEET](/xray-mp-wiki/proteins/miscellaneous/tysemisweet/) — Bacterial SemiSWEET homolog with conserved structural features
- [LbSemiSWEET](/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/) — Bacterial SemiSWEET homolog with outward-open and occluded structures
- [SWEET Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/sweet-transporter/) — OsSWEET2b is a eukaryotic member of the SWEET family
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for membrane extraction
- [DM (n-decyl-beta-D-maltoside)](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used in wash buffer during purification
- [NG (n-nonyl-beta-D-glucopyranoside)](/xray-mp-wiki/reagents/detergents/nm/) — Detergent used in gel filtration and crystallization
