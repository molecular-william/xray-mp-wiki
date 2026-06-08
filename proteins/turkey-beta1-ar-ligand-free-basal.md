---
title: Turkey Beta1-Adrenergic Receptor Ligand-Free Basal State
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2504]
verified: false
---

# Turkey Beta1-Adrenergic Receptor Ligand-Free Basal State

## Overview

Turkey beta1-adrenergic receptor (beta1-AR) in its ligand-free basal state, determined at 3.5 A resolution with highly anisotropic diffraction. The receptor was crystallized without any bound ligands in a membrane-like lipid environment, revealing the inactive conformational state of a GPCR prior to ligand binding. The structure displays an oligomeric arrangement with two distinct dimer interfaces: Interface 1 (TM1-TM2-H8-ECL1, ~1700 A2 buried surface) and Interface 2 (TM4-TM5-ICL2-ECL2, ~900 A2 buried surface). The inactive conformation is characterized by the presence of the ionic lock salt bridge between Arg139(3.50) and Glu285(6.30), and an empty, contracted ligand-binding pocket compared to antagonist-bound structures.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.2504 | 4DA1 | 3.5 A | unknown (highly anisotropic) | Turkey beta1-AR(H0) with deletions of residues 3-32, 249-283, 366-483; mutations C116L and C358A; C-terminal His6 tag | None (ligand-free) |

## Expression and Purification

- **Expression system**: High5 insect cells (baculovirus expression vector system)
- **Construct**: Turkey beta1-AR(H0) with deletions of residues 3-32, 249-283, 366-483; point mutations C116L and C358A; C-terminal His6 tag. Subcloned into baculoviral expression vector pVL1393.
- **Notes**: High5 cells grown in suspension in High5 Express Medium at 27 C, 110 r.p.m. Infected at MOI 5-10, harvested 48 h post-infection.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest and membrane preparation | Cells broken by sonication, membranes pelleted by ultracentrifugation at 45,000 r.p.m. for 1 h at 4 C. | -- | 20 mM Tris-HCl pH 8, 1 mM EDTA (initial); 20 mM Tris-HCl pH 8, 0.35 M NaCl, 0.2 mM EDTA (final) + -- | Membranes resuspended at 10-20 mg protein/ml and flash frozen in liquid nitrogen. |
| DDM solubilization | Detergent solubilization of membrane pellets | -- | 20 mM Tris-HCl pH 8, 0.35 M NaCl, 2% DDM + 2% DDM (n-dodecyl-beta-D-maltopyranoside) | Solubilized at 10 mg/ml protein in ice-cold buffer. |
| Alprenolol-affinity chromatography | Affinity chromatography using alprenolol-sepharose | Alprenolol sepharose | Buffer containing DDM + DDM | Second purification step. Receptor eluted with cyanopindolol. |
| Nickel-affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA | Buffer containing DDM + DDM | Third purification step using His6 tag. |


## Crystallization

### doi/10.1038##nsmb.2504

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) crystallization in membrane-like lipid environment |
| Protein sample | Purified beta1-AR at concentration suitable for LCP. Crystallization at pH ~4 in the presence of synthetic lipids creating a membrane-like environment. |
| Temperature | Not specified in text |
| Notes | Diffraction was highly anisotropic. Structure solved by molecular replacement using the partial agonist (salbutamol)-bound beta1-AR as search model. The crystal packing indicated a membrane-like environment with extensive lipid impaction. At pH ~4, antagonist binding to beta1-AR is reduced, ensuring the ligand-free state. |


## Biological / Functional Insights

### Two distinct GPCR dimer interfaces

