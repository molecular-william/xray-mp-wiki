---
title: Thermus thermophilus SecYEG Translocon Complex
created: 2026-05-27
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.celrep.2015.10.025, doi/10.1038##nature07421]
verified: false
---

# Thermus thermophilus SecYEG Translocon Complex

## Overview

The SecYEG translocon from Thermus thermophilus is a heterotrimeric protein-conducting channel that mediates protein translocation across the bacterial plasma membrane and integration of membrane proteins. The complex comprises [SECY](/xray-mp-wiki/proteins/secy) (core channel-forming subunit with 10 transmembrane helices), [SECE](/xray-mp-wiki/proteins/sece) (essential accessory subunit that stabilizes SecY), and [SECG](/xray-mp-wiki/proteins/secg) (accessory subunit with 2 transmembrane helices and a large cytoplasmic loop). The 2008 structure of SecYE (without SecG) at 3.2 A revealed a 'pre-open' state of the translocon in complex with an anti-SecY Fab fragment, showing how SecA binding induces conformational changes. The 2015 structures at 2.7 A (resting) and 3.6 A (peptide-bound) further elucidated the complete SecYEG architecture in a lipidic cubic phase environment using [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.celrep.2015.10.025 | 5AWW | 2.7 A | I222 | Full-length Thermus thermophilus SecYEG complex; SecY(R252G)-His6, SecE, SecG; expressed in E. coli BL21(DE3) | None |
| doi/10.1016##j.celrep.2015.10.025 | 5CH4 | 3.6 A | C222_1 | Full-length Thermus thermophilus SecYEG complex with peptide-bound state; SecY(R252G)-His6, SecE, SecG; expressed in E. coli BL21(DE3) | SecE N-terminal MFARL peptide |
| doi/10.1038##nature07421 | Not specified in paper | 3.2 A | Not specified in paper | Full-length Thermus thermophilus SecY(L2V/R252E) with C-terminal His6-tag (auto-cleaved), SecE; complexed with anti-SecY Fab fragment | None (apo-SecYE in pre-open state) |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecY(R252G)-His6, SecE, SecG co-expressed from two plasmids (pAK22/pAK24); SecY contains R252G mutation in periplasmic loop

### Purification Workflow

*Source: doi/10.1016##j.celrep.2015.10.025*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane fraction preparation | Differential centrifugation | -- | Not specified + -- | Total membrane fraction from E. coli BL21(DE3) cells co-expressing SecYEG |
| Solubilization | Detergent solubilization | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 300 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.1 mM [PMSF](/xray-mp-wiki/reagents/additives/pmsf) + 2% n-dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm)) | 1 hr at 4 C; ultracentrifugation at 138,000 x g for 30 min |
| Ni-NTA affinity chromatography | Affinity chromatography (His-tag) | Ni-NTA agarose | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 300 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Equilibration with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole); wash with 40 mM imidazole; elution with 300 mM imidazole |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 10/300 GL column | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 300 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Concentrated to ~15 mg/ml using Amicon Ultra 50-kDa cutoff filter |
| Ion-exchange chromatography | Ion-exchange chromatography | HiTrap SP HP column | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 0.25% n-decyl-beta-D-maltoside (DM), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + 0.25% DM | Elution with linear gradient of 0-100% elution buffer (1 M NaCl, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 0.25% DM, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol)); final sample dialyzed against 0.25% DM and 5% glycerol |

### Purification Workflow

*Source: doi/10.1038##nature07421*

- **Expression system**: Escherichia coli
- **Expression construct**: Full-length T. thermophilus SecY(L2V/R252E)-His6, SecE; co-expressed from two plasmids (pTT159/pSTD343)
- **Tag info**: C-terminal His6-tag on SecY; auto-cleaved during storage at 20 C for 2 weeks

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane fraction preparation | Differential centrifugation | -- | Not specified + -- | Total membrane fraction from E. coli cells overproducing SecYE |
| Solubilization | Detergent solubilization | -- | Not specified + n-dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm)) | SecYE complex solubilized from membrane fraction with DDM |
| Purification | Column chromatography (three steps) | Ni-NTA + gel filtration | Not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Three successive chromatography steps; His6-tag auto-cleaved after storage at 20 C for 2 weeks; re-chromatographed on Ni-NTA |
| Fab complex purification | Gel filtration chromatography | Gel filtration column | Not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | SecYE mixed with stoichiometric excess of Fab; complex isolated by gel filtration |


## Crystallization

### doi/10.1016##j.celrep.2015.10.025

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase crystallization |
| Protein sample | Purified SecYEG (~15 mg/ml) mixed with liquefied [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) at 2:3 protein-to-lipid ratio (w/w) |
| Temperature | 20 C |
| Growth time | About 10 days |
| Cryoprotection | Cryocooled to 100 K for X-ray data collection |
| Notes | I222 space group; resting state structure at 2.7 A resolution; crystals grown using glass sandwich plates |

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase crystallization |
| Protein sample | Purified SecYEG mixed with liquefied [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) at defined protein-to-lipid ratio |
| Temperature | 20 C |
| Growth time | Not specified |
| Cryoprotection | Cryocooled to 100 K for X-ray data collection |
| Notes | C222_1 space group; peptide-bound state structure at 3.6 A resolution |

