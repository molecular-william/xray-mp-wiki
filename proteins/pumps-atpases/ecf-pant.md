---
title: ECF-PanT (Energy-Coupling Factor Pantothenate Transporter)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.64389, doi/10.1073##pnas.1412246112]
verified: false
---

# ECF-PanT (Energy-Coupling Factor Pantothenate Transporter)

## Overview

ECF-PanT is a group II energy-coupling factor (ECF) transporter that mediates the import of pantothenate (vitamin B5) across the bacterial membrane. The transporter consists of four subunits: the S-component PanT (substrate-binding integral membrane protein), the T-component EcfT (transmembrane coupling subunit), and two ATPase subunits EcfA and EcfA' (nucleotide-binding domains). Two structures have been determined from different Lactobacillus species: a 2.8 A crystal structure from L. delbrueckii subsp. bulgaricus (PDB 6ZG3), determined using a  crystallization chaperone, revealing an open, post-hydrolysis conformation with a largely occluded substrate-binding cavity; and a 3.25 A crystal structure of the LbECF-PanT complex from L. brevis, which together with the LbECF-FolT and LbECF-HmpT structures revealed the molecular basis for how different S-components share a common [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/ecf-transporter-family/) module in group II [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/ecf-transporter-family/) transporters.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.64389 | 6ZG3 | 2.8 A | P1 | Full ECF-PanT complex (PanT, EcfT, EcfA, EcfA') from L. delbrueckii subsp. bulgaricus, co-purified with  Nb81 (CA14381) |  (from crystallization condition, occupying substrate-binding pocket) |
| doi/10.1073##pnas.1412246112 |  | 3.25 A |  | Full LbECF-PanT complex (PanT, EcfT, EcfA, EcfA') from L. brevis |  |

## Expression and Purification

- **Expression system**: Escherichia coli (for ECF complex)
- **Construct**: ECF-PanT complex expressed from p2BAD plasmid in E. coli. PanT, EcfT, EcfA, EcfA' cloned under arabinose promoter.
- **Notes**: Expression in E. coli with 0.1 mg/mL L-arabinose induction at 25 C for 3 h. Solitary PanT expressed in Lactococcus lactis NZ9000 using pNZ8048 plasmid with nisin promoter. For functional studies, panT-ecfTAA' genes were cotransformed into E. coli DV1 (panF panD) strain.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Cell disruption and ultracentrifugation | -- | 50 mM potassium phosphate pH 7.5, 1 mM MgSO4, DNase + -- | Cells disrupted in Constant Cell Disruption System (E. coli: 25 kPSi, 1 passage; L. lactis: 39 kPSi, 2 passages). Membranes collected at 193,727 xg for 120 min, homogenized in 50 mM potassium phosphate pH 7.5. |
| Membrane solubilization | Detergent solubilization | -- | 50 mM potassium phosphate pH 7.5, 300 mM NaCl, 10% (v/v)  + 1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm/) () | Membranes incubated with 1%  for 1 h at 4 C. Non-solubilized material removed by centrifugation at 286,286 xg for 35 min. |
|  [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (IMAC) | Nickel-Sepharose | 50 mM potassium phosphate pH 7.5, 300 mM NaCl, 50 mM  (wash); 500 mM  (elution) + 0.05% (w/v)  | Solubilized protein mixed with Ni-Sepharose resin for 1 h. Washed with 20 CV of wash buffer. Protein eluted in three-step gradient. Second fraction (highest protein content) supplemented with 1 mM Na-. |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) (with ) | Gel filtration | Superdex 200 10/300 (GE Healthcare) | 50 mM  Hcl]] pH 7.5, 150 mM NaCl + 0.05% (w/v)  | Purified  Nb81 mixed with ECF-PanT complex and applied to gel filtration column. Fractions containing -bound ECF-PanT pooled and concentrated. |

**Final sample**: ECF-PanT-Nb81 complex in 50 mM  Hcl]] pH 7.5, 150 mM NaCl, 0.05% 
**Yield**: Sufficient for crystallization trials
**Purity**: >95% by SDS-PAGE


## Crystallization

### doi/10.7554##eLife.64389

