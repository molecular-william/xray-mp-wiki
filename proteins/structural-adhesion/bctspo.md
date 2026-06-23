---
title: "BcTSPO Translocator Protein from Bacillus cereus"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1126##science.aaa1534]
verified: false
---

# BcTSPO Translocator Protein from Bacillus cereus

## Overview

BcTSPO is the translocator protein (TSPO) homolog from *Bacillus cereus*, a bacterial member of the tryptophan-rich TSPO family. Crystal structures were determined for the apo form at 1.7 Å resolution and for the PK11195-bound dimer, revealing a five-transmembrane-helix fold with a highly conserved ligand-binding pocket between TM1 and TM2. BcTSPO binds the benzodiazepine ligand [Pk11195](/xray-mp-wiki/reagents/ligands/pk11195/) and the endogenous porphyrin protoporphyrin IX (PpIX), and catalyzes the photooxidative degradation of PpIX — a reaction involving conserved tryptophan residues W51 and W138. The A142T mutation (corresponding to the human A147T polymorphism associated with psychiatric disorders) abrogates PpIX degradation activity and alters ligand binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.aaa1534 | 4RYQ | 1.7 | — | Wild-type BcTSPO (apo) |  |
| doi/10.1126##science.aaa1534 | 4RYQ | — | — | PK11195-bound BcTSPO dimer |  |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Wild-type BcTSPO and variants (W51F, W138F, W51F/W138F, A142T)

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein purification | Affinity chromatography | — |  | Purified BcTSPO used for crystallization and activity assays |


## Crystallization

### doi/10.1126##science.aaa1534

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) and detergent micelle |
| Notes | Apo structure solved from detergent micelle at 1.7 Å. PK11195-bound dimer crystallized in LCP. Apo micelle may be a swapped dimer. |


## Biological / Functional Insights

### Conserved five-helix TSPO fold

BcTSPO adopts a five-transmembrane-helix bundle (TM1–TM5). The protein is tryptophan-rich, with four conserved tryptophans (W31, W40, W51, W138) that play key roles in structure and function. The fold is distinct from the NMR model of mouse TSPO1 (MmTSPO1, PDB 2MGY) but closely matches the [Rstspo](/xray-mp-wiki/proteins/structural-adhesion/rstspo/) structure from R. sphaeroides (PDB 4UC1).

### PK11195 binding pocket

[Pk11195](/xray-mp-wiki/reagents/ligands/pk11195/) binds in a highly conserved cavity between TM1 and TM2. The ligand's carbonyl oxygen forms hydrogen bonds with the indole-NH groups of W51 and W138. The chloride atom contacts N87. Additional van der Waals contacts involve residues from all five helices and the TM1–TM2 loop. The binding pocket is water-filled in the apo structure, and protoporphyrin IX can be docked into the same cavity.

### Photooxidative degradation of protoporphyrin IX

BcTSPO catalyzes the light-dependent degradation of protoporphyrin IX (PpIX), involving oxidative cleavage at the methene bridge between vinyl-bearing pyrrole rings. Conserved tryptophans W51 and W138 are poised near the scissile methene bridge and vinyl groups. The W51F/W138F double mutant and the A142T mutant both lose PpIX degradation activity. The degradation product has spectral features reminiscent of biliverdin and phycocyanobilin, suggesting a formyl analog of biliverdin as a plausible product. [Pk11195](/xray-mp-wiki/reagents/ligands/pk11195/) binding substantially inhibits PpIX decay.

### A142T mutation mimics human A147T polymorphism

The A142T mutation in BcTSPO corresponds to the human A147T polymorphism associated with psychiatric disorders and reduced pregnenolone production. Ala142 projects into the binding pocket; mutation to threonine interferes with ligand binding. The A142T mutation abrogates PpIX photooxidative activity and is consistent with the reduced binding affinity for PET radioligands PBR28 and [18F]-FEPPA observed in human A147T carriers.


## Cross-References

- [PK11195](/xray-mp-wiki/reagents/ligands/pk11195/) — PK11195 is a high-affinity ligand of BcTSPO, binding in the conserved pocket between TM1 and TM2
- [Protoporphyrin IX (PpIX)](/xray-mp-wiki/reagents/ligands/protoporphyrin-ix/) — PpIX is an endogenous porphyrin ligand that is photooxidatively degraded by BcTSPO
- [RsTSPO Translocator Protein from Rhodobacter sphaeroides](/xray-mp-wiki/proteins/structural-adhesion/rstspo/) — BcTSPO and RsTSPO share the conserved five-helix TSPO fold and are bacterial homologs of mammalian TSPO
