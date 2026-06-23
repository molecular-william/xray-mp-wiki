---
title: GPR6 — Orphan G Protein-Coupled Receptor Implicated in Parkinson's Disease
created: 2026-06-11
updated: 2026-06-11
type: protein
category: proteins
layout: default
tags: [gpcr, gpcr, membrane-protein]
sources: [doi/10.1126##scisignal.ado8741]
verified: false
---

# GPR6 — Orphan G Protein-Coupled Receptor Implicated in Parkinson's Disease

## Overview

GPR6 is an orphan class A G protein-coupled receptor belonging to the MECA cluster
(Melanocortin/EDG/Cannabinoid/Adenosine) that exhibits one of the highest levels of
constitutive activity among GPCRs. It is primarily expressed in the CNS, highly
selectively enriched in [Dopamine](/xray-mp-wiki/reagents/dopamine/) D2 receptor-expressing medium spiny neurons (MSNs)
in the striatum, and implicated in Parkinson's disease (PD). Multiple structures were
determined: a pseudo-apo state (2.1 Å, PDB 8TF5) showing a lipid-like density in the
orthosteric pocket stabilizing an active-like conformation; two inverse agonist-bound
inactive structures (GPR6-3h at 2.6 Å, PDB 8T1V; GPR6-CVN424 at 3.5 Å, PDB 8T1W);
and a cryo-EM structure of the fully active GPR6-Gs signaling complex (3.3 Å, PDB 8TYW,
EMDB EMD-41729). The GPR6-selective inverse agonist CVN424 improved motor symptoms in
PD patients in a recent phase II clinical trial (NCT04191577). The structures reveal
that constitutive activity may be driven by an endogenous lipid-like ligand rather than
intrinsic conformational preference of the protein itself.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1126##scisignal.ado8741 | 8TF5 | 2.10 | Orthorhombic | GPR6-CC pseudo-apo (no ligand added) |  |
| doi/10.1126##scisignal.ado8741 | 8T1V | 2.60 | — | GPR6-CC in complex with IAG 3h |  |
| doi/10.1126##scisignal.ado8741 | 8T1W | 3.50 | — | GPR6-CC in complex with CVN424 (clinical inverse agonist) |  |
| doi/10.1126##scisignal.ado8741 | 8TYW | 3.30 | — | Wild-type GPR6 in complex with Gs heterotrimer and [Nb35](/xray-mp-wiki/reagents/antibodies/nb35/) [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) |  |

## Expression and Purification

- **Expression system**: Sf9 insect cells (Bac-to-Bac baculovirus system); HEK293 mammalian cells for select constructs
- **Construct**: Human GPR6 (UniProt P46095) N-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) Δ1-47, ICL3 replaced with bRIL, 6 point mutations (C123L, A173P, G279R, S291C, Y320L, C345D) for crystallization
- **Notes**: For [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/), wild-type GPR6 co-expressed with dominant-negative Gαs and Gβ1γ2

### Purification Workflow

- **Expression system**: Sf9 insect cells
- **Expression construct**: GPR6-CC (crystallization construct with [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) fusion and 6 point mutations)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Hypotonic lysis and high osmotic washes (1.0 M NaCl) | — |  |  |
| Solubilization | 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + 0.2% CHS, 2.5 h at 4°C | — |  |  |
| Affinity chromatography | [Talon](/xray-mp-wiki/reagents/additives/talon/) IMAC resin, gradient [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) elution | — |  |  |
| Size-exclusion chromatography | Superdex 200 Increase 10/300 | — | 25 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.5, 150 mM NaCl, 0.02% DDM, 0.004% CHS, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |  |


## Crystallization

### doi/10.1126##scisignal.ado8741

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | GPR6-CC at 30-40 mg/mL in complex with IAG ligands or apo |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Temperature | 20 |
| Growth time | 2-7 days |
| Cryoprotection | Flash frozen in liquid nitrogen |
| Notes | LCP mix: 40% receptor solution, 54% [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/), 6% [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/). Crystals harvested using 100 µm dual thickness micromounts. Data collected at APS GM/CA beamline at 1.0332 Å wavelength. |


## Biological / Functional Insights

### High constitutive activity driven by endogenous lipid

The pseudo-apo GPR6 structure shows a lipid-like density in the orthosteric
pocket stabilizing an active-like conformation. Extensive experiments including
native mass spectrometry, lipidomics, MD simulations, and docking suggest the
ligand may be a single-chain lipid (tentatively OLA). Markov State Model
simulations of the apo receptor show 83% preference for the inactive state,
suggesting constitutive activity is driven by the bound lipid rather than
intrinsic protein dynamics.

### Phe152 as a conformational switch

Phe152(3.36) acts as a key molecular switch between inactive and active
states. Inverse agonists lock Phe152 in its inactive conformation where it
π-stacks with Trp292(6.48) and Phe234(5.47). The lipid agonist stabilizes
the active conformation of Phe152, releasing TM5 and TM6 for activation
motions. In the absence of ligands, Phe152 oscillates between both
conformations.

### CVN424 clinical inverse agonist

CVN424 is a potent and selective GPR6 inverse agonist that completed a
phase II clinical trial (NCT04191577) showing improvement of motor symptoms
in PD patients. The co-crystal structure reveals CVN424 binds in the
orthosteric pocket with a single hydrogen bond to Thr319(7.43) and
hydrophobic/π-stacking interactions with residues including His128(2.60),
Phe152(3.36), Phe295(6.51), and Leu315(7.39). GPR6 inhibition represents a
non-dopaminergic therapeutic strategy for PD treatment.

### Lipid entry pathway from membrane

The active-like pseudo-apo structure reveals a continuous channel from the
orthosteric pocket to the lipid bilayer through an opening framed by TM3-TM5.
This opening is gated by Phe152(3.36) and allows lipid agonists to enter
directly from the membrane. This transmembrane entry is closed in most other
MECA cluster receptors but open in the active-like GPR6 conformation,
suggesting a unique access mechanism.

### G protein coupling interface

The [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of the GPR6-Gs complex shows a canonical GPCR-Gs
interface. TM6 undergoes 8.2 Å outward movement from the inactive state.
The α5 helix of Gαs inserts into the cytoplasmic cavity, with Arg166(3.50)
forming a π-cation interaction with Tyr391 of Gαs. Additional interactions
involve Arg332(7.56) and Thr280(6.36) with Gαs residues, and ICL1/ICL2
interactions with Gβ and the αN helix of Gαs.


## Cross-References

- [Dopamine](/xray-mp-wiki/reagents/dopamine/) — Referenced in gpr6 text
- [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Referenced in gpr6 text
- [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Referenced in gpr6 text
- [Bril](/xray-mp-wiki/reagents/protein-tags/bril/) — Referenced in gpr6 text
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in gpr6 text
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in gpr6 text
- [Talon](/xray-mp-wiki/reagents/additives/talon/) — Referenced in gpr6 text
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in gpr6 text
- [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) — Referenced in gpr6 text
- [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) — Referenced in gpr6 text
