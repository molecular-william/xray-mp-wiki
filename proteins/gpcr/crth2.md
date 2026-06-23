---
title: "Human CRTH2 (PGD2 Receptor)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.molcel.2018.08.009, doi/10.1073##pnas.2102813118]
verified: false
---

# Human CRTH2 (PGD2 Receptor)

## Overview

CRTH2 (chemoattractant receptor-homologous molecule expressed on Th2 cells, also known as DP2) is a G-protein-coupled receptor (GPCR) for prostaglandin D2 (PGD2). It mediates type 2 inflammation and is a major drug target for asthma and other inflammatory disorders. CRTH2 is the only member of the prostanoid receptor family that is phylogenetically distant from other prostanoid receptors. This paper reports the crystal structure of human CRTH2 bound to the PGD2 derivative [15R Methyl Pgd2](/xray-mp-wiki/reagents/ligands/15r-methyl-pgd2/) (15mPGD2) by serial femtosecond crystallography (SFX) at 2.6-3.2 A resolution, revealing a "polar group in" binding mode that contrasts with the "polar group out" mode of PGE2 in EP3. Previous structures reported CRTH2 bound to antagonists fevipiprant (2.80 A) and CAY10471 (2.74 A).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.molcel.2018.08.009 | 6D26 | 2.80 | P212121 | Human CRTH2 with mT4L insertion in ICL3, N25A mutation, C-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) (R340-S395 removed), N-terminal 8-amino acid linker | Fevipiprant (QAW039) |
| doi/10.1016##j.molcel.2018.08.009 | 6D27 | 2.74 | P212121 | Human CRTH2 with mT4L insertion in ICL3, N25A mutation, C-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) (R340-S395 removed), N-terminal 8-amino acid linker | CAY10471 |
| doi/10.1073##pnas.2102813118 | 7M8W | 2.60 | P212121 | Human CRTH2 with mT4L insertion in ICL3, N25A mutation, C-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) at R340 | [15R Methyl Pgd2](/xray-mp-wiki/reagents/ligands/15r-methyl-pgd2/) (15mPGD2) |

## Expression and Purification

- **Expression system**: Spodoptera frugiperda (Sf9)
- **Construct**: Human CRTH2 (UniProt Q9Y5Y4) with N-terminal FLAG tag, mT4L insertion in ICL3 (between R237 and I238), N25A mutation, C-terminal [Truncation](/xray-mp-wiki/concepts/methods-techniques/truncation/) at R340. Expressed using Bac-to-Bac baculovirus system in Sf9 insect cells.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Baculovirus infection | -- | -- + -- | Sf9 cells infected with baculovirus, harvested 48 h post-infection |
| Membrane preparation | Centrifugation and homogenization | -- | 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) (pH 7.5), 10 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 20 mM KCl, protease inhibitors + -- | Cells lysed by repeated homogenization and centrifugation |
| Solubilization | Detergent solubilization | -- | 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) (pH 7.5), 500 mM NaCl, 10 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 20 mM KCl, 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) | Membranes solubilized in 1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) + 0.2% CHS; supernatant after 1 h binding with ligand |
| Affinity purification | Anti-FLAG M1 affinity chromatography | Anti-FLAG M1 resin | 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) (pH 7.5), 500 mM NaCl, 10 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 20 mM KCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) + 0.002% CHS | Bound in 2 mM CaCl2; eluted with 5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) + 200 ug/ml FLAG peptide |
| Size-exclusion chromatography | SEC | Superdex 200 | 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) (pH 7.5), 150 mM NaCl, 10 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 20 mM KCl + 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) + 0.002% CHS | Final purification after concentrating eluted protein. Final sample buffer for crystallization. |


## Crystallization

