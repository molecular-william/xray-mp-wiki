---
title: Cannabinoid Receptor CB2
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [gpcr, membrane-protein]
sources: [doi/10.1016##j.cell.2020.01.008]
category: proteins
---
layout: default

# Cannabinoid Receptor CB2

## Overview

CB2 (Cannabinoid Receptor 2) is a Class A GPCR primarily expressed in the immune system and peripheral tissues. Like CB1, it is a target of cannabinoids but does not mediate psychoactive effects. CB2 couples selectively to G(i) proteins and shares 44% total sequence identity (68% in transmembrane regions) with CB1. CB2 is a therapeutic target for inflammatory and neuropathic pain without CB1-mediated psychoactivity.

## Structure

### Hua et al. (Cell 2020) — CB2-AM12033-Gi-scFv16 Complex (Cryo-EM, Active State)

- **Resolution**: 2.9 Å
- **PDB ID**: 6KPF
- **Architecture**: 7 transmembrane helices (TM1–TM7) with short N-terminal helix
- **Ligand**: AM12033 (synthetic cannabinoid agonist, Ki = 0.37 nM for CB2)
- **G protein**: Heterotrimeric G(i) (G(alpha)i1, G(beta)1, G(gamma)2) — nucleotide-free
- **Stabilizer**: scFv16 antibody fragment at G(alpha)i/G(beta) interface
- **N-terminal fusion**: [bril-fusion](//xray-mp-wiki/concepts/bril-fusion/) (BRIL protein) inserted at CB2 N terminus to improve expression
- **Expression**: Sf9 insect cells via Bac-to-Bac Baculovirus Expression System (co-expression of CB2, G(alpha)i1, G(beta)1gamma2 at 1:2:2 ratio)

### Hua et al. (Cell 2020) — CB2-AM12033 Crystal Structure (Agonist-Bound)

- **Resolution**: 3.2 Å
- **PDB ID**: 6KPC
- **Architecture**: 7TM with AM12033 agonist bound in orthosteric pocket
- **State**: Active-like (but more converged intracellular region than Gi-coupled state)
- **Cryo-EM vs crystal**: AM12033 binding pose nearly identical in both structures

### Hua et al. (Cell 2020) — CB2-AM10257 (Antagonist-Bound, Inactive State)

- **PDB ID**: 5ZTY
- **Architecture**: 7TM with antagonist AM10257 bound
- **Used as**: Search model for molecular replacement of active CB2 structures

## Activation Mechanism

### Single Toggle Switch

CB2 activation differs fundamentally from CB1:

- **Single "toggle switch"**: Only Trp6.48 undergoes major conformational change
- **TM6 movement**: Large outward movement of intracellular part of TM6 by 11 Å (Arg238 reference) to accommodate G(alpha)i alpha 5 helix
- **TM5 extension**: Cytoplasmic portion of TM5 extended and moved outward by ~6 Å (Val220 reference)
- **Minor extracellular changes**: Extracellular region, including N terminus, undergoes very minor changes during activation
- **Balloon-like plasticity**: CB2 shows far less conformational plasticity than CB1

### Activation Motifs

- **DRY motif**: D213(3.49)–R214(3.50)–Y215(3.51) rearranges upon activation
- **NPxxY motif**: N347(7.49)–P348(7.50)–xx–Y351(7.53) rearranges
- **Tyr7.53**: Establishes contacts with Thr3.46, Leu3.43, and Arg3.50 upon activation
- **Asp6.30 (TM6)**: Interrupts salt-bridge with Arg3.50, unlocking TM6 outward movement
- **Thr3.46**: Atypical polar residue (vs non-polar I/L/M/V in 95% of Class A GPCRs); T3.46A mutation disables G(i) coupling

### G Protein Interface

- **Primary contacts**: TM3, TM5, TM6 of receptor and alpha 5 helix, alpha N helix, alpha N-beta 1 loop of G(alpha)i
- **Hydrophobic pocket**: Formed by Val212(5.61), Leu243(6.33), Leu247(6.37), Leu239(6.29), Leu135(3.54) from cytosolic TM ends
- **G(i) rotation**: ~20° anticlockwise rotation compared to mu-OR-Gi, A1-AR-Gi, 5HT1B-Gi, M2-Gi complexes
- **ICL1 constraints**: Ser69 and Tyr70 in ICL1 form polar interactions with Asp305 in G(alpha)i
- **ICL2**: Pro139 in CB2 (vs Leu222 in CB1) — contributes to G(i)-selective coupling

## Cholesterol Interaction

- **Not observed**: Cholesterol NOT seen in any CB2 structure (active or inactive)
- **Key difference from CB1**: Phe4.46 is unique to CB1 among Class A GPCRs; cholesterol-binding residues not conserved in CB2

## Ligand Binding

### AM12033 (Agonist, Ki = 0.37 nM)

- **Conformation**: L-shape in orthosteric binding pocket
- **Interactions**: Tricyclic tetrahydrocannabinol system forms pi-pi interactions with Phe183(ECL2), Phe281(7.35), Phe94(2.64)
- **H-bond**: Phenolic hydroxyl at C1 forms H-bond with Ser285(7.39)
- **Alkyl chain**: Extends into long channel, hydrophobic interactions with TM3, TM5, TM6 residues

### AM10257 (Antagonist)

- Binding pocket similar to agonist-bound but more compact
- Inward movements of extracellular TM1, TM4, TM7 produce tighter pocket in agonist state

### HU-308 (CB2-Selective Agonist)

- **Selectivity**: Ki = 22.7 nM for CB2 vs almost no measurable Ki for CB1 (~5,000-fold selective)
- **MD simulation**: Stable in CB2 (low RMSD), unstable in CB1 (high RMSD)
- **Entry path**: MetaMD simulations show distinct ligand entry paths into CB1 vs CB2

### L-759,656 (CB2-Selective Agonist)

- **Selectivity**: Ki = 11.8 nM for CB2 vs 4.8 μM for CB1 (>400-fold selective)
- **MD simulation**: Similar binding behavior to HU-308 — stable in CB2, unstable in CB1

## Solubilization, Purification, and Crystallization

### Hua et al. (Cell 2020) — Cryo-EM (CB2-Gi Complex)

- **Expression**: Sf9 insect cells, Bac-to-Bac Baculovirus Expression System
- **Construct**: Wild-type human CB2 with BRIL fusion at N terminus, HA signal sequence, 10xHis tag, Flag tag — cloned into modified pFastBac1
- **G protein co-expression**: G(alpha)i1 in pFastBac1, G(beta)1gamma2 in pFastDual; infected at 2-2.5 x 10^6 cells/mL, ratio 1:2:2
- **Cell harvest**: 48 h post-infection at 27°C, pellets stored at -80°C
- **Detergent**: [lmng](//xray-mp-wiki/reagents/detergents/lmng/) (Lauryl Maltose Neopentyl Glycol, Anatrace Cat#4216588) for membrane solubilization
- **Lipid**: [cholesterol-hydrogen-succinate](//xray-mp-wiki/reagents/lipids/cholesterol-hydrogen-succinate/) (CHS, Sigma Cat#C6512) for stability
- **Reductant**: tcep (TCEP, Thermo Fisher Cat#77720)
- **EDTA**: Ethylenediamine Tetraacetic Acid (Fisher Cat#S311-500)

### Hua et al. (Cell 2020) — X-ray Crystallography (CB2-AM12033)

- **Crystallization method**: [lipidic-cubic-phase](//xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (LCP)
- **Lipid matrix**: 1-Oleoyl-rac-glycerol (monoolein, Sigma Cat#M7765)
- **Protein concentration**: Mixed 1:1 with monoolein using LCP injector (Stoelting)
- **Crystallization setup**: 96-well glass sandwich plates; reservoir containing precipitant solution
- **Crystal growth**: 4°C for 2.5-3 h; crystals reached 40 mm x 20 mm after 2 weeks
- **Harvesting**: Micro-mounts (MiTeGen), flash frozen in liquid nitrogen
- **Data collection**: Spring-8 beamline 41XU, Pilatus3 6M detector, X-ray wavelength 1.0000 Å
- **Processing**: XDS for indexing/integration/scaling; XPREP for merging
- **Phasing**: Molecular replacement with Phaser using 5ZTY (antagonist CB2) as search model
- **Refinement**: COOT for manual modeling; Phenix and Buster for refinement

### Purification Buffers

- **IMAC wash I**: 25 mM HEPES pH 7.5, 100 mM NaCl, 10% glycerol, 0.1% LMNG, 0.02% CHS, 30 mM imidazole, 20 μM AM841
- **IMAC wash II**: 25 mM HEPES pH 7.5, 100 mM NaCl, 10% glycerol, 0.03% LMNG, 0.006% CHS, 50 mM imidazole, 20 μM AM841
- **IMAC elution**: 25 mM HEPES pH 7.5, 100 mM NaCl, 10% glycerol, 0.01% LMNG, 0.001% CHS, 250 mM imidazole, 20 μM AM841
- **Resin**: [imac](//xray-mp-wiki/methods/purification/imac/) TALON IMAC resin (Clontech Cat#635507)
- **Desalting**: PD MiniTrap G-25 column (GE Healthcare)

## Cross-References

- [cb1-receptor](//xray-mp-wiki/proteins/cb1-receptor/) — Cannabinoid Receptor 1 (44% sequence identity, distinct activation mechanism)
- [bril-fusion](//xray-mp-wiki/concepts/bril-fusion/) — BRIL N-terminal fusion for CB2 expression enhancement
- [scfv16](//xray-mp-wiki/reagents/antibodies/scfv16/) — scFv16 antibody fragment for CB2-Gi complex stabilization
- [lmng](//xray-mp-wiki/reagents/detergents/lmng/) — Detergent for CB2 solubilization
- [cholesterol-hydrogen-succinate](//xray-mp-wiki/reagents/lipids/cholesterol-hydrogen-succinate/) — CHS for membrane protein stability
- [monoolein](//xray-mp-wiki/methods/crystallization/monoolein/) — Monoolein lipid matrix for LCP crystallization
- [gdn](//xray-mp-wiki/reagents/detergents/gdn/) — Glycol-diosgenin used in CB1 cryo-EM buffer
- [cryoem](//xray-mp-wiki/methods/structure-determination/cryoem/) — Cryo-EM structure determination (2.9 Å for CB2-Gi-scFv16)
- [xray-crystallography](//xray-mp-wiki/methods/structure-determination/xray-crystallography/) — X-ray crystallography (3.2 Å for CB2-AM12033)
- [lipidic-cubic-phase](//xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization method
- [imac](//xray-mp-wiki/methods/purification/imac/) — TALON IMAC affinity resin for purification
- [size-exclusion-chromatography](//xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — SEC for complex purification
- [sf9-cells](//xray-mp-wiki/methods/expression-systems/sf9-cells/) — Sf9 insect cells for CB2-Gi co-expression
- [am12033](//xray-mp-wiki/reagents/ligands/am12033/) — CB2-selective synthetic cannabinoid agonist
- [am841](//xray-mp-wiki/reagents/ligands/am841/) — THC-like cannabinoid agonist (used for CB1 studies)
- [hu-308](//xray-mp-wiki/reagents/ligands/hu-308/) — CB2-selective agonist (Ki = 22.7 nM CB2)
- [l-759-656](//xray-mp-wiki/reagents/ligands/l-759-656/) — CB2-selective agonist (406x selective over CB1)