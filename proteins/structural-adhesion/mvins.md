---
title: "MvINS - Mycobacterial Insig Homolog from Mycobacterium vanbaalenii"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aab1091]
verified: false
---

# MvINS - Mycobacterial Insig Homolog from Mycobacterium vanbaalenii

## Overview

MvINS is a mycobacterial homolog of mammalian Insig proteins, identified from Mycobacterium vanbaalenii PYR-1 through BLAST searches using human Insig-1 and Insig-2 as queries. MvINS shares 23% and 26% sequence identity with Insig-1 and Insig-2, respectively (40% similarity with both). The crystal structure was determined at 1.9 Å resolution (Hg-SAD phasing), revealing a novel six-transmembrane helix fold that is likely shared by all Insig proteins. Each MvINS protomer contains a V-shaped cavity that accommodates one diacylglycerol ([DAG](/xray-mp-wiki/reagents/lipids/dag/)) molecule, with the DAG-bound structure determined at 2.1 Å resolution. MvINS forms a homotrimer in the crystal and in solution, with the trimeric interface mediated exclusively by hydrophobic residues on TM3 and TM4. Based on the MvINS structure, a homologous model of human Insig-2 was generated, identifying residues involved in 25-hydroxycholesterol (25HC) binding and Scap association.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.aab1091 | 4XU4 | 1.9 | R3 | Full-length MvINS (residues 1-199) | — |
| doi/10.1126##science.aab1091 | 4XU4 | 2.1 | — | Full-length MvINS | Diacylglycerol (bromine-derived [DAG](/xray-mp-wiki/reagents/lipids/dag/)) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Full-length MvINS
- **Notes**: Overexpressed in E. coli; purification details in supporting online material

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: Full-length MvINS
- **Tag info**: —

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | E. coli fermentation | — | — + — | Overexpression in E. coli |
| Purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — | — + [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) (n-dodecyl-N,N-dimethylamine-N-oxide) | Protein extracted and purified in [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) detergent; native structure crystals appeared under different detergents |

**Final sample**: Purified MvINS in [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) or Cymal-7 detergent
**Yield**: —
**Purity**: —


## Crystallization

### doi/10.1126##science.aab1091

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Purified MvINS |
| Temperature | — |
| Growth time | — |
| Cryoprotection | — |
| Notes | Crystals appeared in several conditions under different detergents and diffracted X-rays beyond 2.0 Å resolution. Native structure determined by Hg-SAD from mercury-derivatized crystals. DAG-bound structure obtained by co-crystallization with a bromine-derived [DAG](/xray-mp-wiki/reagents/lipids/dag/) in Cymal-7 detergent. |


## Biological / Functional Insights

### Novel Insig Fold and Internal Symmetry

MvINS comprises six transmembrane segments (TMs 1-6) with both N- and C-termini on the cytosolic side. TM1/TM2 and TM5/TM6 display an internal pseudo twofold symmetry around an axis perpendicular to the membrane plane and superimpose with RMSD of 1.49 Å over 60 Cα atoms. These four TMs form a helical bundle tilted counterclockwise. Connecting sequences between TM1 and TM2 form a short β-strand that caps the cavity on the periplasmic side. Given the level of sequence conservation, all Insig proteins likely exhibit the same fold.

### Homotrimeric Assembly

MvINS forms a homotrimer both in the crystal and in solution. The trimeric interface is mediated exclusively through van der Waals interactions between TM3 of one protomer and TM4 of the adjacent protomer. The trimeric assembly was confirmed by a disulfide bond-mediated cross-linking strategy (MvINS-R77C mutant), which formed a stable homotrimer upon induction of disulfide bond formation.

### DAG Binding in a V-Shaped Cavity

Each MvINS protomer encloses a V-shaped cavity that accommodates one diacylglycerol ([DAG](/xray-mp-wiki/reagents/lipids/dag/)) molecule. The [DAG](/xray-mp-wiki/reagents/lipids/dag/) head group and Sn-1 tail are coordinated by residues from TM1/2/3/6 and periplasmic β-strands, while the Sn-2 tail extends into the lipid bilayer through a cleft between TM2 and TM5. The polar head is coordinated by hydrogen bonds from Asp23 and His26 on TM1, Tyr34 on β1-2, and Tyr150 on β5-6. The Sn-1 aliphatic tail is completely buried and surrounded by hydrophobic residues mainly from TM6, while the Sn-2 chain is loosely coordinated by residues from TM2/5.

### Structural Model of Human Insig-2

Based on the MvINS structure and sequence similarity, a three-dimensional structural model for the transmembrane domain of human Insig-1/2 was generated. The model identified key residues involved in 25HC (25-hydroxycholesterol) binding and Scap association. Phe115 on the cavity-facing side of TM3 is critical for 25HC recognition. Mutations G39F, C77D, or G200F resulted in compromised mScap-TMD binding in the presence of 25HC. Residues Gln132/Trp145/Asp149 mediate interactions with Scap but are not required for 25HC binding.


## Cross-References

- [LDAO (n-Dodecyl-N,N-Dimethylamine-N-oxide)](/xray-mp-wiki/reagents/detergents/ldao/) — LDAO was used as the detergent for MvINS purification and initial crystallization
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — MvINS provides structural insights into how Insig proteins function as sterol sensors in the SREBP pathway
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [LDAO](/xray-mp-wiki/reagents/detergents/ldao/) — Detergent used in purification or crystallization
- [DAG](/xray-mp-wiki/reagents/lipids/dag/) — Additive used in purification or crystallization buffers
