---
title: CusA Inner Membrane Efflux Pump
created: 2026-05-27
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2009.08.029, doi/10.1038##nature09743, doi/10.1038##nature09395]
verified: false
---

# CusA Inner Membrane Efflux Pump

## Overview

CusA is the inner-membrane component of the CusABC tripartite copper/silver efflux system in Escherichia coli. It is the sole heavy-metal efflux RND (Resistance-Nodulation-Cell Division) transporter in E. coli, specifically recognizing and conferring resistance to Ag(I) and [Cu(i)](/xray-mp-wiki/reagents/ligands/cu(i)) ions. CusA is driven by proton import and exports these toxic metal ions directly out of the cell. The protein was overproduced with an N-terminal 6xHis tag and purified by Ni2+-affinity and size exclusion chromatography. Although no crystal structure of CusA was solved in this study, a structural model was generated based on the AcrB crystal structure and sequence alignment, revealing that the periplasmic domain (residues 148-157) is positioned above the vestibule region facing the periplasm, where it interacts with the CusB membrane fusion protein.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2009.08.029 | -- | not solved | -- | Full-length CusA with N-terminal 6xHis tag; structural model based on [Acrb](/xray-mp-wiki/proteins/acrB) (PDB 1WXU) | -- |
| doi/10.1038##nature09743 | -- | 2.90 A | -- | CusA residues 4-1043 in CusBA co-crystal structure; CusA present as trimer | [Cymal 6](/xray-mp-wiki/reagents/detergents/cymal-6) |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3) delta acrB
- **Construct**: Full-length CusA with N-terminal 6xHis tag, overproduced from pET15b cusA expression vector. Host strain BL21(DE3) delta acrB has deletion in chromosomal acrB gene.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and induction | Cells grown in 12 L LB medium with 100 ug/ml [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin) at 37 C, induced with 1 mM IPTG at OD600 ~0.5, harvested within 3 h | -- | LB medium with 100 ug/ml ampicillin + -- | BL21(DE3) delta acrB host strain used |
| Cell lysis and membrane isolation | Cells disrupted with French pressure cell; membrane fraction collected and washed twice with high-salt buffer (20 mM sodium phosphate pH 7.2, 2 M KCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 1 mM EDTA, 1 mM PMSF) and once with 20 mM Hepes-NaOH (pH 7.5) containing 1 mM PMSF | -- | 100 mM sodium phosphate (pH 7.2), 10% glycerol, 1 mM EDTA, 1 mM [PMSF](/xray-mp-wiki/reagents/additives/pmsf) (low-salt); 20 mM sodium phosphate (pH 7.2), 2 M KCl, 10% glycerol, 1 mM EDTA, 1 mM PMSF (high-salt wash) + -- | Membrane fraction collected by ultracentrifugation |
| Solubilization | Membrane protein solubilized in 1% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm); insoluble material removed by ultracentrifugation at 370,000g | -- | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes)-NaOH (pH 7.5) + 1% DDM | Ultracentrifugation at 370,000g to remove insoluble material |
| Ni2+ affinity chromatography | Ni2+-affinity column chromatography | Ni2+-affinity resin | 20 mM Hepes-NaOH (pH 7.5) + 1% DDM | His-tagged CusA captured on Ni2+ column |
| Size exclusion chromatography | G-200 sizing column chromatography | Superdex 200 | 20 mM Na-Hepes (pH 7.5) + 0.05% DDM | Purity >95% by 10% SDS-PAGE stained with Coomassie Brilliant Blue; concentrated to 20 mg/ml |


## Crystallization

### doi/10.1016##j.jmb.2009.08.029

| Parameter | Value |
|---|---|
| Method | not performed |
| Protein sample | -- |
| Reservoir | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | CusA crystal structure was not solved in this study. A structural model was generated based on the AcrB crystal structure and protein sequence alignment. CusA and AcrB share only 19% sequence identity. |

### doi/10.1038##nature09743

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 0.1 mM CusA and 0.1 mM [Cusb](/xray-mp-wiki/proteins/cusB) in 20 mM Na-HEPES pH 7.5, 0.05% CYMAL-6 |
| Reservoir | 10% PEG 6000, 0.1 M Na-HEPES pH 7.5, 0.1 M ammonium [Acetate](/xray-mp-wiki/reagents/buffers/acetate), 20% glycerol |
| Temperature | Room temperature |
| Growth time | 2 months |
| Cryoprotection | Stepwise glycerol increase to 30% in 5% increments |
| Notes | CusA (native) - CusB (SeMet-substituted) co-crystal. Grew within 2 months in sitting-drop vapor diffusion. |


## Biological / Functional Insights

### Heavy-metal specificity of CusA

