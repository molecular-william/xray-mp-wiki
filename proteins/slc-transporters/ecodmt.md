---
title: EcoDMT - Eremococcus coleocola NRAMP Divalent Metal Transporter
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.51913, doi/10.1038##ncomms14033]
verified: false
---

# EcoDMT - Eremococcus coleocola NRAMP Divalent Metal Transporter

## Overview

EcoDMT is a prokaryotic divalent metal transporter from Eremococcus coleocola belonging to the SLC11/NRAMP family. It catalyzes H+-coupled Mn2+ symport and serves as a structural homologue of human DMT1 (SLC11A2), the primary transporter of dietary ferrous  in enterocytes. EcoDMT adopts the  fold characteristic of the [APC Superfamily (Amino Acid-Polyamine-Organocation Transporter Family)](/xray-mp-wiki/concepts/transport-mechanisms/apc-superfamily/), consisting of two topologically related units of five transmembrane helices arranged with opposite orientation. The crystal structure of EcoDMT in complex with the brominated bis-isothiourea inhibitor Br-BIT (PDB 6TL2, 3.8 A) reveals the inhibitor bound to the outward-facing aqueous cavity at the base of a funnel-shaped pocket, with the proximal isothiourea group positioned in direct contact with the metal ion coordination site. This structural characterization, combined with functional studies on both EcoDMT and human DMT1, provides the first detailed mechanistic insight into the pharmacology of SLC11/NRAMP transporters.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.51913 | 6TL2 | 3.8 A | C2 | Full-length EcoDMT with C-terminal His10-tag (cleaved for crystallization) | Br-BIT (3,5-bis-isothiourea-1-bromobenzene) |
| doi/10.1038##ncomms14033 | not specified in paper | 3.3 A | C2 | Full-length EcoDMT, residues 13-506, outward-facing conformation, wildtype | None (apo form) |
| doi/10.1038##ncomms14033 | not specified in paper | 3.6 A | C2 | Selenomethionine-derivatized EcoDMT, residues 13-506, outward-facing conformation | SeMet (for anomalous phasing) |
| doi/10.1038##ncomms14033 | not specified in paper | 3.6 A | C2 | EcoDMT E129Q mutant, outward-facing conformation | None |
| doi/10.1038##ncomms14033 | not specified in paper | 3.9 A | C2 | EcoDMT E129A mutant, outward-facing conformation | None |
| doi/10.1038##ncomms14033 | not specified in paper | 3.7 A | C2 | EcoDMT H236A mutant, outward-facing conformation | None |

## Expression and Purification

- **Expression system**: Escherichia coli MC1061
- **Construct**: EcoDMT with C-terminal 3C protease cleavage site and His10-tag, cloned in pBXC3GH/pBXC3H vectors

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure cell disruption | -- | 20 mM  pH 7.5, 150 mM NaCl | Lysis buffer supplemented with 1 mg/mL lysozyme and 20 ug/mL DNase I. HPL6 high-pressure cell disruptor. |
| Membrane isolation | Differential centrifugation | -- | 20 mM  pH 7.5, 150 mM NaCl | Low-spin at 10,000 x g for 20 min, then ultracentrifugation at 200,000 x g for 1 hr |
| Membrane solubilization | Detergent extraction | -- | 20 mM  pH 7.5, 150 mM NaCl, 10% (w/v)  + 1-2% (w/v)  (or 0.04%  for ITC samples) | Membranes resuspended and extracted, cleared by centrifugation |
| IMAC | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-Sepharose | 20 mM  pH 7.5, 150 mM NaCl, 8.7% (w/v)  + 0.1% (w/v)  (or 0.04%  for ITC) | Tag cleaved with HRV-3C protease at 5:1 protein:protease ratio for 2 hr during dialysis. Second IMAC step to separate cleaved protein. |
| SEC | [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | Superdex 200 (GE Healthcare) | 20 mM  pH 7.5, 150 mM NaCl, 8.7% (w/v) , 0.1% (w/v)  + 0.1% (w/v)  | Final purification step. Peak fractions pooled and concentrated. |


## Crystallization

### doi/10.7554##eLife.51913

| Parameter | Value |
|---|---|
| Method | [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/sitting-drop-vapor-diffusion/) |
| Protein sample | EcoDMT at 7-10 mg/mL in 20 mM  pH 7.5, 150 mM NaCl, 8.7% , 0.1%  |
| Reservoir | 50 mM  Hcl]] pH 8.0-9.0, 22-26%  400 (v/v) |
| Temperature | 4 C |
| Growth time | ~2 weeks |
| Cryoprotection | Not specified |
| Notes | 24-well plates, 1 uL protein + 1 uL reservoir equilibrated against 500 uL reservoir. Inhibitor soaks: Br-BIT and oBr-BIT soaked into pre-grown crystals. Data collected at Swiss Light Source beamlines X06SA and X06DA at wavelength 0.92 A (bromine anomalous edge). 3.8 A resolution. |


## Biological / Functional Insights

### Competitive inhibitor binding at the metal coordination site

The crystal structure of EcoDMT in complex with Br-BIT (PDB 6TL2) at 3.8 A reveals the inhibitor bound at the base of a funnel-shaped extracellular aqueous pocket leading to the metal ion coordination site. The proximal isothiourea group of Br-BIT is positioned in direct interaction distance with Asp51 of the conserved metal binding site, explaining the competitive inhibition mechanism. The distal isothiourea group is not resolved in the electron density, reflecting its conformational flexibility.

### Outward-facing locked conformation

