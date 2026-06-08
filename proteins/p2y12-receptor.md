---
title: Human P2Y12 Receptor
created: 2026-05-27
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.bcp.2022.115291, doi/10.1038##nature13083]
verified: false
---

# Human P2Y12 Receptor

## Overview

The P2Y12 receptor is a class A G protein-coupled receptor (GPCR) expressed on human platelets that mediates ADP-induced platelet activation and aggregation. It is a critical drug target for antiplatelet therapy in the prevention of atherothrombosis. The P2Y12 receptor constitutively activates Gi/o protein signaling, and its inverse agonists can blunt this basal signaling, offering therapeutic advantages over neutral antagonists. The receptor exhibits high plasticity in its ligand binding pocket with striking conformational changes in extracellular regions, distinguishing it from other class A GPCRs.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.bcp.2022.115291 | 7pp1 | 2.78 A | C2 | Human P2Y12 receptor with BRIL fused to ICL3 at T223-R224, D294(7.49)N mutation | selatogrel (ACT-246475) |
| doi/10.1038##nature13083 | 4ntj | 2.6 A | C2 | Human P2Y12 receptor with BRIL fused to ICL3 at T223-R224, D294(7.49)N mutation | AZD1283 |

## Expression and Purification

- **Expression system**: Sf9 insect cells
- **Construct**: Human P2Y12 receptor-BRIL fusion protein. BRIL (thermostabilized apocytochrome b562 RIL) fused into ICL3 at T223-R224 with D294(7.49)N mutation for improved yield.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | Sf9 insect cell expression | -- | -- + -- | P2Y12-BRIL fusion protein expressed in Sf9 insect cells; expressed as previously described |
| Affinity chromatography | Immobilized metal affinity chromatography | IMAC | -- + -- | Purified in the presence of 2 mM selatogrel to stabilize the receptor-ligand complex |


## Crystallization

### doi/10.1016##j.bcp.2022.115291

| Parameter | Value |
|---|---|
| Method | X-ray crystallography |
| Protein sample | P2Y12-BRIL in complex with selatogrel (2 mM) |
| Notes | Data collection and structure refinement statistics in Table 2 of the original paper. PDB accession code 7pp1. |

### doi/10.1038##nature13083

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | P2Y12R-BRIL (D294N mutation) in complex with AZD1283 |
| Notes | Data collection from 15 crystals at 23ID-B/D beamline (GM/CA CAT) at APS using 10 um minibeam at 1.0330 A wavelength. Structure solved by molecular replacement using PAR1 (PDB 3VW7) and BRIL (PDB 1M6T) as initial models. Two receptor molecules form parallel dimer mediated by helix V. Two cholesterol molecules bound per receptor. |


## Biological / Functional Insights

### Inverse agonist efficacy of selatogrel

Selatogrel acts as an inverse agonist of the P2Y12 receptor, stabilizing the inactive form of the Gi/o-Gbeta gamma complex. Using BRET2 probes, selatogrel, ticagrelor, and elinogrel were shown to increase the BRET signal, indicating reassembly of the Gi alpha-G gamma subunits from the active dissociated state. Selatogrel was approximately 100-fold more potent than ticagrelor in dose-response experiments, with comparable maximal efficacy. Selatogrel completely abolished constitutive P2Y12 receptor activity in cAMP assays and increased basal cAMP levels in human platelets.

### Unique straight helix V conformation

The 2.6 A structure of P2Y12R-AZD1283 (PDB 4NTJ) revealed a distinct straight conformation of helix V, setting P2Y12R apart from all other known class A GPCR structures. While helix V in most class A GPCRs is bulged and bent at a highly conserved Pro5.50, P2Y12R has Asn201 at position 5.50, resulting in a lack of helical bend. The straight helix V extends approximately 2 additional helical turns above the extracellular side of the membrane, shifting its extracellular end towards helix IV by more than 6 A compared to other class A GPCRs. This feature is shared with S1P1 receptor but extends further in P2Y12R.

### Dynamic disulfide bridge between helix III and ECL2

