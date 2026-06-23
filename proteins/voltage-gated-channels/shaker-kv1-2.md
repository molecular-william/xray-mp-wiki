---
title: Shaker Kv1.2 Potassium Channel
created: 2026-06-10
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1000142107, doi/10.1126##science.1116269, doi/10.1126##sciadv.abm8804]
verified: false
---

# Shaker Kv1.2 Potassium Channel

## Overview

Kv1.2 is a voltage-dependent potassium channel from Rattus norvegicus belonging to the Shaker family. The channel is a homotetramer with four voltage-sensor domains and one central pore domain. Each subunit contains six transmembrane helices (S1-S6), where S1-S4 form the voltage-sensor domain and S5-S6 contribute to the central pore domain. The original crystal structure (PDB 2A79) was determined at 2.9 Å resolution in complex with an oxido-reductase β2 subunit. The structure revealed the voltage-sensor paddle architecture, the S4-S5 linker coupling mechanism, and the open activation gate with Pro-Val-Pro curved S6 inner helices. Large side portals between the T1 domain and the pore connect the pore to the cytoplasm.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1000142107 | 2A79 | 2.9 | I4 | Full-length Kv1.2 from Rattus norvegicus (transmembrane residues 131-421) with β2 subunit | K+, NADP+ |
| doi/10.1126##science.1116269 | 2A79 | 2.9 | I4 | Kv1.2-β2 subunit complex, co-expressed in Pichia pastoris | K+, NADP+ |

## Expression and Purification

- **Expression system**: Pichia pastoris (co-expression of Kv1.2 and β2 subunit)
- **Construct**: Full-length Kv1.2 from Rattus norvegicus with β2 subunit, co-expressed in P. pastoris
- **Notes**: The β2 subunit is an oxido-reductase that can regulate mammalian Kv channels. A mixture of lipids and detergent was used throughout purification. [DTT](/xray-mp-wiki/reagents/additives/dtt/) and TCEP were used to maintain reducing environment; oxygen-depleted atmosphere was used.

### Purification Workflow

- **Expression system**: Pichia pastoris
- **Expression construct**: Full-length Kv1.2 + β2 subunit

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Yeast fermentation (Pichia pastoris) | — |  | Co-expression of Kv1.2 and β2 subunit |
| Purification | Mixed lipid/detergent purification | — |  | Lipids and detergent mixture used throughout. [DTT](/xray-mp-wiki/reagents/additives/dtt/) and TCEP (tri(2-carboxyethyl)phosphine hydrochloride) present to maintain reducing environment. Oxygen-depleted atmosphere maintained. |

**Final sample**: Kv1.2-β2 complex in lipid/detergent mixture with reducing agents


## Crystallization

### doi/10.1126##science.1116269

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Kv1.2-β2 subunit complex in lipid/detergent mixture |
| Temperature | 100 (cryo) |
| Cryoprotection | Frozen in liquid nitrogen |
| Notes | Crystals in space group I4 (unit cell 113.6, 113.6, 260.5 A), grown by vapor diffusion and frozen in liquid nitrogen. Diffracted to 2.9 A at NSLS X-25 beamline. |


## Biological / Functional Insights

### Open activation gate with Pro-Val-Pro curved S6 helices

The pore of Kv1.2 has a diameter of about 12 Å at the bundle crossing, indicating an open conformation. The S6 inner helices contain the highly conserved Pro-Val-Pro sequence that curves the helices to run almost parallel to the membrane near the intracellular surface. Large side portals between the T1 domain and the pore allow K+ ions and inactivation peptides to access the pore.

### Voltage-sensor paddle architecture

The voltage sensor is latched around the pore of an adjacent subunit. The S4-S5 linker helix runs parallel to the intracellular membrane surface at the level of the inner-helix bundle crossing, positioned to constrict or dilate the S6 inner helices. Two of four conserved Arg residues on S4 are on a lipid-facing surface and two are buried in the voltage sensor.

### β2 subunit as potential redox sensor

The β2 subunit has an NADP+ cofactor and catalytic residues for hydride transfer at its active site. Extra density overlying the active site suggests a bound polypeptide or organic molecule. The β subunit could function as a redox sensor coupling membrane electrical activity to the cellular redox state.

### T1 domain and inactivation gating

The N terminus of the structured β2 subunit is located ~80 Å from the pore, and the channel T1 domain N terminus is ~50 Å from the pore. Shaker channels with N-type inactivation peptides have extended N termini (≥30 amino acids beyond T1) that can reach the pore for "ball and chain" inactivation. The β1 subunit has ~70 additional N-terminal amino acids that serve as an inactivation peptide.


## Cross-References

- [KcsA Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/) — Selectivity filter structure conserved; inner helix bundle comparison for gating mechanism
- [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/kvap/) — Prokaryotic Kv channel used for structural comparison; glycine-gating hinge vs Pro-X-Pro in Shaker
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used in purification steps
- [DTT](/xray-mp-wiki/reagents/additives/dtt/) — Additive used in purification or crystallization buffers
