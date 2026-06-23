---
title: "bcChbC (Bacillus cereus Chitobiose Transporter)"
created: 2026-05-28
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2016.04.003, doi/10.1038##nature09939]
verified: false
---

# bcChbC (Bacillus cereus Chitobiose Transporter)

## Overview

bcChbC is a [Diacetylchitobiose](/xray-mp-wiki/reagents/ligands/diacetylchitobiose/) (GlcNAc2) transporter from Bacillus cereus, belonging to the [Glucose](/xray-mp-wiki/reagents/additives/glucose/) superfamily of enzyme IIC (EIIC) components of the bacterial phosphoenolpyruvate:carbohydrate phosphotransferase system (PTS). Its crystal structure was solved in an inward-facing occluded conformation and serves as a key comparison with bcMalT, which crystallized in the outward-facing occluded conformation. Together, these two structures provide the first structural evidence for the elevator-car transport mechanism in EIIC sugar transporters.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2016.04.003 | 3G5R | 3.2 | P212121 | EIIC domain of chitobiose transporter from Bacillus cereus | [Diacetylchitobiose](/xray-mp-wiki/reagents/ligands/diacetylchitobiose/) (GlcNAc2) |
| doi/10.1038##nature09939 | 4DJB | 3.3 | P43212 | EIIC domain (93 residues) of chitobiose transporter from Bacillus cereus, [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) removed by TEV protease | [Diacetylchitobiose](/xray-mp-wiki/reagents/ligands/diacetylchitobiose/) (GlcNAc2) |

## Expression and Purification

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### Inward-facing occluded conformation

bcChbC crystallized in an inward-facing occluded conformation, in contrast to bcMalT which crystallized in the outward-facing occluded state. The bound substrate, [Diacetylchitobiose](/xray-mp-wiki/reagents/ligands/diacetylchitobiose/) (GlcNAc2), was located near the cytoplasmic surface of the protein but shielded from solvent by a conserved loop from the neighboring protomer in the dimer. The substrate-binding cavity of bcChbC lies near the cytoplasmic surface, while bcMalT's cavity is near the periplasmic surface.

### Rigid-body domain displacement

Comparison of bcChbC (inward-facing) with bcMalT (outward-facing) reveals a rigid-body rotation of 44 degrees and translation of 9 A of the C-terminal substrate-binding domain. This displacement moves the substrate-binding cavity by approximately 20 A across the membrane, supporting an elevator-car transport mechanism where the substrate-binding domain moves as a unit between inward- and outward-facing states.

### Active site conservation and sugar specificity

The same structural elements (HP1, HP2, TM6-8) form the binding site in both bcChbC and bcMalT. The histidine (His250) and glutamate (Glu334) interacting with C6-OH are conserved. Differences in binding site residues explain sugar specificity: bcMalT uses Glu231 and Arg232 to interact with C2-OH and C3-OH on the non-reducing sugar, whereas bcChbC replaces these with shorter side chains (Val241 and His242) to accommodate the bulky N-acetyl group on C2 of GlcNAc2.

### Dimer interface and crystal packing

The ChbC protein forms a homodimer with a substantial dimer interface observed in the P43212 crystal form. The dimer interface involves transmembrane helices and the beta-hairpin region. Crystal packing analysis reveals that the two protomers in the dimer are related by a two-fold rotational symmetry axis. The beta-hairpins from both protomers are visible in the crystal lattice, suggesting the dimer is a stable biological assembly.

### Speculative transport mechanism

A speculative model for the ChbC transport mechanism was proposed based on the crystal structure. Conformational changes to convert the occluded, sugar-bound state to inward- and outward-facing open states were modeled. To convert the occluded state to the outward-facing state, an outward rigid body rotation of the region comprising TM8, HP1-2, and TM9-10 could expose the sugar-binding cavity to the periplasmic space. Opening of the intracellular gate to form the inward-open state could be achieved by straightening of helix TM5 on the neighboring protomer.


## Cross-References

- [bcMalT (Bacillus cereus Maltose Transporter)](/xray-mp-wiki/proteins/enzymes/bc-malt/) — Comparison structure; outward-facing occluded conformation of same superfamily
- [Elevator Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/) — bcChbC provides the inward-facing state for the elevator mechanism
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — bcChbC represents the inward-facing state of the alternating-access cycle
- [Maltose](/xray-mp-wiki/reagents/additives/maltose/) — Related substrate; bcMalT binds maltose while bcChbC binds GlcNAc2
- [Diacetylchitobiose (GlcNAc2)](/xray-mp-wiki/reagents/ligands/diacetylchitobiose/) — bcChbC bound to diacetylchitobiose ligand in crystal structure
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM used in purification and stability testing of ChbC
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — DM used in stability testing of ChbC by gel filtration
- [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease/) — TEV protease used to remove His6 tag from ChbC during purification
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Referenced in the context of Glucose
- [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) — Referenced in the context of His6 Tag
