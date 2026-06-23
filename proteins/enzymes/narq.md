---
title: "NarQ (E. coli Nitrate/Nitrite Sensor Histidine Kinase)"
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [membrane-protein, enzyme]
sources: [doi/10.3390##ijms21093110, doi/10.1073##pnas.2014896117, doi/10.1016##j.bpj.2017.11.3744, doi/10.1002##bies.201700197]
verified: false
---

# NarQ (E. coli Nitrate/Nitrite Sensor Histidine Kinase)

## Overview

NarQ is a transmembrane sensor histidine kinase from Escherichia coli that
detects extracellular nitrate and nitrite to regulate anaerobic respiration
via the NarQ-NarP two-component signaling system. It consists of seven domains:
a four-helical periplasmic sensor domain, transmembrane (TM) bundle, HAMP
domain, signaling helix, GAF-like domain, dimerization and histidine
phosphotransfer (DHp) domain, and catalytic kinase (CA) domain. NarQ functions
as a homodimer and phosphorylates both NarL and NarP response regulators in
the presence of nitrate or nitrite, while dephosphorylating them in the
absence of ligands.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.3390##ijms21093110 | 6YUE | 2.4 | F222 | Sensor-TM-HAMP fragment (residues 1-234) of NarQ R50S mutant | None (mutant unable to bind nitrate) |
| doi/10.1073##pnas.2014896117 | 5IJI | 2.8 | F222 | Sensor-TM-HAMP fragment (residues 1-234) of wild-type NarQ, ligand-bound | Nitrate |
| doi/10.1073##pnas.2014896117 | 5JEQ | 3.0 | C222_1 | Sensor-TM-HAMP fragment (residues 1-234) of NarQ R50K mutant, ligand-free | None |

## Expression and Purification

No purification described.

## Crystallization

### doi/10.3390##ijms21093110

| Parameter | Value |
|---|---|
| Method | In meso (lipidic cubic phase) crystallization |
| Protein sample | Sensor-TM-HAMP fragment of NarQ R50S mutant (30 mg/mL in crystallization buffer) |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Temperature | 22 °C (crystallization), 100 K (data collection) |
| Cryoprotection | 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) added to precipitant solution, 5 min incubation |
| Notes | Crystals of ~100 um grown within 1 week using NT8 robotic system (LCP version). Harvested using micromounts, flash-cooled in liquid nitrogen. Data collected at ESRF beamline ID23-1 with PILATUS 6M-F detector at 100 K. |


## Biological / Functional Insights

### Signal transduction mechanism in NarQ involves helical rotation, diagonal scissoring, and piston-like shifts

The study combined X-ray crystallography of the R50S mutant (PDB 6YUE)
with extensive MD simulations (7 trajectories, 880-1000 ns each) of
ligand-bound WT, ligand-free WT, and ligand-free R50S NarQ to elucidate
the mechanism of transmembrane signal transduction. Nitrate binding to
the sensor domain causes helical rotation of the membrane-proximal
helices H1/H1' and diagonal scissoring (H1-H1' approach, H4-H4'
separation). This disrupts the alpha-helical structure of the TM1-H1
linker, introducing a break that amplifies a subtle piston-like shift
(~1 A in the sensor domain) to ~3 A at the TM domain. The piston motion
is transmitted to the HAMP domain. Gly47 plays a key role: its backbone
alternates between alpha-helix and 3_10-helix-like hydrogen bonding,
mediating the rotation of H1 upon nitrate binding. The study shows that
helical rotation, diagonal scissoring, and piston are not mutually
exclusive mechanisms but represent different degrees of freedom in
coiled-coil proteins, all operating in NarQ.

### R50S mutant trapped in liganded conformation by crystal contacts

The R50S mutant of NarQ sensor-TM-HAMP fragment crystallized (PDB 6YUE)
in the same backbone conformation as the ligand-bound WT protein (PDB
5IJI, RMSD 0.2 A), despite the absence of nitrate. However, MD
simulations of the R50S mutant starting from the crystal structure showed
a fast transition to ligand-free-like conformations with characteristic
features: diagonal scissoring, continuous alpha-helix between TM1 and H1,
and piston-like shifts. This discrepancy arose because the crystallization
conditions and crystal contacts trapped the protein in the
ligand-bound-like conformation, highlighting the caution needed when
interpreting structures of truncated or mutated signaling proteins.

### Sensor domain conformational changes are independent of TM domain

Comparison of NarQ (with TM domain) and NarX (isolated sensor domain)
showed that the conformational changes in the sensor domain are largely
similar regardless of the presence of the TM domain. However, the TM1-H1
linker in NarQ introduces a secondary structure switch that amplifies the
piston-like shift, which could not be predicted from the isolated sensor
domain structure alone. This emphasizes the importance of studying
full-length or multi-domain fragments for understanding TM signaling.


## Cross-References

- [Two-Component Signaling System](/xray-mp-wiki/concepts/signaling-receptors/two-component-signaling-system/) — NarQ is the archetypal TCS sensor used to demonstrate the complete TM signaling mechanism including helical rotation, diagonal scissoring, and piston-like shifts
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — In meso crystallization was essential for obtaining NarQ TM domain structures
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Additive used in purification or crystallization buffers
