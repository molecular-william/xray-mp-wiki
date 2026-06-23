---
title: Human Aquaporin 2 (AQP2)
created: 2026-06-08
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [channel, membrane-protein]
sources: [doi/10.1073##pnas.1321406111, doi/10.1107##s2052252519007395]
verified: false
---

# Human Aquaporin 2 (AQP2)

## Overview

Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) 2 ([AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/)) is a water channel found in the kidney collecting duct, where it plays a key role in concentrating urine through regulated water reabsorption. [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) trafficking between intracellular storage vesicles and the apical membrane is tightly controlled by the pituitary hormone arginine vasopressin (AVP). The 2.75 A X-ray structure reveals the conserved [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) fold with six transmembrane helices and two half-membrane spanning helices, assembled as a tetramer. The C terminus displays multiple conformations, with a C-terminal alpha-helix potentially involved in protein-protein interactions governing cellular sorting. Two Cd2+-binding sites are observed within the tetramer, and Ca2+ is proposed as the physiological ligand. Defective trafficking of [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) results in [Nephrogenic Diabetes Insipidus](/xray-mp-wiki/concepts/miscellaneous/nephrogenic-diabetes-insipidus/) (NDI). An additional room-temperature SFX structure was determined at 3.7 A resolution from on-chip crystallized crystals using the Roadrunner II fixed-target system at LCLS (PDB 6qf5), demonstrating the feasibility of on-chip crystallization for membrane protein serial crystallography.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1321406111 | 4nef | 2.75 | P4_2 | C-terminally truncated at Pro242, expressed in Pichia pastoris |  |
| doi/10.1107##s2052252519007395 | 6qf5 | 3.70 | P4_2 | Full-length hAQP2 expressed in Pichia pastoris |  |

## Expression and Purification

- **Expression system**: C-terminally truncated [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) (residues 1-242) expressed in Pichia pastoris

- **Construct**: [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) truncated at Pro242
- **Notes**: Full-length [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) produced in insect cells failed to yield well-diffracting 3D crystals. [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) at Pro242 (last visible residue in [AQP5](/xray-mp-wiki/proteins/other-ion-channels/human-aqp5/) structure) significantly improved diffraction quality.


### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression and purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | — |  | Details in SI Materials and Methods |


## Crystallization

### doi/10.1073##pnas.1321406111

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Truncated [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) (1-242) |
| Temperature | 100 K (data collection) |
| Cryoprotection | Frozen crystal |
| Notes | CdCl2 used as an additive during crystallization. Complete data collected at ESRF (Grenoble, France) from a single frozen crystal. Crystals belonged to space group P42 with one tetramer in the asymmetric unit (a=119.11 A, b=119.11 A, c=90.48 A).
 |

### doi/10.1107##s2052252519007395

| Parameter | Value |
|---|---|
| Method | On-chip crystallization by sitting-drop vapor diffusion |
| Protein sample | Full-length hAQP2 at 9 mg/ml in 20 mM Tris pH 8.0, 0.3 M NaCl, 0.2% OGNPG |
| Reservoir | 0.1 M Tris pH 8.5, 0.1 M NaCl, 0.1 M MgCl2, 22-25% [PEG](/xray-mp-wiki/reagents/additives/peg/) 400 with 0.1 M CdCl2 |
| Temperature | 298 K (room-temperature data collection) |
| Growth time | 15 min to a few hours |
| Notes | On-chip crystallization on Roadrunner II chip. 100 ul protein-precipitant mix applied to chip, equilibrated against 5-7 ml reservoir. Excess mother liquor removed by blotting. Room-temperature SFX data collected at LCLS MFX beamline using fast-scanning goniometer at 120 images/s, 50 um step size, 25-degree tilt angle. Humidified helium stream used during data collection.
 |


## Biological / Functional Insights

### C-terminal conformational variability

The C-terminal helix of [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) shows significant conformational variability
across the four protomers of the tetramer, with one protomer (D) being
highly disordered. This flexibility likely explains why full-length [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/)
failed to yield well-diffracting crystals. In protomer C, the C-terminal
helix interacts with a symmetry-related [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) molecule via leucine residues
(Leu230, 234, 237, 240), suggesting a role in protein-protein interactions
relevant to cellular sorting and LIP5-mediated trafficking.

### Cd2+ and Ca2+ binding

Two Cd2+ binding sites (Cd1 and Cd2) were identified per [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) tetramer.
Cd1 has full occupancy at the membrane interface between protomers A and D,
ligated by GluA155 and GlnD57. Cd2 has partial (65%) occupancy between loop
B and the C-terminal tail. Binding of Cd2+ influences loop D conformation
and stabilizes crystal contacts. Radioactive Ca2+ binding assays demonstrate
that AQP2-expressing oocytes bind significantly more Ca2+ than controls,
suggesting Ca2+ is the physiological ligand for these sites.

### NDI-causing mutations

The [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) structure reveals locations of mutations causing nephrogenic
diabetes insipidus (NDI). Most mutations are in transmembrane domains and
cause misfolding and ER retention. Key mutation sites include: Gln57 (Cd1
ligand), Ser148 (casein kinase II consensus site, hydrogen bonds to Gln57),
Thr125/Thr126 in loop C near the N-glycosylation site Asn123, and Asp150
in loop D which mediates interactions between loop D and the C-terminal
tail via Arg152.

### LIP5 interaction site

The LIP5 binding site on [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) has been mapped to residues 230-243 within
the C-terminal helix. Leucines 230, 234, 237, and 240 align on the same
side of the helix, creating a leucine-rich region. This is similar to the
AQP0-Calmodulin interaction motif, suggesting exposed hydrophobic residues
on [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) C-terminal helices may be a recurring motif for protein-
protein interactions involved in trafficking.


## Cross-References

- [Human Aquaporin 4 (hAQP4)](/xray-mp-wiki/proteins/other-ion-channels/human-aquaporin-4/) — Related mammalian aquaporin for structural comparison
- [Aquaporin Z (AqpZ)](/xray-mp-wiki/proteins/other-ion-channels/aquaporin-z/) — Bacterial aquaporin homolog for comparative analysis
- [Aquaporin 0 (AQP0)](/xray-mp-wiki/proteins/other-ion-channels/aqp0/) — AQP0-Calmodulin interaction provides comparative model for C-terminal helix interactions
- [On-Chip Crystallization](/xray-mp-wiki/methods/on-chip-crystallization/) — Method used to obtain the 3.7 A room-temperature SFX structure (PDB 6qf5)
- [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — Related biological concept
- [Nephrogenic Diabetes Insipidus](/xray-mp-wiki/concepts/miscellaneous/nephrogenic-diabetes-insipidus/) — Related biological concept
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) — Related protein structure
