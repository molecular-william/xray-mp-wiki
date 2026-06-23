---
title: E. coli YidC Membrane Protein Chaperone and Insertase
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##srep07299]
verified: false
---

# E. coli YidC Membrane Protein Chaperone and Insertase

## Overview

YidC is an evolutionarily conserved membrane protein from the YidC/Oxa1/Alb3 family
that functions as both a membrane protein chaperone (in cooperation with the Sec
translocon) and an independent insertase for membrane proteins. In Gram-negative
bacteria, YidC interacts with [Secyeg](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) and SecDFYajC to form the holo-translocon
complex. The crystal structure of full-length Escherichia coli YidC (EcYidC) at
3.2 Å resolution revealed a hydrophilic groove formed by five transmembrane helices
that is the central functional feature, providing a hydrophilic binding surface for
nascent membrane proteins during folding and insertion.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##srep07299 | 3WVF | 3.2 |  | Full-length EcYidC (residues 2-540) with C-terminal LESSGENLYFQGQFTS-H8 tag, TEV-cleaved |  |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)
- **Construct**: EcYidC2-540 cloned into modified pTV118N vector with C-terminal His8 tag and TEV cleavage site
- **Induction**: 1 mM IPTG for 18 hours at 37°C
- **Media**: LB medium (10 L) supplemented with 50 μg/ml ampicillin

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Ultracentrifugation |  | See reference for details | Total membranes prepared as described previously |
| Solubilization | Detergent extraction |  | 20 mM ADA-NaOH pH 5.6, 300 mM NaCl, 0.1 mM [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/) + 2% n-decyl-β-D-maltoside ([DM](/xray-mp-wiki/reagents/detergents/dm/)) | Solubilized for 1 h at 4°C, then ultracentrifuged at 138,000 × g |
| Ni-affinity chromatography | Immobilized metal affinity chromatography | Ni Sepharose excel (GE Healthcare) | 20 mM ADA-NaOH pH 5.6, 300 mM NaCl, 0.25% [DM](/xray-mp-wiki/reagents/detergents/dm/), 30-500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient + 0.25% [DM](/xray-mp-wiki/reagents/detergents/dm/) | Equilibrated with buffer containing 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), eluted with 100-500 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) gradient |
| TEV cleavage and buffer exchange | Affinity tag removal | Ni Sepharose excel | 20 mM ADA-NaOH pH 5.6, 300 mM NaCl, 0.25% [DM](/xray-mp-wiki/reagents/detergents/dm/), 10 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.25% [DM](/xray-mp-wiki/reagents/detergents/dm/) | C-terminal His8 tag cleaved by His-tagged TEV protease for 12 h at 4°C; flow-through collected |
| Size-exclusion chromatography | SEC | HiLoad 16/600 Superdex 200 (GE Healthcare) | 20 mM ADA-NaOH pH 5.6, 300 mM NaCl, 0.25% [DM](/xray-mp-wiki/reagents/detergents/dm/) + 0.25% [DM](/xray-mp-wiki/reagents/detergents/dm/) | Final purification step |


## Crystallization

### doi/10.1038##srep07299

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified EcYidC in 20 mM ADA-NaOH pH 5.6, 300 mM NaCl, 0.25% [DM](/xray-mp-wiki/reagents/detergents/dm/) |
| Reservoir | See crystallization conditions (not specified in detail in text) |
| Temperature | 20°C |
| Notes | Structure solved by molecular replacement using BhYidC structure (PDB 3WO6) as search model; refined to 3.2 Å resolution with Rwork=22.1% and Rfree=27.7% |


## Biological / Functional Insights

### Hydrophilic groove as chaperone and insertase site

The EcYidC structure revealed that five core TM helices (TM2-TM6) form a
hydrophilic groove open toward both the cytoplasmic and membrane sides through
a gap between TM3 and TM5. This groove contains conserved hydrophilic residues
including Thr362, Arg366, Thr373, Gln429, Thr474, Ser520, Asn521, and Gln527.
The highly conserved Arg366 generates a positively-charged surface in the groove.
Substrate-contacting residues, identified by cross-linking analyses with
Sec-independent substrates (Pf3 coat protein, Foc, MifM), map to the groove
interior and the adjacent TM3/TM5 surface, highlighting the importance of both
hydrophilic and hydrophobic interactions.

### P1 domain orientation and holo-translocon interactions

The full-length EcYidC structure showed that the P1 periplasmic domain (residues
59-320) adopts a β-supersandwich fold connected to the TM region by the PH1
amphipathic helix. The P1 domain is oriented away from the membrane with its
cleft facing the periplasm, suggesting it may bind periplasmic molecules. A
conserved surface on the P1 domain (residues 215-265, including Lys249) interacts
with SecF, and the TM3 helix surface provides interaction sites for the TM regions
of Sec proteins, providing structural insight into the holo-translocon (SecYEG-
SecDFYajC-YidC) organization.


## Cross-References

- [Secyeg](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) — Referenced in context related to Secyeg
- [DM](/xray-mp-wiki/reagents/detergents/dm/) — Referenced in context related to DM
- [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/) — Referenced in context related to Pmsf
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in context related to Imidazole