### doi/10.1038##nature07421

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization |
| Protein sample | Purified Fab-SecYE complex |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Cryocooled to 100 K for X-ray data collection at SPring-8 and PF |
| Notes | Structure determined by MAD method using SeMet-labelled SecYE crystals. Refined to Rwork/Rfree of 24.4%/28.0% at 3.2 A resolution. Asymmetric unit contains one Fab-SecYE complex. Data collected at beamline BL41XU (SPring-8) and NW12 (PF). |


## Biological / Functional Insights

### Cytoplasmic SecG loop covers and seals the protein-conducting channel

The cytoplasmic loop of [SECG](/xray-mp-wiki/proteins/secg) covers the hourglass-shaped [SECY](/xray-mp-wiki/proteins/secy) channel exactly over the pore ring, contributing to channel sealing on the cytoplasmic side. The pore ring consists of six conserved residues (I77, I81, T184, I188, I275, I403 in Thermus thermophilus numbering) that likely maintain membrane permeability. Disulfide bond formation analysis and molecular dynamics simulations confirmed that the SecG loop covers the channel in the membrane environment. This arrangement prevents uncontrolled ion flux while allowing regulated protein translocation.

### Peptide-bound structure reveals lateral gate opening mechanism

The peptide-bound structure (PDB 5CH4) reveals a previously unknown state where the N-terminal MFARL segment of [SECE](/xray-mp-wiki/proteins/sece) inserts into the hydrophobic crack of another [SECY](/xray-mp-wiki/proteins/secy) monomer, expanding the cytoplasmic crack between TM2 and TM8. The hydrophobic side chains of F2 and A3 interact with I85, I89, and F322 on the cytoplasmic hydrophobic crack of SecY, while R4 interacts with conserved Q88. This mimics the early stage of signal peptide binding to the lateral gate, providing structural insight into how signal peptides induce lateral gate opening during protein translocation.

### Resting state structure at high resolution reveals complete SecYEG architecture

The 2.7 A structure of the resting state (PDB 5AWW) elucidates the detailed architecture of the intact SecYEG complex including all three subunits. [SECY](/xray-mp-wiki/proteins/secy) forms an hourglass-shaped channel with ten transmembrane helices; [SECE](/xray-mp-wiki/proteins/sece) is located at the back of SecY and stabilizes the complex; [SECG](/xray-mp-wiki/proteins/secg) comprises two transmembrane helices tightly bound to SecY through hydrophobic interactions. The plug helix seals the periplasmic side of the channel while the SecG loop covers the cytoplasmic side. The lateral gate formed by TM2, TM7, and TM8 of SecY is in a closed conformation. The crystal packing revealed a possible 2-fold symmetric dimer that differs from previously proposed dimer arrangements.

### Crystallographic asymmetric unit contains monomer with crystallographic dimer

Although both crystallographic asymmetric units contain one SecYEG complex, the packing arrangement shows a possible 2-fold symmetric dimer of SecYEG in the lipid bilayer. This dimer association pattern differs from previously proposed face-to-face or back-to-back SecYEG dimers. Due to the lack of direct transmembrane interaction between SecYEG units, the dimer architecture does not appear to be stable in the cytoplasmic membrane, supporting the notion that SecYEG functions as a monomer during co-/post-translational translocation.

### Pre-open state of SecYE revealed by Fab complex structure

The 3.2 A crystal structure of T. thermophilus SecYE in complex with an anti-SecY Fab fragment revealed a 'pre-open' state distinct from the closed state of M. jannaschii SecYEbeta. In this state, TM2, TM7, and TM8 are shifted to create a hydrophobic crack open to the cytoplasm, lined by evolutionarily conserved hydrophobic residues (Ile85, Pro273, Phe276, Ala279). The Fab fragment binds to the Pro-Gly-Ile-Arg-Pro-Gly motif in the C5 cytoplasmic domain of SecY. Molecular dynamics simulations (100 ns) showed that SecYE undergoes large conformational changes from the pre-open toward the closed state, indicating the closed form is the energetically favored ground state.

### SecA induces conformational transition of SecYE

Intermolecular disulfide cross-linking experiments identified the SecA-SecY interface: SecA(Pro202) contacts SecY(Ala259) in C4, and SecA(Leu775) contacts SecY(Pro352) in C5. The motif IV region of SecA (residues 180-188) becomes surface-exposed upon translocon binding, enabling activation of SecA ATPase. SecA binding to SecYE reduced the 92-329 intramolecular disulfide bond formation in membranembedded SecYE, suggesting SecA facilitates the transition from closed to pre-open state. The swinging of TM8 may initiate channel gate opening through exposure of the hydrophobic crack.


## Cross-References

- [Thermotoga maritima SecA ATPase](/xray-mp-wiki/proteins/secretion-translocon/thermotoga-maritima-seca/) — SecA is the cytoplasmic ATPase motor that binds SecYEG to drive protein translocation
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid component for LCP crystallization matrix
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent used for membrane protein extraction
- [n-Decyl-beta-D-maltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Mild detergent used for crystallization sample preparation and ion-exchange chromatography
- [MOPS (3-(N-morpholino)propanesulfonic acid)](/xray-mp-wiki/reagents/buffers/mops/) — Crystallization reservoir buffer component
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) — Affinity chromatography resin for His-tagged SecY purification
- [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Size-exclusion chromatography for complex purification and monodispersity assessment
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for both SecYEG structures
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) — Main buffer component in purification
- [PMSF](/xray-mp-wiki/reagents/additives/pmsf) — Entity mentioned in text
- [SECE](/xray-mp-wiki/proteins/sece) — Related protein