| Parameter | Value |
|---|---|
| Method | [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/sitting-drop-vapor-diffusion/) |
| Protein sample | ECF-PanT-Nb81 complex at 6.3 mg/mL in 50 mM  Hcl]] pH 7.5, 150 mM NaCl, 0.05% (w/v)  |
| Reservoir | 70 mM sodium  pH 4.5, 21-27% (v/v)  300 |
| Temperature | 4 C |
| Growth time | Several days |
| Cryoprotection | 70 mM sodium  pH 4.5, 40% (v/v)  300 |
| Notes | Crystals appeared in sitting drops.  Nb81 (CA14381) used as crystallization chaperone enabled crystal formation. Data collected at Diamond Light Source beamline I24 at 100 K. Crystal belonged to space group P1 (a=97.29 A, b=110.47 A, c=110.50 A, alpha=89.00 deg, beta=102.27 deg, gamma=102.24 deg). 2.8 A resolution. |


## Biological / Functional Insights

### Dynamic S-component exchange in Group II ECF transporters

Co-reconstitution experiments with ECF-PanT and ECF-FoIT2 in proteoliposomes demonstrated that the S-components PanT and FoIT2 dynamically associate with and dissociate from the shared [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/ecf-transporter-family/) module. Folate transport was observed when FoIT2 was co-reconstituted with ECF-PanT, and pantothenate transport was observed when PanT was co-reconstituted with ECF-FoIT2, indicating S-component exchange occurs as part of the transport mechanism.

### Substrate-loaded S-components compete more effectively for the ECF module

Competition experiments showed that the rate of pantothenate transport was inhibited by unlabelled folate, and vice versa, in a dose-dependent manner. This suggests that substrate-bound S-components compete more efficiently for association with the [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/ecf-transporter-family/) module than apo-proteins, recapitulating previous in vivo observations.

### Structural basis for differential substrate binding kinetics

The ECF-PanT structure reveals an occluded binding pocket (880 A^3) with loops L1 and L3 in a closed conformation. Comparison with ECF-FoIT2 suggests smaller conformational changes are needed for pantothenate binding to PanT than folate binding to FoIT2, explaining the faster apparent substrate association kinetics of PanT. In ECF-PanT, key binding residues (R101, N139, W69) all point towards the binding pocket center, while in ECF-FoIT2 the binding site is more accessible from the cytoplasmic side.

### Molecular basis for ECF module sharing in Group II ECF transporters

Structural comparison of LbECF-PanT, LbECF-FolT, and LbECF-HmpT from L. brevis revealed that different EcfS proteins use a common surface area composed of transmembrane helices SM1, SM2, and SM6 to interact with the coupling helices CH2 and CH3 of the same EcfT. CH2 interacts mainly with SM1 via hydrophobic interactions, modulating sliding movement of EcfS. CH3 binds to a hydrophobic surface groove formed by SM1, SM2, and SM6, transmitting conformational changes from EcfA/A' to EcfS. The AxxxA motif (Ala13 and Ala17) in SM1 is involved in EcfT interaction. The conformational flexibility of EcfT allows it to accommodate different EcfS proteins, enabling module sharing in group II [ECF (Energy Coupling Factor) Transporter Family](/xray-mp-wiki/concepts/ecf-transporter-family/) transporters.


## Cross-References

- [ECF Transporter (Energy-Coupling Factor Transporter)](/xray-mp-wiki/concepts/ecf-transporter/) — ECF-PanT is a group II ECF transporter that shares a common ECF module
- [RibU (ECF-Type Riboflavin Transporter S Component)](/xray-mp-wiki/proteins/pumps-atpases/ribu/) — Another characterized ECF transporter S-component for comparison
- [Elevator-Type Transport Mechanism](/xray-mp-wiki/concepts/elevator-mechanism/) — ECF transporters use an elevator-type toppling mechanism for substrate translocation
- [n-Dodecyl-beta-D-Maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane solubilization and purification
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Crystallization method used for ECF-PanT-Nb81 structure determination
- [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) — Referenced in ecf-pant text
- [Citrate](/xray-mp-wiki/reagents/buffers/citrate/) — Referenced in ecf-pant text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in ecf-pant text
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in ecf-pant text
- [Nickel Nta](/xray-mp-wiki/reagents/additives/nickel-nta/) — Referenced in ecf-pant text
