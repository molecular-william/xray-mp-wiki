---
title: RsTSPO Translocator Protein from Rhodobacter sphaeroides
created: 2026-06-10
updated: 2026-06-10
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1126##science.1260590]
verified: false
---

# RsTSPO Translocator Protein from Rhodobacter sphaeroides

## Overview

The 18-kDa translocator protein (TSPO) from *Rhodobacter sphaeroides* (RsTSPO) is a bacterial homolog of the mammalian TSPO, a key player in [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) transport into mitochondria and a major target for diagnostic imaging and therapeutic intervention. Crystal structures were determined at 1.8-2.5 Å resolution for wild-type and the A139T mutant (mimicking the human A147T polymorphism associated with psychiatric disorders). All structures show a tightly interacting parallel dimer formed by five-transmembrane-helix monomers. The A139T mutation causes conformational changes in TM-II and TM-V that alter the [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) recognition consensus sequence (CRAC) site and reduce ligand binding affinity. An endogenous porphyrin ligand is bound in a cavity between TM-I and TM-II, and an external surface transport mechanism is proposed.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.1260590 | 4UC3 | 2.5 | P2₁ | Wild-type RsTSPO |  |
| doi/10.1126##science.1260590 | 4UC1 | 1.8 | C2 | A139T mutant |  |
| doi/10.1126##science.1260590 | 4UC2 | 2.4 | P2₁2₁2₁ | A139T mutant |  |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: RsTSPO wild-type and A139T mutant

### Purification Workflow

- **Expression system**: E. coli

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — |  | Purified RsTSPO used for ligand binding studies and crystallization |


## Crystallization

### doi/10.1126##science.1260590

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | Not specified |
| Notes | Crystals obtained in three different space groups. [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) and [PK11195](/xray-mp-wiki/reagents/ligands/pk11195/) added to crystallization medium improved crystal quality but were not resolved in the electron density. |


## Biological / Functional Insights

### Dimeric architecture with tight interface

RsTSPO forms a stable parallel dimer with a flat interface primarily composed of TM-I and TM-III (~1250 Å², ~15% of monomer surface area). The interface is dominated by alanines and leucines with a G/A-xxx-G/A motif favoring helical dimerization. Five hydrogen bonds at the periphery between TM-I and TM-III anchor the interface. The dimer is unaltered by the A139T mutation.

### A139T mutation alters CRAC site and ligand binding

The A139T mutation (mimicking human A147T) causes TM-II to tilt 7.7° toward TM-V and TM-V to straighten by 6.3°, resulting in closer association of these helices. Side-chain rearrangements of F46, L142, F144, and W135 alter the CRAC motif, reducing binding affinity 4-5 fold for [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/), [PK11195](/xray-mp-wiki/reagents/ligands/pk11195/), and protoporphyrin IX. This provides a molecular basis for the diminished [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) metabolism and altered ligand binding observed in humans carrying the A147T polymorphism.

### Porphyrin as an endogenous ligand

Electron density in the A139T structure between TM-I and TM-II underneath LP1 corresponds to a porphyrin compound that copurifies with the protein. This supports the proposed role of TSPO in porphyrin transport and regulation of the switch between photosynthesis and respiration in R. sphaeroides.

### External surface transport mechanism

The dimeric structure with a tight interface makes an internal pore or transport pathway through the monomer unlikely. Long electron density along surface grooves extending from the porphyrin binding site to the bottom surface of the protein suggests a possible external surface transport mechanism, similar to maltoporin. This would require association with protein partners such as StAR and VDAC.


## Cross-References

- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid component of the lipidic cubic phase used for crystallization
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [PK11195](/xray-mp-wiki/reagents/ligands/pk11195/) — Related ligand or cofactor
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Additive used in purification or crystallization buffers
