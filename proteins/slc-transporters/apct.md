---
title: ApcT Amino Acid Transporter from Methanocaldococcus jannaschii
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1176088]
verified: false
---

# ApcT Amino Acid Transporter from Methanocaldococcus jannaschii

## Overview

ApcT is a 435-amino acid amino acid transporter from the archaeon Methanocaldococcus jannaschii, belonging to the APC (Amino Acid-Polyamine-Organocation) superfamily. It functions as a sodium-independent, proton-coupled amino acid symporter with broad specificity for L-amino acids. The crystal structure was determined at 2.35 Å resolution using [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) SAD phasing, revealing an inward-facing occluded conformation with a [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/)-like fold consisting of 10 transmembrane helices arranged in an inverted repeat.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1176088 | — (see supporting material) | 2.35 | — | Full-length ApcT (residues 1-435) | — |
| doi/10.1126##science.1176088 | — (see supporting material) | 2.35 | — | Full-length ApcT K158A mutant | — |

## Expression and Purification

- **Expression system**: Screening of thermophilic orthologs by FSEC; ApcT from M. jannaschii selected for sharp symmetrical elution profile
- **Construct**: Full-length ApcT (435 residues)
- **Notes**: Expressed with anti-ApcT Fab fragment for stabilization

### Purification Workflow

- **Expression system**: E. coli (expression screening)
- **Expression construct**: Full-length ApcT
- **Tag info**: His-tag (see supporting material)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Fluorescence detection size exclusion chromatography (FSEC) | Screening of thermophilic orthologs | — | — + — | Identified ApcT as promising candidate based on sharp symmetrical elution profile |
| Solubilization | Detergent extraction | — | — + n-octyl-beta-D-thioglucoside | ApcT solubilized in n-octyl-beta-D-thioglucoside (OTG) |
| Complex formation | Fab fragment binding | — | — + — | Complexed with anti-ApcT 7F11 Fab fragment for crystallization |

**Final sample**: Purified ApcT in n-octyl-beta-D-thioglucoside
**Yield**: —
**Purity**: —


## Crystallization

### doi/10.1126##science.1176088

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (see supporting material) |
| Protein sample | ApcT in n-octyl-beta-D-thioglucoside |
| Temperature | — |
| Notes | Crystals grown at pH 9; ApcT alone diffracted to higher resolution than Fab complex |


## Biological / Functional Insights

### Sodium-Independent Proton-Coupled Amino Acid Transport

ApcT is a sodium-independent, broad-specificity amino acid transporter active at acidic pH. Transport is coupled to a proton gradient, as shown by inhibition of transport when the pH gradient is collapsed by proton/potassium ionophores. Substrate uptake does not require sodium or a sodium gradient.

### Substrate Specificity and Binding Pocket

ApcT transports a wide range of L-amino acids (L-Glu, L-Ala, L-Ser, L-Gln, L-Phe) but transports Gly and Trp very slowly. The substrate binding pocket (~195 Å³) is large enough to accommodate phenylalanine but not tryptophan. The pocket is lined by polar, aromatic, and aliphatic residues from TMs 1, 3, 6, and 8, with hydrogen bonding interactions between substrate amino/carboxyl groups and main-chain carbonyl/amide moieties.

### Lys158 as Proton Sensor

Lys158 (TM5) is situated between TMs 1 and 8, forming hydrogen bonds to the main-chain carbonyl of Gly19 (TM1) and hydroxyl of Ser283 (TM8). Based on structural alignment with [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/), the amine of Lys158 superimposes on the Na2 ion of [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/). The K158A mutant showed no measurable transport activity, supporting the hypothesis that Lys158 undergoes reversible protonation/deprotonation during the transport cycle, acting as a proton sensor that modulates the conformation of TM1 and the opening/closing of extracellular and intracellular gates.

### Inward-Facing Occluded Conformation

The ApcT structure represents a substrate-free, inward-facing yet occluded conformation. Three lines of evidence support this: (1) a solvent-accessible path from the cytoplasmic side to Lys158; (2) TM1 conformation that occludes access to the outside but partially opens to the inside; (3) a belt of water molecules at the extracellular face with a solvent-free swath separating it from the putative substrate binding pocket. This apo conformation resembles the substrate-bound occluded state of [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/), demonstrating that occluded state formation does not require bound substrate.

### Structural Comparison with LeuT and AdiC

ApcT adopts the [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/)-like fold with two inverted repeats of five transmembrane helices. Structural superposition shows that ApcT aligns well with [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/), but less well with [V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)](/xray-mp-wiki/proteins/slc-transporters/vsglt/), [Mhp1 Benzyl-Hydantoin Transporter from Microbacterium liquefaciens](/xray-mp-wiki/proteins/slc-transporters/mhp1/), and [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/). Comparison with the [AdiC Arginine/Agmatine Antiporter](/xray-mp-wiki/proteins/slc-transporters/adic/) structure (PDB 3H5M) revealed significant discrepancies in TMs 6-8, suggesting the [AdiC Arginine/Agmatine Antiporter](/xray-mp-wiki/proteins/slc-transporters/adic/) sequence is off-register by ~4 residues in these regions.


## Cross-References

- [APC Superfamily (Amino Acid-Polyamine-Organocation Transporter Family)](/xray-mp-wiki/concepts/transport-mechanisms/apc-superfamily/) — ApcT is a member of the APC superfamily
- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/) — LeuT shares the same structural fold and was used for structural comparison
- [AdiC Arginine/Agmatine Antiporter](/xray-mp-wiki/proteins/slc-transporters/adic/) — AdiC is an APC superfamily member compared structurally to ApcT
- [V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)](/xray-mp-wiki/proteins/slc-transporters/vsglt/) — vSGLT shares the LeuT-like fold and was compared in the structural analysis
- [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/) — BetP occluded conformation was compared to ApcT inward-facing occluded state
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — ApcT structure supports the alternating access model for secondary transporters
- [Rocking-Bundle Mechanism](/xray-mp-wiki/concepts/structural-mechanisms/rocking-bundle-mechanism/) — ApcT structural transitions are consistent with the rocking-bundle model
- [X-ray Crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/) — Method used in the study
- [APC Superfamily (Amino Acid-Polyamine-Organocation Transporter Family)](/xray-mp-wiki/concepts/transport-mechanisms/apc-superfamily/) — Key concept related to this protein
- [Rocking-Bundle Mechanism](/xray-mp-wiki/concepts/structural-mechanisms/rocking-bundle-mechanism/) — Key concept related to this protein
