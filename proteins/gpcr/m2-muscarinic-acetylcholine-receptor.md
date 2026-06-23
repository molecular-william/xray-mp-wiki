---
title: Human M2 Muscarinic Acetylcholine Receptor
created: 2026-06-02
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10753, doi/10.1038##nature12735, doi/10.1038##nature17188, doi/10.1038##ncomms8895]
verified: false
---

# Human M2 Muscarinic Acetylcholine Receptor

## Overview

The human M2 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine) receptor (M2 mAChR) is a class A G protein-coupled receptor that mediates parasympathetic neurotransmission in the central and peripheral nervous systems. It couples to Gi/Go family G proteins to activate G-protein-coupled inwardly rectifying potassium channels, playing an essential role in cardiovascular function. The M2 receptor was the first human [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine) receptor to be characterized structurally. The crystal structure reveals a deeply buried orthosteric binding pocket for antagonists within the transmembrane domain, an aromatic cage of tyrosine residues that forms a lid over bound ligands, and a long aqueous channel extending from the extracellular surface through approximately two-thirds of the membrane. The structure also maps an allosteric binding site at the entrance to the orthosteric pocket, explaining the M2 receptor's exceptional propensity for allosteric regulation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature10753 | 4QDT | 2.8 A | P 21 21 2 | M2-T4L fusion (N-linked glycosylation sites Asn 2, 3, 6, 9 mutated to Asp; cysteine-less T4L residues 2-161 inserted into ICL3 replacing M2 residues 218-376; C-terminal truncation after residue 466) | 3-quinuclidinyl-benzilate (QNB) |
| doi/10.1038##nature12735 | Not specified in paper | 3.5 A | P212121 | M2 receptor (wild-type) in complex with active-state-stabilizing nanobody Nb9-8, bound to agonist iperoxo | iperoxo, Nb9-8 nanobody |
| doi/10.1038##nature12735 | Not specified in paper | 3.7 A | P212121 | M2 receptor (wild-type) in complex with Nb9-8 nanobody, bound to agonist iperoxo and positive allosteric modulator LY2119620 | iperoxo, LY2119620, Nb9-8 nanobody |

## Expression and Purification

- **Expression system**: Sf9 insect cells (baculovirus expression vector system)
- **Construct**: Wild-type human M2 muscarinic acetylcholine receptor. Expressed using baculovirus in Sf9 insect cells. Purified to homogeneity by nickel affinity chromatography, followed by Flag affinity and size exclusion chromatography.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and infection | Baculovirus expression in Sf9 insect cells | -- | -- + -- | M2 receptor expressed in Sf9 insect cells |
| Solubilization | Membrane solubilization | -- | -- + -- | M2 receptor purified in the presence of 10 uM [Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo) |
| Nickel affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA | -- + -- | Initial purification step |
| Flag affinity chromatography | Flag affinity chromatography | Flag affinity resin | -- + -- | Secondary purification step |
| Size exclusion chromatography | Size exclusion chromatography | -- | -- + -- | Final purification step for homogeneity |


## Crystallization

### doi/10.1038##nature12735

| Parameter | Value |
|---|---|
| Method | Lipidic mesophase (LCP) crystallization |
| Protein sample | [Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo)-bound M2 receptor complex with [Nb9-8 Nanobody](/xray-mp-wiki/reagents/antibodies/nb9-8) [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody) |
| Lipid | -- |
| Notes | Crystallized by lipidic mesophase crystallography at Advanced Photon Source beamline 23ID-D. Data collected by X-ray microdiffraction. 17 crystals used for the [Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo)-[Nb9-8 Nanobody](/xray-mp-wiki/reagents/antibodies/nb9-8) structure (3.5 A). Supplementing crystallization conditions with [LY2119620](/xray-mp-wiki/reagents/ligands/ly2119620) yielded crystals of the ternary complex (3.7 A, 18 crystals). Both structures solved in P212121 space group.
 |


## Biological / Functional Insights

### Active-state conformational changes

The active-state M2 receptor shows key conformational changes consistent with
GPCR activation: an outward displacement of TM6 at the intracellular side,
smaller outward movement of TM5, and rearrangement of TM7 around the NPXXY
motif. The DRY motif rearranges with Arg 121 (3.50) adopting an extended
conformation and Asp 120 (3.49) forming a hydrogen bond with Asn 58 (2.39).
The active-state M2 receptor shows larger conformational changes in the
extracellular region and orthosteric binding site than observed in the active
states of the beta2 AR and rhodopsin.

