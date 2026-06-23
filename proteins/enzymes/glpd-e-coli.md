---
title: E. coli Glycerol-3-Phosphate Dehydrogenase (GlpD)
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0712331105]
verified: false
---

# E. coli Glycerol-3-Phosphate Dehydrogenase (GlpD)

## Overview

E. coli glycerol-3-phosphate dehydrogenase (GlpD) is an essential monotopic membrane enzyme that catalyzes the oxidation of sn-glycerol-3-phosphate (G3P) to dihydroxyacetone phosphate (DHAP), with concurrent reduction of FAD to FADH2, and passes electrons on to ubiquinone in the respiratory electron transport chain. It functions at the central junction of respiration, glycolysis, and phospholipid biosynthesis, localized to the cytoplasmic membrane where it may constitute up to 10% of inner membrane proteins in constitutive strains. The enzyme comprises two major domains: an N-terminal FAD-binding domain (residues 1-388) containing the substrate-binding and membrane-embedded base regions, and a soluble C-terminal cap domain (residues 389-501). The dimeric enzyme is formed by monomers related by a noncrystallographic 2-fold axis. Seven crystal structures of the fully active enzyme were determined up to 1.75 A resolution, including complexes with substrate analogues (PEP, 2-PGA, GAP), product (DHAP), and ubiquinone analogues (menadione, HQNO), revealing conformational states, the catalytic mechanism, and the ubiquinone-binding site.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0712331105 | Not specified in raw paper text | 1.75 | I222 | Full-length E. coli GlpD (selenomethionine-labeled) | FAD (cofactor); beta-OG detergent molecules; native enzyme |
| doi/10.1073##pnas.0712331105 | Not specified in raw paper text | 2.1 | I222 | Full-length E. coli GlpD | FAD; DHAP (dihydroxyacetone phosphate, product) |
| doi/10.1073##pnas.0712331105 | Not specified in raw paper text | 2.1 | I222 | Full-length E. coli GlpD | FAD; PEP (phosphoenolpyruvate, substrate analogue) |
| doi/10.1073##pnas.0712331105 | Not specified in raw paper text | 2.3 | I222 | Full-length E. coli GlpD | FAD; 2-PGA (glyceric acid 2-phosphate, substrate analogue) |
| doi/10.1073##pnas.0712331105 | Not specified in raw paper text | 2.9 | I222 | Full-length E. coli GlpD | FAD; GAP (glyceraldehyde-3-phosphate, substrate analogue) |
| doi/10.1073##pnas.0712331105 | Not specified in raw paper text | 2.6 | I222 | Full-length E. coli GlpD | FAD; Menadione (MD, ubiquinone analogue) |
| doi/10.1073##pnas.0712331105 | Not specified in raw paper text | 2.9 | I222 | Full-length E. coli GlpD | FAD; HQNO (2-n-heptyl-4-hydroxyquinoline N-oxide, ubiquinone analogue) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Full-length E. coli GlpD; selenomethionine-labeled for MAD phasing

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Solubilization and purification | Detergent solubilization and protein purification (details in SI) | -- | Crystallization solution with PEG 6000 + [beta-OG (n-octyl-beta-D-glucopyranoside)](/xray-mp-wiki/reagents/detergents/og/) | Five beta-OG detergent molecules found interacting with GlpD dimer. Activity measured in 1% beta-OG. Enzyme can be functionally reconstituted with E. coli membrane vesicles. |


## Crystallization

### doi/10.1073##pnas.0712331105

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified GlpD, DHAP-bound complex crystals |
| Reservoir | Crystallization solution supplemented with 4% extra PEG 6000 |
| Temperature | 4 |
| Growth time | Crystals soaked for 42 h (MD) and 78 h (HQNO) |
| Cryoprotection | 30% ethylene glycol (final concentration); crystals looped and flash-cooled in liquid nitrogen |
| Notes | Soaking experiments: GlpD-DHAP crystals transferred to sitting drops containing 4 uL crystallization solution with 4% extra PEG 6000 and either MD or HQNO at 2.5 mM at 4 C. GAP soaking: similar protocol with 5 mM GAP. Crystals screened after 24 h. Native enzyme crystallized in space group I222 with ~55% solvent content and two molecules per asymmetric unit. |


