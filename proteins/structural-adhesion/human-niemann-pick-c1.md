---
title: Human Niemann-Pick C1 (NPC1)
created: 2026-06-08
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1711716114, doi/10.1107##s2053230x23000705]
verified: false
---

# Human Niemann-Pick C1 (NPC1)

## Overview

Human NPC1 (Niemann-Pick C1) is a large multi-domain membrane protein essential for the export of LDL-derived [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) from late endosomes. It consists of 1,278 amino acid residues, including three luminal domains [N-terminal domain (NTD), middle luminal domain (MLD), and C-terminal domain (CTD/cysteine-rich domain)] and 13 transmembrane helices. NPC1, together with the soluble NPC2 protein, mediates [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) transport across the ~8 nm glycocalyx of the endosomal lumen. Mutations in NPC1 cause Niemann-Pick type C disease, a fatal lysosomal storage disorder. NPC1 also functions as a receptor for Ebola virus in late endosomes.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1711716114 | 5U73 | 3.3 A | not specified | NPC1* (residues 314-1,278), including TM2-13, MLD, and CTD | none detected (itraconazole used during purification but not observed in density) |
| doi/10.1107##s2053230x23000705 | 8EUS | 2.3 A | P2_1 | Human NPC1-C (residues 371-621) with C-terminal His8 tag, nonglycosylated, expressed in E. coli | none |

## Expression and Purification

- **Expression system**: HEK293 cells (mammalian expression, as previously published)
- **Construct**: NPC1* (residues 314-1,278)

### Purification Workflow

- **Expression system**: HEK293 cells
- **Expression construct**: NPC1* (residues 314-1,278)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Sonication | -- | 20 mM Hepes pH 7.0, 150 mM NaCl, 1 mM PMSF, 5 ug/mL leupeptin and aprotinin + -- | Cells resuspended in buffer A |
| Solubilization | Detergent extraction | -- | 20 mM Hepes pH 7.0, 150 mM NaCl, 100 uM itraconazole + 1% (w/v) n-Dodecyl-beta-D-maltopyranoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Incubated 2 h at 4 C |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA | Ni-NTA affinity column (Qiagen) | 20 mM Hepes pH 7.0, 150 mM NaCl, 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Washed twice with 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Gel filtration | Size-exclusion chromatography | Superose 6 or similar | 20 mM Hepes pH 7.0, 150 mM NaCl + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | All buffers supplemented with 10 uM itraconazole |


## Crystallization

### doi/10.1073##pnas.1711716114

| Parameter | Value |
|---|---|
| Method | vapor diffusion (sitting drop) |
| Protein sample | NPC1* at 10 mg/mL, incubated with 100 uM itraconazole on ice for 1 h |
| Notes | Crystals grew in 3 d. Data collected at NECAT beamlines (APS), processed with XDS. Structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using previous NPC1* structure (5I31) as search model. Refined with PHENIX to Rfree 30.5% and Rwork 25.3%. |


## Biological / Functional Insights

### Complete CTD structure revealed

At 3.3 A resolution, the entire C-terminal luminal domain (CTD,
residues 861-1,083) is fully resolved with unambiguous sequence
assignment. The CTD consists of three beta strands surrounded by
five alpha-helices. All eight cysteines form four disulfide bonds,
stabilizing the loop structures on the tip of this domain. This
contrasts with the MLD, which only contains two disulfide bonds
despite sharing a similar fold.

### Omega loop and CTD-NTD interaction

A disulfide bond between Cys909 and Cys914 creates a unique loop
(residues 909-917, termed the Omega loop) that breaks one long
alpha-helix into two shorter helices (alpha2a and alpha2b). The
Omega loop interacts with a Psi loop (residues 230-234) on the NTD,
forming a CTD-NTD interface. Mutagenesis showed that deleting the
Omega loop (NPC1-Delta-Omega-A) completely blocks [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/)
transport, while deleting the Psi loop (NPC1-Delta-Psi) results in
50% loss of activity, confirming the physiological importance of
this interaction.

### Mapping of disease-causing mutations

The improved resolution allows precise mapping of all NPC
disease-causing mutations across the NPC1 structure. The most
frequent mutation, I1061T (15-20% of disease alleles), is located
in the alpha5 helix of the CTD. Analysis suggests that I1061T
would not disrupt the alpha5-alpha2b interaction, explaining why
overexpression of NPC1-I1061T can still partially rescue the
NPC1-deficient phenotype. The P691S mutation (which abolishes
ligand binding to the SSD) is located in TM5, facing the SSD
ligand-binding pocket.

### Hydrophobic hand-off cholesterol transfer model

The structural data support a "hydrophobic hand-off" model for
[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) transfer. [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) binds NPC2 in the endosomal
lumen, inducing conformational changes that facilitate NPC2-MLD
interaction. The Omega loop-Psi loop interaction keeps the NTD in
the proper orientation to receive [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) from NPC2. After
[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) transfer from NPC2 to NPC1-NTD, the Omega loop-Psi
loop interaction may weaken to allow the NTD to reach across the
glycocalyx and deliver [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) to the SSD pocket in the
membrane. Two possible mechanisms are proposed: (1) intramolecular
transfer where TM1 movement docks NTD to SSD, or (2) intermolecular
transfer where NTD from one NPC1 docks to an SSD of a neighboring
molecule.


## Cross-References

- [Saccharomyces cerevisiae Niemann-Pick Type C-Related Protein 1 (NCR1)](/xray-mp-wiki/proteins/structural-adhesion/ncr1/) — Yeast homolog of human NPC1
- [n-Dodecyl-beta-D-maltoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Used for NPC1 solubilization and purification
- [HEPES (HEPES-KOH Buffer)](/xray-mp-wiki/reagents/buffers/hepes/) — Used in all purification and crystallization buffers
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Additive used in purification or crystallization buffers
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used in purification or crystallization
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Additive used in purification or crystallization buffers