### doi/10.1016##j.molcel.2018.08.009

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Purified CRTH2-mT4L in 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.002% CHS, 20 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) (pH 7.5), 150 mM NaCl, 10 mM [Mgcl2](/xray-mp-wiki/reagents/additives/magnesium-chloride/), 20 mM KCl |
| Reservoir | 25% (w/v) [Peg](/xray-mp-wiki/reagents/additives/peg/) 3350, 0.1 M bis-tris propane (pH 6.5-7.0), 0.15 M Na-succinate, and 5% (v/v) [Peg](/xray-mp-wiki/reagents/additives/peg/) 200 |
| Temperature | 20 |
| Growth time | -- |
| Cryoprotection | Reservoir solution supplemented with 25% (v/v) [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Notes | Crystals diffracted to 2.74-2.80 A. Structures solved by molecular replacement using C5aR (6C1R) and T4L from ETBR (5XPR). Data collected at APS GM/CA beamline. Two PDB depositions: 6D26 (fevipiprant-bound) and 6D27 (CAY10471-bound). |


## Biological / Functional Insights

### Novel N-terminal lid domain covers the ligand-binding pocket

CRTH2 has a well-structured N-terminal region with an N-helix and N-loop that packs tightly against ECL2, covering the ligand-binding pocket. A disulfide bond (C26-C188) connects the N terminus to TM5. This structure creates a semi-occluded pocket with a single open end as a ligand entry port between TM1 and TM7, which is different from other lipid GPCRs ([S1P1](/xray-mp-wiki/proteins/gpcr/s1p1/), [LPA1](/xray-mp-wiki/proteins/gpcr/lpa1/), CB1) where the N-terminal region adopts different conformations.

### Conserved and divergent antagonist binding modes

Both fevipiprant and CAY10471 occupy a similar semi-occluded pocket with conserved polar interactions at the distal end (R170, Y184, K210, Y262) anchoring the carboxylate head group. The central aromatic groups engage in extensive aromatic and hydrophobic interactions with F87, F111, F112, F294, F90, H107, Y183, Y184, Y262, and L286. However, the tail groups show distinct binding modes: fevipiprant's methylsulfonyl phenyl group extends toward ECL2, while CAY10471's fluorophenyl group extends toward TM7, causing W283 and L20 side chain rearrangements.

### Charge attraction-guided binding mechanism for PGD2

A novel multi-step binding mechanism is proposed for PGD2. The carboxylate group of PGD2 first binds to the ligand entry port through interactions with positively charged residues (H95, R175, R179), then follows a positive charge gradient extending deeply into the ligand-binding pocket to reach a highly polar distal end (R170, Y184, K210, Y262, E269). This mechanism differs significantly from [S1P1](/xray-mp-wiki/proteins/gpcr/s1p1/), [LPA1](/xray-mp-wiki/proteins/gpcr/lpa1/), and CB1 where acyl chains enter the binding pocket without orientation change.

### Polar group in lipid-binding mode of CRTH2

The crystal structure of CRTH2 bound to 15mPGD2 (PDB 7M8W) reveals a "polar group in" binding mode where the carboxyl head group of 15mPGD2 is buried deep inside the binding pocket, while the omega-chain points toward the extracellular side. This contrasts with the "polar group out" mode observed in EP3-PGE2, where the carboxyl group is positioned near the extracellular surface and the omega-chain extends deep into the pocket. These two modes are associated with distinct charge distributions in the binding pockets.

### Cationic tetrad captures lipid ligands from the bilayer

MD simulations identified a cationic tetrad (R284, R175, R179, H95) at the ligand entry port of CRTH2 that functions like fishhooks to capture anionic lipid ligands from the lipid bilayer. D32 further funnels ligands toward the entry port. Mutagenesis confirmed these residues are critical for PGD2 binding - mutations at any of these positions abolished detectable specific binding, except R284A which reduced affinity 5-fold.

### Distinct PGD2 activation mechanism compared to PGE2 receptors

Unlike EP3 where PGE2 directly contacts W6.48 (the toggle switch), 15mPGD2 binds superficially without directly contacting the F6.44xxCW6.48 motif. Instead, the carboxyl group forms a hydrogen bond with Y262(6.51), and the omega-chain contacts F111(3.32), both packing against W259(6.48). This implies a distinct activation mechanism involving Y262, F111, and W259.


## Cross-References

- [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) — Primary solubilization and purification detergent (1% for solubilization, 0.01% for SEC)
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) — 0.2% CHS added to LMNG for stabilization
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — 20 mM HEPES (pH 7.5) used in purification and crystallization buffers
- [Polyethylene Glycol (PEG)](/xray-mp-wiki/reagents/additives/peg/) — 25% PEG 3350 as crystallization precipitant
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) — CRTH2 expressed in Sf9 insect cells using Bac-to-Bac system
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Anti-FLAG M1 affinity purification
- [Hanging-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/) — Crystallization method for CRTH2 antagonist structures
- [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP used for crystallization in the SFX structure (PDB 7M8W)
- [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — SFX used to collect diffraction data from CRTH2 microcrystals at LCLS XFEL
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) — MD simulations used to study lipid recognition and capture by CRTH2
