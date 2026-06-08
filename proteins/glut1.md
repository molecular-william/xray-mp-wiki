---
title: Human Glucose Transporter GLUT1 (SLC2A1)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature13306]
verified: false
---

# Human Glucose Transporter GLUT1 (SLC2A1)

## Overview

The human glucose transporter GLUT1 (encoded by SLC2A1) catalyses facilitative diffusion of glucose into erythrocytes and is responsible for glucose supply to the brain and other organs. Dysfunctional mutations lead to GLUT1 deficiency syndrome (De Vivo syndrome), characterised by early-onset seizures, microcephaly and retarded development. Over-expression of GLUT1 is a prognostic indicator for cancer. GLUT1 belongs to the sugar porter subfamily of the major facilitator superfamily (MFS) and has a canonical MFS fold with 12 transmembrane segments organised into amino- and carboxy-terminal domains. The crystal structure was determined at 3.2 A resolution in an inward-open conformation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature13306 | unknown | 3.2 | C2 | Full-length human GLUT1, residues 1-492, N45T and E329Q mutations, C-terminal 10x His tag | n-Nonyl-beta-D-glucopyranoside (beta-NG) |

## Expression and Purification

- **Expression system**: High Five insect cells (baculovirus expression)
- **Construct**: Full-length human GLUT1, residues 1-492, C-terminal 10x His tag

### Purification Workflow

- **Expression system**: High Five insect cells (baculovirus)
- **Expression construct**: Full-length human GLUT1, residues 1-492, C-terminal 10x His tag
- **Tag info**: 10x His tag, C-terminal

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Dounce homogenization | — | 25 mM Tris-HCl pH 8.0, 150 mM NaCl | 80 cycles on ice |
| Membrane preparation | Ultracentrifugation | — | 25 mM Tris-HCl pH 8.0, 150 mM NaCl | 150,000g for 1 h; membrane fraction harvested |
| Membrane solubilization | Detergent solubilization | -- | TBS (25 mM Tris pH 8.0, 150 mM NaCl) + 2% (w/v) DDM | 2 h at 4 C with protease inhibitors (aprotinin 0.8 uM, pepstatin 2 uM, leupeptin 5 ug/ml) |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA (Qiagen) | 25 mM MES pH 6.0, 150 mM NaCl, 30 mM imidazole, 5% glycerol, 0.05% DDM + 0.05% DDM | 30 min at 4 C; elute with 300 mM imidazole |
| Size-exclusion chromatography | SEC | Superdex-200 (GE Healthcare) | 25 mM MES pH 6.0, 150 mM NaCl, 5% glycerol, 0.4% beta-NG + 0.4% beta-NG | Concentrated to 10 mg/ml before SEC |

**Final sample**: 10 mg/ml in 25 mM MES pH 6.0, 150 mM NaCl, 5% glycerol, 0.4% beta-NG


## Crystallization

### doi/10.1038##nature13306

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | GLUT1 (N45T, E329Q) purified in 0.4% beta-NG |
| Reservoir | 30% (w/v) PEG400, 0.1 M MES pH 6.0, 0.1 M MgCl2 |
| Temperature | 4 C |


## Biological / Functional Insights

### Inward-open conformation with beta-NG bound

The full-length human GLUT1 structure was captured in an inward-open conformation. A beta-NG molecule binds in the inward-open cavity, with its D-glucopyranoside moiety positioned at the C domain of GLUT1 at approximately the centre of the membrane, while the aliphatic tail points to the intracellular side. The sugar moiety is hydrogen-bonded to polar residues in the C domain including Gln 282/Gln 283/Asn 288 from TM7, Asn 317 from TM8, and Asn 415 from TM11. The similar coordination of D-glucopyranoside by inward-open GLUT1 and D-glucose by outward-facing XylE supports the notion of a single sugar-binding site alternately accessible from either side of the membrane.

### Alternating access mechanism via N/C domain rotation

