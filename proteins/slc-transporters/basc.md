---
title: BasC (Bacterial Alanine-Serine-Cysteine Exchanger)
created: 2026-06-09
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-09837-z]
verified: false
---

# BasC (Bacterial Alanine-Serine-Cysteine Exchanger)

## Overview

BasC is a bacterial L-amino acid transporter (LAT) from the alanine-serine-cysteine exchanger family, a prokaryotic homolog of human heteromeric amino acid transporters (HATs). LATs are obligatory exchangers with asymmetric substrate affinity (high extracellular, low intracellular), a key feature enabling regulation of intracellular amino acid pools. Crystal structures of BasC in complex with nanobody 74 (Nb74) were determined in both apo and substrate (2-aminoisobutyric acid, 2-AIB) bound forms at 2.9 and 3.4 A resolution, respectively, revealing a non-occluded inward-facing conformation. Two conserved residues, Tyr236 (TM7) and Lys154 (TM5), are responsible for the asymmetric substrate interaction. This work fills a gap in the knowledge of the transport cycle of APC superfamily transporters and provides a structural framework for understanding human LATs.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-019-09837-z | 6F2G | 2.9 | C2 | BasC-Nb74 complex (apo) | None (apo) |
| doi/10.1038##s41467-019-09837-z | 6F2W | 3.4 | Not specified | BasC-Nb74 complex (2-AIB bound) | 2-aminoisobutyric acid (2-AIB) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21-CodonPlus-RIPL
- **Construct**: Full-length BasC from unclassified Enterococcus species with N-terminal His10-GFP-TEV tag

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell lysis by French press, ultracentrifugation | — | 20 mM Tris-Base, 150 mM NaCl, pH 7.4, 10% glycerol | Membrane pellet resuspended at 8-12 mg/mL protein, flash-frozen and stored at -80 C |
| Solubilization | Detergent extraction | — | 20 mM Tris-Base, 150 mM NaCl, pH 7.4, 10% glycerol + 2% (w/v) n-decyl-beta-D-maltopyranoside (DM) | 1 h solubilization at 4 C |
| Ni-NTA affinity chromatography | Immobilized metal-affinity chromatography | Ni-NTA Superflow beads | 20 mM Tris-Base, 150 mM NaCl, pH 7.4, 0.17% DM, 10% glycerol, 20 mM imidazole | On-column cleavage with HRV-3C protease for 16 h. Cleaved BasC collected in flow-through. |
| Nanobody incubation and size-exclusion chromatography | Gel filtration | Superdex 200 10/300 GL | 20 mM Tris-Base, 150 mM NaCl, pH 7.4, 0.17% DM | BasC incubated with nanobody Nb74 at 1:1.2 molar ratio overnight before SEC. For 2-AIB-bound protein, all buffers contained 100 mM 2-AIB. |


## Crystallization

### doi/10.1038##s41467-019-09837-z

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | BasC-Nb74 complex in DM at ~6 mg/mL |
| Reservoir | 100 mM MES pH 6.0-6.5, 200 mM NaCl, 30% PEG 5000 MME (apo); 100 mM Na citrate pH 5.5-5.6, 200 mM (NH4)2SO4, 20-25% PEG 4000 (holo) |
| Temperature | 20 C |
| Notes | Selenomethionine-labeled protein used for experimental phasing. Apo crystals diffracted to 2.9 A (space group C2), 2-AIB-bound crystals to 3.4 A. |


## Biological / Functional Insights

### Nb74 reveals sidedness of substrate interaction

Nanobody 74 binds exclusively to the cytoplasmic side of BasC, blocking efflux but not influx of L-alanine. By inhibiting inside-out oriented BasC in proteoliposomes, Nb74 enables kinetic characterization of the extracellular side alone, revealing high apparent affinity (Km ~50 uM) versus low intracellular affinity (Km ~2 mM).

### Substrate binding site in unwound TM1 and TM6

2-AIB binds at the unwound segments of TM1 and TM6. The alpha-carboxyl forms H-bonds with backbone N-atoms of Ala20 and Gly21 (TM1). The alpha-amino group bonds with carbonyls of Val17 (TM1) and Phe199, Ala200, Asp202 (TM6). The alpha-amino and alpha-carboxyl groups are essential substrate requirements, as demonstrated by inability to exchange with acetate or ethylamine.

### Substrate-induced fit mechanism

Upon 2-AIB binding, Gly19 (TM1 unwound region) shifts by 2 A to form an H-bond with Ser282 (TM8). MD simulations show that substrate dissociation is accompanied by relaxation of the TM1 unwound segment, supporting a substrate-induced fit mechanism.

### Tyr236 partially mediates substrate asymmetry

Tyr236 (TM7) is positioned at the Na1 site equivalent of sodium-dependent APC transporters. Mutation Y236F in BasC (and homologous Y280F in human Asc-1) selectively increases the cytoplasmic apparent affinity (Km(i) from ~2 mM to ~560 uM), making the transporter more symmetric without affecting extracellular affinity or Vmax.

### Lys154 supports high extracellular affinity

Lys154 (TM5) at the Na2 site equivalent interacts with Gly15 (TM1a C-terminus). Mutation K154A reduces extracellular affinity ~10-fold (to ~474 uM) and dramatically reduces Vmax (~1/20 of WT), while leaving intracellular affinity unchanged. This turns BasC into a more symmetric transporter with mM-range affinity on both sides. The homologous K194A mutation in human Asc-1 produces similar effects.

### Substrate release to cytoplasm

MD simulations show 2-AIB can dissociate from the binding site and interact simultaneously with the epsilon-amino group of Lys154 and the backbone carbonyl of Thr16 (TM1a), suggesting a pathway for substrate release to the cytoplasm.

### Comparison with GkApcT reveals occlusion mechanism

Comparison of BasC (non-occluded inward-facing) with GkApcT (occluded inward-facing) shows that tilting of TM1a and TM6b, together with accompanying TM7 movement, closes the substrate vestibule at the cytoplasmic side. TM1a-TM5 interaction is key for the occlusion process.

### Structural framework for human LATs

BasC provides the first atomic-resolution structure of a LAT family transporter. The low sequence identity (14-22%) between bacterial APC transporters and human LATs limits model reliability. BasC fills this gap, enabling structure-function analysis of human LATs, including mutations causing autism (LAT1), hearing loss (LAT2), and lysinuric protein intolerance (y+LAT1 K191E corresponds to BasC K154E).


## Cross-References

- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — BasC is an obligatory exchanger using alternating access for amino acid transport
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer component throughout purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used in Ni-NTA affinity chromatography
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Ni-NTA IMAC used for initial purification
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC used as final polishing step and for nanobody complex formation
- [Single-Wavelength Anomalous Diffraction (SAD)](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — Apo structure solved by Se-Met SAD phasing
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Holo structure solved by MR using apo model
- [French Press](/xray-mp-wiki/methods/cell-lysis/french-press/) — Used for cell lysis in BasC purification
- [AdiC](/xray-mp-wiki/proteins/slc-transporters/adic/) — Distant bacterial APC superfamily homolog, used for structural comparison
- [Selenomethionine](/xray-mp-wiki/reagents/additives/selenomethionine/) — SeMet-labeled protein used for SAD phasing
