---
title: "GluA2/3 Heteromeric AMPA Receptor"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aad3873]
verified: false
---

# GluA2/3 Heteromeric AMPA Receptor

## Overview

GluA2/3 is a heteromeric AMPA-type ionotropic glutamate receptor composed of GluA2 and GluA3 subunits, representing the predominant form of AMPA receptors in the brain. The crystal structure of the GluA2/3 N-terminal domain (NTD) heteromer was determined at 2.1 A resolution, revealing a novel compact 'O-shape' tetrameric arrangement with alternating subunits around a central axis, in contrast to the 'N-shape' arrangement of GluA2 homomers. [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) structures of the full-length GluA2/3 heteromer at 8.25 A and 10.3 A resolution captured the receptor in resting and desensitized states, revealing substantial vertical compression and close NTD-LBD associations resembling NMDA receptors. GluA2 occupies the pore-proximal (AC) position while GluA3 occupies the pore-distal (BD) position. The work reveals organizational features of heteromeric AMPARs and provides snapshots of gating transitions.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##science.aad3873 | 5FWX | 2.1 |  | GluA2/3 NTD heteromer (GluA2 residues 1-379, GluA3 residues 1-380) | none |
| doi/10.1126##science.aad3873 | 5FWX | 2.5 |  | GluA2/4 NTD heteromer | none |

## Expression and Purification

- **Expression system**: HEK293S GnTI- cells (stable transfection)
- **Construct**: GluA2 NTD (residues 1-379), GluA3 NTD (residues 1-380), GluA4 NTD (residues 1-380)

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Stable transfection in HEK293S GnTI- cells | — | DMEM culture medium | Proteins produced in stably transfected HEK293S-GnTI- cells |
| Initial purification | Cross-flow concentration and dialysis | — | 1 M NaCl, 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8 | Cross-flow concentration followed by dialysis |
| Affinity chromatography | HisTrap HP column | HisTrap HP (GE Healthcare) | 1 M NaCl, 50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8 + not specified |  |
| Size exclusion chromatography | SEC - S200 (GE Healthcare) | — | 50 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.4, 150 mM NaCl | [Endoh](/xray-mp-wiki/reagents/additives/endoh/) treatment for deglycosylation in 100 mM sodium [Acetate](/xray-mp-wiki/reagents/buffers/acetate/) pH 5.2, followed by final SEC |


## Crystallization

### doi/10.1126##science.aad3873

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | GluA2/3 NTD heteromer at 22 mg/ml (mixed stepwise from GluA3 5 mg/ml + GluA2 0.5 mg/ml) |
| Reservoir | 14-16% [Peg](/xray-mp-wiki/reagents/additives/peg/) 3350, 0.27 M ammonium sulfate, 0.1 M [Bicine](/xray-mp-wiki/reagents/buffers/bicine/) pH 9 |
| Temperature | 20 C |
| Cryoprotection | 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Notes | GluA2/3 NTD crystallized at 12.5 mg/ml. GluA2/4 NTD crystallized in 17% [Peg](/xray-mp-wiki/reagents/additives/peg/) 3350, 0.1-0.35 M ammonium sulfate. Data collected at Diamond Light Source I04-1 beamline. |


## Biological / Functional Insights

### O-shape NTD tetramer with alternating subunit arrangement

The GluA2/3 and GluA2/4 NTD heterodimers assemble into a novel tetrameric arrangement called the O-shape, where the four subunits alternate around a central axis. This is distinct from the N-shape seen in GluA2 homomers. The tetrameric interface harbors three major contact regions mediated predominantly by the upper lobes (ULs), with GluA2 at specific diagonal positions. The arrangement is reminiscent of NMDA receptors.

### Vertical compression of the extracellular region

The GluA2/3 heteromer exhibits substantial vertical compression compared to GluA2 homomers. The center of mass distance between the NTD layer and the gate residue Thr625 is 76 A in GluA2/3 (M1), compared to 97 A in GluA2 homomers. This compression is akin to NMDAR architecture and brings the NTD and LBD layers into close contact, creating novel inter-layer interfaces.

### Two distinct ligand-free states captured by cryo-EM

[Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) revealed two models of GluA2/3 in the nominal absence of ligand. Model 1 (M1, 8.25 A) resembles a resting state with intact LBD dimers. Model 2 (M2, 10.3 A) resembles a desensitized state with one LBD dimer ruptured. These provide snapshots of gating transitions in the apo state.

### Subunit positioning in heteromeric AMPARs

In the GluA2/3 heteromer, GluA2 occupies the pore-proximal (AC) position and GluA3 occupies the pore-distal (BD) position at the LBD and TMD levels. However, subunit placement does not follow strict rules, as GluA2 can also occupy the BD position according to the crystal lattice, contrasting with obligatory iGluR heteromers like NMDARs.

### NTD compaction is compatible with gating

Crosslinking the NTD layer in the O-shape conformation did not impair receptor function. O-crosslinked mutants showed similar peak currents, desensitization kinetics, and recovery from desensitization compared to wild-type. This demonstrates that rupture of the NTD layer is not a prerequisite for desensitization, and a compact NTD arrangement permits LBD dynamics and gating transitions.


## Cross-References

- [GluA2 AMPA Receptor](/xray-mp-wiki/proteins/other-ion-channels/glua2-ampa-receptor/) — GluA2 is a subunit of the GluA2/3 heteromeric AMPA receptor
- [Desensitization in Cys-loop Receptors](/xray-mp-wiki/concepts/signaling-receptors/desensitization-in-cys-loop-receptors/) — The M1/M2 states reveal desensitization-like transitions in AMPARs
- [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Referenced in glua2-3-ampa-receptor text
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in glua2-3-ampa-receptor text
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in glua2-3-ampa-receptor text
- [Acetate](/xray-mp-wiki/reagents/buffers/acetate/) — Referenced in glua2-3-ampa-receptor text
- [Endoh](/xray-mp-wiki/reagents/additives/endoh/) — Referenced in glua2-3-ampa-receptor text
- [Bicine](/xray-mp-wiki/reagents/buffers/bicine/) — Referenced in glua2-3-ampa-receptor text
- [Peg](/xray-mp-wiki/reagents/additives/peg/) — Referenced in glua2-3-ampa-receptor text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in glua2-3-ampa-receptor text
