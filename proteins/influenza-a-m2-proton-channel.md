---
title: Influenza A M2 Proton Channel
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein]
sources: [doi/10.1021##jacs.8b06741, doi/10.1021##jacs.9b02196]
verified: false
---

# Influenza A M2 Proton Channel

## Overview

The M2 proton channel of influenza A virus is a homotetrameric ion channel that transports protons from the low-pH environment of the endosome into the viral interior during viral entry. The transmembrane (TM) domain (residues 23-46 in full-length M2, residues 22-46 in crystallized constructs) is sufficient for selective proton transport and forms the target of the adamantyl-amine class of antiviral drugs including amantadine and rimantadine. The channel adopts Inward_closed and Inward_open conformational states that cycle during proton transport, with His37 serving as a selectivity filter and proton shuttle.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1021##jacs.8b06741 | 6BKK | 2.00 | P21 | M2 TM domain (residues 22-46), Inward_closed conformation | amantadine |
| doi/10.1021##jacs.8b06741 | 6BKL | 2.00 | P21 | M2 TM domain (residues 22-46), Inward_closed conformation | rimantadine |
| doi/10.1021##jacs.8b06741 | 6BMZ | 2.63 | P21 | M2 TM domain (residues 22-46), Inward_closed conformation | spiro-adamantyl amine |
| doi/10.1021##jacs.8b06741 | 5BOC | 2.25 | P21 | M2 TM domain (residues 22-46), Inward_open conformation | rimantadine |
| doi/10.1021##jacs.9b02196 | 6MJH | 2.2 | P21 | M2 TM domain (residues 22-46), S31N mutant, Inward_open conformation | none |
| doi/10.1021##jacs.9b02196 | 6MJH | 2.2 | P21 | M2 TM domain (residues 22-46), S31N mutant, Inward_closed conformation | none |

## Expression and Purification

No purification described.

## Crystallization

### doi/10.1021##jacs.8b06741

| Parameter | Value |
|---|---|
| Method | Lipidic Cubic Phase (LCP) |
| Protein sample | M2 TM domain (residues 22-46) |
| Lipid | monoolein |
| Temperature | 20 |
| Notes | Amantadine-bound structure (6BKK); DMNG detergent additive used to stabilize Inward_closed state |

| Parameter | Value |
|---|---|
| Method | Lipidic Cubic Phase (LCP) |
| Protein sample | M2 TM domain (residues 22-46) |
| Lipid | monoolein |
| Temperature | 20 |
| Notes | Rimantadine-bound structure (6BKL); DMNG detergent additive used to stabilize Inward_closed state |

| Parameter | Value |
|---|---|
| Method | Lipidic Cubic Phase (LCP) |
| Protein sample | M2 TM domain (residues 22-46) |
| Lipid | monoolein |
| Temperature | 20 |
| Notes | Spiro-adamantyl amine-bound structure (6BMZ) |

| Parameter | Value |
|---|---|
| Method | Lipidic Cubic Phase (LCP) |
| Protein sample | M2 TM domain (residues 22-46) |
| Lipid | monoolein |
| Temperature | 20 |
| Notes | Rimantadine-bound structure (5BOC) in Inward_open conformation |

### doi/10.1021##jacs.9b02196

| Parameter | Value |
|---|---|
| Method | Lipidic Cubic Phase (LCP) |
| Protein sample | M2 TM domain (residues 22-46), S31N mutant |
| Lipid | monoolein |
| Temperature | 100 |
| Notes | S31N mutant in two conformational states; Inward_open and Inward_closed in same crystal lattice; MNG-3-C8 additive critical for Inward_closed stabilization |

| Parameter | Value |
|---|---|
| Method | Solution NMR |
| Protein sample | M2(19-49) WT and S31N mutant |
| Temperature | 313 |
| Notes | Solution NMR screening of detergents for conformational state stabilization; LPPG stabilizes Inward_open, MNG-3-C8 stabilizes Inward_closed, C14-betaine allows interconversion |


## Biological / Functional Insights

### Adamantyl drug binding mechanism

The hydrophobic adamantane moiety of amantadine and rimantadine binds in a predominantly hydrophobic pocket lined by Val27, Ala30, and Ser31 sidechains and mainchains. The ammonium group of the drugs is directed downward in the aqueous pore toward His37, where it forms hydrogen bonds with the Ala30 water layer. The adamantane groups displace waters from the portion of the pore facing the viral interior, while the positively charged ammonium group locks into water networks that normally hydrate and stabilize protons.

### Conformational states and drug binding

M2 exists in Inward_closed and Inward_open conformational states. Drugs bind to both states, explaining pH-independent binding. In the Inward_closed state, helices bend at Gly34; in the Inward_open state, helices straighten, increasing the diameter at the C-terminus. The Inward_closed state is stable at higher pH where His37 is neutral or monoprotonated. At lower pH, protonated His37 residues cause repulsion leading to the Inward_open state.

### Water-mediated drug interactions

The ammonium and adamantyl groups of adamantyl-amine drugs are free to rotate in the channel, minimizing the entropic cost of binding. The ammonium group forms hydrogen bonds with two of the four waters in the Ala30 water layer, tilting slightly (11.3 +/- 0.7 degrees for amantadine) to accommodate asymmetric interactions. The spiro-adamantyl amine extends deeper into the channel, displacing the Ala30 water layer entirely and engaging the Gly34 water layer instead.

### Drug resistance mutations

Resistance mutations cluster in the upper portion of the channel between residues 26-31, disrupting the hydrophobic adamantane-binding site. However, pore-lining residues important for water-mediated conduction (Ala30, Gly34, His37) remain unchanged in over 99% of identified viral strains. Inhibitors can be designed to either hydrogen-bond to Ala30-associated waters or displace these water molecules entirely, as shown by the spiro-adamantyl amine complex.

### S31N drug resistance mechanism

The S31N mutation, found in over 98% of adamantane-resistant influenza A strains, confers resistance through two mechanisms. In the Inward_open conformation, Asn31 faces the pore and sterically blocks the adamantane binding site. In the Inward_closed conformation, Asn31 forms hydrogen bonds with carbonyls at the monomer-monomer interface, twisting the monomer helices and constricting the pore at the drug binding site. The Asn31 sidechain carbonyl oxygen closely approaches the alpha-carbon of Ala30 from a neighboring monomer (3.3-3.5 A), forming a C-H...O hydrogen bond that contributes to pore constriction.

### Detergent-dependent conformational equilibrium

The conformational equilibrium between Inward_open and Inward_closed states of M2 is highly dependent on detergent choice. LPPG exclusively stabilizes the Inward_open state. MNG-3-C8 exclusively stabilizes the Inward_closed state. C14-betaine allows interconversion between states. The equilibrium is also pH-dependent: the Inward_closed state reaches maximum stability at pH 6 and becomes undetectable at pH 4.3 or lower. This reflects energetic coupling between protonation of the His37 tetrad and conformational change.


## Cross-References

- [Amantadine](/xray-mp-wiki/reagents/ligands/amantadine/) — Primary adamantyl-amine inhibitor bound to M2 in structures 6BKK and 6BKL
- [Rimantadine](/xray-mp-wiki/reagents/ligands/rimantadine/) — Racemic adamantyl-amine inhibitor bound to M2 in structures 6BKL and 5BOC
- [Decyl Maltose Neopentyl Glycol (DMng)](/xray-mp-wiki/reagents/detergents/dmng/) — Detergent additive used in M2 crystallization to stabilize Inward_closed state
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP method used for all M2 crystal structures
- [Influenza A M2 Proton Channel S31N Mutant](/xray-mp-wiki/proteins/influenza-a-m2-proton-channel-s31n/) — S31N mutant with PDB 6MJH; most prevalent drug resistance mutation
- [MNG-3-C8 Detergent](/xray-mp-wiki/reagents/detergents/mng-3-c8/) — MNG detergent critical for crystallizing Inward_closed state of S31N mutant
- [Decylphosphocholine (DPC)](/xray-mp-wiki/reagents/detergents/dpc/) — Zwitterionic detergent used in NMR screening of M2 conformational states
- [M2 Proton Channel Conformational Equilibrium](/xray-mp-wiki/concepts/m2-conformational-equilibrium/) — Conformational dynamics between Inward_open and Inward_closed states