The conserved disulfide bridge between Cys97 in helix III and Cys175 in ECL2, which is observed in all other GPCR structures solved to date, is not observed in the P2Y12R structure. No electron density is visible for most of ECL2 or for C97, suggesting a labile or dynamic disulfide bond. C97A and C175A mutations retain similar protein yield and stability, and their melting temperatures in complex with AZD1283 are substantially higher than in the apo form. This labile disulfide may leave C97 available for interactions with the thiol moieties of drug metabolites such as the active metabolites of clopidogrel and prasugrel.

### Two-pocket ligand binding model

Within the P2Y12R extracellular cavity, residues Tyr105(3.33) and Lys280(7.35) form a barrier separating the cavity into two pockets. Pocket 1 is composed of helices III-VII and forms the binding site for AZD1283. Pocket 2 consists of helices I-III and VII and is unoccupied in the structure. Dinucleotide docking suggests one nucleotide may bind in pocket 1 while the second half wraps around helix III to reach pocket 2, with the polyphosphate moiety occupying a highly cationic region. This two-pocket model extends understanding of purinoceptor family ligand recognition mechanisms.

### Basal activity and DRY motif rearrangement

The P2Y12R structure shows that the intracellular tip of helix VII is in an inward position, and helix VI is shifted outward and translated by a half helical turn compared to other GPCRs. The conserved Arg122(3.50) in the DRY motif is at the same level as hydrophobic residue Val238(6.37), excluding formation of the ionic lock between helix VI and the DRY motif. The lack of ionic lock and active-like conformations of intracellular helices VI and VII suggest P2Y12R is more prone to activation, consistent with reported high basal activity of this receptor.

### Constitutive Gi/o protein signaling

The P2Y12 receptor constitutively activates Gi- and Go-protein-mediated signaling in human platelets. BRET assays with G alpha-RLuc8 probes showed that P2Y12 receptor expression significantly reduced the basal BRET signal compared to no-receptor controls, indicating constitutive G protein activation. This constitutive activity was specific to Gi and Go isoforms, with no significant effect on Gq or Gs proteins. The constitutive activation was associated with high thrombotic risk in diabetes patients and correlated with bleeding syndrome when abolished.

### Selatogrel binding mode and inactive conformation

The 2.78 A resolution crystal structure of P2Y12-BRIL bound to selatogrel (PDB 7pp1) confirmed that selatogrel stabilizes the inactive, basal state of the receptor. Selatogrel binds to pocket 1, spanning helix III to VII. The binding mode shows steric overlap with the proposed binding site of ADP and the ADP analog 2MeSADP, consistent with competitive antagonism of ADP binding. Key residues His 187(5.38), Phe 252(6.51), Arg 256(6.55), and Lys 280(7.35) are essential for high-affinity selatogrel interaction. The conformational change of Tyr 259(6.58) is specific to selatogrel binding and distinguishes its binding mode from other P2Y12 ligands.

### Comparison with other P2Y12 receptor structures

Compared to the AZD1283-bound P2Y12 structure (PDB 4NTJ), the selatogrel-bound receptor conformation is highly similar and clearly in the antagonized state, with only minor side chain rearrangements in the ligand binding site. The selatogrel-bound structure (7PP1) represents the basal state, while the 2MeSADP-bound structure (PDB 4PXZ) represents the active state. Selatogrel pushes Tyr 259(6.58) farther out of the pocket than AZD1283. Elinogrel showed off-target effects on multiple G-protein subtypes (Gi, Go, Gq, Gs) in HEK293T cells, limiting its therapeutic window.


## Cross-References

- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — BRIL fused to ICL3 for crystallization
- [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel/) — Co-crystallized inverse agonist ligand
- [AZD1283](/xray-mp-wiki/reagents/ligands/azd1283/) — Co-crystallized reversible antagonist in first P2Y12 structure (PDB 4NTJ)
- [Ticagrelor](/xray-mp-wiki/reagents/ligands/ticagrelor/) — Related P2Y12 inverse agonist for comparison
- [Elinogrel](/xray-mp-wiki/reagents/ligands/elinogrel/) — Related P2Y12 antagonist studied in paper
- [GPCR Active Conformation](/xray-mp-wiki/concepts/gpcr-active-conformation/) — Selatogrel stabilizes inactive conformation vs active
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — IMAC purification method used
- [A2A-PSB1-bRIL Adenosine A2A Receptor](/xray-mp-wiki/proteins/a2a-psb1-bril/) — Related GPCR-BRIL fusion structure
