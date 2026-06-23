---
title: Apolipoprotein N-acyltransferase (Lnt) from Escherichia coli
created: 2026-06-08
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##s41598-020-57419-7, doi/10.1126##sciadv.adf5799]
verified: false
---

# Apolipoprotein N-acyltransferase (Lnt) from Escherichia coli

## Overview

Apolipoprotein N-acyltransferase (Lnt) is an integral membrane enzyme that catalyzes the final step of lipoprotein maturation in Gram-negative bacteria — the N-acylation of the N-terminal cysteine of apolipoproteins. Lnt belongs to the [Nitrilase Superfamily](/xray-mp-wiki/concepts/nitrilase-superfamily/) and employs a Glu-Lys-Cys catalytic triad (E267-K335-C387 in E. coli) to perform a two-step ping-pong mechanism. The first step involves acyl transfer from a phospholipid substrate to the active site cysteine, forming a thioester acyl-intermediate. The second step transfers the acyl chain from this cysteine to the N-terminal cysteine of the incoming apolipoprotein. This work reports two crystal forms of E. coli Lnt that capture the thioester acyl-intermediate and reveal conformational dynamics of a flexible arm (residues 345-365) that may regulate active site access.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41598-020-57419-7 | 6NWR | 3.5 | P2_12_12_1 | Full-length with C-terminal 15-aa tail including [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (Lnt-C1) |  |
| doi/10.1038##s41598-020-57419-7 | 6Q3A | 3.01 | P6_422 | Full-length with N-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) removed by TEV cleavage (Lnt-C2) |  |

## Expression and Purification

- **Expression system**: E. coli (DH5α genomic DNA)
- **Construct**: Full-length Lnt with C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (Lnt-C1) or N-terminal TEV-cleavable [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (Lnt-C2)

### Purification Workflow

- **Expression system**: E. coli K12 DH5α
- **Expression construct**: Full-length Lnt with C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (Lnt-C1) or N-terminal TEV-cleavable [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (Lnt-C2)
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (C-terminal for Lnt-C1; N-terminal TEV-cleavable for Lnt-C2)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | — |  | Purification via [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) |
| Tag removal | TEV protease cleavage | — |  | Lnt-C2 only — TEV cleavage removed N-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) |

**Final sample**: Purified Lnt in crystallization buffer


## Crystallization

### doi/10.1038##s41598-020-57419-7

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Lnt-C1 with C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) |
| Temperature | 20 |
| Growth time | ~2 weeks |
| Notes | Crystals grew in P2_12_12_1 space group with 2 molecules in asymmetric unit. Loop-harvested and snap-cooled in liquid nitrogen without additional cryoprotectant. |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase |
| Protein sample | Lnt-C2 (TEV-cleaved, 15 mg/mL) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (9.9 [MAG](/xray-mp-wiki/reagents/lipids/mag/)) |
| Protein-to-lipid ratio | 2:3 |
| Temperature | 18 |
| Growth time | ~6 weeks |
| Notes | Initial trials at 18°C, optimized at 10°C for 3 weeks then 4°C for 3 weeks. Crystals in P6_422 space group. Loop-harvested and snap-frozen without cryoprotectant. |


## Biological / Functional Insights

### Thioester acyl-intermediate captured in Lnt-C1 chain B

Extra electron density extending off the active site C387 in chain B of Lnt-C1 is consistent with a palmitoyl thioester acyl-intermediate, confirmed by mass spectrometry. The acyl tail curves upward above the predicted membrane interface and fits into a hydrophobic binding groove. No large-scale active site rearrangements are required to accommodate the modification.

### Conformational dynamics of the flexible 345-365 arm

The long 345-365 arm displays remarkable flexibility. In Lnt-C1 chain B it extends at a ~60° upward angle above the membrane, likely acting as a protective lid over the active site during the reactive thioester state. In chain A and Lnt-C2, the arm lies parallel to the membrane, creating an open, accessible active site cavity. This arm may regulate access to the active site and protect the thioester intermediate from unwanted hydrolysis.

### W237 movement mediates substrate binding

W237, located at the entry of the large substrate-binding cavity, adopts two alternate conformations across available Lnt structures: an upward position coordinated with T271 (pointing away from the portal), and a downward position pointing into the portal where it can interact with substrates. This movement (~8.5 Å) appears to be triggered by substrate binding and may help stabilize incoming apolipoproteins for the second catalytic step.

### Proposed window mechanism for substrate selectivity

When the 345-365 arm is above the membrane and W237 is in the downward position, a restricted window is formed at the narrowest part of the cavity involving E343, W415, W237, and P346. This may selectively allow only the N-terminus of apolipoproteins to access the reactive thioester state, providing substrate selectivity at the second catalytic step.


## Cross-References

- [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — Used in LCP crystallization reservoir at 100 mM pH 7.2
- [PEG200](/xray-mp-wiki/reagents/additives/peg200/) — Used as precipitant in LCP crystallization at 36%
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used for LCP crystallization of Lnt-C2
- [Ammonium Phosphate](/xray-mp-wiki/reagents/additives/ammonium-phosphate/) — Used at 400 mM in LCP crystallization reservoir
- [His6-tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) — Used for affinity purification of both Lnt constructs
- [TEV Protease](/xray-mp-wiki/reagents/additives/tevp-protease/) — Used to remove N-terminal His6-tag from Lnt-C2
- [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for Lnt-C2
- [Nitrilase Superfamily](/xray-mp-wiki/concepts/nitrilase-superfamily/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [MAG](/xray-mp-wiki/reagents/lipids/mag/) — Additive used in purification or crystallization buffers
