---
title: Human Adenosine A2A Receptor A2A-StaR2-bRIL (PDB 7ARO)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1021##acs.jmedchem.0c01856, doi/10.1021##acs.jmedchem.2c00462]
verified: false
---

# Human Adenosine A2A Receptor A2A-StaR2-bRIL (PDB 7ARO)

## Overview

The A2A-StaR2-bRIL construct is an engineered human adenosine A2A receptor with nine thermostabilizing mutations (A54L, T88A, R107A, K122A, N154A, L202A, L235A, V239A, S277A), N-terminal deletion of the first three residues, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation) after residue 315 with a His10 tag, and apocytochrome b562 RIL (bRIL) fused into the third intracellular loop between residues L208 and G218. The crystal structure (PDB 7ARO, 1.9 A) was solved in complex with the nonriboside partial agonist LUF5833 (compound 8), a dicyanopyridine derivative that lacks the ribose moiety typical of adenosine agonists.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1021##acs.jmedchem.0c01856 | 7ARO | 1.9 A | P212121 | A2A-StaR2-bRIL: human A2AR with 9 thermostabilizing mutations (A54L, T88A, R107A, K122A, N154A, L202A, L235A, V239A, S277A), N-terminal deletion of first 3 residues, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation) after L315 with 3 alanines + 10 histidines, bRIL fused into ICL3 (L208-G218)
 | [LUF5833 (Compound 8)](/xray-mp-wiki/reagents/ligands/luf5833) (compound 8) |
| doi/10.1021##acs.jmedchem.2c00462 | 8CU7 | 2.05 A | not specified | A2A-StaR2-bRIL: human A2AR with 9 thermostabilizing mutations (A54L, T88A, R107A, K122A, N154A, L202A, L235A, V239A, S277A), N-terminal deletion, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation) after L315 with His10 tag, bRIL fused into ICL3 (L208-G218)
 | [LJ-4517 (Compound 2)](/xray-mp-wiki/reagents/ligands/lj-4517) (compound 2) |

## Expression and Purification

- **Expression system**: HEK293 mammalian cells
- **Construct**: A2A-StaR2-bRIL: human adenosine A2A receptor with 9 thermostabilizing mutations, N-terminal 3-residue deletion, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/truncation) after L315 with His10 tag, bRIL fusion in ICL3


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane preparation | HEK293 cell expression; membranes harvested by ultracentrifugation at 200,000g for 50 min | -- | 50 mM [Tris-HCl](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.6 + -- | Membranes washed with 1 M NaCl; resuspended in [Tris](/xray-mp-wiki/reagents/buffers/tris) buffer with protease inhibitors; frozen at -80 C |
| Solubilization | Membranes incubated with 3 mM [Theophylline](/xray-mp-wiki/reagents/ligands/theophylline) for 2 h at room temperature, then solubilized with 1.5% DM at 4 C for 2 h | -- | 40 mM [Tris](/xray-mp-wiki/reagents/buffers/tris) pH 7.6 + 1.5% DM (n-decyl-beta-D-maltopyranoside) | [Theophylline](/xray-mp-wiki/reagents/ligands/theophylline) present during solubilization to stabilize receptor |
| [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) Superflow cartridge (Qiagen) | [Ni-NTA](/xray-mp-wiki/reagents/additives/nickel-nta) Superflow cartridge | 40 mM Tris pH 7.6, 1 mM [Theophylline](/xray-mp-wiki/reagents/ligands/theophylline) + DM | Elution with buffer containing 1 mM [Theophylline](/xray-mp-wiki/reagents/ligands/theophylline); fractions pooled and concentrated |
| [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | Superdex200 [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) (GE Healthcare) | Superdex200 | 40 mM [Tris](/xray-mp-wiki/reagents/buffers/tris) pH 7.6, DM + DM | Concentrated to ~35 mg/mL; ultracentrifuged at 436,000g prior to crystallization; protein concentration measured by DC assay |


## Crystallization

### doi/10.1021##acs.jmedchem.0c01856

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) [crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) with in meso soaking |
| Protein sample | A2A-StaR2-bRIL in complex with [Theophylline](/xray-mp-wiki/reagents/ligands/theophylline) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Protein-to-lipid ratio | 40:60 (w/w) |
| Temperature | 20 C |
| Growth time | Crystals grew within 2 weeks; soaked for 24 h with 1 mM compound 8 |
| Cryoprotection | None; flash-frozen in liquid nitrogen |
| Notes | Crystals first formed with [Theophylline](/xray-mp-wiki/reagents/ligands/theophylline) in LCP, then incisions were made and wells flooded with mother liquor containing 1 mM compound 8 (LUF5833). Single crystals mounted in LithoLoops and flash-frozen. Data collected at Swiss Light Source beamline X06SA on Eiger 16M detector.
 |

### doi/10.1021##acs.jmedchem.2c00462

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) [crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) |
| Protein sample | A2A-StaR2-bRIL in complex with [LJ-4517 (Compound 2)](/xray-mp-wiki/reagents/ligands/lj-4517) (compound 2, 30 mg/mL) |
| Lipid | Monoolein/cholesterol (9:1 w/w) |
| Protein-to-lipid ratio | 2:3 (v/v) protein to lipid |
| Temperature | not specified |
| Growth time | Crystals appeared within 6 days, maximum size 50 x 10 x 3 um |
| Cryoprotection | Flash-frozen in liquid nitrogen |
| Notes | Crystals harvested directly from [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) using 50 um microcounts (MiTeGen) and flash-frozen. Data collected at 23ID-B beamline of the Advanced Photon Source, Argonne, IL, equipped with Dectris Eiger 16M detector.
 |


