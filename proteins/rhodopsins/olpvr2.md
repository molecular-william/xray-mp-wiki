---
title: "OLPVRII (Organic Lake Phycodnavirus Rhodopsin II)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-019-12718-0]
verified: false
---

# OLPVRII (Organic Lake Phycodnavirus Rhodopsin II)

## Overview

OLPVRII (Organic Lake Phycodnavirus Rhodopsin II) is a viral rhodopsin from group 2, encoded by a nucleocytoplasmic large DNA virus (NCLDV) that infects marine phytoplankton. With only 211 amino acids, it is the smallest microbial rhodopsin with a known crystal structure. OLPVRII assembles into a pentamer with a unique bottle-like central channel featuring a narrow vestibule lined by a ring of five arginine residues (R29) on the cytoplasmic side and a hydrophobic barrier formed by five phenylalanine residues (F24). The proton donor is Glu42 located in helix B, whereas most microbial rhodopsins have the proton donor in helix C. Functional characterization and molecular dynamics simulations suggest that OLPVRII acts as an outward proton pump in liposomes, but its unique pentameric architecture with a central pore analogous to pentameric ligand-gated ion channels suggests it may function as a light-gated ion channel.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41467-019-12718-0 | 6S7I | 2.50 | P21 | Full-length OLPVRII (residues 1-211) | all-trans Retinal |

## Expression and Purification

- **Expression system**: Escherichia coli (C41 strain)
- **Construct**: Codon-optimized OLPVRII (Uniprot F2Y2Z0) in pEKT vector
- **Induction**: Not specified
- **Media**: 2xYT medium

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | -- | 2xYT medium + -- | 5L culture |
| Membrane preparation | Cell disruption and membrane isolation | -- | 50 mM Tris-HCl pH 7.6, 300 mM NaCl + -- | Standard membrane preparation protocols |
| Solubilization | Detergent solubilization | -- | 50 mM Tris-HCl pH 7.6, 300 mM NaCl + DDM (n-Dodecyl-beta-D-maltopyranoside) | Protein solubilized in DDM |
| Affinity chromatography | Immobilized metal-affinity chromatography (IMAC) | Ni-NTA | 50 mM Tris-HCl pH 7.6, 300 mM NaCl, 20 mM imidazole + DDM | His-tag purification |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 | 10 mM Tris-HCl pH 7.6, 100 mM NaCl, 0.03% DDM + 0.03% DDM | Monomeric and pentameric fractions separated |

**Final sample**: 20 mg/ml in DDM
**Purity**: High (A280/A520 ratio 1.0-1.3 for monomers, 1.3-1.7 for pentamers)


## Crystallization

### doi/10.1038##s41467-019-12718-0

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | 20-25 mg/ml OLPVRII in DDM |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Protein-to-lipid ratio | 60:40 (w/w) |
| Temperature | 22 |
| Growth time | 6-12 weeks |
| Cryoprotection | Crystals flash-cooled in liquid nitrogen |
| Notes | Crystals grown using in meso approach. Diffraction data collected at P14 beamline (PETRAIII, Hamburg). Structure solved by molecular replacement using archaerhodopsin-2 (PDB 2Ei4) as search model. |


## Biological / Functional Insights

### Unique pentameric architecture with central channel

OLPVRII assembles as a pentamer with a bottle-shaped central pore formed by the A and B helices of the protomers. The narrowest section (vestibule) is 11 Å long with a mean diameter of 6 Å. On the cytoplasmic side, a ring of five conserved arginine residues (R29) forms the entrance, while five phenylalanine residues (F24) create a hydrophobic barrier deeper in the pore. This architecture is unique among microbial rhodopsins and is structurally analogous to the transmembrane channels of pentameric ligand-gated ion channels (pLGICs) such as GLIC.

### Proton donor relocated to helix B

Unlike most microbial rhodopsins where the proton donor is Asp96 in helix C (as in bacteriorhodopsin), OLPVRII has its proton donor Glu42 located in helix B. This is a striking difference in the architecture of the proton translocation pathway. The E42Q mutant showed a prolonged M-state decay (similar to D96N in bacteriorhodopsin), confirming its role as the proton donor. The proton acceptor is Asp75, as the D75N mutant failed to form the M-state.

### Photocycle kinetics

The total photocycle of OLPVRII is approximately 70 ms at pH 7.5, with seven exponential components. The microsecond part (1-340 µs) includes K540-like to M410-like transitions representing RSB deprotonation. The millisecond part (10-73 ms) involves recovery of the ground state via M410-, N525-, and O550-like intermediates. The pKa of the RSB is 10.36 ± 0.08, and the pKa of the proton acceptor Asp75 is 3.34 ± 0.11.

### Outward proton pump activity

Black lipid membrane (BLM) experiments showed that OLPVRII generates photocurrents upon illumination. Without protonophores, a transient current was observed; with the ionophores 1799 and monensin, continuous pumping was detected. Time-resolved BLM measurements identified charge movements with time constants of 24 µs, 6 ms, 90 ms, and 950 ms, corresponding to the photocycle transitions. Direct pH measurements in liposomes confirmed outward proton pumping, although the charge transfer per photocycle is small compared to expected channel activity.

### Pentameric assembly is conserved in group II viral rhodopsins

The key amino acids forming the pentamer (E26, R36, W203) are highly conserved in group II viral rhodopsins. A triple mutant (E26A/R36A/W203A) showed reduced pentamer:monomer ratio (1:1 vs 4:1 for WT), confirming the importance of these residues for pentamerization. The pentameric assembly is required for the formation of the central pore/channel and likely determines the function of group II viral rhodopsins.


## Cross-References

- [OLPVR1](/xray-mp-wiki/proteins/rhodopsins/olpvr1/) — Related group 1 viral channelrhodopsin from the same virus
- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Archetypal microbial rhodopsin for structural comparison
- [KR2 (Krokinobacter eikastus sodium-pumping rhodopsin)](/xray-mp-wiki/proteins/rhodopsins/kr2/) — Reference for pentameric rhodopsin structure comparison
- [GLIC (Gloeobacter violaceus ligand-gated ion channel)](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) — Structural analog for pentameric channel architecture
- [All-trans retinal](/xray-mp-wiki/reagents/ligands/retinal/) — Chromophore cofactor covalently bound via Schiff base to Lys195
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — LCP crystallization lipid matrix
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent for protein solubilization and purification
