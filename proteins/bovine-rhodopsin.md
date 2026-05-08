---
title: Bovine Rhodopsin (Dark State)
created: 2026-05-07
updated: 2026-05-07
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography, visual-pigment]
sources: [doi/10.1016##J.JMB.2004.08.090]
---

# Bovine Rhodopsin (Dark State)

## Overview

Bovine rhodopsin is the photoreceptor GPCR in vertebrate retinal rod cells, responsible for dim-light vision. The dark-state structure (PDB 1GZM) was determined at 2.65 A resolution in the trigonal space group P31 from native untwinned crystals. The protein consists of 7 transmembrane helices with kinks at proline and glycine residues, forming a binding pocket for the 11-cis-retinal chromophore. The structure reveals extensive inter-helical hydrogen-bonding networks, ordered water molecules, and a tightly packed hydrophobic barrier that stabilizes the inactive state. Key features include the Glu113 counterion for the protonated Schiff base, the NPxxY motif in H7, and the E(D)RY motif in H3. The cytoplasmic loops C2 and C3 show high flexibility, while the extracellular domain is highly ordered.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##J.JMB.2004.08.090 | 1GZM | 2.65 A | P31 | Native bovine rhodopsin (residues 1-326 of 348) | 11-cis-retinal (covalently bound to Lys296 via protonated Schiff base) |

## Expression and Purification

- **Expression system**: Bovine retinal rod cells (disc membrane)
- **Construct**: Native rhodopsin holoprotein with 11-cis-retinal chromophore

### Purification Workflow

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane isolation | Disc membrane preparation from bovine retina | -- | not specified | Native rhodopsin from bovine retinal disc membranes |
| Solubilization | [C8E4](/xray-mp-wiki/reagents/detergents/c8e4/) detergent solubilization | -- | [C8E4](/xray-mp-wiki/reagents/detergents/c8e4/) detergent | Solubilization in n-octyltetraoxyethylene ([C8E4](/xray-mp-wiki/reagents/detergents/c8e4/)) |


## Crystallization

### doi/10.1016##J.JMB.2004.08.090

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (native crystals) |
| Protein sample | Rhodopsin solubilized in C8E4 |
| Reservoir | not specified |
| Mixing ratio | not specified |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Untwinned native crystals in space group P31 diffracting to 2.65 A. Heavy atom derivative (EMTS) prepared but significant non-isomorphism prevented experimental phasing. Molecular replacement from P41 form (1F88) followed by multiple crystal averaging. |


## Biological / Functional Insights

### Transmembrane H-bonding network

An extensive inter-helical hydrogen-bonding network extends from Trp265 in the chromophore binding pocket via ordered water molecules (including Wat10) all the way to the conserved NPxxY motif (Asn302-Tyr306) in H7 near the cytoplasmic limit of the hydrophobic zone. This network involves Asn55 (H1), Asp83 (H2), Gly120 (H3), Met257 and Trp265 (H6), and Ser298, Ala299, Tyr301, Asn302 (H7). A hydrophobic barrier of Leu76, Leu79 (H2), Leu128, Leu131 (H3), and Met253, Met257 (H6) seals this network from the cytoplasmic compartment.

### Schiff base counterion stabilization

Glu113 serves as the counterion for the protonated Schiff base linking 11-cis-retinal to Lys296. A water molecule (Wat16) is hydrogen-bonded between the peptide carbonyl and side-chain carboxyl oxygen atoms of Glu113, delocalizing the negative charge and lowering its pKa. OE2 of Glu113 is hydrogen-bonded to the backbone of Cys187 in beta4, creating an H-bonding network from the chromophore-binding pocket through the plug to the extracellular surface. The distance between OE2 of Glu113 and the Schiff base nitrogen is 3.2 A, stabilizing the proton with pKa > 16 in the dark state.

### Helix kinks and activation mechanism

Transmembrane helices contain kinks at proline (H1:Pro53, H4:Pro170, H5:Pro215, H6:Pro267, H7:Pro302) and glycine (H2:Gly89-Gly90) residues. The H6 kink at Pro267-Tyr268 provides a pivot for outward tilt of the cytoplasmic segment during activation. A water molecule bridges the H6 and H7 kinks (4.8 A between C-alpha atoms of Tyr268 and Pro291). Photoisomerization of retinal to all-trans form triggers pivoting movements of kinked helices, amplified by translation of helix ends near membrane surfaces.


## Cross-References

- [Octyltetraoxyethylene (C8E4)](/xray-mp-wiki/reagents/detergents/c8e4/) — Primary detergent used for solubilization and crystallization
- [Lauryldimethylamine N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/lDAO/) — Added at 0.05% to C8E4-solubilized rhodopsin, key for obtaining isotropically diffracting crystals; ordered LDAO molecule bound to H5/H6/H7
- [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) — Light-sensitive chromophore covalently bound to Lys296 via protonated Schiff base; defines the visual pigment
- [Opsin (Retinal-Free Rhodopsin)](/xray-mp-wiki/proteins/opsin/) — Apoprotein form of rhodopsin; same protein family with related structural features
- [Membrane Mimetics and Structural Biology Concepts](/xray-mp-wiki/concepts/membrane-mimetics/) — General structural biology methods for membrane protein determination
