---
title: Human P2Y12 Receptor
created: 2026-05-27
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein]
sources: [doi/10.1016##j.bcp.2022.115291, doi/10.1038##nature13083, doi/10.1038##nature13288]
verified: false
---

# Human P2Y12 Receptor

## Overview

The P2Y12 receptor is a class A G protein-coupled receptor (GPCR) expressed on human platelets that mediates [ADP](/xray-mp-wiki/reagents/ligands/adp)-induced platelet activation and aggregation. It is a critical drug target for antiplatelet therapy. The receptor exhibits high plasticity in its extracellular regions with striking conformational changes between agonist- and antagonist-bound states, distinguishing it from other class A GPCRs. The first structure of a GPCR bound to an agonist revealed large-scale extracellular rearrangements forming a closed lid over the ligand binding pocket.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.bcp.2022.115291 | 7pp1 | 2.78 A | C2 | Human P2Y12 receptor with [BRIL](/xray-mp-wiki/reagents/protein-tags/bril) fused to ICL3 at T223-R224, D294(7.49)N mutation | [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel) (ACT-246475) |
| doi/10.1038##nature13083 | 4ntj | 2.6 A | C2 | Human P2Y12 receptor with [BRIL](/xray-mp-wiki/reagents/protein-tags/bril) fused to ICL3 at T223-R224, D294(7.49)N mutation | [AZD1283](/xray-mp-wiki/reagents/ligands/azd1283) |
| doi/10.1038##nature13288 | ~ | 2.5 A | C222(1) | Human P2Y12 receptor with BRIL fused to ICL3 at T223-R224, D294(7.49)N mutation | [2MeSADP](/xray-mp-wiki/reagents/ligands/2me-sadp) |
| doi/10.1038##nature13288 | ~ | 3.1 A | C2 | Human P2Y12 receptor with BRIL fused to ICL3 at T223-R224, D294(7.49)N mutation | [2MeSATP](/xray-mp-wiki/reagents/ligands/2me-satp) |

## Expression and Purification

- **Expression system**: Sf9 insect cells
- **Construct**: Human P2Y12 receptor-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril) fusion protein. [BRIL](/xray-mp-wiki/reagents/protein-tags/bril) (thermostabilized apocytochrome b562 RIL) fused into ICL3 at T223-R224 with D294(7.49)N mutation for improved yield.

### Purification Workflow

*Source: doi/10.1016##j.bcp.2022.115291*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | Sf9 insect cell expression | -- | -- + -- | P2Y12-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril) fusion protein expressed in Sf9 insect cells; expressed as previously described |
| Affinity chromatography | Immobilized metal affinity chromatography | IMAC | -- + -- | Purified in the presence of 2 mM [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel) to stabilize the receptor-ligand complex |

### Purification Workflow

*Source: doi/10.1038##nature13288*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| 1. Membrane preparation | Hypotonic buffer washing with low and high salt | — |  | Membranes washed repeatedly before solubilization |
| 2. Ligand incubation | Incubation with 20 uM ligand | — |  | 2MeSADP or 2MeSATP in presence of 2 mg/ml iodoacetamide and EDTA-free protease inhibitor cocktail, 30 min |
| 3. Solubilization | Detergent extraction | — | 0.5% DDM + 0.1% cholesteryl hemisuccinate (CHS) | 4 deg C, 2.5 h |
| 4. Affinity chromatography | TALON IMAC | TALON IMAC resin (Clontech) | 50 mM HEPES pH 7.5, 1 M NaCl, 10% glycerol, 0.05% DDM, 0.01% CHS | Wash with 30 mM imidazole, elute with 270 mM imidazole |
| 5. Buffer exchange and tag removal | PD MiniTrap G-25, PreScission protease + PNGase F treatment | — |  | Ligand increased to 2 mM after buffer exchange. His-tag removed by PreScission protease. Deglycosylated by PNGase F. Cleaved tag removed by Ni-NTA. |

**Final sample**: 30-40 mg/ml purified P2Y12R-BRIL in complex with ligand
**Yield**: N/A


## Crystallization

### doi/10.1016##j.bcp.2022.115291

| Parameter | Value |
|---|---|
| Method | X-ray crystallography |
| Protein sample | P2Y12-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril) in complex with [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel) (2 mM) |
| Notes | Data collection and structure refinement statistics in Table 2 of the original paper. PDB accession code 7pp1. |

