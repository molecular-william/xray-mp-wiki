---
title: PepT_St Proton-Dependent Oligopeptide Transporter from Streptococcus thermophilus
created: 2026-05-29
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##EMBOJ.2012.157, doi/10.1016##j.str.2018.01.005]
verified: false
---

# PepT_St Proton-Dependent Oligopeptide Transporter from Streptococcus thermophilus

## Overview

PepT_St is a proton-dependent oligopeptide transporter (POT) from Streptococcus thermophilus that mediates the uptake of di- and tripeptides across the cell membrane. It belongs to the Major Facilitator Superfamily (MFS) and adopts the canonical 12-transmembrane-helix MFS fold with N and C domains that cradle a centrally located substrate binding cavity. PepT_St exhibits broad substrate specificity for dipeptides, binding them with millimolar affinity. The structure reveals a highly adaptable binding site that accommodates diverse peptide side chains through conformational changes in binding pocket residues, water network rearrangement, and peptide repositioning. Two crystal structures have been determined: an inward open conformation from the 2012 EMBO J paper and inward-facing partially occluded conformations from the 2018 Structure paper. The 2012 structure provides key insights into the alternating access mechanism of POT family transporters, revealing a hinge-like movement in the C-terminal half that opens the intracellular gate.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##EMBOJ.2012.157 | 4APS | 3.3 A | P212121 | PepT_St from Streptococcus thermophilus, wild type, full length | none (apo, inward open conformation) |
| doi/10.1038##EMBOJ.2011.017 | 2XUT | 3.0 A | not specified | PepT_So from Shewanella oneidensis, wild type, inward occluded conformation | dipeptide substrate |
| doi/10.1016##j.str.2018.01.005 | 5OXK | 2.7 A | -- | PepT_St wild type, full length | Ala-Gln |
| doi/10.1016##j.str.2018.01.005 | 5OXL | 2.5 A | -- | PepT_St wild type, full length | Ala-Leu |
| doi/10.1016##j.str.2018.01.005 | 5OXM | 2.7 A | -- | PepT_St wild type, full length | Asp-Glu |
| doi/10.1016##j.str.2018.01.005 | 5OXN | 2.2 A | -- | PepT_St wild type, full length | Phe-Ala |
| doi/10.1016##j.str.2018.01.005 | 5OXO | 2.0 A | -- | PepT_St wild type, full length | none (apo) |
| doi/10.1016##j.str.2018.01.005 | 5OXP | 2.4 A | -- | PepT_St wild type, full length | phosphate |
| doi/10.1016##j.str.2018.01.005 | 5OXQ | 2.2 A | -- | PepT_St wild type, full length | [HEPES](/xray-mp-wiki/reagents/buffers/hepes), phosphate |
| doi/10.1016##j.str.2018.01.005 | 6EIA | -- | -- | PepT_St wild type, full length | [HEPES](/xray-mp-wiki/reagents/buffers/hepes), phosphate |

## Expression and Purification

- **Expression system**: Escherichia coli C41
- **Construct**: Full-length PepT_St cloned into pNIC-CTHF vector with C-terminal His-Tag and TEV cleavage site
- **Notes**: [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin) resistance marker. Cells grown at 37°C in terrific broth media with 30 µg/ml [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin), induced with 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at OD600 0.6-0.8, continued at 18°C for 16-18 hours.


### Purification Workflow

- **Expression system**: Escherichia coli C41
- **Expression construct**: Full-length PepT_St with C-terminal His-Tag, TEV cleavage site
- **Tag info**: His-Tag, TEV cleavage site

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Membrane fractionation | -- | -- + -- | Cells harvested by centrifugation, pellet stored at -20°C |
| Membrane solubilization | Detergent solubilization | -- | -- + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | -- |
| Affinity chromatography | Ni-NTA affinity chromatography | -- | -- + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | His-Tag affinity capture |
| Size-exclusion chromatography | Size-exclusion chromatography | -- | -- + 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | -- |

**Final sample**: Purified in 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm) at pH 7.5


## Crystallization

### doi/10.1016##j.str.2018.01.005

| Parameter | Value |
|---|---|
| Method | lipidic cubic phase |
| Lipid | [MAG](/xray-mp-wiki/reagents/lipids/mag) 7.8 (1-(7Z-pentadecenoyl)-rac-[Glycerol](/xray-mp-wiki/reagents/additives/glycerol), Avanti Lipids) |
| Protein-to-lipid ratio | 1:1 (volume) |
| Temperature | -- |
| Notes | Crystallization plates set up using Mosquito-LCP robot (TTP Labtech). 50 nl mesophase dispensed in wells, overlaid with 800 nl precipitant. Laminex UV Plastic Bases with 100 µm depth wells sealed with Laminex UV Plastic 200 micron Film Covers. Crystallant contains [HEPES](/xray-mp-wiki/reagents/buffers/hepes), phosphate, and small PEGs. Overall pH between 5.0 and 5.8.
 |

| Parameter | Value |
|---|---|
| Method | lipidic cubic phase |
| Lipid | [MAG](/xray-mp-wiki/reagents/lipids/mag) 7.8 (1-(7Z-pentadecenoyl)-rac-[Glycerol](/xray-mp-wiki/reagents/additives/glycerol), Avanti Lipids) |
| Protein-to-lipid ratio | 1:1 (volume) |
| Temperature | -- |
| Notes | Apo structure obtained by changing buffer to [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate) pH 4.5 to inhibit peptide binding. High-quality 2.0 A inward open structure.
 |

