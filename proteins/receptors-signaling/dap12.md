---
title: DAP12 (CD331)
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.celrep.2015.04.045]
verified: false
---

# DAP12 (CD331)

## Overview

DAP12 (Discoidin Domain-Related Protein 12, also known as CD331 or KARAP) is a eukaryotic immunoreceptor signaling module that lacks a structured ectodomain. It associates with various client receptors to form hetero-oligomeric complexes in the endoplasmic reticulum, enabling activating immune receptor signaling. The transmembrane domain of DAP12 forms homo-oligomers (dimers, trimers, tetramers) through polar interactions between aspartic acid and threonine motifs, and also hetero-oligomerizes with client receptors via a central lysine residue in the receptor TM domain. This paper presents the first crystal structures of DAP12 transmembrane oligomers determined in a lipidic cubic phase membrane environment.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.celrep.2015.04.045 | 4WOL | 1.77 A | Not specified | Human DAP12 transmembrane peptide (33 amino acids, beginning from second extracellular cysteine, sequence CSTVSPGVLAGIVVGDLVLTVLIALAVYFLGRL), disulfide-linked dimer precursor | Coordinated potassium ion at the aspartic acid/threonine polar core |
| doi/10.1016##j.celrep.2015.04.045 | 4WO1 | 2.14 A | Not specified | Human DAP12 transmembrane peptide (33 amino acids, beginning from second extracellular cysteine), disulfide-linked dimer precursor | Coordinated calcium ion(s) at the aspartic acid/threonine polar core |

## Expression and Purification

- **Expression system**: E. coli (trpLE fusion system)
- **Construct**: DAP12-TM peptide (33 amino acids) produced as a trpLE fusion, disulfide-linked through N-terminal cysteine, cyanogen bromide digested, HPLC purified

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Fusion protein expression | Expression in E. coli | -- | -- + -- | DAP12-TM peptide produced as trpLE fusion in E. coli |
| Disulfide-linked dimer formation | Refolding | -- | -- + -- | Disulfide-linked through N-terminal cysteine |
| Cyanogen bromide cleavage | Proteolytic digestion | -- | -- + -- | Cleavage to release TM peptide from trpLE fusion; methionine changed to valine to avoid internal cleavage |
| HPLC purification | High-performance liquid chromatography | -- | -- + -- | Purified following published procedure (Sharma et al., 2013); stored as lyophilized product |


## Crystallization

### doi/10.1016##j.celrep.2015.04.045

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | DAP12-TM peptide reconstituted into [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) LCP by co-dissolution in hexafluoroisopropanol (HFIP), followed by solvent removal and mixing with water |
| Temperature | Not specified |
| Growth time | 5-7 days (small oval discs visible) |
| Cryoprotection | Not specified |
| Notes | Trimer structure (PDB 4WOL) diffracted to 1.77 A. Three parallel alpha helices in asymmetric unit arranged in right-handed trimeric coiled coil. Coordinated potassium ion at polar core. |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | DAP12-TM peptide reconstituted into [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) LCP by co-dissolution in hexafluoroisopropanol (HFIP), followed by solvent removal and mixing with water |
| Temperature | Not specified |
| Growth time | 1-3 days (star-like clusters visible) |
| Cryoprotection | Not specified |
| Notes | Tetramer structure (PDB 4WO1) diffracted to 2.14 A. Four parallel alpha helices in asymmetric unit. Coordinated calcium ion at polar core. |


## Biological / Functional Insights

### Trimeric coiled coil structure with coordinated potassium

The DAP12-TM trimer (PDB 4WOL) consists of three parallel alpha helices
arranged in a right-handed trimeric coiled coil. The helices are tightly
packed in the lower half, facilitated by the small side chain at alanine 31.
At the core of the trimeric interface, aspartic acid and threonine side
chains are oriented toward the center, where their polar groups are shielded
from the hydrophobic environment. A potassium ion is coordinated by seven
side-chain oxygen atoms (distances 2.7-3.1 A) from aspartic acids and
threonines from all three chains. Molecular dynamics simulations in a [Popc](/xray-mp-wiki/reagents/lipids/popc/)
bilayer showed that the structure with one ionized aspartic acid (1 Asp-)
was the most stable over 200-ns simulation.

### Tetrameric structure with coordinated calcium

The DAP12-TM tetramer (PDB 4WO1) contains four parallel alpha helices in
the asymmetric unit. As in the trimer, aspartic acid/threonine motifs from
all chains are sequestered in the polar core. Extra density was modeled as
two overlapping calcium coordination sites with pentagonal bipyramidal
geometry, each with 50% occupancy, including a network of water molecules.
MD simulations in [Popc](/xray-mp-wiki/reagents/lipids/popc/) bilayer with 50 mM CaCl2 showed stability with one
or two calcium ions and four or two ionized aspartic acid residues
respectively.

### Higher-order oligomers form in the endoplasmic reticulum

Biochemical analysis of full-length DAP12 in 293T cells and isolated ER
microsomes revealed disulfide-linked dimers, trimers, and tetramers.
Mutagenesis studies showed that aspartic acid-to-alanine substitution
severely impaired trimer and tetramer formation (10-fold and 2-fold
reduction), while threonine-to-alanine impaired trimer formation (5-fold
decrease) but shifted distribution toward tetramer (2-fold increase). These
higher-order oligomers represent a substantial fraction of full-length
DAP12 generated during ER synthesis.

### DAP12 trimer formation competes with receptor assembly

In ER assembly assays, increasing amounts of the NK cell activating
receptor KIR2DS2 (with poly-leucine TM domain containing a central lysine)
resulted in recovery of less DAP12 trimer and concomitant increase in
dimeric form. The aspartic acid-to-asparagine mutant (DN), which forms
trimers but cannot assemble with receptor, was unperturbed by receptor
presence. This demonstrates that the balance between DAP12 homo-oligomerization
and receptor assembly is governed by both the chemical nature of polar side
chains and the relative availability of complementary ligands.

### Glycine zipper motif on exterior helix surface

Both trimeric and tetrameric structures feature an exterior triplet of
[Glycine](/xray-mp-wiki/reagents/buffers/glycine/) spaced with helical periodicity forming a potential [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) zipper
motif. Substitution of all three [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) with bulky hydrophobic residues
(triple leucine or triple phenylalanine) did not significantly alter the
distribution of DAP12 products in the ER, indicating the [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) zipper is
not essential for oligomer assembly. The [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) zipper motif is consistent
with findings in other transmembrane proteins (Kim et al., 2005).


## Cross-References

- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — DAP12-TM crystallized in monoolein LCP to obtain trimer and tetramer structures
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid component of the cubic phase membrane environment for DAP12 crystallization
- [POPC](/xray-mp-wiki/reagents/lipids/popc/) — Palmitoyl-oleoyl phosphatidylcholine used in MD simulations of DAP12 oligomers
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — PEG 3350 used as precipitant in both crystallization conditions
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — 10% cholesterol used in trimer crystallization condition
- [Intramembrane Ion Coordination](/xray-mp-wiki/concepts/intramembrane-ion-coordination/) — Central mechanism discovered - potassium and calcium coordination at DAP12 TM polar core
- [Calcium Chloride](/xray-mp-wiki/reagents/additives/calcium-chloride/) — 0.269 M calcium chloride used in tetramer crystallization condition
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) — 200-ns MD simulations validated trimer/tetramer stability in POPC bilayer
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Referenced in context related to Glycine
