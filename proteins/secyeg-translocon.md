---
title: SecYEG Translocon
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [membrane-protein, channel, protein-translocation]
sources: [doi/10.1016##j.celrep.2015.10.025]
category: proteins
---
layout: default

# SecYEG Translocon

## Overview

The SecYEG translocon is a conserved protein-conducting channel in bacterial membranes that mediates the translocation of secretory and membrane proteins across the plasma membrane. It is the functional homolog of the eukaryotic Sec61 complex. The bacterial complex is composed of three subunits: SecY (channel-forming), SecE (stabilizer), and SecG (regulator). Over 30% of newly synthesized proteins in bacteria are transported via the Sec pathway.

## Structure

### Tanaka et al. (Cell Reports 2015) — SecYEG Resting State

- **Resolution**: 2.7 Å
- **PDB ID**: 5AWW
- **Space group**: I222
- **Organism**: *Thermus thermophilus* (TtSecYEG)
- **Complex**: Full-length SecYEG (SecY + SecE + SecG)
- **Refinement**: Rwork/Rfree = 21.9%/26.8%
- **Key feature**: Resting (closed) state with plug helix sealed on periplasmic side and SecG loop covering cytoplasmic side

### Tanaka et al. (Cell Reports 2015) — SecYEG Peptide-Bound State

- **Resolution**: 3.6 Å
- **PDB ID**: 5CH4
- **Space group**: C222₁
- **Ligand**: Signal peptide (N-terminal MFARL segment from SecE or bacterial signal peptide)
- **Key feature**: Expanded cytoplasmic hydrophobic crack at lateral gate, peptide bound to cytoplasmic side of SecY

## Subunit Architecture

### SecY
- **TM helices**: TM1–TM10
- **Cytoplasmic loops**: C1–C6
- **Periplasmic loops**: P1–P5
- **Pore ring**: I77, I81, T184, I188, I275, I403 (6 residues, membrane-permeability barrier)
- **Lateral gate**: TM2, TM7, TM8 (hydrophobic crack + rift, signal peptide contact site)
- **Plug helix**: Seals periplasmic side of channel
- **Mutations**: R252G, 248KVVGGRV254→GAAG (for crystallization)

### SecE
- **TM helices**: TM1–TM2
- **Cytoplasmic region**: N-terminal MFARL sequence
- **Role**: Stabilizes SecY at the back, N-terminal hydrophobic residues can insert into SecY's hydrophobic crack

### SecG
- **TM helices**: TM1 and TM2
- **Cytoplasmic loop**: Covers the hourglass-shaped channel pore ring on cytoplasmic side
- **Contact area**: ~30% of SecG surface contacts TM3, TM4, C2, C3 of SecY
- **Key residue**: L35 (cytoplasmic loop) positioned near I272 of SecY (Cα–Cα distance confirmed by disulfide crosslinking)

## Channel Conformational States

### Resting State (5AWW)
- Plug helix seals periplasmic side
- SecG cytoplasmic loop covers pore ring (I272–L35 crosslinkable)
- Lateral gate closed
- Hourglass-shaped channel

### Peptide-Bound State (5CH4)
- Expanded cytoplasmic hydrophobic crack
- Signal peptide (MFARL) binds to lateral gate
- Periplasmic side of lateral gate unchanged
- MD simulation: crack immediately closes without peptide

### SecA-Bound State (reference: PDB 3DIN)
- SecA covers cytoplasmic surface of SecY
- Lateral gate fully open
- Plug displaced

## Expression, Purification, and Crystallization

### Tanaka et al. (Cell Reports 2015)

- **Expression**: *E. coli* BL21 (DE3), 40°C, 18 hr
- **Plasmids**: pAK24 (SecY-R252G-H6, SecE) + pAK22/pAK80 (SecG)
- **Antibiotics**: 50 μg/ml ampicillin, 20 μg/ml chloramphenicol
- **Membrane prep**: Total membrane fraction
- **Detergent solubilization**: 2% DDM (n-dodecyl-β-D-maltoside), 1 hr at 4°C
- **Buffer**: 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 5% glycerol, 0.1 mM AEBSF
- **Affinity**: Ni-NTA agarose (QIAGEN), 20 mM imidazole wash, 300 mM imidazole elution
- **SEC**: [superdex-columns](//xray-mp-wiki/methods/purification/superdex-columns/) 200 10/300 GL (GE Healthcare)
- **SEC buffer**: 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 0.1% DDM, 5% glycerol
- **Ion exchange**: HiTrap SP HP column (GE Healthcare), 0–100% gradient of 1 M NaCl
- **Desalting**: Amicon Ultra 50-kDa cutoff, concentrated to ~15 mg/mL
- **Dialysis**: 0.25% DM (n-decyl-β-D-maltoside), 5% glycerol for crystallization
- **LCP**: Mixed with monoolein at 2:3 protein-to-lipid ratio (w/w)

#### Resting State Crystallization (I222)
- Reservoir: 30–32% PEG 500 MME, 100 mM MgSO4, 100 mM Na2SO4, 50 mM MOPS pH ~7
- Temperature: 20°C
- Growth: ~10 days to full size

#### Peptide-Bound Crystallization (C222₁)
- Reservoir: 27% PEG 500 MME + additional components (truncated in source)
- Temperature: 20°C

- **Phasing**: Molecular replacement with Phaser using SecYE (PDB: 2ZJS) as search model
- **Model building**: COOT
- **Refinement**: PHENIX

## Biological Function

- **Post-translational translocation**: SecA ATPase-driven
- **Co-translational translocation**: Ribosome-nascent chain complex
- **Signal peptide recognition**: TM2, TM7, TM8 of SecY contact signal peptides
- **Proton-driven enhancement**: SecDF ATPase-independent mechanism
- **Dimerization**: Transient dimeric forms in membrane (not stable in crystal packing)

## Cross-References

- [ddm](//xray-mp-wiki/reagents/detergents/ddm/) — DDM detergent for solubilization (2% w/v)
- [dm](//xray-mp-wiki/reagents/detergents/dm/) — DM detergent for crystallization (0.25% w/v)
- [monoolein](//xray-mp-wiki/methods/crystallization/monoolein/) — LCP lipid matrix (2:3 protein:lipid ratio)
- [lipidic-cubic-phase](//xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization method
- [superdex-columns](//xray-mp-wiki/methods/purification/superdex-columns/) — Superdex 200 SEC
- [imac](//xray-mp-wiki/methods/purification/imac/) — Ni-NTA affinity chromatography
- [molecular-replacement](//xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Phaser MR (PDB: 2ZJS)
- [mops-buffer](//xray-mp-wiki/reagents/buffers/mops-buffer/) — MOPS buffer for crystallization
- [magnesium-sulfate](//xray-mp-wiki/reagents/additives/magnesium-sulfate/) — MgSO4 in crystallization
- [sodium-sulfate](//xray-mp-wiki/reagents/additives/sodium-sulfate/) — Na2SO4 in crystallization
- [peg-5000](//xray-mp-wiki/reagents/additives/peg-5000/) — PEG 500 MME precipitant
- trihexylamine — Triethylamine (implied by Tris)