CusA is the only heavy-metal efflux RND (HME-RND) transporter in E. coli, distinguishing it from the six multidrug efflux RND (HAE-RND) pumps (AcrB, AcrD, AcrF, MdtB, MdtC, and YhiV) also present in E. coli. CusA specifically recognizes and confers resistance to [Ag(i)](/xray-mp-wiki/reagents/ligands/ag(i)) and Cu(I) ions, which are highly toxic even at low concentrations. The protein works in conjunction with the periplasmic MFP CusB and the outer-membrane channel CusC to form the CusABC tripartite efflux complex.

### Structural model based on AcrB homology

Although the CusA crystal structure was not determined, a structural model was generated based on the AcrB crystal structure and sequence alignment. CusA and AcrB share only 19% protein sequence identity. The model indicates that the periplasmic domain of CusA (residues 148-157) is located directly above the vestibule region, facing the periplasm. This location corresponds to the PN2 region of AcrB. The C-terminus of CusB interacts with CusA at a position corresponding to the PC1 region of AcrB, analogous to the interaction between [ACRA](/xray-mp-wiki/proteins/acra) and AcrB.

### CusA-CusB cross-linking interaction

Chemical cross-linking with disuccinimidyl suberate (DSS) followed by LC-MS/MS analysis revealed that the N-terminal polypeptide of CusB (residues 84-101: IDPTQTQNLGVKTATVTR) directly interacts with the periplasmic domain of CusA (residues 148-157: SGKHDLADLR). This interaction was confirmed by identifying cross-linked lysine residues between the two proteins. The interaction site is consistent with the PC1 region of AcrB, where the C-terminus of AcrA binds.

### CusBA co-crystal structure and interaction interface

The co-crystal structure of the CusBA complex (2.90 A resolution) revealed that CusA exists as a trimer, with each protomer binding two CusB molecules, for a total of six CusB protomers per CusA trimer. Key interactions between CusA and CusB include: (1) four salt bridges formed by CusB residues K95, D386, E388 and R397 with CusA residues D155, R771, R777 and E584; (2) hydrogen bonds between CusB T89, the backbone oxygen of N91, and R292 with CusA K594, R147, and the backbone oxygen of Q198; (3) additional hydrogen bonds in molecule 2 of CusB where Q108, S109, S253 and N312 form hydrogen bonds with CusA Q785, Q194, D800 and Q198. The equilibrium dissociation constant (Kd) for CusA-CusB interaction was measured by isothermal titration calorimetry as 5.1 +/- 0.3 uM.

### Metal ion transport pathway through CusA

CusA is proposed to take up metal ions from both the periplasm and cytoplasm using a methionine-residue ion relay network. Metal ions enter the three-methionine binding site of CusA, formed by M573, M623 and M672, located inside the cleft between subdomains PN2 and PC1 on the periplasmic portion of CusA. Ions may also enter through methionine pairs within the transmembrane domain. The proposed pathway involves: (1) direct transfer from CusF chaperone to the three-methionine binding site (M49, M64, M66) at the N-terminal tail of CusB; (2) delivery from CusB to the three-methionine cluster (M573, M623, M672) inside the periplasmic cleft of CusA; (3) release to the nearest methionine pair (M271-M755) located above the three-methionine binding site; (4) extrusion through the [Cusc](/xray-mp-wiki/proteins/cusC) outer membrane channel.


## Cross-References

- [AcrB Multidrug Efflux Pump](/xray-mp-wiki/proteins/abc-transporters/acrB/) — AcrB crystal structure used as template for CusA structural model; 19% sequence identity
- [CusB Membrane Fusion Protein](/xray-mp-wiki/proteins/abc-transporters/cusb/) — CusB is the periplasmic MFP partner; cross-linking MS confirmed CusA-CusB interaction
- [MexB Efflux Pump](/xray-mp-wiki/proteins/abc-transporters/mexB/) — MexB is a P. aeruginosa RND efflux pump homologous to CusA
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM (1% solubilization, 0.05% crystallization buffer) used for CusA purification
- [PMSF (Phenylmethylsulfonyl Fluoride)](/xray-mp-wiki/reagents/additives/pmsf/) — PMSF (1 mM) included in lysis and wash buffers as protease inhibitor
- [Sodium Phosphate Buffer](/xray-mp-wiki/reagents/buffers/sodium-phosphate/) — Sodium phosphate buffer (100 mM pH 7.2) used in lysis buffer; 20 mM in high-salt wash
- [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate) — Entity mentioned in text
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes) — Entity mentioned in text
- [CU(I)](/xray-mp-wiki/reagents/ligands/cu(i)) — Entity mentioned in text
- [CUSC](/xray-mp-wiki/proteins/cusC) — Entity mentioned in text
