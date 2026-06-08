---
title: FocA (Formate Channel A from Vibrio cholerae)
created: 2026-06-02
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10881, doi/10.1038##nsmb.1740]
verified: false
---

# FocA (Formate Channel A from Vibrio cholerae)

## Overview

FocA (formate channel A) from Vibrio cholerae is a pentameric membrane channel belonging to the FNT (formate/nitrite transporter) family. It functions as a formate transporter and was crystallized at 2.13 A (low-formate) and 2.5 A (high-formate) resolution in space group P2_1 2_1 2_1. Each monomer consists of six transmembrane helices with a substrate translocation pore running through the center of the monomer (not the pentamer axis). The selectivity filter comprises a cytoplasmic slit and a central constriction ring (2.3 A diameter). Two formate ions were observed bound in the cytoplasmic slit in the high-formate structure. The channel exhibits flexibility in the Omega loop connecting TM2a and TM3, which modulates the slit dimensions. The structure is similar in overall fold to water and glycerol channels (Aqp1, GlpF). The V. cholerae FocA has been characterized alongside the E. coli FocA (PDBs 3KLZ, 3Q7K), which features ten transmembrane helices per protomer with pH-dependent gating.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.1740 | Not available (not deposited in PDB at time of paper) | 2.13 | P2_1 2_1 2_1 | Full-length FocA from Vibrio cholerae (280 residues) | Formate (20 mM in crystallization) |
| doi/10.1038##nsmb.1740 | Not available (not deposited in PDB at time of paper) | 2.5 | P2_1 2_1 2_1 | Full-length FocA from Vibrio cholerae (280 residues) | Formate (120 mM in crystallization; 2 formate ions bound) |

 - R-work 18.0%, R-free 21.0%; Atoms: 9818; Data collection: SIRAS phasing with platinum derivative; noncrystallographic symmetry averaging
 - R-work 17.0%, R-free 22.0%; Atoms: 9844; Data collection: High-formate crystal form with 2 bound formate ions in cytoplasmic slit

## Expression and Purification

- **Expression system**: E. coli (C43)
- **Construct**: Full-length FocA from Vibrio cholerae (280 residues), C-terminal decahistidine tag, pBAD vector
- **Notes**: Overexpressed from pBAD vector in E. coli C43 cells

### Purification Workflow

- **Expression system**: E. coli (C43)
- **Tag info**: C-terminal decahistidine tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization | DDM solubilization | — | 1% (w/v) DDM | Membrane solubilization after cell disruption |
| Affinity purification | Co2+ affinity (TALON resin) | TALON Co2+ resin | — | Incubated overnight; washed then eluted |
| Elution | Affinity elution | TALON Co2+ resin | 1.1% octylglucoside + 20 mM sodium formate + 100 mM NaCl + 8% glycerol + 10 mM Tris, pH 7.5 | Elution from TALON resin |
| Size-exclusion chromatography | SEC (Sephadex 200) | Sephadex 200 (Akta FPLC, GE Healthcare) | Elution buffer from affinity step | Peak fractions collected and concentrated to ~8 mg/mL |


## Crystallization

### doi/10.1038##nsmb.1740

| Parameter | Value |
|---|---|
| Method | Sitting drop vapor diffusion |
| Protein sample | ~8 mg/mL FocA in elution buffer (1.1% octylglucoside, 20 mM sodium formate, 100 mM NaCl, 8% glycerol, 10 mM Tris pH 7.5) |
| Reservoir | 32% (v/v) PEG 550 monomethyl ether + 25 mM MgCl2 |
| Mixing ratio | Not specified |
| Temperature | Not specified |
| Growth time | 2 days |
| Notes | Low-formate crystals grown with 20 mM formate; high-formate crystals with 120 mM sodium formate + 20 mM MOPS pH 6.7 |


## Biological / Functional Insights

### Formate selectivity filter architecture

The FocA selectivity filter consists of a cytoplasmic slit (2.1 x 4.1 A) and a central constriction ring (2.3 A diameter). The slit is formed by Leu78 (TM2a), Leu88 and Thr90 (Omega loop), and Val174 (TM4). His208 (S loop) sits on the periplasmic side. The central ring is formed by Phe74 (TM2a), Phe201 (TM5a), His208 C-beta (S loop), and Ala211 (TM5b). The pore is basic on the cytoplasmic one-third and hydrophobic on the periplasmic two-thirds. All selectivity filter residues are highly conserved among FNT members including both FocA and NirC.

### Two formate ions bound in cytoplasmic slit

In the high-formate (2.5 A) structure, two formate ions (FMT1 and FMT2) are bound in the cytoplasmic slit. FMT2 forms hydrogen bonds with His208 (N epsilon 2 atom) and van der Waals contacts with Leu88, Thr90, and Asn171. FMT1 sits closer to the cytoplasmic surface, forming hydrogen bonds with FMT2 and van der Waals contacts with Leu88, Phe89, and Asn171. This provides a structural basis for substrate selectivity: the slit dimensions and hydrogen bonding network specifically accommodate formate in a coin-in-slot orientation.

### Omega loop flexibility modulates slit dimensions

The Omega loop connecting TM2a and TM3 adopts two distinct configurations (UP and DOWN) across the five monomers in the crystal. In the UP configuration (monomers A-C), Thr90 and Ser91 are positioned within the slit, narrowing it to 2.1 x 4.1 A. In the DOWN configuration (monomers D-E), the Omega loop moves away, widening the slit to 2.1 x 7.2 A. This flexibility may have mechanistic consequences for substrate access and selectivity, analogous to variations observed in the E. coli water channel AqpZ.

### Pentameric architecture with monomeric transport pores

FocA forms a homopentamer with a diameter of 82 A and thickness of 58 A. The monomer-monomer interface is large (~1,450 A^2) with high surface complementarity (0.68), comparable to antibody-antigen interfaces. However, unlike many pentameric channels, the transport pore is located within each monomer (not at the pentamer axis). The central pentamer pore is too wide to be a selectivity filter and is probably occupied by lipid molecules in the native membrane.

### Transport activity confirmed by 14C formate uptake

Concentrative uptake assay demonstrated formate transport into proteoliposomes reconstituted with purified FocA at pH 6.7. No pH or electrochemical gradient existed across the proteoliposome membrane, suggesting FocA functions as a formate channel or uniporter. The assay used 14C-labeled sodium formate with E. coli total phospholipid proteoliposomes.


## Cross-References

- [FNT Family (Formate/Nitrite Transporter Family)](/xray-mp-wiki/concepts/fnt-family/) — FocA is a member of the FNT family
- [HSC (Hydrosulfide Channel from Clostridium difficile)](/xray-mp-wiki/proteins/hsc/) — Related FNT family channel; extensively compared with FocA in the paper
- [HiTehA (TehA from Haemophilus influenzae)](/xray-mp-wiki/proteins/hiteha/) — Related anion channel within the FNT superfamily
- [Aqp1 (Aquaporin 1 from E. coli)](/xray-mp-wiki/proteins/aqp1/) — Water channel with similar monomeric pore architecture
- [GlpF (Glycerol Facilitator from E. coli)](/xray-mp-wiki/proteins/glycerol-facilitator/) — Glycerol channel with similar monomeric pore architecture
- [Ion Channel Selectivity Filter](/xray-mp-wiki/concepts/selectivity-filter/) — FocA selectivity filter with cytoplasmic slit and central constriction ring