Br-BIT binding locks EcoDMT in the substrate-free outward-facing conformation. By occupying the metal binding pocket, the inhibitor prevents substrate loading and the subsequent conformational transition to the inward-facing state. The compound is positively charged and poorly membrane permeable, consistent with binding from the extracellular side.

### Species-dependent binding at the distal pocket

Mutagenesis of residues on alpha-helix 11 (Asn456, Ser459, Gln463) in EcoDMT shows only small effects on inhibition (2-fold Ki increase), whereas equivalent mutations in human DMT1 (S476V, N520L, F523A) cause 10-100 fold reductions in potency. This indicates stronger, more specific interactions at the distal side of the binding pocket in the human transporter compared to the prokaryotic homologue, reflecting the poor conservation of residues on alpha-11.

### Structure-activity relationship of bis-isothiourea compounds

Seven bis-isothiourea compounds with varying aromatic scaffolds were characterized. TEBIT and TMBIT are the most potent (IC50 0.27-0.35 uM on hDMT1). The brominated compounds Br-BIT (4.66 uM) and Br-DBFIT (1.24 uM) show intermediate potency. Replacement of isothiourea groups with bulkier thio-2-imidazoline groups severely reduces potency (IC50 161 uM), confirming the critical role of the isothiourea moiety for metal binding site interaction.

### No metal chelation by inhibitors

[ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) confirmed that bis-isothiourea compounds do not chelate divalent metal ions (Mn2+), ruling out indirect inhibition via substrate sequestration. The inhibition arises from direct protein-inhibitor interactions.

### Outward-Facing Conformation of EcoDMT Reveals the SLC11 Transport Cycle

The crystal structure of EcoDMT at 3.3 A resolution (ncomms14033) reveals the first outward-facing conformation of any SLC11/NRAMP family member. The protein comprises 12 transmembrane helices (compared to 11 in ScaDMT), with the additional C-terminal helix 12 located at the periphery. The transporter displays a pseudo-symmetric relationship between two structurally analogous domains (helices 1-5 and 6-10). Comparison with the inward-facing ScaDMT structure defines the conformational changes underlying transition-metal ion transport by the alternate-access mechanism, involving movements of helices 1 and 6 around a hinge at the ion-binding region.

### Proton-Coupled Mn2+ Transport in EcoDMT

EcoDMT mediates proton-coupled uptake of Mn2+ with a KM of 18.2 uM (at pH 7.2). Transport is coupled to H+ cotransport, analogous to human DMT1. The transition-metal ion-binding site at the center of the transporter is composed of residues Asp51, Asn54, Met234, and a backbone carbonyl from helix 6a. Mutants of these binding site residues (D51A, N54A, M234A) severely affect or abolish both Mn2+ and H+ transport, and no uncoupled proton leak was observed, confirming that H+ transport requires conformational changes of the ion-binding site.

### His236 as the Primary Proton Acceptor

A conserved histidine on alpha-helix 6b (His236 in EcoDMT, His267 in human DMT1) was identified as the likely primary proton acceptor. Mutation H236A preserves Mn2+ transport (KM 18.1 uM, Vmax reduced to ~50% of WT) but severely disrupts H+ transport, effectively uncoupling metal ion transport from proton cotransport. In the outward-facing structure, His236 is located near the surface of the aqueous path leading to the transition-metal ion-binding site. In the inward-facing structure (ScaDMT), it is positioned at the crossroad of two potential intracellular proton exit pathways. Glu129 was also investigated as a potential proton acceptor, but the conservative E129Q mutation (retaining H-bonding ability) showed WT-like behavior, ruling out Glu129 as the primary H+ acceptor.

### H+-Coupled Transport Mechanism in the SLC11 Family

The combined structural data from EcoDMT (outward-facing) and ScaDMT (inward-facing) define the alternating-access mechanism for H+-coupled transition-metal ion transport. Two scenarios are proposed for proton coupling: (1) the proton is released via the main metal ion exit path together with Mn2+, or (2) the proton exits via a narrow side tunnel lined by conserved acidic and basic residues (Glu119, Asp126, Glu129 on helix 3; Arg368, Arg369, Arg373 on helix 9 in EcoDMT). The acidic and basic residues lining the narrow aqueous cavity are conserved among SLC11 family members but absent from LeuT and other Na+-coupled transporters, suggesting a specialized proton exit pathway unique to the SLC11 family.


## Cross-References

- [Deinococcus radiodurans Nramp (DraNramp)](/xray-mp-wiki/proteins/slc-transporters/dra-nramp/) — Related SLC11/NRAMP family transporter with high-resolution structures of the transport cycle
- [ScaDMT](/xray-mp-wiki/proteins/slc-transporters/sca-dmt/) — Related SLC11/NRAMP family transporter from Staphylococcus capitis
- [SLC11 (NRAMP) Family](/xray-mp-wiki/concepts/protein-families/slc11-nramp-family/) — EcoDMT is a member of the SLC11/NRAMP family of divalent metal transporters
- [LeuT Return State Mechanism](/xray-mp-wiki/concepts/miscellaneous/leut-return-state-mechanism/) — EcoDMT adopts the LeuT fold characteristic of the APC superfamily
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Crystallization method used to grow EcoDMT crystals
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used for purification and crystallization
- [Leut](/xray-mp-wiki/proteins/enzymes/leut/) — Referenced in ecodmt text
- [Iron](/xray-mp-wiki/reagents/iron/) — Referenced in ecodmt text
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in ecodmt text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in ecodmt text
