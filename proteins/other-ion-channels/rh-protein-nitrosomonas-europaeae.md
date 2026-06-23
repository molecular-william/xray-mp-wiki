---
title: "Rh Protein from Nitrosomonas europaea"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0709710104]
verified: false
---

# Rh Protein from Nitrosomonas europaea

## Overview

The Rh protein from Nitrosomonas europaea is the first determined structure of an Rh (Rhesus) family member. Rh proteins are integral membrane proteins implicated in the transport of NH3, CH2NH2, and CO2. The structure reveals a trimeric oligomeric state with 11 transmembrane helices per monomer, plus a unique cytoplasmic C-terminal alpha-helix that forms a three-helix bundle along the three-fold axis. The channel contains a twin-His site (His170, His324) in the middle and a conserved phenylalanine (Phe218) that blocks the transport pathway. CO2 pressurization experiments identified a CO2 binding site near the intracellular channel exit. The structure supports the hypothesis that Rh proteins may function primarily as CO2 channels, with a gating mechanism regulated by partner protein binding to the C-terminal helix.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0709710104 | 3B9Y |  |  | Full-length Rh protein from Nitrosomonas europaea; structure determined by Se-Met MAD phasing |  |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Rh protein from Nitrosomonas europaea (full-length)

### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: Full-length N. europaea Rh protein
- **Tag info**: --

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Overexpression | Fermentation | -- | -- + -- | Rh protein overexpressed in E. coli |
| Purification | Chromatography | -- | -- + -- | Details provided in SI Text |


## Crystallization

### doi/10.1073##pnas.0709710104

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified Rh protein |
| Reservoir | -- |
| Temperature | -- |
| Growth time | -- |
| Cryoprotection | -- |
| Notes | Structure determined by the Se-Met multiwavelength anomalous diffraction (MAD) method using data collected at the Stanford Synchrotron Radiation Laboratory (SSRL). All structural figures prepared with PYMOL. CO2 pressurization experiments performed using SSRL gas pressure cell. |


## Biological / Functional Insights

### First structure of an Rh family member

This is the first reported structure of an Rh (Rhesus) protein. The Rh protein shares a trimeric fold with Amt/MEP proteins, with 11 transmembrane helices per subunit and a central pore. However, it exhibits three key differences: (1) an additional cytoplasmic C-terminal alpha-helix that forms a three-helix bundle; (2) a higher number of internal proline residues in transmembrane helices (6 vs 2 in Amt), which can induce helix kinking; and (3) the absence of the extracellular pi-cation binding site conserved in Amt/Mep structures for ammonium recruitment.

### Twin-His site and Phe barrier

The channel features a twin-His site (His170 and His324) in a coplanar orientation that may stabilize an H+ ion between them, similar to AmtB. Below the twin-His site, Phe218 serves as a steric barrier blocking substrate passage. Unlike AmtB where two Phe residues block the channel, only Phe218 serves this role in the Rh protein due to an altered orientation of the second Phe (Phe110). The neighboring proline Pro216 on helix M6 induces a helical kink whose bending angle dictates Phe218 position, suggesting a mechanism for channel gating via helical kinking.

### CO2 binding site

CO2 pressurization experiments identified a CO2 binding site near the intracellular exit of the channel. The residues forming this site are highly conserved in all Rh proteins except the Rh30 subfamily (RhD and RhCE). The presence of this CO2 binding site, together with the absence of the pi-cation binding site used by Amt proteins for NH4+ recruitment, suggests that Rh proteins may primarily transport CO2 rather than ammonia.

### Proposed partner protein-mediated channel gating

The C-terminal alpha-helix is linked to channel opening via a series of interactions: Glu393 on the C-terminal helix forms salt bridges with Arg63 and Arg64 at the C-terminus of helix M1. Tyr41 on helix M1 is hydrogen-bonded to Ser217 on helix M6 of an adjacent subunit. Ser217 lies directly adjacent to Pro216, which induces a helical kink in M6 and determines the position of Phe218 (the steric barrier). Thus, binding of a partner protein (such as carbonic anhydrase, Rubisco, AMO, or glutamine synthetase) to the C-terminal helix could regulate channel opening by shifting Phe218.

### Implications for human Rh antigens

The structure provides insights into the human Rh blood group antigens (RhD and RhCE of the Rh30 subfamily). These proteins lack several key conserved residues including the CO2 binding site and the C-terminal helix, suggesting they may have adapted a structural role in the erythrocyte membrane or evolved an alternate transport function. The Rh-associated glycoprotein (RHAG) is more similar to the N. europaea Rh protein and likely retains transport function.


## Cross-References

- [Ammonium Transporter AmtB (E. coli)](/xray-mp-wiki/proteins/other-ion-channels/amt-b/) — Homologous Amt/MEP family member; structural comparison reveals key differences in Rh vs Amt architecture