### doi/10.1038##nature13083

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | P2Y12R-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril) (D294N mutation) in complex with [AZD1283](/xray-mp-wiki/reagents/ligands/azd1283) |
| Notes | Data collection from 15 crystals at 23ID-B/D beamline (GM/CA CAT) at APS using 10 um minibeam at 1.0330 A wavelength. Structure solved by molecular replacement using [PAR1](/xray-mp-wiki/proteins/par1) (PDB 3VW7) and [BRIL](/xray-mp-wiki/reagents/protein-tags/bril) (PDB 1M6T) as initial models. Two receptor molecules form parallel dimer mediated by helix V. Two [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) molecules bound per receptor. |

### doi/10.1038##nature13288

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | P2Y12R-BRIL in complex with 2MeSADP |
| Lipid | 10% cholesterol, 90% monoolein |
| Growth time | 1 week |
| Notes | Crystals appeared in 0.30-0.45 M ammonium acetate, 0.1 M sodium citrate pH 5.0, 30-40% PEG400, 3% 1-propanol, 500 uM 2MeSADP. Crystal size: 80 x 50 x 5 um3. 17 crystals used. Data collected at SPring-8 BL41XU beamline using 10 um minibeam. |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization |
| Protein sample | P2Y12R-BRIL in complex with 2MeSATP |
| Notes | 6 crystals used for data collection. Crystal size: 30 x 30 x 5 um3. |


## Biological / Functional Insights

### Inverse agonist efficacy of selatogrel

[Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel) acts as an inverse agonist of the P2Y12 receptor, stabilizing the inactive form of the Gi/o-Gbeta gamma complex. Using BRET2 probes, [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel), [Ticagrelor](/xray-mp-wiki/reagents/ligands/ticagrelor), and [Elinogrel](/xray-mp-wiki/reagents/ligands/elinogrel) were shown to increase the BRET signal, indicating reassembly of the Gi alpha-G gamma subunits from the active dissociated state. [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel) was approximately 100-fold more potent than [Ticagrelor](/xray-mp-wiki/reagents/ligands/ticagrelor) in dose-response experiments, with comparable maximal efficacy. [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel) completely abolished constitutive P2Y12 receptor activity in cAMP assays and increased basal cAMP levels in human platelets.

### Unique straight helix V conformation

The 2.6 A structure of P2Y12R-[AZD1283](/xray-mp-wiki/reagents/ligands/azd1283) (PDB 4NTJ) revealed a distinct straight conformation of helix V, setting P2Y12R apart from all other known class A GPCR structures. While helix V in most class A GPCRs is bulged and bent at a highly conserved Pro5.50, P2Y12R has Asn201 at position 5.50, resulting in a lack of helical bend. The straight helix V extends approximately 2 additional helical turns above the extracellular side of the membrane, shifting its extracellular end towards helix IV by more than 6 A compared to other class A GPCRs. This feature is shared with [S1P1](/xray-mp-wiki/proteins/s1p1) receptor but extends further in P2Y12R.

### Dynamic disulfide bridge between helix III and ECL2

The conserved disulfide bridge between Cys97 in helix III and Cys175 in ECL2, which is observed in all other GPCR structures solved to date, is not observed in the P2Y12R structure. No electron density is visible for most of ECL2 or for C97, suggesting a labile or dynamic disulfide bond. C97A and C175A mutations retain similar protein yield and stability, and their melting temperatures in complex with [AZD1283](/xray-mp-wiki/reagents/ligands/azd1283) are substantially higher than in the apo form. This labile disulfide may leave C97 available for interactions with the thiol moieties of drug metabolites such as the active metabolites of clopidogrel and prasugrel.

### Two-pocket ligand binding model

Within the P2Y12R extracellular cavity, residues Tyr105(3.33) and Lys280(7.35) form a barrier separating the cavity into two pockets. Pocket 1 is composed of helices III-VII and forms the binding site for [AZD1283](/xray-mp-wiki/reagents/ligands/azd1283). Pocket 2 consists of helices I-III and VII and is unoccupied in the structure. Dinucleotide docking suggests one nucleotide may bind in pocket 1 while the second half wraps around helix III to reach pocket 2, with the polyphosphate moiety occupying a highly cationic region. This two-pocket model extends understanding of purinoceptor family ligand recognition mechanisms.

### Basal activity and DRY motif rearrangement

The P2Y12R structure shows that the intracellular tip of helix VII is in an inward position, and helix VI is shifted outward and translated by a half helical turn compared to other GPCRs. The conserved Arg122(3.50) in the DRY motif is at the same level as hydrophobic residue Val238(6.37), excluding formation of the ionic lock between helix VI and the DRY motif. The lack of ionic lock and active-like conformations of intracellular helices VI and VII suggest P2Y12R is more prone to activation, consistent with reported high basal activity of this receptor.

### Constitutive Gi/o protein signaling