## Biological / Functional Insights

### Partial agonist binding pocket analysis

Compound 8 (LUF5833) binds in the orthosteric pocket with its pyridine core positioned similarly to the adenine moiety in NECA, lying between I274(7.39) and F168(5.29). The phenyl substituent extends deepest into the receptor, contacting W246 and forming pi-pi stacking with F168. One cyano group forms a hydrogen bond with N253(6.55), and the exocyclic amine interacts with both N253(6.55) and E169(ECL2). The [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) substituent lies nearest the extracellular face, contacting L267(7.32), M270(7.35), Y271(7.36), and I274(7.39). Nine thermostabilizing mutations were reverted to wild-type in the docking models.

### Structural comparison with antagonist and agonist states

Comparison of the 7ARO structure (compound 8 partial agonist) with the antagonist-bound structure ([ZM241385](/xray-mp-wiki/reagents/ligands/zm241385), PDB 5IU4) and the agonist-bound structure (NECA, PDB 2YDV) reveals that the compound 8 binding pocket shares characteristics of both states. The antagonist-bound pocket does not include the "agonistic" residues S277(7.42) and H278(7.43), while the agonist-bound pocket includes these residues along with T88(3.36). The overall protein-protein RMSD between compound 8 and ZM241385 structures was 0.65 A, consistent with the same receptor construct.

### Derivative pharmacology and activation mechanism

Six derivatives of compound 8 were synthesized to probe the activation mechanism. Compounds 1 and 4, which retain the cyano substituent on the amino "left-hand" side, behaved as partial agonists (Emax 41% and 37%). Compounds 2 and 3, lacking this cyano group, acted as inverse agonists (Emax -48% and -50%). Compound 6 showed neither activation nor inactivation, suggesting neutral antagonism. Induced-fit docking showed that subtle ligand movements in the binding pocket, particularly the position of the phenyl moiety relative to S277 and H278, determined the activation profile.

### Nucleoside antagonist LJ-4517 binding mode (PDB 8CU7)

The nucleoside antagonist LJ-4517 (compound 2) was co-crystallized with A2A-StaR2-bRIL at 2.05 A resolution (PDB 8CU7). The truncated ribose moiety of LJ-4517 only transiently contacts His278(7.43), unlike agonists that simultaneously engage both Ser277(7.42) and His278(7.43). The C8-thiophene group occupies a hydrophobic subpocket that restricts receptor conformational rearrangements required for activation. The n-hexynyl group extends into an open exosite, distinguishing this binding mode from the [ZM241385](/xray-mp-wiki/reagents/ligands/zm241385)-bound structure where the exosite is closed by Tyr271(7.36) conformational switching.


## Cross-References

- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar) — A2A-StaR2-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril) is an engineered construct of the human A2AR
- [A2A-PSB1-bRIL Adenosine A2A Receptor](/xray-mp-wiki/proteins/a2a-psb1-bril) — Another thermostabilized A2AR-[BRIL](/xray-mp-wiki/reagents/protein-tags/bril) construct for comparison
- [LJ-4517 (Compound 2)](/xray-mp-wiki/reagents/ligands/lj-4517) — Co-crystallized nucleoside antagonist ligand in PDB 8CU7
- [LUF5833 (Compound 8)](/xray-mp-wiki/reagents/ligands/luf5833) — Co-crystallized partial agonist ligand in PDB 7ARO
- [Theophylline](/xray-mp-wiki/reagents/ligands/theophylline) — Used for initial crystal formation and receptor stabilization
- [NECA](/xray-mp-wiki/reagents/ligands/neca) — Full agonist reference structure (PDB 2YDV) for comparison
- [ZM241385](/xray-mp-wiki/reagents/ligands/zm241385) — Antagonist reference structure (PDB 5IU4/6WQA) for comparison
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm) — Detergent used for solubilization and purification
- [Sodium Thiocyanate (NaSCN)](/xray-mp-wiki/reagents/additives/sodium-thiocyanate) — Crystallization additive in the reservoir solution
- [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) — Crystallization method used for structure determination
