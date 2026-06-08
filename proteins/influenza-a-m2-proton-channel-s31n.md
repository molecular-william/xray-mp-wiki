---
title: Influenza A M2 Proton Channel S31N Mutant
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein]
sources: [doi/10.1021##jacs.9b02196]
verified: false
---

# Influenza A M2 Proton Channel S31N Mutant

## Overview

The S31N mutant of the influenza A M2 proton channel is the most prevalent drug resistance mutation, found in over 98% of adamantane-resistant influenza A strains. The transmembrane domain (residues 22-46) was crystallized in two distinct conformational states (Inward_open and Inward_closed) within the same crystal lattice. The Ser31ToAsn mutation confers adamantane resistance through two mechanisms: steric blocking of the drug binding site in the Inward_open state and pore constriction via helix twisting in the Inward_closed state. The S31N mutation also alters the hydrogen bonding network of the pore-lining Asn31 sidechain, which can face either the aqueous pore or the monomer-monomer interface depending on the conformational state.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1021##jacs.9b02196 | 6MJH | 2.2 | P21 | M2 TM domain (residues 22-46), S31N mutant, Inward_open conformation | none |
| doi/10.1021##jacs.9b02196 | 6MJH | 2.2 | P21 | M2 TM domain (residues 22-46), S31N mutant, Inward_closed conformation | none |

## Expression and Purification

No purification described.

## Crystallization

### doi/10.1021##jacs.9b02196

| Parameter | Value |
|---|---|
| Method | Lipidic Cubic Phase (LCP) |
| Protein sample | M2 TM domain (residues 22-46), S31N mutant |
| Lipid | monoolein |
| Temperature | 100 |
| Notes | Inward_open conformation; crystals diffracted at ALS 8.3.1; molecular replacement using 5JOO as starting model |

| Parameter | Value |
|---|---|
| Method | Lipidic Cubic Phase (LCP) |
| Protein sample | M2 TM domain (residues 22-46), S31N mutant |
| Lipid | monoolein |
| Temperature | 100 |
| Notes | Inward_closed conformation; molecular replacement using 3LBW as starting model; MNG-3-C8 additive critical for stabilization |


## Biological / Functional Insights

### Adamantane resistance mechanism of S31N mutation

The S31N mutation confers adamantane resistance through two distinct mechanisms depending on the conformational state. In the Inward_open conformation, the Asn31 sidechain faces the channel pore and sterically blocks the adamantane binding site. In the Inward_closed conformation, Asn31 faces away from the pore and forms hydrogen bonds with carbonyls at the monomer-monomer interface. This H-bonding between Asn31 and the Leu26 backbone carbonyl from a neighboring monomer twists each monomer helix at the channel N-terminus, causing the Ala30 sidechain to rotate toward the center of the pore. This constricts the pore at the adamantane binding site and elongates the pore below the Val27 gate.

### Asn31 sidechain conformational flexibility

The Asn31 sidechain can adopt two distinct orientations depending on the conformational state. In the Inward_open state, all four Asn31 sidechains face the aqueous pore and form hydrogen bonds with symmetrically repeated Asn31 sidechains from neighboring monomers. In the Inward_closed state, the Asn31 sidechain engages in three hydrogen bonds: one intra-helix H-bond with the Val27 carbonyl, a second H-bond with the Leu26 carbonyl from a neighboring monomer, and a C-H...O interaction with the alpha-carbon of Ala30 from a neighboring monomer. This Asn-to-backbone hydrogen bonding motif is commonly observed in alpha-helical proteins.

### Detergent-dependent conformational equilibrium

Solution NMR experiments show that the conformational equilibrium between Inward_open and Inward_closed states of M2(19-49) WT and S31N is highly dependent on both detergent choice and pH. LPPG stabilizes the Inward_open state, MNG-3-C8 stabilizes the Inward_closed state, and C14-betaine allows interconversion. The Inward_closed state reaches maximum stability at pH 6 and becomes undetectable at pH 4.3 or lower, reflecting energetic coupling between protonation of the His37 tetrad and conformational change.


## Cross-References

- [Influenza A M2 Proton Channel](/xray-mp-wiki/proteins/influenza-a-m2-proton-channel/) — Wild-type M2 channel; S31N is the most prevalent drug resistance mutation
- [MNG-3-C8 Detergent](/xray-mp-wiki/reagents/detergents/mng-3-c8/) — MNG detergent critical for crystallizing the Inward_closed state of S31N mutant
- [Amantadine](/xray-mp-wiki/reagents/ligands/amantadine/) — Primary adamantyl-amine inhibitor; S31N mutation confers resistance
- [Rimantadine](/xray-mp-wiki/reagents/ligands/rimantadine/) — Related adamantyl-amine inhibitor; S31N mutation confers resistance
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for both conformational states of S31N mutant
