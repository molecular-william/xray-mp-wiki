---
title: Thermus thermophilus SecYEG Translocon Complex
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.celrep.2015.10.025]
verified: false
---

# Thermus thermophilus SecYEG Translocon Complex

## Overview

The SecYEG translocon from Thermus thermophilus is a heterotrimeric protein-conducting channel that mediates protein translocation across the bacterial plasma membrane and integration of membrane proteins. The complex comprises SecY (core channel-forming subunit with 10 transmembrane helices), SecE (essential accessory subunit that stabilizes SecY), and SecG (accessory subunit with 2 transmembrane helices and a large cytoplasmic loop). This paper reports the first high-resolution structure of the intact SecYEG complex at 2.7 A and the first peptide-bound structure at 3.6 A, both determined in a lipidic cubic phase environment using monoolein. The structures reveal that the cytoplasmic loop of SecG covers the channel at the pore ring level, sealing the cytoplasmic side, and that signal peptide binding to the lateral gate induces crack expansion at the cytoplasmic side.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.celrep.2015.10.025 | 5AWW | 2.7 A | I222 | Full-length Thermus thermophilus SecYEG complex; SecY(R252G)-His6, SecE, SecG; expressed in E. coli BL21(DE3) | None |
| doi/10.1016##j.celrep.2015.10.025 | 5CH4 | 3.6 A | C222_1 | Full-length Thermus thermophilus SecYEG complex with peptide-bound state; SecY(R252G)-His6, SecE, SecG; expressed in E. coli BL21(DE3) | SecE N-terminal MFARL peptide |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecY(R252G)-His6, SecE, SecG co-expressed from two plasmids (pAK22/pAK24); SecY contains R252G mutation in periplasmic loop

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane fraction preparation | Differential centrifugation | -- | Not specified + -- | Total membrane fraction from E. coli BL21(DE3) cells co-expressing SecYEG |
| Solubilization | Detergent solubilization | -- | 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 5% glycerol, 0.1 mM PMSF + 2% n-dodecyl-beta-D-maltoside (DDM) | 1 hr at 4 C; ultracentrifugation at 138,000 x g for 30 min |
| Ni-NTA affinity chromatography | Affinity chromatography (His-tag) | Ni-NTA agarose | 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 0.1% DDM, 5% glycerol + 0.1% DDM | Equilibration with 20 mM imidazole; wash with 40 mM imidazole; elution with 300 mM imidazole |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 10/300 GL column | 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 0.1% DDM, 5% glycerol + 0.1% DDM | Concentrated to ~15 mg/ml using Amicon Ultra 50-kDa cutoff filter |
| Ion-exchange chromatography | Ion-exchange chromatography | HiTrap SP HP column | 20 mM Tris-HCl pH 8.0, 0.25% n-decyl-beta-D-maltoside (DM), 5% glycerol + 0.25% DM | Elution with linear gradient of 0-100% elution buffer (1 M NaCl, 20 mM Tris-HCl pH 8.0, 0.25% DM, 5% glycerol); final sample dialyzed against 0.25% DM and 5% glycerol |


## Crystallization

### doi/10.1016##j.celrep.2015.10.025

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase crystallization |
| Protein sample | Purified SecYEG (~15 mg/ml) mixed with liquefied monoolein at 2:3 protein-to-lipid ratio (w/w) |
| Temperature | 20 C |
| Growth time | About 10 days |
| Cryoprotection | Cryocooled to 100 K for X-ray data collection |
| Notes | I222 space group; resting state structure at 2.7 A resolution; crystals grown using glass sandwich plates |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase crystallization |
| Protein sample | Purified SecYEG mixed with liquefied monoolein at defined protein-to-lipid ratio |
| Temperature | 20 C |
| Growth time | Not specified |
| Cryoprotection | Cryocooled to 100 K for X-ray data collection |
| Notes | C222_1 space group; peptide-bound state structure at 3.6 A resolution |


## Biological / Functional Insights

### Cytoplasmic SecG loop covers and seals the protein-conducting channel

The cytoplasmic loop of SecG covers the hourglass-shaped SecY channel exactly over the pore ring, contributing to channel sealing on the cytoplasmic side. The pore ring consists of six conserved residues (I77, I81, T184, I188, I275, I403 in Thermus thermophilus numbering) that likely maintain membrane permeability. Disulfide bond formation analysis and molecular dynamics simulations confirmed that the SecG loop covers the channel in the membrane environment. This arrangement prevents uncontrolled ion flux while allowing regulated protein translocation.

### Peptide-bound structure reveals lateral gate opening mechanism

The peptide-bound structure (PDB 5CH4) reveals a previously unknown state where the N-terminal MFARL segment of SecE inserts into the hydrophobic crack of another SecY monomer, expanding the cytoplasmic crack between TM2 and TM8. The hydrophobic side chains of F2 and A3 interact with I85, I89, and F322 on the cytoplasmic hydrophobic crack of SecY, while R4 interacts with conserved Q88. This mimics the early stage of signal peptide binding to the lateral gate, providing structural insight into how signal peptides induce lateral gate opening during protein translocation.

### Resting state structure at high resolution reveals complete SecYEG architecture

The 2.7 A structure of the resting state (PDB 5AWW) elucidates the detailed architecture of the intact SecYEG complex including all three subunits. SecY forms an hourglass-shaped channel with ten transmembrane helices; SecE is located at the back of SecY and stabilizes the complex; SecG comprises two transmembrane helices tightly bound to SecY through hydrophobic interactions. The plug helix seals the periplasmic side of the channel while the SecG loop covers the cytoplasmic side. The lateral gate formed by TM2, TM7, and TM8 of SecY is in a closed conformation. The crystal packing revealed a possible 2-fold symmetric dimer that differs from previously proposed dimer arrangements.

### Crystallographic asymmetric unit contains monomer with crystallographic dimer

Although both crystallographic asymmetric units contain one SecYEG complex, the packing arrangement shows a possible 2-fold symmetric dimer of SecYEG in the lipid bilayer. This dimer association pattern differs from previously proposed face-to-face or back-to-back SecYEG dimers. Due to the lack of direct transmembrane interaction between SecYEG units, the dimer architecture does not appear to be stable in the cytoplasmic membrane, supporting the notion that SecYEG functions as a monomer during co-/post-translational translocation.


## Cross-References

- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid component for LCP crystallization matrix
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent used for membrane protein extraction
- [n-Decyl-beta-D-maltoside (DM)](/xray-mp-wiki/reagents/detergents/decylmaltoside/) — Mild detergent used for crystallization sample preparation and ion-exchange chromatography
- [MOPS (3-(N-morpholino)propanesulfonic acid)](/xray-mp-wiki/reagents/buffers/mops/) — Crystallization reservoir buffer component
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) — Affinity chromatography resin for His-tagged SecY purification
- [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Size-exclusion chromatography for complex purification and monodispersity assessment
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for both SecYEG structures
