---
title: Thermus thermophilus SecY Core Channel Subunit
created: 2026-05-27
updated: 2026-05-27
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.celrep.2015.10.025]
verified: false
---

# Thermus thermophilus SecY Core Channel Subunit

## Overview

SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric protein-conducting channel complex essential for protein translocation across the bacterial plasma membrane and integration of membrane proteins. SecY from Thermus thermophilus comprises 10 transmembrane helices that form an hourglass-shaped protein-conducting channel with a lateral gate. The channel is sealed on the periplasmic side by a plug helix and on the cytoplasmic side by the [SECG](/xray-mp-wiki/proteins/secg) loop. The lateral gate, formed by TM2, TM7, and TM8, opens laterally to allow signal peptides and nascent polypeptides to exit the channel into the lipid bilayer.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.celrep.2015.10.025 | 5AWW | 2.7 A | I222 | Thermus thermophilus SecY (R252G mutation); part of full-length SecYEG heterotrimer; expressed in E. coli BL21(DE3) | None |
| doi/10.1016##j.celrep.2015.10.025 | 5CH4 | 3.6 A | C222_1 | Thermus thermophilus SecY (R252G mutation); part of SecYEG heterotrimer in peptide-bound state; expressed in E. coli BL21(DE3) | SecE N-terminal MFARL peptide contacting lateral gate |

## Expression and Purification

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Thermus thermophilus SecY(R252G)-His6; co-expressed with SecE and SecG from dual plasmid system

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane fraction preparation | Differential centrifugation | -- | Not specified + -- | Total membrane fraction from E. coli BL21(DE3) cells co-expressing [SECYEG](/xray-mp-wiki/proteins/secyeg) |
| Solubilization | Detergent solubilization | -- | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 300 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.1 mM [PMSF](/xray-mp-wiki/reagents/additives/pmsf) + 2% n-dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm)) | 1 hr at 4 C; ultracentrifugation at 138,000 x g for 30 min |
| Ni-NTA affinity chromatography | Affinity chromatography (His-tag on SecY) | Ni-NTA agarose | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 300 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Equilibration with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole); wash with 40 mM imidazole; elution with 300 mM imidazole |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 10/300 GL column | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 300 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Concentrated to ~15 mg/ml using Amicon Ultra 50-kDa cutoff filter |
| Ion-exchange chromatography | Ion-exchange chromatography | HiTrap SP HP column | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 0.25% n-decyl-beta-D-maltoside (DM), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) + 0.25% DM | Elution with linear gradient of 0-100% elution buffer (1 M NaCl, 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 0.25% DM, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol)) |


## Crystallization

### doi/10.1016##j.celrep.2015.10.025

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase crystallization |
| Protein sample | Purified [SECYEG](/xray-mp-wiki/proteins/secyeg) complex (~15 mg/ml) mixed with liquefied [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) at 2:3 protein-to-lipid ratio (w/w) |
| Temperature | 20 C |
| Growth time | About 10 days |
| Cryoprotection | Cryocooled to 100 K for X-ray data collection |
| Notes | I222 space group; resting state structure at 2.7 A resolution |


## Biological / Functional Insights

### Hourglass-shaped protein-conducting channel

SecY forms an hourglass-shaped channel through its pseudo-symmetrically related N-terminal and C-terminal halves, each contributing 5 transmembrane helices. The constricting region, the pore ring, consists of six conserved hydrophobic residues (I77, I81, T184, I188, I275, I403 in Thermus thermophilus numbering) that create a narrow constriction likely permitting membrane permeability while restricting ion flux. The channel is sealed on the periplasmic side by a plug helix and on the cytoplasmic side by the [SECG](/xray-mp-wiki/proteins/secg) loop, preventing uncontrolled membrane leakage.

### Lateral gate mechanism for substrate access

TM2, TM7, and TM8 of SecY form a cytoplasmic hydrophobic crack and a following rift, termed the lateral gate. This gate opens laterally to allow signal peptides and nascent polypeptide chains to exit the channel into the lipid bilayer. In the resting state, the lateral gate is closed. In the peptide-bound state, the cytoplasmic crack is expanded, with the N-terminal MFARL segment of [SECE](/xray-mp-wiki/proteins/sece) inserting into the crack, demonstrating how peptide binding induces lateral gate opening. This mechanism is conserved across bacterial and eukaryotic Sec translocons.


## Cross-References

- [Thermus thermophilus SecYEG Translocon Complex](/xray-mp-wiki/proteins/secretion-translocon/secyeg/) — SecY is the core channel-forming subunit of the SecYEG heterotrimer
- [Thermus thermophilus SecE Accessory Subunit](/xray-mp-wiki/proteins/secretion-translocon/sece/) — SecE essential accessory subunit that stabilizes SecY in the SecYEG complex
- [Thermus thermophilus SecG Accessory Subunit](/xray-mp-wiki/proteins/secretion-translocon/secg/) — SecG accessory subunit that covers the cytoplasmic side of the SecY channel
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Primary lipid component for LCP crystallization of SecYEG
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for SecYEG structure determination
- [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) — Main buffer component in purification
- [PMSF](/xray-mp-wiki/reagents/additives/pmsf) — Entity mentioned in text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) — Cryoprotectant and buffer additive
- [DDM](/xray-mp-wiki/reagents/detergents/ddm) — Detergent used in solubilization and purification
- [MOPS](/xray-mp-wiki/reagents/buffers/mops) — Crystallization buffer component
