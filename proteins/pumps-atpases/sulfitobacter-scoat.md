---
title: "sCoaT (Co2+/Zn2+-transporting PIB-4-ATPase from Sulfitobacter sp. NAS14-1)"
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.73124]
verified: false
---

# sCoaT (Co2+/Zn2+-transporting PIB-4-ATPase from Sulfitobacter sp. NAS14-1)

## Overview

sCoaT is a PIB-4-type ATPase from Sulfitobacter sp. NAS14-1 (UniProt ID A3T2G5) that functions as a heavy metal transporter for zinc, cadmium, and cobalt. It belongs to the P1B-4 subclass of [P-type ATPases](/xray-mp-wiki/concepts/protein-families/p-type-atpase/), which have the broadest cargo scope among heavy-metal transporting P-type ATPases. The protein was expressed in [Escherichia coli](/xray-mp-wiki/methods/expression-systems/ecoli-expression-system/) C41 cells, purified using Ni2+-NTA affinity chromatography and gel filtration, and crystallized using the [HiLiDe method](/xray-mp-wiki/methods/crystallization/hilide-crystallization/). The structures were determined at 3.1 and 3.3 A resolution by molecular replacement using SsZntA as a search model. The protein has eight transmembrane helices (MA, MB, M1-M6) and lacks classical heavy-metal-binding domains (HMBDs). Key findings include a histidine (H657) that serves as an internal counterion and a dual role in ion release, and the identification of novel inhibitors with antimycobacterial activity. The crystal packing features type I crystals with unrestrained transmembrane domains and minimal contacts between membrane-spanning regions. 

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.73124 | 7QBZ | 3.3 | P 21 21 2 | Full-length sCoaT from Sulfitobacter sp. NAS14-1 (UniProt A3T2G5), expressed in E. coli C41, purified by Ni2+-NTA affinity chromatography and gel filtration, crystallized with AlF4- analogue | AlF4- |
| doi/10.7554##eLife.73124 | 7QC0 | 3.1 | P 21 21 2 | Full-length sCoaT from Sulfitobacter sp. NAS14-1 (UniProt A3T2G5), expressed in E. coli C41, purified by Ni2+-NTA and gel filtration, crystallized with BeF3- analogue | BeF3- |

## Expression and Purification

- **Expression system**: Escherichia coli C41(DE3) cells
- **Construct**: sCoaT from Sulfitobacter sp. NAS14-1 (NAS141_02821) expressed with 1 mM IPTG at 18 C for 16 h
- **Notes**: Cells cultured in LB medium at 37 C until OD600 = 0.6-1, cooled to 18 C, induced with 1 mM IPTG. Resuspended in 20 mM Tris-HCl pH 7.6, 200 mM KCl, 20% glycerol, 5 mM BME. Lysed by high-pressure homogenizer at 25,000 psi with 5 mM MgCl2, 1 mM PMSF, 2 ug/ml DNase I, Roche protease inhibitor cocktail.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Differential centrifugation | -- | 20 mM Tris-HCl pH 7.6, 200 mM KCl, 1 mM MgCl2, 5 mM BME, 20% (vol/vol) glycerol + -- | Membranes isolated by ultracentrifugation at 185,500 x g for 3 h at 4 C |
| Solubilization | Detergent solubilization | -- | 20 mM Tris-HCl pH 7.6, 200 mM KCl, 1 mM MgCl2, 5 mM BME, 20% (vol/vol) glycerol + 1% (w/v) DDM | 3 mg/ml total protein, gentle stirring for 2 h at 4 C. Unsolubilized material removed by ultracentrifugation at 185,500 x g for 1 h. Supplemented with 30 mM imidazole and 500 mM KCl (final). |
| Ni2+-NTA affinity chromatography | Immobilized metal affinity chromatography (IMAC) | Ni2+-NTA (HiTrap Chelating HP, 5 ml) | 20 mM Tris-HCl pH 7.6, 200 mM KCl, 1 mM MgCl2, 5 mM BME, 20% (vol/vol) glycerol, 0.15 mg/ml C12E8 + 0.15 mg/ml C12E8 | Protein from 6 l cells per column. Eluted with 400 mM imidazole gradient. |
| Gel filtration | Size-exclusion chromatography | Superose 6 10/300 GL | 20 mM MOPS-KOH pH 6.8, 80 mM KCl, 20% (vol/vol) glycerol, 1 mM MgCl2, 5 mM BME, 0.15 mg/ml C12E8 + 0.15 mg/ml C12E8 | Peak fractions collected and pooled for crystallization |


## Crystallization

### doi/10.7554##eLife.73124

