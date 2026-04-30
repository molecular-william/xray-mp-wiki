---
title: NtMATE2 Transporter
created: 2026-04-26
updated: 2026-04-28
type: protein
tags: [transporter, membrane-protein]
sources: [doi/10.1002##1873-3468.14136]

category: proteins
layout: default
---



# NtMATE2 (Nicotiana tabacum MATE2)

## Overview

NtMATE2 is a multidrug and toxic compound extrusion (MATE) family transporter from tobacco (*Nicotiana tabacum*). It is a vacuolar membrane-localized protein involved in the transport of nicotine, a secondary metabolic compound, from the cytosol into the vacuolar lumen. NtMATE2 is 95% identical to NtMATE1 and functions as a proton-coupled transporter.

## Structure Determination

- **PDB ID**: 7DQK
- **Resolution**: 3.5 Å
- **Method**: [xray-crystallography](/xray-mp-wiki/methods/structure-determination/xray-crystallography/), [lipidic-cubic-phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization
- **Space group**: P2₁2₁2₁
- **Phase**: [molecular-replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using CasMATE (PDB ID 5YCK)
- **Beamline**: SPring-8 BL32XU (94 crystals collected, processed with KAMO)
- **Refinement**: PHENIX.refine; COOT manual building; Rwork/Rfree = 0.265/0.313
- **Two outward-facing conformations**: Mol-A (outward-open) and Mol-B (outward-releasing)
- **Model**: Residues 18–493 (Mol-A), 15–493 (Mol-B); 7,327 protein atoms, 43 ligands, 15 solvent molecules

## Expression

- **System**: *[pichia-pastoris](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/)* SMD1168 (Invitrogen)
- **Plasmid**: pPIC9K-based, C-terminal GFP-His8 tag
- **Selection**: G418 (50→100→200 μg/mL) on YPD plates
- **Induction**: BMMY medium, 0.5% methanol every 24 h, 20°C for 72 h
- **Lysis**: M-110EH [microfluidizer](/xray-mp-wiki/methods/cell-lysis/microfluidizer/) at 22,000 p.s.i. (5 passes)
- **Harvest buffer**: 300 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 20 mM [tris-buffer](/xray-mp-wiki/reagents/buffers/tris-buffer/) pH 8.0, 10% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/)

## Solubilization Reagents

- **[ddm](/xray-mp-wiki/reagents/detergents/ddm/)** (n-dodecyl-β-D-maltopyranoside, 2% Glycon) — primary solubilization detergent from *[pichia-pastoris](/xray-mp-wiki/methods/expression-systems/pichia-pastoris/)* membrane fraction; 2 hours incubation

## Purification Strategy

1. **[talon-resin](/xray-mp-wiki/methods/purification/talon-resin/) cobalt [affinity-chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) resin** (His-tag capture)
   - Equilibration: 300 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM [hepes-buffer](/xray-mp-wiki/reagents/buffers/hepes-buffer/) pH 7.0, 5% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [lmng](/xray-mp-wiki/reagents/detergents/lmng/), 0.005% [cholesterol-hydrogen-succinate](/xray-mp-wiki/reagents/lipids/cholesterol-hydrogen-succinate/), 20 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/) pH 8.0
   - Wash buffer: 0.03% [lmng](/xray-mp-wiki/reagents/detergents/lmng/) + 0.003% [cholesterol-hydrogen-succinate](/xray-mp-wiki/reagents/lipids/cholesterol-hydrogen-succinate/) + 20-40 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/)
   - Elution buffer: 0.03% [lmng](/xray-mp-wiki/reagents/detergents/lmng/) + 0.003% [cholesterol-hydrogen-succinate](/xray-mp-wiki/reagents/lipids/cholesterol-hydrogen-succinate/) + 200 mM [imidazole](/xray-mp-wiki/reagents/additives/imidazole/)
2. **Concentration**: Amicon Ultra 100K (Merck Millipore)
3. **Size-exclusion chromatography** ([superdex-columns](/xray-mp-wiki/methods/purification/superdex-columns/) Increase 10/30 GL)
   - Buffer: 300 mM [sodium-chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/), 50 mM [hepes-buffer](/xray-mp-wiki/reagents/buffers/hepes-buffer/) pH 7.0, 1% [glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.03% [lmng](/xray-mp-wiki/reagents/detergents/lmng/), 0.003% [cholesterol-hydrogen-succinate](/xray-mp-wiki/reagents/lipids/cholesterol-hydrogen-succinate/)
4. **[tev-protease](/xray-mp-wiki/reagents/protein-tags/tev-protease/)** (S219V variant) tag cleavage at 4°C for 16 hours to remove GFP-His8 tag

## Crystallization

- **Method**: Lipidic cubic phase ([lipidic-cubic-phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/))
- **Lipid**: [monoolein](/xray-mp-wiki/methods/crystallization/monoolein/) (NU-CHEK-PREP / Sigma-Aldrich)
- **Ligand pre-incubation**: 2.5 mM [nicotine-ligand](/xray-mp-wiki/reagents/ligands/nicotine-ligand/) added to purified protein, 10 min at 4°C
- **Mixing**: Twin-syringe method for LCP reconstitution
- **Reservoir**: 0.1 M [nh4h2po4](/xray-mp-wiki/reagents/additives/nh4h2po4/), 0.1 M [hepes-buffer](/xray-mp-wiki/reagents/buffers/hepes-buffer/) pH 7.5, 2.5-7.5 mM [nicotine-ligand](/xray-mp-wiki/reagents/ligands/nicotine-ligand/)
- **Container**: Glass sandwich plates, 30 nL LCP drops
- **Resolution**: 3.5 Å, 94 crystals collected


|