---
title: Thermus thermophilus SecE Accessory Subunit
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.celrep.2015.10.025]
verified: false
---

# Thermus thermophilus SecE Accessory Subunit

## Overview

SecE is an essential accessory subunit of the bacterial Sec translocon that stabilizes the core [SECY](/xray-mp-wiki/proteins/secy) channel subunit within the membrane. SecE from Thermus thermophilus is a small protein with a single transmembrane helix and large cytoplasmic and periplasmic domains. It is located at the back of SecY and contributes to maintaining the structural integrity of the [SECYEG](/xray-mp-wiki/proteins/secyeg) translocon complex. The high-resolution structure of the full SecYEG complex reveals that SecE forms a stable interaction surface with SecY, helping to maintain the hourglass-shaped channel architecture.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.celrep.2015.10.025 | 5AWW | 2.7 A | I222 | Thermus thermophilus SecE; part of full-length SecYEG heterotrimer; expressed in E. coli BL21(DE3) | None |
| doi/10.1016##j.celrep.2015.10.025 | 5CH4 | 3.6 A | C222_1 | Thermus thermophilus SecE; part of SecYEG heterotrimer in peptide-bound state; expressed in E. coli BL21(DE3) | N-terminal MFARL segment contacts SecY lateral gate in peptide-bound state |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecE; co-expressed with SecY(R252G)-His6 and SecG from dual plasmid system

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane fraction preparation | Differential centrifugation | -- | Not specified + -- | Total membrane fraction from E. coli BL21(DE3) cells co-expressing [SECYEG](/xray-mp-wiki/proteins/secyeg) |
| Solubilization | Detergent solubilization | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 300 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.1 mM [PMSF](/xray-mp-wiki/reagents/additives/pmsf) + 2% n-dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm)) | 1 hr at 4 C; ultracentrifugation at 138,000 x g for 30 min |
| Ni-NTA affinity chromatography | Affinity chromatography (His-tag on [SECY](/xray-mp-wiki/proteins/secy)) | Ni-NTA agarose | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 300 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Co-purification of SecE with His-tagged [SECY](/xray-mp-wiki/proteins/secy); equilibration with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole); wash with 40 mM imidazole; elution with 300 mM imidazole |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 10/300 GL column | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 300 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | SecE co-elutes with [SECY](/xray-mp-wiki/proteins/secy) and [SECG](/xray-mp-wiki/proteins/secg) as a stable heterotrimeric complex |
| Ion-exchange chromatography | Ion-exchange chromatography | HiTrap SP HP column | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 0.25% n-decyl-beta-D-maltoside (DM), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + 0.25% DM | [SECYEG](/xray-mp-wiki/proteins/secyeg) heterotrimer eluted with linear gradient of 0-100% elution buffer (1 M NaCl, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 0.25% DM, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol)) |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### Structural stabilization of SecY channel

SecE is located at the back of [SECY](/xray-mp-wiki/proteins/secy) and forms a stable interaction surface that helps maintain the structural integrity of the [SECYEG](/xray-mp-wiki/proteins/secyeg) complex. The high-resolution 2.7 A structure reveals that SecE contributes to the overall architecture of the translocon, stabilizing the hourglass-shaped SecY channel. SecE is essential for SecY stability and function in vivo; deletion of SecE leads to SecY degradation and loss of protein translocation activity.

### N-terminal MFARL segment in peptide-bound state

In the peptide-bound state structure (PDB 5CH4), the N-terminal MFARL segment of SecE inserts directly into the hydrophobic crack of another [SECY](/xray-mp-wiki/proteins/secy) monomer. The hydrophobic side chains of F2 and A3 interact with I85, I89, and F322 on the cytoplasmic hydrophobic crack of SecY, while R4 interacts with conserved Q88. This interaction mimics signal peptide binding to the lateral gate and provides insight into the early stages of protein translocation.


## Cross-References

- [Thermus thermophilus SecYEG Translocon Complex](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) — SecE is the essential accessory subunit of the SecYEG heterotrimer
- [Thermus thermophilus SecY Core Channel Subunit](/xray-mp-wiki/proteins/secretion-translocon/secy/) — SecE stabilizes the SecY channel in the membrane
- [Thermus thermophilus SecG Accessory Subunit](/xray-mp-wiki/proteins/secretion-translocon/secg/) — SecE and SecG both serve as accessory subunits of the SecYEG translocon
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) — Main buffer component in purification
- [PMSF](/xray-mp-wiki/reagents/additives/pmsf) — Entity mentioned in text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) — Cryoprotectant and buffer additive
- [DDM](/xray-mp-wiki/reagents/detergents/ddm) — Detergent used in solubilization and purification
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) — Eluent for affinity chromatography