| Parameter | Value |
|---|---|
| Method | HiLiDe (high lipid-detergent) crystallization |
| Protein sample | 5-8 mg/ml sCoaT in buffer D (20 mM MOPS-KOH pH 6.8, 80 mM KCl, 20% glycerol, 1 mM MgCl2, 5 mM BME, 0.15 mg/ml C12E8) supplemented with 2 mM phosphate analogue (AlF4- or BeF3-) |
| Reservoir | 100 mM MOPS pH 6.8, 0.5 M lithium acetate, 15% PEG 2K MME, 10% glycerol, 3% tert-butanol, 5% D-sorbitol, 5 mM BME |
| Temperature | 19 |
| Growth time | 2-14 days |
| Cryoprotection | 20% (vol/vol) glycerol (included in reservoir) |
| Notes | Crystals obtained using HiLiDe method. Type I crystal packing with unrestrained TM domains - minimal contacts between adjacent membrane-spanning regions. Crystal forming interactions likely take place through lipid-detergent molecules. Two crystal forms obtained: E2-BeF3- and E2-AlF4-, both in P 21 21 2 space group. |


## Biological / Functional Insights

### Architecture of PIB-4-ATPases - no classical HMBDs

The sCoaT structures reveal that PIB-4-ATPases possess eight transmembrane
helices (MA, MB followed by M1-M6) and lack classical heavy-metal-binding
domains (HMBDs). Only the first 47 residues remain unmodelled, shorter than
a classical MBD (70 aa). The N-terminal tail is rich in metal-binding residues
(Met, Cys, His, Asp, Glu) but deletion of the first 33 residues shows only
minor effects on catalytic activity in vitro, suggesting this level of
regulation is absent in many PIB-4-ATPases.

### Internal counterion mechanism via conserved histidine H657

A conserved histidine (H657) of the HEGxT motif in M6 serves as a built-in
counterion in PIB-4-ATPases, analogous to K693 in PIB-2-ATPases (SsZntA).
After ion release, H657 shifts to a sandwiched position between S325 and
C327 (SPC motif of M4), preventing back-transfer of the released ion and
allowing completion of the reaction cycle. This represents a unique internal
counterion principle for the PIB-4 subclass.

### Ion release pathway and mechanism

Ion release from the high-affinity binding site is likely initiated by E658
(M6) rotating away from the ion-binding configuration during E1P to E2P
transition, lowering cargo affinity. Subsequently, E120 (M2) serves as a
transient metal ligand along the exit pathway (lined by M2, M4, M5, M6),
stimulating release from the SPC motif. The two determined structures (E2P*
and E2.Pi) are surprisingly similar, suggesting that sCoaT preorganizes
for dephosphorylation already in a late E2P state, similar to LMCA1.

### Potassium-independent turnover in PIB-ATPases

While classical P-type ATPases require K+ for E2P dephosphorylation,
PIB-ATPases are K+-independent. The A-/P-domain linker in sCoaT is
maintained by a direct interaction between R273 (A-domain) and D601
(P-domain), rather than through a K+ ion. Mutation of these residues
(R273A, D601A, D601K) resulted in marked reduction of turnover,
indicating that PIB-ATPases rely on this particularly tight,
ion-independent stabilization more than classical P-type ATPases.

### Novel inhibitors with antimycobacterial activity

A screen of 20,000 compounds identified two novel inhibitors of sCoaT
that block both PIB-2 and PIB-4 ATPase activity, likely by targeting
the shared release pathway. The inhibitors show activity against
Mycobacterium bovis BCG (MIC90 of 18.75 uM for inhibitor 1), with
limited cytotoxicity toward primary human macrophages. Since PIB-ATPases
function as virulence factors in pathogens and are absent in humans,
they represent potential targets for novel antibiotics.

### Type I crystal packing with unrestrained TM domains

The sCoaT crystals exhibit type I crystal packing with minimal contacts
between adjacent membrane-spanning regions. Crystal forming interactions
likely occur through lipid-detergent molecules rather than direct
protein-protein contacts in the transmembrane region. To the authors'
knowledge, this is the first time type I crystals with unrestrained
transmembrane domains have been reported for a P-type ATPase.


## Cross-References

- [P-type ATPase Family](/xray-mp-wiki/concepts/protein-families/p-type-atpase/) — sCoaT belongs to the P1B-type (heavy metal transporting) ATPase subfamily
- [P-type ATPase Mechanism](/xray-mp-wiki/concepts/enzyme-mechanisms/p-type-atpase-mechanism/) — sCoaT follows the Post-Albers reaction cycle of P-type ATPases
- [Ion Release Pathway](/xray-mp-wiki/concepts/transport-mechanisms/ion-release-pathway/) — Paper describes ion release pathway for PIB-4-ATPases via M2, M4, M5, M6
- [HiLiDe Crystallization](/xray-mp-wiki/methods/crystallization/hilide-crystallization/) — Method used for structure determination
- [SsZntA (Shigella sonnei Zn2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/ss-znta/) — SsZntA was used as molecular replacement search model; related PIB-ATPase
- [DDM (n-Dodecyl-beta-D-Maltopyranoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization of membrane protein
- [C12E8 (Octaethylene Glycol Monododecyl Ether)](/xray-mp-wiki/reagents/detergents/c12e8/) — Detergent used in purification and crystallization
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used for structure determination
