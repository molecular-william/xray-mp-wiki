---
title: Heliobacterial Reaction Center (HbRC)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aan5611]
verified: false
---

# Heliobacterial Reaction Center (HbRC)

## Overview

The heliobacterial reaction center (HbRC) from Heliobacterium modesticaldum is
a homodimeric Type I photosynthetic reaction center that converts light energy
into chemical energy. It is the first homodimeric reaction center structure to
be determined, at 2.2 Å resolution (PDB 5V8K). The HbRC consists of a PshA
homodimer (core) plus two PshX small subunits, binding 54 [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) g
(BChl g), 4 BChl g', two 8'-hydroxychlorophyll a_F, two carotenoids
(4,4'-diaponeurosporene), two lipids, and one [4Fe-4S] cluster. The complex
exhibits perfect C2 symmetry and lacks a bound quinone in the electron transfer
chain — a unique characteristic among all known reaction centers. The HbRC is
the simplest known reaction center and is considered the closest homolog to the
common ancestor of all photosynthetic reaction centers.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.aan5611 | 5V8K | 2.2 | — | HbRC purified from Heliobacterium modesticaldum — homodimeric PshA core + two PshX small subunits | BChl g (54), BChl g' (4), 8'-OH Chl a_F (2), 4,4'-diaponeurosporene (2), [4Fe-4S] cluster (1) |

## Expression and Purification

- **Expression system**: Heliobacterium modesticaldum (native expression)
- **Construct**: Native HbRC complex — PshA homodimer + PshX small subunits, no affinity tags
- **Notes**: H. modesticaldum is a thermophilic anaerobic phototroph isolated from volcanic soil in Iceland.

### Purification Workflow

- **Expression system**: Heliobacterium modesticaldum (native)
- **Expression construct**: Native HbRC complex — PshA + PshX subunits

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Anaerobic phototrophic growth | — |  | H. modesticaldum grown under anaerobic conditions in light |
| Membrane isolation and HbRC purification | As described in ref 22 (Sarrou et al., 2012) | — |  | Purification details in Photosynth. Res. 111, 291-302 (2012). HbRC purified in the absence of [Menaquinone](/xray-mp-wiki/reagents/ligands/menaquinone/). |

**Final sample**: Purified HbRC complex, no bound [Menaquinone](/xray-mp-wiki/reagents/ligands/menaquinone/)


## Crystallization

### doi/10.1126##science.aan5611

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Notes | Crystals grown and diffracted to 2.2 Å resolution. Data collected at Berkeley Center for Structural Biology, Advanced Light Source, and Structural Biology Center at the Advanced Photon Source. |


## Biological / Functional Insights

### First homodimeric reaction center structure

The HbRC is the first homodimeric reaction center structure solved, exhibiting perfect C2 symmetry. All previously solved RC structures (PbRC, PSI, PSII) are heterodimeric. The homodimeric core preserves characteristics of the ancestral reaction center, providing insight into the evolution of photosynthesis.

### C2 symmetry in electron transfer chain

Due to the homodimeric core, the ET cofactors are arranged into two identical branches about the C2 symmetry axis. The ET chain consists of P800 (a pair of BChl g'), Acc (BChl g), A0 (8'-OH Chl a_F), and FX (a [4Fe-4S] cluster). The two identical branches contrast with the asymmetric branches of heterodimeric RCs.

### No bound quinone in electron transfer

The HbRC lacks a bound quinone in the ET chain — a striking divergence from all other known RCs. The crystallized HbRC lacked [Menaquinone](/xray-mp-wiki/reagents/ligands/menaquinone/) (MQ), as it is not bound tightly by the protein. The edge-to-edge distance between A0 and FX is ~10.2 Å (much shorter than the ~14.3 Å in PSI), close enough to allow a maximal ET rate of ~8 × 10^8 s^-1, supporting the hypothesis that ET from A0 to FX does not require an intermediate quinone cofactor.

### Antenna architecture and energy transfer

The HbRC binds 54 BChl g molecules as antenna pigments, forming two layers within the complex. Most are within 6 Å of each other for rapid excitation energy transfer. Only six BChl g molecules (three per symmetric side) are within 13 Å of the ET chain, suggesting that energy transferred to the ET chain arrives via these bridging pigments. The antenna domain is fused to the ET domain, similar to PSI.

### Evolutionary significance

The HbRC displays characteristics expected of the common ancestor of all RCs: a homodimeric core, low number of antenna (B)Chls relative to oxygenic homologs, lack of peripheral antenna complexes, and overall simplicity. While the Firmicutes branched early in bacterial evolution, heliobacteria likely acquired the RC via horizontal gene transfer. Nevertheless, some traits of the last common ancestor are preserved in the HbRC due to its host's anoxic niche, similar to early Earth conditions.


## Cross-References

- [Blastochloris viridis Photosynthetic Reaction Centre (RCvir)](/xray-mp-wiki/proteins/photosynthesis/blastochloris-viridis-photosynthetic-reaction-centre/) — Type II heterodimeric RC for evolutionary comparison with the homodimeric Type I HbRC
- [Photosystem II](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/) — PSII is a Type II heterodimeric RC; HbRC is compared as a Type I homodimeric RC with ancestral features
- [Manganese-Calcium Cluster (Mn4Ca Cluster)](/xray-mp-wiki/concepts/manganese-calcium-cluster/) — HbRC lacks an oxygen-evolving complex; comparison highlights unique features of oxygenic vs anoxygenic photosynthesis
- [Bacteriochlorophyll](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/) — Related ligand or cofactor
- [Menaquinone](/xray-mp-wiki/reagents/ligands/menaquinone/) — Related ligand or cofactor