The P2Y12 receptor constitutively activates Gi- and Go-protein-mediated signaling in human platelets. BRET assays with G alpha-RLuc8 probes showed that P2Y12 receptor expression significantly reduced the basal BRET signal compared to no-receptor controls, indicating constitutive G protein activation. This constitutive activity was specific to Gi and Go isoforms, with no significant effect on Gq or Gs proteins. The constitutive activation was associated with high thrombotic risk in diabetes patients and correlated with bleeding syndrome when abolished.

### Selatogrel binding mode and inactive conformation

The 2.78 A resolution crystal structure of P2Y12-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril) bound to [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel) (PDB 7pp1) confirmed that [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel) stabilizes the inactive, basal state of the receptor. [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel) binds to pocket 1, spanning helix III to VII. The binding mode shows steric overlap with the proposed binding site of [ADP](/xray-mp-wiki/reagents/ligands/adp) and the [ADP](/xray-mp-wiki/reagents/ligands/adp) analog 2MeSADP, consistent with competitive antagonism of [ADP](/xray-mp-wiki/reagents/ligands/adp) binding. Key residues His 187(5.38), Phe 252(6.51), Arg 256(6.55), and Lys 280(7.35) are essential for high-affinity [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel) interaction. The conformational change of Tyr 259(6.58) is specific to [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel) binding and distinguishes its binding mode from other P2Y12 ligands.

### Comparison with other P2Y12 receptor structures

Compared to the [AZD1283](/xray-mp-wiki/reagents/ligands/azd1283)-bound P2Y12 structure (PDB 4NTJ), the [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel)-bound receptor conformation is highly similar and clearly in the antagonized state, with only minor side chain rearrangements in the ligand binding site. The [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel)-bound structure (7PP1) represents the basal state, while the 2MeSADP-bound structure (PDB 4PXZ) represents the active state. [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel) pushes Tyr 259(6.58) farther out of the pocket than [AZD1283](/xray-mp-wiki/reagents/ligands/azd1283). [Elinogrel](/xray-mp-wiki/reagents/ligands/elinogrel) showed off-target effects on multiple G-protein subtypes (Gi, Go, Gq, Gs) in HEK293T cells, limiting its therapeutic window.

### Agonist-induced extracellular lid closure

The 2.5 A structure of P2Y12R bound to the full agonist 2MeSADP reveals striking conformational changes in the extracellular region compared to the antagonist-bound structure. Helices VI and VII move inward towards the 7TM bundle (helix VI tip moves ~3.5 A, helix VII tip moves ~6.1 A), and the extracellular loops (ECL2, ECL3) and N-terminus form a closed lid that almost completely encloses the agonist. This is the first example of a GPCR in which agonist access to the binding pocket requires large-scale rearrangements in the extracellular region. The rearrangements involve distortion of helix III by formation of a disulfide bond between C97(3.25) and C175(ECL2), which is labile in the antagonist-bound state.

### 2MeSADP binding pocket and key residues

The 2MeSADP binding pocket involves residues from helices III, IV, V, VI, and VII. The alpha- and beta-phosphate groups are coordinated by cationic residues K280(7.35), R256(6.55), and R93(3.21). Three water molecules bridge the interaction between the beta-phosphate and R19 (N-terminus). The ribose 3'-hydroxyl group hydrogen bonds with the main chain carbonyl of C97(3.25), and the main chain NH of C175(ECL2) interacts with the beta-phosphate. The conserved K174(ECL2) does not directly contact the agonist but forms a salt bridge with E273(7.28) to stabilize the agonist-bound conformation. R265(ECL3) is positioned away from 2MeSADP, contrary to previous predictions.


## Cross-References

- [BRIL Fusion Protein](/xray-mp-wiki/reagents/protein-tags/bril/) — BRIL fused to ICL3 for crystallization
- [Selatogrel](/xray-mp-wiki/reagents/ligands/selatogrel/) — Co-crystallized inverse agonist ligand
- [AZD1283](/xray-mp-wiki/reagents/ligands/azd1283/) — Co-crystallized reversible antagonist in first P2Y12 structure (PDB 4NTJ)
- [Ticagrelor](/xray-mp-wiki/reagents/ligands/ticagrelor/) — Related P2Y12 inverse agonist for comparison
- [Elinogrel](/xray-mp-wiki/reagents/ligands/elinogrel/) — Related P2Y12 antagonist studied in paper
- [GPCR Active Conformation](/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/) — Selatogrel stabilizes inactive conformation vs active
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — IMAC purification method used
- [A2A-PSB1-bRIL Adenosine A2A Receptor](/xray-mp-wiki/proteins/gpcr/a2a-psb1-bril/) — Related GPCR-BRIL fusion structure
- [PAR1](/xray-mp-wiki/proteins/par1) — Related protein structure
- [S1P1](/xray-mp-wiki/proteins/s1p1) — Related protein structure
