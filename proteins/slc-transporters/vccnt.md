---
title: "vcCNT (Vibrio cholerae Concentrative Nucleoside Transporter)"
created: 2026-06-21
updated: 2026-06-21
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10882]
verified: false
---

# vcCNT (Vibrio cholerae Concentrative Nucleoside Transporter)

## Overview

vcCNT is a concentrative nucleoside transporter from Vibrio cholerae, a member of the SLC28 family of ion-coupled nucleoside transporters. It uses a sodium ion gradient to transport nucleosides across the cell membrane. The crystal structure was solved at 2.4 Å resolution in complex with uridine, revealing a novel fold with a trimeric architecture and an inward-facing occluded conformation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature10882 | 3TIJ | 2.4 | P6_2 | residues 2-416 (full-length construct with His10-MBP fusion removed) | Uridine |

## Expression and Purification

- **Expression system**: Escherichia coli C41 (DE3)
- **Construct**: vcCNT cloned into modified pET26 vector with pelB leader sequence and PreScission Protease-cleavable His10-maltose-binding protein fusion
- **Notes**: Expressed in E. coli C41 (DE3) cells

### Purification Workflow

- **Expression system**: E. coli C41 (DE3)
- **Expression construct**: vcCNT with N-terminal His10-MBP fusion (cleavable by PreScission Protease)
- **Tag info**: His10-MBP fusion, cleaved with PreScission Protease

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Homogenization (Avestin) | — | — + — | Cells lysed with homogenizer |
| Solubilization | Detergent solubilization | — | — + 30 mM dodecyl maltoside (DDM) | 2 h at 4 °C |
| Affinity chromatography | Co2+ affinity chromatography | Talon Co2+ affinity resin | — + — | Eluted with imidazole |
| Tag cleavage | Proteolytic cleavage | — | — + — | Digested overnight with PreScission Protease |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 | 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 2 mM dithiothreitol + 5 mM decyl maltoside (DM) | Presence of 1 mM uridine |

**Final sample**: vcCNT in 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 5 mM DM, 2 mM DTT, 1 mM uridine


## Crystallization

### doi/10.1038##nature10882

| Parameter | Value |
|---|---|
| Method | Microbatch-under-oil |
| Protein sample | ~10 mg/ml vcCNT in 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 5 mM DM, 2 mM DTT, 1 mM uridine |
| Reservoir | 100 mM CaCl2, 37-42% PEG400, 100 mM buffer (Tris-HCl pH 9.0 or glycine pH 9.5) |
| Mixing ratio | 1:1 |
| Temperature | — |
| Growth time | 10-14 days |
| Cryoprotection | 32.5% PEG400 |
| Notes | Crystals grown over pH range 5.6-9.5; data collected from crystals at pH 9.0 (Tris-HCl) and pH 9.5 (glycine). Platinum derivatives prepared by soaking in 2.5 mM K2Pt(CNS)6 for 2-4 h. |


## Biological / Functional Insights

### Overall Architecture

vcCNT crystallizes as a homotrimer shaped like an inverted triangular basin with the mouth facing the intracellular side. Each protomer contains eight transmembrane helices (TM1-TM8), two re-entrant helix-turn-helix hairpins (HP1 and HP2), and three interfacial helices (IH1-IH3). The fold is novel, with a scaffold domain (TM1, TM2, IH1, EH, TM3, TM6) and a transport domain (IH2, HP1, TM4a/b, TM5 and IH3, HP2, TM7a/b, TM8) related by internal two-fold pseudo-symmetry.

### Nucleoside and Sodium Binding

Uridine binds in a cleft between HP1, HP2, TM4, and TM7. HP1 and TM4b interact with the uracil base, while HP2 and TM7 interact with the ribose. Key residues include Gln154, Thr155, Glu156 (HP1), Val188 (TM4b) for uracil, and Glu332 (HP2), Asn368, Ser371 (TM7) for ribose. A Na+ binding site is located between HP1 and the unwound region of TM4, coordinated by three backbone carbonyls, two side-chain hydroxyls, and a water molecule. Na+ binding is proposed to bring HP1 close to TM4 to complete the nucleoside-binding site.

### Transport Mechanism

The structure represents an inward-facing occluded conformation. A hypothetical alternating-access mechanism is proposed where rigid-body movement of the transport domain across TM6 (which serves as a hydrophobic barrier) permits transition between inward-facing and outward-facing conformations, while the scaffold domain is held in place.


## Cross-References

- [vcCNT (Vibrio cholerae Concentrative Nucleoside Transporter)](/xray-mp-wiki/proteins/slc-transporters/vccnt/) — Primary entity described in this paper