| Parameter | Value |
|---|---|
| Method | lipidic cubic phase |
| Lipid | [MAG](/xray-mp-wiki/reagents/lipids/mag) 7.8 (1-(7Z-pentadecenoyl)-rac-[Glycerol](/xray-mp-wiki/reagents/additives/glycerol), Avanti Lipids) |
| Protein-to-lipid ratio | 1:1 (volume) |
| Notes | Structures with adventitiously bound [HEPES](/xray-mp-wiki/reagents/buffers/hepes) obtained using [HEPES](/xray-mp-wiki/reagents/buffers/hepes) buffer. Increasing [HEPES](/xray-mp-wiki/reagents/buffers/hepes) from 100 mM to 300 mM improved electron density.
 |

| Parameter | Value |
|---|---|
| Method | lipidic cubic phase |
| Lipid | [MAG](/xray-mp-wiki/reagents/lipids/mag) 7.8 (1-(7Z-pentadecenoyl)-rac-[Glycerol](/xray-mp-wiki/reagents/additives/glycerol), Avanti Lipids) |
| Protein-to-lipid ratio | 1:1 (volume) |
| Notes | Structure with phosphate and [PEG](/xray-mp-wiki/reagents/additives/peg) bound obtained using phosphate buffer instead of [HEPES](/xray-mp-wiki/reagents/buffers/hepes).
 |


## Biological / Functional Insights

### Extracellular gate stabilized by conserved salt bridge interactions

Two salt bridge interactions stabilize the extracellular gate in PepT_St: Arg53(H1)-Glu312(H7)
at ~2.9 A and Arg33(H1)-Glu300(H7) at ~3.8 A. The Arg53-Glu312 salt bridge is distal from
the peptide-binding site and plays a supportive role during transport (R53A reduces uptake
by 50%, E312A by 70%). The Arg33-Glu300 salt bridge is positioned next to the peptide-binding
site and is critical for transport (E300A abolishes both proton-driven and counterflow
transport). These interactions orchestrate alternating access within the POT family.

### Proton binding and the ExxERFxYY motif on helix H1

A conserved ExxERFxYY motif on helix H1 is important for proton binding during transport.
Glu25 and Arg26 form a salt bridge (~2.5-2.8 A) close to Glu22. Alanine mutants of this
motif showed measurable uptake only under counterflow conditions, indicating proton binding
is required for transport. Tyr29 retained 75% of WT uptake levels and additionally
functions in determining peptide specificity. Lys126 on helix H4 is positioned close to
the motif and may regulate proton coupling.

### Conserved tyrosines determine peptide binding affinities

The peptide-binding site contains three prominent tyrosine side chains: Tyr29 and Tyr30
from helix H1, and Tyr68 from helix H2. The Tyr29Phe mutant showed decreased affinity
for tri-alanine (IC50 1.4 mM vs 0.4 mM WT) while retaining affinity for di-Glu. The
Tyr68Phe mutant showed decreased affinity for di-Glu (IC50 1.63 mM vs 0.56 mM WT) while
retaining affinity for tri-alanine. The Tyr29Ala and Tyr68Ala mutants lost ability to
transport these peptides altogether while retaining affinity for di-Phe and di-Ala.

### Intracellular gate opening via hinge-like movement in helices H10 and H11

Comparing the inward open PepT_St structure with the occluded PepT_So structure reveals
that the intracellular gate opens through a hinge-like movement at the apex of the H10-H11
helix hairpin, specifically at Gly407 (H10) and Trp427 (H11). The cytoplasmic halves of
H7, H10, and H11 swing away from helices H4-H5, moving ~13 A from their occluded positions.
This opens the peptide-binding site to the intracellular side of the membrane without
requiring movement of the entire H10-H11 helix hairpin.


## Cross-References

- [POT Family (Proton-Dependent Oligopeptide Transporters)](/xray-mp-wiki/concepts/transport-mechanisms/pot-family/) — PepT_St is a member of the POT family
- [Major Facilitator Superfamily](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — POT family is a subgroup of MFS transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — POTs transport via alternating access between inward-open and outward-open states
- [PepT_So Oligopeptide Transporter](/xray-mp-wiki/proteins/mfs-transporters/pept-so/) — Another POT family member with reported crystal structure; key comparison for alternating access
- [PEG 400](/xray-mp-wiki/reagents/additives/peg-400/) — Cryoprotectant used in PepT_St crystallization
- [Selenomethionine](/xray-mp-wiki/reagents/additives/selenomethionine/) — Used for anomalous phasing in PepT_St structure determination
- [Mercury(II) Chloride](/xray-mp-wiki/reagents/additives/mercury-ii-chloride/) — Heavy atom derivative used for MIRAS phasing
- [Multiple Isomorphous Replacement with Anomalous Scattering (MIRAS)](/xray-mp-wiki/methods/structure-determination/miras/) — Phasing method used to solve the PepT_St structure
- [PepT_So2 Oligopeptide Transporter](/xray-mp-wiki/proteins/mfs-transporters/pept-so2/) — Another POT family member from Shewanella oneidensis, inward open conformation with substrate
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) — Additive used in purification or crystallization buffers