The beta1-AR oligomers display two alternating dimer interfaces. Interface 1 (TM1-TM2-H8-ECL1) buries ~1700 A2 of surface area and involves residues from TM1 (Gln38, Gln39, Ala42, Leu46, Ala49, Leu50, Val52, Leu53, Leu54), TM2 (Pro96, Ala99, Thr100, Val103), ECL1 (Thr106, Leu108, Trp109), and H8 (Arg351, Lys354, Arg355, Leu356). A Ser45 hydrogen bond and Glu41-Arg104 salt bridge stabilize this interface. Interface 2 (TM4-TM5-ICL2-ECL2) buries ~900 A2 and involves TM4 (Leu171), TM5 (Arg205, Ala206, Ala210, Ile218, Arg229), ICL2 (Tyr140, Leu141, Thr144, Ser145, Phe147, Arg148, Ser151, Leu152), and ECL2 (Trp181, Arg183). Disulfide cross-linking experiments with cysteine mutants confirmed both interfaces form under physiological conditions.

### Inactive conformation with ionic lock

The ligand-free basal state adopts an inactive conformation, characterized by the presence of the ionic lock salt bridge between Arg139(3.50) and Glu285(6.30) in the D(E)R3.50Y motif and the E/D6.30 residue in TM6. This is consistent with the inactive state of class A GPCRs. The ionic lock is also present in antagonist-bound beta1-AR structures, confirming that the ligand-free state is in an inactive conformation.

### Contracted ligand-binding pocket

The ligand-binding pocket in the ligand-free state is empty and contracted compared to antagonist-bound structures. The distance between C-alpha atoms of Ser211 and Asn329 is narrower than in the antagonist-bound structure (cyanopindolol, PDB 2VT4), but similar to that of agonist-bound structures. This suggests that ligand-binding pocket contraction is not an essential feature of full agonist binding but may be a general feature of the activation-competent conformation.

### G-protein coupling and oligomeric architecture

Docking of the Gs protein (from PDB 3SN6) onto the beta1-AR dimer revealed that G-protein binding to the dimer formed through the TM4-TM5-ICL2 interface would cause steric collision. Therefore, if the signaling unit is a pentamer (two GPCRs and one trimeric G protein), the GPCR dimer interface in this signaling unit is TM1-TM2-H8. Only one beta1-AR contacts the G-protein trimer, and the other beta1-AR could function through trans-protomer allosteric regulation. Alternatively, G-protein binding may disrupt the TM4-TM5-ICL2 dimer interface.

### Comparison with beta1-AR thermostabilized mutants

The ligand-free beta1-AR in this structure is in an inactive conformation, unlike the ligand-free opsin which adopts an active-state conformation. This difference may reflect the different crystallization conditions, particularly the presence of a membrane-like environment. The thermostabilizing mutations in beta1-AR(m23) do not stabilize the receptor in an inactive conformation, as most crystal structures of the M23 mutant with agonists or antagonists displayed intermediate conformations without the ionic lock.


## Cross-References

- [Turkey Beta1-Adrenergic Receptor M23](/xray-mp-wiki/proteins/turkey-beta1-ar-m23/) — Related thermostabilized turkey beta1AR construct; this ligand-free structure provides the basal state for comparison
- [Turkey Beta1-Adrenergic Receptor Thermostabilized Mutant M23 with Cyanopindolol (2VT4)](/xray-mp-wiki/proteins/turkey-beta1-ar-m23-2vt4/) — Antagonist-bound structure for comparison of ligand-binding pocket conformation
- [Human Beta2-Adrenergic Receptor with T4 Lysozyme Fusion (beta2AR-t4l)](/xray-mp-wiki/proteins/beta2-adrenergic-receptor/) — Model system for GPCR-G protein coupling studies; used in docking experiments with beta1-AR oligomers
- [N-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for membrane solubilization and all purification steps
- [Alprenolol](/xray-mp-wiki/reagents/ligands/alprenolol/) — Used for affinity chromatography purification step
- [Cyanopindolol](/xray-mp-wiki/reagents/ligands/cyanopindolol/) — Used to elute receptor from alprenolol-affinity column
- [GPCR Inactive Conformation](/xray-mp-wiki/concepts/gpcr-inactive-conformation/) — This structure represents the ligand-free basal state in an inactive conformation with intact ionic lock
- [GPCR-G Protein Coupling](/xray-mp-wiki/concepts/gpcr-g-protein-coupling/) — Docking experiments with Gs protein on beta1-AR oligomers