### Orthosteric binding pocket closure on activation

The activated M2 receptor shows a small orthosteric binding site that
completely occludes the agonist [Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo) from solvent. Transmembrane helices
5, 6 and 7 move inward toward the agonist in the active conformation. TM3
undergoes a slight rotation about its axis. The largest differences involve
TM6, where an inward movement of 2 A at Asn 404 (6.52) allows formation of
a hydrogen bond between its side chain and [Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo). The agonist [Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo)
adopts a bent conformation within the active orthosteric binding pocket.

### Extracellular vestibule contraction

The M2 receptor possesses a large extracellular vestibule above the
orthosteric site that shows substantial contraction upon activation due to
TM6 rotation. This motion of TM6 provides a structural link among three
receptor regions: the extracellular vestibule, the orthosteric binding
pocket, and the intracellular surface. The structural coupling accounts for
the fact that allosteric modulators can affect the affinity and efficacy of
orthosteric ligands and can also directly activate G proteins as allosteric
agonists.

### Allosteric modulator binding site

The positive allosteric modulator [LY2119620](/xray-mp-wiki/reagents/ligands/ly2119620) binds at a site directly
superficial to the orthosteric site in the extracellular vestibule. Its
aromatic rings are situated between Tyr 177 (ECL2) and Trp 422 (7.35),
forming a three-layered aromatic stack. Polar interactions include hydrogen
bonds from Tyr 80 (2.61), Asn 410 (6.58) and Asn 419 (ECL3), and a
charge-charge interaction with Glu 172 (ECL2). [LY2119620](/xray-mp-wiki/reagents/ligands/ly2119620) binds at a site
separated from the orthosteric site only by the tyrosine lid, with Tyr 426
(7.39) interacting with both ligands.

### Asn 58 (2.39) in active-state stabilization

Asn 58 (2.39) stabilizes the active conformation through a hydrogen bond
with Asp 120 (3.49). Mutation of Asn 58 to alanine (N58A) resulted in a
mutant with normal ligand-binding properties but impaired ability to
activate G protein. This residue likely either directly stabilizes the
active conformation or engages in direct interactions with G protein.

### TM6 pivot mechanism

Activation involves a pivot of TM6 that moves inward in the orthosteric
binding site (forming a hydrogen bond with [Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo) via Asn 404) and
outward at the intracellular side (creating the G-protein binding cavity).
This dual motion of TM6 structurally couples the orthosteric site,
extracellular vestibule, and intracellular G-protein binding surface.


## Cross-References

- [Tx24](/xray-mp-wiki/reagents/ligands/tx24/) — Engineered allosteric toxin targeting M2AChR, derived from MT7 via in vitro evolution
- [Three-Finger Toxin Scaffold for GPCR Modulation](/xray-mp-wiki/concepts/three-finger-toxin-gpcr-modulation/) — M2AChR is target of engineered 3FT Tx24 demonstrating scaffold retargetability
- [M1 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m1-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor subtype; orthosteric binding pocket residues identical between M1 and M2
- [M3 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m3-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor subtype; orthosteric binding pocket residues identical between M3 and M2
- [Human M4 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m4-muscarinic-acetylcholine-receptor/) — Related muscarinic receptor subtype; M4 structure solved in same study as M1 (Thal et al., 2016)
- [Acetylcholine-Binding Protein (AChBP)](/xray-mp-wiki/proteins/cys-loop-receptors/acetylcholine-binding-protein/) — Structural homologue showing convergent evolution of acetylcholine binding sites
- [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) — Endogenous orthosteric ligand of the M2 receptor
- [3-Quinuclidinyl-benzilate (QNB)](/xray-mp-wiki/reagents/ligands/3-quinuclidinyl-benzilate/) — Antagonist co-crystallized with inactive M2 receptor (PDB 4QDT)
- [Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo/) — High-affinity agonist co-crystallized with active-state M2 receptor
- [LY2119620](/xray-mp-wiki/reagents/ligands/ly2119620/) — Positive allosteric modulator co-crystallized with active-state M2 receptor
- [Nb9-8 Nanobody](/xray-mp-wiki/reagents/antibodies/nb9-8/) — Active-state-stabilizing nanobody used for crystallization of active M2 receptor
- [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) — Nanobody fusion used for crystallization
