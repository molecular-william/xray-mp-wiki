---
title: sTeLIC (Tevnia jerichonana Endosymbiont Pentameric Ligand-Gated Ion Channel)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1717700115]
verified: false
---

# sTeLIC (Tevnia jerichonana Endosymbiont Pentameric Ligand-Gated Ion Channel)

## Overview

sTeLIC is a prokaryotic pentameric ligand-gated ion channel (pLGIC) from a gammaproteobacterial endosymbiont of the deep-sea tube worm Tevnia jerichonana. It is a cationic channel activated at alkaline pH (pH50 of 8.6) with 28% sequence identity to [ELIC](/xray-mp-wiki/proteins/cys-loop-receptors/elic/). The X-ray crystal structure at 2.3 A reveals the most widely open pore of any pLGIC solved to date, with a minimum pore diameter of 11 A. sTeLIC is allosterically potentiated by aromatic amino acids (Phe, Trp) and 4-bromo-cinnamate, and inhibited by divalent cations (Ca2+, Zn2+, Ba2+). It is not blocked by quaternary ammonium ions ([TMA](/xray-mp-wiki/reagents/ligands/tetramethylammonium/), [TEA](/xray-mp-wiki/reagents/ligands/tetraethylammonium/), TPA).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1717700115 | Not specified in text | 2.3 | Not specified | sTeLIC wild-type at pH 8.0 |  |
| doi/10.1073##pnas.1717700115 | 6FLI | Not specified | — | sTeLIC + 4-bromo-cinnamate (4-BrC) complex | 4-BrC |
| doi/10.1073##pnas.1717700115 | 6FVR | Not specified | — | sTeLIC with Cs+ ions |  |
| doi/10.1073##pnas.1717700115 | Not specified in text | Not specified | — | sTeLIC R86A mutant |  |
| doi/10.1073##pnas.1717700115 | Not specified in text | Not specified | — | sTeLIC soaked with BaCl2 |  |

## Expression and Purification

- **Expression system**: Not specified in text (likely E. coli)
- **Construct**: Full-length sTeLIC expressed in Xenopus oocytes for electrophysiology
- **Notes**: Expressed in Xenopus oocytes and BHK cells for electrophysiology studies

### Purification Workflow

- **Expression system**: Not specified
- **Expression construct**: Full-length sTeLIC

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | Not specified | — |  | For crystallization, details not in extracted text |
| Purification | Not specified | — |  | Crystallization details not fully extracted from raw paper text |


## Crystallization

### doi/10.1073##pnas.1717700115

| Parameter | Value |
|---|---|
| Method | Not specified |
| Protein sample | Purified sTeLIC |
| Notes | [PEG](/xray-mp-wiki/reagents/additives/peg/) 200 (the precipitant) was found to occupy the allosteric potentiator site in the apo structure and may help maintain the open state. The density assigned to [PEG](/xray-mp-wiki/reagents/additives/peg/) 200 is displaced when 4-BrC binds. |


## Biological / Functional Insights

### Widely open pore conformation defines the active state

sTeLIC has the most open pore of any pLGIC structure, with a minimum diameter of 11 A at D2'. This is wider than the open state of alpha1-GlyR ([Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/), 3.9 A) and [GLIC](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) at acidic pH. Two salt bridges (D293-R225 and K224-D227) stabilize the open conformation. The pore contains negatively charged residues D-4' and D2' at the cytoplasmic end, consistent with cation selectivity.

### Two constriction rings in the extracellular domain

Two constriction rings exist in the ECD vestibule: one at K66 (alpha1 helix) and one at D88-R86 (loop Omega). Mutation of R86 or K66 to alanine produces functional channels without significantly altering pH50, showing these rings are not essential for gating. Similar constriction rings are observed in 5HT3A-R and GluCl-alpha.

### Allosteric potentiation by 4-bromo-cinnamate

4-BrC binds to five symmetrical intrasubunit sites in the ECD vestibule, at a site more deeply buried than the benzodiazepine site in [ELIC](/xray-mp-wiki/proteins/cys-loop-receptors/elic/). It potentiates pH 7.5-elicited currents with EC50 of 21 uM. Aromatic amino acids (Phe, Trp) also potentiate sTeLIC, suggesting the binding site preferentially accommodates aromatic compounds. Substitution at the para position with bromine enhances affinity.

### Inhibition by divalent cations

Divalent cations inhibit sTeLIC with IC50 values: Zn2+ (3.5 uM), Ba2+ (91 uM), Ca2+ (1.2 mM). Two Ba2+ binding sites were found in the pore (at D2' and G6'), but functional data favor an allosteric mechanism of inhibition rather than open-channel block. The slow onset of inhibition and lack of voltage dependence support an allosteric mechanism.


## Cross-References

- [ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/elic/) — sTeLIC shares 28% sequence identity with ELIC, a closed-state pLGIC; comparison reveals gating conformations
- [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/cys-loop-receptors/glic/) — sTeLIC and GLIC are prokaryotic pLGICs; sTeLIC shows a more open pore than GLIC
- [HEPES (4-(2-Hydroxyethyl)-1-piperazineethanesulfonic Acid) Buffer](/xray-mp-wiki/reagents/buffers/hepes/) — HEPES buffer used in electrophysiology recording solutions
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/buffer-tris/) — Tris buffer used in electrophysiology recordings
- [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) — Method used in structure determination or purification
- [PEG](/xray-mp-wiki/reagents/additives/peg/) — Additive used in purification or crystallization buffers
- [TEA](/xray-mp-wiki/reagents/ligands/tetraethylammonium/) — Related ligand or cofactor
- [TMA](/xray-mp-wiki/reagents/ligands/tetramethylammonium/) — Related ligand or cofactor