## Biological / Functional Insights

### First structure of a monotypic membrane G3P dehydrogenase enzyme class

The crystal structures of GlpD represent the first structural determination of the monotypic membrane enzyme class of G3P dehydrogenases. The N-terminal FAD-binding domain shows structural similarity to other flavoprotein oxidases (Z-score 34.5 with glycine oxidase), while the C-terminal cap domain represents an unusual fold with no significant structural homologs (highest Z-score 5.3, 5% sequence identity to a hypothetical protein). The cap domain exhibits an overall negative electrostatic surface, while the base of the FAD-domain has positive electrostatic potential that interacts with negatively charged phospholipid head groups.

### Direct hydride transfer mechanism with Arg-317 as catalytic base

Arg-317 is positioned in proximity to the C2 hydroxyl group of GAP (glyceraldehyde-3-phosphate) and is proposed to act as a general base to initiate dehydrogenation of G3P. Arg-317 first deprotonates the O2 hydroxyl of G3P, followed by hydride transfer from C2 of G3P to N5 of FAD, resulting in the dihydroflavin anion state. The C2 of GAP is 4.2 A from N5 of FAD, suggesting G3P binding induces a ~1 A conformational shift for optimal transition state geometry. The reduced flavin is stabilized by Lys-354 positioned 3.7 A from N1, with additional stabilization from the backbone nitrogen of Leu-355. His-233 is a viable alternative candidate but is less likely as its distance to O2 is 4.7 A and its conformation remains invariant across all structures.

### Ubiquinone-binding site identified as hydrophobic plateau

Structures of GlpD complexed with ubiquinone analogues menadione (MD, 2.6 A) and HQNO (2.9 A) identified a hydrophobic plateau on the enzyme surface as the likely ubiquinone (UQ) docking site. The MD/HQNO location places UQ in proximity to the active site to accept electrons generated from G3P oxidation. The closest atomic distance from MD to FAD is 11.6 A (C7 of MD to C7 of FAD); the distance from C7 of MD to N5 of FAD is 15 A. No additional cofactors or metal clusters appear to be required for GlpD activity or electron transfer from FADH2 to UQ.

### Membrane interaction regions defined by electrostatic polarity

Electrostatic surface calculations show distinct regions of highly positive patches at the base region of the enzyme, likely involved with negatively charged membrane phospholipid head groups. The cap domain exhibits highly negative electrostatic potential, with large hydrophobic patches between these two distal regions forming membrane interaction and UQ-binding surfaces. Based on the distribution of polar and hydrophobic residues and the location of bound beta-OG detergent molecules at the base, GlpD is estimated to embed approximately 12-15 A into the lipid bilayer. The enzyme exhibits preference for certain amphiphiles and requires exogenous phospholipids or nondenaturing detergents for electron-transfer activity.


## Cross-References

- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Beta-OG is the detergent used for solubilization and crystallization of GlpD; five molecules found per dimer
- [Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) — 30% ethylene glycol used as cryoprotectant for flash-freezing GlpD crystals
- [PEG 6000](/xray-mp-wiki/reagents/additives/peg-6000/) — PEG 6000 used as crystallization precipitant in sitting-drop vapor diffusion
- [Glycerol Facilitator (GlpF)](/xray-mp-wiki/proteins/other-ion-channels/glycerol-facilitator/) — GlpF is a membrane protein member of the glycerol metabolic pathway that facilitates glycerol transport upstream of GlpD
- [Multi-Wavelength Anomalous Diffraction (MAD)](/xray-mp-wiki/methods/structure-determination/multi-wavelength-anomalous-diffraction/) — Three-wavelength MAD dataset used for phasing selenomethionine-labeled GlpD at SER-CAT beamline ID-22
