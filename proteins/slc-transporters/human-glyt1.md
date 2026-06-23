---
title: Human Glycine Transporter 1 (GlyT1)
created: 2021-03-03
updated: 2026-06-09
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-021-03274-z]
verified: false
---

# Human Glycine Transporter 1 (GlyT1)

## Overview

Human [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) transporter 1 (GlyT1, encoded by the SLC6A9 gene) is a member of the [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/transport-mechanisms/nss-family/) (SLC6) that regulates glycine-mediated neuronal excitation and inhibition through sodium- and chloride-dependent reuptake of [Glycine](/xray-mp-wiki/reagents/buffers/glycine/). GlyT1 is located on presynaptic neurons and astrocytes surrounding both inhibitory glycinergic and excitatory glutamatergic synapses, and is the main regulator of extracellular [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) levels in the brain. Inhibition of GlyT1 prolongs neurotransmitter signaling and has been a key strategy for treating schizophrenia and cognitive impairments. The structure of GlyT1 in complex with a benzoylisoindoline inhibitor (Cmpd1) and a synthetic single-domain antibody (sybody Sb_GlyT1#7) was determined at 3.4 A resolution using serial synchrotron crystallography (Shahsavar et al., 2021, PDB 6ZBV). The inhibitor locks GlyT1 in an inward-open conformation and binds at the intracellular gate of the release pathway, overlapping with the glycine-release site. A second structure of GlyT1 with an N-terminal lichenase fusion (GlyT1-Lic) was determined at 3.9 A resolution (PDB 6ZPL).

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-021-03274-z | 6ZBV | 3.4 A | P2_1 | Human GlyT1 minimal construct with N- and C-terminal deletions (Delta1-90, Delta685-706), EL2 deletion (Delta240-256), point mutations L153A, S297A, I368A, C633A; C-terminal eGFP and decahistidine tag | Cmpd1 (benzoylisoindoline inhibitor) |
| doi/10.1038##s41586-021-03274-z | 6ZPL | 3.9 A | P2_1 | GlyT1-Lic fusion with N-terminal lichenase (residues 9-281, PDB 2CIT), C-terminal eGFP and decahistidine tag | Cmpd1 (benzoylisoindoline inhibitor) |

## Expression and Purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Transient transfection (HEK293) or baculovirus infection (Sf9) | — | FreeStyle 293 expression medium (HEK293) or Sf900-III medium (Sf9) | HEK293 cells transfected with 25 kDa linear polyethylenimine (LPEI) at a GlyT1 DNA:LPEI ratio of 1:2. Cells collected 60 h post-transfection at ~70% viability. Sf9 cells infected at 2-3x10^6 cells/ml, collected 72 h post-infection at ~80% viability. |
| Solubilization | Detergent extraction | — | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl + 1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) (lauryl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl glycol) or 1% [DMNG](/xray-mp-wiki/reagents/detergents/dmng/) (decyl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl glycol) with 0.1% cholesteryl hemisuccinate ([CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)) | Solubilization performed in the continuous presence of Cmpd1 to stabilize the inhibited conformation |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [TALON](/xray-mp-wiki/reagents/additives/talon/) or Ni-NTA resin | 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl, 0.001% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) | Purified in the presence of 100 uM Cmpd1 |


## Crystallization

### doi/10.1038##s41586-021-03274-z

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) with serial synchrotron crystallography |
| Temperature | Room temperature or 4 C |
| Notes | Microcrystals of GlyT1 in complex with sybody Sb_GlyT1#7 and Cmpd1 were grown in LCP. Oscillation patterns collected from 409 mounted loops containing microcrystals by serial synchrotron crystallography at P14 beamline (PETRA III, DESY). Merged dataset yielded 3.4 A resolution. [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using [MhsT Multi-Hydrophobic Amino Acid Transporter from Bacillus halodurans](/xray-mp-wiki/proteins/slc-transporters/mhsT/) (PDB 4US3) and human [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/) (PDB 6DZZ). |


## Biological / Functional Insights

### Unique inhibition mechanism among NSS transporters

Cmpd1 binds at a unique site among NSS-inhibitor complexes, located at the intracellular gate of the release pathway and overlapping with the glycine-release site. The inhibitor is 5.6 A further from the transporter center compared to [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/), ibogaine, and [Cocaine](/xray-mp-wiki/reagents/ligands/cocaine/) bound to [SERT](/xray-mp-wiki/proteins/slc-transporters/ssert/) and DAT. Cmpd1 locks GlyT1 in an inward-open conformation, shifting the conformational equilibrium and preventing the reuptake cycle.

### Inhibitor binding mode

The benzoylisoindoline scaffold of Cmpd1 forms a pi-stacking interaction with Tyr116 (TM1), while the phenyl ring engages in an edge-to-face stacking with Trp376 (TM6). The inhibitor is further stabilized by hydrogen bonds: backbone amines of Gly121 and Leu120 with sulfonyl oxygens, Asn386 (TM6) with the tetrahydropyran oxygen, and Thr472 (TM8) with the carbonyl oxygen. The binding mode provides a template for rational design of new GlyT1 inhibitors.

### Binding pocket plasticity and selectivity

Cmpd1 is >1000-fold selective for GlyT1 over GlyT2. Key differences: Gly373 in GlyT1 corresponds to Ser497 in GlyT2 (steric clash with the inhibitor), and Met382/Ile399 in GlyT1 correspond to Leu/Val in GlyT2 (diminished van der Waals interactions). [Molecular Docking](/xray-mp-wiki/methods/structure-determination/molecular-docking/) of bitopertin places it in the same pocket, with the benzoylpiperazine scaffold matching the benzoylisoindoline scaffold of Cmpd1. The R3 (tetrahydropyran) pocket is solvent-exposed and can accommodate diverse groups.

### Sybody stabilization

The synthetic single-domain antibody sybody Sb_GlyT1#7 binds GlyT1 with 9 nM affinity and stabilizes the inward-open inhibited conformation. The sybody increases thermal stability by 10 C and enhances apparent affinity for the radioligand [3H]Org24598 by almost twofold. The sybody also plays a central role in crystal lattice contacts, essential for successful serial crystallography data collection.


## Cross-References

- [dDAT (Drosophila Dopamine Transporter)](/xray-mp-wiki/proteins/slc-transporters/d-dat/) — Related NSS family transporter used as search model for outward-open conformation
- [GPCR-G Protein Coupling](/xray-mp-wiki/concepts/signaling-receptors/gpcr-g-protein-coupling/) — GlyT1 regulates glycine levels at NMDA receptor synapses, relevant to glutamatergic signaling
- [LMNG (Lauryl Maltose Neopentyl Glycol)](/xray-mp-wiki/reagents/detergents/lmng/) — Primary detergent for solubilization and purification
- [Cholesterol Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — Used as stabilizing additive during solubilization
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for GlyT1 structure determination
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — Used for GlyT1-Lic expression in Sf9 insect cells
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — IMAC purification using Talon/Ni-NTA resin
- [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/transport-mechanisms/nss-family/) — Related biological concept
- [Molecular Docking](/xray-mp-wiki/methods/structure-determination/molecular-docking/) — Method used in structure determination or purification
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Method used in structure determination or purification