Structural comparison of inward-open GLUT1 and outward-facing XylE reveals an approximately 16 degree concentric rotation of the N and C domains. The C domain provides the primary substrate-binding site while the relative motion of the N domain results in alternating access. In the inward-open GLUT1, residues from the N domain are not involved in ligand binding. The ligand-free protein may prefer an outward-open conformation; substrate binding at the primary site on the C domain induces closure of N and C domains on the extracellular side, leading to rearrangement of interactions on both sides of the bound substrate.

### Disease-related mutations in three clusters

Disease-derived mutations from GLUT1 deficiency syndrome map to three clusters: Cluster I comprises substrate-binding residues; Cluster II is located at the interface between the transmembrane domain and the ICH domain; Cluster III comprises residues lining the transport path, mostly committed to interactions between the N and C domains on the extracellular side. Mutations affecting Asn 34, Ser 66, Arg 126, Glu 146, Gly 130, Arg 223, Lys 256, Ala 275, Tyr 292, Ser 294, Thr 295, Val 303, Thr 310, Gly 314, Asn 317, Ser 324, Asp 329, and Asn 45 have been identified from patients.

### ICH domain as intracellular gate latch

The intracellular helix (ICH) domain represents a unique feature of the sugar porter subfamily and functions as a latch to secure closure of the intracellular gate in the outward-facing conformation. The ICH domain forms hydrogen bonds from the backbone amide groups of Gly 154 and Lys 155, stabilized by charge-stabilized hydrogen bonds between Asp 329 and Arg 333. Disease-related mutations in this interface (E329Q) are predicted to weaken these interactions, favouring the inward-facing conformation and impeding the transport cycle.

### Extracellular gate structure

In the inward-open conformation, TM1 and TM7 contact each other on the extracellular side, forming the major constituents of the extracellular gate. Asn 34 on TM1 appears to be an organizing centre mediating hydrogen bonds to Ser 294 and Thr 295 on TM7 and Thr 310 on TM8. Arg 126 on TM4 may form a cation-pi interaction with Tyr 292 on TM7 of the C domain, contributing to the affinity of the extracellular gate. TM7 of GLUT1 contains one extra kink close to its extracellular end compared to outward-facing XylE.

### Comparison of uniporter GLUT1 with proton symporter XylE

Structural comparison of the proton-independent uniporter GLUT1 and its bacterial homologue XylE (a proton-coupled xylose symporter), obtained in distinct conformations, allows mechanistic analysis of facilitative diffusion versus active transport. In XylE, Asp 27 is critical for proton coupling; this residue corresponds to Asn 29 in GLUT1. The structure of GLUT1 provides an opportunity to understand the protonated state of proton symporters. Uniporters catalyse substrate translocation down its concentration gradient, while proton symporters exploit the transmembrane proton gradient to drive uphill translocation.


## Cross-References

- [XylE (Escherichia coli Sugar Transporter)](/xray-mp-wiki/proteins/xyle/) — Bacterial homologue; structural comparison reveals 16 degree domain rotation
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/mfs-transporter/) — GLUT1 belongs to the MFS, specifically the sugar porter subfamily
- [Sugar Porter (SP) Family](/xray-mp-wiki/concepts/sugar-porter-family/) — GLUT1 is a member of the sugar porter subfamily of MFS transporters
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — GLUT1 transports glucose via the alternating access mechanism
- [Conformational Dynamics in MFS Transporters](/xray-mp-wiki/concepts/conformational-dynamics-mfs/) — N/C domain rotation of 16 degrees observed between inward-open and outward-facing states
- [Rocker-Switch Mechanism in MFS Transporters](/xray-mp-wiki/concepts/rocker-switch-mechanism/) — MFS-specific variant of alternating access mechanism employed by GLUT1
- [n-Nonyl-beta-D-glucopyranoside (beta-NG)](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/) — Detergent used for crystallization; binds to substrate-binding site
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for membrane solubilization and purification
