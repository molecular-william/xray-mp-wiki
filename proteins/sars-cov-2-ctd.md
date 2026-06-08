---
title: SARS-CoV-2 Spike Protein C-Terminal Domain
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2020.03.045]
verified: false
---

# SARS-CoV-2 Spike Protein C-Terminal Domain

## Overview

The C-terminal domain (CTD) of the SARS-CoV-2 spike (S) protein, also known as the receptor-binding domain (RBD), is the region responsible for recognizing and binding to the host cell receptor human ACE2 (hACE2). The SARS-CoV-2 CTD spans residues 319-541 of the S1 subunit and forms a core subdomain with beta strands and an external subdomain. It displays stronger affinity for hACE2 compared to the SARS-CoV RBD due to key residue substitutions, and is antigenically distinct from SARS-CoV RBD.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2020.03.045 | 6LZG | 2.50 A | P41212 | SARS-CoV-2 spike protein CTD residues 319-541, in complex with hACE2 | hACE2 (human ACE2 residues 19-615) |

## Expression and Purification

- **Expression system**: HEK293T cells (mammalian)
- **Construct**: SARS-CoV-2 CTD residues 319-541 fused to mouse Fc (mFc) tag, expressed from pCAGGS plasmid

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and protein expression | Mammalian transient transfection | -- | -- | HEK293T cells transfected with pCAGGS plasmid; supernatant collected 24 h post-transfection |
| Affinity chromatography | Protein A affinity chromatography | HiTrap rProtein A FF column | Binding buffer 20 mM Na3PO4 pH 7.0; elution with 0.1 M glycine-HCl pH 3.0 neutralized with 1 M Tris-HCl pH 9.0 | mFc fusion protein captured on Protein A column |
| Gel filtration | Size-exclusion chromatography | Gel filtration column | PBS | Further purification and buffer exchange |


## Crystallization

### doi/10.1016##j.cell.2020.03.045

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | SARS-CoV-2 CTD/hACE2 complex, protein concentration 15 mg/ml |
| Reservoir | 0.1 M MES pH 6.5, 10% w/v PEG 5000 MME, 12% v/v 1-propanol |
| Temperature | 18 C |
| Growth time | not specified |
| Cryoprotection | Reservoir solution supplemented with 20% v/v glycerol before flash-cooling in liquid nitrogen |
| Notes | Crystals diffracted to 2.5 A; data collected at SSRF BL17U (wavelength 0.97919 A) |


## Biological / Functional Insights

### SARS-CoV-2 CTD binds hACE2 with higher affinity than SARS-RBD

The SARS-CoV-2 CTD displays stronger affinity for hACE2 compared to the SARS-CoV RBD. Atomic details at the binding interface show that key residue substitutions in SARS-CoV-2 CTD slightly strengthen the interaction. Surface plasmon resonance (SPR) analysis confirmed specific interactions between SARS-CoV-2 S1 and SARS-CoV-2 CTD with hACE2, while no binding was observed with hCD26 (DPP4) or hAPN (aminopeptidase N). The hACE2 binding site on SARS-CoV-2 CTD involves residues Y453, L455, F456, K417, A475, G476, Y473, N487, Y489, E484, F490, Q493, G446, Y449, Q498, T500, N501, and Y505 forming contacts with hACE2 residues including F28, Y41, H34, D38, Y41, Q42, and L45.

### Antigenic differences between SARS-CoV-2 and SARS-CoV RBD

Despite structural similarity in the overall protein fold, the SARS-CoV-2 CTD and SARS-RBD are antigenically distinct. A panel of six murine monoclonal antibodies (B30A38, A50A1A1, C31A12 targeting SARS-CoV S1; mAbs 1-3 targeting SARS-RBD) that effectively bound SARS-CoV S showed no interaction with SARS-CoV-2 S. Polyclonal antisera against SARS-RBD also failed to bind SARS-CoV-2 S. Electrostatic surface potential maps revealed divergent electrostatic distributions between the two viral ligands, likely explaining their differing immunogenicity. This suggests that SARS-RBD-based vaccine candidates may not confer effective SARS-CoV-2 prophylaxis.

### Structural comparison of SARS-CoV-2 CTD and SARS-RBD

Superimposition of the SARS-CoV-2 CTD/hACE2 and SARS-RBD/hACE2 structures reveals overall similar receptor binding modes. However, the loop exhibiting variant conformations and specific residue contacts differ between the two viruses. The SARS-CoV-2 CTD contains a core subdomain with beta strands labeled with extra c and an external subdomain with elements labeled with prime symbols. A disulfide bond and an N-glycan linked to N343 are present in the SARS-CoV-2 CTD structure.


## Cross-References

- [Human Angiotensin-Converting Enzyme 2 (hACE2)](/xray-mp-wiki/proteins/hace2/) — Co-crystallized receptor in PDB 6LZG
- [2-(N-Morpholino)ethanesulfonic Acid (MES)](/xray-mp-wiki/reagents/buffers/mes/) — Crystallization buffer at pH 6.5
- [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) — PEG 5000 MME used as crystallization precipitant
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Cryoprotectant (20% v/v) for flash-cooling crystals
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Protein A affinity purification of mFc-fusion protein
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Final purification step for SARS-CoV-2 CTD-mFc
